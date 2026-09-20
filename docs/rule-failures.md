# Rule failures

Rules that were present and did not fire, under
[`AGENTS.md` — Self-improvement](../AGENTS.md#self-improvement). A rule that was available and lost
is a phrasing or boundary defect, not only an execution slip, and the entry proposes the amendment.

Entries are struck when a later occurrence repeats one, and counted. Nothing here authorises
deleting a rule: occurrences accumulate and what to do about a rule that keeps failing is
[concern 3](concerns.md)'s, unresolved on purpose.

Whether this register and its rules become their own mechanism is
[01-0019](tickets/01-0019-harness-amends-itself-by-explicit-meta-rules.md).

## 6. The binding form lived on two tickets, and six closed tickets got a bare id — 2026-09-20

**Rules in play:** [01-0011.0050](tickets/done/01-0011.0050-shape-checked.md)'s align, *Related* —
core names a ticket in a binding, never a link, and *a bare ticket id was refused: it ships an
origin id a recipient cannot verify and might collide with*; and
[01-0010.0140](tickets/01-0010.0140-core-stands-alone.md)'s *What to build* — *the 34
ticket-naming links carry `.0050`'s form*. Both read at `/plan` the same day.

**What happened.** The RFC carved the six links to *closed* tickets out of the rule — *the ticket
named in words, no binding: closed work changes nothing* — put it to the user as a choice, read
the user's *I do not understand how it is relevant* as assent, and `/implement` wrote six bare
ids into three mechanism docs and the discover evidence. The user: *keeping the ticket link in
the straw-dog attribute is the valid thing, we already decided this; it is more proper than
adding a ticket id into non-straw-dog text.*

**Why it did not fire.** The decision had no home in core. It sat on a closed ticket's *Related*
bullet and on a live ticket's build list — records, read once at `/plan` — and no sentence in the
entry file, the glossary or a skill said *core names a ticket only through a binding*. With no
standing rule, the question looked open enough to re-derive, and the re-derivation found a
reason (*closed work changes nothing*) the refused form never depended on: the refusal was about
what ships, not about whether the ticket is live.

**Amendment, landed the same day — in two steps, because the first was wrong.** The first cut put
the sentence in *Core and instance* as *the path in the binding, the id in words in the body*,
and rewrote the six as `<straw-dog …>01-0011.0022</straw-dog>'s align`. The user: *you are still
messing with straw dogs — consider what happens to what remains when the rule is migrated to
another project without the ticket referenced; it should still make sense as it is.* A body that
names the ticket ships the bare id the refusal was about. So the rule is about the **body**: it
is what a recipient receives, it reads whole without the condition, and it names no ticket — the
binding does. Landed at entry contract v12 in *Core and instance* (*core names a ticket only in a
straw dog's binding — never in a link, never as a bare id in prose*) and in the straw-dog rule
(*write the body to stand on its own*). The ten wrappers touched today are rewritten so each
body is a sentence a recipient can read — *Two graders, two questions, pre-registered at the
align that declared this mechanism* — with the ticket only in the attribute. Graded by the next
core sentence that names a ticket: bound, with a body that stands alone, or this entry is struck.

## 5. The rule said "allowlist", so a list was built — 2026-09-20

**Rules in play:** mechanism-shape's **R4** — *render an index on request; never commit one
beside its records* — installed in `/mechanism`, loaded; [`AGENTS.md` — Straw dogs](../AGENTS.md#straw-dogs)
— *wrap at the authored home, never where the harness installs or derives it*; and the sentence
in `/mechanism`'s body since 2026-09-08, *a skill belonging to no mechanism goes in the
allowlist, with its reason*, with the spec's *listed with its reason* behind it.

**What happened.** At [01-0011.0050](tickets/done/01-0011.0050-shape-checked.md)'s align the user
accepted "one file" for the unclaimed skills and the `docs/` places; I built
`.agents/mechanisms/allowlist.md` — nineteen rows, each a straw dog, declared as a record of the
mechanism shape — and the user refused it on sight: the idea was to inline the straw dogs into
their targets, since a binding's ticket path is allowed anywhere a tag strips on separation.

**Why it did not fire.** The list was an index — every row said what the skill's own first line
could say — and R4 forbids committing one. But R4 says *index*, and the rule that named the
thing to build said *allowlist*: the noun in the rule was a list, so a list got built, declared
as a record so it would not look like an index. The straw-dog rule's *authored home* did not
fire either, because I was authoring a new record rather than deriving one, and nothing said
that a record made of other files' claims is a derivation.

**Amendment, landed the same day** *(the user: "amend the rules that caused that")*. R4 now
names the shape: *a file listing what other files each say for themselves is an index, whatever
it is called — an allowlist, a register, a manifest — and each entry belongs at its authored
home, wrapped there if provisional.* R6 no longer says *allowlist*: a skill *says so on its
first body line*. The body sentence is gone from `/mechanism`, R6 installed in its place. The
spec and ticket vocabulary stay as history.

**Disposition:** amendment landed; the file deleted; nineteen skills carry their own line.
Graded by the next list anyone proposes for what files can say themselves.

## 4. The wake rule sat in a diagram, and a greeting was answered with a greeting — 2026-09-20

**Rule in play:** [`AGENTS.md` — The loop](../AGENTS.md#the-loop), read at the start of every
session, whose picture has read `session: wake with /recall → /align → /conclude` since v1. Behind
it, [pacer.md](pacer.md#core-rules--under-alignment)'s 2026-09-06 rule that a session starting
with "what's next" starts with `/recall`.

**What happened.** The session of 2026-09-15 opened with "good evening". The first reply announced
the contract, reported the tree clean and *offered* `/recall` — "say `/recall` when you want to
pick up where that left off". The user then invoked it by hand, with the question of how to make
it the default. Twelve earlier sessions had taken the wake by hand too, which
[01-0020](tickets/01-0020-pacer.md) already recorded on 2026-09-09 without treating it as a
failure.

**Why it did not fire.** The instruction lived in a diagram — a noun-phrase picture of the loop,
not a sentence addressed to the agent — and the only sentence-form rule was scoped to a message
that says "what's next", which a greeting does not. Same shape as
[failure 3](#3-the-straw-dog-rule-sat-at-tier-1-and-three-straw-dogs-went-unwrapped--2026-09-14):
present, descriptive, with no verb at the occasion. And the same shape as failures 1 and 2 in the
other direction: the occasion is *every first turn*, and the one sentence every first turn provably
reads — the announce rule, whose line is the evidence — said nothing about it.

**Amendment, landed the same day** *(the user: "any session wake should start with recall", no
specifics)*: a second sentence beside the announce rule, *Run /recall first in every session,
whatever the first message says*, with the contract bumped to v9. A first draft appended it to
the announce sentence as a trailing clause; the user caught that as the failure-3 shape
reproduced in the fix, and it became its own sentence opening with the verb. The diagram stays.

**Disposition:** amendment landed. Graded by the next session's first reply: it runs `/recall`
before anything else, or this entry is struck. **Graded 2026-09-20:** the next session opened
with "good morning" and its first reply ran `/recall`. The rule fired.

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

**Struck, 2026-09-20 — one repeat, and the grade is in.** The amended rule was read at session
start, `/mechanism` was loaded in the same turn, and the new wake rule
([failure 4](#4-the-wake-rule-sat-in-a-diagram-and-a-greeting-was-answered-with-a-greeting--2026-09-20))
went into `AGENTS.md` unwrapped. The user asked who owned it. Three causes, none of them the
2026-09-14 one:

- **The sentence carried no tell.** It was written as permanent — *Run /recall first in every
  session* — because its content and location are final. What a live ticket will change is its
  *form*: hand-authored where the mechanism shape says installed from a rules file. The amended
  rule binds recognition to the writer's provisional vocabulary, and a rule provisional by
  ownership rather than by wording produces none.
- **The governing ticket said "placed".** 01-0020's What-to-build bullet, written 2026-09-06,
  described the core rules as *placed in `AGENTS.md`* — one day before the mechanism shape fixed
  *installed, never authored* — and was never re-read against it. The first trigger, *will a live
  ticket change this*, was asked and answered no on the ticket's own word. A ticket is not a
  mechanism, so nothing re-checks it when what governs it moves.
- **Two satisfiable rules in `/mechanism`, and salience won** — failure 1's shape. Its three-homes
  table names `AGENTS.md` as the home of *meta-rules and general rules*, which the sentence looked
  like; *a sentence about another mechanism is that mechanism's* sits three sections later. No
  check discriminates: the installer sees only blocks, the guesser only tells.

**Amendment, landed the same day** *(the user)* — not to the straw-dog rule, whose tells were never
the cause, but at the moment of the act. The three-homes table in `/mechanism` no longer admits
"general rules" to the entry file: meta-rules, and a mechanism's rules only as installed blocks.
The instruction for the undeclared case is mechanism-shape's **R5**, installed into `/align` and
into `/mechanism` itself: land a mechanism's rule in `AGENTS.md` only as an installed block, and
while the mechanism is undeclared write it by hand and wrap it on the inception ticket as you write
it. Landing R5 surfaced that the shape installed rules into its own skill without saying so and
titled every rules file to say the opposite; the policy is now in `/mechanism` — a rule two
occasions read is installed everywhere it is read, the owner's own skill included — and the titles
say what the practice was. Graded by the next mechanism rule written into the entry file: wrapped
on its ticket, or this strike counts twice.

**Struck again, 2026-09-20 — a third cause.** At
[01-0010.0140](tickets/01-0010.0140-core-stands-alone.md)'s align the same morning, sixteen bare
links from core into `docs/` were counted as violations, sequenced for the ticket's `/plan`, and
left unwrapped; at `.0050`'s `/verify` the hunt found them again and the user asked why they were
still bare. The rule was read at session start both times. **It binds to writing** — *as you write
it* — and nobody was writing them: every one was written before `.0140` existed, on 2026-09-10,
and became text a live ticket will change the day the ticket was minted. Minting is the occasion,
and the rule had no sentence for it; the reading-side rule that does exist is `/verify`'s hunt,
wrapped on 01-0016, which fires at a close and not at a decision.

**Amendment, landed the same day.** The tier-1 sentence gains the second occasion: *or, for text
already written, in the pass that mints the ticket or decides that it will change it* — entry
contract v10. The sixteen are wrapped at `.0140`'s `/plan`. Graded by the next ticket minted
against existing text: wrapped in the minting pass, or this entry counts three times.

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
