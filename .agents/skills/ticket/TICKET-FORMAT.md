# Ticket format

This shelf owns ticket naming, delivery-state vocabulary, the shape of a
ticket, and how to amend the queue table in `docs/tickets/README.md`.
[The development process](../../../docs/process.md#naming) points here.
What an RFC *contains* is `/plan`'s.

## Numbering

```
docs/tickets/done/01-0010.0010-life-informs-dev-harness.md
              │  │    └── slug — what the ticket is. Never changes. Cite by this.
              │  └─────── position — global. Changes when priority changes.
              └────────── release — the contract the ticket serves.
```

- Names are `01-NNNN-slug.md`. Positions step by 10. Insert by splitting the
  difference: `0015`, then `0012`. Positions stay four digits — longer numbers
  break numeric ordering. When the gap is exhausted, take the nearest free
  slot on the correct side and note the placement in the queue row. Never
  renumber anything else.
- Allocate a position where the ticket will actually be worked, not merely at
  the end, checking both `docs/tickets/` and `docs/tickets/done/` for the
  surrounding positions.
- A child appends a four-digit position: `01-0010.0010`. Depth is unbounded
  and means "is a child of", nothing else — work merely filed after `0010`
  takes `0020`.
- A release closes when its contract's criteria are met, not on a date. A
  later release's ticket may land first.
- Maintenance is a `Kind`, never a filename prefix.
- Completed tickets keep their number.

### One basename per work item

A ticket and its RFC share a basename. Cite by slug through a relative link;
add the `done/` segment when the target completes. The filename never
changes, only the folder.

When every acceptance box is checked, including `/verify`, move the ticket to
`docs/tickets/done/` and its RFC to `docs/rfc/done/`, and repair the
citations that pointed at them. A paired close (ticket + RFC) is one pass.
There is no mover script yet; do the move and the citation repair together
by hand. `/maintain` implements that mover.

Artifacts predating this keep their names.

## Status

`Done` · `In progress` · `Ready` · `Partial` · `Planned` · `Blocked`

- **Ready** — dependencies complete, work can start. **Planned** —
  dependencies are not.
- **Partial** — some behavior landed; criteria remain open.
- **Blocked** — stuck for a reason *other than* an incomplete dependency.
  Waiting on a dependency is `Planned`.
- One parenthetical qualifier is allowed: `Planned (own align precedes)`,
  `Done (split)`. `Done` carries its date.

## The ticket

```md
# {Title}

- **Status:** {value} {(qualifier)}
- **Type:** HITL | AFK
- **Kind:** Maintenance
- **Plan:** [{title} RFC](../rfc/{basename}.md) — what it selected
- **Depends on:** [{title}](./RR-NNNN-slug.md) ({what it supplies})
- **Blocks:** [{title}](./RR-NNNN-slug.md) — {why}
- **Outcome:** {the delivered change, one or two sentences}

## Parent
## {Why this exists}          ← 0..n, titled for the claim each argues
## What to build
## Decisions this ticket's align owns
## Acceptance criteria
## Out of scope
## Parent scope addressed
```

Always present: `Status`, `Outcome`, `What to build`, `Acceptance criteria`.
The rest appear when they have something to say. Header fields keep this
order; `Outcome` is always last.

| Field | Rule |
|---|---|
| `Status` | A [status](#status) value. |
| `Type` | `HITL` needs a human decision or review; `AFK` merges unattended. |
| `Kind` | `Maintenance` when the work delivers no product capability. Absent otherwise. |
| `Plan` | The RFC link plus one clause on what it selected. Absent until a plan exists. |
| `Depends on` | Blockers, each with a parenthetical naming what it supplies — not a bare link. |
| `Blocks` | Only when the blocking relation is itself an argument; carries its `— why`. |
| `Outcome` | Observable behavior, never code shape. Copied verbatim into the queue table. |

One-off fields (`Trigger`, `Related`, `Owning decision`) are fine when the
ticket carries that fact. Older tickets use `Legacy id:` / `RFC:` /
`Parent PRD` / `User stories addressed`; leave them, don't write them.

| Section | Rule |
|---|---|
| `Title` | Names the outcome, not the mechanism. No number, no release. |
| `Parent` | The PRD or coarse ticket this was carved from; otherwise the durable doc owning the context (architecture section, roadmap phase, concern). Never a session. A subticket says which slice it is and what the parent keeps. |
| Narrative | Titled for what it argues. Diagram the mechanism; link the evidence. Say what is deliberately *not* a defect. Omit entirely when the framing is uncontested. |
| `What to build` | End-to-end behavior, not a file-by-file plan. Each constraint carries its reason. |
| `Decisions this ticket's align owns` | One bullet per open question, each saying why it cannot be answered yet. After the align it becomes `What this ticket does not decide`, resolved entries struck and answered inline. |
| `Acceptance criteria` | Checkboxes, each observably true when done. |
| `Out of scope` | What a reader expects and won't find, each with its actual home. |
| `Parent scope addressed` | The parent's stories or criteria this closes, by number. |

### Acceptance criteria

- Behavior altitude, always: types, fields, formulas and module layout are
  the RFC's.
- Name the instrument when the naive check would pass for the wrong reason.
- Refactor tickets: behavior unchanged, the new constraint machine-enforced
  by a failing guard test, dependents unblocked.
- A parent split into subtickets states the end-state that holds only when
  all children land.
- Provisional criteria say so in the heading, and are firmed in place at the
  align.
- Check a box only for work that satisfied it; a criterion satisfied early is
  checked with a date.
- Every ticket includes a `/verify` criterion. A ticket is not Done until
  `/verify` has been run against it. Do not move to `done/` without it.

### Conventions

- Cite by slug through a relative link; add the `done/` segment when the
  target completes.
- Reference the architecture, ADRs, glossary, concerns and edge records;
  never restate them.
- Strike superseded text, answer inline in bold, keep the question.
- Date anything that changed after minting.
- Update the queue in the same pass.
- Wrap at ~100 columns.

## The queue

The queue is `docs/tickets/README.md`. `/ticket` amends **the table** in the
same pass as minting, a status flip, or a completion. Pacing prose around
the table (`Completed step`, `Current pass`, `Current stage`, working-document
pointers) is not the table; leave it in place, do not restate it here, and
do not replace it with another skeleton.

```md
| Ticket | Status | Type | Outcome |
|---|---|---|---|
| [Title](./RR-NNNN-slug.md) | Ready | HITL | {verbatim from the ticket header} |
```

| Field | Rule |
|---|---|
| `Last updated` | The date **delivery state** last moved, not the date the file was last touched. A copy-edit or a link repair does not advance it; a status flip, a minted ticket, or a reorder does. |
| `Ticket` | Relative link to the ticket. Add the `done/` segment when it completes. The row stays. |
| `Status` | A [status](#status) value, including an allowed qualifier. |
| `Type` | `HITL` or `AFK`. |
| `Outcome` | Copied verbatim from the ticket header. |

When minting, add a row where the ticket will actually be worked. When
status, type, or outcome changes, update the row. When completing, set
status to `Done (date)` and add `done/` to the link. Do not add columns.
