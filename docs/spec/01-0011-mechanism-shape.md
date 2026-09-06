# A mechanism has one home for its rules, and a derived index

**Status:** Draft, 2026-09-06. Not accepted. Developed through `/spec` → `/align`; decomposition is
`/ticket`'s.

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

The concept is not missing. [The glossary](../glossary.md) defines **Mechanism** — a behavior on
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
separate them are *delivery* and *listing*. That gives three independent properties, and the day's
failures sort onto them cleanly:

1. **Delivered** — the duty reaches the occasion it governs. The archive duty did not.
2. **Indexed** — the mechanism declares a compact view of its own records, derived from them and
   asked for when a session needs it. Nothing could list eligible-but-unarchived records.
3. **Singly authored** — the rules have exactly one home, and copies are installed rather than
   written. This is what produced the three-skill and four-place restatements.

Failures 1 and 2 lose work. Failure 3 produces drift. They do not substitute for each other, and
injection — the fix for 3 — would not have saved the five tickets.

## Solution

`/mechanism` owns what a mechanism is, what it is made of, and where each of its parts lives.
`/maintain` applies those rules and re-checks work when they change; it does not own them.

A mechanism reaches its shape when all three properties hold. A property that does not hold is
declared as a named gap with a ticket, never left absent — an undeclared gap is what the five
tickets were.

**Three homes, one axis, no fourth:**

| home | holds | reaches a session |
|---|---|---|
| `AGENTS.md` | meta and strict rules | at start, every session |
| `.agents/skills/<name>/` | how to use the thing, at the moment of use | when the skill is invoked |
| `.agents/mechanisms/<slug>/` | how it works: its parts, its moments, its rules' single home | when installing, amending or debugging |

A skill holds *use*; a mechanism doc holds *mechanics*. This is the cut most of `docs/process.md`
is waiting for, and it is not the cut this project previously assumed — an earlier decision this
session sent skill rules to the skill and stopped there, which leaves no home for how a thing works.

**Injection.** A mechanism's rules live in one file in its directory, one section per rule, each
naming its target. A generic installer writes delimited, visibly owned blocks into the targets. A
copy in a target is installed, never authored. Injection is mechanical in both directions or it is
not injection: what can be written can be removed, and a hand-edited block is detectable drift
rather than a second opinion.

**Index.** A register declares its own index in its own file, and the index is derived from the
records on request — never a second copy kept beside them. The queue is the first: `Status`, `Type`
and `Outcome` stop being transcribed into a table and are read from the ticket headers that own
them. A hand-maintained index is a copy, and this one demonstrably drifted — two rows carried
paraphrased outcomes on 2026-09-06 and were repaired by hand.

**Scope of the first build.** One mechanism proves all three properties: **paired close**, which
already spans `/ticket`, `/maintain`, `move_doc.py`, `docs_corpus.py` and five test files, and whose
span is exactly where it broke. The second mechanism is what proves the shape generalises; nothing
is built for a third.

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
15. As a maintainer, I want each of the three properties to carry a state, so that a mechanism that
    has not reached its shape says which part is missing.
16. As a maintainer, I want a missing property to name a ticket, so that a declared gap is work
    rather than a permanent excuse.
17. As a maintainer, I want the reason a property is absent to be distinguishable — instructed
    elsewhere, embedded in the wrong home, deliberately unowned, or genuinely not yet — so that a
    thing that looks like a gap and is not stops being re-investigated.
18. As a maintainer, I want a mechanism's story kept in a sidecar and out of its doc, so that the
    doc says what is true now and the history stays available.
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

- **Membership test.** Reliance, not code: does something else depend on this as a source of
  instructions or behavior? A mechanism is a system, never a file — one spans skills, scripts,
  records and rules injected into skills it did not write. Writing an *entry* into a record is not
  mechanism work; it belongs to the skill that owns the entry.
- **Three properties, each with a state.** Delivered, indexed, singly authored. A property that does
  not hold carries which kind of absence it is and, when it is a genuine gap, the ticket that will
  close it. The taxonomy distinguishes *elsewhere* (instructed by another mechanism, which is named)
  from *embedded* (instructed, but from the wrong home) from *unowned by design* from *not yet*.
  The first two are the ones that get misread, and they pull in opposite directions.
- **Directory.** `.agents/mechanisms/<slug>/` holds the doc, the rules file and the evidence
  sidecar. Working parts stay where the harness needs them: skills in `.agents/skills/`, scripts in
  `.agents/scripts/`, tests in `tests/`. `.agents/` is the unit recipient projects receive, so a
  mechanism travels by construction. Filenames repeat the slug.
- **Doc and instruction file are never the same file.** The doc says how it works; the skill says
  how to use it. Enforced by the shape check, not by convention.
- **Rules file.** One section per rule, each naming its target and anchor. That file is the rule's
  only home. A generic installer reads it; there are no per-mechanism installers holding rule text,
  because that shape puts the rules in two places and makes the doc assert the wrong one.
- **Index.** A register declares its own index inside its own file, naming the shape and the fields.
  A renderer derives it from the records on request. Rendered output is not committed — an index
  kept beside its records is a copy. The queue's table is removed; its marker and its pacing prose
  remain.
- **`TICKET-FORMAT` loses its queue section.** Nothing is copied, so *"Outcome copied verbatim"*,
  the `done/` segment instruction and *"do not add columns"* have nothing to govern. `/ticket` no
  longer amends a table.
- **Ownership of shared parts.** A part may be claimed by several mechanisms; several users, exactly
  one claimant. A doc *should* name a part it relies on but does not own, marked as relied-on with
  its owner. What may not name it is anything that installs, removes or extracts.
- **Allowlist.** A skill or file belonging to no mechanism is listed with its reason. An allowlist
  is how a gap stays declared rather than becoming invisible.
- **Re-check on governing change.** `/maintain` re-checks a mechanism when what governs it has moved
  since the last check. Comparison normalises line endings first, excludes evidence sidecars — story
  does not govern, so story cannot go stale — and excludes installed rule blocks, which are policed
  as injection drift rather than as content.
- **`/maintain` applies, `/mechanism` owns.** `/maintain` keeps its own maintenance rules in its own
  body and gains no authority over mechanism rules. The rules it applies are injected into it from
  their home.
- **`/skill-up` is not this.** It governs how a skill's text is written; `/mechanism` governs the
  system and its lifecycle. Both exist. `/skill-up` remains owed by `01-0010.0100`.
- **First build is paired close only.** Its rules move to one home and are injected into `/ticket`
  and `/maintain`; its index is the queue; its listing is eligible-but-unarchived records. Nothing
  is generalised until a second mechanism needs the same part.

## Testing Decisions

A good test here asserts external behavior: what a command reports, what a file contains after an
operation, what a refusal refuses. It does not assert how the code is arranged. The existing
`tests/` suite is the prior art — 72 behavioral tests over the maintenance scripts, each building a
real temporary repository through `tests/harness.py` rather than reaching into this one, with
refusals proved to change no byte and no Git index.

Four modules, all to be tested — **agreed with the user 2026-09-06**:

- **The rules installer** — installs a block into a target, removes it, is idempotent, refuses an
  unknown target, refuses a missing anchor, and reports a hand-edited block as drift rather than
  overwriting it. Round-trip is the load-bearing case: what it writes, it removes, leaving the
  target byte-identical to before.
- **The index renderer** — derives fields from records, reflects a record edit on the next render,
  reports a record it cannot parse rather than omitting it silently, and never reads a committed
  copy of its own output.
- **The eligibility lister** — reports records whose work is finished and whose folder does not say
  so; distinguishes eligible from ineligible on the acceptance boxes; holds a ratchet count and is
  silent at or below the mark.
- **The shape check** — reports, per mechanism, which of the three properties hold and which gap
  each declares; fails on a doc and instruction file that are the same file; fails on a declared gap
  with no ticket.

Not unit-tested: the mechanism docs themselves, which are prose, and the taxonomy of absences, which
is a judgment the check records rather than derives.

## Out of Scope

Hooks and wake-time delivery: this harness has none, and Tier 1 delivery here means `AGENTS.md`.
Per-mechanism install, uninstall and extract scripts, which Life's own evidence warns against
building per concept before a second one needs them. A mechanism register as a separate artifact —
`.agents/README.md` already lists installs against their authorising slices and is the register in
embryo. `/edge` and `docs/edge/`, owned by `01-0010.0100`. The pacer, and `docs/process.md`'s final
disposition, owned by `01-0020`. Migrating every existing mechanism: this spec builds one and states
what the second must prove.

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
rule, and its own text records that the answer stalled because repair-and-report is applied by three
skills. Injection dissolves that — one home, three installed copies — which suggests this work runs
before the rule refactors rather than after them.
