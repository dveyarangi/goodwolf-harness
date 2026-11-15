# A tree's standing sessions each answer for an area, and the cut is kept true — implementation plan

- **record of** what it intends to become

**Authored:** 2026-11-15
**Last amended:** 2026-11-15, after two validations by a judge that did not write it

Implements [01-0090](../tickets/01-0090-standing-sessions-each-answer-for-an-area.md).

## What it keeps

[q-ja5mp4](../questions/q-ja5mp4-does-the-method-have-one-session-direct-the-others-an-orchestrator-and-what-does-it-owe-the-sessions-it.md),
*Where it stands* as accepted on 2026-11-15, and its decisions 1, 2, 4, 5 and 6: no session
directs the others; the way of working is reproducible, each step in the journal; core ships the
keeper of the harness as the default role; one record holds the tree's roles, each with its name,
its map and its brief; the standing sessions are the session mechanism's part, kept apart, its
skill `/pack`. The roles of this tree are
[q-dyc63i](../questions/q-dyc63i-which-standing-roles-does-this-tree-have-where-every-session-develops-the-harness-itself.md)'s
decision 1. Until stage 1 lands the doc's section, the accepted *Where it stands* is the durable
owner of every shape below; each choice names the line of it that it keeps.

## Where the plan reads an accepted line one way

Six readings the person sees before the plan is accepted; each is the narrowest that the code
and the records allow, and the last has an alternative.

1. **"A section of its doc"** is a subsection of *How it works*, `### Standing sessions`, holding
   all of the part's prose. Its rows stand in the doc's shared tables and its skill in the header:
   the shape check reads one table under each heading and finds a skill by the header's bullet,
   so a table of the part's own would declare nothing. The part leaves by moving the subsection,
   its rows and its rules — more than a move of one block, and all the format admits.
2. **"One record — the tree's roles"** is one file, `docs/roles.md`, a section per role. A
   session with a role reads the others' maps too: they are how it knows whose area a path
   outside its own is in.
3. **The brief stands in that record**, and reaches a session only through the rule that reads
   it (S10). The opening words of
   [q-mvd4pi](../questions/q-mvd4pi-how-does-a-session-take-on-a-standing-role-learn-it-and-hand-it-on-so-the-role-outlives-any-one-chat.md)
   place a brief in a skill or a rules file; decision 5 and the accepted whole, later and the
   person's, place it in the record, and the plan follows them — without decision 5's holder,
   which the accepted whole dropped. S10 is bound to that question.
4. **"The harness offers to start the default session"**: on a yes, the session the install ran
   in takes the keeper's role, unless the person names another chat for it. `/pack` starts none.
   The offer is a sentence in the reply that says the install is ready and asks for no answer,
   so it stands in no order with the first question the work asks.
5. **"Its own area whole"** is a bound and no reading list: the session's reading stays inside
   its map, and nothing has it read the whole of its area at its wake. Read whole, the keeper's
   area alone is more than any free session reads, and the whole's fourth test asks for less.
6. **Two files have two writers.** The session mechanism's doc and rules file are written by the
   session that keeps the rows and by the one that keeps this part, each its own passages, each
   telling the other before it lands.
   [q-dyc63i](../questions/q-dyc63i-which-standing-roles-does-this-tree-have-where-every-session-develops-the-harness-itself.md)'s
   decision 1 has an owner hand a change in another's mechanism to its owner; the alternative
   that keeps it to the letter is the keeper handing the part's passages to the rows' session to
   land. The plan takes the first: the part's text is shown to the person by the session that
   wrote it and lands on their word, with no session between; decision 6 named what the overlap
   would show — collisions repeating there call for the part to leave.

## The shape

**The part's files are its own.** *Keeps:* decision 6.

| part | where |
|---|---|
| the pack's instruction file | `.agents/skills/pack/SKILL.md` |
| the roles' format shelf | `.agents/skills/pack/ROLES-FORMAT.md` |
| the default role's shelf | `.agents/skills/pack/KEEPER.md` |
| the roles' script | `.agents/scripts/gw/roles.py` |
| its tests | `.agents/scripts/gw/test/test_roles.py` |

In the files the session mechanism already has, the part adds: a header bullet for the skill, the
subsection, rows at the ends of the *Moments* and parts tables, bullets under *What it produces*,
the whole's four tests under the grading, a sentence on what retires the part — a host that keeps
its sessions' areas itself, or its leaving as a mechanism — and three rules after the last one.
Nothing in the rows' script changes.

**Two files have two writers**, by the sixth reading: this tree's roles name each of the two
files in both maps, each entry narrowed by words to its own passages. The shape check's script
has been changed by both sessions; the one line the plan adds to it is told with them.

**The record: `docs/roles.md`.** The format is the shelf's:

- the title, and `- **record of** what must always hold` — the cut is the person's decision and
  changes only by one; a map that names something gone is redrawn by decision, never regenerated;
- a `## ` section per role, headed by the role's name, and no other `## ` section: every one is
  read as a role;
- `### Owns` — the map, a bullet each: a path or a path pattern in a code span, a mechanism by
  its slug, a question by its link, standing for the questions under it, or, for what no path
  names — the landing on main —, words; words after an entry narrow it to a part of what it
  names;
- `### Brief` — prose a successor reads without the chat that held the role before.

It names no session. *Keeps:* "the record … names no session". Tier 2: read when a session
takes a role and when `/pack` reads the cut. A role's section is removed when the person closes
the role. One session writes the file — the one whose map holds it, the keeper where a tree has
one: another role's session hands it a change to its own brief, so no two sessions' lines meet
there.

**The check: `roles.py --check`, the format and nothing of the content.** It refuses a file
without the kind's mark, and a role whose heading is empty, with no bullet under `### Owns`, or
with an empty `### Brief`. A tree with no `docs/roles.md`, or with one that holds no role, has
nothing to check and passes: a tree with one session needs no roles. It does not rule on two maps that overlap — an overlap may be the cut
the person chose — nor on a map entry that names nothing: a check that failed there would refuse
one role's push over a path it moved inside its own area, on a record another role keeps. Both
are `/pack`'s read. The script reads the tree's files alone and nothing of the question store.
*Keeps:* the ticket's second criterion; R1.

**Where the check runs:** the push's list in `harness.py` (`PUSH_CHECKS`), a rule installed into
`/maintain` (S12), and this tree's L3. Not the install skill's list of checks, which does not
carry the rows' check either. A script of its own rather than a call inside `sessions.py --check`:
the rows' script is bound for the server
([01-0010.0250.0090](../tickets/01-0010.0250.0090-the-rows-live-in-a-database.md)) in another
session's hands.

**`/pack`.** Its description names the use cases and nothing else: standing sessions step on each
other; the person asks which standing sessions the project needs or whether its cut still fits;
a session is given a standing role; a freshly installed tree's person accepts its default
session. Its body carries `## Installed from other mechanisms` before `## What the person hears`,
so the tree's local block there stays the last.

- *Sessions step on each other.* It reads what the tree keeps — the rows, the session records,
  git history, the roles — the sessions' own words where the host lets one session ask another,
  and an outside read by a subagent given the evidence and not its guess, and says which areas
  overlapped. One collision is mended where it happened; a second in the same area brings a
  proposal — the code or the records separated, the map redrawn, or a new role named for what it
  answers for. *A second* is the plan's value for "repeated", wrapped as a straw dog bound to
  [q-jz3mlm](../questions/q-jz3mlm-how-does-a-project-cut-its-work-into-standing-sessions-and-how-does-the-cut-change-as-the-project-grows.md),
  which sets it after the first read of this tree.
- *The cut is read against the work.* The sessions the person actually runs — the rows, the
  session records, the host's list of sessions where it gives one, and the person's word, since
  no commit names its session — against the roles: a role to open, to close, two to merge.
- *The default session accepted.* It writes the keeper's role from `KEEPER.md`, fitted to the
  tree, and the session takes it by S10.
- *A session takes a role.* S10, installed here as in `/recall`.

It recommends, and the record is written only on the person's decision, by the session that
keeps it; it starts and ends no session, hands out no work, and writes nothing in another role's
area.
*Keeps:* "`/pack` recommends and the person decides"; *Its moments*.

**The default role's shelf, `KEEPER.md`.** The keeper of the harness as core ships it to a tree
where the harness serves another product: its map — core's directory, the entry file, the local
rules file, the rule-failure register, the roles — and its brief: the updates from core, what the
sweep leaves, the tree's own rules, the sessions beside it; it directs no work and brings what
crosses areas to the person. The landing on main stays folded into it, as decision 4 has it for
a small tree, until
[q-7ebz2f](../questions/q-7ebz2f-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of-sessions.md)
says how landing is done. Its text is wrapped as a straw dog bound to
[q-wit7by](../questions/q-wit7by-what-does-a-fresh-tree-under-the-harness-need-to-set-up-standing-sessions-by-itself.md).
*Keeps:* *Two trees, one skill*; decision 4.

**Three rules, none in the entry file.** The impact of the split counted two; the third is what
`/maintain` is owed for any record (M1).

| id | read at | targets | anchor |
|---|---|---|---|
| S10 | a session is given a role, at its wake or mid-chat | `.agents/skills/recall/SKILL.md`, `.agents/skills/pack/SKILL.md` | `## Installed from other mechanisms` |
| S11 | the first install has closed | `.agents/skills/harness/SKILL.md` | `## After the first install` |
| S12 | the maintain pass | `.agents/skills/maintain/SKILL.md` | `## Installed from other mechanisms` |

- **S10** — a session the person gives a role reads that role's section of the record first, its
  brief and its map, and the other roles' maps; what its wake then reads — the path, the last
  session, the questions and the docs that bear on the work — it reads inside its map, and
  outside it only what the work in hand asks; it names the role in its title where the host lets
  a session name itself. The map bounds the reading; nothing asks the session to read its area
  whole. The role comes by the person's word alone: no row or title is read for it. Wrapped
  around its section as a straw dog bound to q-mvd4pi. *Keeps:* "A session takes a role"; the
  second reason — a session holds its own area and is not cluttered by the rest.
- **S11** — in the reply that says the install is ready, offer the default session in one
  sentence that asks for no answer: something a tree with more than one standing session wants;
  a yes is carried out through `/pack`, and silence or a no writes nothing and is not followed
  up.
  Wrapped around its section as a straw dog bound to q-wit7by. The anchor is a heading of the
  install's skill, named in the doc's *Relies on* so a renamed heading fails the check; that
  skill names `/pack` nowhere in its own text (R8). *Keeps:* "offered, never required".
- **S12** — check the roles with `roles.py --check`; a diagnostic is a finding. A rule of its own
  rather than a clause in S3, so the part's rules leave with it.

What every session pays: one more skill description, and S10's paragraph in `/recall`, which
every conversation reads. The entry file does not change, and its contract's version stands.

**The method's glossary** gains *Role*: an area of the work one standing session answers for
across chats — its name, the map of what it owns, its brief; never what an agent is granted at
its start. Wrapped as a straw dog bound to
[q-p4sdnv](../questions/q-p4sdnv-what-is-an-agent-role-and-which-mechanism-keeps-roles.md).

## Docs, first

The session mechanism's doc is the architecture here; each stage writes its part of it before
the thing it describes, and a row lands with the part it names, never ahead of it.

## Stages

Each stage ends with the checks green, and with the tests green where it changed a file that is
not markdown. Every instruction's text — the skill's, each shelf's, each rule's — is drafted
through `/skill-up` and shown to the person before it lands. Each stage writes its step into
[the journal](../research/standing-sessions-journal.md).

0. **The cheapest example first.** Before anything is built: this tree's roles written to the
   format in the scratchpad, and a fresh subagent handed them and the draft of `/pack`'s first
   moment, in the clone the first proof below describes — does it name the overlapping area and
   a way to separate it? A no reopens the record's form before a script is written around it.
1. **The declaration, the skill, its shelves and S10.** The doc's header bullet,
   subsection, the rows of the three moments the skill instructs, the skill's and shelves' parts,
   the relied-on heading, the sentence on the row's seam made true, the roles and `/pack`'s
   report under *What it produces*, the four
   tests, what retires the part; the glossary's entry; the skill and its two shelves, naming no
   check yet; `docs/roles.md` added to the shape check's painted doors beside a `TODO` naming
   q-la5n2i; S10 in the rules file with its row, installed before the doc is checked, and the
   local file installed again for the new skill's own block. Proof: `mechanisms.py --check` and
   `inject_rules.py --check` pass; the tests pass.
2. **The record's check.** `test_roles.py` first, each refusal watched to fail in both
   polarities — a file without its mark; a role lacking its name, its map, its brief; a tree with
   no file passing; a push that carries a role without its brief refused — then `roles.py`, its
   parts' rows and the check's moment in the doc, the format shelf's sentence naming the check,
   `PUSH_CHECKS`, S12 and S11 with their rows, and L3 through the local file and the installer,
   which re-renders its block in `/verify`, `/implement` and `/maintain`. The offer at install
   lands here and not before, so no ref offers a record that nothing checks; between the two
   stages `/pack` can write one, checked from the next ref. The run over what exists: no prior
   corpus, stated so.
3. **This tree.** `/pack` is run here: the sessions the person actually runs, and this tree's
   roles written to the record — core's keeper, the merging, and an owner for each family of
   mechanisms a standing session holds — each shown, the cut the person's; `docs/README.md`
   names the file. Then the judged tests below.

## What proves the criteria

| criterion | proof |
|---|---|
| the morning's collision named untold | a fresh subagent running `/pack` in a clone that holds no ref later than `e1b2ec36` — the second of the two commits that met in the questions and the session mechanisms' docs, `3a15e79a` the first — with every file that tells the collision put back to its state before `3a15e79a`, the journal first, the two sessions' rows copied in as they stand and the part's files added; it is given the words "two sessions collided this morning" and nothing else. What tells the collision is withheld by construction, and what shows it — the two commits — is there. A second subagent, given the collision's true account, judges the area and the way to separate it |
| the roles record and its check | `docs/roles.md` in this tree; `test_roles.py`; the check run over it |
| the sessions actually run, a role only where a collision came twice | `/pack`'s report at stage 3, judged by the person |
| a role's session reads its own first, counted | two fresh subagents handed what a session is handed at its start, one given a role by word, one free, the same question from that role's area; the count is the token total the host reports for each subagent, with the files each says it read, their bytes summed from the tree, beside it as its own account; a third judges both answers. Both numbers are reported whichever way they fall |
| the default session offered, a no leaves nothing | a fresh subagent given a freshly installed, committed tree and the install's skill alone: its reply that the install is ready carries the offer once; answered no, and again with no answer, the tree's status is unchanged |
| the declaration holds the part | `mechanisms.py --check`, and `/verify`'s read of the doc's tables against the part's files, since the check holds no shelf and no moment's row to anything |
| texts shown before landing | each under its header in the reply before the commit that lands it |
| `/verify` | the pass itself |

## Impact

**Impact.** Five new files of the part; the session mechanism's doc and rules file; the method's
glossary; the shape check's list of painted doors; the push's list of checks; the install's
skill, by one installed block; `/recall` and `/maintain`, by their installed blocks; this tree's
local rules, with their block in `/verify`, `/implement` and `/maintain`; `docs/README.md` and
one new record.

**Hidden edges.**

- The two files with two writers, and the shape check's script, above.
- A subsection inside *How it works* is new to the mechanisms' docs: the format leaves that
  section's prose unparsed and the check refuses no heading there, and no doc has one yet.
- A skill whose `## Installed from other mechanisms` followed its `## What the person hears`
  would put a mechanism's block after the local one, refused here and in every recipient that
  installs a local rule into every skill's closing section; the order is fixed above.
- A recipient whose local block in the install's skill stands in a section before
  `## After the first install` is refused at its update until its local anchor moves. game-delta
  has no local rule in that file, and this tree's stands after it. The other recipients are not
  read; their keepers are told the ref.
- A recipient that already keeps a `docs/roles.md` of its own in another form is refused at its
  next push. game-delta has none; the others are asked when the ref is told.
- A new check is wired by hand in two lists, which go when each mechanism's records carry them.
  A pushed commit that predates the script runs the other checks and says so.
- Whether a host lists a new skill before a new chat is not known; the judged tests run in fresh
  subagents either way.
- game-delta keeps its roles in local rules, which will stand beside core's record.
- The count for a session with a role may move little: both are handed the same window, and the
  rule narrows only what the wake reads
  ([q-gus5k2](../questions/q-gus5k2-how-is-each-areas-knowledge-kept-apart-so-a-session-holds-its-own-areas-context-and-the-boundary-stays.md)).
- The doc's sentence that the row admits a role as a seam says more than the rows' script does:
  the row's form ends at the unit it holds. The rows' session, told, left the sentence to this
  plan; stage 1 rewrites it, inside its straw dog, to what the script holds — the row admits
  neither a role nor a lock yet. A field for a role is asked of the rows' session when one is
  needed.
- `/maintain`'s marks for the session mechanism, the shape and the install go stale as their
  parts move; the next pass re-marks them, and its check does not fail meanwhile.

**Leave alone.** `sessions.py` and its tests; the rows, the holds, the window and the wake; S1 to
S9; the entry file; the install skill's own text; a role's rights and skill set; recipients'
local rules.

**Recommendation.** Proceed, in the three stages after the example of stage 0.

## Limits and follow-ups

- Which session holds a role is said by its title alone, and no rule reads a title, until the row
  has a field ([01-0010.0250.0090](../tickets/01-0010.0250.0090-the-rows-live-in-a-database.md)).
- A brief is rewritten by the session that keeps the record, at the person's word, until
  q-mvd4pi says how a role is handed on, and where a brief lives.
- The lander as a role of its own waits on q-7ebz2f.
- The window per role's area, where most of the reading is saved, is q-gus5k2's.
