# Session 39 — every written thing has a source of truth

**2026-10-07.** Claude Code, one conversation, resumed by its host under a second id
(`a3c9b354…`, then `2ccc7021…`). Entry contract v32 throughout. Eleven commits. A parallel
session landed `reword` in the same tree during the first hour; its files were left alone and it
committed them itself.

The session set out to grade `.0040`'s last box and take up `.0170`, the first install's last
step. It never reached `.0170`: reading it raised where the verification set lives, which raised
whether a project's environment is a mechanism, which raised what kinds of written thing a tree
holds at all. The last question is where the day's substance is.

## What was decided, and what chose it

### The environment is a mechanism — q-0018.0022

- **The necessity gate passes whole** *(the user)*. I had proposed passing it for the
  verification set alone, since every recorded failure was about the set and none about setting
  up tooling, running the app or a pipeline. The user: *there was no failure in setting up tools
  because we have not yet set up tools from scratch, nor adapted existing ones to the harness.*
  Absence of evidence from an unexercised path is not evidence against the need.
- **The environment owns the verification set** *(the user)*; `/verify`, `/implement` and
  `/maintain` consume it. I had named a conflict of interest — the one who sets up tooling
  proposes the measure. The user: *the set does not check the tooling.* Right: the set measures
  the work produced, never the tooling, so no conflict there. The conflict that does exist is the
  implementer weakening the set its work is measured by; that is a rule on changing the set, not
  a question of its owner, and it is still open.
- **The set's home is `local.rules.md`, injected into the skills that run it, and into no
  document** *(the user)*. Twice decided: first with an injected copy in `docs/cicd.md` for the
  person, then reversed the same hour — *if the agent can tell the user about the environment, a
  special file is not needed; and the user may try to change it, and the file is not
  authoritative.* Before that the user had set the frame: *the verification set is a key set of
  rules; a script cannot be its home*, against my proposal of an executable entry point. This
  reverses the 2026-09-23 decision that L3 is a pointer to `docs/cicd.md`.
- Still open under it: the set's shape (q-0018.0022.0001 "Where does a project's verification set
  live, and what shape does it take?" — home decided, shape not), the rule on changing it, and
  whether the environment keeps any description record at all, which the sort below answers:
  a description of what exists is kind 3 and is rendered, not kept.
- An outside pass was filed first,
  [discover-environment-seam-2026-10-07](../research/discover-environment-seam-2026-10-07.md):
  nine families, the strongest recent evidence being that coding agents game visible tests, and
  the pass's own finding that my tasking had bundled a policy (acceptance), two capabilities
  (setup, run) and an external system (CI) under one word.

### Every written thing has a source of truth — q-0024.0009

Raised by the user when "an agent can read the files a month later" was seen to argue against an
architecture doc as much as against `cicd.md`. In their words: *I see several reasons for docs to
exist — describe the aim, which drifts in itself because it keeps being refined; describe what
must always hold, which drifts from the docs to the derivatives; describe what already is, for
quick understanding, which drifts from the derivatives to the docs; describe what happened, which
drifts by definition. Sounds like different citizens on different substrates.*

- **Four kinds, named by what the record is of**: what it intends to become; what must always
  hold; what exists; what happened. *Purpose* was the first name of the first kind and the user
  struck it: *everything has a purpose, evolutionary docs included* — a property of every record,
  not a kind. *What it intends to become* replaced it. The test between the first two kinds, both
  written before the thing obeys them: the first expires when the thing reaches it, the second
  keeps governing. The tree already runs that handover — a decision lands in its durable home
  before its ticket closes; a spec's surviving agreements get homes before it is archived.
- **A kind of what** *(the user: persistence? mutability? drift?)*: **a kind of source of truth**,
  on two axes — which side is right when record and thing disagree (record, thing, neither), and
  whether the record's authority expires once reached. Persistence, mutability and drift were
  tried as the axis and are consequences; drift alone does not tell the first kind from the
  second.
- **The sort is of a mechanism's records, never its instruction** *(the user)*: a skill or a
  rule is the mechanism itself. For the mechanism shape, which produces instructions, a skill is
  a record of the second kind, and its invariants are `/skill-up`'s today.
- **No mechanism mixes kinds in one record, and each declares the kind of every output**
  *(the user)*. The ticket and the queue each mix three kinds today.
- **The whiteboard is the body of the question the task stands on; the ticket is a record of the
  first kind alone** *(the user)*. The user named the need first — *a place where we write
  everything bearing on a task until enough has gathered to see its form* — and offered the
  fork: the ticket is such a draft, unless drafting moves to the questions and the ticket becomes
  the project's form of one kind of interaction. The decisive fact: a ticket is minted only once
  its form is seen, so it cannot be where the form is found; and this very session drafted three
  aligns in question bodies with no ticket and lost nothing.
- **Core owns the ticket's contract; the file form is its default realization; a project's own
  board is admitted** *(the user)*. I had recommended the file form alone with a named seam,
  on the ground that no recipient had asked for a board. The user: *not the decisive fact — our
  simulation with different users named their own board as a recurring reason.* The adoption
  panel of 2026-09-26 is the second shape.
- **The queue is the first kind alone** *(the user)*: order, candidate, what follows what. Its
  table and counts are rendered, as 01-0011.0040 already decided; its completed-step narrative is
  a second home for what the session records hold and shrinks to a pointer; its ordering rule goes
  to a rules file when a mechanism owns it.
- **Every document is marked with its kind** *(the user)*; how the mark is written is the
  ticket's.
- **A kind is a relation, so every record declares its referent; the thing carries a mark back
  to the record that governs it** *(the user)*. The user asked whether each record must say both
  what it is a record of and what it is a thing for. The relation is authored once, at the record,
  and installed at the thing as a mark — the way a straw dog names its question in the text and an
  installed block names its owner. I first offered the reverse map rendered by a script; the user:
  *is that an optimization or the real direction the agent reads in?* It is the real direction:
  the agent that changes a thing reads the thing, so the pointer must be in it. Then: *what does a
  script have to do with it?* Nothing — a check may hold the two ends in agreement, as the
  installer's does, but it is not what serves the direction.
- **The mark back is needed only where the thing is agentic** *(the user)*: a thing a script
  derives — a rendered table, a binary, a file on a remote board — carries none, since no agent
  is ever at it with a change in hand.
- Shown on `.0171`'s chain: ticket and RFC of the first kind, spent; the architecture's
  *Installing* of the second, standing; the queue row and the marks of the third; the session
  record, the evidence and the archived question of the fourth. The one gap: `harness.py`'s
  install path names the architecture in prose and not its section, so an agent there does not
  meet the invariant. And `.0170`'s header carries `Related: .0171` — a live record of the first
  kind pointing at history, which belongs in a body or a session record.

## General principles derived, with no durable home yet

- Four kinds of record by source of truth, and the two axes that sort them. Home: the method
  glossary and the mechanism shape's format, once the ticket lands.
- The whiteboard is a state before the sort, not a kind; it lives in the question store.
- Authored once at the record, installed at the thing: the general form of which straw dogs,
  installed blocks and `TODO q-N` are three cases.
- An unexercised path yields no failures; its silence is not evidence against the need.
- A copy of a rule in a document invites editing where it is not authoritative, so a rule is
  delivered only to what executes it.

## What was done

- `.0040`'s last box graded by the user on the fresh sessions of 2026-10-05 and 2026-10-07; the
  paired close, the queue row deleted, the parent's status at `.0050` next. q-0001.0016 stays
  open on its child, the judge.
- q-0018.0021 opened and moved under the new q-0018.0022; q-0023.0015 and q-0018.0020.0003 now
  wait on q-0018.0022, which waits on q-0024.0009.
- `/conclude` amended at the user's request before this record: substance before form — each
  decision with what chose it, the principles derived, what was refuted — against the old text's
  *brief summary of work done, no need to repeat details stored elsewhere*, which had no slot for
  reasoning and read as a licence to drop it. Not a rule failure: no rule had been there to fail.

## What was refuted or went wrong, and what it taught

- Three of my recommendations were overturned by a single sentence each — the gate narrowed to
  the set, the script as the set's home, the file form alone for tickets — and each time the
  user's sentence named evidence I had not weighed. The pattern: I argued from the absence of
  recorded failures; the user argued from what has not been exercised and from the panel.
- The `cicd.md` injection was decided and reversed inside an hour. The reversal held a general
  principle (a non-authoritative copy invites the wrong edit) that the first decision had missed.
- Two forks were posed too many: by *3b* the user was lost, and the way back was one concrete
  example — a fresh Python project and its three files.
- The host resumed the conversation under a second id again; the earlier row is ended with this
  one. q-0001.0006 is struck once more.

## What continues

- **Next step: `/impact` on the sort**, then `/ticket`. The shape is an amendment of the
  mechanism shape — kind and referent on each declared output, `/maintain`'s *docs to their
  implementation, both ways* split into two repair directions, four glossary terms, the ticket
  and queue formats thinned, the mark on every document — with one decision still open: how the
  mark is written. HITL, `breakdown=ask`.
- **The environment align** resumes after it: the set's shape, the rule on changing the set, and
  `setup-devops` as the mechanism's instruction file. Then `.0170` is re-read against both.
- **Two small repairs the chain showed**, for a maintenance pass: `harness.py`'s install docstring
  to name `architecture.md#installing`; `.0170`'s `Related` line to `.0171` moved out of the
  header.
- Seven maintenance levels are due by the clock and were not re-checked here.
- Thirteen session rows from 2026-10-05 still read running; this conversation's two are ended.
