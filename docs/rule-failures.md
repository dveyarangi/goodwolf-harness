# Rule failures

Rules that were present and did not fire, under
[`AGENTS.md` — Self-improvement](../AGENTS.md#self-improvement). A rule that was available and lost
is a phrasing or boundary defect, not only an execution slip, and the entry proposes the amendment.

Entries are struck when a later occurrence repeats one, and counted. Nothing here authorises
deleting a rule: occurrences accumulate and what to do about a rule that keeps failing is
[concern 3](concerns.md)'s, unresolved on purpose.

Whether this register and its rules become their own mechanism is
[01-0019](tickets/01-0019-harness-amends-itself-by-explicit-meta-rules.md).

## 3. The straw-dog rule sat at tier 1 and three straw dogs went unwrapped — 2026-09-14

**Rule in play:** [`AGENTS.md` — Straw dogs](../AGENTS.md#straw-dogs), read at the start of every
session. As it read until today: *"What you write to serve only until a named ticket replaces it
is a straw dog. Wrap it as you write it…"*

**What happened.** A hunt crossing live tickets against the core text they name found three
unwrapped straw dogs, written in at least three different sessions: `/ticket`'s *"it does not yet
recommend…"* (01-0010.0080), `.agents/README.md`'s *"which links are actually required is
untested"* (01-0010.0120) and its after-clone procedure ending *"once it exists"* (01-0010.0130).
Two more in the queue, both 01-0020's. Every one carried its own tell — *not yet*, *untested*,
*once it exists*, *until the pacer exists* — and none was wrapped.

**Why it did not fire** *(the user, 2026-09-14)*: **the rule was phrased descriptively, with the
imperative buried as a secondary clause.** It opened with a definition of what a straw dog *is* and
told the writer what to do once they already knew they were writing one. It never named how they
would know, so the tells the writers themselves produced went unconnected to it.

**Rejected alternative:** that tier is not the mechanism — that a rule describing an act from the
outside cannot fire on a writer who experiences the act from the inside, whatever tier it sits at.
Generalised from this one case; set aside in favour of the cheaper hypothesis, which is testable
by the next session that writes provisional text.

**Amendment, landed the same day.** The rule now opens with the verb — *"Wrap anything a live
ticket will change, as you write it"* — names the tells as the same signal, and resolves them to
*find the ticket, or mint one*. The glossary entry and `/implement`'s restatement were brought into
line.

**Disposition:** amendment landed; the five found were wrapped. Whether the rephrasing fires is
graded by the next unwrapped straw dog a hunt finds, or the absence of one.

## 2. A partial sweep was reported as a settled count — 2026-09-10

**Rule in play:** [`/maintain`](../.agents/skills/maintain/SKILL.md) — **B1** *"Declare the scope
first … and write it into the report"* and **B2** *"Certify only what you examined; mark nothing
checked that was not."*

**What happened.** Asked to hunt untagged straw dogs, I ran the guesser over `.agents` and
`AGENTS.md` — omitting `docs/`, which T1's own invocation names — and a five-phrase grep of my own
invention over `.agents` markdown only, excluding the scripts and excluding `AGENTS.md`. I then
reported *"only three places in core claim machinery"* and *"the whole corpus yields one wrap, so
there is no sweep"*, and used those to recommend a wording change to a tier-1 rule. The user asked
what the sweep had actually looked for.

**Why it did not fire.** B1 and B2 are `/maintain`'s rules and `/maintain` was not the skill being
run — this was an ad-hoc hunt inside `/align`. **The rules that govern sweeping a scope and
reporting what was covered are scoped to one skill, while the behaviour they govern happens
wherever anyone searches anything.** That is the same shape as
[failure 1](#1-a-concern-was-written-where-a-ticket-was-wanted--2026-09-10): a rule whose occasion
is broader than the skill it lives in, invisible at the moment it applies.

**Proposed amendment.** Not a rewording of B1/B2, which are correct where they sit. The two failures
together are one finding for [01-0018](tickets/01-0018-reachability-coherent.md): a rule whose
occasion is *any turn* cannot live only inside a skill's body. Whether the answer is a tier-1 line,
a group injection, or something else is that ticket's — this register's job is to record that the
same shape has now cost twice.

**Disposition:** the two overstated claims withdrawn in the same reply; the sweep not yet redone.
The reachability finding is routed to [01-0018](tickets/01-0018-reachability-coherent.md) and is not
repeated on a third record.

## 1. A concern was written where a ticket was wanted — 2026-09-10

**Rules in play, both loaded:**

- [`TICKET-FORMAT`](../.agents/skills/ticket/TICKET-FORMAT.md) — *"A ticket blocked on unresolved
  product or architectural decisions may begin as a decision-bearing HITL ticket"*, and an incepted
  ticket *"hosts chunks: routed inputs, ideas, open questions, any section."*
- [`/align`](../.agents/skills/align/SKILL.md) — *"Open questions and risks live in
  `docs/concerns.md`, this skill's artifact."*

**What happened.** Mid-align, two open decisions needed homes — whether harness self-amendment is
its own mechanism, and the group-target design gap. Both were filed as concerns. The user asked why
self-amendment was not a ticket, and named the answer: fast minting for later alignment is the
behaviour the project wants.

**Why it did not fire.** Neither rule is wrong and neither names the other. `/align` claims open
questions for its own artifact without qualification; `TICKET-FORMAT` offers the decision-bearing
ticket without saying it outranks a concern. Both were satisfiable, and the one belonging to the
skill being executed won on salience. **This is a missing boundary between two rules, not a defect
inside either** — the class that raises no error anywhere, because each rule is individually obeyed.

**Proposed amendment**, to `/align`'s concerns section rather than to `TICKET-FORMAT`, since
`/align` is where the fork is met:

> A concern is unresolved pressure **nobody is working**. The moment anyone intends to work it —
> including "later, once evidence accumulates" — it is a decision-bearing ticket, and the concern
> keeps only its architectural contact surface plus `→ queued as <ticket-slug>`. Prefer the ticket:
> minting early is cheap and a concern nobody converts is pressure with no owner.

**Disposition:** [01-0019](tickets/01-0019-harness-amends-itself-by-explicit-meta-rules.md) minted
the same day; [concern 3](concerns.md) reduced to its contact surface. The amendment to `/align` is
not yet made — `/align`'s glossary and concerns rules are both moving under
[01-0017.0010](tickets/01-0017.0010-terms-defined-before-they-land.md) and this wording should land
with them rather than ahead of them.
