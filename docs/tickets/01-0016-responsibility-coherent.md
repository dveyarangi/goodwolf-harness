# Each skill owns its own responsibility

- **Status:** Planned (hierarchy and scope precede)
- **Type:** HITL
- **Depends on:** [Scope reads the same everywhere](./01-0014-scope-coherent.md) (settled
  vocabulary for what a responsibility covers), [/impact recommends the work's
  shape](./01-0010.0080-impact-work-shape.md) (so this pass sees a finished `/impact`)
- **Blocks:** [Rules reach the occasion they are for](./01-0018-reachability-coherent.md)
- **Outcome:** Every skill states only what it owns and links for the rest; a rule appears once, in
  the skill responsible for it; contradictions between skills are resolved rather than coexisting.

## Parent

[AGENTS.md](../../AGENTS.md) and [the process](../process.md#mechanisms-and-skills), which already
says a mechanism is maintained whole but does not say which skill owns which rule.

## Impact

**2026-09-06.** `/align` is 137 lines over 15 sections; `/impact` is 54. At least four of `/align`'s
sections are another skill's work: "Check whether it was already decided" and "Cross-reference with
code" are `/impact`'s enumerated checks; "Challenge against the Edge records" is `/edge`'s and
`/maintain`'s; "Record resolutions in the owning ticket inline" is `/ticket`'s and
`TICKET-FORMAT`'s. Two more are arguable rather than obvious: "Update glossary.md inline" and
"Update architecture.md inline". Verdict: proceed. The pass touches every installed skill, so it
runs after the vocabulary tickets and before reachability.

## Why this exists

**2026-09-06, user:** `/align` is very noisy — instead of specifying the entire flow methodology
directly it should link to the skills that cover those responsibilities, and the responsibilities
should be well defined. `/impact` can host the whole section about investigating what exists.

The same restatement happens elsewhere: `/verify` restates repair-and-report that
[the process](../process.md#autonomy-and-repair) owns; `/maintain` restates archive eligibility that
`TICKET-FORMAT` owns; `/plan` and `/ticket` both carry slicing rules. Restatement is how two sites
drift apart without either being edited.

**2026-09-06, `/maintain` — observed drift.** The queue's `Current stage` line asserted "entry
contract at v2" and told the next session to check its first line said v2, while
[AGENTS.md](../../AGENTS.md), which owns the entry contract and its version, was already at v3. Both
the restatement and the bump landed in `0538387`, so the copy was wrong from the commit that made
it: no edit drifted them apart, the second home was never true. Repaired by deleting the assertion
and pointing at the owner; the resume instruction keeps its function without naming a version. This
is the class of defect this ticket exists for, caught in a record rather than a skill.

This ticket also hosts the canonical accounts that
[01-0012](./01-0012-hierarchy-coherent.md) and [01-0014](./01-0014-scope-coherent.md) deliberately
left unhosted.

## What to build

- A stated responsibility for each installed skill: what it owns, what it delegates, and to whom.
- Restated methodology replaced by links. A skill keeps a rule only if it owns it.
- Contradictions between skills surfaced and resolved, not annotated.
- Repair-and-report moves into the skill. **2026-09-06, user:** the `/maintain` bullet that links
  out to [the process](../process.md#autonomy-and-repair) should carry the rule itself instead. It
  currently lives in `docs/process.md` and is linked from `/verify`, `/implement` and `/maintain`,
  while [the pacer's temporary block](../process.md) says step rules move into their skills as those
  skills install. What this pass still owes is the consequence, not the decision: three skills apply
  the rule, so moving it into one of them either duplicates it or makes that skill its owner and the
  others its callers.
- The investigation responsibility consolidated into `/impact`, per the user's example.

## Decisions this ticket's align owns

- Whether responsibility is owned per skill, per mechanism, or per rule. `docs/process.md` defines
  a mechanism as spanning several skills, so "one skill owns one rule" may not hold.
- Whether `docs/process.md` survives this pass as a rule home or becomes policy-only — its
  `<temporary>` block already promises the sequence to [the pacer](./01-0020-pacer.md).
- Whether "update the glossary/architecture inline" is `/align`'s or `/maintain`'s.
- A live instance to settle: on 2026-09-06 `/verify`'s skill body lost its opening line — "`/verify`
  is the verification of landed work, not only documentation or shape review" — while
  [the process](../process.md#verification) still says it. The skill and its governing document now
  differ in emphasis, and nothing decided that. Whichever way it resolves, one of them stops
  saying it.

## Already landed

**2026-09-06:** `/align` now states that decomposing work during an align belongs to `/ticket`,
which calls `/impact`, and that the chain's output is presented as a suggestion without minting.
Landed early at the user's direction; the rest of `/align`'s de-noising is this ticket's.

## Acceptance criteria

- [ ] Every installed skill states what it owns and what it delegates.
- [ ] No rule appears in full in two skills; the check is mechanical enough to rerun.
- [ ] `/align` carries no methodology it does not own, and links instead.
- [ ] Repair-and-report has one home, cited by everything that applies it.
- [ ] The canonical accounts deferred by 01-0012 and 01-0014 have hosts.
- [ ] `/verify` has been run on this ticket against its ticket, RFC, and governing docs.

## Out of scope

Whether a rule *arrives* where it is needed — [reachability](./01-0018-reachability-coherent.md).
Installing any skill.
