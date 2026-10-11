# Context tax of peer harnesses, as of 2026-10-11

**Kind:** evidence — a dated measurement. What a session pays in context before the person's
first message, in a freshly installed project under Claude Code, for this harness and seven peers;
and, [below](#per-step), what each step of the work makes the agent read.

**Method.** Tokens are characters ÷ 4. *Always-loaded instructions* is the CLAUDE.md or AGENTS.md
text the tool installs, plus whatever its session-start hook injects. *Descriptions* is the
frontmatter `name` and `description` of every skill, command and subagent the host lists at start;
bodies load on invocation and are not counted. Peers were measured from shallow clones of their
public repositories at the named commits, by reading the installer's source and templates; no
installer was run. Each figure is ±10%: the ÷4 convention, the keys counted with the values, and
the host's own listing format are not modelled. Excluded everywhere: context a tool generates
later from the project (BMAD's context block, GSD's generated CLAUDE.md, Pocock's agent-skills
block) and anything that grows with use (beads' memories).

This harness, by the same method: a fresh install's `AGENTS.md` plus the 24 skill descriptions
is about 4,000 tokens; in this repository, with its own installed blocks and local rules,
`AGENTS.md` is 17,008 characters and the descriptions 2,458, about 4,900 tokens.

| tool | always-loaded instructions | skill/command descriptions | before the first message | hook at session start | per message | source |
|---|---|---|---|---|---|---|
| **this harness** | ≈3,400 (`AGENTS.md`, fresh) | ≈600 (24 skills) | **≈4,000** | yes: the wake report, ≈2,700 in this repository after a month | yes: the question window, by a hook | this tree, 2026-10-11 |
| **GSD Core** | 0 — no CLAUDE.md written at install; `generate-claude-md` runs later from `/gsd:new-project` | ≈1,975 (72 skills); plus 35 subagents ≈1,965 in the Agent roster | **≈1,975** (≈3,940 with the subagent roster) | yes, but injects no model context by default; a STATE.md head only with `hooks.community: true` | none for Claude Code; tool-call guards instead | open-gsd/gsd-core b747aca, v1.16.0, 2026-10-11 |
| **BMAD-METHOD** | 0 at install — the `bmad:context` AGENTS.md block is written by `bmad-project-context` later, project-sized (this repo's: ≈550) | ≈343 (the documented minimal 5 skills) to ≈2,267 (all 33) | **≈343–2,267** | none | none | bmad-code-org/BMAD-METHOD bda3c59, 2026-10-06 |
| **superpowers** | ≈850 — the hook injects `using-superpowers/SKILL.md` whole as `additionalContext` | ≈733 (15 skills) | **≈1,580** | yes, on startup, clear and compaction, so it is paid again after each | none | obra/superpowers bb92a77, v7.0.0, 2026-10-09 |
| **spec-kit** | 0 — the constitution is read by command bodies on invocation | ≈370 (10 commands) | **≈370** | none by default | none | github/spec-kit 0443760, 2026-10-09 |
| **beads** | ≈695 — the minimal profile block `bd init` writes into AGENTS.md | 0 for Claude Code (the skill ships for Codex and Cursor) | **≈2,100** (695 + ≈1,400 from the hook) | yes: `bd prime --hook-json`, ≈1,400 by measurement, "~1–2k" by its own docs, plus stored memories; again after compaction | none | steveyegge/beads 7477ec1, 2026-10-11 |
| **Matt Pocock's skills** | 0 — an optional setup skill later adds a ≈100-token block | ≈1,180 (27 skills in the plugin) | **≈1,180** | none | none | mattpocock/skills 49dd158, plugin v1.3.1, 2026-10-09 |
| **OpenSpec** | 0 — `init` no longer writes CLAUDE.md or AGENTS.md | ≈1,145 (12 skills + 12 commands) | **≈1,145** | none | none | Fission-AI/OpenSpec 9111a76, 2026-10-06 |

## Reading it

- Fresh, this harness starts two to ten times heavier than any peer: about 4,000 tokens against
  370–2,100, GSD reaching ≈3,940 only when its 35 subagents are counted.
- The difference is in kind, not only in size. Every peer loads next to nothing before the first
  message and pays inside each command, when its body loads. This harness loads the method's rules
  themselves — the entry file — so that they bind every turn, commands or not; that is the tax of
  rules that reach the agent rather than wait to be invoked.
- Two peers pay a session-start hook as this one does: superpowers (≈850, a skill body) and beads
  (≈1,400, project state). This harness's wake report is the largest of the three and grows with
  the tree; its per-message window has no peer at all.
- What the tax buys has not been measured, here or anywhere in the panel; q-0017 and q-0018.0008
  hold that.

The user asked for this comparison on 2026-10-11, for the front page's cost paragraph. The
figures were gathered by a delegated agent from the repositories named; nothing was taken from a
tool's own claims except where the table says so.

## Per step

The user asked for this the same day, after the session-start table. Same clones, same commits,
same ÷4 convention.

**Method.** The step unit is this harness's ring — align, recall, ticket, plan, implement, verify,
commit — and each peer's commands are mapped onto it; the mapping is a judgement, and one peer
command may cover several steps. A cell is the fixed text the method makes the agent read at that
step: the command's body loaded at invocation, plus the tool's own shipped files the body makes
it read — templates, checklists, workflows, sub-skills marked required — one level down, and a
loaded workflow's own mandatory includes. Conditional reads are left out of the sums. Project-sized
records — the spec, the plan, the state file, the code — are not counted. What a step hands to a
subagent is counted nowhere.

Each cell: body + shipped reads = total. `—` is a step the tool has no command for.

| tool | align | recall | ticket | plan | implement | verify | commit | ticket → commit |
|---|---|---|---|---|---|---|---|---|
| **this harness** | 2,390 + 420 = **2,810** | **1,040** | 1,770 + 3,000 = **4,770** | 1,730 + 1,580 = **3,310** | 680 + 2,980 = **3,660** | 1,530 + 3,080 = **4,610** | **550** | **≈16,900** |
| **GSD Core** | 1,495 + 14,265 = **15,760** | 175 + 5,440 = **5,615** | — (inside plan-phase) | 1,270 + 34,000 = **35,270** | 805 + 34,050 = **34,855** | 365 + 14,180 = **14,545** | — (per task, inside execute) | **≈84,670** |
| **BMAD-METHOD** | 4,160 + 605 = **4,765** | 630 + 475 = **1,105** | 2,500 + 5,305 = **7,805** | 420 + 6,600 = **7,020** | **910** (same build invocation) | **3,040** (same) | **285** (same) | **≈19,060** |
| **superpowers** | 2,520 + 220 = **2,740** | — | — (inside writing-plans) | **2,585** | 5,100 + 6,165 = **11,265** | **910** | **1,945** | **≈16,705** |
| **spec-kit** | **4,875** (clarify) | — | 6,275 (specify) + 5,150 (tasks) = **11,425** | 2,010 + 945 = **2,955** | **3,195** | **2,940** (analyze, before implementing) | — | **≈20,515** |
| **OpenSpec** | **5,700** (explore) | — | 4,060 + 4,640 = **8,700** (propose; covers plan) | — (in propose) | 2,790 + 50 = **2,840** | **4,585** | — (archive ≈4,140, no git commit) | **≈16,125** |
| **Matt Pocock's skills** | 40 + 520 = **560** (grill-me) | — | **1,480** (to-tickets) | **780** (to-spec) | 160 + 1,875 = **2,035** | **1,690** (code-review) | — | **≈5,985** |
| **beads** | — | ≈1,400 (the session-start hook) | **1,215** (the skill, where installed) | — | — | — | — | **≈1,215** |

**Per message.** No peer injects anything unconditionally before each message; GSD's tool-call
guards add ≈60 tokens only on a finding. This harness's hook injects the question window: a line
of ≈90 tokens when the session's position has not moved, the window redrawn — ≈4,430 in this
repository today, growing with the store — when it has. At session start and after a compaction
the wake report is ≈7,680 here today.

**Project-sized records the steps read.** This harness: the ticket, RFC, architecture, ADRs,
glossary, edge records and the question store. GSD: PROJECT, REQUIREMENTS, ROADMAP, STATE,
CONTEXT, RESEARCH, PLAN, SUMMARY, VERIFICATION and the codebase map. BMAD: the initiative's
ticket tree, plans, the spec kernel and persistent facts. superpowers: the design doc, the plan
and the progress ledger. spec-kit: the constitution, spec, plan, tasks, research, data model and
contracts. OpenSpec: the change's proposal, specs, design and tasks, and the main specs. Pocock:
the tracker doc, glossary, ADRs and coding standards. beads: the issue graph and stored memories.

### Reading it

- Per ring this harness is in the middle: ≈16,900 tokens of the method's own text from ticket to
  commit, beside superpowers, OpenSpec, BMAD and spec-kit at 16,000–20,500. Pocock's skills are a
  third of that; GSD is five times it, its workflows alone 22,000–24,000 a step.
- So the morning's gap — two to ten times heavier before the first message — is mostly where the
  text is paid, not how much: this harness pays the rules up front so that they bind every turn,
  the peers pay inside each command. Over one ring the difference shrinks to the entry file,
  ≈4,400, carried through every step.
- The cost no peer has is the window before each message: small while the work stays on one
  question, ≈4,400 each time it moves, and growing with the store. With every injected token
  re-read on each later model call, it is the item to watch.
- A static count is the text, not the tax. The tax is steps times context length (see
  [the first measures](measures-2026-10-11/REPORT.md)), and how many steps a method makes for the
  same work is not read here. GSD hands its heaviest work to subagents, whose contexts this
  counts nowhere.

**Caveats.** Each figure ±10%: whole files, ÷4, keys counted with values; spec-kit's placeholders
and BMAD's rendered step files move a cell a few percent. This harness's step bodies carry its own
installed blocks and local rules, larger than a fresh install's; the peers were measured from
source, without what their installers write into a project.

## The project's own records, per step

The section above left out the records the steps read, as project-sized. The user pointed out the
same day that this misses what each agent must actually read. They are measured here on real
projects.

**Method.** For each tool, the step bodies were read for which project records each step tells
the main agent to read always, and which only on a condition. Only the always reads are summed.
Each peer was measured on five or six public repositories that use it for real work — dozens to
hundreds of features done, pushed within weeks, no forks or demos — from the blob sizes in their
git trees. Each repository gives its median feature, and the table gives the median across
repositories, with the range. This harness was measured on frost_map, a product project a month
under it, and on this tree. Source code and git output are counted for no one. One agent per
tool did the work; their scripts and data are in the session's scratchpad, not in the tree.

Main agent, tokens, median (range):

| tool | align | recall | ticket | plan | implement | verify | ticket → commit | project-wide, read always |
|---|---|---|---|---|---|---|---|---|
| **this harness**, frost_map | 17,700 | 22,300 | 9,600 | 18,600 | 14,200 | 22,500 | **≈65,000** | ≈20,000 |
| **this harness**, this tree | 7,900 | 25,500 | 10,400 | 10,300 | 13,000 | 13,200 | **≈47,000** | ≈20,600 |
| **GSD Core** | 28,700 (10,000–74,600) | 11,100 (6,500–43,400) | — | 2,000 (550–2,800) | 7,000 (3,400–24,800) | 5,000 (3,900–9,200) | **≈14,000**, subagents +216,000 | 28,100 (11,600–84,500) |
| **spec-kit** | 4,590 (3,756–8,278) | 0 | 6,958 (5,484–12,482) | 8,229 (5,387–15,665) | 6,856 (6,016–11,398) | 15,943 (12,572–28,080) | **≈40,100** (31,200–67,600) | 2,843 (1,158–10,892) |
| **superpowers** | 0 | 0 | — | 3,360 (1,170–7,040) | 20,690 (8,400–40,280) | 0 | **≈25,100** (9,400–43,600) | 0 |
| **OpenSpec** | 530 (5–2,534) | — | 6,413 (3,576–7,692) | — (in ticket) | 6,674 (3,862–8,180) | 5,793 (3,499–6,708) | **≈18,900** | 530 (5–2,534) |
| **BMAD-METHOD** | 0 | ≈30 | 5,900 (2,600–20,500), per epic | 4,400 (1,000–14,700) | 2,300 (500–13,900) | 1,900 (500–6,400) | **≈18,500** | 2,400 (850–4,800) |
| **Matt Pocock's skills** | 0 | — | 4,060 (1,900–10,010) | 3,050 (1,350–6,350) | 1,120 (1,030–1,830) | 4,060 (1,630–9,750) | **≈14,000** (7,700–22,100) | 3,050 (1,350–6,350) |
| **beads** | — | 1,086 (678–5,382) | 193 (88–287) | — | — | — | **≈1,300** | 1,086 |

This harness's cells, from its skills: recall reads the wake report, the queue, the live tickets,
the last session record, the architecture and the ticket and RFC in flight; align the
architecture, glossary, ADRs and the question; ticket the parent spec and the live tickets; plan
the ticket, architecture, ADRs and glossary; implement the spec, ticket, RFC and glossary; verify
the ticket, RFC, architecture, ADRs and glossary. In frost_map the architecture alone is ≈15,100;
in this tree it is ≈4,600, the rest spread over the mechanisms' docs.

Method text and project records together, ticket to commit:

| tool | method text | project records | together |
|---|---|---|---|
| GSD Core, main agent | ≈84,700 | ≈14,000 | **≈98,700**, subagents +216,000 |
| **this harness**, frost_map | ≈16,900 | ≈65,000 | **≈81,900** |
| **this harness**, this tree | ≈16,900 | ≈47,000 | **≈63,900** |
| spec-kit | ≈20,500 | ≈40,100 | **≈60,600** |
| superpowers | ≈16,700 | ≈25,100 | **≈41,800** |
| BMAD-METHOD | ≈19,100 | ≈18,500 | **≈37,600** |
| OpenSpec | ≈16,100 | ≈18,900 | **≈35,000** |
| Matt Pocock's skills | ≈6,000 | ≈14,000 | **≈20,000** |
| beads | ≈1,200 | ≈1,300 | **≈2,500** |

### Reading it

- Counted with the project's records, this harness is the second heaviest main agent of the ring,
  after GSD: ≈82,000 in a product project against 20,000–61,000 for the rest. The previous
  section's "in the middle" holds for the method's text alone.
- The weight is of a kind only GSD shares: project-wide records read at every step. This harness
  re-reads the architecture, glossary and ADRs at plan, verify, align and recall; GSD re-reads
  STATE, ROADMAP and PROJECT, which reach 60,000–95,000 in half its repositories. Both grow with
  every feature. spec-kit, superpowers, OpenSpec, BMAD and Pocock read the feature's own spec,
  plan and tasks, with a project-wide record of 0–3,000 — their cost per step does not grow with
  the number of features.
- That is the price of the harness's central claim: a step is checked against what the project
  has decided, not only against the feature's own plan. Whether it buys fewer re-decisions and
  less drift is what the measurement of savings has to show.
- The largest single item is one document. Reading only the sections of the architecture a step
  bears on, rather than the whole file, would take most of the difference away; no skill says
  that today.

**Caveats.**

- Summing the steps assumes each runs in a fresh context. Run in one session, a record read at
  plan is still in context at verify, and both this harness's and GSD's sums fall the most.
- This harness is measured on one product project and on this tree; each peer on five or six
  repositories, mostly young and solo, picked for depth from the hundreds found.
- Always against conditional is a judgement on each tool's wording. Conditional reads are large
  for some: spec-kit's design files, present in nine features of ten, add 4,000–12,000 at ticket
  and implement; OpenSpec's relevant main specs add ≈6,600; BMAD's architecture and UX documents,
  where they exist, 4,000–40,000.
- Records are measured at their final size; a plan read at implement was smaller then. GSD's
  subagent contexts, and every tool's reviewer subagents, are separate contexts the main agent
  never holds.
