# q-ja5mp4 Does the method have one session direct the others - an orchestrator - and what does it owe the sessions it directs?

- **record of** what it intends to become
- **part of** q-zxnc6y
- **state** open
- **owner** [01-0090](../tickets/01-0090-standing-sessions-each-answer-for-an-area.md)
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-15T00:05:13Z
- **struck** 0, last 2026-11-15T00:05Z

The user, 2026-11-15: ask the orchestrator session of game-delta how it works with agents and
sessions, which problems arose and were solved and which were not, and have it ask the sessions it
directs where its orchestration is missing or too much — an audit by those it directs; then weigh
what this harness should add or change, and whether such a way of working is wanted at all.
Widened the same day: how well the harness's mechanisms hold in such work — its rules, the
question store and the others — and how often sessions collide.

Evidence: [an outside read of game-delta](../research/game-delta-orchestration-audit-2026-11-15.md),
2026-11-15 — nine sessions in one shared tree and index; a commit carrying another session's lines
8 times, master red for every session at least 5 times, 4 id collisions under hand-given ids.
The orchestrator's own report with all eight sessions' answers, 2026-11-15:
`D:\Dev\workspaces\games_workspace\game-delta\docs\sessions\orchestration-report-2026-11-15.md`
(game-delta f24efe9). Both reads agree the shared checkout is the root of most friction; the
orchestrator there directs no work — each session works its area with the person — it keeps the
rules, arbitrates stray lines and broadcasts rules; all eight sessions name the reply's form as
the main excess.

Options:

1. **No directing session in the method.** The person stays the one judge; areas per session stay
   a project's practice; what the orchestrator does by hand becomes mechanism in core — a worktree
   per writing session with one lander, ids no session hands out, a notice of changed rules to
   running sessions, the scheduled sweep.
2. **An orchestrator role in core**, with its duties — rules, ids, arbitration, the survey of the
   sessions it serves.
3. **As it is**: each project decides alone.
4. **A keeper of the harness as one area among the others**, raised by the user 2026-11-15 ("нужна
   сессия которая будет ответственна за правки харнесса и арбитраж, не? … какие-то части ее это
   безусловно механизмы"). It directs no work. It owns the rules, the mechanisms, the rule-failure
   register and the updates from core; the other sessions register a failure and hand its
   amendment to it rather than land it themselves. Its arbitration is finding where areas
   collide — contradicting records, a boundary gone stale — and bringing each to the person as a
   decision, never settling one on another area's question. Merging into main is a second
   such area, the lander. Mechanism takes what needs no judgement: ids, lines kept apart by a
   worktree per writing session, landing through the lander, a notice of changed rules to running
   sessions, the scheduled sweep.

Recommendation: 4 — one writer of the rules ends the stream of amendments landing mid-work from
many hands; arbitration as deciding stays the person's, and arbitration as finding needs one
session that reads across areas; what option 1 gave to mechanism stays mechanism.

## Decisions

1. **Option 4: a keeper of the harness, one area among the others** — the user, 2026-11-15:
   "давай сразу начнем, прям с тебя, ты будешь одной из сессией из нового способа работы нашего
   харнесса. мы будем его предлагать." The way of working is built first in this tree, with the
   session local_aa6167bc as its first keeper, and offered to every tree.
2. **Reproducible, not added and forgotten** — the user, same message: how it was built is
   written down step by step, each step with the rule a fresh tree under the harness would need to
   set itself up the same way; the cut into sessions differs between projects and changes as a
   project grows, and onboarding is not to be lost. The journal:
   [standing-sessions-journal.md](../research/standing-sessions-journal.md).
3. **The keeper does not raise the coordinator.** The first call that finds none raises it
   ([q-7ebz2f](q-7ebz2f-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of-sessions.md),
   decision 9), so no session is the server's single point of failure; the keeper sees that it
   runs, and its address across machines is the person's.

Neighbours: [q-psa5ha](q-psa5ha-how-do-sessions-hand-work-to-each-other-a-verification-a-close-a-unit-and-when-may-one-take-over-what.md)
(hand-over between sessions), [q-37xc3y](q-37xc3y-how-does-the-harness-serve-several-people-steering-agents-in-one-project.md)
(several sessions of one person are one judge with several hands),
[q-2gw24v](q-2gw24v-how-do-running-sessions-reach-each-other-beyond-one-working-directory.md)
(how sessions reach each other).
4. **The roles' first draft is the ground for the keeper's brief** — the user, 2026-11-15, "а так
   черновик ок". Core ships two standing roles to a tree with more than one standing session, the
   keeper of the harness and the lander, the lander folded into the keeper in a small tree; judges,
   discovery and audits are subagents. The maintenance sweep is a session too, but no standing
   one: the host's schedule starts it, and the keeper owns what it leaves — in this tree the task
   "GoodWolf Maintenance" runs it nightly; game-delta has no schedule, so the sweep its
   orchestrator was given by hand never ran. A project cuts its own roles by the rule of
   [q-jz3mlm](q-jz3mlm-how-does-a-project-cut-its-work-into-standing-sessions-and-how-does-the-cut-change-as-the-project-grows.md);
   a role carries its skill, the map of what it owns, and its name. In this tree the keeper is
   also core's own, the one a recipient's keeper turns to.
5. **A mechanism of its own keeps the standing sessions, the keeper its first session** — the
   user, 2026-11-15: "ты заводишь себе механизм /swarm или как-то так. будешь работать в двух
   режимах: дефолтная сессия, которую харнес предлагает запустить в инсталляции, для управления
   харнессом и агентами; в этом дереве, ты будешь меньше управлять харнесс, больше сессиями;
   будешь решать какие сессии нужны - анализируя какие сессии пользователь использует … и
   запутывается ли работа в сессиях пользователя достаточно сильно для того чтобы оправдать
   новую выделенную постоянную правильно проименованную сессию; сварм скил обьявляет себя как
   скил который используют если сессии наступают друг-другу на пятки. его задача понять какое
   смешение зон ответстенности привело к тому что сессии мешают друг другу, и рекомендовать
   рефактор для разведения кода и сессий, и если нужно - добавления стабильной ролевой сессии."
   Its name and its edges are not settled ("как-то так"); the keeper's additions are put to the
   person before it is declared.
   The keeper's additions, accepted by the user the same day ("ага"): sessions notice a collision
   and this work says why it happened; a collision repeated in one area is what calls for a
   proposal, a single one does not; the cut goes stale both ways, so a role is also closed or two
   merged; it recommends and the person decides, starting and ending no session and handing out no
   work; its evidence is what the tree already keeps — rows, session records, git history, the
   sessions' own words and an outside read; one record, the tree's roles, each with its name, the
   map of what it owns, its brief and its holder; the default session is offered at install, never
   required; standing roles are kept here, the rights of a role staying
   [q-p4sdnv](q-p4sdnv-what-is-an-agent-role-and-which-mechanism-keeps-roles.md)'s. The user then
   asked whether this is the session mechanism itself, or whether that one is already overloaded
   — not settled.
6. **It is the session mechanism's, a part kept apart, and its skill is `/pack`** — the user,
   2026-11-15: "pack, по твоей рекоммендации все остальное", on the keeper's recommendation: the
   session mechanism already keeps every rule on how sessions interact and holds a seam for a
   role, and a mechanism of its own would own one skill and one record and rely on the rest. The
   part has a skill, a record and a section of the doc of its own, so it can leave as a mechanism
   at the cost of a move; collisions repeating between the sessions that write the session
   mechanism are the evidence that would call for it. Decision 5's "a mechanism of its own" reads
   so from here.
7. **Decisions 1 and 4 narrowed for this tree** — the user, 2026-11-16, asked whether the
   keeper stays the one writer of the rules here: "да, в этом дереве другие сессии тоже могут
   править свои механизмы". Where the harness serves another product the keeper is the one
   writer of the rules and holds what the sweep leaves; in this tree an owner writes its own
   mechanism's rules, skills and scripts, as
   [q-dyc63i](q-dyc63i-which-standing-roles-does-this-tree-have-where-every-session-develops-the-harness-itself.md)'s
   decision 1 says, and what the sweep finds goes to the owner of the mechanism it falls in
   once a record of the roles can say who that is.

## Where it stands

Accepted by the user, 2026-11-17: "да, все верно" — of this whole retold to them in fifteen points,
the keeper's three readings of decisions that meet accepted with it.

**The problem.** Two things, and one cut answers both. One person runs several standing sessions
in one tree, and they step on each other: one session's lines in another's commit, two writing one
file, a rule landing mid-work from several hands. Each collision is mended where it happened, so
its cause — two areas of responsibility that overlap — stays and returns. And a session that
answers for everything holds everything: each session here is handed the whole store's window,
some 55 KB, at its start and again after a compaction, whatever it works on. The person named
this the point of dividing the work at all — each session holds the context of its own area and
is not cluttered by the rest, which asks a clean separation, kept clean. Nothing in the method
says which standing sessions a project needs, what each answers for, or when that cut should
change.

**The cut.** A *zone* is paths. A project's architecture is cut where its load-bearing seams
pass: a module that suggests itself is encapsulated, so that a session writes mostly in its own
files and a little in the shared ones. The cut depends on the domain, never on who writes, and
the roles follow it: a *role* is a zone with a name, answered for across chats, and it owns whole
modules, so re-cutting the roles moves no text. A role is given paths, never a part of a file.
The form the cut moves towards is every file one role's. Until a tree's files have been moved
apart, a file several roles write is allowed, marked as a straw dog where each of those roles'
zones is written, the person told what follows; that state is expected to be common.

**One session to a zone.** A zone has one session and never a second. A zone one session no
longer carries is split into zones, each on paths of its own — whether to split is read from the
flow of its tasks and its load; where its work cannot be split, its session works through
subagents. Zones can outnumber sessions: a session may hold several roles, and a role with little
work is given to a session that holds another. A shift has two sizes: a role passes whole to
another session, no path moving; or paths pass from one role to another.

**What carries a role.** Every role has a mechanism of its own; a role a project composes has
the project's own. Its skill is the role's brief, which a successor reads without the chat that
held the role before; its parts and what it produces are the role's zone; who reads what it
produces are its seams with the other zones. A mechanism may be a skill and its doc and nothing
more, and no skill is without one. Where what a role produces is itself a mechanism, as in this
tree, the role's mechanism names it, and the name stands for the paths that mechanism declares.
The roles' zones and briefs are kept nowhere apart from their mechanisms, and questions are no
part of a zone: who stands on a question and who holds it is the store's and the rows' to say.
Zones are chosen and shifted by paths and the domain's seams, the same in every tree, never by
which of the harness's mechanisms they touch; a role's own mechanism is where the zone, once cut,
is written, so a shift is decided in paths and recorded there.

**Who holds which.** Which session holds which role is the tree's own setting: a table in its
local rules file, installed into the entry file, where every session reads it. A session is
named there by its name, never by a chat's id. What the table does not name is held by the
session that holds the harness — the default core ships, which a tree's own table replaces — so
a tree with one session writes nothing. A standing session writes the name the table gives it on
its row. No silence ends such a row and no pass removes it, so every rule treats a role's
sleeping session as any running one. The row ends at its own conclude, or when its name passes
to another chat, which takes its position and what it held; a name seen in the last three hours
does not pass. Otherwise only the cut reassigns or closes it.

**Crossing a boundary.** A session that edits a file in another role's path is told at the edit
whose path it is, and the edit is recorded where that role's session sees it; it is never
refused. A crossing repeated on one path is ground to propose shifting the zone or marking the
file shared; the cut's skill counts the crossings. It is built in parts: said at the edit where
a host has a hook on file edits and at the commit where it has none; the record of who touched a
file waits on the store's server; and the harness can say whose a path is only where a role's
mechanism names the paths of what it produces.

**Rebuilt, not fixed.** The cut is no fixed structure; what is asked of it is that it can be
rebuilt reliably: the roles are recorded where they are seen, which role an instruction and a
zone belong to is visible to every session, that attribution is kept true as the cut changes and
as the work goes on, and shifting a zone is something the harness itself can do.

**The skill.** The session mechanism keeps the cut as a part of its own, kept apart so that it
can leave as a mechanism: the skill `/pack` and a section of its doc. `/pack` recommends and the
person decides: it starts and ends no session, hands out no work and writes nothing in another
role's zone. Keeping the cut is itself a role: held in this tree by the session that holds the
store, and in a tree that installed the harness and took this part, by the session that holds
the harness. That role is carried by this part of the session mechanism until the part leaves as
a mechanism of its own.

**The roles core ships.** To a tree with more than one standing session, two: the one that holds
the harness, offered at install as the default session, and the lander, folded into the first in
a small tree. A project composes the rest by this cut. Judges, discovery and audits are
subagents; the maintenance sweep is a session the host's schedule starts, and no standing one.

**Its moments.**

- *Sessions step on each other.* `/pack` says why: which zones overlapped, read from what the
  tree already keeps — the rows, the session records, git history, the sessions' own words — and
  from a read by someone outside. One collision is mended where it happened. A collision repeated
  in one zone brings a proposal: the code or the records separated so the zones stop sharing
  them, which is also what lets each session read its own and no more; paths shifted from one
  role to another; or a new role, named for what it answers for.
- *A zone outgrows its session.* `/pack` reads the flow of the zone's tasks and its load and
  proposes a split; where the work does not split, the zone's session works through subagents.
- *The cut is read against the work.* On the person's ask, `/pack` reads which sessions the
  person actually runs against the roles, and proposes what the cut lacks or no longer needs: a
  role opened, a role closed, two merged, a role with little work given to a session that holds
  another.
- *A tree is installed.* The harness offers to start the default session; it is offered, never
  required, and a tree with one session needs no roles.
- *A session takes a role.* It writes its name on its row, reads the role's skill, and reads the
  tree by the role's zone: its own whole, the rest through what is shared and the contracts
  between zones, without loading it.

**Two trees.** Where the harness is a tool serving another product, the whole harness is most
likely one session's, and that session is the one writer of the rules and holds what the sweep
leaves; such a tree writes that limit into that session's skill or its local rules, never into
core's common rules. In this tree, where the rules are the product, a role's session writes its
own mechanisms' rules, skills and scripts and asks a change in another's of that session; what
the sweep finds goes to the session of the zone it falls in.

**This tree.** Four standing sessions — the keeper of core's boundary with the other trees, the
store, the product, the practice; the landing on main is a role not opened while every session
commits to main itself; the work on how rules are made is cut off the keeper into a session of
its own once this whole is accepted
([q-dyc63i](q-dyc63i-which-standing-roles-does-this-tree-have-where-every-session-develops-the-harness-itself.md)).

**What is not its own.** A role's rights and skill set ([q-p4sdnv](q-p4sdnv-what-is-an-agent-role-and-which-mechanism-keeps-roles.md)); how sessions reach each
other ([q-2gw24v](q-2gw24v-how-do-running-sessions-reach-each-other-beyond-one-working-directory.md)) and when one writes to another
([q-cdw6yk](q-cdw6yk-when-does-a-session-write-to-another-session-and-to-which.md)); handing a unit over ([q-psa5ha](q-psa5ha-how-do-sessions-hand-work-to-each-other-a-verification-a-close-a-unit-and-when-may-one-take-over-what.md)); a worktree per writing session and
the landing on main ([q-7ebz2f](q-7ebz2f-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of-sessions.md)).

**What is open.**

- The window drawn for a role's zone, and whose the files are that stay shared for good — the
  glossary, the contracts between zones
  ([q-gus5k2](q-gus5k2-how-is-each-areas-knowledge-kept-apart-so-a-session-holds-its-own-areas-context-and-the-boundary-stays.md)).
- How many collisions in one zone, and crossings on one path, count as repeated, set after the
  first read of this tree; and who carries out a shift once the person has decided it
  ([q-jz3mlm](q-jz3mlm-how-does-a-project-cut-its-work-into-standing-sessions-and-how-does-the-cut-change-as-the-project-grows.md)).
- What a role's skill must hold for a successor, and who writes it in a tree where one session
  writes the rules
  ([q-mvd4pi](q-mvd4pi-how-does-a-session-take-on-a-standing-role-learn-it-and-hand-it-on-so-the-role-outlives-any-one-chat.md)).
- Which of the skills no mechanism names get one each and which share one
  ([q-gbt7cy](q-gbt7cy-does-each-skill-state-only-what-it-owns.md)).
- What a session reads again after its context is compacted
  ([q-sxrf66](q-sxrf66-what-does-a-session-read-again-after-its-context-is-compacted.md)).
- What the keeper keeps once the rules leave it, and how a session that holds several roles is
  named
  ([q-dyc63i](q-dyc63i-which-standing-roles-does-this-tree-have-where-every-session-develops-the-harness-itself.md)).
- What a fresh tree is given at install
  ([q-wit7by](q-wit7by-what-does-a-fresh-tree-under-the-harness-need-to-set-up-standing-sessions-by-itself.md)).

**What would show it working**, graded by someone who did not build it:

1. Given a collision — two sessions editing the same two mechanism docs — does a fresh session
   running `/pack` name the overlapping zones and a way to separate them, untold?
2. Run over this tree, does it name the sessions the person actually runs, and propose a new role
   only where a collision repeated or a zone outgrew its session?
3. In a freshly installed tree, is the default session offered, and does declining it leave
   nothing behind?
4. Does a session that took a role start with less in its context than a free session in the same
   tree, counted, and still answer a question of its own zone rightly?
5. Is a session that edits a file in another role's path told whose it is — and, once the record
   of who touched a file exists, does that role's session see the edit?
6. After a shift the person decided, do the table and the mechanisms of the roles it touched
   agree, and does every session read the new cut at its next turn?

**Next.** The plan of
[01-0090 standing-sessions-each-answer-for-an-area](../tickets/01-0090-standing-sessions-each-answer-for-an-area.md)
goes back through `/plan` under this whole, each step written in
[the journal](../research/standing-sessions-journal.md) with what a fresh tree would need to do
the same. The keeper plans it and keeps the unit, asking the session that holds the store for
what lands in the session mechanism, which that session writes and puts to the person. Then
`/pack` is run on this tree.

## Impact of the split — 2026-11-15

One ticket,
[01-0090 standing-sessions-each-answer-for-an-area](../tickets/01-0090-standing-sessions-each-answer-for-an-area.md),
not split: the parts are one mechanism's, and none shows anything without the skill.

**Impact.** The session mechanism's declaration, its rules file and a new skill; the method's
glossary, which defines no role; one new record with its format and its check; an installed block
in the install's skill. No script of the session mechanism changes.

**Hidden edges.**

- The row has no slot for a role: the seam is the doc's sentence, and the rows' script writes
  nothing of it. A field there is the rows' script's, in the unit the coordinator's session holds
  and bound for the server
  ([01-0010.0250.0090 the-rows-live-in-a-database](../tickets/01-0010.0250.0090-the-rows-live-in-a-database.md));
  this ticket leaves the holder to the session's title.
- The word *role* has two accounts — an area a session answers for, here, and what an agent is
  granted at its start, in [q-p4sdnv](q-p4sdnv-what-is-an-agent-role-and-which-mechanism-keeps-roles.md); the glossary's entry lands bound to that question.
- The install's skill has no anchor for other mechanisms' blocks, and the session mechanism is
  `installed`, so its skill is named there by a block alone.
- The record's file is a new painted door where core names the file and not its folder; that
  list is the shape check's, held by hand.
- A check of the record written into the rows' script lands in the coordinator's unit; a script
  of its own adds a line to this tree's verification set.
- Recipients receive the skill at their next update; game-delta keeps its roles in local rules,
  which then stand beside core's record.
- The count of what a session with a role starts with moves little until the window is cut by
  area ([q-gus5k2](q-gus5k2-how-is-each-areas-knowledge-kept-apart-so-a-session-holds-its-own-areas-context-and-the-boundary-stays.md)): an instruction narrows what the session reads at its wake, not what
  the hook hands it.

**Leave alone.** The row's lifecycle and the holds; the window and the wake's script; the rules
on who writes a rule; the coordinator's server tickets; a role's rights.

**Recommendation.** Proceed as one ticket, the row's field and the window left out; the plan
stages it — the skill and the declaration, the record with its check and this tree's roles, the
two installed rules.

## What the whole of 2026-11-17 changes in the one accepted 2026-11-15

Each line names the decision that changed it; the old whole stands in git at 57abdbb7. A judge
that did not write the whole read it against the decisions, and what it found is in it.

**Changed.**

- **The roles' record is gone.** As accepted: "one record — the tree's roles", each with its
  name, map and brief. Now every role has a mechanism of its own, its skill the brief and its
  parts and outputs the zone
  ([q-mvd4pi](q-mvd4pi-how-does-a-session-take-on-a-standing-role-learn-it-and-hand-it-on-so-the-role-outlives-any-one-chat.md),
  decision 1; [q-gbt7cy](q-gbt7cy-does-each-skill-state-only-what-it-owns.md), decision 1).
  Decisions 4, 5, 6 and 7 above read without that record from here: "the map of what it owns",
  "one record, the tree's roles", "a skill, a record and a section of the doc", "once a record
  of the roles can say who that is" — the table says who.
- **Who holds a role is recorded.** As accepted: "which session holds a role now is no part of
  the record, which names no session: the session's title says it". Now a table in the tree's
  local file, a session named by its name
  ([q-jz3mlm](q-jz3mlm-how-does-a-project-cut-its-work-into-standing-sessions-and-how-does-the-cut-change-as-the-project-grows.md),
  decisions 4 and 5), and the name on its row, which no silence ends
  ([q-q5i2um](q-q5i2um-how-does-the-row-of-a-session-that-holds-a-role-outlive-its-sleep-and-when-does-it-end.md);
  q-jz3mlm, decision 7). The title is no longer the sign the whole names.
- **A zone is paths.** As accepted, a role's map held "paths, mechanisms, questions". Questions
  left it, and a mechanism named there stands for the paths it declares
  ([q-gus5k2](q-gus5k2-how-is-each-areas-knowledge-kept-apart-so-a-session-holds-its-own-areas-context-and-the-boundary-stays.md),
  decisions 3 and 5). The whole says *zone* where the old one said *area* and *map*.
- **Who keeps the cut in this tree is reversed.** As accepted: in this tree the default session
  "keeps the sessions first". Now the cut is held here with the store's role (q-jz3mlm,
  decisions 3 and 4).
- **The open list, the tests and Next.** Open: "how a role is handed on" is answered by
  q-q5i2um and by the role's skill being its brief; added are the files shared for good, who
  carries out a shift, who writes a role's skill where one session writes the rules, the
  compaction, what the keeper keeps, the name of a session with several roles. Tests 5 and 6 are
  new. Next no longer mints a ticket: the ticket exists and its plan returns to `/plan`.

**New in the whole:** by what a zone is cut (q-gus5k2, decision 1); one session to a zone, the
split and the subagents, more roles than sessions, the two sizes of a shift (q-jz3mlm, decisions
3 and 6); the telling at an edit of another's path (q-gus5k2, decision 4); that the cut is
rebuilt, not fixed (q-jz3mlm, decision 1); the roles core ships (decision 4 above); this tree's
four sessions
([q-dyc63i](q-dyc63i-which-standing-roles-does-this-tree-have-where-every-session-develops-the-harness-itself.md),
decision 2); and decision 7 above with q-dyc63i's decision 1 in "Two trees".

**The keeper's readings, put to the person with the whole, and accepted with it** — the user,
2026-11-17, "да, все верно", once the whole had been retold in plain Russian: its first
showing, the record's English text under a digest, they could not read.

1. "The rule for choosing and shifting zones names no mechanism" (q-jz3mlm, decision 2) beside
   "every role has a mechanism of its own" (q-mvd4pi, decision 1). Read: the first is said of
   what a zone is cut and shifted by — paths and the domain's seams, never which of the harness's
   mechanisms it touches; the second of where a role, once cut, is written and what carries its
   skill. The person held both in one breath ("да, но в любом дереве, чтобы поддерживать роль
   нужен скил") and saw no contradiction; that a shift is *recorded* in the roles' mechanisms is
   the keeper's step from there.
2. "Every role has a mechanism of its own" beside the cut's role, which decision 6 above keeps
   as a part of the session mechanism. Read: the part carries that role until it leaves as a
   mechanism.
3. q-dyc63i's decision 2 cuts the work on rules off the keeper "once the align of q-gus5k2 has
   its whole accepted". q-gus5k2 carries no whole of its own; read: this whole is the one meant.

**Not decided, and stated in Next as intent:** that the unit of
[01-0090](../tickets/01-0090-standing-sessions-each-answer-for-an-area.md) is handed to the
session that holds the cut here. It follows from who holds the cut; the hand-over itself takes
the person's word and that session's.

That session's answer, the same day, asked whether it takes the unit: it holds a unit of
eleven stages and would let it go, so the keeper keeps this one and plans it, and asks that
session for whatever lands in the session mechanism. Next says so now; the hand-over is not put
to the person.
