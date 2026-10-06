# Session 26 — a reviewer reads the switches, and the rules leave memory

**2026-09-27.** Woke with `/recall` on nothing in flight. Turned into a tool trial, a roadmap, an
outside review's fixes, and the user moving the rules I kept in private memory into the harness.

## What happened

**A diagram tool, tried and dropped.** The user asked to run
[tt-a1i/archify](https://github.com/tt-a1i/archify), an agent skill that renders checked HTML
diagrams, on this repository. Its own suite on Windows: 1397 tests, 32 failing — symlink privilege
and Windows assumptions in its tests, not its renderer. Its architecture map of the harness
validated cleanly and was, in the user's word, useless: it redrew three files' prose, and the
harness's substance — rules, invariants, the loop — is not boxes and arrows. Nothing of it is kept.

**Core stopped naming recipient trees.** The harness mechanism's grading paragraph and two test
comments named frost_map and ai-game-1, which a recipient cannot resolve. Removed *(the user: just
remove it)*.

**A roadmap.** Published as a private page: the 23 closed tickets on a timeline, where the work
stands, the 30 open ones by track. The tracks are my grouping; it is a snapshot.

**The outside review's second pass.** An agent installed the harness into a fresh tree and traced
which skill reads each switch. Checked against the tree, nearly every finding held. Fixed and
pushed the same day — the list and where the rest went are on
[the parent](../tickets/01-0010-dev-harness-shared-and-local.md#outside-review-second-pass--2026-09-27):
`/commit` contradicted `commit=auto`; an unset switch now reads `ask`; `--update` reported every
file written; two tests passed only on Windows or as a plain user; the front page claimed an
arrival flow nothing performs. Entry contract **v17**.

**Decided** *(the user)*: the harness is personal memory; team memory is the next step after the
scheduled work, undiscussed and unminted (team-memory, unminted).

**Rules out of memory.** Fixing four skill descriptions, I added their method and named other
skills. The user: *only usecase* in a description, and no skill names in skills unless injected —
[rule failure 13](../rule-failures.md). The first rule tightened the tiering rule. The second
became the mechanism shape's **R8**, reshaped twice before it held: it is about the skill *named*,
not the one naming, and only an installed mechanism's skill is off limits; one still on its way to
a mechanism may be named. Then the user ruled that critical rules cannot live in the agent's
memory, which does not migrate: *write for a capable model* went to the entry file, *problem before
machinery* to `/align`, *land the amendment in the same pass* to Self-improvement, and the
installer rule was already R5. Only the edit-tools preference stays in memory.

## What the passes kept finding

- **Fixing past my own change.** A description fix spread into `/implement`'s body and
  `/conclude`'s whole description, which predated me, and `/celebrate` gained occasions it never
  had. The user: *only fix your latest changes, not what was there before*.
- **Adding what the rule said to leave out.** The tiering rule ended *and nothing else*; *with the
  context that makes it fire* read as licence for method.
- **A rule applied to the wrong side.** R9 forbade naming *from* a skill on its way to a mechanism;
  the user meant the skill being named.
- **Running the tests when asked to run the tool.** *Run everything* meant the tool on our repo;
  seven minutes of its suite went first.

## Open questions

- **R8's drift.** Eight skills name `/ticket` or `/maintain` outside installed blocks. Listed on
  [01-0016 responsibility-coherent](../tickets/01-0016-responsibility-coherent.md), whose outcome
  now reads R8's way.
- **`/dream`'s lost rule.** Leaving tier 1 took *a dream never amends rules* with it, and the skill's
  own addition was reverted. Parked by the user; it has no home but this record.
- **Rule failure 13 is not replayed**, by the method on
  [01-0019 harness-amends-itself-by-explicit-meta-rules](../tickets/01-0019-harness-amends-itself-by-explicit-meta-rules.md).
- **The two POSIX test fixes have not run on Linux.** Left to
  [01-0011.0090 a-test-catches-what-its-name-promises](../tickets/01-0011.0090-a-test-catches-what-its-name-promises.md),
  which now asks for a Linux run and CI.
- **What the memory is for, and what it may cost** — on
  [01-0010.0168 the-harness-measures-what-it-costs-and-saves](../tickets/01-0010.0168-the-harness-measures-what-it-costs-and-saves.md)'s align.
- **The queue's order** — whether
  [01-0010.0172 a-first-install-says-what-stopped-it](../tickets/done/01-0010.0172-a-first-install-says-what-stopped-it.md)
  goes ahead of the releases chain — still undecided; the delivery status leads with `.0185`.

## Continuation

- **Next in the ring:** `01-0011.0090`, Ready and AFK, or `.0172`, Ready and opening with its align on
  `arrived`. `next-cycle=ask`.
- **The next session announces v17.**
- **Everything through `7f238b1` is pushed.** This record is not yet committed.
- **The Completed step** in the queue is still a changelog; unrepaired.
