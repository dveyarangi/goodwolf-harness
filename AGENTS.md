# Entry contract

Entry contract: v16, 2026-09-21.

Open your first reply of every session with the `Entry contract:` line above, verbatim.

<straw-dog until="01-0020 is done" ticket="docs/tickets/01-0020-pacer.md">
Run /recall first in every session, whatever the first message says.
</straw-dog>

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

- Clarity and simplicity first — Occam's razor: take the shape with the fewest parts that does the job, and remove before you add.

<straw-dog until="01-0018 declares the mechanism that owns tiering" ticket="docs/tickets/01-0018-reachability-coherent.md">
- A skill's description is its tier-1 surface: name there every occasion the skill serves, with the context that makes it fire, and nothing else. Write every rule at the tier its occasion reads, and no higher: what sits at tier 1 is paid for by every session.
</straw-dog>

<installed by="ticket">
**P9** Name a ticket by a link to its record; one that has no record yet, by a slug and its state word.
</installed>

## Core and instance

`docs/` is substituted whole in a harness instance: a recipient project replaces its contents with
its own.

What core may not do is **depend** on it. Nothing under `.agents/` may reference a file in `docs/`,
or rely on one for its instruction or for any separable part of its own functioning. A core file
may name a path under `docs/` only when that path is a record a mechanism declares — the directory
that holds a kind of record, or a file that is one — never a particular record inside such a
directory: `docs/tickets/` and `docs/glossary.md` are painted doors; one particular ticket inside
`docs/tickets/` is a document only this project has. Content inside the
[local block](#project-local) is the instance's, not core's. A `<straw-dog>` exempts
nothing: its wrapper is stripped on install and whatever it wrapped ships. Core names a ticket
only in a straw dog's binding — never in a link, never as a bare id in prose — since a recipient
can resolve neither.

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

The project sets each switch in its local block, under *Project-local*; skills defer to those values.

| Switch | Meaning |
|---|---|
| commit | `ask`: commit only on explicit permission, per change. `auto`: commit when the work is verified. |
| push | `ask`: separate from commit, per push. `never`, `auto`. |
| next-cycle | `ask`: starting the next ticket after one lands needs a nod. `auto`. |
| breakdown | `ask`: a /ticket split needs approval before minting. `auto`. |
| repair | `report`: a clear violation of an explicit rule inside authorized work is fixed and reported. `ask`: show it first. |

`repair=report` holds only when all four are true: the governing rule is explicit, and cited; the
repair restores compliance inside the authorized work and keeps every other agreed contract; the
affected behaviour is understood well enough to say so; the result is verifiable against the
rule. Otherwise `/align`. *(the user, 2026-09-05)*

## Project-local

<installed by="mechanism-shape">
**R7** A project's own answers and overrides are authored in one file beside the entry file,
`local.rules.md`, in the rules-file format, and reach a file only as the local block — the
installed block whose owner is `local` — which the installer writes after every mechanism's block
there, so the project's answer is what a reader meets after core's rule. An override names the rule it
overrides. A local change to a rule is written in the local file, never into a skill or the entry
file: `inject_rules.py --check` fails on a block that differs from its source and on a block
nothing owns, and the repair is the local file, re-installed. The local block is the project's,
not core's, and a redeploy preserves it.
</installed>

<installed by="local">
**L1** This repository develops the shared dev harness using its own loop; its own architecture and
progress live in docs/ like any other project's — the instance half doing its job, not a leak.
Terms: docs/glossary.md, this project's own; the method's are .agents/glossary.md's. What each
version of the entry contract changed: docs/research/entry-contract-findings.md.

**L2** commit=ask · push=ask · next-cycle=ask · breakdown=ask · repair=report
</installed>

## Straw dogs

Wrap anything a live ticket will change, as you write it — or, for text already written, in the
pass that mints the ticket or decides that it will change it:
`<straw-dog until="condition" ticket="path">`, or in code a `TODO` naming the ticket. Treat *not
yet*, *until*, *once it exists*, *for now*, *untested* in your own text as the same signal: find
the ticket, or mint one. Wrap at the authored home, never where the harness installs or derives it.
Make the condition testable and the ticket path repository-relative. Write the body to stand on
its own: it is what a recipient receives once the wrapper is stripped, so it reads whole without
the condition and names no ticket — the binding does. Leave what no ticket would change
unwrapped.

Follow a straw dog like any other rule until its condition is visibly met; then act on reality,
report the stale block, and do not treat the contradiction as a violation.
