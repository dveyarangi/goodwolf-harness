"""The statements that expire, and the one mechanical edit that retires them.

    uv run --offline --no-project python .agents/scripts/temporary_statements.py PATH [PATH ...]
    uv run --offline --no-project python .agents/scripts/temporary_statements.py \
        --remove FILE:LINE --expect sha256:...

Reading a scope reports every operative `<temporary>` block in it as JSON, with the condition and
owning ticket as written and a diagnostic for anything a maintainer must look at. Removing takes
out one block a maintainer has already judged obsolete.

This tool never decides that a condition holds — it does not interpret an `until` phrase, and it
certainly does not execute one. Judgement is `/maintain`'s; the entry contract owns the syntax.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from docs_corpus import without_code  # noqa: E402  (path set just above)

_TAG = re.compile(r"<temporary\b[^<>]*>|</temporary\s*>|<temporary\b|</temporary\b", re.S)
_ATTRIBUTE = re.compile(r'\b(until|ticket)\s*=\s*"([^"]*)"', re.S)
_USAGE = "usage: temporary_statements.py PATH [PATH ...] | --remove FILE:LINE --expect HASH"


class Refused(Exception):
    """A removal that must not happen. Nothing was written; the reason says what to settle first."""


@dataclass(frozen=True)
class Statement:
    """One operative temporary statement, as written.

    `until` and `ticket` are the author's words, not a verdict: an unresolved condition stays
    unresolved here. `fingerprint` covers the whole file's bytes, so a removal can prove it is
    acting on the reading it was shown.
    """

    path: str
    opens: int
    closes: int
    until: str | None
    ticket: str | None
    depth: int
    contains: int
    fingerprint: str
    span: tuple[int, int]

    def as_record(self) -> dict:
        return {
            "path": self.path,
            "opens": self.opens,
            "closes": self.closes,
            "until": self.until,
            "ticket": self.ticket,
            "depth": self.depth,
            "contains": self.contains,
            "fingerprint": self.fingerprint,
        }


@dataclass(frozen=True)
class Diagnostic:
    """Something in the scope a maintainer has to resolve before the scope can be called clean."""

    path: str
    line: int
    problem: str

    def as_record(self) -> dict:
        return {"path": self.path, "line": self.line, "problem": self.problem}


@dataclass(frozen=True)
class Surveyed:
    """What one reading of a declared scope found. Empty statements and no diagnostics is a result."""

    scanned: list[str]
    statements: list[Statement]
    diagnostics: list[Diagnostic]

    def as_record(self) -> dict:
        return {
            "scanned": self.scanned,
            "statements": [statement.as_record() for statement in self.statements],
            "diagnostics": [note.as_record() for note in self.diagnostics],
        }


def main(argv: list[str], root: Path | None = None) -> int:
    root = root or Path(__file__).resolve().parents[2]
    if argv[:1] == ["--remove"]:
        return _removal(root, argv[1:])
    if argv[:1] in (["--help"], ["-h"]):
        print(_USAGE)
        return 0
    if not argv or any(operand.startswith("-") for operand in argv):
        print(_USAGE)
        return 2
    try:
        surveyed = survey(root, argv)
    except Refused as refusal:
        print(f"refused, nothing surveyed: {refusal}")
        return 2
    print(json.dumps(surveyed.as_record(), indent=2))
    return 1 if surveyed.diagnostics else 0


def _removal(root: Path, argv: list[str]) -> int:
    if len(argv) != 3 or argv[1] != "--expect":
        print(_USAGE)
        return 2
    where, expected = argv[0], argv[2]
    path, _, line = where.rpartition(":")  # from the final colon, so `D:/…/x.md:3` still parses
    if not path or not line.isdigit():
        print(_USAGE)
        return 2
    try:
        remove_statement(root, path, int(line), expected)
    except Refused as refusal:
        print(f"refused, nothing written: {refusal}")
        return 2
    print(f"removed the temporary statement at {path}:{line}")
    return 0


def survey(root: Path, paths: list[str]) -> Surveyed:
    """Every operative temporary statement in a declared scope, with what is wrong alongside it."""
    scanned: list[str] = []
    statements: list[Statement] = []
    diagnostics: list[Diagnostic] = []
    for name in _records_in(root, paths):
        scanned.append(name)
        try:
            text = _read(root / name)
        except (OSError, UnicodeDecodeError):
            diagnostics.append(Diagnostic(name, 0, "unreadable"))
            continue
        found, notes = _statements_in(root, name, text)
        statements += found
        diagnostics += notes
    return Surveyed(scanned, statements, diagnostics)


def remove_statement(root: Path, path: str, line: int, expect: str) -> None:
    """Take out the one obsolete statement opening at `path:line`, and nothing else.

    Refuses unless the file still hashes to `expect` and the block holds no nested statement: this
    tool has no way to tell whether a child expired with its parent, and a surviving agreement
    inside an obsolete wrapper must be rehomed before the wrapper can go.
    """
    record = root / path
    if not _inside_repository(root, path):
        raise Refused(f"{path} resolves outside the repository")
    if not record.is_file():
        raise Refused(f"{path} is not a record of this repository")
    if _fingerprint(record) != expect:
        raise Refused(f"{path} has changed since it was read; scan it again and reselect")
    text = _read(record)
    statements, _ = _statements_in(root, path, text)
    opening = [statement for statement in statements if statement.opens == line]
    if not opening:
        raise Refused(f"no temporary statement opens at {path}:{line}")
    statement = opening[0]
    if statement.contains:
        raise Refused(
            f"{path}:{line} contains {statement.contains} nested statement(s); "
            "dispose of them first, then read the file again"
        )
    start, end = _whole_lines_of(text, statement.span)
    _replace_content(record, text[:start] + text[end:])


def _statements_in(root: Path, name: str, text: str) -> tuple[list[Statement], list[Diagnostic]]:
    """Read one record's tags into statements, keeping every tag that does not make sense visible."""
    fingerprint = _fingerprint(root / name)
    prose = without_code(text)
    open_tags: list[tuple[int, re.Match[str]]] = []
    spans: list[tuple[int, int, str]] = []
    diagnostics: list[Diagnostic] = []
    for tag in _TAG.finditer(prose):
        written = tag.group(0)
        if not written.endswith(">"):
            diagnostics.append(Diagnostic(name, _line_of(text, tag.start()), "malformed"))
            continue
        if written.startswith("</"):
            if not open_tags:
                diagnostics.append(Diagnostic(name, _line_of(text, tag.start()), "never opened"))
                continue
            _, opened = open_tags.pop()
            spans.append((opened.start(), tag.end(), opened.group(0)))
        else:
            open_tags.append((tag.start(), tag))
    diagnostics += [
        Diagnostic(name, _line_of(text, opened.start()), "never closed") for _, opened in open_tags
    ]
    statements = _nested(name, text, fingerprint, sorted(spans))
    return statements, diagnostics + _attribute_problems(root, statements)


def _nested(
    name: str, text: str, fingerprint: str, spans: list[tuple[int, int, str]]
) -> list[Statement]:
    """Turn raw spans into statements that know their depth and how many children they hold."""
    statements = []
    for start, end, written in spans:
        attributes = dict(_ATTRIBUTE.findall(written))
        parents = [other for other in spans if _holds(other, (start, end))]
        children = [other for other in spans if _holds((start, end), other)]
        direct = [child for child in children if not any(_holds(kin, child) for kin in children)]
        statements.append(
            Statement(
                path=name,
                opens=_line_of(text, start),
                closes=_line_of(text, end - 1),
                until=attributes.get("until"),
                ticket=attributes.get("ticket"),
                depth=len(parents),
                contains=len(direct),
                fingerprint=fingerprint,
                span=(start, end),
            )
        )
    return statements


def _holds(outer, inner) -> bool:
    """Whether one span strictly encloses another. Equal spans are the same statement, not nesting."""
    return outer[0] < inner[0] and inner[1] <= outer[1]


def _attribute_problems(root: Path, statements: list[Statement]) -> list[Diagnostic]:
    """An expiry nobody owns, or one nobody can test, is a finding — never a silent pass."""
    problems = []
    for statement in statements:
        if statement.until is None:
            problems.append(Diagnostic(statement.path, statement.opens, "no condition"))
        if statement.ticket is None:
            problems.append(Diagnostic(statement.path, statement.opens, "unbound"))
        elif not (root / statement.ticket).is_file():
            problems.append(Diagnostic(statement.path, statement.opens, "unknown owner"))
    return problems


def _records_in(root: Path, paths: list[str]) -> list[str]:
    """The markdown records a declared scope covers, in a stable order.

    A path naming nothing is refused rather than contributing no records: a scope the caller
    believes it declared and this tool silently dropped would report as a clean, complete scan.
    """
    found: list[str] = []
    for path in paths:
        selected = root / path
        if selected.is_dir():
            found += [
                record.relative_to(root).as_posix()
                for record in selected.rglob("*.md")
                if ".git" not in record.relative_to(root).parts
            ]
        elif selected.is_file():
            found.append(selected.relative_to(root).as_posix())
        else:
            raise Refused(f"{path} is not a record or directory of this repository")
    return sorted(set(found))


def _whole_lines_of(text: str, span: tuple[int, int]) -> tuple[int, int]:
    """Widen a block's span to the lines it occupies, when nothing else shares them."""
    start, end = span
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", end)
    line_end = len(text) if line_end == -1 else line_end + 1
    if text[line_start:start].strip() or text[end:line_end].strip():
        return span
    return line_start, line_end


def _line_of(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _fingerprint(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _inside_repository(root: Path, name: str) -> bool:
    try:
        return (root / name).resolve().is_relative_to(root.resolve())
    except OSError:
        return False


def _read(path: Path) -> str:
    with path.open(encoding="utf-8", newline="") as handle:
        return handle.read()


def _replace_content(path: Path, text: str) -> None:
    """Write through a neighbouring temporary file, so a failed write never truncates the original."""
    staging = path.with_name(path.name + ".maintain-tmp")
    with staging.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    staging.replace(path)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
