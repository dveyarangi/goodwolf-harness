# /maintain lands, and the rules get tickets

**Date:** 2026-09-06
**Historical handoff:** current state belongs to the [delivery queue](../tickets/README.md) and the owning tickets. This record is a snapshot of the fifth session, in Claude Code. `/conclude` is not installed; this was written by hand at the user's request.

## Work completed

Committed the 0070 planning round (`0f1dc93`), then implemented it. `/maintain` is installed at `.agents/skills/maintain/SKILL.md`, composed from the selected `denoise` and `sync-arch` plus the owed `<temporary>` enumerator, with mechanical support under `.agents/scripts/` — `move_doc.py`, `temporary_statements.py` and the shared `docs_corpus.py`, standard library only. 68 behavioral tests under `tests/`, built through `/tdd` as vertical slices; the project's [verification set](../process.md#verification) is no longer empty.

First live use closed the [01-0010.0040](../tickets/done/01-0010.0040-install-plan.md) pair into `done/`, repairing citations in six records including a historical session. `/verify` on 0070 made three repairs. Seven tickets minted through `/ticket` → `/impact`. Entry contract bumped to v3. Nothing committed after `0f1dc93`.

## Settled decisions and their owners

- A **shape** sits between an idea and a thing, and being one says nothing about being load-bearing → [glossary](../glossary.md), Tier 1 line in [AGENTS.md](../../AGENTS.md), coherence owned by [01-0012](../tickets/01-0012-hierarchy-coherent.md).
- **Hierarchy** is from what heights we look at things; it and **scope** each get a consolidation ticket, and **responsibility** and **reachability** are two more → [01-0012](../tickets/01-0012-hierarchy-coherent.md), [01-0014](../tickets/01-0014-scope-coherent.md), [01-0016](../tickets/01-0016-responsibility-coherent.md), [01-0018](../tickets/01-0018-reachability-coherent.md). The four refactors run before [the pacer](../tickets/01-0020-pacer.md).
- Repair-and-report **moves inside the skill**; the consequence for three calling skills is 01-0016's → [01-0016](../tickets/01-0016-responsibility-coherent.md).
- Decomposing during an `/align` runs `/ticket` → `/impact` and presents a suggestion without minting → landed in [`/align`](../../.agents/skills/align/SKILL.md).
- `/discover` is not experimental here; `/impact` is pass 1 and reads the corpus, `/discover` is pass 2 and must not → [the skill](../../.agents/skills/discover/SKILL.md), standing owned by [01-0010.0090](../tickets/01-0010.0090-install-discover.md).
- Maintenance owns correct transformations and failure reporting; per-file writing technique is implementation's, with Git as the recovery fallback → [architecture](../architecture.md#interruption-and-recovery).

## Open, with owners

- Fresh-session discovery of `/maintain`, the only unchecked criterion on [01-0010.0070](../tickets/01-0010.0070-install-maintain.md).
- `docs/glossary.md`'s pacer link resolves nowhere → [01-0020](../tickets/01-0020-pacer.md).
- `/dream`'s standing, and whether an uninstalled skill belongs in the entry file → [the parent](../tickets/01-0010-dev-harness-shared-and-local.md#adoption-shortlist--recommendations-awaiting-alignment).
- `/verify`'s body lost a line that [the process](../process.md#verification) still carries → [01-0016](../tickets/01-0016-responsibility-coherent.md).
- `/maintain`'s Edge-record and concern-index checks name documents this project does not have → [01-0010.0100](../tickets/01-0010.0100-remaining-named-corpus.md).
- Everything after `0f1dc93` is uncommitted.

## Session through the advise questions

**Great:** the mover's first live close did exactly what the ticket predicted it would exercise — mutual links, outgoing links, and incoming references from the queue, three tickets, the catalog and a historical session — and the session record's recorded facts survived the repair untouched. **Good enough:** `/verify` catching three real gaps in work I had just written, including a preflight that would have crashed mid-run rather than refusing. **Questionable:** producing a ticket-shaped breakdown inside an `/align` without running `/ticket` → `/impact`, then presenting it for approval; the user caught it and it became the evidence for splitting reachability from responsibility. **Missing:** a mechanism for this record — `/conclude` is still not installed, so the fifth and largest session was nearly the first with no snapshot. **Redundant:** two definitions of load-bearing, in the entry file and the glossary, neither pointing at the other. **Out of balance:** four rule refactors queued because the rules outgrew their homes while nobody was maintaining them. **Hidden edges:** correct ownership does not produce arrival — the `/ticket` → `/impact` rule was unambiguous, correctly placed, and still did not reach an agent standing inside `/align`. **Easier:** a session that starts with `/impact` already returning a work shape. **Next:** [01-0010.0080](../tickets/01-0010.0080-impact-work-shape.md), then [01-0012](../tickets/01-0012-hierarchy-coherent.md).

## Housekeeping

`docs/architecture.md` still claimed `/maintain` was not installed; repaired. The `<temporary>` block in `docs/process.md` was rebound from `until="/pacer is installed"` to `until="01-0020 is done"`, the old condition having presumed a skill 01-0020 may not create. The entry file's bad/better example is now wrapped in a `<temporary>` block bound to [01-0012](../tickets/01-0012-hierarchy-coherent.md), making "keep it for now" testable. [Entry contract evidence](../research/entry-contract-findings.md) created, holding the v1–v3 deltas.
