# Session 48 — the queue copies nothing

**2026-10-10.** Claude Code in the desktop app, one conversation, `fcfe212c…`. Entry contract v53
at the start; v54 and v55 raised here, v56 and v57 by parallel sessions, v58 in flight in another
when it ended. It opened with a `/recall` whose candidate was
[01-0011.0110.0040.0010 every-record-shows-what-it-is-a-record-of](../tickets/01-0011.0110.0040.0010-every-record-shows-what-it-is-a-record-of.md);
the user turned instead to the drift the recall reported, and the session ended with the queue
holding no copy of anything a ticket says.

## What was decided, and what chose it

### The completed-step narrative goes whole — q-0024.0009.0003.0003

- The recall found the queue's `Completed step` four sessions stale. Asked which task fixes it,
  none did: the parent [01-0011.0110.0040](../tickets/01-0011.0110.0040-the-ticket-and-the-queue-are-what-comes-next.md)
  planned *one pointer at the last step*, and none of its three slices carried the bullet.
- First recommended: render the pointer. The user asked *who reads completed step? and isn't it
  redundancy?* Nobody did — no script, no skill; `/recall` takes the last session from
  `docs/sessions/`. The pointer of 2026-10-07 was revised on that evidence: the line went whole,
  from the queue and the arrival state, and the format says the queue keeps no account of steps
  done. The user chose a separate edit. Its home is the ticket format; the reasoning sits in
  [q-0024.0009](../questions/q-0024.0009-what-kinds-of-written-thing-does-a-tree-hold-and-which-of-them-does-maintain-hold-in-agreement.md).

### The ticket list is rendered, never copied — 01-0011.0040

[The ticket](../tickets/done/01-0011.0040-the-ticket-list-is-rendered-never-copied.md) holds the
decisions; how they turned:

- **Committed or not.** The ticket's case for committing the table rested on *this harness has no
  wake hook*, untrue since session 46. R4 of the mechanism shape, an index rendered on request and
  never committed, stood.
- **Whether anyone reads the table.** The user: *I don't look at the table at all either.* I
  recommended removing it with no renderer. The user corrected it: *how is a priority chosen, or
  existing tickets found for some task to extend them? I don't think nobody reads it — the
  process just isn't written anywhere.* Two readers, unwritten: whoever orders the queue, and
  whoever is about to mint. So the list exists, on request, and P12 tells both to read it; the
  ordering method stays q-0027's, the finding method
  [q-0024.0011](../questions/q-0024.0011-how-does-a-new-task-find-the-live-ticket-it-belongs-to-before-another-is-minted.md)'s.
- **A recipient's table.** The user: *in a foreign project the person will look at their own
  table as they already do; either you tell them what is happening, or the file list is visible —
  that is enough.* No migration; a note waits on the edge-line question, q-0018.0020.0002.0001.
- **The list's form.** Shown before building, at the user's request. The question column a link
  by id and slug — *the slug is descriptive enough*; the title column named `Title`, not
  `Outcome`, so it is not taken for the header's field.
- **`Last updated`** goes with the copy: the log holds when the hand-written part moved.

### A slug changes when it no longer says what the ticket is

- The format's *Never changes. Cite by this.* — the user: *irrelevant since the day the mover
  appeared; cite-by-this is covered by the rule we install.* The line now reads *slug — what the
  ticket is.*, and a sentence elsewhere in the shelf saying the filename never changes went with
  it during the implementation.
- Ten live tickets and the shared-harness spec were renamed to slugs drawn from their titles, the
  pacer's title with them (*Each turn knows its next step*); this ticket was renamed at the end of
  its own align. The mover repairs link targets, not link text, so link texts in live records were
  rewritten by hand; snapshots keep their old text.

### Two rules amended on the user's word — rule failures 17 and 29

- *I have no idea what these numbers are — why don't you write their slugs anywhere? did we lose
  that rule?* P9 had been read across the conversation rather than per reply, and a table cell
  not as a mention. Now: every reply and every record, a table's cell included, the id written
  whole. Entry 17 struck; v54.
- *Why an empty tangle?* *Debug or not, a row each* had been read as *each table, always*. Now: a
  table only where it has a row. Entry 29; v55.

## Principles derived, with no home yet

- **Look for an output's readers in what is done, not only in what is written.** I declared the
  table readerless from the scripts and skills; the user found two readers in practice. The
  mechanism skill says every output has a reader or a stated reason for none; it does not say that
  an unwritten reading is a reader whose process is missing.

## What was done

- `tickets.py --list`, P12 installed in `/recall` and `/ticket`, P8 retracted, the queue's table
  and every copy instruction removed, the architecture's delivery-state sentence landed; planned
  over four validation passes, implemented test-first, verified at 664 tests, closed by
  `/maintain`.
- Two maintenance passes: seven levels marked, then edge's two once its building sessions had
  committed.
- Questions opened: q-0024.0011, q-0024.0009.0003.0004 (what the queue's file is called now it
  holds no status), q-0021.0001 (which test holds the hook to exiting clean — the hosts record's one
  unguarded promise). q-0020 decided.

## What went wrong, and what it taught

- **The `/ticket` anchor.** P12 was first planned under `## Process`; the second pass found the
  installer writes at the end of an anchor's section, which would have put *read before minting*
  after minting. It sits at step 1.
- **A stray row that did not exist.** The first plan pass reported a duplicated queue row; it was
  a `sed` printing from mid-file. Read a file's structure before reporting one.
- **A concurrent commit took an uncommitted edit.** The edge session's `a87fd43` swept in this
  session's `TICKET-FORMAT.md` edit. The content was right; the provenance is noted in `e67c969`.
  It is q-0032's case.
- **Messaging another session was overpromised.** Desktop sessions are reachable by title and a
  short handle; the store knows sessions only by the host's id, and a UUID v7 id has belonged to
  Codex and Cursor here. Recorded in
  [q-0034](../questions/q-0034-what-is-a-session-to-the-harness-and-which-mechanism-keeps-its-lifecycle.md).

## Open questions touched

- **q-0024.0011** — how a new task finds the live ticket it belongs to; P12 gives the occasion,
  not the method.
- **q-0024.0009.0003.0004** — the queue's file, heading and the installer's constant still say
  *delivery status*.
- **q-0021.0001** — no test asserts the hook's exit status.
- **q-0034** — a session row carries no host and no address.
- **q-0027** — how the queue is ordered; P12 reads the list before it.
- The front page's *15,000 of work queue* figure, a straw dog bound to q-0024.0009, is stale twice
  over and waits to be measured afresh.

## What continues

The queue's candidate, unchanged:
[01-0011.0110.0040.0010 every-record-shows-what-it-is-a-record-of](../tickets/01-0011.0110.0040.0010-every-record-shows-what-it-is-a-record-of.md),
its `/plan` first. Its sibling
[01-0011.0110.0040.0020 a-decision-lives-in-the-question-until-it-lands](../tickets/01-0011.0110.0040.0020-a-decision-lives-in-the-question-until-it-lands.md)
is independent of it.
