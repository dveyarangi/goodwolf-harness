---
name: conclude
description: >-
  Use when a session ends, or the user asks to conclude the current chat.
---

<straw-dog question="q-0023.0006">Mechanism: not yet</straw-dog>

Write one session record under `docs/sessions/`: the account of what happened, for a reader who
has the tree and not the transcript. Substance before form — a session that produced decisions
is recorded by its decisions, not by its commits. It holds:

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
Session files live under `docs/sessions/`, named `NNNN-<YYYYMMDD>-<name>` with a constantly incrementing number.

## Installed from other mechanisms

<installed by="questions">
**Q3** Write a lean line on each question the session touched and left open —
`questions.py lean q-N '<line>' --session <tag>` — and nothing else: placements and closures were written as they
happened. As the conclude's last act, run `questions.py --end --session <tag>`.
</installed>
