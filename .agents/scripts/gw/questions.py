"""The open questions of the tree, kept in one store, and whether the store keeps its shape.

    uv run --offline --no-project python .agents/scripts/gw/questions.py --check
    uv run --offline --no-project python .agents/scripts/gw/questions.py --window --session <tag>
    uv run --offline --no-project python .agents/scripts/gw/questions.py --wake [--session <tag>]
    uv run --offline --no-project python .agents/scripts/gw/questions.py --end --session <tag>
    uv run --offline --no-project python .agents/scripts/gw/questions.py --tree [<q-id>]

The store is `docs/questions/`: one file per question, its parent line the hierarchy's one home,
wholly closed subtrees in `docs/questions/done/`, and `docs/questions/sessions`, where each running
session keeps its position. The formats are the questions skill's.

`--check` is the maintainer. It writes nothing; its exit status is the verdict and its JSON is for
the person reading a failure. A tree with no store has nothing to check and passes. `--window` is
what the agent reads before placing a message; `--wake` registers a session and reads where the
work stands; `--end` closes a session's line; `--tree` draws the live tree for a person. Only the
wake and the end write, and each writes only its own session's line.
"""

from __future__ import annotations

import hashlib
import json
import posixpath
import re
import secrets
import sys
import tempfile
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from docs_corpus import cited_record, citations, corpus, target_of  # noqa: E402  (path set above)

STORE = "docs/questions"
SESSIONS = "docs/questions/sessions"
STALE_AFTER_DAYS = 7
# A twin shares at least this many content words, and at least half of the shorter title's.
TWIN_SHARED_WORDS = 3
SLUG_LENGTH = 160
# Where the fingerprint of each session's last window is kept; `None` is the machine's temp folder.
WINDOW_MEMORY: str | None = None
PARTS = ("part of", "depends on", "state", "owner", "answer", "lean")
KINDS = ("decided", "pruned", "merged", "deferred", "moot", "superseded")
_USAGE = (
    "usage: questions.py --check | --window --session <tag> | --wake [--session <tag>] "
    "| --end --session <tag> | --tree [<q-id>] | --declare \"<line>\" --session <tag>"
)
_STOPWORDS = frozenset(
    "a an and are as at be by can do does for from how in is it of on or should the this to we "
    "what when where whether which who why will with".split()
)
_TITLE = re.compile(r"^# (q-\d{4,}) (\S.*)$")
_BULLET = re.compile(r"^- \*\*([^*]+)\*\* ?(.*)$")
_CONTINUATION = re.compile(r"^\s+\S")
_STATE = re.compile(rf"^(open|closed:({'|'.join(KINDS)}))(, suspect)?$")
_IDENTITY = re.compile(r"^q-\d{4,}$")
_ENTRY_NAME = re.compile(rf"^{STORE}/(?:done/)?(q-\d{{4,}})-([a-z0-9]+(?:-[a-z0-9]+)*)\.md$")
_DEFERRAL = re.compile(r"^until \S.*, meanwhile \S.*$")
_SESSION = re.compile(
    r"^([A-Za-z0-9][\w.-]*) (running|ended) (\d{4}-\d{2}-\d{2}) (q-\d{4,}|-)(?: (q-\d{4,}(?:,q-\d{4,}){0,3}))?$"
)
_HEADING = re.compile(r"^#{1,6} +(.*?)(?: +#+)? *$")
_FENCE = re.compile(r"^\s*(```|~~~)")


@dataclass(frozen=True)
class Part:
    """One bullet of an entry, its continuation lines joined, and the line it starts on."""

    value: str
    line: int


@dataclass(frozen=True)
class Entry:
    """One question as its file says it. Nothing here has been judged yet."""

    record: str
    identity: str | None
    question: str
    parts: dict[str, Part]

    @property
    def state(self) -> re.Match[str] | None:
        said = self.parts.get("state")
        return _STATE.match(said.value) if said else None

    @property
    def kind(self) -> str | None:
        """How it closed, or `None` while it is open or its state cannot be read."""
        return self.state.group(2) if self.state else None

    @property
    def open(self) -> bool:
        return bool(self.state) and self.state.group(1) == "open"

    @property
    def suspect(self) -> bool:
        return bool(self.state and self.state.group(3))

    @property
    def parent(self) -> str | None:
        said = self.parts.get("part of")
        return said.value if said and _IDENTITY.match(said.value) else None

    @property
    def dependencies(self) -> list[str]:
        said = self.parts.get("depends on")
        return (_ids(said.value) or []) if said else []

    @property
    def archived(self) -> bool:
        return self.record.startswith(f"{STORE}/done/")

    @property
    def held_open(self) -> bool:
        """Whether the live store must keep it: open, or closed with something still to re-read —
        a deferral whose condition the wake re-checks, or a suspect answer."""
        return self.open or self.suspect or self.kind == "deferred"

    @property
    def points_to(self) -> str | None:
        """The question a merge or a supersession points at."""
        answer = self.parts.get("answer")
        if self.kind in ("merged", "superseded") and answer and _IDENTITY.match(answer.value):
            return answer.value
        return None


@dataclass(frozen=True)
class Diagnostic:
    record: str
    line: int | None
    problem: str

    def as_record(self) -> dict:
        return {"record": self.record, "line": self.line, "problem": self.problem}


@dataclass(frozen=True)
class Finding:
    """What a person should look at and the store is not wrong for: it never fails the run."""

    record: str
    line: int | None
    finding: str

    def as_record(self) -> dict:
        return {"record": self.record, "line": self.line, "finding": self.finding}


@dataclass(frozen=True)
class Skipped:
    """A file the check could not read. Reported and failed, never dropped: a narrowed scan is not
    a pass."""

    record: str
    why: str

    def as_record(self) -> dict:
        return {"record": self.record, "why": self.why}


@dataclass(frozen=True)
class Checked:
    present: bool
    entries: int
    diagnostics: list[Diagnostic]
    findings: list[Finding]
    skipped: list[Skipped]

    def as_record(self) -> dict:
        return {
            "store": "present" if self.present else "absent",
            "entries": self.entries,
            "diagnostics": [note.as_record() for note in self.diagnostics],
            "findings": [note.as_record() for note in self.findings],
            "skipped": [passed_over.as_record() for passed_over in self.skipped],
        }


class Refused(Exception):
    """A call the store cannot answer as asked. The message says what to settle first."""


def main(argv: list[str], root: Path | None = None, today: date | None = None) -> int:
    root = root or Path(__file__).resolve().parents[3]
    today = today or date.today()
    # A title may hold any character, and a Windows console's default encoding holds few of them:
    # printed as-is, one arrow in a question would end the run with nothing shown.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        if argv == ["--check"]:
            checked = check(root, today)
            print(json.dumps(checked.as_record(), indent=2))
            return 1 if checked.diagnostics or checked.skipped else 0
        if len(argv) in (3, 4) and argv[:2] == ["--window", "--session"] and argv[3:] in ([], ["--full"]):
            print(window(root, argv[2], full=argv[3:] == ["--full"]))
            return 0
        if len(argv) == 2 and argv[0] == "--hook":
            print(hook(root, argv[1], sys.stdin.read(), today))
            return 0
        if argv == ["--wake"] or (len(argv) == 3 and argv[:2] == ["--wake", "--session"]):
            print(wake(root, today, argv[2] if len(argv) == 3 else None))
            return 0
        if argv[:1] == ["--tree"] and len(argv) <= 2:
            print(tree(root, argv[1] if len(argv) == 2 else None))
            return 0
        if len(argv) == 4 and argv[0] == "--declare" and argv[2] == "--session":
            written = declare(root, argv[3], parse(argv[1]), today)
            for record in written.entries:
                print(f"wrote {record}")
            if written.session is not None:
                print(f"{written.session.tag} at {written.session.current}")
            return 0
        if len(argv) == 3 and argv[:2] == ["--end", "--session"]:
            held = end(root, argv[2], today)
            print(f"ended {held.tag} at {held.current or 'no position'}")
            return 0
    except Refused as refusal:
        print(f"refused: {refusal}")
        return 2
    except WriteInterrupted as stopped:
        print(f"stopped: {stopped}; nothing was rolled back")
        for record in stopped.completed:
            print(f"completed: {record}")
        return 1
    print(_USAGE)
    return 2


def check(root: Path, today: date | None = None) -> Checked:
    """Every entry, live and archived, and the sessions file against the store's shape; then what
    a person should look at in a store that keeps it."""
    if not (root / STORE).is_dir():
        return Checked(False, 0, [], [], [])
    entries, diagnostics, skipped = _entries(root)
    diagnostics += [note for read in entries for note in _answer_problems(root, read)]
    index = {read.identity: read for read in entries if read.identity}
    sessions, session_problems, unreadable = _sessions(root)
    diagnostics += (
        _identity_problems(entries)
        + _relation_problems(entries, index)
        + session_problems
        + _position_problems(sessions, index)
    )
    findings = (
        _session_findings(sessions, index, today or date.today())
        + _likely_twins(entries)
        + _ready_for_done(entries, index)
    )
    return Checked(True, len(entries), diagnostics, findings, skipped + unreadable)


def _entries(
    root: Path, seen: dict[str, bytes] | None = None
) -> tuple[list[Entry], list[Diagnostic], list[Skipped]]:
    """Every entry file read, with what its own text gets wrong: its form and its name. Whether its
    answer resolves reads other files, so it is the check's to ask and not every reader's.

    `seen`, when given, receives the bytes each entry was read from, so a writer can tell later
    whether the file moved since.
    """
    entries: list[Entry] = []
    diagnostics: list[Diagnostic] = []
    skipped: list[Skipped] = []
    for name in _entry_files(root):
        stem = _ENTRY_NAME.match(name)
        if stem is None:
            diagnostics.append(
                Diagnostic(name, None, f"is not named `q-NNNN-<slug>.md` in {STORE}/ or its done/")
            )
            continue
        raw = (root / name).read_bytes()
        if seen is not None:
            seen[name] = raw
        try:
            read, problems = _read(name, raw.decode("utf-8"))
        except UnicodeDecodeError:
            skipped.append(Skipped(name, "is not UTF-8, so the entry cannot be read"))
            continue
        entries.append(read)
        diagnostics += problems + _name_problems(read, stem)
    return entries, diagnostics, skipped


def _entry_files(root: Path) -> list[str]:
    """Every markdown file under the store. The sessions file is not markdown and not an entry."""
    return sorted(
        name for name in corpus(root) if name.startswith(f"{STORE}/") and name.endswith(".md")
    )


# --- reading an entry ---------------------------------------------------------------------------


def _read(name: str, text: str) -> tuple[Entry, list[Diagnostic]]:
    """The entry a file's text holds, and whatever in it the format does not admit.

    A line the format does not admit is reported and the rest is still read, so one defect does
    not hide the others behind it.
    """
    lines = text.splitlines()
    problems: list[Diagnostic] = []
    title = _TITLE.match(lines[0]) if lines else None
    if title is None:
        problems.append(Diagnostic(name, 1, "does not open with a title line `# q-NNNN <question>`"))
    parts: dict[str, Part] = {}
    last: str | None = None
    for number, line in enumerate(lines[1:], start=2):
        bullet = _BULLET.match(line)
        if bullet:
            last = bullet.group(1).strip()
            if last not in PARTS:
                problems.append(Diagnostic(name, number, f"`{last}` is not a part of an entry"))
            elif last in parts:
                problems.append(Diagnostic(name, number, f"`{last}` is written twice"))
            else:
                parts[last] = Part(bullet.group(2).strip(), number)
        elif last in parts and _CONTINUATION.match(line):
            joined = parts[last]
            parts[last] = Part(f"{joined.value} {line.strip()}", joined.line)
        elif line.strip():
            problems.append(Diagnostic(name, number, "holds a line that is not one of its parts"))
    read = Entry(name, title.group(1) if title else None, title.group(2) if title else "", parts)
    return read, problems + _state_problems(read) + _relation_form_problems(read)


def _ids(value: str) -> list[str] | None:
    """A comma-separated list of ids, or `None` where anything else is written."""
    written = [item.strip() for item in value.split(",")]
    return written if all(_IDENTITY.match(item) for item in written) else None


def _relation_form_problems(read: Entry) -> list[Diagnostic]:
    """A relation is written as ids: one parent, any number of dependencies."""
    notes = []
    parent = read.parts.get("part of")
    if parent and not _IDENTITY.match(parent.value):
        notes.append(Diagnostic(read.record, parent.line, f"part of is `{parent.value}`, not one id"))
    dependencies = read.parts.get("depends on")
    if dependencies and _ids(dependencies.value) is None:
        notes.append(
            Diagnostic(
                read.record, dependencies.line, f"depends on is `{dependencies.value}`, not a list of ids"
            )
        )
    return notes


def _state_problems(read: Entry) -> list[Diagnostic]:
    said = read.parts.get("state")
    if said is None:
        return [Diagnostic(read.record, 1, "has no state")]
    if read.state is None:
        return [
            Diagnostic(
                read.record,
                said.line,
                f"state is `{said.value}`, not `open` or `closed:<kind>` over {', '.join(KINDS)}, "
                "with `, suspect` after it at most",
            )
        ]
    if read.open and "answer" in read.parts:
        return [Diagnostic(read.record, read.parts["answer"].line, "is open and carries an answer")]
    return []


def _name_problems(read: Entry, stem: re.Match[str]) -> list[Diagnostic]:
    """The filename's id is the title's, and its slug is the whole question, as the writer names it
    (parent decision 55), so a name shortened or left behind by a reworded question is caught."""
    if read.identity is None:
        return []
    if stem.group(1) != read.identity:
        return [
            Diagnostic(read.record, 1, f"is named {stem.group(1)} and its title says {read.identity}")
        ]
    wanted = _slug(read.question)
    if stem.group(2) != wanted:
        return [
            Diagnostic(
                read.record,
                1,
                f"its slug `{stem.group(2)}` is not the question's words; name it `{read.identity}-{wanted}.md`",
            )
        ]
    return []


def _words(text: str) -> list[str]:
    """A text's words as a slug spells them: lower case, an apostrophe dropped inside a word."""
    return re.findall(r"[a-z0-9]+", re.sub(r"['’]", "", text.lower()))


# --- the answer ---------------------------------------------------------------------------------


def _answer_problems(root: Path, read: Entry) -> list[Diagnostic]:
    """A closed question points to its answer and never holds it (parent decision 43).

    What it points to depends on how it closed: the doc, ADR or code that decided it; the
    question it was merged into or superseded by; for a deferral, the condition and the default
    to act on meanwhile; for a dead end, its one-line reason.
    """
    if read.kind is None:
        return []
    answer = read.parts.get("answer")
    if answer is None:
        return [
            Diagnostic(read.record, read.parts["state"].line, f"is closed:{read.kind} and has no answer")
        ]
    if read.kind == "decided":
        return _decision_link_problems(root, read, answer)
    if read.kind in ("merged", "superseded") and not _IDENTITY.match(answer.value):
        return [
            Diagnostic(
                read.record, answer.line, f"a {read.kind} answer is the id it points to, not `{answer.value}`"
            )
        ]
    if read.kind == "deferred" and not _DEFERRAL.match(answer.value):
        return [
            Diagnostic(
                read.record, answer.line, "a deferred answer reads `until <condition>, meanwhile <default>`"
            )
        ]
    return []


def _decision_link_problems(root: Path, read: Entry, answer: Part) -> list[Diagnostic]:
    """At least one link, and every link resolving: a renamed heading breaks it as a moved file does."""
    written = citations(answer.value)
    if not written:
        return [Diagnostic(read.record, answer.line, "a decided answer is not a link to what decided it")]
    return [
        Diagnostic(read.record, answer.line, f"the answer links {link}, which does not resolve")
        for link in written
        if not _resolves(root, read.record, link)
    ]


def _resolves(root: Path, citing: str, written: str) -> bool:
    target = target_of(written)
    if target.elsewhere:
        return True
    record = cited_record(root, citing, target)
    if record is None or not (root / record).exists():
        return False
    anchor = target.fragment[1:]
    if not anchor or not record.endswith(".md"):
        return True
    return anchor in _anchors((root / record).read_text(encoding="utf-8"))


def _anchors(text: str) -> set[str]:
    """The fragment each heading of a markdown file answers to, as the host renders it: lower
    case, punctuation dropped, each space a hyphen, a repeated heading numbered from its second."""
    seen: dict[str, int] = {}
    anchors: set[str] = set()
    inside_fence = False
    for line in text.splitlines():
        if _FENCE.match(line):
            inside_fence = not inside_fence
            continue
        heading = _HEADING.match(line)
        if inside_fence or heading is None:
            continue
        slug = re.sub(r"[^\w\- ]", "", heading.group(1).strip().lower()).replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        anchors.add(slug if count == 0 else f"{slug}-{count}")
    return anchors


# --- the store as a whole -----------------------------------------------------------------------


def _identity_problems(entries: list[Entry]) -> list[Diagnostic]:
    """An id is one question's, live or archived: two files holding it make every reference to it
    ambiguous."""
    holders: dict[str, list[str]] = {}
    for read in entries:
        if read.identity:
            holders.setdefault(read.identity, []).append(read.record)
    return [
        Diagnostic(records[1], 1, f"{identity} is held by two files: {', '.join(records)}")
        for identity, records in sorted(holders.items())
        if len(records) > 1
    ]


# --- the relations ------------------------------------------------------------------------------


def _relation_problems(entries: list[Entry], index: dict[str, Entry]) -> list[Diagnostic]:
    """Relations are ids resolved over the live store and `done/` together: an id is placement
    and never a path, so an archived question is still the same question."""
    return _orphans(entries, index) + _cycles(index) + _unmarked_suspects(entries, index)


def _orphans(entries: list[Entry], index: dict[str, Entry]) -> list[Diagnostic]:
    notes = []
    for read in entries:
        named = [("part of", read.parent)] + [("depends on", each) for each in read.dependencies]
        named.append(("answer", read.points_to))
        for relation, identity in named:
            if identity and identity not in index:
                line = read.parts[relation].line
                notes.append(
                    Diagnostic(read.record, line, f"{relation} names {identity}, which no entry holds")
                )
    return notes


def _cycles(index: dict[str, Entry]) -> list[Diagnostic]:
    """Each cycle in *part of* once, reported at its lowest id: a cycle has no root to draw a path
    from."""
    notes = []
    reported: set[str] = set()
    for start in sorted(index):
        walked: list[str] = []
        at: str | None = start
        while at in index and at not in walked:
            walked.append(at)
            at = index[at].parent
        if at not in walked:
            continue
        cycle = walked[walked.index(at) :]
        if reported.isdisjoint(cycle):
            reported.update(cycle)
            lowest = index[min(cycle)]
            notes.append(
                Diagnostic(lowest.record, None, f"part of runs in a cycle: {' → '.join(sorted(cycle))}")
            )
    return notes


def _unmarked_suspects(entries: list[Entry], index: dict[str, Entry]) -> list[Diagnostic]:
    """A closed entry whose ground moved and which does not say so.

    Two grounds are visible to a script: a parent reopened, which is its closure as *superseded*;
    and a dependency still open, which the entry was decided under. An entry already marked
    suspect says what this would, so it is not reported again.
    """
    notes = []
    for read in entries:
        if read.open or read.suspect or read.kind is None:
            continue
        parent = index.get(read.parent or "")
        if parent is not None and parent.kind == "superseded":
            notes.append(
                Diagnostic(
                    read.record,
                    read.parts["part of"].line,
                    f"is closed under {parent.identity}, which was superseded, and is not suspect",
                )
            )
        for identity in read.dependencies:
            if identity in index and index[identity].open:
                notes.append(
                    Diagnostic(
                        read.record,
                        read.parts["depends on"].line,
                        f"is closed, depends on {identity}, which is open, and is not suspect",
                    )
                )
    return notes


# --- the sessions -------------------------------------------------------------------------------
# TODO docs/tickets/01-0010-dev-harness-shared-and-local.md: one sessions file in the working tree
# is how running sessions see each other until that work says how registrations reach sessions
# that do not share the directory.


@dataclass(frozen=True)
class Session:
    """One line of the sessions file: where one conversation stands in the store."""

    tag: str
    running: bool
    wrote: date
    current: str | None
    recent: list[str]
    line: int


def _sessions(root: Path) -> tuple[list[Session], list[Diagnostic], list[Skipped]]:
    """Every session line, and every line the form does not admit. No file is no sessions."""
    path = root / SESSIONS
    if not path.is_file():
        return [], [], []
    try:
        text = path.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        return [], [], [Skipped(SESSIONS, "is not UTF-8, so no session can be read")]
    sessions: list[Session] = []
    problems: list[Diagnostic] = []
    for number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        read = _session(line, number)
        if read is None:
            problems.append(
                Diagnostic(
                    SESSIONS,
                    number,
                    f"line {number} is not "
                    "`<tag> running|ended <YYYY-MM-DD> <q-id>|- [<q-id>,… up to four]`",
                )
            )
        elif any(earlier.tag == read.tag for earlier in sessions):
            problems.append(Diagnostic(SESSIONS, number, f"{read.tag} is registered twice"))
        else:
            sessions.append(read)
    return sessions, problems, []


def _session(line: str, number: int) -> Session | None:
    said = _SESSION.match(line.rstrip())
    if said is None:
        return None
    try:
        wrote = date.fromisoformat(said.group(3))
    except ValueError:
        return None
    current = None if said.group(4) == "-" else said.group(4)
    recent = said.group(5).split(",") if said.group(5) else []
    return Session(said.group(1), said.group(2) == "running", wrote, current, recent, number)


def _session_line(held: Session) -> str:
    recent = f" {','.join(held.recent)}" if held.recent else ""
    state = "running" if held.running else "ended"
    return f"{held.tag} {state} {held.wrote} {held.current or '-'}{recent}"


def _write_own_line(root: Path, held: Session) -> None:
    """Replace this session's line and no other, appending it where there is none.

    The file is re-read just before the write, so a line another session wrote a moment ago is
    kept as found: one session's write is never a refusal of another's (RFC item 10). The new
    text replaces the old in one rename, so a reader never meets half a file.
    """
    path = root / SESSIONS
    lines = path.read_text(encoding="utf-8").splitlines() if path.is_file() else []
    mine = [at for at, line in enumerate(lines) if line.split(" ", 1)[0] == held.tag]
    if mine:
        lines[mine[0]] = _session_line(held)
    else:
        lines.append(_session_line(held))
    path.parent.mkdir(parents=True, exist_ok=True)
    staging = path.with_name(f".{path.name}.{held.tag}.tmp")
    try:
        staging.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
        staging.replace(path)
    finally:
        staging.unlink(missing_ok=True)


def _position_problems(sessions: list[Session], index: dict[str, Entry]) -> list[Diagnostic]:
    return [
        Diagnostic(SESSIONS, held.line, f"{held.tag} stands at {identity}, which no entry holds")
        for held in sessions
        for identity in ([held.current] if held.current else []) + held.recent
        if identity not in index
    ]


def _session_findings(
    sessions: list[Session], index: dict[str, Entry], today: date
) -> list[Finding]:
    """A running session whose question closed under it, or that stopped writing.

    Neither fails the run: the first is shown in that session's next window, and a silent session
    may be alive — a crash leaves a `running` line nobody ends, and only a person can tell.
    """
    notes = []
    for held in sessions:
        if not held.running:
            continue
        standing = index.get(held.current or "")
        if standing is not None and not standing.open:
            notes.append(
                Finding(SESSIONS, held.line, f"{held.tag} stands at {held.current}, which is closed")
            )
        if (today - held.wrote).days > STALE_AFTER_DAYS:
            notes.append(
                Finding(SESSIONS, held.line, f"{held.tag} is running and has not written since {held.wrote}")
            )
    return notes


# --- for a person to settle ---------------------------------------------------------------------


def _likely_twins(entries: list[Entry]) -> list[Finding]:
    """Live title pairs sharing enough content words to be one question asked twice.

    Only the live store is paired: it tracks the open count, while `done/` grows without bound and
    is searched by title when a question looks asked before (parent decision 43). Merging is a
    person's call, so a pair is a finding and never a failure.
    """
    live = [
        (read, set(_words(read.question)) - _STOPWORDS) for read in entries if not read.archived
    ]
    notes = []
    for at, (one, one_words) in enumerate(live):
        for other, other_words in live[at + 1 :]:
            shared = one_words & other_words
            shorter = min(len(one_words), len(other_words))
            if len(shared) >= TWIN_SHARED_WORDS and 2 * len(shared) >= shorter:
                notes.append(
                    Finding(
                        other.record,
                        1,
                        f"{one.identity} and {other.identity} may be one question: both ask about "
                        + ", ".join(sorted(shared)),
                    )
                )
    return notes


def _ready_for_done(entries: list[Entry], index: dict[str, Entry]) -> list[Finding]:
    """The live roots of wholly closed subtrees that nothing held open depends on, each reported
    once at its highest root — the moves `/maintain` makes (parent decision 34)."""
    children: dict[str, list[Entry]] = {}
    for read in entries:
        if read.parent:
            children.setdefault(read.parent, []).append(read)
    leaning = {identity for read in entries if read.held_open for identity in read.dependencies}

    def movable(read: Entry) -> bool:
        return (
            not read.held_open
            and read.identity not in leaning
            and all(movable(child) for child in children.get(read.identity or "", []))
        )

    def moves_with_its_parent(read: Entry) -> bool:
        parent = index.get(read.parent or "")
        return parent is not None and not parent.archived and movable(parent)

    return [
        Finding(read.record, 1, f"{read.identity} and everything under it are closed and ready for done/")
        for read in entries
        if not read.archived and movable(read) and not moves_with_its_parent(read)
    ]


# --- the window ---------------------------------------------------------------------------------


@dataclass(frozen=True)
class Store:
    """The live questions as a tree, with every id resolvable and every session's line.

    The tree is the live directory alone: `done/` holds wholly closed subtrees, which no window
    draws. Ids still resolve over both, since an id is placement and never a path.
    """

    index: dict[str, Entry]
    children: dict[str, list[Entry]]
    roots: list[Entry]
    sessions: list[Session]

    def path(self, identity: str) -> list[Entry]:
        """From the root down to the question, following *part of* lines."""
        return list(reversed(_ancestry(self.index, identity)))

    def under(self, identity: str) -> list[Entry]:
        """Every live question below this one, in id order."""
        found: list[Entry] = []
        waiting = list(self.children.get(identity, []))
        while waiting:
            read = waiting.pop()
            found.append(read)
            waiting += self.children.get(read.identity or "", [])
        return sorted(found, key=_order)

    def session(self, tag: str) -> Session:
        held = next((each for each in self.sessions if each.tag == tag), None)
        if held is None:
            raise Refused(f"no session {tag} is registered in {SESSIONS}; `--wake` registers one")
        return held

    @property
    def next_free(self) -> str:
        return _next_free(self.index)


def _next_free(index: dict[str, Entry]) -> str:
    """The id a new question takes: one past the highest ever given, live or archived, so an id is
    never handed out twice."""
    highest = max((int(identity[2:]) for identity in index), default=0)
    return f"q-{highest + 1:04d}"


def _ancestry(index: dict[str, Entry], identity: str) -> list[Entry]:
    """The question and every question it is part of, up to its root. A cycle stops the walk
    where it would repeat, so a broken store still renders."""
    found: list[Entry] = []
    at = index.get(identity)
    while at is not None and at not in found:
        found.append(at)
        at = index.get(at.parent or "")
    return found


def read_store(root: Path, seen: dict[str, bytes] | None = None) -> Store:
    """The store as the window and the wake read it. A file the check would report is read as far
    as it goes, and one that cannot be read at all is left out — the check is what says so."""
    entries, _, _ = _entries(root, seen)
    sessions, _, _ = _sessions(root)
    live = sorted((read for read in entries if read.identity and not read.archived), key=_order)
    children: dict[str, list[Entry]] = {}
    for read in live:
        if read.parent:
            children.setdefault(read.parent, []).append(read)
    index = {read.identity: read for read in entries if read.identity}
    roots = [read for read in live if read.parent is None or read.parent not in index]
    return Store(index, children, roots, sessions)


def window(root: Path, tag: str, full: bool = False) -> str:
    """What the agent reads before placing a message: the session's position and what is near it.

    It prints position, never relevance — it has no idea what the message says. The rendering is
    the one the window test in the mechanism's evidence measured, with each line's state and lean
    added; a change to it reruns that test.

    Every window drawn stays in the conversation, so one is drawn only when something moved: when
    neither this session's position nor any entry changed since the last one, a single line says
    so (parent decision 44). Another session's position alone is not a change.
    """
    if not (root / STORE).is_dir():
        return f"no store at {STORE}/: nothing to place a message in yet"
    seen: dict[str, bytes] = {}
    store = read_store(root, seen)
    held = store.session(tag)
    fingerprint = _fingerprint(held, seen)
    memory = _memory(root, tag)
    if not full and memory.is_file() and memory.read_text(encoding="utf-8") == fingerprint:
        return (
            f"window unchanged since your last one: {held.tag} at {held.current or 'no position yet'}; "
            f"`questions.py --window --session {held.tag} --full` draws it again"
        )
    drawn = _drawn(store, held)
    memory.parent.mkdir(parents=True, exist_ok=True)
    memory.write_text(fingerprint, encoding="utf-8")
    return drawn


def _drawn(store: Store, held: Session) -> str:
    if held.current is None or held.current not in store.index:
        return _without_position(store, held)
    path = store.path(held.current)
    return "\n".join(
        [f"session: {held.tag}", f"current: {held.current}", ""]
        + _path_lines(path)
        + _frontier_lines(store, path)
        + _root_lines(store, path)
        + _elsewhere_lines(store, held)
    )


# --- the wake -----------------------------------------------------------------------------------


def wake(root: Path, today: date, tag: str | None = None) -> str:
    """Where the work stands when a session starts: who else is where, what waits to be re-read,
    and the window this session opens on.

    Called without a tag it registers a new session and draws the window of a session with no
    position yet. Called with the tag of a registered one it registers nothing, so `/recall` asked
    mid-session reads the same as at the start without giving one conversation two sessions.
    """
    if tag is None:
        held = _register(root, today)
        return _wake_read(root, held, f"session: {held.tag}, registered now")
    held = read_store(root).session(tag)
    return _wake_read(root, held, f"session: {held.tag}, already registered")


def _wake_read(root: Path, held: Session, header: str) -> str:
    """Who else is where, what waits to be re-read, and this session's window drawn whole."""
    store = read_store(root)
    live = sorted((read for read in store.index.values() if not read.archived), key=_order)
    others = [other for other in store.sessions if other.tag != held.tag]
    deferred = [read for read in live if read.kind == "deferred" and "answer" in read.parts]
    return "\n".join(
        [header, ""]
        + _section("sessions:", [f"  {_session_state(other)}" for other in others])
        + _section(
            "deferred, to re-check whether each condition is met:",
            [f"  {_line(read)} — {read.parts['answer'].value}" for read in deferred],
        )
        + _section("suspect, to re-read:", [f"  {_line(read)}" for read in live if read.suspect])
        + [window(root, held.tag, full=True)]
    )


def _register(root: Path, today: date, tag: str | None = None) -> Session:
    """A new session's line, running and with no position yet, under the host's own session id
    where a hook gave one, or else a tag minted here that no session holds."""
    if tag is None:
        taken = {held.tag for held in _sessions(root)[0]}
        tag = f"s-{today:%m%d}-{secrets.token_hex(2)}"
        while tag in taken:
            tag = f"s-{today:%m%d}-{secrets.token_hex(2)}"
    held = Session(tag, True, today, None, [], 0)
    _write_own_line(root, held)
    return held


# --- the hooks ----------------------------------------------------------------------------------


@dataclass(frozen=True)
class Host:
    """What one host's hooks send and expect: everything host-specific about delivery is here.

    Read from each host's hook documentation (parent decision 44); a row is documented, not
    observed, until a live session in that host shows it.
    """

    session_field: str
    starts: str
    messages: str | None
    compactions: tuple[str, ...]
    answer: Callable[[str, str], str]
    quiet: str


def _hook_specific(event: str, context: str) -> str:
    return json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": context}})


HOSTS = {
    "claude-code": Host("session_id", "SessionStart", "UserPromptSubmit", (), _hook_specific, ""),
    "codex": Host("session_id", "SessionStart", "UserPromptSubmit", ("PostCompact",), _hook_specific, ""),
    # Cursor's prompt hook can only allow or block, so its agent draws the window by the rule.
    "cursor": Host(
        "conversation_id",
        "sessionStart",
        None,
        ("preCompact",),
        lambda event, context: json.dumps({"additional_context": context}),
        "{}",
    ),
}


def hook(root: Path, host_name: str, payload: str, today: date) -> str:
    """What a host's hook prints: the wake's read when a session starts, the window before a
    message, nothing after a compaction but a forgotten window.

    It never fails the host. A prompt hook that fails can hold back the person's message, so any
    problem is answered as one line of context that names it, and the exit status stays 0. Once the
    host and the event are known, the notice goes out in that host's own form, since a host that
    reads its hook's answer as JSON would drop plain text.
    """
    host = HOSTS.get(host_name)
    event: str | None = None
    try:
        if host is None:
            raise Refused(f"no host `{host_name}`; the hosts are {', '.join(HOSTS)}")
        sent = json.loads(payload)
        event = sent.get("hook_event_name")
        tag = _tag(str(sent.get(host.session_field) or ""))
        if event in host.compactions:
            _forget_window(root, tag)
            return host.quiet
        if event == host.starts:
            return host.answer(event, _started(root, tag, sent.get("source"), today))
        if event == host.messages:
            if tag not in {held.tag for held in _sessions(root)[0]}:
                # The start was never seen — the hooks arrived mid-session — so this is the start.
                return host.answer(event, _started(root, tag, None, today))
            return host.answer(event, window(root, tag))
        return ""
    except Exception as problem:  # noqa: BLE001 — the boundary to a host: nothing may escape it
        notice = f"questions hook: {problem}"
        if host is not None and event in (host.starts, host.messages):
            return host.answer(event, notice)
        return notice


def _started(root: Path, tag: str, source: str | None, today: date) -> str:
    """A session starting, resuming or compacted: registered once under the host's id, running
    again if it had ended, and given a whole window, since its context has none."""
    _forget_window(root, tag)
    known = {held.tag: held for held in _sessions(root)[0]}
    if tag not in known:
        held = _register(root, today, tag)
        return _wake_read(root, held, f"session: {tag}, registered now")
    held = known[tag]
    if not held.running:
        held = Session(held.tag, True, today, held.current, held.recent, held.line)
        _write_own_line(root, held)
    if source == "compact":
        return window(root, tag, full=True)
    return _wake_read(root, held, f"session: {tag}, already registered")


def _tag(identity: str) -> str:
    """A host's session id as a session tag: the characters a sessions line holds, no others."""
    tag = re.sub(r"[^\w.-]", "-", identity.strip())
    if not tag:
        raise Refused("the hook's input names no session")
    return tag if tag[0].isalnum() else f"s{tag}"


def end(root: Path, tag: str, today: date) -> Session:
    """The conclude's last act: the session is marked ended and keeps its position, so a later
    wake can offer to resume where it stopped."""
    held = read_store(root).session(tag)
    ended = Session(held.tag, False, today, held.current, held.recent, held.line)
    _write_own_line(root, ended)
    return ended


def _session_state(held: Session) -> str:
    state = "running" if held.running else "ended"
    recent = f" (recent {', '.join(held.recent)})" if held.recent else ""
    return f"{held.tag} {state}, last wrote {held.wrote}, at {held.current or 'no position yet'}{recent}"


# --- the tree -----------------------------------------------------------------------------------


def tree(root: Path, identity: str | None = None) -> str:
    """The live tree, whole or under one question: the index derived from the parent lines, for a
    person, rendered at every call and never committed (parent decision 34)."""
    if not (root / STORE).is_dir():
        return f"no store at {STORE}/"
    store = read_store(root)
    if identity is None:
        tops = store.roots
    else:
        top = store.index.get(identity)
        if top is None or top.archived:
            raise Refused(f"no live entry holds {identity}")
        tops = [top]
    lines: list[str] = []

    def draw(read: Entry, depth: int) -> None:
        lines.append(f"{'  ' * depth}{_line(read)}")
        for child in store.children.get(read.identity or "", []):
            draw(child, depth + 1)

    for top in tops:
        draw(top, 0)
    return "\n".join(lines)


def _fingerprint(held: Session, seen: dict[str, bytes]) -> str:
    """What a window was drawn from: this session's position and every entry's bytes."""
    digest = hashlib.sha256(f"{held.current}\n".encode())
    for name in sorted(seen):
        digest.update(name.encode() + b"\0" + seen[name] + b"\0")
    return digest.hexdigest()


def _memory(root: Path, tag: str) -> Path:
    """Where the fingerprint of a session's last window is kept: outside the tree, so it never
    churns the store, keyed by tree and session."""
    tree = hashlib.sha256(str(root.resolve()).encode()).hexdigest()[:16]
    return Path(WINDOW_MEMORY or Path(tempfile.gettempdir()) / "questions-windows") / tree / tag


def _forget_window(root: Path, tag: str) -> None:
    """After a compaction the last window is gone from the conversation, so the next is whole."""
    _memory(root, tag).unlink(missing_ok=True)


def _path_lines(path: list[Entry]) -> list[str]:
    lines = ["path (root to current):"]
    for depth, read in enumerate(path):
        marker = "  <- current" if read is path[-1] else ""
        lines.append(f"  {'  ' * depth}{_line(read)}{marker}")
    return lines + [""]


def _frontier_lines(store: Store, path: list[Entry]) -> list[str]:
    """Every child of every question on the path. A closed one is shown with its kind, so that a
    question asked again is seen as a reopening, and a deferral can be told from drift."""
    frontier = [
        f"  under {read.identity}: {_line(child)}"
        for read in path
        for child in store.children.get(read.identity or "", [])
        if child not in path
    ]
    return _section("frontier (children of each question on the path):", frontier)


def _root_lines(store: Store, path: list[Entry]) -> list[str]:
    """The open questions of the current root, and its suspect entries wherever they sit in it:
    open questions are bounded by attention within a root, closed ones are not."""
    root = path[0]
    below = store.under(root.identity or "")
    shown = path + [child for read in path for child in store.children.get(read.identity or "", [])]
    return (
        _section(
            f"open questions under this root ({root.identity}), with their parent:",
            [
                f"  {read.identity} (parent {read.parent}) {read.question}{_lean(read)}"
                for read in below
                if read.open
            ],
        )
        + _section(
            "suspect under this root:",
            [f"  {_line(read)}" for read in below if read.suspect and read not in shown],
        )
        + _section("other roots:", [f"  {_line(other)}" for other in store.roots if other is not root])
    )


def _elsewhere_lines(store: Store, held: Session) -> list[str]:
    others = [
        f"  {other.tag} at {other.current or 'no position yet'} (last wrote {other.wrote})"
        for other in store.sessions
        if other.running and other.tag != held.tag
    ]
    return _section("other running sessions:", others) + [
        f"recently attached: {', '.join(held.recent) or 'none'}",
        f"next free id: {store.next_free}",
    ]


def _without_position(store: Store, held: Session) -> str:
    """A session that has not placed itself yet: the roots to place it among, and who is where."""
    return "\n".join(
        [f"session: {held.tag}", "current: none yet — the first declared `at` places it", ""]
        + _section("roots:", [f"  {_line(read)}" for read in store.roots])
        + _elsewhere_lines(store, held)
    )


def _line(read: Entry) -> str:
    return f"{read.identity} [{read.parts['state'].value}] {read.question}{_lean(read)}"


def _lean(read: Entry) -> str:
    lean = read.parts.get("lean")
    return f"  ~ {lean.value}" if lean else ""


def _section(heading: str, lines: list[str]) -> list[str]:
    """A heading, its lines, and the blank line that ends it. A heading with nothing under it says
    so, so an empty section is not read as a missing one."""
    return [heading] + (lines or ["  (none)"]) + [""]


def _order(read: Entry) -> int:
    return int((read.identity or "q-0")[2:])


# --- the writer ---------------------------------------------------------------------------------


@dataclass(frozen=True)
class Clause:
    """One event of a declared line, as the writer applies it.

    The parser makes these from a line; a judge's typed value will be turned into the same list
    without parsing (parent decision 39), so the writer has one front door for both.
    """

    verb: str
    question: str | None = None
    other: str | None = None
    lower: str | None = None
    text: str | None = None


_ID = r"(q-\d{4,})"
# A record named by its id, `01-0011.0100` of a ticket's file name, is labelled by that id alone.
_RECORD_ID = re.compile(r"^\d{2}-\d{4}(?:\.\d{4})*")
_CLAUSES = (
    ("at", re.compile(rf"^at {_ID}$")),
    ("opens", re.compile(rf"^opens {_ID}(?: under {_ID}| between {_ID} and {_ID})?: (.+)$")),
    ("moves", re.compile(rf"^moves {_ID} (?:under {_ID}|to root)$")),
    ("depends", re.compile(rf"^depends {_ID} on {_ID}$")),
    ("closes", re.compile(rf"^closes {_ID}: ({'|'.join(KINDS)})(?:, (.+))?$")),
    ("suspects", re.compile(rf"^suspects {_ID}$")),
    ("clears", re.compile(rf"^clears {_ID}$")),
    ("leans", re.compile(rf"^leans {_ID}: (.+)$")),
    ("assigns", re.compile(rf"^assigns {_ID} to (.+)$")),
)


def parse(line: str) -> list[Clause]:
    """A declared line as clauses, in the order written; `nothing` alone is a turn that placed
    nothing. Free text may not hold `;`, since `; ` is what separates clauses."""
    if line.strip() == "nothing":
        return [Clause("nothing")]
    clauses = []
    for written in line.strip().split("; "):
        if ";" in written:
            raise Refused(f"`{written}` holds a `;`, which free text in a declared line may not")
        clauses.append(_clause(written))
    placed = [clause for clause in clauses if clause.verb == "at"]
    if len(placed) != 1:
        raise Refused("a declared line names its session's position with exactly one `at`, or is `nothing`")
    return clauses


def _clause(written: str) -> Clause:
    for verb, grammar in _CLAUSES:
        said = grammar.match(written)
        if said is None:
            continue
        groups = said.groups()
        if verb == "opens":
            return Clause(verb, groups[0], groups[1] or groups[2], groups[3], groups[4])
        if verb == "closes":
            return Clause(verb, groups[0], groups[1], text=groups[2])
        if verb in ("leans", "assigns"):
            return Clause(verb, groups[0], text=groups[1])
        return Clause(verb, *groups)
    raise Refused(f"`{written}` is not a clause of the declared line; the clauses are:\n{FORMS}")


# The declared line's clauses, printed with a refusal so a malformed line is fixed in the same turn.
FORMS = "\n".join(
    f"  {form}"
    for form in (
        "at q-N                                   (required, once, unless the line is `nothing`)",
        "opens q-N: <question>                    (a root; q-N is the next free id)",
        "opens q-N under q-P: <question>",
        "opens q-N between q-U and q-L: <question>",
        "moves q-K under q-P  |  moves q-K to root",
        "depends q-A on q-B",
        "closes q-N: decided, [link](path) — who, date",
        "closes q-N: deferred, until <condition>, meanwhile <default>",
        "closes q-N: merged, q-M  |  closes q-N: superseded, q-M",
        "closes q-N: pruned, <reason>  |  closes q-N: moot, <reason>",
        "suspects q-N  |  clears q-N  |  leans q-N: <line>  |  assigns q-N to <path>",
        "nothing",
    )
) + "\nclauses are separated by `; `, and free text may not hold `;`"


@dataclass
class Written:
    """What one declaration wrote, in the order it was written."""

    entries: list[str]
    session: Session | None


def declare(
    root: Path,
    tag: str,
    clauses: list[Clause],
    today: date,
    between: Callable[[], None] | None = None,
) -> Written:
    """Apply a declared line's clauses in order to the store, validate the result whole, then
    write the entries it changed and the session's line last.

    Nothing is written unless everything validates. Just before writing, every entry file the
    line changes is read again, and one that moved since it was read refuses the line: detected
    interference is a failure, never authority to overwrite. The sessions file is the exception,
    since each session replaces only its own line there. `between` runs after validation and
    before that last read — the moment another writer may act.
    """
    seen: dict[str, bytes] = {}
    entries, _, _ = _entries(root, seen)
    held = read_store(root).session(tag)
    draft = _Draft(root, {read.identity: read for read in entries if read.identity})
    for clause in clauses:
        draft.apply(clause)
    position = next((clause.question for clause in clauses if clause.verb == "at"), None)
    if position is not None:
        draft.place(position)
    if between is not None:
        between()
    draft.recheck(seen)
    written = draft.write()
    moved = _moved(held, position, today)
    if moved is not None:
        try:
            _write_own_line(root, moved)
        except OSError as error:
            raise WriteInterrupted(written, SESSIONS, error) from error
    return Written(written, moved)


def _moved(held: Session, position: str | None, today: date) -> Session | None:
    """The session's line after an `at`: the old position joins the recent ones, at most four."""
    if position is None:
        return None
    recent = [held.current] if held.current and held.current != position else []
    recent += [identity for identity in held.recent if identity != position and identity not in recent]
    return Session(held.tag, True, today, position, recent[:4], held.line)


class _Draft:
    """The store as a declared line leaves it, held in memory until the whole line validates."""

    def __init__(self, root: Path, index: dict[str, Entry]) -> None:
        self.root = root
        self.index = dict(index)
        self.changed: list[str] = []
        self.new: set[str] = set()

    def apply(self, clause: Clause) -> None:
        getattr(self, f"_{clause.verb}")(clause)

    def place(self, identity: str) -> None:
        read = self._existing(identity)
        if not read.open:
            state = read.parts["state"].value
            raise Refused(f"`at {identity}`: {identity} is {state}; a position is an open question")

    def _at(self, clause: Clause) -> None:
        """Checked once the whole line has applied, by `place`."""

    def _opens(self, clause: Clause) -> None:
        identity = clause.question or ""
        expected = _next_free(self.index)
        if identity != expected:
            raise Refused(f"`opens {identity}`: the next free id is {expected}")
        parts = {"state": "open"}
        if clause.other:
            self._existing(clause.other)
            parts = {"part of": clause.other} | parts
        record = f"{STORE}/{identity}-{_slug(clause.text or '')}.md"
        self._put(Entry(record, identity, clause.text or "", {n: Part(v, 0) for n, v in parts.items()}))
        self.new.add(identity)
        if clause.lower:
            lower = self._existing(clause.lower)
            if lower.parent != clause.other:
                raise Refused(
                    f"`opens {identity} between {clause.other} and {clause.lower}`: {clause.lower} is not "
                    f"part of {clause.other}"
                )
            self._put(_with(lower, **{"part of": identity}))

    def _moves(self, clause: Clause) -> None:
        moving = self._existing(clause.question or "")
        if clause.other is not None:
            self._existing(clause.other)
            if moving in _ancestry(self.index, clause.other):
                raise Refused(f"`moves {moving.identity} under {clause.other}` makes a cycle in part of")
        self._put(_with(moving, **{"part of": clause.other}))

    def _depends(self, clause: Clause) -> None:
        waiting, awaited = self._existing(clause.question or ""), self._existing(clause.other or "")
        if waiting.identity in self._awaited_by(awaited.identity or ""):
            raise Refused(f"`depends {waiting.identity} on {awaited.identity}` makes a cycle in depends on")
        if awaited.identity not in waiting.dependencies:
            listed = ", ".join(waiting.dependencies + [awaited.identity or ""])
            self._put(_with(waiting, **{"depends on": listed}))

    def _closes(self, clause: Clause) -> None:
        """A question closes only by a recorded kind with its pointer (parent decision 35); a prune
        leaves no open question under it, so the ones that stand alone are moved out first."""
        closing = self._existing(clause.question or "")
        kind = clause.other or ""
        if kind == "pruned":
            left = [
                read.identity for read in self.index.values() if read.parent == closing.identity and read.open
            ]
            if left:
                raise Refused(
                    f"`closes {closing.identity}: pruned` leaves {', '.join(left)} open under it; move out "
                    "the ones that stand alone and close the rest first"
                )
        state = f"closed:{kind}" + (", suspect" if closing.suspect else "")
        closed = _with(closing, state=state, answer=clause.text)
        problems = _answer_problems(self.root, closed)
        if problems:
            raise Refused(f"`closes {closing.identity}: {kind}`: {problems[0].problem}")
        if closed.points_to:
            self._existing(closed.points_to)
        self._put(closed)

    def _suspects(self, clause: Clause) -> None:
        read = self._existing(clause.question or "")
        self._put(_with(read, state=f"{read.state.group(1) if read.state else 'open'}, suspect"))

    def _clears(self, clause: Clause) -> None:
        read = self._existing(clause.question or "")
        self._put(_with(read, state=read.state.group(1) if read.state else "open"))

    def _leans(self, clause: Clause) -> None:
        self._put(_with(self._existing(clause.question or ""), lean=clause.text))

    def _assigns(self, clause: Clause) -> None:
        """The owner is the record holding the deliberation, written as a link from the entry, so
        the mover repairs it when either one moves."""
        read = self._existing(clause.question or "")
        owner = (clause.text or "").strip()
        if not (self.root / owner).is_file():
            raise Refused(f"`assigns {read.identity} to {owner}`: no file {owner} in this tree")
        name = posixpath.splitext(posixpath.basename(owner))[0]
        label = _RECORD_ID.match(name)
        link = posixpath.relpath(owner, posixpath.dirname(read.record))
        self._put(_with(read, owner=f"[{label.group(0) if label else name}]({link})"))

    def _nothing(self, clause: Clause) -> None:
        """A turn that placed nothing writes nothing."""

    def _awaited_by(self, identity: str) -> set[str]:
        """Every question this one waits on, directly or through another."""
        found: set[str] = set()
        waiting = [identity]
        while waiting:
            for awaited in self.index[waiting.pop()].dependencies:
                if awaited not in found and awaited in self.index:
                    found.add(awaited)
                    waiting.append(awaited)
        return found

    def _existing(self, identity: str) -> Entry:
        read = self.index.get(identity)
        if read is None:
            raise Refused(f"no entry holds {identity}")
        return read

    def _put(self, read: Entry) -> None:
        self.index[read.identity or ""] = read
        if read.identity not in self.changed:
            self.changed.append(read.identity or "")

    def recheck(self, seen: dict[str, bytes]) -> None:
        """Every entry this line changes is as it was read, and every id it opens is still free —
        under any slug, since another session names its question in its own words."""
        for identity in self.changed:
            record = self.index[identity].record
            if identity in self.new:
                if _files_holding(self.root, identity):
                    raise Refused(
                        f"{identity} was written by another session since this line was read; declare "
                        "it again with the next free id"
                    )
                continue
            now = (self.root / record).read_bytes() if (self.root / record).is_file() else None
            if now != seen.get(record):
                raise Refused(f"{record} changed since this line was read; read it again and declare anew")

    def write(self) -> list[str]:
        """The changed entries, in the order the line changed them. A failure stops the run and
        says what was written: nothing is rolled back."""
        written: list[str] = []
        for identity in self.changed:
            read = self.index[identity]
            try:
                path = self.root / read.record
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(_entry_text(read), encoding="utf-8", newline="\n")
            except OSError as error:
                raise WriteInterrupted(written, read.record, error) from error
            written.append(read.record)
        return written


class WriteInterrupted(Exception):
    """A write that failed after another had succeeded. Nothing was rolled back; `completed` is
    what was written and `failed` where it stopped."""

    def __init__(self, completed: list[str], failed: str, error: OSError) -> None:
        super().__init__(f"writing {failed} failed: {error}")
        self.completed = completed
        self.failed = failed


def _files_holding(root: Path, identity: str) -> list[Path]:
    return [
        path
        for folder in (root / STORE, root / STORE / "done")
        if folder.is_dir()
        for path in folder.glob(f"{identity}-*.md")
    ]


def _with(read: Entry, **changes: str | None) -> Entry:
    """The same entry with some parts replaced; a part given as `None` is removed."""
    parts = dict(read.parts)
    for name, value in changes.items():
        name = name.replace("_", " ")
        if value is None:
            parts.pop(name, None)
        else:
            parts[name] = Part(value, 0)
    return Entry(read.record, read.identity, read.question, parts)


def _entry_text(read: Entry) -> str:
    bullets = [f"- **{name}** {read.parts[name].value}" for name in PARTS if name in read.parts]
    return "\n".join([f"# {read.identity} {read.question}", "", *bullets]) + "\n"


def _slug(question: str) -> str:
    """Every word of the question, cut at a word boundary only past `SLUG_LENGTH` characters, so a
    person reading a listing reads the whole question (parent decision 55)."""
    slug: list[str] = []
    for word in _words(question):
        if slug and len("-".join(slug + [word])) > SLUG_LENGTH:
            break
        slug.append(word)
    return "-".join(slug) or "question"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
