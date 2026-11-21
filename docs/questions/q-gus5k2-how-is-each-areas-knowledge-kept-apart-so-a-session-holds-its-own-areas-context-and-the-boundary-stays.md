# q-gus5k2 How is each area's knowledge kept apart, so a session holds its own area's context and the boundary stays clean?

- **record of** what it intends to become
- **part of** q-jz3mlm
- **state** open
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-15T00:53:18Z
- **struck** 2, last 2026-11-16T13:19Z

The user, 2026-11-15: "смысл в разделении обязанностей - чтобы каждая сессия держала контекст своей
области кода или доков или еще чего - и не сильно захламляла контекст всем остальным. это
подразумевает чистое разделение и поддержку его. это надо подкрепить правилами и это мне кажется
важный пререквизит вообще разделения на роли сессий." The case that raised it: game-delta's
architecture document written by five sessions, its orchestrator proposing a file per area with
an index; core's answer given there was a file per area, the index keeping the contracts between
areas ([the journal](../research/standing-sessions-journal.md), step 4).

What it covers: the architecture and the other records cut by area, the code's paths owned by
area, the question store's window showing a session its own area, what stays shared (the
glossary, the contracts between areas), and what holds the boundary — a rule, a check at landing,
or both. Neighbour: [q-p4sdnv](q-p4sdnv-what-is-an-agent-role-and-which-mechanism-keeps-roles.md),
which rules and skills a role carries.

## The case from game-delta — 2026-11-15

game-delta cut its architecture by owner (its commits a9d7b99, f72e2f5): `docs/architecture.md`
became an index holding what binds more than one area, with a file per standing session beside it
under `docs/architecture/`, and some seventy-five pointers from code, questions and tickets were
turned to `architecture/<area>.md: "<section>"`. What the cut then showed:

- **Seams.** Six sentences that one session wrote in its own file bind its neighbours — the
  flight and the music, the tunnel and the look, the story's levers and every area among them.
  The seven sessions propose moving the six into the index, each paragraph of the index with one
  holder.
- **The holder's home.** Who holds what stands in the record of a question of that tree; the
  index names each file's keeper again, and the area files' headers name none.
- **Core's own bound.** A file in the core directory may name `docs/architecture.md` and no file
  under `docs/architecture/` — the painted doors hold the one path — so a section a core-side
  file points at could not leave the index.
- **The code.** The same sessions propose cutting the code along the same lines. The person's
  word in that tree, 2026-11-15: two sessions in one file is a sign to refactor the boundary.

Core's keeper answered its orchestrator from the plan of
[01-0090 standing-sessions-each-answer-for-an-area](../tickets/01-0090-standing-sessions-each-answer-for-an-area.md),
not yet accepted: who holds what stays in one home, shaped as the roles' record, the holder of an
index paragraph being a map's entry narrowed by words; no header field for an owner and no form
of its own for a seam; the code cut where a collision repeated, on the person's decision. None of
that answers this question.

The person, the same day: "у нас есть подлежащий вопрос, который все еще требует ответа - как
правильно резать архитектуру. мы на него ответили?" It is not answered. The keeper's reading of
what it asks, not the person's words: by what an architecture is cut — who writes a sentence,
what it describes, or whom it binds — and which of the two cuts, the sessions' and the
architecture's, follows the other.

The user, 2026-11-15, asked which goes first — this question's align or the building of
[01-0090 standing-sessions-each-answer-for-an-area](../tickets/01-0090-standing-sessions-each-answer-for-an-area.md):
"Да, сначала разрез". The align runs here; the ticket's plan waits unaccepted until it lands.

## Each role sees its own installed rules — the user, 2026-11-21

Raised while `/pack`'s plan placed the entry file's installed blocks: "в идеале хотелось бы чтобы
каждая сессия не видела инсталляцию скилов чужих ролей (но могла бы видеть общие и свои). но я не
знаю как такое сделать, это значит что каждой роли нужен свой AGENTS.md". Not answered: today every
session is handed the one entry file and every skill's description; a role-scoped entry file is
one way, among others to be weighed here.

## Decisions

1. **The architecture is cut where its load-bearing seams pass, and the roles follow the cut** —
   the user, 2026-11-15, asked whether an architecture is cut by what it describes or by who
   writes it: "режем по тому, где проходят load-bearing швы )) или не знаю как тебе сказать - если
   есть напрашивающийся модуль - инкапсулируем его? вот по этому принципу. чтобы можно было писать
   в основном свое в свои файлы, и только чуть чуть в общие. это зависит от домена, а не от того
   кто пишет." A module that suggests itself is encapsulated; a session writes mostly in its own
   module's files and a little in the shared ones; the cut depends on the domain, never on who
   writes. A role owns whole modules, so re-cutting the roles moves no text. *Seam* is
   [the method's glossary](../../.agents/glossary.md)'s word, and *load-bearing seam* its
   proposed definition, which this decision stands on.
2. **The cut is rebuilt reliably, not held** →
   [q-jz3mlm](q-jz3mlm-how-does-a-project-cut-its-work-into-standing-sessions-and-how-does-the-cut-change-as-the-project-grows.md),
   decision 1: the roles recorded where they are seen, the attribution of instructions and zones
   visible to all and kept true, a zone shifted by the harness.
3. **A role is given paths, and a file several roles write is allowed while it is marked** — the
   user, 2026-11-15, asked whether a role is given paths alone or parts of files too: "роли
   приписываются пути. но давай не будем делать это жестким - если система не доконца
   мигрировала, это ок файлу принадлежать нескольким ролям, если это эксплицитно указано как
   собака, и пользователю сказано о последствиях. т.е конечная идеальная форма - свои файлы
   роли. вероятная частая - файлы меняют несколько ролей, до миграции." A role is given paths,
   never a part of a file. The form the cut is moved towards is every file one role's; a file
   that several roles write stands in each of their maps as a straw dog, said so in the record,
   with the person told what follows from it. That state is expected to be common until a tree's
   files have been moved apart.
4. **A session editing a file in another role's path is told, and the edit is recorded; it is not
   refused** — the user, 2026-11-16: "Б", of three ways put to them. At the moment of the edit the
   harness tells the session whose path it is; who touched the file is written where its owner
   sees it; a crossing repeated on one path is ground to propose shifting the zone or marking the
   file shared. Refusing was set aside as making the cut rigid, against decision 2. An
   instruction alone was set aside on the evidence: under such a rule in game-delta the largest
   group of messages that were needed and never sent gathered — uncommitted work left in a file
   another session works in, before any commit
   ([the count](../research/inter-session-messages-2026-11-15.md), "Where a message was
   missing"). It is built in parts: saying it at the edit needs a host's hook on file edits, and
   falls back to the commit where a host has none; the record of who touched a file waits on the
   store's server; counting the crossings is the pack's.
5. **A role's map holds paths, and a mechanism where there is one** — the user, 2026-11-16, asked
   whether decision 3 narrows the accepted map of "paths, mechanisms, questions" to paths alone:
   "пути и механизм, если он есть. но не факт что он есть )) надо сделать чтобы был всегда, даже
   если это просто скил - но всегда с описанием документа механизма, как минимум, даже если без
   скриптов". A mechanism named in a map stands for the paths its declaration lists as its
   parts, read by the script and written nowhere a second time. Questions leave the map: who
   stands on a question and who holds it is the store's and the rows' to say. That every skill
   has a mechanism, with its doc at the least, is recorded where the skills' ownership is asked
   — [q-gbt7cy](q-gbt7cy-does-each-skill-state-only-what-it-owns.md), decision 1.
