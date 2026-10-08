# Discover — the fixed root questions of a project's store, 2026-10-09

One /discover pass for [q-0001.0022](../questions/q-0001.0022-which-root-questions-does-every-projects-store-stand-on-from-its-first-install.md),
a general-purpose subagent told not to read the repository, answering from its own knowledge with
no web search. Filed as it came back.

**What the tasking transmitted:** the store described functionally (a tree of questions, a
position, closure, re-examination below a changed answer); the user's draft of three roots in
their words — why the project needs to exist (product), how it is built and where it is developing
(technical), what else it could be, who its neighbours are, "what is this project?" (research);
that the set itself may be wrong; four example missing roots (who it is for, what it must never
do, how we know it works, what it costs), which the pass names as priming.

---

**Key:** [P] principle — still cited or not; [E] evidence — recency, on what; confidence H/M/L.

## Families

The shape's parts below: (a) fixed roots, (b) parent/child decomposition, (c) a positioned
current question, (d) closure by answer, (e) a closed answer flagging what lies below for
re-examination.

### 1. Aristotle's four causes (explanatory schema)
- **Mapping.** (a) = the four "because" questions you can ask of any made thing — final (what it
  is for), formal (what it is), material (what it is made of), efficient (what makes it, how).
  (b) = sub-explanations within a cause; (d) = an explanation accepted; (e) = a change in one cause,
  e.g. purpose, forces re-explanation of the others (for artifacts, form follows function). **H**
- **Where the triad sits.** It covers three of the four, one mislabelled: "why exist" = final;
  "how built" = material + efficient fused; "what is it really" = formal — but the draft files it
  as exploration. The schema has no ladder; completeness is against the four. **H**
- **Failure modes.** Final causes read as mysterious purposes ("teleology"), which early modern
  science dropped; for artifacts, formal and final tend to collapse into each other — which
  predicts roots 1 and 3 will blur. [P, still cited in philosophy of technology and design theory,
  rarely in software practice] **H/M**
- **Proposed roots.** "What is it for?", "What is it?", "What is it made of?", "How does it come
  to be?" **H**

### 2. Artifact as interface (Simon 1969; Zave & Jackson's world, machine and requirement)
- **Mapping.** (a) = purpose, inner environment (the artifact's own make-up), outer environment
  (the surroundings it operates in) — almost one for one with the draft. Zave & Jackson (1997)
  restate it as: a machine specification S, together with world assumptions W, must produce the
  requirement R. (d) = that argument holds; (e) = a broken world assumption reopens both the
  requirement and the specification. **H**
- **Where the triad sits.** A near-copy, with two errors. Root 3 should be the outer environment —
  neighbours, dependencies, what the project assumes about the world — instead of "what is it
  really", which in Simon is not a root but the *fit* between the other three. And the three are
  not parallel topics but are joined by one argument, which the draft drops. **M/H**
- **Failure modes.** Requirements quietly taking on implementation ("implementation bias"); wrong
  world assumptions — Jackson's example (1995) is the 1993 Lufthansa landing at Warsaw, whose
  braking logic took spinning wheels to mean the plane was on the ground; unstated assumptions are
  the classic failure. [P, heavily cited in requirements-engineering teaching] **H** [E: case
  studies, 1990s; no controlled studies of root-set use] **M**
- **Proposed roots.** "What must be true in the world?", "What is the machine?", "What does it
  assume about its surroundings?" **H**

### 3. Interrogative grids (classical "circumstances"; 5W1H; Zachman 1987)
- **Mapping.** (a) = the question words who, what, when, where, why, how; (b) = in Zachman, each
  question word crossed with a viewpoint (planner, owner, designer, builder…), giving a grid;
  (d) = a cell filled; (e) = no native mechanism. **H**
- **Where the triad sits.** Three of the six — why, how/where, what — with who and when missing.
  Zachman's lesson: the roots form a *matrix*, question word × viewpoint, not a list; a tree has
  to pick one axis, and the draft quietly picks a mixed one. **H**
- **Failure modes.** A taxonomy, not a method; cells filled to look complete, artefacts unused.
  [P, still cited in enterprise architecture, fading] [E: practitioner reports of this
  documentation overhead, 2000s–2010s] **M**
- **Proposed roots.** The six question words, possibly crossed with viewpoints. **H**

### 4. Stasis theory (Hermagoras, Cicero, Quintilian)
- **Mapping.** (a) = four ordered issues any dispute settles on — conjecture (is it so?),
  definition (what is it?), quality (is it good, justified?), jurisdiction (is this the right
  forum, who decides?); (b) = sub-disputes within each; (c) = the stasis a debate currently sits
  at; (e) = reopening a lower stasis invalidates the higher ones — exactly the shape's "closed
  answer flags what lies below". **H/M**
- **Where the triad sits.** "Why exist" = quality; "what is it really" = definition; "how built /
  where developing" = conjecture, the facts. Jurisdiction — governance, who may close a question —
  is missing, and the draft loses the dependency order. **M**
- **Failure modes.** Arguing at the wrong stasis, e.g. debating worth before the facts are agreed.
  [P, still taught in rhetoric and composition, alive in legal reasoning] **H**
- **Proposed roots.** "What is the case?", "What is it?", "Is it worth it?", "Who decides?" **M**

### 5. Issue-based design rationale (IBIS, Kunz & Rittel 1970; QOC; dialogue mapping; wicked problems)
- **Mapping.** (a) = the root issue; (b) = issues, positions, arguments; (c) = the issue under
  discussion; (d) = a position chosen; (e) = the issue reopened. **H**
- **Where the triad sits.** IBIS has *one* root issue. Its natural fixed set is Rittel's *issue
  types* — kinds of question, not topics: factual, deontic (what ought to be), explanatory,
  instrumental (how to), conceptual. Against these the draft reads product = deontic, technical =
  instrumental + factual, root 3 = conceptual. **M**
- **Failure modes.** Wicked problems have no definitive formulation (Rittel & Webber 1973):
  formulating the problem *is* the problem, so fixing roots in advance goes against the family's
  founding claim. [P, very much cited] **H** Capturing rationale costs the writers while the
  benefit goes to later readers; maps go stale and are abandoned. [E: Conklin & Begeman gIBIS
  1988; Buckingham Shum & Hammond 1994; 1990s design-rationale field studies] **M/H** The recent
  success of small architecture decision records (Nygard 2011 onward) is consistent with "keep each
  record small and local". [E: 2020s practitioner and mining studies] **M/L**
- **Proposed roots.** One root issue, or roots by issue type rather than by department. **M**

### 6. Erotetic logic and the logic of inquiry (Wiśniewski 2013; Hintikka; Collingwood 1939–40; Dewey 1938)
- **Mapping.** Wiśniewski's erotetic search scenarios are almost literally the shape: (a) = the
  *principal question*; (b) = the auxiliary questions it implies; (d) = answers obtained; (e) = an
  answer cancelling a presupposition removes the questions resting on it. **M/H**
- **Where the triad sits.** Three roots with no parent means the principal question they jointly
  serve is unstated. Collingwood: the deepest layer is not questions but "absolute
  presuppositions", never answered, only held — fixed roots are presuppositions dressed as
  questions. Dewey: working out the problem is the first stage of inquiry, and fixing roots skips
  it. **M**
- **Failure modes.** Questions on false presuppositions (the "have you stopped…" kind); strategy
  fixed too early. [P, cited in logic and philosophy, little used in practice] **M**
- **Proposed roots.** One stated principal question (e.g. "What should this become?") with the
  triad as its first decomposition; the decomposition stays revisable, the principal question does
  not. **M**

### 7. Issue trees and MECE (consulting; Minto 1987)
- **Mapping.** (a) = one key question; (b) = a breakdown into parts mutually exclusive and
  collectively exhaustive (MECE); (c) = the branch being analysed; (d) = a hypothesis confirmed;
  (e) = the tree re-cut when the hypothesis fails. **H**
- **Where the triad sits.** It fails MECE at the top: roots 1 and 3 overlap (purpose and identity;
  need is defined against the neighbours); roots 2 and 3 overlap (where it is developing vs what
  else it could be); nothing covers who decides, cost or evidence. **M/H**
- **Failure modes.** Truly MECE splits are rarely reachable at the top; the first split anchors
  all later thinking; practitioners re-cut freely — fixed top levels are not the practice. [P,
  widely used] [E: practitioner lore only] **M**
- **Proposed roots.** Decided per project from its key question, not fixed across projects. **H**

### 8. Viable System Model (Beer 1972/79) and Soft Systems Methodology (Checkland 1981)
- **VSM mapping.** System 5, identity and policy = "why exist / what is it really"; System 4, the
  outside and the future = "neighbours / what else could it be"; System 3, inside and now = "how
  built / where developing". Missing: System 1 (the operations) and System 2 (coordination
  between them) — in a mixed team of people and agents, coordination is not a trivial gap.
  (c) = which function is attending; (e) = System 5 rebalancing 3 and 4. **M**
- **SSM mapping.** The root definition "do P by Q to achieve R" = what, how, why; SSM holds
  *several* root definitions from different worldviews on purpose. **H**
- **Failure modes.** VSM: System 3 starves System 4 — the urgent drives out the exploratory, which
  predicts that root 3 withers or becomes a junk drawer; System 5 collapses into System 3. [P,
  cited in management cybernetics] [E: case studies only, 1970s–2010s] **M/L** SSM: a single
  "what is it really" erases the plurality of worldviews — exactly the cost of the "what is this
  project?" wording. **M**
- **Proposed roots.** Identity; environment and future; here and now; plus coordination. Or SSM's
  CATWOE checklist — customers, actors, transformation, worldview, owner, environmental
  constraints — of which customers and owner are missing from the draft. **M**

### 9. Product-discovery risk sets (Cagan's four risks, 2017; Torres's opportunity solution tree, 2021)
- **Mapping.** Cagan: (a) = four fixed risks — value (will they want it), usability (can they use
  it), feasibility (can we build it), viability (does it work for the business); (d) = a risk
  retired by a test. Torres: (a) = *one* desired outcome; (b) = opportunities → solutions →
  assumption tests; (e) = the outcome changes, the tree re-forms. **H**
- **Where the triad sits.** Root 1 ≈ value + viability; root 2 = feasibility; usability, and the
  users themselves, missing; root 3 has no counterpart — exploration here is a mode applied to
  every risk, not a branch of its own. **M/H**
- **Failure modes.** Outputs disguised as outcomes; the tree decays into a backlog; solutions
  listed without the needs they answer. [P, widely used in product management] [E: practitioner
  reports, 2017–2024; no controlled studies] **M**
- **Proposed roots.** "Will they want it?", "Can they use it?", "Can we build it?", "Does it
  sustain itself?" **H**

### 10. Proposal catechisms (Heilmeier, DARPA, 1970s)
- **Mapping.** (a) = a fixed list of about nine questions asked of every project — What are you
  trying to do? How is it done today, and what are its limits? What is new in your approach? Who
  cares? What difference will success make? What are the risks? What will it cost? How long will
  it take? What are the mid-term and final exams? (d) = the review passed; any open question can
  be homed under one of them. **H**
- **Where the triad sits.** "How is it done today" and "what is new" are root 3's neighbours,
  phrased much more sharply; risk, cost, time and checks of success are missing. **H**
- **Failure modes.** It becomes a funding gate, answered once and never revisited. [P, still
  widely used and copied in research funding] [E: institutional longevity only] **M**
- **Proposed roots.** The catechism itself, or the triad plus "how will we know?" and "what will
  it cost?" **M**

### 11. Assurance cases (Goal Structuring Notation)
- **Mapping.** (a) = one top goal, "the system is acceptably fit in context C"; (b) = goals broken
  down through strategies; (d) = a goal supported by evidence; (e) = changed evidence or context
  invalidates the goals above it — literally the shape, with propagation running upward. **H**
- **Where the triad sits.** "How do we know it works" is the *spine* here, not one root among
  several; context and assumptions are side nodes — root 3's neighbours. **M**
- **Failure modes.** The case becomes paperwork and confirmation bias sets in — the Nimrod Review
  (Haddon-Cave, 2009) is the canonical example; arguments that only ever seek support for the
  claim, never what would defeat it. [P, cited in safety engineering] [E: 2009 inquiry report;
  mixed 2010s comprehension studies] **H/M**
- **Proposed roots.** One claim plus its context, every question homed as something that might
  defeat the claim. **M**

### 12. Knowledge organisation (Dewey's enumerative classification vs Ranganathan's faceted PMEST, 1933)
- **Mapping.** (a) = main classes; (b) = subclasses; (c) = a shelf mark; (d) = the item classed;
  (e) = reclassification. **H**
- **Where the triad sits.** An *enumerative* top level, Dewey style. Ranganathan would give each
  question a value on five facets instead — personality (the thing itself), matter (what it is
  made of), energy (process, action), space, time — with no single home. **M**
- **Failure modes.** Fixed top classes freeze the worldview of their founding (Dewey's 200s,
  religion, are mostly Christianity — Olson 2002); "miscellaneous" classes bloat; compound subjects
  cannot be placed, since a tree cannot cross-classify — Alexander (1965): a semilattice, not a
  tree. [P, all still cited] **H**
- **Proposed roots.** Facets instead of roots, or a few abstract main classes with facets
  beneath. **M**

### 13. Strategy kernels (Rumelt 2011/2022) and the Golden Circle (Sinek 2009)
- **Mapping.** Rumelt: (a) = diagnosis, guiding policy, coherent action. Sinek: (a) = why, how,
  what, in that order. (b) = elaboration within each; (e) = a new diagnosis forces new policy and
  action. **H**
- **Where the triad sits.** Nearly Sinek's circle — why, how, what — with "what" changed from
  "what we do" to "what it is". On Rumelt's ladder it lacks a diagnosis, the crux or challenge;
  "why exist" is a goal, which Rumelt counts as bad strategy. **H/M**
- **Failure modes.** Rumelt's: fluff, goals mistaken for strategy, failure to face the challenge.
  [P, cited in strategy] **H** Sinek's account has no empirical support, and its neuroscience
  claims are widely criticised. [E: none] **H**
- **Proposed roots.** "What is the crux?", "What is our approach to it?", "What are we doing about
  it?" **M**

## Wordings

**Root 1, the product side** (draft: "Why does this project need to exist?")
- *Why should this exist?* — normative; admits "it shouldn't", a legitimate kill decision; drops
  "need", whose necessity presupposes a lack and excludes projects built from want or curiosity.
- *What is it for?* — the final cause, shortest, neutral about justification; excludes "why this
  rather than nothing or something else".
- *What changes, and for whom, if it succeeds?* (Heilmeier) — brings in the users and the success
  condition; excludes purposes inside the builders themselves, such as learning or craft.
- *What problem does it solve?* — presupposes a problem, leans toward solutionism; excludes
  artistic, research and tool-for-self purposes.

**Root 2, the technical side** (draft: "How is it built, and where is it developing?") — the
draft fuses structure (static) and trajectory (dynamic); "where" is ambiguous between a place
(repo, platform) and a direction.
- *How does it work?* — structure and behaviour; excludes progress and roadmap.
- *What is it made of?* — material only; excludes construction and process.
- *Where is it heading?* — trajectory only; could be a root of its own, or a facet on every node.
- *How do we build it?* — the method, as distinct from the artifact. The draft has no home for
  questions about the work process itself, which in a tree shared by people and agents will be
  frequent.

**Root 3, the research / exploration side** — several questions, not one. The draft fuses four:
1. *What is this one of?* — its class, precedents, identity.
2. *What surrounds it?* — neighbours, dependencies, the outer environment.
3. *What else could it be?* — the alternatives, the option space.
4. *What don't we know?* — exploration as a *mode*; it cuts across every root, so as a branch it
   becomes a junk drawer.

Candidates: *What is this one of?* (class and neighbours, excludes futures); *What surrounds it?*
(environment — Simon's and Jackson's root; excludes identity and alternatives); *What else could
it be?* (the possibility space; excludes the present environment); *How is it done elsewhere?*
(Heilmeier — precedent and the limits of existing approaches; the most testable of the four).

**What is lost with "what is this project?"** It is the principal question the *whole* tree
answers: as one root among three it either swallows its siblings or becomes a catch-all. It loses
outwardness (the neighbours) and modality ("could be"); it presupposes a single essence, erasing
the plurality of worldviews SSM keeps on purpose; it invites a definitional answer that closes
early and then, through re-examination, needlessly reopens everything below it.

## The set itself

**Is three the right number?** No family converges on three except those that build in the rule of
three — Simon (with his link dropped), Rumelt, Sinek. The rest split: *one root* (IBIS, erotetic
logic, MECE issue trees, opportunity solution trees, assurance cases), or *four to nine fixed
parts* (four causes, four stases, four risks, six question words, PMEST, Heilmeier). Together they
point to one stated principal question with a small *revisable* first breakdown below it. **M**

**Missing roots, as the families see them.**
- *Who decides, who may close a question* — stasis jurisdiction, CATWOE's owner; acute when
  agents close questions; the strongest omission. **M/H**
- *Who it is for* — Cagan's usability, CATWOE's customers; foldable into root 1 only if the
  wording names them.
- *What it must never do* — Rittel's deontic issues, VSM's policy function, Jackson's world
  assumptions: constraints and invariants.
- *How we know it works* — the spine of assurance cases; probably better as a facet on every root.
- *What it costs* — Heilmeier, viability; also probably a facet.

**Are two of the three really one?** Roots 1 and 3 overlap through the formal and final causes,
and through "need is defined against the neighbours"; roots 2 and 3 through trajectory vs
possibility. A cleaner cut, after Simon, Jackson and Beer:
- **Purpose** — what it is for, for whom, and what it must never do.
- **Constitution** — what it is made of and how it works.
- **Situation** — what surrounds it, what it is one of, how it is done elsewhere.

Trajectory, evidence, cost and authority then become facets or cross-links, not roots. The pass's
own synthesis, not any one family's. **M/L**

**Is a fixed root set a good idea at all?** For: every question has a home, so placement is
deterministic for agents; projects can be compared; the vocabulary is shared. Against: Rittel and
Dewey — working out the problem is part of the work; classification history — fixed top levels
freeze their founding worldview; Alexander — questions overlap, a single home is false; VSM — the
roots allocate attention, so the technical root will absorb the work and the exploration root will
starve or bloat. What survives: fixed roots last when they are abstract — kinds of question, as
Rittel's issue types or the stases, rather than topics — with an explicit procedure for revising
them, and allowing a question more than one parent. A test, not evidence: re-file a real project's
last 50 questions under the proposed roots; if a large share is ambiguous, or lands in the
exploration root, the cut is wrong. The families agree on all of this as principle; there is no
empirical evidence that any fixed root set improves project outcomes. **H**

## What the tasking smuggled in

1. *"Every later question has a home under one of them"* — assumes a single-parent tree and treats
   homing as the goal, rather than retrieval or attention. Alexander, Ranganathan and Zachman each
   break it.
2. *Roots divided by department* — product, technical and research mirror an org chart (product
   manager, engineering, research): Conway's law applied to a question space. Several families
   divide by *kind* of question instead.
3. *Roots framed as "sides" of the project* — makes exploration a territory rather than a mode,
   the main reason root 3 resists wording.
4. *The why, how, what template* — the draft's order is Sinek's Golden Circle, a pop template with
   no evidence behind it; it probably shaped the draft more than any analysis did.
5. *"Sharper wordings"* — frames the problem as wording when it is the cut; the brief does allow
   the set to be wrong, but asks for wordings first.
6. *"Root questions"* — assumes the roots are questions; they could be facets, kinds of question,
   or unasked presuppositions (Collingwood). Also assumes questions, rather than goals, claims or
   decisions, are the right unit; opportunity solution trees and assurance cases use outcomes and
   claims.
7. *"Every new project"* — assumes all projects share one top structure; a library, a research
   spike, a product and a method harness may not.
8. *The example missing roots* (who it is for, must never do, how we know, what it costs) — prime
   product-management and requirements vocabulary and pulled the "missing" list toward them; "who
   decides" was not offered and came out the strongest.
9. *The requested format* — asking for families of *fixed* root sets, each with a maturity ladder
   and evidence, casts the emergent-structure traditions (grounded theory, folksonomy, wicked
   problems) as mere objections; assumes ladders exist, while most of these families have none;
   assumes evidence exists, while it barely does, so the honest answer rests almost entirely on
   principles.
10. *The mix of people and agents* — "every question has a home" is mainly an agent requirement:
    agents need deterministic placement, people tolerate ambiguity; this biases toward MECE-style
    rigidity.
11. *The pass's own bias* — sources mostly Western-canon and English-language.

## Nothing to take

Considered and refused:
- *Double Diamond and other design-phase models* — phases are temporal; a question does not stay
  homed in a phase, and closure has no counterpart. No statable mapping.
- *Toulmin's argument model* — one argument, not a tree of questions; claim and warrant are not
  homes for questions.
- *Backlog hierarchies (themes, epics, stories) and OKRs* — they home work items, not questions,
  and are replaced each cycle; permanent roots and closure by answer do not map.
- *Cynefin* — classifies how known a *situation* is, and a question's domain shifts as knowledge
  grows, so it cannot be a home; possibly usable as a facet, not as roots.
- *Wardley mapping* — nodes are components on an evolution axis, not questions; echoes "where is it
  developing" only loosely.
- *Bounded contexts (domain-driven design)* — partition a domain model as it emerges; not a fixed
  question set.
- *Grounded theory and folksonomy* — the anti-family: no fixed roots, so the shape is not an
  instance of them; used above only as the alternative to fixing roots.
- *Bloom-type question taxonomies* — classify the cognitive level of a question, not where its
  subject lives in a project.
- *Dilts's "logical levels"* — a mapping can be stated (environment, behaviour, capability,
  belief, identity, purpose); refused for lack of standing, not lack of mapping — a different
  reason from the brief's criterion.
