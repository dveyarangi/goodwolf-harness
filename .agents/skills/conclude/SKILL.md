---
name: conclude
description: >-
  Use when a session ends, or the user asks to conclude the current chat.
---

Mechanism: session

First go over the session once more for what it left undone — a step a reply promised and did not
take, a decision not landed in its home, a change of its own not committed, drift met and left
unrepaired, untold and undecided — and finish or name each.

Write one session record under `docs/sessions/`: the account of what happened, for a reader who
has the tree and not the transcript. Substance before form — a session that produced decisions
is recorded by its decisions, not by its commits. It opens with
`- **record of** what happened`, the line after its title: it is of that kind and no other —
never repaired, never copied into a record of another kind. It holds:

- Each decision with what chose it: the alternatives weighed, what refuted them, and the
  correction that turned the answer, in the user's words where the wording carried the point.
  The decision's home holds the result and who decided it; the reasoning stays here unless an
  evidence file or an ADR took it.
- General principles the session derived that have no durable home yet, each named as such, so
  the next session lands it rather than rediscovers it.
- What was done, briefly; what another record holds in full is linked, not repeated.
- What was refuted or went wrong, and what it taught.
- The open questions the session touched, each with where it stands and what it waits on.
- What continues, and the first step of the next session.
Session files live under `docs/sessions/`, named `NNNN-<YYYYMMDD>-<name>` with a constantly incrementing number:
the session record, tier 2, read by the next session's `/recall` and kept. The session mechanism's
other record is the row, one file per session under `docs/sessions/rows/`, named by its tag and
holding `<tag> running|ended <YYYY-MM-DDTHH:MMZ> <q-id>|- [<q-id>,… up to four] [holds <q-id> | taken <q-id> by <tag>]`;
tier 1 through
the window and the wake's read; gone when it reads ended and its time is seven days or older.
The script writes it, never a hand.

The session's unpushed commits are the conclude's to settle, once the ended row is committed, as
the project's way of working with git says in its local file.

Where the host lets a session rename itself, prefix this session's name there with `(closed) `
before the row is ended.

## Installed from other mechanisms

<installed by="questions">
**Q3** Write a lean line on each question the session touched and left open —
`questions.py lean q-N '<line>' --session <tag>` — and nothing else: placements and closures were written as they
happened.
</installed>

<installed by="session">
**S2** As the conclude's last act, run `sessions.py --end --session <tag>`.
</installed>
