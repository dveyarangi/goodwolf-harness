# What the harness is for

**Kind:** what must always hold — the pains, the goals and the causes. The status column is as of
2026-10-09, and each mechanism not in place names the open question that waits on it.

The leading product document. The project's goals and its front page are derived from it, and a
piece of work earns its place by the pain it relieves. It was found, not designed: at the
front-page align of 2026-10-08 every attempt to say what the harness *is* came out as its
implementation, until the user named the pains. The argument is in
[q-0033](questions/q-0033-which-pains-of-developing-software-with-coding-agents-does-the-harness-exist-to-relieve-and-what-answers-each.md)
"Which pains of developing software with coding agents does the harness exist to relieve, and
what answers each?".

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

Neither may be lost as a goal, though nothing guarantees either today.

- **G1 Better over time, not worse.** Decisions do not erode, contradictions do not accumulate,
  and a lesson learned in one session holds in the next.
- **G2 No harm.** The agent does not destroy work, leak secrets, or act beyond what it was
  allowed.

## Causes

- **C1** Instructions don't reach the agent, or are wrong: scattered, contradictory, unchecked.
- **C2** The model decides where models are known to be weak.
- **C3** The person's space of ideas and the exploration space diverge. A task set wrong is one
  case.
- **C4** The exploration space is lost, between sessions, at a compaction, or when the host resumes
  a conversation under a new identity.
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

Each answer serves several pains. Each row is a mechanism.

- ✓ the mechanism is in the tree
- ◐ it is partly there
- ✗ it is absent

A row not marked ✓ is bound, in this page's source, to the open question that waits on it.

| answer and mechanism | causes | 1 | 2 | 3 | G1 | G2 | status |
|---|---|---|---|---|---|---|---|
| **The shared exploration space** — memory keeps it; alignment keeps it matching the person's ideas | | | | | | | |
| the question store: open questions as a tree, each with its lean and what it waits on; every message placed on its question before the reply; questions returned to rise | C3, C4 | ● | ● | ● | | | ✓ |
| the store's neighbourhood handed over at session start and before every message | C4 | ● | ● | ● | | | ✓ by hooks an install merges into each host's file; Cursor's hooks can add context at session start only, so there the agent fetches it before a message by rule |
| a position kept through a compaction and a resume under a new identity | C4 | ● | ● | | | | <straw-dog question="q-0001.0006">◐ in one host</straw-dog> |
| a session resumes the work at the step it stopped | C4 | ● | ● | | | | <straw-dog question="q-0027">◐ the wake finds where the work stands; resuming at the step is not built</straw-dog> |
| provisional text bound to the question it waits on; answers under a changed answer marked suspect | C3, C6 | | | ● | ● | | ✓ |
| a question split into the parts it needs before anyone answers it | C2, C3 | ● | ● | | | | <straw-dog question="q-0001.0020">✗</straw-dog> |
| a judge outside the agent for where a message belongs | C3 | ● | | ● | | | <straw-dog question="q-0001.0016.0001">✗</straw-dog> |
| a question nobody reaches kept from sinking | C4 | | | ● | | | <straw-dog question="q-0001.0018">✗</straw-dog> |
| **Alignment of intent** | | | | | | | |
| `/align`: one question at a time, each with a recommended answer; facts looked up, decisions put to the person; opens on the present customer, the observable problem, and why what exists cannot serve | C3, C9, C11 | ● | ● | ● | | | ✓ |
| one vocabulary for the person and the agent, defined before a term lands in a record | C3 | ● | | ● | | | <straw-dog question="q-0024.0001">◐ the glossaries exist; keeping a term out until defined is not built</straw-dog> |
| a task takes its form in its question before a ticket is minted from it | C3 | ● | ● | | | | <straw-dog question="q-0024.0009.0003.0002">◐ decided, not landed</straw-dog> |
| **Decisions placed by their weight** | | | | | | | |
| the load-bearing test: `/impact` routes load-bearing work to the person and a spec, local work to the agent and a ticket; a raised decision that bears no load is settled and reported, one that does goes to the person, and doubt counts as load | C2, C8, C9 | ● | ● | ● | | | ✓ |
| HITL or AFK on every ticket; a spec accepted, a breakdown approved; commit, push and the next cycle each `ask` or `auto`; repair fixed and reported only under four conditions | C2, C9, C12 | ● | ● | ● | | ● | ✓ |
| the project says which kinds of decision stop for the person | C9 | | ● | ● | | | <straw-dog question="q-0027.0002">✗</straw-dog> |
| a record of where models are known to be weak, deciding which decisions go to the person | C2, C9 | ● | | ● | | | <straw-dog question="q-0033.0001">✗</straw-dog> |
| **Visible footing** | | | | | | | |
| each reply shows the question it stands on, the principle it reasons by, what waits on the person and drift met, in plain words; every step leaves a record | C10, C2 | ● | | ● | | | <straw-dog question="q-0030">◐ being graded</straw-dog> |
| **Guards on known model weaknesses** | | | | | | | |
| an outside view before saying what a thing is (`/discover`); a plan probed by the cheapest example that could prove it wrong; one case is not a class; the fewest parts, removing before adding; no reopening a settled decision without new evidence | C2, C11 | ● | ● | ● | | | ✓ |
| guards on the checks themselves: a check written before what it checks and seen to fail; a run with no tests is not a pass; a fixture built the way the real thing came to be | C7 | ● | | | ● | | ✓ |
| **Delivery and evaluation** | | | | | | | |
| a ticket with checkable criteria; thin vertical slices; a plan validated against the governing docs; test-first; `/verify` against the ticket, the plan, the docs and the project's checks; checks run before a commit | C3, C7 | ● | ● | | | | ✓ |
| the project's checks, and a rule on who may change them | C7 | ● | | | | | <straw-dog question="q-0018.0022.0001">◐ weakening a check is forbidden; where the checks live and their shape is not settled</straw-dog> |
| a failure traced to its cause, so that what let it through is corrected | C7 | ● | | | ● | | <straw-dog question="q-0033.0003">◐ to an instruction, in the register; to a decision boundary or a task's form, not yet</straw-dog> |
| every mechanism names what would show it working, graded by someone who did not build it | C7 | | | | ● | | ✓ |
| the harness's own tests catch what their names promise | C7 | | | | ● | | <straw-dog question="q-0021">✗</straw-dog> |
| **Instructions that reach the agent** | | | | | | | |
| one home per rule, copied by a script into every place that reads it, at the tier its occasion is read at, and checked | C1 | ● | ● | | ● | | <straw-dog question="q-0025.0002">◐ which mechanism owns tiering is open</straw-dog> |
| rules written to a form an agent follows: an occasion and a checkable outcome, no overlap, no contradiction | C1 | ● | | | ● | | <straw-dog question="q-0028">◐ `/skill-up` holds the form; a rule without it is not refused</straw-dog> |
| each skill states only what it owns, and everything a mechanism produces has a reader | C1 | ● | ● | | | | <straw-dog question="q-0023">◐ six of twenty-four skills are declared mechanisms</straw-dog> |
| whether a rule reaches its occasion observed, not asserted | C1 | ● | | | | | <straw-dog question="q-0025">◐ the session announces the rules it runs, self-reported</straw-dog> |
| a document informs and never instructs, so text in one is not taken as a command | C1, C12 | ● | | | | ● | <straw-dog question="q-0029">◐ a rule, not yet settled</straw-dog> |
| **One source of truth between decisions and code** | | | | | | | |
| decisions in the architecture, its records and the glossary; who decided each rule, and when | C1, C6 | ● | | ● | ● | | ✓ |
| every record says which side wins when it and the code disagree | C6 | ● | | | ● | | <straw-dog question="q-0024.0009">◐ named; records being brought to it</straw-dog> |
| what bears load is written down, the rest lives in code and its comments | C6, C8 | ● | ● | | ● | | <straw-dog question="q-0024.0002.0005">◐ a rule, not yet settled</straw-dog> |
| an edited thing carries its mark back to the record that governs it | C6 | ● | | | ● | | <straw-dog question="q-0024.0009.0004">✗</straw-dog> |
| the queue derived from its tickets, its order the person's | C6, C9 | | ● | ● | | | <straw-dog question="q-0020">◐ the order is the person's; the table is still kept by hand</straw-dog> |
| a contract per edge, for those who consume the system and those who extend it, its outward text derived from it | C6, C10 | ● | | | ● | | <straw-dog question="q-0018.0023.0002">◐ the edge mechanism and the hosts record exist; no text is derived from a record yet</straw-dog> |
| **Maintenance** | | | | | | | |
| `/maintain`: records against each other and against the code, a clock of what is due, finished records archived | C6, C8 | ● | ● | | ● | | <straw-dog question="q-0024.0005">◐ links are checked only when records move; what is due is not announced</straw-dog> |
| **Self-improvement — the seed of a test suite for instructions** | | | | | | | |
| a register of rules that were in place and did not fire; the next occurrence grades the rewording | C7, C1 | ● | | | ● | | ✓ |
| a recorded failure replayed as a test against the amended rule | C7, C1 | ● | | | ● | | <straw-dog question="q-0026.0004">◐ replayed by hand at times; no suite</straw-dog> |
| the method measured on the same tasks with and without it | C7 | ● | | | ● | | <straw-dog question="q-0017">✗</straw-dog> |
| its cost counted, and what it saves | C7, C8 | | ● | | ● | | <straw-dog question="q-0018.0008">✗</straw-dog> |
| a free reading of the record for what is missing, redundant or out of balance (`/dream`, `/advise`) | C7 | | | | ● | | <straw-dog question="q-0018.0002">◐ in use, not declared</straw-dog> |
| **Coordination between sessions** | | | | | | | |
| each session sees where the others stand; the question store refuses a write to an entry that moved; a commit holds only its own session's work | C5, C12 | ● | ● | | | ● | <straw-dog question="q-0018.0015">◐ within one working directory</straw-dog> |
| no session overwrites another's write | C5, C12 | ● | ● | | | ● | <straw-dog question="q-0032">✗</straw-dog> |
| a starting session takes an area no other session is in | C5 | | ● | | | | <straw-dog question="q-0016.0001">✗</straw-dog> |
| **Process weighed to the work** | | | | | | | |
| one step per reply, with a point to reassess at its end | C8, C9 | | ● | ● | | | <straw-dog question="q-0027">◐ defined, not instructed</straw-dog> |
| the work's shape recommended, and a lighter path for small work and a heavier one for large | C8 | | ● | ● | | | <straw-dog question="q-0027.0003">✗</straw-dog> |
| **Refusing harm** | | | | | | | |
| writes that refuse rather than overwrite: a refusal writes nothing, interference is a failure, a removal needs the fingerprint it expects, push waits for a yes | C12 | | | | | ● | <straw-dog question="q-0032">◐ the harness's own scripts refuse; an agent's own edits are guarded by nothing</straw-dog> |
| an agent's role bounding its permissions, its rights over the records and its skills | C12, C5 | | | | | ● | <straw-dog question="q-0016">✗</straw-dog> |
| the host refuses an action a rule forbids | C12 | | | | | ● | <straw-dog question="q-0018.0005">✗</straw-dog> |

<straw-dog question="q-0033">
Read by column:

- **1 Ineffective** has the most answers, and most of them are in place.
- **2 Suboptimal** waits on the two absent rows that weigh most: no session overwriting
  another's write, and a lighter path for small work.
- **3 Agency** rests on the load-bearing test, HITL and the switches, visible footing and the
  exploration space. Its absent rows are the ones that would let the person move the point on the
  scale: which kinds of decision stop for them, and a record of where models are weak.
- **G1** rests on one source of truth, maintenance and self-improvement, and nothing measures
  whether it holds.
- **G2** has guarded writes and the switches, and none of the three things that would bound the
  agent: roles, the host refusing, locks.
</straw-dog>

## Correction and evaluation, together

These two cut across every pain, and neither works without the other.

- **Evaluation without correction** produces a report nobody acts on.
- **Correction without evaluation** rewords rules blind.

Work is evaluated against its own criteria and the project's checks. A failure is traced to its
cause above, and corrects both the work and whatever let it through: an instruction, a decision
boundary, a task's form.

## Who it is for

<straw-dog question="q-0033.0004">Every pain above is framed for one person steering agents on one project. Several people sharing one project — their queue, their decisions, their branches — are not served yet.</straw-dog>

## A pain of the harness itself

**The method doesn't fit the project, and the project's changes are lost on update.** This is a
pain of adopting a tool, not of developing with agents. The harness answers it with:

- the project's own rules file, applied last and kept through updates;
- an update that stops rather than overwrite a hand edit, and a refusal that writes nothing;
- a check that the installed copy matches the release it came from;
- a check that core never depends on a project's own documents.

Its open parts:

- <straw-dog question="q-0018.0020.0001">An install meets an existing `CLAUDE.md` or `AGENTS.md` by moving it aside, in one mode only.</straw-dog>
- <straw-dog question="q-0018.0011">An install does not draft an architecture and glossary from the project's code.</straw-dog>
- <straw-dog question="q-0018.0011.0004">An install does not find what the project exists to solve, or the answers it has already built into its docs and code.</straw-dog>
- <straw-dog question="q-0018.0020.0003">A first install does not end with the project's own checks in place.</straw-dog>
- <straw-dog question="q-0018.0019">A project's own mechanisms have no declared home, so they are not checked like the shipped ones.</straw-dog>
- <straw-dog question="q-0018.0020.0002">An update does not say what changed or what the project has to do about it.</straw-dog>
- <straw-dog question="q-0018.0014">A harness failure found in a project does not reach the harness.</straw-dog>
- <straw-dog question="q-0018.0018">An improvement a project makes to the harness does not reach it either.</straw-dog>
- <straw-dog question="q-0018.0012">What maintenance re-checks for the harness inside a project is not settled.</straw-dog>
- <straw-dog question="q-0018.0020.0001.0002">A shipped skill's name can collide with a project's own command.</straw-dog>
- <straw-dog question="q-0024.0002">A project cannot change how it builds in one edit.</straw-dog>
- <straw-dog question="q-0018.0013">There is no uninstall.</straw-dog>
- <straw-dog question="q-0018.0023">Three hosts are supported.</straw-dog>

Its home is q-0018 "How do projects share one development method without losing their own
conventions?".
