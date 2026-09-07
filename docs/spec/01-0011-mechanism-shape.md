# A mechanism has one home for its rules, and a derived index

**Status:** **Accepted by the user, 2026-09-06.** Developed through `/spec` → `/align`;
decomposed by `/ticket` into [01-0011.0010](../tickets/01-0011.0010-mechanism-declared.md) …
[.0050](../tickets/01-0011.0050-shape-checked.md), with
[01-0017](../tickets/01-0017-io-graph-coherent.md) re-parented here as the generalisation step.

**Amended 2026-09-06** during [01-0011.0010](../tickets/01-0011.0010-mechanism-declared.md)'s
`/align`, on the user's decision, after Life's own mechanism apparatus was read in detail. Four
changes, each recorded in its section below: a mechanism has **one instruction file**; the shape
is read **in the skill**, not in the doc; the three properties are **not three co-equal states**
but three rules at different altitudes; and the **first mechanism declared is `/mechanism`
itself**, then `/maintain`, then `/ticket`. The problem statement and its evidence are unchanged.

**Amended again 2026-09-07** during that ticket's `/plan`, on the user's decision, after Life was
read directly rather than through this spec's summary of it. One change: **the register is derived
and no file holds it**, superseding *the register is `.agents/README.md`*. Two corrections of fact
also land here — Life's `/mechanism` says an instruction file is *"usually a skill, and there may
be several"*, so one-instruction-file-per-mechanism is this project's tightening rather than
Life's practice restated; and Life keeps `skills` as a **separate mechanism** with `/skill-up` as
its instruction file, which confirms this spec's *`/skill-up` is not this* from the other estate's
own structure rather than by assertion.

**Amended a third time 2026-09-07** during that ticket's `/implement`, on the user's decision, on
reading the installed skill back. One change: **the membership test names its subject** — a
mechanism is part of how the work gets done, never what the project produces. The question that
found it was what the tier-1 trigger would do in a recipient project asked to build a feature.
Recorded in *Implementation Decisions* below; the glossary's **Mechanism** carries it too, since
the leak was in the definition rather than in the skill.

Acceptance covers the shape, the three homes, injection, the derived index and the
one-mechanism scope of the first build. It does not settle whether the queue's rendered table is
committed — that reasoning was taken from a tree with wake hooks this harness lacks, and the
question is [01-0011.0040](../tickets/01-0011.0040-queue-derived-index.md)'s align to answer.

## Problem Statement

A rule in this harness has no home rule. It lands wherever the person writing it happened to be, and
nothing notices when that place is wrong. Four failures on 2026-09-06, all the same defect wearing
different clothes:

- **Five tickets sat finished and unarchived.** The duty that requires the move is written only in
  `/ticket`'s files, while `/maintain` owns archiving. `/maintain`'s own body carries the permission
  form — *a ticket moves only when…* — and never the duty. Nothing swept for eligible records, so
  the backlog was invisible rather than ignored.
- **`docs/concerns.md` has never existed**, while `/align` calls it *this skill's artifact*, `/plan`
  reads it, `/ticket` writes promotions into it and `/maintain` sweeps it as the concern index. Four
  skills transact against an absent document. `docs/adr/` is the same story.
- **Repair-and-report is stated in three skills; scope in four places.** `docs/process.md` claims a
  split — *the steps belong to the skill; this document owns the policy* — that its own text does
  not honour: the spec-archive rule appears near-verbatim twice, and the missing-script rule twice
  within `process.md` itself.
- **66% of `docs/process.md`** — 1056 of 1591 words — is rules belonging to a skill or to an owner
  that does not exist. `process.md:72` says why: *"Mechanism boundaries, document layout,
  maintenance triggers and automation are still to be specified."* The concept was adopted and its
  owner deferred, so its rules accreted where the adoption note was.

The concept is not missing. [The glossary](../../.agents/glossary.md) defines **Mechanism** — a behavior on
which other work relies, together with its instructions, producers, consumers, checks and records —
and **Skill** as an invocable instruction part of one. Nothing owns the definition, so nothing
applies it.

### Why these are one problem, and what actually separates success from failure

This repository ran a natural experiment on 2026-09-06 without meaning to. Two mechanisms, one held
all day and one lost five tickets:

| | temporary statements — held | paired close — failed |
|---|---|---|
| where the duty is delivered | `AGENTS.md`, supplied at session start | `/ticket`'s files, behind a link |
| restated elsewhere | yes, in `architecture.md` | yes, in two files |
| a way to list what it owes | `temporary_statements.py` | nothing |
| result | correct on three passes | five records lost |

**Both are duplicated**, so duplication is not what broke the second one. The two differences that
separate them are *delivery* and *listing*, and the day's failures sort onto three concerns:

1. **Delivery** — the duty reaches the occasion it governs. The archive duty did not.
2. **Listing** — what a mechanism currently owes can be asked for and derived. Nothing could list
   eligible-but-unarchived records.
3. **Single authorship** — the rules have exactly one home, and copies are installed rather than
   written. This is what produced the three-skill and four-place restatements.

Failures 1 and 2 lose work. Failure 3 produces drift. They do not substitute for each other, and
injection — the fix for 3 — would not have saved the five tickets.

**They are not three co-equal states, and an earlier draft of this spec made them one.** Amended
2026-09-06: each lands at a different altitude, and forcing them into one per-mechanism verdict
asks the question at the wrong granularity.

| concern | where it lives | assessed |
|---|---|---|
| delivery | the mechanism's **moments table** — one row per occasion at which a person acts on it | per row, each carrying its instruction or its kind of none |
| single authorship | `/mechanism`'s injection rule — a rule's only home is its mechanism's rules file | **not assessed** — structural; a hand-written copy is drift, not an opinion |
| listing | the **record contract** — a register declares its own index in its own file | per register, and only mechanisms that accumulate records owe one |

The decisive case against the verdict form is Life's, which tried it and abandoned it: *"Does it
have an instruction file is the wrong question — M03 answered `none` while one of its four moments
was instructed and three were not."* A per-mechanism *delivered: yes* would have passed paired
close on 2026-09-06 — `/maintain` is on the ring and `/ticket` is invoked — while the one moment
that mattered, *a ticket's boxes are checked and it sits in the active folder*, was instructed by
nobody. A moments table would have forced that row to exist on the day it was declared.

## Solution

`/mechanism` owns what a mechanism is, what it is made of, and where each of its parts lives.
`/maintain` applies those rules and re-checks work when they change; it does not own them.

**One mechanism, one instruction file** (the user, 2026-09-06). A mechanism's own instruction file
is one skill. Rules it needs in skills it does not own are **injected pointers**, not second
instruction files. `/maintain` is therefore not a part of any mechanism it maintains: it is the
mechanism for maintaining mechanisms, and it acts on the others from outside.

A mechanism reaches its shape when every moment it has is instructed, or carries a declared kind of
absence. An absence that is a genuine gap names a ticket, never left silent — an undeclared gap is
what the five tickets were.

**Three homes, one axis, no fourth:**

| home | holds | reaches a session |
|---|---|---|
| `AGENTS.md` | meta and strict rules | at start, every session |
| `.agents/skills/<name>/` | the act, and every rule read *in the work it governs* | when the skill is invoked |
| `.agents/mechanisms/<slug>/` | why the instruction is what it is: the mechanism's parts, its moments, its rules' single home | when installing, amending or debugging |

**The cut is *when is this read*, not use-versus-mechanics** — amended 2026-09-06, correcting an
earlier draft of this spec. The shape rules are read while incepting or amending a mechanism, and
that is the work the skill governs, so they live in `/mechanism`'s body and nowhere else. Life
reached the same placement and states it as a rule: *"Meta-rule 10 routes here and states none of
this; this is its only home."* A doc holding rules that govern other mechanisms puts them where
nobody reads them at the moment of use.

**The chain** (the user, 2026-09-06):

> The doc is the instruction's *why*. The evidence is the doc's *why*.

So evidence belongs to a doc, never to an instruction file, and there is one per mechanism. Life
left *may a doc and an instruction file share a sidecar* open and flagged it for its operator; this
chain dissolves the question rather than answering it. It also reclassifies what Life files as a
sidecar: evidence is *why*, so a mechanism's accumulated **records** are not evidence and are
governed by the record contract instead. *Sidecar* is retired as a name here — it says where a
file sits and nothing about what is in it.

This is the cut most of `docs/process.md` is waiting for, and it is not the cut this project
previously assumed — an earlier decision this session sent skill rules to the skill and stopped
there, which leaves no home for why a thing is the way it is.

**Injection.** A mechanism's rules live in one file in its directory, one section per rule, each
naming its target. A generic installer writes delimited, visibly owned blocks into the targets. A
copy in a target is installed, never authored. Injection is mechanical in both directions or it is
not injection: what can be written can be removed, and a hand-edited block is detectable drift
rather than a second opinion.

**Records have a declared shape, and it is enforced.** A mechanism that has records says what a
record is — its fields, what a row means, its tier, and what removes an entry when it is finished
with. This is not optional and does not wait for a record that happens to look structured: a
record with no declared shape is one nothing can check, and *format never content* is exactly the
part a script can hold. A mechanism with no records owes none of this.

**Index.** A register declares its own index in its own file, and the index is derived from the
records on request — never a second copy kept beside them. The index is the reader over the
declared shape, not a separate feature to opt into. The queue is the first: `Status`, `Type`
and `Outcome` stop being transcribed into a table and are read from the ticket headers that own
them. A hand-maintained index is a copy, and this one demonstrably drifted — two rows carried
paraphrased outcomes on 2026-09-06 and were repaired by hand.

**Scope of the first build** — revised 2026-09-06 (the user). Three mechanisms, in order, and the
order is a bootstrap rather than a preference:

1. **`/mechanism`** — the mechanism that decides what counts as one, declared by its own shape.
   Always on: nothing can install or uninstall the thing that defines what installing means, so it
   takes no lifecycle scripts, and that absence is a declared property rather than a gap.
2. **`/maintain`** — declared by *running* `/mechanism`. It is the mechanism for maintaining
   mechanisms, so declaring it second gives the third one a maintainer that has been through the
   shape.
3. **`/ticket`** — whose paired close is the behavior that broke on 2026-09-06 and whose span is
   exactly where it broke.

*Paired close* is a **behavior of `/ticket`**, not a mechanism: it is not a skill, and under one
instruction file per mechanism it cannot be one. The earlier draft named it as the first mechanism
and its span as `/ticket` + `/maintain`; that span was the multi-skill reading this amendment
removes. Nothing is built for a fourth mechanism.

## Impact — 2026-09-06

Assessed on the draft split before minting. Verdict: **narrow**, and the split was revised before
presentation.

Blast radius is `TICKET-FORMAT` in four places rather than one section, `/ticket`'s amend rule,
`/maintain`'s queue-row rule, `docs/process.md`'s pointer, and five session records that cite the
old table as history and keep their facts.

Four findings changed the breakdown:

- **The index has no delivery path here.** [AGENTS.md](../../AGENTS.md) routes every session to the
  queue as the thing that owns current state. Life can leave its table uncommitted because wake
  hooks inject state; this spec puts hooks out of scope. Taking the uncommitted decision on Life's
  precedent imports a constraint we do not share, so the queue slice became decision-bearing rather
  than settled.
- **A declaration slice with no check is horizontal**, and asserting an unverified shape is the
  defect this spec exists to stop. The first slice now ships the check that its own declaration is
  true.
- **The skill allowlist and the absent-artifact dispositions exceed one mechanism**, which is the
  scope this spec set. They moved out of the first build.
- **`Done (split)` was wrong for `01-0017`.** Its work is not split across children; it is
  superseded in framing and survives whole as *apply the shape to the remaining mechanisms*.

The backlog listing was also moved ahead of the queue index: it is the live defect and carries no
delivery question.

## Impact — 2026-09-07

Assessed on the re-slice draft after this spec's amendment, before minting. Verdict: **narrow**,
and the draft was revised on both findings before presentation.

Blast radius is `docs/process.md`'s *Tree maintenance* and *Mechanical maintenance* sections,
`TICKET-FORMAT`'s four queue citations, and `.agents/README.md`, which three consecutive slices
write to.

Two findings changed the split:

- **`/maintain` has no records, so declaring it exercises neither injection nor the record rule.**
  `temporary_statements.py` reads `<temporary>` blocks in place; there is no marks file and nothing
  accumulates. The slice was kept, but its justification was rewritten from *proves the shape
  generalises* to *falsifies it cheaply, before three slices depend on it*, and its record
  obligation is stated as `none` by property rather than deferred.
- **The shape check's dependencies were drawn for the superseded framing.** It was blocked on a
  listing and an index because the three properties needed something to observe. Moments need only
  a declaration, so its blockers narrow to the three declaration slices.

Also surfaced and left alone: `docs/process.md`'s *Autonomy and repair*, *Verification* and
*Mechanisms and skills* belong to mechanisms nobody has declared, and moving them now is the
accretion this spec exists to stop.

## User Stories

1. As a maintainer, I want one stated test for what counts as a mechanism, so that I can tell
   whether a thing I am building needs this shape at all.
2. As a maintainer, I want a mechanism's rules to have exactly one home, so that changing a rule is
   one edit rather than a search.
3. As a maintainer, I want a rule that applies in several skills to be installed into each of them
   from that one home, so that the copies cannot disagree.
4. As a maintainer, I want an installed rule block to be visibly owned and delimited, so that I can
   see at a glance what I may edit and what I may not.
5. As a maintainer, I want to remove an injected rule as mechanically as I added it, so that a
   mechanism can be retracted without hand-hunting its traces.
6. As a maintainer, I want a hand-edited injected block to be reported as drift, so that a local
   fix cannot silently become a second source.
7. As an agent in a session, I want a mechanism's duty delivered at the occasion it governs, so
   that I act on it without having chosen to fetch it.
8. As an agent in a session, I want to ask for a register's index and receive it derived from the
   records, so that what I read cannot be staler than what it describes.
9. As a maintainer, I want the queue's status and outcome read from the tickets, so that the queue
   cannot contradict them.
10. As a maintainer, I want the pacing prose in the queue to stay hand-written, so that judgment
    about where the work stands is not faked by a generator.
11. As an agent, I want to list what a mechanism currently owes — records eligible and not yet
    moved, statements whose condition holds — so that a backlog surfaces without being looked for.
12. As a maintainer, I want a standing backlog held as a ratchet rather than a threshold: silent at
    or below its mark, loud when it rises, lowered freely as it clears, and raised only with a
    stated cause written beside the number.
13. As a maintainer, I want every skill to be named by a mechanism or to sit in an allowlist with
    its reason, so that a rule injected into a skill nothing knows about is reported.
14. As a maintainer, I want a mechanism to name the parts it relies on but does not own, so that a
    shared script has exactly one claimant and an uninstall cannot remove what another mechanism
    needs.
15. As a maintainer, I want a mechanism to list every moment at which a person acts on it and what
    instructs them there, so that a mechanism that has not reached its shape says which occasion is
    uncovered — not whether it is covered overall.
16. As a maintainer, I want an uninstructed moment to name a ticket, so that a declared gap is work
    rather than a permanent excuse.
17. As a maintainer, I want the reason a moment is uninstructed to be distinguishable — instructed
    elsewhere, embedded in the wrong home, deliberately unowned, or genuinely not yet — so that a
    thing that looks like a gap and is not stops being re-investigated.
18. As a maintainer, I want a mechanism's story kept in its evidence file and out of its doc, so
    that the doc says what is true now and the history stays available.
19. As `/maintain`, I want to re-check a mechanism when what governs it has changed, so that a
    governing edit does not leave built work quietly stale.
20. As `/maintain`, I want to apply mechanism rules without owning them, so that a rule has one
    author and one enforcer rather than a skill that is both.
21. As a recipient project, I want a mechanism's rules to travel with `.agents/`, so that an
    installed skill does not depend on documents my project never received.
22. As a recipient project, I want a mechanism to declare what a clean copy takes, so that this
    project's own records do not arrive with it.
23. As a maintainer, I want `docs/process.md` to shed what belongs to a skill or a mechanism, so
    that what remains is process or nothing.
24. As a maintainer, I want a mechanism to name what would retire it, so that a mechanism whose
    worth has ended can be ended.
25. As a maintainer, I want the shape checked mechanically, so that conformance is observed rather
    than asserted.

## Implementation Decisions

- **Membership test.** A mechanism is part of **how the work gets done** — the development method
  and its machinery. What the project produces is not one, however much depends on it. Within that
  subject the test is reliance, not code: does other work depend on this as a source of instruction
  or behavior about how to work? A mechanism is a system, never a file — one spans skills, scripts,
  records and rules injected into skills it did not write. Writing an *entry* into a record is not
  mechanism work; it belongs to the skill that owns the entry.
  **Narrowed 2026-09-07** *(the user)*: the earlier wording — *"does something else depend on this
  as a source of instructions or behavior?"* — was scoped by *reliance, not code* alone, which the
  tier-1 trigger does not carry to the occasion. In a recipient project it would fire on ordinary
  product behavior that other code relies on. The subject is now stated ahead of the test.
- **One instruction file per mechanism** *(the user, 2026-09-06)*. A mechanism's own instruction
  file is one skill. Rules it needs in skills it does not own are injected pointers back to that
  skill, never second instruction files. **Corrected 2026-09-07 on a direct read:** Life's
  `/mechanism` states the opposite — *"usually a skill, and there may be several"* — and its
  register lists several surfaces per mechanism. This is therefore a tightening this project took,
  not a rule Life's practice already separated, and it stands on the user's decision alone. What
  Life does supply is the consequence we adopted: a mechanism reaches skills it does not own by
  **injection**, not by a second instruction file.
- **Moments, each with a kind.** A mechanism's doc lists every moment at which a person acts on it
  and what instructs them there. A moment with no instruction file carries which kind of absence it
  is: *elsewhere* (instructed by another mechanism, which is named), *embedded* (instructed, but
  from the wrong home), *unowned by design*, or *not yet* — the only genuine gap, and it names a
  ticket. The first two are the ones that get misread, and they pull in opposite directions. There
  is no *none needed*: if nobody acts, it is not a moment and the row does not exist.
- **Directory.** `.agents/mechanisms/<slug>/` holds the doc and the rules file. Working parts stay where the harness needs them: skills in `.agents/skills/`, scripts in
  `.agents/scripts/`, tests in `tests/`. `.agents/` is the unit recipient projects receive, so a
  mechanism travels by construction. Filenames repeat the slug.
- **Doc and instruction file are never the same file.** The skill carries the act and every rule
  read in the work it governs; the doc carries why that instruction is what it is; the evidence
  carries why the doc is what it is. Enforced by the shape check, not by convention.
- **The third shape is called evidence, not a sidecar** *(the user, 2026-09-06)*. *Sidecar*
  describes where a file sits and says nothing about what is in it, and this spec used it for six
  sections without ever saying. **Evidence** holds why the doc is what it is: what was tried, what
  was refuted, what it cost, what it used to be. Evolution belongs there. **Provenance does not** —
  the `(the user, 2026-09-06)` on a rule stays inline, because attribution at the moment of reading
  is what makes a rule challengeable, and a name inviting it into the evidence file would license
  moving it out.
- **Evidence belongs to a doc, not to an instruction file.** One per mechanism. A skill's
  `EVIDENCE.md` written before its mechanism was declared is an unsorted mixture, not a second
  evidence file: doc material goes to the doc, the doc's own why to the evidence.
  `.agents/skills/discover/EVIDENCE.md` and `docs/research/maintenance-findings.md` are both in
  that state and are sorted when their mechanisms are declared.
- **Evidence lives in `docs/`, at `docs/mechanisms/<slug>.evidence.md`** *(the user,
  2026-09-06)*. It is the one part of a mechanism that cannot be made instance-neutral — it cites
  this project's tickets, sessions and dates — so shipping it inside `.agents/` would send our
  records into a recipient's tree as dangling links. The decisive fact is who reads one and when:
  evidence is read at *amend* time, and amendment happens at the canonical source, where `docs/`
  is this project's. A recipient receives a mechanism and does not amend one. The doc names its
  evidence from inside a `<project-local>` block, per `AGENTS.md`'s *Core and instance* rule, so
  the chain stays navigable here and is replaced there. Filename carries the slug, so the tie is
  visible without opening the file.
  Refuted rather than weighed: folding the story into the doc. Life measured what that licence
  produces — its two heaviest docs reached 2,644 and 2,059 words of dated narrative before the
  rule was corrected.
- **Rules file.** One section per rule, each naming its **target**, its **anchor** and its
  **tier**. That file is the rule's only home, and a rule states its authority — who may change it,
  at what strength — inline.
- **The injector is one generic core script, never per-mechanism.** It reads any mechanism's rules
  file and writes delimited, visibly owned blocks into the targets. Life built per-mechanism
  installers and reverted: *"M23 shipped with its rule bodies in a per-mechanism `.js` while
  `/mechanism` asserted the doc held them: two homes, and the skill claimed the one that was
  false... Twenty-three bespoke installers would have been a larger corpus than the thing they
  install."* Two details taken whole from that reversal: **there is no default mode** — install and
  retract are not points on a spectrum with an obvious middle, so a bare invocation refuses; and it
  **refuses rather than guesses** on a missing target, a missing anchor, an already-present block,
  or a block whose body has drifted. A partial install reporting success is what this whole
  mechanism exists to make impossible.
- **A record-bearing mechanism has a maintainer script**, carrying the slug in its filename and
  checking its records against their declared shape. **Format never content, live rows only**;
  archived history is exempt. Whether a row should have been written, or is any good, is judgment
  and not the script's. `/maintain` is instructed to run it, and where one is missing, *writing it
  is the maintenance* rather than reading the rows by hand.
- **Every part declares its tier**, and tier is reachability rather than importance or read
  frequency: forced into context mechanically, asked for, or reachable only by someone who already
  knows it exists — the third a diagnosis rather than a tier. Here tier 1 is `AGENTS.md` and every
  skill description, so a skill file spans two tiers, which is the case the heuristic breaks on.
  The placement rule itself is `01-0018`'s.
- **Inception aligns on the mechanism's shape before anything is built.** `/align`, every incepted
  mechanism, no exceptions, opening with what the mechanism is in plain terms. The agenda is its
  moments, its authority, its record shape, its index, the tier of each part, and what retires it.
  A mechanism nobody can describe is one whose doc will describe the wrong thing.
- **Index, and the record shape under it.** A mechanism that has records declares their shape —
  fields, what a row means, its tier, what removes a finished entry — inside the record's own file,
  and that shape is **enforced mechanically rather than left optional for records that happen to
  look unstructured** *(the user, 2026-09-07)*. A renderer derives the index from the records on
  request; the index is the reader over the declared shape, not a feature to opt into. Rendered
  output is not committed — an index kept beside its records is a copy. The queue's table is
  removed; its marker and its pacing prose remain. A mechanism with no records owes none of this,
  and that absence is a property rather than a gap.
- **`TICKET-FORMAT` loses its queue section.** Nothing is copied, so *"Outcome copied verbatim"*,
  the `done/` segment instruction and *"do not add columns"* have nothing to govern. `/ticket` no
  longer amends a table.
- **Ownership of shared parts — the constraint is on the scripts, not on the doc.** A part may be
  claimed by several mechanisms; a system shares parts, and asserting uniqueness fails the tree on
  every legitimate sharing. A doc *should* name a part it relies on but does not own, marked as
  relied-on with its owner. What may not name it is anything that installs, removes or extracts,
  and where that bites, the claimant is the always-on mechanism, because it is the one that cannot
  leave. This harness has no install, uninstall or extract script and none in scope, so ownership
  of `docs_corpus.py` and `tests/harness.py` is **not a live question**: both are declared
  relied-on and named by every doc that leans on them.
- **Allowlist.** A skill or file belonging to no mechanism is listed with its reason. An allowlist
  is how a gap stays declared rather than becoming invisible.
- **Re-check on governing change.** `/maintain` re-checks a mechanism when what governs it has moved
  since the last check. Comparison normalises line endings first, excludes evidence — story
  does not govern, so story cannot go stale — and excludes installed rule blocks, which are policed
  as injection drift rather than as content.
- **`/maintain` applies, `/mechanism` owns.** `/maintain` keeps its own maintenance rules in its own
  body and gains no authority over mechanism rules. The rules it applies are injected into it from
  their home.
- **`/skill-up` is not this.** It governs how a skill's text is written; `/mechanism` governs the
  system and its lifecycle. Both exist. `/skill-up` remains owed by `01-0010.0100`.
- ~~**The register is `.agents/README.md`** *(the user, 2026-09-06)*.~~ **Superseded 2026-09-07 by
  the user: the register is derived, and no file holds it.** The mechanism directories are the
  records; a register is their index; and this spec's own index rule says an index is derived on
  request and never committed beside its records. Committing one would be
  [01-0011.0040](../tickets/01-0011.0040-queue-derived-index.md)'s defect one level up, shipped by
  the slice whose job is to establish the rule against it.
  **The new evidence is Life's own.** Its register is hand-written because it is a *migration
  ledger* — twenty-three mechanisms, roughly four with directories, and rows exist for mechanisms
  that have no folder to walk (`M01 | doc: —`). Life records the writer it declined and the
  condition that reverses the decline: *"roughly half the rows having folders."* This tree has no
  such backlog — every mechanism gets its directory in the slice that declares it — so that
  condition is met at 100% on day one, and the enumeration is `.agents/mechanisms/*/` itself.
  Consequence: `.agents/README.md` keeps loaders, layout and symlink recovery, all of which
  travel, and needs **no `<project-local>` block**. Its install narrative was a copy of the queue
  and the tickets, and its roster a second home to `AGENTS.md`'s `Installed:` line — which is
  deleted in the same pass, the host listing the skill set every session.
- **First build is `/mechanism`, then `/maintain`, then `/ticket`.** `/mechanism` is declared by
  its own shape; `/maintain` is declared by running it; `/ticket` carries paired close, whose rules
  move to one home and are injected into `/maintain`, and whose listing is eligible-but-unarchived
  records. Nothing is generalised until a second mechanism needs the same part.

## Testing Decisions

A good test here asserts external behavior: what a command reports, what a file contains after an
operation, what a refusal refuses. It does not assert how the code is arranged. The existing
`tests/` suite is the prior art — 72 behavioral tests over the maintenance scripts, each building a
real temporary repository through `tests/harness.py` rather than reaching into this one, with
refusals proved to change no byte and no Git index.

Four modules, all to be tested — **agreed with the user 2026-09-06**:

- **The rules installer** — installs a block into a target, removes it, is idempotent, refuses an
  unknown target, refuses a missing anchor, **refuses a bare invocation carrying no mode**, and
  reports a hand-edited block as drift rather than overwriting it. Round-trip is the load-bearing case: what it writes, it removes, leaving the
  target byte-identical to before.
- **The index renderer** — derives fields from records, reflects a record edit on the next render,
  reports a record it cannot parse rather than omitting it silently, and never reads a committed
  copy of its own output.
- **The eligibility lister** — reports records whose work is finished and whose folder does not say
  so; distinguishes eligible from ineligible on the acceptance boxes; holds a ratchet count and is
  silent at or below the mark.
- **A record maintainer** — reports a row that violates its record's declared shape, leaves a
  conforming record byte-identical, and touches no archived history. Format only: it never judges
  whether a row should have been written.
- **The shape check** — reports, per mechanism, every moments row and the kind of absence it
  declares; fails on a doc and instruction file that are the same file; fails on a `not yet` row
  naming no ticket, or naming one that does not exist; fails on a named part that is absent.

Not unit-tested: the mechanism docs themselves, which are prose, and the taxonomy of absences, which
is a judgment the check records rather than derives.

## Out of Scope

Hooks and wake-time delivery: this harness has none, and Tier 1 delivery here means `AGENTS.md`.
Per-mechanism install, uninstall and extract scripts, which Life's own evidence warns against
building per concept before a second one needs them — and which this harness has none of, so the
shared-part ownership rule is stated and not yet enforced. A register as a *separate* artifact,
which is now moot: **no file holds the register at all**, and a renderer derives it from the
mechanism directories on request — see *Implementation Decisions*, amended 2026-09-07. `/edge`
and `docs/edge/`, owned by `01-0010.0100`. The pacer, and `docs/process.md`'s final disposition,
owned by `01-0020`. Migrating every existing mechanism: this spec builds three and states what
the next must prove.

Also out of scope, and surfaced by this spec's own align on 2026-09-06: the references from core
into this project's own documents, which `AGENTS.md`'s *Core and instance* rule makes a violation
rather than an untidiness. Measured that day — `docs/process.md` from `/maintain`, `/implement` and
`/impact`; `docs/architecture.md` from `/maintain`; `docs/research/maintenance-findings.md` from
`/maintain`; and one ticket of this project from `/discover`'s evidence file. A path convention the
harness imposes is not one of these. The repairs belong to their owning tickets, not here.

## Further Notes

The three-home split supersedes an earlier decision taken this session, that rules are either
global-and-strict or skill-specific. That split leaves no home for how a thing works, which is what
most of `docs/process.md` is. It is superseded rather than wrong: `docs/architecture.md` and
`docs/process.md` still cannot hold a distributed skill's rules, and that reasoning stands.

The vocabulary here is deliberate. **Index**, not *digest* or *summary* — a compact list derived
from records on request, never a second home for what a record already says. This matters because a
hand-maintained index looks like an index and behaves like a copy.

`01-0017` was minted earlier on 2026-09-06 as a fifth rule refactor: every skill declares what it
reads and produces, every document names its writers and readers, and the declarations must compose.
That is a slice of this spec, not a sibling of the rule refactors — the same questions a mechanism
doc answers about its own parts. It should be re-parented here or folded in, and `01-0018`'s
dependency chain re-linked accordingly.

The ordering question this spec raises and does not settle: `01-0016` asks which skill owns which
rule, and its own text records that the answer stalled because repair-and-report is applied by
several skills. **Re-counted 2026-09-07, correcting a wrong figure of five taken the day before:**
three skills touch the policy and only **two restate it** — `/verify` and `/maintain`, while
`/implement` names only the `repair` switch and points at `AGENTS.md`, which is correct as it
stands. The earlier count matched `/ticket`, `TICKET-FORMAT` and `/impact` on a different sense of
the word: the mover *repairing citations*. Injection dissolves the stall — one home, one installed
copy — which suggests this work runs before the rule refactors rather than after them.

**Where this amendment's evidence came from.** Life's `/mechanism` skill, its `mechanism-shape`
doc and register, `evidence-sidecars`, `maintenance` (doc and rules file) and `/mechanism`'s
`EVIDENCE.md`, read in full on 2026-09-06 at the user's instruction. Three things this spec had
reasoned to independently and got wrong, and one it had right:

- **The skill/doc split was inverted here.** Corrected above.
- **The absence taxonomy attaches to moments, not to a whole-mechanism verdict.** Life tried the
  verdict form and abandoned it for a stated reason. Corrected above.
- **Indexing is the record contract's, not the shape's.** Life's `register-index.js` records the
  operator asking *why is this a new mechanism?* and the answer — the declaration place already
  existed, so the contract owns only the form of the declaration and the reader, and *"there is
  deliberately no central list of registers."*
- **The queue-index defect is real and larger than measured here.** Life's hand-maintained queue
  index was 41% wrong or unverifiable across 94 tickets: 24 statuses outside the vocabulary, 14
  legal contradictions, 34 of 78 `Outcome` cells differing from the ticket's own field, and one
  ticket with no row. This spec cited two paraphrased rows. Same defect, far more evidence, and it
  strengthens `01-0011.0040` without settling its delivery question.

Two things Life leaves open that this spec now closes on the user's decision: one instruction file
per mechanism, and whether a doc and an instruction file may share a sidecar — closed by the chain
*doc is the instruction's why, evidence is the doc's why*, which makes it not a question.
