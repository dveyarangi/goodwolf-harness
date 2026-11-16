# q-jz3mlm How does a project cut its work into standing sessions, and how does the cut change as the project grows?

- **record of** what it intends to become
- **part of** q-ja5mp4
- **state** open
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-15T00:43:20Z
- **struck** 1, last 2026-11-15T18:31Z

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
