# Development process

<temporary until="01-0020 is done" ticket="docs/tickets/01-0020-pacer.md">
This document is a suggestion of sequence, not a rulebook. The sequence and the scoping of work are the [pacer's](pacer.md) concern, and the pacer owns this document once it exists. Each step's rules belong in the step's own skill and move there as the skill is installed. Where the installed skills or the [entry file](../AGENTS.md) differ from what follows, they are right.
</temporary>

The user requested on 2026-09-05 that this harness be developed using its own tickets, RFCs and development loop. Their [loop sketch](../dev-skills.png) is the discussion input; its command names and exact transitions remain under alignment.

## Work and documents

The loop itself, its stages, skills and human checkpoints, the autonomy switches and the `<temporary>` convention are owned by [AGENTS.md](../AGENTS.md), the session entry file every host loads at start. This section holds the detail behind it.

- Substantial new work, including this harness, uses a spec before implementation decomposition. `/spec` develops the brief through `/align`, records agreed scope, behavior, architectural boundaries and testing decisions, then hands off to `/ticket`. Small, bounded work can start directly as a ticket. The spec is a document, not a separately queued work item.
- A ticket owns the intended outcome, acceptance criteria and unresolved decisions. The [queue](tickets/README.md) owns ordering and delivery status.
- `/align` resolves decisions against evidence and records them in the owning ticket. Accepted architecture belongs in `architecture.md`, created when a design is settled.
- An implementation RFC belongs to a ticket, under `docs/rfc/` with the same basename. It follows agreement on the boundaries it implements; a research finding or an unsettled proposal is not an accepted implementation plan.
- Implementation follows the RFC when the work needs one. `/verify` is the
  verification of landed work, not only documentation or shape review. The
  project's check set lives in [Verification](#verification); skills link it,
  they do not inline commands.
- `/maintain` is declared at [`.agents/mechanisms/maintain/`](../.agents/mechanisms/maintain/maintain.md); its rules are its body's, and its mechanical support is under `.agents/scripts/`.
- Sessions preserve the handoff; `/recall` checks maintained documents and current files rather than treating session history as delivery state.

The accepted bootstrap selection uses `/ticket`, `/plan`, `/spec` and `/verify` for the former `/to-tickets`, `/plan-impl`, `/to-spec` and `/review-impl`, and consolidates `/denoise` and `/sync-arch` under `/maintain`.

## Naming

Ticket names, `done/` moves, citation, and the queue table:
[TICKET-FORMAT.md](../.agents/skills/ticket/TICKET-FORMAT.md).

## Autonomy and repair

Autonomy is bounded by the authorized work and established principles, architectural decisions and contracts. New foundational choices and unresolved architectural questions go through `/align`. Project age, successful prior work and the absence of a prohibition do not themselves authorize a change.

**Repair and report** when all of the following hold:

- The governing rule is explicit and unambiguous; cite its source.
- The repair restores compliance within the authorized work and preserves other agreed contracts and constraints.
- The affected behavior and dependencies are understood well enough to justify that assessment.
- The result can be verified against the rule with appropriate checks or direct evidence.

Make the repair, verify it, and report the violated rule, what changed, the verification result and any remaining uncertainty. Record the finding and outcome in the owning work item; do not create a separate ticket for a repair already covered by it. A failed verification remains unfinished work.

**Escalate through `/align`** when the rule is missing, ambiguous or contradictory; the repair requires a new foundational decision, an exception or a change to an agreed contract; consequential impact remains unresolved; or the work exceeds current authorization. Present the concrete discrepancy, affected constraints, recommended resolution and the decision needed. Pause the dependent change; independently authorized work may continue.

Do not rewrite a governing rule, weaken a validator or relax acceptance criteria merely to make a violation disappear. Existing commit, push and other action-specific permissions still apply. Reuse decisions and permissions already supplied within their scope.

Example: restoring a dependency direction explicitly required by the architecture can be repair-and-report. Deciding that two modules should exchange responsibilities changes their boundary and requires alignment.

This section owns the current policy. Its decision record is in the [shared-harness ticket](tickets/01-0010-dev-harness-shared-and-local.md#resolutions-and-constraints). Routing the policy through installed skills and checking its delivery across hosts remain implementation work.

## Verification

`/verify` is the verification of landed work: the ticket's observable criteria, the RFC if any, governing docs, and every check in this project's verification set. Match, leakage and doc-caused weirdness stay in that pass. A failed check remains unfinished work. Discrepancies follow [autonomy and repair](#autonomy-and-repair).

The verification set is this project's typechecker, tests, and any other commands required of landed work. `/implement` and `/verify` link here. They do not inline those commands. `/implement` may run named checks during the work; that run is not `/verify`. `/tdd` still owns red-green.

**This project:** no typechecker. The set is the maintenance scripts' behavioral tests and the mechanism check:

```
uv run --offline --no-project python -m unittest discover -s tests -p "test_*.py"
uv run --offline --no-project python .agents/scripts/mechanisms.py --check
uv run --offline --no-project python .agents/scripts/inject_rules.py --check
```

Discovery reporting success with zero tests is not verification; the run must show a positive count. The mechanism check reports the checks it skipped, and a skip is not a pass; a clean run means nothing was caught, never that the tree obeys. The installer's check fails on a block absent from a target its rules file names, on a block that differs from its source, and on a block nothing owns. Alongside them, `/verify` uses the ticket, RFC (if any), governing docs, and the work.


