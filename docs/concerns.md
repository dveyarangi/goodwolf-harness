# Concerns

Unresolved pressure on this project's architecture — open questions and risks that have no
disposition yet. Not delivery sequencing, which is the [queue](tickets/README.md)'s, and not
decisions, which live in their owning ticket, ADR or architecture section.

Numbers are stable identifiers, not ranks. A settled concern moves out to the document that owns
its answer, leaving its number behind.

Created 2026-09-10, at the align that produced its first entry. Until then this file was named by
`/align`, `/edge`, `/ticket` and three format shelves and did not exist — a reference
[01-0017](tickets/01-0017-io-graph-coherent.md) holds as a defect, and this is half of its repair.

## 3. Whether harness self-amendment is its own mechanism

**Kind:** open classification, deliberately unresolved while evidence accumulates; no owner ·
**Refs:** [`AGENTS.md` — Self-improvement](../AGENTS.md#self-improvement),
[`/mechanism`](../.agents/skills/mechanism/SKILL.md), [`/skill-up`](../.agents/skills/skill-up/SKILL.md)

→ queued as [01-0019](tickets/01-0019-harness-amends-itself-by-explicit-meta-rules.md)

**Contact surface.** `/mechanism` holds self-amendment today and `/skill-up` is its neighbour;
whether the occasion (*a rule failed to fire*) and its register need a mechanism of their own is
answered from accumulated strikes rather than from argument. Deletion on repeated failure is
deliberately not adopted. The deliberation is on the ticket.

## 2. A group install target needs a denominator on both sides

**Kind:** design gap in a shape three mechanisms want; blocked, no owner ·
**Refs:** [01-0017.0010](tickets/01-0017.0010-terms-defined-before-they-land.md),
[01-0011.0050](tickets/done/01-0011.0050-shape-checked.md),
[architecture — installed blocks](architecture.md#installed-blocks)

*(the user, 2026-09-10)*

A rules file today names an explicit `target` file and an `anchor` line within it. Three mechanisms
now want to name a **group** instead — vocabulary into everything, a dev-method corpus into the
skills that carry practice, and `/maintain` wanting a *maintain yourself* line in every recording
mechanism. That clears the entry file's bar against generalising from one shape.

**The missing piece is that a group name alone is not an address.** "Install into the dev-method
group" says nothing about *where inside each member* the block lands. So group membership has to be
**declared from both ends**: the rules file names the group, and each member mechanism declares, in
its own instance, that belonging to this group means *this file and this anchor in me*. Without the
second half a group target cannot resolve to a write, and the installer's guarantee that a refusal
changes no file cannot hold.

**Membership is enumerable since 2026-09-20** — [01-0011.0050](tickets/done/01-0011.0050-shape-checked.md)
landed: `mechanisms.py --check` reports every installed skill as named by a mechanism or
claiming `not yet` on its own first line, three named of twenty-two. A group over mechanisms
still reaches those three; the transition state is now counted rather than guessed.

Kept out of [01-0017.0010](tickets/01-0017.0010-terms-defined-before-they-land.md) deliberately: it
is broader than the glossary, and the glossary ships on explicit targets without it.

## 1. The rule set could be composite, with no pure core anywhere

**Kind:** structural alternative, raised as more interesting than the design being built; no driver,
no owner · **Refs:** [01-0017.0020](tickets/01-0017.0020-practice-swaps-in-one-edit.md),
[01-0018](tickets/01-0018-reachability-coherent.md),
[ADR-0001](adr/0001-agents-is-runtime-docs-is-construction.md)

*(the user, 2026-09-10, at the dev-method align)*

The shape currently being built assumes a mechanism owns a body of text and injects rules from it
into the skills that need them. Core is a thing that exists, and mechanisms add to it.

The alternative inverts that: **the entire rule set is composite — no "pure core" anywhere, every
rule owned by some installed skill, and the loop expressed dynamically by what is installed** rather
than stated in one place and distributed from it. The entry contract would then be a rendering of
what is present, not an authored document that mechanisms write into.

Why it is not idle: the harness already has the machinery. Rules have one authored home, the
installer writes them into targets it does not own, and `inject_rules.py --check` can tell an
installed block from a hand-edited one. What is missing is the inversion — today the composition is
implicit and `AGENTS.md` is written by hand. *(Observed 2026-09-20, at
[01-0010.0110](tickets/01-0010.0110-project-facets-injected.md)'s `/verify`: one section of the
entry file, *Project-local*, is now installed blocks alone — the shape's R7 and the project's own
— and nobody hand-writes it. The rest is still authored. Evidence that the inversion is reachable
a section at a time, not a driver.)*

Why it is not queued: nothing forces it. Every ticket that would touch it has an ordinary reading
that works, and adopting the composite reading would reopen the entry contract, tier 1 and the
injection contract at once. It is recorded so that the ordinary reading is understood as a choice
rather than as the only shape available, and so the next design that strains against a hand-written
`AGENTS.md` can find this.

**What would move it:** a second mechanism whose rules cannot be expressed as a block injected into
a hand-authored tier 1 — that is, a case where the composition itself has to be derived. One does
not exist yet.
