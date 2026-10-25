# Session 0074 — the store and the session, deferred

- **record of** what happened

2026-10-25 to 2026-10-26. Started by the session on
[q-0037.0006.0020.0001.0001](../questions/q-0037.0006.0020.0001.0001-does-an-install-keep-a-projects-claude-md-and-add-one-import-line-rather-than.md)
to align with the user on how to cut
[q-0037.0006.0024.0003](../questions/q-0037.0006.0024.0003-can-the-store-run-without-the-session-mechanism-the-session-sitting-on-the-store.md),
the store running without the session, and to carry the cut through the ring. The user had
already taken the direction: the session sits on the store, and the store imports nothing of it.
The question was decided as far as its direction and deferred; no ticket was minted, and no code
moved.

## Decisions

All three are in the question's `## Decisions` and in
[session.md, Delivery](../../.agents/mechanisms/session/session.md), inside the straw dog bound to
the question.

1. **One package for now, the dependency to be inverted inside** (the user, 2026-10-26). The user
   corrected the frame the session had carried: the store can be installed without the session,
   the session never without the store, and the three are not to be offered apart yet, because *a
   store without the session and maintain may drift*; the inversion is wanted *for correctness*.
2. **Each mechanism's hook in its turn** (the user, 2026-10-26). Weighed against a list of
   listeners the store calls, and against the session taking over the store's entry points
   (`hook.sh` and Q1 calling `sessions.py`). The session had recommended the listener list, first
   as one seam shared with
   [q-0037.0006.0024.0001](../questions/q-0037.0006.0024.0001-how-does-an-installed-method-put-its-own-records-into-the-path-and-the-counters-so.md);
   that argument fell when the user's word on the unit of work (q-0037.0006.0024.0002 decision 6,
   a local rule, not a call) left the seam one user. The user: *each hook in turn sounds the most
   right* — the listener list was still a call from the store, hidden.
3. **The cut deferred** (the user, 2026-10-26): *оставим это на будущее, пока оставим все как
   есть, все равно же устанавливаем пакет целиком*. Closed `deferred` until the store is to be
   installed without the session.

## What went wrong

- **The session lost the user for six turns over where a chat's position lives.** It offered
  three shapes in three replies — a note of the store's, the session placing through its own
  `at`, the session asking the store — each said as settled. The user's questions (*where a chat
  stands is the session's, isn't it?*; *why does the session ask the store who stands where?*)
  were each right against the shape just offered. It taught: when the person does not follow,
  draw the one picture of who does what before and after, and do not offer a new shape until the
  last one is accepted or refused.
- **The builder judged nothing, at the end.** Asked *is this right?*, the session handed the shape
  to a fresh agent with the code and no conclusion. The judge found four breaks the session had
  not seen — the store needs a chat's identity for its own window memory, two hooks' JSON answers
  cannot be concatenated, renames would leave rows on dead ids, rules cannot override one another
  — and a shape with fewer parts. It is kept in the question's body, under *For the cut, when it
  comes due*.

## Principles without a home

- **A shape the person has not followed is not proposed again in other words; it is drawn as one
  table of who does what, before and after.** Named here; no rule holds it.

## Also done

- The reading in the question's body re-checked against the code: it held; its two disagreeing
  records had been repaired in `a118773`; it had weighed too lightly that the hook's entry and
  `at` are the store's.
- [q-0037.0006.0020.0001.0006.0001](../questions/q-0037.0006.0020.0001.0006.0001-does-a-project-under-node-need-python-for-core-or-do-its-scripts-run-on.md)
  opened: the user asked what JavaScript copies of core's scripts beside the Python would cost. A
  proposed answer to objection 20 of the run-4 meeting. The session's estimate: the port is once,
  the double is every change after, and the tests, calling Python in-process, would not test a
  copy; it recommended weighing one runtime against a Python the install fetches itself, after
  seeing which runtime the recipients have. Left open on the user's word.
- Told: the session on q-0037.0017.0005.0002 that nothing in the scripts moves; the session on
  q-0037.0006.0024.0001 of the seam and then of the deferral; the session on
  q-0037.0006.0020.0001.0006 of the new child question.

## Open questions touched

- [q-0037.0006.0024.0003](../questions/q-0037.0006.0024.0003-can-the-store-run-without-the-session-mechanism-the-session-sitting-on-the-store.md)
  — closed deferred; due when the store is to be installed without the session.
- [q-0037.0006.0020.0001.0006.0001](../questions/q-0037.0006.0020.0001.0006.0001-does-a-project-under-node-need-python-for-core-or-do-its-scripts-run-on.md)
  — open; waits on which runtime the recipients have.
- [q-0037.0006.0024.0002](../questions/q-0037.0006.0024.0002-does-every-rule-of-the-entry-file-belong-to-a-mechanism-so-that-an-install-adds-the.md)'s
  body still says q-0037.0006.0024.0003 is *in work*, and q-0037.0017.0005.0002's says the cut is
  *proposed*; both are the other sessions' to correct: the second was told, the first goes in this session's report to the session that started it.

## What continues

The first step on the Node question: read which runtime each recipient on this machine has —
the TypeScript tree of objection 20 among them — before the user chooses between one runtime and
a Python the install provides.
