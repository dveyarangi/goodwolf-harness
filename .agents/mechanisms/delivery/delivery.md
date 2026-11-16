# delivery — the ring a unit of work goes through: planned against what governs it, done, and verified against its criteria, whatever the work is

- **instruction** `.agents/skills/plan/SKILL.md` — planning: the unit's plan, validated against its governing decisions before anything is built
- **instruction** `.agents/skills/implement/SKILL.md` — doing the agreed work
- **instruction** `.agents/skills/verify/SKILL.md` — verifying: the landed work against its unit, its plan, its governing decisions and the project's checks
- **state** installed
- **record of** what must always hold
- **owner** core

## How it works

A unit of agreed work goes round three steps: it is planned, it is done, it is verified. Planning
reads what governs the unit and settles every choice that shapes more than the unit itself;
doing writes the work to that plan; verifying compares what landed with the unit's criteria, the
plan and the decisions that govern it, and runs the project's checks. Planning repeats until no
load-bearing doubt is left, doing and verifying repeat until the checks pass, and a discrepancy no
step may settle alone goes to the person. Work closes with its commit once verification passes.

**The steps are general.** A unit may be code, a document, a rule of the method or anything else
with an outcome and criteria; a step's own text holds for any of them. How a project
writes its tests, its code and its comments, and documents its architecture, is its practice — a
mechanism of its own that reaches the steps as installed text, so a project changes how it builds
without editing a step *(the user, 2026-11-16)*.

**What the ring uses and does not own.** Slicing work into units opens the ring, and it and the
unit's record are the ticket mechanism's. Bringing a decision to the person, tracing a change's
reach and holding the tree in agreement serve the ring and more than it; they are not this
mechanism's, nor practice, and the practice may reach them too *(the user, 2026-11-16)*. The plan is
this mechanism's record, one per unit and named by it; the paired close that ends it is the ticket
mechanism's.

<straw-dog question="q-hrfk7l">
**The ring's order, the ladder and the homes of decisions** stand in the entry file, authored
there by hand: the delivery ring and where it returns for a decision, development's ladder, and
where a load-bearing decision lands. They are this mechanism's text and move into its rules file.
</straw-dog>

**Who decided.**

| what | decided by |
|---|---|
| the ring's form and its practice are two mechanisms; the steps serve work that is not code | the user, 2026-11-16, revising the one mechanism of 2026-10-25 |
| the name, delivery | the user, 2026-11-16 |
| `/align`, `/maintain` and `/impact` are neither its own nor practice, and the practice may reach them | the user, 2026-11-16 |

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| planning a unit of work against its governing decisions | `.agents/skills/plan/SKILL.md` | |
| validating a plan again before it is built | `.agents/skills/plan/SKILL.md` | |
| doing the agreed work | `.agents/skills/implement/SKILL.md` | |
| verifying landed work against its criteria, its plan and the checks | `.agents/skills/verify/SKILL.md` | |
| mending a discrepancy, or taking it to the person | `.agents/skills/verify/SKILL.md` | |
| committing the work once verification has passed | `.agents/skills/implement/SKILL.md` | |
| slicing work into units, and keeping the unit's record | — | elsewhere — the unit and its shape are the ticket mechanism's, `.agents/skills/ticket/SKILL.md` |
| closing a plan with its unit | — | elsewhere — the paired close is the ticket mechanism's, run by the maintenance pass, `.agents/skills/maintain/SKILL.md` |
| reading the ring's order, the ladder and where a decision lands | — | embedded — authored by hand in the entry file, `AGENTS.md` |
| installing this mechanism into a tree, with the rest of core | `.agents/scripts/gw/harness.py` | |
| removing this mechanism from a tree | — | <straw-dog question="q-qzeuf3">not yet</straw-dog> |

## Install adds, uninstall removes

| part | where |
|---|---|
| planning | `.agents/skills/plan/SKILL.md` |
| doing | `.agents/skills/implement/SKILL.md` |
| verifying | `.agents/skills/verify/SKILL.md` |
| this doc | `.agents/mechanisms/delivery/delivery.md` |

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| the unit's record | `.agents/skills/ticket/TICKET-FORMAT.md` | `ticket` |
| the project's checks, in its local block | `local.rules.md` | the project |
| the method's vocabulary | `.agents/glossary.md` | nobody removable |

## What it produces, and who reads it

- **The plan** — *what it intends to become, what happened once closed* — read by doing for what
  to build, by verifying for what was meant, and by every later validation pass over it; closed
  with its unit by the maintenance pass.
- **The verified criteria** — *its format's* — the unit's boxes checked with their dates, read by
  the maintenance pass for whether the unit is finished.

Nothing else. The work itself is the project's, not a record of this mechanism.

## Not yet at the shape

<straw-dog question="q-ggpx2r">**The steps still say *code* where they mean the work** — `/implement`'s
description, *architecture must lead code shape* in `/plan`, *documents against code* in
`/verify`. Each holds for any unit read so; a word for the work that is not code is not
settled.</straw-dog>

<straw-dog question="q-hrfk7l">**Its text is in the entry file**, authored by hand; it has no rules
file yet.</straw-dog>

<straw-dog question="q-oehis2">**The plan's record is declared in part**: its name and header in
planning's own text, its close in the ticket mechanism's, its tier nowhere.</straw-dog>

## What retires this

Nothing in this tree: a unit of work is planned, done and verified however the method is cut. A
project with a ring of its own retires it there by removing it, not by amending it.

## What would show it working, graded by someone who did not build it

1. **A fresh agent, given this doc alone**, says what delivery is for and that its steps serve work
   that is not code. Run at its declaration.
2. **The session that declares the practice** grades the line between them: could every rule of
   practice leave the steps without a step's own text changing what it says? A step that had to be
   reworded to let a practice rule out is this doc having drawn the line wrong.
