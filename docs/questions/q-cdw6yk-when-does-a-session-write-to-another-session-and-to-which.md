# q-cdw6yk When does a session write to another session, and to which?

- **record of** what it intends to become
- **part of** q-ja5mp4
- **state** open
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-15T19:06:38Z
- **struck** 1, last 2026-11-16T09:22Z

The user, 2026-11-15: "еще одна задача - правда уже не разрезания, а скила - это чтобы агенты
знали в каких случаях кому писать. запусти ка под-сессию, и либо спроси Оркестратор игры, либо
сам проверь когда агенты писали друг-другу по делу, а когда зря, чтобы мы смогли из этого
вывести правила".

What stands today: core's rules on a neighbour's work say when a session is told without asking
and say nothing of which messages are waste; game-delta wrote a rule of its own after a day's
messages were counted, its local rule "What one session sends another", 2026-11-11. The
evidence is gathered first, by a session started for it: which messages between sessions
changed what their receiver did, and which did not. It is written to
`docs/research/` and the rules are derived from it with the person.

## The evidence — 2026-11-16

[Messages between sessions — which were worth sending](../research/inter-session-messages-2026-11-15.md):
1,011 messages read, 897 of them game-delta's, each judged by what its receiver did next; 98
cases there where a message was needed and not sent; game-delta's orchestrator asked once and
answered; eleven candidate rules, each with what it stands on. The keeper checked that the
commits and the report it names exist in game-delta; the counts were not derived again.

What it shows, as the keeper reads it:

- Four in five messages were useful, before game-delta's own rule and after it. The rule ended
  acknowledgements and halved duplicates; the share of waste did not move, because a new waste
  grew — a claim sent unchecked and stale on arrival.
- The larger loss is the message that was not sent: uncommitted work left in a file another
  session works in is the largest group, and it happens before any commit.
- A hand-off along a declared order, a break reported to its owner with the commit and the test,
  and a question were useful almost every time. A question needs no rule.
- Part of what the sessions wrote to each other is shared state — a hold while a suite runs, who
  touched a file, master red — which a record every session reads would carry once.

The candidates fall in three piles, the keeper's sorting and no decision: rules about a
message itself, which can be written now; shared state that belongs in a record or a hook and
goes to the align of the cut and to the store's server; and rules that need the roles' record
to say who the receiver is.

## Decisions

1. **The rule on what a session writes to another landed** — the user, 2026-11-16: "Да, пробуй и
   вноси". S10 of the session mechanism, in the entry file's general rules at v134; its trial
   and what it refused in [the mechanism's evidence](../mechanisms/session.evidence.md). Open
   under this question still: a change to a contract others read, told to every reader before it
   lands — the count's candidate 8, left out untried; and which session a message goes to where
   no row names the owner of a file, which waits on the record of who holds which role.
