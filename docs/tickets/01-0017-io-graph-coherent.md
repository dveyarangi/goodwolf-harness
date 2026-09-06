# Every skill and document has named producers and consumers

- **Status:** Planned (responsibility precedes)
- **Type:** HITL
- **Depends on:** [Each skill owns its own responsibility](./01-0016-responsibility-coherent.md)
  (settled ownership, so a declaration says who writes a thing rather than who happens to touch it)
- **Blocks:** [Rules reach the occasion they are for](./01-0018-reachability-coherent.md) — arrival
  cannot be checked until the consumers are named
- **Outcome:** Every installed skill declares what it reads and what it produces, every harness
  document names its writers and readers, a rule requires those declarations to compose, and
  `/maintain` checks that they still do.

## Parent

[AGENTS.md](../../AGENTS.md). Sibling of [01-0012](./01-0012-hierarchy-coherent.md),
[01-0014](./01-0014-scope-coherent.md), [01-0016](./01-0016-responsibility-coherent.md) and
[01-0018](./01-0018-reachability-coherent.md), inserted as the fifth rule refactor.

## Impact

**2026-09-06.** Assessed before minting. Touches all eleven `SKILL.md` files — none of which
declares a source or target today, their frontmatter carrying only `name` and `description` — plus
`docs/README.md`, the three `align/*-FORMAT.md` shelves that name documents, and `AGENTS.md` if the
convention is Tier 1. Verdict: **proceed, narrowed** — exclude `/edge`, and make the graph check
mechanical rather than prose. The narrowing is recorded in `Out of scope` below; the two
shapes that forced the concept are in `Why this exists`.

## Why this exists

Two failures of the same kind, in opposite directions, neither caught by anything:

**A duty whose worklist nothing produces.** "When every acceptance box is checked, move the ticket
to `done/`" is written only in `/ticket`'s files — [SKILL.md](../../.agents/skills/ticket/SKILL.md)
and [TICKET-FORMAT.md](../../.agents/skills/ticket/TICKET-FORMAT.md) — while
[the process](../process.md#tree-maintenance) assigns archive operations to `/maintain`, whose body
carries only the gate form. On 2026-09-06 five tickets were eligible and unarchived
(`01-0010.0020`, `.0030`, `.0035`, `.0050`, `.0060`), three with unarchived RFCs. No skill's
declared output is "the records that should have moved", so the backlog was invisible rather than
ignored.

**A declared producer that has never produced.** [`/align`](../../.agents/skills/align/SKILL.md)
says open questions and risks live in `docs/concerns.md`, *this skill's artifact*. That file does
not exist and never has. `/plan` reads it, `/ticket` writes concern promotions into it, `/maintain`
sweeps it as the concern index. Four skills transact against an absent document, one of them
claiming to own it, across every `/align` this project has run. `docs/adr/` is the same story from
`/plan` and `ARCH-FORMAT.md`.

The two are materially different — a missing producer versus an absent artifact with a named owner
— and force the same concept, which is what [the entry file](../../AGENTS.md) requires before
generalising from one shape.

The other direction is unwatched too: `docs/pacer.md` and two of the three
`docs/research/*-findings.md` are named by no skill file at all.

## What to build

- A source and target declaration for each installed skill: what it reads to do its work, and what
  it produces. Not a file list — the artifacts it is responsible for, in the vocabulary the graph
  is checked in.
- A writer and reader declaration for each harness document. A document with no writer or no reader
  is a finding, not a fact to record.
- **A rule that the declarations must compose**, placed by the tier it belongs to: a skill declaring
  a source nothing produces is a defect, and so is a document nobody writes or reads. This is the
  enforcing rule the ticket exists to add, not a description of good practice.
- **`/maintain` instructed to check it**, in the skill's own body, so the check survives
  distribution to a project that has neither `docs/process.md` nor `docs/architecture.md`.
- The check itself, mechanical where it can be —
  [mechanical maintenance](../process.md#mechanical-maintenance) makes a missing script work to do,
  not a reason to leave the repair outstanding. A declaration nothing sweeps decays the way the
  archive duty did.
- Dispositions for `docs/concerns.md` and `docs/adr/`, which the check surfaces on its first run:
  created and owned, or their references removed.

## Decisions this ticket's align owns

- Where the declarations live: skill frontmatter, a section in each body, or one derived index. Only
  the first two travel with a distributed skill.
- Which tier the composition rule sits at. It governs every skill, which argues `AGENTS.md`; it is
  checked by one, which argues `/maintain`. Those give different answers about who owns it.
- What a "document" is for this graph — whether tickets, RFCs and session records participate, or
  only durable documents. They have writers and readers too, but their lifecycle is archival.
- Whether `docs/concerns.md` and `docs/adr/` are created or their references removed. Four skills
  assume the first; nothing in this project has ever needed it.

## Acceptance criteria

- [ ] Every installed skill declares its source and its target, in a place that travels with the
  skill to a project that has no `docs/process.md` or `docs/architecture.md`.
- [ ] Every harness document names its writers and its readers.
- [ ] A rule states that the declarations must compose, and names what a violation is.
- [ ] `/maintain`'s own body instructs it to check the graph; the instruction does not depend on a
  project-local document.
- [ ] The check runs mechanically and reports: a declared source nothing produces, a document with
  no writer, a document with no reader.
- [ ] `docs/concerns.md` and `docs/adr/` each have a disposition, and no skill references an
  artifact without one.
- [ ] The check is run once and its output is clean or its findings have owners.
- [ ] `/verify` has been run on this ticket against its ticket, RFC, and governing docs.

## Out of scope

`/edge` and `docs/edge/` — [01-0010.0100](./01-0010.0100-remaining-named-corpus.md) owns the Edge
half, down to whether `/maintain`'s Edge-record check has records to check. What each skill *owns*
is [01-0016](./01-0016-responsibility-coherent.md)'s; this is what each skill reads and writes.
Whether a rule *arrives* at its occasion is [01-0018](./01-0018-reachability-coherent.md)'s.
Relocating `docs/architecture.md`'s script contracts, which moves for a different reason.

## Parent scope addressed

The entry file's rule that a shape's context and relationships are explored rather than assumed,
applied to the harness's own artifacts.
