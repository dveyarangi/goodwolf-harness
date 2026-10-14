# Mechanism: product
"""The product document held to the question store, and each answer's coverage read from it.

    uv run --offline --no-project python .agents/scripts/gw/product.py --check
    uv run --offline --no-project python .agents/scripts/gw/product.py --coverage

The document is `docs/product.md`, in the product format, `.agents/skills/product/PRODUCT-FORMAT.md`:
an answer is a row of its answers table whose first cell opens with its bold lead,
`**A<n> <name>**`, and whose last cell, *waits on*, is empty once it is decided and holds a straw
dog bound to a purpose question while it is not. `--check` reports every way the document and the
store disagree: what is broken — a malformed row, a link naming no answer or a name its answer no
longer has, a row bound where it may not be — fails it; what is missing — an orphan, an unrealized
answer, a purpose question no row names — is reported and never fails it (the user, 2026-10-13).
`--coverage` renders, for a person, each answer's coverage — absent, in progress, present — read
from the questions whose trace links name it, and never written. A tree with no product document
has nothing to check or render, and passes. A document with no answers heading is not in the
format, and fails.

The one write is `seed`, the installer's to call: where no file is at the document's path, the
empty document its shelf words, `.agents/skills/product/PRODUCT-ARRIVAL.md`. Everything else
writes nothing.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import questions  # noqa: E402  (path set just above)
from docs_corpus import bindings_in  # noqa: E402

DOCUMENT = "docs/product.md"
ANSWERS = "## Answers"
ARRIVAL = ".agents/skills/product/PRODUCT-ARRIVAL.md"
_ARRIVAL_BLOCK = re.compile(r"^```product-document\n(?P<said>.*?)^```", re.M | re.S)
# TODO q-0037.0018.0011: the store's shelf words these roots too, until each mechanism declares the
# root it owns — the purpose root this one, the structure root the development method.
PURPOSE_ROOT = "What is this project for?"
STRUCTURE_ROOT = "How is this project built?"
_USAGE = "usage: product.py --check | --coverage"
_LEAD = re.compile(r"^\*\*(A\d+) +([^*]*[^*\s])\*\*")
_SEPARATOR = re.compile(r"^\|[\s:|-]+\|$")


class Refused(Exception):
    """A seed that cannot say the document: nothing is written."""


@dataclass(frozen=True)
class Answer:
    """One answer row: its id, never renumbered; its name, which a trace link quotes; and what its
    last cell says it waits on, empty once it is decided."""

    identity: str
    name: str
    line: int
    waits: str = ""

    @property
    def decided(self) -> bool:
        return not self.waits

    @property
    def bound_to(self) -> list[str]:
        return [identity for _, identity in bindings_in(DOCUMENT, self.waits)]


@dataclass(frozen=True)
class Note:
    """A diagnostic or a finding, at the record and line it stands on."""

    record: str
    line: int | None
    says: str

    def as_record(self, key: str) -> dict:
        return {"record": self.record, "line": self.line, key: self.says}


def main(argv: list[str], root: Path) -> int:
    if argv == ["--check"]:
        diagnostics, findings, answers = check(root)
        report = {
            "document": DOCUMENT if (root / DOCUMENT).is_file() else None,
            "answers": len(answers),
            "diagnostics": [note.as_record("problem") for note in diagnostics],
            "findings": [note.as_record("finding") for note in findings],
        }
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 1 if diagnostics else 0
    if argv == ["--coverage"]:
        for line in coverage(root):
            print(line)
        return 0
    print(_USAGE)
    return 2


def check(root: Path) -> tuple[list[Note], list[Note], list[Answer]]:
    """What is broken, what is missing, and the answers read: the document's form, then the
    document and the store against each other."""
    path = root / DOCUMENT
    if not path.is_file():
        return [], [], []
    answers, diagnostics = read_answers(path.read_text(encoding="utf-8"))
    store = questions.read_store(root)
    purpose, structure = _root(store, PURPOSE_ROOT), _root(store, STRUCTURE_ROOT)
    diagnostics += _link_problems(store, answers) + _binding_problems(store, answers, purpose)
    findings = (
        _orphans(store, structure)
        + _unrealized(root, answers)
        + _unnamed_purpose_questions(store, answers, purpose)
    )
    return diagnostics, findings, answers


def coverage(root: Path) -> list[str]:
    """One line per answer, in the document's order: its id and name, its coverage, and the
    questions that realize it."""
    path = root / DOCUMENT
    if not path.is_file():
        return []
    answers, _ = read_answers(path.read_text(encoding="utf-8"))
    realizing = _questions_realizing(root)
    return [_coverage_line(found, realizing.get(found.identity, [])) for found in answers]


def seed(root: Path) -> list[str]:
    """The empty document the shelf words, written where no file is at the document's path, on an
    install or an update alike; what was written. A file already there is the project's from its
    first line, in the format or not, and is left as it stands (the user, 2026-10-14)."""
    path = root / DOCUMENT
    if path.exists():
        return []
    shelf = root / ARRIVAL
    if not shelf.is_file():
        raise Refused(f"seed: no shelf at {ARRIVAL}")
    said = arrival_document(shelf.read_text(encoding="utf-8"))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(said)
    return [DOCUMENT]


def arrival_document(shelf: str) -> str:
    """The document a shelf's `product-document` block words. Read from text rather than a path,
    so the installer can ask it of a ref before anything of the ref is written; found by the info
    string, so prose may be written around it."""
    said = _ARRIVAL_BLOCK.search(shelf.replace("\r\n", "\n"))
    if said is None:
        raise Refused(f"seed: {ARRIVAL} holds no `product-document` block")
    return said.group("said")


# --- what is broken -----------------------------------------------------------------------------


def _link_problems(store: questions.Store, answers: list[Answer]) -> list[Note]:
    """Each live question's own link held to the answers: a reference no answer holds, or a name
    its answer no longer has. Only the link a question writes is held, so one broken link is
    reported once, where it is written; a closed question in `done/` is history."""
    names = {found.identity: found.name for found in answers}
    notes = []
    for read in _live(store):
        link = read.trace_link
        if link is None:
            continue
        line = read.parts["realizes"].line
        for reference, name in link.answers:
            if reference not in names:
                notes.append(Note(read.record, line, f"realizes {reference}, which no answer holds"))
            elif name != names[reference]:
                notes.append(Note(read.record, line, f'quotes {reference} as "{name}", and it is "{names[reference]}"'))
    return notes


def _binding_problems(store: questions.Store, answers: list[Answer], purpose: str | None) -> list[Note]:
    """An undecided row waits on a purpose question, bound to it: one bound to nothing, to a
    question the store does not hold, or to one outside the purpose root, is broken."""
    notes = []
    for found in answers:
        if found.decided:
            continue
        if not found.bound_to:
            notes.append(Note(DOCUMENT, found.line, f"answer {found.identity} waits on something and binds no question"))
        for identity in found.bound_to:
            if identity not in store.index:
                notes.append(Note(DOCUMENT, found.line, f"answer {found.identity} binds {identity}, which no entry holds"))
            elif purpose and not _under(store.index, identity, purpose):
                notes.append(Note(DOCUMENT, found.line, f"answer {found.identity} binds {identity}, outside the purpose root"))
    return notes


# --- what is missing ----------------------------------------------------------------------------


def _orphans(store: questions.Store, structure: str | None) -> list[Note]:
    """An open question under the structure root that realizes nothing and says it is derived
    nowhere: its link is missing."""
    if structure is None:
        return []
    return [
        Note(read.record, None, f"{read.identity} is an orphan: no trace link, and not derived")
        for read in _live(store)
        if read.open and _under(store.index, read.identity or "", structure)
        and questions.realizes(store.index, read.identity or "") is None
    ]


def _unrealized(root: Path, answers: list[Answer]) -> list[Note]:
    """A decided answer no question realizes: declared, and nobody builds it."""
    realizing = _questions_realizing(root)
    return [
        Note(DOCUMENT, found.line, f"answer {found.identity} {found.name} is unrealized")
        for found in answers
        if found.decided and not realizing.get(found.identity)
    ]


def _unnamed_purpose_questions(store: questions.Store, answers: list[Answer], purpose: str | None) -> list[Note]:
    """An open question under the purpose root that no row binds, neither it nor an ancestor below
    the root: a product question asked off the document."""
    if purpose is None:
        return []
    bound = {identity for found in answers for identity in found.bound_to}
    return [
        Note(read.record, None, f"{read.identity} is a purpose question no answer row names")
        for read in _live(store)
        if read.open and _under(store.index, read.identity or "", purpose)
        and not bound.intersection(_lineage(store.index, read.identity or "", purpose))
    ]


# --- coverage -----------------------------------------------------------------------------------


def _coverage_line(found: Answer, realizing: list[questions.Entry]) -> str:
    """Absent while no question realizes the answer, in progress while one that does is open,
    present once every one is decided; a question closed otherwise built nothing (settled at the
    plan, 2026-10-13)."""
    if not realizing:
        return f"{found.identity} {found.name} — absent"
    state = "in progress" if any(_counts_as_open(read) for read in realizing) else "present"
    return f"{found.identity} {found.name} — {state}: {', '.join(read.identity or '' for read in realizing)}"


def _questions_realizing(root: Path) -> dict[str, list[questions.Entry]]:
    """Each answer's reference, and the questions that realize it, in the store's order. Only an
    open question, a deferred one with it, or a decided one realizes."""
    index = questions.read_store(root).index
    found: dict[str, list[questions.Entry]] = {}
    for identity in sorted(index):
        read = index[identity]
        link = questions.realizes(index, identity)
        if link is None or not (_counts_as_open(read) or read.kind == "decided"):
            continue
        for reference, _ in link.answers:
            found.setdefault(reference, []).append(read)
    return found


def _counts_as_open(read: questions.Entry) -> bool:
    return read.open or read.kind == "deferred"


# --- the store ----------------------------------------------------------------------------------


def _root(store: questions.Store, words: str) -> str | None:
    """The live root whose question is these words, or `None` where the store holds none."""
    return next((read.identity for read in store.roots if read.question == words and read.parent is None), None)


def _live(store: questions.Store) -> list[questions.Entry]:
    return [read for _, read in sorted(store.index.items()) if not read.archived]


def _lineage(index: dict[str, questions.Entry], identity: str, root: str) -> list[str]:
    """The question and each question it is part of, up to the root and without it."""
    found: list[str] = []
    at = index.get(identity)
    while at is not None and at.identity != root and at.identity not in found:
        found.append(at.identity or "")
        at = index.get(at.parent or "")
    return found


def _under(index: dict[str, questions.Entry], identity: str, root: str) -> bool:
    """Whether a question stands below the root — never the root itself."""
    at = index.get(identity)
    seen: set[str] = set()
    while at is not None and at.parent and at.identity not in seen:
        seen.add(at.identity or "")
        if at.parent == root:
            return True
        at = index.get(at.parent)
    return False


# --- reading the document -----------------------------------------------------------------------


def read_answers(text: str) -> tuple[list[Answer], list[Note]]:
    """The answers the document's answers table holds, and whatever in it the format does not
    admit. A row whose first cell alone is filled is a group heading, no answer. A document with no
    answers heading is not in the format at all: read as holding no answer, it would pass in
    silence (the user, 2026-10-14)."""
    if not in_format(text):
        return [], [Note(DOCUMENT, None, f"the document is not in the product format: it has no `{ANSWERS}` heading")]
    answers: list[Answer] = []
    problems: list[Note] = []
    for number, cells in _answer_rows(text):
        if not any(cells[1:]):
            continue
        lead = _LEAD.match(cells[0])
        if lead is None:
            problems.append(Note(DOCUMENT, number, "an answer row whose first cell does not open with `**A<n> <name>**`"))
            continue
        if any(seen.identity == lead.group(1) for seen in answers):
            problems.append(Note(DOCUMENT, number, f"answer {lead.group(1)} is written twice"))
            continue
        answers.append(Answer(lead.group(1), lead.group(2), number, cells[-1] if len(cells) > 1 else ""))
    return answers, problems


def in_format(text: str) -> bool:
    """Whether a document is in the product format at all: it has the answers heading."""
    return any(line.strip() == ANSWERS for line in text.splitlines())


def _answer_rows(text: str) -> list[tuple[int, list[str]]]:
    """The cells of each body row of the first table under the answers heading, with its line."""
    rows: list[tuple[int, list[str]]] = []
    inside = header_read = False
    for number, line in enumerate(text.splitlines(), start=1):
        if line.startswith("## "):
            if inside:
                break
            inside = line.strip() == ANSWERS
            continue
        if not inside or not line.startswith("|"):
            if inside and rows and not line.strip():
                break
            continue
        if not header_read or _SEPARATOR.match(line.strip()):
            header_read = True
            continue
        rows.append((number, [cell.strip() for cell in line.strip().strip("|").split("|")]))
    return rows


if __name__ == "__main__":
    # The tree this script sits in; anything that imports it names its tree itself.
    sys.exit(main(sys.argv[1:], Path(__file__).resolve().parents[3]))
