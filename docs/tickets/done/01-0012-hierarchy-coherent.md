# Hierarchy reads the same everywhere — landed as a decision

- **Status:** Done (2026-09-28, landed as a decision: height is depth in the question structure, and
  the questions are kept by a mechanism, [01-0011.0100](../01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md))
- **Type:** HITL
- **Outcome:** The align this ticket hosted, 2026-09-27 to 2026-09-28, eliminated its minted
  feature — one account of height reconciled across the skills — by finding what height is an
  instance of: depth in a structure of open questions. That structure, and the mechanism that keeps
  it, are [01-0011.0100](../01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md)'s; every
  decision of the align is extracted there, and this record keeps the narrative.

## Parent

[AGENTS.md](../../../AGENTS.md), whose General rules and load-bearing section are where the concept
surfaced, 2026-09-06. Not a child of
[01-0010](../01-0010-a-shared-harness-improves-without-losing-project-conventions.md): that ticket's contract is distributing a
canonical harness across projects, and the coherence of the method's own concepts is a different
contract — the same argument that kept [the pacer](../01-0020-each-turn-knows-its-next-step.md) out of it.

**Closed as a landed decision, 2026-09-28** *(the user)*. The residues went to their owners: the
height vocabulary sweep is a criterion of
[01-0011.0100.0010](01-0011.0100.0010-the-store-and-questions-writes-it.md); *Unit of work —
proposed* is [01-0020](../01-0020-each-turn-knows-its-next-step.md)'s; the entry file's load-bearing threshold and its
wrapped example are [01-0017.0020](../01-0017.0020-practice-swaps-in-one-edit.md)'s. The three
`/discover` passes and the Life trace are research records, pointed at below. The sections that
follow are the align as it ran, kept whole.

## Impact

**2026-09-06.** 33 hierarchy-flavoured statements across 9 files; heaviest in
`ticket/SKILL.md` (12), `docs/glossary.md` (6), `align/SKILL.md` (5). Eight of those nine files also
carry the scope statements owned by [01-0014](../01-0014-scope-reads-the-same-everywhere.md), so the two passes are
sequential, never parallel. Verdict: proceed.

## Why this exists

The project keeps reaching for height under different names and never says what it is. `/ticket`
calls it altitude and granularity; `/plan` and `/align` speak of high-level and resolution;
`AGENTS.md` distinguishes Tier 1 from Tier 2 and load-bearing from local; the glossary carries
scale, coarse and *Unit of work — proposed definition*. None of them defines the axis, so nothing
can be checked against it and each site is free to mean something slightly different.

The user's formulation, 2026-09-06: **hierarchy is from what heights we look at things.**

**What it is for** *(the user, 2026-09-27, at this ticket's align)*: steering, not a taxonomy.
Know at what height a pass or a conversation is speaking; notice when a topic narrows or rises;
redirect it to the home of that height, or at least name the shift; and use the heights to see
where a unit of work has a gap — because a gap in height that nobody names is one nobody amends.
Two specimens from the align itself, the same day: a ticket minted with no statement of the
problem it answers is a gap at the top height, and this ticket was one; and a discovery pass
whose result came back as one sheet mixing every height is a shift that landed without a shape,
so its gaps cannot be read off it. Whether a discovery or an impact pass is itself a shift in
height is not settled; what is settled is that a pass which moves height must return an outcome
robust enough to read the structure and its gaps from, not a flood of prose. The earlier
"retire" recommendation of this align, made on the necessity gate before this purpose was
stated, is withdrawn.

**What a gap is, and is not** *(the user, 2026-09-27)*: a gap is work that was supposed to be
done at a height and was not, because the discussion shifted to another height. A ticket minted
with no statement of its problem is not a gap but something dislocated — a thing missing from,
or sitting at, the wrong height — and the two are kept apart. *Dislocated* is a candidate word,
not yet a term.

**The heights are not the loop's steps** *(the user, 2026-09-27)*: folding intent and behaviour
into "inception" collapsed two heights into one step and dropped the second. Four heights, each
a question a unit of work answers: **intent** — what is wanted, and why; **strategy** — which way
we go, the chosen approach and its boundaries; **behaviour** — what is observably true when it
is done; **action** — the concrete steps that make it true. A step of the loop may speak at
several. The specimen, this align on 2026-09-27: opened at strategy (*how is it enforced?*),
answered at action (a glossary entry and a script), pulled back to strategy (*no method's
artifact in the definition*), down to action (the level names), up to intent by `/discover` and
further by *what is the point at all?* — leaving the enforcement question at strategy unsettled
and the levels half-done, with nothing recording either, so nothing would have brought the work
back to them.

**The two directions are not alike** *(the user, 2026-09-27)*: moving down before the current
height is settled leaves the picture above incomplete — that is the gap. Moving up restructures
the lower heights rather than leaving them, because the descent happens again anyway: the loop
itself descends, `/align` → `/plan` → `/implement` → `/verify`. Checked against the tree: every
step routes a rising decision to `/align`, so ascent has a home; nothing says when a step may
descend, and the recorded descent is this align answering a strategy question at action. Two
qualifications, held: ascent is safe only while the descent
returns, so the rule keeps the return rather than merely permitting the rise; and ascent's own
failure is unbounded rising, which `/discover`'s *stop where no further grounds appear* already
guards. Parking the lower heights' leftovers on ascent would preserve work the higher answer
invalidated, so what is written at a shift is the unsettled *higher* question, on descent.

**The counter-case, from Life** *(the user pointed at it, 2026-09-27; read from
`D:\Dev\AI\life`, its ticket 0028 *reasoning-failure-class*, ticket 0027, session 0050)*. Life
records the opposite error: *a compound term treated as atomic* — *a shape conceived and then
acted on without being expanded, when expanding is cheap and would have produced a different
shape*. Its worked case: one word, *the scan*, covered two acts, and an argument built on the
unexpanded word chose a wake hook wrongly; the operator's correction was to split the word. The
remedy Life names: *expand before acting*, *instantiate before asserting* — every one of its
specimens was caught by making the thing concrete, none by thinking harder about the sentence.
So a descent is often required to decide rightly above. **Our own tree holds the same error**:
[rule failure 11](../../rule-failures.md) was `/plan` treating *architecture* as atomic — any
sentence in the architecture doc counted — and acting on it without expanding it into the
load-bearing test; it is not a descent, as this record said before this correction.

**So the rule is not about direction but about where the commitment lands** *(this align,
2026-09-27)*: go down to look, decide at the height the question was asked, and return there. An
expansion is a descent that comes back with what it found; a premature commitment is a descent
that stays. The harness already has the shape of a controlled descent — a nested pass with an
output contract that hands back to its caller, `/impact` and `/discover` — and
[rule failure 8](../../rule-failures.md), *a nested skill's output contract ended its caller's
turn*, is what a broken return looks like. No descent needs blocking; the return needs
protecting, and naming what a descent serves before taking it is what protects it.

**A principle and a procedure, kept apart** *(the user, 2026-09-27)*: the general rule — decide
at the height asked; rising is free; going down commits nothing below until above is settled —
is a principle, read at tier 1 and applied by judgement, and it names no moment and no output,
so on its own it misses. It is kept, and at the moments where the failure happens the procedure
is enforced as an instruction with a defined output, the way a mechanism's moments table does.
The moments, from this day's evidence and the tree: `/align` answering a question (the reply's
first line names the height, or the shift; an answer below is named *to decide X* and returns);
`/align` when the user shifts height (on a descent, the unsettled question above is written into
the ticket's *Open issues* before answering below); `/align` before landing a decision on a term
(expand it first — Life's *expand before acting*, our rule failure 11); a nested pass returning
(its material into the caller's record, the caller's turn continuing — instructed for `/impact`
since rule failure 8); `/conclude` (the continuation names the height the work stands at and
what is unsettled above it); `/plan` writing the RFC (already enforced: the decision lands in
the docs first, load-bearing architecture only). The procedure exists at `/plan` and
`/implement` and is missing at `/align` and `/conclude`, where the day's gaps formed.

**The moment is the turn, and it needs a state and an observer** *(the user, 2026-09-27)*. If
the rule holds for every discussion and for the agent's autonomous work alike, its owner is the
pacer, [01-0020](../01-0020-each-turn-knows-its-next-step.md), whose outcome is what a turn's reply is scoped to. The
moments above were vague because two parts were missing. *State*: the current height must be
declared constantly and held, or there is nothing to compare against. *An observer outside the
generator*: the agent cannot watch its own tokens as it produces them, so a shift is detected only
by something reading the message once it exists — the user, the main session judging a
subagent's draft, or a judge model. With both, a shift is **observed height ≠ declared height**,
and its output is defined: name it; on a descent, write the unsettled question above into the
session's live state — the resume state the pacer already owes — or the ticket's *Open issues*
when it is that ticket's; set the new height. *Before landing a decision on a term* is not a
moment, since it has no manifestation before the tokens; it stays Life's principle, and the
checkable event is the write of a decision, with the expansion beside it, caught after by
`/verify`.

**Jev as the observer** *(the user, 2026-09-27; read from
[typesafe.ai](https://typesafe.ai/blog/introducing-system-one-models-and-jev))*: a "System One
model" — text in, a value from a schema declared in advance out, with a calibrated confidence,
70–500 ms, API-only early access. It fits the observer slot: schema the four heights, input the
message and the declared height, output the observed height and whether it shifted. What it needs
from this ticket is height definitions crisp enough to be a schema; what it depends on is an
external service and a place to run and speak from —
[01-0010.0120](../01-0010.0120-what-each-host-says-without-being-asked.md)'s question. The moments still have to be
defined for it to judge them.

**An optional judge in the turn** *(the user, 2026-09-27; the pipeline as this align read it
back, unconfirmed in its parts)*. A mechanism that can be switched off to conserve tokens and
configured to judge through Jev, for those with access, or through a subagent, the pricier
alternative; both are to be available eventually. The turn, with the judge in it: **1.** the judge
reads the request against the declared height — observed height, shift or none, confidence;
**2.** on a shift the main names it, and on a descent writes a *marker* — *topic T at height H did
not land* — into the live state, then sets the new height; **3.** the main drafts at the declared
height; **4.** the judge reads the draft — its observed height, and whether it commits below an
unlanded height; **5.** the main emits a clean draft, emits an expansion with its naming, or
revises a premature commitment; **6.** a marker clears when that height's discussion lands in a
written decision, and unlanded markers are carried into the continuation at `/conclude`. **The
marker is the material outcome**: it records not the gap, which cannot be known until that height
is revisited, but that a height was left without landing — so *we started high, drilled down and
forgot we were ever high* cannot happen silently. Settled by structure: the judge and the emitter
cannot be one process, so the main drafts and emits and the judge — Jev or a subagent, never the
main — observes both request and draft; the height is set by the judge from the request, never
self-declared; the judge reads the markers, since without knowing whether the height above has
landed it cannot tell an expansion from a premature commitment. *Split* is read as the existing
nested-pass shape, a descent with its own contract that returns to its caller. Configuration:
judge = `jev` | `agent` | `off`, in the local file — *agent*, since the judge may be the main
model or a subagent *(the user, 2026-09-28)*. Depends on height definitions crisp enough
to be the judge's schema, the pacer's turn and resume state, and `.0120` for where the judge runs
and speaks.

**Two mechanisms behind one judge call, and the draft judge dropped** *(the user, 2026-09-27)*.
The model answers at the request's height on its own; judging the draft for height is not the
need. The day's one answer-side descent — a strategy question answered with a glossary entry and
a script — reads as a missing *expansion*: machinery reached for before the shape was
deliberated, which `/align`'s *problem before machinery* already names. Kept as the assumption's
test: answer-side descents recurring once expansion is in place are the evidence to revisit.
What is missing on the answer side is **detecting that a shape needs expanding before it is
answered** — hidden complexity, Life's *expand before acting*. The deliberations exist,
`/impact` and `/discover`, named in the entry file for hidden complexity; the trigger that says
*this turn needs one* does not, and raw models are conservative about calling tools mid-turn, so
the trigger wants a judge. That is a different mechanism from height steering, though both sit in
the turn. Gating emission through a tool definition would enforce the reply mechanically; whether
a host allows it is `.0120`'s finding.

**Two judges on two inputs, and what steering is** *(the user, 2026-09-28, correcting this
record's "one judge call")*. The **steering judge reads the request** — the user's message or the
autonomous trigger — for its height against the declared one, the shift, and whether a descent
expands a higher shape. The **expansion judge reads the draft** — the model's own answer — for a
shape whose hidden complexity, expanded, would change the answer; a generic hidden-complexity
prompt, nothing height-specific. So the draft is judged after all, for expansion and never for
height. The two share only plumbing — the Jev client or subagent harness, and the switch.
*Steer or emit* is about the user's descent: **premature** — the height above has not landed and
nothing in the message expands a higher shape — is steered back: name the shift, name what is
unlanded above, ask whether to land it first; **worthwhile** — the user saw hidden complexity in
the higher shape — is followed: the marker is written first, *the height above is incomplete*,
then the answer goes below. The turn: steering judge on the request; ascent named and height set,
premature descent steered, worthwhile descent marked and followed; draft at the height; expansion
judge on the draft, and if flagged, expand and redraft; emit; markers clear on a written decision
and are carried at `/conclude`. Two tickets: this one keeps height steering — the steering judge,
the markers, steer-or-follow, the height definitions as a schema; expansion detection is its own,
supplying the trigger `/impact` and `/discover` lack — through `/ticket` and `/impact`, not
minted here.

**The mechanics in this framework** *(2026-09-28, correcting this record's "judge ≠ emitter" to
judge ≠ generator)*. The main's reply reaches the chat as it is written — no hold-back — so a
reply judged after emission shows the reader draft and correction both, which is what a Stop hook
would produce. What never reaches the chat: a tool result, and a file the main writes. So a draft
held in a subagent's report or a scratch file can be judged and replaced before anything is
emitted, and the main can be the judge of a subagent's draft and the emitter of the final reply
*(the user's configuration)*. A subagent starts without the conversation; the Agent tool refers to
a `fork` type that inherits it, not among this session's listed types — to check at
implementation. The turn, in that configuration: **1** the main calls the steering judge on the
request with the declared height — a Jev script or a subagent — for height, shift, whether a
descent expands a higher shape, confidence (later a `UserPromptSubmit` hook, `.0120`'s); **2**
ascent sets the height; a premature descent makes the reply the steer — *this leaves H unlanded:
X; land it, or go down?* — and ends the turn; a worthwhile descent writes the marker, sets the
height, continues; **3** the main spawns the drafting subagent at height H, the draft returning as
a tool result; **4** the main, or Jev, judges the draft for hidden complexity; **5** if flagged,
expand and redraft; **6** the main emits the final reply, the draft as-is or transformed, opening
with its height — the only text that reaches the chat besides a steer; **7** a written decision
clears its marker, `/conclude` carries the rest. The alternative, the main drafting to a scratch
file the judge reads, keeps full context and needs no fork, and generates the reply twice. Either
way about twice the reply's output plus the judge; Jev makes the judge negligible, a subagent
judge is a whole agent call, hence `off`. Of this, **steps 1, 2 and 7 are this ticket's**; 3–6
and the draft-pipeline choice are the expansion ticket's.

**What is written at a worthwhile descent** *(the user, 2026-09-28: *emit* meant *write*)*: not
a bare marker that height H did not land, but the height being left, written as a **semi-formed
decision** — what is settled there, which way it leaned, what is still open — to a home robust
enough to be read back from and resumed. The marker rows above are read as this. Its home is the
resume state the pacer owes; until that exists, the ticket's *Open issues* when the discussion is
a ticket's — the section already defined as what is unresolved and why it cannot be answered yet
— and the session's *Continuation* otherwise. A written decision at that height, when the
discussion returns and lands, replaces it.

**Two kinds of height were running together** *(the user, 2026-09-28)*: the harness's own
opinionated, fixed heights — the shapes a method assigns its document kinds: load-bearing, spec,
ticket, RFC, with the ticket muddy, since one may become a spec, an RFC or several tickets — and
the dynamic height of a conversation, relative and moving turn by turn. The four names proposed
above were pinned to neither cleanly; the first discover pass had flagged this (its points 3 and
9). The definition is open, and a second `/discover` is run on the shape as it now stands, fed
none of the first pass's output.

## What to build

*(As it stood at the close, 2026-09-28, before the work moved to
[01-0011.0100](../01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md) and its slices; kept
as the record of what this align arrived at.)*

- **The `questions` mechanism, declared to the shape**: its skill, doc, rules file, the store's
  format in the skill, a maintainer for the store, a check written before the thing and run over
  the prior corpus — every open concern, *Open issues* row and straw dog in the tree.
- **The store**: every open question written, with two relations kept distinct — *part of* (AND/OR
  decomposition) and *depends on* (cannot be asked until) — and a state; identity apart from
  structure. Its unit is an *issue*, resolved by a decision; a ticket stays a *goal*, satisfied by
  evidence, and links to the issues it owns.
- **The state**: the current question and its path, set by a judge from the request, read at every
  turn.
- **Closure by recorded kind**: decided, pruned as wrong, merged, deferred with a default for
  acting meanwhile, moot, superseded. Core records the kind; the method says which count.
- **Four judgements as moments with defined outputs**: attach (which open question a message
  addresses, opens, or neither), close, expand (a shape hiding children), prune. Judge = `jev` |
  `agent` | `off`, in the local file; the unasked hook is `.0120`'s.
- **Link maintenance**: a child goes *suspect* when its parent's answer changes, until cleared —
  `.0060`'s marks applied to links.
- **The method's instruments injected**, from each method mechanism's rules file: how to branch,
  dive, close, what counts as evidence, what to discard, what counts as complexity.
- **`/align` adopts it first**, walking and writing the store; the coherence tickets refactor
  onto it; nothing else breaks meanwhile.
- **What folds in**: `concerns.md`, tickets' *Open issues*, straw dogs, the written height — each
  already doing one part right, each becoming a view or an entry of the store.
- **Records small, formalised incrementally, with derived views** — capture cost is the one
  well-evidenced failure of the idea, and ceremony the adoption panel's first blocker.
- **Height, as the ticket was minted** *(2026-09-06)*: one account, with height derived as depth
  in the question structure rather than classified; every statement about height across the entry
  file, glossary and skills — 33 on 2026-09-06, heaviest in `/ticket`, the glossary and `/align`
  — restated as a pointer, corrected, or kept with its reason; *Unit of work* and *Load-bearing
  seam* promoted from "proposed" or retired; the entry file's load-bearing threshold ("several")
  named, and its domain-specific example, kept for now *(the user, 2026-09-06)*, wrapped on this
  ticket. Tier 1/Tier 2 is not a height: the glossary already defines tier as reachability.

## Decisions this ticket's align owned

None remain here. The mechanism's own — record shape, moments, tiers, retirement, question
identity — are [01-0011.0100](../01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md)'s; the
queue order is put to the user at `/ticket`.

## Discover — 2026-09-27

The first `/discover` pass, on the candidate *intent → behaviour → action*: moved verbatim to
[docs/research/discover-height-2026-09-27.md](../../research/discover-height-2026-09-27.md) on 2026-09-28.

## The unit is the open question, and the ticketing is the same tree — 2026-09-28

**Reframed** *(this align, on the second pass's convergence; the user, extending it)*: the unit
tracked is not a height but an **open question** that serves a parent question; height is depth in
that tree, derived and never classified; a shift is a message attaching to a different open
question — an ancestor, a new child, or none; a warranted descent is a child whose closing
advances its parent; the record is the open questions with their parent links, and the
semi-formed decision is the parent's entry; the fixed heights of a method's document kinds are its
*plan* of questions each kind must answer, coupled to the dynamic stack by accommodation. **What
follows** *(the user, 2026-09-28)*: the ticketing system is this tree — a spec a question, its
tickets the children that serve it, an RFC the child *how*, *Open issues* open questions, *Decided*
a question closed, *done* every question answered, the parent link the dominance link — or is
what the project has been circling. What obscures it is that the ticket record carries the
question tree and a method's bookkeeping — ids, statuses, folders, RFC naming — in one, which
[01-0017.0020](../01-0017.0020-practice-swaps-in-one-edit.md) already marks for separation; a
ticket is muddy because a question may grow a spec, an RFC or children, which is the tree growing.
A third `/discover`, on the open-question concept itself, follows.

## A question mechanism at the core — proposed 2026-09-28

**The user's proposal**, on the third pass: redesign the core align driver on the open-question
concept — a mechanism that manages the question DAG with rules, judges and strict recordings.
The analogy as stated: open with a broad question; split it into subquestions, which is what
`/align` does; register them by writing, never by carried session text; dive into a branch, which
splits again; the harness knows where in the DAG the work stands; a question may prove wrong and
is pruned; one question may be reached from several branches; open issues, concerns and the rest
are wrapped under this one structure first. The *method* defines instruments over questions —
how to branch, how to dive, how to close, what to collect evidence about, how to discard or
obsolete, when to steer or expand and what counts as complexity — while the generic core drives
the starting question, the turn's current question or set, the store and its maintenance, and
steering, with the method's instruments injected. The judges remain: to detect the question, the
steering, the shapes that need subquestions. Not a patch of existing structures with aspects of a
DAG: a clear question-DAG mechanism first, built separately, adopted in `/align` first, breaking
nothing, with other mechanisms refactored onto it.

**Filled by this align, pending the user's confirmation.** `/align`'s own text already describes
it in prose with no record behind it — *walk down each branch of the design tree, resolving
dependencies between decisions one-by-one* — and its concerns rules are a question store with
closure by relocation: stable ids, a settled concern moving out to its owning home, never resolved
in place. The parts: a **store**, every open question written, one record kind with its format in
the mechanism's skill, identity apart from structure; **two relations**, *part of* (AND/OR
decomposition) and *depends on* (cannot be asked until), kept distinct as project practice keeps
decomposition and dependence — the second is what makes it a DAG; the **state**, the current
question and its path, set by the judge from the request; the **unit**, an *issue* resolved by a
decision, tickets staying *goals* satisfied by evidence and linking to the issues they own;
**closure kinds** — decided, pruned as wrong, merged, deferred with a default for acting meanwhile,
moot, superseded — core recording the kind, the method saying which count; **four judgements** as
moments with defined outputs — attach, close, expand, prune; **link maintenance**, a child going
*suspect* when its parent's answer changes, `.0060`'s marks applied to links; the **instruments
injected** from each method mechanism's rules file, the existing shape; and **what folds in** —
`concerns.md`, tickets' *Open issues*, straw dogs (a landed decision with an open child bound to a
ticket, Rust's unresolved questions exactly), the written height. Pushed: capture cost is the one
well-evidenced failure of the idea (gIBIS, Compendium: structuring costs the author at the wrong
moment, pays a later reader) and ceremony is the adoption panel's first blocker, so records stay
strict but small, formalised incrementally, with derived views; fragmentation, so the align's
one-question-at-a-time stays and the DAG records what it settles; no controlled evidence anywhere,
so the need rests on this tree's own record — the day's gaps, rule failures 11 and 14, Life's
zero self-caught specimens; and scope — built separately, adopted in `/align` first, the
coherence tickets refactored onto it, which is a queue-order occasion for `/ticket`. The way in
is `/mechanism`'s *Incept*: this align on moments, authority, record shape, index, tier, what
retires it; then doc and rules file; the check before the thing; the run over the prior corpus,
which exists — every open concern, *Open issues* row and straw dog.

## Impact — 2026-09-28, the inception

Run at this align on the `questions` mechanism as filled above. **Must change**: `/align`, the
first client; a new mechanism directory, skill, store format in the skill, maintainer, tests, and
a painted door for the store; the ticket mechanism's *Open issues* becoming a view or pointer and
P7 reworded against the store; `concerns.md` (3 entries, read by seven core files); the 82 straw
dogs, each an open question bound to a ticket, their listing becoming a view; `/recall` and
`/conclude`, which read and write the open questions; the glossary's *Open issue*, whose clause
*its current owning record holds it* is the thing replaced; the written height and the expansion
judge, which become store entries and the *expand* moment. **Must verify**: the checks with a new
door and a changed *Open issues* rule; and a reconciliation test — the three stores today and the
store tomorrow hold the same set. **May simplify**: the concerns' stable ids and relocation and the
straw dogs' binding and expiry are two implementations of one thing; the pacer's resume state is
the store's current question and path. **Hidden edges**: `/align` undeclared as the mechanism's
main client; the store's questions the instance's and its format and judges core's, with a
recipient's method having no mechanism to inject instruments from; a per-turn judge is not a
verification-set check and is called by rule until `.0120`; question identity across rewording
undecided, the suspect-link rule flooding on prose; capture cost on the agent and ceremony on the
user; the issue–goal link as a new seam where 01-0017.0020's one-maintainer issue sits. **Leave
alone**: the ticket record as a goal, the `<straw-dog>` syntax, `.0060`'s marks, the rule-failures
register and 01-0019, the releases and arrival work. **Recommendation**: proceed, narrowed to a
first slice — the store, its format and maintainer, the *attach* and *close* moments, `/align`
writing it, `concerns.md` folded in, judge `off` by default — with *Open issues* and the straw dogs
folding in second slices each with a reconciliation test, *expand* and *prune* waiting on the
expansion ticket and an identity rule; two decisions first: whether `/align` is declared with this,
and the identity threshold. The second concrete shape justifying the abstraction exists:
`concerns.md` and the straw dogs are two materially different open-question stores.

**`/align` carries the interview and nothing else** *(the user, 2026-09-28)*: everything else in
its body is another mechanism's, installed from its rules file or wrapped as a straw dog until
that mechanism exists. Stays: the necessity gate, problem before machinery, the interview one
question at a time with recommendation and alternatives, facts looked up and decisions asked,
the decisive fact, the shared assumption, sharpening language, scenarios, cross-reference with
code, no enacting before confirmation. Becomes this mechanism's: the concerns rules, rewritten to
the store. Installed from ticket: decomposing is `/ticket`'s with `/impact`, and recording
resolutions in the owning ticket, beside P7 and P10. Straw dogs: the glossary challenge and inline
update and `GLOSSARY-FORMAT.md` on [01-0017.0010](../01-0017.0010-terms-defined-before-they-land.md);
good architecture, domain awareness, checking ADRs, updating architecture inline, offering ADRs,
`ARCH-FORMAT.md` and `ADR-FORMAT.md` on [01-0017.0020](../01-0017.0020-practice-swaps-in-one-edit.md);
the edge challenge and `EDGE-FORMAT.md` on [01-0010.0100](../01-0010.0100-the-remaining-named-corpus-arrives.md).
**This align's reading, pending the user**: `/align` stripped to its act — open a question, split
it, walk the branches with the user, close each by a recorded decision — is the act of the
`questions` mechanism, so `/align` is its instruction file; a separate `align` mechanism would
have the same act under another name, the sign the gate warns about. That resolves the impact's
first hidden edge: `/align` is declared by this inception.

## Discover, third pass — the open question, 2026-09-28

The third `/discover` pass, on the open question as the unit of deliberation and of work: filed
whole in [docs/research/discover-open-questions-2026-09-28.md](../../research/discover-open-questions-2026-09-28.md).

## What the judge loop is — Life's reasoning failures, 2026-09-28

The trace of Life's reasoning failures, and this align's reading of it: moved verbatim to
[docs/research/life-reasoning-failures-2026-09-28.md](../../research/life-reasoning-failures-2026-09-28.md)
on 2026-09-28.

## Discover, second pass — 2026-09-28

The second `/discover` pass, on the dynamic level of a conversation against the fixed levels of a
method's document kinds: moved verbatim to
[docs/research/discover-conversation-level-2026-09-28.md](../../research/discover-conversation-level-2026-09-28.md)
on 2026-09-28.

## Acceptance criteria

*(Rewritten at the close to the landed decision, the one case the format admits a ticket closing
without becoming an implementation ticket.)*

- [x] The decision is landed in its durable home: height is depth in the question structure, and
  the mechanism that keeps the questions is
  [01-0011.0100](../01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md), with every decision
  of this align extracted there under *Decisions landed at 01-0012's align* *(2026-09-28)*.
- [x] The three `/discover` passes and the Life trace are research records, verbatim
  *(2026-09-28)*.
- [x] Each residue of the minted scope has an owner: the vocabulary sweep, *Unit of work*, the
  load-bearing threshold and the wrapped example *(2026-09-28)*.
- [x] `/verify`, as the reconciliation of a landed decision: every dated decision in this record
  maps to an item of the parent's list or a research record, checked at the close
  *(2026-09-28)*.

## Out of scope

Everything this align arrived at —
[01-0011.0100](../01-0011.0100-the-open-questions-are-kept-by-a-mechanism.md) and its slices.

