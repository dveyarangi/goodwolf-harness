# Every skill and document has named producers and consumers

- **Status:** Planned (the first mechanism precedes)
- **Type:** HITL
- **Depends on:** [The shape is checked mechanically](./01-0011.0050-shape-checked.md) (a proven
  shape and a working check, so applying it to the rest is application rather than design)
- **Outcome:** Every mechanism in this tree is declared to the shape paired close proved, every
  installed skill is named by one or allowlisted with its reason, and the documents four skills
  transact against either exist with an owner or stop being referenced.

## Parent

[A mechanism has one home for its rules, and a derived index](../spec/01-0011-mechanism-shape.md).

**Re-parented 2026-09-06.** This was minted earlier the same day as a fifth rule refactor, before
the mechanism spec existed. Its questions — who produces a thing, who consumes it, what verifies it
— are the ones a mechanism doc answers about its own parts, so this is the spec's generalisation
step rather than a sibling of the rule refactors. It is not `Done (split)`: nothing was split, and
the work survives whole. What changed is its vocabulary and its place in the order.

## Impact

**2026-09-06, at minting.** Touches all eleven `SKILL.md` files — none of which declares a source or
target today — plus `docs/README.md`, the three `align/*-FORMAT.md` shelves that name documents, and
`AGENTS.md` if the convention is Tier 1. Verdict: **proceed, narrowed** — exclude `/edge`, and make
the check mechanical rather than prose.

**2026-09-06, on the mechanism split.** Re-assessed as part of
[that breakdown](../spec/01-0011-mechanism-shape.md#impact--2026-09-06). The declaration this ticket
wanted is a mechanism doc; the composing rule is the shape check; the enforcement is
`/mechanism`'s. What remains here is applying both to the tree once one mechanism has proved them.

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

- Every remaining mechanism in this tree declared to the shape
  [paired close](./01-0011.0010-mechanism-declared.md) proved: its parts named with their owners,
  its three property states stated, each absence carrying its kind and, where it is a gap, a ticket.
- Every installed skill named by a mechanism or placed in the allowlist with its reason. Eleven are
  installed; the allowlist rows are as much the deliverable as the declarations, because a skill
  nothing knows about is where an injected rule goes to hide.
- Documents brought into the mechanisms that own them. A document no mechanism writes or reads is a
  finding, not a fact to record — `docs/pacer.md` and two of the three `docs/research/*-findings.md`
  are named by no skill file today.
- Dispositions for `docs/concerns.md` and `docs/adr/`: created with an owning mechanism, or their
  references removed from `/align`, `/plan`, `/ticket` and `/maintain`. The check surfaces these on
  its first run over a tree that declares more than one mechanism.

## Decisions this ticket's align owns

- Where the mechanism boundaries actually fall. The delivery ring, the entry contract, the autonomy
  switches and the verification set are all candidates, and drawing them wrong produces a register
  that groups subjects while missing the action that spans them.
- Whether tickets, RFCs and session records are parts of a mechanism or only records it accumulates.
  They have writers and readers, but their lifecycle is archival.
- Whether `docs/concerns.md` and `docs/adr/` are created or their references removed. Four skills
  assume the first; nothing in this project has ever needed it.

## Acceptance criteria

- [ ] Every mechanism this tree has is declared, with its parts, owners and three property states.
- [ ] Every installed skill is named by a mechanism or allowlisted with a written reason; none is
  silent.
- [ ] Every durable document is named by the mechanism that writes it and by the ones that read it,
  or is listed with its reason.
- [ ] `docs/concerns.md` and `docs/adr/` each have a disposition, and no skill references an
  artifact without one.
- [ ] The shape check runs over the whole tree and its output is clean or every finding has an
  owner.
- [ ] `/verify` has been run on this ticket against its ticket, RFC, and governing docs.

## Out of scope

`/edge` and `docs/edge/` — [01-0010.0100](./01-0010.0100-remaining-named-corpus.md) owns the Edge
half, down to whether `/maintain`'s Edge-record check has records to check. What each skill *owns*
is [01-0016](./01-0016-responsibility-coherent.md)'s; this is what each mechanism is made of.
Whether a rule *arrives* at its occasion is [01-0018](./01-0018-reachability-coherent.md)'s.
Building the shape and proving it on one mechanism is
[01-0011](../spec/01-0011-mechanism-shape.md)'s children; this applies what they proved.
Relocating `docs/architecture.md`'s script contracts, which moves for a different reason.

## Parent scope addressed

The spec's generalisation step: stories 13, 14, 21, 22, and the second mechanism that proves the
shape holds beyond the one it was built on.
