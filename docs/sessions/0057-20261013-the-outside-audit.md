# The outside audit

- **record of** what happened

Session `local_44ec47e0`, 2026-10-13. Opened on a second outside audit of the whole project, pasted
by the user (*ещё один аудит*); kept as
[external-audit-2026-10-13](../research/external-audit-2026-10-13.md) and turned into
[01-0035 the-harness-never-loses-the-persons-work](../tickets/done/01-0035-the-harness-never-loses-the-persons-work.md),
minted, planned, built, verified and closed in the same session with its four slices. Two more
repairs fell out: the README brought in line with the installer, and a test that had never been
able to pass on Windows.

## Decisions and what chose them

- **Keep the audit, and give its defects homes as tickets** *(the user: "сохраняй аудит, и делай
  тикеты")*. The agent checked the audit's claims at `ac5401d` before proposing anything: E3 (a move
  losing an intervening edit) and the unlocked sessions file held; the README's install promise was
  false; `--check` exiting 1 no longer held. The weightier finding was its own: the 2026-09-30
  audit's E1, E2, E3 had no ticket and no question anywhere — a second pass whose findings had no
  path to work. The split — one parent, four slices — went through `/impact`, which turned the
  sessions slice HITL: the audit proposed a lock, and the architecture says the harness locks
  nothing *(the user, 2026-10-11)*.
- **01-0035 before 01-0040, slices from `.0010`** *(the user: "поехали", then "и продолжай")*.
  The agent recommended the data-loss fixes first as small, verifiable and cheap, then freezing
  the contract and running q-0038.0001's experiment, as the audit itself advised. The freeze and the
  experiment were not decided; only the order of 01-0035.
- **The sessions slice: a file per session** *(the user: "(a), в подпапке")*, over re-read,
  compare and retry, which would only narrow the race. Landed in
  [q-0036.0004](../questions/done/q-0036.0004-how-do-session-lines-written-at-once-all-survive-when-the-harness-locks-nothing.md).
  Then the correction that turned the build: the agent had put the folder at the old file's own
  path, `docs/questions/sessions`, and was engineering a rename-based carry-over with retries and a
  give-back of a folder taken by mistake, still failing a race. The user: *в общей подпапке для
  всех сессий, дубина.* Named apart as `docs/questions/sessions.d/`, the carry-over became copies
  that never overwrite, and every race left with the rename. Rule failure 42; `/plan` amended.

## What was done

- **[01-0035.0010](../tickets/done/01-0035.0010-a-moved-record-keeps-an-edit-made-while-it-moved.md)**
  — a move re-checks its source against what it read, as the citation repair already did (E3).
- **[01-0035.0020](../tickets/done/01-0035.0020-an-install-that-will-refuse-writes-nothing.md)**
  — the installer rehearses the injection over a scratch tree of the rules files and their targets
  before its first write, using the injector itself rather than a second reading of the grammar;
  a second `--install` over core names `--update --overwrite` (E2).
- **[01-0035.0030](../tickets/done/01-0035.0030-an-update-never-replaces-a-file-the-project-owns.md)**
  — an update refuses a path its new ref adds where the project holds its own file (E1, found still
  open while planning, not in the user's list).
- **[01-0035.0040](../tickets/done/01-0035.0040-session-lines-written-at-once-all-survive.md)**
  — `sessions.d/`, one file per session; this tree carried itself over on its first write (103
  sessions). On Windows the old writer did not only lose lines: simultaneous starts raised
  `PermissionError`.
- **README**: an existing `CLAUDE.md` stops the install rather than being moved aside; counts at 57
  sessions and 41 misses.
- **The ownership refusal's test** replaced `os.environ` with a dict, which never reaches a child
  Git; it could not pass on this machine. Fixed under `repair=report`, separately committed.

## What went wrong, and what it taught

- **A cost the plan wrote down was engineered around** — rule failure 42. The RFC's *Hidden edges*
  named the shared path as forcing a rename; the agent built the rename. Taught: a complication a
  choice of name or place brings reopens the choice.
- **A test that pinned the defect.** `test_an_injector_refusal_is_unfinished_and_names_the_resume`
  asserted the write-then-refuse behaviour E2 named; it was rewritten to the contract (*every
  refusal writes nothing*) rather than kept green.
- **A docs commit landed with the shape check red** (the questions skill named the new folder
  before the painted door did); repaired in the next commit.

## Open questions touched

- [q-0037.0015](../questions/q-0037.0015-how-is-produced-work-gone-over-again-over-what-scope-by-what-criteria-by-whom-and-to-what.md)
  — the evidence that an outside pass's findings need a path into the work; open.
- [q-0037.0009.0011.0001](../questions/q-0037.0009.0011.0001-how-does-core-code-name-the-architecture-rule-it-follows-when-core-may-not-cite-a.md)
  — opened: `/implement`'s pointer rule against *Core and instance*.
- [q-0038.0001](../questions/q-0038.0001-does-working-under-the-harness-deliver-software-better-than-working-without-it-measured-on-the.md)
  — the audit's main point and next step; not taken up.
- The audit's other findings have no home yet: the injection's unbounded growth (the wake listing
  every ended session), the path-encoded id and its renames, *struck* counting visits, the reply
  format's per-session cost, near-dead skills and the shipped tests' weight, the vocabulary.

## What continues

The queue's next is [01-0040](../tickets/01-0040-a-projects-account-stays-in-agreement-with-its-work.md),
its first slice `.0010` Ready, waiting on a nod. Before it, the user may want the audit's unhomed
findings and its advice — freeze the contract, run q-0038.0001 — put to an align.
