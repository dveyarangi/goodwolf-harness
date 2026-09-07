# Life findings and a proposed dev-harness change loop

Research snapshot: 2026-09-05. **Proposal for alignment, not an adopted architecture.**

Owned by [the completed research ticket](../tickets/done/01-0010.0010-life-informs-dev-harness.md), within [the shared-harness work](../tickets/01-0010-dev-harness-shared-and-local.md). The earlier [copy and discrepancy audit](audit-2026-09-05/REPORT.md) remains the source for existing skill variants. Subsequent accepted policy is in [the process](../process.md); this dated research proposal is not the current policy, including where it suggests exempting historical records.

## Recommendation

Keep shared and project-local instructions in **one installed skill file**, with an explicit local block. Keep the accepted shared method in the future canonical Git repository. Let a project propose a shared improvement from its working copy; accept it through the core project's ticket/RFC/development loop; let other projects pull accepted revisions at a task boundary.

The requested canonical home is `D:\Dev\AI\agents`; the working research home remains `D:\Dev\AI\.agents`. The former has not been created. Moving this project's working documents belongs with the agreed canonical layout.

Use a last-installed baseline to distinguish incoming core changes from outgoing project changes. The baseline is machine data: the agent does not need to load it to follow the skill. This therefore does not introduce the extra instruction-delivery dependency that motivated keeping the local instructions inline.

Life supplies useful concepts and concrete failure cases. Its implementation should be treated as design evidence, not copied as a complete framework. In particular, the current injector is not a three-way distributor, and its file checks do not prove live instruction delivery.

## What was investigated

I read Life's governing definitions, rule evidence, all existing mechanism `.doc.md` and `.evidence.md` files, the mechanism register, and the relevant development and maintenance skills. I traced the injector, maintenance calculation and delivery checks into code, inspected representative tests, and ran seven isolated probes against the existing implementation. Detailed scope is at the end.

The observed Life HEAD near completion was `5fa11d3` (2026-09-05 13:57:51 +03:00). Reads used its working tree; this was not a frozen checkout or a whole-repository certification. No Life files were edited. The six implementation files fingerprinted around the probes remained unchanged. Probe fixtures were created in a new temporary directory.

Life documents contain project instructions, historical operator decisions, experimental claims and external discussion. These were read as research material. Their auto-commit permission, public-board activity, mandatory session routines and rule-adoption permissions have not been adopted here.

## 1. Separate three questions about a rule

Life's [core definitions](D:/Dev/AI/life/core/README.md), [meta-rule mechanism](D:/Dev/AI/life/mechanisms/meta-rules/meta-rules.doc.md), [rule evidence](D:/Dev/AI/life/docs/rules-evidence.md) and [skill evidence](D:/Dev/AI/life/memory/skills.md) distinguish:

| Question | Life's model | Useful application here |
|---|---|---|
| Who owns the decision? | Strict, meta and ordinary rules; different adoption/amendment authority | Distinguish user decisions, accepted shared method and project conventions. A locally edited shared instruction is a proposal until accepted into core. |
| How does it reach the agent? | Delivery tier 1: supplied without a fetch; tier 2: routed/fetched; tier 3: no effective route | Track delivery per host and opening context. A correct file can still be undiscovered. A link to a file does not establish that it was read. |
| Why believe it helps? | Bone, muscle, skin, unlabelled; evidence retained separately | Record whether a change responds to an observed failure, a tested case, an external method or a preference. Preserve limitations and withdrawn ideas without carrying their history in every invocation. |

**These are independent axes.** A user decision can have high authority and no empirical claim. A tested technique does not gain authority to override a user decision. A rule's placement in a frequently loaded surface says nothing about its correctness.

There is a terminology trap worth avoiding: Life's `/failure` also numbers detection failures as tiers 1–3—no memory, memory not delivered, memory delivered but insufficient. Those numbers mean something different from the delivery tiers above. For this project, explicit names would be clearer than reusing numbered tiers for both.

Life itself revised “requested at wake” into tier 2 after discovering that instructions to read a file are not forced loading. We should carry that distinction into all three hosts, with `unverified` available where the actual session input cannot be observed.

**Pushback:** I would not import the bone/muscle/skin vocabulary or all of Life's rule classes as mandatory metadata initially. Plain evidence and decision ownership on a ticket/RFC provide the needed distinction with less machinery. Nor should we inherit the blanket rule that a later session must grade all work: a fresh context can help challenge criteria, but is not independent evidence by itself. Deterministic verification can and should happen during implementation.

## 2. A mechanism is the behavior and its consumers

Life's [mechanism skill](D:/Dev/AI/life/.agents/skills/mechanism/SKILL.md) and [mechanism-shape document](D:/Dev/AI/life/mechanisms/mechanism-shape/mechanism-shape.doc.md) ask who produces a thing, who consumes it, what triggers the work, what verifies it, and what happens when it changes or is removed.

This is useful for us because the current shared suite already spans files: skill bodies, format appendices, scripts, Python imports, loader links, hooks and project document paths. Moving only `SKILL.md` would leave some of that behavior behind. The Phase A audit's `move_doc.py` imports and the differing A-versus-M/F relative link depths are concrete examples.

Life's “moments” table is the most reusable documentation device. For each important transition, name the actor, the input and the action that consumes it. A draft saved somewhere is not a proposal workflow until the core project's loop has a way to find and decide it. A discrepancy report is not distribution until a recipient can apply it.

A small initial mechanism record can fit in the owning RFC/architecture section:

| Field | What it answers |
|---|---|
| Purpose and boundary | What outcome does this provide, and what remains a project/host responsibility? |
| Producer and consumer | Who writes each artifact, and which exact command or skill reads it? |
| Trigger | When is the consumer invoked? What happens if that event was missed? |
| Ownership and dependencies | Which files or regions are managed, local, generated or merely depended on? |
| Verification | What observable failure would expose a broken implementation or a wrong assumption? |
| Change/removal behavior | What becomes stale, how is it repaired, and what data survives removal? |

This does not yet justify a directory, installer, uninstaller, evidence sidecar and registry row for every concept. Life's own [metrics evidence](D:/Dev/AI/life/mechanisms/metrics/metrics.evidence.md) records that the most complete implementation was mistaken for the right shape. Its [concerns evidence](D:/Dev/AI/life/mechanisms/concerns-register/concerns-register.evidence.md) finds the registry grouped subjects while missing the action that spans them. Structure needs to follow the behavior we actually build.

## 3. What works in Life's mechanics, and where the claim stops

### Injection

The [generic injector](D:/Dev/AI/life/.agents/scripts/inject-rules.js) reads one rule source with target and anchor information. It writes visibly owned, delimited blocks into host skills. Its [shared parser/renderer](D:/Dev/AI/life/.agents/lib/injected-blocks.js) is also consumed by the state checker, avoiding two incompatible definitions of a matching block.

Useful behavior confirmed in fixtures:

- Install preserves surrounding text; a repeated install is idempotent; install followed by pause restores the fixture host exactly.
- A changed source and a changed installed block both produce a refusal without explicit overwrite.
- `--check` reports an absent block without writing.

Limits confirmed in fixtures:

- **The two-file comparison cannot identify the direction of change.** Both a source amendment and a target edit receive the same explanation. Life deliberately supplies intent through `--overwrite`; its evidence records rejecting coupling this to the unrelated maintenance clock. Our distribution use case needs an actual installation baseline for a different purpose.
- **Application can be partial.** With two target rules, the first valid target was updated and the second missing target refused. Exit code was 1 and the document still declared `paused`. The tool reports the partial result honestly; it does not promise or perform transaction rollback.
- **Exit zero is not “already synchronized.”** An absent block with a valid anchor produced exit zero and “absent, would install.” A caller needs structured states or must interpret the output correctly.
- The renderer points writers to “its doc,” although the actual text source is the mechanism's `.rules.md`. This is a small routing inconsistency in the component whose purpose is single ownership.

The [probe script](probe-life.cjs) and [captured results](probe-life-results.json) contain the reproducible cases. These checks characterize the existing implementation; they are not a new distributor or a claim that Life's full suite passes.

### Maintenance

Life implements a useful dependency chain:

```text
governing /mechanism instruction changes
    → dependent mechanism rules need rechecking
mechanism's own instruction surfaces change
    → its outputs/records need rechecking
maintenance finishes at a level
    → record the version checked at that level
```

The [maintenance document](D:/Dev/AI/life/mechanisms/maintenance/maintenance.doc.md), [shared calculation](D:/Dev/AI/life/.agents/lib/maintenance-marks.js), [wake consumer](D:/Dev/AI/life/.claude/hooks/maintenance-due.js) and [mark writer](D:/Dev/AI/life/.agents/scripts/maintenance-mark.js) implement this using hashes and marks. The read-only calculation is reused by the turn-report counter. Missing files contribute an absence marker. Line endings are normalized. Evidence and externally owned injected blocks are excluded from the governing hash.

The probes confirmed that a governing change creates persistent staleness, repeated assessment does not write the marks, a real content change affects the hash, and an LF/CRLF change does not. This is a stronger recovery mechanism than an edit notification that only fires once in the already-busy authoring session.

What we should retain:

- Compare **what was checked** against **what now governs it**.
- Keep `never checked`, `stale`, `unavailable` and `checked against this version` distinct.
- Derive status from one implementation reused by reporting and updating.
- Keep content synchronization and semantic verification separate: copying a new skill is not proof that its existing RFCs or generated documents satisfy the new rule.
- Maintenance repairs within the authorized task, verifies the repair and records the result. Merely describing a defect must not clear it. Life's [maintenance evidence](D:/Dev/AI/life/.agents/skills/maintain/EVIDENCE.md) records exactly that failure.

What we should not treat as stronger evidence than it is:

- A maintenance mark is an attestation. The writer computes hashes; it cannot establish that the procedure or judgment really happened.
- The record-churn implementation counts observed hash transitions. It has no session-identity deduplication; “distinct sessions” depends on the caller invoking it appropriately. Its representative test simulates repeated wakes, not distinct session identities.
- Missing one maintenance level is not the same as never having any mark. The current calculation treats either level's mark as `marked`; a distributor should model each required check explicitly.
- The five-session threshold and context budgets are local choices, not established universal settings.
- A hook has runtime, maintenance and notification costs even when it saves instruction tokens. Life's wake runner records multiple process launches delaying or losing delivery under load; mechanical does not mean free.
- Ignoring another owner's block is appropriate for an ownership hash. It is not automatically appropriate for a behavior-verification hash: changing an injected instruction can still change what the host skill does.

Life's [maintenance evidence](D:/Dev/AI/life/mechanisms/maintenance/maintenance.evidence.md) and [suite evidence](D:/Dev/AI/life/mechanisms/hook-suite/hook-suite.evidence.md) also record tests polluting live measurement data. Fixture isolation and separate read/calculation/write functions are requirements worth carrying into our implementation.

### Delivery and observability

| Surface | What the implementation establishes | What remains unproved by that check |
|---|---|---|
| [`rules-loaded.js`](D:/Dev/AI/life/.claude/hooks/rules-loaded.js) | Certain phrases and a meta-rule count exist in the disk `CLAUDE.md` | That these bytes were supplied to a live agent session. The probe returned quiet with synthetic disk text and no context input. |
| [`skills-reachable.js`](D:/Dev/AI/life/.claude/hooks/skills-reachable.js) | Skills exist in the home; the Claude loader path resolves to that home; a plain-text link checkout is diagnosed | A live catalog lists them, invocation selects the intended variant, or a rule-reference graph is traversed. The code acknowledges the catalog limit; broader prose elsewhere overstates it. |
| [`wake.js`](D:/Dev/AI/life/.claude/hooks/wake.js) | Declared announcement parts return content, return quiet, are missing, throw or time out; a ledger is emitted | That the host delivered the emitted output in full, or that an agent used it. A part that catches its own error and returns quiet hides that error from the runner. |
| [`extract-core.js`](D:/Dev/AI/life/.agents/scripts/extract-core.js) | Source selection and, on the copy path, certain settings/import/link references can be checked | A fresh installation actually boots and behaves correctly across hosts. It also skips symlinks for manual recreation. |

The read-error probe on `rules-loaded.announce()` returned the same quiet shape as the valid-file case. This probe deliberately calls the module with a directory path, bypassing its standalone argument-kind check; it demonstrates the swallowed-exception contract, not that the production runner normally passes that invalid path.

The [turn-report evidence](D:/Dev/AI/life/mechanisms/turn-report/turn-report.evidence.md) is a particularly useful positive example: it records an actual operator-facing probe of which hook fields rendered, how line breaks appeared, and whether links worked. That kind of end-to-end measurement is what our three-host work needs.

For our acceptance checks, distinguish:

1. Installed files and aliases are correct.
2. The host discovers the intended skill in the actual opening context.
3. Invocation reads the intended body, local block and required supporting files.
4. A representative task demonstrates the intended behavior, including a local exception.

Record host/version/opened root/core revision for that observation. If a host exposes no direct context inspection, say what was observed and what remains inferred. A filesystem check cannot stand in for steps 2–4. New copies, links and compatibility aliases can also create duplicate discovery; test the selected entry, not only whether a name appears somewhere.

## 4. Life also demonstrates the maintenance burden we should avoid

Several contradictions remain visible across the current instruction and documentation surfaces:

- [`triage/SKILL.md`](D:/Dev/AI/life/.agents/skills/triage/SKILL.md) opens with one item per pass, then specifies one per backlog. Its local text still says a ticket cannot be declined, although [`TICKET-FORMAT.md`](D:/Dev/AI/life/.agents/skills/ticket/TICKET-FORMAT.md) defines and routes declining. These are behavior changes that did not reach all their statements.
- [`staggered-refiling.doc.md`](D:/Dev/AI/life/mechanisms/staggered-refiling/staggered-refiling.doc.md) says a bare invocation pauses, alongside text saying the mode is required; current injector code requires exactly one mode. It also retains references to per-mechanism installers while explaining that the generic injector replaced them.
- [`core/glossary.md`](D:/Dev/AI/life/core/glossary.md) says `/recall` has never named the session-record directory. Current [`recall/SKILL.md`](D:/Dev/AI/life/.agents/skills/recall/SKILL.md) explicitly reads it. A definition carrying a historical diagnosis became stale.
- [`skill-up/SKILL.md`](D:/Dev/AI/life/.agents/skills/skill-up/SKILL.md) says local blocks never override the body. Phase A found actual project exceptions that do. Synchronization needs an honest exception policy instead of assuming this sentence describes practice.

These findings do not invalidate the concepts. They argue for fewer authoritative statements and mechanically derived inventories, with history in the ticket/RFC that already owns it. A broad taxonomy and many mutually referring files will not enforce their own consistency.

We should also resist treating every symptom as a new mechanism. Life's failure/retrieval evidence shows classifiers themselves manufacturing plausible measurements, and warns that zero observed failures can mean no opportunities, no observation, or successful prevention. For the dev harness, begin with observable discrepancy states and concrete regression cases; add instrumentation when a question needs it.

## 5. Keeping one instruction file

The user's preference is a sound starting point. Recommended installed shape:

```markdown
---
name: skill-name
description: When to use it.
---

Shared instructions.

<project-local>
Project conventions and explicitly scoped exceptions.
</project-local>
```

The exact parser rules remain for the RFC. The intended contract should be:

- The local block stays in the file the agent opens. Its bytes are preserved during shared updates.
- Ordinary text mentioning `<project-local>` is not a local block. Malformed, nested or ambiguous real delimiters produce a discrepancy before any update.
- Shared text outside the block may be edited in a project and becomes an outgoing shared-change candidate; it is never silently discarded as “corruption.”
- A project exception names what it specializes or overrides. Newly conflicting core behavior requires review even if the text merge is clean. This policy needs alignment; the present “adds, never overrides” assertion does not match actual usage.
- The core repository's own project-local block is for developing the core project. It does not replace the consumer's block during distribution.
- Supporting files need explicit ownership too. Shared TDD guidance must not be skipped merely because it is an appendix; project-owned ticket formats must not be overwritten merely because they are next to a shared skill. Phase A provides the initial classification evidence.

**The limit of “one file”:** keep the executable instructions together; do not also put revision baselines, the whole change history and every test result into it. Machine state can live in a lock/manifest without becoming another instruction file. A script dependency can remain a script. None of those requires the agent to fetch a second policy before following the first.

## 6. Project A → core → project B

Example grounded in the audit: Forecast Collector improved `/recall` so work that landed but still needs verification is not lost at the next session. That is a plausible shared candidate; it is not automatically universal just because it is newer.

Recommended flow, with command names illustrative rather than implemented:

1. **A works on a real ticket.** It finds the omission and edits the shared part of its installed `/recall`. Evidence and intended behavior go on that ticket. A project-specific path or exception belongs in its local block.
2. **A checks the harness state.** The checker compares A's shared content to A's last-installed shared baseline and the accepted core revision. It reports an outgoing change separately from incoming updates and local edits.
3. **A prepares a core proposal.** A core ticket carries the patch, originating project/ticket, installed base revision and the case motivating the change. The local block is excluded. Repeated checks identify the same proposal rather than minting duplicates. Detection can be automatic; generalization and acceptance remain decisions.
4. **The core project develops the change using its own loop.** Align shared scope; write an RFC where the design needs one; implement and verify against the motivating case and relevant project/host variations. Record an accepted revision through the agreed commit/release process. This research has not authorized a commit.
5. **B pulls an accepted revision at a task/session boundary.** Compare before replacing anything. Retain B's local block and unowned files, include managed dependencies, validate the installed result, then advance B's baseline. Report the exact revision and any skipped/conflicted files.
6. **A reconciles with the accepted result too.** If core accepted A's exact shared text, it is already converged; record that known installed state after validation. If core revised the proposal, reconcile A's remaining shared difference rather than overwrite it.

The core may enumerate which projects are behind, but should initially **publish availability rather than rewrite active project files**. Pull is easier to reason about with active tasks, multiple checkouts and project exceptions. Later, an opted-in launcher/startup adapter can perform an ordinary clean pull automatically. A missing or unsupported startup event must remain visible; an explicit check should work in all hosts.

This is not a claim that changing files reloads an active skill or clears an agent's earlier context. Updates become the declared baseline for a subsequent task/session, or a deliberate re-invocation with the revision made explicit. Avoid global live symlinks from all projects straight into mutable core content: they make a core edit active everywhere immediately and leave no place for independent inline local blocks.

### The comparison needs three versions

Let **B** be the last installed shared baseline, **C** the selected accepted core revision, and **P** the project's current shared content. Compare the rendered form where installation adapts paths. Do not use timestamps to infer lineage.

| Relationship | State | Recommended action |
|---|---|---|
| P = B and C = B | Current | No shared update |
| P = B and C differs | Incoming only | Eligible for an ordinary pull; preserve local content |
| C = B and P differs | Outgoing only | Prepare a shared proposal; preserve P |
| P = C, both differ from B | Converged | Validate and advance baseline; avoid an unnecessary rewrite |
| P and C differ from B and from each other | Both changed | Present a three-way diff; retain both sides until reconciled |
| Baseline absent/unresolvable | Unknown installation | Import/reconcile explicitly; never guess which side is ahead |

A hash identifies a version but cannot reconstruct it. The baseline therefore needs retrievable content, such as the exact source revision plus deterministic rendering, or a stored installed snapshot. Comparison may normalize line endings; it should not erase arbitrary whitespace, formatting or instruction clauses to make differences disappear.

Other states are explicit: a locally deleted managed file, a core removal, a new local skill, a renamed managed file, unavailable core, malformed marker and conflicting same-name file. An updater should know its managed set and report unknown files instead of claiming to copy “everything” safely.

### What can be mechanical

- Inventory links/copies and enumerate managed files, hashes and dependencies.
- Detect incoming, outgoing, converged, conflicting and unknown states.
- Preserve well-formed local regions and project-owned files.
- Prepare a patch and provenance for a core proposal.
- Apply an accepted, conflict-free update and validate its result.
- Report installation state independently of host delivery and behavioral verification.

What remains judgment: whether A's fix belongs in every project, whether it contradicts an intended local exception, whether the evidence supports a broader instruction, and whether a textually clean merge changes the method incorrectly.

The first updater should preflight the full selected update, stage the intended files, check for concurrent edits before writing, retain recovery data and advance installation state only after verification. Multiple file writes are not inherently atomic; failures must report what changed and support recovery. A dry-run is a reviewable update, not proof the apply will succeed. The RFC should make interrupted updates and changed files between check/apply explicit cases.

## 7. The proposed development loop

The user's [sketch](../../dev-skills.png) separates session continuity from delivery work, and places tickets, RFCs, architecture, external reality and code inside the delivery loop. That is a useful model. The colors and dotted lines have not been assigned semantics beyond what the image labels establish.

I would retain the shape with these clarifications:

| Part of the loop | Recommendation |
|---|---|
| `/align` | Resolve the need, language and consequential decisions. Reachable whenever a premise changes, not only through plan/verify escalation. Record decisions in the owning ticket. |
| `/ticket` ↔ `/plan` | A ticket defines the outcome and acceptance criteria; planning tests feasibility and can refine/split the ticket. A substantive implementation RFC owns the plan. Small routine changes need not manufacture an RFC. |
| `/plan` → `/implement` | Establish the verification approach before building. Describe observable behavior, including failure cases and local exceptions. |
| `/implement` ↔ `/verify` | Make failed verification return explicitly to implementation. Verify the ticket outcome as well as tests; documentation and architecture consistency are part of this, not postponed indefinitely. |
| `/maintain` | Triggered by governing-method changes, stale outputs, drift or a selected maintenance task. Repair and verify, or record the decision preventing repair. Avoid a full harness maintenance pass after every product ticket. |
| `/conclude` → `/recall` | Can bridge an interruption anywhere in the loop. Preserve active work, unresolved decisions, verification owed and installed method revision. Recall reads current ticket state; a session summary is not a second delivery queue. |
| `/dream` | Optional source of candidates. A candidate can enter alignment/ticketing; it does not amend shared instructions or count as evidence by itself. |
| Accepted change → distribution | Add an explicit accepted-revision/check/pull transition for method changes. This can sit inside the completion flow rather than becoming another top-level skill. It is presently implicit in the sketch. |

The current suite does not yet use all the sketch's names: `/to-tickets`, `/plan-impl` and `/review-impl` provide parts of `/ticket`, `/plan` and `/verify`. Renaming should follow agreement on responsibilities, with references and host invocations checked together. Do not create parallel synonyms with diverging implementations.

For the method corpus, initially use accepted shared skills and their supporting references, with proposals and evidence in tickets/RFCs. It should have a route for editing the shared method without becoming a second independently maintained copy of the instructions.

## 8. Minimal structure to carry forward

Three boundaries are sufficient for the first design:

1. **Shared method:** accepted skills, their shared dependencies, and the mechanism that checks/distributes them.
2. **Project conventions and state:** inline local blocks, explicitly project-owned supporting files, project docs and the installed-version baseline.
3. **Host delivery:** a small integration per Claude Code, Codex and Cursor that exposes the same installed method through the host's supported routes, with separate verification of those routes.

The core project consumes its own shared method and keeps its own local conventions, like a recipient. Its tickets/RFCs develop distribution and host integration through the same loop; it does not need a separate self-development bureaucracy.

Start with the updater's shared parse/comparison logic, a CLI and a reviewable report. Add host automation after proving explicit installation and invocation. This sequencing isolates distribution failures from loader failures and avoids betting the first version on three supposedly equivalent startup hooks.

**Next alignment decision:** may a project edit the installed shared body, with that difference proposed back to core, while accepted revisions are pulled by recipients at a task boundary? This is the recommended ownership direction. Canonical membership, exact local override policy, supporting-file ownership, layout and automatic-update policy follow from it; they are still open.

## Source coverage and limits

Read in full for this investigation (some governing skills were also read during Phase A):

- Life `CLAUDE.md`; `core/README.md`, `core/process.md`, `core/glossary.md`; `.agents/README.md`; `memory/README.md`, `memory/skills.md`; `docs/rules-evidence.md`.
- All existing mechanism `.doc.md` and `.evidence.md` files under: `bootstrap`, `concerns-register`, `evidence-sidecars`, `experiments`, `failure-register`, `hook-liveness`, `hook-suite`, `layer-separation`, `links`, `maintenance`, `mechanism-shape`, `meta-rules`, `metrics`, `reasoning`, `retrieval-audit`, `skills`, `staggered-refiling`, `ticket-queue`, `turn-report`. Not every mechanism has an evidence file. Also the mechanism-shape register and maintenance rules file.
- Skills: `mechanism`, `maintain`, `failure`, `ticket` and `TICKET-FORMAT`, `implement`, `recall`, `triage`, `conclude`, `dream`, `skill-up`; mechanism and maintain skill evidence. The Meteoscape `align` skill was read and supplies the current alignment procedure.
- Implementation: `inject-rules.js`, `extract-core.js`; libraries `injected-blocks.js`, `mechanism-state.js`, `maintenance-marks.js`, `argv-path.js`; hooks `rules-loaded.js`, `skills-reachable.js`, `maintenance-due.js`; script `maintenance-mark.js`.

Selected code paths/readings, not a whole-file or whole-suite audit: `wake.js`, `tier1-budget.js`, `stages-name-owners.js`, `layers.js`; injector/maintenance/rules-loaded/reachability tests and fixture isolation setup in `hooks.test.js`. Existing evidence documents and code comments were used to locate historical failures; their entire Git history and external forum accounts were not independently reconstructed.

Not read exhaustively: every Life ticket and session, all skills unrelated to this design, raw telemetry streams, private bindings/secrets, mirrored external discussions, every hook/library implementation, all experiment/metric data. No live hooks, public-board operations, full Life test suite, extraction, or host installations were run. No claim is made that all Life behavior was verified or that any live host supplied a new dev-harness instruction.

The next implementation RFC should cite the useful findings and relevant cases here, rather than copy this research history into installed skills.
