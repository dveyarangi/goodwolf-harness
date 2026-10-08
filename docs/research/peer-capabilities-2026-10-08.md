# What peer tools can do, as of 2026-10-08

Run at the front-page align on
[q-0031](../questions/q-0031-what-is-the-harness-said-to-a-reader-who-arrives-cold-and-what-of-it-does-the-front-page-carry.md).
The agent was about to write the page's positioning from the
[2026-09-26 pass](discover-what-this-is.md). The user said that pass was long out of date.
[The README survey of the same day](readme-survey-2026-10-08.md) already contradicted it: GSD and
BMAD now advertise memory between sessions. Four web-only passes ran at once, three or four tools
each. Each answered the same ten questions about every tool from its current docs and releases,
with a date and a confidence for every claim. None was told anything about this project.

The summary below is the agent's reading. The harness's row is the agent's account of its own
tree, not a pass's. The four reports follow it as they came back.

## Summary

Cells: **Y** yes, **P** partial, **N** no. The questions, in short:

1. Repo-resident state
2. Oriented automatically at session start
3. Something injected before every message
4. Open questions as structured items
5. Decision records apart from tasks
6. Drift checked and repaired
7. Verification as its own step
8. Awareness of other sessions
9. A failed instruction leads to its amendment
10. Project overrides that survive updates
11. Hosts

| tool, version | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GSD Core 1.16.0 | Y | P | N | P | P | Y | Y | Y | N | Y | ~15 |
| BMAD 6.12.1 | Y | P | N | P | Y | P | Y | P | P | Y | ~45 |
| Spec Kit 1.1.2 | Y | N | N | P | P | P | Y | N | N | Y | 40+ |
| OpenSpec 1.14.1 | Y | P | N | P | P | P | Y | P | N | Y | 40+ |
| Superpowers 6.4.2 | Y | Y | N | N | P | P | Y | P | P | P | 16 |
| mattpocock/skills 1.3.1 | Y | P | N | Y | Y | P | Y | P | P | P | 2+ |
| beads 1.3.1 | Y | Y | N | P | P | N | P | Y | N | Y | ~15 |
| Backlog.md 1.53.0 | Y | P | N | N | Y | N | Y | P | N | P | ~6 |
| Cline (Memory Bank) 4.1.23 | Y | Y | P | N | P | P | N | P | P | Y | own host |
| claude-mem 13.34.2 | P | Y | N | N | P | N | N | P | N | P | ~14 |
| Kiro, IDE 1.2.4 | Y | Y | P | N | P | P | P | P | P | Y | own host |
| Agent OS 3.0 | Y | N | N | N | P | P | N | N | N | P | ~5 |
| cc-sdd 3.1.0 | Y | P | N | N | Y | P | Y | P | N | Y | 8 |
| Gas Town 1.2.1 | Y | Y | Y | P | N | N | P | Y | N | Y | ~11 |
| Archon 0.11.1 | P | N | N | P | P | P | Y | Y | N | Y | 3 |
| Claude Code memory 2.1.294 | P | Y | N | N | P | P | P | P | P | Y | own host |
| **this harness** | Y | Y | Y | Y | Y | Y | Y | P | Y | Y | 3 |

Notes on the cells:

- **Column 3, per-message injection.** Gas Town's per-message hook delivers mail between agents,
  not project state. Cline and Kiro offer a hook the user may configure, and ship none.
- **Column 4, open questions.** mattpocock's `wayfinder` keeps decision tickets apart from task
  tickets, as child issues of a map, linked by blocking edges. It is a situational skill for large
  work, not the default flow.
- **Column 6, drift.** GSD repairs the documents toward the code. Its fact-drift pass names which
  side is authoritative, and only reports. Spec Kit's `converge` repairs the code toward the spec.
  The harness declares the direction per kind of record, both ways.
- **Column 8, other sessions.** GSD, beads and Gas Town have locks, claims and worktrees. The
  harness has awareness only: each session sees the others' positions, and nothing locks.
- **Column 9, failed instructions.** Superpowers tests its skills like code and diagnoses failed
  sessions, but only upstream. BMAD writes a pitfall line into the project's instructions. The
  harness keeps a register in the project that ties a rule that did not fire to its rewording.

**Standard in the field now**, in most of the sixteen:

- state kept in the repository
- a verification step against criteria
- project overrides that survive an update
- some orientation at session start
- many hosts: most support fifteen or more

**Rare**, held by one or two tools, or by none of them:

- **project context injected before every message:** none
- **open questions as structured items, at the centre of the method:** none; one tool has them situationally
- **a repair direction declared per kind of record, both ways:** none; two tools have one direction each
- **an in-project tie from a rule that did not fire to its amendment:** none; one writes pitfall lines

**Where the harness is behind:**

- three hosts against fifteen to fifty
- awareness of other sessions without locks
- no lighter path for small work
- one author, one month old

---

# Pass 1 — GSD Core, BMAD-METHOD, Spec Kit

# Capability survey: GSD Core, BMAD-METHOD, Spec Kit (checked 2026-10-08)

Docs pages without their own date are marked "accessed 2026-10-08". Release dates come from the GitHub releases API.

## GSD Core (open-gsd/gsd-core)

**Which repo is canonical:** open-gsd/gsd-core. gsd-build/get-shit-done was archived on 2026-06-26 and its notice says the project "now continues as GSD Core" ([archived repo](https://github.com/gsd-build/get-shit-done)).
**Latest version:** v1.16.0, published 2026-10-05 ([releases](https://github.com/open-gsd/gsd-core/releases)). The README still links "What's new in 1.7.0", so it is out of date.

| # | Question | Answer | How | Source + date | Conf. |
|---|---|---|---|---|---|
| 1 | What persists | yes | Files in the repo under `.planning/`: PROJECT, REQUIREMENTS, ROADMAP, STATE.md, config.json, `phases/XX-*/` (CONTEXT, RESEARCH, PLAN, SUMMARY), plus threads/, seeds/, backlog/, todos/, notes/, debug knowledge-base, HANDOFF.json. A "global learnings store" covers several projects. An optional mempalace memory store is external (it appears in the 1.16.0 changelog). | [ARCHITECTURE.md](https://github.com/open-gsd/gsd-core/blob/main/docs/ARCHITECTURE.md), [FEATURES.md](https://github.com/open-gsd/gsd-core/blob/main/docs/FEATURES.md), accessed 2026-10-08; [CHANGELOG 1.16.0](https://github.com/open-gsd/gsd-core/blob/main/CHANGELOG.md), 2026-10-05 | H |
| 2 | Session orientation | partial | The SessionStart hooks only check for updates, fix install paths and track session state for shell-based runtimes. Orientation needs a command: `/gsd-resume-work`, `/gsd-next` (reads STATE/ROADMAP/git and dispatches one command) or `/gsd-progress`. A generated CLAUDE.md is always loaded and lists the entry points. Nothing runs before each user message (no UserPromptSubmit hook). A PostToolUse context monitor injects context-budget warnings. | [ARCHITECTURE.md hooks table](https://github.com/open-gsd/gsd-core/blob/main/docs/ARCHITECTURE.md), [COMMANDS.md](https://github.com/open-gsd/gsd-core/blob/main/docs/COMMANDS.md), accessed 2026-10-08; CLAUDE.md entry-point list in [CHANGELOG 1.16.0](https://github.com/open-gsd/gsd-core/blob/main/CHANGELOG.md), 2026-10-05 | H |
| 3 | Open questions as first-class items | partial | There are capture types other than tasks: threads (`.planning/threads/`, cross-session knowledge outside any phase), seeds (ideas with trigger conditions that surface at a milestone), and a backlog numbered 999.x. None of them is an open-question item with parent/child links or dependencies. | [FEATURES.md](https://github.com/open-gsd/gsd-core/blob/main/docs/FEATURES.md), accessed 2026-10-08 | M |
| 4 | Decision records separate from tasks/specs | partial | `/gsd-discuss-phase` writes decisions into each phase's CONTEXT.md. A "decision coverage gate" traces them into plans (blocking) and into shipped work (non-blocking). One-way-door plans raise `checkpoint:decision`. Decisions are kept per phase; no project-wide decision register is described. | [ARCHITECTURE.md](https://github.com/open-gsd/gsd-core/blob/main/docs/ARCHITECTURE.md), [FEATURES.md](https://github.com/open-gsd/gsd-core/blob/main/docs/FEATURES.md), accessed 2026-10-08 | M |
| 5 | Drift check and repair | yes | (a) A fact-drift pass compares the same fact across ROADMAP, PLAN, STATE and CONTEXT. It reports contradictions and names which side is authoritative, but does not fix them (added in v1.11.0, 2026-08). (b) A plan drift guard checks plan symbols against live source. (c) A post-execute codebase drift gate either warns or auto-remaps `.planning/codebase/`, so the documents are brought in line with the code. `/gsd-health --repair` fixes `.planning/` integrity. | [ARCHITECTURE.md](https://github.com/open-gsd/gsd-core/blob/main/docs/ARCHITECTURE.md), [FEATURES.md](https://github.com/open-gsd/gsd-core/blob/main/docs/FEATURES.md), accessed 2026-10-08; [releases](https://github.com/open-gsd/gsd-core/releases) v1.11.0 | M |
| 6 | Verification against acceptance criteria as its own step | yes | Verify is its own phase of the loop. `/gsd-verify-work` runs UAT with auto-diagnosis and writes fix plans; automated items pass on their own and judgment items go to a human. Each plan has `verify`/`done` fields. `/gsd-audit-milestone` checks the definition of done, and `/gsd-audit-uat` checks across phases. | [COMMANDS.md](https://github.com/open-gsd/gsd-core/blob/main/docs/COMMANDS.md), [README](https://github.com/open-gsd/gsd-core), accessed 2026-10-08 | H |
| 7 | Awareness of concurrent sessions/agents | partial | Workstreams (`.planning/workstreams/<name>/`) are documented "for concurrent work". Every STATE.md write takes a lock (`STATE.md.lock`, O_EXCL). Parallel executors run in waves, and quick-batch serializes worktree create/merge. No registry of live sessions is described. | [ARCHITECTURE.md](https://github.com/open-gsd/gsd-core/blob/main/docs/ARCHITECTURE.md), [USER-GUIDE.md](https://github.com/open-gsd/gsd-core/blob/main/docs/USER-GUIDE.md), accessed 2026-10-08 | H |
| 8 | Improving its own instructions after a rule was not followed | no | `/gsd-extract-learnings`, `/gsd-forensics` (post-mortem of failed workflows) and the debug knowledge base record lessons about the work. None of them amends GSD's own prompts or rules. | [COMMANDS.md](https://github.com/open-gsd/gsd-core/blob/main/docs/COMMANDS.md), [FEATURES.md](https://github.com/open-gsd/gsd-core/blob/main/docs/FEATURES.md), accessed 2026-10-08 | M |
| 9 | Project overrides that survive updates | yes | The installer backs up locally modified GSD files to `gsd-local-patches/`, and `/gsd-update --reapply` puts them back. Since 1.14.0 (2026-09-14) it skips customizations that upstream has already adopted. Custom skill files go to `gsd-user-files-backup/`. Settings live in `.planning/config.json`. | [USER-GUIDE.md](https://github.com/open-gsd/gsd-core/blob/main/docs/USER-GUIDE.md), accessed 2026-10-08; [CHANGELOG 1.14.0](https://github.com/open-gsd/gsd-core/blob/main/CHANGELOG.md), 2026-09-14 | H |
| 10 | Agent hosts | yes | 15 or more runtimes: Claude Code, OpenCode, Kilo, Kimi CLI, Codex, Copilot, Antigravity, Cursor, Windsurf, Augment, Trae, Qwen Code, Hermes Agent, CodeBuddy, Cline. | [ARCHITECTURE.md](https://github.com/open-gsd/gsd-core/blob/main/docs/ARCHITECTURE.md), [README](https://github.com/open-gsd/gsd-core), accessed 2026-10-08 | H |

Notes:
- Of the three tools, GSD does the most with hooks and state. It has thirteen hooks, but none of them injects project state at session start or before a user message, so orientation still depends on a command plus the generated CLAUDE.md.
- Drift checking is real and comes in several layers. The direction is either report-only (contradictions between documents) or repair of the documents toward the code (codebase map remap). It never repairs code toward the documents.
- Releases come about every 1–2 weeks (v1.11 to v1.16 between August and October 2026). Some fetched docs mention "since v1.17", which looks like version numbering carried over from the archived get-shit-done repo.

## BMAD-METHOD (bmad-code-org/BMAD-METHOD)

**Latest version:** v6.12.1, published 2026-10-04; v6.12.0 came out 2026-09-04 ([releases](https://github.com/bmad-code-org/BMAD-METHOD/releases)).
**Caution:** The main-branch CHANGELOG has an "Unreleased (v7)" section: initiative folders, `bmad-ticket` (renamed from `bmad-preview-ticketing`), Toolsmith, a memory agent. docs.bmad-method.org appears to describe that main-branch state, so items marked "(v7?)" below may not be in any shipped release yet.

| # | Question | Answer | How | Source + date | Conf. |
|---|---|---|---|---|---|
| 1 | What persists | yes | Files in the repo. `_bmad/` holds the runtime, config.toml and `custom/`. `_bmad-output/` holds plans, PRD, the architecture spine, `sprint-status.yaml` and `research-<topic>.md`. A `<!-- bmad:context -->` block lives in AGENTS.md. memlog is an append-only working-memory file (v6.9.0). Party mode has optional memory under `{memory_dir}`. | [v6.9.0 notes](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.9.0), 2026-06-22; [Install](https://docs.bmad-method.org/start/install-bmad/), accessed 2026-10-08 | H |
| 2 | Session orientation | partial | The host loads the AGENTS.md context block every session (CLAUDE.md gets an `@AGENTS.md` import). `persistent_facts` load when a skill activates; since 6.12.0 they ship empty, so project-context.md must be re-added by hand. On command, the `bmad` skill reads the active initiative and says what to do next. No hooks; nothing is injected per message. | [Project context](https://docs.bmad-method.org/existing-codebases/set-and-maintain-project-context/), [Get answers](https://docs.bmad-method.org/start/get-answers-about-bmad/), accessed 2026-10-08; [v6.12.0](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.12.0), 2026-09-04 | M |
| 3 | Open questions as first-class items | partial | The ticket tree is structured: initiative, then epics, then stories/spikes/bugs in `tickets.toml`, with `after` dependencies. Those are work items, though. Uncertainty is held only as `unknown` fields on entries. Retrospective action items live in sprint-status.yaml. (v7?) | [Ticket tree](https://docs.bmad-method.org/plan/set-up-the-ticket-tree/), accessed 2026-10-08; [v6.9.0](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.9.0), 2026-06-22 | M |
| 4 | Decision records separate from tasks/specs | partial | The architecture "spine" records only decisions that would conflict if made independently. Each has a stable ID that specs and stories cite. Research produces cited `research-<topic>.md` files. There are no ADR files, and memlog replaced the per-skill decision logs. | [Design UX & architecture](https://docs.bmad-method.org/plan/design-ux-and-architecture/), [Research a decision](https://docs.bmad-method.org/plan/research-a-decision/), accessed 2026-10-08 | M |
| 5 | Drift check and repair | partial | `bmad-project-context` Refresh diffs deletions and renames since the recorded commit and updates the AGENTS.md block, so the document is repaired toward the code. The retrospective flags where code diverged from the epic or requirements but only proposes fixes ("Nothing touches your code or your specs automatically"). `bmad-correct-course` is run by hand. | [Project context](https://docs.bmad-method.org/existing-codebases/set-and-maintain-project-context/), [Finish an epic](https://docs.bmad-method.org/build/finish-an-epic/), accessed 2026-10-08 | M |
| 6 | Verification against acceptance criteria as its own step | yes | Review includes a dedicated pass that checks "whether the change does what it claims" against the plan's intent. Since 6.12.0, triage logs a verdict and evidence for every finding in the plan's `## Code Review` section. Build stops at `built`; only a human or an orchestrator marks a story done. | [Review a change](https://docs.bmad-method.org/build/review-a-change/), accessed 2026-10-08; [v6.12.0](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.12.0), 2026-09-04 | M |
| 7 | Awareness of concurrent sessions/agents | partial | An orchestrator session can dispatch one Build Auto worker per ticket, and independent epic streams can run in parallel. No locking or claiming is documented. Announced but not shipped: "bmad-loop orchestrator does not dispatch from the ticket tree yet". | [Autonomous loops](https://docs.bmad-method.org/build/autonomous-development-loops/), accessed 2026-10-08 | M |
| 8 | Improving its own instructions after a rule was not followed | partial | The project-context **Record** intent ("An agent just made a mistake worth writing down") writes the pitfall into the AGENTS.md block. That improves the project's instructions, not BMAD's own skills. Toolsmith's session-log mining for skills is unreleased (v7). | [Project context](https://docs.bmad-method.org/existing-codebases/set-and-maintain-project-context/), accessed 2026-10-08; [CHANGELOG Unreleased](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/CHANGELOG.md) | H |
| 9 | Project overrides that survive updates | yes | Overrides are layered: `_bmad/custom/<skill>.user.toml` (personal), then `_bmad/custom/<skill>.toml` (team), then the shipped `customize.toml`. They can change principles, activation steps, menus and review layers. "Updates do not touch your files". In 6.12.1 every skill reads the same merged config. | [Customize BMad](https://docs.bmad-method.org/customize/customize-bmad/), accessed 2026-10-08; [v6.12.1](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.12.1), 2026-10-04 | H |
| 10 | Agent hosts | yes | Plugin marketplaces for Claude Code and Codex. The skills CLI (`npx skills add`) covers "42+" platforms: Cursor, Copilot, Gemini, OpenCode, Kimi, Antigravity, Rovo Dev and others. 6.12.0 added Polytoken, Grok and ZCode. | [Install](https://docs.bmad-method.org/start/install-bmad/), accessed 2026-10-08; [CHANGELOG](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/CHANGELOG.md); [v6.12.0](https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.12.0) | M |

Notes:
- BMAD is the only one of the three with a built-in way to write a lesson down after an agent's mistake (the Record intent). It goes into the project's AGENTS.md, not into the method's own skills.
- The 6.11 and 6.12 releases consolidated skills (Quick Dev became Build, fourteen core skills became eight) and moved config to layered TOML. Expect older guides on the web to be wrong.
- A version mismatch weakens confidence on rows 3, 4 and 7: the docs site seems to follow the unreleased v7 main branch.

## Spec Kit (github/spec-kit)

**Latest version:** v1.1.2, published 2026-10-07; 1.1.0 came out 2026-10-02 ([releases](https://github.com/github/spec-kit/releases)).

| # | Question | Answer | How | Source + date | Conf. |
|---|---|---|---|---|---|
| 1 | What persists | yes | Files in the repo: `.specify/memory/constitution.md`, `specs/NNN-feature/` (spec, plan, research, data-model, contracts, tasks, checklists), `.specify/extensions.yml`, and the install manifest. No database or hosted service. | [README](https://github.com/github/spec-kit), [Upgrade](https://github.github.io/spec-kit/upgrade.html), accessed 2026-10-08 | H |
| 2 | Session orientation | no | The user drives everything with `/speckit-*` commands. Extension hooks run only before or after a command, never at session start or per message. The current plan template has no step that updates the agent context file. Community extensions (`companion`, `dubsar`) add resume and checkpoints. | [plan.md template](https://github.com/github/spec-kit/blob/main/templates/commands/plan.md), [community catalog](https://github.com/github/spec-kit/blob/main/extensions/catalog.community.json), accessed 2026-10-08 | M |
| 3 | Open questions as first-class items | partial | `[NEEDS CLARIFICATION]` markers sit inline in the spec. `/speckit.clarify` asks at most 5 questions per session and records `Q: → A:` bullets under `## Clarifications / ### Session YYYY-MM-DD`. The coverage report lists items as Outstanding or Deferred. Questions have no IDs and no parent/child or dependency links. `/plan` errors out while clarifications remain unresolved. | [clarify.md](https://github.com/github/spec-kit/blob/main/templates/commands/clarify.md), [plan.md](https://github.com/github/spec-kit/blob/main/templates/commands/plan.md), accessed 2026-10-08 | H |
| 4 | Decision records separate from tasks/specs | partial | Each feature's `research.md` records "Decision / Rationale / Alternatives considered". The constitution holds principles. Core has no ADR register; the community `adrkit` and `arch-governance` extensions add one. | [plan.md](https://github.com/github/spec-kit/blob/main/templates/commands/plan.md), [community catalog](https://github.com/github/spec-kit/blob/main/extensions/catalog.community.json), accessed 2026-10-08 | M |
| 5 | Drift check and repair | partial | `/speckit.analyze` checks spec, plan, tasks and constitution against each other and is "STRICTLY READ-ONLY": it suggests fixes and never applies them. `/speckit.converge` (0.11.2, 2026-06-17) checks the code against spec/plan/tasks and only appends tasks to tasks.md; it "MUST NOT" modify spec or plan, so drift is repaired on the code side. An opt-in constitution-sync preset exists (0.15.1, 2026-07-31); its direction is not documented. Community: `canon`, `ci-guard`, `blueprint-index`. | [analyze.md](https://github.com/github/spec-kit/blob/main/templates/commands/analyze.md), [converge.md](https://github.com/github/spec-kit/blob/main/templates/commands/converge.md), accessed 2026-10-08; [CHANGELOG](https://github.com/github/spec-kit/blob/main/CHANGELOG.md) | H |
| 6 | Verification against acceptance criteria as its own step | yes | `/speckit.converge` finds requirements and acceptance criteria that are "unmet, incomplete, or only partially satisfied". `/implement` halts while checklist items are unchecked and validates against the spec before it reports done. | [converge.md](https://github.com/github/spec-kit/blob/main/templates/commands/converge.md), [implement.md](https://github.com/github/spec-kit/blob/main/templates/commands/implement.md), accessed 2026-10-08; added 0.11.2 (2026-06-17) | H |
| 7 | Awareness of concurrent sessions/agents | no | Tasks marked `[P]` may run in parallel inside one implement run, and tasks that touch the same file run in order. Each feature gets its own branch and directory. Nothing tracks other live sessions. Community `fleet`, `conduct` and `agent-assign` add orchestration. | [implement.md](https://github.com/github/spec-kit/blob/main/templates/commands/implement.md), accessed 2026-10-08 | M |
| 8 | Improving its own instructions after a rule was not followed | no | No such mechanism in core. The community `improve` extension audits the codebase, not the instructions. | [community catalog](https://github.com/github/spec-kit/blob/main/extensions/catalog.community.json), accessed 2026-10-08 | M |
| 9 | Project overrides that survive updates | yes | Templates resolve in this order: `.specify/templates/overrides/` (project-local), then presets, then extensions, then core. Presets can prepend, append or wrap (0.8.0, 2026-04-23). On upgrade, the install manifest detects locally edited managed files and stops unless `--force` is given. specs/ and constitution.md are preserved. The docs do not state outright that `overrides/` survives an upgrade. | [Presets](https://github.github.io/spec-kit/reference/presets.html), [Upgrade](https://github.github.io/spec-kit/upgrade.html), accessed 2026-10-08 | M |
| 10 | Agent hosts | yes | "50+" integrations, including Copilot (the default), Claude Code, Gemini CLI, Cursor, Codex, Cline, Goose, Devin, Factory Droid, RovoDev and a `generic` option. 32 of them are safe to install side by side. | [Integrations](https://github.github.io/spec-kit/reference/integrations.html), accessed 2026-10-08 | H |

Notes:
- Spec Kit keeps its core thin and pushes most capabilities into extensions and presets. Concurrency, ADRs, resume and drift sync all exist only as community extensions; the catalog does not vouch for their quality.
- The repair direction is explicit: analyze only reports, and converge treats spec, plan and tasks as the ground truth and adds work for the code. Nothing in core repairs a spec to match the code.
- Two items are announced but experimental: an MCP server ("experimental version-only stdio server", 1.1.1, 2026-10-06) and an artifact-list MCP tool (1.1.2, 2026-10-07). `/speckit.taskstoissues` is deprecated in core and moved to the bundled github extension (1.1.0).


---

# Pass 2 — OpenSpec, Superpowers, mattpocock/skills

# Capability survey — OpenSpec, Superpowers, mattpocock/skills (checked 2026-10-08)

GitHub release pages show no year for current-year dates. The year is 2026, confirmed where a release page carries a full date (e.g. Superpowers v6.2.0, 2026-07-23).

## Fission-AI/OpenSpec — latest v1.14.1, 2026-10-06

| # | Question | Answer | How | Source + date | Conf |
|---|---|---|---|---|---|
| 1 | What persists | yes (repo files) | `openspec/specs/` (current truth), `openspec/changes/<name>/` (proposal.md, specs/ deltas, design.md, tasks.md), `openspec/changes/archive/YYYY-MM-DD-<name>/`, `openspec/config.yaml`, `openspec/schemas/`. No DB or hosted service; telemetry is opt-out | [README](https://github.com/Fission-AI/OpenSpec), [commands.md](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md), as of v1.14.1 (2026-10-06) | H |
| 2 | Session orientation | partial (on command) | No hook and no always-loaded file ("No `AGENTS.md` is created or edited"; `update` removes old AGENTS.md marker blocks). The agent reorients on slash commands (`/opsx:apply` picks up at the first unchecked task) and `openspec status`, which ends with a "Next:" line (v1.13.1). Nothing is injected before each message | [supported-tools.md](https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md), [workflows.md](https://github.com/Fission-AI/OpenSpec/blob/main/docs/workflows.md); v1.13.1 2026-09-17 | H |
| 3 | Open questions first-class | partial | design.md template has an "Open Questions" section, a flat list per change ("unknowns that can safely be answered later without changing the specs…"). Not separate items, and no parent/child links or dependencies | [schemas/spec-driven/schema.yaml](https://github.com/Fission-AI/OpenSpec/blob/main/schemas/spec-driven/schema.yaml), main @ 2026-10 | H |
| 4 | Decision records | partial | design.md has a "Decisions" section ("technical choices with rationale; include alternatives considered"). It sits inside each change folder and is archived with it. No standalone decision/ADR log | schema.yaml, main @ 2026-10 | H |
| 5 | Drift check / repair | partial | `openspec validate` checks spec structure (v1.14.1 also rejects requirements over 500 chars). `/opsx:verify` searches the code for evidence the change was implemented and reports CRITICAL/WARNING/SUGGESTION, but only reports and does not repair. Archive/sync merges delta specs into main specs (change → spec). Nothing checks code → spec | [commands.md](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md); [releases](https://github.com/Fission-AI/OpenSpec/releases) v1.14.1 2026-10-06 | H |
| 6 | Verify vs acceptance | yes | `/opsx:verify` (in the expanded profile, set with `openspec config profile`) checks Completeness (tasks, requirements), Correctness (spec intent, scenarios) and Coherence (design.md reflected in code). It does not block archive. Since v1.14.1, apply asks for review before archive once all tasks are checked | commands.md; v1.13.2 2026-09-23 (verify report shows the checks it ran), v1.14.1 2026-10-06 | H |
| 7 | Concurrent sessions/agents | partial | Several active changes can run side by side. Bulk archive detects when two changes touch the same spec and orders them chronologically. No awareness of live sessions or locking | [workflows.md](https://github.com/Fission-AI/OpenSpec/blob/main/docs/workflows.md), main @ 2026-10 | M |
| 8 | Self-improving instructions | no | No such mechanism documented | README/docs, 2026-10 | M |
| 9 | Project overrides survive update | yes | `openspec/config.yaml` holds `context` (goes into every artifact prompt), per-artifact `rules`, and `operations.apply/archive.guidance`. Project schemas live in `openspec/schemas/` (`openspec schema fork`). `update` refreshes only managed skill/command files and "never modifies user-customized configuration files" | [customization.md](https://github.com/Fission-AI/OpenSpec/blob/main/docs/customization.md), supported-tools.md, 2026-10 | H |
| 10 | Hosts | yes (30–40+) | Installs skills plus `opsx-*` commands for each tool: Claude Code, Cursor, GitHub Copilot, Codex, Amazon Q, Cline, Continue, Crush, Devin Desktop, and more. v1.14.0 added ten (Amp, AtomCode, DeepSeek Harness, …) | supported-tools.md; v1.14.0 2026-09-30 | H |

Notes: OpenSpec is centred on the spec. Specs are the source of truth, and changes are deltas merged into them at archive. Decisions and open questions exist only as sections of a per-change design.md. Its main extension point is the schema system plus config.yaml rule injection. It has no session hooks and no always-loaded instructions (it chose to stop editing AGENTS.md). README says "30+ assistants" while supported-tools.md says "40+", so the count is inconsistent.

## obra/superpowers — latest v6.4.2, 2026-09-25

| # | Question | Answer | How | Source + date | Conf |
|---|---|---|---|---|---|
| 1 | What persists | yes (repo files) | Specs go in `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md` and plans in `docs/superpowers/plans/YYYY-MM-DD-<feature>.md` (user can move both). The execution ledger lives in `.superpowers/sdd/<plan-basename>/` and is deleted after a clean final review. Git history is "the durable record". No DB or hosted service | [brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md), [writing-plans](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md) SKILL.md @ 2026-10; [v6.2.0](https://github.com/obra/superpowers/releases/tag/v6.2.0) 2026-07-23 | H |
| 2 | Session orientation | yes (automatic) | A native `SessionStart` hook injects the `using-superpowers` bootstrap (Claude Code, Codex, Cursor, Gemini, Muse, Antigravity…). Pi's extension also re-injects it after compaction; Hermes has no post-compaction hook. The bootstrap is about skills, not project state; resuming a plan happens on command. No per-message injection documented | [README](https://github.com/obra/superpowers), main @ 2026-10 | H (hook) / M (no per-message) |
| 3 | Open questions first-class | no | Questions are settled in brainstorming dialogue. The plan self-review rejects "TBD" lines. No question store | writing-plans SKILL.md, 2026-10 | M |
| 4 | Decision records | partial | A plan is "the set of decisions the implementer cannot make alone". v6.4.2 plans record decisions instead of full code. Decisions sit inside the plan/spec; no separate ADR/decision log | writing-plans SKILL.md; [releases](https://github.com/obra/superpowers/releases) v6.4.2 2026-09-25 | M |
| 5 | Drift check / repair | partial | The spec self-review checks internal consistency ("Do any sections contradict each other?") and the agent fixes the spec inline before user review. The plan pre-flight read checks for internal conflicts (v6.0.0). v6.4.2 self-review checks plan size against spec. Nothing checks docs against code over time | brainstorming SKILL.md 2026-10; [RELEASE-NOTES.md](https://github.com/obra/superpowers/blob/main/RELEASE-NOTES.md) | H |
| 6 | Verify vs acceptance | yes | `verification-before-completion`: "Re-read plan → Create checklist → Verify each → Report gaps"; "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE". Every plan task has a verification step (command + expected output). One fresh whole-branch review runs at the end (v6.4.1) | [verification-before-completion](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md) 2026-10; v6.4.1 2026-09-19 | H |
| 7 | Concurrent sessions/agents | partial | `dispatching-parallel-agents`, `subagent-driven-development`, and `using-git-worktrees` (asks consent since v5.1.0). Plan-scoped workspaces stop plans from colliding (v6.2.0). Covers only subagents it spawns; no awareness of independent sessions | RELEASE-NOTES.md; v6.2.0 2026-07-23 | M |
| 8 | Self-improving instructions | partial | `writing-skills` runs a TDD loop for skills: pressure-test, rationalization tables, "Agent found new rationalization? Add explicit counter". `diagnosing-superpowers` (v6.4.1) reads session transcripts, reports with path:line evidence, and drafts an upstream GitHub issue. It does not amend skills itself | [writing-skills](https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md) 2026-10; [v6.4.1](https://github.com/obra/superpowers/releases/tag/v6.4.1) 2026-09-19 | H |
| 9 | Project overrides survive update | partial | Precedence rule: the user's CLAUDE.md/AGENTS.md and direct requests beat skills (v5.0.0, v6.0.0). Spec/plan location preferences override defaults. Personal skills go in `~/.claude/skills/` or `~/.agents/skills/`. Overriding a single core skill per project is not documented. Update = reinstall the plugin | RELEASE-NOTES.md; writing-skills SKILL.md, 2026-10 | M |
| 10 | Hosts | yes (16) | Claude Code, Antigravity, Codex App, Codex CLI, Cursor, Devin CLI, Factory Droid, Gemini CLI, GitHub Copilot CLI, Grok Build CLI, Kimi Code, OpenCode, Pi, Qwen Code, Hermes Agent, Muse | README @ 2026-10; v6.3.0 2026-08-12, v6.4.1 2026-09-19 | H |

Notes: Superpowers is centred on skills and the process. Orientation is automatic, but what gets injected is the "use your skills" bootstrap, not project memory. Its persistent artifacts are dated specs and plans, and the run ledger is temporary. Verification discipline is its strongest point. Its "self-improvement" means skill-authoring tests plus upstream diagnosis, not an in-project rule-amendment loop. Release cadence is high: 6.1.1 (2026-07-02) to 6.4.2 (2026-09-25).

## mattpocock/skills — latest v1.3.1, 2026-10-04

| # | Question | Answer | How | Source + date | Conf |
|---|---|---|---|---|---|
| 1 | What persists | yes (repo files + hosted tracker) | `GLOSSARY.md`/`GLOSSARY-MAP.md` (renamed from CONTEXT.md in v1.3.0), `docs/adr/`, `docs/agents/{issue-tracker,domain,triage-labels}.md`. Tickets go to GitHub/GitLab issues or local `.scratch/<feature>/issues/NN-slug.md`. `/handoff` writes to the OS temp dir, which is not durable | [setup SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/setup-matt-pocock-skills/SKILL.md), [to-tickets](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/to-tickets/SKILL.md), [CHANGELOG](https://github.com/mattpocock/skills/blob/main/CHANGELOG.md) v1.3.0 2026-10-04 | H |
| 2 | Session orientation | partial | Setup adds a "## Agent skills" pointer section to CLAUDE.md (or AGENTS.md), which the host always loads. No hook. `/handoff` (manual) writes a note for the next session, and `/ask-matt` routes to skills. No per-message injection | setup SKILL.md; [handoff](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/handoff/SKILL.md), 2026-10 | H |
| 3 | Open questions first-class | yes | `/wayfinder` keeps "decision tickets" as child issues under a `wayfinder:map` parent. Native tracker blocking links show the frontier. A resolution comment closes each one and is appended to the map's "Decisions-so-far". Planning is kept apart from implementation tickets | [wayfinder SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/wayfinder/SKILL.md); v1.1.0 graduation, v1.2.0 2026-08-05 | H |
| 4 | Decision records | yes | `domain-modeling` writes ADRs to `docs/adr/` only when a decision is hard to reverse, surprising, and a real trade-off. The glossary stays free of implementation detail. Wayfinder resolutions are a second, tracker-side record | [domain-modeling SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/domain-modeling/SKILL.md), 2026-10 | H |
| 5 | Drift check / repair | partial | During grilling, domain-modeling compares the user's statements with the code ("Your code cancels entire Orders… Which is right?"). The user picks which side to fix, and the glossary is updated immediately. No standing doc-vs-code audit; code-review explicitly leaves ADR/glossary currency out | domain-modeling, [code-review](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/code-review/SKILL.md) SKILL.md, 2026-10 | M |
| 6 | Verify vs acceptance | yes | Tickets carry acceptance-criteria checkboxes. `code-review` runs a separate Spec axis sub-agent (missing/partial requirements, scope creep, wrong implementations) apart from the Standards axis. `/implement-spec` runs code-review on the integration branch once all tickets are done | to-tickets, code-review, [implement-spec](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/implement-spec/SKILL.md) SKILL.md; implement-spec graduated v1.3.0 2026-10-04 | H |
| 7 | Concurrent sessions/agents | partial | `/implement-spec` runs parallel implementer subagents, each in its own worktree and branch, picking from a frontier of unblocked tickets and merging into an integration branch. Nothing covers independent sessions | implement-spec SKILL.md, 2026-10 | H |
| 8 | Self-improving instructions | partial | `/retro` (graduated v1.3.0) reviews a session and suggests environment fixes: navigation, automated checks, coding standards, and "steering instructions in AGENTS.md that should be moved to coding standards (or automated checks)". It moves rules elsewhere rather than rewording them; no failure register | [retro SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/retro/SKILL.md); v1.3.0/1.3.1 2026-10-04 | M |
| 9 | Project overrides survive update | partial | Project choices live in `docs/agents/*.md` and the CLAUDE.md section. Repo standards override code-review's Fowler baseline (v1.1.0). `npx skills add` copies editable skills into the repo; the plugin install is read-only and auto-updates. Whether re-running npx keeps local edits is not documented | [README](https://github.com/mattpocock/skills), CHANGELOG v1.1.0/v1.2.0, 2026-10 | M |
| 10 | Hosts | partial | Claude Code (native plugin since v1.2.0, plus npx) and Codex (`agents/openai.yaml` since v1.3.0). Other agents via the `npx skills` installer, without host-specific metadata | README; CHANGELOG v1.2.0 2026-08-05, v1.3.0 2026-10-04 | M |

Notes: mattpocock/skills is a loose toolkit, not one enforced loop. Its distinctive pieces are wayfinder's decision tickets (open decisions as first-class, dependency-linked items) and ADRs with a strict "when to write" test. Durable state is split between repo docs and an external issue tracker, which may be hosted. v1.3.0 and v1.3.1 shipped one minute apart on 2026-10-04; 1.3.1 is a routing fix in `ask-matt`.


---

# Pass 3 — beads, Backlog.md, Cline

# Capability survey 3: beads, Backlog.md, Cline

Researched 2026-10-08 from each tool's current docs, README, changelog and release pages. Where a page carries no date of its own, the date given is the access date (2026-10-08), tied to the latest release.

## beads (gastownhall/beads)

Latest stable: **v1.3.1, 2026-09-30**. Pre-release v1.3.2-rc.1 came out 2026-10-05 ([releases](https://github.com/gastownhall/beads/releases)). The docs live at beads.gascity.com.

| # | Question | Answer | How | Source + date | Conf. |
|---|---|---|---|---|---|
| 1 | What persists | yes | A Dolt (versioned SQL) database stored in the repo at `.beads/embeddeddolt/`, or an external `dolt sql-server` when several writers need it. Sync runs through `bd dolt push/pull` to `refs/dolt/data` on the git remote. `issues.jsonl` is an export only. Memories (`bd remember`) are kept in the same database. | [README](https://github.com/gastownhall/beads), accessed 2026-10-08 (v1.3.1) | H |
| 2 | Orientation at session start | yes | `bd setup claude` installs a SessionStart hook that runs `bd prime --hook-json`. The hook prints about 1–2k tokens of workflow context plus the stored memories, and it fires again after compaction. It also adds a short beads section to CLAUDE.md. Equivalent setups exist for Gemini CLI and Codex. Nothing is injected before every user message. | [Claude Code integration](https://beads.gascity.com/integrations/claude-code.md), [bd prime](https://beads.gascity.com/cli-reference/prime.md), accessed 2026-10-08 | H |
| 3 | Open questions as first-class items | partial | There is no "question" type. Items needing a human carry the `human` label and are handled with `bd human list/respond/dismiss`. Because they are ordinary issues, they get parent-child links, `blocks` dependencies and gates. | [bd types](https://beads.gascity.com/cli-reference/types.md), [bd human](https://beads.gascity.com/cli-reference/human.md), accessed 2026-10-08 | M |
| 4 | Decisions kept as separate records | partial | `decision` is a core issue type (alongside bug, task, feature, chore and epic), with `--design` and `--notes` fields. It lives in the same tracker as tasks, so it is not a separate record kind and has no rationale or alternatives template. Graph links `supersedes` and `relates-to` are available. | [bd types](https://beads.gascity.com/cli-reference/types.md), [bd create](https://beads.gascity.com/cli-reference/create.md), accessed 2026-10-08 | M |
| 5 | Drift check and repair | partial | Only the tracker is checked; docs are not checked against code. `bd orphans` finds issues named in commit messages that are still open, and `--fix` closes them (the tracker is repaired to match the code). `bd lint` flags issues missing recommended sections. `bd stale` lists abandoned items. `bd doctor` checks the installation. | [bd orphans](https://beads.gascity.com/cli-reference/orphans.md), [bd lint](https://beads.gascity.com/cli-reference/lint.md), accessed 2026-10-08 | H |
| 6 | Verification against acceptance criteria as its own step | partial | There is an `--acceptance` field, and `bd lint` expects an Acceptance Criteria section on bug, task and feature. Gates can block `bd close` unless `--force` is used. There is no verify step that checks the criteria. | [bd create](https://beads.gascity.com/cli-reference/create.md), [bd close](https://beads.gascity.com/cli-reference/close.md), accessed 2026-10-08 | M |
| 7 | Aware of concurrent sessions/agents | yes | Atomic `bd update --claim` (first claim wins), assignees, and `merge-slot` (an exclusive lock that one agent holds at a time). Hash IDs avoid collisions. Server mode supports concurrent writers. Worktrees share one `.beads`. Agents also have mail/messages and federation. | [Agent coordination](https://beads.gascity.com/multi-agent/coordination.md), [README](https://github.com/gastownhall/beads), accessed 2026-10-08 | H |
| 8 | Improving its own instructions after a missed rule | partial | `bd rules audit` scans `.claude/rules/` for contradictions and merge candidates, and `bd rules compact` merges them. `bd remember` stores durable facts. Neither is triggered by a rule failing to fire. | [bd rules](https://beads.gascity.com/cli-reference/rules.md), accessed 2026-10-08 | M |
| 9 | Project rule overrides that survive updates | yes | `.beads/PRIME.md` (one in the clone, or one in the workspace) fully replaces the default `bd prime` output, and `--export` dumps the default text to start from. Projects also have `.beads/config.yaml`, including `types.custom`, and `no-git-ops`. | [bd prime](https://beads.gascity.com/cli-reference/prime.md), [CHANGELOG](https://raw.githubusercontent.com/gastownhall/beads/main/CHANGELOG.md) (Unreleased), accessed 2026-10-08 | H |
| 10 | Agent hosts | yes | Integration pages exist for Claude Code (plus a plugin), Codex, Gemini CLI, Cursor, Factory Droid, Mux, Aider, Cody, Junie, Kilo Code, Kiro CLI, OpenCode, Windsurf and GitHub Copilot. The MCP server (`beads-mcp`) is for hosts without a CLI, such as Claude Desktop. | [docs index](https://beads.gascity.com/llms.txt), accessed 2026-10-08 | H |

Notes:
- beads is a tracker and coordination substrate. Orientation reaches the agent only through a host hook (`bd prime`). Decisions are one issue type among others, not a separate record kind.
- Its only drift repair runs from code to tracker (`bd orphans --fix` closes items). It has no doc/spec layer to keep in agreement.
- The `decision` type appears in `bd types` and `bd create`, but the "Issues & Dependencies" concept page still lists five types, so the docs disagree with each other here.

## Backlog.md (MrLesk/Backlog.md)

Latest: **v1.53.0, 24 Sep (2026)**, which added pagination and cut idle CPU. v1.52.0 (12 Sep) added `--watch` JSON streaming ([releases](https://github.com/MrLesk/Backlog.md/releases)). The release page shows no year; 2026 is inferred from the release sequence.

| # | Question | Answer | How | Source + date | Conf. |
|---|---|---|---|---|---|
| 1 | What persists | yes | Plain Markdown files with frontmatter in a `backlog/` folder in the repo, holding tasks, drafts, docs, decisions, milestones, completed and archive. Config is in `backlog.config.yml`. Local-first: no server, no account. | [README](https://github.com/MrLesk/Backlog.md), [ADVANCED-CONFIG](https://raw.githubusercontent.com/MrLesk/Backlog.md/HEAD/ADVANCED-CONFIG.md), accessed 2026-10-08 (v1.53.0) | H |
| 2 | Orientation at session start | yes (instruction-driven) | `backlog init` writes a short nudge into CLAUDE.md, AGENTS.md, GEMINI.md or copilot-instructions: "At the beginning of each conversation, run `backlog instructions overview`". In MCP mode the server's overview resource and nudge play the same role. No hook, and nothing is injected per message. | [cli-agent-nudge.md](https://raw.githubusercontent.com/MrLesk/Backlog.md/main/src/guidelines/cli-agent-nudge.md), [src/cli.ts](https://raw.githubusercontent.com/MrLesk/Backlog.md/main/src/cli.ts), accessed 2026-10-08 | H |
| 3 | Open questions as first-class items | no | Questions go into task comments (`--comment`), and the overview says to skip creating tasks for questions. A decision record can carry `status: proposed`, but decisions have no hierarchy or dependencies. Tasks themselves do have parent/subtasks, dependencies and milestones. | [overview.md](https://raw.githubusercontent.com/MrLesk/Backlog.md/main/src/guidelines/cli-instructions/overview.md), [agent-guidelines.md](https://raw.githubusercontent.com/MrLesk/Backlog.md/main/src/guidelines/agent-guidelines.md), accessed 2026-10-08 | M |
| 4 | Decisions kept as separate records | yes | `backlog decision create/list` writes ADR-style files to `backlog/decisions/`. Frontmatter: id, title, date, status. Sections: Context, Decision, Consequences, References. Long-lived reference material goes to `backlog/docs/`. | [backlog/decisions](https://github.com/MrLesk/Backlog.md/tree/main/backlog/decisions) (decision-1, 2025-06-22), accessed 2026-10-08 | H |
| 5 | Drift check and repair | no | No check of docs or tasks against code. `checkActiveBranches` reconciles task state across active git branches (tracker against tracker), and the guidelines prevent drift only by forbidding direct edits to the Markdown. | [ADVANCED-CONFIG](https://raw.githubusercontent.com/MrLesk/Backlog.md/HEAD/ADVANCED-CONFIG.md), accessed 2026-10-08 | M |
| 6 | Verification against acceptance criteria as its own step | yes | Finalization is a separate guide. It requires evidence for every acceptance criterion and DoD item ("Code presence, grep output... are not verification evidence"), relevant tests run, ticks via `--check-ac N` / `--check-dod N`, a Final Summary, and user review before Done. The verifier is the same agent; no separate checker. | [task-finalization.md](https://raw.githubusercontent.com/MrLesk/Backlog.md/main/src/guidelines/cli-instructions/task-finalization.md), accessed 2026-10-08 | H |
| 7 | Aware of concurrent sessions/agents | partial | Each agent assigns itself (`-a @myself`) and logs progress in notes. Cross-branch checking tracks task state on other active branches and avoids ID collisions. `--watch` gives full-replacement JSON streams. The model is "one task = one context window = one PR". No locks or atomic claim. | [agent-guidelines.md](https://raw.githubusercontent.com/MrLesk/Backlog.md/main/src/guidelines/agent-guidelines.md), [README](https://github.com/MrLesk/Backlog.md), accessed 2026-10-08 | M |
| 8 | Improving its own instructions after a missed rule | no | Nothing found. The workflow guides ship inside the CLI and are read through `backlog instructions`. | [src/guidelines](https://github.com/MrLesk/Backlog.md/tree/main/src/guidelines), accessed 2026-10-08 | M |
| 9 | Project rule overrides that survive updates | partial | `backlog.config.yml` (DoD defaults, statuses, git behaviour, `onStatusChange` command) and the project's own agent files are the project's to keep. The workflow guide text is bundled in the binary, and no override for it is documented. | [ADVANCED-CONFIG](https://raw.githubusercontent.com/MrLesk/Backlog.md/HEAD/ADVANCED-CONFIG.md), accessed 2026-10-08 | M |
| 10 | Agent hosts | yes | CLI mode writes instruction files for Claude Code (CLAUDE.md), Codex/Cursor/Zed/Warp/Aider/RooCode (AGENTS.md), Gemini (GEMINI.md) and Copilot. The MCP wizard sets up Claude Code, Codex, Gemini CLI and Kiro, with "Other" for the rest (the init text also mentions Cursor). | [src/cli.ts](https://raw.githubusercontent.com/MrLesk/Backlog.md/main/src/cli.ts), accessed 2026-10-08 | H |

Notes:
- Its loop is spec review, then plan review, then code review, with a human checkpoint at each. Its acceptance-criteria and DoD finalization is the strongest verification step of the three tools.
- Decisions are real ADR records, but open questions have no home beyond task comments.
- The workflow lives in guidance text bundled with the CLI and is pulled on demand, so a project tunes config, not the guide.

## Cline (cline/cline)

Latest extension: **v4.1.23, 7 Oct (2026)**. CLI v3.0.70 and SDK v0.0.92 are dated 8 Oct, and Desktop v0.0.44 is dated 7 Oct ([releases](https://github.com/cline/cline/releases)). The release-page summary read the year as 2024, but the notes mention 2026-era models, so 2026 is taken as the real year. v4.0.0 moved the extension onto the shared Cline SDK (changelog entries are undated).

| # | Question | Answer | How | Source + date | Conf. |
|---|---|---|---|---|---|
| 1 | What persists | yes | In the repo: rules files (`.clinerules/` or `.cline/rules/`), and the Memory Bank `memory-bank/` folder if the user adopts that pattern (projectbrief, productContext, activeContext, systemPatterns, techContext, progress). Elsewhere: global rules in `~/Documents/Cline/Rules`, plus local task history and checkpoints. No built-in memory store; persistent memory comes from third parties via hooks or MCP. | [Memory Bank](https://docs.cline.bot/features/memory-bank), [Rules](https://docs.cline.bot/customization/cline-rules.md), accessed 2026-10-08 | H |
| 2 | Orientation at session start | yes | Rules load into every task. The Memory Bank instruction says "read ALL memory bank files at the start of EVERY task". Hooks (TaskStart; v4 SDK `before_agent_start`) can inject context. Something can be injected before messages too: UserPromptSubmit hooks with `contextModification`, and Focus Chain re-injects the todo list every 6 messages by default. | [Memory Bank](https://docs.cline.bot/features/memory-bank), [v3.36 hooks post](https://cline.bot/blog/cline-v3-36-hooks) (2025-11-06), [SDK plugins](https://docs.cline.bot/sdk/plugins), accessed 2026-10-08 | M |
| 3 | Open questions as first-class items | no | No question store. Under the Memory Bank pattern, "active decisions and considerations" are prose in `activeContext.md`. Focus Chain is a flat todo checklist. | [Memory Bank](https://docs.cline.bot/features/memory-bank), accessed 2026-10-08 | H |
| 4 | Decisions kept as separate records | partial | Only through the Memory Bank pattern: `systemPatterns.md` holds key technical decisions and `activeContext.md` holds active ones. These are prose sections, not individual records. | [Memory Bank](https://docs.cline.bot/features/memory-bank), accessed 2026-10-08 | M |
| 5 | Drift check and repair | partial | The "update memory bank" command has the agent re-read every memory-bank file and rewrite them to match the current state (docs repaired toward the code). It is manual and part of the pattern, not a built-in check. | [Memory Bank](https://docs.cline.bot/features/memory-bank), accessed 2026-10-08 | M |
| 6 | Verification against acceptance criteria as its own step | no | Plan and Act modes plus Deep Planning (`/deep-planning`) cover planning, and checkpoints allow rollback. There is no acceptance-criteria step, though a TaskComplete hook or rule could add one. | [docs index](https://docs.cline.bot/llms.txt), accessed 2026-10-08 | M |
| 7 | Aware of concurrent sessions/agents | partial | Agent Teams (SDK, CLI, Kanban only; not in the VS Code or JetBrains extensions) provide a shared task board, an inter-agent mailbox and a mission log under `~/.cline/data/teams/`. Subagents run parallel research and are temporarily disabled in the VS Code extension since v4.0.0. Independent sessions are not aware of each other. | [Agent Teams](https://docs.cline.bot/cli/agent-teams.md), [CHANGELOG](https://raw.githubusercontent.com/cline/cline/main/CHANGELOG.md), accessed 2026-10-08 | M |
| 8 | Improving its own instructions after a missed rule | partial | The "self-improving Cline" pattern has the user ask Cline to refine a `.clinerule` from feedback, and `/newrule` generates rules. Both are started by the user; no failure trigger or register. | [blog: toggleable clinerules / self-improving Cline](https://cline.bot/blog/double-clicking-on-toggleable-clinerules-self-improving-cline) (v3.13 era), [Rules](https://docs.cline.bot/customization/cline-rules.md), accessed 2026-10-08 | M |
| 9 | Project rule overrides that survive updates | yes | Workspace `.clinerules/` (or `.cline/rules/`, `.cursorrules`, `.windsurfrules`, AGENTS.md) is combined with global rules, and workspace wins on conflict. Rules can be toggled per rule, and `paths:` frontmatter makes a rule conditional. Updates do not touch these files. | [Rules](https://docs.cline.bot/customization/cline-rules.md), accessed 2026-10-08 | H |
| 10 | Agent hosts | yes (it is the host) | Cline is its own agent: VS Code extension (and VS Code forks), JetBrains extension, CLI, Desktop app, SDK, Kanban, and ACP clients (Zed, JetBrains, Neovim, Emacs and others). It reads AGENTS.md, `.cursorrules` and `.windsurfrules` for cross-tool rules. | [ACP](https://docs.cline.bot/usage/acp.md), [releases](https://github.com/cline/cline/releases), accessed 2026-10-08 | M |

Notes:
- The Memory Bank is a custom-instructions pattern, not a shipped feature. Its decisions, progress and drift repair are all prose the agent keeps up when asked.
- In v4 the hooks docs now point to SDK Plugins (`run_start`, `before_agent_start`, `tool_call_before/after`, `run_end`). The v4.0.0 changelog says `.clinerules/hooks` scripts still run, but the old hook reference page is now a stub. The 2025 post said hooks ran on macOS and Linux only; current Windows support is not stated.
- Focus Chain shipped in v3.25 and is still mentioned in the v4.1.20 changelog, but its docs page now redirects to the slash-commands page. Its current status is M confidence.


---

# Pass 4 — claude-mem, Kiro, Agent OS, cc-sdd, Claude Code memory

# Capability survey: memory, method and project-context tools (as of 2026-10-08)

Sources were read on 2026-10-08. A date in brackets is the release or page date the source shows. "n.d." means the page shows no date, and the claim stands as of the read date. Claims about GitHub repos come from the README, releases or commits on 2026-10-08.

---

## thedotmack/claude-mem

Latest version: **v13.34.2, 2026-10-06** ([releases](https://github.com/thedotmack/claude-mem/releases)). Very fast release cadence: v13.29.0 to v13.34.2 shipped between Oct 3 and Oct 6.

| # | Question | Answer | How | Source + date | Conf. |
|---|---|---|---|---|---|
| 1 | What persists, in what form | yes | Stored outside the repo: a local SQLite DB (sessions, observations, summaries) plus an optional Chroma vector index, both under `~/.claude-mem`. Optional folder `CLAUDE.md` files inside the repo (off by default). Optional hosted multi-device sync through cmem.ai Pro, which is paid with a 30-day trial. A hosted server is marked Beta. | [architecture/hooks](https://docs.claude-mem.ai/architecture/hooks.md) (n.d.); [cloud-sync](https://docs.claude-mem.ai/cloud-sync.md) (n.d.); [v13.34.1](https://github.com/thedotmack/claude-mem/releases) [2026-10-06] | H |
| 2 | Session orientation | yes (automatic) | The SessionStart hook injects recent observations as `additionalContext`: 50 by default, filterable by type, capped at 10,000 characters, with open work-state items at the top. The documented UserPromptSubmit hook only records the prompt (`suppressOutput`) and injects nothing per message. | [hooks](https://docs.claude-mem.ai/architecture/hooks.md) (n.d.); [v13.29.0](https://github.com/thedotmack/claude-mem/releases/tag/v13.29.0) [2026-10-03] | M (the hooks page may predate the v13.30 hook rework) |
| 3 | Open questions as first-class items | partial | There is no question type. `work_state_write`/`work_state_read` keep named lists of to-dos (`todo/doing/done/dropped`) plus free key/value state, append-only and last-write-wins. Items have no parent/child links and no dependencies. | [v13.29.0](https://github.com/thedotmack/claude-mem/releases/tag/v13.29.0) [2026-10-03] | M |
| 4 | Decision records separate from tasks/specs | partial | An AI compressor writes observations and tags each with a type, including `decision`, in the DB. They are auto-extracted narratives rather than curated records, and they carry no status or supersession. | [configuration](https://docs.claude-mem.ai/configuration.md) (n.d.) | M |
| 5 | Drift check / repair | no | Nothing compares memory with code or docs. Folder `CLAUDE.md` files are regenerated from observations, which is a refresh, not a check. | [folder-context](https://docs.claude-mem.ai/usage/folder-context.md) (n.d.) | M |
| 6 | Verification vs acceptance criteria | no | Nothing documented. | README, docs index [2026-10-08] | M |
| 7 | Concurrent sessions/agents | partial | Each session is keyed by its host `session_id`, and several sessions in one project keep separate streams. Work state is scoped across worktrees. Cloud sync merges devices. Nothing coordinates live sessions with each other. | [hooks](https://docs.claude-mem.ai/architecture/hooks.md) (n.d.); [v13.29.0](https://github.com/thedotmack/claude-mem/releases/tag/v13.29.0) | M |
| 8 | Self-improving instructions | no | It remembers what happened. It does not amend instructions. | docs index [2026-10-08] | M |
| 9 | Project rule overrides survive update | partial | Settings live only at user level in `~/.claude-mem/settings.json` and survive reinstall. There is no per-project override file. In folder `CLAUDE.md` files, text you write outside the `<claude-mem-context>` tags is kept when the file is regenerated. | [configuration](https://docs.claude-mem.ai/configuration.md); [folder-context](https://docs.claude-mem.ai/usage/folder-context.md) (n.d.) | M |
| 10 | Hosts | yes (many) | Claude Code, Codex, Gemini, Copilot, OpenCode, Cursor, OpenClaw, Hermes, Antigravity CLI, Kimi Code, T3 Code, Grok Bot, Claude Desktop (via MCP). Pi and DeepSeek Harness were added in v13.34.0. | [README](https://github.com/thedotmack/claude-mem) [2026-10-08]; [v13.34.0](https://github.com/thedotmack/claude-mem/releases) [2026-10-06] | H |

Notes: claude-mem is a capture-and-recall layer. It records what happened through lifecycle hooks and re-injects it at session start. It does not carry a method. The project is now commercial: cmem.ai Pro sync, a trial, a hosted server in beta. The to-do "work state" added on 2026-10-03 is its first step toward tracking open work, but the lists are flat. Docs pages carry no dates, and the architecture page may lag the v13.30 hook changes.

---

## Kiro (AWS): steering, specs, hooks

Latest versions: **CLI 2.28.0, 2026-10-05** and **IDE 1.2.4, 2026-09-30**. Kiro Crew 0.7.0 shipped 2026-09-24 ([changelog](https://kiro.dev/changelog/)). Kiro is now several surfaces: IDE, CLI (V3 replacing "Classic"), Web, and Crew, an open-source agent workspace announced 2026-08-04.

| # | Question | Answer | How | Source + date | Conf. |
|---|---|---|---|---|---|
| 1 | What persists, in what form | yes | Files in the repo: `.kiro/steering/*.md`, `.kiro/specs/<feature>/{requirements,design,tasks}.md`, `.kiro/hooks/*.json`. Global steering lives in `~/.kiro/steering`. Kiro Web keeps a hosted per-user "memory". Crew persists sessions, memory and checkpoints on your own machine. | [steering](https://kiro.dev/docs/steering/) [2026-10-06]; [hooks](https://kiro.dev/docs/hooks/) [2026-09-30]; [web memory](https://kiro.dev/docs/web/memory/) (n.d.) | H |
| 2 | Session orientation | yes (automatic) | Steering files with `inclusion: always` load in every interaction. Others load by `fileMatch`, by `auto` (description match) or manually. AGENTS.md is discovered automatically. Session Start and Prompt Submit hooks can add context, and Prompt Submit runs per message, but only if the user configures it. | [steering](https://kiro.dev/docs/steering/) [2026-10-06]; [hook types](https://kiro.dev/docs/hooks/types/) (n.d.) | H |
| 3 | Open questions as first-class items | no | Only tasks are first-class. `tasks.md` has a dependency graph that runs in waves. Questions have no item type. | [specs](https://kiro.dev/docs/specs/) [2026-10-02] | M |
| 4 | Decision records separate | partial | Design rationale sits inside each spec's `design.md`. There is no ADR or decision log separate from specs. | [specs](https://kiro.dev/docs/specs/) [2026-10-02] | M |
| 5 | Drift check / repair | partial | "Sync Files" regenerates tasks after requirements or design change and marks tasks complete by scanning the code. You can also ask Kiro to "check which tasks are already complete". The repair runs both ways, but on the code-to-spec side only task status is updated. Requirements and design are not checked against the code automatically. | [specs best practices](https://kiro.dev/docs/specs/best-practices/) [2026-09-25] | M |
| 6 | Verification vs acceptance criteria | partial | "Spec correctness" turns EARS requirements into properties and runs property-based tests against the code. It is optional and IDE-only. On a failure the user decides whether to fix the code, the test or the requirement. | [correctness](https://kiro.dev/docs/specs/correctness/) [2026-08-04] | H |
| 7 | Concurrent sessions/agents | partial | Independent spec tasks run in parallel. CLI 2.27 added sub-agent delegation, and Web/IDE got background Workflows on 2026-09-30. Crew runs concurrent managed sessions through a Gateway. Nothing makes separate user-started IDE/CLI sessions aware of each other. | [specs](https://kiro.dev/docs/specs/) [2026-10-02]; [changelog](https://kiro.dev/changelog/) [2026-09-30/10-01]; [Crew blog](https://kiro.dev/blog/introducing-kiro-crew/) | M |
| 8 | Self-improving instructions | partial | Kiro Web "memory" learns from PR feedback, can be viewed and deleted, and is user-scoped. It does not amend steering, and it is not documented for the IDE or CLI. | [web memory](https://kiro.dev/docs/web/memory/) (n.d.) | M |
| 9 | Project rule overrides survive update | yes | Steering, specs and hooks are project files the product does not overwrite. Workspace steering takes priority over global steering. Team steering can be distributed through MDM or a repo. | [steering](https://kiro.dev/docs/steering/) [2026-10-06] | H |
| 10 | Hosts | partial | Kiro's own IDE, CLI, Web and Crew. Crew 0.7.0 previews other agent backends (OpenCode, goose, Pi). Kiro reads AGENTS.md; its specs are plain Markdown other tools can read. | [changelog](https://kiro.dev/changelog/) [2026-09-24] | H |

Notes: Kiro is the reference shape for spec-driven development: steering, then requirements (EARS), design and tasks, with hooks and property-based tests on top. Its strengths are always-on steering and specs checked by property tests. It has no question store and no separate decision log, and spec sync covers task status only. Memory exists only in Kiro Web and learns from PR comments. In 2026 most of the momentum went to multi-surface work (Workflows, Crew), not to the spec method itself.

---

## buildermethods/agent-os

Latest version: **3.0, 2026-01-20** ([CHANGELOG](https://raw.githubusercontent.com/buildermethods/agent-os/main/CHANGELOG.md)). Two shell-script fixes (#327, #328) were merged on 2026-05-05 and are still listed as "Unreleased". The commit on 2026-10-07 (#353) only removes maintainer provisioning scripts and does not affect users ([PR #353](https://github.com/buildermethods/agent-os/pull/353)). The project looks largely dormant since January.

| # | Question | Answer | How | Source + date | Conf. |
|---|---|---|---|---|---|
| 1 | What persists, in what form | yes | Files in the repo under `agent-os/`: `standards/` with an `index.yml`, `product/` (mission, roadmap, tech stack) and `specs/<spec>/` (plan.md, shape.md, standards.md, references.md, visuals/). Base profiles live in `~/agent-os`. | [shape-spec.md](https://raw.githubusercontent.com/buildermethods/agent-os/main/commands/agent-os/shape-spec.md); [project-install.sh](https://raw.githubusercontent.com/buildermethods/agent-os/main/scripts/project-install.sh) [v3.0, 2026-01-20] | H |
| 2 | Session orientation | no (on command) | Nothing loads automatically. The user runs `/inject-standards`, which suggests or injects standards matched through `index.yml`; `/shape-spec` also calls it. There are no hooks and nothing is injected per message. | [inject-standards.md](https://raw.githubusercontent.com/buildermethods/agent-os/main/commands/agent-os/inject-standards.md) [v3.0] | H |
| 3 | Open questions as first-class items | no | `/shape-spec` asks its questions live through AskUserQuestion and does not keep them as items. | [shape-spec.md](https://raw.githubusercontent.com/buildermethods/agent-os/main/commands/agent-os/shape-spec.md) [v3.0] | H |
| 4 | Decision records separate | partial | Each spec's `shape.md` records "key decisions" and constraints. There is no project-level decision log: v1.4.1 replaced decision tracking with "Recaps" (2025). | [shape-spec.md](https://raw.githubusercontent.com/buildermethods/agent-os/main/commands/agent-os/shape-spec.md); [releases](https://github.com/buildermethods/agent-os/releases) | M |
| 5 | Drift check / repair | partial | `/discover-standards` extracts standards from the code, so code feeds the docs. A sync script pushes project standards back into the base profile. No check compares standards or specs with the code. | [CHANGELOG 3.0](https://raw.githubusercontent.com/buildermethods/agent-os/main/CHANGELOG.md) [2026-01-20] | M |
| 6 | Verification vs acceptance criteria | no | v3.0 retired the implementation and orchestration phases and leaves execution to the host's plan mode. v2.1.0 had already removed the documentation-verification requirements. | [CHANGELOG 3.0](https://raw.githubusercontent.com/buildermethods/agent-os/main/CHANGELOG.md); [releases](https://github.com/buildermethods/agent-os/releases) | H |
| 7 | Concurrent sessions/agents | no | Nothing documented. The subagent options of v2 were retired in v3. | [CHANGELOG 3.0](https://raw.githubusercontent.com/buildermethods/agent-os/main/CHANGELOG.md) | M |
| 8 | Self-improving instructions | no | `/discover-standards` captures conventions from the code. Nothing reacts to an agent not following a rule. | [workflow](https://buildermethods.com/agent-os/workflow) (n.d.) | M |
| 9 | Project rule overrides survive update | partial | Profiles inherit through `config.yml`. A project re-install overwrites `standards/` (after a y/N prompt) unless you pass `--commands-only`. Commands are always overwritten. | [project-install.sh](https://raw.githubusercontent.com/buildermethods/agent-os/main/scripts/project-install.sh) [v3.0] | H |
| 10 | Hosts | partial | Claude Code is primary (commands installed into `.claude/commands/agent-os/`, and `/shape-spec` requires plan mode). The README also names Cursor, Antigravity and "other AI tools" that can read the Markdown. | [README](https://github.com/buildermethods/agent-os) [2026-10-08] | M |

Notes: v3 is a deliberate retreat. Agent OS now covers coding standards (discover, index, inject) plus a plan-mode spec shaper, and leaves task breakdown, implementation and verification to the host. That makes it the least stateful tool here. It has no session-start load, no questions, no verification and no concurrency handling. Its idea worth keeping is standards discovered from the code and kept in an index for selective injection.

---

## Newer entrant 1: gotalab/cc-sdd (Kiro-style SDD for other agents)

Why it belongs: it ports Kiro's spec method (steering, then EARS requirements, design, tasks) to eight non-Kiro hosts as Agent Skills. v3.0 (2026-04-09) rebuilt it around long-running autonomous implementation with independent review. It has about 3.7k stars. Latest version: **v3.1.0, 2026-09-23** ([releases](https://github.com/gotalab/cc-sdd/releases)).

| # | Question | Answer | How | Source + date | Conf. |
|---|---|---|---|---|---|
| 1 | What persists, in what form | yes | Files in the repo: `.kiro/steering/`, `.kiro/specs/<feature>/` (requirements, design, research, tasks, spec.json) and `.kiro/settings/{templates,rules}/`. | [README](https://github.com/gotalab/cc-sdd) [v3.1.0, 2026-09-23]; [templates/specs](https://github.com/gotalab/cc-sdd/tree/main/tools/cc-sdd/templates/shared/settings/templates/specs) | H |
| 2 | Session orientation | partial | The installer writes an instruction file (`CLAUDE.md` for Claude Code) that tells the agent to load the core steering files for spec and implementation work. That is conditional and instruction-driven, not a hook. `/kiro-spec-status` and `/kiro-discovery` run on command. Nothing is injected per message. | [CLAUDE.md template](https://raw.githubusercontent.com/gotalab/cc-sdd/main/tools/cc-sdd/templates/agents/claude-code-skills/docs/CLAUDE.md) [main, 2026-10-08] | M |
| 3 | Open questions as first-class items | no | `research.md` holds risks and per-decision "follow-up" fields, and tasks carry `_Depends:_`/`_Boundary:_` annotations. Questions have no item type. | [research.md template](https://raw.githubusercontent.com/gotalab/cc-sdd/main/tools/cc-sdd/templates/shared/settings/templates/specs/research.md) | M |
| 4 | Decision records separate | yes (per spec) | `research.md` has a "Design Decisions" section with context, alternatives, selected approach, rationale, trade-offs and follow-up, kept apart from requirements and tasks. It is scoped to the spec, not the project. | [research.md template](https://raw.githubusercontent.com/gotalab/cc-sdd/main/tools/cc-sdd/templates/shared/settings/templates/specs/research.md) | H |
| 5 | Drift check / repair | partial | `/kiro-validate-gap` compares requirements with existing code, `/kiro-validate-design` checks design quality, and `/kiro-validate-impl` checks cross-task consistency and spec coverage. They report findings; any repair is to the code or the spec as the user directs. | [README](https://cdn.jsdelivr.net/gh/gotalab/cc-sdd@main/README.md) [v3.x] | M |
| 6 | Verification vs acceptance criteria | yes | `/kiro-impl` gives each task a fresh TDD implementer and an independent reviewer that checks it against acceptance criteria, with an auto-debug pass. `/kiro-validate-impl` checks the feature as a whole. `/kiro-verify-completion` requires fresh evidence and rejects "done because all tasks are checked". | [README](https://cdn.jsdelivr.net/gh/gotalab/cc-sdd@main/README.md); [verify-completion SKILL](https://raw.githubusercontent.com/gotalab/cc-sdd/main/tools/cc-sdd/templates/agents/claude-code-skills/skills/kiro-verify-completion/SKILL.md) [v3.0+, 2026-04] | H |
| 7 | Concurrent sessions/agents | partial | Native subagents run per-task implementation and review in parallel. `/kiro-spec-batch` runs several specs by dependency wave. Separate user sessions are not aware of each other. | [README](https://github.com/gotalab/cc-sdd) [v3.1.0] | M |
| 8 | Self-improving instructions | partial | Per-task learnings are written to `## Implementation Notes` in `tasks.md` and carried forward. Nothing amends the skills or rules. | [README](https://cdn.jsdelivr.net/gh/gotalab/cc-sdd@main/README.md) | M |
| 9 | Project rule overrides survive update | yes | Templates and rules in `.kiro/settings/` are meant to be edited. The installer's `--overwrite=prompt/skip/force` lets a re-install keep them. | [README](https://github.com/gotalab/cc-sdd); [DeepWiki install](https://deepwiki.com/gotalab/cc-sdd/2.1-installation-and-setup) | M |
| 10 | Hosts | yes | Claude Code and Codex are stable. Cursor, GitHub Copilot, Devin Local/CLI (added in v3.1.0), OpenCode, Gemini CLI and Antigravity are beta. | [README](https://github.com/gotalab/cc-sdd); [v3.1.0](https://github.com/gotalab/cc-sdd/releases) [2026-09-23] | H |

Notes: cc-sdd is the strongest method-carrier among the 2026 tools here. It is the only one with a separate verification gate that demands fresh evidence and a per-spec decision record with alternatives and trade-offs. Its context is per-feature, though. Nothing gives the project a standing picture at session start, and nothing tracks questions across specs. It uses the `.kiro/` layout, so a project can move between it and Kiro.

---

## Newer entrant 2: Claude Code built-in memory (CLAUDE.md / AGENTS.md / rules / auto memory)

Why it belongs: in 2026 the host itself absorbed much of what plugins like claude-mem provided. Auto memory now writes typed notes (user, feedback, project, reference) under an always-loaded index. Claude Code reads AGENTS.md natively (since v2.1.277), and `/doctor prompt-audit` (since v2.1.283) audits instruction files. Latest version: **2.1.294, 2026-10-08** ([changelog](https://code.claude.com/docs/en/changelog)).

| # | Question | Answer | How | Source + date | Conf. |
|---|---|---|---|---|---|
| 1 | What persists, in what form | yes | In the repo: `CLAUDE.md`/`AGENTS.md`, `.claude/rules/*.md` and a gitignored `CLAUDE.local.md`. Outside the repo: auto memory in `~/.claude/projects/<project>/memory/` (a `MEMORY.md` index plus topic files), which is machine-local and shared across worktrees. User-level and managed-policy files also apply. | [memory](https://code.claude.com/docs/en/memory) (n.d., read 2026-10-08) | H |
| 2 | Session orientation | yes (automatic) | At launch it loads the CLAUDE.md/AGENTS.md hierarchy and the first 200 lines or 25KB of `MEMORY.md`. Path-scoped rules and subdirectory files load on demand. SessionStart and UserPromptSubmit hooks can inject context, but only if the user configures them. No per-message memory injection is documented, although changelog 2.1.288 mentions a "memory recall" step whose mechanism is not documented. | [memory](https://code.claude.com/docs/en/memory); [changelog 2.1.288](https://code.claude.com/docs/en/changelog) [2026-10-02] | H (load) / L (recall) |
| 3 | Open questions as first-class items | no | Task tools hold pending, in-progress and completed tasks with dependencies, kept locally per session or team. Questions have no item type. | [agent-teams](https://code.claude.com/docs/en/agent-teams) (n.d.) | M |
| 4 | Decision records separate | partial | The auto memory `project` type holds "ongoing work, deadlines, and decisions" Claude can't derive from code. These are free-form notes, not structured records. | [memory](https://code.claude.com/docs/en/memory) | M |
| 5 | Drift check / repair | partial | `/doctor prompt-audit` checks instruction files for outdated content, references to missing files or commands, and contradictions between files. It proposes edits and changes nothing until asked. When `MEMORY.md` approaches its limit, Claude Code prompts a merge or prune. Product specs are not checked against code. | [memory](https://code.claude.com/docs/en/memory) [v2.1.283+] | H |
| 6 | Verification vs acceptance criteria | partial | Nothing built in. `TaskCompleted`/`TeammateIdle` hooks can block completion until a user-written check passes. | [agent-teams](https://code.claude.com/docs/en/agent-teams) | M |
| 7 | Concurrent sessions/agents | partial | Agent teams share a task list with file locking and mailboxes; the feature is experimental and off by default. Cross-session messaging connects your own sessions. Auto memory is shared across worktrees with no documented locking. | [agent-teams](https://code.claude.com/docs/en/agent-teams) (n.d.) | H |
| 8 | Self-improving instructions | partial | Auto memory saves `feedback` notes from your corrections and loads them in later sessions. `/doctor prompt-audit` proposes fixes to instruction files. Nothing ties a specific rule that failed to an amendment of that rule. | [memory](https://code.claude.com/docs/en/memory) | H |
| 9 | Project rule overrides survive update | yes | All instruction files belong to the user, and updates never touch them. Precedence: managed policy cannot be excluded; files are concatenated root to cwd, with `CLAUDE.local.md` last at each level; `claudeMdExcludes` works per settings layer. | [memory](https://code.claude.com/docs/en/memory) | H |
| 10 | Hosts | partial | Claude Code only (CLI, desktop, IDE extensions, web, SDK). It reads AGENTS.md, so files are shared with Codex, Cursor and others, but the memory is not. | [memory](https://code.claude.com/docs/en/memory) [v2.1.277+] | H |

Notes: the host now covers the always-loaded layer (instructions plus a memory index) and a light self-correction loop (feedback memories plus prompt-audit). It still has no method: no specs, no question store and no verification gate. A harness on top of Claude Code can rely on CLAUDE.md, AGENTS.md and MEMORY.md loading at session start, but has to add questions, decisions, drift repair and verification itself.

---

### Cross-tool observations (2026-10-08)

- **Questions** (Q3): none of the five tools keeps unresolved questions as first-class items, let alone with parent/child structure. The closest are claude-mem's flat work-state lists and cc-sdd's per-decision "follow-up" fields.
- **Decisions** (Q4): only cc-sdd keeps them as structured records with alternatives and trade-offs, and only per spec.
- **Verification as its own step** (Q6): cc-sdd has it outright. Kiro has it partly, through optional property-based tests.
- **Drift repair** (Q5): repair is mostly limited to task status (Kiro Sync Files) or to instruction files (Claude Code prompt-audit). None repairs architecture or decision docs against the code.
- **Self-improvement** (Q8): every tool that has it learns from the user's feedback (Claude Code, Kiro Web). None ties a rule that was not followed to an amendment of that rule.
