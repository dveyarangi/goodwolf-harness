# Session 33 — Cursor live lands without the window

**2026-10-03.** A Cursor agent chat under v22, first message a ping, to observe the last host
row of [01-0011.0100.0010](../tickets/done/01-0011.0100.0010-the-store-and-questions-writes-it.md).
No wake and no window were in context.

## What happened

**Cursor live, recorded on [01-0010.0120](../tickets/01-0010.0120-host-delivery-surfaces.md).**
The agent registered as `s-1003-7b62` by a bare `questions.py --wake`, placed itself at q-0001,
and drew the window by the entry file's rule. `sessionStart` → `additional_context` did not
arrive.

**Why.** Cursor's `sessionStart` is fire-and-forget; `additional_context` is a confirmed drop
(composer handle race). This chat has no host-id line, so a successful registration did not
complete: the event payload documents `session_id`, `questions.py` reads only `conversation_id`,
and fed `session_id` alone it writes nothing. Whether the command executed is the Hooks output
channel's. Accepting `session_id` as well was offered, not made — it still would not put the
wake in the first turn.

## Continuation

- **Next in the ring:** [`.0020` open-issues-are-entries-of-the-store](../tickets/01-0011.0100.0020-open-issues-are-entries-of-the-store.md),
  HITL, which opens at `/align`.
- **Still open under q-0001:** q-0001.0006 — a conversation's position when the host resumes it under
  a new session id; this session is a minted tag beside the host id.
- **Uncommitted:** the 0120 Cursor observation, this record. Session 31's leftovers remain that
  session's.
