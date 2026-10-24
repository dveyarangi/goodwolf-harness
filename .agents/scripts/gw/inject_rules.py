# Mechanism: mechanism-shape
"""A mechanism's rules reach other skills as installed blocks, from the one file that holds them.

    uv run --offline --no-project python .agents/scripts/gw/inject_rules.py <slug> --install [--overwrite]
    uv run --offline --no-project python .agents/scripts/gw/inject_rules.py --install [--overwrite]
    uv run --offline --no-project python .agents/scripts/gw/inject_rules.py <slug> --retract
    uv run --offline --no-project python .agents/scripts/gw/inject_rules.py --check [--line]
    uv run --offline --no-project python .agents/scripts/gw/inject_rules.py --set <setting>=<value>
    uv run --offline --no-project python .agents/scripts/gw/inject_rules.py --settings

One block per source per target, holding every rule the source sends there. A source is a
mechanism's rules file, or the project's own — `local.rules.md` beside the entry file, the slug
`local` — whose block lands after every mechanism's in a target and whose rules may name the
core rule each overrides. A rule may name the condition of its installation, `when
<setting>=<value>`; a mechanism declares the settings it owns in its rules file, the project sets
their values in its local file, and a rule is written into a target only while its conditions
hold under those values. The grammar of the rules file is the format shelf's,
`MECHANISM-FORMAT.md`; the contract — a named mode or a refusal, every target validated before
anything is written, retraction byte-identical, a differing block refused until the caller says
overwrite — is the architecture's. A block that differs from its rendering only in which of the
file's own rules it holds differs by the settings alone, and is re-rendered without being asked:
the contract's refusal is for an edited copy or an amended source, which that block is not.

Without a slug, `--install` is the installer's run: every source in the harness's order,
mechanisms then local, so a changed setting brings the whole tree to match. `--set` changes one
value in the local file and runs it. `--settings` renders the tree's settings as one table and
writes nothing: an index is rendered on request, never committed. `--check --line` prints one
line for a host's hook, or nothing.

The script never decides what a rule means and never writes a doc.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

sys.path.insert(0, str(Path(__file__).resolve().parent))

from docs_corpus import (  # noqa: E402  (path set just above)
    INSTALLED_CLOSING,
    INSTALLED_OPENING,
    citations,
    corpus,
    without_code,
)

MECHANISMS = ".agents/mechanisms"
# The project's own rules file: beside the entry file, outside core, so a redeploy that replaces
# the core directory cannot delete it. Its slug is the block tag the leak check already skips.
LOCAL = "local"
LOCAL_FILE = "local.rules.md"
MODES = ("--install", "--retract", "--check", "--set", "--settings")
_USAGE = (
    "usage: inject_rules.py <slug> --install [--overwrite] | --install [--overwrite] | <slug> --retract"
    " | --check [--line] | --set <setting>=<value> | --settings"
)
_HEADING = re.compile(r"^(#{1,6}) (.*)$", re.M)
_WRAPPER_OPENING = re.compile(r"^<straw-dog\b[^<>]*>$")
_CELL = re.compile(r"^`([^`]+)`$")
# A preamble's tables are told apart by their header row; a row under no known header is prose.
_ANCHOR_HEADER = ("target", "anchor")
_DECLARATION_HEADER = ("setting", "values", "default", "set by")
_VALUE_HEADER = ("setting", "value")
_HEADERS = (_ANCHOR_HEADER, _DECLARATION_HEADER, _VALUE_HEADER)
_VALUES_APART = " · "
THE_PERSON = "the person"
_TARGET = re.compile(r"^- \*\*target\*\* `([^`]+)`\s*$")
_OVERRIDES = re.compile(r"^- \*\*overrides\*\* `([^`/]+)/([^`/]+)`\s*$")
_AUTHORITY = re.compile(r"^- \*\*authority\*\* (.+?)\s*$")
_WHEN = re.compile(r"^- \*\*when\*\* ([^\s=`]+)=(.+?)\s*$")
_SPAN_EDGE = re.compile(r"^</?rule>\r?\n?$")
_PATTERN_CHARACTERS = re.compile(r"[*?\[]")


class Refused(Exception):
    """Something that must not be written past. The message says what to settle first."""


@dataclass(frozen=True)
class Rule:
    id: str
    title: str
    targets: tuple[str, ...]
    authority: str
    body: str
    overrides: tuple[str, str] | None = None
    """The core rule this one replaces, as (slug, id) — a project's override names its rule."""
    when: tuple[tuple[str, str], ...] = ()
    """The conditions of its installation, `(setting, value)` each, all of which must hold."""

    @property
    def paragraph(self) -> str:
        """As installed: the id, the rule it overrides where it does, so a reader sees the
        disagreement where they meet it, and the body unreshaped."""
        cited = f" *(overrides {'/'.join(self.overrides)})*" if self.overrides else ""
        return f"**{self.id}**{cited} {self.body}"


@dataclass(frozen=True)
class Setting:
    """A setting as its mechanism declares it: what it is called, what it may be, what it is
    unless the project says, and who may set it — a rung's name, or the person."""

    name: str
    values: tuple[str, ...]
    default: str
    set_by: str
    owner: str


@dataclass(frozen=True)
class Settings:
    """The tree's settings resolved: every declaration across the rules files, and the values the
    local file sets. A setting the local file leaves unset stands at its default."""

    declared: dict[str, Setting]
    values: dict[str, str]

    def value(self, name: str) -> str:
        return self.values.get(name, self.declared[name].default)

    def holds(self, when: tuple[tuple[str, str], ...]) -> bool:
        return all(name in self.declared and self.value(name) == value for name, value in when)


NO_SETTINGS = Settings({}, {})


@dataclass(frozen=True)
class RulesFile:
    """One mechanism's rules, with the place in each target its block goes, the settings it
    declares, and — the local file alone — the values the project sets."""

    slug: str
    anchors: dict[str, str]
    rules: tuple[Rule, ...]
    settings: tuple[Setting, ...] = ()
    values: dict[str, str] = field(default_factory=dict)

    def block(self, rows: tuple[str, ...], settings: Settings = NO_SETTINGS) -> str | None:
        """What a file the anchor table's rows reach must hold: every rule naming one of the rows
        whose conditions hold, file order, ids from the headings — or nothing, where the settings
        call for none of them. A rule names a row — a file, or a group's pattern — never a member."""
        paragraphs = [
            rule.paragraph
            for rule in self.rules
            if set(rows) & set(rule.targets) and settings.holds(rule.when)
        ]
        if not paragraphs:
            return None
        return f'<installed by="{self.slug}">\n' + "\n\n".join(paragraphs) + f"\n{INSTALLED_CLOSING}"

    def paragraphs(self, rows: tuple[str, ...]) -> set[str]:
        """Every paragraph a rule of this file could put in a file the rows reach, whatever the
        settings."""
        return {rule.paragraph for rule in self.rules if set(rows) & set(rule.targets)}


@dataclass(frozen=True)
class Located:
    """A block found in a target by its tag. `text` is None when the tag never closes."""

    start: int
    end: int
    text: str | None


def main(argv: list[str], root: Path) -> int:
    word, mode, overwrite, line, usage = _parsed(argv)
    if usage:
        print(_USAGE)
        return 2
    if mode == "--check":
        report = check(root)
        print(check_line(report) if line else json.dumps(report, indent=2))
        return 1 if report["diagnostics"] else 0
    if mode == "--settings":
        print(settings_table(root))
        return 0
    if mode == "--set":
        report = set_value(root, word)
        print(json.dumps(report, indent=2))
        return 1 if report["refusals"] else 0
    if mode == "--install" and word is None:
        report = install_every(root, overwrite)
        print(json.dumps(report, indent=2))
        return 1 if report["refusals"] else 0
    try:
        rules = read_rules_file(root, word)
        settings = settings_resolved(root)
        if mode == "--install":
            overrides_resolve(root, rules)
            conditions_resolve(rules, settings)
    except Refused as refusal:
        print(json.dumps({"slug": word, "mode": mode[2:], "refusals": [str(refusal)]}, indent=2))
        return 1
    report = install(root, rules, overwrite, settings) if mode == "--install" else retract(root, rules, settings)
    print(json.dumps(report, indent=2))
    return 1 if report["refusals"] else 0


def _parsed(argv: list[str]) -> tuple[str | None, str | None, bool, bool, bool]:
    """Exactly one mode, always named; a word present exactly when the mode takes one — the slug
    of an install or retraction, `<setting>=<value>` of a set — an install with no slug being the
    run over every source; `--overwrite` with an install alone, `--line` with the check alone."""
    modes = [operand for operand in argv if operand in MODES]
    flags = [operand for operand in argv if operand.startswith("-") and operand not in MODES]
    words = [operand for operand in argv if not operand.startswith("-")]
    overwrite = flags == ["--overwrite"]
    line = flags == ["--line"]
    if len(modes) != 1 or (flags and not (overwrite or line)):
        return None, None, False, False, True
    mode = modes[0]
    if mode == "--check":
        return None, mode, False, line, bool(words) or overwrite
    if line:
        return None, mode, False, False, True
    if mode == "--settings":
        return None, mode, False, False, bool(words) or overwrite
    if mode == "--set":
        return (words[0] if words else None), mode, False, False, len(words) != 1 or overwrite
    if mode == "--install" and not words:
        return None, mode, overwrite, False, False
    if len(words) != 1 or (overwrite and mode != "--install"):
        return None, mode, overwrite, False, True
    return words[0], mode, overwrite, False, False


# --- the rules file --------------------------------------------------------------------------


def read_rules_file(root: Path, slug: str) -> RulesFile:
    if slug == LOCAL and (root / MECHANISMS / LOCAL).is_dir():
        raise Refused(_COLLISION)
    path = _rules_path(root, slug)
    if not path.is_file():
        raise Refused(f"no rules file at {path.relative_to(root).as_posix()}")
    return parse_rules_file(slug, _read(path))


def _rules_path(root: Path, slug: str) -> Path:
    """A mechanism's file sits in its directory; the project's sits beside the entry file."""
    if slug == LOCAL:
        return root / LOCAL_FILE
    return root / MECHANISMS / slug / f"{slug}.rules.md"


_COLLISION = f"a mechanism directory named {LOCAL} collides with the local file {LOCAL_FILE}"


def parse_rules_file(slug: str, text: str) -> RulesFile:
    """The shelf's grammar, one line at a time.

    What kind of line it is — heading, bullet, table row, span edge — is decided on the
    code-blanked view, so an example in a fence is never a rule; what it says is read from the
    raw line, since the values are code spans and the blanked view has erased them.
    """
    lines = list(zip(text.splitlines(keepends=True), without_code(text).splitlines(keepends=True)))
    starts = _section_starts(lines)
    if not starts:
        raise Refused("no rule sections — an install of nothing is not a success")
    tables = _tables(lines[: starts[0]])
    anchors = _anchor_table(tables.get(_ANCHOR_HEADER, []))
    declared = _declarations(slug, tables.get(_DECLARATION_HEADER, []))
    values = _values(slug, tables.get(_VALUE_HEADER, []))
    rules = [
        _rule(lines[start:end], anchors)
        for start, end in zip(starts, starts[1:] + [len(lines)])
    ]
    ids = [rule.id for rule in rules]
    for rule_id in ids:
        if ids.count(rule_id) > 1:
            raise Refused(f"rule id {rule_id} appears twice")
    return RulesFile(slug, anchors, tuple(rules), declared, values)


def _section_starts(lines: list[tuple[str, str]]) -> list[int]:
    """Every `## ` line outside a span. One inside a span is refused here, where it is seen first."""
    starts: list[int] = []
    inside_span = False
    for index, (_, seen) in enumerate(lines):
        if _SPAN_EDGE.match(seen):
            inside_span = seen.startswith("<rule>")
        elif seen.startswith("## "):
            if inside_span:
                raise Refused("a rule's body holds a heading line")
            starts.append(index)
    return starts


def _tables(preamble: list[tuple[str, str]]) -> dict[tuple[str, ...], list[list[str]]]:
    """The preamble's tables, each by its header row, its rows as lists of raw cells, the divider
    skipped. A row under no known header is prose and is not read."""
    tables: dict[tuple[str, ...], list[list[str]]] = {}
    header: tuple[str, ...] | None = None
    for raw, seen in preamble:
        if not seen.lstrip().startswith("|"):
            header = None
            continue
        cells = [cell.strip() for cell in raw.strip().strip("|").split("|")]
        named = tuple(cell.lower() for cell in cells)
        if named in _HEADERS:
            header = named
            tables.setdefault(header, [])
        elif header is not None and not all(set(cell) <= set("-: ") for cell in cells):
            tables[header].append(cells)
    return tables


def _anchor_table(rows: list[list[str]]) -> dict[str, str]:
    anchors: dict[str, str] = {}
    for cells in rows:
        spans = [_CELL.match(cell) for cell in cells]
        if len(cells) != 2 or not all(spans):
            continue  # not a row of two code spans: prose in the table
        target, anchor = spans[0].group(1), spans[1].group(1)
        if target in anchors:
            raise Refused(f"{target} is named twice in the anchor table — a mechanism has one place in a target")
        anchors[target] = anchor
    return anchors


def _declarations(slug: str, rows: list[list[str]]) -> tuple[Setting, ...]:
    """The settings this file declares: the name and each value a code span, the values told
    apart by ` · `, the default among them, `set by` a rung's name or the person. Values are the
    project's, so the local file declares nothing."""
    if rows and slug == LOCAL:
        raise Refused(f"{LOCAL_FILE} declares a setting; a setting is declared by the mechanism it belongs to")
    declared: list[Setting] = []
    for cells in rows:
        if len(cells) != 4:
            raise Refused(f"a settings row has {len(cells)} cells, not setting, values, default and set by")
        name_span, default_span = _CELL.match(cells[0]), _CELL.match(cells[2])
        value_spans = [_CELL.match(value.strip()) for value in cells[1].split(_VALUES_APART)]
        if name_span is None or default_span is None or not all(value_spans):
            raise Refused(f"a setting's name, values and default are code spans: {' | '.join(cells)}")
        name, default = name_span.group(1), default_span.group(1)
        values = tuple(span.group(1) for span in value_spans)
        if default not in values:
            raise Refused(f"setting {name}'s default `{default}` is not among its values")
        if any(one.name == name for one in declared):
            raise Refused(f"setting {name} is declared twice")
        if not cells[3]:
            raise Refused(f"setting {name} says nothing of who sets it")
        declared.append(Setting(name, values, default, cells[3], slug))
    return tuple(declared)


def _values(slug: str, rows: list[list[str]]) -> dict[str, str]:
    """The values the project sets, name and value each a code span; a mechanism's file sets
    none, since values are the project's."""
    if rows and slug != LOCAL:
        raise Refused(f"{slug}'s rules file sets a value; values are the project's, in {LOCAL_FILE}")
    values: dict[str, str] = {}
    for cells in rows:
        spans = [_CELL.match(cell) for cell in cells]
        if len(cells) != 2 or not all(spans):
            raise Refused(f"a value row is a setting and a value, each a code span: {' | '.join(cells)}")
        name, value = spans[0].group(1), spans[1].group(1)
        if name in values:
            raise Refused(f"setting {name} is set twice")
        values[name] = value
    return values


def _rule(section: list[tuple[str, str]], anchors: dict[str, str]) -> Rule:
    heading = section[0][0][3:].strip()
    rule_id, _, title = heading.partition(" — ")
    rule_id = rule_id.strip()
    targets: list[str] = []
    overrides: list[tuple[str, str]] = []
    authorities: list[str] = []
    when: list[tuple[str, str]] = []
    edges: list[int] = []
    for index, (raw, seen) in enumerate(section[1:], start=1):
        if seen.startswith("- **target**") and (match := _TARGET.match(raw)):
            targets.append(match.group(1))
        elif seen.startswith("- **overrides**") and (match := _OVERRIDES.match(raw)):
            overrides.append((match.group(1), match.group(2)))
        elif seen.startswith("- **authority**") and (match := _AUTHORITY.match(raw)):
            authorities.append(match.group(1))
        elif seen.startswith("- **when**"):
            if (match := _WHEN.match(raw)) is None:
                raise Refused(f"rule {rule_id}'s condition is not `when <setting>=<value>`: {raw.strip()}")
            when.append((match.group(1), match.group(2)))
        elif _SPAN_EDGE.match(seen):
            edges.append(index)
    if not targets:
        raise Refused(f"rule {rule_id} names no target")
    for target in targets:
        if target not in anchors:
            raise Refused(f"rule {rule_id} targets {target}, which has no row in the anchor table")
    if len(overrides) > 1:
        raise Refused(f"rule {rule_id} states overrides more than once")
    if len(authorities) != 1:
        raise Refused(f"rule {rule_id} must state its authority exactly once")
    if len(edges) != 2 or [section[i][1].rstrip("\r\n") for i in edges] != ["<rule>", "</rule>"]:
        raise Refused(f"rule {rule_id} needs exactly one <rule> … </rule> span")
    body = "".join(raw for raw, _ in section[edges[0] + 1 : edges[1]]).rstrip("\r\n")
    _body_problems(rule_id, body)
    return Rule(
        rule_id, title.strip(), tuple(targets), authorities[0], body,
        overrides[0] if overrides else None, tuple(when),
    )


def overrides_resolve(root: Path, rules: RulesFile) -> None:
    """Every override names a rule that exists and is sent to every target the override names.

    Read from the cited rules file's declared targets, never from whether its block is present:
    an absent mechanism block is that mechanism's diagnostic, and the override's refusal names
    the local entry so the author knows which one to fix.
    """
    for problem in override_problems(root, rules):
        raise Refused(problem)


def override_problems(root: Path, rules: RulesFile) -> list[str]:
    """Each override that names no rule the tree installs where the override goes, in file order."""
    problems = []
    for rule in rules.rules:
        if rule.overrides is None:
            continue
        slug, cited_id = rule.overrides
        said = f"{rule.id} overrides {slug}/{cited_id}"
        try:
            cited = read_rules_file(root, slug)
        except Refused as refusal:
            problems.append(f"{said}, but {refusal}")
            continue
        found = next((one for one in cited.rules if one.id == cited_id), None)
        if found is None:
            problems.append(f"{said}, which {slug}'s rules file does not define")
            continue
        problems += [
            f"{said}, which is not installed in {target}"
            for target in rule.targets
            if target not in found.targets
        ]
    return problems


# --- the settings -----------------------------------------------------------------------------


def settings_resolved(root: Path) -> Settings:
    """The tree's settings, or a refusal naming the first thing wrong with them."""
    settings, problems = read_settings(root)
    if problems:
        raise Refused(problems[0])
    return settings


def read_settings(root: Path) -> tuple[Settings, list[str]]:
    """Every declaration across the mechanisms' rules files and the values the local file sets,
    with what is wrong among them: a setting declared by two mechanisms, a value set for a
    setting nobody declares, a value no declaration holds. A rules file that cannot be read is
    its own diagnostic elsewhere and declares nothing here."""
    declared: dict[str, Setting] = {}
    problems: list[str] = []
    for slug, rules in _sources_read(root).items():
        if rules is None:
            continue
        for setting in rules.settings:
            if setting.name in declared:
                problems.append(
                    f"setting {setting.name} is declared by {declared[setting.name].owner} and by {slug}"
                )
                continue
            declared[setting.name] = setting
    values: dict[str, str] = {}
    local = _sources_read(root).get(LOCAL)
    for name, value in (local.values if local else {}).items():
        if name not in declared:
            problems.append(f"{LOCAL_FILE} sets {name}, which no mechanism declares")
        elif value not in declared[name].values:
            problems.append(
                f"{LOCAL_FILE} sets {name} to `{value}`, which is none of "
                + ", ".join(f"`{one}`" for one in declared[name].values)
            )
        else:
            values[name] = value
    return Settings(declared, values), problems


def _sources_read(root: Path) -> dict[str, RulesFile | None]:
    """Every source the tree holds, in the harness's order — the mechanisms, then the local file —
    each read, or None where its file refuses."""
    files: dict[str, RulesFile | None] = {}
    directories = sorted((root / MECHANISMS).glob("*/")) if (root / MECHANISMS).is_dir() else []
    for directory in directories:
        slug = directory.name
        if slug == LOCAL or not (directory / f"{slug}.rules.md").is_file():
            continue
        try:
            files[slug] = read_rules_file(root, slug)
        except Refused:
            files[slug] = None
    if (root / LOCAL_FILE).is_file():
        try:
            files[LOCAL] = read_rules_file(root, LOCAL)
        except Refused:
            files[LOCAL] = None
    return files


def conditions_resolve(rules: RulesFile, settings: Settings) -> None:
    for problem in condition_problems(rules, settings):
        raise Refused(problem)


def condition_problems(rules: RulesFile, settings: Settings) -> list[str]:
    """Each condition naming a setting no mechanism declares, or a value its declaration lacks."""
    problems = []
    for rule in rules.rules:
        for name, value in rule.when:
            if name not in settings.declared:
                problems.append(f"rule {rule.id} is conditioned on {name}, which no mechanism declares")
            elif value not in settings.declared[name].values:
                problems.append(
                    f"rule {rule.id} is conditioned on {name}=`{value}`, which is none of "
                    + ", ".join(f"`{one}`" for one in settings.declared[name].values)
                )
    return problems


def settings_table(root: Path) -> str:
    """The tree's settings as one table, rendered on request and never committed: an index of the
    declarations and the local file, each entry at its authored home."""
    settings, problems = read_settings(root)
    rows = [
        "| setting | values | default | this tree | set by | declared by |",
        "|---|---|---|---|---|---|",
    ]
    for name in sorted(settings.declared):
        one = settings.declared[name]
        rows.append(
            f"| `{name}` | {_VALUES_APART.join(f'`{value}`' for value in one.values)} | `{one.default}` "
            f"| `{settings.value(name)}` | {one.set_by} | {one.owner} |"
        )
    return "\n".join(rows + [f"\n{problem}" for problem in problems])


def set_value(root: Path, said: str | None) -> dict:
    """One setting changed in the local file, then the run, so the tree matches at once. Refuses an
    undeclared name or value before writing; who may run it is not the script's to tell."""
    name, apart, value = (said or "").partition("=")
    report: dict = {"mode": "set", "setting": name, "value": value, "refusals": []}
    if not apart or not name or not value:
        report["refusals"].append(f"not `<setting>=<value>`: {said!r}")
        return report
    settings, problems = read_settings(root)
    if name not in settings.declared:
        report["refusals"].append(f"no mechanism declares {name}")
    elif value not in settings.declared[name].values:
        report["refusals"].append(
            f"{name} is none of " + ", ".join(f"`{one}`" for one in settings.declared[name].values)
        )
    if report["refusals"]:
        return report
    path = root / LOCAL_FILE
    if not path.is_file():
        report["refusals"].append(f"no {LOCAL_FILE} to set it in")
        return report
    _write(path, _with_value(_read(path), name, value))
    report["written"] = LOCAL_FILE
    run = install_every(root, overwrite=False)
    report["installed"] = run["sources"]
    report["refusals"] = run["refusals"]
    return report


def _with_value(text: str, name: str, value: str) -> str:
    """The local file with the setting's row holding the value: the row rewritten where it is,
    appended to the table where the setting had none, the table opened after the anchor table
    where the file has none. Everything else stays byte for byte."""
    newline = "\r\n" if "\r\n" in text else "\n"
    lines = text.split(newline)
    seen = without_code(text).split(newline)
    header: tuple[str, ...] | None = None
    value_rows: list[int] = []
    anchor_rows: list[int] = []
    value_header: int | None = None
    for index, (raw, blank) in enumerate(zip(lines, seen)):
        if blank.startswith("## "):
            break
        if not blank.lstrip().startswith("|"):
            header = None
            continue
        cells = tuple(cell.strip().lower() for cell in raw.strip().strip("|").split("|"))
        if cells in _HEADERS:
            header = cells
            if header == _VALUE_HEADER:
                value_header = index
            continue
        if all(set(cell) <= set("-: ") for cell in cells):
            continue
        if header == _VALUE_HEADER:
            value_rows.append(index)
        elif header == _ANCHOR_HEADER:
            anchor_rows.append(index)
    row = f"| `{name}` | `{value}` |"
    for index in value_rows:
        if lines[index].strip().startswith(f"| `{name}` |"):
            lines[index] = row
            return newline.join(lines)
    if value_header is not None:
        last = value_rows[-1] if value_rows else value_header + 1
        lines.insert(last + 1, row)
        return newline.join(lines)
    after = anchor_rows[-1] if anchor_rows else -1
    lines[after + 1 : after + 1] = ["", "| setting | value |", "|---|---|", row]
    return newline.join(lines)


def _body_problems(rule_id: str, body: str) -> None:
    # A citation is rewritten per the file it sits in, so one body in two directories would drift
    # apart on the next record move; a heading would split the section; the tag would end the block.
    if citations(body):
        raise Refused(f"rule {rule_id}'s body carries a citation; name paths in words or backticks")
    if _HEADING.search(body):
        raise Refused(f"rule {rule_id}'s body holds a heading line")
    if "<installed" in body or INSTALLED_CLOSING in body:
        raise Refused(f"rule {rule_id}'s body holds the installed tag")
    # A body is copied into every target, and the listing blanks an installed block before it
    # scans: a straw dog written here would be invisible in every place it landed. An expiring
    # rule is wrapped around its section instead, where the rule is authored and the listing looks.
    if "<straw-dog" in body or "</straw-dog>" in body:
        raise Refused(
            f"rule {rule_id}'s body holds a straw dog; wrap the section, not the body, so the "
            "listing sees it where the rule is authored"
        )


# --- the target -----------------------------------------------------------------------------


def locate(text: str, slug: str) -> Located | None:
    """The block by its tag — never by its body, which an edit would hide from us."""
    seen = without_code(text)
    openings = [m for m in INSTALLED_OPENING.finditer(seen) if m.group(1) == slug]
    if not openings:
        return None
    if len(openings) > 1:
        raise Refused(f"two blocks of {slug} in one file")
    start = openings[0].start()
    close = seen.find(INSTALLED_CLOSING, start)
    if close == -1:
        return Located(start, -1, None)
    end = close + len(INSTALLED_CLOSING)
    return Located(start, end, text[start:end])


def matches(found: str, rendered: str) -> bool:
    # Both sides normalised, in one place: Life's injector and its wake normalised one side each
    # and disagreed about the same blocks for a week.
    return found.replace("\r\n", "\n") == rendered.replace("\r\n", "\n")


def after_anchor(text: str, anchor: str) -> int:
    """The offset just past the anchor line's newline; the line must be whole, terminated, unique."""
    seen = without_code(text)
    hits = []
    offset = 0
    for line in seen.splitlines(keepends=True):
        if line.rstrip("\r\n") == anchor:
            if not line.endswith("\n"):
                raise Refused(f"anchor {anchor!r} is the last line and has no newline to install after")
            hits.append(offset + len(line))
        offset += len(line)
    if not hits:
        raise Refused(f"anchor {anchor!r} not found")
    if len(hits) > 1:
        raise Refused(f"anchor {anchor!r} is ambiguous — it occurs {len(hits)} times")
    return hits[0]


def section_end(text: str, anchor: str) -> int:
    """The offset just past the last non-blank line of the anchor's section: the section runs
    from the anchor line to the next heading of the anchor's level or higher, or to the end of
    the text; a line that is not a heading is ended by any heading. Fences are not read. A straw
    dog opening on a line of its own with nothing of the section after it wraps what follows, so
    it is the next section's: a block placed after it would expire with text it does not belong to."""
    start = after_anchor(text, anchor)
    seen = without_code(text)
    level = _heading_level(anchor)
    end = start
    offset = start
    for line in seen[start:].splitlines(keepends=True):
        heading = _heading_level(line.rstrip("\r\n"))
        if heading is not None and heading <= (level if level is not None else 6):
            break
        offset += len(line)
        if line.strip() and not _WRAPPER_OPENING.match(line.strip()):
            end = offset
    return end


def _heading_level(line: str) -> int | None:
    match = _HEADING.match(line)
    return len(match.group(1)) if match else None


def insertion_point(text: str, anchor: str, slug: str) -> int:
    """At the end of the anchor's section, so blocks stand in install order after the section's
    own text — and, for a mechanism's block, before the local block if one is already there, so
    the project's answer stays what a reader meets after core's rules."""
    end = section_end(text, anchor)
    if slug == LOCAL:
        return end
    local = locate(text, LOCAL)
    if local is not None and after_anchor(text, anchor) <= local.start < end:
        return local.start - 1
    return end


def following_block(text: str, offset: int) -> tuple[str, int] | None:
    """The first installed block opening at or after `offset`: its slug and line, or None."""
    seen = without_code(text)
    for opening in INSTALLED_OPENING.finditer(seen):
        if opening.start() >= offset:
            return opening.group(1), text.count("\n", 0, opening.start()) + 1
    return None


def with_block(text: str, at: int, block: str) -> str:
    return text[:at] + "\n" + block + "\n" + text[at:]


def without_block(text: str, found: Located) -> str:
    """Exactly what install added: the block, the newline before it, the newline after it."""
    start, end = found.start, found.end
    if not (start >= 1 and text[start - 1] == "\n" and text[end:end + 1] == "\n"):
        raise Refused("the block is not spaced as the installer writes it")
    return text[: start - 1] + text[end + 1:]


# --- the modes ------------------------------------------------------------------------------


@dataclass(frozen=True)
class Reached:
    """A file a rules file's block goes to: the file, the anchor-table rows that reach it — the one
    whose anchor places the block first — and that anchor."""

    file: str
    rows: tuple[str, ...]
    anchor: str


def reached(root: Path, rules: RulesFile, listed: list[str] | None = None) -> list[Reached]:
    """Every file the anchor table reaches. An explicit row reaches its own file; a group's row — a
    path pattern — reaches every listed file it wholly matches that holds its anchor line, a member
    declaring itself by the heading and the rest passed over, an empty group reaching nothing. A
    mechanism has one place in a target: a file its own row names and a group also reaches holds
    one block at the named row's anchor, with both rows' rules; a file two groups reach is refused
    (docs/architecture.md: "Installed blocks")."""
    found: dict[str, Reached] = {
        row: Reached(row, (row,), anchor) for row, anchor in rules.anchors.items() if not is_pattern(row)
    }
    named = set(found)
    for row, anchor in rules.anchors.items():
        if not is_pattern(row):
            continue
        listed = corpus(root) if listed is None else listed
        for name in listed:
            if not PurePosixPath(name).full_match(row) or not _holds(root / name, anchor):
                continue
            if name in named:
                place = found[name]
                found[name] = Reached(name, place.rows + (row,), place.anchor)
            elif name in found:
                raise Refused(f"{name} is reached by two groups of the anchor table — a mechanism has one place in a target")
            else:
                found[name] = Reached(name, (row,), anchor)
    return list(found.values())


def is_pattern(row: str) -> bool:
    """Whether an anchor-table row names a group — a path pattern — rather than one file."""
    return bool(_PATTERN_CHARACTERS.search(row))


def holds_anchor(text: str, anchor: str) -> bool:
    """Whether a text holds the anchor line outside code — how a group's member declares itself."""
    return any(line.rstrip("\r") == anchor for line in without_code(text).split("\n"))


def _holds(path: Path, anchor: str) -> bool:
    return path.is_file() and holds_anchor(_read(path), anchor)


def install(root: Path, rules: RulesFile, overwrite: bool, settings: Settings = NO_SETTINGS) -> dict:
    """Every target validated first; then, only if all of them passed, every target written."""
    return _installing_or_retracting(root, rules, "install", overwrite, settings)


def retract(root: Path, rules: RulesFile, settings: Settings = NO_SETTINGS) -> dict:
    return _installing_or_retracting(root, rules, "retract", False, settings)


def install_every(root: Path, overwrite: bool) -> dict:
    """The installer's run: every source in the harness's order, the mechanisms then the local
    file, each installed under the tree's settings; the first refusal ends it, and the report
    says which source and why. Run twice, the second run changes nothing."""
    report: dict = {"mode": "install", "sources": [], "refusals": []}
    try:
        settings = settings_resolved(root)
    except Refused as refusal:
        report["refusals"].append(str(refusal))
        return report
    for slug in _sources_read(root):
        try:
            rules = read_rules_file(root, slug)
            if slug == LOCAL:
                overrides_resolve(root, rules)
            conditions_resolve(rules, settings)
            outcome = install(root, rules, overwrite, settings)
        except Refused as refusal:
            report["refusals"].append(f"{slug}: {refusal}")
            return report
        report["sources"].append({"slug": slug, "targets": outcome["targets"]})
        if outcome["refusals"]:
            report["refusals"].append(f"{slug}: {outcome['refusals'][0]}")
            return report
    return report


def _installing_or_retracting(
    root: Path, rules: RulesFile, mode: str, overwrite: bool, settings: Settings
) -> dict:
    planned: list[tuple[str, str]] = []
    outcomes: list[dict] = []
    refusals: list[str] = []
    try:
        places = reached(root, rules)
    except Refused as refusal:
        return {"slug": rules.slug, "mode": mode, "targets": [], "refusals": [str(refusal)]}
    for place in places:
        try:
            outcome, new_text = _planned(root, rules, place, mode, overwrite, settings)
        except Refused as refusal:
            refusals.append(f"{place.file}: {refusal}")
            continue
        outcomes.append(outcome)
        if new_text is not None:
            planned.append((place.file, new_text))
    if mode == "install":
        for dropped in _dropped_targets(root, rules, {place.file for place in places}):
            try:
                outcome, new_text = _removal(root, rules.slug, dropped)
            except Refused as refusal:
                refusals.append(f"{dropped}: {refusal}")
                continue
            outcomes.append(outcome)
            planned.append((dropped, new_text))
    report = {"slug": rules.slug, "mode": mode, "targets": outcomes, "refusals": refusals}
    if refusals:
        return report
    return _written(root, planned, report)


def _planned(
    root: Path, rules: RulesFile, place: Reached, mode: str, overwrite: bool, settings: Settings
) -> tuple[dict, str | None]:
    target, anchor = place.file, place.anchor
    path = root / target
    if not path.is_file():
        raise Refused("target missing")
    text = _read(path)
    found = locate(text, rules.slug)
    if found is not None and found.text is None:
        raise Refused("the block opens and never closes")
    rendered = rules.block(place.rows, settings)
    if rendered is None:
        # The settings call for none of the file's rules here: a block present is taken out by
        # retraction's cut, as a dropped target's is, whatever the mode.
        if found is None:
            return {"target": target, "state": "not called for"}, None
        return {"target": target, "state": "removed", "removed": found.text}, without_block(text, found)
    if mode == "install":
        if found is None:
            at = insertion_point(text, anchor, rules.slug)
            if rules.slug == LOCAL and (follows := following_block(text, at)):
                raise Refused(
                    f"the local block would not be last: a block of {follows[0]} at line {follows[1]} "
                    "would follow it; anchor the local rule after every mechanism's block"
                )
            return {"target": target, "state": "installed"}, with_block(text, at, rendered)
        if matches(found.text, rendered):
            return {"target": target, "state": "present"}, None
        if _differs_by_settings_alone(found.text, rules, place.rows):
            replaced = text[: found.start] + rendered + text[found.end:]
            return {"target": target, "state": "re-rendered", "replaced": found.text}, replaced
        if not overwrite:
            raise Refused(
                "the block differs from the rules file — an amended source not yet installed, or a "
                "copy edited in place; the tool cannot tell, so say --overwrite and read what it replaced"
            )
        replaced = text[: found.start] + rendered + text[found.end:]
        return {"target": target, "state": "overwritten", "replaced": found.text}, replaced
    if found is None:
        return {"target": target, "state": "absent"}, None
    if not matches(found.text, rendered):
        raise Refused(
            "the block differs from the rules file; reconcile the source, install with --overwrite, "
            "then retract"
        )
    return {"target": target, "state": "retracted"}, without_block(text, found)


def _differs_by_settings_alone(found: str, rules: RulesFile, rows: tuple[str, ...]) -> bool:
    """A block holding nothing but paragraphs of this file's own rules for this target, unedited:
    which of them it holds is the settings' doing, not an edit's nor an amendment's, so it is
    re-rendered without being asked."""
    inside = found.replace("\r\n", "\n").split("\n", 1)[1].rsplit("\n", 1)[0]
    held = {paragraph for paragraph in inside.split("\n\n") if paragraph}
    # Both sides normalised, as `matches` normalises them: a rules file kept in CRLF renders
    # bodies with CRLF, and a block in an LF target is still its own.
    could = {paragraph.replace("\r\n", "\n") for paragraph in rules.paragraphs(rows)}
    return bool(held) and held <= could


def _dropped_targets(root: Path, rules: RulesFile, files: set[str]) -> list[str]:
    """Every file holding a block of this source that the source no longer reaches: a target
    dropped from the rules file, or a group's member that stopped holding its heading, whose block
    the check would report as one nothing owns."""
    return [
        name for name in corpus(root)
        if name.endswith(".md") and name not in files
        and any(opening.group(1) == rules.slug for opening in INSTALLED_OPENING.finditer(without_code(_read(root / name))))
    ]


def _removal(root: Path, slug: str, target: str) -> tuple[dict, str]:
    """The block taken out by the retraction's own cut, so the file is what it was before the
    block was installed. It is installed, never authored, so nothing is asked; what it held is
    reported, as an overwrite reports what it replaced."""
    text = _read(root / target)
    found = locate(text, slug)
    if found is None or found.text is None:
        raise Refused("the block opens and never closes")
    return {"target": target, "state": "removed", "removed": found.text}, without_block(text, found)


def _written(root: Path, planned: list[tuple[str, str]], report: dict) -> dict:
    # The mover's contract: on a failure after mutation starts, stop and say what landed and what
    # did not. Nothing is rolled back; the maintainer inspects the files.
    done: list[str] = []
    for target, new_text in planned:
        try:
            _write(root / target, new_text)
        except OSError as failure:
            pending = [other for other, _ in planned if other not in done and other != target]
            report["refusals"] = [f"{target}: could not be written — {failure}"]
            report["done"] = done
            report["pending"] = pending
            return report
        done.append(target)
    return report


def check(root: Path) -> dict:
    """Every rules file against every target it names, every block against the rules files, and
    the settings against the declarations — what a tree carries read under its own settings."""
    files: dict[str, RulesFile | None] = {}
    blocks: list[dict] = []
    diagnostics: list[str] = []
    settings, problems = read_settings(root)
    diagnostics.extend(problems)
    for directory in sorted((root / MECHANISMS).glob("*/")) if (root / MECHANISMS).is_dir() else []:
        slug = directory.name
        if slug == LOCAL:
            diagnostics.append(f"{slug}: {_COLLISION}")
            continue
        if not (directory / f"{slug}.rules.md").is_file():
            continue
        try:
            files[slug] = read_rules_file(root, slug)
        except Refused as refusal:
            files[slug] = None
            diagnostics.append(f"{slug}: {refusal}")
    if (root / LOCAL_FILE).is_file():
        try:
            files[LOCAL] = read_rules_file(root, LOCAL)
        except Refused as refusal:
            files[LOCAL] = None
            diagnostics.append(f"{LOCAL}: {refusal}")
    reach: dict[str, set[str] | None] = {}
    listed = corpus(root)
    for slug, rules in files.items():
        if rules is None:
            continue
        diagnostics.extend(f"{slug}: {problem}" for problem in override_problems(root, rules))
        diagnostics.extend(f"{slug}: {problem}" for problem in condition_problems(rules, settings))
        try:
            places = reached(root, rules, listed)
        except Refused as refusal:
            reach[slug] = None
            diagnostics.append(f"{slug}: {refusal}")
            continue
        reach[slug] = {place.file for place in places}
        for place in places:
            state = _state(root, rules, place, settings)
            blocks.append({"slug": slug, "target": place.file, "state": state})
            if state not in ("present", "not called for"):
                diagnostics.append(f"{slug} in {place.file}: {state}")
    orphans = _orphans(root, files, reach, listed)
    diagnostics.extend(f"orphan block of {slug} in {path}" for slug, path in orphans)
    return {
        "rules files": len(files),
        "blocks": blocks,
        "orphans": [{"slug": slug, "file": path} for slug, path in orphans],
        "diagnostics": diagnostics,
    }


def check_line(report: dict) -> str:
    """One line for a host's hook, or nothing: how many things are out of step, and the run that
    brings the tree to match."""
    count = len(report["diagnostics"])
    if not count:
        return ""
    return (
        f"installed blocks: {count} thing{'s' if count > 1 else ''} out of step with the rules files and "
        "the settings — run `inject_rules.py --install`, then `--check` for what it could not mend"
    )


def _state(root: Path, rules: RulesFile, place: Reached, settings: Settings = NO_SETTINGS) -> str:
    target, anchor = place.file, place.anchor
    path = root / target
    if not path.is_file():
        return "target missing"
    text = _read(path)
    try:
        found = locate(text, rules.slug)
    except Refused as refusal:
        return str(refusal)
    rendered = rules.block(place.rows, settings)
    if rendered is None:
        return "not called for" if found is None else "present though the settings call for none of it"
    if found is None:
        try:
            after_anchor(text, anchor)
        except Refused as refusal:
            return "anchor ambiguous" if "ambiguous" in str(refusal) else "anchor missing"
        return "absent"
    if found.text is None:
        return "the block opens and never closes"
    if not matches(found.text, rendered):
        return "out of step with the settings" if _differs_by_settings_alone(found.text, rules, place.rows) else "drifted"
    if rules.slug == LOCAL and following_block(text, found.end):
        return "not last"
    return "present"


def _orphans(
    root: Path, files: dict[str, RulesFile | None], reach: dict[str, set[str] | None], listed: list[str]
) -> list[tuple[str, str]]:
    """A block whose slug has no rules file, or whose rules file does not reach that file. A rules
    file that cannot be read, or whose table cannot be resolved, is that file's diagnostic, and
    its blocks are judged by none."""
    orphans = []
    for name in listed:
        if not name.endswith(".md"):
            continue
        seen = without_code(_read(root / name))
        for opening in INSTALLED_OPENING.finditer(seen):
            slug = opening.group(1)
            rules = files.get(slug)
            files_reached = reach.get(slug)
            if slug not in files or (rules is not None and files_reached is not None and name not in files_reached):
                orphans.append((slug, name))
    return orphans


def _read(path: Path) -> str:
    with path.open(encoding="utf-8", newline="") as handle:
        return handle.read()


def _write(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    # The tree this script sits in; anything that imports it names its tree itself.
    sys.exit(main(sys.argv[1:], Path(__file__).resolve().parents[3]))
