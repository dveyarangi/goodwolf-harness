# Development process

<straw-dog until="01-0020 is done" ticket="docs/tickets/01-0020-pacer.md">
This document is a suggestion of sequence, not a rulebook. The sequence and the scoping of work are the [pacer's](pacer.md) concern, and the pacer owns this document once it exists. Each step's rules belong in the step's own skill and move there as the skill is installed. Where the installed skills or the [entry file](../AGENTS.md) differ from what follows, they are right.
</straw-dog>

The user requested on 2026-09-05 that this harness be developed using its own tickets, RFCs and development loop. Their [loop sketch](../dev-skills.png) is the discussion input; its command names and exact transitions remain under alignment.

## Work and documents

The loop itself, its stages, skills and human checkpoints, the autonomy switches and the `<straw-dog>` convention are owned by [AGENTS.md](../AGENTS.md), the session entry file every host loads at start. This section holds the detail behind it.

- Substantial new work, including this harness, uses a spec before implementation decomposition. `/spec` develops the brief through `/align`, records agreed scope, behavior, architectural boundaries and testing decisions, then hands off to `/ticket`. Small, bounded work can start directly as a ticket. The spec is a document, not a separately queued work item.
- A ticket owns the intended outcome, acceptance criteria and unresolved decisions. The [queue](tickets/README.md) owns ordering and delivery status.
- `/align` resolves decisions against evidence and records them in the owning ticket. Accepted architecture belongs in `architecture.md`, created when a design is settled.
- An implementation RFC belongs to a ticket and is named by it, per [the ticket format](../.agents/skills/ticket/TICKET-FORMAT.md#one-basename-per-work-item). It follows agreement on the boundaries it implements; a research finding or an unsettled proposal is not an accepted implementation plan.
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

The policy is the entry file's: the `repair` switch and its four conditions in
[AGENTS.md § Autonomy](../AGENTS.md#autonomy), moved there on 2026-09-20 under
[01-0010.0140](tickets/done/01-0010.0140-core-stands-alone.md) so that core carries what core reads. Its
decision record is in the [shared-harness ticket](tickets/01-0010-dev-harness-shared-and-local.md#resolutions-and-constraints).

## Verification

The definition is [`/verify`'s](../.agents/skills/verify/SKILL.md#the-verification-set), moved
there the same day under the same ticket; this project's four commands sit in the entry file's
local block beside its switches. `/tdd` still owns red-green.


