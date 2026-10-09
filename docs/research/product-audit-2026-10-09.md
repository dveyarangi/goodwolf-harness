# The product document audited against the tree — 2026-10-09

The audit of [the product document](../product.md) as it stood at `aa54092`, run at the align on
[q-0033](../questions/q-0033-which-pains-of-developing-software-with-coding-agents-does-the-harness-exist-to-relieve-and-what-answers-each.md)
when the user asked whether anything was forgotten. One read-only agent swept the tree in a fixed
order: the skills, the mechanism docs and rules files, the entry file and local rules, the method
glossary, the open questions, and the queue and tickets. It reported in five sections. It read
this repository, so it saw what the agent sees: it is not an outside view.

Kept because the user chose it as the comparison for a future mechanism that generates the
harness's own question tree (q-0018.0011.0004). It is one agent's judgement. The oracle is this
list after the person has ruled on each item.

What the agent checked of it before use, 2026-10-09:

- every question id it cites exists and is open;
- 19 of 24 skills carry `Mechanism: not yet`;
- *one step per reply* appears only in the glossary and `docs/pacer.md`.

Its other status judgements were taken without separate checks.

Filed as it came back, its findings whole. Some items are condensed, and some of the paths and
line numbers the original cited are left out.

---

## 1. Mechanisms in the tree that serve a pain, goal or cause but are missing from the matrix

- **Necessity gate.** `/align` opens by naming the present customer, the observable problem, and why what exists cannot serve it. `/impact` asks whether the change solves a demonstrated problem and whether it can be narrower. `/questions` says "Build X" is a proposed answer to "what is X for?". Serves C3 and pain 2. **✓** (`.agents/skills/align/SKILL.md`, `.agents/skills/impact/SKILL.md`, `.agents/skills/questions/SKILL.md`)
- **Facts are looked up, decisions go to the person.** `/align` also asks one question at a time, each with a recommended answer. This works on both ends of the agency scale. Serves C9 and pain 3. **✓** (`.agents/skills/align/SKILL.md`)
- **Settling a raised question inside the turn.** The rule: look it up first. A decision that does not bear load is settled and reported. One that bears load goes to the person. When unsure, treat it as load-bearing. Serves C9 and C2. **✓** (`.agents/skills/questions/SKILL.md`, "Who settles what is not found"). The matrix credits this routing only to `/impact`.
- **Suspect answers and `depends on`.** When an answer changes, its dependents are marked suspect. The check reports suspects nobody marked, and the wake lists them. `questions.md` says the mechanism "was raised for" this. Serves C6 and G1. **✓**, though the marking itself is the agent's call. (`.agents/skills/questions/SKILL.md` "Closing"; `.agents/scripts/gw/questions.py` `_unmarked_suspects`)
- **Maintenance clock.** Marks plus `maintain.py --check` work out which mechanisms are due for a re-check. Serves C6 and G1. **✓** (`docs/mechanisms/maintenance.md`, `.agents/skills/maintain/MARKS-FORMAT.md`)
- **Archiving finished records.** Rule B3, the paired close by `move_doc.py`, and the store's `done/` folders keep the live working set small. Serves pain 2 and C4. **✓** (`.agents/skills/maintain/SKILL.md`)
- **Pre-registered outside grading.** Every mechanism doc has a section "What would show it working, graded by someone who did not build it", and `/mechanism` Incept step 6 requires it. Serves C7 and G1. **✓** for the 5 declared mechanisms.
- **Guards on the checks themselves.** "Write the check before the thing it checks", watching it fail in both directions. "Absence is not clearance." A run that passes with zero tests is not verification. A fixture must be built the way the real thing came to be. Serves C7. **✓** (`.agents/skills/mechanism/SKILL.md`, `.agents/skills/verify/SKILL.md`)
- **Adversarial planning.** `/plan` asks for "the cheapest real example that could prove this design assumption wrong", probes with counterexamples (empty, partial, raced), and separates sourced facts from assumptions. This guards against C2. **✓** (`.agents/skills/plan/SKILL.md`, `.agents/skills/align/SKILL.md` "Good architecture")
- **Edge records.** Per-surface contract and invariants; customer-facing text derived from them; an unguarded promise flagged. Serves C6 and C10. **◐**: the skill exists, but this tree has no `docs/edge/`; see q-0023.0009 and q-0018.0002.
- **Commit discipline.** Commit only this session's work (C5, G2). Run the project's checks before a code commit (C7). **✓** (`.agents/skills/commit/SKILL.md`)
- **Where knowledge lives.** "Document load-bearing, code&comment the rest", with `/improve-comments` and the `TODO` bindings in `/implement`. Serves C6, C1 and pain 2. **✓**, though the rule is straw-dogged on q-0024.0002.0005.
- **Writes that cannot destroy work (G2).** A refusal writes nothing, and detected interference is a failure, never permission to overwrite (`docs/architecture.md` "Interruption and recovery"; `questions.py` `_declared`). The installer refuses rather than guesses, a hand-edited block is drift, and retraction leaves the file byte-identical. Removing a straw dog needs `--remove … --expect <fingerprint>`. D3: never invent a past fact. push=ask. **◐**
- **"A document informs."** A document never instructs and never authorizes; guards against injected instructions (G2, C1). **◐**, a straw dog in `AGENTS.md`. Its binding to q-0029 (second look) looks wrong.
- **Plain language for the person.** P10: say what a ticket is, with every term explained. `/recall`: "simple but precise language, no moonspeak". L6: emoji glyphs as anchors for thinking. Serves C10 and pain 3. **✓**
- **Every output has a reader.** "Everything a mechanism produces is read by someone, or the doc says why nobody does." Serves pain 2 and C1. **◐**; the full producer/consumer graph is q-0024 / 01-0017.
- **`/skill-up` writing rules.** No overlap, no contradiction, fit the set, no project facts in a body. Serves C1. **✓**
- **`/dream`.** Distils principles and hidden edges from the record. Serves G1 and C7. **◐**: experimental.
- **Four undeclared skills, each ◐:** `/advise` (G1); `/setup-devops`, which creates the toolchain and CI the verification set runs (C7; q-0023.0015, q-0018.0022); `/review-architecture` (pain 1; q-0018.0003.0002); `/celebrate` serves no cause.

## 2. Absent mechanisms the tree already plans or asks about, but the matrix lacks

- **Agent roles** (permissions, rights over the store, skill set): q-0016. Serves G2 and C5.
- **Splitting a question before it is answered:** q-0001.0020, ticket 01-0011.0100.0050. `/impact` recommending the work's shape: q-0018.0001, ticket 01-0010.0080. Serves C2, C3 and C8.
- **Resuming at the step that stopped:** 01-0020 (pacer), q-0027. Serves C4.
- **A resumed conversation keeps its position:** q-0001.0006. Landed for Claude Code only. Serves C4, **◐**.
- **Sessions that do not share one working directory:** q-0018.0015. Serves C5.
- **The queue:** derived from the tickets (q-0020, 01-0011.0040), its order the person's (q-0027). Serves C6 and C9.
- **C1 coherence work:** each skill states only what it owns (q-0023, 01-0016); producers and consumers of every skill and document (q-0024, 01-0017); what notices a new skill a rules file should now name (q-0024.0003); one account of scope (q-0022, 01-0014); a rules-file section names its moment and outcome (q-0028).
- **Terms defined before they land:** q-0024.0001, 01-0017.0010. Serves C3.
- **Links checked outside a close:** q-0024.0005. An edited thing carries its mark back: q-0024.0009.0004, 01-0011.0110.0050. Both serve C6.
- **Tests catch what their names promise:** q-0021, 01-0011.0090. Serves C7.
- **Where a tree's invariants are declared as criteria a pass applies:** q-0029.0005. **Self-amendment** questions: q-0026.0001 and q-0026.0002. Both serve C7.
- **Observing what each host delivers:** q-0018.0004 / 01-0010.0120, and q-0018.0004.0001.
- **Team memory:** "unminted", with no question at all. Every pain is framed for one person.

## 3. Status errors and wrong bindings

- **"One step per reply" ✓ should be ◐.** Only a glossary definition and `docs/pacer.md`. Bind to q-0027 / 01-0020.
- **"Declared and checked mechanisms" ✓ should be ◐.** 5 declared; 19 of 24 skills say `Mechanism: not yet`. A recipient's own mechanisms have no home (q-0018.0019).
- **"A rule on who may change the checks" ✗ should be ◐.** `/verify` already forbids weakening a validator. Bind to q-0018.0022.0001.
- **"G2 has no answer at all" is wrong.** See the guarded writes in section 1.
- **"Each session sees where the others stand" ✓ should be ◐.** Only within one working directory (q-0018.0015).
- **"Neighbourhood handed over before every message" ◐**, partial in this repository too (Cursor at session start only). Add q-0018.0023.
- **"Whether a rule reaches its occasion is observed" ✗ should be ◐.** The announce line and delivery evidence exist. Add q-0018.0004.0001.
- **"A failure traced to its cause" ✗ should be ◐.** The rule-failure register traces failures to the instruction.
- **"`/recall` at every wake, `/conclude` at every end" ✓ is overstated.** The wake rule is a straw dog (q-0027); nothing makes a session end with `/conclude`.
- **"`/maintain` … when what governs them moved" ✓ is partial.** The due list is never announced; links outside a close are not checked (q-0024.0005).
- **"One vocabulary … glossaries" ✓ is ◐ for enforcement.** q-0024.0001.0001, 01-0017.0010.
- **"Every rule at its tier" ✓ is arguably ◐.** q-0025.0002, q-0025.0001.
- **"A task takes its form in its question"** belongs to q-0024.0009.0003.0002 / 01-0011.0110.0040.0020.
- **"Method measured … and its cost counted"**: cost has its own question, q-0018.0008 / 01-0010.0168.
- **"The person choosing which kinds of decision are theirs"** (q-0033.0002) duplicates q-0027.0002 "Which questions stop for a human?".
- **"Its own skills checked like the shipped ones"** is overstated for a recipient (q-0018.0019).
- **The harness-pain open parts omit:** releases (q-0018.0020.0002, 01-0010.0160 / .0185 / .0190 / .0195); reporting upstream (q-0018.0014 / 01-0010.0205, q-0018.0018); arrival harvest (q-0018.0011 / 01-0010.0175); the first install's verification set (q-0018.0020.0003 / 01-0010.0170); harness maintenance in a recipient (q-0018.0012 / 01-0010.0180); a skill name colliding with a project's command (q-0018.0020.0001.0002); changing how the project builds in one edit (q-0024.0002 / 01-0017.0020).
- **The harness pain's present answers omit** `harness.py --check`, the leak check, and "every refusal writes nothing".

## 4. Causes, pains or goals the tree's own records treat as reasons, but missing here

- **The harness's own weight in context.** "Tier is paid by every session", Occam and "a capable reader", q-0018.0008.
- **Over-building.** The necessity gate, `/discover` "never the reason to change something … worthening", `/impact` "can it be narrower?", "remove before you add".
- **No cause listed for G2.** Implied: no role-bounded permissions (q-0016), documents read as instructions, concurrent writers (q-0032).
- **C4 is too narrow.** Loss also happens at compaction and when the host resumes under a new id (q-0001.0006).
- **The freedom-to-think pain dropped out** of the pains list.
- **Correction and evaluation together** is scattered across rows.
- **Teams.**

## 5. Rows that are implementation detail rather than a mechanism answering a cause

- Five rows of the exploration space are one mechanism, the question store.
- "HITL or AFK …" overlaps the switches row and the `/spec` row; the load-bearing test, `/spec` and the lighter path are three statements of one routing.
- "One home per rule, copied by a script" and "every rule at its tier" are two properties of one installer.
- Three self-improvement rows are one mechanism — the seed of a test suite for instructions.
- "Locks" is one implementation of "no session overwrites another's write".
- "A record of every step" is a by-product of the delivery skills.
- "Declared and checked mechanisms" answers C1 more than self-improvement.
- "Every second look at work as one pass" (q-0029) restructures `/verify` and `/maintain` rather than answering a cause.
- "Thin vertical slices; `/plan`; `/tdd`" bundles three practices in one row.
