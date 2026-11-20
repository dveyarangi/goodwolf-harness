# Messages between sessions — which were worth sending, 2026-11-15

- **record of** what happened

Evidence for [q-cdw6yk](../questions/q-cdw6yk-when-does-a-session-write-to-another-session-and-to-which.md),
gathered 2026-11-15/16 by a session the keeper started at the person's word. It holds material
and candidate rules, not a verdict.

## What was read, and how

Transcripts under `C:\Users\owner\.claude\projects\` were parsed by script. A received message
is the `<cross-session-message>` wrapper in the receiver's transcript, and a sent one is the
`SendMessage` / `send_message` call in the sender's. Copies a resumed transcript repeats were
removed. Each message went into a digest with the first 750 characters of its text, what its
receiver wrote next (520 characters), and the tools that receiver called before its next human
turn: the files it edited, its commits and the messages it sent. Nine subagents each classified
one slice of the digest, message by message, judging each message by what its receiver did next,
never by its tone. This session read this tree's 36 messages of 2026-11-15 itself and
spot-checked 12 random labels against the digest. Two of the 12 "effect" labels were debatable
(the receiver's next turn was empty) and no verdict looked wrong.

| Set | Messages | Span |
|---|---|---|
| game-delta, before L10 landed (2026-11-11 21:31Z, 117ba9e) | 229 | 11-09 … 11-11 |
| game-delta, after L10 | 668 | 11-11 … 11-15 |
| this tree, October | 114 | 10-11 … 10-30, most of it on 10-25 |
| this tree, 2026-11-15 | 36 | read by this session |

game-delta by day: 4, 6, 278 (11-11), 225, 103, 104, 177. Also read: game-delta's
`local.rules.md` (L7, L8, L10), its orchestration report with eight sessions' survey answers
(`docs/sessions/orchestration-report-2026-11-15.md`), its rule-failure register, the
orchestrator's own count of 2026-11-11 (read in its transcript), and the delivery results of all
1,348 sends.

**What a label means.** *Useful*: the receiver's work changed, a collision was prevented or
mended, a decision or hand-off arrived, or the sender got an answer it needed. *Vain*: nothing
would have gone differently without the message. *Mixed*: part of each.

## The count

| Set | Useful | Mixed | Vain | Not wholly useful |
|---|---|---|---|---|
| game-delta before L10 (229) | 179 | 29 | 21 | 22% |
| game-delta after L10 (668) | 536 | 67 | 65 | 20% |
| this tree, October (114) | 67 | 17 | 30 | 41% |
| this tree, 2026-11-15 (36) | 31 | 1 | 4 | 14% |

The orchestrator's own count of 2026-11-11 came from a different reader and a different rubric:
245 sent messages, of which 134 needed action, 55 were useful to know and 56 (23%) were noise. It
counted rule broadcasts as noise. The person answered that count: «рассылки правил это нормально
как раз / а важно да, добавь».

game-delta's share not wholly useful, by day: 22% (11-11), 25%, 17%, 13%, 17% (11-15).

### By kind, game-delta, all 897

| Kind | Count | Useful | Mixed | Vain |
|---|---|---|---|---|
| answer | 191 | 159 | 22 | 10 |
| the person's decision or a contract change | 151 | 125 | 23 | 3 |
| request in the receiver's area | 126 | 108 | 9 | 9 |
| hand-off | 119 | 116 | 3 | 0 |
| rule or mechanism | 76 | 52 | 8 | 16 |
| lines and shared files | 71 | 53 | 10 | 8 |
| breakage or blocker | 56 | 43 | 9 | 4 |
| status nobody asked for | 55 | 20 | 9 | 26 |
| question | 22 | 22 | 0 | 0 |
| correction of one's own message | 21 | 17 | 1 | 3 |
| acknowledgement | 9 | 0 | 2 | 7 |

Why a message was not wholly useful (182 in game-delta), before → after L10, per 100 messages:

| Reason | All | Before | After |
|---|---|---|---|
| the receiver could read it from git, a record or its window | 37 | 3.9 | 4.2 |
| stale on arrival, overtaken, crossed | 29 | 0.4 | 4.2 |
| duplicate, the receiver already had it | 27 | 5.2 | 2.2 |
| status nobody asked for | 25 | 3.9 | 2.4 |
| acknowledgement | 12 | 3.9 | 0.4 |
| a broadcast that changes nothing for this receiver | 12 | 0 | 1.8 |
| wrong addressee | 8 | 0.4 | 1.0 |
| the sender could have found it in the code or records | 4 | 1.3 | 0.1 |
| other | 28 | 2.6 | 3.3 |

## Kinds worth their cost

**Hand-offs along a known order**: 119, of which 116 were useful and none vain. This is the
steadiest traffic of all. The pair between a branch's owner and the merge session ("branch head
X, ready" in, "landed as Y, start from master" out) was acted on every time.
- Сценарии → Слияние, 2026-11-13: "The hold is off … db92b5e and 10bb20a on top of a625496 …
  the person played it … Ready to land." Слияние dropped a separate publish run so that one suite
  run covered both.
- Оптимизация → Геймплей, 2026-11-11: measurements and two named fixes. The owner cut a run's
  start from 1.77 s to 0.12 s within half an hour.

**Breakage and blockers sent to the owner, with the commit, the test and the reproduction**: 43
of 56 were useful.
- Слияние → Геймплей, 2026-11-12: "Your ccbec3f … makes rhythm_test.gd's … hang. Run alone on
  935e52d … it passes in 8 s". The loop was fixed within a minute. The suite had been stuck for
  about eight hours, and every landing and deploy waited on it.
- Сценарии → Геймплей, 2026-11-14: "Blocker: master doesn't compile … 9ae2727 … tunnel.gd at line
  1507". Fixed three minutes later in 1cf20a9.
- Сценарии → Оптимизация, 2026-11-13: a freeze report with the command that reproduces it. Found
  and fixed in about 15 minutes.

**Questions**: all 22 were useful, and only 4 messages in all of game-delta were judged
self-answerable. A question between sessions was never the waste. In this tree's October chunk
the 29 questions mostly came from one coordinator's shutdown poll, and they were useful too.

**The person's decision, with their words, dated, to the session that builds on it**: 125 of 151
were useful.
- Сценарии → Геймплей, 2026-11-14: «строим оба варианта пустоты, чтобы можно было и этот сохранить
  и новый проверить», with a proposed minimal form. Геймплей built it at once, in that form.
- A relayed approval to land or to add a rule was asked of the person again every time (d_02,
  d_08). A relayed change was acted on at once.

**Lines: who holds what in a shared file**: 53 of 71 were useful.
- Оптимизация → Музыка, 2026-11-12: it announced its uncommitted change in Музыка's file, and
  Музыка kept out of those functions until the hash came. The lines never mixed.
- Геймплей → Графика, 2026-11-14: "my commit 9ae2727 went around some uncommitted lines that look
  like yours; are they?" It was answered within the minute.
- Слияние → Музыка, 2026-11-13: "hold game/ commits". This ended four suite runs restarted by
  Музыка's commits, and the branch landed on the next try, 280/280.

**One message per receiver, tailored, with "what changes for you"**. Of the orchestrator's 12
broadcasts (one body to three or more receivers, 62 copies), the one every receiver acted on said
exactly that: "a short stop for the whole tree is coming … What changes for you"
(2026-11-15T01:14Z, 7 of 7). The orchestrator's review question, "answer in one message, change
nothing", drew seven substantive answers within minutes, which became one list for the person
and one commit, ff444e0.

## Kinds not worth their cost

**Status nobody asked for**: 26 of 55 vain, 9 mixed. "Clean", "committed", "fixed" sent to the
merge session changed nothing: its watcher polls master and acts on its own (d_03 and d_04
patterns). One example is a commit reported to a session that had just met it as a refused commit
on the same file (2026-11-14).

**Acknowledgement**: 7 of 9 vain. Before L10 there were 3.9 per 100 messages, after it 0.4, so
this is the clear effect of L10. In game-delta's last day no thread ended on thanks: receivers
told their person instead that no reply was needed. This tree has no such rule, and here today the
keeper's "taken — the plan's stage 1 now rewrites …" was answered with «С моей стороны здесь
делать нечего».

**Stale, overtaken, crossed**: 0.4 per 100 before L10, 4.2 after. This is the waste that grew.
Crossed messages cluster around landings and around the person's changing mind.
- Слияние → Музыка, 2026-11-12: three asks about lines Музыка had already committed. Each cost a
  reply and a 15-minute suite restart.
- Графика relayed each of the person's words on the Void's script to Сценарии as it was said,
  about twenty messages, several corrected within minutes ("Echo: grid shows through until
  period 6", four minutes later "Echo correction"). Сценарии then relayed them on to Геймплей.
  One change of mind cost two or three messages and a commit each.
- A blocker alarm about a test already fixed on master (2026-11-12).

**What the receiver could read from a record**: 37. These were landing notices with nothing
waiting on them, and reminders restating what the receiver had itself recorded hours before.

**Rule broadcasts, the common part**: 76 rule messages, 16 vain and 8 mixed, all of the vain ones
after L10. Every receiver retold the rule to its person, and it mattered only where the receiver
named a practice it would change. Слияние and Путь answered each of four fan-outs that nothing
changed for them. The gate then prints the same text at the first refusal anyway. The person
keeps broadcasts (2026-11-11), and the sessions asked for them batched, with "what changes for
you" (survey, 2026-11-15).

**Wrong addressee**: 8 in game-delta and 14 in this tree's October. In game-delta, the owner of a
commit or a line was guessed from a commit subject. A notice once went to the sender itself
(d_03-027), and the red test of 1b4a756 was blamed on Музыка when the commit was Геймплей's. In
this tree, senders chose a recipient by the question its registry row showed. A closed session's
row, flipped back to "running" when a message woke it, kept drawing mail: "Dial steps" received
front-page notes after it had concluded, recorded them and forwarded them, which led to
duplicates and a retraction that came too late. One test note acted on wrote a decision into
another's question, and the person later cancelled it.

**A claim relayed unchecked**: this tree, 2026-11-15, the keeper passed the coordinator's "a
re-run picks up the draft" to game-delta and had to send a correction after. In game-delta
2026-11-15, the orchestrator took uncommitted lines in `tunnel_biome.gd` for Геймплей's, then on
Геймплей's guess asked Графика to commit them. Both disclaimed: the lines were Музыка's, and
Музыка had told only Геймплей.

## Where a message was missing

The subagents recorded 98 cases in game-delta and 12 in this tree's October where a message was
needed and not sent, or came too late. This session grouped game-delta's cases (the counts are its
own grouping, approximate):

| What went unsaid | ≈ | How it was found | What it cost, typically |
|---|---|---|---|
| Uncommitted or staged lines left in a file, or under a branch, that another session works in | 26 | a refused landing or commit, a red test, a diff; two were left by sessions that had ended | a landing refused or its suite rerun (up to 40 min); the owner traced from edit records |
| One's own commit, or a half-edited shared tree, broke master or the tests | 15 | another session's suite, or opening the game | landing and deploy blocked for hours (12:35–15:08 on 11-13); the person met a blank game |
| The person's decision not carried to its owner, carried late, or crossed | 12 | the person playing; the owner reading another's record | work built and reverted; the owner recorded the opposite (6c1e705) |
| A contract, data form or tool changed; not every reader told | 11 | a refused landing; the person hearing or seeing it | a duplicated seam; a deploy broken live (index.js and wasm, 11-11) |
| A commit landed in game/ while another's suite or landing ran | 9 | the suite thrown away | a green 284-test run discarded; 40-minute restarts |
| The shared machine: test processes killed, captures and profiles on top of each other | 7 | empty runs; skewed measurements | repeated ~23-minute reruns |
| A commit took another's lines and the owner was not told, or was told through a third | 4 | git; a broken master | master stopped running (7155852) |
| Asked after acting, written to the person instead of the session, a hand-off without its conditions | 6 | the person, or the receiver asking | a second commit (ff444e0); a 40-minute run killed |
| A harness defect met and not passed on | 3 | the next session meeting it | the same false refusal met again |
| Ids minted in parallel | 2 | a third session's remark; an audit | renumbering |

Examples:
- Путь → Оркестратор only, 2026-11-11: it reported its uncommitted `flight_view.gd` edit but did
  not tell Графика, whose hunks were in that file. Its commit by path, 7155852, then took them and
  broke master. It took four sessions and about twelve messages to mend.
- Сценарии handed a branch to Слияние, 2026-11-15, without saying the person had not approved
  landing it. Слияние's run would have landed it; it was killed only because Слияние asked.
- The orchestrator's rebind note, 2026-11-15, said nothing about waiting, so Музыка committed into
  game/ in the middle of a landing run, a 40-minute restart.
- Путь sent the demo-ending order to Сценарии at 20:29 and to Музыка only at 20:35, after Музыка
  had recorded a closing chord on the old order.
- Оболочка proposed who owns `game.gd` to its person instead of asking the orchestrator. The
  person: «почему ты решаешь зоны ответственности?».

This tree's October cases: uncommitted edits in two tickets that seven sessions disowned; a
"lean" written into another session's question without telling it; two sessions taking the same
rule-failure entry; a 110-file rename that raced a question's close and was announced only
afterwards; nothing telling senders that a session was closed. On 2026-10-25 the scheduled
maintain pass could not send at all ("needs a person's approval"). On 2026-11-15 it could, and its
findings were acted on.

## What game-delta's L10 covers, and where it was broken or silent

L10 (2026-11-11): send what the receiver must act on or would go wrong without (a hand-off, a
blocker, a question, a change to its files or lines); always and at once, a commit that took any
of its lines; no acknowledgement, no unasked "done", nothing the two have already settled; one
message per receiver; the orchestrator tells the running sessions of each new rule.

**Held.** Acknowledgements fell from 3.9 to 0.4 per 100 messages and duplicates from 5.2 to 2.2.

**Held in part.** Of the commits after L10 that took another's lines:
- 87c3faa and 9ae2727 were told to the owner directly;
- 93a238d went through the orchestrator, because the owner was unknown;
- 59faf4a was reported only to the orchestrator, and its owner found it when master broke.

**Did not move.** The share of messages not wholly useful stayed at 22% before and 20% after.

**Broken.** Unasked status went on (2.4 per 100). Rules went out one by one, several a day: the
surveyed sessions' common complaint. The stream of one message per piece of news went on
(Графика → Сценарии, 11-12).

**Silent**, and this is where the remaining waste and almost every missing message fall:
- uncommitted work in another's file before any commit, the largest missing group;
- one's own red master;
- a hold while a suite runs;
- who the receiver is when the owner is unknown: L7 covers only a stray line, asked of the
  orchestrator, and the guesses that went to the wrong session;
- checking a claim before sending it, the source of the stale messages, which grew;
- the person's decision made in another session's area, with a route only by whoever heard it;
- what belongs in a record rather than a message;
- messages to a closed session;
- language: the sessions' messages are English while the person speaks Russian, and Сценарии
  translates twice.

## The orchestrator's answer

The question was asked once, 2026-11-15, with three questions, and answered 2026-11-16 in
Russian; summarized here. Its context had been compacted, so it said little of the days before
and did not know where the 11-11 count lay (it is in its own transcript, quoted above).

- **Worth it:**
  - a blocker with the specifics: Слияние's "whose reordering in `the-void-settings.json`, it
    blocks landing Сценарии's branch", settled by a stash in a minute;
  - a hand-off naming the function or commit (`SettingsMenu.from_launch` 8f484ae,
    `Music.from_launch` 4dc9cad);
  - one batched message per session saying what changed in its files, with the new rule
    (ff444e0), after which the sessions mended their parts without asking;
  - asking the owners before cutting the architecture: seven answers, all used.
- **Not worth it:** its own wrong message about another's lines; guesses of whose lines are whose
  passed on unchecked; the person's decision relayed through another session, which works but
  whose authority cannot be checked from the letter.
- **What L10 changed:** acknowledgements and unasked "done" stopped. It keeps to one message per
  receiver itself. "Got it, here is a correction" still comes now and then, and is useful when
  there is a correction.
- **What L10 does not cover:**
  - uncommitted lines nobody owns, which need a record of who touched the file rather than a
    letter;
  - who waits on what: the person asked, and it gathered the answer by reading transcripts;
  - a busy receiver queues a message, and the sender cannot tell when it will be read;
  - a hold while the full suite runs, which had to be written to each session by hand. Shared
    state belongs in a record, not a broadcast.

## Candidate rules the evidence supports

Each is given as: the occasion; to whom, and how the sender knows who that is; what the message
carries; what is never sent; and the evidence it stands on.

1. **Your uncommitted work sits in a file another session works in, or under a branch waiting to
   land; or your commit took its lines.**
   - **To:** the file's owner by the roster, and the merge session when a landing waits.
   - **Carries:** the file, the lines, the state they are left in, when they will be committed,
     what the owner must not redo.
   - **Never:** only after the collision; only to a third session when the owner is known.
   - **Stands on:** the largest missing group (≈26 + 4); 53 of 71 lines messages useful; two
     cases in this tree today. Strong. The orchestrator holds that the lasting answer is a
     record of who touched a file, not a letter.
2. **Your commit or your half-edited tree broke master or another's tests.**
   - **To:** the merge session and the sessions blocked by it.
   - **Carries:** the commit, the failing test, what was reproduced, when the fix lands.
   - **Never:** only the fix, after the others found the break.
   - **Stands on:** ≈15 missing; 43 of 56 breakage messages useful; the reports' speed of
     repair. Strong.
3. **A step of a declared order is done.**
   - **To:** the next session in that order.
   - **Carries:** the commits, what the person has and has not approved, what it waits on.
   - **Never:** "done" to a session outside the order.
   - **Stands on:** 116 of 119 hand-offs useful; the killed 40-minute run. Strong; the
     conditions part rests on one case.
4. **The person decided something in another session's area.**
   - **To:** that area's owner by the roster, once the decision has settled.
   - **Carries:** the person's words, dated, and where they are recorded; a correction replaces
     the earlier message and says so.
   - **Never:** a stream of interim values; an approval passed on as authority (receivers ask
     the person again anyway).
   - **Stands on:** 125 of 151 useful; the 23 mixed are relays the person's next word overtook;
     12 missing; the orchestrator's answer. Medium-strong.
5. **No acknowledgement, no unasked status.**
   - **Rule:** a message ends its thread unless it asks something, and the sender says when no
     answer is needed. "Committed", "clean" and "landed" go only to the session that waits on
     them.
   - **Stands on:** acknowledgement 7 of 9 vain, unasked status 26 of 55 vain, before L10 and
     after it; this tree today. Strong.
6. **Before you send a claim about another's lines, master or a commit, check it against git or
   the record.**
   - **Rule:** a guess of the owner goes as a question to the session the roster names, never as
     a request to commit.
   - **Stands on:** stale messages the largest growing waste (0.4 → 4.2 per 100); 37 readable from
     a record; 8 + 14 to the wrong addressee; the orchestrator's own lesson. Strong.
7. **A rule or mechanism change.**
   - **To:** the sessions it changes, in one batch.
   - **Carries:** what changes for you.
   - **Never:** the rule's text to a session it does not touch.
   - **Stands on:** 16 of 76 rule messages vain, all after L10; the one broadcast acted on by
     all; the survey. The person keeps broadcasts; batching and "for you" are the sessions'
     ask, not yet his. Medium.
8. **You are about to change a contract, a data form or a tool that others read.**
   - **To:** every reader at once, not one after another.
   - **Carries:** what changes and from which commit.
   - **Stands on:** ≈11 missing; Путь's staggered sends. Medium. Sessions ask for a list of who
     reads what.
9. **Shared state is a record, not a message.** A hold on commits while a suite runs, who
   touched a file, who waits on whom, master red, the machine busy: each is written once where
   every session reads it, instead of a message to each.
   - **Stands on:** ≈9 + 7 missing; the hand-written holds; the orchestrator's answer; the
     survey's asks (an owners map, a machine lease, a "master is red" flag, path-scoped holds).
   - This is where a rule about messages ends rather than a rule about messages. Medium.
10. **Address a session by its id, found in the roster or the window; never a closed session.**
    - **Stands on:** this tree's October (14 to the wrong addressee, closed sessions woken by
      mail); one misroute by an old title in game-delta; three dead pipe addresses. Medium for
      this tree, thin for game-delta.
11. **A question needs no restriction.** All 22 questions in game-delta were useful, and only 4
    messages were self-answerable. The count supports no rule here.

## What could not be read or verified

- The labels are subagents' readings of a digest: 750 characters of each message and what the
  receiver did before its next human turn. An effect after that turn is missed, and a receiver
  that got a message mid-turn shows an empty reaction. 12 labels were spot-checked; none was
  checked against git.
- The before and after sets of L10 differ in more than the rule. Before it, the sessions were
  fewer and task-titled, and most of that set is one day. The comparison is a hint, not a
  measure.
- The missing groups are this session's grouping of the subagents' 98 notes. The counts are
  approximate, and a case can fall in two groups.
- This tree's October traffic was partly a deliberate test of sessions meeting each other, and
  most of it was one shutdown poll. It is a weak sample of standing sessions.
- The orchestrator's 11-11 data files were not opened; its counts are quoted from its transcript,
  not re-derived. Its answer of 11-16 came from a compacted context, as it said itself.
- The per-chunk data stands in this session's scratchpad (`out\*.json`, `agg_all.json`), outside
  the repository, and may be cleared.
