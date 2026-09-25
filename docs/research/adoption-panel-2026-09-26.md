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
