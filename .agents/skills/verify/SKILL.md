---
name: verify
description: >-
  Use after an implementation pass, or to verify a landed slice before close.
  Whole verification of landed work: ticket, RFC, governing docs, and the
  project's verification set. Repair-and-report where that policy holds.
---

<straw-dog until="01-0017 declares the verify mechanism" ticket="docs/tickets/01-0017-io-graph-coherent.md">Mechanism: not yet</straw-dog>

Compare the work to its ticket, RFC if any, governing docs, and every check
in the project's [verification set](../../../docs/process.md#verification).
Find out:

- How well the work matches and represents the documentation
- Where the work went wrong or weird because of underspecification or
  contradiction in the docs
- Whether the verification set's checks hold

Look for architectural or responsibility leakage.


## Check and repair

- Cross-check documents against each other and against code, in both directions.
  Ask whether the implementation contract could be reconstructed from the architecture
  alone; a load-bearing decision visible only in code is a documentation finding.
- Code that contradicts an accepted decision is a code finding. Do not settle a
  contradiction by weakening the rule.
- Check named validators still exist and still assert the promise they were named for.
  A missing or drifted validator is a finding, as is an unguarded normative promise.
- Sweep the concern index for entries in scope: a concern the implementation has since
  answered belongs in its owning record, and a dead trigger retires.
- Apply [repair-and-report](../../../docs/process.md#autonomy-and-repair) where it holds:
  make the repair, verify it, and record the violated rule, the change, the verification
  result and any remaining uncertainty in the owning work item.
- Everything else goes to [/align](../align/SKILL.md): a missing, ambiguous or
  contradictory rule, a new foundational decision, or work beyond the authorization.
  Pause that change; independently authorized work continues.
- Anything that can be maintained mechanically must be. If the script is missing, write
  it — a missing script is work to do, not an excuse to leave the repair outstanding.

<straw-dog until="the mechanism responsible for straw dogs is elected" ticket="docs/tickets/01-0016-responsibility-coherent.md">
- Read the landed work against the pending tickets. What one of them will replace is a straw
  dog: wrap it and bind it to that ticket, per the entry file, and leave what has no named
  successor alone. Run `straw_dogs.py --guess` over the files the slice touched and judge its
  candidates.
</straw-dog>

Discrepancies:

- If [repair-and-report](../../../docs/process.md#autonomy-and-repair) holds,
  make the repair, verify it, and report in the owning work item. Cite the
  violated rule, what changed, the verification result and any remaining
  uncertainty. The `repair` switch is in `AGENTS.md`.
- Otherwise `/align`: present the discrepancy, affected constraints,
  recommended resolution and the decision needed. Do not amend until that
  returns.
- Do not rewrite a governing rule, weaken a validator or relax acceptance
  criteria to make a violation disappear. Action permissions (`commit`, `push`)
  still apply.

A missing RFC is not a defect of this skill when the ticket has none.

- Docstrings say what their own unit does. Apply
  [/improve-comments](../improve-comments/SKILL.md) to comments in scope and check
  that TODO tags still describe something pending.


Apply `/plan` rules that help this review. Do not start a whole-tree
maintenance pass; `/maintain` owns that.
