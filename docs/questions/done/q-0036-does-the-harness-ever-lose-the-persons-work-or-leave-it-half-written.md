# q-0036 Does the harness ever lose the person's work, or leave it half-written?

- **record of** what happened
- **state** closed:decided
- **owner** [01-0035](../../tickets/done/01-0035-the-harness-never-loses-the-persons-work.md)
- **answer** [01-0035](../../tickets/done/01-0035-the-harness-never-loses-the-persons-work.md) — no longer, for the four losses found: each refused before its write or its write kept whole, each held by a test; the user, 2026-10-13
- **struck** 0, last 2026-10-13T07:34Z

Opened 2026-10-13 from [the outside audit of that day](../../research/external-audit-2026-10-13.md),
which found the data-loss findings of [the audit of 2026-09-30](../../research/project-evaluation-2026-09-30/REPORT.md)
still open and with no home. What governs the answer is
[Interruption and recovery](../../architecture.md#interruption-and-recovery): a preflight refusal
changes no files; expected contents are re-checked before a write and interference is a failure;
the harness locks nothing *(the user, 2026-10-11)*.

## Impact of the split, 2026-10-13

**Impact.** Three slices repair code to a contract already written: the mover's source re-check
(E3, [move_doc.py](../../../.agents/scripts/gw/move_doc.py)); the installer's validation of local
rules and overrides before its first write, `_inject` running after `_write` today (E2,
[harness.py](../../../.agents/scripts/gw/harness.py)); an update refusing a new path the project
already holds, `_write` overwriting it silently today (E1). Each adds a regression test for the
loss it closes and no new abstraction. The fourth, the sessions file, is read and written by the
wake, the window, `--check` and the conclude; its writer re-reads, edits and renames, so the last
of two simultaneous writers wins.

**Hidden edges.** The sessions slice cannot take the lock the audit proposes without reopening
"locks nothing"; its two shapes — a file per session, or re-read, compare and retry before the
rename — differ in what they touch, the first every reader of the file, the second only the writer
while narrowing the race rather than closing it. A session at q-0035 may be working in
`questions.py` at the same time. The README's promise to move an existing `CLAUDE.md` aside is
[01-0010.0150 harness-meets-a-tree-with-a-method](../../tickets/01-0010.0150-harness-meets-a-tree-with-a-method.md)'s
work, and its wording q-0031's.

**Leave alone.** "Locks nothing" in the first three slices; the sessions file's format beyond what
the race needs.

**Recommendation.** Narrow: the sessions slice HITL, the rest AFK; then proceed.
