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
- `/maintain` owns tree maintenance as defined below, including all responsibilities of `/denoise` and `/sync-arch`, and archiving. It is installed, with its mechanical support under `.agents/scripts/`.
- Sessions preserve the handoff; `/recall` checks maintained documents and current files rather than treating session history as delivery state.

The accepted bootstrap selection uses `/ticket`, `/plan`, `/spec` and `/verify` for the former `/to-tickets`, `/plan-impl`, `/to-spec` and `/review-impl`, and consolidates `/denoise` and `/sync-arch` under `/maintain`. `/align`, `/impact`, `/ticket`, `/spec`, `/plan`, `/implement`, `/tdd`, `/improve-comments`, `/verify` and `/maintain` are installed under those names.

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
```

Discovery reporting success with zero tests is not verification; the run must show a positive count. The mechanism check reports the checks it skipped, and a skip is not a pass; a clean run means nothing was caught, never that the tree obeys. Alongside them, `/verify` uses the ticket, RFC (if any), governing docs, and the work.

## Mechanisms and skills

<temporary until="01-0011.0022 is done" ticket="docs/tickets/01-0011.0022-shape-survives-second-mechanism.md">
Maintenance covers the whole mechanism: whether its instructions still express the agreed behavior, its consumers receive and use them, its checks detect the intended failures, and its records remain consistent with their governing rules. Repair follows the autonomy and repair policy above.
</temporary>

## Tree maintenance

`/maintain` owns ensuring that all mechanisms are applied correctly according to their actual governing rules across the maintained tree. This includes the full responsibilities the selected `/denoise` and `/sync-arch` carried: architecture/code consistency in both directions, reconstruction of load-bearing contract shape, document consistency and canonical ownership, prose and inline-comment cleanup, concern disposition, records, indexes, links and archive lifecycle. It also covers instruction delivery, supporting checks and derived work; maintenance is not limited to prose cleanup or recently edited files.

A pass declares its scope: the whole tree, a project, or work associated with a particular RFC. Derive every applicable mechanism and its obligations within that scope, including the consumers and dependencies needed to verify them. A narrower pass uses the same governing rules and reports its coverage; it cannot certify the rest of the tree. Findings beyond the covered scope remain visible with an owner rather than disappearing from the result.

A pass uses one integrated procedure — identify, check and repair, clean up, resolve temporary statements, archive and verify references — with the scope deciding which checks apply. The steps belong to [the skill](../.agents/skills/maintain/SKILL.md); this document owns the policy they follow.

Archive decisions and mechanical archive operations belong to `/maintain`. Before archiving a spec, establish that surviving agreements have maintained homes, its obligations have explicit dispositions, unresolved issues retain active owners, and moves/indexes/references are consistent. Record delivery, transfer, withdrawal and supersession accurately. Current work must not require archived specs to reconstruct its governing contracts; historical investigation and mechanical maintenance may still use them.

Repair and verification follow the policies in this document. Derive and fix mechanically where possible, write missing maintenance scripts, and keep incomplete checks or repairs visible. Ambiguities that require a new decision return to `/align`.

## Mechanical maintenance

Mechanisms must be designed from inception to support mechanical derivation, checking and repair. Their identities, governing sources, dependencies and record contracts must be explicit enough for tooling to enumerate affected artifacts and derive required changes. Derive inventories, indexes and other computable views from their owning sources rather than maintaining duplicate facts by hand. The concrete representation and tooling remain implementation design.

Anything that can be maintained mechanically must be maintained mechanically. The maintainer writes or extends missing maintenance scripts as part of the repair; a missing script is work to do, not a reason to leave a mechanical repair outstanding. This includes historical records, which have no blanket exemption.

When a governing skill or rule changes, derive its affected consumers and artifacts, repair governing surfaces before their derived work, and verify the affected scope. Installing updated instructions alone does not establish that their derived work is current. Keep unresolved effects visible; mark only what has actually been checked and repaired or established as unaffected. Semantic decisions that cannot be derived from established rules follow `/align` under the repair policy.

Mechanical history repairs preserve the facts and decisions being recorded, with traceable transformations. They must not invent unknown past facts or imply that a newly introduced requirement was satisfied at the time. Current instructions remain separate from historical decision and evidence records even when both are mechanically maintained.

## Current documents and evidence

Core documents and skills state current behavior, instructions and compact examples, with references to their sources. Tickets and RFCs retain deliberation and decisions about their work.

Each mechanism has one evidence/evolution record, created when there is material to preserve. It holds observations, failed approaches and lessons across changes, linking to the deciding tickets/RFCs without duplicating their arguments. Following a skill does not require reading its history; maintaining or challenging the mechanism follows the relevant evidence references.

This evidence/evolution record is distinct from the work and operational records produced under the mechanism's instructions.

