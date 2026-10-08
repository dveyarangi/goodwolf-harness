# q-0033 Which pains of developing software with coding agents does the harness exist to relieve, and what answers each?

- **state** open
- **lean** the user, 2026-10-09: three pains — work called done that is not, time and tokens, thinking that cannot range freely; the first two share causes — instructions that do not reach the agent, wrong model decisions, a task set wrong, agents out of sync — answered by tiers, one source of truth, counted misses, the person at the weak decisions; correction and evaluation run across all
- **struck** 0, last 2026-10-08T21:08Z

Opened 2026-10-09 from the front-page align (q-0031). Each list of what the harness *is* came
out as either its implementation or general engineering claims. The user: *none of this answers
the user's pain.* The user then named the pains, and a second pass sorted them into a causal
chain. This body is the whiteboard: the user's words sorted, with what the tree has today against
each and what is missing. Its decisions land in a durable home once their form is seen. The user:
*much of this should determine how we develop the project.*

## The chain

The first list put pains and their causes side by side. The user: *2 and 3 are links of one
chain.* Instructions that do not reach the agent are a cause of work that is called done and is
not, and so is agent desync. The chain runs from pains, through their causes, to what answers
each cause.

```
PAIN  work called done that does not work, or is not what was meant
  ├─ cause  instructions don't reach the agent, or are composed wrongly
  │     ├─ scattered        → tiers
  │     ├─ contradictory    → one source of truth (also answers drift)
  │     └─ unchecked        → misses counted, evidence accumulated
  ├─ cause  the model took a wrong decision
  │     └─ → the person present at the decisions where models are known to be weak,
  │          and able to see what the agent's work stands on
  ├─ cause  the task was set wrong
  │     └─ → (proposed) the task takes its form in the open question before it is minted
  └─ cause  agents out of sync with each other
        └─ → coordination between sessions (locks: q-0032)

PAIN  time and tokens
  └─ the same causes: rework after each of the above, and duplicated work between agents

PAIN  thinking cannot range freely
  └─ → a memory of the exploration space

ACROSS ALL  correction and evaluation, together
```

## The pains

### Work is called done and does not work, or is not what was meant

The pain the person meets most directly. Its causes are below, each with its own answer.

### Time and tokens

The user: *this is also the cause of another pain — time and tokens.* Every cause of the first
pain spends again: rework after a wrong result, and agents in desync repeating each other's work.
The harness's own cost belongs here too, as context loaded every session. That is measured,
honestly, on the front page, and what it saves is not yet (q-0017, q-0018.0008).

### Thinking cannot range freely

The user: *it is also the ability to think and write freely, jumping from topic to topic.* With an
agent, whatever is not the task in hand evaporates, so the person narrows their own thinking to
what the agent can hold.

**Answer: a memory of the exploration space.** Not only what was decided and done, but what was
asked, what is open, where each question leaned, and what is provisional and waiting on which
question. A message lands where it belongs; a jump to another topic loses nothing; a new session
continues the exploration rather than restarting it.

- **Today:** the question store and its tree; every message placed before the reply; the window;
  the strike count; leans; straw dogs bound to the questions they wait on.
- **Missing:** a judge outside the agent, for placement (q-0001.0016.0001); hook wiring in
  installed trees (q-0018.0020.0005); a way to keep a question nobody reaches from sinking
  (q-0001.0018).

## The causes, and what answers each

### Instructions don't reach the agent, or are composed wrongly

The user: *they are scattered, contradictory and unchecked.* The principle is control over
whether an instruction reaches its reader, in a form it will follow. Each of the three has its
own answer.

**Scattered → tiers.** Every rule is placed at the tier its occasion is read at: always loaded,
delivered at the moment it governs, or reachable on demand.

- **Today:** the tiers, installed blocks at their anchors, the entry contract.
- **Missing:** whether each rule reaches its occasion is asserted, not observed (q-0025,
  q-0025.0003).

**Contradictory → one source of truth.** Every rule, fact and decision has one authoritative home;
copies are generated and checked; each record declares which side wins when it and the thing it
governs disagree. This also answers drift between decisions and code.

- **Today:** rules files and the installer's check, the four kinds, `/maintain`.
- **Missing:** the kinds are still being brought to the records (q-0024.0009).

**Unchecked → misses counted and evidence accumulated.** Every rule that was in place and did not
fire is registered, with the rules in play and the amendment, and the next occurrence grades the
amendment. The user: *this mechanism is the seed of a test suite for instructions.*

- **Today:** the rule-failure register (22 entries), the per-mechanism evidence records, the
  strikes that grade a rewording.
- **Missing:** replaying a recorded failure as a test against the amended rule; a measure of
  whether rules fire at all.

### The model took a wrong decision

The user: *fixed by the user's presence in the decisions where an LLM is known to be weak.* That
needs two things.

- **A definition of what is in the person's hands:** the main decisions, and the ability to say
  which kinds of decision the person takes and which are left to the agent's judgement.
- **Seeing what the work stands on.** The user: *important, but not a pain of its own — it is what
  puts the user where a decision has to be taken.* A reply that shows its question, the principle
  it reasons by and what it rests on lets the person catch a wrong decision cheaply.

Status of each part:

- **Today:** every decision goes through `/align`. A load-bearing decision is the person's, and
  one that is not is settled in the turn and reported. The switches cover commit, push, the next
  cycle, the breakdown and repair. Each rule carries who decided it. The rows and marks on each
  reply (q-0030).
- **Missing:**
  - **A record of where models are known to be weak.** The tree already holds pieces: the
    questions mechanism says the agent fails at judging whether a question is load-bearing and
    whether a shape hides parts; the rule-failure register records where rules were filled
    loosely. These are not gathered into the list that decides which decisions go to the person.
  - **Kinds of decision.** The switches name actions, not kinds of decision. The boundary is the
    load-bearing test, applied by the agent's judgement, and a project cannot move it.

### The task was set wrong

The user names it as the third cause and gives no answer yet.

- **Proposed by the agent:** the whiteboard answers it. Everything bearing on a task is written in
  the body of the question it stands on until its form is seen, and the ticket is minted only
  then, with checkable criteria; `/align` stress-tests it. If so, the memory of the exploration
  space is also the answer to this cause, not only to its own pain.
- **Today:** question bodies used as whiteboards; `/align`; `/spec`; `/impact`; tickets with
  criteria.
- **Missing:** the rule that a ticket is minted only from a question's body is decided in
  q-0024.0009 and not yet landed.

### Agents out of sync with each other

The user: *not a pain of its own, but one of its causes — desync between agents leads either to
overspending tokens and time, or to a wrong decision.*

- **Today:** the shared sessions file, so each session sees where the others stand; the store
  refuses a write to an entry that moved since it was read.
- **Missing:** locks (q-0032); a starting session choosing an area that does not overlap another's
  (q-0016.0001).

## Across all of them: correction and evaluation

The user: *solved by a mechanism of correction and evaluation; neither works without the other.*

- **Evaluation** without correction produces a report nobody acts on.
- **Correction** without evaluation rewords rules blind.

Work is evaluated against its own criteria and the project's checks. A failure is traced to its
cause in the chain above, and corrects both the work and whatever let it through: an instruction,
a decision boundary, a task's form.

- **Today:** tickets with acceptance criteria; `/verify`; `/maintain`; the rule-failure loop.
- **Missing:** tracing a failure to its cause in this chain; evaluating the method itself on the
  same tasks with and without it (q-0017); a second look as one shape (q-0029, 01-0030); who may
  change the verification set (q-0018.0022).

## Not a root pain

**The method doesn't fit my project, and my changes are lost on update.** The user: *a detail of
onboarding and lifecycle — a pain of the harness itself, not of developing with agents.* It can be
named on the page, but not as a root pain. Its home is q-0018 "How do projects share one
development method without losing their own conventions?".
