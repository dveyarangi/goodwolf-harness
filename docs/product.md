# What the harness is for

**Kind:** what must always hold — the pains, the goals, the causes and the answers, in the product
format. How much of each answer is built is read from the questions that realize it, never
written here.

**What it is for.** A harness that keeps an agent's work coherent on any task that needs a memory
of its own and holds a moving target — research, learning, a diary, development. It gives that
work the memory of the exploration space, the person's place in it, and instructions that reach
the occasion they are for and can be carried out there. And it lets your own method be built on
it: a memory of its own, its instructions reaching their occasions, and its amendment by the same
means as the harness amends itself. It is modular: a core of memory and self-improvement, and the
method for the work at hand installed on it. Software development is the first such method, and
the one the product is tested by *(the user, 2026-10-25)*: this tree develops the harness with the
harness, and every project that takes it is a trial.

The leading product document. The project's goals and its front page are derived from it, and a
piece of work earns its place by the pain it relieves. It was found, not designed: at the
front-page align of 2026-10-08 every attempt to say what the harness *is* came out as its
implementation, until the user named the pains. The argument is in
[q-0033](questions/q-0033-what-is-this-project-for.md) "What is this project for?".

**What it does, in one line.** Fewer steps, each more precise: at every step the agent knows what
is needed now — which rule, which record, which question — and does that, not the rest. The
project's own practices stay its own, by its choice; the harness fits into them and replaces none.
Its memory stays true: one home for every fact, every record knowing which side wins against the
code, what rests on what linked, the open questions kept with the thinking on them, the whole
reaching the agent before every message.

## Pains

1. **The agent is ineffective.** It does not reach the intended result: work called done that does
   not work, or is not what was meant.
2. **The agent is suboptimal.** It reaches the result at too high a cost: tokens, time, rework, and
   the person's attention.
3. **The person's agency is off its point.** Agency is a scale, and it fails at both ends.
   - **Too little: loss of control.** Decisions that matter are taken without the person, and the
     shared picture drifts from theirs. They narrow their own thinking to what the agent can hold,
     because whatever is not the task in hand evaporates. The project stops being theirs to steer.
   - **Too much: micromanagement.** The person re-explains, re-checks, approves each step, and
     babysits work the agent could carry.

   The right point puts the person at the decisions that bear load and where models are known to
   be weak, and nowhere else. There the person can think freely, jumping from topic to topic,
   and lose nothing.

## Goals with no guarantee yet

None may be lost as a goal, though nothing guarantees any of them today.

- **G1 Better over time, not worse.** Decisions do not erode, contradictions do not accumulate,
  and a lesson learned in one session holds in the next.
- **G2 No harm.** The agent does not destroy work, leak secrets, or act beyond what it was
  allowed.
- **G3 The agent is the interface.** A person steers the project, its settings included, through
  the agent and never needs to open a file; a hand edit is allowed, rare, and treated as drift
  *(the user, 2026-10-23)*.

## Causes

- **C1** Instructions don't reach the agent, or are wrong: scattered, contradictory, unchecked.
- **C2** The model decides where models are known to be weak.
- **C3** The person's space of ideas and the exploration space diverge. A task set wrong is one
  case.
- **C4** The exploration space is lost, between sessions, at a compaction, or when the host resumes
  a conversation under a new identity — or it is written and costs a search to reach, a price paid
  by every newcomer and every session.
- **C5** Agents are out of sync with each other.
- **C6** What was decided and what was built drift apart.
- **C7** Failures go undetected or unattributed, so nothing is learned.
- **C8** The process weighs the same for small and large work, and the method's own instructions
  cost context in every session.
- **C9** Where the person is placed is left to the agent's mood rather than to the weight of the
  decision.
- **C10** What the agent's work stands on is invisible. The person can neither check it cheaply
  nor trust it.
- **C11** The agent over-builds: it adds what no demonstrated problem asks for.
- **C12** The agent can act beyond what it was allowed. Nothing bounds its permissions, it may
  take a document's text for an instruction, and its writes may overwrite another's.

## Answers

Each answer serves several pains. Its coverage — absent, in progress, present — is
`product.py --coverage`'s, read from the questions whose trace links name it. An answer not chosen
yet waits on its purpose question, bound to it in *waits on*.

| answer | causes | 1 | 2 | 3 | G1 | G2 | waits on |
|---|---|---|---|---|---|---|---|
| **The shared exploration space** — memory keeps it; alignment keeps it matching the person's ideas | | | | | | | |
| **A1 The question store** — the question store: open questions as a tree, each with its lean and what it waits on; every message placed on its question before the reply; questions returned to rise | C3, C4 | ● | ● | ● |  |  |  |
| **A2 The store handed over every message** — the store's neighbourhood handed over at session start and before every message; by hooks an install merges into each host's file; Cursor's hooks can add context at session start only, so there the agent fetches it before a message by rule | C4 | ● | ● | ● |  |  |  |
| **A3 A position kept through compaction and resume** — a position kept through a compaction and a resume under a new identity | C4 | ● | ● |  |  |  |  |
| **A4 A session resumes at its step** — a session resumes the work at the step it stopped | C4 | ● | ● |  |  |  |  |
| **A5 Provisional text bound to its question** — provisional text bound to the question it waits on; answers under a changed answer marked suspect | C3, C6 |  |  | ● | ● |  |  |
| **A6 A question split before it is answered** — a question split into the parts it needs before anyone answers it | C2, C3 | ● | ● |  |  |  |  |
| **A7 An outside judge of where a message belongs** — a judge outside the agent for where a message belongs | C3 | ● |  | ● |  |  |  |
| **A8 No question left to sink** — a question nobody reaches kept from sinking | C4 |  |  | ● |  |  |  |
| **Alignment of intent** | | | | | | | |
| **A9 Alignment one question at a time** — `/align`: one question at a time, each with a recommended answer; facts looked up, decisions put to the person; opens on the present customer, the observable problem, and why what exists cannot serve | C3, C9, C11 | ● | ● | ● |  |  |  |
| **A10 A shared glossary, terms defined before use** — one vocabulary for the person and the agent, defined before a term lands in a record | C3 | ● |  | ● |  |  |  |
| **A11 A task takes its form before its ticket** — a task takes its form in its question before a ticket is minted from it; a decision lands as it is made, provisional ones bound to the question that will change them | C3 | ● | ● |  |  |  |  |
| **Decisions placed by their weight** | | | | | | | |
| **A12 The load-bearing test** — the load-bearing test: `/impact` routes load-bearing work to the person and an align on its question, local work to the agent and a ticket; a raised decision that bears no load is settled and reported, one that does goes to the person, and doubt counts as load | C2, C8, C9 | ● | ● | ● |  |  |  |
| **A13 Human checkpoints and the dial** — HITL or AFK on every ticket; a question's `Where it stands` accepted; a dial on each method's ladder — below it the agent acts, at it shows first, above it the person decides — and a question's highest rung saying where it stops | C2, C9, C12 | ● | ● | ● |  | ● |  |
| **A14 The project names its stopping decisions** — the project says which kinds of decision stop for the person, by the dial it sets on each ladder | C9 |  | ● | ● |  |  |  |
| **A15 A record of model weaknesses** — a record of where models are known to be weak, deciding which decisions go to the person | C2, C9 | ● |  | ● |  |  | <straw-dog question="q-0033.0001">✗</straw-dog> |
| **Visible footing** | | | | | | | |
| **A16 Each reply shows its footing** — each reply shows the question it stands on, the principle it reasons by, what waits on the person and drift met, in plain words; every step leaves a record | C10, C2 | ● |  | ● |  |  |  |
| **Guards on known model weaknesses** | | | | | | | |
| **A17 Guards on model reasoning** — an outside view before saying what a thing is (`/discover`); a plan probed by the cheapest example that could prove it wrong; one case is not a class; the fewest parts, removing before adding; no reopening a settled decision without new evidence | C2, C11 | ● | ● | ● |  |  |  |
| **A18 Guards on the checks** — guards on the checks themselves: a check written before what it checks and seen to fail; a run with no tests is not a pass; a fixture built the way the real thing came to be | C7 | ● |  |  | ● |  |  |
| **Delivery and evaluation** | | | | | | | |
| **A19 Delivery against criteria** — a ticket with checkable criteria; thin vertical slices; a plan validated against the governing docs; test-first; `/verify` against the ticket, the plan, the docs and the project's checks; checks run before a commit | C3, C7 | ● | ● |  |  |  |  |
| **A20 The project's checks, guarded** — the project's checks, and a rule on who may change them | C7 | ● |  |  |  |  |  |
| **A21 A failure traced to its cause** — a failure traced to its cause, so that what let it through is corrected | C7 | ● |  |  | ● |  | <straw-dog question="q-0033.0003">✗</straw-dog> |
| **A22 Every mechanism graded from outside** — every mechanism names what would show it working, graded by someone who did not build it | C7 |  |  |  | ● |  |  |
| **A23 Tests that catch what they promise** — the harness's own tests catch what their names promise | C7 |  |  |  | ● |  |  |
| **Instructions that reach the agent** | | | | | | | |
| **A24 Each rule written once, installed where it is read** — one home per rule, copied by the rules installer into every place that reads it, at the tier its occasion is read at, and checked | C1 | ● | ● |  | ● |  |  |
| **A25 Rules in a followable form** — rules written to a form an agent follows: an occasion and a checkable outcome, no overlap, no contradiction | C1 | ● |  |  | ● |  |  |
| **A26 Each skill owns only its own** — each skill states only what it owns, and everything a mechanism produces has a reader — usually an agent, not the person, except the top summaries | C1 | ● | ● |  |  |  |  |
| **A27 Rules observed reaching their occasion** — whether a rule reaches its occasion observed, not asserted | C1 | ● |  |  |  |  |  |
| **A28 A document informs, never instructs** — a document informs and never instructs, so text in one is not taken as a command | C1, C12 | ● |  |  |  | ● |  |
| **One source of truth between decisions and code** | | | | | | | |
| **A29 Decisions in the records** — decisions in the architecture, its records and the glossary; who decided each rule, and when | C1, C6 | ● |  | ● | ● |  |  |
| **A30 Every record says which side wins** — every record says which side wins when it and the code disagree | C6 | ● |  |  | ● |  |  |
| **A31 Load-bearing written, the rest in code** — what bears load is written down, the rest lives in code and its comments | C6, C8 | ● | ● |  | ● |  |  |
| **A32 An edited thing carries its mark back** — an edited thing carries its mark back to the record that governs it | C6 | ● |  |  | ● |  |  |
| **A33 The path read from the records** — what comes next read from the records: the work in hand, the ready work and what each serves, the roots' balance; its order the product roadmap's, no written queue | C6, C9 |  | ● | ● |  |  |  |
| **A34 A contract per edge** — a contract per edge, for those who consume the system and those who extend it, its outward text derived from it | C6, C10 | ● |  |  | ● |  |  |
| **Maintenance** | | | | | | | |
| **A35 Maintenance** — `/maintain`: records against each other and against the code, a clock of what is due, finished records archived | C6, C8 | ● | ● |  | ● |  |  |
| **Self-improvement — the seed of a test suite for instructions** | | | | | | | |
| **A36 The rule-failure register** — a register of rules that were in place and did not fire; the next occurrence grades the rewording | C7, C1 | ● |  |  | ● |  |  |
| **A37 Failures replayed as tests** — a recorded failure replayed as a test against the amended rule | C7, C1 | ● |  |  | ● |  |  |
| **A38 The method measured against none** — the method measured on the same tasks with and without it | C7 | ● |  |  | ● |  |  |
| **A39 Its cost counted** — its cost counted, and what it saves | C7, C8 |  | ● |  | ● |  |  |
| **A40 A free reading of the record** — a free reading of the record for what is missing, redundant or out of balance (`/dream`, `/advise`) | C7 |  |  |  | ● |  |  |
| **Coordination between sessions** | | | | | | | |
| **A41 Sessions collaborate** — each session sees where the others stand; the question store refuses a write to an entry that moved; a commit holds only its own session's work | C5, C12 | ● | ● |  |  | ● |  |
| **A42 No session overwrites another** — no session overwrites another's write; the host's: its edit tool refuses a write over a file changed since it was read, and a worktree per session where it offers one; the harness locks nothing (the user, 2026-10-11) | C5, C12 | ● | ● |  |  | ● |  |
| **A43 A starting session takes a free area** — a starting session takes an area no other session is in | C5 |  | ● |  |  |  |  |
| **A51 Several people develop one project together** — their queue, their decisions, their branches | C5 |  |  | ● |  |  | <straw-dog question="q-0033.0004">✗</straw-dog> |
| **Process weighed to the work** | | | | | | | |
| **A44 One step per reply** — one step per reply, with a point to reassess at its end | C8, C9 |  | ● | ● |  |  |  |
| **A45 Work weighed to its shape** — the work's shape recommended, and a lighter path for small work and a heavier one for large | C8 |  | ● | ● |  |  |  |
| **Refusing harm** | | | | | | | |
| **A46 Writes that refuse** — writes that refuse rather than overwrite: a refusal writes nothing, interference is a failure, a removal needs the fingerprint it expects, push waits for a yes; the harness's own scripts refuse; an agent's own edits are guarded by the host — its stale-write refusal, its worktrees — not by the harness | C12 |  |  |  |  | ● |  |
| **A47 Agent roles** — an agent's role bounding its permissions, its rights over the records and its skills | C12, C5 |  |  |  |  | ● |  |
| **A48 The host refuses forbidden actions** — the host refuses an action a rule forbids | C12 |  |  |  |  | ● |  |
| **The project's own account** | | | | | | | |
| **A50 The product document kept in step with the work** — this document's answers numbered, the questions that build each linked to it, its coverage read from them, and drift between them found | C6, C10 | ● |  | ● | ● |  |  |
| **A52 The front page tells a newcomer what the harness is for** — the account above, told to a reader who arrives cold | C10 |  |  | ● |  |  | <straw-dog question="q-0033.0008">✗</straw-dog> |
| **Adopting the harness** | | | | | | | |
| **A49 Installs and updates without losing the project's own rules** — the answer to the pain below: the project's own rules file applied last and kept, an update that stops rather than overwrite a hand edit, a check of the installed copy | | | | | | ● | |

<straw-dog question="q-0033">
Read by column:

- **1 Ineffective** has the most answers, and most of them are in place.
- **2 Suboptimal** waits on the two absent rows that weigh most: no session overwriting
  another's write, and a lighter path for small work.
- **3 Agency** rests on the load-bearing test, HITL and the dial, visible footing and the exploration
  space. The dial lets the person move the point on the scale; its absent row is a record of where
  models are weak.
- **G1** rests on one source of truth, maintenance and self-improvement, and nothing measures
  whether it holds.
- **G2** has guarded writes and the dial, and neither of the two things that would bound the
  agent: roles, the host refusing. Locks are the host's, not the harness's.
</straw-dog>

## Correction and evaluation, together

These two cut across every pain, and neither works without the other.

- **Evaluation without correction** produces a report nobody acts on.
- **Correction without evaluation** rewords rules blind.

Work is evaluated against its own criteria and the project's checks. A failure is traced to its
cause above, and corrects both the work and whatever let it through: an instruction, a decision
boundary, a task's form.

A disagreement between records, or between a record and the code, is repaired where a session
meets it, and every session meets its own. No pass reads the whole tree; the method is the repair
by encounter, not the audit.

## Who it is for

Every pain above is framed for a person steering agents on one project, in one session or several
at once: sessions in one tree see each other's position, and the host keeps their writes apart.
<straw-dog question="q-0033.0004">Several people sharing one project — their queue, their decisions, their branches — are not served yet.</straw-dog>

## A pain of the harness itself

**The method doesn't fit the project, and the project's changes are lost on update.** This is a
pain of adopting a tool, not of developing with agents. The stance behind every answer: the harness
integrates. A project's practices — its gates, its decision records, its scripts, its coordinators —
stay as they are, kept by the project's choice; the harness is added beside them, and what it asks
is counted against what the project's method already asks, so the gain shows as fewer and more
precise steps, never as a practice removed. The harness answers it with:

- the project's own rules file, applied last and kept through updates;
- an update that stops rather than overwrite a hand edit, and a refusal that writes nothing;
- a check that the installed copy matches the release it came from;
- a check that core never depends on a project's own documents;
- a first install that ends with the project's verification set written from what exists, an
  empty one stated.

Its open parts:

- <straw-dog question="q-0037.0006.0020.0001">An install meets an existing `CLAUDE.md` or `AGENTS.md` by moving it aside, in one mode only.</straw-dog>
- <straw-dog question="q-0037.0006.0011">An install does not draft an architecture and glossary from the project's code.</straw-dog>
- <straw-dog question="q-0037.0006.0011.0004">An install does not find what the project exists to solve, or the answers it has already built into its docs and code.</straw-dog>
- <straw-dog question="q-0037.0006.0019">A project's own mechanisms have no declared home, so they are not checked like the shipped ones.</straw-dog>
- <straw-dog question="q-0037.0006.0020.0002">An update does not say what changed or what the project has to do about it.</straw-dog>
- <straw-dog question="q-0037.0006.0014">A harness failure found in a project does not reach the harness.</straw-dog>
- <straw-dog question="q-0037.0006.0018">An improvement a project makes to the harness does not reach it either.</straw-dog>
- <straw-dog question="q-0037.0006.0012">What maintenance re-checks for the harness inside a project is not settled.</straw-dog>
- <straw-dog question="q-0037.0006.0020.0001.0002">A shipped skill's name can collide with a project's own command.</straw-dog>
- <straw-dog question="q-0037.0010.0002">A project cannot change how it builds in one edit.</straw-dog>
- <straw-dog question="q-0037.0006.0013">There is no uninstall.</straw-dog>
- <straw-dog question="q-0037.0006.0023">Three hosts are supported.</straw-dog>

Its home is q-0037.0006 "How do projects share one development method without losing their own
conventions?".
