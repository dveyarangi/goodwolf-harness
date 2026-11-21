# A tree's standing sessions each answer for an area, and the cut is kept true

- **record of** what it intends to become
- **Status:** Ready (split 2026-11-18, its slices re-ordered 2026-11-20)
- **Type:** HITL
- **Minted:** 2026-11-15
- **Answers:** [q-ja5mp4](../questions/q-ja5mp4-does-the-method-have-one-session-direct-the-others-an-orchestrator-and-what-does-it-owe-the-sessions-it.md)
- **Outcome:** In a tree with several standing sessions each role's zone and brief stand in a
  mechanism of the role's own, a table says which session holds which role, a session that writes
  in another's zone is told whose it is, and `/pack` proposes how the cut should change when
  sessions collide or a zone outgrows its session.

## Parent

[The session mechanism](../../.agents/mechanisms/session/session.md), whose part the keeping of
the cut is. The whole is the question's accepted
[Where it stands](../questions/q-ja5mp4-does-the-method-have-one-session-direct-the-others-an-orchestrator-and-what-does-it-owe-the-sessions-it.md#where-it-stands),
of 2026-11-17; the impact of splitting it:
[q-ja5mp4](../questions/q-ja5mp4-does-the-method-have-one-session-direct-the-others-an-orchestrator-and-what-does-it-owe-the-sessions-it.md#impact-of-the-split-2026-11-18).

## What to build

Nothing in the method says which standing sessions a tree needs, what each answers for, or when
that cut should change, and a session that answers for everything reads everything (the whole's
*The problem*). The whole is too coarse for one plan and is reached by its slices, each with its
own text; this ticket keeps the end-state that holds when all have landed.

1. [01-0090.0020 the-cut-is-read-against-the-work](./01-0090.0020-the-cut-is-read-against-the-work.md)
   — `/pack` and the session mechanism's section: the rules a cut is derived by, and where its
   record stands, in what form, who reads it and when; this tree's cut derived by its first run.
2. [01-0090.0010 each-role-of-this-tree-stands-in-a-mechanism-of-its-own](./01-0090.0010-each-role-of-this-tree-stands-in-a-mechanism-of-its-own.md)
   — the cut `/pack` derived written where `/pack` says: this tree's roles each in a mechanism of
   their own, and the table of who holds which in place of the list in the local rules.
3. [01-0090.0030 a-session-crossing-into-anothers-zone-is-told-whose-it-is](./01-0090.0030-a-session-crossing-into-anothers-zone-is-told-whose-it-is.md)
   — the telling at an edit in another role's path.

The order is the person's, 2026-11-20: a cut is derived by `/pack`'s own rules and never written
by hand, so `/pack` stands before any cut is written
([q-mz6gd4](../questions/q-mz6gd4-where-does-a-session-of-this-tree-read-each-roles-zone-and-brief-and-which-session-holds-it.md#decisions)).

*(Overturned 2026-11-21 as to "each in a mechanism of their own" in slice 2, and the same in the
Outcome and the criterion on a shift: a role is the mechanisms a session holds, so no mechanism
is written for a role, and who holds which is one table in the local rules —
[the plan](../rfc/01-0090.0020-the-cut-is-read-against-the-work.md#decided-by-the-person) of
[01-0090.0020](./01-0090.0020-the-cut-is-read-against-the-work.md), "Decided by the person". This
ticket and its second slice are rewritten once the table's form stands in that plan.)*

Kept here, and cut as a slice once its question is aligned: an install offers the default session
— the one that holds the harness — and the offer is never a requirement. What a fresh tree is
given at install is open
([q-wit7by](../questions/q-wit7by-what-does-a-fresh-tree-under-the-harness-need-to-set-up-standing-sessions-by-itself.md)),
fed by [the journal](../research/standing-sessions-journal.md), where each step of this work is
written with what a fresh tree would need to do the same.

Every instruction's text is shown to the person before it lands: the work changes the way of
working.

## Acceptance criteria

- [ ] Given a collision — two sessions editing the same two mechanism docs — a fresh session
      running `/pack` names the overlapping zones and a way to separate them, untold; judged by
      someone who did not build it.
- [ ] Run over this tree, `/pack` names the sessions the person actually runs, and proposes a
      new role only where a collision repeated or a zone outgrew its session.
- [ ] In a freshly installed tree the default session is offered, and declining it leaves
      nothing behind; judged on a fresh reader given only what a session would read.
- [ ] A session that took a role starts with less in its context than a free session in the
      same tree, counted, and still answers a question of its own zone rightly.
- [ ] A session that edits a file in another role's path is told whose it is.
- [ ] After a shift the person decided, the table and the mechanisms of the roles it touched
      agree, and every session reads the new cut at its next turn.
- [ ] `/verify` passes against this ticket and the governing docs.

## Out of scope

- The window drawn for a role's zone, where most of the reading is saved, and whose the files are
  that stay shared for good:
  [q-gus5k2](../questions/q-gus5k2-how-is-each-areas-knowledge-kept-apart-so-a-session-holds-its-own-areas-context-and-the-boundary-stays.md).
- A role's rights and skill set: [q-p4sdnv](../questions/q-p4sdnv-what-is-an-agent-role-and-which-mechanism-keeps-roles.md).
- The record of who touched a file, where a role's session sees an edit made in its zone: it
  waits on the store's server,
  [01-0010.0250 every-session-shares-one-store-through-the-coordinator](./01-0010.0250-every-session-shares-one-store-through-the-coordinator.md).
- The lander as a role with a session, and a worktree per writing session:
  [q-7ebz2f](../questions/q-7ebz2f-how-do-sessions-on-separate-branches-share-one-question-store-and-one-registry-of-sessions.md).
- How sessions reach each other and when one writes to another:
  [q-cdw6yk](../questions/q-cdw6yk-when-does-a-session-write-to-another-session-and-to-which.md).
