# `.agents/` is runtime, `docs/` is construction

The harness is developed in the same tree it ships from, so every asset has to be sorted into what a
recipient receives and what stays behind. We split it by **when the asset is read**: `.agents/` holds
what an agent reads while doing work — skills, rules files, mechanism docs, the method's glossary,
the scripts — and travels; `docs/` holds what is read while *building* the harness — architecture,
tickets, RFCs, evidence, sessions — and is replaced whole by a recipient. A recipient needs the
harness's output, not the record of its construction.

**Amended 2026-11-16** *(the user, decision 1 of [q-dsxyi5](../questions/q-dsxyi5-where-does-a-recipient-declare-its-own-mechanisms.md))*: what travels is
core — under `.agents/`, everything but the mechanisms a tree declares `local`, which are the
project's own and stay where they were made, with their skills and their parts.

## Considered options

**A core architecture document, `.agents/architecture.md`, travelling with the scripts it describes.**
Rejected. The argument for it was that a script without its failure contract is unusable on arrival,
which sounds right and is not: the *operational* half already travels inside the skill that runs the
script — `/maintain`'s **D4** tells a maintainer what to do when a mechanical repair stops partway —
while `docs/architecture.md#interruption-and-recovery` holds the design rationale behind that rule,
which a recipient never needs to operate it. `/maintain` already encodes this correctly, by keeping
its pointer to that section inside a `<project-local>` block.

**Splitting by subject rather than by reading occasion** — script contracts to core, project progress
to `docs/`. Rejected: the seam is unstable. "The paired-close contract" and "how far this project has
got with paired close" are the same sentence often enough that the file re-mixes itself, which is how
`docs/architecture.md` came to hold both.

## Consequences

**The development process is core, not a document.** The loop and its steps are read while doing the
work, so they belong in the mechanisms and rules under `.agents/` — the harness's process happening
also to be its own self-development process changes nothing about where it lives.
The process is now held by [the entry file's Autonomy section](../../AGENTS.md#autonomy) and
[the ticket format](../../.agents/skills/ticket/TICKET-FORMAT.md); `docs/process.md` (removed 2026-11-22, eadd0b64)
held it with several chunks with no home yet, a straw dog bound to [q-p4mcme](../questions/q-p4mcme-how-does-each-turn-know-its-next-step-and-each-session-where-to-resume.md), and what survives it is the
*architecture* of the process, in `docs/architecture.md`, not the process itself.

For this repository the two halves collide: its product *is* the method, so `docs/architecture.md` is
the method's own architecture. That is the instance half doing its job, not a leak — but it means a
load-bearing decision here can look like core content and be written into `.agents/` by mistake. This
ADR exists because that mistake was made twice in one session, on 2026-09-09, and refuted by hand
both times.
