# q-0035 What is a project's product document to the method, and which of the method's mechanisms keeps it and the project's work in agreement both ways?

- **record of** what it intends to become
- **state** open
- **lean** decisions 1–11, the user, 2026-10-12/13; its spec drafted, docs/spec/01-0040-a-projects-account-stays-in-agreement-with-its-work.md, awaiting acceptance; open: the README derivation (.0005), the measure (.0004, parked)
- **struck** 0, last 2026-10-12T16:02Z

Opened 2026-10-12 from the align on what is now q-0035.0002. The user: *the customer is not only
me — I'd like to add a product method for all users; first we need to focus on the mechanism
itself working properly both ways* — and: *not core, method*. Every project steered under the
method keeps a product document, which leads its work (q-0035.0002) and stays true to it as work
appears (q-0035.0001). This tree's own product document is the first case.

## Decisions

1. **A row is linked to the work through the question store, never through tickets** *(the user,
   2026-10-12)*: while its need is open, a row's status is a straw dog bound to the question it
   waits on, and the wake reports it due when that question closes; once closed, the row carries a
   visible link to where the answer landed, taken from the closing pointer. A question carries no
   product mark for the link. *Narrowed by decision 4: the binding is the undecided row's alone; a
   decided row is itself the home its purpose question closes against and points nowhere; a
   question under another root carries a trace link to it, and its coverage is read from those.*
   Evidence, 2026-10-12: all 46 bound rows wait on live open
   questions; 114 of 155 open questions reach a row through themselves, an ancestor or a
   descendant; the 14 rows marked done link nowhere, and 2 unfinished rows carry no binding.
2. **The product document is the home of the purpose root's answers** *(the user, 2026-10-13)*:
   as the architecture and the ADRs are the structure root's, the product document is where the
   purpose root's decisions land — pains, goals, causes, answers — and a row whose answer is not
   yet chosen is bound to a question under the purpose root. A question under another root serves
   the product through an answer's row — the way a pain is relieved — never through a row of its
   own, by the trace link of decision 4; decision 8 gave each root its mechanism. In this tree,
   whose store predates the seed, q-0033 stands as the purpose root.
3. **The product mechanism's own check reads the link** *(the user, 2026-10-13)*, in the
   verification set and in `/maintain`: an undecided row with no binding, a row bound outside the
   purpose root, a question under the purpose root that no row names, and — by decision 4 — an
   orphan, an unrealized answer, a trace link naming no answer. A row whose question closed is
   still the wake's to report, as every due straw dog is. Each is a matter of form, so the check
   needs no judgement.
4. **Allocation and the trace link** *(the user, 2026-10-13, taking the traceability vocabulary
   whole — the glossary's *Product to implementation*)*: a decided purpose question closes, its
   answer becomes a row, and a structure question opens under the structure root with a trace link
   to it. A trace link is an opaque reference the question store keeps without interpreting; it
   may name several answers; sub-questions carry it by trace propagation; a question opened
   directly under the structure root states its answers or that it is derived. A decided answer's
   coverage is read from the questions that realize it and never written; the product document
   points out only from an undecided row to the purpose question it waits on. The product
   mechanism installs the allocation into `/align` and the statement at opening into the questions
   skill, and its check finds orphans and unrealized answers; the development method and the store
   know nothing of the product. Where a question came from — the decision it was opened from — is
   history in its body, never a checked link.
5. **A pain does not close; it is measured** *(the user, 2026-10-13: "the pain does not close, for
   now; we can add a way; the pain has to be measured somehow, it is not a binary value")*: answers
   are added to a pain, and none of them closes it; whether the answers relieve it is read from a
   measure of the pain that takes values, never from a yes or no on an answer. Coverage says what
   is built; the pain's measure says what it relieved.
6. **Purpose and structure zigzag** *(the user, 2026-10-13, taking Suh's zigzagging from the
   discover pass)*: allocation is not a one-way crossing. Building an answer may show that the
   answer, or the causes it was chosen for, should be split or worded again; then a purpose
   question opens from that structure work — its origin history in its body — and its decision
   adds or replaces answers, never renumbering one. A pain's measure moving, or not, is the other
   road back.
7. **The document leads by showing, the order stays the person's** *(the user, 2026-10-13)*: what
   is minted comes from allocation (decision 4); the queue's order is the person's, and beside it
   the product mechanism shows the answers each item realizes — read through ticket, question and
   trace link — and the unrealized answers, by goal and by pain, so what is left out is a choice
   made in sight. Weighting the order by pain waits on the pain's measure (q-0035.0004).
8. **Each seeded root belongs to the mechanism whose questions it holds** *(the user,
   2026-10-12; moved from q-0035.0003)*: the purpose to the product mechanism, where every product
   link goes; the structure to the development method; the landscape to the research mechanism,
   which grows into what the GoodWolf research harness does — the landscape, the study of methods,
   and analysis, the study of what methods yield. An empirical study answering a product question —
   frost_map's crop-table figures — is analysis, the research mechanism's work, whichever root its
   question sits under.
9. **A root's words belong to its mechanism** *(the user, 2026-10-13)*: the store only seeds, into
   an empty store, the roots the installed mechanisms declare. Until the product and research
   mechanisms exist, the store's shelf keeps all three words, its sentence of ownership a straw dog
   bound here.
10. **One mechanism, `product`, tells the project's account to each of its readers** *(the user,
    2026-10-13, at the spec)*: the product document inside, the root README to a reader arriving
    cold, the release note to one updating — the README derived from the document, the note's
    product half from the coverage that moved since the last release. Its instruction file is a
    `/product` skill holding the three formats and the writing of all three. A line of contract
    change stays the edge mechanism's, read by the note and the README, never written by them;
    publishing a release stays the harness's. No separate releases mechanism is declared.
11. **In core for now** *(the user, 2026-10-13, at the spec)*: the product mechanism ships with
    core like every other, its script beside theirs; in a tree with no product document its check
    finds nothing, and the rules it installs hold where a project keeps a product document — that
    condition a straw dog bound to q-0018.0024, until a project can take a mechanism alone.

## Open within it

- **41 of 155 open questions reached no row** on 2026-10-12. Under decision 2 a question outside
  the purpose root is not expected to: of those, the product needs with no row — the work's shape
  (q-0018.0001 beside the row bound to q-0027.0003), what each host shows unasked, a session's
  lifecycle, this mechanism itself — are the ones to re-read once the purpose root is drawn here.

## Discover pass, 2026-10-13

Asked by the user mid-align, of the whole situation: a product document per project, three seeded
roots each owned by a module, the hand-off from a product decision to implementation questions,
and the back-reference from those to the answer rows. A separate process, told not to read this
repository; transmitted: the question-tree organisation, the three-root split, the hand-off as
proposed, the owners' worry about coupling. Its material as it came back:

### Families

**1. Requirements engineering — goal models and traceability** (KAOS, i*, Gotel & Finkelstein, SysML, DO-178C)
- Mapping: pains/causes = problem analysis (obstacles in KAOS); goals = goals/soft-goals; answer rows = operationalisations/requirements; building questions = design elements. The purpose document is a goal model + requirements baseline. (high)
- Back-reference = a **trace link**, specifically a *satisfy/realize* link (SysML «satisfy», «refine»). Inheritance by sub-questions = **trace propagation**. Derived state = **coverage analysis** over a traceability matrix. A building question with no row = an **orphan**; a row with nothing building it = an **unrealised requirement**. (high)
- The explicit "none" is DO-178C's **derived requirement** — one with no parent, which must be flagged and reviewed. (high)
- Hand-off = **requirements allocation** (or baselining then allocation). (high)
- Ladder: CMMI REQM SP1.4 asks for bidirectional traceability; storing one direction and traversing for the other is how mature tools (DOORS, Polarion) do it. Mid-ladder, sound. (medium)
- Known failures: **trace decay** — links rot because nobody is paid to maintain them (Cleland-Huang); links made for compliance and never read; granularity mismatch between rows and design units. (high, as practice knowledge)
- Evidence: Rempel & Mäder (2017) — traceability completeness correlates with fewer defects. Correlation, not proof of payoff. (medium)

**2. Systems/design engineering — means-ends hierarchies** (Suh's axiomatic design, QFD, Rasmussen's abstraction hierarchy)
- Mapping: purpose rows ≈ functional requirements; building questions ≈ design parameters; pains → causes → answers is a QFD whats/hows cascade. (medium)
- Back-reference = a cell of Suh's **design matrix** (FR→DP), or the **"why" link** of a means-ends hierarchy: up answers *why*, down answers *how*. (high)
- Hand-off = Suh's **zigzagging**: choose a DP for an FR, then decompose the FR again in light of that DP, iterating between domains. A one-shot crossing that closes the purpose question is the less mature version. (medium)
- On the coupling worry: Suh's **coupled design** and the independence axiom are the test. Rasmussen would say purpose and building are one hierarchy at different abstraction levels; splitting them into two trees is a chosen cut, and the cross-link is its price. (medium)
- Known failures: QFD matrices bloat, are filled once and abandoned. (medium)
- Longevity: means-ends reasoning is still taught everywhere; the independence axiom is a principle, not evidence. (high)

**3. Product management — discovery → delivery** (Torres's Opportunity Solution Tree, Adzic's Impact Mapping, dual-track agile)
- Mapping: outcome = the project's purpose; opportunities = pains/causes; solutions = answer rows; delivery = building. (high)
- Back-reference = Impact Mapping's **deliverable→impact** link, or a portfolio tool's **parent link / roll-up** (epic→initiative→objective). (high)
- Hand-off = the **discovery-to-delivery hand-off** — which Cagan and Torres criticise as an antipattern ("throwing over the wall"); they favour continuous, overlapping tracks. (high)
- Ladder: the shape sits on the "output" rung. Its answer states record **shipped**, not **pain relieved**; outcome-focused practice adds validation — did the cause go away? (high)
- Known failures: the **feature factory** — shipped answers mistaken for relieved pains; solution trees that go stale once delivery starts. (medium)
- Evidence: almost entirely practitioner literature. (high that this is so)

**4. Design science research — Hevner's three cycles** (2004, 2007)
- Mapping: purpose = **relevance cycle** (environment, problems, opportunities); building = **design cycle** (build/evaluate); landscape = **rigor cycle** (knowledge base of methods and prior artefacts). The closest established precedent for the three-way split. (medium-high)
- Back-reference: Hevner has no named link; relevance is a property of the artefact, not a pointer. (medium)
- Hand-off: requirements enter the design cycle from relevance, and **field testing returns** to it — the cycles return results to their source; this shape's hand-off has no return path. (high)
- Ladder: Hevner's guidelines require evaluation inside the design cycle; the shape has no evaluation step. (high)
- Known failures: weak relevance return; a ritual "rigor" survey bolted on. (medium)
- Longevity: still widely taught in IS; a framework, not evidence. (high)

**5. Design rationale / argumentation** (Rittel & Kunz's IBIS, gIBIS, Compendium, MacLean's QOC, Nygard's ADRs)
- Mapping: the question tree is an **IBIS issue map**; closing with a pointer = an issue resolved by a chosen **position**; decisions landing in documents = ADRs. (high)
- Back-reference = gIBIS's **"is-suggested-by"** (a new issue suggested by a position), or **generalizes/specializes**. (medium)
- Hand-off = **a position spawning new issues** — routine in IBIS, not a special cross-module crossing. (medium)
- Ladder: IBIS was designed as a *graph* for wicked problems; a strict tree is a simplification, and multi-parent issues are the first thing to break it. (high)
- Known failures: the **capture problem** — rationale is costly to record and benefits someone else later (Grudin's asymmetry; Buckingham Shum & Hammond 1994); maps become write-only. (high)
- Evidence: thin and mixed for rationale capture; lightweight ADRs survive because they are cheap. (medium)

**6. Software architecture — modularity and bounded contexts** (DDD, plugins, AOP, CQRS)
- Mapping: modules = **bounded contexts / plugins**; the purpose module installing rules into the building module's procedures = **extension points / hooks**, at the limit **aspect weaving**; the derived answer state = a **read model / projection** (CQRS). (medium-high)
- Back-reference = a **foreign key held by the downstream context** — a data dependency of building records on purpose records even when no code depends on purpose. Standard remedies: an **opaque correlation id / tag** the building side stores without interpreting; an **upstream-owned association** (the purpose module keeps the link table); an **anti-corruption layer**. (medium)
- Hand-off = a **domain event** ("AnswerChosen") consumed downstream. (medium)
- Known failures: obliviousness in AOP produces invisible coupling and **feature interaction** (Filman & Friedman's quantification/obliviousness debate); plugins that rewrite their host's procedures are the classic hard-to-reason-about case. (medium)

**7. Organisational design — functional vs cross-functional structure, Conway's law**
- Mapping: modules owning roots = **functions owning domains** (product, engineering, research — the "product trio"). (medium)
- Hand-off = the **functional hand-off**, the best-documented coordination loss in organisational design; Conway's law predicts the module boundary will show up as a seam in the work. (medium)
- Counter-pattern: cross-functional ownership of a question from *why* through *built*. (medium)

### What the tasking smuggled in

- **Tree, not graph.** Rows already address several causes; a building question may realise several rows, and one row may need many building questions. The single-parent tree plus one back-reference is a choice the brief treats as given.
- **Roots as partitions rather than viewpoints.** In ISO 42010 terms purpose, structure and landscape may be *concerns every question has*, not bins each question falls into. Hevner treats them as interacting cycles, not territories.
- **"Owned by a module"** merges three things: who owns the questions, who owns the documents, who owns the procedures.
- **"Present" as the end state.** None of the families stops at "built"; the shape lacks evaluation against the pain.
- **Coupling framed as the main risk.** The families' recorded failure is link decay and capture cost — nobody maintaining or reading the links. Code-level coupling is secondary.
- **"Is there a better-known concept for the back-reference"** assumes one thing to name. There are two: a *trace link* (this realises that row — a standing claim to check) and a *provenance link* (this was spawned by that decision — history). The hand-off produces both, and they behave differently over time.
- **"The building module must not depend on purpose"** assumes the reference must be typed; an opaque "realises: <ref>" field removes most of the puzzle.
- **Self-study swaps in a learning module "instead of" purpose.** Learning objectives *are* a purpose; it may be a specialisation of the purpose module, not an alternative to it.
- **Three as the right number** comes from the seed, not an argument; Hevner gives independent precedent, not evidence of fit.

### Nothing to take

- CMMI maturity-level numbering, DOORS-style link-type taxonomies, DO-178C certification ceremony — costs of a regulated setting this is not in.
- Suh's mathematical design-matrix treatment (information axiom, quantitative tests).
- QFD's full House of Quality roof.
- Hevner's guidelines as publication criteria.
- None of these families offers evidence that a question tree outperforms other forms for steering AI agents — only principles with continued life: means-ends reasoning, bidirectional traceability, keeping rationale capture light, and closing the loop with evaluation.
