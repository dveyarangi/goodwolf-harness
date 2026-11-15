# q-gus5k2 How is each area's knowledge kept apart, so a session holds its own area's context and the boundary stays clean?

- **record of** what it intends to become
- **part of** q-jz3mlm
- **state** open
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-15T00:53:18Z
- **struck** 1, last 2026-11-15T17:37Z

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
