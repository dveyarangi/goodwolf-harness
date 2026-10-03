# Session 34 — Codex fresh chat receives the wake and windows

**2026-10-03.** Codex desktop chat `01a0fef1-9b89-7873-826a-c2d7c38814f4`, under entry
contract v22. Recorded this fresh-chat test in
[01-0010.0120 host-delivery-surfaces](../tickets/01-0010.0120-host-delivery-surfaces.md),
including its capability-matrix row.

The wake arrived under the actual host session id before the test instruction and before any
agent command. An unchanged-window notice followed; after the agent's `at q-0001`, the next
message supplied the full window with that position. No manual wake was used. The rollout's
ordering supports startup delivery, but lacks the raw event needed to distinguish `SessionStart`
from the first prompt's registration fallback.

q-0001 remains open. Codex resume, compaction and helper ids remain unobserved in this test;
0120 permits named limits, so these are useful further observations rather than prerequisites
for every cell. Its broader matrix and dynamic-surface decisions remain open. The delivery
queue's next store slice is
[01-0011.0100.0020 open-issues-are-entries-of-the-store](../tickets/done/01-0011.0100.0020-open-issues-are-entries-of-the-store.md);
this evidence session did not start that cycle.

The user asked how session closure works, then requested `/conclude`, clarifying that no
questions should close. The handoff is saved; the lean update was declined, so q-0001's
existing lean is retained and the Codex evidence stays in 0120. The final registry operation
marks only this session ended, retaining its position for resumption. All questions stay open.
No implementation, commit or push was requested. Existing changes from other sessions remain
in the working tree alongside this evidence and handoff.
