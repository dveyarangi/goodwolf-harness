# Session 31 — the line becomes calls, and the store learns to count

**2026-10-02 to 2026-10-03.** Woke with `/recall` under v18, committed session 30's leftovers, and
ran the delivery ring over the questions mechanism's slices: three planned, one more incepted at
an align, all four built, verified and closed. Resumed once under a new host session id, which
left the old id running at a closed question until it was ended by hand.

## What happened

**Four slices of [01-0011.0100](../tickets/01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md),
each planned, implemented, verified and closed:**
- [`.0017`](../tickets/done/01-0011.0100.0017-an-entry-name-carries-its-whole-question.md): an
  entry's name holds its whole question, and the check holds every name to it.
- [`.0011`](../tickets/done/01-0011.0100.0011-the-agent-calls-a-subcommand-per-event.md): the
  declared line's grammar replaced by a `questions.py` subcommand per event, the script drawing
  ids. It was incepted mid-session, at the align on q-0001.0007 that produced decision 56: the line was
  the interface while a hook was to read it from the reply, and no such hook ever shipped.
- [`.0012`](../tickets/done/01-0011.0100.0012-a-raised-question-is-looked-up-before-it-is-held.md):
  Q1's lookup before a question is opened.
- [`.0015`](../tickets/done/01-0011.0100.0015-a-question-that-keeps-coming-back-rises.md): strikes,
  the count on window lines and the wake's ranking.

**`.0010`**'s window and wake boxes closed on live evidence: a second session saw this one, and
the `debug=on` display was observed. Only Codex and Cursor live remain.

**The entry contract went from v18 to v21:**
- v19: the calls, and *write for a capable model* keeping out what a script already does
  ([rule failure 7](../rule-failures.md)'s strike).
- v20: the lookup.
- v21: the reply shows the question it landed on, not the call.

**Two fixes on the user's word:**
- The hook's unchanged window now names the turn's `at` call
  ([rule failure 16](../rule-failures.md), registered and landed).
- The marks' format moved to `MARKS-FORMAT.md` beside the maintain skill.

**A local rule, L5:** how Python runs here.

## What kept happening

- **Script behaviour written as instruction.** The 160-character cut went into the skill, and
  R7, Q4 and the *Marks* section each told the agent what a script does. The user's *what the
  hell is this for?* turned it into a meta-rule.
- **The every-turn placement lapsed** once the hook's line said nothing moved. The user noticed
  the `at` had disappeared from the replies.
- **Plans went stale against what landed first.** `.0012` and `.0015` each took a validation
  pass after `.0011`.
- **The user's redirections were the better designs:**
  - calls in place of a grammar;
  - a readable question, not a command line, as the display;
  - a queue-row check on the ticket that owns the queue rather than inline in `tickets.py`.

## Open questions

- **`.0010` is Done**, every box checked after this record was first written. Codex and Cursor
  each tested themselves live and recorded the result on
  [01-0010.0120](../tickets/01-0010.0120-what-each-host-says-without-being-asked.md).
  - **Codex** registers under its id and delivers the window.
  - **Cursor** did not register at first, and the box was ticked on an inference and reverted.
    Cursor's Hooks output channel then showed the cause: the hook ran, but read its input in the
    Windows code page. Read by its byte-order mark instead, a fresh chat registered under its own
    id, and its tag went out as `env`.
  - **The `env` does not reach Cursor's agent's shell.** `echo $env:QUESTIONS_SESSION` printed
    nothing, so the agent cannot see its hook's tag, and a Cursor chat holds two session lines.
    That is a known limit on `.0120`. Adopting the hook's line from a bare `--wake`, or
    registering nothing from Cursor's hook, are the alternatives left undecided.
  
  `.0010` was closed with its RFC at a `/maintain` the same night.
- **q-0001.0006, a resumed conversation under a new id.** Seen again: the old tag stayed `running` at
  a closed question. The time-gap strike does without session identity; the position still does
  not carry over.
- **`.0040`'s align** rests on *this harness has no wake hooks*, which decision 44 made untrue.
  That is new evidence for its committed-or-not question. It now also holds the queue's
  whole-rows task.
- **The other session's uncommitted work:** Q1's display as a one-cell table, touching
  `AGENTS.md`, the rules file, the skill, the findings record and the parent ticket. It is that
  session's to land.

## Continuation

- **Everything is committed and pushed** at this record's last write.
- **Next in the ring:** [`.0020` open-issues-are-entries-of-the-store](../tickets/done/01-0011.0100.0020-open-issues-are-entries-of-the-store.md),
  HITL, which opens at `/align`. Behind it is the coherence chain the queue orders.
