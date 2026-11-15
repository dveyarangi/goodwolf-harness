# q-gus5k2 How is each area's knowledge kept apart, so a session holds its own area's context and the boundary stays clean?

- **record of** what it intends to become
- **part of** q-jz3mlm
- **state** open
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-15T00:53:18Z
- **struck** 0, last 2026-11-15T00:53Z

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
