---
name: verify
description: >-
  Use after an implementation pass, or to verify a landed slice before close.
  Whole verification of landed work: ticket, RFC, governing docs, and the
  project's verification set. Repair-and-report where that policy holds.
---

Compare the work to its ticket, RFC if any, governing docs, and every check
in the project's [verification set](../../../docs/process.md#verification).
Find out:

- How well the work matches and represents the documentation
- Where the work went wrong or weird because of underspecification or
  contradiction in the docs
- Whether the verification set's checks hold

Look for architectural or responsibility leakage.

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

Apply `/improve-comments` rules to groom the comments and check that TODO tags
are correct.

Apply `/plan` rules that help this review. Do not start a whole-tree
maintenance pass; `/maintain` owns that.
