# Core may not depend on the instance half

A recipient replaces `docs/` whole, so anything under `.agents/` that references a file there
dangles on arrival. Core may name a painted door — `docs/tickets/`,
`docs/glossary.md` — but may not point at a document only one project has, and may not rely on one
for its instruction or for any separable part of its functioning. Content inside a
`<project-local>` block is the recipient's, not core's — and the same holds for the
`<installed by="local">` block that [01-0010.0110](../tickets/01-0010.0110-project-facets-injected.md)
replaces it with. A `<straw-dog>` exempts nothing.

**Amended 2026-09-20** *(the user, at [01-0010.0140](../tickets/done/01-0010.0140-core-stands-alone.md)'s
align)*: until then this ADR and the entry file exempted a `<straw-dog>` on the grounds that it is
bound to a ticket and expires. It expires only here. The install spec's shear strips the wrapper
and ships what it wrapped, so a `docs/` link inside a straw dog dangled in every recipient and was
refused at install — the exemption had moved the failure to the port, not removed it. Instance
ownership is the only exclusion, and it is read mechanically from the enclosing block.

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
its two exemptions, not the answer to that question. The live instances of the tension —
`/verify`'s three links to `docs/process.md`, and the `not yet` rows linking tickets because the
format required a link — ended on 2026-09-20 under
[01-0011.0050](../tickets/done/01-0011.0050-shape-checked.md) and
[01-0010.0140](../tickets/done/01-0010.0140-core-stands-alone.md); `mechanisms.py --check` now fails at
home on any new one.
