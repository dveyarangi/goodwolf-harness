# 0068 — A tree carries the method's text its settings call for

- **record of** what happened

The session ran 2026-10-20 to 2026-10-25. It began on a sidenote about how a reply says that it
stops for the person, and went from there to making the whole decoration of a reply switchable,
then to settings as a part of the method, and built that as
[01-0010.0220](../tickets/done/01-0010.0220-a-tree-carries-the-methods-text-its-settings-call-for.md).

## Decisions

**A stop is said as the act** —
[q-0037.0013.0005.0007](../questions/q-0037.0013.0005.0007-how-does-a-reply-report-by-the-agents-dial.md),
landed as v100 to v102. The user could barely read *At the dial, 🛠️ self-improvement=a rule*.
Four forms were weighed: the act in the person's words, the glyph alone, the host's next-step box,
and a gloss beside the old form. The act won; the user then struck its two variants, one for the
dial and one above it, as bloat — *не надо различать случаи остановки* — and took ✋ for both.
🛠️ left the contract for 🐛, which the user placed only on debug items that carry no glyph of
their own. The first explanation of the four forms was not understood; a second, by example, was.

**The skills row** — v105: under `debug=on` the head table names every skill a turn read, with
the gear the user chose. Commits already showed under debug alone; nothing changed for them.

**A tree carries only the method's text its settings call for** —
[q-0037.0006.0026](../questions/done/q-0037.0006.0026-how-does-a-project-choose-which-of-the-methods-text-its-tree-carries.md),
decided in five passes. The user's proposal: the whole decoration switchable, and its installed
text removed when off, to save tokens, by external variables marking what installs. The turns:

- A setting-per-mechanism shape was offered first; the user answered that a setting is often a
  component of one mechanism — whether a judge runs, which verification set — and proposed that
  each installable block state its own condition. That shape contains the first and dissolves a
  separate variables mechanism; it was taken.
- The declaration was first put in the mechanism's doc, which the user could not follow — *разве
  документ механизма может держать настройки?* Three things had been called by one word: which
  keys exist, which value the project chose, where a key fires. Told apart, the declaration went
  to the rules file of the mechanism the setting belongs to — `debug` is debugging's, by the
  user's correction — and any mechanism's rule may use it.
- A consolidated table at tier 1 was refused for its cost; it is reached through `/harness` at
  two occasions, a setting changed and the set-up asked about.
- *Who may change a setting depends on the setting*: the declaration carries `set by`, a rung or
  the person.
- *The agent is the interface, never the file* — a hand edit is allowed, rare, and drift, repaired
  the moment it is noticed. The user called it a product principle; it landed as G3 in
  [the product document](../product.md).
- *Sync* was asked about and turned out to be the installer's own run; the word was dropped.

**At the plan** the RFC named three contradictions, each decided: no declared setting existed for
the live criteria, so the debugging mechanism came to the shape with the ticket, declaring
`debug` and owning the announce line, and the dial from the table waits for the ladder
mechanisms; the wake's line goes through the hook's wrapper, which the always-on mechanism now
claims; the edge record is committed by hand with a pointer to the renderer in the table's place,
since R4 forbids committing the index — the user's own answer, neither of the two offered.

**A criterion names its judge as a role** — the ticket shelf's *Acceptance criteria*. The criteria
had said *read by the person*, and when another session verified the ticket and handed the close
here, this session put the close to the user. The user: the close wanted verification, not their
word. Registered as rule failure 65, the mirror of 64.

## What was built

The installer reads tables by header, a settings declaration, `when` conditions and the local
file's values; renders a target from the rules whose conditions hold and removes a block none
calls for; re-renders a block that differs by the settings alone without `--overwrite`; runs over
every source, changes a value by `--set`, renders the table by `--settings`, and gives the hook one
line. The wrapper hands that line to the store's hook, which prints it last at a session's start.
The debugging mechanism, its rules file, doc and skill; S4 conditioned on `debug`; the settings
edge record; the contract in [the architecture](../architecture.md), *A tree carries the method's
text its settings call for*; *Setting* in the method's glossary.

## What went wrong

- Patches written through a shell heredoc broke on escaped newlines and on CRLF files, three times;
  each was caught by the next test run, never by reading.
- The counters line was once copied from the previous window, losing a `(-1)`, and once 🐺 stood
  for 🐕; the window sat in a saved file the reply did not open.
- Twice a question was put to the person that was not theirs: a new ticket's place in the queue
  (rule failure 61, landed in `/ticket`), and a close another session had verified (rule failure 65).

## Principles without a home yet

- **A setting's name, values and way of being set is a product seam**, the user's words. The
  declaration is its one home and the settings edge record its account; the product document
  names only G3, not the seam itself.

## Open, and where it stands

- [q-0037.0013.0005.0007](../questions/q-0037.0013.0005.0007-how-does-a-reply-report-by-the-agents-dial.md) —
  the stop's form is landed; its ticket, 01-0020.0020, waits on a judge reading a live session.
- [q-0037.0009.0021](../questions/q-0037.0009.0021-which-mechanism-owns-how-a-reply-is-laid-out-for-its-reader-debugging-or-interaction-and-what-does-it-own.md) —
  the debugging mechanism now exists with one rule; the rest of what debug shows moves under
  [01-0016.0020](../tickets/01-0016.0020-what-debug-shows-is-installed-not-read.md), unblocked.
- The dial from the settings table waits on
  [q-0037.0010.0002.0005](../questions/q-0037.0010.0002.0005-what-does-the-practice-mechanism-own.md),
  the ladder mechanisms' declaration.

## Drift met, not repaired

`docs/rule-failures.md` holds two entries numbered 61 and two numbered 63. This session's 61 was
written first, 2026-10-23 02:45; the other 61 and the second 63 came later from other sessions.

## What continues

01-0016.0020 is the next step on this line: move the remaining debug-only texts into the
debugging mechanism's conditioned rules, so a tree at `debug=off` carries none of them.
