# A role's session is never concluded

- **record of** what happened
- **Status:** Done (2026-11-20)
- **Type:** AFK
- **Minted:** 2026-11-20
- **Related:** [A standing session keeps its row while it sleeps](./01-0100-a-standing-session-keeps-its-row-while-it-sleeps.md) —
  the named row this changes
- **Answers:** [q-g6lj7m](../../questions/q-g6lj7m-who-ends-the-session-of-a-role-if-not-its-conclude.md)
- **Outcome:** A session that holds a role is not ended by its `/conclude`, nor its row by time;
  the person ends it by telling it to drop its role, after which it concludes as any session.

## Parent

[The session mechanism](../../../.agents/mechanisms/session/session.md), whose rows' script and
conclude this is. The decisions are q-g6lj7m's, amending
[q-q5i2um](../../questions/q-q5i2um-how-does-the-row-of-a-session-that-holds-a-role-outlive-its-sleep-and-when-does-it-end.md)
decision 3's "it ends at its own `/conclude`".

## What to build

- `/conclude` in a session that holds a role ends nothing: it says that a role's session is ended
  by the person or by a re-cut, and stops.
- `sessions.py --end` refuses a row that bears a name, naming the way to drop it.
- Told by the person to drop its role, the session wipes the name from its row; its `/conclude`
  then ends it as any session's.
- A named row is never removed by time, ended or not; an unnamed row ended for seven days still
  goes.
- The session mechanism's document, its rules, the conclude skill, the glossary's *Session* and the
  architecture say the same.

## Acceptance criteria

- [x] `--end` on a named row is refused and writes nothing; on an unnamed row it ends it as before.
- [x] A named row, its name dropped, is ended by `--end`, and is removed seven days later.
- [x] A named row that reads ended for eight days is still there after a wake.
- [x] `/conclude` in a session that holds a role writes no session record and ends no row.
- [x] `/verify` passes against this ticket and the governing docs. 2026-11-20, judged by a verifier that did not build it, and the conclude skill tried three times on fresh subagents until a role's session stopped before any step and a drop alone did not conclude.

## Out of scope

- The re-cut that ends a role's session by the harness:
  [q-jz3mlm](../../questions/q-jz3mlm-how-does-a-project-cut-its-work-into-standing-sessions-and-how-does-the-cut-change-as-the-project-grows.md).
- Whether a row bears the session's name or the role's, which the keeper puts to the person.
