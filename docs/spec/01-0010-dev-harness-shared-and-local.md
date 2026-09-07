# A shared dev harness improves without losing project conventions

**Status:** Draft for alignment — not an approved implementation specification.
**Owning work:** [Shared-harness ticket](../tickets/01-0010-dev-harness-shared-and-local.md).

This draft gathers agreed requirements and exposes unresolved behavior. The ticket owns deliberation and decisions; the [process](../process.md) owns the current working rules. Recommendations below are labelled separately from agreed requirements.

## Problem Statement

Developers and agents use divergent copies of the same development skills across projects. A useful improvement in one copy does not reliably reach the others. Whole-folder copying cannot distinguish shared improvements from project conventions, and identical instruction files do not establish equivalent behavior in Claude Code, Codex and Cursor.

The [comparison](../../audit-2026-09-05/REPORT.md) also found dependencies outside skill bodies, local exceptions that conflict with shared instructions, and host-specific automation. The harness needs to maintain both its instructions and the work derived from them.

## Solution

Maintain one accepted shared dev harness. Projects can contribute shared improvements to core and pull accepted revisions while preserving their project-local content. Begin with shared and local instructions in one installed skill file. Treat skills as instruction parts of mechanisms whose consumers, checks and records are maintained together.

Use the harness's own development loop to evolve it. `/align` remains the entry, reentry and human-decision procedure at any stage. This effort develops a spec before implementation decomposition. This harness is itself developed that way: `/spec` develops this spec, then `/ticket` slices the remaining work, including the delivery-ring skills, from it.

## User Stories

1. As a project maintainer, I want to identify the accepted shared revision and local divergence, so I can understand what an update would change.
2. As an agent improving a project, I want to propose a shared skill improvement to core, so other projects can benefit after acceptance.
3. As a recipient maintainer, I want accepted improvements without losing local instructions, so updating the method preserves project behavior.
4. As a maintainer, I want conflicting and unknown states exposed, so an updater does not silently choose which work to discard.
5. As a developer using any supported framework, I want the intended skills and required supporting behavior available, so changing hosts does not silently change the method.
6. As a project owner, I want autonomy within established constraints and escalation for unresolved consequential choices, so control changes with the clarity of the project's agreements.
7. As a mechanism maintainer, I want affected work to be derivable and mechanically repairable, including historical records, so instruction changes do not leave invisible maintenance debt.
8. As an agent following a skill, I want current instructions separated from evolution records, so I can act on current rules and follow evidence when maintaining or challenging them.
9. As a developer, I want governing principles and sufficiently specified load-bearing seams, so I can implement the harness or a consuming system without inventing missing architectural decisions.
10. As a project owner, I want the relevant rule slices deliberately selected and their delivery and application observable, so expected rules do not silently disappear from the development process.
11. As a harness owner, I want work on this harness to complete the delivery ring — `/plan`, `/implement`, `/verify`, `/maintain` — and move a ticket whose criteria are met, including `/verify`, to `done/`, so finished work is not left in the active queue.

## Governing principles — for alignment

The user requires governing principles to apply both to harness development and to software developed using it. The qualities below are requested; their operational definitions are proposed for alignment. The [glossary](../../.agents/glossary.md) owns terminology, including the proposed definition of a load-bearing seam.

| Principle | Proposed obligation and evidence |
|---|---|
| Stability | Preserve established contracts through change, or explicitly decide and verify their migration. Validate existing consumers as well as the new behavior. |
| Predictability | Equivalent declared inputs, revisions and decisions yield behavior within the same specified contract; judgment and uncertainty are explicit. Agent prose need not be byte-identical. |
| Observability | Distinguish intended, selected, emitted, delivered, retrieved, applied and verified instructions or outcomes using the evidence actually available. Missing observation remains unknown, not success. |
| Extensibility | Add a supported variation through a named boundary with stated constraints; validate existing consumers. Do not require a general extension framework before distinct concrete uses justify it. |
| Maintainability | Derive dependencies, inventories and repairs mechanically where possible; changes include their affected consumers and derived work, including history. |
| Reconciliability | Retain origin and revision evidence sufficient to explain divergent states and resolve them without silently losing either side's work. |
| Architectural determinacy | Specify both ends of load-bearing seams so an implementer need not invent a further architectural decision to reconstruct their behavior. Equivalent implementation-local choices remain available. |

Additional candidates, not yet adopted: recoverability after interruption or partial change; proportionality of machinery and context to demonstrated need; and one authoritative owner per fact with derivation instead of duplicated maintenance. Their adoption should be justified by concrete failure cases rather than expanding a generic checklist.

### Load-bearing seams — proposed test

Identify the producer, consumer and the responsibility boundary. Then ask whether a change that is locally valid at one end can violate promised behavior, authority, data interpretation or integrity, compatibility, or recovery at the other end. If so, the seam is load-bearing; an unresolved answer is an architectural issue, not permission to omit its contract.

For such a seam, the architecture must settle the applicable inputs and outputs, meaning, invariants, ownership and authority, transitions and timing, failure and recovery behavior, compatibility, and observable proof. Include only dimensions that matter to that seam. An independent implementer should be able to reconstruct both ends without relying on conversation history or deciding a missing contract.

Concrete harness examples: core acceptance to recipient update; local instruction composition; hook output to agent context; governing skill changes to record maintenance. An internal helper that can be replaced without changing any of these guarantees does not become load-bearing merely because another function calls it.

### Rule selection and delivery

The user's intended delivery model places strict/meta rules and skill descriptions in Tier 1, with detailed instructions routed into Tier 2 when needed. Occasion-specific generated context that needs Tier 1 is supplied through hooks. This is the target behavior; equivalent hook support and actual context visibility across hosts remain to be established.

The applicable rule set and the current slices must be deliberately selected and observable. Proposed selection contract: identify each slice's source/revision, authority, applicability, trigger, intended recipient and lifetime; account for required slices that were excluded, missed or could not be delivered. Context compression must preserve required obligations. Hook output alone does not prove delivery, and delivery alone does not prove application.

Authority and delivery are separate: putting text in Tier 1 does not grant it new authority. Occasion-specific generated data must remain distinguishable from governing instructions. If a host cannot expose a required observation, report that limitation and the resulting verification gap; do not declare equivalent rule application from filesystem checks.

## Implementation Decisions

### Harness loop on itself — agreed 2026-09-06

Spec-first and completing the delivery ring are one path. `/spec` develops this spec in place. `/ticket` then slices remaining work from it, including `/plan`, `/implement`, `/verify` and `/maintain`. Each slice is planned, implemented, verified, and maintained; a ticket whose criteria are met, including `/verify`, moves to `done/` as part of that close. `/plan` is planned by reading `/plan`. Ring-skill tickets are not minted before this spec says they are the work.

Until `/maintain` is installed, the `done/` move follows the ticket format, and only after `/verify` has been run on that ticket.

### Spec lifecycle and issue routing — proposals under alignment

The user directs that enduring spec content land in architecture and the spec eventually become history. `/maintain` ownership of tree maintenance, all `/sync-arch` and `/denoise` responsibilities, and archiving is now agreed in [the process](../process.md#tree-maintenance). The remaining lifecycle states and routing allocation below are proposals, not installed skill behavior.

**Spec lifecycle:** draft → accepted → in delivery → reconciled → archived. Acceptance supplies governing decisions before dependent implementation planning; it does not claim those decisions are already implemented. Maintained architecture must distinguish agreed target from current behavior. Enduring capability requirements, terminology and contracts belong in their appropriate maintained homes rather than every detail being copied into architecture.

As decisions land, update those homes and let the spec reference them. At reconciliation, account for every obligation as delivered with evidence, explicitly withdrawn/superseded, or transferred to a named continuing owner under an agreed scope change. Child tickets closing does not establish this by itself. Before archival, verify that no enduring contract is owned only by the spec, unresolved issues have active owners, and moves/indexes/references are consistent. Preserve the archive's disposition; transferred or cancelled scope is not delivered scope.

Current development must be reconstructable without fetching archived specs. Historical investigation and mechanical history repair remain valid consumers. Archive movement, reference repair and structural coverage checks should be scripted; semantic completeness must not be inferred solely from a successful move or all boxes being checked.

**Agreed maintenance ownership:** [Tree maintenance](../process.md#tree-maintenance) governs whole-tree and narrower project/RFC passes, complete mechanism coverage in scope, repair and archiving. Remaining implementation design includes how supporting routines are exposed and how coverage is derived and demonstrated. Source gaps: current `/denoise` treats RFCs as historical without consistently separating active plans, and current Life `/maintain` exempts archives from scripted repair; neither exception is adopted here.

**Capture and routing:** requests such as "open an issue", "record this problem" and "keep this for later" first preserve the issue and its relevant context. Reuse an existing owner when identifiable; a genuinely unowned issue needs a visible intake home, whose representation remains open. Do not fabricate a spec, implementation RFC or full decomposition simply to record an issue. Capture alone does not authorize further work.

**Proposed division of responsibilities:** `/align` handles capture/routing and unresolved decisions; `/impact` supplies consequence and contract analysis with a recommended continuation; `/ticket` owns decomposition into delivery work; `/plan` owns its implementation plan. `/impact` can challenge a split without becoming a second authoritative decomposition writer. Selecting what proceeds now follows authorization, dependencies and the autonomy policy; a scale assessment does not grant permission.

At any downstream stage, a newly exposed missing agreement returns to its owning spec or architecture decision; an overlarge ticket returns to decomposition. Preserve the originating issue and valid work, mark the dependent work as waiting, and resume it after resolution. The same stage may continue if the finding only concerns an implementation-local choice.

A HITL ticket may capture work before its shape is understood; investigation can reveal a spec with multiple delivery tickets. Preserve the originating issue and decision history when its work changes shape. HITL, decomposition maturity and artifact role must not be treated as the same state. The exact ticket-to-spec transition and general spec gate remain open; architecture change alone is a candidate to assess with `/impact`, not an adopted automatic trigger. The [pacer idea](../pacer.md) owns the proposed unit-of-work definition and live step-size hypothesis.

Natural-language capture triggers belong in the chosen entry skill's Tier 1 description and routing contract; detailed selection lives in Tier 2. Verify discovery and representative paraphrases on each supported host. A description containing the right phrase is not proof that the host delivered it or that an agent routed the request correctly. No new `/step` or `/decompose` skill is selected: additional names require a distinct responsibility and concrete examples that existing boundaries cannot serve.

Agreed boundaries are in the [owning ticket](../tickets/01-0010-dev-harness-shared-and-local.md#resolutions-and-constraints): canonical acceptance and recipient pulls; inline local instructions initially; mechanisms covering instructions, consumers, checks and records; mechanical maintenance from inception; and dynamic autonomy with repair-and-report.

No module layout, storage schema, transport or implementation RFC is approved. Cross-project comparison, instruction delivery and downstream verification are separate responsibilities; success in one must not be reported as proof of another. The concrete representation of these responsibilities remains to be designed.

## Testing Decisions

Verification must demonstrate observable behavior. The following are draft acceptance scenarios to refine through alignment, not a selected test implementation:

| Scenario | Required observation or unresolved contract |
|---|---|
| Project A proposes an improvement; core accepts; project B pulls | B receives the accepted shared change with provenance and preserved local content. |
| Core and a project both change shared content | Both changes remain available for reconciliation; which reconciliations may be automatic remains open. |
| A shared requirement conflicts with a local exception | **Deferred open issue:** distinguish a supported variation from an incompatible exception and define the update response after governing principles are settled. |
| A renamed skill has callers and automation | Updated invocation and supporting behavior work together; the planning hook is a concrete dependency to cover. |
| A governing contract changes | Affected current and historical artifacts are enumerated, repaired where mechanical, and verified; unknown historical facts are not invented. |
| A file is installed but the host does not discover or use it | Delivery remains unverified or failed, despite installation freshness. |
| An update is interrupted or files change during application | **Unresolved:** observable partial state, recovery and when the installed revision may advance. |
| An implementer reconstructs a load-bearing seam from architecture | Its contract can be implemented without an undocumented architectural choice; producer and consumer agree under relevant failure cases as well as success. |
| A required rule slice is omitted, stale or emitted but not delivered | The relevant observation identifies the discrepancy or explicitly leaves delivery unknown; the run is not certified compliant solely from a successful hook or existing file. |
| Maintenance is requested for an RFC rather than the whole tree | Every mechanism applicable to the declared scope is assessed under its actual rules, relevant dependencies are accounted for, and the report does not certify unchecked parts of the tree. |
| A captured HITL ticket proves to require a spec and several tickets | The original issue and decisions remain traceable through the change of shape; scope transfer is not reported as completed delivery. Exact transition mechanics remain open. |
| A ticket's acceptance criteria are all checked, including `/verify` | The ticket is in `docs/tickets/done/` with citations repaired. `done/` without that run is a failed close. |

Prior evidence includes the audit and [isolated Life probes](../research/life-harness-findings.md). Those probes expose useful failure cases; they do not verify a dev-harness implementation. The selected seams, checks and live-host verification procedure remain to be agreed.

## Out of Scope

Wholesale adoption of Life's operating policies, unrelated changes to consuming products, and general queue machinery without a demonstrated need in this harness. Queue requirements may enter scope when concrete cases justify them.

The [queue](../tickets/README.md) owns the current step. Bootstrap suite membership and source variants are accepted in the owning ticket. Broader open design includes operational principle definitions, load-bearing seams, observable rule delivery, local exceptions, detailed ownership, proposal and pull behavior, activation in sessions, maintenance representation and canonical layout. The glossary distinguishes unresolved issues from the documents that hold or resolve them. This draft does not resolve them by implication.

## Delivery-ring breakdown — 2026-09-06

Parent of this `/ticket` pass: the agreed loop-completion requirement (story 11 and [Harness loop on itself](#harness-loop-on-itself--agreed-2026-09-06)), not the unaccepted rest of this draft. [01-0020](../tickets/01-0020-pacer.md) is a different contract. **Minted 2026-09-06.**

### Impact

**Main blast radius.** Four children of [01-0010](../tickets/01-0010-dev-harness-shared-and-local.md). `/verify` is installed when there is landed work to review; it does not wait on `/implement`. A ticket is not moved to `done/` until `/verify` has been run. Catalog, `AGENTS.md` installed-list, and renamed callers change per slice. `/plan` must call `/impact`. `/maintain` enumerates `<temporary>` blocks.

**Hidden edges.** `/maintain` has no source file (denoise + sync-arch plus the `<temporary>` enumerator); composition is still open on 0010. `/implement` and `/verify` still name `/tdd`, `/improve-comments`, `/review-impl`, `/sync-arch`; adapt per slice. The rest of this draft (principles, distribution, local overrides) is not accepted and is not sliced here.

**Leave alone.** [01-0020](../tickets/01-0020-pacer.md), `/edge`, `/recall`, the remaining selected corpus, spec acceptance.

**Recommendation.** Proceed, narrowed to the four ring skills.

1. **Title:** Install `/plan`.
   **Interaction:** HITL.
   **Depends on:** [01-0010.0035](../tickets/done/01-0010.0035-install-spec.md) (the spec and `/spec`).
   **Parent scope covered:** story 11; selection `/plan`; `/plan` calls `/impact`.
   **Basename:** `01-0010.0040-install-plan.md`.

2. **Title:** Install `/implement`.
   **Interaction:** HITL.
   **Depends on:** slice 1 (an RFC from `/plan`'s first use).
   **Parent scope covered:** story 11; selection `/implement`.
   **Basename:** `01-0010.0050-install-implement.md`.

3. **Title:** Install `/verify`.
   **Interaction:** HITL.
   **Depends on:** landed work to review ([01-0010.0035](../tickets/done/01-0010.0035-install-spec.md) or an earlier landed slice); not slice 2.
   **Parent scope covered:** story 11; selection `/verify`; repair-and-report.
   **Basename:** `01-0010.0060-install-verify.md`.

4. **Title:** Install `/maintain`.
   **Interaction:** HITL — decision-bearing: compose denoise + sync-arch and the `<temporary>` enumerator; first use is a paired close, not a whole-tree sync.
   **Depends on:** slice 3.
   **Parent scope covered:** stories 7 and 11; selection `denoise`/`sync-arch`; paired ticket+RFC close (RFC → `docs/rfc/done/`).
   **Basename:** `01-0010.0070-install-maintain.md`.
