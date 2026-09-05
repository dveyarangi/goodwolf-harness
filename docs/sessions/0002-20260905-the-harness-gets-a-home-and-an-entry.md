# The harness gets a home and an entry

**Date:** 2026-09-05
**Historical handoff:** current state belongs to the [delivery queue](../tickets/README.md) and the owning tickets. This record is a snapshot of the second session, which followed the inception session on the same day.

## Work completed

Reviewed what the inception session had landed and reconciled it with the earlier skills comparison; the second audit superseded the first and the first is marked so. Created `D:\Dev\AI\agents` as a git repository and moved the whole working tree into it, the July corpus kept under `legacy/skills` as evidence and the Aug 31 loop sketch brought in from Downloads. Installed `align` with its format shelf and `impact` from Meteoscape with the accepted deltas, under the recipient layout `.agents/skills` with tracked `.claude/skills` and `.cursor/skills` symlinks, which needed Windows Developer Mode to become real links rather than junctions. Minted the first delivery slice, [01-0010.0020](../tickets/01-0010.0020-live-alignment-across-hosts.md), and ran the first `/align` in this repository on its entry contract, which produced `AGENTS.md` and the one-line `CLAUDE.md`. Two commits, `1867375` and `7e80b2d`; the split announce line and the subagent observation are staged after the second.

## Settled decisions and their owners

- The harness lives at `D:\Dev\AI\agents`, a git repository; installed corpus at `.agents/skills`, July corpus under `legacy/skills` → [child ticket, root decision](../tickets/01-0010.0020-live-alignment-across-hosts.md#decisions-this-tickets-align-owns).
- One root `AGENTS.md` owns the entry contract; `CLAUDE.md` is `@AGENTS.md`; no Cursor rule file → same section.
- The entry file is core plus `<project-local>` like a skill; switch values are local, so nothing local overrides core → same section.
- The loop is two rings joined at `/align`: wake with `/recall` → `/align` → `/conclude`, and `/ticket` → `/plan` → `/implement` → `/verify` → `/maintain` → `/ticket`. `/spec` and `/impact` are called from inside the rings, not stages → [AGENTS.md](../../AGENTS.md#the-loop).
- Autonomy switches `commit`, `push`, `next-cycle`, `breakdown`, `repair`, with this project's values in the local block → [AGENTS.md](../../AGENTS.md#autonomy).
- `<temporary until="condition">` marks expiring statements anywhere; followed until visibly met, then reported as stale; `/maintain` removes → [AGENTS.md](../../AGENTS.md#temporary-statements).
- Delivery evidence is the versioned announce line opened by every session's first reply → child ticket, evidence decision.
- `/spec` and `/verify` are the names for to-spec and review-impl → [parent ticket, selection table](../tickets/01-0010-dev-harness-shared-and-local.md#bootstrap-corpus-selection).
- Five core changes are owed to later installs: impact recommends a shape, commit reads the switches, skill-up documents the tag, maintain enumerates it, ticket and plan call impact → [parent ticket](../tickets/01-0010-dev-harness-shared-and-local.md#core-changes-owed-by-later-installs).

## Open, with owners

- Session-start delivery in Claude Code is unobserved; the import route is proven by a subagent → child ticket, host observations. The bundled CLI is not logged in, so the headless probe could not run; a new desktop session in this folder is the cheaper trial.
- Codex and Cursor discovery and delivery are untested; the `codex` on PATH is a May 2025 build that predates `AGENTS.md`, so the real Codex host must be the one tried → child ticket.
- Whether the loader links are needed at all: Cursor documents reading `.agents/skills` directly, Claude Code may too → child ticket, known gaps.
- `align/EDGE-FORMAT.md` cites a ticket format not installed until `/ticket` lands → child ticket, known gaps.
- Local overrides of core remain deferred; the switch design avoided the question rather than answering it → parent ticket.

## Session through the advise questions

**Great:** the two-ring loop, once read off the sketch instead of flattened, and the `<temporary>` tag, which came from the user noticing that half the local block described state that expires. **Good enough:** the entry file at v1; it will change when `/ticket` and `/recall` land. **Questionable:** `repair` as a switch survived on the argument that it is a trust level, not a permission gate; its `ask` position has never been used. **Missing:** any observed session start, in any host. **Redundant:** the first skills comparison, now marked superseded; the second audit should be the only one cited. **Out of balance:** two sessions of design against zero sessions of the loop actually running on a product ticket. **Hidden edges:** the shell used for automation had no symlink privilege even with Developer Mode on, because it inherits an older token; installer code must create links through the OS call, not by shelling out. Perl replacement strings ate backslashes in Windows paths once; mechanical edits need a check step. **Easier:** a logged-in CLI, so probes do not need a human click. **Next:** observe one session start, record it, then install `/ticket`.

## Housekeeping

`D:\Dev\AI\.agents` is an empty folder the session could not delete because its own shell sat in it; remove it by hand.
