# A shared dev harness improves without losing project conventions

**Status:** In progress
**Type:** HITL
**Outcome:** Projects share a canonical development method, contribute improvements to it, and receive accepted changes mechanically while preserving project-specific behavior across Claude Code, Codex and Cursor.

## What to build

Consolidate the existing dev skill family into the requested canonical home, after alignment on the comparison findings. Establish how improvements found in a consuming project are proposed to core, accepted there, and received by other projects. Develop and maintain the harness using its own loop.

## Evidence

- [Harness spec — draft](../spec/01-0010-dev-harness-shared-and-local.md): agreed requirements and unresolved acceptance scenarios, under alignment before implementation decomposition.
- [Initial comparison](../../audit-2026-09-05/REPORT.md): independent physical copies, local loader aliases, divergent bodies, appendices and script dependencies.
- [Life investigation](done/01-0010.0010-life-informs-dev-harness.md): completed research on rule delivery, mechanisms, maintenance and their applicability to the dev harness.

## Resolutions and constraints

- **2026-09-05, user:** this project should use tickets, RFCs and the development loop it provides to others.
- **2026-09-05, user preference:** keep shared and project-local instruction content in one skill file initially. Motivation: extra instruction files create delivery assumptions that need instruction and testing themselves. Treat this as the starting direction; any contrary recommendation needs concrete evidence.
- **2026-09-05, user:** investigate Life thoroughly, especially rule tiers, mechanisms and maintenance, for a cleaner dev-harness structure. The earlier proposal to exclude Life from design input is superseded. This does not approve importing all Life policies or implementation.
- **2026-09-05, user:** agrees overall with project-originated shared improvements being proposed to core and recipients pulling accepted changes. Detailed update policy remains open. Requests smaller, sequential alignment on the development loop, specs, mechanisms, document separation and queue machinery before further design adoption.
- **2026-09-05, user:** accepts a spec for substantial work, including this harness, with the clarification that `/align` remains the common entry/reentry and human-decision procedure across the entire loop: spec inception, resuming any stage and HITL escalations. It is not specialized to specs. The user identifies ticket splitting, commits and moving to the next loop cycle as existing human checkpoints whose treatment needs alignment.
- **2026-09-05, user:** autonomy is dynamic. Early work needs human control over setup, core code shapes, modules, approach and governing principles. As those principles become established, more work can proceed autonomously within them. Gaps, inconsistencies, violations and changes that do not fit architectural constraints should trigger HITL, potentially through `/impact`. This supersedes the assistant's proposed fixed one-ticket/one-cycle authorization default; the exact escalation threshold remains to be aligned.
- **2026-09-05, user:** accepts repair-and-report for clear repairs within authorized work that restore an explicit architectural rule while preserving agreed contracts. Requests a well-defined policy. The current rule, reporting requirements and escalation conditions are recorded once in [the process](../process.md#autonomy-and-repair); architectural ambiguity and changes to principles still require `/align`.
- **2026-09-05, user:** agrees that a skill is the instruction part of a mechanism, with maintenance covering the whole mechanism, including consumers, checks and records. Recorded in [the process](../process.md#mechanisms-and-skills). This adopts the concept, not Life's implementation wholesale.
- **2026-09-05, user:** adopts one evidence/evolution record per mechanism, created when needed, with current behavior in core docs/skills and change decisions retained in their tickets/RFCs. Recorded in [the process](../process.md#current-documents-and-evidence). Also directs attention to Life's existing `/mechanism` and `/maintain` rules for derived work becoming stale after its governing skill changes; this is part of the design, not merely prose cleanup.
- **2026-09-05, user:** anything that can be done mechanically should be fixed mechanically, including history. Maintainers can write maintenance scripts, and mechanisms must encourage mechanical derivation and fixes from inception. This supersedes the assistant's proposed blanket exemption for frozen historical records and does not adopt Life's archive exemption. The current rule is in [mechanical maintenance](../process.md#mechanical-maintenance).
- **2026-09-05, user:** spec first; review the existing skills before proceeding. This reaffirms the earlier spec decision and makes spec development the next step, ahead of further queue design. Source review: Meteoscape and Forecast Collector `/to-spec` explicitly cover substantial inception before ticket decomposition and do not queue the spec itself; `/to-tickets` also accepts bounded discussed work without a spec; `/plan-impl` requires an owning ticket for an RFC. The current workspace's older `/to-tickets` assumes a spec, while its `/to-spec` has conflicting output paths. The existing research/alignment tickets remain valid; implementation decomposition follows the harness spec.
- **2026-09-05, user:** accepted the first bootstrap slice as proposed and decided the root: the harness is the git repository `D:\Dev\AI\agents`, with the installed corpus under `.agents/skills`. `/align` and `/impact` are installed from Meteoscape with the accepted deltas; nothing else is installed or renamed yet.

## Decisions this ticket's align owns

- Spec lifecycle: enduring decisions move to maintained governing documents, specs eventually become history. ~~Who owns maintenance and archiving?~~ **2026-09-05, user: `/maintain` owns all tree maintenance, all `/denoise` and `/sync-arch` responsibilities, and archiving.** It checks all mechanisms against their actual rules and can run at whole-tree, project or RFC scope. Current policy: [tree maintenance](../process.md#tree-maintenance). Exact lifecycle state and implementation design remain open.
- Issue capture, routing, decomposition and pace: define Tier 1 natural-language triggers, an owner for initially unowned issues, and feedback to earlier stages. The user's `/step` and `/decompose` examples are alternatives to assess, not selected new skills. **2026-09-06, user:** the loop's sequence and the scoping of work are the pacer's concern; [`docs/process.md`](../process.md) is marked preliminary and the pacer is expected to own it; each step's rules move into the step's skill as it is installed. The pacer's core rules are Tier 1: they say what the agent does after `/recall` and what one turn's reply is scoped to. Their content is under alignment in [pacer.md](../pacer.md).
- Governing principles for the harness and its use in software development; operational definitions and a robust load-bearing-seam test are now the alignment priority. [Draft principles](../spec/01-0010-dev-harness-shared-and-local.md#governing-principles--for-alignment).
- Observable selection and delivery of rule slices: the user directs Tier 1 strict/meta rules and skill descriptions, Tier 2 routed detail, and occasion-specific generated context supplied by hooks. Cross-host delivery and evidence contracts remain to be defined.
- ~~Bootstrap suite membership and source variants.~~ **2026-09-05, user: accepted the [bootstrap source selection](#bootstrap-corpus-selection).** Exact instruction adaptations and installation remain to be planned.
- Local exceptions, local appendices, and the precise ownership boundary within a skill file. **Deferred open issue at the user's request:** whether approved local overrides are allowed or variations must first be supported by core; do not incept that mechanism before its principles are settled.
- Detailed proposal/acceptance mechanics for project-originated shared improvements; the overall direction is agreed.
- When recipient pulls run automatically and when a change becomes active in a session; recipient pull is the agreed overall direction.
- Evidence required to claim each framework discovers and uses the intended instructions.
- Which mechanisms and maintenance structure earn a place in this harness.
- ~~Final canonical filesystem layout and relocation of these working records.~~ **2026-09-05, user: the harness lives at `D:\Dev\AI\agents`, a git repository. The working records moved there with the tree; the installed corpus takes the recipient layout `.agents/skills` with `.claude/skills` and `.cursor/skills` links; the July corpus is evidence under `legacy/skills`.**

## Bootstrap corpus selection

**Status:** Accepted by the user, 2026-09-05. This completes the source-selection `/align` pass on this ticket. It does not complete the bootstrap milestone or approve an unwritten implementation RFC.

**Evidence rechecked 2026-09-05:** all 99 audited files across M, A and F still match the audit's SHA-256 values. Source repository heads observed: M `6320d3c805dffe63d7bccd86d5874c624a78de38`, F `dd847b5f1720c36d695d287f8a67630f09bbfa20`, A `810edb2692ba59672d9e4ebacd7f5504648ffed0`. The [inventory](../../audit-2026-09-05/inventory.json) owns exact per-file identities. A has an unrelated untracked script document; it is not part of this selection.

**Accepted selection:** use Meteoscape (M) as the base for the full audited development suite. Take the specific Forecast Collector (F) improvements below. Keep DriftSense's (A) initiative and Notion integration out of this project's bootstrap; their source files remain intact for later project integration. The older corpus in this workspace is evidence, not the selected source. Life contributes maintenance design already discussed, not a wholesale imported corpus.

M = `D:/Dev/AI/meteoscape/.agents/skills`; F = `D:/Dev/DriftSense/workspace/forecast_collector/.agents/skills`; A = `D:/Dev/DriftSense/workspace/agents/skills`. "Core" below excludes source-project local content. The rows select source material and required adaptation boundaries; open implementation questions remain open where stated.

| Source skill | Working command | Selected source and disposition |
|---|---|---|
| `advise` | `/advise` | M. Retain hidden-edge analysis and separate questionable/missing prompts; F's shorter wording adds no demonstrated capability. |
| `align` | `/align` | M. Retain its existing format shelf rather than adopting A's structural extraction now. Reconcile current policy and document locations; keep capture/pacer routing proposals distinct from adopted rules. |
| `celebrate` | `/celebrate` | M; shared content equivalent. Retain the capability without making celebration a completion requirement. |
| `commit` | `/commit` | M core; equivalent to A/F. Preserve explicit action permissions. Supply this project's real checks locally; do not copy another project's test or release commands. |
| `conclude` | `/conclude` | M. Retain session/handoff behavior; route archive ownership to `/maintain` under the agreed policy. |
| `denoise` | `/maintain` | M responsibilities absorbed in the new maintenance skill, as agreed. Its archive exclusions and destructive evolution cleanup must be reconciled with history repair and retained evidence. |
| `dream` | `/dream` | M; equivalent to A. Retain for deliberate use. Its daily scheduling trigger is a source policy to review, not an authorization to create a schedule. |
| `edge` | `/edge` | M plus its format. Retain the capability; selection does not create or declare normative Edge records for this project. Reconcile callers with the actual document inventory. |
| `impact` | `/impact` | F's explicit issue/slice trigger with spelling corrected; body equivalent to M/A. Remove the blanket history-update exclusion under the agreed policy. New scale-routing behavior remains a separate design proposal. |
| `implement` | `/implement` | M core; equivalent to A/F. Use this project's validation tools and agreed repair policy; update renamed callers and maintenance handoff. |
| `improve-comments` | `/improve-comments` | M; equivalent shared content. Reconcile any history-reference constraints with the agreed current/evidence separation. |
| `plan-impl` | `/plan` | F core, including explicit repeated validation through the same skill; rename as agreed. Do not import the collector's local `Pass` ownership or Cursor loop configuration. |
| `recall` | `/recall` | F core: retain priority for landed-but-unchecked work. Use this project's delivery records locally. |
| `review-architecture` | `/review-architecture` | M and its `REFERENCE.md`; equivalent shared content. Update calls to the current workflow. |
| `review-impl` | `/verify` | M review body, reconciled directly with agreed repair-and-report. F contains both "do not make changes until requested" and an unconditional amendment direction, so neither body is suitable unchanged. **2026-09-05, user: renamed `/verify`.** |
| `setup-devops` | `/setup-devops` | M; equivalent to A/F and correctly named. Do not use H's mismatched `setup-project` metadata. |
| `skill-up` | `/skill-up` | M/F core as source. Adapt to inline local instructions initially and explicit file ownership; blanket appendix preservation cannot remain. Leave unresolved override policy explicit. |
| `sync-arch` | `/maintain` | M responsibilities absorbed in maintenance, as agreed: architecture/code consistency in both directions and reconstruction of load-bearing contracts. |
| `tdd` | `/tdd` | M with all five identical supporting documents. Retain the existing rule that an agreed RFC can satisfy its planning gate. |
| `to-spec` | `/spec` | M/F ordinary-spec body. Align lifecycle with maintained homes and `/maintain` archival. Do not import A's initiative/Notion branch. **2026-09-05, user: renamed `/spec`.** |
| `to-tickets` | `/ticket` | M body plus F's impact assessment of proposed slices; rename as agreed. Use local Markdown tracking for this project. Do not transfer decomposition to a proposed pacer yet. |

This retains all 21 source capabilities while consolidating `denoise` and `sync-arch` into one `/maintain` entrypoint: **20 selected working commands**. Legacy command compatibility is an installation-design question; all maintained internal references must use the selected names. No `/pacer`, `/step`, `/decompose` or wholesale Life `/mechanism` import is selected.

### Supporting files and project facts

- Carry M's `align/ADR-FORMAT.md`, `ARCH-FORMAT.md`, `GLOSSARY-FORMAT.md`, `EDGE-FORMAT.md`, the five `tdd` references and `review-architecture/REFERENCE.md`. Repair location/routing assumptions against this project's actual documents; a working source-relative link is not automatically a portable one.
- Use M's `TICKET-FORMAT.md` as the local Markdown starting shape, adapted to the conventions already used here. A's `NOTION-FORMAT.md` and `INITIATIVE-FORMAT.md` are not shared bootstrap dependencies. Keep concern formatting in M's existing `/align` body for now; A's extraction remains available as later evidence.
- Use the user's current loop sketch as the design reference. Do not install M's older workflow image as governing instructions merely because it is in the source directory.
- Treat every existing source `<project-local>` block as source-project-owned. Preserve this workspace's original corpus and audit during assembly; introduce only this project's known facts into its installed local blocks. Resolve an actual blocking conflict through `/align`, without inventing the deferred general override mechanism.
- If the selected maintenance instructions use the document mover, package its transitive `docs_corpus` dependency and validate its runtime/path assumptions. F's newline-compatible mover is the preferred code starting point. Copying `.agents/scripts` alone is insufficient.
- The collector planning loop and its tests are a concrete dependency example, not a portable default. Its `Pass` rule must not reach this project without the corresponding behavior. Host-specific automation and Tier 1 delivery still require their own implementation plan and evidence.

### Decision for this pass

~~Adopt the M-based source selection and listed F deltas as the bootstrap foundation?~~ **Accepted, 2026-09-05:** the user agreed to the presented selection, subject to the already-agreed repairs. This selects inputs and intended capabilities; it does not approve an unreviewed rewrite, installation layout or every provisional design in the harness spec.

**Still open after source selection:** exact composed maintenance/skill-update instructions, this project's required local validation facts, host installation and activation behavior, and the unselected command aliases. General queue, pacer, initiative and local-override mechanisms remain in their existing design backlog. An ambiguity that actually blocks safe assembly must be brought back as a concrete case rather than silently chosen.

### Core changes owed by later installs

Decided in [01-0010.0020](./01-0010.0020-live-alignment-across-hosts.md) on 2026-09-05; each lands with the skill it names.

- `/impact` gains a shape recommendation in its output: spec, ticket or RFC, or re-slice. The root entry file already states this intent.
- `/commit`, and any skill that gates on permission, reads the autonomy switches from the entry file's local block instead of carrying its own absolute rule.
- `/skill-up` documents `<temporary until="...">` alongside `<project-local>`.
- `/maintain` enumerates `<temporary>` statements in scope and removes the ones whose condition holds.
- `/ticket` and `/plan` call `/impact` where the entry file says they do.

## First bootstrap delivery ticket — proposed breakdown

**Status:** ~~Proposed for the user's granularity review.~~ **Accepted and minted 2026-09-05 as [01-0010.0020](./01-0010.0020-live-alignment-across-hosts.md); its root decision is resolved there.** This is the output of the requested `/ticket` pass, using M's selected ticket skill and format plus F's impact step.

1. **Title:** Align on harness work in Codex, Cursor and Claude Code.
   **Interaction:** HITL — initial project entry/delivery boundaries still require agreement.
   **Depends on:** the accepted [source selection](#bootstrap-corpus-selection) and current [process policy](../process.md), both already available; not completion of the parent or the still-open Life research ticket.
   **Parent scope covered:** spec stories 5, 6, 8 and 10, narrowly for live alignment and its impact assessment. The parent retains the remaining corpus, maintenance implementation and cross-project distribution.

**Proposed child basename after approval:** `01-0010.0020-live-alignment-across-hosts.md`.

**Outcome:** the user can open this project in any of the three hosts and align on its current work using the same selected instructions, current governing decisions and glossary, with evidence of the entry rules and skills actually made available.

**What to build:** one complete alignment path: project entry → the applicable Tier 1 rules and skill descriptions → selected `/align` and `/impact` instructions and required supporting references → current project records → a concrete decision recommendation recorded in the existing owner. No new pacer routing rules are needed for this slice. `/impact` uses its selected method and agreed history correction; it does not gain an unapproved automatic spec gate.

**Decisions this child's align would own:**

- The root from which this project's three host sessions operate and where the working corpus lives. The current working home and requested future canonical home differ; source selection did not settle this delivery boundary.
- The minimum Tier 1 entry contract for this slice: which already-agreed rules and descriptions must arrive, how the detailed current records are reached, and what observed evidence establishes availability. Host-specific file/hook implementation belongs in the subsequent RFC.

**Provisional acceptance criteria:**

- The entry/delivery decisions above are recorded in maintained governing documents before dependent implementation planning, with expected and unobservable delivery evidence distinguished.
- Fresh sessions in all three hosts discover the intended `/align` and `/impact` skill identities from the same identifiable working revision, and their required references resolve. A manual file read alone does not establish discovery.
- An explicit alignment request and a natural-language request to discuss an unresolved harness decision reach the selected instructions. The agent uses an existing accepted decision when applicable and asks one recommended decision question when a real unresolved choice remains.
- An impact assessment on a bounded change follows actual consumers, identifies what must change or be verified, and treats mechanical history maintenance according to the agreed policy. Matching words or headings alone are insufficient evidence.
- The request's result is recorded in its existing owning work without creating an unrelated ticket, reopening accepted decisions or claiming the remainder of the corpus is installed. Every host's actual observation or verification gap is recorded; missing host verification leaves the delivery criterion unfinished.

**Impact on the proposed split:** this is a thin path through content, discovery, context routing, project records and live behavior in each host. `/align` directly depends on `/impact` and its format shelf, so an align-only file copy would cut the path in the middle. Existing source projects and product code are unaffected. The principal hidden edges are duplicate/absent discovery, wrong source-project links or local facts, stale session context and treating emitted text as delivered instructions. The full installation/distribution engine and the new `/maintain` implementation are not prerequisites for exercising this path.

**Remaining bootstrap scope:** subsequent tickets can extend the same proven entry/delivery boundary to spec/ticket/planning, implementation/review, maintenance, and the remaining selected capabilities. This pass does not claim to have decomposed or approved those later tickets. If the first slice's delivery decisions reveal materially separate contracts, refine this proposed ticket before its RFC rather than silently broadening it.

## Adoption shortlist — recommendations awaiting alignment

This is the compact decision surface extracted from the [Life research](../research/life-harness-findings.md). Rows marked agreed link to the current policy; the other recommendations remain undecided. Resolve one question at a time.

| Order | Decision | Recommendation |
|---|---|---|
| 1 | Does the loop need a spec, including for this job? | **Agreed:** substantial work uses a spec, including this harness; small fixes can start at a ticket. `/align` spans the whole loop. The spec content itself remains to be aligned. |
| 1a | What does each HITL checkpoint require? | **Agreed:** [autonomy and repair policy](../process.md#autonomy-and-repair). Repair-and-report within its conditions; otherwise align. **Remaining implementation:** route this consistently across skills, reconcile existing checkpoint wording, and verify delivery. `/impact` is a candidate assessment procedure, not a mechanical certificate. |
| 2 | How should mechanisms govern skills and maintain themselves? | **Agreed:** [mechanisms and skills](../process.md#mechanisms-and-skills) and [tree maintenance](../process.md#tree-maintenance). `/maintain` covers all applicable mechanisms and owns all `/denoise` and `/sync-arch` responsibilities, including archiving. **Remaining design:** exact boundaries, document layout, maintenance triggers, scope derivation and automation. |
| 3 | Where do current rules, decisions and evolution live? | **Agreed:** [current documents and evidence](../process.md#current-documents-and-evidence), including one evidence/evolution record per mechanism, created when needed. |
| 4 | Should tickets, RFCs, specs, concerns and ideas all be queues? | Share a minimal lifecycle contract for actual queues: entry, owner/consumer, disposition, exit and maintenance. Decide which artifacts really need queues; specs and RFCs can be documents attached to work without independent backlogs. |
| 5 | Which queue machinery should be adopted? | Start with file/index consistency, explicit unresolved decisions, actionable stale/unknown state and evidence-based closure. Consider strikes as recurrence evidence on the affected work item; do not copy Life's entire counters, quotas or scheduling policy. |
| 6 | How should delivery and drift be maintained? | **Agreed:** [mechanical maintenance](../process.md#mechanical-maintenance), including history, missing repair scripts and mechanisms designed for derivation. **Remaining design:** dependency representation, change tracking, scheduling and verification across projects and hosts. Separate installation freshness from derived-work correctness and live instruction delivery. |

The autonomy/repair policy, mechanism concept, current/history separation and mechanical maintenance principle are agreed. Queue design (items 4–5) and the concrete maintenance design remain open. The spec as a whole and any implementation RFC remain unapproved; accepted decisions and command names are recorded above.

## Idea — pacer

→ [Pacer](../pacer.md). Moved to its own document at the user's request, 2026-09-05. It now includes the required unit-of-work definition and a hypothesis for the current bootstrap step; neither a pacer skill nor the hypothesis is adopted by this move.

## Derived work — Life basis and scope decision

Life already supplies the dependency rule; it should be adapted rather than independently reinvented:

- [`/mechanism`, Amend](D:/Dev/AI/life/.agents/skills/mechanism/SKILL.md): derive every reliance, recheck both ends, and treat what the change makes stale as part of the change.
- [`/maintain`, Pipeline](D:/Dev/AI/life/.agents/skills/maintain/SKILL.md): governing mechanism instructions → instance doc/rules → records. Repair upstream first, then downstream; move only the verification marks actually reached.
- [Maintenance mechanism](D:/Dev/AI/life/mechanisms/maintenance/maintenance.doc.md): changed governing versions create persistent maintenance due state. Installation freshness and output verification are separate facts. Phase A/research describes the implementation limits; hashes identify a change, not its semantic effect.

The dev-harness policy is now recorded in [mechanical maintenance](../process.md#mechanical-maintenance). Its scope includes affected tickets, RFCs, specs, docs, code, checks and historical records as appropriate. A wording-only change may require no downstream repair; a changed ticket contract may require a scripted migration of both open and completed tickets. The governing contract determines the repair; unknown historical facts remain unknown.

**Superseded proposal:** the assistant proposed exempting frozen historical records. The user instead required mechanical fixes wherever possible, including history, and derivability by design. Life's narrower live-record repair scope is research evidence, not the adopted dev-harness policy. Cross-project dependency tracking, verification marks and scheduling remain implementation design.

## HITL checkpoints — initial source check

This is an inventory for the spec, not an adopted approval policy or a complete corpus-wide census.

| Checkpoint | Existing evidence | Question for the design |
|---|---|---|
| Ticket breakdown | Meteoscape `/to-tickets` asks the user to approve the breakdown. | What approval covers, and when an amended breakdown needs another decision. |
| Interfaces/test priorities | Meteoscape `/tdd` requests agreement, but explicitly accepts an existing RFC as satisfying its planning gate. | Reuse prior decisions instead of asking again at each nested skill. |
| Architectural conflict | `/plan-impl`, `/sync-arch`, `/review-impl`, `/denoise` route ambiguity or substantial conflict to `/align`. | Resume the affected stage after recording the resolution. |
| Commit and push | `/commit` requires explicit authorization separately for each; `/implement` repeats the commit condition. | Permission scope and one authoritative policy with inline delivery at the action. |
| Review findings | Meteoscape `/review-impl` waits for a request before amendments; Forecast Collector differs (Phase A). | Reconcile the variants with the agreed [repair policy](../process.md#autonomy-and-repair) when updating the canonical skills. |
| Next ticket/cycle | Named by the user as a HITL checkpoint; subsequently clarified as dynamic autonomy within established principles. `/recall` reconstructs current state and calls `/align` for decisions. | Establish whether the next work remains inside agreed scope and architectural constraints; a cycle boundary alone does not define the human decision. |

The ticket text also describes AFK slices as implementable/mergeable without human interaction, while the shared commit skill requires permission. Their relationship needs an explicit scope rule. No existing gate has been removed or changed.

## Acceptance criteria

- [x] Existing copies, links, substantive changes and local divergence are compared in a reviewable report.
- [ ] Shared method, local ownership and propagation decisions are recorded with user agreement.
- [ ] The canonical suite contains the agreed versions with their dependencies intact.
- [ ] A change originating in project A can reach core and project B through the agreed process, with provenance and no unintended local-content changes.
- [ ] Concurrent shared edits, malformed local markers and unknown installation baselines are detected and surfaced rather than silently overwritten.
- [ ] Discovery and invocation of representative installed skills are verified separately in the three frameworks; unavailable checks remain explicitly unverified.
- [ ] Maintenance can identify drift and failed delivery without treating silence as success.

## Out of scope

Importing Life's public-forum operations, identity, private instance data or blanket autonomous rule-adoption policies. Those require separate intent and are not prerequisites for shared dev skills.
