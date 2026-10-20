# Session 0061 — speech set apart from work

- **record of** what happened

2026-10-16 to 20. Began with the user quoting a session's first reply under `/recall` — *Good
morning, within the recall: the session is registered, no position yet. Reading the wake and what
concerns Core and instance* — and proposing that rules be told apart as background work and as how
to speak of it, with tests. Ended with the split decided, a test bench built and run red to green,
three skills and the entry file amended, and Q2 reworded. Every turn under `debug=on`.

## Decisions

All on [q-0037.0010.0012.0001](../questions/q-0037.0010.0012.0001-how-does-a-rule-tell-the-work-an-agent-does-unseen-from-what-it-says-to-the-person-about-that-work-and-how-is-a-reply-tested-for-keeping-them-apart.md),
opened this session under the question of where the method ends and the machinery begins.

- **Speech is marked, work is not.** Marking both kinds was weighed and refused: hundreds of rules
  to classify, and the default would be needed anyway, since the agent narrates its steps with no
  rule asking (rule failure 48). A reserved verb alone was refused as leaving nothing to check. The
  fact that turned it: in both recorded failures speech was *already* set apart — `/recall`'s
  `<hitl>`, `/harness`'s *After the first install* — and written in the work's words; the mark's use
  is to make a speech rule checkable.
- **The method's step is told, its course is not.** The user's own opening example, *good morning,
  recalling what we have*, names the step; the bad reply named what was read and registered. The
  entry file's *the step* was read as the agent's own step; it now says *the method's step as the
  person would name it* (v94).
- **A skill's speech stands in `## What the person hears`** — the user chose the section over an
  inline tag. `<hitl>` was the user's own hand edit of 2026-10-08, read by no script, and the method
  glossary's HITL means a ticket needing a decision; it was renamed into the section, not kept.
- **A reply is tested by a second reader who knows nothing of the rules.** Described in the
  abstract twice, it was not understood — *I understood nothing, what is a run, what is a case
  folder* — and was then shown live: a fresh agent wrote the morning reply under the tree's rules and
  reproduced the failure at once; a second, given only the message and the reply, flagged every
  sentence. Then accepted.
- ***Now I'll look where we stopped* is the method's step** *(the user, 2026-10-18)*, ruling on the
  reader's split.
- **Q2 takes from the wake, never reports it** *(the user, 2026-10-20)*.

## Principles derived, no durable home yet

- **A test of an instruction needs a control the reader must pass, and the control grades the
  reader first.** The first reader failed the good reply three times in three — for the user's own
  *recalling* — and was right about two other faults in it. Without the control the bench would
  have measured a reader that flags everything. The bench is now
  [q-0037.0012.0009](../questions/q-0037.0012.0009-how-is-an-amendment-to-an-instruction-tested-before-it-lands-against-which-cases-chosen-how-run-with-no-instruction-the-standing-one-and-the-new-one.md)'s
  material too.
- **A word that names both a script's output and the agent's words to the person carries the
  narration.** *Report* in Q2, F2 and elsewhere read as speech; the store's words — *suspect*,
  *deferrals*, *straw dogs* — reached the person through it.

## Done

- The question opened, aligned in four decisions, its `Where it stands` accepted.
- [The speech bench](../research/speech-bench/): cases, writer and reader prompts, every run's
  replies; [the morning's red, green and Q2 rounds](../research/speech-bench/results/red.md).
- `/recall`'s `What the person hears`, its `<hitl>` gone; the entry file's *A reply speaks the
  method*, v94.
- `/harness` and `/maintain`, by
  [a session this one proposed](../research/speech-bench/results/install-and-maintain.md), which
  went on to decision 5 of the question (the 🪶 table and a repair's detail under `debug=on`, v95)
  and to the debugging mechanism.
- Q2 reworded in the questions rules file and reinstalled.
- [Rule failure 51](../rule-failures.md) struck a third time, outside `/harness`, its amendment
  landed; 52 registered and refused.

## What went wrong

- **A fork asked that the person had answered** — the second align question offered the user's
  own example as one option of three. Registered as rule failure 52; the user refused the
  amendment: *I worded it imprecisely myself.*
- **An explanation in the bench's own words** — *run*, *case folder* — twice, before the live
  demonstration that was the explanation. The user: *I understood nothing.*
- **A shell command waited on input** (`cat >` with no heredoc) and hung two minutes; stopped and
  cleaned up.
- **Writers read the live tree**: the first red writers ran `git status` and saw the bench's own
  uncommitted files. Later prompts allowed the Read tool alone.

## Open questions touched

- [q-0037.0010.0012.0001](../questions/q-0037.0010.0012.0001-how-does-a-rule-tell-the-work-an-agent-does-unseen-from-what-it-says-to-the-person-about-that-work-and-how-is-a-reply-tested-for-keeping-them-apart.md)
  — open. Three skills and the entry file speak from the split. Waits on: a case for the reply
  after `/recall`'s reads, where Q2 bears; `/maintain`'s report, two in five still in the store's
  words; the other speech sites, as each is next touched.

## Next

A bench case for the reply `/recall` gives once its reads are done — the writer needs the reads'
results in its context, which the morning case does not give — then Q2 graded on it.
