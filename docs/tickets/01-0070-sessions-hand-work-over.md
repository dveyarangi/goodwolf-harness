# Sessions hand work to each other, and none takes what another holds

- **record of** what it intends to become
- **Status:** Partial (2026-10-25, both slices Done; its live case and one word of the stop wait)
- **Type:** HITL
- **Minted:** 2026-10-24
- **Answers:** [q-0037.0017.0006](../questions/q-0037.0017.0006-how-do-sessions-hand-work-to-each-other-a-verification-a-close-a-unit-and-when-may-one-take-over-what-another-is-on.md)
- **Outcome:** A session about to act on a unit another running session holds stops and puts two
  ways to act to the person, and a unit taken over leaves its holder the mark of who took it, so no
  session finishes, closes or commits another's work by default.

## Parent

The session mechanism, [session.md](../../.agents/mechanisms/session/session.md), which owns every
rule on how sessions interact. The work's shape is
[its question's *Where it stands*](../questions/q-0037.0017.0006-how-do-sessions-hand-work-to-each-other-a-verification-a-close-a-unit-and-when-may-one-take-over-what-another-is-on.md#where-it-stands),
accepted by the person 2026-10-24 and rewritten to their decisions of 2026-10-25; the split's impact is
[in the same question](../questions/q-0037.0017.0006-how-do-sessions-hand-work-to-each-other-a-verification-a-close-a-unit-and-when-may-one-take-over-what-another-is-on.md#impact-of-the-split--2026-10-24).
The end-state of two slices:
[01-0070.0010 a-sessions-row-names-the-unit-it-holds](./done/01-0070.0010-a-sessions-row-names-the-unit-it-holds.md)
and [01-0070.0020 a-session-stops-before-anothers-unit](./done/01-0070.0020-a-session-stops-before-anothers-unit.md).

## What to build

What holds once both slices land. A session's row names the unit it holds, by the question the
unit answers, and the ticket names no session, since sessions are lost and records stay, and the
session mechanism cannot stand on another mechanism's format. A turn that would finish, close,
verify, commit or continue a unit another running session holds stops: it says whose the unit
is and where the two touch, brings two ways to act — this session takes the unit over, leaving the
holder the mark of who took it, or a sub-task is cut and taken here — with a recommendation, and
does nothing on the unit until the person names one; the person's word to take it over is acted
on without asking again and lets go the unit the taking session held, as a hold at a step's start
does *(decisions 14 and 15)*. The stop is one rule read off the window, the refusal at a hold the
stop where the window does not reach *(decision 11)*, and any session writes any row *(decision
9)*. Who judges what its builder built is q-0037.0015's, a subagent by the entry file's principle
*(decisions 10 to 12)*. The agent's bias to do as much as it can itself is named in the entry
file's general rules.

## Acceptance criteria

- [x] Both slices are Done — 2026-10-25, judged pass.
- [ ] In a live tree with two running sessions, one holding a ticket In progress, the other asked
      by the person to close it stops with the two ways, and the close is made by the holder or by
      the way the person named — read by a subagent judge, from the rows and the windows.
- [ ] `/verify` passes against this ticket and its slices.

## Out of scope

- How a role is declared — [q-0037.0005](../questions/q-0037.0005-what-is-an-agent-role-and-which-mechanism-keeps-roles.md).
- A session's plan read as the questions one feature links — decision 1 of the question, later.
- A messaging protocol of the method's own: messaging is the host's seam,
  [the hosts edge](../edge/hosts.md).
