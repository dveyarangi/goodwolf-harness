# mechanism-shape — what counts as a mechanism, what one is made of, and where each part lives

- **instruction** `.agents/skills/mechanism/SKILL.md` — the shape: membership, the three homes, moments, injection, records, incept, amend and retire
- **state** always on
<project-local>
- **evidence** `docs/mechanisms/mechanism-shape.evidence.md`
</project-local>

## How it works

A mechanism is part of how the work gets done, and it owes an account of itself: one instruction
file, a doc saying why that instruction is what it is, and evidence saying why the doc is. This
mechanism is that rule, and it is declared by its own shape — the first application, and the one
that would be worthless if the shape could not carry it.

The three homes cut on **when the thing is read** — session start, the work a rule governs, or
changing the mechanism itself. There is no fourth home because there is no fourth occasion, and any
other cut — by subject, by author, by importance — puts a rule where its reader is not.

**A format shelf declares form; why a form is what it is belongs here.** The shelf is read while
writing to the form, and a reason at that moment is text between the reader and the thing they
came for. The cut is the same one the three homes make, applied inside a mechanism's own parts.

**A mechanism declares its own records** because no other mechanism can say when someone else's
record is finished. A maintainer's duty to archive finished records is a duty to read that
declaration, so a record that carries none is a duty that cannot be discharged rather than a duty
nobody has.

**One instruction file**, so that naming a mechanism and naming its skill are one act. A second
would make every reference ambiguous at the moment it is needed most, and it is what lets a moment
instructed `elsewhere` resolve against a file rather than against a declaration that may not exist
yet.

**Mechanical by construction**, because a mechanism whose parts a script cannot enumerate cannot be
checked, and an unchecked declaration is exactly the label this shape exists to prevent.

It is **always on**. Nothing can install or uninstall the thing that defines what installing
means, so it has no lifecycle scripts, and the parts table below is what a person moving this
between trees takes rather than what an installer adds.

The check is what makes the declaration a claim rather than a label. It rules on form: whether
every named part is where the doc says, whether each moment carries an instruction or a stated
kind of absence, whether the referents resolve. Whether a moment *should* exist, and whether an
absence is honestly classified, are judgements it records and never makes.

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| deciding whether a thing is a mechanism | `.agents/skills/mechanism/SKILL.md` | |
| incepting one | `.agents/skills/mechanism/SKILL.md` | |
| telling an inceptor what to hand `/maintain` | `.agents/skills/mechanism/SKILL.md` | |
| amending a declared one, editing a skill that is an instruction file included | `.agents/skills/mechanism/SKILL.md` | |
| retiring a declared one | `.agents/skills/mechanism/SKILL.md` | |
| installing a declared mechanism into a tree, and removing it | — | not yet — the parts table says what an install adds and nothing says how; no installer exists, [01-0010](../../../docs/tickets/01-0010-dev-harness-shared-and-local.md) |
| checking that a declaration is true | `.agents/scripts/mechanisms.py` | |
| installing a mechanism's rules into skills it does not own | `.agents/scripts/inject_rules.py` | |
| retracting them | `.agents/scripts/inject_rules.py` | |
| re-checking a mechanism when what governs it has moved | — | elsewhere — re-checking derived work against a changed source is maintenance, `.agents/skills/maintain/SKILL.md` |
| writing or changing a skill's text | — | elsewhere — a sibling mechanism's subject, and both apply when a skill is an instruction file, `.agents/skills/skill-up/SKILL.md` |
| recording that an installed skill belongs to no mechanism | — | not yet — the shape requires an allowlist and this tree has none, so a skill nothing claims is silent rather than declared, [.0050](../../../docs/tickets/01-0011.0050-shape-checked.md) |
| finding a mechanism's doc, or asking what is declared at all | — | unowned by design — the directory is a routing table and the index renders it on request; looking something up needs no rule |

## Install adds, uninstall removes

| part | where |
|---|---|
| instruction file | `.agents/skills/mechanism/SKILL.md` |
| format shelf | `.agents/skills/mechanism/MECHANISM-FORMAT.md` |
| trigger | `AGENTS.md` → "is mechanism work: use" |
| the hand-edit rule | `AGENTS.md` → "is not that file's to edit" |
| this doc | `.agents/mechanisms/mechanism-shape/mechanism-shape.md` |
| its rules file | `.agents/mechanisms/mechanism-shape/mechanism-shape.rules.md` |
| the check | `.agents/scripts/mechanisms.py` |
| the check's tests | `.agents/scripts/test/test_mechanisms.py` |
| the installer | `.agents/scripts/inject_rules.py` |
| the installer's tests | `.agents/scripts/test/test_inject_rules.py` |
| citation reader | `.agents/scripts/docs_corpus.py` |
| test harness | `.agents/scripts/test/harness.py` |

The last two are shared by every script in the tree and claimed here because this mechanism is
the one that cannot leave: where a shared part's ownership bites, the claimant is the always-on
mechanism, so no uninstall can remove what another mechanism needs *(the user, 2026-09-08,
applying the spec's ownership decision)*.

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| the method's vocabulary | `.agents/glossary.md` | nobody removable |

## What it produces, and who reads it

- **This declaration** — read by whoever amends a mechanism or debugs one, and parsed by the check
  on every `/verify`.
- **[The evidence](../../../docs/mechanisms/mechanism-shape.evidence.md)** — read at amend time,
  by whoever is about to change this doc and needs to know what was already refuted. Never read
  during ordinary work, which is why it lives outside `.agents/` and is excluded from re-checks.
- **`--check`'s report** — read by `/verify` through the verification set, and by anyone who runs
  it. Its exit status is what the set consumes; its JSON is for the person reading a failure.
- **`--index`'s render** — read on request by someone asking what is declared. **Nothing runs it
  unasked**, and nothing consumes its output: it exists so the register never becomes a file, and
  a register nobody asks for is a register nobody needed.

- **Its rules file** — `mechanism-shape.rules.md`, read by the installer alone, and by whoever
  amends a rule of the shape that other skills read. Its block is installed in `/maintain` and in
  this mechanism's own skill, which reads R1 and R4 at incept.
- **The installer's `--check` report** — read by `/verify` through the verification set, and by
  anyone who runs it. Its exit status is what the set consumes; a block absent, drifted or
  owned by nothing is what it fails on.

Nothing else is emitted. It writes no records beyond the mechanism directories that are its
records.

## Not yet at the shape

<straw-dog until="01-0010.0120 is done" ticket="docs/tickets/01-0010.0120-host-delivery-surfaces.md">
**Nothing runs the check unasked.** It runs when a person types it, or when the project's
verification set is run, which happens at `/verify`. That is better than remembering and weaker
than a mechanism that speaks at wake; this tree has no hook to speak from. A run that stays quiet
because nobody started it is indistinguishable from one that passed.
</straw-dog>

**Absence is not clearance.** A clean run means nothing was caught. It never means the tree obeys.

**Nothing refuses to retract the shape's own block from its own skill.** R1 and R4 are installed
into this mechanism's instruction file by the same tool that retracts them, and an always-on
mechanism cannot be retired. The shape's block absent from `/mechanism` under `--check` is the
signal that the always-on mechanism has lost what it installed into itself, and the check is
what says it happened.

**Run it over what already exists has no bite here, and this is not a zero.** That rule exists so
a check landing today cannot claim a clean history it never looked at. This is the first
mechanism, so there is no prior corpus to sweep — not a corpus swept and found clean. The rule's
first real application is [.0050](../../../docs/tickets/01-0011.0050-shape-checked.md), whose
sweep meets every skill installed before the shape existed.

**Three declared mechanisms are still thin evidence for a shape.** The second application, at
`01-0011.0022`, forced three amendments and found two rows the check would have failed; the third,
at `01-0011.0025`, met the first record-bearing mechanism and forced two more — one moment the
shape had no row for, and one header bullet that turned out to feed a check nothing needed. The
fourth is [01-0017](../../../docs/tickets/01-0017-io-graph-coherent.md)'s, and it meets the rest of
the corpus at once.

## What retires this

A tree that can derive a mechanism's parts and moments from itself, making a doc that asserts them
a second home for what the code already says. Until then, declaration is the only way the claim
exists at all. Retirement removes the parts above, this directory, and the trigger — which is a
part, so retracting the mechanism takes its own entry point with it.

## What would show it working, graded by someone who did not build it

The next mechanism declared — `/maintain`, at
[.0022](../../../docs/tickets/done/01-0011.0022-shape-survives-second-mechanism.md) — either passes
this check unedited, or the check has to change to admit it. Which of those happens is the shape's
first real test, and the session that runs it is not this one.

A declaration hand-fixed until the check went quiet is this mechanism failing, and reads
identically to success in the check's own output. The grader is whoever declares the second
mechanism: they answer whether the shape fitted something it was not written against, or whether
the second subject had to be bent to fit the first.
