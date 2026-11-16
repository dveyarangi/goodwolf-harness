# A standing session keeps its row while it sleeps

- **record of** what happened
- **Status:** Done (2026-11-16)
- **Type:** AFK
- **Minted:** 2026-11-16
- **Answers:** [q-q5i2um](../../questions/q-q5i2um-how-does-the-row-of-a-session-that-holds-a-role-outlive-its-sleep-and-when-does-it-end.md)
- **Outcome:** A session that holds a role and sleeps for days keeps its row, its position and its
  hold, until it concludes or its name passes to another chat, which takes them with it.

## Parent

[The session mechanism](../../../.agents/mechanisms/session/session.md), whose rows' script this is;
[01-0090 standing-sessions-each-answer-for-an-area](../01-0090-standing-sessions-each-answer-for-an-area.md)
leaves the row naming its role to the rows' script. The decision is q-q5i2um's *Decided*.

## What to build

- A session that holds a role writes its name on its row when it takes the role; one name stands
  on one row, so a role is held by one chat at a time.
- A wake neither ends nor removes a named row for its silence: a standing session may sleep for
  days, and S10 writes to it asleep.
- A named row ends at its own `/conclude`. A chat that takes a name another row bears takes that
  row's position and hold, and the other row ends — a resume under a new id is the same
  conversation (S6). The name does not pass from a row seen in the last three hours, so two live
  chats never share one role.
- The check reads the name as part of the row's form; a tree whose rows carry no name passes as
  before.
- What the table of [q-jz3mlm](../../questions/q-jz3mlm-how-does-a-project-cut-its-work-into-standing-sessions-and-how-does-the-cut-change-as-the-project-grows.md)
  decision 5 will add — a named row the table does not name reported — waits for that table, a
  `TODO` naming the question.

## Acceptance criteria

- [x] A named row last seen days before a wake still reads as it did after the wake, and is not
      removed however long it stays silent. *(2026-11-16, c637bf62)*
- [x] An unnamed row is ended and removed as before.
- [x] A chat that takes a name held by a row silent past three hours holds that row's position and
      unit, and the old row reads ended; a name on a row seen within three hours is refused,
      naming that row.
- [x] A named row's `/conclude` ends it as any row's, and it is then removed after seven days.
- [x] The session mechanism's doc, `/conclude`'s row form and the hosts' edge say what a name does
      to the row.
- [x] A session that takes a role is told to write its name, by a rule the keeper lands in
      `/recall` on the person's word; until then no row gains a name but by hand. *(2026-11-16,
      S11 at 76991b77)*
- [x] `/verify` passes against this ticket and the governing docs, judged by someone who did not
      build it. *(2026-11-16: the judge's one blocking finding was the missing naming rule, since
      S11; its minor findings mended in c637bf62; the set green, 1160 tests)*

## Out of scope

- The table of which session holds which role:
  [q-jz3mlm](../../questions/q-jz3mlm-how-does-a-project-cut-its-work-into-standing-sessions-and-how-does-the-cut-change-as-the-project-grows.md)
  decision 5.
- The rows moving to the server's database:
  [01-0010.0250.0090 the-rows-live-in-a-database](../01-0010.0250.0090-the-rows-live-in-a-database.md).
- S10's wording for a sleeping session: the keeper's, at
  [q-cdw6yk](../../questions/q-cdw6yk-when-does-a-session-write-to-another-session-and-to-which.md).
