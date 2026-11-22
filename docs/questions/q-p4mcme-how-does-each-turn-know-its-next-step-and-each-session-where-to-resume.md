# q-p4mcme How does each turn know its next step, and each session where to resume?

- **record of** what it intends to become
- **part of** q-fjlob4
- **state** open
- **owner** [01-0020](../tickets/01-0020-each-turn-knows-its-next-step.md)
- **realizes** A4 "A session resumes at its step", A44 "One step per reply"
- **rung** development: load-bearing, self-improvement: the method
- **lean** session 49: a Claude Code session is keyed on the desktop app own id for the conversation, so a reopening under a new id resumes it; observed passing in the app and the terminal; the transcript match removed
- **opened** 2026-10-03T11:36:26Z
- **struck** 5, last 2026-11-22T00:26Z

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
