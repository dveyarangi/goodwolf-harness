# Dev harness discrepancy audit — phase A

Verified 5 September 2026. **Analysis only: no skills, loader links, project configuration, or source repositories were changed.** The existing audit was retained; this report replaces its findings for decision-making.

**There is no single newest corpus.** Meteoscape is the strongest shared dev baseline. Forecast Collector has six later core changes. DriftSense `agents` has a concerns-format extraction plus initiative and Notion adaptations, but an older `skill-up` method. The current `D:\Dev\AI\.agents` collection is behind the other three in every shared skill body.

The requested future home, **`D:\Dev\AI\agents`, does not exist**. It is distinct from the existing **`D:\Dev\AI\.agents`**, where this audit lives. Nothing has been extracted into the future home.

## 1. Scope and evidence

Recursively inventoried `D:\Dev\AI` and `D:\Dev\DriftSense\workspace`, including hidden directories, without following links into duplicate trees. Excluded Git internals, dependencies, build output, caches and this audit's own output directory; the exact exclusion list is in the inventory. No traversal errors remained within that scope. Also inspected the four user-level skill locations under `C:\Users\fimar`.

Compared every file in eight physical corpora using SHA-256, decoded text with line endings normalized, and skill bodies with complete `<project-local>` blocks removed. Trailing whitespace was compared separately. Checked actual link targets, file identities and hardlink counts, Git tracking, relevant history, imports and hooks, skill metadata and relative prose links. No application tests or live sessions in the three frameworks were run; discovery conclusions distinguish documented behavior from inspected configuration.

Evidence:

- [Full file matrix, local blocks, core deltas, history and script diffs](./EVIDENCE.md)
- [Machine-readable inventory with full hashes, file IDs and per-file commits](./inventory.json)
- [CSV file comparison](./file-matrix.csv)
- [Snapshot and structural verification](./verification.json)
- Contextual diffs: [H → M](./H-to-M.diff), [M → A](./M-to-A.diff), [M → F](./M-to-F.diff), [A → F](./A-to-F.diff).

Dates below come from relevant Git commits when available. A copy/import date is not an improvement date. Filesystem timestamps and independent repository histories do not prove a copy lineage or a Git ancestor relationship.

## 2. Physical copies and loader links

| Key | Physical skill home | Skill entrypoints | All files | Latest skill-path commit |
|---|---|---:|---:|---|
| H | `D:\Dev\AI\.agents\skills` | 13 | 22 | No Git repository; latest skill file mtime is in July |
| M | `D:\Dev\AI\meteoscape\.agents\skills` | 21 | 33 | Aug 24, `57c972e` |
| A | `D:\Dev\DriftSense\workspace\agents\skills` | 21 | 36 | Aug 24, `384d318` |
| F | `D:\Dev\DriftSense\workspace\forecast_collector\.agents\skills` | 19 | 30 | Sep 3, `a0ba8d5` |

The counts include appendices and, in M, `workflow.excalidraw`. **These are four independent physical copies.** No files examined have multiple hardlinks. There is no cross-project link to a common canonical skill tree.

Within projects, the following are real, resolving symbolic links, tracked with Git mode `120000`; all three repositories have local `core.symlinks=true`:

| Project | Link | Target, relative to link's parent |
|---|---|---|
| M | `.claude/skills` | `../.agents/skills` |
| M | `.codex/skills` | `../.agents/skills` |
| M | `.cursor/skills` | `../.agents/skills` |
| A | `.cursor/skills` | `../skills` |
| F | `.claude/skills` | `../.agents/skills` |
| F | `.claude/codex` | `../.agents/skills` |
| F | `.codex/skills` | `../.agents/skills` |
| F | `.cursor/skills` | `../.agents/skills` |

Thus editing a skill through one of M's three loaders changes M's one physical copy; it does not update A, F or H. The same holds within F. F's `.claude/codex` is an extra alias, not a documented skills discovery location.

M's `.agents/skills.zip` contains **33 files, all byte-identical to current M, with nothing missing or extra**. It is an untracked snapshot, not a newer version or an update mechanism. Its similarity to F is consistent with seeding F from M, but the archive comparison alone does not prove that transfer occurred.

The three main tracked skill trees and inspected scripts/loaders have no pending modifications. Other project documentation has pre-existing edits. A is its own nested Git repository; the outer DriftSense workspace lists that directory as untracked. Updating or committing the outer workspace is not equivalent to updating A.

## 3. Which version of each dev skill is ahead

`=` below means the same core after ignoring local blocks and harmless whitespace, not necessarily identical bytes. Candidate sources are recommendations for the later alignment, not selections already made. All 21 skills in the main family are covered.

| Skill | H compared with M | M / A / F discrepancy | Candidate for shared core |
|---|---|---|---|
| `advise` | Older formulation | M = A. F changes the description and subject to the current topic, merges questionable/missing, drops hidden edges. Sep 2, `3f2ba65`. | **Decision:** M's broader prompts versus F's shorter formulation; recency does not establish an improvement. |
| `align` | Lacks later necessity gate, falsification, Edge and ticket-resolution guidance | M = F core; F adds local exceptions. A extracts concern format into `CONCERNS-FORMAT.md` and adjusts the body, Aug 24 `384d318`. | **M plus consideration of A's extraction.** A is the newest distinct shared-body branch; F is not a newer core here. |
| `celebrate` | Absent | M = A = F, byte-identical | M/A/F equivalent. |
| `commit` | Absent | M = A = F core. Gate commands and release facts differ in local blocks. | M/A/F equivalent core; retain each project's checks and release rules. |
| `conclude` | Older session/daily-summary guidance | M = A; F differs only in line endings | M/A/F equivalent. |
| `denoise` | Older; lacks later document lifecycle and concern retirement guidance | M = A = F core; F adds a local record-mover command | M/A/F equivalent core. |
| `dream` | Absent | M = A, byte-identical; absent in F | M/A if part of the shared suite. F absence has no explicit omission declaration. |
| `edge` | Absent | M = A, byte-identical; absent in F | M/A if part of the shared suite. F explicitly has no Edge records yet; absence is consistent with local scope, not proof of a stale copy. |
| `impact` | Absent | M = A. F adds an explicit issue/slice trigger to metadata; method otherwise unchanged, Sep 2 `3f2ba65`. | F trigger is a candidate; wording contains “it's slice”. |
| `implement` | Older, missing later implementation and review handoff refinements | M = A = F core; F specifies pytest and absence of a typechecker locally | M/A/F equivalent core. |
| `improve-comments` | Older wording/examples | M = A = F, byte-identical | M/A/F equivalent. |
| `plan-impl` | Older validation and architecture rules | M = A. F explicitly repeats validation through the same skill, Sep 2 `3f2ba65`; Sep 3 adds local ownership of `Pass` by a hook. | F's body sentence is a candidate; the hook/Pass rule remains a separate local dependency. |
| `recall` | Absent | M = A core, different local delivery sources. F prioritizes landed-but-unchecked work at next session start, Aug 29 `29c3cc6`. | F's new rule is a candidate; retain local delivery source. |
| `review-architecture` | Older routing and duplicated issue template | M = A = F, byte-identical, including `REFERENCE.md` | M/A/F equivalent; route findings through existing tickets/RFCs. |
| `review-impl` | Absent | M = A. F adds “Use /implement to amend found discrepancies”, Sep 3 `a0ba8d5`. | **Decision:** this expands a review into amendment; it is a behavioral change, not housekeeping. |
| `setup-devops` | Old metadata declares **`name: setup-project`** despite folder name; wording differs | M = A = F, byte-identical; modern name matches folder | M/A/F equivalent. H's name mismatch can affect invocation. |
| `skill-up` | Absent | M = F. A lacks process-convention guidance, the no-local-override rule, defect repair during porting and guidance for skills present in only one corpus. | M/F are more complete. A's later file commit timestamp does not make its content ahead. |
| `sync-arch` | Older one-direction sync and documentation paths | M = A after trailing whitespace; F adds local no-Edge-records exception | M/A/F equivalent core. |
| `tdd` | Lacks RFC-satisfies-planning-gate rule | M = A = F, byte-identical. **All five supporting Markdown files, including `tests.md`, exist and match in H/M/A/F.** | M/A/F equivalent; no missing appendix to restore. |
| `to-spec` | Older scope/output location; no modern handoff | M = F after final newline. A retargets its process link and adds the initiative alternative plus `INITIATIVE-FORMAT.md`. | **Decision:** ordinary spec core M/F; consider whether A's initiative branch is shared or project-specific. |
| `to-tickets` | Older spec-only decomposition and embedded ticket template | M has current general decomposition. A writes tracker entries via `NOTION-FORMAT.md` with optional local documents. F adds impact analysis of the proposed split, Sep 2 `3f2ba65`. | F's impact step is a candidate on M's core; preserve A's tracker workflow through an explicitly agreed local mechanism. |

After local blocks and trailing whitespace are excluded, A matches M on **17 of 21** skill bodies and differs on four: `align`, `skill-up`, `to-spec`, `to-tickets`. F matches M on **13 of its 19** and differs on six: `advise`, `impact`, `plan-impl`, `recall`, `review-impl`, `to-tickets`.

H differs from M on all 13 shared skill bodies. It is useful as historical evidence, not as the most recent core. F's `advise` returns toward H's wording but is not the same complete text.

F's skill-path history contains four commits: the initial tracked set at `43861b4` on Aug 29, then `29c3cc6`, `3f2ba65` and `a0ba8d5`. Separate hook/script commits are a different history surface. A has three commits touching `skills/`, plus a separate loader-link commit.

## 4. Appendices are part of the discrepancy

| File(s) | Verified difference | Meaning for later canonical extraction |
|---|---|---|
| `align/ADR-FORMAT.md` | M = A = F; H older | Shared format candidate. |
| `align/ARCH-FORMAT.md` | M = A; F only adds a final newline; H differs in layout and links | Shared format candidate; no substantive F improvement. |
| `align/GLOSSARY-FORMAT.md` | H = M = A; F adds a local `docs/glossary.md` location block | Common template plus local location; note mismatch between root-glossary fallback in template and docs layout in modern align. |
| `align/EDGE-FORMAT.md` | H absent; M/F equivalent text; A points to its process seam instead of M's ticket-status section | A contains a valid local documentation link, not an automatically portable change. |
| `align/CONCERNS-FORMAT.md` | A only | Mostly reusable formatting: stable IDs, priority order, entry shape and citations. Moving A's body without this new appendix would break its dependency. |
| `review-architecture/REFERENCE.md` | M = A = F; H retains old issue-template material | Shared candidate; keeping every existing appendix untouched would leave H behind. |
| `tdd/deep-modules.md`, `interface-design.md`, `mocking.md`, `refactoring.md`, `tests.md` | All five byte-identical in H/M/A/F | Shared assets, not differing project conventions. |
| `to-spec/INITIATIVE-FORMAT.md` | A only, explicitly declared project-local; contains Notion header and process references | Concept might be reusable, but this file is not a neutral shared template as written. |
| `to-tickets/NOTION-FORMAT.md` | A only, explicitly local | Tracker properties, ownership and status rules belong to DriftSense; external write semantics also depend on the host's tools and authorization. |
| `to-tickets/TICKET-FORMAT.md` | Three substantive variants | M: numbered queue spanning releases. F: single-release collector, different Python command, reduced examples and Edge references. A: Notion owns status and classification; local document shape excludes those fields. None is universally ahead. |
| `workflow.excalidraw` | M only, included in M's ZIP | A visual workflow asset, not a skill entrypoint. H also has separate top-level `dev-skills` PNG/Excalidraw assets outside `skills/`. |

The existing `skill-up` contract protects **every appendix**, not just `<project-local>` blocks. That policy protects local ticket formats, but would also prevent distributing improvements to genuinely shared formats and TDD assets. File suffix alone cannot identify ownership reliably.

## 5. Project-local boundary and mechanical-update implications

Actual complete blocks, excluding prose that merely mentions the tag:

| Copy | Files with actual blocks | Count |
|---|---|---:|
| H | None | 0 |
| M | `commit/SKILL.md`, `recall/SKILL.md` | 2 |
| A | `commit/SKILL.md`, `recall/SKILL.md` | 2 |
| F | `align/SKILL.md`, `align/GLOSSARY-FORMAT.md`, `commit/SKILL.md`, `denoise/SKILL.md`, `implement/SKILL.md`, `plan-impl/SKILL.md`, `recall/SKILL.md`, `sync-arch/SKILL.md` | 8 |

**No `skill-up/SKILL.md` in H/M/A/F contains a complete local block.** M/A/F mention the marker as an example in their instructions. A naive marker search misclassifies those mentions.

Current boundaries do not fully satisfy “portable body, local additions”:

- A's `to-tickets` body directly specifies Notion-related tracker creation and third-line URL placement; this is outside a local block.
- A's `to-spec` body introduces an initiative workflow tied to a local appendix.
- F's `align` and `sync-arch` blocks waive Edge checks; its `align` block also preserves an existing unnumbered concern format. These are conditional exceptions, in tension with M/F `skill-up` saying local blocks never override the body.
- F's local `implement` block supplies pytest where the shared body assumes checking with a typechecker. Local environment differences already require conditional interpretation.
- Relative paths depend on layout: A uses `skills/<name>` and `../../docs`; M/F use `.agents/skills/<name>` and `../../../docs`. Copying a body between those layouts can break otherwise valid links. The future canonical repo also needs an explicit distinction between its own documents and a consuming project's documents.
- Body changes can add appendix or script dependencies. Preserving all existing local files cannot by itself decide how a **new** appendix is introduced.
- Missing skills can be intentional. F's absence of `edge` has supporting context; `dream` has no equivalent declaration. Deletion versus update cannot be inferred from a hash mismatch.
- No inspected main suite carries a common version manifest or records the last canonical hash applied to each recipient. Hash equality can establish “same/different”; it cannot establish “local is behind” when both sides have changed. A's `skill-up` is a concrete timestamp counterexample.

These are requirements to resolve during alignment, not an implemented sync design. At minimum, the later mechanism must distinguish shared content, local content, intentionally absent skills and local edits to previously shared content; account for dependency and path changes; and report ambiguous divergence before overwriting it. A whole-folder mirror does not currently preserve the intended semantics.

## 6. Framework coverage and surrounding harness

Interpreting the three frameworks as **Claude Code, Codex and Cursor**, based on the project folders. This session itself is Codex.

Codex documents scanning `.agents/skills` from the current directory up to the repository root, supports symlinked skill folders and does not merge skills sharing a name. Its documented CLI/IDE explicit invocation uses `$skill`; `/skill` strings inside this suite are workflow references, not a guaranteed host command syntax. [Official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills).

Claude Code documents project skills under `.claude/skills`, parent discovery up to the repository root and nested discovery on demand. Its docs support symlinked individual skill directories. A whole-root loader link on disk was verified here; actual installed-host discovery was not exercised. [Claude Code skills](https://code.claude.com/docs/en/skills).

Cursor documents `.agents/skills` and `.cursor/skills`, compatibility discovery from Claude/Codex skill directories, and nested project scoping. Thus multiple aliases are redundant entry paths, not evidence of separate versions; duplicate handling for this installation was not tested. [Cursor skills](https://cursor.com/docs/skills).

| Project/opening context | Claude Code | Codex | Cursor |
|---|---|---|---|
| M opened as project | Resolving `.claude/skills` alias | Native `.agents/skills` present | Native `.agents/skills` and aliases present |
| F opened as project | Resolving `.claude/skills` alias | Native `.agents/skills` present | Native `.agents/skills` and aliases; Cursor-only loop hook |
| A opened as project | No project loader found | No project `.agents/skills` found; plain `skills/` is not the documented repo path | Resolving `.cursor/skills` alias |
| H opened at current cwd `D:\Dev\AI\.agents` | No `.claude/skills` loader | Suite is not in this session's supplied skill catalog; cwd contains `skills/`, not `.agents/skills` | No project `.agents/skills` or `.cursor/skills` inside this cwd |
| Other DriftSense repos opened alone | No suite loader found | No suite loader found | No physical suite found in those repos |

Do not generalize H's current-session result to every possible opening directory: `D:\Dev\AI\.agents\skills` has the conventional shape relative to **`D:\Dev\AI`**. Its scope is different when opening `.agents` itself. Similarly, a sibling `agents` folder is not a parent-level skill location for a standalone project.

`drift-sense.code-workspace` includes `wrf_coordinator`, `admin`, `static_frontend_farmer`, and **`agents`**. `forecast_collector.code-workspace` includes `forecast_collector` and `forecast_analysis`. These multi-root configurations explain an intended shared Cursor context, but do not prove the same suite is available when opening any sibling independently in another framework.

Other DriftSense findings: `admin`, `static_frontend_farmer` and `wrf_coordinator` have `.cursor/rules/global.md`, not skill suites. `ping/.cursor` is an ordinary text file containing an instruction, not a directory or symlink. `admin/agents` contains no `SKILL.md` discovered by the scan. No additional skill copies were found in the other workspace subprojects.

User-level: five unrelated physical Cursor skills; no repeated dev suite there. No user suite found in `~/.agents/skills` or `~/.claude/skills`. `~/.codex/skills` contains the bundled `.system` skills, so saying it is empty would be wrong. Installed plugin skills are also separate from these project copies and were not treated as canonical-dev candidates.

Surrounding files matter to portability:

- **`move_doc.py` is not self-contained.** M/F import `docs_corpus` from `tests/deterministic`; A imports its sibling `scripts/docs_corpus.py`, which owns the different repository-root calculation. Copying only `.agents/scripts` misses M/F's dependency. A's difference is more than the invocation line.
- **F has a compatibility change in the mover:** explicit `open(..., newline="")` instead of M/A's `Path.read_text(..., newline="")`, plus different launch and verification commands. The transform logic is closely shared; packaging and runtime assumptions differ. [M → A script diff](./move_doc-M-to-A.diff), [M → F script diff](./move_doc-M-to-F.diff).
- **The record mover moves documents, not skills.** Its existence is not an existing skill synchronization mechanism. Documentation integrity/convention guards are associated dependencies, with project-specific queue conventions.
- **F's planning loop is Cursor-specific in this tree:** `.cursor/hooks.json` registers three events through a Windows `.cmd` wrapper calling `venv/Scripts/python.exe`. `plan_impl_loop.py` tracks conversation state under `.cursor/hooks/state`, recognizes collector `01-...` record names, stamps `Pass`, and returns Cursor follow-up messages. It targets three passes with `loop_limit: 2`. There is no corresponding Claude/Codex registration in F. Copying the skill text does not port this behavior.
- **Always-loaded instructions differ:** M has `.claude/CLAUDE.md`; F has Cursor's always-applied venv rule. No `AGENTS.md`/`AGENTS.override.md` was found in the scanned main repos. Instructions written in a harness README are not automatically equivalent to framework-level instructions.
- **Loader READMEs need correction:** M omits its Codex alias; A describes Cursor only; F advertises the stray `.claude/codex` as a Claude loader and its repair command ambiguously mixes the current directory with the link path. Existing links work, but the documentation is not a verified bootstrap procedure.

## 7. Neighboring skill families

Included in the inventory and diff evidence rather than silently discarded as older copies:

| Key | Location | Skills / files | Relationship and finding |
|---|---|---:|---|
| L | `D:\Dev\AI\life\.agents\skills` | 24 / 41 | Active through Sep 5; separate evidence/memory and agent-operation family. Its own `skill-up` explicitly names Meteoscape as reference and declares software-delivery skills such as `edge`, `review-architecture`, `setup-devops`, `to-spec` intentionally unported. |
| L2 | `D:\Dev\AI\life-2\.agents\skills` | 19 / 31 | No Git repository. Earlier-looking Life snapshot with `to-tickets` where L has `ticket`; fewer skills and several unresolved document links. No proof that the timestamp alone establishes its origin. |
| W | `D:\Dev\AI\weather-mcp\.cursor\skills` | 7 / 16 | Earlier-style dev family; includes old `write-prd` and `to-issues` names/output conventions. No Git history available. H adds skills and revises align/denoise; several shared files are identical. |
| S | `D:\Dev\AI\skills-main\skills` | 29 / 61 | Downloaded external source collection. Its README identifies **Matt Pocock's `skills`**, not Anthropic's repository. Nested categories include engineering, productivity, deprecated and in-progress skills; inventory presence does not imply active installation. |

L's later timestamps do not make it the newest dev suite. For example, its `commit` explicitly permits automatic commits and retires the dev suite's commit tags; its `align` governs adoption of local meta-rules; its `skill-up` adds evidence layers, a graveyard and local `core/process.md` conventions. Its implementation workflow splits into `implement`, `mechanism` and `maintain`. These are material differences in authority and purpose. L also has `audit`, `comment`, `experiment`, `failure`, `lurk`, `metric`, `reasoning`, `remember`, `ticket` and `triage`, whose inclusion in a canonical **dev** harness would require a scope decision.

L uses a resolving `.claude/skills` symlink. L2's `.claude/skills` is a separate physical directory with no skill entrypoints, so its Claude loader is not equivalent to L's. W's `.agents` directory is empty; its actual suite is under Cursor.

Evidence covers [M → L](./M-to-L.diff), [L2 → L](./L2-to-L.diff), and [W → H](./W-to-H.diff). All neighboring files have hashes in the CSV/JSON. This is a full discrepancy record, not an approval to import their workflows.

## 8. Verification and corrections to the previous audit

All inventoried source hashes were rechecked and unchanged at verification time. Every main skill entrypoint has `name` and `description`; H's setup name mismatch remains. The relative prose-link check found no missing file targets in M/A/F. H's align contains `./docs/concerns.md`, which does not resolve relative to its skill file. Fenced template examples were excluded from that check. This check does not validate heading anchors, external URLs, runtime invocation or every plain-text path reference.

The previous `SKILLS-AUDIT-2026-09-05.md` should not drive extraction uncorrected:

- Counts are H **13/22**, M **21/33**, A **21/36**, F **19/30**.
- M and A **do have tracked `tdd/tests.md`**, identical to H/F.
- The main `skill-up` files **do not have local blocks**; examples of the tag are not blocks.
- A's `align` has the newest distinct portable-format change; M and F share the same core apart from F's local block.
- F's skill history is four skill-path commits, not five `SKILL:` commits; hook history must be counted separately.
- The external source checkout identifies Matt Pocock, not Anthropic.
- `.codex/skills` is not the documented basis for current Codex project discovery, and the home Codex skills directory is not empty.
- `move_doc.py` has layout/import dependencies as well as invocation differences.
- The files have a mixture of line-ending styles, including mixed files; this is comparison noise to classify, not evidence that every copy must be rewritten before analysis.

## 9. Alignment handoff — stop here

Located and read the dev-family align rules, with the other variants compared:

- [Meteoscape align](D:/Dev/AI/meteoscape/.agents/skills/align/SKILL.md): full general method, Aug 24 `777caa1`.
- [DriftSense agents align](D:/Dev/DriftSense/workspace/agents/skills/align/SKILL.md): same general method with concerns format extracted, Aug 24 `384d318`; read with [CONCERNS-FORMAT.md](D:/Dev/DriftSense/workspace/agents/skills/align/CONCERNS-FORMAT.md).
- [Forecast Collector align](D:/Dev/DriftSense/workspace/forecast_collector/.agents/skills/align/SKILL.md): M core plus collector-specific exceptions.
- [Current H align](../legacy/skills/align/SKILL.md): older; not the best version for the upcoming discussion.

The future alignment should settle the target path spelling, canonical suite membership, the six F changes, A's concerns/initiative contributions, and what counts as local—including exceptions and full appendices—before choosing update mechanics. The current evidence supports using M as a comparison baseline, not declaring its entire folder canonical unchanged.

**Phase A ends here. No canonical extraction, synchronization implementation, links, commits or deployment actions were performed.**
