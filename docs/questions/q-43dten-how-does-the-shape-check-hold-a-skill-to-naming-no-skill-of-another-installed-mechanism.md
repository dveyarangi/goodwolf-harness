# q-43dten How does the shape check hold a skill to naming no skill of another installed mechanism?

- **record of** what it intends to become
- **part of** q-gbt7cy
- **state** open
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-18T04:43:24Z
- **struck** 0, last 2026-11-18T04:43Z

R8 forbids a skill's own text to name a skill of another installed mechanism, and no script reads
it: `mechanisms.py --check` passes over skills that do
([the register](../rule-failures.md), 2026-11-18). The check is the amendment the register
proposes. What it must settle before it lands: which mentions stand today, counted with installed
blocks set aside; whether each becomes an installed block from the naming mechanism's rules file
or is dropped; and the order, the lines mended before the check joins the verification set, the
practice's by that session.

## Evidence, 2026-11-20 — an outside audit's claim, checked at 4314d5bf

[The audit of 2026-11-20](../research/external-audit-2026-11-20.md) says `/ticket`, `/plan` and
`/verify` break R8. A subagent that did not write the rule read every skill's own text, outside
its installed blocks, against each mechanism's declared state. `/ticket` does not break it;
`/plan` and `/verify` do, and four skills the audit did not name. No script checks R8.

| skill | names a skill of another installed mechanism | names a sibling of its own mechanism |
|---|---|---|
| `plan` | `/ticket` ×2 | `/implement` |
| `verify` | `/maintain` | `/implement`, `/plan` |
| `align` | `/ticket` | |
| `debugging` | `/harness` ×2, one in its description | |
| `mechanism` | `/maintain` ×2 | |
| `review-architecture` | `/ticket`, `/plan` | |
| `implement` | | `/verify` ×5 |
| `conclude` | | `/recall` |

Eleven cross-mechanism namings in six skills. By R8's letter a sibling is "another skill" too;
its heading speaks of reaching an installed mechanism by its rules, and delivery has no rules
file to carry a sibling's sentence — whether R8 binds siblings is not said.
