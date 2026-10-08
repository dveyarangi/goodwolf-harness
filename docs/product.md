# What the harness is for

**Kind:** what must always hold — the pains, the goals and the causes. The status column is as of
2026-10-09, and each absent mechanism names the open question that waits on it.

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
   - **Too little: loss of control.** Decisions that matter are taken without the person, the
     shared picture drifts from theirs, and the project stops being theirs to steer.
   - **Too much: micromanagement.** The person re-explains, re-checks, approves each step, and
     babysits work the agent could carry.

   The right point puts the person at the decisions that bear load and where models are known to
   be weak, and nowhere else.

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
- **C4** The exploration space is lost between sessions.
- **C5** Agents are out of sync with each other.
- **C6** What was decided and what was built drift apart.
- **C7** Failures go undetected or unattributed, so nothing is learned.
- **C8** The process weighs the same for small and large work.
- **C9** Where the person is placed is left to the agent's mood rather than to the weight of the
  decision.
- **C10** What the agent's work stands on is invisible. The person can neither check it cheaply
  nor trust it.

## Answers

Each answer serves several pains. Each row is a mechanism.

- ✓ the mechanism is in the tree
- ◐ it is partly there
- ✗ it is absent

A row not marked ✓ names the open question it waits on.

| answer and mechanism | causes | 1 | 2 | 3 | G1 | G2 | status |
|---|---|---|---|---|---|---|---|
| **The shared exploration space** — memory keeps it, alignment keeps it matching the person's ideas | | | | | | | |
| open questions kept as a tree, each with its lean and what it waits on | C3, C4 | ● | ● | ● | | | ✓ |
| every message placed on its question before the reply | C3 | ● | ● | ● | | | ✓ |
| the neighbourhood of the current question handed over before every message | C4 | ● | ● | ● | | | <straw-dog question="q-0018.0020.0005">◐ by hooks in this repository; in an installed project the agent fetches it by rule</straw-dog> |
| questions returned to rise; a start-of-session report of where things stand | C4 | | ● | ● | | | ✓ |
| `/recall` at every wake, `/conclude` at every end, session records | C4 | ● | ● | | | | ✓ |
| provisional text bound to the question it waits on | C3, C6 | | | ● | ● | | ✓ |
| a judge outside the agent for where a message belongs | C3 | ● | | ● | | | <straw-dog question="q-0001.0016.0001">✗</straw-dog> |
| a question nobody reaches kept from sinking | C4 | | | ● | | | <straw-dog question="q-0001.0018">✗</straw-dog> |
| **Alignment of intent** | | | | | | | |
| `/align`, which stress-tests a plan against what is settled | C3 | ● | ● | ● | | | ✓ |
| one vocabulary for the person and the agent, in the glossaries | C3 | ● | | ● | | | ✓ |
| a task takes its form in its question before a ticket is minted | C3 | ● | ● | | | | <straw-dog question="q-0024.0009">◐ decided, not landed</straw-dog> |
| `/spec` for large work, accepted by the person | C3 | ● | | ● | | | ✓ |
| **Decisions placed by their weight** | | | | | | | |
| the load-bearing test: `/impact` routes load-bearing work to the person and a spec, local work to the agent and a ticket | C2, C8, C9 | ● | ● | ● | | | ✓ |
| HITL or AFK on every ticket; every decision at `/align`; spec accepted, breakdown approved | C2, C9 | ● | | ● | | | ✓ |
| switches — commit, push, next cycle, breakdown — and the repair policy | C9 | | ● | ● | | | ✓ |
| a record of where models are known to be weak, deciding which decisions go to the person | C2, C9 | ● | | ● | | | <straw-dog question="q-0033.0001">✗</straw-dog> |
| the person choosing which kinds of decision are theirs | C9 | | ● | ● | | | <straw-dog question="q-0033.0002">✗</straw-dog> |
| **Visible footing** | | | | | | | |
| each reply shows the question it stands on, the principle it reasons by, what waits on the person, and drift met | C10, C2 | ● | | ● | | | <straw-dog question="q-0030">◐ being graded</straw-dog> |
| a record of every step: ticket, plan, verification, commit | C10 | | | ● | | | ✓ |
| **Guards on known model weaknesses** | | | | | | | |
| `/discover`, an outside view before saying what a thing is | C2 | ● | | | | | ✓ |
| general rules against them: one case is not a class; the fewest parts; a shape's context and structure explored | C2 | ● | ● | | | | ✓ |
| no reopening a settled decision without new evidence | C2, C6 | | ● | ● | | | ✓ |
| **Delivery and evaluation** | | | | | | | |
| thin vertical slices; `/plan` validated against the governing docs; `/tdd` | C3, C7 | ● | ● | | | | ✓ |
| `/verify` against the ticket, the plan, the governing docs and the project's checks | C7 | ● | | | | | ✓ |
| a rule on who may change the checks that work is measured by | C7 | ● | | | | | <straw-dog question="q-0018.0022">✗</straw-dog> |
| every second look at work as one pass | C7 | ● | | | ● | | <straw-dog question="q-0029">✗</straw-dog> |
| a failure traced to its cause, so that what let it through is corrected | C7 | ● | | | ● | | <straw-dog question="q-0033.0003">✗</straw-dog> |
| **Tiers** | | | | | | | |
| every rule at the tier its occasion is read at: the entry contract, installed blocks at their anchors | C1 | ● | ● | | | | ✓ |
| whether a rule reaches its occasion observed, not asserted | C1 | ● | | | | | <straw-dog question="q-0025">✗</straw-dog> |
| **One source of truth** | | | | | | | |
| one home per rule, copied by a script into every place that reads it, and checked | C1 | ● | | | ● | | ✓ |
| decisions in the architecture, its records and the glossary; who decided each rule, and when | C1, C6 | ● | | ● | ● | | ✓ |
| every record says which side wins when it and the code disagree | C6 | ● | | | ● | | <straw-dog question="q-0024.0009">◐ named; records being brought to it</straw-dog> |
| **Maintenance** | | | | | | | |
| `/maintain`: records against each other and against the code, after each piece of work and when what governs them moved | C6 | ● | | | ● | | ✓ |
| **Self-improvement** | | | | | | | |
| a register of rules that were in place and did not fire; the next occurrence grades the rewording | C7, C1 | ● | | | ● | | ✓ |
| declared and checked mechanisms, each with its doc and evidence | C1, C7 | | | | ● | | ✓ |
| a recorded failure replayed as a test against the amended rule | C7, C1 | ● | | | ● | | <straw-dog question="q-0026.0004">✗</straw-dog> |
| the method measured on the same tasks with and without it, and its cost counted | C7 | | ● | | ● | | <straw-dog question="q-0017">✗</straw-dog> |
| **Coordination between sessions** | | | | | | | |
| each session sees where the others stand; the question store refuses a write to an entry that moved | C5 | ● | ● | | | | ✓ |
| locks, so two sessions cannot write the same file | C5 | ● | ● | | | | <straw-dog question="q-0032">✗</straw-dog> |
| a starting session takes an area no other session is in | C5 | | ● | | | | <straw-dog question="q-0016.0001">✗</straw-dog> |
| **Process weighed to the work** | | | | | | | |
| one step per reply, with a point to reassess at its end | C8, C9 | | ● | ● | | | ✓ |
| a lighter path for small work and a heavier one for large | C8 | | ● | ● | | | <straw-dog question="q-0027.0003">✗</straw-dog> |
| **Refusing harm** | | | | | | | |
| the host refuses an action a rule forbids | — | | | | | ● | <straw-dog question="q-0018.0005">✗</straw-dog> |

<straw-dog question="q-0033">
Read by column:

- **1 Ineffective** has the most answers, and most of them are in place.
- **2 Suboptimal** waits on two absent rows that weigh most: locks between sessions, and a
  lighter path for small work.
- **3 Agency** rests on the load-bearing test, HITL, the switches and visible footing as much as
  on the exploration space. Its two absent rows are the ones that would let the person move the
  point on the scale.
- **G1** rests on one source of truth, maintenance and self-improvement, and nothing measures
  whether it holds.
- **G2** has no answer at all.
</straw-dog>

## A pain of the harness itself

**The method doesn't fit the project, and the project's changes are lost on update.** This is a
pain of adopting a tool, not of developing with agents. The harness answers it with:

- the project's own rules file, applied last and kept through updates;
- an update that stops rather than overwrite a hand edit;
- its own skills checked like the shipped ones.

Its open parts:

- <straw-dog question="q-0018.0020.0001">An install meets an existing `CLAUDE.md` or `AGENTS.md` by moving it aside, in one mode only.</straw-dog>
- <straw-dog question="q-0018.0013">There is no uninstall.</straw-dog>
- <straw-dog question="q-0018.0023">Three hosts are supported.</straw-dog>

Its home is q-0018 "How do projects share one development method without losing their own
conventions?".
