# q-jz3mlm How does a project cut its work into standing sessions, and how does the cut change as the project grows?

- **record of** what it intends to become
- **part of** q-ja5mp4
- **state** open
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-15T00:43:20Z
- **struck** 4, last 2026-11-25T10:17Z

What a standing session is cut along — a domain of the product, a layer of the code, a process such as
merging — differs between projects and changes as a project grows: game-delta cut nine sessions by
the game's domains, then added "a file has one owner" when two sessions met in one file (its L7,
97edc01). Which signs say a cut has gone stale, who proposes a new one, and who accepts it.
Evidence: [the outside read](../research/game-delta-orchestration-audit-2026-11-15.md).

Neighbours: [q-4fj72c](q-4fj72c-how-does-a-starting-agent-pick-an-area-that-does-not-overlap-another-sessions.md)
(how a starting agent picks an area that does not overlap another session's) and
[A43](../product.md) "a starting session takes a free area" assume an area taken at a session's
start; a standing session holds its area across chats.

The user, 2026-11-15: "нам надо реально подумать какие роли например есть у нас, какие есть у
общего ядра, а какие сочиняются для проекта и как … метаправило выделения ролей такое" — read
by the keeper as naming the rule given just before: a role is cut where a body of context — an
area of code, of records, of anything — can be held by one session and kept out of the others'
([q-gus5k2](q-gus5k2-how-is-each-areas-knowledge-kept-apart-so-a-session-holds-its-own-areas-context-and-the-boundary-stays.md)).
Three kinds to tell apart: the roles core ships to every tree, the roles of this tree, and the
roles a project composes for itself, with how it composes them.

## Decisions

1. **The cut is rebuilt reliably, not held** — the user, 2026-11-15, in the align of
   [q-gus5k2](q-gus5k2-how-is-each-areas-knowledge-kept-apart-so-a-session-holds-its-own-areas-context-and-the-boundary-stays.md):
   "это не жесткая структура. вся идея в том чтобы ее можно было надежно перестраивать, а не
   держать. надежно перестраивать это значит что роли записаны там где их видят, атрибуция
   инструкций и зон ответственности ролей понята и видна всем, и это поддерживается при
   изменении или вообще работе. зоны могут быть сдвинуты и харнес должен уметь это сделать".
   Three things make a rebuild reliable: the roles are recorded where they are seen; which role
   an instruction and a zone belong to is understood and visible to every session; and that
   attribution is kept true as the cut changes and as the work goes on. Shifting a zone is
   something the harness itself can do.
2. **The rule for choosing and shifting zones is general, and names no mechanism** — the user,
   2026-11-16, of the keeper's proposal that a role be a mechanism and a shift move a mechanism
   between sessions: "нет, сдвиг зоны как ты описал подходит только этому дереву. правило про
   выбор и сдвиг зон должно быть общим, не привязанным к механизмам вообще. в инсталляции у
   самого харнесса скорее всего будет только одна сессия, как в game-delta". A zone is paths; a
   shift moves paths from one session's zone to another's. A mechanism in a map is this tree's
   shorthand for the paths it declares
   ([q-gus5k2](q-gus5k2-how-is-each-areas-knowledge-kept-apart-so-a-session-holds-its-own-areas-context-and-the-boundary-stays.md),
   decision 5) and no part of the rule. In a tree that installed the harness, the harness is
   most likely one session's whole zone.
3. **There may be more roles than sessions** — the user, 2026-11-16, asked whether the cut into
   sessions stays the keeper's: "ну можно же сделать больше ролей чем сессий, и те что
   незагруженные почти, давать сессиям с больше чем одна роль? то есть здесь паком будет
   владеть хранилище, а в инсталляции - хранитель?" A role is a zone with a name; one session
   holds a role, and a session may hold several; a role with little work is given to a session
   that holds another. The same role is then held differently from tree to tree: the cut into
   sessions and its skill are held here with the store's role, and in a tree that installed the
   harness by the session that holds the harness. A shift has two sizes: a role passes whole to
   another session, no path moving; or paths pass from one role to another.
4. **Which session holds which role is recorded, as the tree's own settings with defaults** — the
   user, 2026-11-16: "кто-то должен знать как механизмы/роли распределены по сессиям, это таки
   да должно быть записано. например у нас стая записана хранилищу, у клиента - если он решил
   подключить - в сессии харнес. это локальные настройки с дефолтами". Core ships the default,
   a tree's own answer replaces it. In this tree the cut into sessions and its skill are held
   with the store; in a tree that installed the harness and took that part, by the session that
   holds the harness.
5. **The distribution is a table in the tree's local file, a session named by its name** — the
   user, 2026-11-16, "все да", of the form put to them: the tree's local rules file holds which
   named session holds which role; a session is named by its name, never by a chat's id, since
   chats are lost and a name stays; what the table does not name is held by the session that
   holds the harness, so a tree with one session writes nothing; the table is installed into the
   entry file, where every session reads it. It is a table of its own: the settings' table takes
   only values a mechanism declared beforehand, and sessions' names are each project's.
6. **A zone has one session and never a second** — the user, 2026-11-16, of the words drafted
   from fimonitor's case, "a second stands only for a large, long body of planned work": "зона
   держит не держит вторую сессию - она либо разделяется - проверяется по потоку задач и
   загруженности, а если все задачи не разделить - начинает использовать подагенты". A zone
   that one session no longer carries is split, into zones each on paths of its own, and whether
   to split is read from the flow of its tasks and its load; where its work cannot be split, its
   session works through subagents. Replaces the draft below. The draft's sentence on a session
   whose unit is done — it concludes, and is not renamed into a zone — is dropped: the user,
   2026-11-17, "Да, убирай", of the keeper's reading that it guards one tree's one case and
   repeats what concluding a session already does.
7. **A role's session asleep is an ordinary session** — the user, 2026-11-17, asked whether the
   nightly pass repairs in a zone whose session sleeps or only tells its session: "насчет сессии
   которая спит - это обычная сессиия и работает как обычно. идея была не удалять строки ролевых
   сессиий, чтобы они работали как обычно, если только механизм разрезки не решит что нужно
   что-то поменять". A role's row is kept so that every rule reads its session as running: it
   is written to, told what falls in its zone, and holds what it held. No rule has a case of its
   own for sleep, the nightly pass's included: what it does with a finding in a zone is the same
   asleep or awake. How such a row ends and passes stays as decided at
   [q-q5i2um](q-q5i2um-how-does-the-row-of-a-session-that-holds-a-role-outlive-its-sleep-and-when-does-it-end.md)
   — at its own conclude, or its name taken by another chat; otherwise only the cut reassigns or
   closes it. *(Overturned 2026-11-18 as to "at its own conclude": a role's session is not
   concluded; the person, or the harness at a re-cut, ends it —
   [q-g6lj7m](q-g6lj7m-who-ends-the-session-of-a-role-if-not-its-conclude.md),
   decisions 1 and 2.)*

## The case from fimonitor: three sessions in one zone — 2026-11-16

fimonitor, told by core's keeper that a zone is paths cut at the domain's seams and that a
ticket is no role, wrote six zones and named its sessions by them; its three task sessions on the
collector — one a final check away from done, two on a ticket each, all on the same file and its
tests, one after another — became three sessions of one zone. The person there, as its harness
session relays it, 2026-11-16: "зачем нам столько трекер-сессий — у каждой действительно
планируется продолжительный и большой объём работ?" The answer was no.

What the decisions above did not say, and the keeper's advice with them: how many sessions a
zone holds, and how much work a session of its own is worth. A session to a ticket inside one
zone was forbidden by nothing, and renaming the sessions by zone made it the cut.

The criterion the person gave there, relayed, put to the person here and not decided in this
tree: a zone holds one session; a second stands only for a large, long, planned body of work on
paths of its own; a session whose unit is done is closed, never renamed into the zone.

The same day that tree's harness session relayed more: the person decided there that one session
to a zone becomes the rule in fimonitor and in core, and asked that the words agree. The words
the keeper sent, for that tree's local rule now and as a draft for core, not yet confirmed by
the person here: "A zone has one session; a second stands only for a large, long body of planned
work on paths of its own. A session whose unit is done concludes; it is not renamed into a zone.
Zones can outnumber sessions: a session may hold several." *Concludes* is the method's word for
a session ending — its record written, its row ended; archiving a chat is the host's
housekeeping. Core has nowhere to carry the rule until the part on standing sessions is built.

## The case from fimonitor: a role's row read ended, and its session was archived — 2026-11-17

That tree's harness session, to core's keeper: a zone's session there had a row reading ended;
a second chat took the same zone, the harness session read the row as the zone's session
having concluded, and archived it on the person's yes to a question that did not name which
session was meant. The person there, relayed: "ролевые сессии не заканчивают работу". It was
unarchived.

What the keeper read in that tree: its core is 76976feb, an hour older than the commit that
lets a row bear a role's name (c637bf62); the row bore none, and no session record followed
it, so no conclude ran — another session's wake ended the row for three hours' silence. The
naming answers it once that tree updates. What no rule of core's says, and the case asks: an
ended row is no sign that a zone is free; and archiving a chat, the host's housekeeping, has
no rule though it took a role's session out of reach. Words offered for that tree's local
rule until then: "A zone's session is concluded or archived only on the person's word naming
that session. A row of a zone's session that reads ended says it sleeps: write to it, and give
its zone to no other chat."

## A case from a recipient: a mature product asks how to cut its roles — 2026-11-25

A recipient's harness session, on its person's word as it relays it, asked core's keeper how to
organise its roles. As it stands there: two roles, each cut by a kind of work and not by paths,
their rows bearing the role's title; several more sessions with no role, each on one task; the
harness's own upkeep in a session whose row has no name; one person; the code built in another
host, so its sessions meet mostly in the records. It asked what earns a standing role against a
question or one task's session, and what ends or merges one; by what the other trees cut theirs
and what collided; which roles it should have; whether the harness's upkeep is a role and what it
decides; whether domain work is a role's; who takes what falls in no zone or in two; and what its
local rule on roles becomes under core.

The keeper answered from the decisions above, those of
[q-ja5mp4](q-ja5mp4-does-the-method-have-one-session-direct-the-others-an-orchestrator-and-what-does-it-owe-the-sessions-it.md)
and the whole of
[q-mvd4pi](q-mvd4pi-how-does-a-session-take-on-a-standing-role-learn-it-and-hand-it-on-so-the-role-outlives-any-one-chat.md),
each with its date, and marked its own view apart: keep the harness's session and the two roles
it has, open no role for a question or a task, add a domain's role only on a repeated collision
or a window that fills from one area, keep its rule local and build nothing of core's unbuilt
part. Nothing is decided by it in either tree.

What the case shows that no decision here says:

- **A role cut by a kind of work holds no paths of its own.** The rule has a zone be paths at the
  domain's seams; an audit or a refactoring crosses every zone. Whether such a long body of work
  is a role, or a unit that closes when it is done, is unsaid. This tree's own such roles hold
  mechanisms, which a recipient has none of.
- **The entry rules lag the accepted decision.** The recipient's rows bore a role's title while
  the session mechanism's rule on a row's name forbids it; the whole accepted on 2026-11-25 lets
  a row bear the role, and the rule is not yet rewritten.
- **What a recipient writes locally while core's part on roles is unbuilt** is asked a second
  time; [the journal](../research/standing-sessions-journal.md), step 16, holds the first.

Material for the roles' review.
