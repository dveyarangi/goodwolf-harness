# The loop runs a lap, and finds the mechanism that was never specified

**Date:** 2026-09-06
**Historical handoff:** current state belongs to the [delivery queue](../tickets/README.md) and the owning tickets. This record is a snapshot of the sixth session, in Claude Code. `/conclude` is not installed; this was written by hand at the user's request.

## Work completed

Closed [01-0010.0070](../tickets/done/01-0010.0070-install-maintain.md) on its last criterion — a fresh session listing `/maintain` the way it lists `/spec`, which this session could observe and the implementing one could not. The delivery ring is now installed end to end and has run a full lap on itself.

Ran the full ring on [01-0010.0090](../tickets/done/01-0010.0090-install-discover.md): `/align` dissolved both of its questions rather than answering them, `/verify` made four repairs, `/maintain` closed it. `/discover` stops being experimental, files no artifact, and is used the way `/impact` is; its filing apparatus — stored raw returns, a register of declines, a retirement test — is gone from the body, which now ends in a shaped output block.

Cleared the archive backlog: five tickets and three RFCs moved in one invocation, citations repaired across thirteen files. Fixed the enumerator's silent-empty-scan (`--help` reported a clean scan of nothing and exited 0). Verification set 68 → 72.

Wrote and accepted [the mechanism spec](../spec/01-0011-mechanism-shape.md), decomposed into five slices that now run before the rule refactors. Ten commits, `86d63ad` through `c6fc281`.

## Settled decisions and their owners

- Rules live in **three homes**, not two: `AGENTS.md` for meta/strict, the skill for *use*, the mechanism doc for *mechanics* → [the spec](../spec/01-0011-mechanism-shape.md). This supersedes the two-way split taken earlier the same session, which had nowhere to put how a thing works.
- A mechanism has three independent properties — **delivered, indexed, singly authored** — and a gap in any is declared with a ticket rather than left absent → [the spec](../spec/01-0011-mechanism-shape.md), first proved on [01-0011.0010](../tickets/done/01-0011.0010-mechanism-declared.md).
- **Injection** is adopted, proven on paired close first: one rule home, mechanically installed and removable, a hand-edited copy is drift → [01-0011.0020](../tickets/01-0011.0020-rules-one-home.md).
- The queue is a **derived index**, not a transcription → [01-0011.0040](../tickets/01-0011.0040-queue-derived-index.md). The word is *index*; Life's glossary reserves *digest*.
- Mechanism docs live at `.agents/mechanisms/<slug>/`, so they travel with the unit recipient projects actually receive → [the spec](../spec/01-0011-mechanism-shape.md).
- **Archiving is not scope-limited.** A finished record in the active folder is a fact about the folder, not a judgment about work the pass did not examine → [`/maintain`](../../.agents/skills/maintain/SKILL.md).
- `/discover` is installed because the user installed it; the audited source selection records what was taken from three estates and is not the roster of what is installed → [01-0010.0090](../tickets/done/01-0010.0090-install-discover.md).
- `/mechanism` runs **before** the four rule refactors, because injection dissolves the question that stalled [01-0016](../tickets/01-0016-responsibility-coherent.md).

## Open, with owners

- Whether the queue's rendered table is committed. The spec's reasoning came from a tree with wake hooks this harness lacks, while [AGENTS.md](../../AGENTS.md) routes every session to the queue → [01-0011.0040](../tickets/01-0011.0040-queue-derived-index.md).
- Nothing sweeps for archive eligibility. `/maintain` says archiving is tree-wide; the five were found by hand → [01-0011.0030](../tickets/01-0011.0030-archive-backlog-listed.md).
- `docs/concerns.md` and `docs/adr/` do not exist while four skills transact against them → [01-0017](../tickets/01-0017-io-graph-coherent.md).
- Two mechanisms keep their evidence records in different places; the process says each has one without saying where it lives → [01-0016](../tickets/01-0016-responsibility-coherent.md).
- 66% of `docs/process.md` is rules belonging to a skill or a mechanism. Paired close's share leaves in [01-0011.0020](../tickets/01-0011.0020-rules-one-home.md); the rest waits for its own mechanisms and for [01-0020](../tickets/01-0020-pacer.md).

## Session through the advise questions

**Great:** the natural experiment nobody designed — temporary statements and paired close are both duplicated, so duplication was not what killed the second one, and the two differences that remained gave the spec its three properties from this repo's own evidence rather than from Life's structure. **Good enough:** `/impact` returning *narrow* on my own draft split and changing four things in it, including the one slice that had no check. **Questionable:** I twice cited `docs/process.md` at the user as governing authority minutes after agreeing it could not govern a distributed skill — and the second time quoted the half that was not even `/maintain`'s rule. **Missing:** a real review of the Life tree before proposing a shape; the first pass read about a fifth of one skill, and the user had to send me back. What came back changed the vocabulary (*index*, not *digest*), added a third home, and reframed a ticket minted that morning. **Redundant:** the queue-row verbatim check I reported as a quality signal all day exists only because the data is duplicated; a derived index makes both the check and the drift impossible. **Out of balance:** five tickets sat finished and unarchived through three `/maintain` passes that each correctly declined to touch them. **Hidden edges:** a duty can be correctly written, unambiguous and still unreachable — the archive rule was never scope-limited, only its reachable phrasing made it look that way. And an index without a delivery path is worse than a copy. **Easier:** a session that starts with the mechanism shape already declared, so a new rule has somewhere to go. **Next:** [01-0011.0010](../tickets/done/01-0011.0010-mechanism-declared.md), which needs a nod under `next-cycle=ask`.

## Housekeeping

The queue stopped restating the entry contract version, a fact `AGENTS.md` owns and which was wrong from the commit that copied it. Two queue rows had paraphrased outcomes against `TICKET-FORMAT`'s verbatim rule; repaired, and the row check later gained a `Type` comparison that immediately caught two more. `/maintain`'s Identify rule named `AGENT.md`, which does not exist here. `/discover`'s `EVIDENCE.md` referred to another estate's store, a sibling agent's handle and its classification table as though they were local; each now names the estate, with every recorded fact intact. `01-0017` was re-parented to the mechanism spec rather than closed `Done (split)` — nothing was split, and its work survives whole.
