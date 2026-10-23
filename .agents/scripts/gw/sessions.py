# Mechanism: session
"""The sessions of the tree: each one's row, from its registration to its removal.

    uv run --offline --no-project python .agents/scripts/gw/sessions.py --end --session <tag>
    uv run --offline --no-project python .agents/scripts/gw/sessions.py --check

A session is one chat of a host with the tree, from its `/recall` to its `/conclude`, known by the
steadiest id the host gives the chat. Its row is one file under `docs/sessions/rows/`, named by
its tag and holding one line — its tag, whether it runs, when the row was last written, its
current question or `-`, and up to four recent ones — so no two sessions ever write one file. A
store from before keeps its rows under `docs/questions/sessions.d/`, or every row in the single
file `docs/questions/sessions`; both are carried into the folder at the first write, by links
that never overwrite.

The question script imports this one and never the reverse: what the row's life needs of the
store — the entry index for a position's check, the store's own types for what it reports — is
taken as an argument or imported inside the function that uses it, so the row stands without the
store. `--end` is the conclude's last act; `--check` is the rows' maintainer, format never
content.
"""

from __future__ import annotations

import functools
import hashlib
import json
import os
import re
import secrets
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

# The rows' folder, a file per session, shared by every session.
ROWS = "docs/sessions/rows"
# Where a store from before kept the rows, and before that every row in one file; each is read
# until its first write carries it over.
FORMER_ROWS = "docs/questions/sessions.d"
SINGLE_FILE = "docs/questions/sessions"
# A running row whose session nothing has seen for this long is ended by the next wake, quietly
# (the user, 2026-10-10).
SILENT_AFTER = timedelta(hours=3)
# A row that has read ended for this long is removed by the next wake: a chat the host reopens
# finds its row under the same id until then, and rarely comes later (the user, 2026-10-22).
GONE_AFTER = timedelta(days=7)
# Where the fingerprint of each session's last window is kept, the session's sign of life; `None`
# is the machine's temp folder.
WINDOW_MEMORY: str | None = None
ROW_FORM = "`<tag> running|ended <YYYY-MM-DDTHH:MMZ> <q-id>|- [<q-id>,… up to four]`"
_USAGE = "usage: sessions.py --end --session <tag> | --check"


@dataclass(frozen=True)
class Session:
    """One session's row: where one conversation stands in the store, and when the row was last
    written, in UTC to the minute. `record` is the file it was read from, for the check to name."""

    tag: str
    running: bool
    wrote: datetime
    current: str | None
    recent: list[str]
    line: int
    record: str = ROWS


def main(argv: list[str], root: Path, now: datetime | None = None) -> int:
    now = now or datetime.now(timezone.utc)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    from questions import Refused  # noqa: PLC0415 — the store's types, never at module level

    try:
        if len(argv) == 3 and argv[:2] == ["--end", "--session"]:
            ended = end(root, argv[2], now)
            print(f"ended {ended.tag} at {ended.current or 'no position'}")
            return 0
        if argv == ["--check"]:
            problems, findings, unreadable = check(root, _index(root))
            print(
                json.dumps(
                    {
                        "diagnostics": [note.as_record() for note in problems],
                        "findings": [note.as_record() for note in findings],
                        "skipped": [passed_over.as_record() for passed_over in unreadable],
                    },
                    indent=2,
                )
            )
            return 1 if problems or unreadable else 0
    except Refused as refusal:
        print(f"refused: {refusal}")
        return 2
    print(_USAGE)
    return 2


# --- the rows -----------------------------------------------------------------------------------
# TODO q-0037.0017.0005: one folder in the working tree is how running sessions see each other,
# until that work says how registrations reach sessions that do not share the directory.


def rows(root: Path) -> tuple[list[Session], list, list]:
    """Every session, and every file or line the form does not admit: the folder's, a file per
    session named by its tag; and in a store from before, the rows under the former folder or the
    single file's lines not carried over yet — a session in two places is read from the folder,
    which is newer. Listed by when each last wrote, then by tag. None is no sessions."""
    sessions, problems, unreadable = _rows_in(root, ROWS)
    for former in (FORMER_ROWS,):
        older, older_problems, older_unreadable = _rows_in(root, former)
        filed = {held.tag for held in sessions}
        sessions += [held for held in older if held.tag not in filed]
        problems += older_problems
        unreadable += older_unreadable
    single, single_problems, single_unreadable = _rows_in_single_file(root)
    filed = {held.tag for held in sessions}
    sessions += [held for held in single if held.tag not in filed]
    ordered = sorted(sessions, key=lambda held: (held.wrote, held.tag))
    return ordered, problems + single_problems, unreadable + single_unreadable


def held(root: Path, tag: str) -> Session:
    """The row of a registered session; an unregistered tag is refused with the way to register."""
    found = next((each for each in rows(root)[0] if each.tag == tag), None)
    if found is None:
        from questions import Refused  # noqa: PLC0415

        raise Refused(f"no session {tag} is registered in {ROWS}; `--wake` registers one")
    return found


def _rows_in(root: Path, folder_name: str) -> tuple[list[Session], list, list]:
    """Each file one line, the session its name says. A writer's staging file, its name leading
    with a dot, is not a session yet."""
    from questions import Diagnostic, Skipped  # noqa: PLC0415

    folder = root / folder_name
    sessions: list[Session] = []
    problems: list = []
    unreadable: list = []
    if not folder.is_dir():
        return sessions, problems, unreadable
    for path in sorted(folder.iterdir()):
        if not path.is_file() or path.name.startswith("."):
            continue
        record = f"{folder_name}/{path.name}"
        try:
            lines = [line for line in path.read_bytes().decode("utf-8").splitlines() if line.strip()]
        except UnicodeDecodeError:
            unreadable.append(Skipped(record, "is not UTF-8, so its session cannot be read"))
            continue
        read = _row(lines[0], 1) if len(lines) == 1 else None
        if read is None:
            problems.append(Diagnostic(record, 1, f"is not one line {ROW_FORM}"))
        elif read.tag != path.name:
            problems.append(Diagnostic(record, 1, f"holds {read.tag}, not the session it is named for"))
        else:
            sessions.append(Session(read.tag, read.running, read.wrote, read.current, read.recent, 1, record))
    return sessions, problems, unreadable


def _rows_in_single_file(root: Path) -> tuple[list[Session], list, list]:
    """A store from before: one line per session in one file."""
    from questions import Diagnostic, Skipped  # noqa: PLC0415

    path = root / SINGLE_FILE
    try:
        text = path.read_bytes().decode("utf-8")
    except (FileNotFoundError, IsADirectoryError, PermissionError):
        return [], [], []
    except UnicodeDecodeError:
        return [], [], [Skipped(SINGLE_FILE, "is not UTF-8, so no session can be read")]
    sessions: list[Session] = []
    problems: list = []
    for number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        read = _row(line, number)
        if read is None:
            problems.append(Diagnostic(SINGLE_FILE, number, f"line {number} is not {ROW_FORM}"))
        elif any(earlier.tag == read.tag for earlier in sessions):
            problems.append(Diagnostic(SINGLE_FILE, number, f"{read.tag} is registered twice"))
        else:
            sessions.append(Session(read.tag, read.running, read.wrote, read.current, read.recent, number, SINGLE_FILE))
    return sessions, problems, []


@functools.cache
def _form() -> re.Pattern[str]:
    """The row's form, compiled once: the id's form is the store's, read when first needed."""
    from questions import _ID  # noqa: PLC0415

    return re.compile(
        rf"^([A-Za-z0-9][\w.-]*) (running|ended) (\d{{4}}-\d{{2}}-\d{{2}})(?:T(\d{{2}}:\d{{2}})Z)? ({_ID}|-)"
        rf"(?: ({_ID}(?:,{_ID}){{0,3}}))?$"
    )


def _row(line: str, number: int) -> Session | None:
    """A line read, its time as written; a line from before the time was written holds the date
    alone, read as that day's start, and carries the time from its next write."""
    said = _form().match(line.rstrip())
    if said is None:
        return None
    try:
        wrote = datetime.fromisoformat(f"{said.group(3)}T{said.group(4) or '00:00'}").replace(tzinfo=timezone.utc)
    except ValueError:
        return None
    current = None if said.group(5) == "-" else said.group(5)
    recent = said.group(6).split(",") if said.group(6) else []
    return Session(said.group(1), said.group(2) == "running", wrote, current, recent, number)


def row_line(held_row: Session) -> str:
    recent = f" {','.join(held_row.recent)}" if held_row.recent else ""
    state = "running" if held_row.running else "ended"
    return f"{held_row.tag} {state} {stamp(held_row.wrote)} {held_row.current or '-'}{recent}"


def stamp(moment: datetime) -> str:
    return f"{moment:%Y-%m-%dT%H:%MZ}"


def minute(now: datetime) -> datetime:
    """The clock's time as a row holds it: UTC, to the minute."""
    return now.astimezone(timezone.utc).replace(second=0, microsecond=0)


def state(held_row: Session) -> str:
    """One session as the wake's read lists it."""
    running = "running" if held_row.running else "ended"
    recent = f" (recent {', '.join(held_row.recent)})" if held_row.recent else ""
    return f"{held_row.tag} {running}, last wrote {stamp(held_row.wrote)}, at {held_row.current or 'no position yet'}{recent}"


# --- writing a row ------------------------------------------------------------------------------


def write_row(root: Path, held_row: Session) -> None:
    """Write one session's row to its own file and touch no other, so however many sessions write
    at once none undoes another's, and nothing is locked. The line replaces the old in one rename,
    so a reader never meets half a file. It is the writing session's own, except when a wake ends a
    silent one or a rename rewrites the ids it names."""
    _write_row_file(folder(root), held_row.tag, row_line(held_row))


def _write_row_file(rows_folder: Path, name: str, line: str) -> None:
    path = rows_folder / name
    staging = rows_folder / f".{name}.{secrets.token_hex(4)}.tmp"
    try:
        staging.write_text(line + "\n", encoding="utf-8", newline="\n")
        staging.replace(path)
    finally:
        staging.unlink(missing_ok=True)


def folder(root: Path) -> Path:
    """The folder, made at its first need; a store from before has its former folder and its
    single file carried over first."""
    rows_folder = root / ROWS
    rows_folder.mkdir(parents=True, exist_ok=True)
    if (root / FORMER_ROWS).is_dir():
        _carry_over_folder(root / FORMER_ROWS, rows_folder)
    if (root / SINGLE_FILE).is_file():
        _carry_over_single_file(root / SINGLE_FILE, rows_folder)
    return rows_folder


def _carry_over_folder(former: Path, rows_folder: Path) -> None:
    """Each row of the former folder to its file in the folder unless that file exists — its
    session wrote it since, and it is newer — then the former file removed, and the former folder
    once it holds nothing. Every step may run twice at once and lands the same: a row is placed by
    a link that refuses an existing name, so it is never half-written and never over a newer one."""
    for path in sorted(former.iterdir()):
        if not path.is_file() or path.name.startswith("."):
            continue
        try:
            os.link(path, rows_folder / path.name)
        except FileExistsError:
            pass
        except FileNotFoundError:
            continue  # another writer carried it over meanwhile
        _remove(path)
    try:
        former.rmdir()
    except OSError:
        pass  # a file left for the next write, or a writer still placing one


def _carry_over_single_file(single: Path, rows_folder: Path) -> None:
    """The single file's lines, each to its session's file unless that file exists, then the single
    file removed. A line the form does not admit keeps a name of its own, for the check to report."""
    try:
        lines = [line for line in single.read_text(encoding="utf-8").splitlines() if line.strip()]
    except FileNotFoundError:
        return
    for number, line in enumerate(lines, start=1):
        read = _row(line, number)
        name = read.tag if read is not None else f"unreadable-{number}"
        staging = rows_folder / f".{name}.{secrets.token_hex(4)}.tmp"
        try:
            staging.write_text(line + "\n", encoding="utf-8", newline="\n")
            os.link(staging, rows_folder / name)
        except FileExistsError:
            pass
        finally:
            staging.unlink(missing_ok=True)
    _remove(single)


def _remove(path: Path) -> None:
    """A file removed, or left: Windows will not remove a file another process holds open to read,
    and the next write or wake removes what is left; one already gone — another wake removed it —
    is nothing."""
    try:
        path.unlink(missing_ok=True)
    except PermissionError:
        pass


# --- a session's life ---------------------------------------------------------------------------


def register(root: Path, now: datetime, tag: str | None = None) -> Session:
    """A new session's row, running and with no position yet, under the host's own session id
    where a hook gave one, or else a tag minted here that no session holds."""
    if tag is None:
        taken = {each.tag for each in rows(root)[0]}
        tag = f"s-{now:%m%d}-{secrets.token_hex(2)}"
        while tag in taken:
            tag = f"s-{now:%m%d}-{secrets.token_hex(2)}"
    held_row = Session(tag, True, minute(now), None, [], 0)
    write_row(root, held_row)
    return held_row


def arrive(root: Path, tag: str, now: datetime) -> tuple[Session, bool]:
    """A session starting or resuming: registered once under the host's id, running again if it
    had ended, its position kept. Says whether it was registered now."""
    known = {each.tag: each for each in rows(root)[0]}
    if tag not in known:
        return register(root, now, tag), True
    held_row = known[tag]
    if not held_row.running:
        held_row = Session(held_row.tag, True, minute(now), held_row.current, held_row.recent, held_row.line)
        write_row(root, held_row)
    return held_row, False


def tend(root: Path, now: datetime, waking: str) -> None:
    """What a wake does to the other sessions' rows, and says nothing of: a running row whose
    session nothing has seen for `SILENT_AFTER` reads ended, its position kept and its time the
    moment it was last seen, so the days until it is gone run from the session's end (the user,
    2026-10-10 and 2026-10-22); a row that already read ended for `GONE_AFTER` is removed — ended at
    this wake, gone at a later one. A running row is never removed.

    The writes to a row not its own, besides a rename: safe because a silent session has no
    write of its own to meet. The session's next message turns an ended row running again; a
    removed one is registered anew when its host returns.
    """
    for held_row in rows(root)[0]:
        if held_row.tag == waking:
            continue
        if held_row.running:
            seen_at = last_seen(root, held_row)
            if now - seen_at >= SILENT_AFTER:
                write_row(root, Session(held_row.tag, False, minute(seen_at), held_row.current, held_row.recent, held_row.line))
        elif now - held_row.wrote >= GONE_AFTER:
            _remove(root / held_row.record)


def last_seen(root: Path, held_row: Session) -> datetime:
    """The later of the row's time and its window memory's: a session is seen while its messages
    reach a hook or it writes its row. The memory is kept outside the tree, so the committed file
    does not move with every message."""
    seen_file = memory(root, held_row.tag)
    if not seen_file.is_file():
        return held_row.wrote
    return max(held_row.wrote, datetime.fromtimestamp(seen_file.stat().st_mtime, timezone.utc))


def seen(root: Path, tag: str, now: datetime) -> None:
    """A sign of life from the session: its window memory takes the time, and a row that reads
    ended runs again, its position kept — a wake may have ended it while it sat idle. A tag no row
    holds is nothing to mark."""
    found = next((each for each in rows(root)[0] if each.tag == tag), None)
    if found is None:
        return
    seen_file = memory(root, tag)
    seen_file.parent.mkdir(parents=True, exist_ok=True)
    if not seen_file.is_file():
        seen_file.write_text("", encoding="utf-8")
    os.utime(seen_file, (now.timestamp(), now.timestamp()))
    if not found.running:
        write_row(root, Session(found.tag, True, minute(now), found.current, found.recent, found.line))


def end(root: Path, tag: str, now: datetime) -> Session:
    """The conclude's last act: the session is marked ended and keeps its position, so the wake of
    a chat the host reopens finds where it stopped."""
    held_row = held(root, tag)
    ended = Session(held_row.tag, False, minute(now), held_row.current, held_row.recent, held_row.line)
    write_row(root, ended)
    return ended


def tag_of(identity: str) -> str:
    """A host's session id as a session tag: the characters a row holds, no others."""
    tag = re.sub(r"[^\w.-]", "-", identity.strip())
    if not tag:
        from questions import Refused  # noqa: PLC0415

        raise Refused("the hook's input names no session")
    return tag if tag[0].isalnum() else f"s{tag}"


def memory(root: Path, tag: str) -> Path:
    """Where the fingerprint of a session's last window is kept: outside the tree, so it never
    churns the store, keyed by tree and session. Its time is the session's sign of life."""
    tree = hashlib.sha256(str(root.resolve()).encode()).hexdigest()[:16]
    return Path(WINDOW_MEMORY or Path(tempfile.gettempdir()) / "questions-windows") / tree / tag


def forget_window(root: Path, tag: str) -> None:
    """After a compaction the last window is gone from the conversation, so the next is whole. The
    memory is emptied rather than removed: its time is the session's sign of life."""
    seen_file = memory(root, tag)
    if seen_file.is_file():
        seen_file.write_text("", encoding="utf-8")


# --- the row and the store's moves --------------------------------------------------------------


def moved(held_row: Session, position: str | None, now: datetime) -> Session | None:
    """The session's row after an `at`: the old position joins the recent ones, at most four. An
    `at` that leaves a running session where it stood leaves its row as it was, so the committed
    file does not move with every turn; the window memory says the session is alive."""
    if position is None:
        return None
    if held_row.running and position == held_row.current:
        return held_row
    recent = [held_row.current] if held_row.current and held_row.current != position else []
    recent += [identity for identity in held_row.recent if identity != position and identity not in recent]
    return Session(held_row.tag, True, minute(now), position, recent[:4], held_row.line)


def renamed(held_row: Session, renames: dict[str, str]) -> Session:
    """This session's row as a rename left it, so its own write does not put old ids back."""
    current = renames.get(held_row.current or "", held_row.current)
    recent = [renames.get(identity, identity) for identity in held_row.recent]
    return Session(held_row.tag, held_row.running, held_row.wrote, current, recent, held_row.line)


def records(root: Path) -> list[str]:
    """Every file a rename reads for the ids a row names: each session's file, wherever it stands,
    and the single file of a store from before."""
    named = []
    for folder_name in (ROWS, FORMER_ROWS):
        rows_folder = root / folder_name
        if rows_folder.is_dir():
            named += [
                f"{folder_name}/{path.name}"
                for path in sorted(rows_folder.iterdir())
                if path.is_file() and not path.name.startswith(".")
            ]
    if (root / SINGLE_FILE).is_file():
        named.append(SINGLE_FILE)
    return named


# --- the check ----------------------------------------------------------------------------------


def check(root: Path, index: dict) -> tuple[list, list, list]:
    """Every row against its form, and against the store: a position naming no entry is a
    diagnostic; a running session whose question closed under it is a finding, shown in that
    session's next window. A silent session is no finding — the next wake ends it."""
    from questions import Diagnostic, Finding  # noqa: PLC0415

    sessions, problems, unreadable = rows(root)
    problems += [
        Diagnostic(held_row.record, held_row.line, f"{held_row.tag} stands at {identity}, which no entry holds")
        for held_row in sessions
        for identity in ([held_row.current] if held_row.current else []) + held_row.recent
        if identity not in index
    ]
    findings = [
        Finding(held_row.record, held_row.line, f"{held_row.tag} stands at {held_row.current}, which is closed")
        for held_row in sessions
        if held_row.running and (standing := index.get(held_row.current or "")) is not None and not standing.open
    ]
    return problems, findings, unreadable


def _index(root: Path) -> dict:
    """The store's entry index, for the check alone; a tree with no store has an empty one."""
    from questions import STORE, read_store  # noqa: PLC0415

    return read_store(root).index if (root / STORE).is_dir() else {}


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:], Path.cwd()))
