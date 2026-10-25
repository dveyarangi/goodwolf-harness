# Mechanism: questions
"""The open questions of the tree, kept in one store, and whether the store keeps its shape.

    uv run --offline --no-project python .agents/scripts/gw/questions.py --check
    uv run --offline --no-project python .agents/scripts/gw/questions.py --window --session <tag>
    uv run --offline --no-project python .agents/scripts/gw/questions.py --wake [--session <tag>]
    uv run --offline --no-project python .agents/scripts/gw/questions.py --tree [<q-id>]
    uv run --offline --no-project python .agents/scripts/gw/questions.py --path
    uv run --offline --no-project python .agents/scripts/gw/questions.py --seed
    uv run --offline --no-project python .agents/scripts/gw/questions.py <event> ... --session <tag>

The store is `docs/questions/`: one file per question, its id nested under its parent's and its
parent line the one the check holds that id against, wholly closed subtrees in
`docs/questions/done/`. Each session's position is its row, the session mechanism's, kept by
`sessions.py`, which this script imports for every window and wake. A re-parent renames the
subtree that moves, across the records under `docs/` (the user, 2026-10-03). The formats are the
questions skill's.

`--check` is the maintainer. It writes nothing; its exit status is the verdict and its JSON is for
the person reading a failure. A tree with no store has nothing to check and passes. `--window` is
what the agent reads before placing a message; `--wake` registers a session, ends every other gone
silent, and reads where the work stands; `--tree` draws the live tree for a person; `--path` reads the path ahead, which the wake carries; `--seed`
opens the roots of a store that holds no entry, as the install does, and is how a person resumes
an install that stopped there. Each
event of a turn is its own call — `at`, `open`, `move`, `depend`, `undepend`, `close`, `suspect`,
`clear`, `lean`, `assign`, `realize`, `rung` — validated and written whole (parent decision 56); `--help`
after any of them says what it takes.

`realizes` answers what a question realizes, for whichever mechanism keeps the answers: the store
keeps the trace link as written and never resolves it (the user, 2026-10-13).
"""

from __future__ import annotations

import argparse
import codecs
import hashlib
import json
import os
import posixpath
import re
import sys
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import move_doc  # noqa: E402  (path set above)
import sessions  # noqa: E402  (path set above)
from docs_corpus import (  # noqa: E402  (path set above)
    STRAW_DOG_SCOPE,
    bindings_in,
    cited_record,
    citations,
    corpus,
    in_straw_dog_scope,
    question_bindings,
    read_text,
    target_of,
    with_question_bindings_retargeted,
)

STORE = "docs/questions"
# The questions mechanism's shelf of the words a fresh store opens with; this script reads it and
# the installer holds none of it (the user, 2026-10-09).
STORE_ARRIVAL = ".agents/skills/questions/STORE-ARRIVAL.md"
# The mechanism's hook wiring, one file per host file at that file's own path beneath this
# directory; the installer merges each into the host file it names and holds no path of its own.
HOOKS = ".agents/skills/questions/hooks/"
# A held question reached again at least this long after it was opened or last struck is struck
# (parent decision 53); a constant until a project wants another.
STRIKE_AFTER = timedelta(hours=12)
# How many of the most-struck open questions the wake's read lists first (parent decision 54).
WAKE_STRUCK_LINES = 5
# A twin shares at least this many content words, and at least half of the shorter title's.
TWIN_SHARED_WORDS = 3
SLUG_LENGTH = 160
# The longest absolute path an entry may take: Windows' limit less its terminating null.
PATH_LIMIT = 259
# The highest four-digit position a child takes; a root's id may grow a digit, as it always could.
LAST_POSITION = 9999
PARTS = ("record of", "part of", "depends on", "state", "owner", "answer", "realizes", "rung", "lean", "struck")
# A trace link names each answer by its reference and its name, as a ticket is named by id and
# slug, or states that the question realizes none (the user, 2026-10-13).
DERIVED = "derived"
# An entry carries what it is a record of as its first part, so the agent writing its body meets
# the kind in context (the user, 2026-10-08): what it intends to become while open, what happened
# once closed. The writer writes it from the state on every write; `kind` was the mark's earlier name.
MARK = "record of"
FORMER_MARK = "kind"
OPEN_KIND = "what it intends to become"
CLOSED_KIND = "what happened"
KINDS = ("decided", "pruned", "merged", "deferred", "moot", "superseded")
# The body's list a decision waits in until it has a home, and the arrow its home follows; no
# home is in the store, a ticket or an RFC (the user, 2026-10-11).
DECISIONS = "## Decisions"
# The body's opening part: the question as it stands, which a question a ticket answers carries
# (the user, 2026-10-15).
WHERE_IT_STANDS = "## Where it stands"
ARROW = "→"
NOT_HOMES = (f"{STORE}/", "docs/tickets/", "docs/rfc/")
_USAGE = (
    "usage: questions.py --check | --window --session <tag> | --wake [--session <tag>] | --path "
    "| --tree [<q-id>] | --seed | <event> ... --session <tag>, the events "
    "at, open, move, reword, depend, undepend, close, suspect, clear, lean, assign, realize, rung"
)
# How many times an `open` takes the next free id again when another session took the one it drew.
OPEN_ATTEMPTS = 3
_STOPWORDS = frozenset(
    "a an and are as at be by can do does for from how in is it of on or should the this to we "
    "what when where whether which who why will with".split()
)
# An id says where its question sits: a root's position, then one four-digit position per level
# below it, as a ticket's id nests (the user, 2026-10-03).
_ID = r"q-\d{4,}(?:\.\d{4})*"
_TITLE = re.compile(rf"^# ({_ID}) (\S.*)$")
_BULLET = re.compile(r"^- \*\*([^*]+)\*\* ?(.*)$")
_CONTINUATION = re.compile(r"^\s+\S")
_STATE = re.compile(rf"^(open|closed:({'|'.join(KINDS)}))(, suspect)?$")
_IDENTITY = re.compile(rf"^{_ID}$")
_ENTRY_NAME = re.compile(rf"^{STORE}/(?:done/)?({_ID})-([a-z0-9]+(?:-[a-z0-9]+)*)\.md$")
_DEFERRAL = re.compile(r"^until \S.*, meanwhile \S.*$")
_STRIKE = re.compile(r"^(\d+), last (\d{4}-\d{2}-\d{2}T\d{2}:\d{2})Z$")
_ANSWER_NAMED = r'([A-Za-z0-9][A-Za-z0-9._-]*) "(\S(?:[^"]*\S)?)"'
_TRACE_LINK = re.compile(rf"^{_ANSWER_NAMED}(?:, *{_ANSWER_NAMED})*$")
# A question's highest rung on each ladder it touches, `<ladder>: <rung>` (the user, 2026-10-15).
_RUNG_NAMED = r"([a-z][a-z-]*): ([a-z][a-z' -]*[a-z])"
_RUNG = re.compile(rf"^{_RUNG_NAMED}(?:, {_RUNG_NAMED})*$")
# An owner as `assign` writes it: a markdown link, its label the record's id.
_LINK_LABEL = re.compile(r"^\[([^\]]+)\]")
_LINK_TARGET = re.compile(r"\]\(([^)\s]+)\)")
# An id in prose: never part of a word or a longer id, so `faq-0007` and `q-00070` are not ids.
_BARE_ID = re.compile(rf"(?<![\w.]){_ID}(?!\w)")
_HEADING = re.compile(r"^#{1,6} +(.*?)(?: +#+)? *$")
# A relative id — `.0003` standing for q-0037.0006.0020.0001.0003 — names nothing a reader can follow;
# an id in an entry is written whole (rule failure 17, struck 2026-10-23).
_RELATIVE_ID = re.compile(r"(?<![\w.])\.\d{4}(?!\d)")
_FENCE = re.compile(r"^\s*(```|~~~)")
_ITEM = re.compile(r"^(?:-|\d+\.) +(\S.*)$")
_ROOTS_BLOCK = re.compile(r"^```roots\n(?P<said>.*?)^```", re.MULTILINE | re.DOTALL)


@dataclass(frozen=True)
class Part:
    """One bullet of an entry, its continuation lines joined, and the line it starts on."""

    value: str
    line: int


@dataclass(frozen=True)
class Entry:
    """One question as its file says it. Nothing here has been judged yet.

    `body` is the argument after the parts, written by hand and kept as read: the script writes
    the parts and never the body (the user, 2026-10-03)."""

    record: str
    identity: str | None
    question: str
    parts: dict[str, Part]
    body: str = ""

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

    @property
    def trace_link(self) -> TraceLink | None:
        """The trace link it writes itself, or `None` when it writes none or its form cannot be read;
        what it realizes through an ancestor is `realizes`'s."""
        said = self.parts.get("realizes")
        return _trace_link(said.value) if said else None

    @property
    def strike(self) -> Strike | None:
        """Its strike count and last stamp, or `None` when it has none or its form cannot be read."""
        said = self.parts.get("struck")
        written = _STRIKE.match(said.value) if said else None
        if written is None:
            return None
        try:
            last = datetime.strptime(written.group(2), "%Y-%m-%dT%H:%M").replace(tzinfo=timezone.utc)
        except ValueError:
            return None
        return Strike(int(written.group(1)), last)


@dataclass(frozen=True)
class Strike:
    """How often a held question was reached again after a delay, and when it was last stamped:
    at its opening, at its first reach if it predates the count, or at its last strike."""

    count: int
    last: datetime

    @property
    def text(self) -> str:
        return f"{self.count}, last {self.last:%Y-%m-%dT%H:%M}Z"


@dataclass(frozen=True)
class TraceLink:
    """The answers a question realizes, each a reference and its name as the link quotes them, or
    none, by its statement that it is derived. Neither is resolved here."""

    answers: tuple[tuple[str, str], ...]
    derived: bool = False


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


def main(
    argv: list[str], root: Path, today: date | None = None, now: datetime | None = None
) -> int:
    today = today or date.today()
    now = now or datetime.now(timezone.utc)
    # A title may hold any character, and a Windows console's default encoding holds few of them:
    # printed as-is, one arrow in a question would end the run with nothing shown.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        if argv[:1] and argv[0] in EVENTS:
            return _called(root, argv, today, now)
        if argv == ["--check"]:
            checked = check(root)
            print(json.dumps(checked.as_record(), indent=2))
            return 1 if checked.diagnostics or checked.skipped else 0
        if len(argv) in (3, 4) and argv[:2] == ["--window", "--session"] and argv[3:] in ([], ["--full"]):
            print(window(root, argv[2], full=argv[3:] == ["--full"]))
            sessions.seen(root, argv[2], now)
            return 0
        if len(argv) == 2 and argv[0] == "--hook":
            print(hook(root, argv[1], _hook_input(), now))
            return 0
        if argv == ["--wake"] or (len(argv) == 3 and argv[:2] == ["--wake", "--session"]):
            print(wake(root, now, argv[2] if len(argv) == 3 else None))
            return 0
        if argv == ["--path"]:
            print(path_ahead(root, now))
            return 0
        if argv[:1] == ["--tree"] and len(argv) <= 2:
            print(tree(root, argv[1] if len(argv) == 2 else None))
            return 0
        if argv == ["--seed"]:
            written = seed(root, now)
            for record in written:
                print(f"wrote {record}")
            if not written:
                print(f"{STORE} holds entries; left as it stands")
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


def check(root: Path) -> Checked:
    """Every entry, live and archived, and the sessions' rows against the store's shape; then what
    a person should look at in a store that keeps it."""
    if not (root / STORE).is_dir():
        return Checked(False, 0, [], [], [])
    entries, diagnostics, skipped = _entries(root)
    diagnostics += [note for read in entries for note in _answer_problems(root, read)]
    diagnostics += _waiting_problems(root, entries)
    index = {read.identity: read for read in entries if read.identity}
    row_problems, row_findings, unreadable = sessions.check(root, index)
    diagnostics += _identity_problems(entries) + _relation_problems(entries, index) + row_problems
    findings = (
        row_findings
        + _likely_twins(entries)
        + _ready_for_done(entries, index)
        + _unstated(entries, index)
        + _unrunged(entries)
        + _relative_ids(root, entries)
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
        diagnostics += problems + _name_problems(root, read, stem)
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
    not hide the others behind it. The parts end at the first blank line after one; what follows is
    the body, never read for parts, so a line in an argument that looks like a part is not one.
    """
    lines = text.splitlines()
    problems: list[Diagnostic] = []
    title = _TITLE.match(lines[0]) if lines else None
    if title is None:
        problems.append(Diagnostic(name, 1, "does not open with a title line `# q-NNNN <question>`"))
    parts: dict[str, Part] = {}
    last: str | None = None
    body = ""
    carries_former_mark = False
    for number, line in enumerate(lines[1:], start=2):
        if last is not None and not line.strip():
            body = "".join(text.splitlines(keepends=True)[number:])
            break
        bullet = _BULLET.match(line)
        if bullet:
            last = bullet.group(1).strip()
            if last == FORMER_MARK:
                carries_former_mark = True
                problems.append(
                    Diagnostic(name, number, f"carries its kind as `- **{FORMER_MARK}**`: the part is `{MARK}`")
                )
            elif last not in PARTS:
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
    read = Entry(name, title.group(1) if title else None, title.group(2) if title else "", parts, body)
    return read, (
        problems
        + _state_problems(read)
        + ([] if carries_former_mark else _mark_problems(read))
        + _relation_form_problems(read)
        + _trace_link_problems(read)
        + _rung_problems(read)
        + _strike_problems(read)
    )


def _kind(read: Entry) -> str | None:
    """What the entry is a record of, by its state; `None` where the state cannot be read."""
    if read.state is None:
        return None
    return OPEN_KIND if read.open else CLOSED_KIND


def _mark_problems(read: Entry) -> list[Diagnostic]:
    """The mark held equal to the kind the entry's state calls for. An unreadable state is
    reported as itself, so no kind is asked of it."""
    expected = _kind(read)
    carried = read.parts.get(MARK)
    if expected is None or (carried and carried.value == expected):
        return []
    if carried is None:
        return [Diagnostic(read.record, 1, f"names no kind: its parts open with `- **{MARK}** {expected}`")]
    said = "an open entry" if read.open else "a closed entry"
    return [Diagnostic(read.record, carried.line, f"is marked {carried.value}, and {said} is {expected}")]


def _ids(value: str) -> list[str] | None:
    """A comma-separated list of ids, or `None` where anything else is written."""
    written = [item.strip() for item in value.split(",")]
    return written if all(_IDENTITY.match(item) for item in written) else None


def _trace_link(value: str) -> TraceLink | None:
    """The trace link a `realizes` part writes, or `None` where its form is anything else: answers
    as `<reference> "<name>"`, comma-separated, each reference once, or `derived` alone."""
    if value == DERIVED:
        return TraceLink((), derived=True)
    if not _TRACE_LINK.match(value):
        return None
    answers = tuple(re.findall(_ANSWER_NAMED, value))
    references = [reference for reference, _ in answers]
    return TraceLink(answers) if len(set(references)) == len(references) else None


def _trace_link_problems(read: Entry) -> list[Diagnostic]:
    """A trace link is optional, since most questions inherit theirs; when written, it reads as
    one."""
    said = read.parts.get("realizes")
    if said is None or _trace_link(said.value) is not None:
        return []
    return [Diagnostic(read.record, said.line, f"realizes is `{said.value}`, {_NOT_A_TRACE_LINK}")]


_NOT_A_TRACE_LINK = 'not a trace link: answers as `<reference> "<name>"`, comma-separated, each once, or `derived`'


def _rung(value: str) -> tuple[tuple[str, str], ...] | None:
    """The rungs a `rung` part writes, `(ladder, rung)` each, or `None` where its form is anything
    else: `<ladder>: <rung>`, comma-separated, each ladder once.

    Only the form is the store's: the rungs' names and their order are each ladder's mechanism's.
    """
    # TODO q-0037.0010.0002.0005: a ladder's rungs are checked by name, and a lowering told, once
    # its mechanism declares them.
    if not _RUNG.match(value):
        return None
    rungs = tuple(re.findall(_RUNG_NAMED, value))
    ladders = [ladder for ladder, _ in rungs]
    return rungs if len(set(ladders)) == len(ladders) else None


def _rung_problems(read: Entry) -> list[Diagnostic]:
    said = read.parts.get("rung")
    if said is None or _rung(said.value) is not None:
        return []
    return [Diagnostic(read.record, said.line, f"rung is `{said.value}`, {_NOT_A_RUNG}")]


_NOT_A_RUNG = "not a rung: `<ladder>: <rung>`, comma-separated, each ladder once"


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


def _strike_problems(read: Entry) -> list[Diagnostic]:
    """A strike is optional, since entries written before the count have none; when written, it
    reads as the writer writes it."""
    said = read.parts.get("struck")
    if said is None or read.strike is not None:
        return []
    return [Diagnostic(read.record, said.line, f"struck is `{said.value}`, not `<n>, last <YYYY-MM-DDTHH:MMZ>`")]


def _name_problems(root: Path, read: Entry, stem: re.Match[str]) -> list[Diagnostic]:
    """The filename's id is the title's, and its slug is the whole question, as the writer names it
    (parent decision 55), so a name shortened or left behind by a reworded question is caught. A
    slug the writer cut so the path fits this tree is the writer's name too."""
    if read.identity is None:
        return []
    if stem.group(1) != read.identity:
        return [
            Diagnostic(read.record, 1, f"is named {stem.group(1)} and its title says {read.identity}")
        ]
    wanted = _slug(read.question)
    if stem.group(2) not in (wanted, _fitted_slug(root, read.identity, read.question)):
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


# --- the decisions list -------------------------------------------------------------------------


def waiting_decisions(root: Path, read: Entry) -> list[str]:
    """The opening words of each decision in the entry's `## Decisions` list that has no home yet.

    A decision lands as it is made; one with nowhere to land yet waits in that list, and takes
    `→ <link>` when it lands (the user, 2026-10-11). The script reads the list and never writes it:
    the body stays the agent's.
    """
    return [_opening_words(item) for item in _decisions(read.body) if not _has_home(root, read.record, item)]


def is_home(root: Path, citing: str, written: str) -> bool:
    """Whether a link holds a decision for good: it resolves, and to a file outside the store, a
    ticket and an RFC — a question's body is where a decision waits, and a ticket and its plan
    expire once their work lands (the user, 2026-10-11)."""
    target = target_of(written)
    if target.elsewhere:
        return True
    record = cited_record(root, citing, target)
    return record is not None and not record.startswith(NOT_HOMES) and _resolves(root, citing, written)


def _decisions(body: str) -> list[str]:
    """Each item of the body's `## Decisions` list, `- ` or `N. `, its indented lines joined to it.

    The list runs to the next `## ` heading; prose between its items, as the bodies written before
    the list was read hold it, belongs to no item, and a fenced block is an illustration.
    """
    items: list[str] = []
    within = inside_fence = continuing = False
    for line in body.splitlines():
        if _FENCE.match(line):
            inside_fence = not inside_fence
            continuing = False
            continue
        item = _ITEM.match(line)
        if inside_fence:
            continue
        if line.startswith("## "):
            within = line.rstrip() == DECISIONS
            continuing = False
        elif within and item:
            items.append(item.group(1))
            continuing = True
        elif within and continuing and _CONTINUATION.match(line):
            items[-1] += f" {line.strip()}"
        else:
            continuing = False
    return items


def _has_home(root: Path, citing: str, item: str) -> bool:
    """Whether a decision names a home after its arrow, and only homes."""
    _, arrow, after = item.partition(ARROW)
    links = citations(after) if arrow else []
    return bool(links) and all(is_home(root, citing, link) for link in links)


def _opening_words(item: str) -> str:
    """The decision as a refusal names it: its first words, emphasis dropped."""
    return " ".join(item.replace("*", "").split()[:8])


def _waiting_problems(root: Path, entries: list[Entry]) -> list[Diagnostic]:
    """A live closed entry still holding a decision with no home: a hand edit did what `close`
    refuses. An archived entry is history and is not read for it."""
    return [
        Diagnostic(
            read.record,
            read.parts["state"].line,
            f'is closed and its Decisions list holds a decision with no home yet: "{words}"',
        )
        for read in entries
        if read.kind and not read.archived
        for words in waiting_decisions(root, read)
    ]


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
    """Relations are ids resolved over the live store and `done/` together: an id says where its
    question sits and never which folder holds it, so an archived question is still the same
    question."""
    return _orphans(entries, index) + _cycles(index) + _unmarked_suspects(entries, index) + _misplaced(entries, index)


def _misplaced(entries: list[Entry], index: dict[str, Entry]) -> list[Diagnostic]:
    """An id that disagrees with its *part of*, the line it restates (the user, 2026-10-03). An
    orphan's is not judged: its missing parent is reported already, and is what to fix first."""
    notes = []
    for read in entries:
        if read.identity is None or (read.parent is not None and read.parent not in index):
            continue
        if _parent_of(read.identity) != read.parent:
            wanted = f"{read.parent}.NNNN" if read.parent else "q-NNNN"
            notes.append(
                Diagnostic(
                    read.record, 1, f"{read.identity} is part of {read.parent or 'nothing'}, so its id is {wanted}"
                )
            )
    return notes


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
    once at its highest root — what a closure left behind, for `/maintain` to sweep (parent
    decision 34, amended: a `close` that finishes a subtree moves it itself)."""
    return [
        Finding(read.record, 1, f"{read.identity} and everything under it are closed and ready for done/")
        for read in _ready_roots(entries, index)
    ]


def _unstated(entries: list[Entry], index: dict[str, Entry]) -> list[Finding]:
    """Each live open question at the top of the work its owner answers that has no `Where it
    stands` — the one its ticket's `Answers` names, read from the store's parts alone: a child its
    owner also owns is held by the parent's picture. A finding, since the questions written before
    the rule get theirs at their next touch (q-0037.0009.0017, decision 2)."""
    notes = []
    for read in entries:
        owner = _owner(read)
        if read.archived or not read.open or owner is None:
            continue
        parent = index.get(read.parent or "")
        if parent is not None and _owner(parent) == owner:
            continue
        if not any(line.strip() == WHERE_IT_STANDS for line in read.body.splitlines()):
            label = _LINK_LABEL.match(read.parts["owner"].value)
            named = label.group(1) if label else posixpath.basename(owner)
            notes.append(Finding(read.record, 1, f"{read.identity} is answered by {named} and has no Where it stands"))
    return notes


def _relative_ids(root: Path, entries: list[Entry]) -> list[Finding]:
    """An id in an entry is written whole; a suffix such as `.0003` is a name no reader can follow.
    A finding, not a diagnostic: bodies are written by hand and are repaired where a session meets
    them. Fenced blocks are not read."""
    findings: list[Finding] = []
    for read in entries:
        if read.archived:
            continue
        inside = False
        for number, line in enumerate((root / read.record).read_text(encoding="utf-8").splitlines(), 1):
            if _FENCE.match(line):
                inside = not inside
            elif not inside and (found := _RELATIVE_ID.search(line)):
                findings.append(Finding(read.record, number, f"names `{found.group(0)}`, a relative id; an id is written whole"))
    return findings


def _unrunged(entries: list[Entry]) -> list[Finding]:
    """Each live open question without a `rung` part, in a store that uses the part: one whose
    method declares a ladder has given some question a rung, and then every open one carries its
    own (q-0037.0019, decision 2). A store with no rung anywhere has no ladder, and is asked
    nothing. A finding, not a diagnostic: another session's question gains its rung at that
    session's next touch."""
    live = [read for read in entries if not read.archived]
    if not any("rung" in read.parts for read in live):
        return []
    return [
        Finding(read.record, 1, f"{read.identity} is open and has no rung")
        for read in live
        if read.open and "rung" not in read.parts
    ]


def _owner(read: Entry) -> str | None:
    """The file an entry's owner links, from the tree's root, so links written from the live store
    and from `done/` name one owner alike."""
    said = read.parts.get("owner")
    target = _LINK_TARGET.search(said.value) if said else None
    if target is None:
        return None
    return posixpath.normpath(posixpath.join(posixpath.dirname(read.record), target.group(1)))


def _ready_roots(entries: list[Entry], index: dict[str, Entry]) -> list[Entry]:
    """Each live root of a wholly closed subtree nothing held open depends on, at its highest; a
    deferred or suspect entry counts as open, since the wake reads it in the live store."""
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
        read for read in entries if not read.archived and movable(read) and not moves_with_its_parent(read)
    ]


# --- the window ---------------------------------------------------------------------------------


@dataclass(frozen=True)
class Store:
    """The live questions as a tree, with every id resolvable and every session's row.

    The tree is the live directory alone: `done/` holds wholly closed subtrees, which no window
    draws. Ids still resolve over both, since an id says where a question sits, never which
    folder holds it.
    """

    index: dict[str, Entry]
    children: dict[str, list[Entry]]
    roots: list[Entry]
    sessions: list[sessions.Session]

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


def _next_free(index: dict[str, Entry], parent: str | None) -> str:
    """The id a question placed under `parent`, or among the roots, takes: the one after every
    position at that level, live or archived (the user, 2026-10-03). No gaps are left, since a
    question's place among its siblings carries no order to insert into — ticket positions step by
    ten for their queue, and a question has none.

    An id freed by a rename may come back below the highest; nothing forwards it, so an old commit
    message naming it may then read wrongly — accepted with the decision.
    """
    level = [_positions(identity)[-1] for identity in index if _parent_of(identity) == parent]
    position = max(level, default=0) + 1
    if position > LAST_POSITION and parent is not None:
        raise Refused(f"no free position under {parent}: four digits end at {LAST_POSITION}")
    return f"{parent}.{position:04d}" if parent else f"q-{position:04d}"


def _parent_of(identity: str) -> str | None:
    """The parent an id names, or `None` for a root's — a flat id from before ids nested is read as
    a root's, so the roots continue past it."""
    return identity.rsplit(".", 1)[0] if "." in identity else None


def _ancestry(index: dict[str, Entry], identity: str) -> list[Entry]:
    """The question and every question it is part of, up to its root. A cycle stops the walk
    where it would repeat, so a broken store still renders."""
    found: list[Entry] = []
    at = index.get(identity)
    while at is not None and at not in found:
        found.append(at)
        at = index.get(at.parent or "")
    return found


def realizes(index: dict[str, Entry], identity: str) -> TraceLink | None:
    """What a question realizes: its own trace link, else its nearest ancestor's, else `None` —
    trace propagation, computed when read and never copied into a sub-question (the user,
    2026-10-13).
    A link whose form cannot be read is the check's to report, and is passed over here."""
    return next((carrier.trace_link for carrier in _ancestry(index, identity) if carrier.trace_link), None)


def read_store(root: Path, seen: dict[str, bytes] | None = None) -> Store:
    """The store as the window and the wake read it. A file the check would report is read as far
    as it goes, and one that cannot be read at all is left out — the check is what says so."""
    entries, _, _ = _entries(root, seen)
    rows, _, _ = sessions.rows(root)
    live = sorted((read for read in entries if read.identity and not read.archived), key=_order)
    children: dict[str, list[Entry]] = {}
    for read in live:
        if read.parent:
            children.setdefault(read.parent, []).append(read)
    index = {read.identity: read for read in entries if read.identity}
    roots = [read for read in live if read.parent is None or read.parent not in index]
    return Store(index, children, roots, rows)


def due(root: Path, read: Entry) -> bool:
    """Whether a straw dog bound to this question is due: its text waited on an answer that has
    now landed, or on a question that no longer stands (the user, 2026-10-03 and 2026-10-04).

    A decided answer has landed when every link it holds is a home: while one cites a question's
    list, a ticket or an RFC, the decision waits there and has not reached its home (the user,
    2026-10-11). A merge or a supersession is never due: the binding follows the successor. A
    deferral, an open question and a suspect one are never due.
    """
    if read.suspect:
        return False
    if read.kind in ("moot", "pruned"):
        return True
    answer = read.parts.get("answer")
    if read.kind != "decided" or answer is None:
        return False
    links = citations(answer.value)
    return bool(links) and all(is_home(root, read.record, link) for link in links)


def successor(index: dict[str, Entry], read: Entry) -> Entry | None:
    """The question that finally stands where a merged or superseded one stood, following a chain
    of them to its end; `None` for a question that stands itself, or a chain that breaks or loops."""
    seen = [read]
    at = read
    while at.points_to:
        at = index.get(at.points_to)
        if at is None or at in seen:
            return None
        seen.append(at)
    return at if at is not read else None


def window(root: Path, tag: str, full: bool = False) -> str:
    """What the agent reads before placing a message: the session's position and what is near it.

    It prints position, never relevance — it has no idea what the message says. The rendering is
    the one the window test in the mechanism's evidence measured, with each line's state and lean
    added; a change to it reruns that test.

    Every window drawn stays in the conversation, so one is drawn only when something moved: when
    neither this session's position nor any entry changed since the last one, a single line says
    so (parent decision 44). Another session's position alone is not a change.

    Either form ends with the counters, since a ticket or a straw dog moves while no entry does.
    """
    if not (root / STORE).is_dir():
        return f"no store at {STORE}/: nothing to place a message in yet"
    seen: dict[str, bytes] = {}
    store = read_store(root, seen)
    held = sessions.held(root, tag)
    counters = _counters(root, store, tag)
    fingerprint = _fingerprint(held, seen)
    memory = sessions.memory(root, tag)
    if not full and memory.is_file() and memory.read_text(encoding="utf-8") == fingerprint:
        # The one line in front of most turns names the act, since "nothing moved" read as nothing
        # to do and the turn's `at` went unmade (rule failure 16). It names the choice and fills in
        # no id: the stored one, offered as the call, read as the placement (rule failure 18).
        return (
            f"window unchanged since your last one: {held.tag} at {held.current or 'no position yet'}; "
            f"say what this turn is — on a question, `questions.py at q-N --session {held.tag}` on the "
            f"one that contains the message; a process, no call — "
            f"or `--window --session {held.tag} --full` to draw it again\n{counters}"
        )
    drawn = _drawn(store, held)
    memory.parent.mkdir(parents=True, exist_ok=True)
    memory.write_text(fingerprint, encoding="utf-8")
    return f"{drawn}\n\n{counters}"


# --- the counters -------------------------------------------------------------------------------


@dataclass
class Counted:
    """What a window counted, by the names that tell one member from another: a ticket by its
    record, a question by its id, a straw dog by its record and the question it binds — never its
    line, which an edit above it moves. `records` holds each scanned record's size, time and
    bindings, so the next window reads again only what moved."""

    tickets: list[str]
    questions: list[str]
    records: dict[str, tuple[int, int, list[tuple[int, str]]]]

    @property
    def dogs(self) -> list[tuple[str, str]]:
        return [(name, bound) for name, (_, _, found) in self.records.items() for _, bound in found]


def _counters(root: Path, store: Store, tag: str) -> str:
    """The line a reply copies: open tickets, open questions and straw dogs, each with how many came
    and went since this session's previous window, its memory then moved to this one."""
    memory = Path(f"{sessions.memory(root, tag)}.counted")
    before, remembered = _recalled(memory)
    now = _tally(root, store, before.records if before else {})
    # Written by hand, and only when it moved: `asdict` copies every binding deeply, and closing a
    # written file costs more than the rest of the count, on every turn.
    said = json.dumps({"tickets": now.tickets, "questions": now.questions, "records": now.records})
    if said != remembered:
        memory.parent.mkdir(parents=True, exist_ok=True)
        memory.write_text(said, encoding="utf-8")
    kinds = (
        ("🎫", now.tickets, before.tickets if before else None),
        ("❓", now.questions, before.questions if before else None),
        ("🐕", now.dogs, before.dogs if before else None),
    )
    return " · ".join(f"{glyph} {len(named)}{_came_and_went(earlier, named)}" for glyph, named, earlier in kinds)


def _came_and_went(earlier: list | None, named: list) -> str:
    """` (+came-went)` after the total, each only where it is not nought and the brackets only
    where they hold one (the user, 2026-10-12); members matched by name and counted as many times
    as they stand. No earlier count — the session's first window — is nothing to compare, never
    everything come."""
    if earlier is None:
        return ""
    then, now = Counter(earlier), Counter(named)
    came, went = sum((now - then).values()), sum((then - now).values())
    moved = (f"+{came}" if came else "") + (f"-{went}" if went else "")
    return f" ({moved})" if moved else ""


def _tally(root: Path, store: Store, known: dict[str, tuple[int, int, list[tuple[int, str]]]]) -> Counted:
    # The ticket mechanism says what a live ticket is; imported here, since it imports this module.
    import tickets

    stamps = _straw_dog_records(root)
    return Counted(
        tickets=tickets.live_tickets(list(stamps)),
        questions=sorted(read.identity for read in store.index.values() if read.open and read.identity),
        records={name: _scanned(root, name, stamp, known.get(name)) for name, stamp in sorted(stamps.items())},
    )


def _straw_dog_records(root: Path) -> dict[str, tuple[int, int]]:
    """Every record of the straw-dog scope with its size and time, by walking it: a quarter of
    what asking Git costs, at the price of counting a record Git ignores, which the listing skips."""
    found: dict[str, tuple[int, int]] = {}
    for prefix in STRAW_DOG_SCOPE:
        top = os.path.join(root, prefix)
        if os.path.isfile(top):
            stat = os.stat(top)
            found[prefix] = (stat.st_size, stat.st_mtime_ns)
        elif os.path.isdir(top):
            _walked(top, prefix, found)
    return {name: stamp for name, stamp in found.items() if in_straw_dog_scope(name)}


def _walked(folder: str, inside: str, found: dict[str, tuple[int, int]]) -> None:
    # The directory's own listing carries each file's size and time on Windows, so no file is
    # stat'ed again: on every turn the walk is most of the counters' cost.
    with os.scandir(folder) as listed:
        for item in listed:
            name = f"{inside}/{item.name}"
            if item.is_dir(follow_symlinks=False):
                _walked(item.path, name, found)
            elif item.is_file():
                stat = item.stat()
                found[name] = (stat.st_size, stat.st_mtime_ns)


def _scanned(
    root: Path, name: str, stamp: tuple[int, int], known: tuple[int, int, list[tuple[int, str]]] | None
) -> tuple[int, int, list[tuple[int, str]]]:
    """A record's size, time and bindings — the remembered ones while its size and time stand."""
    if known is not None and (known[0], known[1]) == stamp:
        return known
    return stamp[0], stamp[1], bindings_in(name, read_text(root, name))


def _recalled(memory: Path) -> tuple[Counted | None, str | None]:
    """The previous window's count and the text it was read from, or `None` where there is none to
    read — never a failure, since a window that cannot compare still counts."""
    try:
        text = memory.read_text(encoding="utf-8")
        said = json.loads(text)
        records = {name: (size, time, [tuple(found) for found in bound]) for name, (size, time, bound) in said["records"].items()}
        return Counted(said["tickets"], said["questions"], records), text
    except (OSError, ValueError, KeyError, TypeError):
        return None, None


def _drawn(store: Store, held: sessions.Session) -> str:
    if held.current is None or held.current not in store.index:
        return _without_position(store, held)
    path = store.path(held.current)
    return "\n".join(
        [f"session: {held.tag}", f"current: {held.current}"]
        + _own_unit_lines(store, held)
        + [""]
        + _path_lines(path)
        + _frontier_lines(store, path)
        + _root_lines(store, path)
        + _elsewhere_lines(store, held)
    )


# --- the wake -----------------------------------------------------------------------------------


def wake(root: Path, now: datetime, tag: str | None = None) -> str:
    """Where the work stands when a session starts: who else is where, what waits to be re-read,
    and the window this session opens on.

    Called without a tag it registers a new session and draws the window of a session with no
    position yet. Called with the tag of a registered one it registers nothing, so `/recall` asked
    mid-session reads the same as at the start without giving one conversation two sessions.
    Either way the other sessions' rows are tended first, as at a hook's start: the silent ended,
    the long ended removed.
    """
    if tag is None:
        held = sessions.register(root, now)
        sessions.tend(root, now, held.tag)
        return _wake_read(root, held, f"session: {held.tag}, registered now", now)
    held = sessions.held(root, tag)
    sessions.tend(root, now, held.tag)
    return _wake_read(root, held, f"session: {held.tag}, already registered", now)


def _wake_read(root: Path, held: sessions.Session, header: str, now: datetime) -> str:
    """What keeps coming back, who else is running and where, what waits to be re-read, and this
    session's window drawn whole. An ended session is nobody's business at a wake."""
    store = read_store(root)
    live = sorted((read for read in store.index.values() if not read.archived), key=_order)
    others = [other for other in store.sessions if other.running and other.tag != held.tag]
    deferred = [read for read in live if read.kind == "deferred" and "answer" in read.parts]
    return "\n".join(
        [header, ""]
        + _section("most struck, open:", [f"  {_line(read)}" for read in _most_struck(live)])
        + _section("sessions:", [f"  {sessions.state(other)}{_holding(store, other)}" for other in others])
        + _section(
            "deferred, to re-check whether each condition is met:",
            [f"  {_line(read)} — {read.parts['answer'].value}" for read in deferred],
        )
        + _section("straw dogs due, their text to re-read:", _straw_dogs_due(root, store))
        + _section("suspect, to re-read:", [f"  {_line(read)}" for read in live if read.suspect])
        + _section("path:", _ahead_lines(root, now))
        + [window(root, held.tag, full=True)]
    )


def _straw_dogs_due(root: Path, store: Store) -> list[str]:
    """One line per straw dog whose question is due, where it stands and the question it waited on."""
    return [
        f"  {name}:{line} → {_line(read)}"
        for name, line, identity in question_bindings(root)
        if (read := store.index.get(identity)) is not None and due(root, read)
    ]


def _most_struck(live: list[Entry]) -> list[Entry]:
    """The open questions that came back most, highest count first and then by id, a few at most,
    so a session sees them before anything else and the read stays bounded (parent decision 54)."""
    struck = [read for read in live if read.open and read.strike and read.strike.count]
    return sorted(struck, key=lambda read: (-read.strike.count, _order(read)))[:WAKE_STRUCK_LINES]


# --- the path -----------------------------------------------------------------------------------

# TODO q-0037.0019: the path is the pathfinder's, drawn here while that mechanism is undeclared.
AHEAD_READY = 5
AHEAD_STRUCK = 3
AHEAD_LATELY = 5
_TICKET_ID = re.compile(r"^(\d\d-\d{4}(?:\.\d{4})*)-")
_FIRST_ID = re.compile(_ID)


def path_ahead(root: Path, now: datetime) -> str:
    """The path read from the records as they are, for the agent to tell the person: the work in
    hand, the questions touched lately with no ticket, the candidates at the next boundary each
    with its reasons, and how the roots balance. A reading, written nowhere, so two sessions read
    one path; it ranks nothing, the order being the queue's, and compares no count with the
    project's limit on work in hand, which the agent reads from the entry file."""
    if not (root / STORE).is_dir():
        return "path: no question store here"
    return "\n".join(["path:", *_ahead_lines(root, now)])


def _ahead_lines(root: Path, now: datetime) -> list[str]:
    ahead = _Ahead.read(root)
    lately = ahead.touched_lately(now)
    return [
        *ahead.in_work(),
        *ahead.touched_lately_lines(lately),
        "  ready, in id order, none ranked above another:",
        *_or_none(line for ticket in ahead.ready()[:AHEAD_READY] for line in ahead.ticket_lines(ticket)),
        "  most struck, no ticket, past those touched lately:",
        *_or_none(line for read in ahead.most_struck(lately)[:AHEAD_STRUCK] for line in ahead.question_lines(read)),
        "  roots:",
        *ahead.roots(),
    ]


def _or_none(lines) -> list[str]:
    found = list(lines)
    return found or ["    (none)"]


@dataclass(frozen=True)
class _Ahead:
    """What the path reads: the live store, the live tickets, the product document's coverage and
    the straw dogs' bindings — each mechanism's records through that mechanism's reader."""

    live: dict[str, Entry]
    tickets: list
    coverage: dict[str, str]
    bindings: list[str]

    @staticmethod
    def read(root: Path) -> "_Ahead":
        import product  # noqa: PLC0415  (it imports this module)
        import tickets  # noqa: PLC0415  (it imports this module)

        live = {identity: read for identity, read in read_store(root).index.items() if not read.archived}
        bindings = [identity for _, _, identity in question_bindings(root)]
        return _Ahead(live, tickets.check(root).records, product.coverage_words(root), bindings)

    # --- the work in hand ---

    def in_work(self) -> list[str]:
        """The tickets In progress with none under them In progress: a parent is in progress
        because a child is, and is counted once, through the child."""
        # TODO q-0037.0019.0001: sessions in the ring count too once the store can tell them.
        going = [ticket for ticket in self.tickets if _status_of(ticket) == "In progress"]
        ids = [_ticket_id(ticket) for ticket in going]
        leaves = [ticket for ticket in going if not any(other.startswith(f"{_ticket_id(ticket)}.") for other in ids)]
        heading = f"  in work: {len(leaves)} — tickets In progress, a parent counted through its child; sessions are not counted"
        return [heading, *(self._ticket_line(ticket) for ticket in leaves)]

    # --- what waits ---

    def touched_lately(self, now: datetime) -> list[Entry]:
        """The open questions no ticket owns, below a root, stamped within the week the session
        rows also keep — what the store can say of a new idea, which records no boundary."""
        # TODO q-0037.0019.0001: since the last boundary, once the store records one.
        horizon = now - sessions.GONE_AFTER
        found = [read for read in self._unowned() if read.strike and read.strike.last >= horizon]
        return sorted(found, key=lambda read: read.strike.last, reverse=True)

    def touched_lately_lines(self, lately: list[Entry]) -> list[str]:
        shown = [
            f"    {read.question} — {read.identity} (struck {read.strike.count}, {read.strike.last:%Y-%m-%d})"
            for read in lately[:AHEAD_LATELY]
        ]
        more = [f"    and {len(lately) - AHEAD_LATELY} more"] if len(lately) > AHEAD_LATELY else []
        return [f"  touched lately, no ticket: {len(lately)}", *shown, *more]

    # --- the candidates ---

    def ready(self) -> list:
        return [ticket for ticket in self.tickets if _status_of(ticket) == "Ready"]

    def most_struck(self, lately: list[Entry]) -> list[Entry]:
        """The open questions no ticket owns that came back most, roots left out — a root is struck
        whenever its tree is — and those already shown as touched lately."""
        shown = {read.identity for read in lately}
        struck = [read for read in self._unowned() if read.strike and read.strike.count and read.identity not in shown]
        return sorted(struck, key=lambda read: (-read.strike.count, _order(read)))

    def ticket_lines(self, ticket) -> list[str]:
        question = _answers_of(ticket)
        waiting = [_title_of(other) for other in self.tickets if _stem(ticket) in (other.fields.get("Depends on") or "")]
        return [self._ticket_line(ticket), self._reasons(question, waiting)]

    def question_lines(self, read: Entry) -> list[str]:
        return [f"    {read.question} — {read.identity}", self._reasons(read.identity, [])]

    def _reasons(self, identity: str | None, waiting: list[str]) -> str:
        """Why a candidate stands: the answer it serves and how much of it is built, how often it
        came back, how much provisional text waits on it, and what waits on it. A reason the
        records do not hold reads `unread`, never guessed."""
        read = self.live.get(identity or "")
        struck = read.strike.count if read and read.strike else 0
        dogs = sum(1 for bound in self.bindings if identity and _within(bound, identity))
        dependents = [other.identity for other in self.live.values() if other.open and identity
                      and any(_within(needed, identity) for needed in other.dependencies)]
        unlocks = ", ".join([*waiting, *(dependent or "" for dependent in dependents)]) or "—"
        return f"      serves {self._serves(identity)} · struck {struck} · {dogs} straw dogs · unlocks {unlocks}"

    def _serves(self, identity: str | None) -> str:
        link = realizes(self.live, identity) if identity in self.live else None
        if link and link.answers:
            return "; ".join(f"{reference} {name}, {self.coverage.get(reference, 'unread')}" for reference, name in link.answers)
        return "derived" if link and link.derived else "unread"

    # --- the roots ---

    def roots(self) -> list[str]:
        """Each root, its open questions and those with a ticket on them or above them; a root with
        open questions and none with a ticket is thin."""
        lines = []
        for root in sorted((read for read in self.live.values() if read.parent is None), key=_order):
            under = [read for read in self.live.values() if read.open and _within(read.identity or "", f"{root.identity}.")]
            ticketed = [read for read in under if self._owned(read.identity or "")]
            thin = ", thin" if under and not ticketed else ""
            lines.append(f"    {root.question} — {root.identity}: open {len(under)}, with a ticket {len(ticketed)}{thin}")
        return _or_none(lines)

    # --- reading ---

    def _unowned(self) -> list[Entry]:
        return [read for read in self.live.values()
                if read.open and read.parent is not None and not self._owned(read.identity or "")]

    def _owned(self, identity: str) -> bool:
        """Whether a live ticket owns the question or a question above it — part of that ticket's work."""
        return any("owner" in at.parts and "/done/" not in at.parts["owner"].value for at in _ancestry(self.live, identity))

    def _ticket_line(self, ticket) -> str:
        return f"    {_title_of(ticket)} — {_ticket_id(ticket)} → {_answers_of(ticket) or 'unread'}"


def _within(identity: str, ancestor: str) -> bool:
    """Whether an id is the ancestor's own or one under it; an ancestor ending in `.` names its
    children alone."""
    return identity.startswith(ancestor) if ancestor.endswith(".") else identity == ancestor or identity.startswith(f"{ancestor}.")


def _status_of(ticket) -> str:
    return (ticket.fields.get("Status") or "").split("(")[0].strip()


def _answers_of(ticket) -> str | None:
    found = _FIRST_ID.search(ticket.fields.get("Answers") or "")
    return found.group(0) if found else None


def _stem(ticket) -> str:
    return posixpath.splitext(posixpath.basename(ticket.record))[0]


def _ticket_id(ticket) -> str:
    named = _TICKET_ID.match(_stem(ticket))
    return named.group(1) if named else _stem(ticket)


def _title_of(ticket) -> str:
    return ticket.title


# --- the hooks ----------------------------------------------------------------------------------


@dataclass(frozen=True)
class Host:
    """What one host's hooks send and expect: everything host-specific about delivery is here.

    Read from each host's hook documentation (parent decision 44); a row is documented, not
    observed, until a live session in that host shows it.
    """

    session_field: str
    # An environment variable naming the conversation more steadily than the payload's field,
    # read first where it is set.
    conversation_variable: str | None
    starts: str
    messages: str | None
    compactions: tuple[str, ...]
    answer: Callable[[str, str, str], str]
    quiet: str
    # A message event whose answer reaches no agent: the session is only marked seen.
    signs_of_life: str | None = None


def _hook_specific(event: str, context: str, tag: str) -> str:
    return json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": context}})


def _cursor_answer(event: str, context: str, tag: str) -> str:
    """Cursor drops a start hook's context (a confirmed host defect), and passes its `env` to
    every later hook of the session, so the session's tag goes there too, for whatever the agent's
    shell can read of it. Its prompt hook can only allow or block, and always allows: nothing here
    may hold back the person's message."""
    if event == "beforeSubmitPrompt":
        return json.dumps({"continue": True})
    answer: dict = {"additional_context": context}
    if tag and event == "sessionStart":
        answer["env"] = {"QUESTIONS_SESSION": tag}
    return json.dumps(answer)


HOSTS = {
    # The desktop app gives Claude Code a new session id when it resumes a conversation (a
    # rollback 2026-10-09, a reopening 2026-10-10) and keeps its own id for the conversation in
    # every process it starts; the terminal keeps the session id on resume, and sets no such id.
    "claude-code": Host(
        "session_id", "CLAUDE_CODE_HOST_SESSION_ID", "SessionStart", "UserPromptSubmit", (), _hook_specific, ""
    ),
    "codex": Host("session_id", None, "SessionStart", "UserPromptSubmit", ("PostCompact",), _hook_specific, ""),
    # Cursor's prompt hook can only allow or block, so its agent draws the window by the rule, and
    # the hook only marks the session seen: in practice the agent draws none (rule failure 28).
    "cursor": Host(
        "conversation_id",
        None,
        "sessionStart",
        None,
        ("preCompact",),
        _cursor_answer,
        "{}",
        "beforeSubmitPrompt",
    ),
}


def _hook_input() -> str:
    """The host's payload as it wrote it. The pipe's bytes are decoded by their own mark, never in
    the console's code page: Cursor on Windows wrote input the code page could not read, and the
    hook registered nothing."""
    pipe = getattr(sys.stdin, "buffer", None)
    if pipe is None:
        return sys.stdin.read()
    raw = pipe.read()
    if raw.startswith((codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)):
        return raw.decode("utf-16")
    return raw.decode("utf-8-sig", errors="replace")


def hook(root: Path, host_name: str, payload: str, now: datetime) -> str:
    """What a host's hook prints: the wake's read when a session starts, the window before a
    message, nothing after a compaction but a forgotten window. A message marks its session seen;
    where its answer reaches no agent, that is all it does.

    It never fails the host. A prompt hook that fails can hold back the person's message, so any
    problem is answered as one line of context that names it, and the exit status stays 0. Once the
    host and the event are known, the notice goes out in that host's own form, since a host that
    reads its hook's answer as JSON would drop plain text.
    """
    host = HOSTS.get(host_name)
    event: str | None = None
    tag = ""
    try:
        if host is None:
            raise Refused(f"no host `{host_name}`; the hosts are {', '.join(HOSTS)}")
        sent = _sent(payload)
        event = sent.get("hook_event_name")
        named = os.environ.get(host.conversation_variable, "") if host.conversation_variable else ""
        tag = sessions.tag_of(named or str(sent.get(host.session_field) or ""))
        if event in host.compactions:
            sessions.forget_window(root, tag)
            return host.quiet
        if event == host.starts:
            return host.answer(event, _noticed(_started(root, tag, sent.get("source"), now)), tag)
        registered = tag in {held.tag for held in sessions.rows(root)[0]}
        if event == host.messages:
            if not registered:
                # The start was never seen — the hooks arrived mid-session — so this is the start.
                return host.answer(event, _started(root, tag, None, now), tag)
            drawn = window(root, tag)
            sessions.seen(root, tag, now)
            return host.answer(event, drawn, tag)
        if event == host.signs_of_life:
            if not registered:
                sessions.register(root, now, tag)
            sessions.seen(root, tag, now)
            return host.answer(event, "", tag)
        return ""
    except Exception as problem:  # noqa: BLE001 — the boundary to a host: nothing may escape it
        notice = f"questions hook: {problem}"
        if host is not None and event in (host.starts, host.messages, host.signs_of_life):
            return host.answer(event, notice, "")
        return notice


def _noticed(context: str) -> str:
    """The wake's read with the line another mechanism handed the hook's wrapper — the installer's,
    when the tree's installed blocks are out of step with its rules files and settings — last, so
    the agent meets it before its first command. The wrapper hands it as `GW_NOTICE`."""
    notice = os.environ.get("GW_NOTICE", "").strip()
    return f"{context}\n\n{notice}" if notice else context


def _sent(payload: str) -> dict:
    """The host's payload as JSON; what is not is named by its length and its first characters,
    so a host's hook log shows what arrived."""
    try:
        return json.loads(payload)
    except json.JSONDecodeError:
        raise Refused(
            f"the hook's input is not JSON: {len(payload)} characters, beginning {payload[:40]!r}"
        ) from None


def _started(root: Path, tag: str, source: str | None, now: datetime) -> str:
    """A session starting, resuming or compacted: registered once under the host's id, running
    again if it had ended, and given a whole window, since its context has none. A start that is
    not a compaction tends the other sessions' rows first."""
    sessions.forget_window(root, tag)
    held, registered_now = sessions.arrive(root, tag, now)
    if registered_now:
        sessions.tend(root, now, tag)
        return _wake_read(root, held, f"session: {tag}, registered now", now)
    if source == "compact":
        return window(root, tag, full=True)
    sessions.tend(root, now, tag)
    return _wake_read(root, held, f"session: {tag}, already registered", now)


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


def _fingerprint(held: sessions.Session, seen: dict[str, bytes]) -> str:
    """What a window was drawn from: this session's position and every entry's bytes."""
    digest = hashlib.sha256(f"{held.current}\n".encode())
    for name in sorted(seen):
        digest.update(name.encode() + b"\0" + seen[name] + b"\0")
    return digest.hexdigest()


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
                f"  {read.identity} (parent {read.parent}) {read.question}{_count(read)}{_lean(read)}"
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


def _position(store: Store, current: str | None) -> str:
    """Another session's position with its question's words, so a reply can name it as written."""
    if current is None:
        return "no position yet"
    entry = store.index.get(current)
    return f"{current} {entry.question}" if entry else current


def _holding(store: Store, held: sessions.Session) -> str:
    """The unit a session holds, as another's line names it: the question and its owner, while
    the question is open; a closed question holds nobody."""
    unit = _held_unit(store, held)
    return f", holding {unit}" if unit else ""


def _own_unit_lines(store: Store, held: sessions.Session) -> list[str]:
    """The unit this session holds, or the mark of one another session took over from it."""
    unit = _held_unit(store, held)
    if unit:
        return [f"holding: {unit}"]
    return [f"taken: {held.taken} by {held.taken_by}"] if held.taken else []


def _held_unit(store: Store, held: sessions.Session) -> str | None:
    entry = store.index.get(held.holds or "")
    if entry is None or not entry.open:
        return None
    return f"{held.holds} ({sessions.owner_of(store.index, held.holds)})"


def _elsewhere_lines(store: Store, held: sessions.Session) -> list[str]:
    others = [
        f"  {other.tag} at {_position(store, other.current)} (last wrote {sessions.stamp(other.wrote)}){_holding(store, other)}"
        for other in store.sessions
        if other.running and other.tag != held.tag
    ]
    return _section("other running sessions:", others) + [
        f"recently attached: {', '.join(held.recent) or 'none'}",
    ]


def _without_position(store: Store, held: sessions.Session) -> str:
    """A session that has not placed itself yet: the roots to place it among, and who is where."""
    return "\n".join(
        [f"session: {held.tag}", "current: none yet — the first `at` call places it"]
        + _own_unit_lines(store, held)
        + [""]
        + _section("roots:", [f"  {_line(read)}" for read in store.roots])
        + _elsewhere_lines(store, held)
    )


def _line(read: Entry) -> str:
    return f"{read.identity} [{read.parts['state'].value}] {read.question}{_count(read)}{_lean(read)}"


def _count(read: Entry) -> str:
    """How often the question came back, when it has (parent decision 54)."""
    strike = read.strike
    return f" (struck {strike.count})" if strike and strike.count else ""


def _lean(read: Entry) -> str:
    lean = read.parts.get("lean")
    return f"  ~ {lean.value}" if lean else ""


def _section(heading: str, lines: list[str]) -> list[str]:
    """A heading, its lines, and the blank line that ends it. A heading with nothing under it says
    so, so an empty section is not read as a missing one."""
    return [heading] + (lines or ["  (none)"]) + [""]


def _order(read: Entry) -> tuple[int, ...]:
    """Tree order: a child after its parent and before the parent's next sibling."""
    return _positions(read.identity or "q-0")


def _positions(identity: str) -> tuple[int, ...]:
    return tuple(int(position) for position in identity[2:].split("."))


# --- the writer ---------------------------------------------------------------------------------


@dataclass(frozen=True)
class Clause:
    """One event, as the writer applies it.

    A call makes one from its arguments; a judge's typed value will be turned into the same list
    without parsing (parent decision 39), so the writer has one front door for both. An `opens`
    carries no id: the writer takes the next free one.
    """

    verb: str
    question: str | None = None
    other: str | None = None
    lower: str | None = None
    text: str | None = None


# A record named by its id, `01-0090.0030` of a ticket's file name, is labelled by that id alone.
_RECORD_ID = re.compile(r"^\d{2}-\d{4}(?:\.\d{4})*")
EVENTS = (
    "at", "open", "move", "reword", "depend", "undepend", "close", "suspect", "clear", "lean", "assign", "realize",
    "rung",
)


def _called(root: Path, argv: list[str], today: date, now: datetime) -> int:
    """One event of a turn, as its call says it (parent decision 56): written whole and reported,
    or refused with its usage and nothing written."""
    try:
        said = _calls().parse_args(argv)
    except SystemExit as stopped:
        return stopped.code if isinstance(stopped.code, int) else 2
    left = sessions.held(root, said.session).current
    written = declare(root, said.session, [_clause(said)], today, now=now)
    for record in written.entries:
        print(f"wrote {record}")
    for identity in written.opened:
        print(f"opened {identity}")
    for old, new in written.renamed.items():
        print(f"renamed {old} → {new}")
    for identity in written.reworded:
        print(f"reworded {identity} {read_store(root).index[identity].question}")
    if written.archived:
        print(f"moved {', '.join(written.archived)} to done/")
    if written.session is not None:
        print(_landed(root, written.session.current, left))
    if written.archive_refused:
        print(f"the closure stands; the subtree it finished stays live: {written.archive_refused}")
        return 1
    return 0


# TODO q-0037.0009.0021: read under `debug=on` until debugging installs its own blocks.
def _landed(root: Path, current: str | None, left: str | None) -> str:
    """Where an `at` placed the session, as a person reads it under `debug=on`: the question, and
    the one it left when it moved (the user, 2026-10-03, amending parent decision 25)."""
    index = read_store(root).index

    def titled(identity: str) -> str:
        read = index.get(identity)
        return f"{identity} {read.question}" if read else identity

    moved = f" (from {titled(left)})" if left and left != current else ""
    return f"at {titled(current or '')}{moved}"


def _clause(said: argparse.Namespace) -> Clause:
    """The writer's clause for one call."""
    if said.event == "open":
        upper, lower = said.between or (said.under, None)
        return Clause("opens", other=upper, lower=lower, text=said.text)
    if said.event == "move":
        return Clause("moves", said.question, other=said.under)
    if said.event in ("depend", "undepend"):
        return Clause(f"{said.event}s", said.question, other=said.on)
    if said.event == "close":
        return Clause("closes", said.question, other=said.kind, text=said.pointer)
    if said.event in ("lean", "assign", "reword", "realize", "rung"):
        return Clause(f"{said.event}s", said.question, text=said.text)
    return Clause({"at": "at", "suspect": "suspects", "clear": "clears"}[said.event], said.question)


def _calls() -> argparse.ArgumentParser:
    """The events of a turn, one subcommand each, every one naming the session that makes it."""
    calls = argparse.ArgumentParser(prog="questions.py")
    events = calls.add_subparsers(dest="event", required=True)

    def event(name: str, does: str) -> argparse.ArgumentParser:
        call = events.add_parser(name, help=does, description=does)
        call.add_argument("--session", required=True, help="the session making the call")
        return call

    def of_question(name: str, does: str) -> argparse.ArgumentParser:
        call = event(name, does)
        call.add_argument("question", type=_question_id)
        return call

    of_question("at", "place the session at an open question")
    opening = event("open", "open a question; prints the id it was given")
    opening.add_argument("text", help="the question, phrased short")
    where = opening.add_mutually_exclusive_group()
    where.add_argument("--under", type=_question_id, help="its parent")
    where.add_argument("--between", nargs=2, type=_question_id, metavar=("UPPER", "LOWER"),
                       help="its parent, and a child of that parent moved under it")
    moving = of_question("move", "give a question a new parent, or none")
    to = moving.add_mutually_exclusive_group(required=True)
    to.add_argument("--under", type=_question_id)
    to.add_argument("--to-root", action="store_true")
    of_question("reword", "give an open question new words; its id stays").add_argument("text")
    for name, does in (("depend", "a question waits on another"), ("undepend", "it waits no more")):
        of_question(name, does).add_argument("--on", required=True, type=_question_id)
    closing = of_question("close", "close a question by a kind, with its pointer")
    closing.add_argument("kind", choices=KINDS)
    closing.add_argument("pointer", nargs="?", help="what the questions skill's Closing names for the kind")
    of_question("suspect", "mark a question's answer to be re-read")
    of_question("clear", "lift the mark")
    of_question("lean", "write a question's lean").add_argument("text")
    of_question("assign", "name the record of the work that answers a question").add_argument("text", metavar="path")
    of_question("realize", 'write the answers a question realizes, `A7 "<name>", ...`, or `derived`').add_argument(
        "text", metavar="link"
    )
    of_question("rung", "write a question's highest rung on each ladder it touches, `<ladder>: <rung>, ...`").add_argument(
        "text", metavar="rungs"
    )
    return calls


def _question_id(given: str) -> str:
    if not _IDENTITY.match(given):
        raise argparse.ArgumentTypeError(f"`{given}` is not a question id, `q-NNNN` or `q-NNNN.NNNN`")
    return given


@dataclass
class Written:
    """What one declaration wrote, in the order it was written, the ids it opened, each id a
    re-parent renamed, with the one it took, and the ids whose questions it reworded."""

    entries: list[str]
    session: sessions.Session | None
    opened: list[str]
    renamed: dict[str, str] = field(default_factory=dict)
    reworded: list[str] = field(default_factory=list)
    archived: list[str] = field(default_factory=list)
    archive_refused: str | None = None


class Taken(Refused):
    """An id this declaration drew for an `opens` was written by another session meanwhile."""


def declare(
    root: Path,
    tag: str,
    clauses: list[Clause],
    today: date,
    between: Callable[[], None] | None = None,
    now: datetime | None = None,
) -> Written:
    """Apply clauses in order to the store, validate the result whole, then write the entries they
    changed and the session's line last. `now`, the clock's UTC time unless a caller injects one,
    stamps what opens and strikes what is reached again (parent decision 53).

    Nothing is written unless everything validates. Just before writing, every entry file the
    clauses change is read again, and one that moved since it was read refuses them: detected
    interference is a failure, never authority to overwrite. The one exception is an id drawn for
    an `opens` that another session took meanwhile: the store is read again and the next free id
    drawn, up to `OPEN_ATTEMPTS` times, since the other session's entry is untouched either way.
    The rows are outside the recheck, since each session replaces only its own.
    `between` runs after validation and before that last read — the moment another writer may act.
    """
    now = now or datetime.now(timezone.utc)
    attempt = 1
    while True:
        try:
            return _declared(root, tag, clauses, today, now, between if attempt == 1 else None)
        except Taken:
            if attempt == OPEN_ATTEMPTS:
                raise
            attempt += 1


def _declared(
    root: Path,
    tag: str,
    clauses: list[Clause],
    today: date,
    now: datetime,
    between: Callable[[], None] | None,
) -> Written:
    seen: dict[str, bytes] = {}
    entries, _, _ = _entries(root, seen)
    held = sessions.held(root, tag)
    draft = _Draft(root, {read.identity: read for read in entries if read.identity}, now)
    for clause in clauses:
        draft.apply(clause)
    position = next((clause.question for clause in clauses if clause.verb == "at"), None)
    if position is not None:
        draft.place(position)
    if between is not None:
        between()
    draft.recheck(seen)
    written = draft.write()
    if draft.moves:
        written = _carry_renames(root, draft.moves, draft.renames, written)
        held = sessions.renamed(held, draft.renames)
    moved = sessions.moved(held, position, now)
    if moved is not None:
        try:
            sessions.write_row(root, moved)
        except OSError as error:
            raise WriteInterrupted(written, sessions.ROWS, error) from error
    opened = [identity for identity in draft.changed if identity in draft.new]
    closed = [draft.renames.get(clause.question or "", clause.question or "") for clause in clauses if clause.verb == "closes"]
    archived, refused = _archive_finished(root, closed, written) if closed else ([], None)
    return Written(written, moved, opened, dict(draft.renames), list(draft.reworded), archived, refused)


def seed(root: Path, now: datetime) -> list[str]:
    """A store that holds no entry, live or archived, opens with the roots its shelf words, in the
    shelf's order and with nothing under them — the questions mechanism's *Three roots from the
    start*. A store holding any entry is the project's: nothing is written and nothing returned.

    An install is not a turn, so no session is read or registered, which is why `declare` is not
    the way in; the draft still refuses an id another writer took meanwhile."""
    if _entry_files(root):
        return []
    shelf = root / STORE_ARRIVAL
    if not shelf.is_file():
        raise Refused(f"seed: no shelf at {STORE_ARRIVAL}")
    draft = _Draft(root, {}, now)
    for question in arrival_roots(shelf.read_text(encoding="utf-8")):
        draft.apply(Clause("opens", text=question))
    draft.recheck({})
    return draft.write()


def arrival_roots(shelf: str) -> list[str]:
    """The root questions a shelf's `roots` block words, one to a line. Found by the info string and
    not by position, so prose may be written around the block; read from text rather than a path,
    so the installer can ask it of a ref before anything of the ref is written."""
    said = _ROOTS_BLOCK.search(shelf.replace("\r\n", "\n"))
    if said is None:
        raise Refused(f"seed: {STORE_ARRIVAL} holds no `roots` block")
    roots = [line.strip() for line in said.group("said").splitlines() if line.strip()]
    if not roots:
        raise Refused(f"seed: {STORE_ARRIVAL}'s `roots` block names no root")
    return roots


def _archive_finished(root: Path, closed: list[str], written: list[str]) -> tuple[list[str], str | None]:
    """The subtrees these closures finished, moved to `done/` in one invocation of the mover —
    the same one a rename carries its entries with — and the ids moved, or why the mover refused.
    The closures stand either way: they are the decisions, and the maintainer sweeps what stays."""
    entries, _, _ = _entries(root)
    index = {read.identity: read for read in entries if read.identity}
    finished = [
        top
        for top in _ready_roots(entries, index)
        if any(top in _ancestry(index, identity) for identity in closed)
    ]
    moving = sorted((read for top in finished for read in _subtree(entries, top) if not read.archived), key=_order)
    pairs = [(read.record, f"{STORE}/done/{posixpath.basename(read.record)}") for read in moving]
    if not pairs:
        return [], None
    why = move_doc.refusal(root, pairs)
    if why:
        return [], why
    try:
        move_doc.perform(root, pairs)
    except move_doc.CloseInterrupted as stopped:
        raise WriteInterrupted(written, "the finished subtree's move to done/", stopped) from stopped
    return [read.identity or "" for read in moving], None


def _subtree(entries: list[Entry], top: Entry) -> list[Entry]:
    """The question and every question below it, by *part of*."""
    found = [top]
    for read in found:
        found += [child for child in entries if child.parent == read.identity and child not in found]
    return found


def _carry_renames(
    root: Path, moves: list[tuple[str, str]], renames: dict[str, str], written: list[str]
) -> list[str]:
    """After the renamed entries are written in place: move them, which repairs every link to
    them, then rewrite their bare ids — so nothing under `docs/` names an id that is gone."""
    try:
        move_doc.perform(root, moves)
    except move_doc.CloseInterrupted as stopped:
        raise WriteInterrupted(written, "the renamed entries' move", stopped) from stopped
    landed = dict(moves)
    if renames:
        _rewrite_ids(root, renames)
    return [landed.get(record, record) for record in written]


def _rewrite_ids(root: Path, renames: dict[str, str]) -> None:
    """Every renamed id written outside a link, in the records under `docs/` and the sessions' rows,
    and every straw dog's binding to one, wherever the straw dogs stand.

    An id is matched whole, so a longer one that starts the same way is never touched. Under
    `docs/` a code span is rewritten, since an id there names this store's question; a fenced block
    is not — it holds samples, whose ids are examples, never references (the user, 2026-10-03).
    Elsewhere only a binding moves: core names a record of this tree in a straw dog's binding and
    nowhere else, so an id in its prose is an example. Each file is read and replaced in one
    rename; a person editing it at that moment can still lose the race, as with the mover.
    """
    for name in _records_naming_ids(root):
        path = root / name
        text = path.read_bytes().decode("utf-8")
        if name.startswith("docs/"):
            rewritten = _outside_fences(text, lambda line: _BARE_ID.sub(lambda found: renames.get(found.group(0), found.group(0)), line))
        else:
            rewritten = with_question_bindings_retargeted(name, text, renames.get)
        if rewritten != text:
            _replace(path, rewritten)


def _records_naming_ids(root: Path) -> list[str]:
    """The records a rename reads: the documents under `docs/`, each session's row wherever it
    stands, and the documents and scripts where straw dogs stand outside `docs/`."""
    names = [
        name
        for name in corpus(root)
        if (name.startswith("docs/") and name.endswith(".md")) or (in_straw_dog_scope(name) and not name.startswith("docs/"))
    ]
    return names + sessions.records(root)


def _outside_fences(text: str, change: Callable[[str], str]) -> str:
    """The text with `change` applied to every line outside a fenced block, its line ends kept."""
    lines = text.splitlines(keepends=True)
    inside = False
    for at, line in enumerate(lines):
        if _FENCE.match(line):
            inside = not inside
        elif not inside:
            lines[at] = change(line)
    return "".join(lines)


def _replace(path: Path, text: str) -> None:
    """The file's new text in one rename, so a reader never meets half a file."""
    staging = path.with_name(f".{path.name}.renaming.tmp")
    try:
        staging.write_bytes(text.encode("utf-8"))
        staging.replace(path)
    finally:
        staging.unlink(missing_ok=True)


class _Draft:
    """The store as the clauses leave it, held in memory until all of them validate."""

    def __init__(self, root: Path, index: dict[str, Entry], now: datetime) -> None:
        self.root = root
        self.index = dict(index)
        self.now = now
        self.changed: list[str] = []
        self.new: set[str] = set()
        # Each id a re-parent renamed, with the one it took, and where each renamed entry's file
        # sits on disk until the rename moves it.
        self.renames: dict[str, str] = {}
        self.origin: dict[str, str] = {}
        # The ids whose questions were reworded: the id stays, and only the file's name may move.
        self.reworded: list[str] = []

    @property
    def moves(self) -> list[tuple[str, str]]:
        """Each renamed entry's file, from where it sits to where its new id puts it."""
        return [(self.origin[identity], self.index[identity].record) for identity in self.origin]

    def apply(self, clause: Clause) -> None:
        getattr(self, f"_{clause.verb}")(clause)

    def place(self, identity: str) -> None:
        """The position is an open question, and reaching it may strike it."""
        read = self._existing(identity)
        if not read.open:
            state = read.parts["state"].value
            raise Refused(f"`at {identity}`: {identity} is {state}; a position is an open question")
        self._reach(read)

    def _reach(self, read: Entry) -> None:
        """A reach twelve hours or more after the last stamp strikes the question; an entry written
        before the count is stamped and not struck, so the old ones do not all strike at once; any
        other reach writes nothing, so a turn that stays does not redraw every window. A stamp the
        check would refuse is left for the check to report."""
        strike = read.strike
        if strike is None and "struck" not in read.parts:
            self._put(_with(read, struck=Strike(0, self.now).text))
        elif strike is not None and self.now - strike.last >= STRIKE_AFTER:
            self._put(_with(read, struck=Strike(strike.count + 1, self.now).text))

    def _at(self, clause: Clause) -> None:
        """Checked once every clause has applied, by `place`."""

    def _opens(self, clause: Clause) -> None:
        """A new question takes the next free position under its parent; the recheck finds it
        still free, or `declare` draws again."""
        if clause.other:
            self._existing(clause.other)
        identity = _next_free(self.index, clause.other)
        parts = {"state": "open", "struck": Strike(0, self.now).text}
        if clause.other:
            parts = {"part of": clause.other} | parts
        record = f"{STORE}/{identity}-{_fitted_slug(self.root, identity, clause.text or '')}.md"
        self._put(Entry(record, identity, clause.text or "", {n: Part(v, 0) for n, v in parts.items()}))
        self.new.add(identity)
        if clause.lower:
            lower = self._existing(clause.lower)
            if lower.parent != clause.other:
                raise Refused(f"`open --between {clause.other} {clause.lower}`: {clause.lower} is not part of {clause.other}")
            self._seat(lower, identity)

    def _moves(self, clause: Clause) -> None:
        moving = self._existing(clause.question or "")
        if clause.other is not None:
            self._existing(clause.other)
            if moving in _ancestry(self.index, clause.other):
                raise Refused(f"`move {moving.identity} --under {clause.other}` makes a cycle in part of")
        self._seat(moving, clause.other)

    def _rewords(self, clause: Clause) -> None:
        """An open question takes new words and keeps its id, its parts and its body (the user,
        2026-10-05): the same question means the same answers, never the same wording. The file
        is named by the words, so it moves when they change its slug, and the mover repairs every
        link to it. A closed question keeps the words it was answered under."""
        read = self._existing(clause.question or "")
        identity = read.identity or ""
        words = " ".join((clause.text or "").split())
        if not words:
            raise Refused(f"`reword {identity}` gives no words")
        if not read.open:
            state = read.parts["state"].value
            raise Refused(f"`reword {identity}`: {identity} is {state}; it keeps the words it was answered under")
        if words == read.question:
            raise Refused(f"`reword {identity}`: it already reads so")
        record = posixpath.join(posixpath.dirname(read.record), f"{identity}-{_fitted_slug(self.root, identity, words)}.md")
        if record != read.record and identity not in self.new:
            self.origin.setdefault(identity, read.record)
        self.reworded.append(identity)
        self._put(Entry(record, identity, words, read.parts, read.body))

    def _seat(self, read: Entry, parent: str | None) -> None:
        """Give a question its parent, renaming it and everything under it so each id says where
        it sits (the user, 2026-10-03). One already there, under an id that says so, is left as
        it is; a flat id from before ids nested is renamed even under the parent it has."""
        if read.parent == parent and _parent_of(read.identity or "") == parent:
            return
        renames = self._renames_below(read, _next_free(self.index, parent))
        for old, new in renames.items():
            moved = self.index.pop(old)
            above = parent if old == read.identity else renames[moved.parent or ""]
            slug = _fitted_slug(self.root, new, moved.question)
            record = posixpath.join(posixpath.dirname(moved.record), f"{new}-{slug}.md")
            if old in self.new:
                self.new.discard(old)
                self.new.add(new)
            else:
                self.origin[new] = self.origin.pop(old, moved.record)
            self.changed = [new if each == old else each for each in self.changed]
            self._put(Entry(record, new, moved.question, _with(moved, **{"part of": above}).parts, moved.body))
        self.renames.update(renames)
        for other in list(self.index.values()):
            self._name_renamed_ids(other, renames)

    def _renames_below(self, top: Entry, identity: str) -> dict[str, str]:
        """The new id of every question in the subtree, from its top down: a child whose id nests
        under its parent's keeps its last position, and one whose id never did takes the next free
        position after its nested siblings."""
        renames = {top.identity or "": identity}
        waiting = [top]
        while waiting:
            above = waiting.pop(0)
            children = sorted(
                (read for read in self.index.values() if read.parent == above.identity), key=_order
            )
            nested = [read for read in children if _parent_of(read.identity or "") == above.identity]
            taken = [_positions(read.identity or "")[-1] for read in nested]
            for child in children:
                if child in nested:
                    position = _positions(child.identity or "")[-1]
                else:
                    position = max(taken, default=0) + 1
                    if position > LAST_POSITION:
                        raise Refused(f"no free position under {renames[above.identity or '']}")
                    taken.append(position)
                renames[child.identity or ""] = f"{renames[above.identity or '']}.{position:04d}"
            waiting += children
        return renames

    def _name_renamed_ids(self, read: Entry, renames: dict[str, str]) -> None:
        """An entry's relations, rewritten to the ids a rename gave."""
        changes: dict[str, str] = {}
        if read.parent in renames:
            changes["part of"] = renames[read.parent]
        if any(identity in renames for identity in read.dependencies):
            changes["depends on"] = ", ".join(renames.get(identity, identity) for identity in read.dependencies)
        if read.points_to in renames:
            changes["answer"] = renames[read.points_to]
        if changes:
            self._put(_with(read, **changes))

    def _depends(self, clause: Clause) -> None:
        waiting, awaited = self._existing(clause.question or ""), self._existing(clause.other or "")
        if waiting.identity in self._awaited_by(awaited.identity or ""):
            raise Refused(f"`depend {waiting.identity} --on {awaited.identity}` makes a cycle in depends on")
        if awaited.identity not in waiting.dependencies:
            listed = ", ".join(waiting.dependencies + [awaited.identity or ""])
            self._put(_with(waiting, **{"depends on": listed}))

    def _undepends(self, clause: Clause) -> None:
        """One dependency lifted; the part goes with the last."""
        waiting, awaited = self._existing(clause.question or ""), clause.other or ""
        if awaited not in waiting.dependencies:
            raise Refused(f"`undepend {waiting.identity} --on {awaited}`: {waiting.identity} does not depend on {awaited}")
        left = [each for each in waiting.dependencies if each != awaited]
        self._put(_with(waiting, **{"depends on": ", ".join(left) or None}))

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
                    f"`close {closing.identity} pruned` leaves {', '.join(left)} open under it; move out "
                    "the ones that stand alone and close the rest first"
                )
        waiting = waiting_decisions(self.root, closing)
        if waiting:
            successor = f", or to {clause.text}" if kind in ("merged", "superseded") else ""
            raise Refused(
                f'`close {closing.identity} {kind}`: its Decisions list holds a decision with no home yet: '
                f'"{waiting[0]}"; land it, or move it to the nearest open question above that holds '
                f"everyone who needs it{successor}"
            )
        state = f"closed:{kind}" + (", suspect" if closing.suspect else "")
        closed = _with(closing, state=state, answer=clause.text)
        problems = _answer_problems(self.root, closed)
        if problems:
            raise Refused(f"`close {closing.identity} {kind}`: {problems[0].problem}")
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
        read = self._existing(clause.question or "")
        if found := _RELATIVE_ID.search(clause.text or ""):
            raise Refused(f"`lean {read.identity}`: `{found.group(0)}` is a relative id, which names nothing a reader can follow; write the id whole")
        self._put(_with(read, lean=clause.text))

    def _assigns(self, clause: Clause) -> None:
        """The owner is the record of the work that answers the question — the deliberation is
        the entry's own body — written as a link from the entry, so the mover repairs it when
        either one moves."""
        read = self._existing(clause.question or "")
        owner = (clause.text or "").strip()
        if not (self.root / owner).is_file():
            raise Refused(f"`assign {read.identity} {owner}`: no file {owner} in this tree")
        name = posixpath.splitext(posixpath.basename(owner))[0]
        label = _RECORD_ID.match(name)
        link = posixpath.relpath(owner, posixpath.dirname(read.record))
        self._put(_with(read, owner=f"[{label.group(0) if label else name}]({link})"))

    def _realizes(self, clause: Clause) -> None:
        """The trace link replaces whatever the question carried, on any entry the store holds,
        open or closed, live or archived — coverage reads closed questions too."""
        read = self._existing(clause.question or "")
        link = (clause.text or "").strip()
        if _trace_link(link) is None:
            raise Refused(f"`realize {read.identity} {link}`: {_NOT_A_TRACE_LINK}")
        self._put(_with(read, realizes=link))

    def _rungs(self, clause: Clause) -> None:
        """The highest rungs replace whatever the question carried. Raising is the agent's and
        lowering the person's; the store cannot tell which until a ladder declares its order."""
        read = self._existing(clause.question or "")
        rungs = (clause.text or "").strip()
        if _rung(rungs) is None:
            raise Refused(f"`rung {read.identity} {rungs}`: {_NOT_A_RUNG}")
        self._put(_with(read, rung=rungs))

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
            raise Refused(
                f"no entry holds {identity}; an id changes when its question is re-parented — "
                "draw the window again, `--window --session <tag> --full`"
            )
        return read

    def _put(self, read: Entry) -> None:
        self.index[read.identity or ""] = read
        if read.identity not in self.changed:
            self.changed.append(read.identity or "")

    def recheck(self, seen: dict[str, bytes]) -> None:
        """Every entry the clauses change is as it was read, and every id they open or rename to is
        still free — under any slug, since another session names its question in its own words;
        then the mover has no reason to refuse the renamed entries' move."""
        for identity in self.changed:
            taking = identity in self.new or (identity in self.origin and identity not in self.reworded)
            if taking and _files_holding(self.root, identity):
                raise Taken(f"{identity} was written by another session since this call read the store")
            if identity in self.new:
                continue
            record = self.origin.get(identity, self.index[identity].record)
            now = (self.root / record).read_bytes() if (self.root / record).is_file() else None
            if now != seen.get(record):
                raise Refused(f"{record} changed since this call read it; call it again")
        why = move_doc.refusal(self.root, self.moves) if self.moves else None
        if why:
            raise Refused(f"the renamed entries cannot move: {why}")

    def write(self) -> list[str]:
        """The changed entries, in the order the clauses changed them — a renamed one where its file
        still sits, for the mover to carry. A failure stops the run and says what was written:
        nothing is rolled back."""
        written: list[str] = []
        for identity in self.changed:
            read = self.index[identity]
            record = self.origin.get(identity, read.record)
            try:
                path = self.root / record
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(_entry_text(read), encoding="utf-8", newline="\n")
            except OSError as error:
                raise WriteInterrupted(written, record, error) from error
            written.append(record)
        return written


class WriteInterrupted(Exception):
    """A write that failed after another had succeeded. Nothing was rolled back; `completed` is
    what was written and `failed` where it stopped."""

    def __init__(self, completed: list[str], failed: str, error: Exception) -> None:
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
    """The same entry, its body untouched, with some parts replaced; a part given as `None` is
    removed."""
    parts = dict(read.parts)
    for name, value in changes.items():
        name = name.replace("_", " ")
        if value is None:
            parts.pop(name, None)
        else:
            parts[name] = Part(value, 0)
    return Entry(read.record, read.identity, read.question, parts, read.body)


def _entry_text(read: Entry) -> str:
    """The entry as the store writes it: the parts in the format's order, the mark first and as the
    state calls for, whatever the file carried before; then the body as it was read."""
    kind = _kind(read)
    parts = {**read.parts, MARK: Part(kind, 0)} if kind else read.parts
    bullets = [f"- **{name}** {parts[name].value}" for name in PARTS if name in parts]
    parts = "\n".join([f"# {read.identity} {read.question}", "", *bullets]) + "\n"
    return parts + ("\n" + read.body if read.body else "")


def _slug(question: str) -> str:
    """Every word of the question, cut at a word boundary only past `SLUG_LENGTH` characters, so a
    person reading a listing reads the whole question (parent decision 55)."""
    slug: list[str] = []
    for word in _words(question):
        if slug and len("-".join(slug + [word])) > SLUG_LENGTH:
            break
        slug.append(word)
    return "-".join(slug) or "question"


def _fitted_slug(root: Path, identity: str, question: str) -> str:
    """The question's slug, cut further at a word boundary while the entry's path in `done/` — the
    longer of its two homes — would pass `PATH_LIMIT`. The id is never cut (the user, 2026-10-03);
    a single word that still does not fit is kept, and the platform says so when it is written."""
    words = _slug(question).split("-")
    while len(words) > 1 and len(str(root / STORE / "done" / f"{identity}-{'-'.join(words)}.md")) > PATH_LIMIT:
        words.pop()
    return "-".join(words)


if __name__ == "__main__":
    # The tree this script sits in; anything that imports it names its tree itself.
    sys.exit(main(sys.argv[1:], Path(__file__).resolve().parents[3]))
