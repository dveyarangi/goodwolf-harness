# Scope reads the same everywhere

- **Status:** Planned (hierarchy precedes)
- **Type:** HITL
- **Depends on:** [Hierarchy reads the same everywhere](./01-0012-hierarchy-coherent.md) (eight
  shared files, and height is half of what scope is stated against)
- **Outcome:** Scope — the extent of what a pass, a ticket or a document covers — has one account,
  and every scope statement across the harness either is that account or points at it.

## Parent

[AGENTS.md](../../AGENTS.md) and [the process](../process.md). Sibling of
[01-0012](./01-0012-hierarchy-coherent.md), on the same argument for staying out of
[01-0010](./01-0010-dev-harness-shared-and-local.md).

## Impact

**2026-09-06.** 37 scope statements across 12 files; heaviest in `maintain/SKILL.md` (11),
`docs/process.md` (5), `TICKET-FORMAT.md` (4). Eight files overlap
[01-0012](./01-0012-hierarchy-coherent.md)'s set. Verdict: proceed, strictly after 01-0012.
Amending 01-0012's prose at a shared site is this ticket's completion, not a reopened decision.

## Why this exists

Scope is asserted everywhere and defined nowhere. `/maintain` requires a declared scope and says a
scope "is the work and its dependencies, not a list of filenames". `/impact` calls its version
blast radius. `/spec` is "change-scoped". `/ticket` has `Out of scope` and `Parent scope addressed`.
`AGENTS.md` says `/impact` determines "the scope and load-bearingness of the shape". The glossary
defines neither scope nor blast radius.

Whether these are one concept at different resolutions or several concepts sharing a word is
exactly what nobody has had to answer, and a pass that cannot say what its scope was cannot report
coverage honestly.

## What to build

- One account of scope, with the glossary carrying the term, and its relation to blast radius,
  declared scope, out-of-scope and parent scope made explicit — same concept or distinct ones.
- Every existing scope statement reconciled against it, dispositioned as pointer, correction, or
  deliberate keep with a reason.
- The relationship to height settled by [01-0012](./01-0012-hierarchy-coherent.md) stated: whether
  scope and height are two axes of one act, or independent.

## Decisions this ticket's align owns

- Whether blast radius, declared scope and change scope are one concept. If they are, one term wins
  and the glossary's *Avoid* list carries the rest.
- What a scope must name to be declarable — `/maintain` already asserts "the work and its
  dependencies", which is a rule with no home.
- Hosting of the operational rules is deferred to
  [responsibility](./01-0016-responsibility-coherent.md), as in 01-0012.

## Acceptance criteria

- [ ] Scope is defined once, in the glossary, with its relation to blast radius stated.
- [ ] All 37 statements read and dispositioned; the count is reported.
- [ ] No two sites make contradictory claims about what a scope is or what declaring one requires.
- [ ] 01-0012's shared sites are re-read after this pass and still agree.
- [ ] `/verify` has been run on this ticket against its ticket, RFC, and governing docs.

## Out of scope

Hierarchy, responsibility and reachability. Installing any skill.
