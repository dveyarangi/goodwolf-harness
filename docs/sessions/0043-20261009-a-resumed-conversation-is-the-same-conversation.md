# Session 43 — a resumed conversation is the same conversation

**2026-10-09.** Claude Code, session `eb103bd9…`. Entry contract v42 at the start, v44 at the
close. Parallel sessions worked q-0033, q-0001.0022–.0023 and q-0018.0020 in the same tree; their
files, `README.md` among them, were left alone.

## What was decided, and what chose it

### /recall runs once per conversation, and the hook knows a resumed one — v43

The user brought a line from another session: after they stopped and rolled back a reply, the
agent announced that the host had resumed the conversation under a new session id and ran /recall
again. Their question: *does a second recall make sense at all, or is the context kept when the
session id changes?* It is kept: a rollback in the desktop app resumes the same conversation, its
transcript carried over under a new id, the first recall in it. The agent had obeyed two things
worded too loosely: the straw dog *Run /recall first in every session*, which read "session" as
the host's id, and the questions hook, which answered an unknown id with *registered now*, the
same as a new session. The user: *fix it now.*

- The straw dog now says *conversation*, and that one resumed under a new id is the same one
  ([rule failure 23](../rule-failures.md)).
- The Claude Code hook finds the session a new id continues: the resumed transcript repeats the
  old messages under the uuids they had, so the registered session whose transcript, beside the
  new one, holds the new one's first message is the one continued. The new id takes its
  position, the old row ends, and the start says no new recall is due. Of several matches, the
  latest written. Recorded in the questions mechanism's doc under *Delivery*.

Alternative weighed and left: trusting the payload's `source: resume`. It does not say which
session is continued, and a rollback may not send it; the transcript is the evidence.

### Text just written carries its 🧩 too — v44

The reply that reported the landed straw dog quoted it in a bare blockquote. The user: *why is it
not wrapped as 🧩? — everything planned to be added, or just added, must be wrapped with 🧩.* The
rule covered text *proposed*; once landed it read as no longer proposed. The bullet now covers
text written into such a record in this session, under `🧩 **Landed change — <record>**` or
`⚓ **Landed invariant — <record>**` ([rule failure 24](../rule-failures.md)). The agent offered
to wait, the user meaning to check the instruction in another session; the user: *land it here,
now.*

## What went wrong, and what it taught

The first live run of the predecessor lookup, read-only on the real transcripts, named this
session as the one the rollback continued: the grep that confirmed the shared uuids had quoted
one into this session's own transcript. A plain substring match counts quotation as identity.
The match is now on a message's own `"uuid":"…"` field, its quotes bare, since quoted text holds
them escaped, with a test for exactly this. Run again: `a9b67b24…` continues `693642b7…`, found in
0.03 s; a fresh session finds none in about 0.5 s. **Principle without a home yet:** a check run
on live data can be contaminated by the session running it — the evidence the agent gathered
became the input it then tested.

## What was done

- [questions.py](../../.agents/scripts/gw/questions.py): `_resumed_from`, `_first_message`, and a
  `transcript_field` on each host, Claude Code's only; four tests in `TheHook`, 207 green.
- `693642b7…`'s row ended by hand at the user's word: the rollback's original, which the fix,
  acting only at a start, could not end.
- Entry contract v43 and v44, recorded in
  [entry-contract-findings.md](../research/entry-contract-findings.md).

## Open questions touched

- **q-0001.0006** How does a conversation keep its position when its host resumes it under a new
  session id? Landed for Claude Code; open on one unseen fact: whether a resumed transcript is
  already written when its start hook runs. The next rollback shows it: its first hook output
  should read `resumes <old id>`. Codex and Cursor carry nothing yet.
- **q-0030** How does a reply show the principles each of its claims stands on, and where are the
  principles named for it? The form now at v44 with the landed line; `.0020` still waits on the
  week of grading.

## What continues

The user checks the v43–v44 instructions in another session. First step of the next session that
meets a rollback: read the start hook's line, and close or re-lean q-0001.0006 by it.
