# Question format

This shelf owns the shape of the store's records: an entry, its body, and the sessions folder.

## An entry

One file in `docs/questions/`, named `<id>-<slug>.md`, the slug made by the script from the
question's words — so phrase a question short. Tier 2: read by the script, and by a person through
the questions skill. It moves to `docs/questions/done/` with a wholly closed subtree nothing open
depends on, a deferred or suspect entry counting as open; it is never deleted.

```md
# q-0090.0003 Which package manager do we use?

- **record of** what happened
- **part of** q-0090
- **depends on** q-0070, q-0080.0001
- **state** closed:decided, suspect
- **owner** [01-0090.0030](../tickets/01-0090.0030-the-outcome-it-names.md)
- **answer** [the ADR](../adr/0009-the-decision-it-records.md) — the user, 2026-09-28
- **realizes** A7 "The question store"
- **rung** development: load-bearing
- **lean** the flat directory, for insertion cost
- **struck** 2, last 2026-10-02T19:40Z

## Where it stands

…
```

**The parts** are the script's to write, never a hand's. Every part but **state** is optional, and
a closed entry carries its **answer**. **realizes** is the trace link, kept as written and never
resolved; a question without one carries its nearest ancestor's. **rung** is the question's
highest rung on each ladder it touches, `<ladder>: <rung>`, comma-separated, each ladder once; the
rungs' names and order are each ladder's. The state is `open` or
`closed:<kind>`, with `, suspect` after it at most.

**The id is the place**: a root is `q-NNNN`, a child its parent's id and one more position. A
re-parent renames the moved question and everything bound to it, so an id seen earlier may be gone:
draw the window again. A reword changes the words and the file's name, never the id.

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

<straw-dog question="q-0037.0006.0015">
## The sessions folder

`docs/questions/sessions.d/`, shared by all sessions, one file per session named by its tag and
holding its one row: `<tag> running|ended <YYYY-MM-DDTHH:MMZ> <q-id>|- [<q-id>,… up to four]` —
its tag, whether it runs, when its line last changed, its current question or `-` before it has
one, and its recent ones. Tier 1 through the window and the wake's read. What removes a row: kept
by design — an ended row lets a later wake offer to resume.
</straw-dog>

<straw-dog question="q-0037.0017">
**A silent row ends at the next wake.** Every wake ends each other running row whose session
nothing has seen for three hours, and says nothing of it. A session is seen while its messages
reach a hook — the window drawn, or Cursor's prompt hook — or it writes its row; the next message
turns an ended row running again.
</straw-dog>
