# The development method

The vocabulary the harness itself is written in — the terms its skills, rules, records and checks
use. It travels with `.agents/`. A project's own domain vocabulary belongs in `docs/glossary.md`,
which the project owns outright; when a term here and a term there collide, the project's wins
inside its own domain and this one wins about the method.

These definitions are a working vocabulary for alignment; a proposed distinction does not by
itself authorize new process machinery.

## Language

**Harness**:
The development instructions and supporting mechanisms through which projects define, implement, verify and maintain software, including the harness itself.

**Mechanism**:
A part of how the work gets done — the development method and its machinery — on which other work relies, together with its instructions, producers, consumers, checks and records. It has exactly one instruction file and may span many other files. What the project produces is not one.

**Skill**:
A mechanism's own instruction file, invocable and identified by its purpose and conditions of use. A skill may also host rules installed into it by mechanisms that do not own it.

**Part**:
A file or asset a mechanism owns: installing the mechanism adds it, uninstalling removes it. What a mechanism leans on but would not take with it is relied-on, named with its owner, and not one of its parts.
_Avoid_: component, piece, asset.

**Moment**:
An occasion at which a person acts on a mechanism. Each is either instructed, or carries a stated kind of absence. If nobody acts, it is not a moment.

**Doc**:
The record of why a mechanism's instruction is what it is. Never the same file as the instruction.
_Avoid_: manual, reference, spec as a name for this.

**Evidence**:
The record of why a doc is what it is: what was tried, what was refuted, what it cost, what it used to be. One per mechanism. Evolution belongs here; provenance does not.
_Avoid_: sidecar, notes, history, appendix. *Sidecar* describes a file's position, never its contents.

**Provenance**:
Who decided a rule and when, carried inline on the rule itself. It is not evidence and does not move to the evidence file: attribution at the moment of reading is what makes a rule challengeable.

**Authority**:
Who may change a rule, and at what strength. Stated on the rule, inline.

**Tier**:
How a thing reaches a session — forced into context, asked for, or reachable only by someone who already knows it exists. Reachability, never importance or read-frequency.

**Index**:
A compact list of a register's records, derived from them on request rather than kept beside them. Enough per record to decide whether to open it, and never a second home for what the record already says.
_Avoid_: digest, summary, table of contents.

**Core**:
The accepted shared method and supporting assets governed at their canonical source.

**Project-local**:
Instructions or assets owned by a consuming project for its particular circumstances. Local ownership alone does not settle precedence when they conflict with core.

**Open issue**:
An unresolved problem, question or risk that needs a disposition. It is unresolved subject matter, not a synonym for a spec, ticket or RFC; its current owning record holds it.
_Avoid_: issue as a generic name for every development document.

**Spec**:
A change-scoped definition of intended capability, scope and governing behavior from which delivery work can be derived. Its enduring agreements belong in maintained governing documents; its eventual historical status does not itself establish that the change was delivered.

**Architecture**:
The maintained description of system responsibilities, load-bearing seams and governing constraints, with the status of current and agreed target behavior explicit.

**Capture**:
Recording an issue with enough context to preserve its meaning and an identifiable owner. Capture does not by itself authorize investigation, implementation or a new mechanism.

**Routing**:
Selecting the existing record or kind of work that should own an issue, and the next applicable development stage.

**Decomposition**:
Dividing agreed work into independently verifiable parts while preserving its scope, contracts and dependencies.

**Pace**:
Which authorized work proceeds now, pauses, or awaits a decision. Pace is distinct from the scale or document type of the work.

**Execution step**:
The execution of a single skill. It has an input state, an immediate purpose, an expected result and a reassessment boundary at its end, and need not complete its owning ticket.

**Turn**:
One agent reply, from the user's message to the reply's end. A turn holds at most one execution step; a step may span turns.

**Archived record**:
A historical account retained after its active role ends, with its disposition explicit. Current work should be understandable from maintained sources without requiring that record; historical investigation and mechanical maintenance may still reach it.

**Ticket**:
A tracked unit of work with an intended outcome and observable completion criteria. It may own unresolved decisions before implementation is ready.

**HITL ticket**:
A ticket whose progress requires a human decision or interaction. Its scope may still be undecomposed, but HITL does not itself specify size or maturity; investigation can reveal a need for a spec and multiple delivery tickets.

**RFC**:
An implementation proposal or agreed plan for an owning ticket, grounded in the governing architecture and contracts. Its existence alone does not mean its proposal has been accepted.

**Shape**:
Whatever is currently under consideration, held between an idea and a thing: it has taken enough form to have a context and a structure, and is not yet exhausted by any one realization. A concept, contract, invariant, behavior, rule, method or artifact can each be held as a shape.

- Idea — "historical forecasts should stay comparable." No form yet; `/align` owns it.
- Shape — "historical forecast issues must remain independently addressable by (location, valid_time, issue_time)."
- Thing — "forecasts are stored in the `forecast_hourly` collection." One realization.

Being a shape says nothing about being load-bearing. An implementation method is a shape, and can be a rich one that repays `/impact` and `/discover`, while remaining local to the code it lives in.
_Avoid_: form, construct, entity.

**Seam**:
A boundary across which a producer supplies behavior, information or an artifact that a consumer relies upon.

**Load-bearing seam — proposed definition**:
A seam across distinct responsibilities whose contract determines a promised outcome, authority, data meaning or integrity, compatibility, or recovery beyond either side's implementation-local choices. A change that appears valid at one end can invalidate the other end or their shared guarantee.

**Rule authority**:
The standing of a rule, including who may establish, amend or waive it. Authority is separate from delivery tier and evidence of effectiveness.

**Strict rule**:
A rule designated as protected by an explicit authority; its amendment or waiver belongs to that authority.

**Meta-rule**:
A rule governing how other rules or mechanisms are created, changed, checked or maintained.

**Tier 1**:
Context supplied to the agent at the relevant occasion without a separate retrieval action. Intended Tier 1 placement and observed delivery are distinct facts.

**Tier 2**:
Content retrieved when a Tier 1 trigger or reference makes it relevant. A request to read content does not itself establish retrieval.

**Rule slice**:
The selected portion of governing instructions relevant to a particular task, stage or event, retaining its source and applicability.

**Delivery evidence**:
An observation supporting that selected content reached the agent's context. It is distinct from a file existing, a hook emitting output, or evidence that the instruction was followed.

**Derived work**:
An artifact or behavior produced or maintained under a governing rule or contract, whose validity may need reassessment when that source changes.

**Reconciliation**:
Resolving differences between independently evolved states against their origins and governing agreements, retaining unresolved differences until they have a disposition.

**Entry contract**:
The instructions every host supplies at session start, versioned, and announced verbatim by the session's first reply as evidence of delivery.

**Autonomy switch**:
A named setting a project gives a value to, deciding whether an action proceeds or waits for a human; skills defer to it.

**Temporary statement**:
An instruction that names the condition on which it expires. Followed until the condition is visibly met, then reported as stale rather than obeyed.
