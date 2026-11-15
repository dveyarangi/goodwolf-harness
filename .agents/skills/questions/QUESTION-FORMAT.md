# Question format

This shelf owns the shape of the store's records: an entry and its body.

## An entry

One file in `docs/questions/`, named `<id>-<slug>.md`, the slug made by the script from the
question's words as it was opened — so phrase a question short — and kept for good: a reword
changes the title alone. Tier 2: read by the script, and by a person through
the questions skill. It stays where it is, closed or not, and is never deleted; once it and every
question below it is neither open, deferred nor suspect, and no question held open depends on any
of them, it is finished, and the window leaves it out.

```md
# q-7f3k2a Which package manager do we use?

- **record of** what happened
- **part of** q-m4x2pq
- **depends on** q-c3vn5h, q-r2zt6k
- **state** closed:decided, suspect
- **owner** [01-0090.0030](../tickets/01-0090.0030-the-outcome-it-names.md)
- **answer** [the ADR](../adr/0009-the-decision-it-records.md) — the user, 2026-09-28
- **realizes** A7 "The question store"
- **rung** development: load-bearing
- **lean** the flat directory, for insertion cost
- **asks** the person, 2026-10-26
- **opened** 2026-09-27T08:14:03Z
- **struck** 2, last 2026-10-02T19:40Z

## Where it stands

…
```

**The parts** are the script's to write, never a hand's. Every part but **state** is optional, and
a closed entry carries its **answer**. **realizes** is the trace link, kept as written and never
resolved; a question without one carries its nearest ancestor's. **rung** is the question's
highest rung on each ladder it touches, `<ladder>: <rung>`, comma-separated, each ladder once; the
rungs' names and order are each ladder's. **asks** is `the person, <date>`: an open question
waiting on the person's decision, shown by every wake until it closes; a close ends it, a merge or
a supersession carries it to its open target. **opened** is the second the question was opened;
siblings stand in its order. The state is `open` or
`closed:<kind>`, with `, suspect` after it at most.

**The id never changes**: `q-` and six characters of lowercase base32, a letter and a digit among
them, given when the question opens. Its place is its **part of** alone, so a move rewrites that
part and nothing else, and a reword changes the title alone.

## The body

It follows the parts after one blank line, written by hand with the edit tools; the script keeps it
as it found it. A line in it shaped like a part is not one. It runs in three parts, in this order:

- `## Where it stands` — the question as it stands, for a reader arriving cold: the problem, the
  shape agreed so far, what is open. Rewritten whole whenever a decision lands; it holds no
  history. A question a ticket answers carries it.
- `## Decisions` — a decision with nowhere to land yet is an item, `- ` or `N. `, and takes
  `→ <link>` to its home when it lands. A decision that refused an alternative names it and why,
  after `Not:`. The script reads the list at `close` and in the check; prose between the items and
  a fenced block hold no decision.
- Dated evidence — the case, a discovery's material, an impact — each under its own heading with
  its date, appended and never rewritten.

