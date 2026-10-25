# The meeting, run 5 on GoodWolf's own tree — the study read on the repository that writes it

- **record of** what happened
- **evidence for** [q-0037.0006.0020.0001.0004](../questions/q-0037.0006.0020.0001.0004-how-does-the-install-read-a-tree-with-a-method-and-report-what-goodwolf-would-change-there-before-anything-is-written.md), [q-0037.0006.0020.0001.0004.0001](../questions/q-0037.0006.0020.0001.0004.0001-in-a-tree-that-runs-goodwolf-does-the-blind-run-answer-as-one-of-its.md)

2026-10-25. A fresh agent ran [MEETING.md](../../.agents/skills/harness/MEETING.md) as written on
this repository, main at `ec60b81`, checked out with other sessions' uncommitted changes in place.
It read with read-only shell and git calls and ran none of the project's scripts. Its one write is
this record. The person changed one thing for this tree: the blind run did not come in knowing
nothing of GoodWolf. It answered as one of this tree's own sessions would, using GoodWolf's read
calls (`questions.py --wake --session`, `--tree`, `--path`, `--check`, `tickets.py --list`,
`--check`), and was told nothing of the measurement or the key
([q-0037.0006.0020.0001.0004.0001](../questions/q-0037.0006.0020.0001.0004.0001-in-a-tree-that-runs-goodwolf-does-the-blind-run-answer-as-one-of-its.md),
lean the user, 2026-10-25). Cost of the study, by the host's account: 244,389 tokens, 133 tool
calls, 1,554 s. Cost of the blind run, by the host's account: 231,610 tokens, 51 tool calls, 547 s.

Score: settled 5 hit · in flight 3 hit · undecided 3 hit · contradictory or incomplete records
2 noticed and said, 1 answered from one side · hidden 1 of 3 recovered.

---

# What would GoodWolf change here?

## 0. How this was read

You asked what GoodWolf would change here. Here that question turns back on itself: this repository
develops GoodWolf using GoodWolf's own method. So the report says what GoodWolf's study finds in
GoodWolf's own tree, and which of GoodWolf's own repairs would meet each finding. The words
*mechanism*, *store*, *straw dog*, *rung*, *dial*, *ring* and *window* are this project's own
words. They are used as the project uses them.

The study has three parts, and every paragraph below carries the mark of the part it comes from:

- **[inventory]** lists what the tree already has, in its own names. That covers the entry file
  and what it includes, the skills, the scripts and checks, the outside parties, the kinds of
  record and where the current state lives, and the size of a change as the history shows it.
- **[reading]** is eight readings. Each one looks for a single way that written knowledge fails to
  reach the person who needs it, or fails to hold once it has:
  1. what it costs to reach what is written;
  2. kinds of record mixed in one file;
  3. one fact in several homes that have parted;
  4. what no one records;
  5. where the project does not follow its own rules;
  6. who owns what;
  7. where you stand, the person;
  8. a decision without its reason.
- **[ledger]** is a measurement.
  - A separate agent answered 17 questions about the project from the files, the git history and
    the store's read calls.
  - The key was built from the code and the records before that agent ran.
  - The answers were scored against the key, and the cost of the run was counted.

The read was quick and sampled, by search, not file by file. What it found is what it met, not an
inventory of every disagreement. GoodWolf repairs a disagreement where a session meets it, so
every session meets and mends its own. A finding against the tree is said plainly, with its
numbers.

## 1. What was found

### The inventory

**The entry file.** `CLAUDE.md` is one line, `@AGENTS.md`. `AGENTS.md` is 345 lines and 3,772
words, at "Entry contract: v121, 2026-10-25". It holds:

- the general rules;
- the loop: two rings joined at `/align`;
- autonomy as a dial on two ladders, development and self-improvement;
- the straw-dog convention;
- six installed blocks, carrying 15 rule ids;
- 16 straw-dog wrappers.

168 commits touch it. There have been 121 versions in 50 days, 11 of them on 2026-10-25, and each
is recorded in `docs/research/entry-contract-findings.md`. No date stands in the entry file
itself. [inventory]

**The project's own answers.** `local.rules.md` holds nine rules and one setting (`debug=on`):

| rule | what it says |
|---|---|
| L1 | what the repository is |
| L2 | the dials, `development=a feature · self-improvement=a rule`, and push each commit |
| L3 | the verification set |
| L5 | how Python runs |
| L7 | nothing copied to the host's memory |
| L8 | the commit step words |
| L9 | the voice |
| L10 | what core names under `docs/` |
| L12 | at most 8 open questions in work |

Each rule names its target and its authority. [inventory]

**Skills, mechanisms, scripts.**

- **Skills:** 25 under `.agents/skills/`, in one physical home, reached by per-clone links (ADR-0003).
- **Mechanisms:** 9 declared under `.agents/mechanisms/`, with their evidence under `docs/mechanisms/`.
- **Scripts:** 12 Python modules under `.agents/scripts/gw/`, 10,284 lines, standard library only
  (ADR-0004), and 15 test files.
- **Checks:** the verification set is 8 `--check` commands always, plus the `unittest` suite when a
  non-markdown file changed.
- **No CI and no git hook.** The hosts' hooks hand the wake and the window to each session.

[inventory]

**Outside parties.**

- **Hosts:** three — Claude Code, Codex and Cursor — each with an edge record under `docs/edge/`.
- **Recipients:** the projects that install core. Today they take it from this working tree, and
  releases are not built.
- **A second checkout inside the tree:** `.claude/worktrees/suspicious-faraday-766026` has 685
  files and stands detached at `0c7ae5b` (2026-10-12). It is excluded in `.git/info/exclude`, not
  in `.gitignore`, so a plain recursive grep meets its stale copies. Its `AGENTS.md` still carries
  the switch table.

[inventory]

**Kinds of record, and where state lives.**

| record | where | count |
|---|---|---|
| question store | `docs/questions/` | 201 live entries (188 open), 102 in `done/` |
| tickets | `docs/tickets/` | 49 live, 78 done; a ticket's header owns its state |
| queue | `docs/tickets/README.md` | one file, the order |
| RFCs | `docs/rfc/` | 4 live, 67 done |
| specs | `docs/spec/` | 5 |
| ADRs | `docs/adr/` | 4 |
| architecture | `docs/architecture.md` | one file |
| product document | `docs/product.md` | 52 answers |
| glossaries | project and method | two |
| session records | `docs/sessions/` | 72 |
| session rows | `docs/sessions/rows/` | 58 files |
| rule-failure register | `docs/rule-failures.md` | 84 entries, 2,429 lines |
| dreams | `docs/dreams/` | 6 |
| research and benches | `docs/research/` | most of `docs/`' 1,598 files |

The current state lives in four places: the store, the ticket headers, the queue, and the session
rows. [inventory]

**The size of a change.** There are no pull requests. Work lands as direct commits to `main`, by
one author, pushed as they land.

- **History:** 1,187 commits from 2026-09-05 to 2026-10-25, over 40 active days, with one merge.
- **Size per commit:** a median of 3 files and 54 lines (p90: 11 files, 387 lines). Over the last
  14 days, 2 files and 40 lines.
- **Pace:** per ISO week from W36 to W43, 15, 72, 32, 75, 86, 375, 218 and 314 commits; the median
  active day has 22, and the busiest, 2026-10-25, had 136.
- **Kind of step,** read from the subject's first word: ALIGN 271, IMPLEMENT 151, QUESTIONS 128
  (before the closed list), FIX 104, MAINTAIN 97, CONCLUDE 89, PLAN 87, VERIFY 68, TICKET 56,
  DISCOVER 22.

So a unit of work here is one step of the ring: a few files, tens of lines, one commit. [inventory]

### The readings

**1. What it costs to reach what is written.**

- **Every session's first read:** before its first answer, a session reads 516 lines and 5,786
  words: `AGENTS.md`, `/recall`'s skill, the queue, and the latest session record. On top of that
  come 398 words of skill descriptions and the hook's wake and window.
- **The largest live records:** q-0037.0019 is 799 lines and holds its Where it stands, seven
  decisions, a case, six passes and an outside view of twelve families. Ticket 01-0010 is 943
  lines. The register is 2,429 lines in a single file.
- **Where a rule's reason sits:** two or three files from the rule. A rules file holds the rule
  and who decided it, and when. The reason stands in the mechanism doc, its evidence file, or the
  question that decided it. For example, L12 leads to q-0037.0019's decisions 4 and 6, and from
  there to its Where it stands. The four ADRs are the exception: they carry their reason inline.
- **The blind run's report:** one wake call "answered or pointed to most questions". Its output was
  about 65 KB and "too large to read in one go". [reading]

**2. Kinds of record mixed in one file.**

- **`docs/pacer.md`** keeps decided rules beside an idea under alignment, for example "2026-09-06,
  user: a turn holds at most one execution step". No rule orders a session to read it. The entry
  file's own *A document informs* calls such text drift.
- **The queue** is a record of what it intends to become, yet it ends on a rule: "Next cycle needs
  a nod (`next-cycle=ask`)". Rule failure 66, of 2026-10-24, records that it had grown its history
  back in fourteen days.
- **The open questions** are their work's working documents, by design. Thirty-one of them hold 90
  dated sections beside their current state.
- **`docs/architecture.md`** carries nine dated marks of authority inside its contract text. The
  entry file carries none. [reading]

**3. One fact in several homes that have parted.** Each pair is written as GoodWolf's maintenance
would hold it: what is written ↔ what it is of. The study met these ten:

1. The queue's last line, `next-cycle=ask`, written 2026-10-24 ↔ the dial that replaced the five
   switches on 2026-10-15 (L2; `docs/process.md`).
2. `docs/process.md`: "this project's four commands sit in the entry file's local block" ↔ L3,
   which holds eight checks and the tests, installed into three skills, none of them the entry file.
3. `docs/pacer.md` "Idea under alignment", `docs/README.md` "held here until the pacer is a
   mechanism", and architecture's "The pacer owns turn progression" ↔ q-0037.0019, accepted
   2026-10-23: "The pacer dissolved".
4. The queue as the order of the work — its ten numbered items, `/recall`'s Q2 "read the queue",
   the ticket mechanism's "read by `/recall` for the order", and `questions.py`'s "the order being
   the queue's" ↔ q-0037.0019 decision 7, of 2026-10-25: "The path is not read from a written
   queue".
5. The anchor that places S5 and L8 in `/commit`, as `session.rules.md` and `local.rules.md` name
   it ↔ the line itself, rewritten by `6308d1d` on 2026-10-25. Reading `inject_rules.py`, not
   running it: `--check` calls a present, matching block "present" without testing its anchor. An
   install that writes the block afresh refuses with "anchor … not found".
6. Ticket 01-0060's header, "its first slice Ready" ↔ 01-0060.0010, Done on 2026-10-25.
7. Ticket 01-0019, "Blocked (accumulating evidence before its align)" ↔ its six slices, minted
   2026-10-24 and queued third on 2026-10-25.
8. Ticket 01-0011.0110.0020, "three boxes wait" ↔ two unchecked boxes.
9. ADR-0001, which says `docs/process.md` is a straw dog "bound to 01-0020", a ticket ↔ ADR-0002
   and architecture, which say a straw dog binds to a question, never to a ticket.
10. The preamble of the entry-contract findings, which says a version covers "the switch roster" ↔
    the entry file, which has had a dial and no roster since 2026-10-15.

[reading]

The blind run met pairs 1, 3 and 5 and the header of pair 8 on its own, and three more pairs the
study had not met:

- 01-0011.0110.0020's Outcome says a paragraph "opens with" its principle, but since v35 the mark
  closes the paragraph.
- 01-0019 says the register "has one entry"; it holds 84.
- The lean on q-0037.0009.0021.0002 says q-0037.0002 is "aligned next", but q-0037.0002 is in
  `done/`.

That makes thirteen parted pairs met in one read. [ledger]

**4. What no one records.** This tree records its own operation more than most: 72 session
records, 58 rows, 89 CONCLUDE commits, 84 register entries, and 121 recorded versions of the entry
contract. The gaps met:

- **Session numbers given twice:** two session records are numbered 0068, both of 2026-10-25, and
  two are numbered 0044, both of 2026-10-09. The number is picked by hand. Rule failure 75 records
  the same race for entry-contract versions.
- **The rows at reading:** ten read running, two of them with no position. One ended row still
  reads `holds q-0037.0006.0005`.
- **Untraced work:** the blind run could not trace the untracked `README.draft.md` to any session.
- **History in rules:** some local rules' authority lines carry history, for example "the switches
  of 2026-09-05 to 2026-10-10 given way to the dial". [reading]

**5. Where the project does not follow its own rules.**

- **Naming sessions in commits.** `/commit` says "Do not reference sessions in commit comments,
  sessions are ephemeral" ↔ 37 subjects name a session by number, 7 of them since 2026-10-18.
  Nothing gates this.
- **Session numbering.** `/conclude` asks for "a constantly incrementing number" ↔ 0044 and 0068
  are each given twice. Nothing gates this either: `sessions.py --check` reads rows only.
- **The closed list of step words.** L8 is a closed list (2026-10-11) ↔ 30 commits from 2026-10-12
  to 10-15 used words off it (QUESTIONS 9, RULE 8, SPEC 4, README 3, IMPACT 2, none 2, QUEUE 1,
  PRODUCT 1). None has done so since 2026-10-16, which is held by attention alone. Two commits
  carry three prefixes, against "One prefix per commit".
- **The cap.** L12 sets eight ↔ no script compares the count with it. The path "compares no count
  with the project's limit". The blind run found the cap stepped over on its first day and brought
  back under on 2026-10-25 by `3d6d0af`, when fourteen tickets stood In progress.
- **Ticket positions.** TICKET-FORMAT says "the next free position after its siblings' … stepping
  by 10" ↔ 35 of 128 tickets stand off the step of ten. Twenty-eight of them are children inserted
  between siblings.
- **A gate that covers less than its rule.** Architecture says the installer validates "its anchor
  matching exactly one line". The check does not, while a block is present (pair 5). [reading]

**6. Who owns what.**

- **Written:**
  - nine mechanisms each declare their records, instructions and settings;
  - each installed block names its owner;
  - core and instance are kept apart by ADR-0001 and ADR-0002, held by `mechanisms.py --check`;
  - a session's hold on a unit is in its row, taken over only on the person's word (S9).
- **Unsaid:**
  - 15 of the 25 skills read "Mechanism: not yet", among them `/align`, `/plan`, `/implement`,
    `/verify` and `/commit`;
  - "ordering the queue and writing its pacing prose" has no instructing file; rule failure 66
    says "no file instructs writing the queue at all";
  - which work comes next is claimed by two parties: the queue, through the ticket mechanism and
    `/recall`'s Q2, and the path, through q-0037.0019 decision 7. [reading]

**7. Where the person stands.**

- **What stops for the person:** 180 of the 188 open questions stand at or above a dial; 3 stand
  below; 5 carry no rung, which is a finding of the store by q-0037.0019 decision 2. In the
  decision's own words: "nearly every open question of this tree stands at or above them is the
  dial working".
- **What waits on the person:** ticket 01-0011.0110.0020 has waited 17 days for a week of grading
  by the person. 01-0017.0010 and .0020 have had "no session on it since 2026-10-15".
- **What was decided without the person:**
  - q-0037.0019.0004 (uncommitted) records a decision "written by a session acting on a test
    message; the user struck it as wrong";
  - rule failure 84: a *yes, but which moment?* was taken as the yes;
  - rule failure 80: a rule was read as leave to commit other sessions' work.
- **What came to the person that need not have:** rule failure 81, "The person was asked to choose
  among a record's ids". [reading]

**8. A decision without its reason.**

- **The local rules:** only two of the nine carry a reason in the file — L10 ("read only by
  whoever writes core") and L12 ("on trial, to be re-read by what it stops").
- **L8:** its step words have an authority and no recorded why.
- **L12:** the number eight has no reason beyond the trial. The blind run: "'Why eight' has no
  derivation anywhere."
- **By contrast:** the four ADRs and the Decisions lists in the questions carry their reasons and
  their refuted options ("Not: …") as a habit. [reading]

### What the method asks of a change

| what | count |
|---|---|
| read by every session | 516 lines, 5,786 words in the tree; 398 words of skill descriptions; the wake and the window |
| outside the tree, named only | the host's memory index |
| CI | none |
| local checks per change | 8; plus 1 test run, 15 files, when non-markdown changed |
| steps per change | the ring: `/ticket → /plan → /implement → /verify → /maintain`, joined at `/align`; a commit per step |
| acceptance criteria per ticket | median 5, p90 8, max 17 (128 tickets) |
| the commit subject, the account in place of a PR body | median 207 characters, p90 555, max 1,774 |
| ADRs | 4 in 1,187 commits |
| open questions with a Decisions list | 23 |
| ALIGN commits | 271 |

[ledger]

### What stays as it is

These stay the project's own, kept by its choice, and GoodWolf works with them: the step words, the
verification set, the dials, the push-as-it-lands way with git, the voice, the benches under
`docs/research/`, the register, and the ADRs with their considered options. [inventory]

## 2. Main recommendations

1. **Run GoodWolf's maintenance over `docs/`:** the queue, `process.md`, `pacer.md`,
   architecture's deferred decisions, ADR-0001's binding sentence, three ticket headers and two
   preambles. Maintenance holds each document to what it is of, and one quick read met thirteen
   parted pairs. The blind run named six of them unprompted, so you are already seeing them as
   drift.
2. **Put the queue's role to yourself as the decision it now is.** q-0037.0019 decision 7 withdrew
   the written order. Four instructions and a script docstring still read it. GoodWolf keeps a
   decision with what it waits on: the text the decision changes is wrapped and bound to
   q-0037.0019.0004, and that question is above your dial.
3. **Give a check to each rule held by attention.** That means a session record's number drawn by
   the session script, the commit subject read against `/commit` and L8, and the installer's check
   testing a present block's anchor. GoodWolf's way is a check per kind of record, and these three
   rules have 37, 2 and 1 cases standing against them.
4. **Write down what only the history and the code keep.** That means the shape of a commit subject
   in L8, which links do not count as a decision's home in Q6, and what a ticket's position does
   in the format. GoodWolf installs a rule where it is read, and the blind run, using GoodWolf,
   missed two of these three. It recovered the third while saying it is "stated nowhere".
5. **Give L8 and L12's number their reasons.** GoodWolf keeps a decision with its reason, so the
   next session can tell a choice from an accident and see when the trial of eight ends.

## 3. What clearly improves, and what you will likely give up

What you will see change is that the documents a session reads stop contradicting the decisions
you made last week.

- A session asked what comes next will meet one answer, not a path and a queue that disagree.
- A session asked for the verification set will meet one count.
- A session asked about the pacer will learn it dissolved without having to find q-0037.0019.
- You will see three more mistakes caught at the moment they are made, where today they are found
  later by reading: a second session record numbered like the first, a commit subject naming a
  session, and an anchor rewritten under the installer.
- The conventions you keep by habit — the unit's id and your authority in every subject, positions
  inserted between siblings — will be written where a new session reads them. The blind run went
  to the history for the first and missed the second.
- What waits on you will read the same in a ticket's header as in its boxes.

What you will likely let go of are habits of this tree:

- a queue that is both an order and a place for a rule;
- headers whose parenthetical keeps a state that has since moved;
- session numbers picked by hand;
- commit conventions that live in the history alone;
- rules whose only guard is the attention of whoever writes next;
- the comfort of a written order, once the path is the order — or, if you decide the other way,
  the path's claim to it.

## 4. The migration plan

| # | what | what of GoodWolf carries it | what it touches · what depends on it | size |
|---|---|---|---|---|
| 1 | GoodWolf in place | nothing to take in: the tree is its origin, at v121 | — | none |
| 2 | Repair the parted documents: the queue's last line, `process.md` § Verification, `pacer.md`'s status, `docs/README.md`'s pacer line, architecture § Deferred decisions, ADR-0001's binding sentence, the findings preamble | `/maintain`: every fact to one home | 7 files under `docs/` · nothing depends on it | one MAINTAIN commit, tens of lines |
| 3 | Repair three ticket headers: 01-0060, 01-0019, 01-0011.0110.0020 (status and Outcome) | `/maintain`, the ticket format | 3 tickets · the path's ready and in-work lists | one MAINTAIN commit |
| 4 | Point the `/commit` anchor in `session.rules.md` and `local.rules.md` at the line as it stands, and re-install | the mechanism shape's installer | 2 rules files, `/commit` · every fresh install of core | one FIX commit, 2 files |
| 5 | The queue's role decided: kept as an order, or reduced to what the path cannot read | `/align` on q-0037.0019.0004, at your dial | `/recall` Q2, `ticket.md`, TICKET-FORMAT, the `questions.py` docstring, the queue · items 2 and 6 | an align, then a few commits |
| 6 | State what the history and the code keep alone: the commit subject's shape in L8, a decision's non-homes in Q6, what a ticket's position does in TICKET-FORMAT | `/align` and the self-improvement ladder, installed where read | `local.rules.md`, `questions.rules.md`, TICKET-FORMAT · depends on 5 for the format | 1–3 ALIGN commits |
| 7 | Reasons for L8 and for L12's eight | the local file, your word | `local.rules.md` | one commit |
| 8 | Checks for the rules held by attention: session record numbers drawn, commit subjects read against `/commit`, an anchor tested under a present block, a parent ticket's status read against its children | the session, ticket and mechanism-shape scripts | `sessions.py`, `inject_rules.py`, `tickets.py`, their tests · depends on 4 | a ticket each, at the grain: one IMPLEMENT commit of a few files and tests |

The order is 2, 3 and 4 first, as repairs at the project's grain; then 5, which waits on you; then
6 and 7; then 8, one ticket at a time. [inventory]

## 5. What this report does not say

- **No comparison.** It compares this tree's method with no other method. Here the method is
  GoodWolf, and nothing was measured against an alternative.
- **Not an inventory.** It lists what one quick read met, not every disagreement.
- **The ledger measures one thing:** what it cost a session of this tree, using GoodWolf's read
  calls, to recover the project's state on 17 questions. It is far from the whole of GoodWolf.
  Because the run used GoodWolf, it is no before-and-after measure.
- **The second reading** after the plan is carried out is that plan's verification. Until the
  plan is finished, nothing is read from it but which items have landed.
- **GoodWolf's own not-yets that the plan meets.** Four, each met in this tree as a finding:
  - no check holds a parent ticket's status to its children's;
  - the installer's check does not test the anchor of a block that is present;
  - nothing draws a session record's number;
  - the path does not compare the count in work with the cap.

## 6. Appendix: the ledger

### How the run was taken

- **The agent:** a fresh agent working as a session of this tree, tagged
  `local_e308ebac-e37e-4fee-8436-4863e4928f00`. It knew GoodWolf and used it, read-only.
- **What it was told:** nothing of the measurement or the key. It was given the 17 questions alone.
- **What it could use:**
  - the files and read-only git;
  - GoodWolf's read calls: `questions.py --wake --session`, `--tree`, `--path`, `--check`;
    `tickets.py --list` and `--check`.
- **How it differs from runs 2 to 4,** whose blind agents were told nothing of GoodWolf: this mode
  is the person's choice for GoodWolf's own tree, held as
  [q-0037.0006.0020.0001.0004.0001](../questions/q-0037.0006.0020.0001.0004.0001-in-a-tree-that-runs-goodwolf-does-the-blind-run-answer-as-one-of-its.md).
- **The key:** built from the code and the records before the run, and corrected only where the run
  proved it wrong. It proved no key wrong. Where it proved a key incomplete, the addition is marked
  *Addition from the run*, and no score changed.

### The counts

| what | count |
|---|---|
| blind run, tokens (host) | 231,610 |
| blind run, tool calls (host) | 51 |
| blind run, wall time (host) | 546,570 ms, about 9 min 7 s |
| blind run, tool calls (its own account) | about 42 |
| blind run, files read (its own account) | about 45, whole or in part |
| blind run, searches and store calls (its own account) | about 12 greps; 6 GoodWolf read calls |
| the study itself, tokens (host) | 244,389 |
| the study itself, tool calls (host) | 133 |
| the study itself, wall time (host) | 1,554 s |
| read by every session, in the tree | `AGENTS.md` 345 lines / 3,772 words; `/recall` 58 / 811; the queue 18 / 213; the latest session record 95 / 990 — 516 lines, 5,786 words |
| loaded beside them | 25 skill descriptions, 398 words; the wake and the window from the hooks; outside the tree, named and not counted: the host's memory index |
| CI | none: no `.github/`, no active git hook |
| local checks per change | 8 always; 1 `unittest` run over 15 test files when a non-markdown file changed |
| check scripts | 8 in the set; 12 modules, 10,284 lines |
| steps per change | the ring `/ticket → /plan → /implement → /verify → /maintain`, joined at `/align`; one commit per step |
| checklist items | acceptance criteria per ticket, median 5, p90 8, max 17, over 128 tickets |
| PR body length | no pull requests; the commit subject is the account: median 207 characters, p90 555, max 1,774 |
| decision records per change | 4 ADRs in 1,187 commits; 23 open questions with a Decisions list; 271 ALIGN commits |
| grain | 1,187 commits, 40 active days, median 3 files / 54 lines per commit; last 14 days 2 / 40 |

### The score

| # | group | question, short | score |
|---|---|---|---|
| 1 | settled | standard library only | hit |
| 2 | settled | links not committed | hit |
| 3 | settled | `.agents/` and `docs/` apart | hit |
| 4 | settled | one shared checkout on main | hit |
| 5 | settled | the cap, and eight | hit |
| 6 | in flight | the voice | hit |
| 7 | in flight | the README from the product document | hit |
| 8 | in flight | a paragraph shows what it stands on | hit |
| 9 | undecided | self-amendment as a mechanism | hit |
| 10 | undecided | releases | hit |
| 11 | undecided | weighing a change | hit |
| 12 | contradictory | what comes next | noticed and said |
| 13 | contradictory | the verification set | answered from one side |
| 14 | contradictory | the pacer | noticed and said |
| 15 | hidden | a decision's home | not |
| 16 | hidden | a commit subject's shape | recovered |
| 17 | hidden | a ticket's number | not |

By group:

| group | score |
|---|---|
| settled | 5 hit of 5 |
| in flight | 3 hit of 3 |
| undecided | 3 hit of 3 |
| contradictory or incomplete records | 2 noticed and said, 1 answered from one side, 0 filled the gap |
| hidden | 1 recovered of 3 |

**Why each score that is not a plain hit:**

- **12:** the run answered from decision 7 and named both of the queue's stale parts — its numbered
  order and `next-cycle=ask` — as drift.
- **13:** the run gave L3 exactly, eight checks and the tests, and said it is "written once", in
  "no document". It did not meet `docs/process.md`'s "four commands … in the entry file". It
  answered from the right side, but from one side.
- **14:** the run named "dissolved" and listed three places that "have not caught up".
- **15:** the run restated Q6 and the homes the entry file names. It did not say that a link into
  a ticket, an RFC or a question's body does not count as a home.
- **16:** the run named the unit id and the closing authority with counts: 180 of 300 and 261 of
  300. It said this is "kept by history alone and stated nowhere".
- **17:** the run noticed ".0168, .0172 and .0175 show that the step of 10 has not always held".
  It read them as the rule failing, not as positions placed between siblings, and said "the
  number says nothing about order".

**Additions from the run.** These are marked here and change no score.

- **4:** the reason in full is at q-0037.0017.0002. In one checkout a branch means a worktree with
  its own copy of the store; sessions in separate worktrees mint ids blind; a session registered in
  the main checkout's store was refused from its worktree. The evidence was PR #5 and a held-back
  merge that `push=auto` published.
- **5:** the cap was stepped over on its first day. On 2026-10-25 `3d6d0af` brought fourteen
  tickets In progress under it. The wake counts tickets, not sessions in the ring, which is
  deferred at q-0037.0019.0001.
- **7:** what is decided so far at the align on q-0037.0018.0005: one front page; written by hand
  and checked, a straw dog on q-0037.0018.0005.0001; the check run both ways; the README as the
  mechanical copy of a marked source, a straw dog on q-0033.0010.
- **8:** the ticket's Outcome says the principle "opens" a paragraph, while since v35 the mark
  closes it. The rule now stands under debugging's D3.
- **9:** 01-0019 says the register "has one entry"; it holds 84.
- **14:** where a session resumes belongs to the session mechanism, per architecture § Deferred
  decisions.
- **16:** the anchor drift after `6308d1d`, met by the run from the same reading of
  `inject_rules.py`.
- **Beyond the sample:** the lean on q-0037.0009.0021.0002 names q-0037.0002 "aligned next", but
  it is in `done/`.

### The sample and its key

Scoring:
- settled, in flight, undecided — hit · partial · miss
- contradictory or incomplete records — noticed and said · answered from one side · filled the gap
- hidden invariants or structures — recovered · not


#### Settled decisions — the decision and its reason

##### 1. Why do the scripts under `.agents/scripts/gw/` use nothing beyond Python's standard library, with their tests on `unittest`?

**Key.** Decided at 01-0010.0070's RFC, 2026-09-06. The reason is the invocation, not taste:
GoodWolf runs its checks offline and with no project environment (`uv run --offline --no-project
python`, L5), and the scripts travel into recipients whose dependency management GoodWolf does
not control and must not disturb — a dependency would have to resolve in every estate on first use
with no install step; the scripts' work (file walking, Git subprocesses, Markdown scanning) needs
none. The price, accepted: test wall clock — no framework's parallel execution.
**Hit:** the decision and the offline/no-environment/travels-into-recipients reason. **Partial:**
one of the two halves of the reason, or the decision with a generic reason ("simplicity").
**Sources:** `docs/adr/0004-scripts-run-on-the-standard-library-alone.md`; `local.rules.md` L5.

##### 2. Why are the `.claude/skills` and `.cursor/skills` links not committed, so that every clone has to make its own?

**Key.** Skill bodies live once under `.agents/skills/`; hosts reach them by directory symlink
(ADR-0003, 2026-09-05). Amended 2026-09-26 by the user: tracked links were the harm — Git for
Windows checks a tracked link out as a 17-byte text file, which GoodWolf then refuses as a file
where a link goes, so a Windows clone met a refusal the tracking created (found by an adoption-panel
reader). Untracked, every clone on every platform behaves alike and GoodWolf makes the links per
clone (`harness.py . --links`). Tracking again was declined 2026-10-06: a Windows clone needs the
privilege anyway. A junction is never a substitute (nothing sees through it; `git ls-files` lists
files twice).
**Hit:** the Windows text-file checkout and the refusal it caused, with per-clone creation.
**Partial:** "made per clone by GoodWolf" without the Windows reason.
**Sources:** `docs/adr/0003-one-physical-home-for-skills-reached-by-link.md`; `.gitignore` comment;
`.agents/README.md`.

##### 3. Why does this repository keep `.agents/` and `docs/` apart — what decides which side a file belongs on?

**Key.** Split by when an asset is read: `.agents/` holds what an agent reads while doing the work
(skills, rules files, mechanism docs, the method's glossary, scripts) and travels to recipients;
`docs/` holds what is read while building GoodWolf (architecture, tickets, RFCs, evidence,
sessions) and a recipient replaces it whole. Splitting by subject was rejected — the seam is
unstable, the file re-mixes itself. Consequence: core may not depend on `docs/` (ADR-0002), held by
`mechanisms.py --check`.
**Hit:** reading occasion / what travels, and that a recipient replaces `docs/`. **Partial:** one of
them, or "runtime vs docs" without the travelling reason.
**Sources:** `docs/adr/0001-agents-is-runtime-docs-is-construction.md`; `docs/adr/0002-…`;
`docs/README.md`.

##### 4. Why do all sessions work in the one shared checkout on `main`, rather than each on a branch of its own?

**Key.** The question store travels through git: a branch per session comes only together with a
question store that does not (the user, 2026-10-12). q-0037.0017.0002.0001 was closed deferred —
"until separate branches per session are taken up, meanwhile nothing leaves git and sessions share
the main checkout", lean: probably the whole store moves out then. Beside it: whatever stands on
main may be published; work held back stays on its own branch (the user, 2026-10-12); keeping two
sessions out of one file is the host's job (its edit tool, a worktree where offered), GoodWolf
locks nothing and its scripts refuse a write to an entry that moved since it was read (2026-10-11).
**Hit:** the store travelling through git as the reason (deferred until branches are taken up).
**Partial:** only "the host keeps sessions apart / nothing locks", or "push each commit" (L2).
**Sources:** `docs/architecture.md` § Interruption and recovery (the straw dog bound to
q-0037.0017.0002.0001); `docs/questions/q-0037.0017.0002.0001-…` (closed:deferred, still under
`docs/questions/`); `.agents/skills/commit/SKILL.md`.

##### 5. Why is the number of questions in work at once capped, and why at eight?

**Key.** The problem stated: the person guesses a lot and closes little; a new idea said in
conversation tends to become the next thing by being the last thing said, earlier guesses are not
held in mind. The cap makes what enters work the person's word at a boundary (session start, the
person's explicit word, a unit's close); the ninth is opened and placed and waits. Eight is "on
trial", to be re-read by what it stops (decision 4, the user, 2026-10-22; a session counts in the
ring alone, 2026-10-23). No reason is recorded for the number itself beyond the trial (the outside
view in the same entry notes hoshin practice holding three to five, and eight already failure).
**Hit:** the last-idea-wins problem (or "guesses many, closes little") and eight as a trial
re-read by what it stops. **Partial:** one of these.
**Sources:** `docs/questions/q-0037.0019-…` (Where it stands; Decisions 4 and 6);
`local.rules.md` L12; `AGENTS.md` L12; `docs/tickets/01-0060-…`.

#### In flight — the item and its state

##### 6. Where does the work on giving every skill the project's voice stand right now?

**Key.** Ticket 01-0016.0030 *the voice speaks every skill that speaks*, In progress (planned
2026-10-25, re-planned the same day to one local rule). Implemented 2026-10-25 (2ad57e2, entry
contract v113): L9 cut to the voice's name and the language of the message, installed in the entry
file and as a group under every `## What the person hears`. Criteria: two of four checked; the
speech bench "not met — Lem recognised in 0 of 10, the prose plain; the person judges the voice by
talking with it"; `/verify` not passed. L9 is itself a straw dog bound to q-0037.0006.0027 (how
core ships a default a project may replace). Queue item 4.
**Hit:** In progress, rule landed, the bench criterion failed/open and verify open. **Partial:**
In progress without what is open, or the rule landed without the open criteria.
**Sources:** `docs/tickets/01-0016.0030-…`; `docs/rfc/01-0016.0030-…`; `local.rules.md` L9;
`docs/tickets/README.md` item 4; `git log` 2ad57e2, cc01e9b.

##### 7. Where does the work on telling the root README from the product document stand right now?

**Key.** Ticket 01-0040.0070 *the root README is told from the product document*, In progress
(2026-10-25: its align underway), answering q-0037.0018.0005 (open; lean the user, 2026-10-25: one
front page, the root README the mechanical copy of a hand-written marked source; Where it stands
still open). Both criteria unchecked. First item of the queue; the front page itself, q-0033.0008,
is item 2, unminted. An untracked `README.draft.md` stands at the root (uncommitted, another
session's). Parent 01-0040 Partial, `.0070` in progress.
**Hit:** In progress at its align, decision on q-0037.0018.0005 not yet landed. **Partial:** In
progress only, or the draft only.
**Sources:** `docs/tickets/01-0040.0070-…`; `docs/questions/q-0037.0018.0005-…`;
`docs/tickets/README.md` items 1–2; `README.draft.md` (untracked); `docs/tickets/01-0040-…`.

##### 8. Where does the work on making a reply's paragraphs show the principle each stands on stand, and what is left of it?

**Key.** Ticket 01-0011.0110.0020 *a paragraph shows what it stands on*, Partial: implemented and
verified 2026-10-08; what is left is the person's week of grading — two unchecked boxes (the marks
graded honest over a week of replies; at least one box naming a principle the list lacked, or the
user recording none did). The header says "three boxes wait on a fresh session's reading"; the
ticket shows two unchecked. Its RFC stays live under `docs/rfc/`. The rule now lives in the
debugging mechanism (D3, `when debug=on`; this tree has `debug=on`).
**Hit:** implemented and verified, waiting on the person's grading. **Partial:** one of them.
**Sources:** `docs/tickets/01-0011.0110.0020-…`; `docs/rfc/01-0011.0110.0020-…`;
`.agents/mechanisms/debugging/debugging.rules.md`; `local.rules.md` settings.

#### Undecided — that it is open, and who decides

##### 9. Will the way the harness changes its own rules become a mechanism of its own? Is that settled, and who settles it?

**Key.** Open: q-0037.0012.0001 *is harness self-amendment its own mechanism*, owner 01-0019;
the rule-failure register calls it "unresolved on purpose". Rung development: load-bearing,
self-improvement: the method — above both dials (L2: development=a feature, self-improvement=a
rule), so the agent settles nothing: it brings options and a recommendation, the person decides, at
an align. Its ticket 01-0019 reads Blocked (accumulating evidence before its align), though six
slices were minted 2026-10-24 from q-0037.0012.0009's accepted Where it stands and the user queued
them third on 2026-10-25.
**Hit:** open, the person decides (at an align). **Partial:** open without who decides, or who
decides without open.
**Sources:** `docs/questions/q-0037.0012.0001-…`; `docs/rule-failures.md` preamble;
`docs/tickets/01-0019-…`; `AGENTS.md` § Autonomy; `local.rules.md` L2; `docs/tickets/README.md`
item 3.

##### 10. How will core reach the projects that install it — as published releases? Is that decided, and who decides it?

**Key.** The direction is decided (the user, 2026-09-21): a change to the core–instance edge
reaches a recipient as a release — core published to a repository of its own, each publish with a
note for an instance; whether to take one is the installing agent's decision with its user. How it
is published is open: q-0037.0006.0020.0002.0002, owner 01-0010.0190, Planned; the chain
01-0010.0185 (decision-bearing, its own align precedes) → .0190 → .0195 under 01-0010.0160, none
started. Today "nothing does this yet: core is shared from the working tree". Rung development: a
product slice — above the dial: the person decides.
**Hit:** releases as the decided direction, the how open and the person's. **Partial:** open
without who decides, or the direction without its open state.
**Sources:** `docs/architecture.md` § Installing (straw dog bound to
q-0037.0006.0020.0002.0002); `docs/questions/q-0037.0006.0020.0002.0002-…`;
`docs/tickets/01-0010.0160-…`, `.0185`, `.0190`, `.0195`; `docs/tickets/README.md` item 7.

##### 11. Does the method weigh small work lighter than large work, and is it decided what weighs a change? Who decides?

**Key.** The principle stands: *Weight follows the work* — "a change costs what it weighs, in
checks, records and steps" — in the entry file, a straw dog bound to q-0037.0013.0003 (the user,
2026-10-11: one principle, not a list of exempt cases). What weighs a change is open, "if the
principle alone proves too loose"; lean 2026-10-15: part answered at q-0037.0013.0005 — a change's
path follows the method's ladder. Rung self-improvement: the method — above the dial: the person
decides.
**Hit:** principle in place, what weighs a change open, the person decides. **Partial:** two of
the three.
**Sources:** `AGENTS.md` § General rules (*Weight follows the work*);
`docs/questions/q-0037.0013.0003-…`; `AGENTS.md` § Autonomy.

#### Resting on contradictory or incomplete records — the two records

##### 12. How does a session here decide which piece of work to take up next?

**Key — two sides.**
- *Not from a written queue.* q-0037.0019 decision 7 (the user, 2026-10-25): the path is not read
  from a written queue; its candidates are its own reading; until q-0037.0019.0004 is answered they
  stand unordered and the agent recommends one with its reason — "nor the queue beside the path as a
  second source". `/recall` (straw dog bound to q-0037.0019.0004): "recommend one and say why,
  taking no order from a written queue". The person decides (product-slice rung).
- *From the queue.* `docs/tickets/README.md` is a numbered order, ten items, each "(the user,
  2026-10-25)" or earlier; `/recall`'s installed Q2 "then read the queue as this skill says";
  the ticket mechanism's doc: the queue "read by `/recall` for the order" (straw dog bound to
  q-0037.0019.0004); TICKET-FORMAT: "the order of the work" (same binding); `questions.py`'s path
  docstring: "it ranks nothing, the order being the queue's"; the queue's last line, "Next cycle
  needs a nod (`next-cycle=ask`)", names a switch the dial replaced on 2026-10-15.
**Noticed and said:** both sides, or that the queue's ordering role is being withdrawn while it
still stands. **One side:** either alone.
**Sources:** `docs/questions/q-0037.0019-…` Decisions 6–7; `docs/questions/q-0037.0019.0004-…`
(uncommitted edit, lean only); `.agents/skills/recall/SKILL.md`; `.agents/mechanisms/ticket/ticket.md`
lines 76, 117; `.agents/skills/ticket/TICKET-FORMAT.md` § The queue; `docs/tickets/README.md`;
`.agents/scripts/gw/questions.py` `path_ahead`.

##### 13. Which commands make up this project's verification set, and where are they written?

**Key — two records.** `local.rules.md` L3 (authored home): eight checks always —
`mechanisms.py`, `inject_rules.py`, `tickets.py`, `edges.py`, `maintain.py`, `questions.py`,
`sessions.py`, `product.py`, each `--check` under `uv run --offline --no-project python` — and the
`unittest discover` suite of `.agents/scripts/gw/test` when a non-markdown file changed; installed
into `/verify`, `/implement` and `/maintain`, not into the entry file. `docs/process.md`
§ Verification: "this project's four commands sit in the entry file's local block beside its
dials" — four, and in the entry file; neither holds (the entry file's local block holds L1, L2, L5,
L7, L9, L12).
**Noticed and said:** the eight-plus-tests set and that process.md says otherwise. **One side:**
either alone. **Filled the gap:** a count or home invented from neither.
**Sources:** `local.rules.md` L3; `.agents/skills/verify/SKILL.md` § The verification set;
`docs/process.md` § Verification; `AGENTS.md` § Project-local.

##### 14. What is the pacer, and where does it stand?

**Key — two records.**
- *Still to come.* `docs/pacer.md`: "Status: Idea under alignment; no skill or runtime mechanism
  adopted", its core rules recorded "until the pacer is installed and carries them";
  `docs/README.md`: process and pacer "held here until the pacer is a mechanism" (straw dog bound
  to q-0037.0013); `docs/architecture.md` § Deferred decisions: "The pacer owns turn progression";
  the ticket mechanism's two `not yet` rows, "the pacer, the installer".
- *Dissolved.* q-0037.0019 Where it stands, accepted by the user 2026-10-23: "Not the pacer. The
  pacer dissolved: the ring's rules are the practice mechanism's; a driver that runs the ring with
  judges outside the working agent is q-0037.0010.0002.0005.0001; which work comes next is this
  question's."
**Noticed and said:** both. **One side:** either alone.
**Sources:** `docs/pacer.md`; `docs/README.md`; `docs/architecture.md`;
`.agents/mechanisms/ticket/ticket.md` line 136; `docs/questions/q-0037.0019-…`.

#### Strong but hidden invariants or structures — what the code enforces, or the shape implies

##### 15. When has a decision in this project reached its home — what counts as a place where it has landed?

**Key.** The code: a decision has landed when every link after its `→` (or in a decided answer)
resolves to a file outside `docs/questions/`, `docs/tickets/` and `docs/rfc/`, or to an outside
URL. A link into a question's body, a ticket or an RFC is no home: the decision still waits there
(`is_home`, `NOT_HOMES`); `close` refuses a question whose Decisions list holds such a line; a
straw dog bound to a decided question is due only when its answer's links are all homes; the check
reports a closed live entry holding one. The governing rule (Q6, installed in `/align`) says only
"final in its durable home"; the exclusion is stated in code docstrings ("a ticket and its plan
expire once their work lands", the user, 2026-10-11) and in one done RFC
(01-0011.0110.0040.0020, "a ticket or an RFC is no home *(decision 2)*"), a dated snapshot — in no
governing doc. AGENTS.md names architecture, ADRs and glossary as the homes for load-bearing
decisions, not the exclusion.
**Recovered:** says a ticket, an RFC or a question body is not a home / the decision waits until it
links outside them, or names the code's rule. **Not:** "its durable home" restated, or a home list
without the exclusion.
**Sources:** `.agents/scripts/gw/questions.py` (`is_home`, `NOT_HOMES`, `_has_home`,
`waiting_decisions`, `close`); `.agents/mechanisms/questions/questions.rules.md` Q6;
`docs/rfc/done/01-0011.0110.0040.0020-…` line 120.

##### 16. What does a commit subject in this repository carry, beyond the word that opens it?

**Key.** The shape of the history: `STEP: <unit> — <what landed, as what is now true>; <who
authorized it>, <date>`. Of the 316 commits since 2026-10-18, 303 carry " — " after the prefix,
183 open on a question id (`q-…`) or a ticket id (`01-…`), and 275 end on "the user, 2026-MM-DD"
(539 of all 1187). Subjects are long: median 207 characters, p90 555, max 1774 — the subject is
the account; bodies hold only the co-author line, in all but 1 of the 316. No record states the unit id, the account or the
authority clause as a rule: L8 states only the step prefix from a closed list; `/commit` says to
write the subject in the project's convention, "the one it states, else … the one its recent
history keeps".
**Recovered:** names at least the authority clause ("the user, date") or the unit id after the
prefix as a regular part, read from the history. **Not:** only the step prefix, or Conventional
Commits.
**Sources:** `git log --format=%s`; `local.rules.md` L8; `.agents/skills/commit/SKILL.md`.

##### 17. What does a ticket's number tell you about the ticket?

**Key.** Stated: `01-NNNN(.NNNN)*-slug` — `01` the release (the contract the ticket serves), the
position its identity, never renumbered, a new ticket the next free position after its siblings',
live and done, "stepping by 10"; depth means "is a child of", nothing else; "the order of the work
is the queue's". The shape says more: 35 of 128 tickets stand off the step of ten, 28 of them
children inserted between siblings to stand in sequence — `.0165`, `.0167`, `.0168`, `.0171`–`.0176`
between 01-0010.0160 and .0180; `.0185`, `.0195`, `.0205`; 01-0011.0100.0011/.0012/.0015/.0017/.0018
between .0010 and .0020 — so a position also places a ticket among its siblings, which no record
says and the format's "next free position after its siblings'" and "the order is the queue's" deny;
`questions.py` says in passing that ticket positions "step by ten for their queue". Roots step
unevenly (0010, 0012, 0014, 0016–0020, 0030, 0035, 0040 … 0080); `01-0011` has no ticket file, its
children hang under the spec `docs/spec/01-0011-mechanism-shape.md`. A ticket's id bears no relation
to the id of the question it answers (01-0010.0150.0010 answers q-0037.0006.0020.0001.0004).
**Recovered:** says positions are inserted between siblings / encode sequence, or that the id is
independent of the question id and that the parent is read from the prefix — beyond restating the
format. **Not:** the format restated alone.
**Sources:** `.agents/skills/ticket/TICKET-FORMAT.md` § Numbering; `ls docs/tickets docs/tickets/done`;
`.agents/scripts/gw/questions.py` `_next_free` docstring.



### The blind run's return, whole and unedited

# Blind run: 17 questions on D:\Dev\AI\agents, answered as one of its sessions would

Entry contract: v121, 2026-10-25.

Session tag used for the wake: local_e308ebac-e37e-4fee-8436-4863e4928f00. Its wake places it at
q-0037.0006.0020.0001.0004, and this run is the first case of q-0037.0006.0020.0001.0004.0001. Nothing
was written to the repository. No store events were made, so the position was not moved.

## Answers

### 1. Why the scripts use only the standard library, with tests on unittest
The reason is how the scripts are run, not taste. The harness runs its own checks offline with
`uv run --offline --no-project python`, so there is no project environment. It also travels into
recipient trees whose dependency management it neither controls nor may disturb. A dependency
would have to resolve in every tree on first use, with no install step. The work the scripts do
(walking files, calling Git in a subprocess, scanning Markdown) needs no dependency anyway. The
price is accepted openly: test wall clock. Each case shells out to Git at about 68 ms per spawn
on Windows, and a framework with parallel runs is deliberately not taken. This was decided in
01-0010.0070's RFC on 2026-09-06, when the runtime was seen to be Python 3.14.6.
Sources: docs/adr/0004-scripts-run-on-the-standard-library-alone.md; .agents/README.md ("Mechanical
support"); local.rules.md L5 (how Python runs here).

### 2. Why the .claude/skills and .cursor/skills links are not committed
Skills live in one physical place, `.agents/skills/`, and hosts reach it through a directory
symlink. Codex reads `.agents/skills` natively. Until 2026-09-26 the links were tracked as mode
120000. That tracking caused harm: Git for Windows checks a tracked link out as a 17-byte text
file, and the harness then refused it as "a file where a link goes". An adoption-panel reader
found this when cloning on Windows. The user then decided (2026-09-26) that each clone makes its
own links and never commits them, so every clone on every platform behaves the same way. The
links are made by `harness.py . --links` or by /harness, or the person is handed the exact
elevated `mklink` command. Rejected options:
- **A junction:** nothing sees through it, and `git ls-files` lists every skill twice.
- **A junction fallback:** refused 2026-09-09.
- **Tracking again and replacing the text file:** declined 2026-10-06, because Windows still needs the privilege either way.

Both links are required, as observed 2026-09-21.
Sources: docs/adr/0003-one-physical-home-for-skills-reached-by-link.md (amendment of 2026-09-26);
.agents/README.md.

### 3. What decides whether a file goes in .agents/ or docs/
The deciding test is **when the file is read**, not what it is about.
- `.agents/` is the runtime half: what an agent reads while doing work. That means skills, rules files, mechanism docs, the method's glossary and the scripts with their tests. It travels to recipients.
- `docs/` is the construction half: what is read while building the harness. That means architecture, ADRs, tickets, RFCs, evidence, sessions, the question store and the product document. A recipient replaces it whole.

Splitting by subject was rejected because that seam keeps re-mixing. Two consequences follow:
- Core may not point at a document only one project has (ADR 0002). The `mechanisms.py --check` holds that, and L10 limits what core may name under `docs/`.
- The process itself belongs in core, not in a document.

This tree's product is the method, so `docs/architecture.md` is the method's own architecture.
L1 calls that "the instance half doing its job, not a leak". The ADR exists because this mistake
was made twice on 2026-09-09.
Sources: docs/adr/0001-agents-is-runtime-docs-is-construction.md; docs/adr/0002-core-may-not-depend-on-the-instance-half.md;
docs/README.md; local.rules.md L1 and L10.

### 4. Why all sessions share the one checkout on main
The user decided this on 2026-10-12, at the align on q-0037.0017.0002. Branches per session will
come only together with a question store that does not travel through Git. The reasoning:
- In one checkout, a branch means a worktree, and a worktree has its own copy of the store.
- Sessions in separate worktrees stop seeing each other, mint ids blind, and conflict on merge over the hand-bumped entry-contract version.
- A session registered in the main checkout's store could not use the store from its worktree; every call was refused as "not registered".

The evidence was PR #5, which carried 8 unrelated commits, and a held-back merge that `push=auto`
published. The rule that came out of it: whatever stands on the shared main may be published, and
work the person holds back stays on its own branch. A check refusing a push over other sessions'
commits was weighed and dropped, because it would stall every push. Keeping writers out of each
other's files is the host's job (its stale-write refusal, worktrees), not the harness's.
How a store outside Git would work is deferred: q-0037.0017.0002.0001, closed:deferred, "until
separate branches per session are taken up". The architecture sentence is a straw dog bound there.
Sources: docs/architecture.md ("Interruption and recovery", straw dog on q-0037.0017.0002.0001);
docs/questions/q-0037.0017.0002-how-does-a-sessions-landed-work-get-from-its-branch-into-main.md;
docs/questions/q-0037.0017.0002.0001-*.md; the wake's "deferred" list; /commit's held-back-work line.

### 5. Why work in progress is capped, and why at eight
**Why a cap.** The problem stated in q-0037.0019 is that the person guesses a lot and closes
little. A new idea tends to become the next thing simply by being the last thing said. Outside
families (Kanban/flow WIP limits, hoshin, Shape Up and others) were read through /discover. Their
strongest answers were not weighing functions but limits and cadences. Their first rung is
"simply cap what is open", and they treat unbounded work in progress as the defect itself. So the
cap and the cadence came before any weighing.

**Why eight.** No record derives the number. Decision 4 says "it is 8 on trial", set by the user
on 2026-10-22, to be "re-read by what it stops". L12 carries it "eight on trial, to be re-read by
what it stops". The only nearby figure is an outside note that hoshin practitioners say three to
five objectives and treat eight as already failure.

**Current state:**
- The cap was stepped over on its first day, 2026-10-24: ten tickets In progress, and the person took 01-0060.0010 in by their own word.
- On 2026-10-25 /maintain brought fourteen In-progress tickets down to five (commit 3d6d0af).
- The wake now shows "in work: 3".
- The wake counts tickets only, not sessions in the ring. That is deferred at q-0037.0019.0001 until the count is seen to be wrong.

Sources: local.rules.md L12; AGENTS.md L12; docs/questions/q-0037.0019-*.md (Where it stands;
decisions 1, 4, 6; "The cap's first bite"; the discover families); q-0037.0019.0001; commit 3d6d0af;
docs/sessions/0066-20261025-every-open-question-given-its-rung.md.

### 6. Where giving every skill the project's voice stands now
Ticket 01-0016.0030 ("The voice speaks every skill that speaks") is **In progress** and answers
q-0037.0009.0021.0002. It was re-planned on 2026-10-25 down to one local rule: L9 names the voice
(Lem) and the language of the person's message, and nothing more. It was implemented in commit
2ad57e2 (entry contract v113). L9 is installed in the entry file and, as a group, under every
`.agents/skills/*/SKILL.md` "## What the person hears". Core's own voice phrases were removed.
Two of four criteria are checked. Still open:
- **Criterion 3 failed:** the speech bench recognised Lem in 0 of 10 runs and the prose read plain. The note says the person judges the voice by talking with it.
- **Criterion 4:** /verify.

Nothing about it is uncommitted. L9 in local.rules.md is still wrapped as a straw dog on
q-0037.0006.0027, which asks how core ships a default answer such as the voice. The wake shows
session local_a982e585 standing on the parent question q-0037.0009.0021. The ticket is in the
path's "in work" list.
Sources: docs/tickets/01-0016.0030-the-voice-speaks-every-skill-that-speaks.md; docs/research/speech-bench/results/voice-name-alone-2026-10-25.md
(named in the ticket, not opened); git log 2ad57e2, cc01e9b, 9802c55; local.rules.md L9; the wake's
"path" and "sessions".

### 7. Where telling the root README from the product document stands now
Ticket 01-0040.0070 is **In progress**, with its align still underway. It answers q-0037.0018.0005,
which is open and struck twice; its lean is the user's of 2026-10-25. Decided at the align so far:
1. **One front page per project.** It is the root README, told from the project's product document. In this tree it also ships to recipients as `.agents/README.md`.
2. **Written by hand and checked, not generated.** This is a straw dog on q-0037.0018.0005.0001, which asks what would show it can be generated.
3. **The check runs both ways.** A paragraph that makes a claim carries marks naming its product answers. The README comes due for a re-read when the document or the edge records move.
4. **The README is the mechanical copy of a hand-written, marked source.** The product script writes it. Each paragraph is one of three kinds: a claim, an explanation or an experiment. This is a straw dog on q-0033.0010.

Later the same day the align added "measured where benefit is decided" and brought in three
front-page principles from q-0033.0008 (commits a6fd821, 38d4120). Whether those principles become
criteria has not yet been put to the user.

Still open:
- The question's "Where it stands" is not written or accepted.
- The source's path and the mark syntax are the plan's to decide.
- Both acceptance boxes are unchecked.

Session local_2f2b7d3e stands on q-0037.0018.0005. An untracked `README.draft.md` (296 lines),
rewriting the opening and adding "Where you start", is in the working tree. It is probably another
running session's work in progress; I could not attribute it.
Sources: docs/tickets/01-0040.0070-*.md; docs/questions/q-0037.0018.0005-*.md and .0001; docs/tickets/README.md (item 1);
git log a6fd821, 514e112, 89ea635, 38d4120; git status and diff README.md vs README.draft.md; the wake's
sessions; docs/sessions/rows/local_2f2b7d3e-*.

### 8. Where showing each paragraph's principle stands, and what is left
Ticket 01-0011.0110.0020 ("A paragraph shows what it stands on") is **Partial**. It answers
q-0037.0016, which is open and the most struck question in the store (8). The rule was written at
tier 1 and verified on 2026-10-08. A fresh session's first reply carried the marks without being
asked. The form then moved several times:
- The marks moved out of the text, the 💡 lamp closing the paragraph (v35 to v37).
- Header frames were added for proposed text (🧩/⚓/✏️, v56).
- The 🪢, 🛠️ and 🪶 rows were added (v57, v66, v71).
- A proposed text names its file and section (v97, the latest lean).
- Since v121 the 💡/🕯️/無 marks are installed only with debug on, as the debugging mechanism's D3. The "A paragraph shows what it stands on" text in AGENTS.md is a straw dog on q-0037.0009.0021.

**What is left:** two criteria, both about grading.
- The user grades the marks honest over a week of replies.
- At least one box (now 無) names a principle the list lacked, or the user records that none did.

Drift in the ticket:
- Its status line says "three boxes wait", but two boxes are open.
- Its Outcome still says a paragraph "opens with" the principle. Since v35 the lamp closes the paragraph.

Sources: docs/tickets/01-0011.0110.0020-a-paragraph-shows-what-it-stands-on.md;
docs/questions/q-0037.0016-*.md; AGENTS.md (straw dog q-0037.0009.0021 and installed debugging D3); git log 0357c14 (v121).

### 9. Will self-amendment become a mechanism of its own? Is that settled, and who settles it?
**Not settled.** q-0037.0012.0001 ("Is harness self-amendment its own mechanism?") is open, owned
by 01-0019, and that ticket is **Blocked** while evidence accumulates before its align. The ticket
says deliberately that the decision "waits on accumulated strikes rather than on argument". It is
to be answered from the rule-failure register. Today the register has 84 entries, but no
disposition has been made on them.
- **Case for a separate mechanism:** neither /mechanism nor /skill-up owns the occasion or the record.
- **Case against:** one wish is one shape.

Nine mechanisms are declared today, and none is for self-improvement. Self-improvement's ladder in
AGENTS.md is a straw dog bound to q-0037.0012.0001 until such a mechanism is declared.
**Who settles:** the person. The question's rung is development: load-bearing, self-improvement:
the method. The dials are development = a feature and self-improvement = a rule (L2), so it is
above both. The agent brings options and a recommendation; the person decides at 01-0019's align.
Sources: docs/questions/q-0037.0012.0001-*.md; docs/tickets/01-0019-harness-amends-itself-by-explicit-meta-rules.md;
`questions.py --tree q-0037.0012`; AGENTS.md Autonomy and its straw dog; local.rules.md L2;
docs/rule-failures.md (84 headings); ls .agents/mechanisms.

### 10. How core will reach recipient projects: as releases? Decided, and by whom?
**The direction is decided.** Core reaches a recipient as a release: core published to a
repository of its own, each publish carrying a note written for an instance. A recipient reads the
notes between its ref and the latest. Whether to take them is the installing agent's decision with
its user, never the script's. The user decided this on 2026-09-21: releases had been refused on
Occam at 01-0010.0130, were reopened on new evidence, and were aligned on 01-0010.0160.

**Nothing does it yet.** The architecture's straw dog says core is shared from the working tree and
an update crosses edge changes silently. How core is published is open:
- q-0037.0006.0020.0002.0002, never struck, with three sub-questions: whether the adoption panel gates a publish, whether history is mirrored or each release is one commit, and whether the first publish is a baseline.
- Ticket 01-0010.0190, Planned, after 01-0010.0185 and before 01-0010.0195, as item 7 in the written queue.
- The destination is this repository's own answer, a local rule.

**Who decides:** the person. Its rung is development: a product slice, which is above the dial.
Sources: docs/architecture.md ("The edge, and what crosses it" plus the straw dog on q-0037.0006.0020.0002.0002);
docs/spec/01-0010.0130-harness-installs-into-another-tree.md ("Releases, reopened on evidence");
docs/tickets/01-0010.0190-core-is-published-as-a-release.md; the question file and the wake listing for it;
docs/tickets/README.md item 7.

### 11. Does the method weigh small work lighter than large? Is it decided what weighs a change? Who decides?
**The principle is decided; the measure is not.** "Weight follows the work: a change costs what it
weighs — in checks, records and steps" is a general rule in AGENTS.md since v64. The user chose one
principle over a list of exempt cases on 2026-10-11. It is a straw dog on q-0037.0013.0003 ("How
does the method lighten for small work and weigh more for large?"), which is open. Product answer
A45, "Work weighed to its shape", is in progress.

Some of the weighing is concrete:
- A change's path follows the method's ladder: a decision's rung is read from what it decides, and the dial says who settles it (q-0037.0013.0005).
- /impact tells load-bearing work, which goes to an align on its question, from mechanical work, which becomes a ticket.
- L3 runs the tests only when a non-markdown file changed.

**Still open:** "what weighs a change, if the principle alone proves too loose".
**Who decides:** the person. Its rung is self-improvement: the method, above the dial (a rule).
Sources: AGENTS.md ("Weight follows the work", straw dog q-0037.0013.0003; Autonomy; Helpers /impact);
docs/questions/q-0037.0013.0003-*.md; the wake's lean on q-0037.0013.0005; docs/product.md row A45; local.rules.md L3.

### 12. How a session decides which piece of work to take next
1. It runs /recall first, whatever the message (S6). /recall reads the wake: other sessions' positions, suspect entries, deferrals that may be due, straw dogs that are due, and **the path**.
2. It reads the live tickets with `tickets.py --list` (P12), plus git status and the log.
3. The first item is an open ticket whose work has landed but whose criteria are unchecked.
4. Otherwise the path's candidates are read: what is in work against L12's cap, what was touched lately with no ticket, tickets Ready in id order "none ranked above another", the most-struck questions, and the roots' balance (q-0033 and q-0038 are "thin").
5. By q-0037.0019 decision 7 (the user, 2026-10-25), the order is not read from a written queue. The candidates stand unordered, and the agent recommends one with its reason, said as what it would give the person. In /recall this is a straw dog on q-0037.0019.0004.

Some limits apply:
- Nothing another running session stands on is re-ranked (S1).
- A unit another session holds is not continued without the person's word (S9).
- New work enters only at a boundary core holds: the session's start, the person's word, or a unit's close (decision 6).
- "What gets built next" is the rung "a product slice", above the dial, so the person decides.

Drift: `docs/tickets/README.md` still holds a numbered order with the user's dates. It ends with
"Next cycle needs a nod (`next-cycle=ask`)", a switch the dial replaced on 2026-10-15.
Sources: .agents/skills/recall/SKILL.md (S1, Q2, P12, straw dog q-0037.0019.0004); AGENTS.md S6, S9, L12, Autonomy;
docs/questions/q-0037.0019-*.md decisions 6–7; `questions.py --path`; docs/tickets/README.md.

### 13. The verification set, and where it is written
The checks always run. The tests run too when the work changed a non-markdown file (the question
store's own writes aside). The checks:
```
uv run --offline --no-project python .agents/scripts/gw/mechanisms.py --check
uv run --offline --no-project python .agents/scripts/gw/inject_rules.py --check
uv run --offline --no-project python .agents/scripts/gw/tickets.py --check
uv run --offline --no-project python .agents/scripts/gw/edges.py --check
uv run --offline --no-project python .agents/scripts/gw/maintain.py --check
uv run --offline --no-project python .agents/scripts/gw/questions.py --check
uv run --offline --no-project python .agents/scripts/gw/sessions.py --check
uv run --offline --no-project python .agents/scripts/gw/product.py --check
```
The tests:
`uv run --offline --no-project python -m unittest discover -s .agents/scripts/gw/test -p "test_*.py"`.

It is written once, as rule L3 in `local.rules.md`. The installer copies it into the local blocks
of `.agents/skills/verify/SKILL.md` ("## The verification set"), `implement/SKILL.md` and
`maintain/SKILL.md`, and into no document. L3 is a straw dog on q-0037.0006.0022.0001, which asks
where a project's verification set lives and what shape it takes.
Sources: local.rules.md L3; .agents/skills/verify/SKILL.md lines 34–54; local blocks in implement and maintain;
the wake's lean on q-0037.0006.0022.

### 14. What the pacer is, and where it stands
The pacer was a proposed agency over turn progression: how a "do the next thing" request turns
into a bounded execution step, at which scale, and when to continue, repeat, decompose, go back
upstream or ask. It also covered resume state between /conclude and /recall. `docs/pacer.md` still
says "Idea under alignment; no skill or runtime mechanism adopted." Its rules that were settled
moved out: "a turn holds at most one execution step", and every wake starts with /recall (AGENTS.md since v9).

**It is dissolved.** q-0037.0019's "Not the pacer" splits its job three ways:
- The ring's rules belong to the practice mechanism, and a driver that runs the ring is q-0037.0010.0002.0005.0001.
- Which work comes next belongs to the pathfinder (q-0037.0019, ticket 01-0060).
- Where a session resumes belongs to the session mechanism.

Drift, three places that have not caught up:
- docs/pacer.md's status line.
- docs/architecture.md's "Deferred decisions" still says "The pacer owns turn progression".
- docs/README.md's straw dog on q-0037.0013 still says process.md and pacer.md are "held here until the pacer is a mechanism".

Sources: docs/pacer.md; docs/questions/q-0037.0019-*.md ("Not the pacer"); docs/architecture.md; docs/README.md; docs/glossary.md (unit).

### 15. When a decision has reached its home
A decision forms in the body of the question it answers. It lands as it is made, with its
provenance (who, when). Its home depends on the kind of decision:
- A load-bearing decision lands in the project's architecture, ADRs or glossary.
- A decision about a mechanism lands in that mechanism's doc, and what was refuted goes in its evidence.
- An instruction lands in the entry file, a skill or a rules file. A document only informs.
- A principle lands in the entry file's general section, a mechanism's doc or the glossary.
- A rule lands in its mechanism's rules file, then is installed.
- A product decision lands in the product document, through /product (U2).

It is final in that home only where no open question's answer could change its form or its home.
Otherwise it lands as a straw dog bound to the nearest open ancestor question that could. A
decision with nowhere to land yet stays as a line in the `## Decisions` list of the lowest question
holding everyone who needs it, and takes "→ <link>" when it lands. The question is then closed
`decided` against where it landed, and entries closed against the list are repointed there. A
decision not to do something that nothing instructs lands in its question alone.
Sources: AGENTS.md ("Document load-bearing", "A document informs", "Straw dogs"); /align and /questions Q6 (installed by questions);
.agents/skills/questions/SKILL.md ("A raised question"); .agents/glossary.md (principle, rule); /align U2.

### 16. What a commit subject carries beyond the opening word
L8 requires one prefix naming the loop step, from a closed list: ALIGN, TICKET, PLAN, IMPLEMENT,
VERIFY, MAINTAIN, DISCOVER, RECALL, CONCLUDE, FIX, EQUIP, DREAM. After it, the history shows a steady
convention:
- The unit's id, then " — ": a ticket (`01-0010.0230 —`), a question (`q-0033.0008 —`) or an entry-contract version (`v121 —`). 180 of the last 300 subjects open this way.
- What is now true, in prose, with each decision separated by semicolons. Where the work spans two steps, the bleed is named, as L8 asks.
- A closing provenance, "; the user, 2026-10-25". 261 of the last 300 end this way.

Rules: no sessions are named (/commit). The Co-Authored-By line goes in the body.
**Possible drift, not run:** /commit's subject line was reworded in 6308d1d. Both
`local.rules.md` and `.agents/mechanisms/session/session.rules.md` still anchor on the old text,
"- Write the subject in the project's own convention, where it states one.". The installer needs
an exact, unique anchor line (`inject_rules.py` after_anchor). So `inject_rules.py --check` may
refuse. I was not allowed to run it.
Sources: .agents/skills/commit/SKILL.md (L8, S5); local.rules.md L8 and its anchor table; `git log -300 --format=%s` counted;
git show 6308d1d; inject_rules.py lines 664–678.

### 17. What a ticket's number tells you
In `01-0090.0030-slug`:
- **`01`** is the release: the contract the ticket serves. A release closes when its criteria are met, not on a date.
- **The four-digit position** is the ticket's identity. It is never changed and never renumbered. New positions take the next free slot after the siblings, live or done, stepping by 10.
- **An appended position (`.0030`)** means "is a child of" and nothing else. Depth is unbounded.

The number says nothing about order. "The order of the work is the queue's", and now the path's.
The ticket and its RFC share the basename. A finished ticket moves to `done/` with the same name.
Older positions such as .0168, .0172 and .0175 show that the step of 10 has not always held.
Sources: .agents/skills/ticket/TICKET-FORMAT.md ("Numbering", "One basename per work item"); `tickets.py --list`.

## How I searched

**Harness calls, all allowed and read-only:**
- `questions.py --wake --session local_e308ebac-…`. Output was about 65 KB: the most-struck questions, 8 running sessions, 5 deferrals, 0 due straw dogs, 1 suspect entry, the path (in work 3, touched lately 6, Ready 5, roots), this session's position q-0037.0006.0020.0001.0004 and its root-to-current path, the frontier, and every open question under q-0037 with its lean. This one call answered or pointed to most questions: 4, 5, 9, 10, 11, 12 and 13 by lean lines.
- `tickets.py --list`: 52 live tickets with status and their Answers question. Gave me the units for 6, 7, 8, 9 and 10.
- `questions.py --tree q-0037.0012`: the self-amendment subtree (Q9).
- `questions.py --path`: the path alone (Q12).
- `questions.py --check`: 303 entries, 0 diagnostics, 86 findings (relative ids, possible duplicates, a session row standing on a closed question).
- `tickets.py --check`: 0 diagnostics.

**Files read (about 45), whole or in part:**
- Instructions: AGENTS.md (in context), .agents/skills/recall/SKILL.md, local.rules.md.
- ADRs and READMEs: docs/adr/0001–0004 (4), .agents/README.md, docs/README.md.
- Architecture and process: docs/architecture.md, docs/pacer.md, docs/product.md (rows A1–A50 region), docs/tickets/README.md.
- Questions: q-0037.0017.0002, q-0037.0017.0002.0001, q-0037.0019 (head, decisions, cap and cadence sections, grep of the rest), q-0037.0019.0001 and done q-0037.0019.0002 (grep), q-0037.0018.0005, q-0037.0018.0005.0001, q-0037.0016 (head and later sections), q-0037.0012.0001, q-0037.0006.0020.0002.0002, q-0037.0013.0003.
- Tickets and spec: 01-0016.0030, 01-0040.0070, 01-0011.0110.0020, 01-0019, 01-0010.0190 (most of it), docs/spec/01-0010.0130 (releases section).
- Skills and formats: .agents/skills/commit/SKILL.md, verify/SKILL.md (grep), implement and maintain (grep), align/SKILL.md (Q6 region), questions/SKILL.md ("A raised question"), .agents/skills/ticket/TICKET-FORMAT.md (Numbering, fields).
- Glossaries: .agents/glossary.md (grep), docs/glossary.md (grep).
- Other: docs/rule-failures.md (headings), .agents/scripts/gw/inject_rules.py (grep), docs/sessions/0063, 0064, 0066 (grep), 3 session rows, README.md and README.draft.md (head and diff).

**Searches:** about 12 greps.
- "standard library|stdlib|unittest".
- eight/cap/limit in q-0037.0019 and the sessions.
- "durable home|lands in" in the glossary and skills.
- "subject" across .agents.
- anchor logic in inject_rules.py.
- release in the spec.
- A45 in product.md.
- pacer in the glossaries.

**Git (read-only):** log (-40, by ticket id grep, subject statistics over 300), show 6308d1d,
diff --stat and diff of the uncommitted tickets and questions, log for commit/SKILL.md.

**Tool calls:** about 42.

**Where the harness helped:**
- The wake and `tickets.py --list` were the map. Every "where does X stand" question (6–10) resolved to a ticket and a question in two calls. The lean lines often carried the answer and who decided it, with a date.
- The rung on each question file, read against L2's dials, answered every "who decides" mechanically (9, 10, 11, 12).
- The ADRs answered the "why" questions (1–3) outright.
- Straw-dog bindings pointed each provisional sentence at the question that would change it (4, 13, 11).

**Where it did not:**
- "Why eight" has no derivation anywhere. The record says only "on trial".
- The wake's output was too large to read in one go; I had to read it from a saved file in chunks.
- `--check` prints JSON with no summary line.
- Several records lag what they are about: docs/pacer.md, the architecture's pacer line, docs/tickets/README.md's written order and `next-cycle=ask`, 01-0011.0110.0020's status line and Outcome, 01-0019's "the register has one entry", and the voice question's lean pointing at q-0037.0002 as open though it is done.
- The stale anchor in local.rules.md and session.rules.md (Q16) may make `inject_rules.py --check` fail. I could not confirm it within the allowed calls.
- The commit convention beyond the prefix (unit id, provenance tail) is kept by history alone and stated nowhere.
- `README.draft.md` cannot be traced to a session from the rows.

**Housekeeping:** one scratch file (qcheck.json) was first written to the scratchpad root by
mistake. I moved it into meeting-self/blind/ straight away.
