# q-g6lj7m Who ends the session of a role, if not its /conclude?

- **record of** what it intends to become
- **part of** q-q5i2um
- **state** open
- **owner** [01-0110](../tickets/01-0110-a-roles-session-is-never-concluded.md)
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-18T07:03:21Z
- **struck** 1, last 2026-11-20T09:57Z

Raised by the user, 2026-11-18, answering whether a concluded named row is removed after seven
days: "conclude должен удалять только временные сессии, постоянными управляет пользователь и
харнесс (в случае пере-резки). в другом случае ролевые сессии живут вечно, conclude вообще не из
их лайфцикла".

## Decisions

1. **`/conclude` is not in a role's session's life** *(the user, 2026-11-18)*. It ends and
   removes only a session that holds no role. In place of
   [q-q5i2um](q-q5i2um-how-does-the-row-of-a-session-that-holds-a-role-outlive-its-sleep-and-when-does-it-end.md)
   decision 3's "it ends at its own `/conclude`".
2. **A role's session lives until the person or the harness ends it**, the harness when it
   carries out a re-cut the person decided *(the user, 2026-11-18)*. The passing of a name to
   another chat, q-q5i2um decision 3's rest, stands: the row it leaves ends nameless.
3. **The person ends a role's session through its own drop of the role** *(the user,
   2026-11-20: "Да, сначала его", on the slice put to them on 2026-11-19)*. Until a re-cut is built,
   told by the person to drop its role, the session wipes the name from its row, and is then a
   session like any other, which its `/conclude` ends.
   → [01-0110](../tickets/01-0110-a-roles-session-is-never-concluded.md)

## Where it stands

Accepted by the user, 2026-11-20, with decision 3; the ticket
[01-0110](../tickets/01-0110-a-roles-session-is-never-concluded.md) carries it out:
- `/conclude` in a session whose row bears a name ends nothing and says that a role's session is
  ended by the person or by the cut; `sessions.py --end` refuses a named row the same way.
- A named row is then never ended and never removed by time; the seven days after `/conclude`
  in session.md, the conclude skill and `tend` go.
- Who carries out a re-cut is
  [q-jz3mlm](q-jz3mlm-how-does-a-project-cut-its-work-into-standing-sessions-and-how-does-the-cut-change-as-the-project-grows.md)'s;
  until it is built, a role's row ends only by the passing of its name, or by the drop of its
  role on the person's word (3).
