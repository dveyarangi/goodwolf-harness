# Outside view — going over produced work again, 2026-10-05

Requested during the align on what holds a tree's invariants and who checks them, after the user
said that judging is not an instance but a method — a second pass on the same object under mostly
different rules and data — and doubted that *judge* is the umbrella term. This is material, not a
verdict.

The separate agent received no conversation history and was told not to read the repository. Its
task described the shape as a produced thing — a text, a plan, a change to a codebase, an answer,
or the whole state of a body of files — gone over again afterwards by the same worker, another
worker, an automated routine or a person, with mostly different criteria and information than the
producing act had, so that defects are found and the thing is corrected or sent back. Transmitted
deliberately, and named to it as such: that five instances are one shape — a periodic sweep
repairing what earlier workers left inconsistent, a check of a finished change against what it was
to achieve, going over a plan several times, a language model assessing another's output, a human
who accepts, rejects or corrects; three sorts of defect — a condition that should always hold, the
manner of expression, a general value not honoured; that a few conditions are checked by a
program and most need reading for meaning; and the setting, software development by LLM agents
under written instructions with a human in the loop. It was asked for several families with each
family's own vocabulary, ladder, known failures and confidence per claim, a survey of the terms in
use in LLM and agentic systems and whether any is an accepted umbrella, and what the tasking
smuggled in. It reported four web searches; everything else is from its own knowledge. The words
the tasking avoided were *judge*, *review*, *verify*, *maintain* and *invariant*. The output
follows verbatim.

## Families

Confidence tags: H = high, M = medium, L = low. "Principle" marks a long-lived general claim; "Evidence" marks a recent LLM-agent finding.

### F1. Software verification and validation (V&V), reviews and inspections

**Mapping.** A work product is examined after production against something outside the producing act: its spec, standards, or user need. Defects are logged and the product is reworked.

- **(a) Act:** verification ("built it right", against the spec) and validation ("built the right thing", against need), per Boehm and IEEE 1012. Subtypes: review, walkthrough, technical review, inspection (Fagan), audit (IEEE 1028), static analysis, testing, regression testing. A sweep over an aged codebase is called maintenance, refactoring, or paying down technical debt, and is not usually called V&V at all. H
- **(b) Performer:** reviewer, inspector, moderator, tester, QA; "independent V&V" (IV&V) when organisationally separate; linter, static analyser or CI for the mechanical part. H
- **(c) Criteria:** requirements, acceptance criteria, coding standards, checklists, invariants and assertions, "definition of done". Tests need an oracle; the "oracle problem" names the case where no mechanical oracle exists. H
- **(d) Outcome:** defect or finding with severity; a disposition of accept, accept with rework, or re-inspect; pass/fail; approve or request changes. H
- **Ladder.**
  - Below: ad hoc self-check and desk-checking.
  - Middle: informal peer review, then checklist-driven review, then formal inspection with roles, entry and exit criteria, and defect data fed back into the process.
  - Above: IV&V, and formal verification by proof or model checking.
  - The described shape (mixed performers, mostly meaning-based, a little automated) sits between informal peer review and checklist inspection, with a thin static-analysis layer. M
- **Known failure modes (principle).**
  - Reviewers find fewer defects as size and speed rise; inspection-rate limits come from Fagan and the later SmartBear/Cisco data. H
  - Review catches style and maintainability issues more than deep functional defects (Bacchelli and Bird 2013; Mäntylä and Lassenius). H
  - An author reviewing their own work repeats the same misreading; independence is the stated remedy. H
  - Rubber-stamp approval. H
  - Verification passes while validation fails, when the spec itself is wrong. H
  - Tests written by the author of the code share the author's misunderstanding. H
- **Disagreement inside the family.** The family treats verification, validation and maintenance as different activities with different triggers. It would not call the periodic sweep and the post-change check one thing.

### F2. Manufacturing quality: inspection, QC, QA, TQM and lean

**Mapping.** A produced unit is examined after the producing operation against a specification. Nonconforming units are reworked, scrapped or returned.

- **(a) Act:** inspection, quality control, quality audit. In-process versus final inspection; source inspection (Shingo). H
- **(b) Performer:** inspector, QC department. Under jidoka, the operator or the machine itself stops the line. Poka-yoke devices do mechanical checking. H
- **(c) Criteria:** specification and tolerance, acceptance sampling plans (AQL), control limits. Juran separates "conformance to specification" from "fitness for use"; Garvin adds further definitions of quality. H
- **(d) Outcome:** conforming or nonconforming; accept, reject, rework, scrap, or concession ("use as is"); a nonconformance report; corrective and preventive action (CAPA). H
- **Ladder.**
  - Inspection (sort good from bad afterwards).
  - Quality control (measure, with statistical process control).
  - Quality assurance (a system that prevents defects).
  - TQM and continuous improvement (defects are treated as information about the process, and the process is fixed).
  - The described shape is mostly the bottom rung, inspection plus rework. It rises a rung only if findings change how production is done. H on the ladder, M on the placement.
- **Known failure modes (principle).**
  - Deming: "cease dependence on inspection"; quality cannot be inspected in. H
  - 100% human inspection is well short of 100% effective. Juran's figure of roughly 80% is often quoted; the exact figure is M.
  - Adding inspectors diffuses responsibility: each relies on the other, upstream and downstream. H
  - Inspection hides process defects by fixing the unit and not the cause. H
  - Cost-of-quality: a defect costs more the later it is caught. H
  - The 1-10-100 figure itself is folklore-grade. L
- **Disagreement with F1 and F3.** This family holds that after-the-fact going-over is the immature form and that mature systems shrink it. F3 holds that independent after-the-fact review is the mature form.

### F3. Audit, assurance and internal control

**Mapping.** An asserted state (accounts, a process, a body of records) is examined by a party with different information and incentives than the preparer, against stated criteria. Exceptions are reported and remediation is required.

- **(a) Act:** audit, review, examination, assurance engagement, attestation, reconciliation, monitoring. Controls are preventive, detective or corrective, and the shape is the detective-plus-corrective pair. "Continuous auditing/monitoring" names the automated form. H
- **(b) Performer:** auditor (internal or external), reviewer, checker. "Maker-checker", the "four-eyes principle" and "segregation of duties" are related controls. The "three lines" model has management self-check, then a risk and compliance function, then independent internal audit. H
- **(c) Criteria:** "suitable criteria" (ISAE 3000), standards, policies, control objectives, assertions (completeness, accuracy, existence and so on), materiality thresholds. H
- **(d) Outcome:** findings, exceptions, deficiencies (ranked as deficiency, significant deficiency, material weakness). The opinion is unqualified, qualified, adverse or a disclaimer. A management letter follows, and remediation is tracked to closure. H
- **Ladder.** The assurance level rises from agreed-upon procedures (no opinion) to review (limited or negative assurance) to audit (reasonable assurance). Separately, COSO-style control maturity runs ad hoc, repeatable, documented, monitored, optimised. A human who "looks and accepts" is at about the review or limited-assurance level. A sweep with repair is a detective and corrective control with no opinion issued. M
- **Known failure modes (principle).**
  - Independence threats: self-review, familiarity, advocacy, self-interest and intimidation, as in the IESBA code. The self-review threat is named exactly. H
  - Expectation gap: users read "reviewed" as "correct". H
  - Sampling risk. H
  - Checkbox compliance, which is form over substance. H
  - The auditor relying on the auditee's own evidence. H
  - Control fatigue and override. H
  - "Who audits the auditor": a regress handled by standards and oversight bodies, never eliminated. H
- **Disagreement inside the family.** The auditor classically does not correct the thing, because correcting impairs independence. The described shape merges finder and fixer.

### F4. Editing, refereeing and peer review

**Mapping.** A text produced by an author is gone over by others under criteria that differ by pass. It is corrected or returned to the author.

- **(a) Act:** publishing has named passes with different criteria: developmental or substantive editing (does it do its job), line editing (manner of expression), copyediting (consistency, house style, correctness), proofreading (the final mechanical pass), and fact-checking. Scholarship has peer review or refereeing. Authors call their own pass revision. H
- **(b) Performer:** editor (of each kind), copyeditor, proofreader, fact-checker, referee or reviewer, the author revising; spellcheck or style linter for the mechanical part. H
- **(c) Criteria:** house style and style guide, editorial standards, journal scope, novelty, soundness, clarity. H
- **(d) Outcome:** marked-up copy, queries to the author, a reader's report; accept, minor revision, major revision ("revise and resubmit"), or reject. H
- **Ladder.**
  - Self-revision.
  - A second reader.
  - Staged editorial passes from substance down to mechanics.
  - Blind or multiple refereeing.
  - Post-publication review, replication and errata.
  - The order of passes is itself a rule: substance before surface, because surface fixes are wasted on text that will be cut. H
- **Known failure modes (principle).**
  - Authors cannot see their own errors because they read what they meant; time delay and a change of medium partly help. H
  - Referee agreement is low. H
  - Peer review detects planted errors poorly (the BMJ studies by Godlee and by Schroter). H
  - Reviewers substitute their preferences for the stated criteria. H
  - Over-editing introduces errors and flattens voice. M
  - Endless revision cycles with no convergence criterion. M
- **Note.** This family already separates the three sorts of defect the tasking named, as value or purpose (developmental), manner (line and copy) and invariant (copy and proof). It treats them as different passes done by different people in a fixed order, not as one act.

### F5. Control theory and cybernetics (feedback regulation)

**Mapping.** The output of a process is sensed, compared with a reference, and the difference drives correction. The sensor path is distinct from the forward path.

- **(a) Act:** feedback: measurement, comparison, error correction. In software operations this is reconciliation, as in a control loop driving observed state toward desired state. H
- **(b) Performer:** sensor plus comparator plus controller or regulator. The human case is a supervisory controller (Sheridan). H
- **(c) Criteria:** reference, setpoint, desired state; in cybernetics the "essential variables" to be kept in bounds (Ashby). H
- **(d) Outcome:** an error signal leading to a control action or correction. H
- **Ladder.**
  - Open loop (no check).
  - Closed loop with a single sensor.
  - Feedforward plus feedback.
  - Cascaded and hierarchical loops, with slow outer loops setting references for fast inner ones.
  - Adaptive control, where the loop modifies the controller itself; this is double-loop learning in Argyris's management translation.
  - The described shape is closed loop with several heterogeneous sensors. The periodic sweep is a slow outer loop. M
- **Known failure modes (principle).**
  - Requisite variety (Ashby): a regulator cannot correct disturbances it cannot distinguish. H
  - The good-regulator theorem (Conant and Ashby): the regulator needs a model of what it regulates. H as a citation, M as to how much the theorem strictly proves.
  - Delay in the loop causes oscillation: fix, counter-fix, churn. H
  - Sensor noise is treated as signal, giving over-correction. Deming's funnel experiment calls this "tampering". H
  - Measuring a proxy and not the essential variable: Goodhart's and Campbell's laws. H
  - Gain too high gives instability; too low gives drift. H
- **Disagreement with F3.** Control theory has no concept of independence. The sensor merely needs to be accurate, and who owns it is irrelevant. Audit says ownership is the point.

### F6. Safety engineering and human-reliability practice (defence in depth, independent checks)

**Mapping.** An action or product is re-checked by a separate barrier before its consequences reach the world. Each barrier is imperfect, and they are layered.

- **(a) Act:** independent verification, double-check, cross-check, challenge-and-response, checklist, monitoring, surveillance testing, safety review, hazard review. H
- **(b) Performer:** second checker, monitoring pilot, independent verifier, safety officer; interlocks and automatic protection for the mechanical part. H
- **(c) Criteria:** procedures, limits and operating envelopes, checklists, safety requirements. H
- **(d) Outcome:** catch or trap of an error; stop, hold or go; a deviation report. H
- **Ladder.**
  - Reliance on operator vigilance.
  - Checklists.
  - Independent double-checks.
  - Engineered interlocks and forcing functions.
  - Designs that remove the hazard.
  - This is the "hierarchy of controls". Human checking is the weak lower end and mechanical forcing the strong upper end. H
- **Known failure modes (principle).**
  - Swiss-cheese alignment of holes (Reason). H
  - Common-mode or common-cause failure: redundant checkers that share training, information or assumptions fail together, so redundancy without diversity buys little. H
  - Human double-checks are not independent in practice; the second checker sees what the first asserted. Medication-safety literature (ISMP) supports this. H
  - Automation bias and complacency toward a usually-right automated producer (Parasuraman and Riley; Bainbridge's "Ironies of Automation", 1983). H
  - Vigilance decrement in low-defect-rate monitoring. H
  - Risk compensation: producers take less care when they know a check follows. M
  - Alarm fatigue from false positives. H

### F7. Generate-and-test, prover-verifier and actor-critic (computing and ML theory)

**Mapping.** One component proposes a candidate and a separate component with a different function evaluates it. The evaluation accepts, rejects or drives revision.

- **(a) Act:** test (in generate-and-test, Newell and Simon), verification (complexity theory), criticism or evaluation (actor-critic), discrimination (GANs). In search the related terms are pruning and selection. H
- **(b) Performer:** tester, verifier, critic, discriminator, oracle. H
- **(c) Criteria:** a goal test or predicate, a value function, a proof checker's rules, a learned decision boundary. H
- **(d) Outcome:** accept or reject, a value or advantage estimate, a gradient or feedback, a counterexample (in CEGIS, counterexample-guided synthesis). H
- **Ladder.**
  - A verifier that is sound and cheap (proof checking; the NP asymmetry that checking is easier than finding).
  - A verifier that is probabilistic (interactive proofs).
  - A verifier that is learned and fallible (critic, discriminator).
  - A verifier that is the same model as the generator.
  - Rigor falls as the verifier loses soundness and independence from the generator. The described shape, mostly meaning-reading with a few programmatic checks, sits low: mostly unsound, learned verifiers, with a thin sound layer. M
- **Known failure modes (principle).**
  - The benefit rests on verification being easier or more reliable than generation; where it is not, the loop adds nothing. H
  - A generator optimised against a fallible critic learns the critic's blind spots (adversarial examples, mode collapse, reward hacking). H
  - A critic trained on the generator's own distribution shares its errors. M
- **Disagreement with F4 and F6.** This family says a same-substrate verifier can still be valuable if the checking task is intrinsically easier. F6 says same-substrate checking is common-mode and nearly worthless. Both positions are live in the LLM literature below.

### F8. Formative assessment and revision research (education, writing studies, metacognition)

**Mapping.** Produced work is compared with a standard by the learner or another person. The gap is identified and action closes it.

- **(a) Act:** assessment (formative versus summative), feedback, marking or grading, self-assessment and peer assessment. In writing research: reviewing, split into evaluating and revising (Flower and Hayes 1981). In metacognition: monitoring and control (Nelson and Narens). H
- **(b) Performer:** assessor, marker, examiner, peer, self; moderator, who checks the markers. H
- **(c) Criteria:** standards, rubrics, criteria, exemplars. Sadler (1989) is explicit that many standards cannot be fully stated as rules and are carried by exemplars and connoisseurship ("guild knowledge"). H
- **(d) Outcome:** grade or judgement (summative); feedback that closes the gap (formative). H
- **Ladder.**
  - Unaided self-check.
  - Rubric-guided marking.
  - Double marking.
  - Moderation and standard-setting across markers.
  - On a separate axis: from summative-only to formative use. M
- **Known failure modes (principle).**
  - Sadler's three conditions: the reviser must hold a concept of the standard, be able to compare the work with it, and have a repertoire of moves to close the gap. Feedback fails when any is missing. H
  - Novice revisers fix surface features and leave meaning-level problems (Sommers 1980; Faigley and Witte). H
  - Poor self-monitoring correlates with poor performance; self-assessment is least reliable where competence is lowest. M, since the size and reading of the Dunning-Kruger effect are disputed.
  - Rubrics narrow what gets attended to; "criteria compliance" replaces quality (Torrance). M
  - Inter-rater unreliability, halo effects, leniency drift. H

### F9. Appellate and judicial review (law)

**Mapping.** A decision produced by one body is gone over by another, under a defined standard and on a defined record, and is affirmed, corrected or sent back.

- **(a) Act:** review, appeal, judicial review. H
- **(b) Performer:** the reviewing or appellate court or tribunal. H
- **(c) Criteria:** the "standard of review": de novo (decide afresh), clear error, abuse of discretion, reasonableness. Separately, the "scope of review", meaning which questions and which record. H
- **(d) Outcome:** affirm, reverse, vacate, modify, or remand (send back with instructions). H
- **Ladder.** By intensity of review, from deferential to de novo. The family's distinctive content is that how hard the second look should be is a decided, stated variable per kind of question. It also has a harmless-error doctrine: a defect that did not affect the result does not trigger correction. H
- **Known failure modes (principle).**
  - A reviewer substituting its own judgement where it should defer, and the reverse. H
  - Review limited to the record misses what the record omits. H
  - Endless relitigation without finality rules (res judicata). H
- **Mapping limit.** The reviewer here typically has less information than the producer (the record only). The tasking said "different" information, so the mapping holds, but in the opposite direction from F3.

### F10. Data integrity and storage maintenance (partial mapping, stated)

**Mapping.** This covers only the "always-must-hold condition" defect sort and the periodic-sweep instance. A stored body of state is scanned against declared invariants and repaired.

- **(a) Act:** integrity or consistency check, scrubbing, anti-entropy or read repair, reconciliation, garbage collection, fsck, vacuum. H
- **(b) Performer:** checker, scrubber, repair daemon, collector. H
- **(c) Criteria:** integrity constraints, invariants, checksums, schema. H
- **(d) Outcome:** a repair, a quarantine ("lost+found"), or a report of unrepairable corruption. H
- **Ladder.**
  - No checking.
  - Offline periodic check and repair.
  - Online background scrubbing.
  - Constraints enforced at write time, so violation is impossible.
  - End-to-end checksums.
- **Known failure modes (principle).**
  - Repair that guesses can destroy the only good copy. H
  - A checker enforcing a stale invariant damages valid data. H
  - Sweeps racing live writers. H
  - Periodic repair masks the writer bug that keeps causing the damage. H
- **What it does not cover.** Manner of expression and unhonoured values; nothing here is read for meaning. It contradicts the tasking's premise that the sweep and the human review are one shape. In this family the sweep belongs with constraint enforcement, not with review.

### F11. LLM and agentic systems: terminology survey (last two years)

**Terms in use, by how I judge their spread.**

Dominant:
- **Evaluation / "evals"; evaluator; grader.** The broadest ML term. Primarily it means measuring a system across many cases offline. It is increasingly also used for per-output runtime scoring. Vendor documentation speaks of code-based, model-based and human graders. H on dominance; M on the grader taxonomy as I recall it.
- **LLM-as-a-judge / judge model / autorater.** The dominant term for one model assessing another's output (Zheng et al. 2023 onward). It has a large bias literature. "Agent-as-a-judge" is a narrower 2024-2026 extension. H
- **Guardrails.** Dominant for runtime checks that block or redirect. Its connotation is safety and policy, usually on inputs, outputs or tool calls, more than work quality. It is used in vendor SDKs and several products. H
- **Human-in-the-loop (HITL), human oversight, approval, review gate.** Dominant for the human instance. "Human oversight" is also the regulatory term (EU AI Act, Article 14). H
- **Reflection / self-reflection / self-critique / self-correction / self-refine.** Dominant in the agent-pattern literature for the same model going over its own output. Sources: Reflexion (Shinn et al. 2023), Self-Refine (Madaan et al. 2023), and Andrew Ng's 2024 "four agentic design patterns", which popularised "reflection". H
- **Verification / verifier / "verify your work".** Common in coding-agent practice and in reasoning research. H

Narrower:
- **Generator-critic, actor-critic, review-and-critique, maker-checker.** Multi-agent pattern names. A 2026 pattern-taxonomy paper lists generator-critic with self-, cross-model and tool-grounded variants (seen in a search snippet only). M
- **Chain-of-Verification** (Dhuliawala et al. 2023) and **CRITIC** (Gou et al.). These are paper-specific method names. H
- **Multi-agent debate.** A research line. H
- **AI code review / review agent / reviewer subagent.** Coding-specific. H
- **Trusted/untrusted monitoring, monitor, scalable oversight.** The AI-safety and "AI control" literature. This is adversarial framing, where the producer may be misaligned. H
- **Plan review / plan critique.** There is no stable term for going over a plan repeatedly; I know of none. L

Vendor-, author- or paper-specific:
- **Evaluator-optimizer.** Anthropic, "Building effective agents", December 2024. Widely copied in tutorials. H
- **Harness engineering.** 2025-2026 coinage for the environment around a coding agent. Used by OpenAI, Thoughtworks/Böckeler, Osmani, HumanLayer and others. H that the term is current.
  - Böckeler's formulation, as I recall it, splits controls into feedforward "guides" and feedback "sensors", each either "computational" (deterministic) or "inferential" (model-based). M; I did not re-open the article.
- **Back-pressure.** Typechecks, tests and lints wired to push failures back into the agent loop. Associated with Geoffrey Huntley's "Ralph" writing and repeated in harness-engineering posts. M
- **Garbage collection / entropy management / doc-gardening agents.** OpenAI's 2026 harness-engineering write-up uses these for periodic agent sweeps that repair drift. This is the closest named match to the tasking's "periodic sweep". M; from memory.
- **Loop engineering.** A search snippet attributes it to Osmani, June 2026: an outer system that hands out work and has a second agent check the result. L; snippet only.

**Is there an accepted umbrella over all listed instances, including the human and the mechanical program?** I found none. The candidates each fall short:
- "Evaluation" is the widest in ML. It connotes measurement of a system, not correction of an instance, and practitioners do not normally call a human approving a PR or a repair sweep an "eval".
- "Verification" covers the post-change check, the program and the judge. It is not normally used for style passes or periodic sweeps.
- "Feedback loops" or "sensors" (harness engineering) is the only current scheme I know that deliberately puts deterministic programs, model reviewers and humans in one category. It is one author-cluster's vocabulary, not accepted usage. M
- "Oversight" covers human and monitor. It connotes authority and safety, not copy-level correction. One search-engine summary asserted the field is "converging on oversight as the umbrella term"; that was the summariser's inference from vendor blogs, and I do not hold it as supported.
- "Review" is the ordinary-language umbrella and is used for all five instances informally. It has no technical definition in this literature.

Confidence that no umbrella is accepted: M-H. Absence is hard to prove; this rests on the survey above.

**Evidence (recent, LLM-specific) versus principle.**

Evidence:
- Self-feedback without external grounding often fails to improve reasoning outputs and can degrade them (Huang et al. 2023/ICLR 2024, "Large Language Models Cannot Self-Correct Reasoning Yet"). The survey by Kamoi et al. (TACL 2024, "When Can LLMs Actually Correct Their Own Mistakes?") finds self-correction works mainly when reliable external feedback is available or the task suits verification. H
- LLM judges show self-preference, and also position and verbosity bias (Zheng et al. 2023; Panickssery et al. 2024; Wataoka et al. 2024, arXiv 2410.21819, which links self-preference to low perplexity, meaning familiarity). 2026 titles extend this to model-family preference (arXiv 2609.17857; title and snippet only). H for the 2023-24 findings, L for the 2026 ones.
- Tool-grounded feedback (tests, typecheckers, linters) improves coding-agent outcomes. This is widely reported in practice write-ups and consistent with Kamoi et al.; it is mostly practitioner testimony, not controlled study. M
- Long-running agent loops can mistake stagnation for progress under self-evaluation (arXiv 2607.25152; title only). L
- A precise reviewer agent does not guarantee the producer takes up its critique (arXiv 2607.15388; title only). L
- Human oversight of coding agents is capacity-limited and fatiguing (arXiv 2606.08919 and 2606.05391; titles only). L from these sources. The principle is H from F6.

Principles the LLM literature re-derives rather than discovers:
- Common-mode failure of same-model review (F6).
- The self-review threat (F3).
- Requisite variety of the checker (F5).
- The verification-easier-than-generation precondition (F7).
- Goodhart effects when the producer optimises to the judge (F5, F7).
- Automation bias in the human reviewer (F6).

**Disagreement kept visible.** Reflection-pattern advocacy (Ng, many tutorials) presents same-model critique as a reliable gain. Huang et al., Kamoi et al. and Kambhampati's group ("LLM-Modulo", 2024) hold that it is unreliable unless the critic is external or sound. Both are current.

Sources used from search (titles or snippets unless noted):
- [A Two-Dimensional Framework for AI Agent Design Patterns](https://arxiv.org/pdf/2605.13850)
- [Self-Preference Bias in LLM-as-a-Judge](https://arxiv.org/pdf/2410.21819)
- [Who Judges Matters: Family-Conditioned Preference in LLM-as-Judge Panels](https://arxiv.org/pdf/2609.17857)
- [Precise but Uncoupled: Reviewer Precision Does Not Guarantee Critique Uptake](https://arxiv.org/pdf/2607.15388)
- [When Do Agent Loops Mistake Stagnation for Progress?](https://arxiv.org/pdf/2607.25152)
- [Agent Harness Engineering (Osmani)](https://addyosmani.com/blog/agent-harness-engineering/)
- [Skill Issue: Harness Engineering for Coding Agents (HumanLayer)](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents)
- [Engineering the harness (Thoughtworks)](https://www.thoughtworks.com/en-us/insights/blog/architecture/engineering-the-harness-a-practical-pattern-for-reliable-coding-agents)
- [Closing the verification loop (Datadog)](https://www.datadoghq.com/blog/ai/harness-first-agents/)
- [Oversight Has a Capacity](https://arxiv.org/pdf/2606.08919)
- [Human oversight of agentic systems in practice](https://arxiv.org/pdf/2606.05391)
- [How to Build Human-in-the-Loop Oversight for AI Agents (Galileo)](https://galileo.ai/blog/human-in-the-loop-agent-oversight)

Everything else in F11 (Reflexion, Self-Refine, CoVe, CRITIC, Zheng, Panickssery, Huang, Kamoi, Anthropic's "Building effective agents", the OpenAI harness post, Böckeler) is from memory.

## What the tasking smuggled in

1. **That it is one shape.** This was declared as transmitted, but its effect is larger than a premise. Several families refuse the unification on their own terms:
   - F1 separates verification, validation and maintenance.
   - F2 separates inspection from process improvement.
   - F3 separates the auditor (who finds) from remediation (who fixes).
   - F4 treats the three defect sorts as different passes by different people.
   - F10 puts the sweep with constraint enforcement, not with review.
   - I produced "families of the whole shape" because I was asked to. A tasking that asked "are these one thing?" would have returned more splits.
2. **"Afterwards" and "gone over again".** The framing is post hoc and detective. It excludes the prevention end that F2, F6 and F10 all regard as the mature rung: write-time constraints, forcing functions, and feedforward guidance (the "guides" half of the guides/sensors scheme). The instructions under which the agents work are the same kind of control in those families, but the tasking places them in "the setting", outside the shape.
3. **"Defects are found and the thing is corrected."** This assumes a defect-finding purpose and merges detection with repair. Other purposes that families attach to the same act were left out: assurance to a third party (F3), authorisation or accountability (F9, human approval), knowledge transfer (the code-review literature finds this is a main real function), learning for the producer (F8), and measurement of the process (F2). An accept/reject by a human may be an act of authority, not of defect detection.
4. **"With (mostly) different criteria and different information."** This is offered as the distinguishing feature. It imports the independence thesis of F3 and F6 as a definition, and it quietly excludes plain re-doing or self-rereading with the same criteria. It is silent on direction: whether the going-over has more information (F3) or less (F9).
5. **The three defect sorts.** The trichotomy of invariant, manner and value reads as a ranked ladder from mechanical to judgemental. It omits at least: factual wrongness, wrong problem solved (validation), incompleteness or omission, and defects in the criteria themselves. It steers toward F4, whose editorial passes match it almost exactly.
6. **The mechanical/non-mechanical split, with "most cannot be checked mechanically".** This is stated as fact. F2, F6 and F10 would treat that proportion as a design variable to be pushed, not a given. Stating it as fixed steered the ladder placements toward "low rung, judgement-heavy".
7. **Performer-neutrality.** Listing "same worker, different worker, routine, person" as interchangeable performers presupposes that who performs it is a parameter and not a kind distinction. F3, F6 and F9 hold that it is a kind distinction (independence, authority).
8. **"One act of work" producing "a thing".** This assumes discrete artefacts and discrete producing acts. "The whole state of a body of files" was produced by many acts over time. Treating it as one "thing" is what lets the sweep sit beside the single-change check.
9. **Vocabulary avoided, and what the avoidance signals.** The tasking carefully says "going over" and never "review", "verify", "maintain" or "evaluate". That is useful hygiene. The instance descriptions still carry the terms in disguise: "what it was supposed to achieve" is verification against a spec, "accepts, rejects or corrects" is a disposition, "a condition that should always hold" is an invariant.
10. **"Families from different fields."** Asking for alternative full accounts presumes each field has one. I may have over-regularised each family into the (a) to (d) grid plus a ladder. The "ladder of maturity" request in particular presumes a single ordered scale. F2's ladder and F3's point in opposite directions about after-the-fact checking, and F9 has intensity levels, not maturity.
11. **Recency rule for evidence, longevity for principles.** This shaped what I counted. Older empirical results (inspection effectiveness, the BMJ peer-review studies) were filed as "principles", though they are evidence, merely not about LLMs.
12. **The setting.** Naming LLM agents under written instructions with a human in the loop made F11 a required family and tilted examples in every other family toward text and code.

## Nothing to take

- **Error-correcting codes and checksums as a full family.** Refused. Redundancy is built into the thing at production time, and detection is purely syntactic. I cannot state a mapping to going-over "with different criteria and information" or to meaning-level defects. The residue is absorbed into F10.
- **Immune system and biological proofreading (DNA mismatch repair, kinetic proofreading).** A mapping exists for invariant-type defects: a separate enzyme rechecks a product using different chemistry. I cannot state one for criteria, outcome vocabulary or the human instance without metaphor. Refused.
- **Signal detection theory.** Not a family of the shape. It is a measurement lens on any checker (hits, misses, false alarms, criterion placement). It has no account of correction or criteria. Usable inside F6 and F11, not alongside them.
- **Scientific method (conjecture and refutation, replication).** Popper's structure maps onto F7's generate-and-test. I found nothing it adds for this shape beyond F4 (peer review) and F7. No separate material.
- **Military after-action review and agile retrospective.** These go over the process to change future work, not the produced thing to correct it. The mapping fails on the object. Refused.
- **Hermeneutics and textual criticism (emendation of corrupted texts).** Suggestive for the periodic sweep, as restoring a text from divergent witnesses. I could not state performer, criteria and outcome terms with confidence. Nothing taken.
- **Regulatory inspection and licensing (building inspection, food safety).** Statable, but it yields the same vocabulary and failure modes as F3 plus F6. No distinct material.
