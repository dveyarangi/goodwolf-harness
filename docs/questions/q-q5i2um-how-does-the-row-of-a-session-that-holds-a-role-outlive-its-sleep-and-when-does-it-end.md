# q-q5i2um How does the row of a session that holds a role outlive its sleep, and when does it end?

- **record of** what happened
- **part of** q-jz3mlm
- **state** closed:decided
- **owner** [01-0100](../tickets/done/01-0100-a-standing-session-keeps-its-row-while-it-sleeps.md)
- **answer** [01-0100](../tickets/done/01-0100-a-standing-session-keeps-its-row-while-it-sleeps.md) — the user, 2026-11-16
- **opened** 2026-11-16T20:26:47Z
- **struck** 0, last 2026-11-16T20:26Z

Raised by the user, 2026-11-16, through the keeper of S10: "у нас иногда ролевые сессии могут спать
днями, это тоже их закроет? может надо убедиться что майнтайн и никто другой не вытирает ролевую
сессию (только когда она на самом деле изменилась или закрылась из-за изменения ролей?)". Recorded
at [q-cdw6yk](q-cdw6yk-when-does-a-session-write-to-another-session-and-to-which.md), *Three gaps
the person found in the landed rule*.

What the code does today (`sessions.py`, `tend`): another session's wake writes a running row
*ended* once nothing has been seen of it for three hours (`SILENT_AFTER`,
[q-jsj6sb](q-jsj6sb-when-does-a-session-row-that-stopped-running-read-ended-and-who-ends-it.md)),
and removes a row ended for seven days (`GONE_AFTER`); a session that returns after that is
registered anew, its position and its hold gone. The row tells neither *concluded* from *silent*
nor a session that holds a role from one that does not. The store's own row read ended on
2026-11-16 at 09:14Z between two of its turns.

What it meets: [q-jz3mlm](q-jz3mlm-how-does-a-project-cut-its-work-into-standing-sessions-and-how-does-the-cut-change-as-the-project-grows.md)
decision 5 — which session holds which role is a table in the tree's local file, a session named
by its name, never a chat's id; nothing of it is built. The row is where that name meets the id a
host gives.

## Decided — the user, 2026-11-16: "Да, все четыре"

1. A row carries the name of the session that holds a role, written by the session when it takes
   the role; a name stands on one row at a time.
2. A named row is not ended by silence and not removed by time.
3. It ends at its own `/conclude`, or when its name passes to another chat; the chat that takes
   the name takes the row's position and hold with it, a resume under a new id being the same
   conversation. A name whose row was seen within the last three hours does not pass.
4. Once the table of decision 5 exists, the check reports a named row the table does not name.

Decision 3's `/conclude` amended by the user, 2026-11-18: a role's session is not concluded, and
the person or the harness at a re-cut ends it —
[q-g6lj7m](q-g6lj7m-who-ends-the-session-of-a-role-if-not-its-conclude.md).

Decisions 2 and 3 overturned by the user, 2026-11-25: a row holds its role while the session does, no longer
([q-mvd4pi](q-mvd4pi-how-does-a-session-take-on-a-standing-role-learn-it-and-hand-it-on-so-the-role-outlives-any-one-chat.md), *Where it stands*). Not yet carried into the script.
