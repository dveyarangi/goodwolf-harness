# q-ja5mp4 Does the method have one session direct the others - an orchestrator - and what does it owe the sessions it directs?

- **record of** what it intends to become
- **part of** q-zxnc6y
- **state** open
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
