# A session is a chat, and gets its mechanism

- **record of** what happened

**2026-10-20 to 2026-10-23.** Opened on a question about why the tree commits the rows of ended
sessions; ended with the session mechanism declared, built, verified, closed and maintained, and
with the first decisions on what a method is. Two rule failures on the way, both landed.

## Decisions, and what chose them

**A session is a chat, from its `/recall` to its `/conclude`** *(the user, 2026-10-21)*. The
agent offered three readings — a host process, a conversation known by the host's steadiest id,
a person's stint across chats — and recommended the second on the fact that the hook already keys
the row on the desktop app's conversation id. The user's words were sharper than the offer:
*session is a chat, starting with recall and ending with conclude*, which made the two skills the
session's two ends. Landed as the term in the method's glossary.

**`/recall` and `/conclude` are the session mechanism's; the pacer takes neither.** The agent
found the revision the user half-remembered: the pacer had been cut into tier-1 method rules
(the wake, the turn, the dial), the pathfinder as its ordering half (q-0037.0019), and the stepping
half left in q-0037.0013; and on 2026-10-11 the user had drawn the line *sessions are machinery*.
A session therefore runs the method but is not of it: the pacer is method and owns no machinery.
Two ownership questions closed with it.

**Modes refused** *(the user's own doubt, 2026-10-22; the agent's pushback)*. The user proposed
that the harness ships *agent modes*, the pathfinder in core and the rest swappable. The agent
pushed back: the unit of a mode is neither the turn nor the session but a stretch, and the loop
already names the two stretches — the align on a question and the delivery ring on its tickets —
readable from the store, set by nobody; what is set at start is a role (q-0037.0005). The user
let the modes go and kept the seam: *a session can be locked into one method by a setting, or be
free*. Landed as decision 3, the lock and a role seams in the row, nothing built.

**A method is the machinery of a root question; core is what methods share; a practice is what a
project swaps inside a method** *(the user, 2026-10-22)*, in a new question, q-0037.0006.0025,
with the roots each worked by a mechanism of their own — product for purpose, discovery for
landscape — so the agent's first cut, which put two roots into core, was wrong and corrected the
same hour. The user asked for a discovery on what the method actually is before the words land in
the glossary; a session of its own ran it ([session 0063](0063-20261022-the-method-seen-from-outside.md)),
nine families and what the one-line account leaves out, filed in the question. The glossary words
wait for that question's align.

**The rows are the session's records and leave the question format** *(the user, twice, 2026-10-21)*.
The agent proposed the removal rule into `QUESTION-FORMAT.md` twice; the user: *question-format is
not a place for instructions on a session's work … it describes a format*, then *why are you again
proposing to add this to the question format?* The answer was that the record is not the question
store's at all. Registered as rule failure 58, whose amendment to `/mechanism`'s *Records* landed
2026-10-23: a format declares *when a finished entry is gone — the condition, never the actor or
the moment*.

**The folder moves under `docs/sessions/`, named `rows`; a row is gone seven days after its end; a
silent row ended takes its last-seen time** *(the user, 2026-10-22)*. The last came from the plan's
second pass: the silence rule kept the row's old time, so a long session that never moved would
have been gone at the wake that ended it. The first came from the user mid-pass: *we should also
move sessions.d under sessions folder, no?*

**The code moves into a script of its own**, since a part is checked by the mechanism's name at its
head, which a shared file cannot carry. **Every rule on how sessions interact is the session's**
*(the user, 2026-10-22)*: six rules in its rules file, the 🪢 table among them, and on 2026-10-23
the recall rule too, out of the pacer's straw dog at the entry file's head.

## Done

[01-0050](../tickets/done/01-0050-a-session-is-kept-by-a-mechanism-of-its-own.md), one ticket in
four stages, each a green commit: the shape admitting two skills; `sessions.py` carved out one way
with the folder's move and this tree's 129 rows; the declaration, five rules installed, the format's
exit, the architecture and the questions doc pointing at the mechanism, the entry contract at v103;
the removal, the first wake taking 108 rows. Verified, closed as a pair, maintained; the plan is
[the RFC](../rfc/done/01-0050-a-session-is-kept-by-a-mechanism-of-its-own.md), the evidence
[session.evidence.md](../mechanisms/session.evidence.md). Then S6 and v104 to v108 — other sessions
bumped the contract meanwhile — and a second maintenance pass over the whole tree.

## What went wrong, and what it taught

- A rule was proposed in a reply without `/skill-up` or `/mechanism`: rule failure 50 struck
  again, and the entry file's 🧩 header now says *written through `/skill-up`*.
- An instruction was written into a format file, twice: rule failure 58, above.
- The declaration had to land a stage earlier than planned: the shape check refuses a script that
  names a mechanism no declaration lists it under. The carry-over's tests were written after the
  code, their red unobserved; the removal's nine were red first. Both in the evidence.
- A long align in one chat made the user say three times that they did not understand a decision
  table's row. The rows were terse pointers to things decided hours earlier; a decision row has
  to say the choice in full words, as the last reply did.

## Principles with no durable home yet

- A mode of working — investigating, delivering — is where a session stands in the loop, derived
  from the store, set by nobody; what is set at a session's start is a role. q-0037.0005 is the
  nearest home.
- Self-improvement creates methods and not only amends one: minting a method is a moment of the
  mechanism shape. q-0037.0006.0025's align should place it.
- A decision row in a reply says the whole choice, never a pointer to a thing decided earlier.

## Open questions touched

- [q-0037.0006.0025](../questions/q-0037.0006.0025-what-is-a-method-a-root-question-with-the-ring-that-works-it-and-the-records-it-keeps-and-what-is-a-practice-to-it-so-that-study-research-or-a-personal.md)
  — three decisions landed, the discovery filed; waits on its align, the glossary words.
- [q-0037.0006.0025.0001](../questions/q-0037.0006.0025.0001-which-root-a-research-or-study-method-asks-in-place-of-how-is-this-project-built-and-whether-the-structure-root-is-the-methods-to-word.md)
  — opened, reworded to the method; waits on the parent.
- [q-0037.0017.0004](../questions/q-0037.0017.0004-how-does-a-conversation-keep-its-position-when-its-host-resumes-it-under-a-new-session-id.md)
  and [q-0037.0017.0005](../questions/q-0037.0017.0005-how-do-running-sessions-reach-each-other-beyond-one-working-directory.md)
  — gathered under the closed session question; `not yet` rows of the session doc.
- [q-0037.0009.0021.0001](../questions/done/q-0037.0009.0021.0001-how-does-what-debug-shows-reach-a-tree-as-the-debugging-mechanisms-installed-blocks-and-how-does-a-tree-switch-it-on-and-off.md)
  — its ticket now carries the fork the 🪢 block forces: the debugging mechanism switches a block
  another mechanism owns, or the debug half of S4 becomes its own rule.

## What continues

The queue's order has [01-0010.0175 arrival-describes-what-it-finds](../tickets/01-0010.0175-arrival-describes-what-it-finds.md)
next; this chat's thread has the method question's align. The user did not choose between them.
The first step of the next session is `/recall`, which puts that choice.
