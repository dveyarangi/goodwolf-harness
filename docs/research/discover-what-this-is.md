# What this repository is an instance of — a `/discover` pass, 2026-09-26

Run at the front-page align, when the agent was about to say what sets the harness apart and had
only this tree's account and two reviews by models that had read it
([rule failure 10](../rule-failures.md)). The pass cloned the repository fresh from GitHub at
`1475df1`, read it cold, searched the web for the field, and was given only the question and the
answer format. Filed as it came back, its claims, confidences and sources whole and only its
layout condensed; what the align took from it is the align's.

Two things the pass reported about its own isolation, before the material:

- **The host loaded this tree's entry file and the user's memory index into it** before it read
  anything, and its git status showed the modified `/discover` skill and the untracked front-page
  review. The isolation the skill buys was breached by how the host starts a subagent in this
  working directory, not by the pass.
- **It read the earlier outside review** as part of the repository, so some of its framings may
  echo that one.

---

## How it was read

Fresh clone of https://github.com/dveyarangi/goodwolf-harness.git at `1475df1`. Read:
`README.md`, `AGENTS.md`, `local.rules.md`, `.agents/README.md`, `.agents/glossary.md`, the three
mechanism rules files and the maintain and mechanism-shape declarations, about 15 skills,
`docs/architecture.md`, the ADRs, `docs/pacer.md`, `docs/process.md`, `docs/tickets/README.md`,
`docs/rule-failures.md`, `docs/research/external-review.md`, `life-harness-findings.md`,
`entry-contract-findings.md`, the head of `audit-2026-09-05/REPORT.md`, one dream, one session
record, and the headers of `harness.py` and `inject_rules.py`. Ran the suite (337 tests, OK, 1
skipped, 214 s), `mechanisms.py --check` and `straw_dogs.py` (both clean). Measured: 150 commits,
one author, 2026-09-05 to 2026-09-24, subjects prefixed by loop stage (IMPLEMENT 27, MAINTAIN 20,
ALIGN 19, CONCLUDE 18, TICKET 15, PLAN 14, VERIFY 12); `AGENTS.md` 1,516 words; skill bodies about
14.5k words, all `.agents/` prose about 32k, `docs/` about 214k including the audit dump; 23
session records.

**What it is, plainly.** A development method for coding agents, shipped as a tier-1 entry file,
22 skills with one physical home linked into Claude Code and Cursor and read natively by Codex,
and standard-library Python scripts that install core into another repository, inject rules, and
check the repository's own records. The method is two loops — a session loop (recall → align →
conclude) and a delivery loop (ticket → plan → implement → verify → maintain) — and the repository
is developed with it, so most of its mass is its own development record under `docs/`.

## Family A: phase-gated, spec-driven workflow packs for coding agents

**Mapping.** `AGENTS.md`'s general rules and "Document load-bearing" ↔ Spec Kit's
`constitution.md` or a steering file. `/spec` → `/ticket` (vertical slices, tracer bullets) →
`/plan` (RFC) → `/implement` → `/verify` ↔ specify → plan → tasks → implement. `/align`'s
one-question interview with a recommended answer ↔ Superpowers' brainstorming. Human checkpoints ↔
phase gates. `docs/tickets/`, `docs/rfc/`, `docs/spec/` ↔ per-feature artifacts. Direct lineage:
the audit names Matt Pocock's `skills` as a source corpus; traces in `.agents/skills/tdd/`,
`/review-architecture`, and `/ticket`'s wording.

**Ladder** (medium): 0 ad hoc prompting · 1 one rules file · 2 a skill or command pack · 3 a
phase-gated workflow with persisted artifacts (Spec Kit, OpenSpec, Superpowers, BMAD) · 4 gates
enforced mechanically (hooks or CI) · 5 a method evaluated against outcomes. It sits on rung 3,
with part of 4 (`tickets.py --check`), no hooks, nothing on 5 — the repository's own external
review says its value "is asserted rather than measured".

**How it goes wrong.** Ceremony cost on small changes and markdown review burden (Böckeler's SDD
tool review, martinfowler.com, Oct 2025 — medium on attribution); specs drifting from code; agents
ignoring long instructions; longer context files costing more (ETH Zurich, ICLR 2026 workshop:
LLM-written context files −3% success, >20% cost; human-written about +4% at about +20% cost —
high). In the tree: making "the loop's ceremony switchable" is open under `01-0020`, and
`docs/pacer.md` records the struggle to size one step.

**Peers.** Current: GitHub Spec Kit, BMAD-METHOD, OpenSpec, GSD, AWS Kiro, obra/Superpowers (in
Anthropic's plugin marketplace since Jan 2026), mattpocock/skills. Long-lived: RUP, Scrum, ADRs
(Nygard, 2011).

**Commonplace:** the phased loop and PRD → issues → TDD chain; interview-before-build; a
constitution file; one skill directory linked for several hosts (Ruler, rulesync, AgentSync,
ai-rules-sync). **Rare** — no comparator in Spec Kit, BMAD, Superpowers or Pocock (medium): a
second, per-session loop (recall/conclude) with a numbered session log; a separate maintain stage
for drift, distinct from verify; an `/impact` pass deciding whether work is a spec or a ticket.

**Confidence:** mapping high, ladder medium, rarity medium (30+ tools not audited).

## Family B: a harness in the "harness engineering" sense, turned mostly on itself

**Mapping** onto Böckeler's frame (martinfowler.com, 2 Apr 2026). Guides (feedforward):
`AGENTS.md`, the skills, installed blocks. Computational sensors: `inject_rules.py --check`,
`mechanisms.py --check`, `tickets.py --check`, `straw_dogs.py`, the shipped suite. Inferential
sensors: `/verify` and `/maintain`. Steering loop ("each time the agent errs, engineer it away"):
`docs/rule-failures.md`, graded by the next occurrence.

**Material observation: the sensors point mostly at the harness's own artifacts, not at product
code or agent behaviour.** Checks on a recipient's product come only from its own `L3`. In
Böckeler's three regulation dimensions (maintainability, architecture fitness, behaviour) this is
closest to a maintainability harness for a harness.

**Ladder** (Böckeler; marmelab's 2026 survey): 1 instructions only · 2 plus deterministic guards
and tests of the harness · 3 plus evals of agent behaviour · 4 plus observability of what fires ·
5 measured before/after changes. Solidly on 2, beyond most peers there; no evals, no firing
telemetry (`01-0010.0120` acknowledges delivery is unobserved).

**How it goes wrong** (marmelab, 24 Sep 2026, unless stated). "When everything is important
nothing is"; 4–16% of security rules in 481 CLAUDE.md files measurably enforced (citing arXiv
2608.23550 — not verified by the pass). Context bloat: OpenAI keeps AGENTS.md to about 100 lines
as a table of contents; here 1,516 words plus a description per skill. Harnesses written by AI
more than the code they govern (52 of 79 repositories); here the harness is the product. Extra
reviewer agents can lower success (−8 pp, citing arXiv 2603.25723) — relevant to repeated `/plan`
and `/verify` passes. Rules that did not fire — what the register exists for.

**Peers.** OpenAI's Codex harness engineering (Feb 2026: AGENTS.md as table of contents, custom
lints carrying fix instructions, doc-gardening). Anthropic, "Effective harnesses for long-running
agents" (Nov 2025: initializer agent, progress file, feature list, git as cross-session state) —
structurally the same as recall/conclude plus the queue. flow-next (306 tests, bug-prevention
decision records mapping incidents to rules) — the closest peer to the register, per marmelab.
codex-claude-code-config (executable guards replacing prose rules). Long-lived: architectural
fitness functions (Ford, Parsons, Kua, 2017); cybernetic feedback control.

**Commonplace:** an instruction file (63% of major open-source projects), multi-agent targeting
(46%), markdown with little enforcement. **Rare and present:** the harness tests itself (about
21%); explicit decision records per rule, with authority; an incident-to-rule register. **Rare and
absent here as in most peers:** evals (about 60% have neither tests nor evals), observability (5 of
391), published before/after measurement (1 repository). Percentages medium — one survey.

**Confidence:** mapping high; "turned mostly on itself" high; peer statistics medium.

## Family C: a software product line extracted from clone-and-own, distributed as a managed template

**Mapping.** Clone-and-own origin: the audit's "four independent physical copies" with no
canonical tree — the textbook start of extractive adoption. Core asset base `.agents/`; variants
the recipient trees; variation points the rules files' anchors and declared painted doors;
variant configuration `local.rules.md`. "Core may not depend on the instance": `AGENTS.md`, ADR
0002, enforced by the leak check. Derivation and update: `harness.py` — clone at a ref, read
through `git archive`, transform (strip local blocks, shear straw dogs, stamp the announce line),
compare file by file. Managed regions: installed blocks, the idiom of Ansible `blockinfile` and
projen's generated files.

**Ladder:** 0 copy-paste · 1 clone-and-own · 2 vendored copy with provenance · 3 template with a
re-runnable update (copier, cruft) · 4 versioned releases with migration notes read before upgrade ·
5 feature model and automated derivation. Between 2 and 3; rung 4 is ticketed (`01-0010.0190`,
`01-0010.0195`). It merges nothing: an update refuses over an edited core file unless
`--overwrite`; copier's 3-way merge is the next step on that axis, not taken.

**How it goes wrong.** Extractive adoption brings refactoring bugs and variability drift (Kuiter et
al., SPLC 2018; Rubin and Chechik). Template drift and divergence never healed. Silent breaking
changes at the core–user interface — here: frost_map stranded at `2c733f0`, and rule failure 9, an
updater refusing every older tree, the classic backward-compatibility-of-the-updater failure. Core
erosion from local patches — countered by refusing edits to installed blocks.

**Peers.** copier, cruft, projen, Renovate-style update PRs; agent-rule distributors ruler,
rulesync, AgentSync, ai-rules-sync; Spec Kit's upgrade path; Claude Code plugin marketplaces; the
Agent Skills standard (agentskills.io, Dec 2025). Long-lived: Clements and Northrop, *Software
Product Lines* (2001); Krueger's extractive and reactive adoption.

**Commonplace:** symlinked multi-host skill directories; one source to many agent config files; a
template recording its source commit. **Rarer:** ship-time transformation stripping origin-only
content, with a leak rule enforced at the origin — no comparator among the rule syncers (medium);
refusing rather than merging on a drifted core file. **Absent here, common in template tools:** a
3-way merge.

**Confidence:** mapping high; ladder high; rarity of ship-time shearing medium.

## Family D: a defined-process quality management system, with corrective action

**Mapping.** Core ↔ the organisation's standard process set. `local.rules.md` ↔ tailoring; "an
override names the rule it overrides" ↔ a tailoring record. A mechanism declaration ↔ a process
definition (SIPOC, work products with consumers). `/maintain` ↔ document control plus internal
audit. `docs/rule-failures.md` ↔ CAPA, or CMMI Causal Analysis and Resolution: nonconformity →
root cause → corrective action → effectiveness check. Rule authority ↔ approval records.
`entry-contract-findings.md` ↔ controlled-document revision history. The paired close ↔ records
retention. Argyris and Schön's double-loop learning is what *Self-improvement* describes;
`01-0019` is deutero-learning.

**Ladder** (CMMI): 1 initial · 2 managed · 3 defined · 4 quantitatively managed · 5 optimizing.
Structure at level 3, with a level-5 practice (CAR, the register) and level 4 skipped entirely: no
baseline of defect rates, cycle times or rule-firing rates, so causes are established narratively,
one incident at a time. Next rung: measure something, such as rule-failure recurrence.

**How it goes wrong.** Process bloat and the paper system; maturity theatre; the process group
drifting from delivery; CAPA addressing symptoms, effectiveness checks never closed. In the tree:
construction prose six times core, and a self-development loop that "generates its own work".
Humphrey's PSP is the one-person version, with the documented weakness of heavy personal
record-keeping and poor persistence.

**Peers:** CMMI CAR, ISO 9001 clause 10.2, PSP/TSP, Argyris and Schön. No current agent harness
uses the QMS framing explicitly; flow-next's incident-to-rule records are nearest.

**Commonplace** in QMS practice: all of it. **Rare** in agent harnesses: the same features.

**Confidence:** mapping high; "level 3 plus a level-5 practice without level 4" medium.

## Family E: a self-improving agent memory architecture

**Mapping.** `/conclude` writing session records ↔ episodic memory write. `/recall` at every wake ↔
retrieval into working context. Skills ↔ procedural memory, a skill library (Voyager). Rule
failures plus amendment ↔ reflection and a curated delta update (ACE's Reflector and Curator).
`/dream` ↔ offline consolidation, sleep-time compute. Tier 1, skill body, mechanism doc ↔ memory
tiers and progressive disclosure. The human stays the curator.

**Ladder:** 0 stateless · 1 a notes file · 2 structured episodic plus procedural memory with
retrieval rules · 3 reflection loops that edit procedural memory (Reflexion, ACE) · 4 automated
validation of memory edits against held-out tasks · 5 learned consolidation policies. On 3 with a
human curator; nothing on 4. Next: test that an amended rule changes behaviour on a replayed task.

**How it goes wrong.** Context collapse and brevity bias under iterative rewriting (ACE, arXiv
2510.04618: one collapse from 18,282 tokens to 122, below the no-memory baseline) — the rules file
and whole-block install are ACE's answer, incremental structured deltas. Memory bloat; stale
memories retrieved as current — `/recall`'s *dated snapshots, read for why, never for whether* is
the standard guard. Self-reinforcing errors when the system grades itself — `/discover` exists
partly against this.

**Peers:** ACE (Oct 2025); Letta sleep-time compute (Apr 2025); Anthropic's long-running harness;
Claude Code auto-memory. Long-lived: Reflexion, Voyager, sleep consolidation.

**Commonplace:** a progress or session file plus git. **Rare:** a dream pass in a development
harness. **Unique in what was found:** dreams written in a language picked at random.

**Confidence:** mapping medium-high (structural analogy; text files, not model memory); rarity of
dreams medium.

## Family F: a codified legal order

**Mapping.** `AGENTS.md` ↔ constitution. Rules files ↔ statutes, the single authored home.
Installed blocks ↔ consolidation, derived and never amended where they sit. `local.rules.md`
placed last, naming what it overrides ↔ local ordinance or derogation citing what it derogates
from. Straw dogs ↔ sunset clauses with a testable condition and a responsible body. Evidence kept
out of the doc ↔ legislative history. "Do not reopen an accepted decision without new evidence" ↔
stare decisis. `repair=report` ↔ a bounded administrative-correction power. The entry contract's
version record ↔ versioned consolidation.

**Ladder:** 1 customary · 2 written, scattered · 3 codified · 4 consolidated with point-in-time
versions · 5 Rules as Code (OECD OPSI, 2020; Catala). At 4 with rung-5 traits — placement, drift
and leaks are checked, the rules stay natural language. Next: rules whose application is checked,
not just their placement.

**How it goes wrong.** Sunset clauses renewed routinely; empirical studies find sunset legislation
does not reduce waste (Journal of Regulatory Economics 2025; WFD 2022; Cato, Fall 2026), and
sunsets raise the chance of enactment by about 60% because reversibility lowers the cost of yes. In
the tree: about 65 live straw dogs; 19 skills carry `Mechanism: not yet` bound to `01-0017`, behind
four HITL tickets — renewal by inertia (medium). Statute accretion and conflicting provisions: two
decisions the entry file answers both ways; three coherence tickets reconciling hierarchy, scope
and responsibility. Legalism: rule failure 7, an argument built on a declaration's literal verbs.

**Peers:** Rules as Code (OECD OPSI; NZ Better Rules), Catala, Akoma Ntoso.

**Commonplace** in law: all of it. **Among agent harnesses:** a machine-checked single home per
rule with derived copies, rare (Life, the predecessor estate, had an injector; Spec Kit has no
injection); sunset markers with conditions, rare — code-level analogues are `todo_or_die` and
eslint's `expiring-todo-comments`, but straw dogs bind a ticket and a free-text condition instead of
a date, and cover prose as well as code.

**Confidence:** mapping high; the sunset-literature match to straw-dog persistence medium.

## Family G: a monastic Rule with customaries and a filiation of houses

**Mapping.** The Rule ↔ core. Each house's customary ↔ `local.rules.md`. The daily office ↔ wake
with `/recall`, `/conclude` at day's end, `/dream` after. The chapter of faults ↔ the rule-failure
register. Cistercian Carta Caritatis (1119): uniformity of observance ↔ core installed identically;
annual visitation of daughter by mother ↔ `harness.py --check` against the announced ref;
filiation ↔ the announce line and a fork naming itself through the `Repository:` line; the
abbot's authority ↔ the user's.

**Ladder:** a cycle, not a ladder — foundation → customaries (Cluny) → relaxation → reform
(Cîteaux, La Trappe) → re-codification. At foundation with first filiation, two daughter trees.
The next rung in the family's terms is the general chapter, where daughters' experience amends the
common Rule — the parked *contribution back*.

**How it goes wrong.** Customaries proliferate until observance is mostly custom; uniformity by
visitation breeds formalism; the mother house's needs drive the Rule; reform arises when the letter
has outgrown the purpose.

**Peers:** only long-lived — the Rule of St Benedict, Carta Caritatis, the Nomasticon Cisterciense.
Principles, not evidence about software.

**Confidence:** mapping medium. Surface-cue risk is real — the repository's vocabulary is
contemplative — but the core, filiation and visitation mapping holds without those cues.

## Family H (thin): a self-hosting, bootstrapped toolchain

**Mapping.** Developed with itself; the origin is the host compiler, recipients targets; the
install transform is a cross-build; `--check` against the announced ref is a reproducibility check;
tests ship inside core so a recipient learns the scripts arrived intact.

**Ladder:** self-applied → self-hosting → reproducible from an independent seed (diverse
double-compiling). At self-hosting.

**How it goes wrong.** Circular validation; new code tested against artifacts only new code can
produce — rule failure 9 verbatim; growth driven by the tool's own development needs — the queue
ranks by "which slice hands the next one a tool that makes the harness work better".

**Peers:** self-hosting compilers, Smalltalk images, Wheeler's DDC (2009).

**Confidence:** medium; covers the development relationship, not the method's content.

## What the tasking smuggled in

- **The vocabulary is the repository's own.** "Instance of", "families", "not topical neighbours",
  "ladder", "recency for evidence, longevity for principles", "material, never a verdict" are
  near-verbatim from `/discover` and the entry file; the answer was pre-shaped toward the
  repository's own view of a good answer.
- **The pass was not context-free** — the host loaded the entry file and memory index, and git
  status hinted that the pass feeds a front page or a change to `/discover`.
- **It read a previous pass**, the filed external review.
- **"This" as one thing.** The repository is a shippable method (`.agents/`, about 32k words) and
  one project's development record of it (`docs/`, about 214k). Families A, B and E describe mostly
  the first; D, F and H mostly the second.
- **"Ladder of maturity" presupposes higher rungs** — every ladder has one by construction.
- **"Commonplace versus rare" invites a distinctiveness frame**, which reads as merit.
- **"Peers and prior art" presumes a field** — F and G have no software peers.
- **"Read it as an outsider would" presumes one outsider** — a human, an installing agent and a
  model primed by the entry file read it differently; the pass was the third.

## Nothing to take

- **Docs-as-code, living documentation, DDD ubiquitous language** — maps one skill and its records,
  a slice, not the whole.
- **Multi-agent orchestration frameworks** — one agent runs every stage; subagents appear only in
  `/discover`.
- **Personal knowledge management** — topical (Obsidian as a viewer); no counterpart for tickets,
  ownership, installed rules or checks.
- **CI/CD pipeline** — topical; the verification set is run by an agent, and no pipeline exists.

## A second pass, from another model — 2026-09-26

Brought in by the user from a model that did not see the commissioning session. It read the
repository to extract the shape, then handed an isolated classification pass a functional
description with none of this tree's vocabulary:

> An installable repository-resident method for AI coding assistants that persists a
> software-development process across context resets; separates deliberation, planning,
> implementation, verification and upkeep; externalizes decisions and work state; mechanically
> checks some consistency properties; supports project-specific policy; records cases where its own
> instructions failed to affect behavior; and develops itself using the same method.

Its families, as it gave them:

- **Agentic software-process harness** (high). Spec Kit asks how a feature goes from intent to
  implementation; this additionally asks how the process itself is maintained — its rules,
  records, provenance, installation, temporary assumptions, and the correspondence between process
  and reality. Closer to an *agentic software-process system* than another Spec Kit. Failure mode:
  ritualization — the process grows internally elaborate while its relation to software quality
  becomes unclear.
- **Policy-as-code** (high). Authored policy separated from where it is enforced, mechanically
  inspectable, divergence detected — OPA the canonical example. Here: canonical rule → distributed
  to the decision context → drift detected → overrides → retracted or updated mechanically. On
  documentation → machine-checkable policy → enforcement engine, it sits in the middle: some
  properties enforced by scripts, many semantic rules still relying on the model obeying prose.
  *Rule presence isn't rule enforcement.*
- **Organizational memory for an ephemeral workforce** (high; "may be the most illuminating").
  An engineering organization whose every engineer suffers total amnesia on leaving the room and is
  replaced by a slightly different one would care obsessively about current decisions versus
  historical records, why something was decided, where a fact officially lives, not reopening
  settled questions, explicit unfinished assumptions, handoffs, and reconstructing state from
  durable artifacts. Agents as capable but radically transient organizational participants; the
  harness as institutional-memory architecture. Failure mode: bureaucratic entropy — maintaining
  the representation of knowledge costs more than the forgetting it prevents.
- **Software process improvement, double-loop learning** (very high). Argyris: when something goes
  wrong, examine whether the governing rule caused it — the distinction between a development
  failure and a rule that existed but did not fire. On ad-hoc → defined → measured → adapting, it
  sits between defined and adapting: sophisticated machinery for changing the process from
  experience, little quantitative evidence that the changes improve outcomes — and evaluating
  whether a process intervention improved outcomes is a known, badly confounded problem.
- **Reflective, self-hosting systems** (medium-high). Genuinely self-hosting, weakly reflective:
  the reflection is socio-technical, a model reading and modifying artifacts, not intrinsic to a
  runtime. Danger: a self-contained reflective method growing more internally coherent while
  drifting from external usefulness.

**What its tasking smuggled in.** *Method* biases toward software process over institutional
design; *AI coding assistants* toward agent frameworks; *persists across context resets* makes
memory the problem; *changes its own instructions* primes organizational learning and reflection.
Subtlest: describing it as one system — it may be several bundled: development methodology,
institutional memory, policy distribution, maintenance tooling.

**Nothing to take.** Multi-agent orchestration (coordinating concurrent actors is not the central
object); formal methods (tests and invariants, no proof of the process); a prompt engineering
framework (too shallow — the persistent artifacts and mechanical maintenance do the interesting
work).

**What it changed in its own evaluation.** The thesis is closer to: *treat agentic software
development as an organization whose workers are transient, then turn as much of that
organization's culture, memory, governance and learning as possible into repository-resident
executable structure.* And the unresolved question: *it is increasingly good at proving that it is
internally coherent. Does that coherence causally produce better engineering?* — the boundary its
machinery cannot validate from inside itself.

## Sources

- Böckeler, "Harness engineering for coding agent users", martinfowler.com, 2 Apr 2026: https://martinfowler.com/articles/harness-engineering.html
- marmelab, "The State of AI Harness Engineering 2026", 24 Sep 2026: https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html
- Gloaguen et al., "Evaluating AGENTS.md…", ICLR 2026 workshop: https://arxiv.org/abs/2602.11988
- OpenAI, "Harness engineering: leveraging Codex in an agent-first world": https://openai.com/index/harness-engineering/
- Anthropic, "Effective harnesses for long-running agents": https://anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Spec Kit: https://github.com/github/spec-kit/blob/main/spec-driven.md ; SDD comparisons: https://dev.to/willtorber/spec-kit-vs-bmad-vs-openspec-choosing-an-sdd-framework-in-2026-d3j , https://docs.bswen.com/blog/2026-08-07-ai-spec-frameworks-compared/
- Superpowers: https://blog.fsck.com/2025/10/09/superpowers/ , https://pasqualepillitteri.it/en/news/215/superpowers-claude-code-complete-guide
- mattpocock/skills: https://github.com/mattpocock/skills
- Agent Skills standard: https://agentskills.io/home , https://github.com/agentskills/agentskills
- ruler: https://github.com/intellectronica/ruler ; rulesync: https://github.com/dyoshikawa/rulesync ; AgentSync: https://github.com/lunetics/agent_sync
- copier/cruft: https://cruft.github.io/cruft/ , https://www.blenddata.nl/en/blogs/cruft-vs-copier-automating-template-updates-at-scale
- Clone-and-own to product line: https://dl.acm.org/doi/10.1145/3233027.3233050 , https://dl.acm.org/doi/10.1145/2791060.2791086
- ACE: https://arxiv.org/abs/2510.04618 ; Letta sleep-time compute: https://www.letta.com/blog/sleep-time-compute/
- CMMI CAR: https://www.oreilly.com/library/view/cmmi-guidelines-for/9780321635839/ch08.html , https://en.wikipedia.org/wiki/Process_area_(CMMI)
- Sunset clauses: https://link.springer.com/article/10.1007/s11149-025-09498-5 , https://www.wfd.org/commentary/can-sunset-clauses-live-their-promise , https://www.cato.org/regulation/fall-2026/what-happens-after-sunset
- Rules as Code: https://oecd-opsi.org/publications/cracking-the-code/
- todo_or_die: https://github.com/searls/todo_or_die ; eslint-plugin-unicorn expiring-todo-comments: https://github.com/sindresorhus/eslint-plugin-unicorn/blob/main/docs/rules/expiring-todo-comments.md
- Carta Caritatis: https://en.wikipedia.org/wiki/Carta_Caritatis , https://www.britannica.com/topic/Cistercians
