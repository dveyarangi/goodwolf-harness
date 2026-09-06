# The delivery ring except /maintain

**Date:** 2026-09-06
**Historical handoff:** current state belongs to the [delivery queue](../tickets/README.md) and the owning tickets. This record is a snapshot of the fourth session, in Cursor.

## Work completed

Installed the implementation mechanism ([01-0010.0050](../tickets/01-0010.0050-install-implement.md)): `/implement`, `/tdd` with its five files, and `/improve-comments`. First use of `/implement` was that install. `/verify` on 0050 and on [01-0010.0040](../tickets/done/01-0010.0040-install-plan.md). Both tickets Done; records stay in `docs/tickets/` until 0070. `/maintain` was not installed. An `/align` on 0070 was opened and then stopped at the user's request; 0070 is Ready again. No commit or push in the working session; this record is written at conclude.

## Settled decisions and their owners

- 0050 installs the implementation mechanism, not `/implement` alone → [01-0010.0050](../tickets/01-0010.0050-install-implement.md) and the parent.
- `/verify` is the verification of landed work; the check set is linked from [Verification](../process.md#verification), not inlined → parent and [01-0010.0060](../tickets/01-0010.0060-install-verify.md).
- A skill carries `<project-local>` only when it has a project-specific fact → parent. `/plan`'s RFC dropped a restated local block on `/verify` of 0040 → [01-0010.0040](../tickets/done/01-0010.0040-install-plan.md).
- Ticket not Done until `/verify`; paired `done/` close waits on `/maintain` → TICKET-FORMAT and [01-0010.0070](../tickets/done/01-0010.0070-install-maintain.md).

## Open, with owners

- How denoise and sync-arch compose into `/maintain`, and what the first live close covers → [01-0010.0070](../tickets/done/01-0010.0070-install-maintain.md). Align was not finished this session.
- `/sync-arch` still named in `align/EDGE-FORMAT.md` (pre-existing `/edge` shelf) → 0070 or `/edge`.
- Remaining selected corpus, `/edge` → parent. The pacer → [01-0020](../tickets/01-0020-pacer.md).

## Session through the advise questions

**Great:** treating 0050 as the mechanism (`/implement` + `/tdd` + `/improve-comments`) so `/plan`'s `/tdd` cites resolve in the same slice. **Good enough:** `/verify` on 0040 after 0050, with RFC repairs rather than reopening composition. **Questionable:** starting 0070's `/align` and then abandoning it in the same session. **Missing:** `/maintain`, so Done tickets still sit in the active folders. **Redundant:** none new. **Out of balance:** the delivery ring is installed except the close that would archive it. **Hidden edges:** a whole-tree grep for `/sync-arch` is not a 0050 defect. **Easier:** a session that starts on 0070 with composition still open. **Next:** [01-0010.0070](../tickets/done/01-0010.0070-install-maintain.md), `/align` first.

## Housekeeping

None.
