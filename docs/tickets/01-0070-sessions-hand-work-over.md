# Sessions hand work to each other, and none takes what another holds

- **record of** what it intends to become
- **Status:** Planned (its two slices carry the work)
- **Type:** HITL
- **Minted:** 2026-10-24
- **Answers:** [q-0037.0017.0006](../questions/q-0037.0017.0006-how-do-sessions-hand-work-to-each-other-a-verification-a-close-a-unit-and-when-may-one-take-over-what-another-is-on.md)
- **Outcome:** A session about to act on a unit another running session holds stops and puts three
  ways to act to the person, and a handover reaches the holder as a record it can act on, so no
  session finishes, closes or commits another's work by default.

## Parent

The session mechanism, [session.md](../../.agents/mechanisms/session/session.md), which owns every
rule on how sessions interact. The work's shape is
[its question's *Where it stands*](../questions/q-0037.0017.0006-how-do-sessions-hand-work-to-each-other-a-verification-a-close-a-unit-and-when-may-one-take-over-what-another-is-on.md#where-it-stands--2026-10-24),
accepted by the person 2026-10-24; the split's impact is
[in the same question](../questions/q-0037.0017.0006-how-do-sessions-hand-work-to-each-other-a-verification-a-close-a-unit-and-when-may-one-take-over-what-another-is-on.md#impact-of-the-split--2026-10-24).
The end-state of two slices:
[01-0070.0010 a-sessions-row-names-the-unit-it-holds](./01-0070.0010-a-sessions-row-names-the-unit-it-holds.md)
and [01-0070.0020 a-session-stops-before-anothers-unit](./01-0070.0020-a-session-stops-before-anothers-unit.md).

## What to build

What holds once both slices land. A session's row names the unit it holds, the ticket In progress
it took, and the ticket names no session, since sessions are lost and records stay, and the
session mechanism cannot stand on another mechanism's format. A turn that would finish, close,
commit, continue or duplicate a unit another running session holds stops: it says whose the unit
is and where the two touch, brings three ways to act — the holder releases it, this session judges
it, a sub-task is cut and taken here — with a recommendation, and does nothing on the unit until
the person names one. A handover is written into the unit's record and the holder woken to act on
it where the host can reach it; where it cannot, the session that wrote the verdict closes. The
agent's bias to do as much as it can itself is named in the entry file's general rules. A judge's
verdict, and the holder closing on it, are TICKET-FORMAT's already, landed 2026-10-23 with register
entry 65; this ticket builds on them and does not restate them.

## Acceptance criteria

- [ ] Both slices are Done.
- [ ] In a live tree with two running sessions, one holding a ticket In progress, the other asked
      by the person to close it stops with the three ways, and the close is made by the holder or
      by the way the person named — read by a judge who did not build it, from the transcripts.
- [ ] `/verify` passes against this ticket and its slices.

## Out of scope

- How a judge's role is declared — [q-0037.0005](../questions/q-0037.0005-what-is-an-agent-role-and-which-mechanism-keeps-roles.md).
- A session's plan read as the questions one feature links — decision 1 of the question, later.
- A messaging protocol of the method's own: messaging is the host's seam,
  [the hosts edge](../edge/hosts.md).
