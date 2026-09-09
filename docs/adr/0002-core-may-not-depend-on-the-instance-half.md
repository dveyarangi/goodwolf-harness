# Core may not depend on the instance half

A recipient replaces `docs/` whole, so anything under `.agents/` that references a file there
dangles on arrival. Core may name a path convention the harness imposes — `docs/tickets/`,
`docs/glossary.md` — but may not point at a document only one project has, and may not rely on one
for its instruction or for any separable part of its functioning. Two blocks are exempt: a
`<straw-dog>`, which is bound to a ticket and expires, and a `<project-local>`, which is the part a
recipient replaces.

Landed in [AGENTS.md](../../AGENTS.md) on 2026-09-07 — and, being one of the four sections the entry
contract's version record does not cover, with no version entry of its own.

## Considered options

**Core carrying its own documents, so it depends on nothing replaceable.** This is the shape the
glossary took: [01-0011.0010](../tickets/done/01-0011.0010-mechanism-declared.md) split
`.agents/glossary.md` from `docs/glossary.md` because that slice added a core term, and a new core
term landing in the half that gets replaced would have committed the defect while describing it.
It works for a vocabulary. It was not generalised, because a travelling counterpart is not always
available or wanted — a mechanism's evidence cites this project's own records and could not travel
if it tried.

## Consequences

The general case is open and is **not settled here**: what core may lean on at all — a travelling
counterpart, a local block, or an accepted limit stated out loud — is
[01-0017](../tickets/01-0017-io-graph-coherent.md)'s align to weigh. This ADR records the rule and
its two exemptions, not the answer to that question. Live instances of the tension exist:
`/verify` links `docs/process.md` three times outside any block, and a mechanism doc's `not yet`
rows link tickets under `docs/` because the format requires a markdown link.
