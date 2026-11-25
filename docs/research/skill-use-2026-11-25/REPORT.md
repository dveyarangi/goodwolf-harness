# Was the skill an act needs in the session's context — a first reading, 2026-11-25

- **record of** what happened

Asked by the person on 2026-11-24, as the reading to compare against once this tree's work is cut
into roles and short sessions:
[q-b4um7c](../../questions/q-b4um7c-do-sessions-load-the-skill-their-act-needs-counted-from-the-hosts-transcripts-before-and-after-a-change.md)
"Do sessions load the skill their act needs, counted from the hosts transcripts before and after a
change to the method?". Evidence, not a decision. Read by [skill_use.py](skill_use.py) over Claude
Code's transcripts of this tree — 310 files, 2026-09-06 to 2026-11-24 — in 23 seconds, calling no
model; every row stands in [rows.csv](rows.csv). The script is a one-off read, kept so the numbers
can be read again; no mechanism's part.

## What is counted

A row is one transcript, turn and kind of act; the skill's state is taken at the turn's first such
act. A turn starts at any message that is not a tool's result — the person's, another session's, a
helper's return. An act a forked or resumed transcript copies is counted once.

| act | the skill it needs | how it is seen |
|---|---|---|
| an instruction file edited | `/skill-up` | the host's edit tools on the entry file, a rules file, a file of a skill |
| a rule's frame drawn in a reply | `/skill-up` | the frame's header in the reply's text |
| a ticket, a plan written new | `/ticket`, `/plan` | a file the host reports as created |
| a commit made | `/commit` | `git commit` in a shell command |
| the product document, an edge record edited | `/product`, `/edge` | the host's edit tools |

The states: the skill **invoked in the turn**; **invoked earlier, no compaction between**;
**carried across a compaction** — the host's own list of the skills it re-attached; **its file
read, not invoked** — printed by a read or a shell command since the last compaction; **neither**.

## The reading to compare against: from 2026-11-01

| act | skill | rows | invoked in the turn | invoked earlier, no compaction between | carried across a compaction | its file read, not invoked | neither |
|---|---|---|---|---|---|---|---|
| an instruction file edited | `/skill-up` | 26 | 2 (8 %) | 12 (46 %) | 11 (42 %) | 0 (0 %) | 1 (4 %) |
| a rule's frame drawn in a reply | `/skill-up` | 58 | 11 (19 %) | 19 (33 %) | 27 (47 %) | 0 (0 %) | 1 (2 %) |
| a ticket written new | `/ticket` | 2 | 0 (0 %) | 1 (50 %) | 1 (50 %) | 0 (0 %) | 0 (0 %) |
| a plan written new | `/plan` | 6 | 2 (33 %) | 2 (33 %) | 2 (33 %) | 0 (0 %) | 0 (0 %) |
| a commit made | `/commit` | 257 | 9 (4 %) | 22 (9 %) | 0 (0 %) | 21 (8 %) | 205 (80 %) |
| the product document edited | `/product` | 3 | 1 (33 %) | 2 (67 %) | 0 (0 %) | 0 (0 %) | 0 (0 %) |
| an edge record edited | `/edge` | 1 | 0 (0 %) | 0 (0 %) | 0 (0 %) | 0 (0 %) | 1 (100 %) |

- A rule was written or proposed 84 times; the skill was absent twice. It was a load carried
  across a compaction 38 times, 45 %: the skill in context, read long before. The keeper's two
  slips of the register's entry *76. Rules were proposed in a reply without `/skill-up`*, second
  strike, are among these — a load nine days and at least ten compactions old. A short session
  has no such load.
- A commit was made 257 times, 226 of them, 88 %, with `/commit` not invoked.
- The other acts are too few here to read.

## The whole history

| act | skill | rows | invoked in the turn | invoked earlier, no compaction between | carried across a compaction | its file read, not invoked | neither |
|---|---|---|---|---|---|---|---|
| an instruction file edited | `/skill-up` | 334 | 9 (3 %) | 24 (7 %) | 13 (4 %) | 57 (17 %) | 231 (69 %) |
| a rule's frame drawn in a reply | `/skill-up` | 219 | 21 (10 %) | 64 (29 %) | 35 (16 %) | 20 (9 %) | 79 (36 %) |
| a ticket written new | `/ticket` | 51 | 12 (24 %) | 36 (71 %) | 1 (2 %) | 0 (0 %) | 2 (4 %) |
| a plan written new | `/plan` | 77 | 49 (64 %) | 26 (34 %) | 2 (3 %) | 0 (0 %) | 0 (0 %) |
| a commit made | `/commit` | 1296 | 62 (5 %) | 352 (27 %) | 0 (0 %) | 278 (21 %) | 604 (47 %) |
| the product document edited | `/product` | 7 | 2 (29 %) | 2 (29 %) | 0 (0 %) | 0 (0 %) | 3 (43 %) |
| an edge record edited | `/edge` | 13 | 0 (0 %) | 4 (31 %) | 0 (0 %) | 8 (62 %) | 1 (8 %) |

By week, an instruction file edited and a rule's frame drawn:

| week | rows | invoked in the turn | invoked earlier, no compaction between | carried across a compaction | its file read, not invoked | neither |
|---|---|---|---|---|---|---|
| 2026-W36 | 3 | 0 (0 %) | 0 (0 %) | 0 (0 %) | 2 (67 %) | 1 (33 %) |
| 2026-W37 | 42 | 0 (0 %) | 0 (0 %) | 0 (0 %) | 29 (69 %) | 13 (31 %) |
| 2026-W38 | 25 | 0 (0 %) | 0 (0 %) | 0 (0 %) | 9 (36 %) | 16 (64 %) |
| 2026-W39 | 36 | 0 (0 %) | 0 (0 %) | 0 (0 %) | 1 (3 %) | 35 (97 %) |
| 2026-W40 | 26 | 0 (0 %) | 0 (0 %) | 0 (0 %) | 0 (0 %) | 26 (100 %) |
| 2026-W41 | 168 | 1 (1 %) | 2 (1 %) | 0 (0 %) | 12 (7 %) | 153 (91 %) |
| 2026-W42 | 65 | 5 (8 %) | 11 (17 %) | 0 (0 %) | 2 (3 %) | 47 (72 %) |
| 2026-W43 | 98 | 10 (10 %) | 41 (42 %) | 8 (8 %) | 22 (22 %) | 17 (17 %) |
| 2026-W44 | 6 | 1 (17 %) | 3 (50 %) | 2 (33 %) | 0 (0 %) | 0 (0 %) |
| 2026-W46 | 13 | 2 (15 %) | 6 (46 %) | 5 (38 %) | 0 (0 %) | 0 (0 %) |
| 2026-W47 | 58 | 6 (10 %) | 20 (34 %) | 31 (53 %) | 0 (0 %) | 1 (2 %) |
| 2026-W48 | 13 | 5 (38 %) | 5 (38 %) | 2 (15 %) | 0 (0 %) | 1 (8 %) |

Until week 42 a rule was written with `/skill-up` hardly ever invoked; from week 43 — the week
the register's entry on it was struck and the rule reworded — it is nearly always in context, and
from week 46 about half the time as a carried load.

Carried loads, by how many compactions old at least: one, 52 rows in 5 transcripts; two or three,
11 in 3; four to nine, 20 in 2. A transcript that begins at a compaction counts from there, so an
age is a floor.

## Judged twice

By a subagent that did not write the script, each time against the transcripts by a reader of its
own.

**The first script failed.** It counted an act once for every transcript that copies it — a fork
or a resume carries its parent's history — so 1,280 of 3,310 rows were repeats; and it took a
skill's file printed through the shell for no load at all, which is how skills were mostly read
in September and October. Of 16 sampled rows, 3 of the 5 early rows it called not loaded were wrong.

**The rewrite**, judged on five named points: the rows equal the judge's own count of distinct
acts, exactly, on every act. Its verdict on what is printed above:

- *Stood on as they are*: the plan, product and ticket lines; the row total of every act; the
  three invoked and carried columns of every line, and of the by-week table from week 41 on.
- *Only with a caveat*: for instruction edits, frames, commits and edge records, the line between
  *its file read* and *neither* is soft — 100 of 386 rows in *its file read* had under half the
  file in context, 25 rows in *neither* had it whole by a way the script does not see. Read the
  two together as *not invoked*.
- *Not at all*: instruction files written through the shell. The script finds them by a pattern
  and keeps them out of every table above: 184 rows, 110 with the skill invoked or carried; of 20
  sampled, 12 were real. Since those run more often with the skill than the tool-made edits do,
  the tables understate invocation in October and November.

Made after the second judging, on its findings, and not judged: a skill's first day is taken to
the instant it entered the tree, which took 22 rows of 2026-09-06 out, and week 36 with them.

## What it does not say

- Whether a rule written with the skill in context came out well.
- Anything of Cursor or Codex, which record a skill's load differently.
- Anything a helper did: subagents' transcripts are not read. The judge found five helper runs in
  November that edited instruction files, none with `/skill-up`.
- Seven turns hold acts on both sides of a compaction; the later side has no row.

## Reading it again

`uv run --offline --no-project python docs/research/skill-use-2026-11-25/skill_use.py <the host's
transcripts directory for this tree> rows.csv` — the directory is under the person's profile and
is named nowhere here. The by-week table carries any later cut; the lines to watch are the carried
share where a rule is written, and *not invoked* where a commit is made.
