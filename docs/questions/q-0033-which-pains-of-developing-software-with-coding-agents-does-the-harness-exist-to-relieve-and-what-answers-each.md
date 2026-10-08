# q-0033 Which pains of developing software with coding agents does the harness exist to relieve, and what answers each?

- **state** open
- **lean** the user, 2026-10-09: the answer lives in docs/product.md, the leading product document — pains, goals without a guarantee, causes, and a matrix of mechanisms marked present, partial or absent; goals and the front page derive from it; open while the absent rows are
- **struck** 0, last 2026-10-08T21:08Z

Opened 2026-10-09 from the front-page align (q-0031). Each list of what the harness *is* came
out as either its implementation or general engineering claims. The user: *none of this answers
the user's pain.* The user then named the pains, and a second pass sorted them into a causal
chain. This body is the whiteboard: the user's words sorted, with what the tree has today against
each and what is missing. Its decisions land in a durable home once their form is seen. The user:
*much of this should determine how we develop the project.*

## The pains generalized — fourth sorting, 2026-10-09

The user generalized the pains to three — *the agent is ineffective; the agent is suboptimal; the
user is not agentic* — and noted that causes and answers overlap across all of them. *The
person's presence at important points is agency; aligning the person's space of ideas with the
exploration space is agency too, and it also serves effectiveness and optimality.* The third
sorting worded the third pain as *the person loses the lead*. The user: *the user's agency is a
scale — at one end loss of control, at the other micromanagement; "loses the lead" is half of
what I meant.*

### Three pains

1. **Ineffective.** The agent does not reach the intended result: work called done that does not
   work, or is not what was meant.
2. **Suboptimal.** It reaches the result at too high a cost: tokens, time, rework, and the
   person's attention.
3. **The person's agency is off its point.** It sits on a scale and fails at both ends:
   - **Too little: loss of control.** Decisions that matter are taken without the person, the
     shared picture drifts from theirs, and the project stops being theirs to steer.
   - **Too much: micromanagement.** The person re-explains, re-checks, approves each step, and
     babysits work the agent could carry.

   The right point puts the person at the decisions that bear load and where models are known to
   be weak, and nowhere else.

### Two goals with no guarantee yet

The user: *both are important, we have nothing yet to guarantee either, and neither may be lost as
a goal.*

- **G1 Better over time, not worse.** Decisions do not erode, contradictions do not accumulate,
  and a lesson learned in one session holds in the next.
- **G2 No harm.** The agent does not destroy work, leak secrets or act beyond what it was
  allowed. The only answer today is trust (q-0018.0005).

### Causes

- **C1** instructions don't reach the agent, or are wrong — scattered, contradictory, unchecked
- **C2** the model decides where models are known to be weak
- **C3** the person's space of ideas and the exploration space diverge; a task set wrong is one
  case
- **C4** the exploration space is lost between sessions
- **C5** agents out of sync with each other
- **C6** what was decided and what was built drift apart
- **C7** failures go undetected or unattributed, so nothing is learned
- **C8** the process weighs the same for small and large work
- **C9** where the person is placed is left to the agent's mood rather than to the weight of the
  decision, so both ends of the agency scale happen
- **C10** what the agent's work stands on is invisible, so checking it cheaply is impossible, and
  the person either trusts blindly or re-checks everything

### Answers against pains

**The exploration space is one answer, not two.** The third sorting split memory from alignment
and called the second *aligning the idea space with the agent's map*. The user: *alignment of the
idea space with the exploration space — what is the agent's map, docs?* It was not docs. It was
the question tree and the agent's placements in it, which is the exploration space itself. So:

- **memory** keeps the space;
- **alignment** keeps it matching the person's ideas — each message placed, a missing parent
  opened, a question reworded, an uncharted one put to the person.

Docs are a different answer: where settled outcomes land.

| answer — today's mechanisms | causes | 1 | 2 | 3 | G1 | G2 |
|---|---|---|---|---|---|---|
| **the shared exploration space** — the question store, every message placed, the window, leans, strikes; `/recall`, `/conclude`; straw dogs bound to questions | C3, C4 | ● | ● | ● | | |
| **alignment of intent** — `/align`; a shared vocabulary in the glossaries; the whiteboard, with a ticket minted only once the form is seen; `/spec` | C3 | ● | ● | ● | | |
| **the load-bearing test** — `/impact` routes load-bearing work to the person and a spec, local work to the agent and a ticket; a load-bearing decision is the person's, any other is settled and reported | C2, C8, C9 | ● | ● | ● | | |
| **HITL and human checkpoints** — HITL or AFK on every ticket; every decision at `/align`; spec accepted, breakdown approved | C2, C9 | ● | | ● | | |
| **switches and the repair policy** — commit, push, next cycle, breakdown each `ask` or `auto`; repair `report` under four conditions, otherwise `ask` | C9 | | ● | ● | | |
| **visible footing** — the rows that open each reply, the marks on a paragraph, the ⚖️ and 🍂 tables, a record of every step | C10, C2 | ● | ● | ● | | |
| **guards on known model weaknesses** — `/discover`'s outside view; *one shape is not a class*, *Occam*, the shape's context and structure; no reopening a decision without new evidence | C2 | ● | ● | | | |
| **delivery discipline** — thin vertical slices, `/plan` validated against the governing docs, `/tdd`, `/verify` against the ticket, the plan and the checks | C7, C3 | ● | ● | | | |
| **tiers** — the entry contract, installed blocks at their anchors, hooks, *tier is paid by every session* | C1 | ● | ● | | | |
| **one source of truth** — rules files and the installer's check, the four kinds, architecture and decisions, provenance on every rule | C1, C6 | ● | | ● | ● | |
| **maintenance** — `/maintain`, marks and what is due, suspect answers under a moved parent | C6 | ● | | | ● | |
| **self-improvement** — the rule-failure register, evidence records, declared and checked mechanisms, `/skill-up`, `/dream` | C7, C1 | ● | | | ● | |
| **coordination between sessions** — the sessions file and positions, the store refusing a moved entry; locks to come (q-0032) | C5 | ● | ● | | | |
| **process weighed to the work** — one step per turn with a reassessment boundary; a lighter path to come (q-0027.0003) | C8, C9 | | ● | ● | | |
| **refusing forbidden actions** — none yet (q-0018.0005) | — | | | | | ● |

Read by column:

- **Ineffective** has the most answers.
- **Agency** rests on the load-bearing test, HITL, the switches and visible footing as much as on
  the exploration space. The third sorting missed the first three, and they are what set the
  point on the scale.
- **G1** rests on one source of truth, maintenance and self-improvement, and nothing yet measures
  whether it holds (q-0017).
- **G2** has no answer at all.

## The chain — second sorting, kept for its detail per cause

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
