# The harness never loses the person's work

- **record of** what it intends to become
- **Status:** Planned
- **Type:** HITL
- **Minted:** 2026-10-13
- **Answers:** [q-0036](../questions/q-0036-does-the-harness-ever-lose-the-persons-work-or-leave-it-half-written.md)
- **Outcome:** No script of the harness overwrites, drops or half-writes what a person or another
  session wrote: each one either finishes whole or refuses before its first write.

## Parent

[Interruption and recovery](../architecture.md#interruption-and-recovery), which owns the
contract; the findings come from [the outside audit of 2026-10-13](../research/external-audit-2026-10-13.md)
and [the audit of 2026-09-30](../research/project-evaluation-2026-09-30/REPORT.md) (E1, E2, E3).
Split assessed in [q-0036's impact of the split](../questions/q-0036-does-the-harness-ever-lose-the-persons-work-or-leave-it-half-written.md#impact-of-the-split-2026-10-13).

## What to build

Four slices, independent of one another:
[.0010 a-moved-record-keeps-an-edit-made-while-it-moved](./done/01-0035.0010-a-moved-record-keeps-an-edit-made-while-it-moved.md),
[.0020 an-install-that-will-refuse-writes-nothing](./done/01-0035.0020-an-install-that-will-refuse-writes-nothing.md),
[.0030 an-update-never-replaces-a-file-the-project-owns](./01-0035.0030-an-update-never-replaces-a-file-the-project-owns.md),
[.0040 session-lines-written-at-once-all-survive](./01-0035.0040-session-lines-written-at-once-all-survive.md).
Each loss found is closed by a regression test that reproduces it, so it cannot return unseen.

## Acceptance criteria

- [ ] Each of the four losses — a moved record's intervening edit, a refused install's writes, a
      project's file at a path an update adds, a session's line written at once with another's —
      is reproduced by a test that fails before its slice and passes after.
- [ ] Every docstring and skill that promises a write is whole or refused says only what its code
      keeps.
- [ ] `/verify` has been run on this ticket against its children and the governing docs.

## Out of scope

- Moving an existing `CLAUDE.md` or `AGENTS.md` aside on install —
  [01-0010.0150 harness-meets-a-tree-with-a-method](./01-0010.0150-harness-meets-a-tree-with-a-method.md).
- A lock, or safe simultaneous writers in general — ruled out by
  [Interruption and recovery](../architecture.md#interruption-and-recovery).
- The window experiment's reproducibility (R1 of 2026-09-30) — with q-0017's experiment.
