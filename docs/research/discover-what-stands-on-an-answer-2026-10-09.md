# Discover — what stands on an answer, and what a change does to it, 2026-10-09

One /discover pass for [q-0001.0023](../questions/q-0001.0023-how-does-a-change-in-one-answer-reach-what-stood-on-it.md),
a general-purpose subagent told not to read the repository, answering from its own knowledge with
no web search; citations and figures are from memory. Filed as it came back, its layout condensed.
Not fed the earlier pass of the same day.

**What the tasking transmitted:** questions and answers written down over months by people and
agents; answers given on the strength of other answers, questions posed on the strength of what is
taken as known (*which language* takes a service for granted); a change sometimes re-choosing an
answer, sometimes unmaking a question, seemingly by how far the answer moved (one more developer
against no team) and by how settled the project is; nobody can list everything taken for granted,
and recording all of it costs more than it saves; the builders want changes to reach what they
affect without freezing work or recording everything, and do not know what the relations are or
how many kinds. None of the store's own terms — *depends on*, *assumes*, presupposition — was
given.

---

**Key:** P — a principle, with whether it is still cited and used; E — evidence that something
works, how recent, on what; confidence H/M/L.

## Families

### F1. Reason maintenance (Doyle's JTMS 1979, de Kleer's ATMS 1986, Forbus and de Kleer 1993)
- **Mapping.** A node is an answer. A justification is ⟨in-list, out-list⟩ → consequent: the
  in-list is the answers this one is given on the strength of; the out-list means *unless* — the
  answer stands on something being *absent*. A premise is a node held with no justification; an
  assumption, a node that can be retracted and that others rest on; a nogood, a recorded
  inconsistency. Relabelling is how a change reaches what it affects; dependency-directed
  backtracking assigns blame.
- **Ladder.** Monotonic dependency net → JTMS → LTMS → ATMS (all consistent assumption-sets at
  once). The shape is a JTMS whose justifications are mostly unrecorded. In this family's terms a
  node IN with no recorded justification *is a premise*, and propagation never retracts a premise:
  it predicts the shape's failure exactly — support not recorded silently becomes premise status.
- **How it goes wrong.** Incomplete justifications leave stale IN nodes; circular self-support must
  be excluded, since support must be well-founded; odd loops through out-lists have no stable
  labelling; thrashing; in the ATMS, labels grow exponentially.
- **Question vs answer.** Refuses the distinction: everything is a proposition; a question appears
  only as a node "Q is askable", justified like any other. The ATMS cut between assumed and derived
  is the nearest thing, and a different cut.
- **Settledness.** Binary only, premise or assumption; ATMS focus control the nearest to a gradient.
- **Confidence.** P = H (canonical, alive in its descendants: incremental solvers, Datalog
  provenance, build systems). E for TMS by name in production = L, faded after the 1990s; E for its
  descendants = H.

### F2. Belief revision (AGM 1985; Gärdenfors and Makinson 1988 on entrenchment; Hansson on belief bases; Harman, *Change in View* 1986; Katsuno and Mendelzon 1991; Olsson and Westlund 2006 on the agenda)
- **Mapping.** The belief base is the recorded answers, its closure what they imply; revision and
  contraction are what a change does; entrenchment is settledness. The *foundations theory* keeps
  justifications and drops what loses support; the *coherence theory* keeps every belief not
  contradicted and records no reasons. Harman's conservatism — don't track reasons, keep beliefs
  until there is reason to doubt them — is exactly the shape's cost argument against recording
  everything. Agenda revision revises the open questions together with the beliefs.
- **Ladder.** AGM on closed sets → base revision → iterated revision (Darwiche and Pearl) →
  revision vs update → agenda-sensitive revision → dynamic epistemic logic. The shape is iterated
  base revision with an agenda. It runs on coherence-theory economics but expects
  foundations-theory propagation — an incoherent pairing.
- **How it goes wrong.** Belief perseverance: beliefs outlive the withdrawal of their evidence
  (Ross, Lepper and Hubbard 1975) — coherence theory's known cost. AGM does not say how
  entrenchment looks *after* a revision; the family leaves the evolution of settledness open.
  **Conflating revision with update**: revision is "we were wrong about a static world", update is
  "the world changed"; they obey different postulates and propagate differently.
- **Question vs answer.** Core AGM refuses, having no questions. Agenda and Levi-style accounts
  define a question as a set of potential answers relative to the current full beliefs; a
  presupposition is then simply a belief the answer-space is defined over. Contracting it removes
  the question from the agenda; adding beliefs opens new ones.
- **Settledness.** Entrenchment is how unwilling you are to give a belief up — explicitly *not*
  probability: a belief can be highly entrenched and doubtful at once.
- **Confidence.** P = H (an active field). E that it guides practical record-keeping = L. E for
  perseverance = M (classic; its size debated). The revision/update distinction = H.

### F3. The logic and pragmatics of questions (Belnap and Steel 1976; Wiśniewski's inferential erotetic logic; Hintikka's interrogative model; Stalnaker on common ground; Roberts on the question under discussion; Lewis on accommodation)
- **Mapping.** A question is its set of direct answers, a partition of the possibilities. **A
  presupposition of Q is whatever every direct answer to Q entails**; Q is sound iff its
  presupposition is true. Erotetic implication and evocation (Wiśniewski) give sub-questions, and
  questions arising from what is already held. The QUD stack and strategy tree is the
  decomposition; common ground, what is taken for granted; accommodation, how unrecorded
  presuppositions are added silently; a corrective answer denies the presupposition.
- **Ladder.** Yes/no → wh-questions with existence and uniqueness presuppositions → erotetic
  implication → strategies of inquiry (QUD trees, interrogative games) → a common ground evolving
  across a discourse. The shape is a long-running QUD tree over a common ground that is persistent,
  incomplete and *not shared* across participants.
- **How it goes wrong.** Presupposition failure, no direct answer true; accommodated false
  presuppositions (loaded questions); a question popped off the stack unresolved; a "defective
  context" — participants whose common grounds diverge (Stalnaker).
- **Question vs answer.** This family owns the distinction and gives a test. A premise of answer
  *a* is used in *a*'s support and not entailed by rival answers: if it changes, the rivals survive
  and you re-choose. If a presupposition fails, every rival fails with it and Q is unsound. If only
  some answers die, Q *narrows* — the in-between case.
- **Settledness.** Not native; in the simple models common ground only grows.
- **Confidence.** P = H (QUD and inquisitive semantics heavily used now). E for project records = L.

### F4. Absolute presuppositions and hinges (Collingwood 1939–40; Wittgenstein, *On Certainty*; Moyal-Sharrock, Pritchard, Coliva)
- **Mapping.** Every question rests on presuppositions. *Relative* ones are answers to earlier
  questions and can be questioned. *Absolute* ones, hinges, answer no question inside the inquiry:
  they must stand fast for questions to be asked at all. The riverbed: hardened propositions
  channel the fluid ones, the bed itself shifts slowly, and the same content can be tested at one
  time and be a standard of testing at another.
- **Ladder.** Answer → relative presupposition → absolute presupposition → "constellation", a set
  of absolute presuppositions defining an era. The late project is a hardened riverbed; the early
  one is fluid.
- **How it goes wrong.** Treating a hinge as an answer that needs justifying — a category mistake.
  Hinges do not shift by refutation but under strain, when the constellation stops being jointly
  holdable, so the shift cannot be argued for from inside. Trying to list the hinges defeats
  itself.
- **Question vs answer.** The sharpest refusal to merge them: what a question takes for granted is
  not the same kind of item as an answer. "Nobody can list it in advance" is a theorem here, not an
  accident.
- **Settledness.** Central — a *functional role*, not a property of content, and content moves
  between roles.
- **Confidence.** P = H (hinge epistemology active). E as anything operable = L: it explains, it
  supplies no mechanism.

### F5. Research programmes and traditions (Duhem and Quine; Kuhn 1962; Lakatos 1970; Laudan 1977)
- **Mapping.** Answers are theories and auxiliary hypotheses. The hard core is the settled
  presuppositions, the protective belt the revisable answers, the positive heuristic the agenda.
  Duhem–Quine: a failure does not say which node to revise. Normal-science puzzles presuppose the
  paradigm; a revolution dissolves questions — "what does phlogiston weigh?" stops being askable.
  Laudan: problems can be solved, be anomalous, or *stop being problems* when the tradition
  changes.
- **Ladder.** A puzzle within the paradigm → adjusting the belt → changing the core → paradigm
  shift. Kuhn's pre-paradigm stage, everything contested, is the shape's "early on".
- **How it goes wrong.** Degenerating programmes patch the belt ad hoc to protect the core;
  anomalies pile up unrecorded until a crisis; incommensurability — questions asked after a shift
  cannot be stated in the old vocabulary, so re-asking in other words is not translation; blame
  stays ambiguous.
- **Question vs answer.** Kuhn and Laudan make it (the paradigm licenses which questions are
  legitimate); Quine refuses it — one web, differing only in centrality.
- **Settledness.** Lakatos: the hard core is a *methodological decision*, made irrefutable by fiat,
  not discovered. Quine: centrality is how much else would have to be readjusted.
- **Confidence.** P = H. E as historical description = M (contested historiography). E as tools = L.

### F6. Design rationale (Kunz and Rittel's IBIS 1970; Rittel and Webber 1973; QOC 1991; Lee's DRL 1991; Kruchten 2004; Nygard's ADRs 2011; Burge's SEURAT)
- **Mapping.** An issue is a question, a position or option an answer, an argument or criterion
  support. IBIS links: responds-to, supports, objects-to, generalizes, specializes, replaces,
  questions, is-suggested-by. Kruchten's relations: constrains, forbids, enables, subsumes,
  conflicts-with, overrides, comprises, is-alternative-to, is-bound-to; his states: idea →
  tentative → decided → approved → challenged → rejected or obsolesced. An ADR's *Context* is what
  was taken for granted when deciding; records are append-only and superseded, not edited.
  SEURAT: assumptions can be disabled, and the rationale depending on them is flagged.
- **Ladder.** None → ADR log → IBIS/QOC graph → typed graph (DRL, Kruchten) → computational
  rationale with propagation (SEURAT). The shape sits between an ADR log and a typed graph.
- **How it goes wrong.** *The capture problem* is the family's central result: rationale is valued
  and rarely recorded or read (Tang et al. 2006, surveys since). Graphs decay; typed links are used
  inconsistently. Wicked problems: formulating and solving co-evolve, with no stopping rule.
- **Question vs answer.** Partial. ADR Context holds the frozen presuppositions, unstructured.
  Kruchten's *enables* plays presupposition and *constrains* is kept apart from it; he separates
  existence, property and *executive* decisions, and executive ones (team, process, tools) are
  typically those that make other questions askable. DRL may have had a "presupposes" relation (L).
- **Settledness.** Decision states and supersession.
- **Confidence.** P = H (ADRs widely used today). E for the capture problem = H. E that typed
  rationale graphs pay off in long-lived projects = L.

### F7. Incremental computation and build systems (Mokhov, Mitchell and Peyton Jones, "Build systems à la carte" 2018; Shake; Bazel; Adapton; Salsa)
- **Mapping.** A key is a question, a value an answer, a task how an answer is computed from
  others, the trace what stands on what. **Applicative (static) against monadic (dynamic)
  dependencies**: with monadic ones, *which* keys a task depends on is decided by the values of
  earlier keys — a question exists only given an answer. **Early cutoff**: a recomputed answer that
  comes out equal leaves its dependents alone. Hermeticity: every dependency declared.
  **Durability (Salsa)**: inputs tagged by how likely they are to change.
- **Ladder.** Make (static, timestamps) → Shake (monadic, early cutoff) → Bazel (hermetic, shared
  cache) → Salsa/Adapton (demand-driven, red-green validation, durability). The shape is monadic,
  demand-driven and *non-hermetic* — the family's own failure case.
- **How it goes wrong.** An undeclared dependency gives a silently stale result; over-declaring
  causes rebuild storms — this family's version of freezing work; early cutoff knows only exact
  equality, with no notion of an answer that "moved a little".
- **Question vs answer.** Monadic dependencies encode it, but as one relation in the trace; the two
  kinds differ only in *when* they are discovered.
- **Settledness.** Durability as a declared cost tier: a query on high-durability inputs alone
  skips revalidation when only low-durability ones change.
- **Confidence.** P = H. E = H at production scale, only on machine-checkable dependencies.
  Transfer to human records = L.

### F8. Dynamic and conditional constraint satisfaction (Dechter and Dechter 1988; Mittal and Falkenhainer 1990; minimal perturbation; feature models, FODA 1990)
- **Mapping.** A variable is a question, a value an answer, a domain the option set; a
  compatibility constraint relates answers to each other; **an activity constraint makes a
  variable exist only under certain assignments**; a nogood is a recorded incompatibility. The
  *minimal perturbation problem* — re-solve after a change altering as few assignments as possible
  — is "without freezing work" stated formally. In feature models a parent feature's presence
  conditions its children.
- **Ladder.** Static → dynamic (constraints come and go) → conditional (variables come and go) →
  solution stability → open CSP (variables and domains not known in advance). The shape is open,
  conditional, and wants minimal perturbation.
- **How it goes wrong.** Thrashing; nogood blow-up; the stability–optimality trade-off — minimal
  perturbation keeps worse solutions alive.
- **Question vs answer.** Yes: compatibility and activity constraints are structurally different
  relations; a unary or domain constraint gives a third, "narrows the option set".
- **Settledness.** Committed or frozen variables in interactive configuration.
- **Confidence.** P = H. E = H in industrial product configurators, L for project records.

### F9. The frame, ramification and qualification problems (McCarthy and Hayes 1969; McCarthy 1980; Hanks and McDermott 1987; Reiter; McCain and Turner; Lin 1995)
- **Mapping.** An action is a change to an answer, fluents the other answers. *Frame*: what stays
  the same, said without listing it — the default is inertia. *Ramification*: indirect effects, the
  dependents that must change. *Qualification*: the preconditions that cannot be listed but are
  taken for granted. Circumscription minimises abnormality.
- **Ladder.** STRIPS assumption → frame axioms → successor-state axioms → nonmonotonic and
  circumscription approaches → causal theories (handling ramification).
- **How it goes wrong.** The Yale shooting problem: simply minimising change picks the wrong world;
  causal or chronological direction is needed, so the *direction* of "stands on" carries
  information. State constraints without causal direction give wrong ramifications.
  Qualifications cannot be solved by listing them, only by a default of "nothing abnormal".
- **Question vs answer.** Aligns with it: qualification ≈ presupposition, ramification ≈
  dependence on a premise, and the literature solves them with *different mechanisms*.
- **Settledness.** None beyond uniform inertia.
- **Confidence.** P = H. E = M (works in planning and answer-set programming, e.g. PDDL derived
  predicates).

### F10. Requirements: satisfaction arguments, goal refinement, traceability (Jackson and Zave 1995–97; van Lamsweerde and Letier 2000 on KAOS obstacles; Gotel and Finkelstein 1994; DOORS suspect links)
- **Mapping.** A goal is a question, an operationalisation an answer, AND/OR refinement the
  decomposition. **W, the domain assumptions,** is what an answer stands on, through the
  satisfaction argument W, S ⊢ R. Obstacles are conditions that break W. A trace link becomes
  *suspect* when its upstream end changes.
- **Ladder.** Trace matrix → suspect-link propagation → goal models → explicit satisfaction
  arguments → monitoring assumptions at runtime (Fickas and Feather 1995). The shape is a goal tree
  whose W is implicit.
- **How it goes wrong.** Traces decay; floods of suspect links get ignored — alarm fatigue standing
  in for freezing; unrecorded assumptions about the environment are the classic root cause (Ariane
  5 reused Ariane 4's horizontal-velocity assumption); Gotel and Finkelstein — traceability
  *before* the requirements spec, back to where things came from, is the hardest and least
  practised.
- **Question vs answer.** W is indicative, R optative. A sub-goal under an OR-refinement exists
  only if its alternative was chosen — presupposition under another name.
- **Settledness.** Volatility classes and baselines.
- **Confidence.** P = H. E that suspect links exist in industry = H, that they are effective = M.
  Ariane = H.

### F11. Common-law precedent
- **Mapping.** The issue or question presented is the question, the holding the answer. *Ratio
  decidendi* is what the answer stands on; obiter dicta, remarks nothing rests on. Citing cases are
  the dependents; treatment ranges over followed / distinguished / limited / questioned /
  overruled; citators (Shepard's, KeyCite) propagate. **Mootness**: the question has lost its live
  controversy; **ripeness**: not yet askable. **"Assumed without deciding"** explicitly marks a
  question's presupposition.
- **Ladder.** Dictum → holding → line of authority → settled doctrine → "super-precedent".
- **How it goes wrong.** Stealth or implicit overruling — a precedent hollowed out without being
  named, citators miss it; citators disagree (Hellyer 2018); "distinguishing" used to dodge an
  overruling, doctrine turning incoherent; **what a holding stood on is often fixed only *later*,
  by the courts that rely on it** — what an answer stands on decided after the fact.
- **Question vs answer.** Yes, cleanly: mootness, ripeness and assumed-without-deciding belong to
  the question; the ratio to the answer.
- **Settledness.** Stare decisis; overruling factors are workability, reliance, doctrinal erosion
  and changed facts (Casey 1992). Weight comes from *accrued reliance*, not age as such.
- **Confidence.** P = H. E on citator reliability = M (small samples). That the ratio is fixed
  retrospectively = H, a jurisprudential commonplace.

### F12. Assurance cases and defeasible argumentation (Toulmin 1958; Pollock 1987; Dung 1995; GSN Community Standard v3 2021; Goodenough, Weinstock and Klein on eliminative argumentation; Bloomfield and Rushby, "Assurance 2.0")
- **Mapping.** A goal is a claim to be answered, a strategy a decomposition, a solution evidence.
  **Context** is what the claim is posed within; **Assumption**, a premise held without support;
  **Justification**, why a strategy is fit. **Defeaters**: *rebutting* counts against the
  conclusion, *undercutting* attacks the inference link, *undermining* attacks the evidence.
  Confidence comes from defeaters eliminated.
- **Ladder.** Claims plus evidence → GSN/CAE → modular cases → confidence arguments → eliminative
  argumentation → dynamic assurance cases updated at runtime. The shape is a long-lived case under
  change — dynamic assurance.
- **How it goes wrong.** The Nimrod review (Haddon-Cave 2009): the safety case became paperwork,
  its assumptions unchallenged. Confirmation bias: support sought rather than defeaters. Context
  and Assumption used interchangeably in practice.
- **Question vs answer.** Yes: Context, Assumption and Evidence are three distinct roles, and the
  defeater types split change further.
- **Settledness.** Residual doubt and defeaters eliminated, not age.
- **Confidence.** P = H. E = M. Nimrod as a cautionary case = H; outcome studies sparse.

### F13. Engineering change propagation and modularity (Steward and Eppinger on the DSM; Baldwin and Clark 2000; Eckert, Clarkson and Zanker 2004; Sobek, Ward and Liker 1999 on set-based design)
- **Mapping.** Design parameters are answers; the dependency structure matrix records what stands
  on what. **Design rules** are visible parameters others take as given; **hidden parameters**,
  answers nobody else stands on. Eckert classifies elements as **constants, absorbers, carriers
  and multipliers**; later work adds **margins** — how far a parameter can move before its
  dependents notice. **Set-based design** keeps sets of answers open and only ever narrows them.
- **Ladder.** Change-order workflow → DSM → change prediction (likelihood × impact) → design rules
  → set-based design.
- **How it goes wrong.** Change avalanches; emergent changes (fixing one thing triggers others);
  tacit dependencies missing from the DSM; design rules locked in too early.
- **Question vs answer.** Design rules play the presupposition role. Baldwin and Clark: modularity
  is *created* by deciding which answers become rules, so the graph can be designed, not only
  recorded.
- **Settledness.** Design rules, freeze milestones, narrowed sets, margins.
- **Confidence.** P = H. E = M (industrial case studies, e.g. Rolls-Royce, Westland, Toyota).

### F14. Decision analysis and framing (Howard; Spetzler, Winter and Meyer 2016 on the decision hierarchy; Mitroff on Type III error; value of information)
- **Mapping.** A decision is a question, an alternative an answer; uncertainties and values are
  what the answer stands on, kept as two kinds. **The decision hierarchy splits decisions into
  given / focus / deferred**: "given" is precisely what the question takes for granted. A
  *switching value* is how far an input must move before the choice flips; value of information
  decides whether to look again; Type III error is the right answer to the wrong question.
- **Ladder.** A single choice → influence diagram → sensitivity analysis and VOI → framing and
  hierarchy → sequential decisions and real options.
- **How it goes wrong.** Frame blindness, anchoring, Type III errors, over-analysis.
- **Question vs answer.** Yes, as frame against model inputs, beliefs kept apart from preferences.
- **Settledness.** The tier in the hierarchy, plus robustness — distance to the switching value.
  This is the precise form of "how far the answer moved", and it is a property **of each dependent
  decision, not of the change**.
- **Confidence.** P = H. E = M (practitioner literature, e.g. pharma and energy).

### F15. Interface contracts and versioning (SemVer 2.0; Hyrum's law; consumer-driven contracts, Pact; stability tiers)
- **Mapping.** A published interface is an answer, its consumers the dependents. What consumers
  take for granted is the documented contract plus, by Hyrum's law, all observable behaviour.
  Patch / minor / major is a change's magnitude; version ranges are each consumer's tolerance.
  **0.x means unsettled, 1.0 is a stability promise.** Consumer-driven contracts have dependents
  declare what they stand on.
- **Ladder.** Pinning → ranges → consumer-driven contracts → stability tiers and long-term support,
  up to "never break userspace". Early projects at 0.x, mature ones at 1.x.
- **How it goes wrong.** Hyrum's law — reliance nobody declared; mislabelled versions (Raemaekers
  et al. 2014: roughly a third of Maven releases broke something whatever the version number;
  later re-analyses found less, M); projects stuck at 0.x indefinitely.
- **Question vs answer.** Weak: a major version that *removes* a capability makes the consumer's
  question moot; one that *changes* behaviour has the consumer re-choose.
- **Settledness.** Declared, as a *commitment*, not observed.
- **Confidence.** P = H. E = M.

## The distinctions

**Stable** — drawn independently by three or more families in their own vocabulary — each with a
software example.

1. **Support, justification** — one answer stands on another. F1 justification, F7 trace, F11
   ratio, F12 warrant, F6 argument, F10 W. *Example:* Postgres chosen because orders and inventory
   needed transactions spanning both.
2. **Presupposition, applicability** — a question exists only given an answer. F3, F4, F8 activity
   constraints, F7 monadic dependencies, F9 qualification, F10 OR-refinement, F11 moot, F12
   Context, F13 design rules, F14 "given". Belnap and Steel's test makes it decidable: a
   presupposition is whatever *every* answer to the question entails. *Example:* "Kafka, RabbitMQ
   or SQS?" presupposes asynchronous messaging between services, since every option entails it; go
   synchronous and the question is moot.
   - Two directions: **moot**, the presupposition lost; **unripe**, not yet established (F11
     ripeness, F8 inactive variable, F3 not yet on the stack). *Example:* "Which sharding key?"
     before anyone has established that one database won't suffice.
   - **Narrowing** in between: some answers die and the question survives smaller.
3. **Constrains** — narrows the option set without choosing. F8 domains, F6 Kruchten's
   *constrains*, F13 design rules. A third relation, between presupposition and support.
   *Example:* "we are on AWS" narrows the broker question to {SQS, MSK, self-hosted} without
   justifying any one.
4. **Decomposition** — a question has sub-questions. F3, F10, F12, F6. About how a question is
   answered, not about truth. *Example:* "How do users authenticate?" splits into "Which identity
   provider?" and "Sessions or tokens?"; changing one sub-answer leaves the other intact.
5. **Fact against criterion** — an answer stands on beliefs and on values. F14
   beliefs/preferences, F10 W against R, F6 QOC criteria. *Example:* "Go over Rust" rests on the
   criterion "hiring pool outweighs runtime safety"; when hiring stops being the constraint you
   re-choose though no fact changed.
6. **Rebut against undercut.** F12 (Pollock), F11 (distinguish against overrule), F1 (a
   justification invalidated while its antecedent survives). *Example:* the benchmark favouring
   library X ran a debug build; X is not shown slower, its support is simply void — the answer
   becomes unsupported, not wrong.
7. **Revision against update** — we were wrong, against the world changed. F2 (Katsuno and
   Mendelzon), F11 (error against changed facts), F10 (wrong W against changed environment).
   *Example:* "single-tenant". Discovering the contract always required multi-tenancy is
   revision: every answer since the beginning is suspect. The company now *deciding* to go
   multi-tenant is update: past answers were right, and the work is forward migration. They
   propagate differently.
8. **Tolerance** — a change's size against what a dependent can absorb. F14 switching values, F13
   margins, absorbers and multipliers, F15 version ranges, F11 distinguishing, F7 early cutoff (the
   binary form). The stable insight: tolerance belongs to the edge or the dependent, not to the
   change. *Example:* the team gains one developer — the review policy absorbs it; the team splits
   in three — service boundaries are re-chosen (Conway); the team vanishes — the review-policy
   question is moot.
9. **Entrenchment, settledness.** Stable as a concept, *unstable as to what it is a property of*:
   of an item (F7 durability); of its position in the web (F5, Quine); a methodological decision
   (F5, Lakatos); accrued reliance (F11, and F15 through Hyrum); a declared commitment (F15 at
   1.0); a functional role content moves through (F4). The families agree settledness is not
   confidence (F2). *Example:* public API field names and the internal module layout are the same
   age; the field names are settled by reliance, the layout is not.
10. **Standing on an absence** — "unless". F1 out-lists, F9 inertia and abnormality, F11 "absent
    X". *Example:* "no cache, as long as no read-heavy consumer exists" — a *new* item triggers it,
    no answer changing.
11. **Conflict, alternative.** F6, F8 nogoods, F1. *Example:* event sourcing conflicts with
    hard-deleting user data on request (GDPR), though each is fine alone.

**One family's vocabulary only:** SemVer's three magnitude levels (an artefact of version syntax);
Kruchten's roughly ten relations, which collapse onto 2, 3, 4 and 11 above (*enables* is
presupposition, *constrains* constraint, *comprises* and *subsumes* decomposition, *forbids* and
*conflicts-with* conflict); the binary hard core against belt (Lakatos's methodology; Quine shows
a continuum); the TMS premise/assumption cut; ATMS environments; GSN's Context/Assumption split as
actually used, which practitioners blur, though the distinction under it (2 against 1) is stable;
the four labels of Eckert's taxonomy (the absorber/multiplier concept is stable); the ratio/obiter
terminology, mapping onto 1 against non-load-bearing; early cutoff's exact equality.

## What the tasking smuggled in

1. **Atomism.** Questions and answers taken as discrete records with stable identity; F4 and F5
   hold that much of what is taken for granted is holistic or tacit and not a proposition at all.
   "Which relations exist between items?" excludes "some of it isn't an item".
2. **Question identity across rewordings.** "Re-asking in other words" assumes a question persists
   across wordings; in F3 a question *is* its answer-set, so a rewording that changes the set is a
   different question; F5 incommensurability — some rewordings cannot be translated.
3. **Two kinds, set up by the example.** "Answer stands on" against "question takes for granted"
   pre-cuts the space into two; the families find at least six stable relations (1–5 and 11) plus
   two dimensions of change (6 and 7). The example chosen, *which language presupposes a service*,
   is an *existence* presupposition, the cleanest kind; uniqueness ("which language" assumes one),
   scope and option-set presuppositions are murkier.
4. **"How far the answer moved" as a property of the change.** F7, F13, F14 and F15 put it on the
   dependent's tolerance: the same change is nothing to one dependent and a reframing to another.
   Often there is no metric over answers at all — categorical choices.
5. **Settledness as a phase of the project ("early on… later").** The families treat it per item,
   per position, as accrued reliance, as a decision or as a promise — none of them project age.
   Nor is it monotone: Kuhnian crises and rewrites unsettle mature projects. "How far things are
   fixed" also blurs entrenchment (how much rests on something) with confidence (how likely it is
   true).
6. **Change starts at an answer.** Triggers that change no answer: a *new* item (10, absence
   dependence); a new question that exposes a conflict; a change of criterion (5); an undercut (6);
   discovering that something was *never* true — revision, not update (7). "When an answer
   changes" merges revision and update.
7. **Push propagation.** "Changes reach what they affect" assumes push. Alternatives: pull,
   validating on use (F7 demand-driven checks, F11 checking a citator when citing); Harman's
   conservatism, keeping things until doubted (F2); fixing dependencies retrospectively, dependents
   defining what they relied on (F11 ratio, F15 consumer-driven contracts).
8. **Recording as the only lever.** "Without recording everything" frames the trade-off as how much
   to record. Other families *shape the graph* instead: Parnas-style information hiding, Baldwin
   and Clark's design rules, F13 margins and set-based deferral, F8 minimal perturbation — reducing
   what stands on what rather than writing it down.
9. **Only one cost counted.** "Wrong" and "freezing" are named; churn and thrash are not — needless
   re-asking, suspect-link floods that get ignored (F10, F7 rebuild storms); nor the state of an
   answer *unsupported but still true*.
10. **A shared reader.** "Taken for granted" presumes a community with common ground. A stateless
    agent session has none beyond what is written and what it guesses (accommodation); each session
    may accommodate differently — a defective context in F3's sense. So human traditions' budget for
    tacit knowledge does not carry over; this bears on the record-against-cost calculus more than
    anything else here.
11. **A single consistent state.** One current belief state to repair is assumed; F1's ATMS and F8
    hold several contexts in parallel, and F2's paraconsistent variants tolerate local
    inconsistency. "Freezing" is a cost only if consistency must come first.
12. **Acyclicity and direction.** "Built on" suggests foundations. Coherentism (F2, F5 Quine)
    allows mutual support; F1 forbids it; F9 shows direction carries information. Which holds is
    open, not given.

## Nothing to take

Refused for want of a statable mapping:

- **Developmental canalization, sensitive periods** — a good analogue for settledness (early
  plasticity, later robustness), but nothing for a question, a presupposition or a record; a
  slice.
- **Trophic cascades, epidemic cascade models** — propagation only.
- **Data provenance and lineage (W3C PROV)** — records derivation, says nothing of what a change
  does; a slice of F1 and F7.
- **Version control and merging** — changes to text, not what stands on what.
- **Argyris's single- and double-loop learning, Schein's basic assumptions** — name the two
  outcomes, re-choosing against re-posing, with no structure of dependence or propagation; a slice.
- **Mission command and commander's intent** — a two-level slice, intent against orders.
- **Ontology evolution (OWL change propagation)** — answers as axioms, no question side; reduces to
  F2's base revision.
- **Bayesian networks as a family of their own** — fixed structure, so whether a question exists
  falls outside; what is useful (sensitivity, VOI) is in F14.
- **Sheaf or category-theoretic local-to-global consistency** — attractive, but no statable notion
  of a question.
- **Serial-fiction continuity management (story bibles, retcons)** — long-lived and multi-author,
  and retcons do make plotlines moot, but only answers map, with no relation beyond "contradicts";
  a practice, not an account.
- **Hegelian dialectic** — no statable mapping.
