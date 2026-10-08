# q-0033 Which pains of developing software with coding agents does the harness exist to relieve, and what answers each?

- **state** open
- **lean** the user, 2026-10-09: four root pains — thinking that cannot range freely, instructions that do not reach the agent, work that is called done and is not, important decisions slipping out of hand; the answers should steer how the project develops
- **struck** 0, last 2026-10-08T21:08Z

Opened 2026-10-09 from the front-page align (q-0031). Each list of what the harness *is* came
out as either its implementation or general engineering claims. The user: *none of this answers
the user's pain.* The user then named the pains and what answers each. This body is the
whiteboard: the user's words, sorted, with what the tree has today against each and what is
missing. Its decisions land in a durable home once their form is seen. The user: *much of this
should determine how we develop the project.*

## The root pains, and what answers each

A root pain is one that comes from developing with agents at all, not from adopting this tool.

### 1. Thinking cannot range freely

The pain is more than explaining the project again each morning. The user: *it is also the
ability to think and write freely, jumping from topic to topic.* With an agent, whatever is not
the task in hand evaporates. So the person narrows their own thinking to what the agent can hold.

**Answer: a memory of the exploration space.** Not only what was decided and done, but what was
asked, what is open, where each question leaned, and what is provisional and waiting on which
question. A message lands where it belongs, and a jump to another topic loses nothing. A new
session continues the exploration rather than restarting it.

- **Today:** the question store and its tree; every message placed before the reply; the window;
  the strike count; leans; straw dogs bound to the questions they wait on.
- **Missing:** a judge outside the agent, for placement (q-0001.0016.0001); hook wiring in
  installed trees (q-0018.0020.0005); a way to keep a question nobody reaches from sinking
  (q-0001.0018).

### 2. Instructions do not reach the agent

The user: *instructions don't reach the agent because they are scattered, contradictory and
unchecked.* The principle is control over whether an instruction reaches its reader. Each cause
has its own answer.

- **Scattered → tiers.** Every rule is placed at the tier its occasion is read at: always loaded,
  delivered at the moment it governs, or reachable on demand. Today: the tiers, installed blocks
  at their anchors, the entry contract. Missing: whether each rule reaches its occasion is
  asserted, not observed (q-0025).
- **Contradictory, and drifting → one source of truth.** Every rule, fact and decision has one
  authoritative home. Copies are generated and checked, and each record declares which side wins
  when it and the thing it governs disagree. This also answers drift between decisions and code.
  Today: rules files and the installer's check, the four kinds, `/maintain`. Missing: the kinds
  are being brought to the records (q-0024.0009); there are no locks between sessions (q-0032).
- **Unchecked → misses counted and evidence accumulated.** Every rule that was in place and did
  not fire is registered, with the rules in play and the amendment. The next occurrence grades the
  amendment. The user: *this mechanism is the seed of a test suite for instructions.* Today: the
  rule-failure register (22 entries), the per-mechanism evidence records, and the strikes, which
  grade a rewording. Missing: replaying a recorded failure as a test against the amended rule; a
  measure of whether rules fire at all (q-0017, q-0018.0008).

### 3. Work is called done and does not work

The user: *this comes together with counting misses, and it is solved by a mechanism of
correction and evaluation; neither works without the other.*

- **Evaluation** without correction produces a report nobody acts on.
- **Correction** without evaluation rewords rules blind.

The answer pairs them. Work is evaluated against its own criteria and the project's checks, and a
failure corrects both the work and the instruction that let it through.

- **Today:** tickets with acceptance criteria; `/verify` against the ticket, the plan, the
  governing docs and the verification set; `/maintain`; the rule-failure loop.
- **Missing:** evaluating the method itself on the same tasks with and without it (q-0017); a
  second look as one shape, one pass under different rules and readers (q-0029, 01-0030); who may
  change the verification set (q-0018.0022).

### 4. Important decisions slip out of hand

The user: *keep a hand on the pulse of the important decisions.* The answer is a definition of
what is in the person's hands: the main decisions, and the ability to say which kinds of decision
the person wants to take and which to leave to the agent's judgement.

- **Today:** every decision goes through `/align`. A load-bearing decision is the person's, and
  one that is not is settled in the turn and reported. The switches cover commit, push, the next
  cycle, the breakdown and repair. Each rule carries who decided it.
- **Missing:** the switches name actions, not kinds of decision. The boundary between the
  person's decisions and the agent's is the load-bearing test, applied by the agent's judgement,
  and a project cannot yet move it. How far the method's ceremony scales with the work's weight is
  the pacer's (q-0027.0003, 01-0020).

## Not a root pain

**The method doesn't fit my project, and my changes are lost on update.** The user: *a detail of
onboarding and lifecycle — a pain of the harness itself, not of developing with agents.* It can be
named on the page, but not as a root pain. Its home is q-0018 "How do projects share one
development method without losing their own conventions?".

## Proposed by the agent, for the user to accept or refuse

- **Several agents at once trip over each other.** Running sessions in parallel is where agent
  work scales, and today they overwrite each other's files, repeat work, or stand on the same
  question unaware. The user decided on 2026-10-08 that locks are needed (q-0032). This is a root
  pain the four above do not cover.
- **The person cannot see what the agent's work stands on.** Reviewing an agent's output costs
  more attention than writing it did. Without seeing which question a reply stands on, which
  principle it reasons by and what it rests on, the person cannot correct it cheaply. Today: the
  rows that open each reply and the marks on a paragraph (q-0030). This may be part of pain 4,
  since a hand on the pulse needs a visible pulse, or a pain of its own.
