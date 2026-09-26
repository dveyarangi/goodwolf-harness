# Adoption panel — 2026-09-26

The first run of the panel [01-0010.0190](../tickets/01-0010.0190-core-is-published-as-a-release.md)
puts at every release, run by hand on the repository as published at `d3af46f`, the day the front
page landed. Five independent agents, each given a different project and different needs, cloned
the repository fresh, read it from its README as a newcomer would, searched the web for the
alternatives they would weigh it against, and answered: would you install it over those, why, what
would change your answer, and what the front page got wrong. Each was told to set aside the
project instructions already in its context; the host loads this tree's entry file into every
subagent regardless, so none was blind. Two ran on a different model. Filed as they came back,
their layout condensed; what is taken from them is the work items'.

**Verdicts: one *no*, four *not yet*.**

## 1. Existing instructions — *not yet*

A mid-sized TypeScript app, three developers, a hand-written 200-line `CLAUDE.md` and four team
slash commands in `.claude/commands/`.

- **It refuses to install over what I already have.** The install stops on any file it ships that
  already exists, `CLAUDE.md` among them; the 200 lines would have to be rewritten into the local
  file's rule grammar by hand. The ticket that would carry them over,
  [01-0010.0150](../tickets/01-0010.0150-harness-meets-a-tree-with-a-method.md), is only planned.
  `.claude/commands/` would survive, since only `.claude/skills` is linked, but nothing integrates
  the commands.
- **Every change gets the full process** — a non-starter for three developers on 40k lines.
- **Heavy context and in-house vocabulary** — 23 skills, about 2,100 lines, and a 10 KB entry file
  of its own terms.
- **Maturity** — created 2026-09-09, one author, 0 stars, 158 commits, developed mostly by
  dogfooding; no uninstall; updates don't say what changed; nothing on several developers editing
  tickets and session records in parallel.

Compared: **OpenSpec** fits best — specs only for what changes, beside an existing `CLAUDE.md`,
less rigorous on decisions. **Spec Kit** — large community, a heavy pipeline for new projects.
**GSD** — popular, also a large process. **Doing it myself** — an ADR folder, a backlog file, a
`/handoff` and `/resume` pair. **What it does better than all of them:** one source per rule with
a drift check, rules the agent failed to follow written down and reworded, provisional items
marked.

Would change it: `.0150` landing, so an install carries the existing `CLAUDE.md` and commands in
without loss; the pacer's lighter path for small work; a trimmed default install or a list of
skills to skip; evidence of a team or a second real project; an uninstall.

Front page: candid about its gaps. *Move them aside* undersells a hard refusal and a hand port;
silent on per-session context cost, on several developers, on an example session, and on the
glossary being required reading.

## 2. Large existing codebase — *not yet*, no for today

A 12-year-old Java/Spring monolith, about 600k lines, 15 developers, a stale wiki and no agent
instructions; Codex and Claude Code used ad hoc, re-discovering the architecture every session.

- **It can't bootstrap from existing code** — the README's own *not yet*, and
  [01-0010.0175](../tickets/01-0010.0175-arrival-describes-what-it-finds.md) admits no real case
  has exercised the code half. That is exactly the problem; the durable understanding would be
  written by hand.
- **Every change gets the full ceremony** — fifteen developers will route around it, and the
  records rot.
- **Built for one person, not a team** — three weeks old, one author, no releases; tickets are
  markdown files with hand-allocated numbers, so fifteen people collide on numbering and duplicate
  the real tracker.
- **The jargon is a barrier.**
- **Setup friction** — existing agent files moved aside, no uninstall, updates don't say what
  changed.
- **What it gets right, worth copying by hand:** decisions in ADRs and the architecture, not in
  chat; rules with one source and drift checks; sessions that start by reading the records.

Compared: **plain `AGENTS.md`/`CLAUDE.md` per module plus an ADR folder** — the realistic baseline,
and probably the winner. **OpenSpec** — delta specs, better fit for a large existing codebase,
lighter per change. **Spec Kit** — the constitution is a similar idea; leans to new projects, heavy.
**BMAD** — far more ceremony. **Kiro** — locks you into AWS's IDE.

Would change it: code-reading onboarding shown working on a large codebase; a lightweight path for
small changes; evidence of multi-developer use, merges included; tagged releases with changelogs;
an uninstall.

Front page: honest, but missing the maturity signal — age, one author, no releases, no outside
users — and the key blocker sits fourth in its list. *Institutional memory* starts empty for a
codebase with no records.

## 3. Greenfield prototype — *not yet* (different model)

A solo founder, an empty repository, two months of mostly agent-written code, burned before by an
unmaintainable prototype nobody remembered the reasons for.

- **Zero track record** — created 2026-09-09, no stars, forks or watchers, one open issue, a single
  contributor. *(Its count of 50 commits and "six days old" disagree with the others' and with the
  record.)*
- **Heavy ceremony for week one** — 23 skills, two loops, format files, straw dogs, a separate
  glossary; the wrong ratio for an empty repository and a rough idea.
- **Mostly *not yet*** — the enforcement and safety parts it would want are the ones missing.
- **Known Windows install pain** — [issue #1](https://github.com/dveyarangi/goodwolf-harness/issues/1):
  a Git ownership error misreported, and symlinks failing while the report still says
  `arrived: true`.
- **Genuine plus:** the problem it targets is exactly what burned this founder; MIT, plain files,
  no lock-in, three hosts.

Compared: **BMAD** — mature, popular, weaker on drift repair and long-term architecture memory.
**Spec Kit** — lighter, no glossary or ADR drift checking. **Cline's Memory Bank** — near-zero
overhead, no enforcement or ticket lifecycle. **Hand-rolled `AGENTS.md` plus ADRs** — purely
manual discipline, the thing that failed before.

Would change it: a second real user, the Windows install fixed, the enforcement and code-drafting
items closed, a documented light on-ramp for week one.

Front page: silent on age, single author and zero adoption, and on the filed Windows failures;
jargon used there is defined only in the linked glossary; no word on per-session token or time cost.

## 4. Single host, Cursor on Windows — *not yet* (different model)

A freelancer working only in Cursor on Windows across three client projects, using Cursor rules,
never Claude Code or Codex; wants a consistent plan-test-verify process and remembered decisions
without running tools they do not understand.

- **Solo and pre-adoption** — no stars or forks, one open issue, eight *not yet* gaps, among them
  *the agent is trusted to keep it*: an honour-system harness.
- **Fails "no tools I don't understand" on day one** — the install runs a Python script that
  writes rule files, symlinks and version markers into the repository.
- **Dense, self-referential vocabulary** — a real per-project overhead across three codebases.
- **The same ceremony for every change**, by its own admission.
- **Cursor support is real** — Cursor shipped Agent Skills in `.cursor/skills` in January 2026 —
  but the repository shows no Cursor-specific example.

Compared: **Spec Kit** — 120k+ stars, 30+ agents including Cursor, the same discipline, far more
mature; less opinionated about memory and postmortems. **OpenSpec** — lighter, easier onboarding.
**Cursor Memory Bank** — solves the remembering directly, no installer, no vocabulary. **Cursor's
own rules and memories** — zero install, weaker on sequencing. **BMAD** — overkill for solo work.

Would change it: real adoption, the pacer's lighter path, an uninstall, and a Cursor quickstart
proving the skills fire in Cursor without hand-holding the installer.

Front page: no disclosure of single-author, zero-adoption status; no worked example; jargon with
no beginner example; the equal-ceremony limit buried in a straw dog; no Cursor-specific screenshot
or command list despite claiming Cursor works.

## 5. Minimal ceremony — *no*

A senior engineer at a small startup shipping many small changes a day with Claude Code and a short
`CLAUDE.md`; dislikes process for its own sake; has lost work twice this month to the agent
forgetting context.

- **The README says the process is uniform** — a one-line fix gets the full loop. That rules it
  out, and it is honest, which earns respect.
- **It is a methodology, not a memory fix** — 23 skills, a 1,500-word entry file, about 32k words
  of skill and format documents, of which only `/recall` and `/conclude` address the problem;
  copied into a `CLAUDE.md` in ten minutes.
- **It collides with the setup** — the `CLAUDE.md` must go; no uninstall; updates don't say what
  changed.
- **Private jargon** — each term needs learning before the agent can be trusted.

Compared: **Claude Code's built-in auto memory and `/rewind`** — no install, the first move.
**claude-mem** — automatic capture with zero ceremony; opaque, token cost, a dependency. **Mem0,
supermemory** — automatic recall, data may leave the repository. **Plain discipline** — a notes
file and frequent work-in-progress commits; lost work is really a git problem. **Its advantage:**
memory in the repository, reviewable, decisions apart from history — for a slow team with
architecture to protect.

Would change it: switchable ceremony with a real light path from recall to commit; an install that
coexists with an existing `CLAUDE.md`; an uninstall; a memory-only profile installing just
`/recall` and `/conclude`.

Front page: no before-and-after of one real session, no install footprint; it opens on
*institutional memory*, which sounds like the exact problem, and only well below says every change
takes the full process; the straw-dog markup is visible without explanation.

## Sources the panel cited

[Claude Code memory](https://code.claude.com/docs/en/memory) ·
[claude-mem](https://github.com/thedotmack/claude-mem) ·
[Mem0](https://docs.mem0.ai/integrations/claude-code) ·
[supermemory](https://supermemory.ai/blog/claude-code-memory-rehab/) ·
[OpenSpec vs Spec Kit](https://codemyspec.com/blog/openspec-vs-spec-kit) ·
[BMAD vs Spec Kit vs OpenSpec](https://medium.com/@reenbit/bmad-vs-spec-kit-vs-openspec-choosing-your-spec-driven-ai-framework-in-2026-a6996b3ebb8d) ·
[brownfield SDD](https://www.augmentcode.com/guides/spec-driven-development-brownfield-codebases) ·
[SDD tools 2026](https://www.marktechpost.com/2026/05/08/9-best-ai-tools-for-spec-driven-development-in-2026-kiro-bmad-gsd-and-more-compare/) ·
[GSD](https://www.codecentric.de/en/knowledge-hub/blog/the-anatomy-of-claude-code-workflows-turning-slash-commands-into-an-ai-development-system) ·
[Spec Kit vs OpenSpec](https://hiddedesmet.com/speckit-vs-openspec)

---

# Second run — 2026-09-26, at `7415581`

The same five needs, after *Where it stands* was rebalanced to say what the agent-led install
already does with a project that has something, and with one rule the first run lacked: each
reader read only what the product ships — the README, `LICENSE`, `AGENTS.md`, `CLAUDE.md` and
`.agents/` — never `docs/` *(the user)*. Two ran on a different model again.

**Verdicts: one *no*, four *not yet* — unchanged.**

## 1. Minimal ceremony — *no*

- **It solves the problem with a methodology** — two loops, tickets, RFCs, ADRs, a glossary,
  mechanisms, a rule-failure register: the process this reader is avoiding.
- **The light path isn't there** — *not yet* says so, and `AGENTS.md` makes every session run
  `/recall` first, *whatever the first message says*: a cost on every one of many daily changes.
- **`CLAUDE.md` goes away** — the install refuses while one exists; afterwards it is `@AGENTS.md`,
  and the facts move into `local.rules.md` in the harness's rule format; about 96 KB of skills and
  3,900 lines of Python arrive.
- **Heavy jargon; memory is plain prose** that no hook enforces.
- **Credit:** honest about its gaps, MIT, standard-library Python, an ask/auto switch for commit
  and push.

Compared: **built-in auto memory plus `CLAUDE.md`** — the zero-process baseline. **claude-mem** —
hooks capture automatically, not depending on the agent remembering `/conclude`; a better fit.
**Superpowers** — skills that fire only when relevant, lighter. **Spec Kit, BMAD** — the same
objection. **The cheapest fix for lost work** — frequent commits and a session-end hook writing a
handoff note.

Would change it: a declared small-change path; a memory-only install with a hook; installing
beside an existing `CLAUDE.md`; enforcement through hooks; evidence from other teams.

Front page: *the install never overwrites what is there* is true only as a refusal — the
`CLAUDE.md` is still restructured. *Small changes don't have to take the whole loop* under *works
today*, *no declared lighter process* under *not yet*, and a mandatory `/recall` in `AGENTS.md`
do not agree. Missing: per-session cost, and one worked one-line fix through the loop.

## 2. Existing instructions — *not yet*

- **It takes over the entry file** — refuses while `CLAUDE.md` or `AGENTS.md` exists; the 200
  lines move out, `CLAUDE.md` becomes `@AGENTS.md`, each fact re-authored as a rule. *Never
  overwrites* is technically true and means *you migrate first* — the throw-away this reader will
  not accept.
- **Heavy for three developers** — 23 skills, ticket positions like `01-0010.0150`, RFCs, paired
  closes, straw-dog tags, an announce line every session.
- **Immature** — weeks old, no stars or forks, one author; no uninstall, updates that don't say
  what changed.
- **Windows friction** — loader links need an elevated prompt, and Git for Windows clones them as
  text unless `core.symlinks` is set on every developer's machine.
- **Name collisions** — generic skill names (`/commit`, `/plan`, `/verify`, `/tdd`) land in
  `.claude/skills` and may shadow the team's four commands.
- **Good:** decisions in ADRs, architecture and a glossary, open work in tickets and never in
  session logs; local overrides applied last; drift checking. *The design thinking is real.*

Compared: **status quo plus conventions** — zero migration, no drift checks. **Spec Kit** — adds
`.specify/` beside the setup without replacing it; a spec per feature, not a queue of unfinished
work. **claude-mem, Remember** — automatic and opaque. **zircote/adr** — a drop-in ADR lifecycle,
no unfinished work. **Superpowers, BMAD** — mature, heavier.

Would change it: **an additive install that leaves `CLAUDE.md` alone and adds one import line**; a
lite mode of recall, conclude, ticket and ADR; an uninstall and a changelog; adoption beyond the
author.

Front page: *never overwrites* hides a hard refusal and a forced migration; silent that `CLAUDE.md`
becomes a pointer, that every session opens with an announce line, and how many skills land; the
Windows symlink requirement is only in `.agents/README.md`; no estimate of adoption effort.

## 3. Large existing codebase — *not yet*

- **It doesn't fix the main problem on day one** — no draft of the architecture from the code;
  written *as the work reaches them*, agents re-discover the system for months.
- **Built for one person, not fifteen** — global ticket positions in one queue table, one concerns
  file, one running session sequence, `/align` asking one person every decision; collides with an
  existing tracker.
- **Too new to trust** — weeks old, one contributor, the entry contract already at v16.
- **Heavy process and vocabulary** — `/recall` and a contract line every session, twenty-odd
  skills, invented terms.
- **Windows friction** — the loader links clone as text files until symlinks are enabled.
- **Worth taking:** the load-bearing test, one home per rule with a drift check, recording and
  rewording rules the agent did not follow.

Compared: **hierarchical `AGENTS.md` plus ADRs by hand** — nearly free, per module, read by both
hosts; no drift checks or loop. **OpenSpec** — specs only for what changes, suits brownfield;
weaker whole-system memory. **Spec Kit** — community, maturity, a constitution; also per change.
**BMAD** — struggles on legacy monoliths, token-heavy.

Would change it: drafting the architecture from the code on arrival; many developers at once —
per-branch-safe ticket IDs, or the existing tracker; a lighter process; an uninstall; evidence from
other teams.

Front page: *it has come into a large existing codebase* has no link, size or outcome; silent on
the single-maintainer assumption, a team, an external tracker, per-session cost and the project's
age; the clone ships the author's `docs/`, `.obsidian` and images, which a newcomer cannot tell
from the product.

## 4. Greenfield prototype — *not yet* (different model)

- **Zero adoption** — weeks old, no stars, forks or watchers, one contributor.
- **Real overhead** — an announce line every session, `/recall` before every message, human
  checkpoints at every `/align`, commit, push and split, all `ask` by default; a dense vocabulary.
- **Enforcement is aspirational** — *the agent is trusted to keep it* is the failure that burned
  this founder; no uninstall.
- **Genuinely good:** the right problem — tickets, ADRs, architecture and a glossary as durable
  memory, with scripted drift checking so documents don't silently rot; MIT, standard library,
  three hosts. *The diagnosis is right; the cure is unproven and heavy.*

Compared: **Spec Kit** — lighter, larger adoption, less rigorous memory. **BMAD** — more mature,
heavier. **Plain `CLAUDE.md` plus hand-written ADRs** — lowest overhead, no drift checking.

Would change it: evidence from other projects; host-enforced rules and an uninstall; proof the
ceremony survives a multi-week build.

Front page: *works today* is confident with no hint of a brand-new, single-author project; no
comparison to alternatives; no estimate of onboarding or token cost.

## 5. Single host, Cursor on Windows — *not yet* (different model)

- **Ceremony far beyond a solo freelancer's needs** — it reads as tooling for the author's own
  meta-project. *(Its count of 30 skills disagrees with the 23 shipped.)*
- **Scripts to trust blind** — the verification set runs the harness's Python tools, against this
  reader's boundary.
- **Windows and Cursor friction** — its fresh clone checked the loader links out as 17-byte text
  files, the `core.symlinks` pitfall `.agents/README.md` describes; the front page does not warn.
- **Admits its immaturity** — no uninstall, no update diff, no lighter path.
- **Credit:** the plan, test and verify discipline — vertical slices, red-green TDD, `/recall`,
  one rule one home — *better reasoned than most competitors*.

Compared: **Cursor's rules and memories** — lighter, no forced loop. **BMAD** — similar weight, a
bigger community, works in Cursor. **Memory Bank** — much lower ceremony. **Task Master AI** — a
lighter PRD-to-tasks breakdown, popular with Cursor users.

Would change it: a Windows install that doesn't depend on real symlinks or an external script; a
lighter tier; a week of hands-on use showing the ceremony pays for itself.

Front page: no Windows symlink warning; no word that `/verify` pulls in Python tooling even for a
pure React repository; jargon in *What holds it together* with no inline glossary link; no
screenshot of a ticket, RFC or output to gauge overhead.

## Sources the second run cited

[Claude Code memory](https://code.claude.com/docs/en/memory) ·
[claude-mem](https://docs.claude-mem.ai/introduction) ·
[methodologies ecosystem](https://claude-codex.fr/en/advanced/methodologies-ecosystem/) ·
[Spec Kit vs Superpowers](https://dev.to/truongpx396/spec-kit-vs-superpowers-a-comprehensive-comparison-practical-guide-to-combining-both-52jj) ·
[Spec Kit](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/) ·
[Remember](https://claude.com/plugins/remember) · [zircote/adr](https://github.com/zircote/adr) ·
[DataCamp on Superpowers and BMAD](https://www.datacamp.com/tutorial/spec-driven-development-with-claude-code) ·
[AGENTS.md for Java](https://dzone.com/articles/agents-md-java) ·
[Agent READMEs study](https://arxiv.org/html/2511.12884v1)

---

# Third run — 2026-09-26, at `ccb66b1`

The same five needs and the same rule — only what the product ships, never `docs/` — after the
page stopped saying *never overwrites* and dropped the small-changes line that contradicted its
*not yet*, and *Use it* gained the Windows link step. Two ran on a different model again.

**Verdicts: one *no*, four *not yet* — unchanged across all three runs.** No reader this time
called anything on the page misleading about the product; one checked it against the code and
found *everything else it documents accurate to what I found*.

## 1. Minimal ceremony — *no*

- **The process it is avoiding** — every change through the loop, and the page says the light
  path is missing; twenty copy tweaks a day need no ticket number.
- **Heavy** — about 16,600 words of skills and glossary, a coined vocabulary, and every session
  opening with `/recall` and a version line, paid for in tokens.
- **Takes over `CLAUDE.md`** — moved aside, replaced by a pointer, its rules folded into the local
  file's format.
- **The part it needs is small** — `/recall` and `/conclude` are the whole fix for forgetting, and
  `/conclude` is about a hundred words.
- **It doesn't address how work was lost** — uncommitted or overwritten changes; neither
  `commit=ask` nor tickets prevent that.

Compared: **built-in auto memory plus `CLAUDE.md`**; **claude-mem, Mem0** — automatic, a third-party
data path; **Superpowers** — lighter per session; **Spec Kit, BMAD, OpenSpec** — the same class;
**a home-made `/handoff` and frequent commits** — the least process, fixing both real failures.

Would change it: the lighter mode landing as recall and conclude only; an install that leaves
`CLAUDE.md` alone; an uninstall; evidence it prevents lost work, not only lost context.

Front page: *institutional memory* undersells it — it is a full delivery methodology, memory a
side effect; missing per-session cost and a worked one-line fix. *The not-yet list is honest.*

## 2. Large existing codebase — *not yet*

- **Too young and changing too fast for fifteen people** — one author, three weeks, the entry
  contract at v16.
- **Built for one person** — tickets, concerns, glossary and session records edited by every
  session; with fifteen in parallel, merge conflicts and competing truths; nothing on concurrent
  work or Jira.
- **Heavy process** — twenty-odd skills, a vocabulary, `/recall` every session, `/align` one
  question at a time, and no lighter path for routine fixes.
- **The core idea is right for this problem** — decisions in architecture, ADRs and a glossary,
  state rebuilt from records, settled decisions not reopened without evidence; building the
  architecture up as work reaches each area suits 600k lines.
- **No help mapping the existing code.**

Compared: **plain `AGENTS.md` plus ADRs** — where this reader would start; **OpenSpec** — for
existing codebases, no ADR or glossary discipline; **Spec Kit** — backed and at 1.0, weaker at
keeping existing decisions in force; **BMAD** — heavier, trouble with legacy code; **Kiro** — IDE
lock-in; **memory tools** — history, not curated decisions.

Would change it: six months of stable rules and outside users; a documented way for many
developers at once, ticket-system integration included; a lighter path; drafting the architecture
from the code; a published brownfield case study.

Front page: *a large existing codebase* with no evidence; silent on age, single author, the size of
what arrives, the entry-contract ritual and per-session cost; the *not yet* items link to tickets
under `docs/`, which a project replaces. *Unusually honest.*

## 3. Existing instructions — *not yet*, closer to no

- **Takes over the setup instead of sitting beside it** — `CLAUDE.md` moved aside and turned into
  a pointer, its content rewritten as rules; shipped core cannot be edited, only overridden.
- **Heavy ceremony** — `/recall` first *whatever the first message says*, the full loop, about 25
  skills and 3,200 lines of method; no lighter path, and most of this team's work is small.
- **Jargon** three people must learn.
- **Immature and hard to leave** — one author, no uninstall, no changelog.
- **Windows friction** — symlinks needing elevation and `core.symlinks` on every clone.
- **Good:** tickets with checkable criteria, ADRs and a glossary in the repository, a drift check
  on copied rules, standard-library Python, MIT, an honest README.

Compared: **Beads** — a git-backed issue graph for agents, additive, targets unfinished work, not
decisions; **OpenSpec** — the best fit for decision tracking with little overhead; **Spec Kit,
BMAD** — heavier; **doing it myself**.

Would change it: a lighter mode; an uninstall; an install leaving `CLAUDE.md` and
`.claude/commands` alone; an answer on name clashes; changelogs; outside teams.

Front page: silent that every session starts with `/recall` and a contract line, that core can be
overridden but not edited, on the method's size and per-session cost, on existing
`.claude/commands`, on the symlink step each teammate meets, and on the project's age and single
author.

## 4. Greenfield prototype — *not yet* (different model)

- **No track record** — seventeen days, no stars, forks or watchers, one committer.
- **Ceremony against week-one speed** — the loop, the entry contract every session, a vocabulary;
  the page admits there is no fast mode yet.
- **The core idea is genuinely good and concrete** — *not just "write good docs" advice*: an
  installer, updater and checker, drift detection, and a mechanism for exactly the failure that
  burned this founder. *More mechanism than most alternatives offer.*

Compared: **Spec Kit** — far more proven, no memory, drift or postmortem layer; **BMAD** — more
popular, role-play overhead, less focused on why; **plain `AGENTS.md` plus ADRs** — relies wholly
on discipline.

Would change it: evidence of outside use — even a handful of stars, forks or issues — or the
lighter mode, whose ticket exists.

Front page: the confident *works today* and the polished diagram give no hint of a seventeen-day
solo project with no outside users.

## 5. Single host, Cursor on Windows — *not yet* (different model)

- **Zero adoption, brand new.**
- **Disproportionate for a freelancer** — about 4,000 lines of markdown and 8,300 of Python into
  every client repository: *a second codebase to maintain per client*.
- **Runs tools this reader doesn't understand** — a script that rewrites files, manages links,
  injects rule blocks.
- **Heavy ceremony for solo work.**
- **Cursor support is second-class** — reached through a link that may need elevation on Windows.

Compared: **Cursor's rules and memories** — native, thin; **Cursor Memory Bank** — the same idea at
a tenth of the surface, easy to remove; **Spec Kit** — official Cursor integration; **BMAD**;
**claude-task-master** — task breakdown only.

Would change it: real adoption and months of stability; a plain description of what the install
script does before running it; an opt-in light mode.

Front page: *works today in Claude Code, Codex and Cursor* reads as parity, and the Windows link
caveat it calls buried in `.agents/README.md` — *(though* Use it *carries it since `ccb66b1`,
which this reader read)*; no maturity disclosure. *Everything else it documents was accurate to the
code.*

## Sources the third run cited

[Claude Code memory](https://code.claude.com/docs/en/memory) ·
[claude-mem guide](https://www.datacamp.com/tutorial/claude-mem-guide) ·
[Mem0 for Claude Code](https://mem0.ai/blog/claude-code-memory) ·
[spec frameworks compared](https://docs.bswen.com/blog/2026-08-07-ai-spec-frameworks-compared/) ·
[OpenSpec](https://github.com/Fission-AI/openspec) ·
[OpenSpec for existing projects](https://github.com/Fission-AI/OpenSpec/blob/main/docs/existing-projects.md) ·
[best SDD tools](https://www.augmentcode.com/tools/best-spec-driven-development-tools) ·
[ADRs for agents](https://dev.to/naman_here/adrs-for-ai-coding-agents-how-to-make-every-agent-read-architecture-decisions-3he4) ·
[Beads](https://github.com/steveyegge/beads) ·
[OpenSpec vs Spec Kit](https://hashrocket.com/blog/posts/openspec-vs-spec-kit-choosing-the-right-ai-driven-development-workflow-for-your-team)

---

# Fourth run — 2026-09-26, at `c845092`

The same five needs and the same reading rule, after the page gained *Why a loop* — agents kept in
check, work that stops at any step and any agent resumes, the user's stops optional, `commit=auto`
committing verified work — the same-opening-every-session line, and a first-session `/align` for an
existing codebase. **The question was split** *(the user)*: first a verdict on the method and its
tooling alone, age and adoption set aside; then, separately, what the reader would need before
trusting it.

**Verdicts on merit: five *not for my case*.** Every reader credited the method; none of the five
needs it. Condensed:

## 1. Minimal ceremony — *not for my case*

A full delivery process where a memory fix is wanted; the part that fixes forgetting — `/recall`
and `/conclude`, about thirty lines — is small and copyable, and the rest keeps the method itself
consistent. Replaces `CLAUDE.md`; nothing forces the recall to happen — a hook would; lost work is
solved by commits and checkpoints. Best fit instead: built-in memory with a session-start hook and a
handoff note. **Its advantage over all:** *auditable written decisions and drift detection between
docs and code* — for a larger, long-lived codebase. Trust needs: a light mode, an uninstall,
updates that say what changed, adoption beyond the author, a case study. Front page: *institutional
memory* never says what the memory costs per change; *observability* named, its cost in tokens or
time not; how much it installs.

## 2. Large existing codebase — *not for my case*

**No team model** — `/align` interviews one person; nothing says whose decision wins across fifteen
on parallel branches; the queue table, repositioned tickets and incrementally numbered sessions
collide in merges. **Arrival is an interview, not tooling** — nothing drafts a first architecture
from 600k lines of Java. **Cost every session** — a mandatory `/recall`, no light path, the harness's
own meta-rules carried in the entry file. **Worth taking:** one home per decision, `/recall` citing
what decided a question or where it is still open, no reopening without evidence — *squarely* the
problem. Compared: nested `AGENTS.md` plus ADRs; Spec Kit, whose per-branch specs collide less, with
a brownfield extension; BMAD, whose document-project task generates brownfield docs from code;
Kiro's steering. Trust needs: a multi-developer install, a published large-codebase case, measured
per-session cost, the light mode, Jira owning tickets, an uninstall, releases, more than one
contributor. Front page: *institutional memory for a workforce* implies a team, and everything is
single-user; *describing an existing codebase* under *works today* is an interview, with the
automated part under *not yet*; silent on per-session cost, the meta-rules shipped in the entry
file, and the fixed `docs/` layout.

## 3. Existing instructions — *not for my case*

Arrival replaces what works — the `CLAUDE.md` spread into the local file and the harness's documents,
left a pointer (the commands would likely survive). Too much ceremony for three people; ticket
positions, the shared queue and session numbers collide across branches; a private vocabulary.
**Real strengths:** one source per rule with a drift checker; decisions in ADRs and architecture,
open work in tickets, never in session logs — *exactly what I want*. Compared: **Beads** — a
dependency graph of unfinished work, hash IDs that avoid merge collisions, additive; OpenSpec; Spec
Kit; BMAD; plain Claude Code with an ADR folder and a `/handoff`. Trust needs: installs by others
into projects with setups, with before-and-after `CLAUDE.md`; a light mode; an uninstall; releases
and changelogs; a team story; some enforcement. Front page: frames the `CLAUDE.md` takeover as a
strength; missing per-task cost, what a one-line fix goes through, team use, a sample ticket.

## 4. Greenfield prototype — *not for my case* (different model)

Process weight against a two-month solo timeline — two rings, the entry contract, mechanisms, drift
checks, a vocabulary to learn before shipping product. **Targets the real fear well in principle** —
forced tickets and architecture, *document load-bearing, code the rest*, drift detection, straw dogs
naming what resolves them: *a genuinely good idea, just heavy machinery for one founder*. Windows
friction, issue #1. Compared: Spec Kit; BMAD; **Agent-OS** — reverse-engineers a codebase's own
conventions, closer to just enough process; plain `CLAUDE.md` plus ADRs, *60% of the benefit*.
Trust needs: a run on someone else's codebase, outside users reporting outcomes, a release, issue #1
closed, a case study of how much it slows early iteration. Front page: candid and mostly accurate;
silent on how much ceremony an agent produces per turn and on the vocabulary's cost.

## 5. Single host, Cursor on Windows — *not for my case* (different model)

Trust cost first — Python scripts that install, check and repair a document tree, to be read before
running on client code. A vocabulary used before it is defined. Ceremony scaled for one evolving
project, not quick tasks across three repositories. **To its credit:** *the loop shape is right for
what I asked* — plan, red-green TDD in vertical slices, implement, verify against the project's own
checks — and memory as committed markdown, *genuinely durable, genuinely auditable*. Windows
friction, and the one open GitHub issue is that failure. Compared: BMAD with native Cursor rules;
Spec Kit, lighter and easiest to trust; Memory Bank; Cursor's own rules and memories. Trust needs:
adoption, issue #1 fixed, a light mode, a plain walkthrough of what the install writes. Front page:
no disclosure of a new single-author project; jargon before explanation; the loop diagram implies
one ceremony size for everything.

---

# Fifth run — 2026-09-26, at `cc5087a`

The same five needs and reading rule, the full question restored — a verdict on merit, **what
would change it**, and apart, what the reader would need to trust it — after the page said that
the skills and records are the agent's equipment, that the checks are tested tooling, how to trial
it, and that it assumes one person steering. Two ran on a different model again.

**Verdicts on merit: five *not for my case*.** What would change each answer, which is what this run
was for, condensed:

| Reader | What would change the answer |
|---|---|
| Minimal ceremony | an opt-in, tested light mode — recall, conclude and a decisions log, no tickets or RFCs for small changes, `CLAUDE.md` left alone; hook enforcement; an uninstall |
| Existing instructions | ticket IDs safe on parallel branches, or GitHub Issues as the ticket store; an install that merges into an existing `CLAUDE.md`; a declared light path; **a plain-language entry file** |
| Large existing codebase | multi-developer operation — branch-safe IDs, tickets in the team's tracker; a pass drafting architecture and glossary from the code on install; a light path; **a slim `AGENTS.md` without the method's own vocabulary and meta-rules** |
| Greenfield prototype | the light mode landing, trivial changes skipping ticket, plan and verify while keeping the memory; evidence from other projects that re-deciding falls without slowing delivery |
| Cursor on Windows | a light track; Cursor support not depending on Windows symlinks; **a quick start needing none of the coined terms** |

What each would need to trust it: users beyond the author and months of stability (all five); an
uninstall and changelogs (three); **the per-session token and time overhead measured** (three);
**a before-and-after on the three signals the page itself proposes** (the large codebase); a
multi-developer pilot; running the test suite and drift checks oneself.

What each credited: the rule that `/recall` cites where each open question is still open; straw
dogs binding *not yet* to a ticket; one source per rule with a standard-library drift check;
rule failures written down and reworded; overrides in one local file; *"persistent decisions,
architecture and glossary plus an explicit what's-still-open beats vibe-coded amnesia."*

Front page, as they read it:

- **The single-steering limit is buried** — seventh of eight in *not yet*, when for any team it is
  the headline (existing instructions, large codebase).
- **No cost figures** — per change, per session, for a one-line fix (four of five).
- ***You meet a few terms* undersells it**, since the entry file every session loads carries the
  method's vocabulary, and teammates reviewing what agents write meet it too (two); and the shipped
  entry file carries the harness's own development rules into every recipient session (the large
  codebase) — a finding about core, not the page.
- **No example session** (two); **no comparison** to Spec Kit, BMAD or a plain `AGENTS.md`, so a
  newcomer cannot place it (greenfield); which skills could be skipped (minimal ceremony).
- **The `CLAUDE.md` takeover** still reads as an arrival feature (minimal ceremony).
- The license's *contributors*, plural, reads as more than one author (greenfield).
- Two readers on the other model again said the Windows link caveat lives only in
  `.agents/README.md`; *Use it* carries it, and a third called it *mentioned only in passing*.

Alternatives newly named in this run: **Backlog.md** — tasks, decisions and docs as markdown in git
with a CLI, an MCP server and a board, additive to an existing `CLAUDE.md`; **claude-remember**;
**Agent OS** again, for adapting to any tool.

---

# Sixth run — 2026-09-26, at `b409d29`

The same five needs, reading rule and full question, after the page said that large work starts as
a spec and is split into slices, and that records stay current instead of piling up. Still not
clean-room: started from this session, each reader told to set aside the context it inherited.

**Verdicts on merit: five *not for my case*.** Condensed:

| Reader | Deciding reason | What would change the answer |
|---|---|---|
| Minimal ceremony | heavy by default for a dozen copy tweaks a day; the part that fixes forgetting is small | a declared light path — a small fix skips ticket and plan but keeps a log line and an auto-commit; keeping `CLAUDE.md`; a minimal profile; a work-in-progress checkpoint at `/conclude` |
| Existing instructions | single steering — three developers decides it | tickets in GitHub Issues or Linear, or branch-safe numbering; installing beside an authoritative `CLAUDE.md`; a light path; an uninstall — *lift the team limit and the takeover and I'd pilot it* |
| Large existing codebase | single steering; arrival is instructions, not tooling | many-developer support with an issue-tracker backend; an arrival script drafting architecture, glossary and ADRs from the code, marked unverified; a light path; the harness's own development rules out of the shipped entry file |
| Greenfield prototype | **the ceremony has nothing to bite on yet** — `/maintain`'s drift and `/align`'s contradictions pay off once there is an architecture and history to drift from | a mode that scales ceremony to the work's size; evidence it holds up once there is enough architecture for `/maintain` to find drift |
| Cursor on Windows | a Python engine to audit before trusting it; a governance system for a product team, not a few-hour ticket | a layer simple enough to read directly; a light path; Windows support with no git configuration step; proof on independent repositories |

Credited on merit: the decision model — decisions in architecture, ADRs and a glossary, concerns
tracked, *do not reopen an accepted decision without new evidence* hitting the contradiction problem
directly; records in the repository, *better thought through than memory plugins*; one home per rule
and drift checks, beating Spec Kit and BMAD there; it *genuinely addresses the undocumented why
better than a plain `CLAUDE.md`*. The large-codebase reader still found a plain `AGENTS.md` with ADRs
*most of this harness's value*.

Trust needs, as in every run: users beyond the author; an uninstall and changelogs; measured cost
per trivial change; a pilot measured by the page's own three signals; a worked example of arriving
in a project like the reader's.

Front page, as read:

- **The team limit is buried** — near the bottom of eight, when it decides it for any team (three
  readers, the third run in a row).
- ***It has come into a large existing codebase*** still carries no evidence or outcome (the large
  codebase, the third run in a row).
- **No worked example** of a day, a bug fix, or an arrival (three).
- **No cost figures** (three).
- *You don't run the steps* reads as lightweight when every step still runs, by the agent; *you meet
  a few terms* is contradicted by the terms on the page itself.
- **Windows:** a reader cloning the repository found `.claude/skills` and `.cursor/skills` checked
  out as 17-byte text files — `core.symlinks` defaults to false in Git for Windows — which the
  install's link step does not cover for a teammate who clones a project that already has them.
