# Rules reach the occasion they are for

- **Status:** Planned (responsibility precedes)
- **Type:** HITL
- **Depends on:** [Each skill owns its own responsibility](./01-0016-responsibility-coherent.md)
  (a rule must be correctly owned before its arrival can be checked)
- **Related:** [01-0010.0120](./01-0010.0120-host-delivery-surfaces.md) — **surfaced 2026-09-07:**
  this ticket's *where it cannot be, the gap is named* assumes an answer about what the hosts can
  deliver that nobody has established. That ticket establishes it; this one decides what to do
  with the gaps that remain.
- **Outcome:** A rule or skill that applies at an occasion is actually in front of the agent at that
  occasion, and where it cannot be, the gap is named rather than assumed away.

## Parent

[AGENTS.md](../../AGENTS.md). Sibling of [01-0012](./01-0012-hierarchy-coherent.md),
[01-0014](./01-0014-scope-coherent.md) and [01-0016](./01-0016-responsibility-coherent.md), the
fourth rule refactor. All four now run after
[the mechanism shape](../spec/01-0011-mechanism-shape.md).

## Impact

**2026-09-06.** Assessed with the other three in one pass. Touches the entry file, every installed
skill's cross-references, and the glossary's existing Tier 1 / Tier 2 / Delivery evidence / Rule
slice entries, which are vocabulary already waiting for this ticket. Verdict: proceed, last of the
four — arrival cannot be checked before ownership is settled.

## Why this exists

Correct ownership does not produce arrival, and this project has an observed instance.

**2026-09-06, evidence:** the rule that decomposition runs `/ticket` → `/impact` is unambiguous and
correctly owned — it is [`/ticket` §3.1](../../.agents/skills/ticket/SKILL.md). During an `/align`
in this repository the agent produced a ticket-shaped breakdown by unaided grouping and skipped the
chain entirely. Nothing was wrong with where the rule lived. Nothing pointed at it from where the
agent was standing.

That is the whole subject: a rule can be well written, well owned, and never reach the occasion.

## What to build

- An account of reachability: what it means for a rule or skill to reach an occasion, and what
  counts as evidence that it did. The glossary's **Delivery evidence** entry already insists this is
  distinct from a file existing.
- Which skill names which, and at what point in its body. The absorbed question from the earlier
  draft: every skill that operates on shapes should name [/impact](../../.agents/skills/impact/SKILL.md)
  and [/discover](../../.agents/skills/discover/SKILL.md) — investigate whether that is one rule in
  the entry file or a pointer in each skill, and land whichever the investigation says.
- What belongs at Tier 1 versus Tier 2, stated as a rule rather than per-case judgement.
- Known unreachable rules recorded as such, with owners.

## Decisions this ticket's align owns

- Whether reachability is enforced mechanically — a check that every named chain is pointed at from
  its calling site — or remains a maintained convention.
- What Tier 1 is allowed to cost. Every rule promoted to the entry file is paid for on every turn in
  every project, which is the constraint that stops "put it at Tier 1" being the answer to
  everything.
- Whether host discovery evidence, which the install tickets each collect separately, belongs here
  as one mechanism.

## Acceptance criteria

- [ ] Reachability is defined once, in the glossary, with what counts as evidence of arrival.
- [ ] Every skill-to-skill chain the harness relies on is pointed at from the site that must run it;
  the inventory is reported, including the chains that are not.
- [ ] The `/ticket` → `/impact` chain is reachable from inside `/align`, demonstrated on real work.
- [ ] A stated rule decides Tier 1 versus Tier 2 placement.
- [ ] `/verify` has been run on this ticket against its ticket, RFC, and governing docs.

## Out of scope

Hierarchy, scope and responsibility. The pacer's session-resumption rules, which are
[01-0020](./01-0020-pacer.md)'s even though they are also Tier 1.
