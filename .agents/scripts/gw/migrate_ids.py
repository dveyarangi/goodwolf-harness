"""The question store's one-time migration from ids that say where a question sits to ids that never
change (docs/architecture.md: "Question store").

Every entry with a dotted id, live or in `done/`, is moved to
`docs/questions/<new id>-<its words>.md` by the mover, which re-points every citation and rebases each moved entry's own links; its title takes the
new id and its header an `opened`, siblings keeping today's order; then every id written in the
records, the rows and the straw dogs' bindings is rewritten through the table of former ids, which
is written last. Run once in each of the person's trees; run again, it gives each question the id
the table already holds, and on a store with no dotted id it changes nothing.

    uv run --offline --no-project python .agents/scripts/gw/migrate_ids.py [--dry-run] [--leave <folder>]...
    uv run --offline --no-project python .agents/scripts/gw/migrate_ids.py --words [--dry-run] [--leave <folder>]...

`--words` is for a tree migrated while a file was named by its id alone: it gives each such entry
the name the writer gives one now, its id and its words, and repairs what cites it.

`--leave` names a folder of evidence whose files must keep agreeing with one another, whatever
their extension, so no id in it is rewritten; a tree names its own.
"""

# TODO q-2jheaw: this script leaves once every tree of the person's has run it.

from __future__ import annotations

import posixpath
import re
import shutil
import subprocess
import sys
from collections.abc import Callable
from dataclasses import dataclass, field, replace
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import move_doc  # noqa: E402  (path set above)
import questions  # noqa: E402
import sessions  # noqa: E402
from docs_corpus import citations, cited_record, corpus, target_of, with_question_bindings_retargeted  # noqa: E402

_USAGE = "usage: migrate_ids.py [--words] [--dry-run] [--leave <folder>]..."
_DOTTED = re.compile(r"^q-\d{4,}(?:\.\d{4})*$")
# A path written whole, outside a link the mover repairs: `q-0037.0017-the-words.md`.
_DOTTED_PATH = re.compile(r"(?<![\w.])(q-\d{4,}(?:\.\d{4})*)-[A-Za-z0-9][A-Za-z0-9-]*\.md")
# A file named by its id alone, written whole outside a link: `q-7f3k2a.md`.
_BARE_NAME = re.compile(r"(?<![\w.-])(q-[a-z2-7]{6})\.md")


@dataclass
class Migrated:
    """What a run did: the table it holds now, the entries it moved, the files it rewrote, the
    mentions the mover could not repair and the citations that resolve to nothing after it."""

    table: dict[str, str]
    moved: list[tuple[str, str]] = field(default_factory=list)
    rewritten: list[str] = field(default_factory=list)
    unrepaired: list[str] = field(default_factory=list)
    broken: list[str] = field(default_factory=list)


class Refused(Exception):
    """The run must not happen as asked; nothing was written."""


def main(argv: list[str], root: Path) -> int:
    dry_run = "--dry-run" in argv
    words = "--words" in argv
    rest = [said for said in argv if said not in ("--dry-run", "--words")]
    if len(rest) % 2 or any(said != "--leave" for said in rest[::2]):
        print(_USAGE)
        return 2
    left_alone = tuple(f"{folder.rstrip('/')}/" for folder in rest[1::2])
    try:
        if words:
            migrated = name_by_words(root, dry_run=dry_run, left_alone=left_alone)
        else:
            migrated = migrate(root, datetime.now(timezone.utc), dry_run=dry_run, left_alone=left_alone)
    except Refused as why:
        print(f"refused: {why}")
        return 2
    if migrated is None:
        print("no entry named by its id alone; nothing to rename" if words else "no dotted id; nothing to migrate")
        return 0
    _report(migrated, dry_run)
    return 1 if migrated.broken else 0


def migrate(
    root: Path,
    now: datetime,
    dry_run: bool = False,
    first_added: Callable[[Path, str], datetime | None] | None = None,
    unsettled: Callable[[Path, list[str]], list[str]] | None = None,
    left_alone: tuple[str, ...] = (),
) -> Migrated | None:
    """The migration as the docstring says it; `None` when no entry holds a dotted id. A dry run
    draws the table and names what would change, and writes nothing."""
    entries, _, _ = questions._entries(root)
    dotted = [read for read in entries if read.identity and _DOTTED.match(read.identity)]
    if not dotted:
        return None
    table = _table_for(root, entries, dotted)
    pairs = [(read.record, _named(root, table[read.identity or ""], read.question)) for read in dotted]
    touched = _touched(root, pairs, table, left_alone)
    left = (unsettled or _unsettled)(root, touched)
    if left:
        raise Refused("uncommitted or untracked, so the run could not be read back on its own: " + ", ".join(left))
    why = move_doc.refusal(root, pairs)
    if why:
        raise Refused(why)
    migrated = Migrated(table, pairs)
    if dry_run:
        migrated.rewritten = touched
        return migrated
    move_doc.perform(root, pairs, announce=lambda said: None)
    migrated.unrepaired = move_doc.unrepaired_mentions(root, pairs)
    done = root / questions.STORE / "done"
    if done.is_dir() and not any(done.iterdir()):
        done.rmdir()
    _name_and_open(root, dotted, table, now, first_added or _first_added)
    migrated.rewritten = _rewritten_through(root, table, _names(pairs), left_alone)
    _write_table(root, table, {read.identity: read.question for read in entries})
    _forget_windows(root)
    migrated.broken = _unresolved(root, left_alone)
    return migrated


def name_by_words(
    root: Path,
    dry_run: bool = False,
    unsettled: Callable[[Path, list[str]], list[str]] | None = None,
    left_alone: tuple[str, ...] = (),
) -> Migrated | None:
    """Each entry named by its id alone renamed to its id and its words, and whatever cites it
    repaired; `None` when no entry is so named."""
    entries, _, _ = questions._entries(root)
    bare = [read for read in entries if posixpath.basename(read.record) == f"{read.identity}.md"]
    if not bare:
        return None
    pairs = [(read.record, _named(root, read.identity or "", read.question)) for read in bare]
    names = _names(pairs)
    naming = [
        name for name in _scope(root, left_alone)
        if name.startswith("docs/") and (root / name).is_file() and _BARE_NAME.search((root / name).read_text(encoding="utf-8"))
    ]
    touched = sorted({operation.subject for operation in move_doc._change_set(root, pairs)} | set(naming) | {source for source, _ in pairs})
    left = (unsettled or _unsettled)(root, touched)
    if left:
        raise Refused("uncommitted or untracked, so the run could not be read back on its own: " + ", ".join(left))
    why = move_doc.refusal(root, pairs)
    if why:
        raise Refused(why)
    migrated = Migrated({}, pairs, touched if dry_run else [])
    if dry_run:
        return migrated
    move_doc.perform(root, pairs, announce=lambda said: None)
    migrated.unrepaired = move_doc.unrepaired_mentions(root, pairs)
    for name in _scope(root, left_alone):
        path = root / name
        if not name.startswith("docs/") or not path.is_file():
            continue
        text = path.read_bytes().decode("utf-8")
        rewritten = questions._outside_fences(text, lambda line: _BARE_NAME.sub(lambda found: names.get(found.group(1), found.group(0)), line))
        if rewritten != text:
            questions._replace(path, rewritten)
            migrated.rewritten.append(name)
    migrated.broken = _unresolved(root, left_alone)
    return migrated


def _named(root: Path, identity: str, question: str) -> str:
    """The record a question stands in: its id and its words, as the writer names one."""
    return f"{questions.STORE}/{questions.entry_name(root, identity, question)}"


def _names(pairs: list[tuple[str, str]]) -> dict[str, str]:
    """Each moved entry's file name, by its id."""
    return {posixpath.basename(target)[: len("q-") + 6]: posixpath.basename(target) for _, target in pairs}


# --- the table --------------------------------------------------------------------------------


def _table_for(root: Path, entries: list[questions.Entry], dotted: list[questions.Entry]) -> dict[str, str]:
    """Each dotted id's new one: the one the table already gives, so a re-run on a branch made
    before the migration agrees with it, or one drawn free of every id held."""
    table = questions.former_ids(root)
    taken = {read.identity for read in entries} | set(table.values())
    for read in dotted:
        identity = read.identity or ""
        if identity not in table:
            drawn = questions.draw_id()
            while drawn in taken:
                drawn = questions.draw_id()
            table[identity] = drawn
            taken.add(drawn)
    return table


def _write_table(root: Path, table: dict[str, str], words: dict[str | None, str]) -> None:
    rows = [f"| {old} | {new} | {words.get(old, '')} |" for old, new in sorted(table.items(), key=lambda pair: questions._positions(pair[0]))]
    text = "\n".join(
        [
            "# Former ids",
            "",
            "Each question's id before the store's ids stopped saying where a question sits, with the id it",
            "has now. Written once by the migration; history is read through it.",
            "",
            "| former | now | question |",
            "|---|---|---|",
            *rows,
        ]
    )
    (root / questions.FORMER_IDS).write_text(text + "\n", encoding="utf-8", newline="\n")


# --- what the run touches ---------------------------------------------------------------------


def _scope(root: Path, left_alone: tuple[str, ...]) -> list[str]:
    """The records the run rewrites ids in: today's rename scope, the evidence and the table left
    out."""
    return [
        name
        for name in questions._records_naming_ids(root)
        if not name.startswith(left_alone) and name != questions.FORMER_IDS
    ]


def _touched(root: Path, pairs: list[tuple[str, str]], table: dict[str, str], left_alone: tuple[str, ...]) -> list[str]:
    """Every file the run would write: the entries it moves, what cites them, and what names an id
    it replaces."""
    named = re.compile("|".join(re.escape(old) for old in sorted(table, key=len, reverse=True)))
    citing = [operation.subject for operation in move_doc._change_set(root, pairs)]
    naming = [name for name in _scope(root, left_alone) if (root / name).is_file() and named.search((root / name).read_text(encoding="utf-8"))]
    return sorted(set(citing) | set(naming) | {source for source, _ in pairs})


def _unsettled(root: Path, names: list[str]) -> list[str]:
    """The files among `names` git holds changes of, or does not track — the sessions' rows aside,
    which every running session writes as it goes."""
    rows = set(sessions.records(root))
    asked = [name for name in names if name not in rows]
    if not asked:
        return []
    # The whole status, filtered here: hundreds of paths overrun a command line on Windows.
    said = subprocess.run(
        ["git", "status", "--porcelain", "-z", "--untracked-files=all"], cwd=root, capture_output=True, encoding="utf-8", check=True
    )
    unsettled = {entry[3:] for entry in said.stdout.split("\0") if len(entry) > 3}
    return sorted(unsettled & set(asked))


# --- the steps ----------------------------------------------------------------------------------


def _name_and_open(
    root: Path,
    dotted: list[questions.Entry],
    table: dict[str, str],
    now: datetime,
    first_added: Callable[[Path, str], datetime | None],
) -> None:
    """Each moved entry's title takes its new id, and its header an `opened`: siblings in today's
    order, each at least a second after the one before, the first at the second its file was first
    added — so siblings added in one commit keep their order."""
    by_parent: dict[str | None, list[questions.Entry]] = {}
    for read in dotted:
        by_parent.setdefault(read.parent, []).append(read)
    for siblings in by_parent.values():
        before: datetime | None = None
        for read in sorted(siblings, key=lambda each: questions._positions(each.identity or "q-0")):
            stamp = first_added(root, read.record) or now
            stamp = stamp.astimezone(timezone.utc).replace(microsecond=0)
            if before is not None and stamp <= before:
                stamp = before + timedelta(seconds=1)
            before = stamp
            new = table[read.identity or ""]
            record = _named(root, new, read.question)
            text = (root / record).read_text(encoding="utf-8")
            moved, _ = questions._read(record, text)
            parts = dict(moved.parts)
            parts.setdefault("opened", questions.Part(stamp.strftime(questions.OPENED_FORMAT), 0))
            (root / record).write_text(
                questions._entry_text(replace(moved, identity=new, parts=parts)), encoding="utf-8", newline="\n"
            )


def _rewritten_through(root: Path, table: dict[str, str], names: dict[str, str], left_alone: tuple[str, ...]) -> list[str]:
    """Every id the table replaces, rewritten where today's rename rewrites one: under `docs/`,
    outside fenced blocks, a path written whole first and then the bare id; elsewhere a straw dog's
    or a `TODO`'s binding alone."""

    def renamed(line: str) -> str:
        line = _DOTTED_PATH.sub(lambda found: names[table[found.group(1)]] if found.group(1) in table else found.group(0), line)
        return questions._BARE_ID.sub(lambda found: table.get(found.group(0), found.group(0)), line)

    rewrote = []
    for name in _scope(root, left_alone):
        path = root / name
        if not path.is_file():
            continue
        text = path.read_bytes().decode("utf-8")
        if name.startswith("docs/"):
            rewritten = questions._outside_fences(text, renamed)
        else:
            rewritten = with_question_bindings_retargeted(name, text, table.get)
        if rewritten != text:
            questions._replace(path, rewritten)
            rewrote.append(name)
    return rewrote


def _forget_windows(root: Path) -> None:
    """The windows remembered for this tree, so a running session's next window does not count
    every question as gone and every one as new."""
    folder = sessions.memory(root, "x").parent
    if folder.is_dir():
        shutil.rmtree(folder, ignore_errors=True)


def _unresolved(root: Path, left_alone: tuple[str, ...]) -> list[str]:
    """Every citation of a markdown record that resolves to no file, as `record: target`."""
    broken = []
    for name in corpus(root):
        if not name.endswith(".md") or name.startswith(left_alone):
            continue
        for written in citations((root / name).read_text(encoding="utf-8")):
            target = cited_record(root, name, target_of(written))
            if target and not (root / target).exists():
                broken.append(f"{name}: {written}")
    return broken


def _first_added(root: Path, record: str) -> datetime | None:
    """The second the file was first added, following renames; `None` where git knows none."""
    said = subprocess.run(
        ["git", "log", "--diff-filter=A", "--follow", "--format=%aI", "--", record],
        cwd=root,
        capture_output=True,
        encoding="utf-8",
    )
    lines = said.stdout.split()
    return datetime.fromisoformat(lines[-1]) if said.returncode == 0 and lines else None


def _report(migrated: Migrated, dry_run: bool) -> None:
    verb = "would move" if dry_run else "moved"
    print(f"{verb} {len(migrated.moved)} entries; {'would rewrite' if dry_run else 'rewrote'} {len(migrated.rewritten)} files")
    for mention in migrated.unrepaired:
        print(f"left as written: {mention}")
    for citation in migrated.broken:
        print(f"resolves to nothing: {citation}")
    if not dry_run:
        print(
            "next: run every script's --check, commit this alone, then "
            "`maintain.py --mark '*' decisions <outcome> <that commit>`"
        )


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:], Path(__file__).resolve().parents[3]))
