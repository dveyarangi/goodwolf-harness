# What a record drifting from its thing is an instance of — a `/discover` pass, 2026-10-10

Run at the align on
[q-0037.0010.0009.0005](../questions/done/q-0037.0010.0009.0005-is-a-mechanisms-doc-a-record-of-what-must-always-hold-or-of-what-exists.md),
after the user asked what the kinds of record are for: *the whole idea is to see drift, not to
hang labels for show*. A separate process, forbidden to read this repository, was given the shape
in nobody's vocabulary. **What it was told:** a project kept by a person and an AI agent holds many
text artifacts beside the code (listed by purpose, not by name); two needs — notice when an
artifact and its thing come apart and know which side to correct, and keep an editing agent from
adding what does not belong; one approach tried — a label per artifact for which side leads, in
four values — with the suspicion that it gives a direction but no pair and no detector, and the
instruction to optimise neither for nor against it. It was asked for several families, each with
its mapping, its ladder, its known failures and a confidence per claim, and for what the tasking
smuggled in.

The material follows as it came back, unedited.

---

## Families

Tags: **[P]** is a principle (it still lives: cited, taught, used to decide things). **[E]** is evidence (recent, about text kept alongside code, with agents in the loop where possible). Confidence is H/M/L. A "ladder" is the family's own ordering unless I say I built it.

---

### 1. Software traceability: typed trace links and suspect-link flagging
(Gotel & Finkelstein 1994; Cleland-Huang et al.; the trace-link types of DOORS, Polarion and SysML)

**Mapping.** Each artifact is a node: a requirement, design element, test, code unit or decision. Drift is a change at one end of a trace link that the other end has not yet absorbed. The family stores what the project's labels leave out:
- **Which thing** the text is paired with: the link's endpoints.
- **What kind of pairing** it is: the link type. SysML has «satisfy», «verify», «derive», «refine» and «trace». The direction of authority lives in the link type.
- **What notices**: tools flag a link "suspect" when either endpoint changes, and a human clears it.

The meaning sits on the edge, not on the node. One artifact can lead on one link and follow on another. The project labels nodes, so it sits in a different place.

**Ladder** (the family's own: Gotel et al. 2012, "ubiquitous traceability"):
1. no links
2. ad hoc links in prose
3. links with types declared in a traceability information model
4. automatic suspect flagging on change
5. links recovered and maintained automatically, continuously

The current approach is at rung 1–2. It declares authority per artifact, with no endpoint and no typed edge. (Placement: M)

**Known failure modes**
- Trace decay: links go stale faster than people re-validate them. [P, H]
- Traceability built for compliance and never read ("trace for the auditor"). [P, H]
- Too many links: every edit lights up suspect flags, and people clear them in bulk without reading. [P, M]
- The information model is defined too coarsely, so links exist but carry no semantics. [P, M]

**Evidence**
- 2025 studies of LLM trace-link recovery between documentation and code report F1 of about 0.79–0.80 for the best models (Claude 3.5 Sonnet, GPT-4o, o3-mini). Requirements quality strongly affects recovery. [E, M — benchmarks are documentation↔code, not decision or plan↔code]
- KIT's LiSSA framework (RAG-based) covers requirements→code, documentation→code and architecture documentation→models; gains from context are modest. [E, M]

---

### 2. Architecture conformance: reflexion models and erosion detection
(Murphy, Notkin & Sullivan 1995; Knodel & Popescu 2007; de Silva & Balasubramaniam 2012; fitness functions in Ford, Parsons & Kua)

**Mapping.** The high-level design description and the decision logs are the "high-level model"; the code is the "source model". The reflexion method demands an explicit **mapping** from model entities to code entities. A computation then sorts each relation:
- convergence: in both
- divergence: in the code, not the model
- absence: in the model, not the code

This is exactly "which thing is the text paired with" plus "what notices".

On direction, it disagrees with fixed labels. The reflexion method does not decide which side is wrong. A human judges each divergence, and either the model or the code is updated. [P, H]

**Ladder** (Knodel & Popescu compare reflexion models, relation-conformance rules and component-access rules; later rungs are fitness functions in CI and LLM-checked decisions):
1. architecture prose only
2. prose plus a manual review
3. explicit mapping and a reflexion computation
4. rules checked continuously in CI

The current approach is at 1–2 for the design description and the decision logs. (M)

**Known failure modes**
- The mapping itself decays and has to be maintained. [P, H]
- Checks catch only structural or dependency rules; rationale and quality properties go unchecked. [P, H]
- Erosion goes unseen when the check is not part of the build. [P, H]
- Both the documented and the implemented architecture can be wrong at once. [P, M]

**Evidence**
- Su et al., arXiv 2602.07609 (ICSA 2026): 980 ADRs across 109 repositories. LLMs reach substantial agreement and strong accuracy for explicit decisions that can be read from the code. Accuracy falls short for implicit or deployment-oriented decisions that depend on configuration or organisational knowledge. [E, H that the paper says this; M on transfer]
- "Sentinel" (a CAIS 2026 demo): per-commit agents check against documented decisions; 18 drift instances at 83% true-positive rate across 120+ services. [E, L — a demo, self-reported]

---

### 3. Desired-state reconciliation: control loops and infrastructure-as-code drift
(Kubernetes controllers, GitOps tools such as Argo CD and Flux, Terraform plan/refresh/import)

**Mapping.**
- "The text leads until the thing catches up" is a declared desired state with a reconciler that has not yet converged.
- "The thing leads" is observed state: Kubernetes `status`, or Terraform refresh/import pulling reality back into the text.
- "The text always leads" is a GitOps repository with auto-sync and self-heal.

Every object names its target by identity: a resource address, or a label selector. A specific controller per kind is what notices; Argo CD calls the drift "OutOfSync". [P, H]

One structural difference: the family splits authority **per field within one object** (spec versus status), not per document. A work item that holds both intended outcome and progress would be two things here. [P, H on the K8s design; M on the analogy]

**Ladder** (practitioner-common, not canonical; L–M):
1. no declared state
2. declared state with manual audits
3. drift detection on a schedule, as in `terraform plan` in CI
4. continuous reconciliation
5. auto-remediation, with explicit exceptions such as `ignore_changes`

Labels alone sit near rung 2: direction declared, with no object identity and no controller. (M)

**Known failure modes**
- "ClickOps" drift from changes made outside the declared path. [P, H]
- `ignore_changes` and suppression lists pile up until the declared state is fiction. [P, M]
- Two controllers fight over one field. [P, H]
- Edge-triggered handling misses events, which is why the family prefers level-triggered checks. [P, H]
- Auto-remediation erases a legitimate emergency change. [P, H]

**Evidence on substrate:** none found. The family works on machine-checkable state, not prose. For prose, the reconciler would have to be a reader such as an LLM, which pulls in the false-positive rates under family 5. [Absence of evidence, M]

---

### 4. Bidirectional transformations and model synchronisation
(Stevens 2008/2010; the BX community; Diskin; lenses; round-trip engineering in model-driven engineering)

**Mapping.** Two models, a text artifact and the code, are linked by a **consistency relation R**. Correcting a mismatch means applying a "restorer" in one direction or the other. The project's label chooses which restorer is legitimate ("master/slave synchronisation"). BX theory holds that R is the primary object and direction secondary; without R you cannot even say whether the pair is consistent. This matches the people's suspicion almost word for word. [P, H]

Properties the family names:
- Correctness: a restore yields consistency.
- Hippocraticness: do not touch a pair that is already consistent.
- Least change. [P, H]

**Ladder** (built by me from the family's distinctions; M):
1. implicit relation
2. declared master side
3. declared relation with a checker
4. restorers in both directions with stated properties

Labels are rung 2.

**Known failure modes**
- In master/slave sync, edits made on the slave side are silently lost on regeneration: the "protected regions" problem of round-trip MDE. [P, H]
- A relation over informal prose cannot be fully stated, so the restorer is a human or LLM judgement with no guarantees. [P, M]
- Several models sharing one relation become a megamodel problem; consistency is not pairwise. [P, M]

**Disagreement.** This family treats prose as a weak model and pushes toward formalising R. Families 10 and 13 push the other way.

---

### 5. Living documentation and executable specification
(Martraire, *Living Documentation*; Adzic, *Specification by Example*; BDD; doctest; literate programming at the far end)

**Mapping.** Sort each artifact's knowledge by how stable it is and where it already lives:
- Knowledge already in code is not restated; it is generated from the code ("the thing leads", made mechanical).
- Stable knowledge goes into "evergreen" documents that avoid volatile detail.
- Knowledge that must be duplicated gets a **reconciliation mechanism** (Martraire's term, I recall; M): typically the doc is executed as tests.

The interface descriptions, some of whose stated properties are tested, are this family's rung 3 for those claims and rung 1 for the rest. [P, H for the family; M for the placement]

**Ladder**:
1. prose
2. prose plus review
3. prose with embedded checks: doctests, link checks, BDD scenarios
4. generated from the thing, or executable as the thing

**Known failure modes**
- BDD collapses into test automation that nobody reads. [P, H]
- Brittle doc-tests get deleted rather than fixed. [P, M]
- Generated docs are noise: Javadoc that restates signatures. [P, H]
- Rationale, decisions and history cannot be made executable, so this family leaves them as prose with no mechanism. [P, H]

**Evidence**
- METAMON (LLM4Code at ICSE 2025): 9,482 doc–code pairs; precision 0.72, recall 0.48. [E, M — API docs, not project records]
- DocPrism (arXiv 2511.00215, 2025): plain LLM use yields "unacceptably high" false positives; with filtering, about 15% flag rate and precision 0.62. [E, M]
- CASCADE (2026): LLM-generated tests built from documentation found 13 inconsistencies, of which 10 were fixed. [E, M]

---

### 6. Redundancy, normalisation and event sourcing ("every fact one home")
(Codd's normal forms; DRY; event sourcing; bitemporal data, Snodgrass)

**Mapping.** A text that restates a fact held in code is a **denormalised copy**, and drift is an update anomaly. The family's options are:
- Remove the copy (normalise).
- Derive it: a view, or a generated doc. This is the "thing leads" label as a materialised view.
- Keep it with a synchronisation constraint: a trigger, or a check.

"Neither — it is history" maps to an append-only event log: corrected by appending, never by editing; current state is derived from it. [P, H]

For need 2 the normal-form principle is useful. A fact belongs in the table whose key it depends on ("the key, the whole key, nothing but the key"). Narrative history in a work item is a fact keyed on a session, not on the work item. [P, H for the principle; M for the transfer]

**Ladder** (the normal forms themselves; plus "derived versus stored"). Labels declare which copy is the base table, but they do not enumerate the copies. (M)

**Known failure modes**
- Denormalising "for convenience" without a constraint. [P, H]
- An event log edited in place loses its evidential value. [P, H]
- Over-normalising text forces readers to assemble many fragments, so readability collapses. [P, M]
- Bitemporal confusion: when a fact was true versus when it was recorded. [P, M]

---

### 7. Records management and document control
(ISO 15489; ISO 9001:2015 §7.5; archival diplomatics; the records continuum)

**Mapping.** ISO 9001:2015 splits documented information into what is **maintained**, which is kept current, and what is **retained**, which is fixed evidence. [P, H] The project's four labels collapse to that binary plus a direction:
- "Neither — history" (session journals, closed questions, accepted decisions) is the retained side.
- The other three labels are kinds of maintained document.

Records management adds what labels lack:
- A file plan says, per record series, its function, its required elements and who may change it.
- Diplomatics ties a record's form to the act it records. [P, M]

Need 2 is native here: misfiling, and contaminating a record with material from another function, destroys a record's authenticity and usability. Adding requirements to a session journal is the canonical error. [P, M]

**Ladder.** Retention schedules, file plans and controlled-document procedures (review cycles, approval, revision history). Labels sit before the file-plan rung: a classification with no per-series content rules and no review trigger. (M)

**Known failure modes**
- Editing records after the fact. [P, H]
- Working documents never declared records, so history evaporates. [P, H]
- Retention without disposition, so stale records crowd out current ones. [P, H]
- Periodic review cycles turn into rubber-stamping. [P, M]

**Disagreement.** Here history is not a "neither" category but the most protected one, and fixity is the point.

---

### 8. Accounting reconciliation (book versus bank statement)

**Mapping.** Two independent records of one reality are matched **pair by pair** (this account against this statement) on a cadence, by someone other than the bookkeeper where possible. Every difference is classified:
- **Timing difference** (deposits in transit, outstanding cheques): no correction; it will clear. This is "the text leads until the thing catches up".
- **Book error**: correct the text.
- **Bank error**: correct the thing.

Direction is decided **per discrepancy by classification**, not per ledger in advance. [P, H for the practice; M for the mapping]

**Known failure modes**
- Stale reconciling items that never clear. "Text leads until…" becomes permanent, and old outstanding items are a classic audit flag. [P, H]
- "Plugging" a difference to make totals agree. [P, H]
- The person who keeps the books also does the reconciling, so there is no segregation of duties. Here, the agent that wrote the text also judges its agreement. [P, H for the practice; M for the transfer]

**Ladder.** Manual monthly reconciliation, then automated matching with exception queues, then continuous close. Labels resemble a chart of accounts with no reconciliation procedure attached. (M)

---

### 9. Spec-driven development, the agent-era native account
(Kiro, GitHub spec-kit, Tessl; Böckeler on martinfowler.com, Oct 2025)

**Mapping.** Böckeler's three levels line up almost one-to-one with the labels:
- **Spec-first**: the spec guides one task and is then dropped.
- **Spec-anchored**: the spec persists and evolves with the feature.
- **Spec-as-source**: humans edit only the spec; code is generated and marked "do not edit".

These match "text leads until caught up", a maintained pairing, and "text always leads". [P, M — the taxonomy is a year old; still cited]

**Ladder.** Böckeler finds spec-kit "spec-first only, not spec-anchored". Most tools do not say how specs are maintained over time. [E, M]

**Known failure modes** (all [E, M]: one practitioner's trials, plus a Scott Logic review)
- A "sea of markdown"; review burden: "I'd rather review code than all these markdown files" (Böckeler).
- Non-determinism: the same spec does not reliably give the same code, so the spec's authority is "conventional, not enforced".
- Agents ignored or over-read instructions.
- One heavy process for every size of problem.
- Böckeler warns spec-as-source may repeat model-driven development's failure, with "inflexibility and non-determinism".

---

### 10. Documentation economics: "travel light" and theory-building
(Ambler's Agile Modeling; the Agile Manifesto; Naur 1985 "Programming as Theory Building"; Parnas & Clements 1986 "A Rational Design Process: How and Why to Fake It")

**Mapping**
- Every artifact has upkeep cost against value. Drift is tolerated until a consumer is hurt ("update only when it hurts"; "just barely good enough"). What notices is the reader at use time. [P, H]
- Naur: the real design lives as a theory in people, and text is an aid to rebuilding it, so drift is expected. [P, H]
- Parnas: design documents are kept as an idealised account of the *current* design; history of how it was reached does not belong in them. This bears directly on need 2. [P, H]

**Ladder.** The family rejects climbing. Its maturity is producing fewer artifacts.

**Known failure modes**
- Documentation debt; tribal knowledge lost when people leave. [P, H]
- Specific to the substrate: "update when it hurts" assumes a reader who notices the pain. An agent reader follows stale text confidently. [P, M]

**Evidence**
- Gloaguen et al., arXiv 2602.11988 (ICLR 2026):
  - LLM-generated context files lowered agent task success by about 3% and raised cost by over 20%.
  - Developer-written ones gained about 4% at up to 19% more cost.
  - Agents do follow the files.
  - Unnecessary requirements make tasks harder; the authors recommend minimal content. [E, H]
- Studies of AGENTS.md (arXiv 2510.21413): the files change often, mostly to fine-tune instructions, with no settled structure. [E, M]

**Disagreement.** This is the strongest dissent from families 1–4: more pairing and checking is cost, not maturity.

---

### 11. Agent memory and context retrieval: freshness checked on read

**Mapping.** The artifacts are the agent's long-term memory, and drift is stale memory. Instead of keeping text current on write, this family:
- serves facts from live sources at request time, or
- attaches provenance and validity time to each stored assertion (bitemporal edges in temporal knowledge-graph memories) and re-checks on read.

[P, L–M — the field is young; "principle" status is not yet earned]

**Known failure modes**
- Hand-maintained instruction files "keep confidently stating the old rule". [E, L — vendor blogs: Unblocked, July 2026]
- Several overlapping instruction files drift apart from each other. [E, L]
- Retrieval moves the staleness problem to the index rather than removing it. [P, M]

**Disagreement.** This family relocates noticing from maintenance time to read time. Families 1–8 keep it at write or check time.

---

### 12. Documentation genre typing (need 2 only)
(Diátaxis; rhetorical genre theory: Miller 1984, Yates & Orlikowski 1992)

**Mapping.** An artifact kind is a genre: a typified response to a recurring situation, defined by its communicative purpose. Content belongs when it serves that purpose. Diátaxis's central failure is mixing types, for example explanation leaking into reference or a tutorial turning into how-to. [P, H for Diátaxis being widely used]

The family classifies by **purpose for a reader**, not by authority over a thing. That is a different axis from the four labels. [P, M]

**Known failure modes**
- Type-mixing.
- Genre drift as situations change, so the taxonomy itself must evolve. [P, M]

It says nothing about text↔thing drift.

---

### 13. Legal consolidation (text↔text subset only)

**Mapping.** Decision logs are amending acts; the high-level design description is the consolidated text. In US law the Statutes at Large govern, and non-positive-law Code titles are only prima facie evidence (1 U.S.C. §204). The consolidated text is derived, and the amendments are authoritative until a title is re-enacted as positive law. [P, H for the law; M for the mapping]

**Known failure modes**
- Consolidation lags behind amendments.
- Errors in consolidation.
- The remedy is periodic re-enactment, which makes the consolidated text authoritative and retires the amendments as history.

It covers only pairs of texts, not text against code.

---

## What the tasking smuggled in

- **One artifact, one thing.** "The artifact and the thing it talks about" assumes each artifact has a single counterpart. Many talk about several things, about other artifacts, or about no external thing: the open-questions list tracks a state of knowledge.
- **A binary choice of side.** "Which side to correct" assumes one side is wrong. Families 2 and 8 add "both", "neither — a timing difference" and "the divergence is legitimate". Family 7 adds "the divergence *is* the record".
- **Detection as the bottleneck.** "Notice" presupposes that. Families 9 and 10 locate the cost in review burden and reading.
- **Per-artifact granularity.** Alternatives work per link (1), per field (3), per discrepancy (8) or per claim (5).
- **"Authoritative" vocabulary.** Other families speak of consistency relations (4), desired versus observed state (3), maintained versus retained (7), or cost (10).
- **Two needs posed as separate.** In families 6 and 7 they are one need: where a fact's home is, and whether that home is fixed, decides both drift handling and what may be added.
- **The project's own kinds.** The artifact list is "functional" but still in the project's own decomposition: decisions, plans, journals, questions. Family 12 would divide by reader purpose; family 6 by subject key.
- **The agent cast as editor only.** The framing worries about what the agent adds. The substrate evidence (Gloaguen) is about the agent as a *reader* misled or burdened by text.
- **Co-location as given.** "Plain text in the same repository" is treated as fixed; family 11 questions it.
- **The suspicion pre-states a remedy.** "No pairing, no detector" primes toward families 1–4. Families 10 and 13 would read the same symptom differently.
- **A maturity ladder.** Asking where the approach "sits on a ladder" assumes a progressive ordering. Family 10 rejects it.

## Nothing to take

Considered and refused, or folded in, for want of a statable separate mapping:
- **Version-control merge conflicts.** Text against text of the same artifact, not text against thing. Refused.
- **Cache invalidation.** Maps only the "thing leads" label; folded into 6.
- **Digital twins.** Structurally the same as 3 with physical assets; no extra content. Folded.
- **Map/territory (Korzybski).** Topical; no mechanism for noticing or resolving. Refused.
- **Wiki gardening.** No structure beyond "someone tends it". Refused.
- **Ontology alignment.** Topical neighbour; aligns schemas, not claims with implementations. Refused.
- **Literate programming.** Merging text and code into one artifact; folded into 5 as its endpoint.
- **Lab notebooks / GLP.** Folded into 7.

The pass did return usable material. Direct substrate evidence is thin: one solid study of agent context files (Gloaguen 2026), one of LLM-checked ADRs (Su et al. 2026), and benchmarks for documentation↔code inconsistency and trace recovery. None of it studies project records of these kinds (plans, questions, journals) under agent maintenance.

Sources:
- [Böckeler — Understanding SDD: Kiro, spec-kit, Tessl](https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
- [Gloaguen et al. — Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988v1)
- [Su et al. — LLMs for Detecting Architectural Decision Violations](https://arxiv.org/abs/2602.07609)
- [Context Engineering for AI Agents in OSS](https://arxiv.org/abs/2510.21413v4)
- [METAMON](https://arxiv.org/pdf/2502.02794)
- [DocPrism](https://arxiv.org/abs/2511.00215v1)
- [CASCADE](https://www.citedrive.com/en/discovery/cascade-detecting-inconsistencies-between-code-and-documentation-with-automatic-test-generation/)
- [LLM trace-link recovery](https://arxiv.org/abs/2506.16440v1)
- [LiSSA](https://helmholtz.software/software/lissa)
- [Sentinel architectural governance](https://caisconf.org/program/2026/demos/sentinel-architectural-governance/)
- [Rules-file rot (vendor blog)](https://getunblocked.com/blog/rules-file-rot/)
- [Keeping agent instructions up to date (vendor blog)](https://getunblocked.com/blog/keep-agent-instructions-up-to-date/)
- [Thoughtworks Radar — spec-driven development](https://www.thoughtworks.com/radar/techniques/spec-driven-development)
