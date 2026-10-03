# The harness changes its own rules by stated meta-rules, not by judgement each time

- **Status:** Blocked (accumulating evidence before its align)
- **Type:** HITL
- **Related:** [`/mechanism`](../../.agents/skills/mechanism/SKILL.md) holds this responsibility
  today and [`/skill-up`](../../.agents/skills/skill-up/SKILL.md) is its neighbour;
  [01-0017.0010](./01-0017.0010-terms-defined-before-they-land.md) — the first registered failure
  proposes an amendment to `/align` that should land with that ticket's rewrites, not ahead of them
- **Answers:** [q-0026](../questions/q-0026-how-does-the-harness-amend-its-own-rules-by-stated-meta-rules.md)
- **Outcome:** Amending the harness's own rules follows stated meta-rules — how a failure is
  registered, when a rule is reworded, what counts as evidence that it did not work — instead of a
  judgement made afresh each time; and whether that is its own mechanism is answered from strikes
  rather than from argument.

## Parent

[Harness architecture](../architecture.md), which owns the agreed maintenance boundaries. This has
no parent spec: it was raised at the 2026-09-10 dev-method align as a set of meta-rules wanted
around a rule the entry file had just gained, and it is minted early on the user's direction that
fast minting for later alignment is what this project should encourage.

## Why it is minted before it can be decided

The entry file now carries a standing rule — *a rule present that did not fire was phrased wrong;
register the failure and propose the rewording.* The register is
[`docs/rule-failures.md`](../rule-failures.md), and it has one entry.

What is wanted around that rule is **a set of explicit meta-rules governing harness
self-amendment** *(the user, 2026-09-10)*. Whether they need a mechanism of their own is
deliberately unresolved: the case for separation is that the occasion (*a rule failed to fire*) and
the record belong to neither `/mechanism` nor `/skill-up`; the case against is that one wish is one
shape, and this project's first general rule refuses to generalise from one. **The decision waits on
accumulated strikes rather than on argument** — which is why this ticket exists now and is not being
worked now.

**Deliberately not adopted: deletion** *(the user, 2026-09-10)*. An early proposal made a rule with
repeated registered failures a deletion candidate. Removing is destructive, and an unaligned
deletion rule is a loaded weapon pointed at rules still wanted. Occurrences are counted and evidence
is collected; what to do with a rule that keeps failing is decided when there is something to decide
it on. A ticket that adopted deletion at minting would be doing the thing this project keeps
catching itself at.

## What to build

Not yet determined; the align decides it. What is known to be in scope:

- **The meta-rules themselves** — what registration requires, who may reword a rule and on what
  evidence, and what distinguishes a rule that was disobeyed from one that could not fire.
- **How an amendment is tested** *(the user, 2026-09-26)*. A new session in this repository, with
  the amended ruleset installed and not this session, receives the request that failed, word for
  word, and is told nothing of the issue; the session that registered the failure grades its reply
  against the rule. A reader asked how it parses the rule, or run in an empty folder, tests
  comprehension, not firing. Record files that describe the failure are withheld. A control under the
  old ruleset shows the failure still reproduces. First run on
  [rule failure 12](../rule-failures.md) through the `claude` CLI, headless.
- **The register's shape**, if it stays: today `rule-failures.md` has a written form and no
  declared format, which is the same gap
  [01-0017.0020](./01-0017.0020-practice-swaps-in-one-edit.md) found for sessions and dreams.
- **Whether this is a mechanism**, answered from the register rather than from this text.
- **One strike is not evidence.** Whatever this ticket concludes, it concludes from a register with
  more than one entry, or it concludes that the register was not worth keeping.

## Acceptance criteria — provisional, firmed at the align

- [ ] The meta-rules governing self-amendment are stated in a durable home, with their provenance.
- [ ] Whether self-amendment is its own mechanism is answered, citing the register's entries as the
      evidence for the answer.
- [ ] The register has a declared format, or is retired with its reason.
- [ ] Every entry in the register has a disposition: amendment made, amendment refused with a
      reason, or struck as repeated.
- [ ] `/verify` has been run on this ticket against its ticket, RFC, and governing docs.

## Out of scope

Deleting a rule on accumulated failures, refused at minting. The glossary mechanism and the
dev-method mechanism, which are [01-0017](./01-0017-io-graph-coherent.md)'s children. Group install
targets — [q-0005](../questions/q-0005-how-does-a-group-install-target-resolve-to-a-file-and-an-anchor-in-each-member.md).
