# Dev harness

The shared development method and the system that delivers, evolves and maintains it across projects and agent frameworks. These initial definitions are a working vocabulary for alignment; proposed distinctions do not independently authorize new process machinery.

## Language

**Harness**:
The development instructions and supporting mechanisms through which projects define, implement, verify and maintain software, including the harness itself.

**Mechanism**:
A behavior on which other work relies, together with its instructions, producers, consumers, checks and records. A mechanism can span several skills and files.

**Skill**:
An invocable instruction part of a mechanism, identified by its purpose and conditions of use.

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

**Unit of work — proposed definition**:
Work with an explicit scale, owner, outcome and completion evidence; a milestone and a ticket can both be units at different scales. The term alone does not specify an agent-sized step; see the [pacer hypothesis](docs/pacer.md#scales-and-steps--revised-hypothesis).

**Execution step — proposed definition**:
A bounded operation or pass on selected work with an input state, immediate purpose, expected result and reassessment boundary. A step may be one skill invocation or a smaller stage within it, and need not complete its owning ticket.

**Archived record**:
A historical account retained after its active role ends, with its disposition explicit. Current work should be understandable from maintained sources without requiring that record; historical investigation and mechanical maintenance may still reach it.

**Ticket**:
A tracked unit of work with an intended outcome and observable completion criteria. It may own unresolved decisions before implementation is ready.

**HITL ticket**:
A ticket whose progress requires a human decision or interaction. Its scope may still be undecomposed, but HITL does not itself specify size or maturity; investigation can reveal a need for a spec and multiple delivery tickets.

**RFC**:
An implementation proposal or agreed plan for an owning ticket, grounded in the governing architecture and contracts. Its existence alone does not mean its proposal has been accepted.

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
