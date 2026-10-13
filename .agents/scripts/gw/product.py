# Mechanism: product
"""Each answer of the product document, and its coverage read from the questions that realize it.

    uv run --offline --no-project python .agents/scripts/gw/product.py --check
    uv run --offline --no-project python .agents/scripts/gw/product.py --coverage

The document is `docs/product.md`, in the product format, `.agents/skills/product/PRODUCT-FORMAT.md`:
an answer is a row of its answers table whose first cell opens with its bold lead,
`**A<n> <name>**`. `--check` rules on that form alone — every answer an id and a name, no id twice —
and prints JSON for the person reading a failure. `--coverage` renders, for a person, each
answer's coverage — absent, in progress, present — read from the questions whose trace links
name it, and never written (q-0035, decision 4). A tree with no product document has nothing to
check or render, and passes. The script writes nothing.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import questions  # noqa: E402  (path set just above)

DOCUMENT = "docs/product.md"
ANSWERS = "## Answers"
_USAGE = "usage: product.py --check | --coverage"
_LEAD = re.compile(r"^\*\*(A\d+) +([^*]*[^*\s])\*\*")
_SEPARATOR = re.compile(r"^\|[\s:|-]+\|$")


@dataclass(frozen=True)
class Answer:
    """One answer row: its id, never renumbered, and its name, which a trace link quotes."""

    identity: str
    name: str
    line: int


@dataclass(frozen=True)
class Diagnostic:
    line: int
    problem: str

    def as_record(self) -> dict:
        return {"record": DOCUMENT, "line": self.line, "problem": self.problem}


def main(argv: list[str], root: Path) -> int:
    if argv == ["--check"]:
        return _check(root)
    if argv == ["--coverage"]:
        for line in coverage(root):
            print(line)
        return 0
    print(_USAGE)
    return 2


def _check(root: Path) -> int:
    path = root / DOCUMENT
    answers, diagnostics = read_answers(path.read_text(encoding="utf-8")) if path.is_file() else ([], [])
    report = {
        "document": DOCUMENT if path.is_file() else None,
        "answers": len(answers),
        "diagnostics": [note.as_record() for note in diagnostics],
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if diagnostics else 0


def coverage(root: Path) -> list[str]:
    """One line per answer, in the document's order: its id and name, its coverage, and the
    questions that realize it."""
    path = root / DOCUMENT
    if not path.is_file():
        return []
    answers, _ = read_answers(path.read_text(encoding="utf-8"))
    realizing = _questions_realizing(root)
    return [_coverage_line(found, realizing.get(found.identity, [])) for found in answers]


def _coverage_line(found: Answer, realizing: list[questions.Entry]) -> str:
    """Absent while no question realizes the answer, in progress while one that does is open,
    present once every one is decided (q-0035.0006, decision 2)."""
    if not realizing:
        return f"{found.identity} {found.name} — absent"
    state = "in progress" if any(_counts_as_open(read) for read in realizing) else "present"
    return f"{found.identity} {found.name} — {state}: {', '.join(read.identity or '' for read in realizing)}"


def _questions_realizing(root: Path) -> dict[str, list[questions.Entry]]:
    """Each answer's reference, and the questions that realize it, in the store's order. Only an
    open question, a deferred one with it, or a decided one realizes: one closed otherwise built
    nothing."""
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


# --- reading the document -----------------------------------------------------------------------


def read_answers(text: str) -> tuple[list[Answer], list[Diagnostic]]:
    """The answers the document's answers table holds, and whatever in it the format does not
    admit. A row whose first cell alone is filled is a group heading, no answer."""
    answers: list[Answer] = []
    problems: list[Diagnostic] = []
    for number, cells in _answer_rows(text):
        if not any(cells[1:]):
            continue
        lead = _LEAD.match(cells[0])
        if lead is None:
            problems.append(Diagnostic(number, "an answer row whose first cell does not open with `**A<n> <name>**`"))
            continue
        if any(seen.identity == lead.group(1) for seen in answers):
            problems.append(Diagnostic(number, f"answer {lead.group(1)} is written twice"))
            continue
        answers.append(Answer(lead.group(1), lead.group(2), number))
    return answers, problems


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
