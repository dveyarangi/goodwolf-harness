# Session 50 — a pair, a direction, a detector

- **record of** what happened

2026-10-10 → 2026-10-11. Opened on the queue's candidate, the record-of mark, and ended on a
rethink of what the kinds of record are for: drift is seen where a record is paired with its
thing and something notices them come apart, not where a label is stamped.

## Decisions, and what chose them

**Every live record marked at once, the checks strict at once** *(the plan of
[01-0011.0110.0040.0010 every-record-shows-what-it-is-a-record-of](../tickets/done/01-0011.0110.0040.0010-every-record-shows-what-it-is-a-record-of.md))*.
The ticket said *at next touch, by `/maintain`*; weighed against it, a check cannot tell an old
unmarked record from a new one, so *none is reported* would go unproven. The 193 question entries
were re-rendered through `questions.py`'s own writer, the tickets and the queue marked by hand.

**A closed ticket and RFC are marked `what happened`, by the mover.** First put as *should the
mover rewrite it*, answered yes on my recommendation; then the user asked *what does it mean, when
did we agree?* — the record of a plan left in `done/` would tell an agent reading it to pull code
toward it. Kept once explained. P3 was amended to name the exception, then reverted at the user's
*why P3 at all, it worked*: the mark is none of the checkbox, status, date or prose P3 keeps the
mover from.

**A mechanism's doc stays `what must always hold`**
([q-0024.0009.0005](../questions/done/q-0024.0009.0005-is-a-mechanisms-doc-a-record-of-what-must-always-hold-or-of-what-exists.md)).
The user opened it: *docs change from time to time and are not the source of truth; they describe
the existing state*. Taken first as `what exists`, which forced the glossary's *never edited by
hand* to go (*the glossary spoke without thinking — we have no mechanical way to make docs*).
Then the user: *the doc leads its instructions, no? sometimes leading, sometimes following is no
place to be*. What turned it: a change by decision moves doc and instruction in one landing, and
drift is the instruction moving without one — so the doc leads, by decision. The fear that the
name reads as *never edit* was tested by a cold read: three agents, one per label set, all read all
four files as meant. `what decides` was weighed and left: after *record of* it names the one who
decides. The names stay.

**The mark says how a record is treated, not what it is paired with.** The user: *I do not see how
these labels give a direction — they do not look relative*. A unary label has no second end; the
spec had asked every record to name its referent, and the slice had dropped it. Direction and drift
go to pairs with a detector.

**[q-0024.0009.0006](../questions/q-0024.0009.0006-how-is-a-record-paired-with-the-thing-it-is-of-so-that-drift-between-them-is-noticed.md)'s
seven decisions**, the align's account in its body. The ones a reasoning turned:

- *Only its own parts*, so one edit makes one doc due.
- *In another's file a mechanism owns only what it installs there* — the user: *watch the
  installed parts; parts lying in others' files should be made installable*.
- *The shape installs its meta-rules* — the user: *the mechanism of mechanisms is core enough to
  hold meta-rules; it alone holds the true meta-instructions, instructions on making instructions.
  Occam is no meta-instruction but a meta-principle — meta too, but for everything.* This reversed
  the format's *a meta-rule is never injected*, by the user's own R7 argument (*otherwise you make
  it tier 3*). Landed in the method glossary's *Meta-rule*.
- *Two levels, `parts` and `output`* — the user: *`rules` is a subtype of parts, no? why is the
  skill output?* `rules` is the mechanism shape's `output`, read one mechanism at a time.
- *The clock names what moved*, rather than a note behind each mark: twelve levels marked *nothing
  to change* this session, each told only *its doc, rules file or skill moved*.
- *Three outcomes of a due pair*, by whether a decision stands behind the move: A1 as written
  would revert a script a landed decision moved.

## Principles without a home yet

- **Seeing drift takes three things at once — the pair, the side that leads, and what notices.**
  A label gives at most the second. Held as the body of q-0024.0009.0006; its home once the slices
  land is the maintain mechanism's doc.
- **Make the right act cheaper than the stamp.** A re-check told which files moved reads them; one
  told only that something moved guesses or stamps.

## What was done

- [.0040.0010](../tickets/done/01-0011.0110.0040.0010-every-record-shows-what-it-is-a-record-of.md)
  landed and closed: `- **record of** <kind>` in mechanism docs, tickets, the queue, question
  entries and RFCs, held by `mechanisms.py`, `tickets.py`, `questions.py`; the mover marks a closed
  pair. Its line for recipients is in q-0018.0020.0002.0001's body.
- A `/discover` pass, kept whole: [what a record drifting from its thing is an instance
  of](../research/discover-record-drift-2026-10-10.md).
- Three slices minted from the align — `.0060`, `.0070`, `.0080` — and the queue ordered
  *(the user)*. [.0070 the-clock-names-what-moved](../tickets/done/01-0011.0110.0070-the-clock-names-what-moved.md)
  landed and closed: a second table of per-file fingerprints beside the marks.
- Two maintenance passes; maintain's `output` is the first mark to keep its files.

## What went wrong, and what it taught

- **A label shipped before its purpose was asked.** The record-of slice built marks and a check
  that holds the mark to its format — a check of the label, not of drift. The user's *the whole
  idea is to see drift, not to hang labels for show* came after the landing. Ask what a mark is
  for before building its check.
- **I overstated the clock.** I said it watched a doc against its scripts; it watched the doc
  against the meta-rules and the records against the doc. Read the surface before describing it.
- **Two decisions put on my recommendation needed explaining afterwards** (the mover's mark, P3).
  A recommendation the user cannot read cold is a question put badly.
- **Flaky tests under load.** One full run failed six tests, another one; each passed alone. Other
  sessions were running beside. It belongs to
  [q-0021](../questions/q-0021-do-the-tests-catch-the-regressions-their-names-promise.md)'s ground.
- **The host resumed this conversation under a new id** (`local_…`); the questions mechanism's
  change of the same day keyed it on the app's id, and it found itself registered.

## Open questions touched

- **q-0024.0009.0006** — the align done; `.0060` and `.0080` remain, `.0080` owning it.
- **q-0024.0009.0006.0001** — `.0060`'s: the shape installs its meta-rules.
- **q-0026.0006** — which other sentences of the entry file are meta-rules (*a capable reader*,
  *tier is paid*, *self-improvement*, *a document informs*).
- **q-0024.0009.0003.0001.0001** — edge records, mechanism evidence and records without a format
  carry no mark.
- **q-0024.0009** — the kinds stand; drift moves to pairs.

## What continues

The queue: [.0020](../tickets/done/01-0011.0110.0040.0020-a-decision-lives-in-the-question-until-it-lands.md),
another session's; beside it [.0060 the-mechanism-shape-installs-its-meta-rules](../tickets/01-0011.0110.0060-the-mechanism-shape-installs-its-meta-rules.md),
its `/plan` first — the entry file it edits now holds v60, landed. The six `rules` levels the clock
reports due moved with v59 and v60, now landed: the next `/maintain` re-checks them against that
text, and their marks keep files from then on.
