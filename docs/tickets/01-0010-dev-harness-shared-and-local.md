# A shared dev harness improves without losing project conventions

- **Status:** In progress
- **Type:** HITL
- **Outcome:** Projects share a canonical development method, contribute improvements to it, and receive accepted changes mechanically while preserving project-specific behavior across Claude Code, Codex and Cursor.

## What to build

Consolidate the existing dev skill family into the requested canonical home, after alignment on the comparison findings. Establish how improvements found in a consuming project are proposed to core, accepted there, and received by other projects. Develop and maintain the harness using its own loop.

## Evidence

- [Harness spec — draft](../spec/01-0010-dev-harness-shared-and-local.md): agreed requirements and unresolved acceptance scenarios, under alignment before implementation decomposition.
- [Initial comparison](../research/audit-2026-09-05/REPORT.md): independent physical copies, local loader aliases, divergent bodies, appendices and script dependencies.
- [Life investigation](done/01-0010.0010-life-informs-dev-harness.md): completed research on rule delivery, mechanisms, maintenance and their applicability to the dev harness.

## Resolutions and constraints

- **2026-09-05, user:** this project should use tickets, RFCs and the development loop it provides to others.
- **2026-09-05, user preference:** keep shared and project-local instruction content in one skill file initially. Motivation: extra instruction files create delivery assumptions that need instruction and testing themselves. Treat this as the starting direction; any contrary recommendation needs concrete evidence.
- **2026-09-05, user:** investigate Life thoroughly, especially rule tiers, mechanisms and maintenance, for a cleaner dev-harness structure. The earlier proposal to exclude Life from design input is superseded. This does not approve importing all Life policies or implementation.
- **2026-09-05, user:** agrees overall with project-originated shared improvements being proposed to core and recipients pulling accepted changes. Detailed update policy remains open. Requests smaller, sequential alignment on the development loop, specs, mechanisms, document separation and queue machinery before further design adoption.
- **2026-09-05, user:** accepts a spec for substantial work, including this harness, with the clarification that `/align` remains the common entry/reentry and human-decision procedure across the entire loop: spec inception, resuming any stage and HITL escalations. It is not specialized to specs. The user identifies ticket splitting, commits and moving to the next loop cycle as existing human checkpoints whose treatment needs alignment.
- **2026-09-05, user:** autonomy is dynamic. Early work needs human control over setup, core code shapes, modules, approach and governing principles. As those principles become established, more work can proceed autonomously within them. Gaps, inconsistencies, violations and changes that do not fit architectural constraints should trigger HITL, potentially through `/impact`. This supersedes the assistant's proposed fixed one-ticket/one-cycle authorization default; the exact escalation threshold remains to be aligned.
- **2026-09-05, user:** accepts repair-and-report for clear repairs within authorized work that restore an explicit architectural rule while preserving agreed contracts. Requests a well-defined policy. The current rule, reporting requirements and escalation conditions are recorded once in [the process](../process.md#autonomy-and-repair); architectural ambiguity and changes to principles still require `/align`.
- **2026-09-05, user:** agrees that a skill is the instruction part of a mechanism, with maintenance covering the whole mechanism, including consumers, checks and records. Recorded in [the glossary](../../.agents/glossary.md), which owns **Mechanism** and **Skill**. This adopts the concept, not Life's implementation wholesale.
- **2026-09-05, user:** adopts one evidence/evolution record per mechanism, created when needed, with current behavior in core docs/skills and change decisions retained in their tickets/RFCs. Recorded in [the process](../../.agents/skills/mechanism/SKILL.md#three-homes-and-the-chain). Also directs attention to Life's existing `/mechanism` and `/maintain` rules for derived work becoming stale after its governing skill changes; this is part of the design, not merely prose cleanup.
- **2026-09-05, user:** anything that can be done mechanically should be fixed mechanically, including history. Maintainers can write maintenance scripts, and mechanisms must encourage mechanical derivation and fixes from inception. This supersedes the assistant's proposed blanket exemption for frozen historical records and does not adopt Life's archive exemption. The current rule is in [mechanical maintenance](../../.agents/skills/mechanism/SKILL.md#mechanical-by-construction).
- **2026-09-05, user:** spec first; review the existing skills before proceeding. This reaffirms the earlier spec decision and makes spec development the next step, ahead of further queue design. Source review: Meteoscape and Forecast Collector `/to-spec` explicitly cover substantial inception before ticket decomposition and do not queue the spec itself; `/to-tickets` also accepts bounded discussed work without a spec; `/plan-impl` requires an owning ticket for an RFC. The current workspace's older `/to-tickets` assumes a spec, while its `/to-spec` has conflicting output paths. The existing research/alignment tickets remain valid; implementation decomposition follows the harness spec.
- **2026-09-05, user:** accepted the first bootstrap slice as proposed and decided the root: the harness is the git repository `D:\Dev\AI\agents`, with the installed corpus under `.agents/skills`. `/align` and `/impact` are installed from Meteoscape with the accepted deltas; nothing else is installed or renamed yet.
- **2026-09-06, user:** mint Install `/spec`. Spec-first and loop completion do not contradict: install `/spec`, use it to develop the spec for completing the delivery ring on this harness, then take the natural course. `/plan` is planned by reading `/plan`. A ticket whose criteria are met moves to `done/` as part of that close. Ring-skill tickets are not pre-minted.
- **2026-09-06, user:** the pacer is not a child of this ticket. It is [01-0020](./01-0020-pacer.md), parented on [pacer.md](../pacer.md).
- **2026-09-06, user:** do not close a ticket until `/verify` has been run on it; reviewing is an acceptance criterion. 0020, 0030 and 0035 were reopened; they stay `Partial` until that box is checked.
- **2026-09-06, user:** 0050 installs the implementation mechanism — `/implement`, `/tdd` (with its files), `/improve-comments` — not the `/implement` skill alone. `/verify` and `/maintain` stay later ring mechanisms.
- **2026-09-06, user:** `/verify` is the verification of landed work, not only documentation or shape review. `/implement`'s typecheck/suite line is generalized and links the [verification set](../process.md#verification); commands are not inlined in the skill.
- **2026-09-09, user, binding on the install script:** the host loader link **is a symlink, or the install stops and escalates**. No junction, no copy, no substitute of any kind when the platform refuses — a refusal is a human decision (Developer Mode, an elevated prompt, or a host that reads `.agents/skills` natively). Decided after I hit a privilege error during [the frost_map probe](../research/separation-probe-frost-map.md) and quietly substituted a junction, which is the move [the repair policy](../process.md#autonomy-and-repair) forbids. The mechanism is in [ADR-0003](../adr/0003-one-physical-home-for-skills-reached-by-link.md): nothing sees through a junction — `is_symlink()` is false, `rglob` walks in, and `git ls-files` lists everything beneath it twice, so the corpus every script shares double-counts. This holds whether or not the link is tracked.
- **2026-09-09, user: the tests move into `.agents/scripts/gw/test/` and ship with core.** Moving them off the root makes core a directory — `.agents/` plus two line-level parts in `AGENTS.md` — so a content hash over `.agents/` is very nearly the core revision the install script needs, which was impossible while half the declared parts lived at the root. They ship because they are declared parts, because a recipient cannot contribute a script change it cannot verify, and because [the probe](../research/separation-probe-frost-map.md) supplied the decisive case: 216 tests passing in frost_map is the only reason anyone knows the scripts survived the trip, so a recipient's first run of them is its arrival check. Whether they stay in a recipient's default verification set, given ~70s per `/verify`, is not settled here.
- **2026-09-09, the install script owns the loader links, and verifies what the host will load** — not only what it wrote. Evidence: [the probe](../research/separation-probe-frost-map.md).
- **2026-09-09, the probe's constraints on the install script**, from [the findings](../research/separation-probe-frost-map.md): core is not a directory (declared parts span `.agents/`, the tests, and two lines inside `AGENTS.md`); a parts-derived manifest would ship 3 skills of 22, so [.0050](./done/01-0011.0050-shape-checked.md)'s allowlist gates it; a commit tag cannot be the core revision because one commit touches both halves, so the identity is a content hash over the manifest and a tag is a label for it; a recipient needs a recorded pointer back to canonical source, because a script maintains only the tree it lives in; and the installer must localise `<project-local>` blocks, which today protect nothing because nothing replaces them.
- **2026-09-09, user:** install `/recall`, `/edge`, `/review-architecture` and `/setup-devops` now — "just copy them into skills for now" — mint tickets for their mechanism work, and delete `legacy/`. With this the selection's twenty working commands are all installed and **this ticket's install backlog is empty**; the five it had held are [01-0010.0105](./01-0010.0105-backlog-five-arrive.md)'s, and `/edge` closed [01-0010.0100](./01-0010.0100-remaining-named-corpus.md)'s first criterion. The rule that a `<project-local>` block is carried only for a fact that would differ elsewhere — decided below on 2026-09-06 and living only here since — reached Tier 1 in the same pass, at entry contract v7, because applying it to `/recall` meant reading it out of this ticket.
- **2026-09-09, user:** `legacy/skills` is deleted, reversing the 2026-09-05 decision below that kept the July corpus as evidence. New evidence for the reversal: its only two capabilities the harness had not installed were both superseded variants — including the `setup-project` metadata the selection explicitly rejects — [`file-matrix.csv`](../research/audit-2026-09-05/file-matrix.csv) retains all 22 files' hashes as corpus `H`, and the bytes remain in this repository's history. Its original source `D:\Dev\AI\.agents\skills` no longer exists, so that folder was the last working-tree copy; the three estates the selection actually drew from are all still on disk.
- **2026-09-06, user:** a skill carries `<project-local>` only when it has a fact that would differ in another project using this harness. Harness layout (`docs/tickets/`, `docs/rfc/`, `docs/spec/`, `docs/glossary.md`, the queue, naming) is shared; how to read an autonomy switch from `AGENTS.md` is shared. `/ticket`, `/spec`, `/plan`, `/verify`, and `/align` had none of those local facts; their blocks are removed. The `Pass` line was Forecast Collector's, not imported.

## Decisions this ticket's align owns

- Spec lifecycle: enduring decisions move to maintained governing documents, specs eventually become history. ~~Who owns maintenance and archiving?~~ **2026-09-05, user: `/maintain` owns all tree maintenance, all `/denoise` and `/sync-arch` responsibilities, and archiving.** It checks all mechanisms against their actual rules and can run at whole-tree, project or RFC scope. Current policy: [tree maintenance](../../.agents/mechanisms/maintain/maintain.md). Exact lifecycle state and implementation design remain open.
- Issue capture, routing, decomposition and pace: define Tier 1 natural-language triggers, an owner for initially unowned issues, and feedback to earlier stages. The user's `/step` and `/decompose` examples are alternatives to assess, not selected new skills. **2026-09-06, user:** the loop's sequence and the scoping of work are the pacer's concern; [`docs/process.md`](../process.md) is marked preliminary and the pacer is expected to own it; each step's rules move into the step's skill as it is installed. The pacer's core rules are Tier 1: they say what the agent does after `/recall` and what one turn's reply is scoped to. Their content is under alignment in [pacer.md](../pacer.md); the ticket is [01-0020](./01-0020-pacer.md).
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

**Evidence rechecked 2026-09-05:** all 99 audited files across M, A and F still match the audit's SHA-256 values. Source repository heads observed: M `6320d3c805dffe63d7bccd86d5874c624a78de38`, F `dd847b5f1720c36d695d287f8a67630f09bbfa20`, A `810edb2692ba59672d9e4ebacd7f5504648ffed0`. The [inventory](../research/audit-2026-09-05/inventory.json) owns exact per-file identities. A has an unrelated untracked script document; it is not part of this selection.

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

Decided in [01-0010.0020](./done/01-0010.0020-live-alignment-across-hosts.md) on 2026-09-05; each lands with the skill it names.

- `/impact` gains a shape recommendation in its output: spec, ticket or RFC, or re-slice. The root entry file already states this intent.
- `/commit`, and any skill that gates on permission, reads the autonomy switches from the entry file's local block instead of carrying its own absolute rule.
- `/skill-up` documents `<temporary until="...">` alongside `<project-local>`.
- `/maintain` enumerates `<temporary>` statements in scope and removes the ones whose condition holds.
- `/ticket` and `/plan` call `/impact` where the entry file says they do.
- A skill install omits `<project-local>` unless that skill has a project-specific fact. Do not restate harness paths or switch lookups there.

## First bootstrap delivery ticket — proposed breakdown

**Status:** ~~Proposed for the user's granularity review.~~ **Accepted and minted 2026-09-05 as [01-0010.0020](./done/01-0010.0020-live-alignment-across-hosts.md); its root decision is resolved there.** This is the output of the requested `/ticket` pass, using M's selected ticket skill and format plus F's impact step.

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

## Second bootstrap delivery — 2026-09-06

**Status:** ~~Five-slice ring-then-spec, awaiting approval.~~ **Minted as [01-0010.0035](./done/01-0010.0035-install-spec.md).** Spec-first and loop completion are one path; `/plan` is planned by reading `/plan`.

### Impact

**Main blast radius.** One child: install `/spec` and use it once on the existing harness spec so that spec requires completing the delivery ring here. Catalog, `AGENTS.md` installed-list, and `.agents/README.md` change when that ticket is implemented. `/ticket` → `/plan` → `/implement` → `/verify` → `/maintain` for the ring skills are sliced from that spec, not from this pass.

**Hidden edges.** The draft at `docs/spec/01-0010-dev-harness-shared-and-local.md` already exists; first use develops it, it does not start a second spec. Source `to-spec` still says `/to-tickets` and `docs/` — those names are this install's adaptations. [01-0020](./01-0020-pacer.md) stays Planned.

**Leave alone.** `/plan`, `/implement`, `/verify`, `/maintain` files; pacer runtime; `/edge`; local-override mechanism; `/impact`'s still-owed shape recommendation; source projects.

**Recommendation.** Proceed. One slice, position `0035`.

1. **Title:** Install `/spec`.
   **Interaction:** HITL.
   **Depends on:** [01-0010.0030](./done/01-0010.0030-install-ticket.md) minting this breakdown; [01-0010.0020](./done/01-0010.0020-live-alignment-across-hosts.md) for the entry path.
   **Parent scope covered:** `/spec` from the selection table; spec-first; loop completion as spec content.
   **Basename:** `01-0010.0035-install-spec.md`.

## Third bootstrap delivery — 2026-09-06

**Status:** Approved by the user and minted. Three children here; four sibling rule refactors were
minted at root, outside this ticket, and are not its children.

### Impact

**Main blast radius.** Three children of this ticket — `/impact`'s owed shape recommendation
(`0080`), `/discover`'s standing and install (`0090`), and the five named remaining commands
(`0100`). The four rule refactors — hierarchy, scope, responsibility, reachability — consolidate
statements that live inside this ticket's corpus but answer to a different contract: coherence of
the method's own concepts, not distribution of a canonical harness across projects. They sit at
root on [the pacer's](./01-0020-pacer.md) precedent.

**Hidden edges.** `/discover` was installed and named in the entry file while sitting outside this
ticket's accepted 21-capability selection, and that inconsistency was live from the moment it
appeared. `0090` settled it on 2026-09-06: the selection records what was taken from the three
audited estates and is not the roster of what is installed, so `/discover` was never a missing
22nd row. It is installed on `0090`'s own authority and listed in the catalog.
`/impact` is touched twice — `0080` lands its owed output, and the responsibility refactor may later
move investigation rules into it — so `0080` runs first. Hierarchy and scope share eight of nine
files and must run sequentially. `/maintain`'s Edge-record and concern-index checks reference
`docs/edge/` and `docs/concerns.md`, neither of which exists here; that is `0100`'s to settle.
Correct ownership does not produce arrival: the `/ticket`→`/impact` chain was correctly owned and
still failed to reach an in-progress `/align` on 2026-09-06, which is why responsibility and
reachability are separate refactors rather than one.

**Leave alone.** [01-0020](./01-0020-pacer.md) and its `<temporary>` block. The
[01-0010.0070](./done/01-0010.0070-install-maintain.md) close, which needs only its fresh-session
observation. The audit corpus and `legacy/skills`. The five selected commands nobody named —
`/conclude`, `/recall`, `/dream`, `/review-architecture`, `/setup-devops` — which stay in this
ticket's backlog. The selection's 21 rows; `0090` questions membership, not their contents.

**Recommendation.** Proceed. Seven slices, none too thick to verify alone, none a horizontal layer.
Re-ordered from the draft: `0080` first; hierarchy then scope, strictly sequential; the earlier
"wire the two passes into shape-handling skills" slice dissolved into reachability.

1. **Title:** `/impact` recommends the work's shape. **Interaction:** HITL.
   **Depends on:** nothing. **Parent scope covered:** first owed core change.
   **Basename:** `01-0010.0080-impact-work-shape.md`.
2. **Title:** Install `/discover`. **Interaction:** HITL, decision-bearing.
   **Depends on:** nothing. **Parent scope covered:** corpus membership and installation.
   **Basename:** `01-0010.0090-install-discover.md`.
3. **Title:** The remaining named corpus arrives. **Interaction:** HITL, decision-bearing.
   **Depends on:** the responsibility refactor. **Parent scope covered:** five of ten remaining
   commands; three of six owed core changes.
   **Basename:** `01-0010.0100-remaining-named-corpus.md`.

## Separation delivery — 2026-09-09

**Status:** Approved by the user and minted as
[01-0010.0130](./done/01-0010.0130-harness-installs-into-another-tree.md). One decision-bearing child,
aligned together with [01-0010.0110](./done/01-0010.0110-project-facets-injected.md) on the user's
direction.

### Impact — 2026-09-09

**Main blast radius.** `AGENTS.md`'s *Core and instance*, whose `<straw-dog>` exemption is granted
because a dog "is bound to a ticket and expires" — true here, false in every recipient, and tier 1
either way. [MECHANISM-FORMAT](../../.agents/skills/mechanism/MECHANISM-FORMAT.md)'s mandated
`not yet` markdown link and the `mechanisms.py` that enforces it.
[TICKET-FORMAT](../../.agents/skills/ticket/TICKET-FORMAT.md) and `tickets.py`, which demand
`Status`, `Type` and a `/verify` box in-file and so require a recipient to keep delivery state
twice. Every script's `root = parents[2]` with no CLI override. `docs/architecture.md`'s *Deferred
decisions*, which parks cross-project distribution with "existing owners". **Must verify:** every
bare `docs/` reference in a core skill — `/verify` ×3, `/implement` ×1, `/align`, `/edge`, `/spec`,
`/setup-devops`, `/skill-up`.

**Hidden edges.** `docs/concerns.md` does not exist in this tree, yet `/align` calls it "this
skill's artifact" and `/edge` points into it — core referencing a missing instance document *at
home*, not only in a recipient. [01-0010.0120](./01-0010.0120-host-delivery-surfaces.md) is the
loader seam from the other side and blocks three tickets, so link and surface must be cut apart or
two tickets decide one thing. The `.0050` dependency is partial: the allowlist gates *what ships*
and nothing else, so it constrains one question rather than the ticket. The entry contract has no
installer and no declared home, which puts the retirement of its hand-bumped version inside this
scope rather than beside it. And this tree cannot grade any of it — it is the configuration that
hid all 28 defects for twelve sessions.

**Leave alone.** The injector contract in [architecture.md](../architecture.md#installed-blocks),
the one part that made the trip intact. The tests-ship decision and the suite's location, settled
2026-09-09. The symlink-or-stop rule, already binding. `docs/`-substituted-whole: ADR-0001 and
ADR-0002 were stressed by the probe and held — what failed was enforcement, not the rule.

**Recommendation.** Narrow, not split — adopted. One decision-bearing slice at position `0130`,
with the loader *surface* cut out to `.0120`, `.0050` recorded as a constraint on the manifest
question rather than as a blocker, and the align forbidden from settling whether "install" is one
mechanism or three until a second tree supplies the shape.

1. **Title:** The harness installs into a tree that is not its own.
   **Interaction:** HITL, decision-bearing.
   **Depends on:** nothing blocking; co-aligned with `01-0010.0110`, constrained by `01-0011.0050`.
   **Parent scope covered:** cross-project distribution, and the install constraints recorded at
   [Resolutions and constraints](#resolutions-and-constraints), 2026-09-09.
   **Basename:** `01-0010.0130-harness-installs-into-another-tree.md`.

## Discover — the premise, 2026-09-10

Run on the user's direction over the whole repository premise, not over one slice. Filed as it came
back, per [`/discover`](../../.agents/skills/discover/SKILL.md): material, never a verdict, and
never the reason to change something. What it names is a candidate for this case, not a finding
about it.

**Isolation was imperfect and the material must be read knowing it.** The pass was tasked not to
read this repository and read no file, but it opened its reply with this project's entry-contract
line — so the project instructions reached it automatically, as they reach any subagent here.
`/discover`'s method assumes a separate process is an uncontaminated one; in this harness it is not.
The pass also caught the smuggling from the other side, unprompted, at *"the epistemic sorting rule
was supplied with the question"*.

**What was transmitted**, stated as the skill requires: the shape was described functionally in
eight properties with no house vocabulary — no file names, no rule ids, no local record names. The
framing that could not be withheld: that the port's defect batch was *"nearly all of one kind"*, and
that nothing had detected it because references resolve at origin. The pass names both as smuggled,
below.

### Families

#### A. Software product lines: core asset base and product derivation

**Mapping.** Canonical location = core asset base. Recipient codebases = products. Locally-adapted
blocks = variation points bound at instantiation. Copying out = product derivation (here manual).
Origin story (distilled from a few projects) = *extractive/reactive* adoption — harvesting a
platform out of existing products rather than designing one up front. Defect batch = variation
points that were never made explicit, silently binding to the origin's values.

**Ladder.** (0) independent projects → (1) clone-and-own → (2) extracted platform with informal
conventions → (3) explicit variability model plus derivation tooling → (4) automated derivation with
round-trip. **Placement: 2, one derivation attempted.** Confidence: high that this ladder is the
family's own; high on placement given the description.

**Known failures** [general / living tradition]:
- Extractive adoption stalls at the *second* product, because the variability the second product
  reveals is structural, not parametric — it can't be absorbed by parameters or flags. Confidence:
  high.
- The asset base drifts toward the union of everything any product needed (the "150 % problem"):
  every recipient carries what no recipient wants. Confidence: high.
- Clone-and-own is genuinely cheaper than a platform at n=2 and becomes lethal somewhere around
  n=4–6; the crossover is real, the number is folklore. Confidence: high on the shape, low on the
  number.

**What this family predicts about the recent port.** The batch is the mechanism working, not
failing. The error would be to fix the 35 items; the move is to read a variability model out of them
— each defect names a thing that must become a declared, bindable point.

#### B. Vendoring and fork management: upstream, downstream, patch queue

**Mapping.** Canonical = upstream. Recipient = a vendored copy. Local adaptation = a patch queue.
"Receive later changes without losing local parts" = rebase or three-way merge of upstream changes
over recorded local diffs. "Send improvements back" = upstreaming.

**Ladder.** (0) copy-paste → (1) copy plus a *recorded* local diff → (2) template with a recorded
answers/adaptation file and a machine update path → (3) a real dependency with extension points and
no local edits at all. **Placement: 1, aiming at 2.** Confidence: high.

**What works** [recent, comparable substrate — text-and-config templates copied into unrelated
repos]: the working shape in this space is a template plus a per-recipient *answers file* plus an
`update` command that three-way-merges upstream changes over local edits (copier is the clearest
instance; cookiecutter, with no update path, is the standard cautionary case; subtree/submodule
solve a different problem — whole-tree, no local edits). The transferable move is making the
recipient's adaptations a first-class artifact *separate from the copied text*, so an update is a
merge of two known things rather than an archaeology of one. Confidence: medium-high, and this is
the most directly liftable item in the pass.

**Known failures** [general / living]:
- Patch rot: local modifications decay against upstream drift, discovered only at update time.
  Confidence: high.
- "We'll upstream it later" does not happen unless unupstreamed local patches are tracked as debt
  with an owner. Confidence: high (Debian, Chromium, every long-lived vendoring shop).
- Asymmetry: upstream cannot see downstream's breakage, so upstream's confidence about portability
  is structurally unfounded. Confidence: high.

**Disagrees with A**: says do not build a platform at n=2; put the investment into the merge path and
let the forks diverge.

#### C. Modules, linkage, and hermetic inputs

**Mapping.** The portable body = a compilation unit. References that resolve only at origin =
dynamically-scoped names, or undeclared build inputs. Layered loading = lazy loading.
Authored-once fragments copied in = macro expansion, with the copy-checker as a hygiene/staleness
check. The port's defect batch = link errors deferred until the first environment that lacks the
ambient definitions.

**Two rungs, two remedies, in tension.** (i) Declare an interface and fail closed when a name is
unresolved — lexical scope, explicit imports, strict-deps. (ii) Remove ambient resolution so the
*origin* cannot resolve them either — sandbox, chroot, hermetic build. **Placement: below both.**
What exists is a prohibition ("the portable half may not reference the instance half") with no
environment in which violating it is visible. Confidence: high, given property 8 as described.

**Known failures** [general / living]:
- A prohibition the origin environment cannot violate *visibly* is not enforced by review; the class
  recurs at every new recipient. Confidence: high.
- The fix is not a better linter but a build where origin equals recipient: copy the portable half
  alone into an empty tree and run every checker there. Anything that resolves only because the
  neighbouring tree was present now fails at home, on every change, not on every port. Confidence:
  high — this is the single most actionable claim in this pass.
- Dynamic scoping was abandoned for precisely this failure mode, and that abandonment is one of the
  more settled results in language design. Confidence: high.

#### D. Structured authoring and single-sourcing

**Mapping.** Fragments authored once and mechanically placed = content references (DITA `conref`,
Antora partials, Sphinx includes), with an integrity check that refuses to build on a broken or
stale reference. Temporary content bound to a replacement condition = a status attribute with a
review trigger. Local adaptation without forking = specialization. Layered instruction =
progressive disclosure in help systems.

**Ladder.** copy-paste prose → marked includes plus a link/staleness checker → keyed references and
conditional profiling → specialization with round-trip. **Placement: 2.** Confidence: high.

**Known failures** [general / living]:
- A byte-equality check proves the copy *matches*; it never proves the fragment is *right where it
  landed*. Context-dependent fragments break silently at the point of use, and the check reports
  green. Confidence: high — this is the standard critique of aggressive conref.
- Reuse pressure pushes fragments toward context-free phrasing, which makes them abstract, hedged,
  and less usable at every site. The trade is real and not avoidable by tooling. Confidence:
  medium-high.
- Over-reuse yields prose that cannot be read at the source (it is a skeleton) and cannot be edited
  at the destination (it is not yours). Confidence: high.
- "Removable without trace" is a property of the marker, not of the content; the markers themselves
  become merge conflict sites in every recipient. Confidence: medium.

**Disagrees with H**: this family wants copies minimized; H says the copy at the point of use is the
only reason the reader complies.

#### E. Standards bodies: normative core, deviations, conformance

**Mapping.** Canonical body = normative text. Recipients = implementations/adoptions carrying
declared deviations. Local blocks = national deviations or profiles. Automated checkers = a
conformance suite. Self-hosting = the amendment procedure living inside the standard. Temporary
content with a replacement condition = a sunset or deprecation clause naming a successor.

**Ladder.** guidance → normative text → normative plus conformance suite → advancement gated on
independent interoperable implementations. **Placement: 2 going on 3.** Confidence: medium-high.

**Key claim** [general / living, high confidence]: the IETF has long gated a specification's
advancement on *two independent, interoperable implementations* (the RFC 2026 lineage), for exactly
the reason at issue here — one implementation cannot distinguish the specification from its own
accidents. This shape has just produced its second implementation and discovered 35 accidents. The
institutional form of that lesson is a rule: nothing enters the portable core until two unrelated
recipients have exercised it.

**Known failures**: without a suite, dialects form and "compliant" stops meaning anything (high);
profiles proliferate until the core is a shell (medium-high); the reference implementation quietly
becomes the real specification and the text becomes commentary (high).

#### F. Methodology definition and tailoring

**Mapping.** Canonical body = an organizational standard process. Recipient's copy = the project's
defined process. Local blocks = tailoring guidelines. Checkers = audit/appraisal. "Distilled from
how a few projects actually worked" = best-practice harvesting.

**Ladder.** This family's ladder is literally a maturity model: ad hoc → project-defined →
organization-standard with tailoring → *measured* → optimizing. **Placement: 3, with no measurement
rung anywhere in the description** — nothing described observes whether following the procedure
improves any outcome. Confidence: high on placement, since the shape is described entirely by its
internal structure.

**Known failures** [general / living]:
- Documented process diverges from enacted process; audits inspect the document. Confidence: high.
- Process work is self-sustaining, because producing procedure is easier to evidence than producing
  outcomes. Confidence: high, and property 5 (self-hosting) is an accelerant, not a safeguard.
- Harvested practices don't transfer, because what carried them was the people and the situation,
  not the text; the argument that methodology is necessarily per-team and varies with team size and
  criticality (Cockburn's) remains cited and, to my knowledge, unrefuted. Confidence: medium-high.

**This family disagrees with the whole enterprise.** It predicts ceremonial adoption or quiet
abandonment in recipients, and says the portable artifact should be the *tailoring conversation*,
not the procedure text. One honest weakening: its central failure ("nobody reads the manual") is
substantially defused when the executing reader is an agent that actually re-reads the text every
session. That is a real disanalogy and it lowers my confidence in this family's prediction to
medium.

#### G. Constitutions: self-amendment, entrenchment, transplants

**Mapping.** Self-hosting = self-amendment; rules about rules are the family's *secondary rules*,
and the always-loaded entry text is a rule of recognition (which text is binding, and how you know).
Local blocks = reserved powers. Temporary content bound to a condition = a sunset clause. Structural
checkers = constitutional review. Distribution to unrelated codebases = a legal transplant.

**Ladder.** custom → written rules → written rules with an amendment procedure → plus a review body
→ plus entrenched provisions the amendment procedure cannot reach. **Placement: 3–4, with zero
entrenchment**: everything, including the procedure for changing procedure, is amendable by the same
route it governs. Confidence: high, since property 5 states this as design.

**Known** [general / living]:
- Self-amendment's paradox (Suber's treatment is the standard reference) is that a self-amending
  rule can be used to lower the bar for amending itself; the near-universal mitigation is
  entrenchment plus a higher bar on the amendment clause specifically. Confidence: high that this is
  the family's settled answer; medium that it bites at this scale.
- **The transplant effect**: transplanted codes perform poorly when adopted without local adaptation
  or local demand, and *receptivity of the recipient* predicts effectiveness better than the quality
  of the origin text (Watson's transplants literature; Berkowitz/Pistor/Richard's counter-result).
  Confidence: high that this is a real, cited finding. Applied here: the 35 defects are the shallow
  problem. The deep one is that a recipient with no demand for the imported procedure keeps it as
  dead text — and the remedy (adaptation *by the recipient*, on its own terms) is in direct tension
  with a canonical upstream that expects improvements sent home.

#### H. Context engineering for agent instruction

The only family here with recent evidence on comparable substrate.

**Mapping.** Layered loading by when-needed = progressive disclosure under a context budget.
Fragments copied to the point of use = restating a rule where the action happens, because the
reader's attention is positional rather than indexical. Structural checkers = the syntactic half of
an eval suite. The person's checkpoints = human-in-the-loop gates.

**Ladder.** one long prompt → sectioned → loaded on demand by activity → *adherence measured against
a suite* → text edited on that evidence, including deletions. **Placement: 3, with nothing described
at rung 4.** Confidence: high on placement.

**What works** [recent, comparable substrate; my knowledge runs to mid-2026 and this area moves
fast]: on-demand loading keyed to activity is the current mainstream design and is the right call.
Adherence degrades as the always-loaded body grows, rules that never fire still cost attention, and
a rule stated once far from its point of use is followed less reliably than the same rule restated
where it applies. Confidence: medium-high on the phenomena, low on any magnitude. This family is the
one that *endorses* the duplication in property 4, and for a reason the DRY families cannot offer:
the copy exists for the reader's attention, not the author's convenience — which means the checker
should be verifying that the copy still *fits its site*, not only that it still matches.

**Known failures** [general, medium confidence — this family is young and I am not going to pretend
otherwise]:
- These bodies grow monotonically: every incident adds a rule, nothing removes one, and the
  always-loaded portion crowds out the task. Without a deletion mechanism tied to evidence, entropy
  wins.
- Conflicting rules do not raise errors; they are arbitrated silently by salience and recency. The
  structural checkers described catch a declared-but-missing part and a duplicated authority claim —
  syntactic conflicts. They cannot catch two rules that are individually satisfiable and jointly
  steer behavior somewhere neither intended.

### What the tasking smuggled in

- **The failure is pre-diagnosed as a detection gap.** "Nothing had detected this, because in the
  original location those references resolve" invites me to supply a detector. Families C and A both
  say the diagnosis is upstream of detection: C says the origin's environment is wrong (make it fail
  at home), A says the separation was never designed (the references aren't defects, they're
  undeclared variability). You get a linter if you take the framing at face value.
- **"Maturity ladder" presupposes the shape is on a path.** Asking each family to place the shape on
  a ladder makes every family answer "immature, here's the next rung" — and structurally excludes
  the answer "this genus does not work; do something else." F and G give versions of that answer
  only because I forced them to.
- **The provenance is doing legitimating work that the description never audits.** "Distilled from
  how a few particular projects actually worked" is presented as a strength. It is n≈3, no
  counterfactual, no control, and total survivorship: you saw the projects that worked. Every family
  that knows about harvesting (A, F) treats that exact origin as the risk, not the credential.
- **"Nearly all of one kind"** invites treating 35 defects as one solvable class. Batches described
  that way usually decompose on inspection into three or four classes with different fixes, and the
  single-class framing gets you one fix that closes 60 % of them and a false sense that the port
  problem is solved.
- **The no-reading rule cuts both ways.** It protects the outside view, and it also means I cannot
  verify a single one of the eight properties. I am reasoning about a *self-description* — the same
  class of artifact whose accuracy just failed empirically in the port. My families are fitted to
  the author's already-translated vocabulary, which is the author's model of the shape, not the
  shape.
- **The epistemic sorting rule was supplied with the question.** "Recent for what works, longevity
  for how things behave" is this project's own principle handed to me as an output constraint. Even
  the outside view arrives pre-shaped by the inside, and I sorted my claims into bins I did not
  choose.
- **Absent entirely, which is itself the finding**: who reads this and how many of them; what it
  costs to maintain; whether any recipient asked for it; and any measure of whether following the
  procedure improves outcomes. The shape is described exclusively in terms of internal structure.
  Combined with property 5 (the procedure maintains itself), that is the standard signature of a
  system whose primary output has become more of itself. Family F names this as its central failure
  and I do not think the description gives grounds to rule it out.
- **The substrate is mentioned once and then dropped.** "An autonomous agent working alongside a
  person" appears in the first sentence; all eight properties afterward are about documents. If the
  determining fact is that the reader has no persistent memory and re-reads text every session, then
  the document-engineering families (A–E) are borrowed clothes and H is the only one talking about
  the actual machine. I cannot tell from here which it is, and neither the description nor the
  tasking treats it as an open question.

### Nothing to take

Refused for want of a statable mapping:

- **Knowledge management / organizational learning** (tacit-to-explicit conversion, communities of
  practice). Subject-matter neighbour with no correspondent for the copy-checker, the derivation
  step, or the port defects. Refused.
- **Memetics and biological replication** (canonical genome, copies, mutation, fidelity). The words
  map; nothing about the mapping constrains any decision here. Refused.
- **Open-source project governance** (CONTRIBUTING, RFC processes, maintainership). Thin: it shares
  the contribution-flow half but has no core/instance distribution structure and nothing
  corresponding to properties 3, 4, or 7. Folded what was usable into B and E rather than listing
  it.
- **Canon-and-commentary traditions** (a fixed canonical text with local interpretive traditions).
  Tempting for property 2, but I cannot state what corresponds to the automated checkers or to the
  port defect batch without inventing it. Refused.
- **Internal developer platforms / golden-path templates** — not refused, but it is not an
  independent account; it is B's substrate with a different vocabulary, and I folded it in there.

And one genuine gap: I know of no body of work that studies the *combination* at issue — a
self-hosting procedural corpus, transcluded, ported between codebases, executed by an agent that
re-reads it each session. H is the nearest and it is a few years old. Anything I said about that
combination specifically is extrapolation from neighbouring families, and should be weighted
accordingly.

## Hermetic core delivery — 2026-09-10

**Status:** Minted as [01-0010.0140](./done/01-0010.0140-core-stands-alone.md) on the user's direction,
after `/advise` recommended the check and the probe below showed it is not a simple addition. One
decision-bearing child.

### Impact — 2026-09-10

Assessed inline from the probe rather than through a `/impact` pass, because the probe *is* the
blast-radius evidence: it enumerates every affected reference by file, line and class. Recorded
here so the child can point at it.

**Probe, 2026-09-10.** Over all 41 markdown files under `.agents/`, masking `<project-local>` and
`<straw-dog>` blocks: **74 references reach the instance half, of which 27 are the defect.** The
other 47 are inline path conventions — `docs/tickets/`, `docs/rfc/`, `docs/glossary.md`,
`docs/adr/`, `docs/sessions/`, `docs/spec/` — which *Core and instance* explicitly permits ("naming
a path convention the harness imposes is not a reference to a file"). The 27 are markdown links
that resolve to a *particular* document: **11** `not yet` referents in the three mechanisms'
parts tables, **11** prose links in the same three docs citing tickets and evidence, **3** in
`/verify` and **1** in `/implement` to `docs/process.md`, and **1** in `/discover`'s evidence
shelf. *(Corrected 2026-09-14: the first read-out said 22 of 74 with 13 and 5; the probe's own
output, re-run at the align commit and today, says 27 with 11 and 11. The total was right, the
split was misread.)*

**Main blast radius.** `AGENTS.md`'s *Core and instance* and
[ADR-0002](../adr/0002-core-may-not-depend-on-the-instance-half.md), which state the prohibition
this makes observable. [MECHANISM-FORMAT](../../.agents/skills/mechanism/MECHANISM-FORMAT.md),
which *mandates* the markdown-link form for a `not yet` referent and so mandates 11 of the 27 —
two core documents in direct contradiction, which is the finding, not a side effect. The project's
[verification set](../process.md#verification), which the check joins.

**Hidden edges.** The green half and the reporting half are separable and only the reporting half
is workable today: 13 findings wait on [01-0011.0050](./done/01-0011.0050-shape-checked.md)'s align,
which owns the referent's form, and the 5 grading links are candidates for `/maintain`'s R3 rather
than for this check. A naive rule — *nothing under `.agents/` may name a document under `docs/`* —
would fail a rule the mechanism format states on purpose: **evidence is instance-side by design**,
which is why the format puts the `evidence` bullet inside the `<project-local>` block. So the check
cannot be written before the exemption vocabulary exists, and no ticket owns that vocabulary today.
Running the scripts themselves in an `.agents`-only tree has the same shape: `mechanisms.py` cannot
pass there, and its failure would be reporting the intended design.

**Leave alone.** The 47 path conventions. The `<project-local>` and `<straw-dog>` exemptions
themselves, which are [01-0010.0110](./done/01-0010.0110-project-facets-injected.md)'s and
[01-0010.0130](./done/01-0010.0130-harness-installs-into-another-tree.md)'s. The four
`docs/process.md` links are repairable today by `/maintain`'s own precedent — it wraps its three in
a `<project-local>` block — but they are left for this ticket so the check and its repairs land
together and the check is what proves the repair.

**Recommendation.** Narrow, one ticket, no split. Splitting the exemption decision from its only
enforcement would leave the decision with nothing that observes it, which is the exact failure the
ticket exists to end.

1. **Title:** Core stands alone, and a check says so at home.
   **Interaction:** HITL, decision-bearing — the exemption vocabulary is a decision.
   **Depends on:** nothing blocking; constrained by `01-0011.0050` on 11 of the 27 findings.
   **Parent scope covered:** acceptance criterion 7, maintenance identifying drift without
   treating silence as success.
   **Basename:** `01-0010.0140-core-stands-alone.md`.

## Existing-tree delivery — 2026-09-21

**Status:** Minted as [01-0010.0150](./01-0010.0150-harness-meets-a-tree-with-a-method.md) on the
user's direction, the evening [01-0010.0130](./done/01-0010.0130-harness-installs-into-another-tree.md)
closed on its frost_map grade. One slice.

### Impact — 2026-09-21

Run by `/ticket` on the one-slice draft: **proceed.** The install as landed knows how to refuse a
tree that already has a method — its own entry file, a stub with content, skill directories, an
`.agents/` of another convention — and not how to meet one: the refusal names the first thing in
the way and nothing of what was found, the skill's flow ends at *populate the local file* with
no step for what the tree already says, and the front page duplicates the skill's flow. Blast
radius is `harness.py`'s refusals and one stamped line, the `/harness` skill, the root README,
and the mechanism's doc; the scripts' contracts, the injector, the shear and the gate are
untouched. Hidden edge: the repository's URL lives in the script alone and the skill does not
name it, so an agent in a recipient cannot see where its core comes from without reading code —
the slice moves the one home into the skill and has the script derive from it. Leave alone:
what the install deletes, which stays nothing of the project's. No generalisation: the
inventory reports the four places the install already refuses on; the flow is instruction, and
the judgment stays the agent's under it. A stranger harness is not a second design, it is the
same refusal with more in the inventory.

### Impact on the split — 2026-09-21, at `.0150`'s `/plan`

Run by `/ticket` on the three-slice split the user directed the same day: **proceed, and narrow
`.0150` by one seam.** [01-0010.0145](./done/01-0010.0145-core-scripts-under-one-directory.md) (AFK):
core's scripts under one directory of their own — five root computations one level deeper, the
gate's path, the parts tables, every live command and citation; archived records keep the old
path. Hidden edge: it is the first edge change with a real recipient behind it — frost_map's
local verification set names the old paths, and its `--update` will delete them and say nothing
about the set — which is the first strike for
[01-0010.0160](./01-0010.0160-harness-edge-changes-reach-an-update.md) (HITL, decision-bearing):
a mechanism owning what the product is, what its installation edge is and how a change to it is
extracted, whose collected changes an update reads as a migration; its first question is where
a change lives so that it ships, since `docs/edge/` is the instance half's and a painted door
nobody declares. [01-0010.0155](./done/01-0010.0155-a-tree-names-the-repository-its-core-comes-from.md)
(AFK) carved out of `.0150`: the repository line has its own comparison rule, its own subprocess
proof, and the stranger-tree grade does not exercise it. `.0150` keeps the inventory, the flow
and the README, one HITL slice with one grade. Order: `.0145` → `.0150` → `.0155` any time after
`.0145` → `.0160`, its align fed by `.0145`'s update into frost_map. Leave alone: the manifest,
the shear, the stamp, the gate; the architecture's refusal sentence; the ticket mechanism's
meet-block (its own align, on [01-0017.0020](./01-0017.0020-practice-swaps-in-one-edit.md)); the
loop's switchability ([01-0020](./01-0020-pacer.md)).

## Arrival-to-ready — 2026-09-23

**Status:** Minted as four slices, `.0165` → `.0170` → `.0175` → `.0180`, at the align of
2026-09-23. The customer is ai-game-1, installed at `goodwolf-harness@47516ce`: one commit, no
remote, six documents, no code. Its verification set came out holding core's own gates and
nothing of the project's, its painted doors were never created, and the install's last step ran
before the project had a toolchain to read. Nine decisions landed at that align — the sequence
(install+gate → L1/L2 → setup → quicklook → L3 → inject → check); doors created by the install
with `docs/tickets/README.md` carrying an arrival state; one fixed quicklook whose admission
scales rather than its effort, with *unread* distinct from *deferred*; harness owning every
moment, `setup-devops` relied-on; the local file's extraction split so the switches precede the
step they authorise; `git init` a refusal bullet and a remote offered, never created; and L3 a
pointer to `docs/cicd.md` with core's gates additive only.

### Impact — 2026-09-23

Run by `/ticket` on the four-slice draft: **proceed on 1, 2 and 4; narrow 3.** Blast radius is
`harness.py`'s post-gate writes, the `/harness` skill's last step, the mechanism's doc — five
Moments rows, a parts row, and *What it produces* — `ARCH-FORMAT` and `GLOSSARY-FORMAT`, and one
clause of `setup-devops`. The manifest, the shear, the stamp, the announce line, the gate's three
checks and `--check`'s comparison are untouched. Hidden edges: the painted-door list would gain a
second home, since [mechanisms.py](../../.agents/scripts/gw/mechanisms.py) already holds it by
hand for the leak check, and two copies is *every fact to one home* broken where neither copy can
detect the drift; creating doors is a write, so it must follow the gate or *every refusal writes
nothing* stops being true; and **unread** collides with `/maintain`'s *docs to their
implementation, both ways*, since a skeletal record disagrees with the code by construction and
the repair maintain would attempt is the quicklook itself. Narrowed for one shape: the
quicklook's read-the-codebase recipe has **zero** cases — frost_map arrived already described and
ai-game-1 has no code — so `.0175` takes only the prose-sourced half, which also defers the
maintain collision. Leave alone: `setup-devops`'s declaration status, since pulling it in imports
[01-0017](./01-0017-io-graph-coherent.md); collisions with a tree's existing `docs/`, which are
[01-0010.0150](./01-0010.0150-harness-meets-a-tree-with-a-method.md)'s.

## Front page — 2026-09-26

**Status:** Minted as three slices at the front-page align of 2026-09-26, on the user's approval:
[`.0125`](./01-0010.0125-the-host-blocks-what-a-rule-forbids.md) (hooks),
[`.0200`](./01-0010.0200-a-project-can-remove-the-harness.md) (uninstall) and
[`.0167`](./done/01-0010.0167-the-front-page-says-what-the-harness-is.md) (the front page), whose
license has one home at the repository root and is copied into every install *(the user)*. The page's content was settled there — title, the two opening
paragraphs, *How it works*, *What holds it together*, *Where it stands* with its not-yet list
wrapped as straw dogs, *Use it* — and tested on cold readers; the evidence is the
[front-page review](../research/external-review-front-page.md) and the
[discovery passes](../research/discover-what-this-is.md). Two of the not-yet items had no ticket
behind them, and the user minted each: the host blocking an action a rule forbids, and removing
the harness from a project.

### Impact — 2026-09-26

Run by `/ticket` on the three-slice draft: **proceed on all three, minted hooks → uninstall →
front page**, because the page's straw dogs bind to the other two. Blast radius of the front page:
the root README and a root LICENSE; [01-0010.0150](./01-0010.0150-harness-meets-a-tree-with-a-method.md)'s
README bullet and its criterion, which this slice now owns; and `/maintain`'s **T1**, whose
straw-dog listing names `docs AGENTS.md local.rules.md .agents` and not the root README — so the
page's own claim that *a script lists every one* would be false of its own examples. Of hooks:
[01-0010.0120](./01-0010.0120-host-delivery-surfaces.md) decides whether the harness takes a
dynamic host surface at all, and a hook is one, so it depends on that decision; the hook's
configuration lives in a file a project often already owns, the collision class `.0150` handles;
and each host hooks differently. Of uninstall: a new `harness.py` mode whose removal set is what
the announced ref shipped plus the loader links, leaving the local file and everything under
`docs/`, and refusing over an edited core file as an update does. Hidden edges: statements that
the harness has no hooks — the mechanism shape's doc and its spec — become text a live ticket will
change and are wrapped in the minting pass; the root LICENSE and `.agents/LICENSE` are one text in
two places with nothing checking they agree; the README quotes live facts (the switch line, an
installed block) that no check reads; and an uninstall after `.0150` must undo what `.0150` carried
into core, so whichever lands second owes the other a case. Leave alone: the harness doc's *the
README is not a part*; `.0190`'s published front page; the manifest, which no root file joins.

## Adoption shortlist — recommendations awaiting alignment

This is the compact decision surface extracted from the [Life research](../research/life-harness-findings.md). Rows marked agreed link to the current policy; the other recommendations remain undecided. Resolve one question at a time.

| Order | Decision | Recommendation |
|---|---|---|
| 1 | Does the loop need a spec, including for this job? | **Agreed:** substantial work uses a spec, including this harness; small fixes can start at a ticket. `/align` spans the whole loop. The spec content itself remains to be aligned. |
| 1a | What does each HITL checkpoint require? | **Agreed:** [autonomy and repair policy](../process.md#autonomy-and-repair). Repair-and-report within its conditions; otherwise align. **Remaining implementation:** route this consistently across skills, reconcile existing checkpoint wording, and verify delivery. `/impact` is a candidate assessment procedure, not a mechanical certificate. |
| 2 | How should mechanisms govern skills and maintain themselves? | **Agreed:** [mechanisms and skills](../../.agents/glossary.md) and [tree maintenance](../../.agents/mechanisms/maintain/maintain.md). `/maintain` covers all applicable mechanisms and owns all `/denoise` and `/sync-arch` responsibilities, including archiving. **Remaining design:** exact boundaries, document layout, maintenance triggers, scope derivation and automation. |
| 3 | Where do current rules, decisions and evolution live? | **Agreed:** [current documents and evidence](../../.agents/skills/mechanism/SKILL.md#three-homes-and-the-chain), including one evidence/evolution record per mechanism, created when needed. |
| 4 | Should tickets, RFCs, specs, concerns and ideas all be queues? | Share a minimal lifecycle contract for actual queues: entry, owner/consumer, disposition, exit and maintenance. Decide which artifacts really need queues; specs and RFCs can be documents attached to work without independent backlogs. |
| 5 | Which queue machinery should be adopted? | Start with file/index consistency, explicit unresolved decisions, actionable stale/unknown state and evidence-based closure. Consider strikes as recurrence evidence on the affected work item; do not copy Life's entire counters, quotas or scheduling policy. |
| 6 | How should delivery and drift be maintained? | **Agreed:** [mechanical maintenance](../../.agents/skills/mechanism/SKILL.md#mechanical-by-construction), including history, missing repair scripts and mechanisms designed for derivation. **Remaining design:** dependency representation, change tracking, scheduling and verification across projects and hosts. Separate installation freshness from derived-work correctness and live instruction delivery. |

**Open, 2026-09-06 — `/dream`'s standing.** The entry file names `/dream` in its Helpers list and
describes it as experimental, while the [selection table](#bootstrap-corpus-selection) says to
retain it for deliberate use with its daily scheduling trigger treated as a source policy to
review. It is not installed. Nothing has decided whether "experimental" is this project's position,
whether an uninstalled skill belongs in the entry file at all, or which ticket installs it. It stays
here with `/conclude`, `/recall`, `/review-architecture` and `/setup-devops` — the selected commands
[01-0010.0100](./01-0010.0100-remaining-named-corpus.md) does not cover.

The autonomy/repair policy, mechanism concept, current/history separation and mechanical maintenance principle are agreed. Queue design (items 4–5) and the concrete maintenance design remain open. The spec as a whole and any implementation RFC remain unapproved; accepted decisions and command names are recorded above.

## Idea — pacer

→ [Pacer](../pacer.md). Moved to its own document at the user's request, 2026-09-05. The delivery ticket is [01-0020](./01-0020-pacer.md), not a child of this one.

## Derived work — Life basis and scope decision

Life already supplies the dependency rule; it should be adapted rather than independently reinvented:

- [`/mechanism`, Amend](D:/Dev/AI/life/.agents/skills/mechanism/SKILL.md): derive every reliance, recheck both ends, and treat what the change makes stale as part of the change.
- [`/maintain`, Pipeline](D:/Dev/AI/life/.agents/skills/maintain/SKILL.md): governing mechanism instructions → instance doc/rules → records. Repair upstream first, then downstream; move only the verification marks actually reached.
- [Maintenance mechanism](D:/Dev/AI/life/mechanisms/maintenance/maintenance.doc.md): changed governing versions create persistent maintenance due state. Installation freshness and output verification are separate facts. Phase A/research describes the implementation limits; hashes identify a change, not its semantic effect.

The dev-harness policy is now recorded in [mechanical maintenance](../../.agents/skills/mechanism/SKILL.md#mechanical-by-construction). Its scope includes affected tickets, RFCs, specs, docs, code, checks and historical records as appropriate. A wording-only change may require no downstream repair; a changed ticket contract may require a scripted migration of both open and completed tickets. The governing contract determines the repair; unknown historical facts remain unknown.

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
- [ ] `/verify` has been run on this ticket against its ticket, RFC, and governing docs.
  *(Added 2026-09-09 under repair-and-report: the shelf requires the box of every ticket, and
  this one was minted before the rule.)*

## Out of scope

Importing Life's public-forum operations, identity, private instance data or blanket autonomous rule-adoption policies. Those require separate intent and are not prerequisites for shared dev skills.
