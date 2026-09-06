# Session entry

Entry contract: v3, 2026-09-06.

Open your first reply of every session with the line above, verbatim.

<project-local>
This repository develops the shared dev harness using its own loop. The queue,
docs/tickets/README.md, owns current state and says where to resume. Decisions live in the owning
ticket under docs/tickets/. Detailed rules: docs/process.md. Terms: docs/glossary.md.
What each version of this contract changed: docs/research/entry-contract-findings.md.
</project-local>

## General rules

A **shape** is whatever is under consideration, held between an idea and a thing: formed enough
to have a context and a structure, not yet exhausted by any one realization. Being a shape says
nothing about being load-bearing — an implementation method is a shape too. → [glossary](docs/glossary.md).

- Do not generalize from one shape. Preserve a seam. Generalize only when a second materially different shape forces the same concept.
- Explore shape context - what is the shape one of? what are its relationships? does its scope overlap any other shape?
- Explore shape structure - how this shape is/can be built? does expanding its structure change the contract or even what the shape is?

- Recency for evidence, longevity for principles.

## Core and instance

`docs/` is substituted whole in a harness instance: a recipient project replaces its contents with
its own. This repository develops the harness using itself, so its own architecture and progress
live in `docs/` like any other project's — that is the instance half doing its job, not a leak.

What core may not do is **depend** on it. Nothing under `.agents/` may reference a file in `docs/`,
or rely on one for its instruction or for any separable part of its own functioning. Naming a path
convention the harness imposes — `docs/tickets/`, `docs/glossary.md` — is not a reference to a
file; pointing at a document only this project has is. A `<temporary>` block is exempt: it is bound
to a ticket and expires.

Where a reference is genuinely unavoidable — a mechanism's evidence sidecar is the case that forces
it, since a sidecar cites this project's own records — it goes inside a `<project-local>` block.
That block is the part a recipient replaces, so the reference does not travel.

## Document load-bearing, code&comment the rest

Core docs and ADRs are the home for:
- Constitution — identity semantics, consistency model, source-of-truth rules
- Structure — service boundaries, data ownership, event/data flows, extension seams
- Load-bearing — see the definition below

<temporary until="01-0012 is done" ticket="docs/tickets/01-0012-hierarchy-coherent.md">
Bad architectural documentation:
- Forecasts are stored in MongoDB collection forecast_hourly.

Better:
- Historical forecast issues must remain independently addressable by (location, valid_time, issue_time) because validation compares what was known at different issue times.
</temporary>

## What makes a thing "load-bearing"

- A decision or invariant whose violation would cause multiple parts of the system to become wrong, not merely require local refactoring.
- A thing is load-bearing when several of these are true: has high blast radius, crosses boundaries (i.e. services, persistence, APIs, ownership), other decisions depend on it, it protects an invariant,
is expensive to reverse, holds non-obvious rationale, long-standing.

- Counter-test: if it can be changed locally without understanding the rest of the architecture, it is not load-bearing.

## The loop

Two rings, joined at /align.

    session:   wake with /recall → /align → /conclude → (next session)
    delivery:  /ticket → /plan → /implement → /verify → /maintain → /ticket

/align opens the delivery ring and is where it returns whenever a decision is needed:
/spec for load-bearing shapes, /plan when the governing docs contradict, /verify when a finding needs one, /maintain when maintenance surfaces one. /ticket⇄/plan and /implement⇄/verify iterate as pairs.

Human checkpoints: every decision at /align; spec accepted; breakdown approved; commit; push;
next cycle at /maintain → /ticket.

Do not reopen an accepted decision without new evidence.

### Helpers

- /impact determines the scope and load-bearingness of the shape. Use it to evaluate work volume and its ticketing shape (spec for load-bearing work, tickets for mechanical), work units slicing or whether a shape deserves further investigation due to hidden complexity.
- /discover to investigate hidden complexity, by detecting what else the shape is.
- /dream is an experimental second "lobe" of the harness, aiming to reassess load-bearingness. It is optional, runs after /conclude, and writes dreams that /maintain and /align may pick up; it never amends rules.

## Autonomy

The project sets each switch in its local block below; skills defer to those values.

| Switch | Meaning |
|---|---|
| commit | `ask`: commit only on explicit permission, per change. `auto`: commit when the work is verified. |
| push | `ask`: separate from commit, per push. `never`, `auto`. |
| next-cycle | `ask`: starting the next ticket after one lands needs a nod. `auto`. |
| breakdown | `ask`: a /ticket split needs approval before minting. `auto`. |
| repair | `report`: a clear violation of an explicit rule inside authorized work is fixed and reported. `ask`: show it first. |

## Temporary statements

A statement that expires or temporary placeholders is wrapped in `<temporary until="condition" ticket="path">`, anywhere: in
a local block, a skill body, a doc. The condition is testable: the ticket is done, or the condition
is fulfilled.

The ticket is the one whose work meets the condition, as a path from the
repository root. Follow the block like any other rule until you can see the condition is met; then act on reality, report the stale block, and do not treat the contradiction as a violation.

<project-local>
commit=ask · push=ask · next-cycle=ask · breakdown=ask · repair=report

Installed: /align, /impact, /discover, /ticket, /spec, /plan, /implement, /tdd,
/improve-comments, /verify, /maintain, /advise, /celebrate, /commit, /skill-up, /dream. Named
above but not installed here: /recall, /conclude, /edge.
</project-local>
