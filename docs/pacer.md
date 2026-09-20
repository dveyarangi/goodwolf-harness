# Pacer

**Status:** Idea under alignment; no skill or runtime mechanism adopted.

## Need

The project owner and agent need to interpret requests such as "let's do the next thing" against the current work, its uncertainty and authorization. The artifact currently holding an issue may not represent its eventual scope: an undecomposed HITL ticket can reveal a spec and multiple delivery tickets, and an RFC can expose a missing upstream agreement.

**2026-09-06, user:** resume state is the pacer's concern: what a session writes down at `/conclude` so the next `/recall` can resume the delivery ring at the stage it stopped, rather than waking into `/align` by rule. Until the pacer exists the wake goes to `/align` as drawn.

The pacer must represent work at multiple scales and select execution steps small enough for an agent to handle controllably. It must explain when evidence requires expansion, decomposition, a repeated pass, a return to an earlier stage, or a human decision. Preserve the original issue, valid decisions and completed work through such changes.

## Core rules — under alignment

The pacer's core rules are Tier 1: they say what the agent does after `/recall` and what one turn's reply is scoped to. A **turn** is one agent reply, from the user's message to the reply's end. Resolved rules are recorded here until the pacer is installed and carries them.

- ~~What is a turn scoped to?~~ **2026-09-06, user: a turn holds at most one execution step.** A step may span turns; a turn never spans steps. The reply ends at the step's reassessment boundary. Chaining steps inside one turn up to the next human checkpoint is the intended later shape, to arrive as a stated allowance when principles settle, not as the default. Evidence: the first observed wake, whose reply was about to run `/recall` into `/align` by rule. **Same day, user: a step is the execution of a single skill**; the glossary's earlier "or a smaller stage within it" is dropped.
- ~~When the user's message names no step, how is the step chosen?~~ **2026-09-06, user: a session that starts with "what's next" starts with `/recall`, which finds the next probable move; if nothing is active, `/align` on what's next.** The precedence recall uses, accepted as "ok for now, a bit muddy": landed-but-unverified work first; then a decision parked at `/align` on the active ticket; then the active ticket's current stage, continued; then, nothing active, `/align` on what comes next, which is the `next-cycle` checkpoint. A tie at one rank is presented, not resolved. **2026-09-20, user: every session wake starts with `/recall`, whatever the first message says** — no carve-out for a message that names a skill or a task. Landed in [AGENTS.md](../AGENTS.md) at v9, beside the announce line; the first core rule to leave this page. Occasion: [rule failure 4](rule-failures.md#4-the-wake-rule-sat-in-a-diagram-and-a-greeting-was-answered-with-a-greeting--2026-09-20). How it sits with *one turn, one step* when the first message names a task is the chaining question above, still open.
- **2026-09-06, user: bootstrap the pacer on the `<temporary>` blocks.** Each block's `until` condition is bound to a real ticket, so the conditions become the queue the pacer paces, and "what's next" can be answered from them for the current work here.

<straw-dog until="01-0020 is done" ticket="docs/tickets/01-0020-pacer.md">
Until the pacer is installed, the wake runs `/recall` and stops at the fork it finds; the pacer then reads state, resumes the ring at the next step, and stops only for a HITL escalation.
</straw-dog>

## Scales and steps — revised hypothesis

The previous definition was scale-blind: a bounded, verifiable outcome can still be a milestone. Work scale, understanding of its shape, and the next execution step must be represented separately. The following are candidate scales, not a required document hierarchy:

| Scale | What is controlled | Typical representation |
|---|---|---|
| Direction / milestone / capability | Intended change and governing agreements | A spec, roadmap or parent ticket, as appropriate |
| Delivery work | A verifiable slice, dependencies and readiness | A ticket or subticket |
| Execution step | One bounded operation or pass and its feedback | A skill invocation or a bounded stage within it, recorded on the existing work |

**Unit of work — revised proposal:** work with an explicit scale, owner, outcome and completion evidence. Saying "unit" without naming its scale is insufficient for pacing.

**Execution step — proposal:** a bounded pass over the selected work with known input state, one immediate purpose, expected output/evidence and a reassessment boundary. It need not finish a ticket or independently deliver a feature. A skill invocation is a candidate step, not a guarantee of boundedness: a broad `/implement` or `/maintain` may need a smaller declared stage or scope.

The shape can move from requested → explored/expanded → decomposed at any relevant scale. Exploration can reveal missing siblings, consumers or contracts; decomposition can force a return upstream. HITL describes needed human involvement, not size or whether exploration is complete.

## Proposed assessment

For a "next thing" request, identify the containing outcome and its scale, the selected work's current state, the last pass and its evidence, applicable constraints and authorization, and the next bounded operation. State its expected result and when to reassess. "Deliver the milestone" is not an execution-step recommendation.

A representative sequence supplied by the user is: pick ticket → plan ticket → split ticket or review plan → review plan → implement → verify → verify → verify → maintain → pick ticket. These are possible bounded passes, with branching and feedback, not a mandatory pass count or a single uninterrupted unit. Repeated planning validates the same RFC; repeated verification needs an identified scope or question and evidence of what that pass established.

At each boundary, choose continue, repeat, decompose, return upstream, switch work or request a human decision from the resulting state. Reassessment does not require a human approval after every skill. Prior authorization continues within its scope; an unresolved consequential choice remains a HITL boundary.

If the outcome is unclear, align or explore; if its shape is insufficiently understood, expand it before decomposition; if the plan cannot be bounded coherently, split the work. Exact allocation among a pacer and existing skills remains open.

## Project stage and evidence

The user's direction is that pacing consider project stage and observe changes in commits, architecture and work records. Proposed inputs include established versus provisional contracts, recent relevant changes, active work and dependencies, review/verification results, unresolved issues and existing authorization. Commit count or project age alone does not establish maturity or permission.

Different parts of one project can have different maturity. A new subsystem in an established project can require foundational alignment, while an early project can contain a fully understood repair. Some artifact levels may be omitted when they add no necessary agreement or control; this does not remove the need for bounded execution steps and observable feedback. Which omissions are justified, and how stage is derived, remain design questions.

## Live case: use the corpus while developing it

**User purpose:** bring the whole development skill corpus into use on this project in Codex, Cursor and Claude Code now, so its design can be exercised live.

**Containing milestone:** this project can run one coherent working revision of the full selected dev corpus in all three hosts. The user rejected treating this as the next agent-sized step.

**Scope:** assemble a reviewable corpus from the audited sources; reconcile the decisions required to operate it; apply agreed command names and maintenance ownership; include needed appendices and scripts; provide local host entry points; verify discovery and representative behavior. This is a working installation for this project, not acceptance of every draft harness principle.

**Exit evidence:** the exact corpus and its source revisions are identifiable; required references and dependencies resolve; each host discovers the intended skills; explicit and natural-language requests select and exercise representative skills under the agreed rules; observed gaps are reported. Unverified host behavior remains unfinished verification, not a completed three-host installation.

**Outside this unit:** implementing the general project-A-to-core-to-project-B distributor, moving unrelated projects, adopting a pacer runtime, or settling every open queue/override/principle question. A question that actually blocks the working installation must still be resolved rather than hidden by calling the installation provisional.

**Revised hypothesis for the next execution step:** one `/ticket` decomposition pass over this bootstrap milestone, using the existing audit and decisions. Produce a proposed set of bounded delivery tickets and identify the first ready ticket or its precise blocking decision. Reassess that output before moving to a `/plan` pass; do not combine corpus selection, rewriting, installation and three-host verification into this step.

**Live progression, 2026-09-05:** a prerequisite source-selection `/align` pass was taken first on the existing HITL ticket and its [selection was accepted](tickets/01-0010-dev-harness-shared-and-local.md#bootstrap-corpus-selection). The following `/ticket` pass read the selected skill and format, assessed impact and produced [one proposed slice](tickets/01-0010-dev-harness-shared-and-local.md#first-bootstrap-delivery-ticket--proposed-breakdown): live alignment and impact assessment in all three hosts. Its granularity awaits user review; no child ticket or RFC has been created. The [queue](tickets/README.md) owns current delivery state.

**Step evidence:** the proposed slices each have observable outcomes, dependencies and unresolved agreements; together they cover the bootstrap milestone without pretending unresolved design is settled. If the milestone cannot yet be sliced meaningfully, identify the specific missing agreement and return to `/align` rather than producing arbitrary implementation tasks.

**Correction recorded:** the earlier hypothesis mistook milestone completeness for controllable step size. An intermediate planning or decomposition result can be a successful execution step even though the corpus is not yet usable. The milestone remains unfinished until its own exit evidence exists.

## Open issues

- Whether one pacer or existing skills own changes of scope and progression; possible names such as `/step` and `/decompose` remain suggestions.
- How to distinguish changes of scale from pace: what agreement is needed versus what proceeds now.
- Which scales need explicit representation and which artifact levels can be omitted at a given project stage.
- How to bound a skill pass, decide whether another pass adds needed evidence, and observe stage changes without imposing fixed approval or repetition counts.
- The general spec gate. Architecture change alone is a hypothesis to test through `/impact`, not an adopted automatic trigger.
- How a ticket gives rise to a spec and delivery tickets without losing identity, ownership or history.
- How natural-language "next step" requests reach the assessment through Tier 1 and how that routing is observed.

## Context

[Harness spec](spec/01-0010-dev-harness-shared-and-local.md), [glossary](glossary.md), [development process](process.md), and [owning harness work](tickets/01-0010-dev-harness-shared-and-local.md).
