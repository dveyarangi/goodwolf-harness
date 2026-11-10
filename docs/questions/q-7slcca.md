# q-7slcca How do two copies of the question store merge, and where in git do their changes travel?

- **record of** what happened
- **part of** q-7ebz2f
- **state** closed:decided
- **answer** [q-7ebz2f, decisions 36 to 47](q-7ebz2f.md#decisions) — the user, 2026-11-09
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-09T07:51:24Z
- **struck** 1, last 2026-11-03T13:30Z

Opened 2026-10-31 from decision 29 of
[q-7ebz2f](q-7ebz2f.md):
across machines, copies of the store that merge, carried by git; one machine the case of one copy.

## The problem, 2026-11-03

What is merged, by which rule, and where in git a copy's changes travel — so that one machine's
store is built now with a seam a second machine and a cloud session need not reopen.

What stands, read from the tree:

- The store is Markdown files alone; every event rewrites one entry's header in place
  (`questions.py`, the events at, open, move … rung); no log of events is kept apart from git's
  history of those files, which already says who changed what and when (requirement 1.8).
- Some header lines change without anyone deciding anything: `at` on a question reached again
  twelve hours after its last strike rewrites its `struck` line (`STRIKE_AFTER`,
  `questions.py:78`, `_reach`).
- A body is free text, written by hand (requirement 1.4); any merge must merge free text.
- Requirement 1.6: edits from different machines merge without loss, and a conflict is shown,
  never lost — the behaviour of git's three-way merge of text.
- The user, 2026-10-30, on conflicts: "will there really be conflicts?" — with ids stable
  (decision 23) and a unit held by one session, two copies seldom touch one entry.
- Left to this question by q-upe7cs: what a check at push reads once no
  coordinator holds every machine's truth, and whether the sessions' rows travel.
- Left to this question by decision 32 of q-7ebz2f: how the harness detects a second
  machine.

## Decisions

Moved on 2026-11-09 into
[q-7ebz2f's list](q-7ebz2f.md#decisions), by its decision 31:
decisions 1 and 2 are its 36 and 37, 4 to 13 its 38 to 47; 3 left the list, replaced by 12, now 46.

## Two copies tried, 2026-11-04

Git 2.32 for Windows, a scratch bare repository and two clones, the store on a branch with no
history in common with `main`. A plain `git clone` listed that branch with no refspec of its own;
`main` was untouched throughout. A push refused because the other copy had pushed was followed by
`git pull` and a second push, which went through.

| Both copies changed | Result |
|---|---|
| Different entries, one of them new | merged clean |
| One entry, a header line and a body line far from it | merged clean |
| One entry, `lean` and `struck`, neighbouring header lines | conflict |
| One line, to the same text | merged clean |

So the header is the place that conflicts: git treats changes to neighbouring lines as one, even
in different fields. The last row used equal text; a real `struck` carries its time, so two
strikes differ and would conflict.

## With no folder, tried 2026-11-05

Git 2.32 for Windows, a scratch repository, through a temporary index: an entry written to the
branch left only `.git` in the working folder; a close on one line and a body edit on another,
made on two lines of history, merged by `git merge-file` on the three blobs into a commit of two
parents, with no file checked out; a true conflict gave a non-zero exit; a push of the branch to a
local bare repository took 2 to 4 seconds. One first run stalled at the push with stdin open; with
it closed every run passed, the cause not established.

Reading all 355 entries of this tree straight from git, one `ls-tree` and one `cat-file --batch`,
took 933 ms against requirement 1.1's tens of milliseconds: a read at each step needs a process
holding the tree in memory.

## What two copies can do to one another, 2026-11-05

Read from the store's events and the parts of an entry, for two copies that both changed since
they last met. Only the header rows were tried, on a real header, by a field-by-field merge.

| Kind | Cases | Who settles it |
|---|---|---|
| Nothing collides | different entries; different fields of one entry; a header and a body; the same change on both sides; two new questions, given ids apart | merged, nobody |
| One field, a plain rule | `struck` (the larger), `rung` (the higher), `depends on` (both), `lean` (the later, the earlier in history) | the rule |
| A true disagreement | two moves of one question; two different closes; two rewordings; one paragraph of a body; two owners | decision 4 |
| Clean text, wrong meaning | two moves making a cycle; a close on one side and a body changed on the other; one question opened twice under two ids | `--check` finds the first and the third, which it already reports; the second counts as a true disagreement, by decision 7 |
| The process fails | a push refused again; no network; a hook refuses; the remote branch rewritten, no common base; a crash mid-merge; two versions of the harness writing different headers | retry; carry on and say so; say so; stop for the person; nothing moved, the ref moving last; say so |

Decision 23 writes the derived address into each entry's header, rewritten across a moved subtree:
two moves in different places would then conflict in headers neither meant to touch.

Rows do not travel today: of 21 in `docs/sessions/rows/`, 18 are untracked. Session records do, each
committed at `/conclude`.

## With one server, 2026-11-05

Decision 33 of
[q-7ebz2f](q-7ebz2f.md)
makes the server one across machines. Writes through it go in turn, so sessions that reach it
cannot diverge: the first four kinds above arise only from a write it did not take. Decision 2's
direct run of `questions.py` is such a write, on a machine that cannot reach the server, in a cloud
session, which reaches the repository and never a server on the person's machine, or on a second
machine that raises its own server before its address is set. Read so, a merge has one place: the
server, on finding the store's branch moved by a write it did not take.

Decision 5 keeps such writes.

## A folder through a link, tried 2026-11-09

Git 2.32 for Windows, a scratch repository: the store's branch, with no history in common with
`main`, checked out as a worktree at `.git/gw/questions`; `docs/questions` in `.gitignore` and made
a junction to it with `mklink /J`, Developer Mode off and no administrator. The entry read through
the link; `git status` on `main` stayed clean; an edit through the link showed as a change in the
store's checkout; a second code worktree, with a junction of its own, read the same file;
`git clean -fdx` in either code worktree left the junction and the store's files in place.
