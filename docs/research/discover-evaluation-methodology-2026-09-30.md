# Outside view — evaluation methodology, 2026-09-30

Requested while designing the whole-project evaluation. This is methodological material,
not an evaluation of the project. The user gives personal practical value, readiness for
other people and projects, and research value equal standing.

The separate agent received no conversation history. Its task described the subject as
“an evaluation of a repository-distributed kit of written instructions, persistent work
records, and scripts intended to help coding agents carry software work across sessions
and projects.” It was instructed not to read the repository, skills or earlier reviews;
to give several structurally different evaluation families, evidence and failure modes;
to identify framing transmitted by the task; and to return no project verdict. The
user's three priorities were sent afterward. No repository reads or external research
were reported by the agent. The output follows verbatim.

## Families

Confidence labels concern the proposed evaluation logic, not whether this kit works. No claims below establish the capabilities or limitations of contemporary agents.

**1. A causal intervention.** Treat the kit as a treatment intended to change software outcomes. Compare equivalent work with and without it, controlling or recording model, tools, task difficulty, available context, and human intervention. Measure independently judged correctness, completion, regressions, and total cost. An equally resourced alternative helps distinguish the kit’s particular contribution from the benefit of receiving additional attention or instructions. Useful evidence is a reproducible outcome difference with uncertainty reported; compliance with the kit alone is insufficient. Evaluation fails through unequal baselines, contamination between conditions, selective tasks, or adjusting the kit against its own test set. **Confidence: high** that these controls strengthen attribution; **unknown** effect size, variance, and required sample size.

**2. A continuity and recovery system.** Treat sessions, records, people, and scripts as a system that must preserve justified work through interruptions. Evaluate complete work histories containing handoffs, changed requirements, stale records, interrupted execution, and mistaken prior conclusions. The principal outcomes are recoverability, retained obligations, and the ability to correct an inherited error without perpetuating it. Useful versions recover the intended work and expose unresolved uncertainty at acceptable cost; ineffective versions preserve text while losing its meaning or authority. Evaluation fails when scenarios test only clean restarts, score record completeness as successful recovery, or make deliberately pathological disruptions the whole workload. **Confidence: high** in the distinction between preserving records and preserving usable state; **medium** that any selected disruption set represents ordinary use.

**3. An operational protocol.** Treat the kit as a specification of who or what may decide, act, persist evidence, and resolve disagreement. Evaluate whether its rules produce determinate, acceptable behavior across realistic situations, including conflicting instructions and exceptional cases. Combine static contradiction checks with observed executions: a logically consistent rule may still be unusable in practice. Useful evidence includes correctly resolved cases, traceable authority, and exceptions handled without accidental deadlock. Evaluation fails by treating rule obedience as the ultimate objective, rewarding excessive escalation, or declaring every failure an operator mistake. **Confidence: high** that consistency and execution must be distinguished; **medium** that agreement among reviewers establishes acceptable behavior, since reviewers may share the protocol’s assumptions.

**4. An external memory and evidence system.** Treat the kit as a way of storing, retrieving, revising, and forgetting claims needed for future decisions. Evaluate whether later workers can answer consequential questions from accumulated records, distinguish decisions from proposals, locate supporting evidence, and retire superseded claims. Useful evidence is better downstream judgment with less reconstruction, including correct recognition that an answer is unavailable. Evaluation fails when retrieval of a matching passage counts as understanding, when internally consistent false records receive credit, or when every additional record is counted as improved memory. **Confidence: high** that evidence validity differs from retrievability; **unknown** whether a particular representation improves agent judgment or merely increases reading cost.

**5. A maintained product with adoption costs.** Treat the kit as something projects must install, adapt, operate, upgrade, and possibly remove. Evaluate its total contribution across the lifecycle and across materially different project environments. Include onboarding, human review, maintenance, migration, and opportunity costs alongside delivered software outcomes. Useful versions retain enough benefit after these costs and survive changes without disproportionate repair. Evaluation fails by counting only execution time, averaging away environments where the kit is harmful, or letting successful adopters stand for everyone who attempted adoption. **Confidence: high** that lifecycle accounting changes the evaluand; **medium** that a chosen project sample supports transfer claims.

## What the tasking smuggled in

“Kit” assumes these components form one intervention. “Help” suggests improvement before specifying whose outcomes matter. “Across sessions and projects” combines continuity with portability, which require different evidence. Repository distribution may be incidental packaging. “Coding agents” leaves human participation and responsibility unresolved. Designing evaluation separately from implementation can conceal observability limits. These are hypotheses to make explicit, not premises to inherit.

## Nothing to take

No family establishes that written rules are followed, records remain accurate, scripts improve outcomes, or portability follows from success in one project. None supplies a project verdict. Choosing a family also chooses what counts as success; that choice needs an explicit intended use and beneficiary.
