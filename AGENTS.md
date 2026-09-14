# Entry contract

Entry contract: v8, 2026-09-09.

Open your first reply of every session with the `Entry contract:` line above, verbatim.

<project-local>
This repository develops the shared dev harness using its own loop. Terms: docs/glossary.md, this
project's own; the method's are .agents/glossary.md's.
What each version of this contract changed: docs/research/entry-contract-findings.md.
</project-local>

## General rules

A **shape** is whatever is under consideration, held between an idea and a thing: formed enough
to have a context and a structure, not yet exhausted by any one realization. Being a shape says
nothing about being load-bearing — an implementation method is a shape too. → [glossary](.agents/glossary.md).

- Do not generalize from one shape. Preserve a seam. Generalize only when a second materially different shape forces the same concept.
- Explore shape context - what is the shape one of? what are its relationships? does its scope overlap any other shape?
- Explore shape structure - how this shape is/can be built? does expanding its structure change the contract or even what the shape is?

- Changing how the work is done — a skill, a check, a record, the loop — is mechanism work: use [/mechanism](.agents/skills/mechanism/SKILL.md). Building what the project produces is not.

- An `<installed>` block in a file is not that file's to edit. Change the rule in the rules file of the mechanism named on the block, and re-install.

- Recency for evidence, longevity for principles.

## Core and instance

`docs/` is substituted whole in a harness instance: a recipient project replaces its contents with
its own.

<project-local>
This repository's own architecture and progress live in docs/ like any other project's — the
instance half doing its job, not a leak.
</project-local>

What core may not do is **depend** on it. Nothing under `.agents/` may reference a file in `docs/`,
or rely on one for its instruction or for any separable part of its own functioning. Naming a path
convention the harness imposes — `docs/tickets/`, `docs/glossary.md` — is not a reference to a
file; pointing at a document only this project has is. Two blocks are exempt: a `<straw-dog>`,
bound to a ticket and expiring, and a [`<project-local>`](#project-local).

## Document load-bearing, code&comment the rest

A project's architecture, ADRs and glossary are the home for:
- Constitution — identity semantics, consistency model, source-of-truth rules
- Structure — service boundaries, data ownership, event/data flows, extension seams
- Load-bearing — see the definition below

A decision forms in its owning ticket and lands in one of these when it is ready. A decision about a
mechanism lands in that mechanism's doc, and what was refuted in its evidence.

<straw-dog until="01-0012 is done" ticket="docs/tickets/01-0012-hierarchy-coherent.md">
Bad architectural documentation:
- Forecasts are stored in MongoDB collection forecast_hourly.

Better:
- Historical forecast issues must remain independently addressable by (location, valid_time, issue_time) because validation compares what was known at different issue times.
</straw-dog>

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

## Self-improvement

<straw-dog until="01-0019 is done" ticket="docs/tickets/01-0019-harness-amends-itself-by-explicit-meta-rules.md">
- The rule was present and did not fire - usually means the rule was phrased wrong. This is a call for registration and rephrasing it - write rule failure to docs/rule-failures.md (or strike if exists) and suggests way to amend the rule to capture (use /mechanism and /skill-up for ideas)
- Keeping the register: an entry names the rules that were in play and proposes the amendment; a repeat strikes the entry it repeats rather than opening a second; an entry closes when its amendment lands, or is refused with its reason. Nothing here authorises deleting a rule.
</straw-dog>

## Autonomy

The project sets each switch in its local block below; skills defer to those values.

| Switch | Meaning |
|---|---|
| commit | `ask`: commit only on explicit permission, per change. `auto`: commit when the work is verified. |
| push | `ask`: separate from commit, per push. `never`, `auto`. |
| next-cycle | `ask`: starting the next ticket after one lands needs a nod. `auto`. |
| breakdown | `ask`: a /ticket split needs approval before minting. `auto`. |
| repair | `report`: a clear violation of an explicit rule inside authorized work is fixed and reported. `ask`: show it first. |

## Project-local

A recipient replaces every `<project-local>` block with its own → [glossary](.agents/glossary.md).

- Carry one only for a fact that would differ in another project. Harness layout and the switch
  lookup are shared.
- One block per local fact, beside the rule it answers.
- An unavoidable core reference into `docs/` goes in one, so it does not travel.

## Straw dogs

Wrap anything a live ticket will change, as you write it:
`<straw-dog until="condition" ticket="path">`, or in code a `TODO` naming the ticket. Treat *not
yet*, *until*, *once it exists*, *for now*, *untested* in your own text as the same signal: find
the ticket, or mint one. Wrap at the authored home, never where the harness installs or derives it.
Make the condition testable and the ticket path repository-relative. Leave what no ticket would
change unwrapped.

Follow a straw dog like any other rule until its condition is visibly met; then act on reality,
report the stale block, and do not treat the contradiction as a violation.

<project-local>
commit=ask · push=ask · next-cycle=ask · breakdown=ask · repair=report
</project-local>
