# Mechanism: mechanism-shape
"""The rule-failure register's attribution: every occurrence — an entry's first and each strike —
names the host, the model and the time it happened under, and the case it links agrees.

    uv run --offline --no-project python .agents/scripts/gw/rule_failures.py --check

An occurrence names them in a source line under its `**Source…` label: one form, linked to the
occurrence's case where it has one — `- [<host> · <model> · <time>](cases/<id>/case.json)` — and
bare where it has none yet — `- <host> · <model> · <time>`, what follows the time free. Where no
source survives it stands on a line `- [Evidence gap](...)`. A model the source does not
record is written `unknown`, in its case as well or as `null`; a model named carries the place in the
source it was read from. Format, never content: whether the source says what the case reads from
it is the extraction's to show.
"""

from __future__ import annotations

import json
import re
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path

REGISTER = "docs/rule-failures.md"
UNKNOWN = "unknown"
_USAGE = "usage: rule_failures.py --check"
_ENTRY = re.compile(r"^## ")
_STRIKE = re.compile(r"^\*\*Struck\b")
_SOURCE = re.compile(r"^- \[(?P<text>[^\]]*)\]\((?P<link>[^)]*)\)")
_BARE = re.compile(r"^- (?!\[)(?P<text>.+)$")
_LABEL = re.compile(r"^\*\*Source\b")
_TIME = re.compile(r"^\d{4}-\d\d-\d\dT\d\d:\d\d(:\d\d(\.\d+)?)?(Z|[+-]\d\d:\d\d)$")
_GAP = "Evidence gap"


@dataclass(frozen=True)
class Note:
    line: int
    problem: str
    detail: str

    def as_record(self) -> dict:
        return {"where": f"{REGISTER}:{self.line}", "problem": self.problem, "detail": self.detail}


@dataclass
class Checked:
    occurrences: int = 0
    unknown: int = 0
    gaps: int = 0
    diagnostics: list[Note] = field(default_factory=list)

    def as_record(self) -> dict:
        return {"occurrences": self.occurrences, "unknown_models": self.unknown, "evidence_gaps": self.gaps,
                "diagnostics": [note.as_record() for note in self.diagnostics]}


def check(root: Path) -> Checked:
    checked = Checked()
    register = root / REGISTER
    if not register.is_file():
        return checked
    lines = register.read_text(encoding="utf-8-sig").splitlines()
    linked: dict[Path, int] = {}
    for start, sources in _occurrences(lines):
        checked.occurrences += 1
        if not sources:
            checked.diagnostics.append(Note(start, "occurrence names no host and model", lines[start - 1]))
        for number, text, link in sources:
            if text == _GAP:
                checked.gaps += 1
                checked.diagnostics.extend(_against_gap(number, register.parent, link))
                continue
            parts = [part.strip() for part in text.split("·")]
            if len(parts) == 3 and not link:
                parts[2] = parts[2].split(maxsplit=1)[0].rstrip(".,;") if parts[2] else ""
            if len(parts) != 3 or not all(parts):
                checked.diagnostics.append(Note(number, "source line is not host · model · time", text))
                continue
            checked.unknown += parts[1] == UNKNOWN
            if not _TIME.match(parts[2]):
                checked.diagnostics.append(Note(number, "time is not an ISO instant", parts[2]))
            if not link:
                continue
            target = (register.parent / link.split("#")[0]).resolve()
            if target in linked:
                checked.diagnostics.append(Note(number, "case stands for a second occurrence",
                                                f"first at line {linked[target]}"))
                continue
            linked[target] = number
            checked.diagnostics.extend(_against_case(number, parts, target, root))
    for number, problem, detail in _cases(root, set(linked)):
        checked.diagnostics.append(Note(number, problem, detail))
    return checked


def _occurrences(lines: list[str]) -> list[tuple[int, list[tuple[int, str, str]]]]:
    """Each occurrence's first line and the source lines under its `**Source…` label, each with
    its link or `""` where it is bare, in the register's order; the preamble before the first entry
    holds none."""
    found: list[tuple[int, list[tuple[int, str, str]]]] = []
    listing = False
    for number, line in enumerate(lines, 1):
        if _ENTRY.match(line) or (found and _STRIKE.match(line)):
            found.append((number, []))
            listing = False
        elif found and _LABEL.match(line):
            listing, read = True, False
        elif listing and (match := _SOURCE.match(line)):
            found[-1][1].append((number, match["text"].strip(), match["link"]))
            read = True
        elif listing and (match := _BARE.match(line)):
            found[-1][1].append((number, match["text"].strip(), ""))
            read = True
        elif listing and (line.strip() or read):
            listing = False
    return found


def _read(path: Path) -> tuple[dict | None, str]:
    """A case's JSON object, or why it cannot be read as one."""
    try:
        record = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        return None, str(error)
    return (record, "") if isinstance(record, dict) else (None, "not a JSON object")


def _shown(path: Path, root: Path) -> str:
    return path.relative_to(root.resolve()).as_posix() if path.is_relative_to(root.resolve()) else str(path)


def _against_gap(number: int, base: Path, link: str) -> list[Note]:
    file, _, pointer = link.partition("#")
    record, why = _read((base / file).resolve())
    if record is None:
        return [Note(number, "evidence gap does not resolve", f"{link}: {why}")]
    node: object = record
    for key in filter(None, pointer.split("/")):
        if isinstance(node, dict) and key in node:
            node = node[key]
        elif isinstance(node, list) and any(isinstance(row, dict) and row.get("id") == key for row in node):
            node = next(row for row in node if isinstance(row, dict) and row.get("id") == key)
        else:
            return [Note(number, "evidence gap does not resolve", link)]
    return []


def _against_case(number: int, parts: list[str], target: Path, root: Path) -> list[Note]:
    host, model, at = parts
    shown = _shown(target, root)
    if not target.is_file():
        return [Note(number, "linked case is missing", shown)]
    record, why = _read(target)
    if record is None:
        return [Note(number, "linked case does not parse", f"{shown}: {why}")]
    provenance = record.get("provenance")
    if not isinstance(provenance, dict):
        return [Note(number, "case names no model", shown)]
    notes = []
    if not _points_here(target, record, root):
        notes.append(Note(number, "case does not point at this register", shown))
    if "model" not in provenance:
        notes.append(Note(number, "case names no model", shown))
    elif (provenance["model"] or UNKNOWN) != model:
        notes.append(Note(number, "model differs from its case", f"{model} ≠ {provenance['model']}"))
    elif model != UNKNOWN and not provenance.get("model_source"):
        notes.append(Note(number, "model names no source", shown))
    if provenance.get("host") != host:
        notes.append(Note(number, "host differs from its case", f"{host} ≠ {provenance.get('host')}"))
    if provenance.get("occurred_at") != at:
        notes.append(Note(number, "time differs from its case", f"{at} ≠ {provenance.get('occurred_at')}"))
    return notes


def _points_here(path: Path, record: dict, root: Path) -> bool:
    failure = record.get("failure")
    pointer = failure.get("register") if isinstance(failure, dict) else None
    return bool(pointer) and (path.parent / pointer).resolve() == (root / REGISTER).resolve()


def _cases(root: Path, linked: set[Path]) -> list[tuple[int, str, str]]:
    """The cases that say they are an occurrence in this register and that no occurrence links,
    and the cases that cannot be read to tell."""
    found = []
    for path in sorted((root / "docs" / "cases").glob("*/case.json")):
        path = path.resolve()
        record, why = _read(path)
        if record is None:
            found.append((0, "case does not parse", f"{_shown(path, root)}: {why}"))
        elif path not in linked and _points_here(path, record, root):
            found.append((0, "case is linked from no occurrence", _shown(path, root)))
    return found


def main(argv: list[str], root: Path, out: Callable[[str], None] = print) -> int:
    if argv != ["--check"]:
        out(_USAGE)
        return 2
    checked = check(root)
    out(json.dumps(checked.as_record(), indent=2, ensure_ascii=False))
    return 1 if checked.diagnostics else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:], Path(__file__).resolve().parents[3]))
