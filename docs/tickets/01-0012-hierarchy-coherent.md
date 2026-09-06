# Hierarchy reads the same everywhere

- **Status:** Ready
- **Type:** HITL
- **Blocks:** [Scope reads the same everywhere](./01-0014-scope-coherent.md) — eight shared files
- **Outcome:** Hierarchy — from what height a thing is looked at — has one account, and every
  statement about height across the entry file, process, glossary and skills either is that account
  or points at it.

## Parent

[AGENTS.md](../../AGENTS.md), whose General rules and load-bearing section are where the concept
surfaced, 2026-09-06. Not a child of
[01-0010](./01-0010-dev-harness-shared-and-local.md): that ticket's contract is distributing a
canonical harness across projects, and the coherence of the method's own concepts is a different
contract — the same argument that kept [the pacer](./01-0020-pacer.md) out of it.

## Impact

**2026-09-06.** 33 hierarchy-flavoured statements across 9 files; heaviest in
`ticket/SKILL.md` (12), `docs/glossary.md` (6), `align/SKILL.md` (5). Eight of those nine files also
carry the scope statements owned by [01-0014](./01-0014-scope-coherent.md), so the two passes are
sequential, never parallel. Verdict: proceed.

## Why this exists

The project keeps reaching for height under different names and never says what it is. `/ticket`
calls it altitude and granularity; `/plan` and `/align` speak of high-level and resolution;
`AGENTS.md` distinguishes Tier 1 from Tier 2 and load-bearing from local; the glossary carries
scale, coarse and *Unit of work — proposed definition*. None of them defines the axis, so nothing
can be checked against it and each site is free to mean something slightly different.

The user's formulation, 2026-09-06: **hierarchy is from what heights we look at things.**

## What to build

- One account of hierarchy, stated once, with the glossary carrying the term.
- Every existing statement about height reconciled against it: restated as a pointer, corrected, or
  kept deliberately with its reason. Contradictions between two sites are findings, not style.
- The relationship to the already-settled idea/shape/thing axis and to load-bearing named
  explicitly, including whether they are the same hierarchy seen twice or genuinely different axes.
- The `Unit of work — proposed definition` and `Load-bearing seam — proposed definition` glossary
  entries either promoted out of "proposed" or retired.
- Two loose ends in the entry file's load-bearing section, from its 2026-09-06 review:
  "a thing is load-bearing when **several** of these are true" leaves the threshold unstated — name
  a number, or name which factors are individually sufficient and treat the rest as accumulating
  evidence. And the bad/better example is domain-specific (MongoDB, forecast issue-times) in a
  section that ships to every consuming project; **2026-09-06, user: keep it for now**, so it is
  wrapped in a `<temporary>` block bound to this ticket rather than left as an open "for now".

## Decisions this ticket's align owns

- Whether idea/shape/thing, load-bearing/local, and Tier 1/Tier 2 are one hierarchy or several.
  They cannot be reconciled without deciding this, and the answer changes every downstream site.
- Where the canonical account lives. **Provisionally deferred:** this ticket lands the *concept*;
  which skill or document *hosts the operational rules* is
  [responsibility](./01-0016-responsibility-coherent.md)'s. Say so in the account itself so the
  later pass is a move, not a reopening.

## Acceptance criteria

- [ ] Hierarchy is defined once, in the glossary, and the entry file carries the Tier 1 line.
- [ ] Every one of the 33 statements has been read and dispositioned: pointer, correction, or kept
  with a reason. The count is reported.
- [ ] No two sites make contradictory claims about height; the check is mechanical enough to rerun.
- [ ] The relationship between the height axis and load-bearingness is stated, not implied.
- [ ] `/verify` has been run on this ticket against its ticket, RFC, and governing docs.

## Out of scope

Scope, responsibility and reachability — their own tickets. Installing any skill.

