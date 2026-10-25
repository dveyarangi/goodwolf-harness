# A document informs, and how an amendment is tested before it lands

- **record of** what happened

Session `local_32bdb1ef`, 2026-10-16 to 2026-10-24. Opened on four findings a coherence audit
returned from a recipient, xuanxue-workshop at `e5e74d6`; closed on an accepted design for testing
every amendment to an instruction, minted as six slices of
[01-0019](../tickets/01-0019-harness-amends-itself-by-explicit-meta-rules.md).

## Decisions, and what chose them

**Core and instance left the entry file** (v96, refined in v98). The user's first question: should
the section reach an instance at all? Moving it into mechanism-shape's rules was answered by their
own follow-up — *they will still be installed in the instance* — and the user turned the answer:
*the instance must follow this rule too where it can — put no instructions in docs*. That made the
section and *A document informs* one border seen from two sides. A first merge simply added the
two (*why did the rule and invariant suddenly get larger?*); the compression that followed was
benched (below) and failed twice before it held. Landed in v98: *A document informs* says a
document reaches the work only through the instruction that reads it; the core clause became the
origin's local rule L10, installed into `/skill-up`, `/mechanism` and `/implement`, since its
reader writes core and core is written here alone; the invariant, *core works the same over any
`docs/` whose records keep their declared shapes*, went to the mechanism shape's doc. skill-up's
*Project-local divergence* — whose appendix pointing at project documentation was the recipient's
second finding — is two sentences, narrowed in v98 when a Sonnet audit showed v96's wording forbade
the local block R7 installs into a shipped skill. Record: [entry-contract-findings](../research/entry-contract-findings.md), v96–v98.

**The leak diagnostic names no rule.** `RULE = "AGENTS.md § Core and instance"` was a second home of
a section's name, edited by hand on the first rename; the diagnostic is whole without it. The user
asked what it was for; removal chosen over pointing at the mechanism doc.

**A proposed or landed text names the file it goes into** (v97), at the user's word.

**Testing an amendment before it lands** —
[q-0037.0012.0009](../questions/q-0037.0012.0009-how-is-an-amendment-to-an-instruction-tested-before-it-lands-against-which-cases-chosen.md),
*Where it stands* accepted 2026-10-21. The user proposed the order of work — write the methodology
in three parts (dataset, subset, runs with no instruction / standing / new), discover how others do
it, plan the mechanism, cost it, and only then return. Each decision with its turn:

- *Two layers*, the corpus audit and behaviour cases — chosen because in five runs every catch was
  the audit's; *the audit layer must be tested by a second layer*, the user's addition, became
  planted contradictions and a background run.
- *The subset is the skill* — the user's: *the most obvious form of a subset is the skills*.
- *Cases along one chain* — I ranked the moments of drawing cases and put writing the rule second;
  the user: *isn't (в) the most obvious?* It is the gate, where the set is assembled; noticing is
  where the situation is cheapest to capture.
- *Several yes-or-no questions per case, never a scale* — the user remembered that a binary verdict
  had hidden an improvement (the speech bench's `/maintain` report, half as long, still five of
  five); the questions give the degree, each yes with its quote.
- *Four verdicts, staging through a host adapter* — from Harness², read again at the user's word.
- *The author is the session that noticed* — I proposed a fresh agent; the user: *why should the
  same agent propose the amendment?*, then *I cannot picture this in practice*, then *explain again
  why*. Under the second explanation both arguments proved weaker than presented: overfitting
  threatens through the keep cases, which the run supplies and the author never sees; the frame
  argument costs the noticing session's context. Left as a hypothesis, q-0037.0012.0009.0003.
- *A step of the self-amendment mechanism*, not its own mechanism nor part of `/skill-up` or the
  mechanism shape, neither of which keeps cases.

**The queue**: the product form first — *the document, the README and the meeting with the
harness*, the user's definition — then the testing family, then the dial.

## Principles derived, without a home yet

- **A clause cut on the claim that a check holds it stays until a test shows the check holds it.**
  Three of the first compression's cuts were wrong in exactly this way; the bare-ticket-id clause
  survived only because its test came back red. Recorded in q-0037.0012.0006's lean; its home is
  the self-amendment mechanism's doc once declared.
- **A fix case must fail on the standing text.** A case that passes on both sides can show only
  that nothing broke. Every behaviour case of the doc-rule bench was of that kind; the fix was
  verified only textually.
- **An example is not decoration when it carries the distinction.** Replacing the old examples of
  *A document informs* with *never what an agent does* brought back the RFC conflict; the examples
  had stated that a document acts through the skill that reads it.

## What was done

The [doc-rule bench](../research/doc-rule-bench/), five runs, results in `results/run-1.md` to
`run-5.md`: about 370 agent runs, some 23M tokens. Two discovery passes and the Harness² reading
are in q-0037.0012.0009's body. Rule failure 53 — a discovery filed and an align opened on it with
the person told nothing of what it found — registered and its amendment to `/discover` landed. Six
tickets minted, 01-0019.0020 to .0070, each answering a question under q-0037.0012.0009.

## What went wrong

- Three compressions in a row cut what something else was claimed to hold; the bench caught each.
- A first judge took an example of the id format for a ticket; corrected and re-judged.
- The bench's text copies were `.md` and the tree's checks read their installed blocks and straw
  dogs as its own; renamed `.txt`.
- I opened an align on discovery material the person had not been told (rule failure 53), and the
  user had to ask twice for plain words; *without ceremony, only the essence*.
- My additions to the queue were dated clauses appended to its body — part of what rule failure 66,
  registered by another session on 2026-10-24, names as the queue growing its history back.

## Open questions touched

- [q-0037.0012.0006](../questions/q-0037.0012.0006-which-sentences-of-the-entry-file-are-meta-rules-the-mechanism-shape-should-hold-in-its.md) — *A capable reader*, *Tier*, *Self-improvement* still unweighed.
- [q-0037.0006.0017](../questions/q-0037.0006.0017-does-the-leak-check-catch-a-ticket-named-by-a-bare-id-in-core.md) — an expected-failure test holds it.
- q-0037.0012.0009.0002 (types of failure and behaviour) and .0003 (a fresh author) wait on the
  family's first runs.
- Drift reported and not repaired: Q1's example calls name `q-0004`, read by some audits as core
  naming a question; skill-up's *Writing rules — to the mechanism shape …* is an authored sentence
  about another mechanism. The narrowing of R8, the recipient's fourth finding, waits as a proposed
  session; the first finding, `/plan` against itself, was never checked against this tree's text.

## What continues

The queue: [01-0060.0010](../tickets/done/01-0060.0010-what-the-path-shows-at-every-recall.md), then one
align on the front page and the README (q-0033.0008 with q-0037.0018.0005). The testing family
starts at [01-0019.0020](../tickets/01-0019.0020-one-amendment-is-tested-end-to-end.md), whose first
step is writing rule failure 53's case.
