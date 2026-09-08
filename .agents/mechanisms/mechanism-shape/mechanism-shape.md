# mechanism-shape — what counts as a mechanism, what one is made of, and where each part lives

- **instruction** `.agents/skills/mechanism/SKILL.md` — the shape: membership, the three homes, moments, injection, incept and amend
- **state** always on
<project-local>
- **evidence** `docs/mechanisms/mechanism-shape.evidence.md`
- **declared by** `docs/tickets/done/01-0011.0010-mechanism-declared.md`
</project-local>

## How it works

A mechanism is part of how the work gets done, and it owes an account of itself: one instruction
file, a doc saying why that instruction is what it is, and evidence saying why the doc is. This
mechanism is that rule, and it is declared by its own shape — the first application, and the one
that would be worthless if the shape could not carry it.

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
| telling an inceptor what to hand `/maintain` | — | not yet — the sentence is the maintenance mechanism's rule, authored in its rules file with this skill's *Incept* as target, and no installer carries it here, [.0020](../../../docs/tickets/01-0011.0020-rules-one-home.md) |
| amending a declared one, editing a skill that is an instruction file included | `.agents/skills/mechanism/SKILL.md` | |
| checking that a declaration is true | `.agents/scripts/mechanisms.py` | |
| installing a mechanism's rules into skills it does not own | — | not yet — no installer exists, and every rule reaching another skill is hand-copied until one does, [.0020](../../../docs/tickets/01-0011.0020-rules-one-home.md) |
| retracting them | — | not yet — one installer owns both directions or neither is mechanical, [.0020](../../../docs/tickets/01-0011.0020-rules-one-home.md) |
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
| this doc | `.agents/mechanisms/mechanism-shape/mechanism-shape.md` |
| the check | `.agents/scripts/mechanisms.py` |
| the check's tests | `tests/test_mechanisms.py` |

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| the method's vocabulary | `.agents/glossary.md` | nobody removable |
| citation reader | `.agents/scripts/docs_corpus.py` | the ticket mechanism, from `01-0011.0025`; a declared gap until then, and not a live question while nothing installs or extracts |
| test harness | `tests/harness.py` | same |

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

Nothing else is emitted. This mechanism injects no rules, so it has no rules file, and it writes
no records beyond the mechanism directories that are its records.

## Not yet at the shape

**Nothing runs the check unasked.** It runs when a person types it, or when the project's
verification set is run, which happens at `/verify`. That is better than remembering and weaker
than a mechanism that speaks at wake; this tree has no hook to speak from. A run that stays quiet
because nobody started it is indistinguishable from one that passed.

**Absence is not clearance.** A clean run means nothing was caught. It never means the tree obeys.

**Run it over what already exists has no bite here, and this is not a zero.** That rule exists so
a check landing today cannot claim a clean history it never looked at. This is the first
mechanism, so there is no prior corpus to sweep — not a corpus swept and found clean. The rule's
first real application is [.0050](../../../docs/tickets/01-0011.0050-shape-checked.md), whose
sweep meets every skill installed before the shape existed.

**Two declared mechanisms are still thin evidence for a shape.** The second application, at
`01-0011.0022`, forced three amendments and found two rows the check would have failed; the third
application is the first that meets a record-bearing mechanism.

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
