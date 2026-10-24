# 0067 — The commit convention is the project's

- **record of** what happened

## Decision

[q-0037.0009.0005.0001](../questions/done/q-0037.0009.0005.0001-which-commit-subject-convention-does-commit-write-where-a-project-states-none-and-how-does-it-find-the-one-a-project-keeps-without-stating-it.md)
was decided by the user: /commit writes the subject in the project's convention, the one it
states, else the one its tooling enforces, else the one its recent history keeps; where a project
has none of these, Conventional Commits. The front page now lists the commit convention among
what stays the project's, and says this repository's step prefixes do not travel.

How the answer turned:

- The first proposal was no default at all, a plain imperative subject where nothing is stated,
  on the ground that a `feat`/`fix` type nobody reads is a ritual. The user refuted the premise:
  *mostly it is agents that will read it*. The point that carried was not that agents need the
  grammar, since they read prose fine, but that every model already knows Conventional Commits.
  Its instruction cost is zero, while the step prefix exists for a reader only through L8.
- The core rule's old wording, *where it states one*, held nothing but words. A mature project
  usually keeps its convention in tooling or in history, not in prose, so the rule never saw it.
- The two conventions sit on different axes. The step prefix says where a commit's reasoning
  lives; Conventional Commits says what the change means to a consumer, breaking or not. Combining
  them through `scope` was rejected as a misuse; a `Step:` trailer would be the clean form, which
  was noted for this repository and not taken up.

## What went wrong, and what it taught

The complaint relayed as *the harness will not let us replace the convention and imposes its own*
turned out, once read, to be xuanxue-cabinet's agent reading this repository without installing,
the live case 1 already recorded under
[q-0037.0006.0020.0001.0004](../questions/q-0037.0006.0020.0001.0004-how-does-the-install-read-a-tree-with-a-method-and-report-what-goodwolf-would-change-there-before-anything-is-written.md).
It took this repository's history of `IMPLEMENT:`/`VERIFY:` subjects for the harness's format.
The install would have carried none of it: L8 has been local since 2026-10-11 (`b3e8fc2`), and
the installer strips the origin's local blocks. The front page was silent, so the history was the
loudest evidence. Lesson: what this repository shows in public is read as what the harness ships,
unless the page says otherwise.

## Principle without a home

A source repository's public face (its history, and the local blocks inside its shipped files) is
read by outsiders as the product. Whatever there is local should be marked local where an
outsider meets it.

## Open questions touched

- [q-0037.0009.0005](../questions/q-0037.0009.0005-what-does-commit-own.md) What does /commit own?
  It stays open; its skill still reads *Mechanism: not yet*.

## After the conclude

At the user's request, /conclude gained a step: where the host lets a session rename itself, it
prefixes the session's name with `(closed) ` before the row is ended. A pass over this tree's
sessions in the host followed, and the eleven that had run /conclude were renamed. Thirteen others
have rows a wake ended without a conclude; they were left as they are. The rows of two sessions
whose process had stopped still read `running` and hold units, pathfinder's and Sessions
interaction's.

## What continues

The cabinet's other point stands and was not taken up: the reply's head tables and glyphs come
from the entry contract itself, so they reach every recipient over its own voice and interface.
The question is what part of the reply's form is the method's and what part is the tree's, and it
belongs near q-0037.0009.0021 and q-0037.0010.0012. A first step for the next session that takes
it: read those two and decide whether this question is already held there.
