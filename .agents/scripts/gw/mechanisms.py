# Mechanism: mechanism-shape
"""What each mechanism declares itself to be made of, and whether the declaration is true.

    uv run --offline --no-project python .agents/scripts/gw/mechanisms.py --check
    uv run --offline --no-project python .agents/scripts/gw/mechanisms.py --index

`--check` reads every declaration under `.agents/mechanisms/` and reports its parts, its moments
and what does not hold; then it asks the reverse question — is every installed skill named by a
declaration, or does it say on its own first line that none does yet — and reports each skill
with who claims it; then it holds every skill, script, test and hook a mechanism owns to naming
that mechanism on its first line, and no script to naming one whose parts omit it, per the
format's *A part's claim*; then it holds core to citing only what its mechanisms declare — every path
under `docs/` a core file names is a painted door, is skipped inside an instance-owned block, is
local — named by a file of a mechanism whose owner is `local`, the project's own — or is a leak
that fails the run. In a recipient — a tree whose
entry file announces `<repository>@<ref>` — a `not yet` standing alone, with no binding, is
upstream's gap, since the harness mechanism sheared the binding on the way, and draws nothing; one
with words after it or an empty wrapper is the tree's own writing and fails, as every unbound one
does at the origin. `--index` renders the register from the same directories; no file holds it, and none is
written.

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

import questions  # noqa: E402  (path set just above)
from docs_corpus import (  # noqa: E402  (path set just above)
    RETIRED_TAG,
    SCRIPTS,
    UnreadableCode,
    announced,
    corpus,
    docs_mentioned,
    docs_mentioned_in_code,
    without_code,
    wrapper_of,
)

MECHANISMS = ".agents/mechanisms"
SKILLS = ".agents/skills"
# Where a mechanism's code lives, every file of it naming its mechanism on its first line.
SCRIPTS_ROOT = ".agents/scripts/"
CORE = ".agents/"
ENTRY_FILE = "AGENTS.md"
TESTS = SCRIPTS + "test/"
# The origin's front page, shipped beside the harness skill: the origin's own document, not core
# text, so what it cites is skipped and reported rather than read as a leak.
FRONT_PAGE = ".agents/skills/harness/README.md"
# What core may name under `docs/`: a painted door — a record some mechanism declares, the directory
# or the one file — and never a particular record behind it. Held here by hand until each owner's
# declaration parses; a row leaves with the ticket that makes it readable, and when the last is
# gone the check reads declarations alone.
PAINTED_DOORS = frozenset(
    (
        # TODO q-la5n2i: the ticket mechanism's records and the shape's evidence are declared in
        # prose; these rows go when `record-bearing` parses.
        "docs/tickets/",
        "docs/tickets/done/",
        # TODO q-la5n2i: the question store's entries are declared in the questions skill's
        # prose, the sessions' rows beside the conclude's; these rows go when `record-bearing` parses.
        "docs/questions/",
        # TODO q-ubd6uz: goes when dotted ids stop being read; an unmigrated tree still holds this folder.
        "docs/questions/done/",
        # The table of the ids a tree's migration replaced, which the store's script reads.
        "docs/questions/former-ids.md",
        "docs/questions/sessions.d/",
        "docs/sessions/rows/",
        # The single sessions file a store from before holds, read until its first write carries it.
        "docs/questions/sessions",
        "docs/mechanisms/",
        # TODO q-la5n2i: the maintain mechanism's marks, declared in its skill's prose until each
        # mechanism's records are declared where a script reads them.
        "docs/mechanisms/maintenance.md",
        # TODO q-pdmw3a: the glossary's, which goes with the glossary mechanism's declaration.
        "docs/glossary.md",
        # TODO q-hrfk7l: the practice's, which go with the homes of decisions.
        "docs/architecture.md",
        "docs/adr/",
        # TODO q-oehis2: /plan's, which go with its declaration.
        "docs/rfc/",
        "docs/rfc/done/",
        # TODO q-d4pypx: /conclude's, which goes with its declaration.
        "docs/sessions/",
        # TODO q-h4dbp3: /dream's, which goes with its declaration.
        "docs/dreams/",
        # TODO q-3cx2m3: /setup-devops's, which goes with its declaration.
        "docs/cicd.md",
        # TODO q-la5n2i: the pathfinder's roadmap, declared in its skill's prose; this row goes
        # when `record-bearing` parses.
        "docs/roadmap.md",
        # TODO q-la5n2i: the edge mechanism's records, declared in its format shelf's prose;
        # this row goes when `record-bearing` parses.
        "docs/edge/",
        # TODO q-la5n2i: the product mechanism's document, declared in its format shelf's prose;
        # this row goes when `record-bearing` parses.
        "docs/product.md",
        # TODO q-tt733j: the register.
        "docs/rule-failures.md",
    )
)
KINDS = ("elsewhere", "embedded", "unowned by design", "not yet")
# A skill's own claim says no mechanism names it yet. Every skill is owned (the user, 2026-11-16):
# `unowned by design` is a moment's kind and no claim, and a kind that points at an owner is not one.
CLAIM = "Mechanism:"
CLAIM_KINDS = ("not yet",)
GRADING = "## What would show it working"
PRODUCES = "## What it produces, and who reads it"
STATES = ("always on", "installed")
# Whose a mechanism is: core's, which ships, or the project's own, which stays where it was made
# and reserves nothing in another tree (the user, 2026-11-15 and 2026-11-16).
OWNER = "owner"
CORE_OWNED = "core"
LOCAL = "local"
OWNERS = (CORE_OWNED, LOCAL)
# A part outside the core directory opens with its mechanism's claim unless its format holds no
# comment: a document, a data file, a file that is not text.
CLAIMLESS = (".md", ".txt", ".json", ".jsonl", ".csv", ".tsv")
COMMENT_LEADERS = ("#", "//", "--", ";")
# A record's kind by its source of truth, as the method's glossary sorts them. An output that is
# another mechanism's record takes that format's kind, so the produces section may say only that.
RECORD_KINDS = ("what it intends to become", "what must always hold", "what exists", "what happened")
OUTPUT_KINDS = (*RECORD_KINDS, "its format's")
# A doc is the record of why an instruction is what it is: the instruction is repaired to it.
DOC_KIND = "what must always hold"
# The bullet a record carries its kind under, read as what the record is a record of; `.0030`
# named it `kind`, and a doc still carrying that name is told so rather than passed over.
MARK = "record of"
FORMER_MARK = "kind"
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
_TARGET = re.compile(r"^- \*\*target\*\* `([^`]+)`", re.M)
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
    instructions: tuple[str, ...]
    state: str | None
    kind: str | None
    kind_under_former_mark: str | None
    owner: str | None
    rules: str | None
    moments: list[Moment]
    parts: list[Part]
    relied_on: list[Part]

    @property
    def local(self) -> bool:
        """Whether the mechanism is the project's own: it ships nowhere, and the tree that holds
        it maintains it."""
        return self.owner == LOCAL

    def as_record(self) -> dict:
        return {
            "mechanism": self.slug,
            "doc": self.doc,
            "instruction": list(self.instructions),
            "state": self.state,
            "owner": self.owner,
            "rules": self.rules,
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
class Claim:
    """What a skill says about its mechanism on its own first line, when no declaration names it."""

    kind: str | None
    why: str
    referent: str | None
    # A wrapped `not yet` followed by words: the question is the reason, and the body says none.
    stray: bool = False

    def as_record(self) -> dict:
        return {"kind": self.kind, "why": self.why, "referent": self.referent}


@dataclass(frozen=True)
class Skill:
    """One installed skill and who claims it: a declaration's instruction bullet, or the skill itself."""

    directory: str
    named_by: list[str]
    claim: Claim | None

    def as_record(self) -> dict:
        return {
            "skill": self.directory,
            "named by": self.named_by,
            "claims": self.claim.as_record() if self.claim else None,
        }


@dataclass(frozen=True)
class Citation:
    """One path under `docs/` a core file names, and where it stands: a painted door, skipped
    inside an instance-owned block, local in a file of a local mechanism, or a leak."""

    file: str
    line: int
    cites: str
    standing: str

    def as_record(self) -> dict:
        return {"file": self.file, "line": self.line, "cites": self.cites}


STANDINGS = {"painted door": "painted doors", "skipped": "skipped", "local": "local", "leak": "leaks"}


@dataclass(frozen=True)
class LocalFiles:
    """The files of a tree's local mechanisms, each with the mechanism it is of: everything in a
    local mechanism's directory and in the folder of a skill that claims it, and each part that
    opens with its claim."""

    folders: dict[str, str]
    parts: dict[str, str]

    @property
    def mechanisms(self) -> tuple[str, ...]:
        """The slugs of the tree's local mechanisms."""
        return tuple(sorted(set(self.folders.values())))

    def owner_of(self, name: str) -> str | None:
        """The local mechanism a file is of, or `None` for a file that is core's."""
        if name in self.parts:
            return self.parts[name]
        return next((slug for folder, slug in self.folders.items() if name.startswith(folder)), None)


@dataclass(frozen=True)
class Checked:
    """What one reading of every declaration found. Every check here can always run."""

    declarations: list[Declaration]
    skills: list[Skill]
    cites: list[Citation]
    diagnostics: list[Diagnostic]

    def as_record(self) -> dict:
        # Four classes and never a total: an exclusion nobody can see is the review this replaces.
        return {
            "declarations": [declared.as_record() for declared in self.declarations],
            "skills": [skill.as_record() for skill in self.skills],
            "core cites": {
                key: [cite.as_record() for cite in self.cites if cite.standing == standing]
                for standing, key in STANDINGS.items()
            },
            "diagnostics": [note.as_record() for note in self.diagnostics],
        }


def main(argv: list[str], root: Path) -> int:
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
    named = _instructions(text)
    return slug, summary, ", ".join(f"`{each}`" for each in named) or "—", bullets.get("state", "—")


def _summary(text: str) -> str | None:
    """What the doc's title says the mechanism is, in its own words."""
    first = text.splitlines()[0] if text.splitlines() else ""
    if not first.startswith("# ") or " — " not in first:
        return None
    return first.partition(" — ")[2].strip()


def check(root: Path) -> Checked:
    """Every declaration under `.agents/mechanisms/`, with what does not hold about it — and, read
    the other way, every installed skill with who claims it."""
    recipient = announced(root) is not None
    diagnostics = [
        Diagnostic(directory.name, f"{directory.name} holds no doc")
        for directory in _directories(root)
        if not _doc(directory).is_file()
    ]
    held = questions.read_store(root).index
    declared = declarations(root, held)
    for one in declared:
        diagnostics += _problems(root, one, (root / one.doc).read_text(encoding="utf-8"), recipient, held)
    skills = _skills(root, declared, held)
    diagnostics += _skill_problems(root, skills, recipient, held)
    diagnostics += _naming_problems(root, declared, skills)
    local = local_files(corpus(root), lambda name: (root / name).read_bytes().decode("utf-8", errors="replace"))
    diagnostics += _leaning_problems(root, declared, local) + _stranded_problems(root, declared, local)
    cites, unreadable = _core_cites(root, local)
    diagnostics += unreadable + _leaks(cites) + _retired_tags(root)
    return Checked(declared, skills, cites, diagnostics)


def local_files(names, read) -> LocalFiles:
    """The files of every local mechanism among `names`, each read through `read`, so a tree on
    disk and a ref held in memory are sorted by one reading.

    A file is a local mechanism's by its place or by its claim, never by the declaration's word
    alone: a row naming a file of core's would otherwise excuse it from the painted doors.
    """
    held = set(names)
    folders: dict[str, str] = {}
    parts: dict[str, str] = {}
    for name in sorted(held):
        slug = declared_by(name)
        if slug is None:
            continue
        text = read(name)
        if _bullets(text).get(OWNER) != LOCAL:
            continue
        folders[f"{MECHANISMS}/{slug}/"] = slug
        for skill in _skills_named(_instructions(text)):
            if skill in held and _named_in_skill(read(skill)) == slug:
                folders[skill[: -len("SKILL.md")]] = slug
        for part in (_part(row).where for row in _rows(text, PARTS_TABLE)):
            if part in held and not part.endswith(CLAIMLESS) and _named_in_text(read(part)) == slug:
                parts[part] = slug
    return LocalFiles(folders, parts)


def rule_targets(text: str) -> list[str]:
    """Every file a rules file installs a rule into, as its rules' `target` bullets name them."""
    return _TARGET.findall(text)


def named_files(text: str) -> list[str]:
    """Every file a declaration names: its instructions, its parts, what it relies on, and what
    instructs a moment or stands as its referent."""
    named = list(_instructions(text))
    for heading in (PARTS_TABLE, RELIED_ON_TABLE):
        named += [_part(row).where for row in _rows(text, heading)]
    for row in _rows(text, MOMENTS_TABLE):
        named += [path for cell in row[1:3] if (path := _backticked(cell))]
    return named


def declared_by(name: str) -> str | None:
    """The slug of the mechanism a file is the doc of, or `None` for any other file."""
    pieces = name.split("/")
    if name.startswith(MECHANISMS + "/") and len(pieces) == 4 and pieces[3] == f"{pieces[2]}.md":
        return pieces[2]
    return None


def _leaning_problems(root: Path, declared: list[Declaration], local: LocalFiles) -> list[Diagnostic]:
    """A core mechanism that names a file of a local one — in its declaration, or as the target
    of a rule — would ship leaning on what stays."""
    notes = []
    for one in declared:
        if one.local:
            continue
        named = named_files((root / one.doc).read_text(encoding="utf-8"))
        if one.rules:
            named += rule_targets((root / one.rules).read_text(encoding="utf-8"))
        for each in dict.fromkeys(named):
            owner = local.owner_of(each)
            if owner:
                notes.append(
                    Diagnostic(one.slug, f"{each} is {owner}'s, a local mechanism's, which does not ship; core names it")
                )
    return notes


def _stranded_problems(root: Path, declared: list[Declaration], local: LocalFiles) -> list[Diagnostic]:
    """A file or a folder a local mechanism names under the core directory and nothing tells as its own —
    outside its directory and its skills' folders, opening with no claim — would ship with core
    and be held to core's rules."""
    notes = []
    for one in declared:
        if not one.local:
            continue
        for named in dict.fromkeys([*one.instructions, *(part.where for part in one.parts)]):
            if named.startswith(CORE) and (root / named).exists() and local.owner_of(named) != one.slug:
                notes.append(
                    Diagnostic(
                        one.slug,
                        f"{named} is a part of {one.slug}, a local mechanism, and nothing tells it as its own: "
                        "it would ship with core — move it into the mechanism's skill's folder, or open it with its claim",
                    )
                )
    return notes


def declarations(root: Path, held: dict[str, questions.Entry] | None = None) -> list[Declaration]:
    """Every mechanism a doc under `.agents/mechanisms/` declares, read as written and unchecked.

    The one reading both the shape check and the re-check clock stand on, so the two cannot
    disagree about what a mechanism is made of. A directory holding no doc declares nothing. A
    `not yet` gives as its reason the words of the question it waits on, read from the store.
    """
    held = questions.read_store(root).index if held is None else held
    return [
        _declaration(root, directory, _doc(directory).read_text(encoding="utf-8"), held)
        for directory in _directories(root)
        if _doc(directory).is_file()
    ]


def _doc(directory: Path) -> Path:
    return directory / f"{directory.name}.md"


def _core_cites(root: Path, local: LocalFiles) -> tuple[list[Citation], list[Diagnostic]]:
    """Every path under `docs/` a file under the core directory or the entry file names, with
    its standing; and the scripts that could not be read, which are diagnostics rather than
    passes. A rule a local mechanism installed into a core file is the instance's, as the local
    block is."""
    cites: list[Citation] = []
    unreadable: list[Diagnostic] = []
    for name in _core_files(root):
        text = (root / name).read_text(encoding="utf-8")
        if name.endswith(".md"):
            mentions = docs_mentioned(root, name, text, local.mechanisms)
        else:
            try:
                mentions = docs_mentioned_in_code(text)
            except UnreadableCode as error:
                unreadable.append(Diagnostic(name, f"{name} could not be read for citations: {error}"))
                continue
        cites += [Citation(name, seen.line, seen.path, _standing(name, seen, local)) for seen in mentions]
    return cites, unreadable


def _core_files(root: Path) -> list[str]:
    """What ships and is read: every `.md` and every non-test `.py` under `.agents/`, and the entry
    file. A test's `docs/` literal is fixture data for a tree the test builds."""
    return [
        name
        for name in corpus(root)
        if name == ENTRY_FILE
        or (name.startswith(CORE) and (name.endswith(".md") or (name.endswith(".py") and not name.startswith(TESTS))))
    ]


def _standing(name: str, seen, local: LocalFiles) -> str:
    """Where one mention stands. A local mechanism travels nowhere, so what its files name under
    `docs/` is the project's own and reserves nothing in another tree."""
    if name == FRONT_PAGE or seen.instance_owned:
        return "skipped"
    if local.owner_of(name):
        return "local"
    if seen.path in PAINTED_DOORS or seen.path + "/" in PAINTED_DOORS:
        return "painted door"
    return "leak"


def _retired_tags(root: Path) -> list[Diagnostic]:
    """A `<project-local>` block left in core: the tag is retired, and a local fact is written in
    the local file. Read through the code-blanked text, so an illustration is not a block."""
    found = []
    for name in _core_files(root):
        if not name.endswith(".md"):
            continue
        seen = without_code((root / name).read_text(encoding="utf-8"))
        at = seen.find(RETIRED_TAG)
        while at != -1:
            line = seen.count("\n", 0, at) + 1
            found.append(
                Diagnostic(
                    name,
                    f"{name}:{line} writes a {RETIRED_TAG} block; the tag is retired, and a local fact "
                    "is written in the local file — AGENTS.md § Project-local",
                )
            )
            at = seen.find(RETIRED_TAG, at + 1)
    return found


def _leaks(cites: list[Citation]) -> list[Diagnostic]:
    return [
        Diagnostic(cite.file, f"{cite.file}:{cite.line} cites {cite.cites}, a document only the instance has")
        for cite in cites
        if cite.standing == "leak"
    ]


def _problems(
    root: Path, declared: Declaration, text: str, recipient: bool, held: dict[str, questions.Entry]
) -> list[Diagnostic]:
    """Everything about one declaration that the tree, or the doc's own shape, contradicts."""
    notes = []
    if GRADING not in text:
        notes.append(Diagnostic(declared.slug, "the doc does not say what would show it working"))
    if PRODUCES not in text:
        notes.append(
            Diagnostic(declared.slug, "the doc does not say what it produces, or who reads it")
        )
    else:
        notes += _output_problems(declared.slug, text)
    malformed = _table_problems(declared.slug, text)
    notes += [note for group in malformed.values() for note in group]
    notes += _header_problems(root, declared)
    # A table whose shape is wrong has already been reported as that. Judging the rows it was
    # misread into would dress a parse failure up as a verdict about the mechanism.
    if not malformed[MOMENTS_TABLE]:
        notes += _moment_problems(root, declared, recipient, held)
        notes += [
            Diagnostic(
                declared.slug,
                f"'{occasion}' is not yet and says why in its body; the reason is the question it is bound to",
            )
            for occasion, _, absence in ((row + ["", "", ""])[:3] for row in _rows(text, MOMENTS_TABLE))
            if _stray_reason(absence)
        ]
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


def _declaration(root: Path, directory: Path, text: str, held: dict[str, questions.Entry]) -> Declaration:
    slug = directory.name
    doc = directory / f"{slug}.md"
    bullets = _bullets(text)
    citing = doc.relative_to(root).as_posix()
    return Declaration(
        slug=slug,
        doc=citing,
        instructions=_instructions(text),
        state=bullets.get("state"),
        kind=bullets.get(MARK),
        kind_under_former_mark=bullets.get(FORMER_MARK),
        owner=bullets.get(OWNER),
        rules=_rules_file(root, directory),
        moments=[_moment(row, held) for row in _rows(text, "## Moments")],
        parts=[_part(row) for row in _rows(text, "## Install adds, uninstall removes")],
        relied_on=[_part(row) for row in _rows(text, "## Relies on, and does not own")],
    )


def _header_problems(root: Path, declared: Declaration) -> list[Diagnostic]:
    """The bullets a declaration stands on: its instruction, the state it is in, its kind, its
    owner, its rules file."""
    return (
        _instruction_problems(root, declared)
        + _state_problems(declared)
        + _kind_problems(declared)
        + _owner_problems(declared)
        + _directory_problems(root, declared)
    )


def _instruction_problems(root: Path, declared: Declaration) -> list[Diagnostic]:
    """The bullet a mechanism cannot be declared without — one per skill it owns, each the act at
    one of its moments (the user, 2026-10-10) — and the file none of them may be."""
    if not declared.instructions:
        return [Diagnostic(declared.slug, "no instruction bullet")]
    problems = []
    for named in declared.instructions:
        if named == declared.doc:
            problems.append(Diagnostic(declared.slug, "the instruction file is the doc"))
        elif not (root / named).is_file():
            problems.append(Diagnostic(declared.slug, f"{named} does not resolve"))
    return problems


def _state_problems(declared: Declaration) -> list[Diagnostic]:
    """Which state a mechanism is in decides how its parts table reads, so it is not free text."""
    if declared.state in STATES:
        return []
    said = declared.state or "nothing"
    return [Diagnostic(declared.slug, f"the state is {said}, not one of {' or '.join(STATES)}")]


def _owner_problems(declared: Declaration) -> list[Diagnostic]:
    """A declaration says whose the mechanism is: core's, which ships, or local. Nothing is
    core's by silence, so a doc that names no owner is told the bullet to write."""
    if declared.owner in OWNERS:
        return []
    admitted = " or ".join(f"`- **{OWNER}** {each}`" for each in OWNERS)
    if declared.owner is None:
        return [Diagnostic(declared.slug, f"the doc names no owner: its header says {admitted}")]
    return [Diagnostic(declared.slug, f"the owner is {declared.owner}: the header says {admitted}")]


def _kind_problems(declared: Declaration) -> list[Diagnostic]:
    """A doc carries its kind on itself, so the agent editing it meets the kind in context before
    adding what the kind refuses (the user, 2026-10-08); the format is the kind's authored home,
    and this holds the two equal."""
    expected = f"`- **{MARK}** {DOC_KIND}`"
    if declared.kind_under_former_mark is not None:
        return [Diagnostic(declared.slug, f"the doc carries its kind as `- **{FORMER_MARK}**`: write {expected}")]
    if declared.kind == DOC_KIND:
        return []
    if declared.kind is None:
        return [Diagnostic(declared.slug, f"the doc names no kind: its header says {expected}")]
    return [Diagnostic(declared.slug, f"the doc's kind is {declared.kind}, and a doc is {DOC_KIND}")]


def _output_problems(slug: str, text: str) -> list[Diagnostic]:
    """Each output the produces section lists, and whether it names a kind the format admits.

    An output is a top-level `- **name**` line of the section; its prose and nested bullets are
    read by people and name nothing the check holds.
    """
    admitted = ", ".join(OUTPUT_KINDS)
    notes = []
    for output, kind in _outputs(text):
        if kind is None:
            notes.append(
                Diagnostic(slug, f"'{output}' names no kind: write `— *<kind>* —` after its name, one of {admitted}")
            )
        elif not _admitted(kind):
            notes.append(
                Diagnostic(slug, f"'{output}' names a kind the format does not admit, '{kind}': one of {admitted}")
            )
    return notes


def _outputs(text: str) -> list[tuple[str, str | None]]:
    """The produces section's outputs, each with the kind written after its name, or none.

    The kind is the italic between the first two dashes after the name, so a path or a comma
    beside the name is allowed and an italic later in the reader's prose is never taken for it.
    """
    lines = text.splitlines()
    found = []
    for line in lines[lines.index(PRODUCES) + 1 :]:
        if line.startswith("## "):
            break
        if not line.startswith("- **"):
            continue
        name, _, rest = line[4:].partition("**")
        segments = rest.split(" — ")
        written = segments[1].strip() if len(segments) > 1 else ""
        kind = written[1:].partition("*")[0].strip() if written.startswith("*") else None
        found.append((name.strip(), kind))
    return found


def _admitted(kind: str) -> bool:
    """One of the format's kinds, or a first one followed by the rule that moves it on."""
    return any(kind == each or kind.startswith(f"{each},") for each in OUTPUT_KINDS)


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


def _moment_problems(
    root: Path, declared: Declaration, recipient: bool, held: dict[str, questions.Entry]
) -> list[Diagnostic]:
    """What each row leaves unsettled: a missing referent, or one the tree does not have."""
    return [
        note
        for moment in declared.moments
        for note in _absence_problems(root, declared.slug, moment, recipient, held)
    ]


def _absence_problems(
    root: Path, slug: str, moment: Moment, recipient: bool, held: dict[str, questions.Entry]
) -> list[Diagnostic]:
    """One absence row's problems — a moment's, or a skill's claim read through the same grammar."""
    if recipient and moment.kind == "not yet" and moment.referent is None and not moment.why:
        # The harness mechanism sheared the binding on the way in: the gap is upstream's, and the
        # recipient can neither see its question nor answer it. The shear leaves the kind alone,
        # unwrapped; words after it, or a wrapper that binds nothing, are the tree's own writing.
        return []
    notes = _row_problems(slug, moment)
    if moment.kind not in ("elsewhere", "embedded", "not yet"):
        return notes
    if not moment.referent:
        # A `not yet` names its question in a straw-dog binding; without one the gap is nobody's.
        problem = 'unbound: no <straw-dog question="q-N"> binding' if moment.kind == "not yet" else "names nothing"
        return notes + [Diagnostic(slug, f"'{moment.occasion}' is {moment.kind} and {problem}")]
    if moment.kind == "not yet":
        return notes + _gap_problems(root, slug, moment, held)
    if not (root / moment.referent).exists():
        notes.append(Diagnostic(slug, f"'{moment.occasion}' names {moment.referent}, which does not resolve"))
    return notes


def _gap_problems(root: Path, slug: str, moment: Moment, held: dict[str, questions.Entry]) -> list[Diagnostic]:
    """A `not yet` waits on a question the store holds, and one still waiting: once its answer has
    landed, the gap is filled and the row is stale — the day the mechanism that fills it lands."""
    where, bound = f"'{moment.occasion}'", moment.referent
    read = held.get(bound)
    if read is None:
        return [Diagnostic(slug, f"{where} binds {bound}, which no entry of the store holds")]
    if read.points_to:
        standing = questions.successor(held, read)
        rebind = f"rebind it to {standing.identity}" if standing else "nothing stands in its place"
        return [Diagnostic(slug, f"{where} binds {bound}, which is {read.kind}: {rebind}")]
    if questions.due(root, read):
        return [Diagnostic(slug, f"{where} binds {bound}, which is due: its answer has landed, so the row is stale")]
    return []


def _skills(root: Path, declarations: list[Declaration], held: dict[str, questions.Entry]) -> list[Skill]:
    """Every installed skill with who claims it: the declaration naming it, or the skill's own line."""
    home = root / SKILLS
    skills = []
    for directory in sorted(path for path in home.glob("*") if path.is_dir()) if home.is_dir() else []:
        named = f"{SKILLS}/{directory.name}/"
        by = [declared.slug for declared in declarations if f"{named}SKILL.md" in declared.instructions]
        skills.append(Skill(named, by, _claim(directory / "SKILL.md", held)))
    return skills


def _claim(instruction: Path, held: dict[str, questions.Entry]) -> Claim | None:
    """The `Mechanism:` line a skill opens its body with, if it makes one.

    The body starts after the frontmatter, which hosts parse as YAML and which no tag may enter.
    The line is a straw dog like a `not yet` row: the kind is its body, the question its binding.
    """
    if not instruction.is_file():
        return None
    lines = instruction.read_text(encoding="utf-8").splitlines()
    first = _after_frontmatter(lines)
    wrapper = wrapper_of(first)
    said = (wrapper.body if wrapper else first).strip()
    if not said.startswith(CLAIM):
        return None
    claimed = said[len(CLAIM) :].strip()
    # Past the label, the line reads through the moments' absence grammar: a wrapped `not yet`
    # keeps its wrapper and loses the label; anything else is the words after the label.
    cell = first.replace(wrapper.body, claimed, 1) if wrapper else claimed
    return Claim(*_absence(cell, held), stray=_stray_reason(cell))


def _after_frontmatter(lines: list[str]) -> str:
    """The first non-blank line of the body, past a `---` frontmatter if the file opens with one."""
    start = 0
    if lines and lines[0].strip() == "---":
        close = next((at for at, line in enumerate(lines[1:], start=1) if line.strip() == "---"), None)
        start = close + 1 if close is not None else 0
    return next((line for line in lines[start:] if line.strip()), "")


def _skill_problems(
    root: Path, skills: list[Skill], recipient: bool, held: dict[str, questions.Entry]
) -> list[Diagnostic]:
    """A skill is one mechanism's instruction file, or says none names it yet — never both, never neither."""
    notes = []
    for skill in skills:
        where = skill.directory
        if len(skill.named_by) > 1:
            notes.append(Diagnostic(where, f"named by {' and '.join(skill.named_by)}"))
        if skill.claim is None:
            if not skill.named_by:
                notes.append(Diagnostic(where, "no mechanism names it and it claims nothing"))
            continue
        if skill.named_by:
            # A named skill's line names its mechanism, held by the parts' naming check; only a
            # line saying none names it yet is a second claim.
            if skill.claim.kind is not None:
                notes.append(Diagnostic(where, f"named by {', '.join(skill.named_by)} and claims {skill.claim.kind}"))
            continue
        if skill.claim.kind is None:
            notes.append(Diagnostic(where, f"names {skill.claim.why}, whose declaration does not name it"))
            continue
        if skill.claim.kind == "unowned by design":
            notes.append(Diagnostic(
                where,
                "claims unowned by design; every skill is owned — name its mechanism, or say `not yet` "
                "bound to the question of what it owns",
            ))
            continue
        if skill.claim.kind not in CLAIM_KINDS:
            notes.append(Diagnostic(where, f"claims {skill.claim.kind}; a claim says no mechanism names the skill yet"))
            continue
        claim = skill.claim
        if claim.stray:
            # The shear keeps the words and drops the binding, and a recipient's check then reads
            # them as the tree's own writing: the origin says so first.
            notes.append(
                Diagnostic(where, "claims not yet and says why in its body; the reason is the question it is bound to")
            )
        claimed = Moment(f"{CLAIM} line", None, claim.kind, claim.why, claim.referent)
        notes += _absence_problems(root, where, claimed, recipient, held)
    return notes


def _naming_problems(root: Path, declared: list[Declaration], skills: list[Skill]) -> list[Diagnostic]:
    """Every skill, script, test and hook a mechanism owns names it on its first line, so an agent
    editing the file meets the doc that governs it; and no script names a mechanism whose parts
    omit it (the user, 2026-10-11). A part that does not resolve is the parts check's to report."""
    notes = []
    lines = {f"{skill.directory}SKILL.md": skill.claim for skill in skills}
    owners: dict[str, str] = {}
    for one in declared:
        for carrier in _carriers(one):
            owners[carrier] = one.slug
            if not (root / carrier).is_file() or _is_not_text(root / carrier):
                continue
            if carrier in lines:
                claim = lines[carrier]
                if claim is not None and claim.kind is not None:
                    continue  # a named skill saying none names it yet is a second claim, reported as one
                named = claim.why if claim else None
            else:
                named = _named_in_code(root / carrier)
            if named != one.slug:
                problem = f"{carrier} names {named}" if named else f"{carrier} names no mechanism"
                notes.append(Diagnostic(one.slug, problem))
    for code in _code_files(root):
        named = _named_in_code(root / code)
        if named and owners.get(code) != named:
            notes.append(Diagnostic(code, f"{code} names {named}, whose parts do not list it"))
    return notes


def _carriers(declared: Declaration) -> list[str]:
    """The parts that name their mechanism: its instruction files, and its parts under the scripts
    or outside the core directory, wherever they stand. The doc and rules file sit in the
    mechanism's own directory and a shelf beside its skill, so their place already says whose
    they are."""
    carriers = _skills_named(declared.instructions)
    carriers += [part.where for part in declared.parts if _carries_a_claim(part.where)]
    return list(dict.fromkeys(carriers))


def _skills_named(instructions) -> list[str]:
    return [named for named in instructions if named.startswith(SKILLS) and named.endswith("/SKILL.md")]


def _carries_a_claim(where: str) -> bool:
    """Whether a part's place and format make it open with its mechanism's claim."""
    if where.startswith(SCRIPTS_ROOT):
        return True
    return not where.startswith(CORE) and not where.endswith(CLAIMLESS)


def _code_files(root: Path) -> list[str]:
    home = root / SCRIPTS_ROOT
    if not home.is_dir():
        return []
    return sorted(
        path.relative_to(root).as_posix()
        for path in home.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    )


def _is_not_text(path: Path) -> bool:
    """Whether a file holds a NUL among its first bytes, as an image or an archive does and text
    does not: such a part has nowhere to carry a claim."""
    with path.open("rb") as handle:
        return b"\0" in handle.read(8192)


def _named_in_code(path: Path) -> str | None:
    """The mechanism a code file names on its first line, a comment after any shebang."""
    return _named_in_text(path.read_bytes().decode("utf-8", errors="replace"))


def _named_in_text(text: str) -> str | None:
    lines = text.splitlines()
    if lines and lines[0].startswith("#!"):
        lines = lines[1:]
    first = lines[0].strip() if lines else ""
    leader = next((each for each in COMMENT_LEADERS if first.startswith(each)), None)
    said = first[len(leader) :].strip() if leader else ""
    if not said.startswith(CLAIM):
        return None
    return said[len(CLAIM) :].strip() or None


def _named_in_skill(text: str) -> str | None:
    """The mechanism a skill names on the first line of its body, or `None` where it names none:
    a line saying `not yet` names no mechanism."""
    said = _after_frontmatter(text.splitlines()).strip()
    if not said.startswith(CLAIM):
        return None
    named = said[len(CLAIM) :].strip()
    return None if not named or any(named.startswith(kind) for kind in KINDS) else named


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


def _instructions(text: str) -> tuple[str, ...]:
    """Every `instruction` bullet of the header, in its order: one per skill the mechanism owns.
    The header's other bullets stand once; this one repeats, so `_bullets` cannot carry it."""
    named = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            break
        if stripped.startswith("- **instruction**"):
            named.append(_value(stripped[len("- **instruction**"):]))
    return tuple(named)


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


def _moment(row: list[str], held: dict[str, questions.Entry]) -> Moment:
    occasion, instructed, absence = (row + ["", "", ""])[:3]
    kind, why, referent = _absence(absence, held)
    return Moment(occasion, _backticked(instructed), kind, why, referent)


def _absence(cell: str, held: dict[str, questions.Entry]) -> tuple[str | None, str, str | None]:
    """The kind an uninstructed row declares, the clause saying why, and what it points at.

    A `not yet` row is a straw dog: its body is the kind, its referent is the wrapper's question —
    the binding the shear strips, so no id of this tree ships — and its reason is that question's
    words, read from the store (the user, 2026-10-04). Every other referent is a backticked path
    from the repository root. A wrapper around one of the other kinds is an ordinary straw dog on
    the cell, read for its body.
    """
    wrapper = wrapper_of(cell)
    body = wrapper.body if wrapper else cell.strip()
    kind = next((name for name in KINDS if body.startswith(name)), None)
    if kind is None:
        return None, body, None
    if kind == "not yet" and wrapper:
        # A wrapper that binds nothing names an empty question, never none: no wrapper at all is
        # what the shear leaves, and the two are told apart by that.
        waits_on = held.get(wrapper.question or "")
        return kind, waits_on.question if waits_on else "", wrapper.question or ""
    if kind == "not yet":
        rest = body[len(kind) :]
        return kind, _clause(rest) or rest.strip(), None
    return kind, _clause(body[len(kind) :]), _backticked(body)


def _clause(rest: str) -> str:
    """The words saying why, with the referent taken out — a link or a path is not a reason."""
    words = _LINK.sub("", rest)
    words = _CODE.sub("", words)
    return words.strip(" —-,.;:").strip()


def _stray_reason(cell: str) -> bool:
    """Whether a wrapped `not yet` carries words after the kind, when its question is its reason."""
    wrapper = wrapper_of(cell)
    return wrapper is not None and wrapper.body.startswith("not yet") and wrapper.body != "not yet"


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
    # The tree this script sits in; anything that imports it names its tree itself.
    sys.exit(main(sys.argv[1:], Path(__file__).resolve().parents[3]))
