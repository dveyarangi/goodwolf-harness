# q-p4mcme How does each turn know its next step, and each session where to resume?

- **record of** what it intends to become
- **part of** q-fjlob4
- **state** open
- **owner** [01-0020](../tickets/01-0020-each-turn-knows-its-next-step.md)
- **realizes** A4 "A session resumes at its step", A44 "A turn runs to the person's next decision"
- **rung** development: load-bearing, self-improvement: the method
- **lean** 2026-11-25: the live check is q-mvd4pi trial by the person word; 01-0020 closes on its verification, which found the accepted account overstated in three parts; the correction put to the person
- **opened** 2026-10-03T11:36:26Z
- **struck** 6, last 2026-11-24T23:40Z

## Where it stands

Accepted by the user, 2026-11-25: "Yes, accept"; its part on how 01-0020 closes is decision 4's since.

Every part of a turn's next step and a session's resume stands in a home of its own (decision
1): the wake is S6; the resume, the store's window keyed on the host's id for the conversation;
the stop for the person, the autonomy dial; the weight of the ceremony, `/impact` and *Weight
follows the work*; the order of work, `/pathfinder`; that a reply says what is next, the reply's
form. A turn chains steps until the first decision at or above its ladder's dial. How the loop's
granularity and ceremony become switchable, which the ticket also held, is open at q-p2tgdv, the
user's words carried there; nothing here decides it. `docs/process.md`
and the glossary's proposed *Unit of work* are gone (decisions 2 and 3). 01-0020 closes on its
verification; that a session which ended mid-ring is resumed by the next at its step is tried at
[q-mvd4pi](q-mvd4pi-how-does-a-session-take-on-a-standing-role-learn-it-and-hand-it-on-so-the-role-outlives-any-one-chat.md)
(decision 4). The product's answer
A44 reads "A turn runs to the person's next decision" since it was brought to decision 1.

## Decisions

1. **01-0020 is cut down to what no rule carries yet** — the user, 2026-11-22, of the align's
   opening reading: "Yes, cut it down". Each part the ticket set out to build has a home: the
   wake, S6; resuming after a break, the store's window — the question a session stands on and the
   unit it holds — keyed on the host's id for the conversation; the stop for the person, the
   autonomy dial; the weight of the ceremony, `/impact` and *Weight follows the work*; the queue's
   order, `/pathfinder`; `/recall`, the session mechanism; that a reply says what is next, the
   reply's form. A turn chains steps up to the first decision at or above its ladder's dial: the
   allowance the user named on 2026-09-06 is the dial, and no rule holds a turn to one step. Left
   to the ticket: `docs/process.md`, the glossary's *Unit of work*, and the record of where each
   part went. Not: a one-step rule standing apart from the dial.
   → [the method's glossary, *Turn*](../../.agents/glossary.md).
2. **`docs/process.md` is removed** — the user, 2026-11-22: "Yes, remove it". No rule lived there
   alone: its straw dog waited on the pacer, dissolved; *Work and documents* retold the entry
   file's helpers, the path's reading at `/recall` and Q6, and said wrongly that the skills link
   the check set, which L3 installs inline; *Naming*, *Autonomy and repair* and *Verification*
   pointed to the ticket format, the entry file's *Autonomy* and L3. What it kept of its own — the
   user's request of 2026-09-05 and the bootstrap's renaming — is history, which git keeps. This
   answers q-t34gyc. Not: a page kept to point at the homes.
   → [the entry file](../../AGENTS.md), where the retold rules stand.
3. **The glossary's *Unit of work — proposed definition* is removed** — the user, 2026-11-22:
   "Yes, remove it". The method says *unit* of what goes round the delivery ring — a ticket here,
   an item on a project's board — and the method's glossary defines a ticket as a tracked unit of
   agreed work; the proposed sense, work at any scale up to a milestone, was used nowhere. The
   scales it pointed to stay as evidence below. Not: an entry of its own in the method's glossary.
   → [the method's glossary, *Ticket*](../../.agents/glossary.md).
4. **The live check is q-mvd4pi's trial, and 01-0020 closes** — the user, 2026-11-25, who saw that the
   Хранилище session prepares the same observation ("а разве хранилище сейчас делает не ровно это?"),
   to the agent's recommendation: "Yes, move and close". The trial is to have the work at its middle and
   resumed at the same step, by the next session, with the person restating nothing, read by a judge
   who did not build it; A4 goes with it.
   → [q-mvd4pi](q-mvd4pi-how-does-a-session-take-on-a-standing-role-learn-it-and-hand-it-on-so-the-role-outlives-any-one-chat.md), told to its session. Not: 01-0020 waiting for a case of its own.

## Evidence — a correction ended the next move, 2026-10-26

In Codex chat `01a177e0-ff53-7c93-9cd3-bcdb4c70db5c`, the first reply to
«приветус, что у нас?» completed the recall with the four tasks in progress, a recommendation
to check the voice and a decision row. The user then asked why the reply did not speak like Lem.
The next reply acknowledged the failure and withdrew the recommendation, but offered neither
a way to investigate it nor a replacement next step. The user asked why the work stopped.

An independent reader, `/root/judge_followthrough`, confirmed this transition. It distinguished
the case from a recall that never proposes work: the first reply did propose it. There was no
reason to stop preparing a concrete next move; changing the method would require the person's
decision. L9 and the next-step instructions had reached the session. A model-internal cause,
and a cause of the reported difference from Claude Code, were not established.

The voice experiment is recorded in
[the voice question](q-53jkvy-is-the-voice-a-reply-speaks-in-its-own-mechanism-owning-how-everything-the-person-hears-is-said-apart.md#evidence--an-isolated-second-pass-2026-10-26).
An attempted handoff of the continuation case to chat `01a17792-eb83-75d1-9fc4-dedb2eed8589`
was refused because that chat is archived; it was not reopened. No completion guard was changed.

## Evidence — distinguishing the stops, 2026-10-26

The project's `.codex/hooks.json` wires SessionStart, UserPromptSubmit and PostCompact;
`.claude/settings.json` wires SessionStart and UserPromptSubmit. Neither project file wires Stop.
This does not establish the absence of hooks from other active configuration layers. OpenAI's
[current hook documentation](https://learn.chatgpt.com/docs/hooks#stop), read on this date,
documents a Stop hook's blocking decision as a request to continue the turn, with its reason
becoming a new continuation prompt. That behaviour was not tested live here.

A fresh reader, `/root/judge_stop_cases`, read the current entry file and recall skill, then four
excerpts of this conversation without an expected verdict. It returned the explanation of the
voice failure to work: acknowledging the failure left the entry file's existing Self-improvement
obligation unfulfilled, specifically registration and preparation of a repair. It allowed the
initial recall's choice, the later prepared choice with its blocked push, and the user's request
for just a short passage like Lem. A missing next-step sentence alone did not make a stop wrong.

The reader assessed supplied excerpts, not complete host transcripts. This establishes no
automatic check's accuracy or live hook behaviour, and no cause of the difference from Claude
Code. The observed distinction is a concrete unfulfilled obligation, not a requirement that every
answer propose more work. No instruction or hook was changed.

## Evidence — what the pacer held, carried from docs/pacer.md, 2026-11-22

Carried when `docs/pacer.md` was emptied ahead of its removal; the person agreed the homes,
2026-11-22 ("да, все верно"). A hypothesis, as the pacer held it, not a decision.

**Scales.** Work scale, the understanding of its shape and the next execution step are held
apart; candidate scales, not a required hierarchy of records:

| Scale | What is controlled | Typical representation |
|---|---|---|
| Direction / milestone / capability | Intended change and governing agreements | A question's `Where it stands`, a roadmap or a parent ticket |
| Delivery work | A verifiable slice, dependencies and readiness | A ticket or subticket |
| Execution step | One bounded operation or pass and its feedback | A skill invocation, or a bounded stage within it |

A unit of work named without its scale is not enough to choose a step by. An execution step is a
bounded pass with known input state, one purpose, an expected output and a point where it is
reassessed; a skill invocation is a candidate step, not a guarantee of boundedness.

**A "next thing" request.** Name the outcome it belongs to and its scale, where the work stands,
the last pass and what it showed, the constraints and authorization, then the next bounded step,
what it should yield and when to reassess. "Deliver the milestone" is not a step.

**Chaining.** The user, 2026-09-06: chaining steps inside one turn, up to the next human
checkpoint, is the intended later shape — a stated allowance once the principles settle, never
the default.

**Read against today, 2026-11-22.** A standing session seldom runs `/recall`: the question of the
next step comes at every step's end, not only at a wake, so this question and its ticket,
written around the wake, are to be read again. `/impact` already weighs a work's volume and its
form — an align for load-bearing work, tickets for mechanical; the person: the one who cuts the
work and the one who names its ceremony seem one actor. Dropped: the pacer's note that a project's
maturity is not read from its age or its commit count — `/impact`'s load-bearing test reads what
a change touches, not how old the project is; the user, 2026-11-22: "про зрелость можно
выкинуть".

## Evidence — the written queue's order, carried from 01-0020, 2026-11-25

Carried when the ticket was rewritten, which alone held it. The user, 2026-09-27, of the
queue then written by hand, retracting an agreement in principle of 2026-09-20: the order is not
re-ranked mechanically when delivery state moves; it changes by the user's decision, when
priorities or product requirements change, when the order is found inconsistent, or when a HITL
ticket's resolution meets unpredicted complexity or a split that forces a reordering. The written
queue is since withdrawn and the order of work is `/pathfinder`'s.

## Evidence — a judge's reading of resumed sessions, 2026-11-25

A fresh reader, given 01-0020's criterion and the transcripts and not the builder's view, this
session excluded as a case. Its verdict: met as worded, on one case of a conversation that ended
and another that took its unit up; none of that kind since units are held (2026-10-24).

- **The case.** 01-0011.0110.0055, conversation `e5a0f888`, concluded 2026-10-12T14:20Z mid-`/implement`;
  taken up by `b46a6e3c` on 2026-10-13, two sessions concluded between. The person's first words:
  «привет волчара». The recall named the unit and what of it remained, as its record did; the
  person then named the ticket and asked what to do; nothing was redone. The commits: 44352beb,
  b4f69c02, e3d471ac. It ran before unit holds, and part of the work ran in another tree.
- **The same conversation, resumed** after its host stopped it, twice, at the right step
  (2026-11-10, 2026-11-16): its context was intact, so it does not show the records carrying the
  resume.
- **Against it.** Units whose holder ended and nobody resumed: 01-0010.0125.0010, 01-0010.0240.0020,
  and 01-0018.0010, its holder's conversation deleted with the unit held. No resume was found
  redoing finished work or asking the person where things stood; not every host restart was read.
- **The wording.** The ticket said until 2026-11-25 *resumed by the next session*; the accepted
  `Where it stands` and the rewritten criterion leave the last four words out, and a conversation
  resumed by its host would pass without them.

## Evidence — a verifier's reading of the homes, 2026-11-25

A fresh reader held the ticket to decision 1, part by part. Whole: the wake, the stop for the person,
the order of work, `/recall`, the chaining, no one-step rule. Not whole, against decision 1 and
`Where it stands`:

- **The resume** holds for the same conversation and for one that takes its name (S11); a new
  conversation with neither is shown nothing of a unit an ended holder left, the wake listing running
  sessions alone; under an id the host does not keep steady it is *not yet* (q-ou6kps).
- **The weight of the ceremony** is not in `/impact`, whose body gives the blast radius alone
  (01-0010.0080); *Weight follows the work* is provisional, bound to q-p2tgdv.
- **That a reply says what is next** stands provisional, bound to q-awqz6b.

Decision 1 was put to the person as each part having its home; the agent's reading, not checked so.
