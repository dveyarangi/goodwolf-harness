"""What each mechanism declares itself to be made of, and whether the declaration is true.

    uv run --offline --no-project python .agents/scripts/mechanisms.py --check
    uv run --offline --no-project python .agents/scripts/mechanisms.py --index

`--check` reads every declaration under `.agents/mechanisms/` and reports its parts, its moments
and what does not hold. `--index` renders the register from the same directories; no file holds
it, and none is written.

The script rules on form alone. Whether a moment should exist, whether an absence is honestly
classified, and whether the prose is any good are judgements it records and never makes.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from docs_corpus import cited_record, citations, target_of  # noqa: E402  (path set just above)

MECHANISMS = ".agents/mechanisms"
KINDS = ("elsewhere", "embedded", "unowned by design", "not yet")
GRADING = "## What would show it working"
PRODUCES = "## What it produces, and who reads it"
STATES = ("always on", "installed")
MOMENTS_TABLE = "## Moments"
PARTS_TABLE = "## Install adds, uninstall removes"
RELIED_ON_TABLE = "## Relies on, and does not own"
TABLES = {
    MOMENTS_TABLE: ("moment", "instructed by", "kind, and why"),
    PARTS_TABLE: ("part", "where"),
    RELIED_ON_TABLE: ("part", "where", "owner"),
}
_COLUMN = re.compile(r"(?<!\\)\|")
_LINK = re.compile(r"\[[^\]]*\]\([^)]*\)")
_CODE = re.compile(r"`[^`]*`")
_USAGE = "usage: mechanisms.py --check | --index"


@dataclass(frozen=True)
class Moment:
    """One occasion a person acts on the mechanism, with its instruction or its declared absence."""

    occasion: str
    instructed_by: str | None
    kind: str | None
    why: str
    referent: str | None

    def as_record(self) -> dict:
        return {
            "moment": self.occasion,
            "instructed by": self.instructed_by,
            "kind": self.kind,
            "why": self.why,
            "referent": self.referent,
        }


@dataclass(frozen=True)
class Part:
    """A file the mechanism owns, or one it leans on — `owner` is what tells the two apart."""

    role: str
    where: str
    anchor: str | None
    owner: str | None

    def as_record(self) -> dict:
        return {"part": self.role, "where": self.where, "anchor": self.anchor, "owner": self.owner}


@dataclass(frozen=True)
class Declaration:
    """One mechanism as its doc declares it. Nothing here has been checked against the tree."""

    slug: str
    doc: str
    instruction: str | None
    state: str | None
    rules: str | None
    evidence: str | None
    declared_by: str | None
    moments: list[Moment]
    parts: list[Part]
    relied_on: list[Part]

    def as_record(self) -> dict:
        return {
            "mechanism": self.slug,
            "doc": self.doc,
            "instruction": self.instruction,
            "state": self.state,
            "rules": self.rules,
            "evidence": self.evidence,
            "declared by": self.declared_by,
            "moments": [moment.as_record() for moment in self.moments],
            "parts": [part.as_record() for part in self.parts],
            "relies on": [part.as_record() for part in self.relied_on],
        }


@dataclass(frozen=True)
class Diagnostic:
    """Something a person must settle before the declaration can be called true."""

    mechanism: str
    problem: str

    def as_record(self) -> dict:
        return {"mechanism": self.mechanism, "problem": self.problem}


@dataclass(frozen=True)
class Skipped:
    """A check that could not run. Reporting it is what stops a skip from reading as a pass."""

    mechanism: str
    check: str
    why: str

    def as_record(self) -> dict:
        return {"mechanism": self.mechanism, "check": self.check, "why": self.why}


@dataclass(frozen=True)
class Checked:
    """What one reading of every declaration found, including what it could not look at."""

    declarations: list[Declaration]
    diagnostics: list[Diagnostic]
    skipped: list[Skipped]

    def as_record(self) -> dict:
        return {
            "declarations": [declared.as_record() for declared in self.declarations],
            "diagnostics": [note.as_record() for note in self.diagnostics],
            "skipped": [passed_over.as_record() for passed_over in self.skipped],
        }


def main(argv: list[str], root: Path | None = None) -> int:
    root = root or Path(__file__).resolve().parents[2]
    if argv == ["--check"]:
        checked = check(root)
        print(json.dumps(checked.as_record(), indent=2))
        return 1 if checked.diagnostics else 0
    if argv == ["--index"]:
        print(index(root))
        return 0
    print(_USAGE)
    return 2


def index(root: Path) -> str:
    """The register, rendered from the directories. No file holds it and none is written."""
    rows = ["| mechanism | what it is | instruction | state |", "|---|---|---|---|"]
    for directory in _directories(root):
        rows.append("| " + " | ".join(_entry(directory)) + " |")
    return "\n".join(rows)


def _entry(directory: Path) -> tuple[str, str, str, str]:
    """One record, read as far as it can be. A doc that will not parse says so and keeps its row."""
    slug = directory.name
    doc = directory / f"{slug}.md"
    if not doc.is_file():
        return slug, "no doc in the directory", "—", "—"
    text = doc.read_text(encoding="utf-8")
    bullets = _bullets(text)
    summary = _summary(text)
    if summary is None:
        return slug, "the doc does not open with a title line", "—", "—"
    return slug, summary, f"`{bullets.get('instruction', '—')}`", bullets.get("state", "—")


def _summary(text: str) -> str | None:
    """What the doc's title says the mechanism is, in its own words."""
    first = text.splitlines()[0] if text.splitlines() else ""
    if not first.startswith("# ") or " — " not in first:
        return None
    return first.partition(" — ")[2].strip()


def check(root: Path) -> Checked:
    """Every declaration under `.agents/mechanisms/`, with what does not hold about it."""
    declarations: list[Declaration] = []
    diagnostics: list[Diagnostic] = []
    for directory in _directories(root):
        doc = directory / f"{directory.name}.md"
        if not doc.is_file():
            diagnostics.append(Diagnostic(directory.name, f"{directory.name} holds no doc"))
            continue
        text = doc.read_text(encoding="utf-8")
        declared = _declaration(root, directory, text)
        declarations.append(declared)
        diagnostics += _problems(root, declared, text)
    return Checked(declarations, diagnostics, _skipped(declarations))


def _skipped(declarations: list[Declaration]) -> list[Skipped]:
    """The checks a legitimately absent field disables, named so a quiet run is not read as clean."""
    return [
        Skipped(
            declared.slug,
            "a not yet row may not name the ticket that declares this mechanism",
            "the doc states no declared by",
        )
        for declared in declarations
        if not declared.declared_by
    ]


def _problems(root: Path, declared: Declaration, text: str) -> list[Diagnostic]:
    """Everything about one declaration that the tree, or the doc's own shape, contradicts."""
    notes = []
    if GRADING not in text:
        notes.append(Diagnostic(declared.slug, "the doc does not say what would show it working"))
    if PRODUCES not in text:
        notes.append(
            Diagnostic(declared.slug, "the doc does not say what it produces, or who reads it")
        )
    malformed = _table_problems(declared.slug, text)
    notes += [note for group in malformed.values() for note in group]
    notes += _header_problems(root, declared)
    # A table whose shape is wrong has already been reported as that. Judging the rows it was
    # misread into would dress a parse failure up as a verdict about the mechanism.
    if not malformed[MOMENTS_TABLE]:
        notes += _moment_problems(root, declared)
    for heading, parts in ((PARTS_TABLE, declared.parts), (RELIED_ON_TABLE, declared.relied_on)):
        if not malformed[heading]:
            notes += _part_problems(root, declared.slug, parts)
    return notes


def _part_problems(root: Path, slug: str, parts: list[Part]) -> list[Diagnostic]:
    """Whether each named part is where the doc says, and still says what the doc anchors on."""
    notes = []
    for part in parts:
        named = root / part.where
        if not named.exists():
            notes.append(Diagnostic(slug, f"{part.where} does not resolve"))
        elif part.anchor and part.anchor not in named.read_text(encoding="utf-8"):
            notes.append(Diagnostic(slug, f'{part.where} does not say "{part.anchor}"'))
    return notes


def _directories(root: Path) -> list[Path]:
    home = root / MECHANISMS
    return sorted(path for path in home.glob("*") if path.is_dir()) if home.is_dir() else []


def _declaration(root: Path, directory: Path, text: str) -> Declaration:
    slug = directory.name
    doc = directory / f"{slug}.md"
    bullets = _bullets(text)
    return Declaration(
        slug=slug,
        doc=doc.relative_to(root).as_posix(),
        instruction=bullets.get("instruction"),
        state=bullets.get("state"),
        rules=_rules_file(root, directory),
        evidence=bullets.get("evidence"),
        declared_by=bullets.get("declared by"),
        moments=[
            _moment(root, doc.relative_to(root).as_posix(), row)
            for row in _rows(text, "## Moments")
        ],
        parts=[_part(row) for row in _rows(text, "## Install adds, uninstall removes")],
        relied_on=[_part(row) for row in _rows(text, "## Relies on, and does not own")],
    )


def _header_problems(root: Path, declared: Declaration) -> list[Diagnostic]:
    """The bullets a declaration stands on: its instruction, the state it is in, its rules file."""
    return (
        _instruction_problems(root, declared)
        + _state_problems(declared)
        + _project_local_problems(root, declared)
        + _directory_problems(root, declared)
    )


def _instruction_problems(root: Path, declared: Declaration) -> list[Diagnostic]:
    """The one bullet a mechanism cannot be declared without, and the file it must not be."""
    if not declared.instruction:
        return [Diagnostic(declared.slug, "no instruction bullet")]
    if declared.instruction == declared.doc:
        return [Diagnostic(declared.slug, "the instruction file is the doc")]
    if not (root / declared.instruction).is_file():
        return [Diagnostic(declared.slug, f"{declared.instruction} does not resolve")]
    return []


def _state_problems(declared: Declaration) -> list[Diagnostic]:
    """Which state a mechanism is in decides how its parts table reads, so it is not free text."""
    if declared.state in STATES:
        return []
    said = declared.state or "nothing"
    return [Diagnostic(declared.slug, f"the state is {said}, not one of {' or '.join(STATES)}")]


def _project_local_problems(root: Path, declared: Declaration) -> list[Diagnostic]:
    """The two optional records. Absent is a state; named and unresolvable is a defect.

    `declared by` is read by the rule that a `not yet` row may not name this mechanism's own
    migration ticket. An unresolvable one makes that comparison match nothing, so the diagnostic
    stops firing without ever saying it stopped.
    """
    return [
        Diagnostic(declared.slug, f"{named} does not resolve")
        for named in (declared.evidence, declared.declared_by)
        if named and not (root / named).is_file()
    ]


def _directory_problems(root: Path, declared: Declaration) -> list[Diagnostic]:
    """Whether the directory holds anything but the two files a mechanism's own name accounts for.

    A mechanism directory holds its doc and its rules file; working parts live where the harness
    needs them. Anything else put here was put here to be read, and nothing reads it.
    """
    directory = (root / declared.doc).parent
    accounted = {f"{declared.slug}.md", f"{declared.slug}.rules.md"}
    return [
        Diagnostic(declared.slug, f"nothing reads {stray.name}, which sits in the mechanism's directory")
        for stray in sorted(directory.glob("*"))
        if stray.is_file() and stray.name not in accounted
    ]


def _table_problems(slug: str, text: str) -> dict[str, list[Diagnostic]]:
    """Per table: whether it is the one its heading promises, and whether its rows are that wide."""
    found = {}
    for heading, expected in TABLES.items():
        named = heading.lstrip("# ")
        lines = _table_lines(text, heading)
        notes = []
        if not lines:
            if heading == MOMENTS_TABLE:
                notes.append(Diagnostic(slug, f"{named} carries no table"))
            found[heading] = notes
            continue
        header = _cells(lines[0])
        missing = [column for column in expected if column not in header]
        if missing:
            notes.append(Diagnostic(slug, f"{named} has no {', '.join(missing)} column"))
        notes += [
            Diagnostic(
                slug,
                f"a row under {named} has {len(_cells(line))} cells "
                f"where the header has {len(header)}",
            )
            for line in lines[2:]
            if len(_cells(line)) != len(header)
        ]
        found[heading] = notes
    return found


def _moment_problems(root: Path, declared: Declaration) -> list[Diagnostic]:
    """What each row leaves unsettled: a missing referent, or one the tree does not have."""
    notes = []
    for moment in declared.moments:
        notes += _row_problems(declared.slug, moment)
        if moment.kind not in ("elsewhere", "embedded", "not yet"):
            continue
        if not moment.referent:
            notes.append(
                Diagnostic(declared.slug, f"'{moment.occasion}' is {moment.kind} and names nothing")
            )
            continue
        named = moment.referent
        if not (root / named).exists():
            notes.append(
                Diagnostic(declared.slug, f"'{moment.occasion}' names {named}, which does not resolve")
            )
        elif moment.kind == "not yet" and named == declared.declared_by:
            notes.append(
                Diagnostic(
                    declared.slug,
                    f"'{moment.occasion}' names {named}, the ticket this doc is declared by; "
                    "that ticket closes when the mechanism reaches the shape",
                )
            )
    return notes


def _row_problems(slug: str, moment: Moment) -> list[Diagnostic]:
    """Whether the row says one thing: instructed, or absent for a stated reason."""
    where = f"'{moment.occasion}'"
    if moment.kind is None:
        if moment.why:
            return [Diagnostic(slug, f"{where} declares no known kind: {moment.why}")]
        if moment.instructed_by is None:
            return [Diagnostic(slug, f"{where} carries neither an instruction nor an absence")]
        return []
    if moment.instructed_by is not None:
        return [Diagnostic(slug, f"{where} carries both an instruction and an absence")]
    if not moment.why:
        return [Diagnostic(slug, f"{where} is {moment.kind} and does not say why")]
    if moment.kind == "unowned by design" and moment.referent:
        return [Diagnostic(slug, f"{where} is unowned by design and still names {moment.referent}")]
    return []


def _rules_file(root: Path, directory: Path) -> str | None:
    """The mechanism's rules file, found by name. A mechanism that injects nothing has none."""
    named = directory / f"{directory.name}.rules.md"
    return named.relative_to(root).as_posix() if named.is_file() else None


def _bullets(text: str) -> dict[str, str]:
    """The header's `- **name** value` lines, read as written.

    The header is what precedes the first section, so a bullet written in prose further down
    states nothing about the mechanism and cannot quietly replace one that does.
    """
    found: dict[str, str] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            break
        if not stripped.startswith("- **"):
            continue
        name, _, rest = stripped[4:].partition("**")
        found[name.strip()] = _value(rest)
    return found


def _value(rest: str) -> str:
    """A bullet's value: a backticked path, or the bare words that follow the name."""
    text = rest.strip()
    if text.startswith("`"):
        return text[1:].partition("`")[0]
    return text.partition(" — ")[0].strip()


def _rows(text: str, heading: str) -> list[list[str]]:
    """A section's table rows, header and separator dropped."""
    lines = _table_lines(text, heading)
    return [_cells(line) for line in lines[2:]]


def _table_lines(text: str, heading: str) -> list[str]:
    lines = text.splitlines()
    if heading not in lines:
        return []
    after = lines[lines.index(heading) + 1 :]
    table = []
    for line in after:
        if line.startswith("|"):
            table.append(line)
        elif table:
            break
    return table


def _cells(line: str) -> list[str]:
    """A row's cells, split on unescaped pipes. A literal pipe is written `\\|` and read back."""
    return [cell.strip().replace("\\|", "|") for cell in _COLUMN.split(line.strip().strip("|"))]


def _moment(root: Path, citing: str, row: list[str]) -> Moment:
    occasion, instructed, absence = (row + ["", "", ""])[:3]
    kind, why, referent = _absence(root, citing, absence)
    return Moment(occasion, _backticked(instructed), kind, why, referent)


def _absence(root: Path, citing: str, cell: str) -> tuple[str | None, str, str | None]:
    """The kind an uninstructed row declares, the clause saying why, and what it points at.

    A referent is written one of two ways and they resolve differently: a ticket arrives as a
    markdown link, relative to the doc so that moving the ticket repairs it, and everything else
    as a backticked path from the repository root.
    """
    written = cell.strip()
    kind = next((name for name in KINDS if written.startswith(name)), None)
    if kind is None:
        return None, written, None
    cited = citations(written)
    referent = (
        cited_record(root, citing, target_of(cited[0])) if cited else _backticked(written)
    )
    return kind, _clause(written[len(kind) :]), referent


def _clause(rest: str) -> str:
    """The words saying why, with the referent taken out — a link or a path is not a reason."""
    words = _LINK.sub("", rest)
    words = _CODE.sub("", words)
    return words.strip(" —-,.;:").strip()


def _part(row: list[str]) -> Part:
    role, where = (row + ["", ""])[:2]
    owner = row[2] if len(row) > 2 else None
    anchor = where.partition('→ "')[2].rpartition('"')[0] or None
    return Part(role, _backticked(where) or where, anchor, owner)


def _backticked(cell: str) -> str | None:
    if "`" not in cell:
        return None
    return cell.partition("`")[2].partition("`")[0]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
