# Every skill and document has named producers and consumers

- **Status:** Planned (the first mechanism precedes)
- **Type:** HITL
- **Depends on:** [The shape is checked mechanically](./done/01-0011.0050-shape-checked.md) (a proven
  shape and a working check, so applying it to the rest is application rather than design)
- **Outcome:** Every mechanism in this tree is declared to the shape paired close proved, every
  installed skill is named by one or allowlisted with its reason, and the documents four skills
  transact against either exist with an owner or stop being referenced.

## Parent

[A mechanism has one home for its rules, and a derived index](../spec/01-0011-mechanism-shape.md).

**Re-parented 2026-09-06.** This was minted earlier the same day as a fifth rule refactor, before
the mechanism spec existed. Its questions — who produces a thing, who consumes it, what verifies it
— are the ones a mechanism doc answers about its own parts, so this is the spec's generalisation
step rather than a sibling of the rule refactors. It is not `Done (split)`: nothing was split, and
the work survives whole. What changed is its vocabulary and its place in the order.

## A recipient receives skills written in a vocabulary they do not receive

**Surfaced 2026-09-07** during [01-0011.0010](./done/01-0011.0010-mechanism-declared.md)'s fifth
planning pass, and it belongs here by subject rather than by where it was found.

`/mechanism` will use **Mechanism**, **Moment**, **Doc**, **Evidence**, **Part** and **Tier**
without defining any of them, which is correct: [the glossary](../glossary.md) owns them,
[`/skill-up`](../../.agents/skills/skill-up/SKILL.md) says a fact one skill states is referenced
rather than restated, and [AGENTS.md](../../AGENTS.md) explicitly permits core to name
`docs/glossary.md` as a path convention.

But the same rule says a recipient replaces `docs/` **whole**. So a recipient receives a core skill
written in a vocabulary their glossary does not contain. The naming-a-convention exemption does not
cover it: what is exempt is naming the path; what is missing is the content behind it.

**Resolved for the glossary, and only for the glossary** *(the user, 2026-09-07)*, in
[01-0011.0010](./done/01-0011.0010-mechanism-declared.md) — because that slice adds **Part**, and a new
core term landing in the instance half would be the same defect committed while describing it.
`.agents/glossary.md` takes the method's vocabulary and travels; `docs/glossary.md` keeps the
project's domain. The corpus already assumed that split: `/align`, `/tdd`, `/implement` and
`GLOSSARY-FORMAT` all mean the domain glossary, and only `/maintain` and `AGENTS.md` meant the
harness's. Life keeps the same split by construction.

**What remains here is the general case, and it is most of it.** Every other core skill still
leans on instance-half documents: `/maintain` cites `docs/process.md`, `docs/architecture.md` and
`docs/research/maintenance-findings.md`; `/implement` and `/impact` cite the process. Each is
owned by its own ticket as a repair, but *what core may lean on at all* — and whether the answer
is a travelling counterpart, a local block, or an accepted limit stated out loud — is this
ticket's align to weigh. The glossary is now the worked example of one answer, not a precedent
that settles the rest.

## Impact

**2026-09-06, at minting.** Touches all eleven `SKILL.md` files — none of which declares a source or
target today — plus `docs/README.md`, the three `align/*-FORMAT.md` shelves that name documents, and
`AGENTS.md` if the convention is Tier 1. Verdict: **proceed, narrowed** — exclude `/edge`, and make
the check mechanical rather than prose.

**2026-09-06, on the mechanism split.** Re-assessed as part of
[that breakdown](../spec/01-0011-mechanism-shape.md#impact--2026-09-06). The declaration this ticket
wanted is a mechanism doc; the composing rule is the shape check; the enforcement is
`/mechanism`'s. What remains here is applying both to the tree once one mechanism has proved them.

**2026-09-10, on carving out the first conversion.** Assessed inline during the align that produced
it rather than through an `/impact` pass, and no split was drafted: one ticket,
[01-0017.0010](./01-0017.0010-terms-defined-before-they-land.md).

*Blast radius.* Six current homes for glossary rules — `/align`'s two sections, `GLOSSARY-FORMAT.md`
on `/align`'s shelf, the two glossaries' preambles, one-liners in `/implement`, `/tdd`, `/dream`,
`/edge`, `/skill-up`, `/recall` and `TICKET-FORMAT`, and a relied-on row in all three mechanism
docs. Plus `AGENTS.md`, which would take **the first installed block any mechanism has written into
tier 1**; every rules file today targets a `SKILL.md`.

*Hidden edges.* The tier-1 line and the injected block may be one fact in two homes, which is
[01-0018](./01-0018-reachability-coherent.md)'s unsettled rule and must not be settled here. Group
targets now have three shapes wanting them and cannot resolve while nineteen skills belong to no
mechanism, so the interim is explicit targets plus a new maintenance duty when a target skill
appears. `AGENTS.md` has no installer, which makes
[01-0010.0130](./done/01-0010.0130-harness-installs-into-another-tree.md) a dependency rather than a
neighbour.

*Leave alone.* The glossary records, their format, and the method-versus-project collision rule —
all held. The defect is that no rule fires at the moment a word is used.

*Recommendation.* One decision-bearing ticket, not a split: the mechanism's declaration, its
tier-1 rule and the six-home consolidation are one act, and separating them would land a rule with
no authored home or a home with no rule.

## Why this exists

Two failures of the same kind, in opposite directions, neither caught by anything:

**A duty whose worklist nothing produces.** "When every acceptance box is checked, move the ticket
to `done/`" is written only in `/ticket`'s files — [SKILL.md](../../.agents/skills/ticket/SKILL.md)
and [TICKET-FORMAT.md](../../.agents/skills/ticket/TICKET-FORMAT.md) — while
[the process](../../.agents/mechanisms/maintain/maintain.md) assigns archive operations to `/maintain`, whose body
carries only the gate form. On 2026-09-06 five tickets were eligible and unarchived
(`01-0010.0020`, `.0030`, `.0035`, `.0050`, `.0060`), three with unarchived RFCs. No skill's
declared output is "the records that should have moved", so the backlog was invisible rather than
ignored.

**A declared producer that has never produced.** [`/align`](../../.agents/skills/align/SKILL.md)
says open questions and risks live in `docs/concerns.md`, *this skill's artifact*. That file does
not exist **here** and never has. `/plan` reads it, `/ticket` writes concern promotions into it,
`/maintain` sweeps it as the concern index, and since 2026-09-09 `/edge` points into it. Five skills
transact against a document this tree does not have.

**Corrected 2026-09-09, against the estates rather than against this tree.** The earlier reading —
*a declared producer that has never produced* — was drawn from this repository alone, and the second
shape refutes half of it. `docs/concerns.md` exists in all four estates the audit drew from:
1264 lines in Meteoscape, 427 in DriftSense, 152 in Life, 127 in Forecast Collector. `docs/adr/`
holds 7 and 5 in the two that use it; `docs/edge/` holds 3 in each of two. **These are conventions
every recipient populates, and core is right to name them.** What is true is narrower and more
useful: *this* project populates none of them, because it builds method rather than software, and
**nothing distinguishes a convention an instance has not populated from a reference that is simply
broken.** A reader here finds four absent documents and cannot tell which kind they are; so did I,
twice, on 2026-09-09 — once in `/advise` and once by writing the wrong finding into this paragraph.
That distinction is what this ticket's disposition must produce, and it is the rule a link check
needs before it can be written at all.

The two are materially different — a missing producer versus an absent artifact with a named owner
— and force the same concept, which is what [the entry file](../../AGENTS.md) requires before
generalising from one shape.

The other direction is unwatched too: `docs/pacer.md` and two of the three
`docs/research/*-findings.md` are named by no skill file at all.

## What to build

- Every remaining mechanism in this tree declared to the shape
  [paired close](./done/01-0011.0010-mechanism-declared.md) proved: its parts named with their owners,
  its three property states stated, each absence carrying its kind and, where it is a gap, a ticket.
- Every installed skill named by a mechanism or placed in the allowlist with its reason. ~~Eleven
  are installed~~ — **twenty-two, as of 2026-09-09**, when `/recall`, `/edge`,
  `/review-architecture` and `/setup-devops` completed the selection; three are named by a
  mechanism, so nineteen rows are owed. The allowlist rows are as much the deliverable as the
  declarations, because a skill nothing knows about is where an injected rule goes to hide.
- Documents brought into the mechanisms that own them. A document no mechanism writes or reads is a
  finding, not a fact to record — `docs/pacer.md` and two of the three `docs/research/*-findings.md`
  are named by no skill file today.
- Dispositions for `docs/concerns.md` and `docs/adr/`: created with an owning mechanism, or their
  references removed from `/align`, `/plan`, `/ticket` and `/maintain`. The check surfaces these on
  its first run over a tree that declares more than one mechanism.

## Routed here at `01-0011.0022`'s align, 2026-09-07

Two findings outside that slice's scope, captured under `/maintain`'s rule that a finding is
routed to the record owning its subject after the open issues are searched; neither was already
held anywhere.

- **A whole-tree link check has no instruction and no script.** The only link check in the tree
  is `move_doc.py`'s dangling-reference note over records a close rewrote; session nine's *zero
  broken links* was counted by hand. `/maintain`'s moments table carries *checking links outside a
  close* as `not yet` naming this ticket, whose outcome already says documents referenced either
  exist or stop being referenced — widened by this sentence to *and every citation resolves*,
  mechanically, rather than minting a ticket for forty lines over `docs_corpus.py`.
- **`/verify` restates a meta-rule.** [verify/SKILL.md:38](../../.agents/skills/verify/SKILL.md),
  *anything that can be maintained mechanically must be*, is `/mechanism`'s meta-rule, D1 of
  `/maintain`'s aligned rules, and meta-rules are never injected *(the user, 2026-09-07)*: a skill
  applying one reads it in `/mechanism` or the entry file. The copy is this ticket's to remove with
  the rest of the corpus sweep. `/implement:38–40`, *do not move the RFC to `done/`; `/maintain`
  does that* and *use `/verify` and `/maintain` to review the work*, ~~was raised in the same
  breath and not ruled on~~ — **ruled 2026-09-07 at `.0022`'s `/plan`** *(the user)*:
  `/implement` should not mention `/maintain` at all; the sentences are an artefact of the era
  when `/sync-arch` was held separately, and they go in this sweep.
- **A mechanism doc's `not yet` rows link specific tickets under `docs/`** — observed at
  `.0022`'s `/verify`, 2026-09-07. **Resolved by `.0050`, 2026-09-20:** a `not yet` row is a
  straw dog and its ticket is the binding, which the shear strips; no cell carries a link. The format requires the link and the check enforces it, both
  decided before *Core and instance* existed; that rule exempts naming the `docs/tickets/`
  convention, not pointing at one document. Whether a doc's ticket links fall under the
  exemption, or belong in a `<project-local>` block the check reads, is this ticket's question
  about what core may lean on. Two declarations carry such rows today.
- **The map of missing instructions has homes here** *(the user, 2026-09-07)*. Every `not yet`
  and `embedded` row a declaration carries is maintenance owed to a skill not yet through
  `/mechanism`'s inception. [.0050](./done/01-0011.0050-shape-checked.md)'s report is the map; this
  ticket gives each row a home — an inception ticket for the mechanism that owns the missing
  rule, or an injection into a target once its owner is declared. An absence should say which fix
  it wants: **a rule injected from a mechanism not yet declared**, **a rule that cannot be
  injected** — a meta-rule, or judgment — **and needs a body**, or **a genuine gap** with no rule
  anywhere.

## Decisions this ticket's align owns

- Where the mechanism boundaries actually fall. The delivery ring, the entry contract, the autonomy
  switches and the verification set are all candidates, and drawing them wrong produces a register
  that groups subjects while missing the action that spans them.
- Whether tickets, RFCs and session records are parts of a mechanism or only records it accumulates.
  They have writers and readers, but their lifecycle is archival.
- ~~Whether `docs/concerns.md` and `docs/adr/` are created or their references removed.~~
  **Narrowed 2026-09-09:** removal is off the table — the estates this harness redeploys into
  already run on both, and Meteoscape's `concerns.md` is 1264 lines. What is open is how an
  instance declares which harness-imposed conventions it populates, so an unpopulated one reads as
  a stated absence rather than as a dangling reference. Until that exists, every reader of this
  tree has to rediscover it.

## Acceptance criteria

- [ ] Every mechanism this tree has is declared, with its parts, owners and three property states.
- [ ] Every installed skill is named by a mechanism or allowlisted with a written reason; none is
  silent.
- [ ] Every durable document is named by the mechanism that writes it and by the ones that read it,
  or is listed with its reason.
- [ ] `docs/concerns.md`, `docs/adr/` and `docs/edge/` each have a disposition **as conventions this
  instance does or does not populate**, stated where a reader meets the absence, and no skill
  references an artifact without one.
- [ ] The shape check runs over the whole tree and its output is clean or every finding has an
  owner.
- [ ] `/verify` has been run on this ticket against its ticket, RFC, and governing docs.

## Out of scope

`/edge` and `docs/edge/` — [01-0010.0100](./01-0010.0100-remaining-named-corpus.md) owns the Edge
half, down to whether `/maintain`'s Edge-record check has records to check. What each skill *owns*
is [01-0016](./01-0016-responsibility-coherent.md)'s; this is what each mechanism is made of.
Whether a rule *arrives* at its occasion is [01-0018](./01-0018-reachability-coherent.md)'s.
Building the shape and proving it on one mechanism is
[01-0011](../spec/01-0011-mechanism-shape.md)'s children; this applies what they proved.
Relocating `docs/architecture.md`'s script contracts, which moves for a different reason.

## Parent scope addressed

The spec's generalisation step: stories 13, 14, 21, 22, and the second mechanism that proves the
shape holds beyond the one it was built on.
