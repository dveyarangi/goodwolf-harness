# Entry contract evidence

Evidence and evolution record for the entry contract — the versioned instructions every host
supplies at session start, announced verbatim by the session's first reply. The contract itself is
[AGENTS.md](../../AGENTS.md); this record holds what changed at each version and why, so a session
announcing a version can find out what it announced.

The version covers the **core** part only: the announce line, the general rules, the loop, the
switch roster with its meanings, and the `<straw-dog>` convention — `<temporary>` until v5.
`<project-local>` values change without a bump.

## v1 — 2026-09-05

The first entry file. Announce line, the two-ring loop, the autonomy switch roster, and
`<temporary until="condition">` as an expiring statement followed until visibly met. Written in
[01-0010.0020](../tickets/done/01-0010.0020-live-alignment-across-hosts.md); the session that produced it
is [0002](../sessions/0002-20260905-the-harness-gets-a-home-and-an-entry.md).

## v2 — 2026-09-06

**One core change:** every `<temporary>` block also names the ticket whose work meets its condition,
as a path from the repository root; an unbound block is reported rather than followed silently.
Decided by the user, recorded in
[01-0010.0020](../tickets/done/01-0010.0020-live-alignment-across-hosts.md#what-this-ticket-does-not-decide).
The three blocks then live were bound the same day.

## v5 — 2026-09-08

**One core change, in two parts.** The `<temporary>` convention is renamed to `<straw-dog>`,
attributes unchanged, after the user named the concept: a thing made to serve until the real one
arrives and then be discarded. And the section that described the convention now instructs the
writer — wrap it when you write it, anywhere, and in code as a `TODO` naming the ticket — with one
line drawn against wrapping everything: what has no named successor is a claim. Decided by the
user at [01-0011.0070](../tickets/done/01-0011.0070-straw-dogs-marked-and-found.md)'s align; the
evidence was four unwrapped expiries the injector's verify found the day before.

## v4 — 2026-09-08

**One core change:** a general rule that an `<installed>` block in a file is not that file's to
edit — change the rule in the rules file of the mechanism named on the block, and re-install.
It replaces a rule the mechanism shape would otherwise have installed into two skills, and the
per-block notice Life's injector writes, with one sentence every session reads. Decided by the
user at [01-0011.0020](../tickets/done/01-0011.0020-rules-one-home.md)'s align.

## v3 — 2026-09-06

Several core changes, landed together after the user added a body of general rules and the agent
reviewed them. Deciding tickets vary by change and are named below.

- **General rules section added.** "Do not generalize from one shape" promoted from `/plan` and
  `/implement` to the entry file. Two shape-exploration dispositions added — what the shape is one
  of, and how it is built. "Recency for evidence, longevity for principles" added.
- **`shape` defined at Tier 1**, held between an idea and a thing, pointing at
  [the glossary](../glossary.md). Being a shape says nothing about being load-bearing — an
  implementation method is a shape too. → [01-0012](../tickets/01-0012-hierarchy-coherent.md).
- **"Document load-bearing, code&comment the rest"** added: constitution, structure and
  load-bearing decisions belong in core docs, with a bad/better example.
- **"What makes a thing load-bearing"** added: a multi-factor test and a counter-test.
  → [01-0012](../tickets/01-0012-hierarchy-coherent.md).
- **Loop line:** `/spec` named as a return path for load-bearing shapes. Helper descriptions moved
  into a `Helpers` subsection, and `/dream` moved there from the loop paragraph.
- **Temporary statements:** the condition reads "the ticket is done, or the condition is fulfilled".
  The sentences describing what `/maintain` does with the blocks — enumerate in scope, report
  unbound expiries, remove the ones whose condition holds — moved into
  [the skill](../../.agents/skills/maintain/SKILL.md), landed by
  [01-0010.0070](../tickets/done/01-0010.0070-install-maintain.md).
- **Installed list:** `/maintain` and `/discover` added; a line names what the file mentions but does
  not install — `/recall`, `/conclude`, `/dream`, `/edge`. `/discover`'s standing is
  [01-0010.0090](../tickets/done/01-0010.0090-install-discover.md)'s.

**Not a bump:** typo repairs, the counter-test's polarity fix, and the section heading change from
"'Load-bearing' quantified" to "What makes a thing load-bearing" — corrections to statements whose
intent did not change.

## Open about this mechanism

- Nothing checks that a session's announced version matches the file. The announce line is the
  contract's [delivery evidence](../glossary.md), and it is currently self-reported.
- Where this record belongs is provisional. It follows
  [one evidence record per mechanism](../../.agents/skills/mechanism/SKILL.md#three-homes-and-the-chain), but a version
  delta is closer to an operational record than to a lesson.
  [01-0016](../tickets/01-0016-responsibility-coherent.md) owns the placement.
