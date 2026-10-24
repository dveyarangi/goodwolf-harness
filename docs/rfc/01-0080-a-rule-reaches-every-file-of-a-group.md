# A rule reaches every file of a group — implementation plan

- **record of** what it intends to become

**Authored:** 2026-10-25

Implements [01-0080](../tickets/01-0080-a-rule-reaches-every-file-of-a-group.md): an anchor-table
row whose target is a path pattern names a group, and the installer, its check and the harness's
rehearsal treat every member as they treat an explicit target.

**Planning state:** authored 2026-10-25 against q-0037.0002's accepted `Where it stands`, its two
decisions, `inject_rules.py` whole, the harness's injection rehearsal, the rules-file format, the
mechanism skill and the architecture's *Installed blocks*. Validated once. Two choices taken here
are under *Taken at `/plan`*.

## Governing boundaries

- **One installer, one grammar.** A rule's only home is its rules file; it reaches a file only as
  an installed block written by the one generic installer
  ([Installed blocks](../architecture.md#installed-blocks)). A group changes how a target is
  addressed, never where a rule lives or who writes it.
- **Refuse rather than guess, validate before writing.** Every member is validated before anything
  is written, and a refusal changes no file (the same section). A member is no weaker than an
  explicit target: drift is refused unless overwritten, an anchor held twice is refused.
- **A mechanism has one place in a target** (the format's anchor table). A file reached twice — by an
  explicit row and a pattern, or by two patterns — is refused.
- **Membership from both ends** (q-0037.0002, decision 1): the pattern at the mechanism's end, the
  anchor line at the member's. A matching file without the anchor is no member, passed over.
- **The tree's own listing.** Members are read from the same listing every script uses,
  `docs_corpus.corpus`, tracked and untracked-but-unignored files alike, so a skill written this
  session is a member before it is committed.

## Impact

**Must change.**

- `.agents/scripts/gw/inject_rules.py`
  - the anchor table read as before; a row's target containing a glob character is a pattern;
  - a function resolving a rules file's rows to the files they address — each file with the row it
    came from and that row's anchor — explicit rows as themselves, a pattern row as every listed
    file it fully matches that holds its anchor line outside code;
  - install, retract, the dropped-target removal, the check's per-target states and the orphan scan
    iterate the resolved files instead of the table's keys;
  - a rendered block selects its rules by the row a file came from, since a rule's `target` bullet
    names the pattern, not the file;
  - the `TODO q-0037.0002` at the missing-anchor refusal comes out: a pattern row never reaches it.
- `.agents/scripts/gw/harness.py`, `_injection_inputs`: a pattern row is expanded over the files as
  the copy leaves them — shipped and held — so the rehearsal reads every member the real install
  will write.
- `.agents/skills/mechanism/MECHANISM-FORMAT.md`, the anchor table's paragraph;
  `.agents/skills/mechanism/SKILL.md`, *Refuse rather than guess* and *installed in every target it
  names*; `docs/architecture.md`, *Installed blocks* — the five straw dogs bound to q-0037.0002,
  rewritten to what lands.
- `.agents/scripts/gw/test/test_inject_rules.py` and `test_harness.py`: the group's cases.

**Must verify.** Every rules file of this tree installs as before — none has a pattern row — and
`inject_rules.py --check` stays green; a recipient install runs the rehearsal and the real install
over the same members.

**Hidden edges.**

- **The block is chosen by the row, the file by the resolution.** Today `RulesFile.block(target)`
  picks the rules whose `target` is that file; a member's rules name the pattern. The resolution
  carries the row, and the block is rendered for it. Mixing the two would install nothing into a
  member and report it present.
- **Which glob.** `PurePosixPath.full_match`, where `*` does not cross a `/`: `.agents/skills/*/SKILL.md`
  matches each skill's file and no file deeper. A pattern written with `**` reaches deeper by
  intent.
- **The listing is git's.** A tree that is no git repository has no listing; the installer already
  needs one for the orphan scan and the dropped targets, so nothing new is assumed.
- **A member's anchor held twice** is a member, refused at planning, as decision 2 has it.

**Leave alone.** The local file's block and its last place; settings and `when` conditions, which
apply per rule as before; `--set` and `--settings`; the debugging mechanism.

## Taken at `/plan`

1. **A pattern is recognised by its characters,** `*`, `?` or `[`, not by a new column or marker in
   the anchor table. Not: a `group` column — a third cell every existing table would need; the
   target cell already says what it addresses.
2. **The resolution is one function both modes and the check call,** returning each addressed
   file with its row's key and anchor. Not: patterns expanded into the anchor table at parse time —
   parsing would need the tree, and the parsed rules file would stop being the file's reading.

## Shapes

A row of a rules file's anchor table, the voice's to be:

```md
| target | anchor |
|---|---|
| `AGENTS.md` | `## General rules` |
| `.agents/skills/*/SKILL.md` | `## What the person hears` |
```

and a rule naming the group as its target, as any target is named:

```md
- **target** `.agents/skills/*/SKILL.md`
```

The flow, for install, retract and the check alike: read the rules file → resolve its rows to
`(file, row, anchor)` over the tree's listing, refusing a file reached twice → for each file, the
block the row's rules render under the settings → plan, refuse or write as today. The dropped-target
removal and the orphan scan read *the resolved files* where they read the table's keys today.

## Stages

Each stage ends green on the verification set; the tests run, scripts changing.

1. **The resolution, red first** — in `test_inject_rules.py`, a case class `Grouping` with a tree of
   three skills, two holding the heading, and a rules file whose row is a pattern:
   - install writes the block into the two that hold the heading, not the third, and into no file
     the pattern misses though it holds the heading;
   - a skill that gains the heading is *absent* at the check, and the next install fills it;
   - a skill that loses its heading holds a block the check calls an orphan, and the next install
     takes it out;
   - a pattern matching nothing installs nothing, and the check is green;
   - a file named by an explicit row and matched by the pattern is refused, nothing written;
   - a member holding the heading twice is refused, nothing written;
   - retract leaves every member byte-identical to before the install.

   Then the resolution, and install, retract, removal, check and orphans read through it.
2. **The rehearsal** — in `test_harness.py`, a recipient install whose shipped rules file has a
   pattern row reaches a member shipped with core and a member the recipient holds; then
   `_injection_inputs` expanded.
3. **The texts** — the five straw dogs rewritten to what landed, each wrapper removed by
   `straw_dogs.py --remove`; the `TODO q-0037.0002` gone; `mechanisms.py --check` and
   `inject_rules.py --check` green.

## Proof of the criteria

| Criterion | Proven by |
|---|---|
| installed in every matching file that holds the heading, and no other | stage 1, first case |
| a file gaining the heading is reported, then filled | stage 1, second case |
| a file losing it is reported, then emptied | stage 1, third case |
| an empty group installs nothing, no finding | stage 1, fourth case |
| a file both explicit and a member is refused | stage 1, fifth case |
| every rules file of this tree installs as before, the check green | the verification set after stage 3 |
| `/verify` passes | `/verify` after stage 3 |

## Out of scope

The voice's rules file and its group row —
[01-0016.0030](../tickets/01-0016.0030-the-voice-speaks-every-skill-that-speaks.md). A group a member
declares by a mark of its own — refused in the question.
