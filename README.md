<p align="center">
  <img src="https://github.com/dveyarangi/goodwolf-harness/raw/main/goodwolf.webp" alt="GoodWolf — a wolf amid a web of linked nodes" width="240">
</p>

# GoodWolf Harness

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-3776AB?logo=python&logoColor=white)](#use-it-instructions-for-your-agent)
[![Dependencies: standard library only](https://img.shields.io/badge/dependencies-stdlib%20only-brightgreen.svg)](#use-it-instructions-for-your-agent)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-supported-D97757?logo=claude&logoColor=white)](#where-it-stands)
[![Codex](https://img.shields.io/badge/Codex-supported-412991?logo=openai&logoColor=white)](#where-it-stands)
[![Cursor](https://img.shields.io/badge/Cursor-supported-000000?logo=cursor&logoColor=white)](#where-it-stands)
[![Last commit](https://img.shields.io/github/last-commit/dveyarangi/goodwolf-harness)](https://github.com/dveyarangi/goodwolf-harness/commits/main)

Project memory and a working method for coding agents.

*The deeper the woods, the meaner the wolves*, says the proverb. A project that has lived for
months is deep woods: hundreds of decisions, rules with their reasons, work stopped halfway, questions
nobody answered yet. A coding agent walks in cold every session, knowing the code but not why it
is the way it is, and the deeper the woods, the more it costs. This is the other wolf — the one
that knows the woods. Working with agents on one project for weeks hurts in three ways:

- **The agent is ineffective.** It calls work done that doesn't work, or isn't what you meant.
- **The agent is expensive.** Tokens, time and rework go on rediscovering what it already knew,
  and your attention goes on re-explaining it.
- **You are in the wrong place.** Either decisions that matter get made without you, or you end up
  approving every step and babysitting work the agent could carry.

GoodWolf answers all three from your repository: plain Markdown and a few standard-library Python
scripts, in Claude Code, Codex and Cursor. Fewer steps, each more precise: at every step the agent
knows what is needed now — which rule, which record, which question — and does that, not the rest.

## What it adds

- **A memory of the project between sessions.** What was decided and why, and what each decision
  still waits on; what is half-built and at which step; every question you raised, kept with where
  the thinking got to, until it is answered. A session starts from these, so "continue" is enough,
  and "we settled that on Tuesday, has something changed?" is a thing the agent can say.
- **You where it matters, and nowhere else.** A decision whose mistake would break several parts
  of the project comes to you with options and a recommendation; anything smaller the agent settles
  and reports. You draw the line between the two, once, on a short list.
- **Records that stay in agreement.** Each rule written once and copied by a script to wherever it
  is read; a check that fails when a copy drifts; and a disagreement between two records, or a
  record and the code, repaired by the session that meets it, not left for an audit.
- **A working method, if you want one.** A piece of work moves ticket → plan → build → verify →
  maintain, and large work is agreed with you on its question first. If your project already has
  a method, yours stays: see the next two sections.

## It fits the project you have

GoodWolf integrates. Your rules file, your CI gates, your decision records, your pull-request
discipline stay as they are and stay the enforcement — it adds no gate and removes none, and its
own checks read only its own records. What it brings is what those usually do not hold: the state
of a decision, the place where a session stopped and why, the questions still open, and where you
stand among them. If you would rather it replaced your method, it can take yours in; that is your
call, made on a report, not on this page.

## How it meets your project

<straw-dog question="q-0037.0006.0020.0001">
In a project that already has rules, skills or a method of its own, the install stops before
writing anything and offers a study instead. Your agent reads how your rules, decisions and history
are kept, measures what it costs a newcomer to recover the state of the project, and writes one
report in your project's language: what GoodWolf would change here, what it would cost you, and in
what order. Nothing is moved. You read the report and decide how to proceed. Taking your method in
after a yes — alongside yours, or in its place — is the next step, and not built yet.
</straw-dog>

Whether your project needs this is answered by that study, not by comparing lists on this page:
a mature project has most of what a tool like this is usually praised for, and what it lacks is
exactly what the study is built to find.

In a fresh project, the install lands the method and the first session works out with you what
the project is and how it should be built.

## What it does about each

**So the work is what you meant, and it works:**

- **What you decide gets built, and stays built.** A plan pulls the code toward it until the work
  matches. A decision about the architecture binds the code from then on: code that drifts from it
  is brought back, never the decision bent to fit the code, and it changes only when you decide
  again.
- **Done means checked.** Each change becomes a ticket with checkable criteria and a written plan,
  is built test-first, and is verified against the ticket, the plan and your tests before it
  counts as done.
- **Instructions that reach the agent.** Each rule lives in one place and is copied by a script to
  wherever it is read, and a check fails if a copy drifts. So the agent isn't working from
  scattered, contradictory instructions.

**So you stop paying twice:**

- **A memory of the project, not just of the code.** What was decided and why, what is half-built
  and at which step, and what is still undecided are kept as files. Every session starts from them,
  so "continue" is enough.
- **Nothing you raise is lost.** Every open question is kept until it is answered, with where the
  thinking had got to, and the ones you keep returning to come up first. Each message is placed
  under the question it is about, so a side remark is noted instead of derailing the work.

**So you are where it matters, and nowhere else:**

- **Decisions go by their weight.** A decision whose mistake would break several parts of the
  project comes to you, with the agent's recommendation. Anything smaller the agent settles and
  tells you about. When it is unsure which one it is, it asks.
- **You set the line.** You say where the agent stops for your yes, on one short list of decisions
  from writing code to what the project is for: below the line it acts, at it it shows you first,
  above it you decide.
- **You can see what it stands on.** Every step leaves a short record you can read, so checking the
  agent's work is cheap and trusting it isn't blind.
- **You can think out loud.** Jump from topic to topic. What you say lands under the question it
  belongs to and comes back when that topic does.

**Two goals it can't promise yet:**

- **Better over time, not worse.** One home for every decision, a maintenance pass that keeps
  documents and code in agreement, and rules reworded each time the agent ignores one all point
  this way. Nothing yet measures whether it holds.
- **No harm.** The harness's own scripts refuse rather than overwrite, and work leaves your machine only the way you said it may.
  Nothing yet bounds what the agent itself may do.

## A morning with it

An illustration: the project is made up; the steps are what the harness does.

**You:** continue

**Agent:** Picking up from yesterday. The export endpoint landed, but one of its acceptance checks
is still open: the CSV header test was never written. Next in the queue is the import endpoint.
And your question from Tuesday — do retries need idempotency keys? — is still open; we were
leaning yes. Close out the export first?

**You:** Yes, then import.

*It writes the test, ticks the check, and plans the import. Halfway through, it stops.*

**Agent:** `docs/architecture.md` doesn't say whether an import is all-or-nothing or row by row.
I'd go all-or-nothing: a half-applied import is hard to undo. Your call?

**You:** All-or-nothing.

**Agent:** Added to `docs/architecture.md`, with the reason.

*It builds the import test-first, runs your tests, checks the result against the ticket, and
asks before committing.*

**You:** Oh — exports will need paging at some point.

**Agent:** Noted as an open question under exports. It will come up again when you next work on
exports.

*Two days later, a fresh session:*

**You:** Let's make imports row by row, it's simpler.

**Agent:** Two days ago we settled on all-or-nothing, because a half-applied import is hard to
undo. Has something changed? If so, I'll reopen it and record why.

You don't type the steps or learn the commands. The agent moves the work along and stops wherever
you have told it to ask.

## Who it is for, and what it costs

It is for **steering agents on a project that lives for months**, in one session or several at
once — a long-lived product, a large refactor, a codebase you return to between other work —
where forgetting costs more every week. It is not worth it in a prototype's first week, when there is nothing settled yet
to keep, or for one-off scripts.

Before you install, know this:

- **Several sessions at once, yes; keeping them apart is your host's job.** Sessions in one tree
  see where the others stand, and the harness's own scripts refuse a write to an entry that moved
  since it was read. Nothing here locks a file: that is your host's — its edit tool refuses to
  write over a file that changed since the agent read it, and where it offers a worktree per
  session, each works in its own.
  <straw-dog question="q-0033.0004">A team sharing one queue across branches is not tested yet, and your team's tracker can't yet take the tickets' place.</straw-dog>
- <straw-dog question="q-0037.0013.0003">**The loop's weight is one size so far.** Every change is meant to go through ticket, plan, build and verify. You can tell the agent to skip that for a one-line fix, but there is no setting yet that makes small work light by itself; a project with a fast cadence of its own keeps it, and the loop's steps join it where the study says they help.</straw-dog>
- <straw-dog question="q-0037.0006.0005">**It adds no gates and removes none.** Everything here is the agent following written rules, plus scripts that check the harness's own files. Your gates stay the enforcement; a model can still slip against a rule, and the records are what lets you see it and reword the rule.</straw-dog>
- <straw-dog question="q-0037.0006.0013">**No uninstall command.** Everything it adds is files, so reverting the install commit removes the harness. What it wrote under `docs/` afterwards stays until you delete it.</straw-dog>

<straw-dog question="q-0038.0001">What it saves has not been measured. To judge it, install it into one project and watch three things over a few weeks: whether an agent arriving cold re-decides less, whether work stopped in one session is found at its step in the next, and whether the questions you raise come back. In a project with a method of its own, the study's report carries a measure to repeat after the migration: what it cost a newcomer to recover the project's state before, and after.</straw-dog>

## It changes with your project

Rule files for agents rot. Rules pile up and contradict each other, the agent quietly ignores
some, and your edits get overwritten when you pull an update. Here:

- **Your changes survive updates.** Your test commands, your approval settings, and any shipped
  rule you want different go in one file, `local.rules.md`. Every install and update applies it
  last and never touches it. If you edited a shipped file by hand instead, an update stops and
  tells you rather than overwrite it.
- **A rule the agent ignored gets reworded, and the next miss shows whether that worked.** When a
  rule was in place and not followed, the agent logs the miss in `docs/rule-failures.md`, shows
  you the rewording, and lands it as one commit you can review and revert.
  <straw-dog question="q-0037.0012">So far it is you who notices the miss: every one in this repository's log was caught by the person, not the agent.</straw-dog>
- **No two copies of a rule disagree.** Each rule is written in one place and copied by a script
  into every instruction that uses it. A check fails if a copy drifts from its source; it runs at
  every install and update, and in your own checks if you add it there.
- **Your own skills get the same checks.** A guided command, `/mechanism`, walks you through adding
  one, and the scripts that check the shipped skills then check yours.
- **Anything provisional says what it waits on.** A rule that will change once an open question is
  answered names that question, and the session report tells you when the answer has landed.

**An example from this repository's log.** One rule tells the agent to file each of your
messages under the open question it belongs to. On 5 October, new sessions kept filing messages
under questions that only sounded similar. Each time, the miss was logged and the rule tightened —
four times that day — until it said: file a message under the narrowest question that actually
covers it, never under one that merely looks alike. The sessions after that got it right. The
harness has been built with itself since September, in 66 sessions, and its log holds 62 misses
so far.

To override a shipped rule, add a section naming it.

## How it works

**When a document and the code disagree, which one is fixed.** Every written thing in the
project is one of four kinds, and the kind says which side wins.

| the document says | who is right | when they disagree | for example |
|---|---|---|---|
| what it intends to become | the document, until the code gets there | the code moves toward it; the document is done once they match | a ticket, a plan, an open question |
| what must always hold | the document, always | the code is fixed; the document changes only by a decision | the architecture, the glossary |
| what exists | the code | the document is rebuilt from the code, never edited by hand | the ticket list, a check's report |
| what happened | neither — it is past | nothing is fixed | a session record, a finished ticket |

**How the right things reach the agent.** There is no vector database and no similarity search;
what the agent reads is chosen by which question you are on. Open questions form a tree, each
under the one it is part of. When a session starts, the agent reads a status report: the open
questions you keep returning to, the ones parked until a condition that may now hold, and what
other running sessions are on. Before each reply it reads the part of the tree around the
question you are on, and follows links from there.

**The steps.** You won't type these; they are the names you will see in the agent's replies. A
session starts with `/recall`, which finds where the work stopped; `/align` settles with you
whatever needs deciding; `/conclude` writes down what the next session needs. A piece of work
moves `/ticket` → `/plan` → `/implement` → `/verify` → `/maintain`; large work is first agreed with
you on its question and split into small tickets. `/verify` asks whether finished work keeps the
promises its ticket and plan made; `/maintain` asks whether the documents still agree with each
other and with the code. Before a big decision, `/impact` traces what a change touches in this
project, and `/discover` asks a separate agent that has not read the project how things like it
usually go wrong elsewhere.

![The session steps — /recall, /align, /conclude — joined at /align to the work steps — /ticket, /plan, /implement, /verify, /maintain](https://github.com/dveyarangi/goodwolf-harness/raw/main/dev-skills-readme.png)

The rules are in [AGENTS.md](AGENTS.md) and every skill is under [`.agents/skills/`](.agents/skills/).

## Where it stands

**Works today**, in Claude Code, Codex and Cursor:

- Installing into a project, updating it, and checking that the installed copy is intact, with
  your own rules applied last.
- Meeting a project that already has a method: the install stops before writing, and the agent
  studies the project and writes the report you decide on.
- Arriving in a project that already has code: the first session after install works out with
  you what the project is, and writes its architecture, decisions and glossary from that
  conversation, deepening as the work reaches each part.
- The open-question tree, with every message placed in it before the reply.
- Each rule kept in one place, and checks on the harness's own files, run at install and update.

**Not yet:**

- <straw-dog question="q-0037.0006.0020.0001.0001">Taking a project's own method in after the report — alongside yours, with your rules file kept and one line added, or in its place — is not built; the report ends with your decision, and the next step is by hand.</straw-dog>
- <straw-dog question="q-0037.0013.0002">You can't yet say which kinds of decision stop for you; the line between yours and the agent's is drawn by its judgement of what bears load.</straw-dog>
- <straw-dog question="q-0037.0006.0011.0004">The install doesn't yet find what your project exists to solve, or the answers already built into its docs and code; the first session builds them with you instead.</straw-dog>
- <straw-dog question="q-0037.0006.0020.0002.0003">Updates name the files they changed, not what changed in them or what your project has to do about it.</straw-dog>
- <straw-dog question="q-0037.0006.0018">There is no way yet to send improvements your project makes to the harness back upstream.</straw-dog>
- <straw-dog question="q-0037.0006.0023">Other hosts — Copilot, Gemini CLI, OpenCode and the rest — aren't supported yet.</straw-dog>

## Use it (instructions for your agent)

Asked to install the harness into a project, or asked whether the project needs it:

1. Clone this repository beside the project, never into it. Already cloned into the folder where
   the project was meant to be? From that folder,
   `python .agents/scripts/gw/harness.py . --install --replace-clone` turns the clean clone into
   an install; go on to step 3.
2. From the project's root, run `python <clone>/.agents/scripts/gw/harness.py . --install`. It
   writes nothing if it refuses, and says why. In a project with rules, skills or a method of its
   own it refuses and names what it found: that is the study's door, not a failure.
3. Read [`.agents/skills/harness/SKILL.md`](.agents/skills/harness/SKILL.md) and follow it: it
   says how to offer and write the study in a project that has a method, how to report what
   arrived in a fresh one, and how to set up the project's own rules with the person. Updating
   and checking the installed copy are in the same skill.

What lands in a fresh repository: `.agents/` (the skills, the scripts and their tests), `AGENTS.md`
(the rules every session reads), a one-line `CLAUDE.md` pointing to it, and a starting work queue
in `docs/tickets/`. `local.rules.md` and the rest of `docs/` — architecture, decisions, questions,
session notes — are written as you work. A repository with a method of its own keeps everything it
has: nothing lands there until you have read the report and said so. Claude Code and Cursor reach
the skills through symbolic links the install makes in each clone; on Windows, where creating one
may need an elevated prompt, it prints the command to run.

Python 3.12 or later, standard library only. [MIT licensed](LICENSE).
