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
2. **The rule reworded on the four gaps the person found, and landed** — the user, 2026-11-16,
   who named each gap and what closes it; the wording tried a second time and judged, at the
   entry contract's v135. Open under this question still, beside decision 1's two: whether a
   role's sleeping session is written only what will still hold when it wakes; and the rows'
   own part — a row whose session holds a role neither ended by silence nor removed — which is
   the rows' session's.
3. **The rule compressed in the entry file, its detail on a shelf it names** — the user,
   2026-11-16: "всю необходимую в моменте инструкцию должна нести agents.md, но сжато и с
   ссылками", accepted the same day; landed 2026-11-17 at the entry contract's v137 after a
   third trial. The rule and its shelf are the session mechanism's, and pass with it to the
   session whose zone holds it.

## Three gaps the person found in the landed rule — 2026-11-16

The user, 2026-11-16, of S10 an hour after it landed: "что такое 'session that has ended'? у нас
иногда ролевые сессии могут спать днями, это тоже их закроет? может надо убедиться что майнтайн и
никто другой не вытирает ролевую сессию (только когда она на самом деле изменилась или закрылась
из-за изменения ролей?) и еще как мы избедим ненужной болтовни? надо указать когда не писать
тоже, наверное?" — and: "и еще не хватает что писать пользователю".

What the code says of the first. A row reads *ended* in two cases the row does not tell apart:
the session concluded, or nothing was seen of it for three hours, when another session's wake
writes its row so (`sessions.py`, `SILENT_AFTER`); a row ended for seven days is removed
(`GONE_AFTER`), and a session that returns after that is registered anew, its position and what
it held gone. So a session that holds a role and sleeps an afternoon reads *ended*, and S10's
"never to a session that has ended" would have a neighbour keep from it what it must act on;
asleep a week, its row is wiped. The count's waste was mail to a session that had *concluded*;
the rule took the row's word for it, and the trial told its readers that *ended* means not
running, so it could not catch this.

Of the second: the rule names two things not to send, an acknowledgement and a status nobody
waits on. The count's largest reason a message was not worth sending is neither — what the
receiver could read from git or a record without the sender, 37 of 182 — and a broadcast that
changes nothing for its receiver is a fourth, 12.

Of the third: the rule says nothing of what a session tells its person about a message it sent
or received. In the count every receiver retold a broadcast rule to its person; in this session
each note from a neighbour was retold to the person at length.

Put to the person, not landed: S10 reworded on all three; and, told to the session that holds
the rows, that a row whose session holds a role is neither ended by silence nor removed.

The user, the same day, of the rule's rewording: "по правилу сообщений, нужно закрыть круг и
симметрию. если спросившая сессия попросила ответ - надо отвечать. если не попросила, но выглядит
так что она ждет работы или решения адресата - надо отвечать. если же нет, то пустую конфирмацию
не надо. спросившая сессия же должна говорить нужна ли ей конфирмация или ждет ли она
результатов работы." The rule as landed spoke of the sender alone. A fourth gap, taken into the
rewording: the sender says what it waits for; the receiver answers what asks for an answer and
what waits on its work or decision unsaid, and sends nothing to the rest.

The user, 2026-11-16, of the session mechanism's block in the entry file: "правила сессий
устанавливающиеся в agents.md какие-то огромные. они для умной модели?" Measured the same hour:
the block is 51 lines and 3,516 characters, the largest any mechanism installs there, and S10
alone 26 lines — written twice that day, each trial answering an ambiguity with more words. It
is paid by every session at every turn, and its detail is wanted at one occasion, writing to
another session. Put to the person, not done: the entry file keeps the rule's few lines, and what
a message carries on each occasion moves to where it is read at that occasion.

Of the point left open at decision 2 — whether a role's sleeping session is written only what
will still hold when it wakes — the session that holds the rows answered from what it saw,
2026-11-16: in the desktop app a message wakes the session it is sent to; its sends to an idle
session came back delivered, the turn started. A session in another permission mode holds a
message for its person's approval, and a remote or cloud session reports nothing. So where
sessions run in the desktop app a sleeper reads a message at once, and the clause would bear
only on the routes that hold a message. Not added to the rule.

The user, the same day, of where the block's detail goes: "всю необходимую в моменте инструкцию
должна нести agents.md, но сжато и с ссылками". So the detail does not leave for a skill a
session must remember to open: the entry file carries the whole instruction a session needs at
the moment, compressed, and links what it compresses.

## The person, 2026-11-21: should messages be grouped

The user, to the keeper, after a day of that session's messages: "а вот мы посылаем сообщения
каждый раз, действительно, а не стоит как-то группировать". Not a decision; a question on S10's
"one message per occasion".

What the keeper's own day shows, counted from its chat, 2026-11-20 to 2026-11-21: 17 messages
sent — six to the store's session, five to game-delta's keeper, three to the audit's, two to the
practice's, one to the product's. Fourteen of them waited for nothing: a change landed, a
decision recorded, a finding given its home. Each started a turn in its receiver. Within one
turn there was never more than one message to a receiver; the seventeen are seventeen occasions,
as the rule asks.

What the count of 2026-11-15 already said
([inter-session-messages-2026-11-15.md](../research/inter-session-messages-2026-11-15.md)): the
surveyed sessions' common complaint was rules and news arriving one by one, several a day; one
batched message per session saying what changed for it was among the messages worth sending; the
sessions asked for batching, and it was "the sessions' ask, not yet his". game-delta's own L10
says one message to each receiver, never one per piece of news, where S10 says one per occasion
([q-t5vmk3](q-t5vmk3-how-does-core-reach-a-recipient-tree-and-leave-it-working-at-a-first-install-and-at-each-update.md),
*A case, 2026-11-21*).

**Decided** *(the user, 2026-11-21: "Да, группировать")*, of the keeper's proposal as put to
them: what is urgent goes at once — a question, a break made in what the receiver runs, a
collision on one file, what the receiver would go wrong without now; the rest is held and goes
as one message to a receiver, when that receiver is written anyway or when silence would start
to cost it. The rule's text is the session mechanism's, written and put to the person by the
session that holds the store; until it lands S10 stands as written.
