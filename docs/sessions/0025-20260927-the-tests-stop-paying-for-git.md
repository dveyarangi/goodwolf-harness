# Session 25 — the tests stop paying for Git

**2026-09-26 to 2026-09-27.** Opened on *what's next, is our queue in order*, and turned twice: into
a rule that failed in the very reply that answered it, and into a test suite that took five minutes.

## What happened

**The queue answer broke P9 while reviewing the queue.** The `/recall` reply named tickets by bare
ids and position-only links; the user asked whether a rule didn't require the slug. It did not quite —
P9 asked for a link, not for what the link shows. [Rule failure 12](../rule-failures.md) records it
and four replays; P9 now reads *the first time a record or a reply names a ticket, its link text
carries the slug* — repeats may be the id alone *(the user)*. The queue's own position-only links,
which the replays copied, were repaired; `.0150` and `.0170` went Ready on the way.

**How a rule amendment is tested** *(the user)*: not by asking a reader how it parses the rule, but by
a fresh session in this repository, under the new ruleset, given the failed request word for word and
told nothing of the issue; the registering session grades the reply. It is on
[01-0019](../tickets/01-0019-harness-amends-itself-by-explicit-meta-rules.md), not in memory, where I
first put it. The user installed the standalone `claude` CLI for it; a clean-room run is now possible
on this machine.

**The suite.** 342 tests took 274 s. Measured, process starts were nine tenths of every test, and
Git was the subject of about 23 of them. An audit read every test against the code it exercises; the
user's call was *prune first, then go*.
[01-0011.0080](../tickets/done/01-0011.0080-a-test-pays-only-for-what-it-proves.md) landed and
closed with its RFC: 8 tests that could not fail gone, 50 duplicates folded, a guard that fails any
unmarked test starting a process, plain folders, the harness's source held in memory. 289 tests,
**24.2 s**; production unchanged, graded on ai-game-1. The testing decision in both specs changed
*(the user)*: a test builds a real repository only when Git or a child process is what it proves.
[01-0011.0090](../tickets/01-0011.0090-a-test-catches-what-its-name-promises.md) holds the weak
tests and untested branches the audit found, Ready. A parallel runner was declined.

## What the passes kept finding

- **I answered the question I had, not the one asked.** *Why do the tests ask Git?* took five
  answers; the user wanted the reason in the code — one `git ls-files` in `corpus()`, inherited by
  every script from the first — not the mechanics or the docs.
- **Estimates went out as measurements.** 227 ms per Git call was PowerShell's overhead, not Git's;
  "four calls per test" was a guess the profile refuted at forty. The numbers that held were the ones
  measured the way the code runs.
- **Narrowing the user's instruction.** *Tell it not to read the docs* became one file; the process
  for testing a rule went to memory instead of its ticket.
- **Over-marking.** Whole classes marked real where one test in them was; each unmarking cut seconds.

## Open questions

- **`TICKET-FORMAT`'s `[Title](…)` against P9's slug-first link text** — the queue table and header
  links. Held on [rule failure 12](../rule-failures.md); the user's.
- **What a replay's tester is kept from** — all of `docs/` left `/recall` nothing to read; the
  register and diffs leaked through git status. On
  [01-0019](../tickets/01-0019-harness-amends-itself-by-explicit-meta-rules.md).
- **The queue's order**, recalled at the session's start: `.0172` ahead of the releases chain was
  recommended and never decided; the candidate paragraph still leads with `.0185`.
- **The clean-room requirement on `.0190`** can now be met with the `claude` CLI; nothing records that
  yet.
- **Why a Git process costs 75–200 ms here** — the machine's, most likely antivirus scanning; the
  user's to check.

## Continuation

- **Next in the ring:** [01-0011.0090](../tickets/01-0011.0090-a-test-catches-what-its-name-promises.md)
  is Ready and AFK; [01-0010.0172](../tickets/done/01-0010.0172-a-first-install-says-what-stopped-it.md)
  is Ready and starts with its align on `arrived`. `next-cycle=ask`.
- **Nothing is pushed** — this session's commits sit on `main`. `push=ask`.
- **The Completed step** in the queue is still a changelog; unrepaired.
