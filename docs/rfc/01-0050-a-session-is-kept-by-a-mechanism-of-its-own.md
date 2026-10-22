# A session is kept by a mechanism of its own — implementation plan

- **record of** what it intends to become

**Authored:** 2026-10-22
**Last amended:** 2026-10-22 — second pass: the state, the ended row's time, the commit anchor, the contract bump

Implements [01-0050 a-session-is-kept-by-a-mechanism-of-its-own](../tickets/01-0050-a-session-is-kept-by-a-mechanism-of-its-own.md).

## What governs it

[q-0037.0017's six decisions and its accepted *Where it stands*](../questions/q-0037.0017-what-is-a-session-to-the-harness-and-which-mechanism-keeps-its-lifecycle.md#where-it-stands):
a session is one chat from its `/recall` to its `/conclude`, known by the host's steadiest id; a
mechanism of its own keeps it, machinery and not method, with the two skills, the row gone seven
days after its end and the session record, its code in a script of its own, every rule on how
sessions interact its own. [The shape](../../.agents/skills/mechanism/SKILL.md) and
[its format](../../.agents/skills/mechanism/MECHANISM-FORMAT.md): a doc, a rules file installed
where read, records declared beside the skill, a part's claim at its head, the inception's six
steps. [Interruption and recovery](../architecture.md#interruption-and-recovery): nothing is
locked, a write refuses interference; [the question store](../architecture.md#question-store):
each session replaces its own row and no other, a rename the one write touching every row.
[The sessions folder's decision](../questions/done/q-0036.0004-how-do-session-lines-written-at-once-all-survive-when-the-harness-locks-nothing.md#decision):
one file per session, the single file from before carried over by copies that never overwrite.

## The shape

**One script, one direction.** `sessions.py` (`# Mechanism: session`) owns the row's whole life;
`questions.py` imports it and `sessions.py` imports nothing of `questions.py` at module level: what
it needs of the store — the entry index for a position's check, the shared types `Refused`,
`Diagnostic`, `Finding`, `Skipped`, `WriteInterrupted` — it takes as arguments or imports inside
the function that uses it, as `questions.py` already does with `tickets`. The session's sign of
life, the window-memory path keyed by tree and tag, moves with it: it is where a session is seen,
and the window reads it through the import.

What moves, by its lines today: the `Session` row, its regex and form, the folder and the single
file's names, the silence constant; reading the folder with the single file's carry-over, writing
a row through a staging file; registering, the sign of life, ending the silent, ending at the
conclude, turning a reopened session running again; the host table, the tag, the hook's session
half; the rename's touch on rows; the rows' check; the wake's list of sessions. What stays:
the window and its fingerprint, the wake's read of the store — most struck, deferred, straw dogs
due — and the `at` call's write of the position, which asks `sessions.py` for the row and hands
back the moved one.

**The hook entry stays `questions.py --hook <host>`**: the hook wiring shelves, `hook.sh` and the
recorded interpreter are the questions mechanism's parts, relied on by the session mechanism, and
no recipient's host file changes. The hook's session half — registered now or already, running
again, the silent ended, the gone removed — is one call into `sessions.py`; its window half is
the questions mechanism's as today. `--wake` stays on `questions.py` for the same reason: it draws
the store. `--end` moves: `sessions.py --end --session <tag>`, and `questions.py --end` goes.
`sessions.py --check` is the rows' maintainer check — the form of each row, a position naming no
entry, a running session on a closed question — and `questions.py --check` stops reporting rows.

**Gone after seven days.** The same walk that ends the silent rows removes each row that reads
`ended` and whose time is seven days or older; a running row is never removed. For that count
to run from the session's end, the wake that ends a silent row writes the time it was last seen
as the row's time — the later of the row's own and its sign of life — where today it keeps the
row's time, which is the last `at` and may be days older than the session's last message. The
conclude's `--end` already writes the time of ending. A removal Windows
refuses because a reader holds the file is left, as the carry-over leaves the single file, and
the next wake removes it. The wake's read lists running sessions only. A session whose row is
gone and whose host returns under the same id is registered anew, with no position: the person or
the agent places it, as Q2 says.

**The declaration.** `.agents/mechanisms/session/session.md` to the format: two `instruction`
bullets, `/recall` and `/conclude`; `state` installed — the harness ships it with core and removes it
with core, as every mechanism but the shape; parts: the two skills, the doc, the rules file, the
script, its tests; relied on: the hook wiring shelves, `hook.sh` and the question script for the
store it reads and the hook entry it answers (`questions`), the mover (`ticket`),
the shape check and installer (`mechanism-shape`), the test harness. Moments: a session starts;
is seen; falls silent; is reopened; concludes; is gone; rows a wake changed in other sessions'
files are committed; a reply's 🪢 table; a recall re-ranking nothing another session is on; a
commit holding one session's work. Not yet: sessions beyond one working directory
(q-0037.0017.0005), the position across a resume under a new id a host does not keep
(q-0037.0017.0004), a lock and a role (q-0037.0017's seams, bound to q-0037.0005 for the role).
Nothing retires it. Graded: four yes-or-no tests, pre-registered below.

The format admits the second `instruction` bullet: its straw dog on one bullet, bound to this
question and due with this ticket, is rewritten to *one bullet per skill the mechanism owns*;
the shape check reads them as a list and matches a skill against any; a mechanism owning two
skills with one bullet is reported. The shape's evidence already says the field becomes a list
when the first such mechanism is declared.

**The records**, declared in `/conclude`'s skill, where the session record's shape already is:
the row — one file per session under `docs/questions/sessions.d/`, named by its tag, holding
`<tag> running|ended <YYYY-MM-DDTHH:MMZ> <q-id>|- [<q-id>,… up to four]`; tier 1 through the
window and the wake's read; gone when it reads ended and its time is seven days or older — and the
session record — one file under `docs/sessions/`; tier 2; kept. The sessions section leaves
`QUESTION-FORMAT.md` whole, with the format's opening line reduced to the entry and its body.

**The rules file**, `session.rules.md`, five rules, each installed under the target's
`## Installed from other mechanisms` where the target has it:

- **S1** → `/recall`: the wake's read is the session's — *Start from the wake's read, the one
  the host's session-start hook put in your context, or `questions.py --wake --session <tag>`
  with the tag that read named; a bare `--wake` registers a new session, and is for a host whose
  hook registered none. Take from it where the other sessions stand, and re-rank nothing another
  running session is on.* Q2 keeps what is the store's: what is suspect, which deferrals and straw
  dogs are due, the position placed with `at`.
- **S2** → `/conclude`: *As the conclude's last act, run `sessions.py --end --session <tag>`.* Q3
  keeps the leans.
- **S3** → `/maintain`: F5, from the skill's body into the rules file — *Commit with the pass each
  row a wake ended or removed in another session's file under `docs/questions/sessions.d/`; a
  file whose row reads `running` stays out* — and R1's duty: *check the rows with
  `sessions.py --check`*. The verification set in the local rules file gains that check.
- **S4** → `AGENTS.md`, under `## General rules`, after the questions and ticket blocks: the 🪢
  table's two sentences, moved verbatim from the reply-layout paragraph, which keeps its pointer
  that the 🪢 table opens the reply. The paragraph's straw dog on q-0037.0009.0021 stays around
  what remains; the block carries no wrapper, since the rule is decided.
- **S5** → `/commit`: *Commit the work in the current session only; another session's changes may
  be work in progress, and in doubt ask the person* — from the skill's body, anchored on the line
  the local block already uses there: the installer places a mechanism's block before the local
  block in the same section, so the project's answer stays last.

The architecture's two paragraphs on the sessions file under *Question store*, one wrapped on
q-0037.0017 and due, become one: the row is the session mechanism's, each session writing its
own and the wake alone touching another's, with a link to the doc; the *Deferred decisions* line
giving the pacer session resumption is struck as what this mechanism now holds. The questions
doc loses its three session moments and the sessions-folder output, gains `sessions.py` under
*relies on*, and its *not yet* on the folder moves to the session doc. Both skills open with
`Mechanism: session`. The painted-door rows for the folder and the single file in the shape check
stay, their comment naming `/conclude`'s declaration, bound as before to q-0037.0010.0004.

**The seams**: the row's form takes no new field. A lock and a role are named in the doc's *not
yet* rows and nowhere in code.

## Stages

Each stage leaves `mechanisms.py --check`, `inject_rules.py --check`, `tickets.py --check`,
`questions.py --check` and the suite green, and is one commit: every other session's hook runs
this file at its next message, so no commit leaves the script half-moved.

1. **The shape admits two skills.** Red: a declaration with two `instruction` bullets, both
   resolving, passes the header check; a mechanism whose doc names one skill while a second skill
   claims it is reported; the index renders both. Green in `mechanisms.py`, MECHANISM-FORMAT's
   bullet rewritten, the shape's evidence noting the first case.
2. **The script, behaviour unchanged.** `sessions.py` carved out with the functions named above;
   `questions.py` imports it; `--end` answered by both for this stage alone, the questions one a
   delegate. `test_sessions.py` takes the nine session classes — 65 tests — with their helpers,
   calling `sessions.*` where they called `questions.*` directly; the fixtures keep writing the
   single file, so every one of them proves the carry-over still. The suite's count is unchanged.
3. **The declaration and the rules.** The doc, the evidence — its first paragraph naming this
   ticket, its count: 125 ended rows in this tree's folder at inception, the prior violation the
   removal clears — the rules file installed with `inject_rules.py session --install`, the
   questions rules Q2 and Q3 amended and re-installed with overwrite, F5 and the commit rule
   lifted from their bodies, the 🪢 sentences moved, `Mechanism: session` on both skills, the
   format and the architecture edited, `questions.py --end` removed, the entry contract bumped
   with its line in the findings record. Red first: the shape check
   reports the session doc until its parts resolve; the installer refuses until every target
   carries its block.
4. **Gone after seven days.** Red: a wake removes a row ended eight days ago and keeps one ended
   six; never a running one; says nothing of it; its read lists running sessions only; a session
   whose row is gone registers anew under the same id; a removal the file system refuses is left
   and reported in the hook's context line, not raised. Green in `sessions.py`. The first wake in
   this tree after it lands removes the rows, and `sessions.py --check` after it reports no row
   ended before 2026-10-15; the number removed goes to the evidence.

## Impact

**Impact.** `questions.py` loses some 600 lines to `sessions.py`; `test_questions.py` loses
nine classes to `test_sessions.py`; the questions rules file, doc and format; `/recall`,
`/conclude`, `/maintain`, `/commit` and the entry file gain a `session` block each, the entry
contract bumped; `mechanisms.py` and MECHANISM-FORMAT for the second bullet; `architecture.md`;
the local rules file's verification set. Every recipient takes the new script, the moved blocks
and the removal at its next update; its host files do not change.

**Hidden edges.** Three sessions run in this checkout while the script moves: the hook never
fails the host, a problem becoming a line of context, and each stage is one commit, so the window
between a half-moved script and its tests is a commit's. A silent row ended with its old time
kept would go seven days after its last `at`, not after its last message: hence the ending writes
the last-seen time, a change to the silence rule's *time kept* put to the person. A reopened chat after seven
days registers with no position and the wake says *registered now*; the rule to run `/recall`
first stands and costs one recall. The shape's painted doors still hold the folder's path, since
record declarations are not parsed. A Windows reader holding a row file defers its removal by one
wake. The desktop app's conversation id is the row's key; a host that keys on nothing steadier
than its process id loses the position on every reopen, which q-0037.0017.0004 holds.

**Leave alone.** The entries and their check; the window, its fingerprint and the counters; the
hook wiring, `hook.sh`, the interpreter record; the carry-over of the single file, which moves
unchanged; the session record under `docs/sessions/` and `/conclude`'s account of it; the
glossary's *Session*.

**Recommendation.** Proceed, in the four stages.

## What would show it working, graded by someone who did not build it

1. Open a chat, conclude it, reopen it the next day: does the wake say *already registered* and
   draw the window at its last position?
2. Leave a chat silent four hours and open another: does the first's row read ended, and the
   second's wake say nothing of it?
3. Eight days after a chat ended, open another: is the first's row gone, and the wake's list of
   sessions free of it?
4. Change the 🪢 rule in the rules file and re-install: does the entry file's block change and
   nothing else in it?

## Out of scope

- A lock or a role written in the row — the doc's *not yet* rows.
- A session's position across a resume under a new id where the host keeps none —
  q-0037.0017.0004.
- Sessions beyond one working directory — q-0037.0017.0005.
- Parsing record declarations, so the painted doors go — q-0037.0010.0004.
