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

## Where it stands

Accepted by the user 2026-11-15 ("да"), with the second reason added at their word: "ты пропустил
вторую причину для этого механизма - чтобы каждая сессия видела свой контекст - это оптимизация".

**The problem.** Two things, and one cut answers both. One person runs several standing sessions
in one tree, and they step on each other: one session's lines in another's commit, two writing one
file, a rule landing mid-work from several hands. Each collision is mended where it happened, so
its cause — two areas of responsibility that overlap — stays and returns. And a session that
answers for everything holds everything: each session here is handed the whole store's window,
some 55 KB, at its start and again after a compaction, whatever it works on. The person named
this the point of dividing the work at all — each session holds the context of its own area and
is not cluttered by the rest, which asks a clean separation, kept clean
([q-gus5k2](q-gus5k2-how-is-each-areas-knowledge-kept-apart-so-a-session-holds-its-own-areas-context-and-the-boundary-stays.md)). Nothing in the method says which standing sessions a project needs, what each
answers for, or when that cut should change: game-delta cut its nine by hand, and this tree found
its three by the person naming them.

**The shape agreed.** The session mechanism keeps the standing sessions as a part of its own: the
skill `/pack`, one record — the tree's roles — and a section of its doc. A *role* is an area of
the work one standing session answers for across chats: its name, the map of what it owns —
paths, mechanisms, questions — and its brief, which a successor reads without the chat that held
the role before. The map is also what the role's session reads: its own area whole, the rest of
the tree through what is shared and the contracts between areas, never held. Which session holds
a role now is no part of the record, which names no session: the session's title says it, and
the row will once the rows' script gives it a field. `/pack` recommends and the person decides: it starts and ends no session, hands out no
work and writes nothing in another role's area.

**Its moments.**

- *Sessions step on each other.* `/pack` says why: which areas overlapped, read from what the
  tree already keeps — the rows, the session records, git history, the sessions' own words — and
  from a read by someone outside. One collision is mended where it happened. A collision repeated
  in one area brings a proposal: the code or the records separated so the areas stop sharing
  them, which is also what lets each session read its own and no more; the roles' map redrawn; or
  a new standing role, named for what it answers for.
- *The cut is read against the work.* On the person's ask, `/pack` reads which sessions the
  person actually runs against the roles, and proposes what the cut lacks or no longer needs: a
  role opened, a role closed, two merged.
- *A tree is installed.* The harness offers to start the default session, the keeper of the
  harness; it is offered, never required, and a tree with one session needs no roles.
- *A session takes a role.* It names the role in its title and its row, reads the brief, and
  reads the tree by the role's map.

**Two trees, one skill.** Where the harness is a tool serving another product, the default session
keeps the harness first — the updates from core, what the sweep leaves, the tree's own rules —
and the sessions beside it. In this tree, where the owners of mechanisms write their rules
themselves, it keeps the sessions first, and the boundary with the other trees.

**What is not its own.** A role's rights and skill set ([q-p4sdnv](q-p4sdnv-what-is-an-agent-role-and-which-mechanism-keeps-roles.md)); how sessions reach each
other ([q-2gw24v](q-2gw24v-how-do-running-sessions-reach-each-other-beyond-one-working-directory.md)); handing a unit over ([q-psa5ha](q-psa5ha-how-do-sessions-hand-work-to-each-other-a-verification-a-close-a-unit-and-when-may-one-take-over-what.md)); a worktree per writing session and
the landing on main ([q-7ebz2f](q-7ebz2f-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of-sessions.md)).

**What is open.** How each area's knowledge is kept apart and what holds the boundary — the
records cut by area, the window drawn for a role's area, a rule or a check at landing
([q-gus5k2](q-gus5k2-how-is-each-areas-knowledge-kept-apart-so-a-session-holds-its-own-areas-context-and-the-boundary-stays.md)); how many collisions in one area count as repeated, set after the first read of
this tree ([q-jz3mlm](q-jz3mlm-how-does-a-project-cut-its-work-into-standing-sessions-and-how-does-the-cut-change-as-the-project-grows.md)); how a role is handed on and what its brief must hold
([q-mvd4pi](q-mvd4pi-how-does-a-session-take-on-a-standing-role-learn-it-and-hand-it-on-so-the-role-outlives-any-one-chat.md)); what a fresh tree is given at install ([q-wit7by](q-wit7by-what-does-a-fresh-tree-under-the-harness-need-to-set-up-standing-sessions-by-itself.md)).

**What would show it working**, graded by someone who did not build it:

1. Given this morning's collision — two sessions editing the same two mechanism docs — does a
   fresh session running `/pack` name the overlapping area and a way to separate it, untold?
2. Run over this tree, does it name the sessions the person actually runs, and propose a new role
   only where a collision repeated?
3. In a freshly installed tree, is the default session offered, and does declining it leave
   nothing behind?
4. Does a session that took a role start with less in its context than a free session in the same
   tree, counted, and still answer a question of its own area rightly?

**Next.** A ticket for the part — the skill, the rules, the record's format and its check — taken
through the ring, each instruction's text shown before it lands; then `/pack` is run on this
tree.

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
