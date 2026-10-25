<p align="center">
  <img src="https://github.com/dveyarangi/goodwolf-harness/raw/main/goodwolf.webp" alt="GoodWolf — a wolf amid a web of linked nodes" width="240">
</p>

# GoodWolf Harness

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-3776AB?logo=python&logoColor=white)](#use-it-instructions-for-your-agent)
[![Dependencies: standard library only](https://img.shields.io/badge/dependencies-stdlib%20only-brightgreen.svg)](#use-it-instructions-for-your-agent)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-supported-D97757?logo=claude&logoColor=white)](#use-it-instructions-for-your-agent)
[![Codex](https://img.shields.io/badge/Codex-supported-412991?logo=openai&logoColor=white)](#use-it-instructions-for-your-agent)
[![Cursor](https://img.shields.io/badge/Cursor-supported-000000?logo=cursor&logoColor=white)](#use-it-instructions-for-your-agent)
[![Last commit](https://img.shields.io/github/last-commit/dveyarangi/goodwolf-harness)](https://github.com/dveyarangi/goodwolf-harness/commits/main)

Work with an agent comes apart over time: the memory fills with clutter, the instructions stop
being followed, the goal slips — and you end up either left out of the decisions or caught in
every one of them. GoodWolf keeps that work coherent from its first day: one true memory in your
own files, instructions that reach the moment they are for, the goal held while it moves, and you
at the decisions that bear the weight. On it you build your own method — for code, study,
research, a diary — and the method gets all of this too. Software development is the first method
built on it, and the one it is tested by.

*The deeper the woods, the meaner the wolves*, says the proverb. Every session makes the woods
deeper: decisions with their reasons, rules, work stopped halfway, questions nobody answered yet.
An agent walks in cold every time, and the deeper the woods, the more that costs — on the first day
a few files, after months the whole project. This is the other wolf — the one that knows the woods.
The cost comes in three ways:

- **The agent is ineffective.** It calls work done that isn't, or isn't what you meant.
- **The agent is expensive.** Tokens, time and rework go on rediscovering what it already knew,
  and your attention goes on re-explaining it.
- **You are in the wrong place.** Either decisions that matter get made without you, or you end up
  approving every step and babysitting work the agent could carry.

GoodWolf answers all three from your own files: plain Markdown and a few standard-library Python
scripts, in Claude Code, Codex and Cursor. Fewer steps, each more precise: at every step the agent
knows what is needed now — which rule, which record, which question — and does that, not the rest.

## It works, or it seems to work

If your project keeps rules, plans and a memory of its own, much of what follows will sound
familiar. The question is not whether you have it, but whether it works — and a project rarely
checks that about itself. Before comparing lists, have your agent find out:

- **Pick one check your project trusts** — a test run, a gate, a closing criterion — and make it
  fail on purpose. Does it? A suite that finds no tests can still exit green.
- **Find the next step of the work.** Is it written down, and when was the last one taken?
- **Open whatever holds the questions waiting on you.** How many, and how old is the oldest?
- **Start a fresh session and ask where the work stands.** How much does it read, and is its
  answer right?

Whatever comes back wrong is what GoodWolf is for.

## Where you start

- **New work.** The first session works out with you what the work is and how it should be done;
  the memory and the method grow with it from there, so nothing piles up to be cleaned later.
- **Work that has lived.** A study comes first, and it installs nothing: your agent reads how your
  rules, decisions and history are kept, measures what it costs a newcomer to recover where things
  stand, and writes one report — what GoodWolf would change here, what it would cost you, in what
  order. Nothing is moved; you decide on the report.
- **A method of your own.** If you have built a setup of your own — Markdown files, prompts, a
  project to learn with — you know how it ends: it grows complicated and starts to tangle. Build it
  on GoodWolf instead, with `/mechanism`, and the checks that hold the shipped method hold yours.

## What it gives you

- **A memory that stays true.** Not notes an agent keeps, but the project's working mind, held
  together:
  - every fact in one home, held there by maintenance;
  - every record knowing whether it says what will be, what must always hold, what is, or what
    was — and so which side wins when it and the code disagree;
  - every decision linked to what it rests on, so that when an answer changes, what stood on it
    comes up;
  - the questions still open and the ideas on the way, each with where the thinking got to, so
    nothing you raise sinks;
  - where each piece of work stopped, at which step, and why.

  It reaches the agent before every message, not when the agent thinks to look; a disagreement is
  repaired where a session meets it. "Continue" is enough. *In your project: your last stalled piece
  of work — is the reason it stopped written anywhere? Where do the questions waiting on you live,
  and how old is the oldest?*
- **One home for every rule.** A rule is written once and copied by script to wherever it is read,
  and a check fails the moment a copy drifts, so the agent is never working from two versions of
  the same instruction. *In your project: when a rule last changed, did every copy of it change?*
- **A provisional decision knows what will change it.** Text written while a question is still
  open is tied to that question, and comes up for rewriting when the question is answered — so
  "for now" does not quietly become "always". *In your project: how much of your docs says "for
  now", and what would tell you it no longer holds?*
- **A rule the agent ignored becomes a record.** The miss is logged with the rule that was in
  place, and the rule is amended in the strongest form that will hold — a check, a hook or a gate
  where one can hold it, a rewording where none can — in one reviewable commit; a miss that comes
  back gets a mechanical fix. *In your project: do the gates your rules name all run, and does each check
  what its rule claims? What share of your fixes did a person find, not a check?*
- **You where it matters, and nowhere else.** You draw the line once, on a ladder ordered by how
  far a decision reaches: below it the agent acts, at it the agent shows you first, above it you
  decide, with options and a recommendation. You can think out loud: whatever you say lands under
  the question it belongs to and comes back when that topic does. *In your project: take your
  last twenty merged changes — which decisions did an agent take on its own that, by how far they
  reach, should have come to you, and where is the line written that would have told it? And of
  the last ten things it asked you, how many needed you?*
- **Checking and keeping are two questions.** Whether finished work keeps the promises its ticket
  and plan made, and whether the documents still agree with each other and with the code, are asked
  separately, so neither hides behind the other. A disagreement a session meets is repaired there,
  not left for an audit, and you can schedule `/maintain` with your host so that drift no session
  meets is swept as well. *In your project: when were the docs last checked against the
  code?*
- **A method that looks like ceremony and works as speed.** A piece of work moves ticket → plan →
  build → verify → maintain, each step as heavy as the work — for a small change, a few lines and
  a few minutes. What the steps buy is that the agent never starts from nothing: the decision, the
  criteria and the state are already written, so the next step is short and right the first time.
  *In your project: how much does every session read before it starts, and has anyone measured
  it?*
- **What you decide gets built, and stays built.** A plan pulls the code toward it until the work
  matches. A decision about the architecture binds the code from then on: code that drifts from it
  is brought back, never the decision bent to fit the code, and it changes only when you decide
  again. *In your project: pick a decision your docs record — does the code still follow it?*
- **Done means checked.** Each change becomes a ticket with checkable criteria and a written plan,
  is built test-first, and is verified against the ticket, the plan and your tests before it
  counts as done. *In your project: pick a change marked done last month — what checked it, and
  would that check have failed if the change were wrong?*
- **You can see what it stands on.** Every step leaves a short record you can read, so checking the
  agent's work is cheap and trusting it isn't blind. *In your project: for the agent's last
  change, can you tell from the record why it chose what it did?*
- **A second opinion from outside.** Before a big decision, a separate agent that has not read the
  project is asked how things like it usually go wrong elsewhere, so the answer is not only the one
  the project already believes.

Plain Markdown and standard-library Python, MIT-licensed, in Claude Code, Codex and Cursor. Its
scripts refuse rather than guess, and leave nothing behind when they refuse.

The study asks these of your project and answers them in numbers from your own repository — run it
before you decide.

## How it meets your project

GoodWolf works with the method you have — your rules file, your gates, your decision records, your
commit convention and your pull requests stay yours, and what it brings sits beside them — or takes
its place, if you would rather: decided on the report. The step prefixes in this repository's own
history are its local rule and do not travel. Whether your project needs it is answered by the study, in
numbers from your own repository.

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

It is for **steering an agent on work that lasts**, in one session or several at once — a
product, a refactor, a course of study, a research line, a diary, new or long-lived — wherever
forgetting would cost you. It is not for a one-off script.

- **Several sessions at once.** Each sees where the others stand, and the scripts refuse a write
  over an entry that moved since it was read.
- **Everything it adds is files.** Reverting the install commit removes the harness; what it wrote
  under `docs/` afterwards stays until you delete it.

**Measure it in your project.** Over a few weeks, watch three things: whether an agent arriving
cold re-decides less, whether work stopped in one session is found at its step in the next, and
whether the questions you raise come back. In a project with a method of its own, the study's
report carries a measure to repeat later: what it cost a newcomer to recover where things stood,
before and after.

## It changes with your project

- **Your own skills get the same checks.** A guided command, `/mechanism`, walks you through adding
  one, and the scripts that check the shipped skills then check yours.

**An example from this repository's log.** One rule tells the agent to file each of your
messages under the open question it belongs to. On 5 October, new sessions kept filing messages
under questions that only sounded similar. Each time, the miss was logged and the rule tightened —
four times that day — until it said: file a message under the narrowest question that actually
covers it, never under one that merely looks alike. The sessions after that got it right. The
harness has been built with itself since September, in 66 sessions.

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

## Use it (instructions for your agent)

Asked whether the project needs it:

0. Answer the four questions under *It works, or it seems to work* for this project, and tell the
   person what came back.
1. Offer the study, which installs and runs nothing: read
   [`.agents/skills/harness/MEETING.md`](.agents/skills/harness/MEETING.md) here and follow it on the
   project. It writes nothing there; the report goes where the person says, and the person decides
   on it.

Asked to install it:

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
