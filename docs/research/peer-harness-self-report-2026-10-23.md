# A peer harness, by its own account, 2026-10-23

**Kind:** evidence: a dated account of another harness. The account was written by that harness's
own agent and sent to this project's user, who passed it on. It is filed under
[q-0038](../questions/q-0038-what-landscape-does-this-project-evolve-in.md) at the user's word,
2026-10-25. The text is the peer's and private, so it is summarized here, not reproduced. People
and the peer's subject matter go unnamed: this tree is public.

The peer was built by one person, a lawyer, for their own work: a long research project, and a
pipeline that reads a document library into a database. It is not a product and is not installed
anywhere else. It runs on Claude Code, alongside the tools named below. Its agent wrote the
account for a programmer, after a week's worth of logged failures.

## How it is built

- **A headquarters and a ladder of executors.** One long Claude Code session designs the work, sends
  sealed packets to executors, accepts what comes back, and talks to the person. It does none of the
  bulk work. The executors are Codex, run as a detached process from a written brief; Claude
  through the Agent SDK on API credits; Gemini through an IDE agent driven by a script; ChatGPT Pro
  and Deep Research through the browser only; a local GPU box with models run as services; and
  another person's ChatGPT agent, reached only through files that person carries. A packet names
  the files that may be read, what must not be touched, a time limit and what to return. Learned
  clauses ride in it: work to the end without questions, and write results in portions every half
  hour, so that a quota reset does not erase the work.
- **Memory in two layers.** The first layer is rules: a global rules file and one-fact memory files
  with frontmatter and an index loaded every session, the same shape as Claude Code's auto-memory.
  Every rule is born of a caught failure and carries the date, the quote, the cause and how to
  apply it. The second layer is project memory: a shift log with timestamps taken from a timezone
  library inside a script (once, timestamps had been written ahead of the clock), handoff files
  between headquarters of different models, and boards. One rule says every thought in a reply is
  turned into a started task or a recorded obligation in the same turn; otherwise it counts as a
  failure.
- **Routines that run by themselves.** A nightly scheduled routine: a council of eleven named
  personas rereads the day's material and gives free guesses and critique. Its own finding is that
  a persona's name adds nothing without a card of techniques, so the names stay only as labels for
  the cards. Two or three times a day, the status and eight questions go to outside models, and the
  answers are synthesized under three heads: new to us, a repeat of ours, self-deception of the
  headquarters. Recurring work hangs on loops and alarms rather than on the model's memory. The
  operating system's scheduler failed silently seven runs in a row; the loop now runs in the
  user's session with a stop file, and an in-session wakeup checks the loop.
- **Acceptance that makes it science.** Every measure first passes an exam on a known answer.
  Thresholds are written before counting, and two runs must match byte for byte. Whoever wrote a
  result does not judge it: Codex's work is checked by Claude, and Claude's by Codex. A registry
  of experiments, 252 rows, gives each a verdict: alive, killed, on the edge, untested, or
  instrument unfit, with `superseded_by`. A bank of the person's ideas records each idea's
  strength and state; an idea is dead only by an experiment with a file. In the library pipeline,
  readers propose a claim with a verbatim quote of 6 to 15 words. The quote is checked
  mechanically against normalized text. Senior models judge meaning only on samples and on the
  dangerous class. One writer imports accepted packets idempotently, on a copy with a rollback.
- **Self-improvement, by its own word not automatic.** Failure, the person catches it, a memory
  file with an example and a rule, the rule loaded every session, a failure counter. Unsolved: a
  handoff between headquarters shifts loses detail, subagents do not see the memory, and nothing
  checks a text before it reaches the person.

## What it has that this harness lacks

Each item is read against this tree as it stands on 2026-10-25.

1. **A ladder of executors priced by cost.** Bulk work goes to cheap or free models; a headquarters
   only designs and accepts. This harness has one host and parallel sessions of the same model. It
   has no notion of handing a sealed packet to a cheaper executor and accepting its return.
2. **A budget ledger.** The real cost of each run is recorded, under an overall ceiling, and a live
   run reserves its own ceiling against its process id, so parallel runs cannot overspend. Here,
   cost is an open question,
   [q-0037.0006.0008](../questions/q-0037.0006.0008-what-does-the-harness-cost-and-save-counted-rather-than-guessed.md),
   and nothing is metered.
3. **An instrument examined before it is used.** A known answer comes first, thresholds are fixed
   before the count, and two runs must be identical. Here `/verify` checks work against its ticket,
   and the benches under `docs/research/` were run once each, with no exam of the bench itself and
   no thresholds written in advance. This bears on
   [q-0038.0001](../questions/q-0038.0001-does-working-under-the-harness-deliver-software-better-than-working-without-it-measured-on-the.md)'s
   design.
4. **A registry of hypotheses with verdicts.** The question store closes a question with a kind and
   an answer, but a guess tested and killed has no row of its own with *instrument unfit* as a
   possible verdict. Refuted shapes live in a mechanism's evidence as prose.
5. **The judge from another vendor.** Here, the judge who did not build a criterion is another
   session of the same model. The peer crosses vendors, so the judge does not share the builder's
   blind spots.
6. **Routines on a clock.** The peer runs a nightly council and outside heads polled several times
   a day, with a synthesis that names the headquarters' self-deception. Here `/dream` is run by
   hand after `/conclude`, and `/discover` is one outside head, on demand.
7. **Mechanical checks on what a model quotes.** A claim carries a verbatim quote, and a script
   checks the quote against the source before any model judges the meaning. Nothing here checks a
   quotation in a record against what it quotes.
8. **A single idempotent writer.** Accepted packets reach the database through one writer, on a
   copy, with a rollback, and a repeat import writes zero rows. Here the store's scripts refuse a
   write to an entry that moved since it was read. That guards against collision, not against a
   repeat or a half-applied batch.

## Where the two meet

The peer's account, written independently, arrives at the same wall this tree records in
[q-0037.0012](../questions/q-0037.0012-how-does-the-harness-amend-its-own-rules-by-stated-meta-rules.md):
the person catches every failure, and a rule is the remedy. Both prefer a mechanism to a promise.
Both forbid showing the person an internal number without saying what it stands for. Both lose
detail across a handoff. The peer has nothing like the question tree, straw dogs, the four kinds
of record, or an install into another project. That is noted, not weighed: the peer is not
trying to be any of these.
