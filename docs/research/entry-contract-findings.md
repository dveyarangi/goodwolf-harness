# Entry contract evidence

Evidence and evolution record for the entry contract — the versioned instructions every host
supplies at session start, announced verbatim by the session's first reply. The contract itself is
[AGENTS.md](../../AGENTS.md); this record holds what changed at each version and why, so a session
announcing a version can find out what it announced.

The version covers the **core** part only: the announce line, the general rules, the loop, the
switch roster with its meanings, and the `<straw-dog>` convention — `<temporary>` until v5.
The local block's values change without a bump.

**A recipient's line is not a version.** Since 2026-09-21 the harness mechanism stamps a
recipient's announce line `<repository>@<ref>, <date>` — the tag where the commit has one, the
short commit otherwise — so a recipient announces which core it holds and the check reads it
back. The hand-bumped version is the origin's, whose entry file cannot carry its own commit, and
this record keeps recording what each bump changed.

## v16 — 2026-09-21

**One core change:** the ticket mechanism's P9, the first block a mechanism installs into the
general rules — *name a ticket by a link to its record; one that has no record yet, by a slug
and its state word*. Decided by the user at
[01-0010.0150](../tickets/01-0010.0150-harness-meets-a-tree-with-a-method.md)'s `/plan`, after
a reply had named two tickets by ids like `.0145` before either existed. Tier 1 because the
occasion — naming a ticket in a reply — is every session's; installed from
`ticket.rules.md` rather than written by hand, so the tiering rule's owner and the injector both
see it.

## v15 — 2026-09-21

**One core change:** the tiering rule, in the general rules, wrapped on
[01-0018](../tickets/01-0018-reachability-coherent.md) under R5 until that ticket declares the
mechanism that owns it — *a skill's description is its tier-1 surface: name there every occasion
the skill serves, with the context that makes it fire, and nothing else; write every rule at the
tier its occasion reads, and no higher: what sits at tier 1 is paid for by every session*.
Decided by the user the evening [01-0010.0130](../tickets/done/01-0010.0130-harness-installs-into-another-tree.md)
closed, on three questions answered no from the tree: no maintenance pass holds skills to
`/skill-up`'s rules, `/skill-up` did not know the description is the whole of a skill's tier-1
presence, and the tier definitions had no owner. It is a meta-rule about how rules are written,
which is what the entry file holds, and every occasion that writes a rule reads it there.

## v14 — 2026-09-20

**One core change:** a general rule — *clarity and simplicity first, Occam's razor: take the shape
with the fewest parts that does the job, and remove before you add*. Decided by the user at
[01-0010.0130](../tickets/done/01-0010.0130-harness-installs-into-another-tree.md)'s second align, on
the question of whether an install needs releases and a record file; the answer to both was the
principle, so it went to tier 1 rather than into one mechanism's rules.

## v13 — 2026-09-20

**Three core changes, one occasion:** [01-0010.0110](../tickets/done/01-0010.0110-project-facets-injected.md)'s
implementation. *Project-local* is the first section of this file made of installed blocks alone:
the shape's R7, describing the local rules file instead of a tag an author writes — one file beside
the entry file, installed last as the local block, an override naming the rule it overrides, and
the rule that a local change to a rule is written there — and after it the project's own block.
*(Written by hand first; the user had it injected the same day.)* *Core and instance*
names the local block where it named the tag. *Autonomy* points at the local block under
*Project-local*, where the switches now sit as an installed rule. This project's own four blocks
left the file for `local.rules.md` the same day, which the version does not cover. Decided by the
user at the joint align of 2026-09-10 → 11, accepted on the install spec 2026-09-14.

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

## v12 — 2026-09-20

**Two core changes, one occasion.** *Core and instance* now says how core names a ticket —
*only in a straw dog's binding, never in a link, never as a bare id in prose* — and the
straw-dog rule says what a body is: *written to stand on its own, it is what a recipient receives
once the wrapper is stripped, so it reads whole without the condition and names no ticket*.
Decided by the user at [01-0011.0050](../tickets/done/01-0011.0050-shape-checked.md)'s align and
twice re-stated at [01-0010.0140](../tickets/done/01-0010.0140-core-stands-alone.md)'s `/implement`:
first when six closed tickets had been written as bare ids, then when the repair put the ids
back inside the wrappers — *consider what remains when the rule is migrated to another project
without the ticket referenced; it should still make sense as it is*. The occasion is
[rule failure 6](../rule-failures.md#6-the-binding-form-lived-on-two-tickets-and-six-closed-tickets-got-a-bare-id--2026-09-20):
the rule had lived on two tickets and nowhere core reads. Same pass: the verification-set block
and `/verify`'s sentence about it are wrapped on
[01-0010.0110](../tickets/done/01-0010.0110-project-facets-injected.md), which converts the block.

## v11 — 2026-09-20

**Two core changes, one occasion:** [01-0010.0140](../tickets/done/01-0010.0140-core-stands-alone.md)'s
implementation. The `repair` switch gains its four conditions as a paragraph under the table —
the policy that `docs/process.md` had held since 2026-09-05, now in the file core reads — and
*Core and instance* names *a ticket's own file* in words where it had illustrated with a ticket's
path, which the new leak check would otherwise flag in the entry file itself. This project's
four verification commands join the file inside a `<project-local>` block, which the version
does not cover.

## v10 — 2026-09-20

**One core change:** the straw-dog rule gains a second occasion. It read *wrap anything a live
ticket will change, as you write it*; it now adds *or, for text already written, in the pass that
mints the ticket or decides that it will change it*. The occasion is
[rule failure 3](../rule-failures.md#3-the-straw-dog-rule-sat-at-tier-1-and-three-straw-dogs-went-unwrapped--2026-09-14)'s
second strike: sixteen bare links from core into `docs/` were counted as violations at
[01-0010.0140](../tickets/done/01-0010.0140-core-stands-alone.md)'s align on 2026-09-20 and left
unwrapped, because the rule binds to writing and nobody was writing them — they were written
before the ticket existed and became provisional the day it was minted. Wrapped at the ticket's
`/plan` the same day, with the amendment. **Same pass, one word:** *Core and instance* said
*places* for what core may name under `docs/`; the user chose the install spec's word, and the
method glossary now defines **painted door**, with *place* and *path convention* under *Avoid*.

## v9 — 2026-09-20

**One core change:** the announce sentence now also says *start every session by running
`/recall`, whatever the first message says*. Decided by the user on 2026-09-20 at
[01-0020](../tickets/01-0020-pacer.md)'s align, and the first of the pacer's core rules to land in
the entry file. The occasion is
[rule failure 4](../rule-failures.md#4-the-wake-rule-sat-in-a-diagram-and-a-greeting-was-answered-with-a-greeting--2026-09-20):
the loop diagram had said *wake with `/recall`* since v1, and on 2026-09-15 a session opened with
"good evening" was answered with a greeting. The sentence sits beside the announce line rather
than in the loop section because it is the one line every session provably reads first — the
announce line is the evidence — and it opens with the verb, as
[failure 3](../rule-failures.md#3-the-straw-dog-rule-sat-at-tier-1-and-three-straw-dogs-went-unwrapped--2026-09-14)'s
amendment taught. The diagram's *wake with `/recall`* stays as the picture of the same rule. The
user refused a carve-out for a first message that names a skill or a task; how that sits with
*one turn, one step* is the pacer's chaining question, still open on the ticket.

## v8 — 2026-09-09

**Three core changes, from an `/align` the user opened on a contradiction I had reported in v7's
own pass.** v7 was never announced by a session; both versions land in one uncommitted change, and
they are kept apart because v8's decisions were taken after v7's were written and would otherwise
be back-dated into them.

**The load-bearing section names real homes.** `Core docs and ADRs are the home for` became
`A project's architecture, ADRs and glossary`. The word was the defect: [the
glossary](../../.agents/glossary.md) reserves **Core** for the accepted shared method at its
canonical source — `.agents/` — so the section, read against this project's own vocabulary,
instructed the reader to put architecture into core. It worked: during the align I recommended a
new `.agents/architecture.md` and argued for it twice before the user refuted it, on the ground
that core is what is useful at runtime while architecture is for construction, and a recipient
needs the harness's output rather than the record of its building. That layering is now
[ADR-0001](../adr/0001-agents-is-runtime-docs-is-construction.md), written because two exchanges
were spent on a decision nothing recorded.

A sentence follows the list: **a decision forms in its owning ticket and lands in one of these when
it is ready; a decision about a mechanism lands in that mechanism's doc, and what was refuted in its
evidence.** The user's rule — *tickets can carry decisions until they are ready, then the
architecture should move to stable docs*. **P7** already fires at `/align` and says *land a resolved
decision in its durable home*; it never named the homes, and the measured cost of that gap was
`mechanism-shape`'s doc asserting rules whose why had stayed in the instruction file. Repaired in
the same session's `/maintain`.

**`<project-local>` gains a multiplicity rule**, nine words: *one block per local fact, beside the
rule it answers.* Written because I collapsed blocks into one per document three times in one
session and produced a justification each time only after the merge — the tag is a marker on a
statement, not a region of a file. It was first recorded as a note about my own habit and moved
here on the user's correction: a rule every agent in this tree needs, and one that must travel, is
not a private memory.

**The opening block sheds four shared statements** — the queue's path, *decisions live in the owning
ticket* (now stated properly in core above), and `docs/process.md`. Each is harness layout, which
*Core and instance* already says is not a reference and needs no block. Three stay: self-hosting;
the contract-change record; and **the glossary split, which is local** — no estate has
`.agents/glossary.md`, so the two-glossary arrangement is this project's answer to a collision only
this project has, its domain being the method.

**ADRs were not removed, and the reason is worth keeping.** The align opened with my recommendation
to delete `docs/adr/` and its four references as an unexercised convention, on the evidence that
this project had written none in twelve sessions. The user refused: the harness redeploys into
estates that already run on them. Meteoscape holds 7 ADRs, Forecast Collector 5, and
`docs/concerns.md` — which I had called a painted door with five transactors — exists in all four
audited estates, 1264 lines of it in Meteoscape. Both of my errors that day were the same error in
opposite directions: this project's emptiness assumed to generalise, and this project's structure
assumed to generalise. Neither took ten seconds to check. What survives is narrower and is
[01-0017](../tickets/01-0017-io-graph-coherent.md)'s: nothing distinguishes a convention an instance
has not populated from a reference that is simply broken.

**A cost, recorded rather than repaired.** Removing the queue's path here and `/recall`'s pointer
block in the same session left a waking session meeting the queue nowhere at tier 1. Each removal
was correct by `/maintain`'s E1; the sum was not. On
[01-0018](../tickets/01-0018-reachability-coherent.md) as its second observed instance, and the
first anyone manufactured while tidying.

## v7 — 2026-09-09

**Four core changes, all from the user reading the file straight through.**

The title became `Entry contract`. It had been `Session entry`, which names the occasion rather
than the thing; the announce line on line 3, the glossary term, this record, and every downstream
mention already said *entry contract*, so the title was the only holdout. The announce instruction
now names that line — `the Entry contract: line above` — instead of pointing at "the line above",
which was a positional reference in the one rule whose whole job is being unambiguous evidence.

`<project-local>` got its own section. It had none: the marker was used twice in the file and
explained only in passing inside **Core and instance**. Two rules, one of them reaching tier 1
for the first time — a block is carried *only* for a fact that would differ in another project,
which had lived since 2026-09-06 in
[01-0010](../tickets/01-0010-dev-harness-shared-and-local.md#resolutions-and-constraints)'s
resolutions and nowhere a session would meet it. It was applied by hand to `/recall` in this same
pass, from the ticket, which is what showed it had no reachable home. The section was drafted at 90
words and cut to 40 on the user's *write for a capable model*: the glossary's definition, the
forcing example, the sentence saying what the rule implies, and finally the pointer to `/skill-up`
all came out. `/skill-up` already carries that as a rule — *a skill is instruction, not story* —
so the padding was a violation rather than a style choice.

**Core and instance** lost its self-hosting paragraph as prose and kept it as a block. My first
attempt merged it into the file's opening `<project-local>` block, on the reasoning that *develops
the harness using its own loop* already said it. The user asked what had forced that, and nothing
had: the two are different facts. One is how work is done here; the other is a reading instruction
for the core/instance rule, and its reader is someone inside that section. It went back there as
its own block. The reference rule left as a paragraph and came back as a clause in the exemption
sentence: 45 words became 26, and the forcing case it named went to the new section.

The word *sidecar* left the entry file. The glossary reserves against it for **Evidence** —
*sidecar describes a file's position, never its contents* — and the removed paragraph used it
twice, so the one file every session reads was teaching the noun the glossary forbids.

**Reported in the same pass and not changed, because each needs a decision:** `Core docs and ADRs
are the home for` names a home this project has never created while the file's own block routes
decisions to tickets; and this record's statement of what a version covers — the announce line,
general rules, loop, switch roster, straw-dog convention — does not name **Core and instance**,
either load-bearing section, or **Helpers**, so four sections of the contract sit outside the
scope the version claims to cover.

## v6 — 2026-09-09

**One core change:** a straw dog is wrapped at its authored home, never where the harness installs
or derives it; what lands there takes the content and not the tag. The wording went through the
user twice: *wrap what is authored* named the act and left the reader to infer the thing, and its
first draft called an installed block a *copy*, which the glossary reserves against for exactly
that noun. The section was also cut from 152
words to 114 at the user's instruction in the same pass — the reasoning left the entry file for
this record, since a tier-1 rule pays its cost every session. Decided by the user at
[01-0011.0025](../tickets/done/01-0011.0025-archive-duty-reaches-maintain.md)'s `/maintain`, from
a concrete miss in that same pass. P8 was minted as an expiring rule, and its marking was put in
the mechanism's doc rather than on the rule, on my wrong claim that a rules file could not hold
the tag. Two probes settled it: the installer parses a wrapped section and renders a byte-identical
block, and the listing finds a straw dog written in a rules file. The rule now has one wrapper at
its authored home instead of a note two files away. The refusal that enforces it is
`inject_rules.py`'s — a `<straw-dog>` inside a rule body, which would be copied into every target
and then blanked by the listing, is refused — and the grammar is the format shelf's.

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
