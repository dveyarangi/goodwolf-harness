# How a context fills, and what a bound on it costs — 2026-11-10 to 2026-11-25

- **record of** what happened

The scripts behind *Whether 20 % is real* and *No letters, if a chat clears itself* of
[q-mvd4pi](../../questions/q-mvd4pi-how-does-a-session-take-on-a-standing-role-learn-it-and-hand-it-on-so-the-role-outlives-any-one-chat.md),
where what they read is written. Over Claude Code's transcripts on this machine; no model called.

- [fill.py](fill.py) `<since>` — the first request, the end of the first turn, the growth a message, and
  the person's messages before a context passes a bound.
- [wakes.py](wakes.py) — what another session's letters woke in this tree, and the same to chats
  cleared.
- [failures.py](failures.py) — the register's dated failures by how full the context was, and the tools
  used; run from the tree's root.
