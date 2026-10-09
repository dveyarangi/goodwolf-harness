# Session 45 — what the harness is for

**2026-10-08 to 2026-10-09.** Claude Code, one conversation, resumed by its host under a second
id (`693642b7…`, then `a9b67b24…`). Entry contract v33 at the start; parallel sessions raised it
to v50 meanwhile. The model was switched from Fable 5.1 to Opus 5.5 early in the first day.

The session set out to rethink the front page. It found that the page could not be written until
the project said what it is for, and spent most of its length on that. It ended with
[the product document](../product.md) as the project's leading record, and the front page
rewritten from it.

## What was decided, and what chose it

### The front page says what the harness is, in the reader's terms — q-0031

- **Not "institutional memory", not "cognition".** The user offered *persistent project cognition
  for stateless coding agents*. The agent refused *cognition* on the ground that the harness is
  not a memory architecture. The user: *how is it not?* The agent's own filed discover pass rated
  that family medium-high. The refusal was withdrawn: it is a memory of the project, not of the
  agent.
- **Two outside passes on the recall structure**, at the user's request
  ([discover-recall-structure](../research/discover-recall-structure-2026-10-08.md)). The user
  had struck the agent's claim that *no embeddings* sets the harness apart (*embeddings are
  already going out of use*). The passes found the claim narrower than either side. Single-vector
  top-k as the only path is losing ground; hybrids remain the default; the field moved to who
  controls retrieval. The user's second point held as well: a source of truth per record does not
  replace a recall structure. The harness has one, with several selectors — position, activation,
  dependency, obligation.
- **Useful tool, not technical curiosity** *(the user)*. The page was rebuilt around the reader's
  jobs. Two cold readers, a solo developer and a sceptical tech lead, read each draft, the second
  round with fresh agents. Their findings:
  - the workflow's weight was hidden;
  - the `CLAUDE.md` handling was buried;
  - absolute promises contradicted the page's own *instructions, not enforcement*;
  - the page claimed that hooks delivered context in installed projects. They did not then;
    another session has since carried the wiring.
- **The genre surveyed** ([readme-survey](../research/readme-survey-2026-10-08.md)): install in
  the first third, benefit bullets, a session told from the user's seat. Of eleven peers, none
  says who it is not for or what it costs. The user kept the honest sections and the mechanism
  section, and asked for a session from the user's seat.
- **The positioning was redone from evidence of the day.** The user: *the 2026-09-26 pass is long
  out of date.* Four capability passes built
  [a matrix of sixteen peers](../research/peer-capabilities-2026-10-08.md). Then the user:
  *no comparisons at all; say what is.* The final page names no peer.
- **Wording struck by the user, each turn by turn:**
  - the version announcement in the morning scene — *a debugging line*;
  - *decisions live in…* — *too verbose, and undersells*;
  - *every open question kept as a record* — method, not result;
  - *starts over from whatever static notes you left it* — sounds like a chore laid on the user;
  - *a system that keeps the documentation true* — *the point is not maintaining documentation
    but that decisions taken get built*;
  - *what's new* — *we need what is*.

### What the harness is for — q-0033, now `docs/product.md`

The user rejected two lists in a row: the agent's implementations, then its general engineering
claims. *None of this answers the user's pain.* The pains were then found in four sortings, each
correcting the last:

1. The user named four root pains. The agent mixed pains with their causes.
2. *2 and 3 are links of one chain.* Instructions that don't reach the agent cause work called
   done that isn't, and so do agent desync and wrong model decisions. Time and tokens are a pain
   of their own.
3. Generalized by the user to **ineffective**, **suboptimal** and **the user is not agentic**.
   Causes and answers overlap across all three.
4. *Agency is a scale — at one end loss of control, at the other micromanagement.* *Better over
   time* and *no harm* are goals nothing guarantees yet and that may not be lost. The agent had
   forgotten the load-bearing test and HITL; the user named them, and a sweep found more.

The format — a list of pains, a list of causes, a matrix of answers — was chosen by the user as
the leading product document, from which goals and the front page are derived. Within it:

- **Causes are seed**, with pains and goals; the agent may propose new ones.
- **The matrix should become a derivative** of the tree, except what the operator seeded *(the
  user, not yet sure)*. A poorer derived matrix is no problem: *the "full" one is full of
  mechanisms that are not mechanisms.* For everything in it that is not a mechanism, a markup and
  extraction procedure is owed.
- **The product mark lives on questions, never on tickets or other temporary records** *(the
  user)*. A ticket reaches the product through the question it answers.
- **Collecting the marks may be the release mechanism reincarnated** *(the user)*. Recorded as an
  intention on q-0033.0005; 01-0010.0190 carries the note's product half.
- **Built answers.** Answers built through the question store are fine. The harness's own
  historical rules count as seed, as straw dogs, until q-0026 settles who owns them. An install
  into an existing project harvests its answers in two stages. First, an align on what is hard and
  what causes it, gated on at least one solvable difficulty. Then a pass over docs and code that
  writes what it finds as questions, never as marks in code. A found answer is HITL until the
  person confirms it (q-0018.0011.0004, q-0027.0002).
- **The "why" of a found answer is the cause the person recognized** *(the user, correcting the
  agent)*. The agent had run two whys together: why a thing exists, which is the product's, and
  why it was built this way, which is the architecture's.

### Smaller decisions

- **Locks between sessions are needed;** the architecture's disclaimer is wrapped as a straw dog
  (q-0032).
- **More hosts are needed** (q-0018.0023).
- **Integration with an existing entry file in two modes** — the harness takes over, or is added
  by one import line — is one of the most important candidates for work (q-0018.0020.0001).
- **The front page's review by outside agents is kept as a process,** described rather than made a
  skill ([record](../research/front-page-review-by-outside-agents-2026-10-08.md)). It is a case of
  q-0029.
- **A sweep of `docs/product.md` against the whole tree by `/maintain` is premature:** the tree
  also serves structure and evolution.

## General principles derived, with no durable home yet

- **Start from the pain, not the mechanism.** A list of what a thing *is* comes out as its
  implementation unless it begins from what hurts the person.
- **Agency is a scale with two failing ends.** The right point is set by the weight of the
  decision and by where models are weak.
- **Correction and evaluation only work together.** Evaluation without correction is a report
  nobody acts on; correction without evaluation rewords rules blind.
- **A mark belongs on the record that outlives the work** — a question, not a ticket.
- **A product's *why* is its cause.** A design's *why* is the architecture's, and only the second
  is at risk of being invented by reconstruction.
- **An audit by the same model measures agreement, not truth.** The oracle is its list after the
  person has ruled on each item.

## What was done

- **The front page,** rewritten five times and landed from the product document.
- **[docs/product.md](../product.md)** — three pains, two goals, twelve causes, 48 mechanisms marked
  present, partial or absent, each absent one bound to its question.
- **Research filed:**
  - the two recall passes;
  - the README genre survey;
  - the sixteen-peer capability matrix;
  - the front-page review process;
  - the [product audit](../research/product-audit-2026-10-09.md);
  - [the consolidated inventory](../research/harness-answers-inventory-2026-10-09.md): 157 items,
    78 weaknesses, and the rule-failure register read entry by entry.
- **Questions opened:**
  - q-0031, q-0032, q-0033 and its children;
  - q-0018.0023, q-0018.0011.0004, q-0025.0003;
  - q-0026.0004 and its child q-0026.0004.0002;
  - q-0026.0005, q-0023.0020, q-0025.0004, q-0018.0004.0002.
- **Questions merged and moved:** q-0033.0002 merged into q-0027.0002; q-0026.0002 moved under
  its missing parent, as q-0026.0004.0001.
- **Release tickets:** 01-0010.0185 and .0190 rebuilt. .0185 had briefly carried a product line,
  withdrawn when the mark moved to questions.

## What was refuted or went wrong, and what it taught

- **Claims made from stale or second-hand evidence.** The agent refused *memory architecture*
  against its own filed pass. It positioned the page from a twelve-day-old pass. It wrote a
  "real" example that the transcripts showed to be one conversation resumed, not a fresh session.
  Each was caught by the user or by a check, and each taught the same thing: check the record
  before claiming from it.
- **The page described the method instead of the result,** through three drafts, until outside
  readers and the user's corrections forced each line into the reader's terms.
- **Statuses were overstated.** The first matrix marked as present what was a definition, a
  straw dog, or a skill not declared as a mechanism.
- **The audit's list was not filed** until the user asked whether everything was collected. Twice
  more, sources that were not on disk were nearly lost.
- **Two of the agent's own edits went by script** — a `sed` and a heredoc — against the user's
  rule that edits are made with edit tools.
- **Parallel sessions collided on a session number.** Two records numbered 0044 exist this day,
  live evidence for q-0032.

## Open questions touched, and where they stand

- **q-0031** — the front page. Landed from the product document; it waits on the product
  document's own evolution.
- **q-0033** — the product root; stays open while absent rows remain. Its children:
  - q-0033.0001 — where models are weak;
  - q-0033.0003 — tracing a failure to its cause;
  - q-0033.0004 — teams;
  - q-0033.0005 — keeping the document true: marks on questions, derivation, collection at
    release.
- **q-0018.0011.0004** — an arrival's two-stage harvest and a generated question tree; to be
  tested on the harness itself against the inventory, once the person has ruled on its items.
- **q-0027.0002** — HITL as a mark on questions.
- **q-0032** — locks. **q-0018.0023** — more hosts. **q-0018.0020.0001** — two integration modes.
- **q-0025.0003** — the version announcement as a straw dog. The wrap is pending the user, and the
  entry contract has moved on since.
- **The five opened for the register's weaknesses:** q-0023.0020, q-0025.0004, q-0026.0005,
  q-0026.0004.0002, q-0018.0004.0002.

## What continues

- **First step: derive goals from the product document** — the queue's order read against its
  absent rows. 01-0010.0150, the existing entry file in two modes, was named one of the most
  important; whether it becomes the candidate is the user's.
- **The inventory awaits the person's verdicts** before it can serve as the oracle for a mechanism
  that generates a project's question tree.
- **Entry 22 of the rule-failure register** may have regressed under a later rewrite
  (q-0026.0004.0002).
