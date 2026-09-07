# Shared dev harness: research, principles and bootstrap selection

**Date:** 2026-09-05
**Historical handoff:** current state belongs to the [delivery queue](../tickets/README.md) and owning work. No earlier session record exists in this project.

## Work completed

Compared the dev-skill corpora and loader aliases; investigated Life's mechanism, maintenance and rule-delivery design and implementation; ran seven isolated research probes; developed a draft harness spec and working glossary; captured the pacer idea and corrected its scale model; selected the bootstrap sources; and proposed the first delivery slice after reading the selected ticket skill and its format.

Evidence: [audit and exact file identities](../research/audit-2026-09-05/REPORT.md), [Life research and scope limits](../research/life-harness-findings.md), [probe results](../research/probe-life-results.json). The final source-selection check found all 99 audited M/A/F files unchanged. No live three-host discovery or behavior test has been performed.

## Settled decisions and their owners

- The harness develops through its own tickets, specs, RFCs and loop; `/align` remains entry, reentry and HITL across stages. [Process](../process.md#work-and-documents).
- Substantial inception includes a spec; this harness has a [draft spec](../spec/01-0010-dev-harness-shared-and-local.md). The general spec gate and exact lifecycle states remain unsettled.
- Begin with shared and project-local instructions in one installed skill file; projects propose shared improvements to core and recipients pull accepted revisions. [Owning decisions](../tickets/01-0010-dev-harness-shared-and-local.md#resolutions-and-constraints).
- Autonomy is bounded by established agreements and authorized scope. Clear compliant repairs use repair-and-report; consequential unresolved choices return to `/align`. [Policy](../process.md#autonomy-and-repair).
- Skills are instruction parts of mechanisms; maintenance includes their consumers, checks and records. [Definition](../../.agents/glossary.md).
- `/maintain` owns all tree maintenance, all `/denoise` and `/sync-arch` responsibilities and archiving, with whole-tree or declared narrower scope. [Policy](../process.md#tree-maintenance).
- Mechanisms must support mechanical derivation and repair from inception; missing scripts are maintenance work; history is included without inventing past facts. [Policy](../process.md#mechanical-maintenance).
- Current instructions, work decisions and per-mechanism evidence/evolution have distinct homes. [Ownership](../process.md#current-documents-and-evidence).
- The user requires governing principles, reconstructable load-bearing seams, and observable, deliberately selected Tier 1/Tier 2 delivery; operational definitions remain proposals. [Draft principles and delivery](../spec/01-0010-dev-harness-shared-and-local.md#governing-principles--for-alignment), [glossary](../glossary.md).
- The pacer is a separate [idea document](../pacer.md), not an installed skill. It must distinguish milestone/ticket scale from bounded execution passes and consider project stage and feedback.
- Bootstrap selection is accepted: M baseline, selected F improvements, 20 working commands after maintenance consolidation, `/ticket` and `/plan` names, with project-specific Notion/initiative content excluded here. [Exact selection](../tickets/01-0010-dev-harness-shared-and-local.md#bootstrap-corpus-selection).

## Open work and exact reentry point

**Resume with the proposed first ticket's granularity review:** [Align on harness work in Codex, Cursor and Claude Code](../tickets/01-0010-dev-harness-shared-and-local.md#first-bootstrap-delivery-ticket--proposed-breakdown). It covers the selected `/align` and `/impact`, supporting references, project context and evidence of live delivery in all three hosts. Its HITL decisions are the project/corpus location and minimum observable Tier 1 entry contract.

The user requested session conclusion before answering whether this is the right first slice. Do not treat this proposal as approved. No child file, implementation RFC, rewritten corpus or installed host integration exists. After granularity agreement, mint/register the child under the selected ticket conventions and resolve its owned decisions before dependent planning. Source selection is already accepted and should not be reopened without new evidence.

Other open issues remain in the [parent ticket](../tickets/01-0010-dev-harness-shared-and-local.md#decisions-this-tickets-align-owns), [spec proposals](../spec/01-0010-dev-harness-shared-and-local.md), and [pacer issues](../pacer.md#open-issues): artifact/scale routing, project-stage signals, bounded and repeated passes, issue capture and Tier 1 triggers, detailed lifecycle transitions, queue machinery/strikes, local overrides, maintenance mechanics, update activation and cross-project reconciliation. No additional mechanism was adopted merely because it was discussed.

The working home remains `D:/Dev/AI/.agents`; requested future canonical `D:/Dev/AI/agents` has not been created. Existing skill sources and host configurations remain unchanged. No commit or publication occurred or was authorized.

## Session assessment

The strongest outcome is an evidence-backed source selection and explicit separation of accepted rules from design hypotheses. The audit and isolated probes are sufficient inputs for the next bounded bootstrap decisions; they are not delivery evidence for a working harness.

The main process failure was over-expansion: the assistant repeatedly proposed broad design questions or a milestone when the user wanted an agent-sized pass. The pacer now records that correction. Another error was retaining stale "pending" language after decisions had landed; session conclusion repaired the queue, spec reentry note and pacer progression, and closed the research ticket whose criteria were satisfied.

The practical next improvement is to finish one bounded transition at a time with a named owner, current input state, concrete output and reassessment boundary. Keep design alternatives out of current rule bodies and do not demand repeated approval for an already accepted source choice. Live host discovery, authority-versus-delivery distinctions, and archive completeness remain important verification boundaries.

Handoff validation: checked 120 local links across the 10 current Markdown records; no broken targets or incoming links to session records. Confirmed the completed research ticket exists in its archive location and no longer at its active path.
