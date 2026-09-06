# /ticket is installed

**Date:** 2026-09-06
**Historical handoff:** current state belongs to the [delivery queue](../tickets/README.md) and the owning tickets. This record is a snapshot of the third session, in Cursor.

## Work completed

Opened in Cursor; the entry contract arrived at v2. Confirmed `/align` and `/impact` in the catalog, then aligned and installed `/ticket` from Meteoscape's `to-tickets` plus Forecast Collector's split impact, with TICKET-FORMAT adapted to this repo's table and naming. Repaired the EDGE-FORMAT cite, removed the `AGENTS.md` temporary, pointed `docs/process.md#naming` at the format. `/impact` on that install was recorded on [01-0010.0020](../tickets/done/01-0010.0020-live-alignment-across-hosts.md). Catalog listing of `/ticket` observed in this Cursor session.

## Settled decisions and their owners

- `/ticket` amends the existing queue table (`Ticket | Status | Type | Outcome`, plus `Last updated`); TICKET-FORMAT records that amendment. Meteoscape's richer queue skeleton is not imported. `/maintain` does not own the current table → [01-0010.0030](../tickets/done/01-0010.0030-install-ticket.md).
- `breakdown=ask`: run `/impact` on the draft before asking; that approval is what gets minted. Ask again only if a later impact would change membership, granularity, or dependencies → same ticket.
- Claude Code, Codex and Cursor discover the installed `/align` and `/impact` → [01-0010.0020](../tickets/done/01-0010.0020-live-alignment-across-hosts.md).

## Open, with owners

- One real slice minted through `/ticket`, with `/impact` on the split and breakdown approved → [01-0010.0030](../tickets/done/01-0010.0030-install-ticket.md).
- Natural-language route to `/align` (a request to discuss an unresolved harness decision without naming the skill) → [01-0010.0020](../tickets/done/01-0010.0020-live-alignment-across-hosts.md).
- `/impact` does not yet recommend spec / ticket / RFC / re-slice → parent, core change owed with `/impact`.
- Remaining bootstrap (spec/plan/implement/verify/maintain and the rest of the selected corpus), `/edge` → parent. The pacer → [01-0020](../tickets/01-0020-pacer.md).

## Session through the advise questions

**Great:** keeping the queue table we already have, and putting `/impact` before the breakdown approval so `ask` has a single object. **Good enough:** `/ticket` installed without waiting on `/impact`'s missing shape recommendation. **Questionable:** 0030's catalog criterion named Claude Code; the evidence taken was Cursor via `.claude/skills`. **Missing:** the first mint, which is what would exercise the skill rather than only listing it. **Redundant:** none new. **Out of balance:** the delivery ring now names `/ticket` and the skill exists, but it has not yet minted a slice. **Hidden edges:** this chat's injected catalog was captured at session start (align and impact only); live listing after install is a different fact, verified through the loader path. **Easier:** a session that starts after the install, so the injected catalog includes `/ticket`. **Next:** first `/ticket` pass on the parent's remaining bootstrap.

## Housekeeping

None.
