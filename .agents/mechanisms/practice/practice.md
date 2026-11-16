# practice — how a project writes its code, its tests and its comments, reaching the steps of delivery as installed text

- **instruction** `.agents/skills/tdd/SKILL.md` — writing tests first, in red-green-refactor cycles at agreed seams
- **instruction** `.agents/skills/improve-comments/SKILL.md` — writing and reviewing comments and docstrings
- **state** installed
- **record of** what must always hold
- **owner** core

## How it works

Delivery's steps are general: they plan, do and verify a unit of work of any kind. What is true of
code alone — how a plan presents code and stages its tests, how code is named, tested, laid out
and commented, how a fixture and a comment are checked — is this mechanism's. Its rules file
installs those rules into the steps that read them; its two skills hold the practice's own long
form, which the installed rules point to. A project changes how it builds by changing this
mechanism alone: it overrides a rule from its local rules file, or replaces the mechanism, and no
step is edited *(the user, 2026-11-16)*.

The rules came from the steps' own bodies, word for word, the day the practice was declared; their
authority names the step they came from.

**Who decided.**

| what | decided by |
|---|---|
| the practice is a mechanism of its own, apart from the ring's form, and reaches the steps by injection | the user, 2026-11-16 |
| T13, T17 — the code's pointer to the architecture rule it follows, and its reading at verification | the user, 2026-10-12 |

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| writing tests first, a cycle at a time | `.agents/skills/tdd/SKILL.md` | |
| writing and reviewing comments and docstrings | `.agents/skills/improve-comments/SKILL.md` | |
| planning code: its shapes, its stages, its tests | `.agents/skills/plan/SKILL.md` | |
| writing code to the practice | `.agents/skills/implement/SKILL.md` | |
| checking fixtures, comments and pointers at verification | `.agents/skills/verify/SKILL.md` | |
| documenting architecture and decisions | — | embedded — the shelves of architecture and ADRs sit beside the align skill, `.agents/skills/align/ARCH-FORMAT.md` |
| holding every code pointer to the rule it names, by a check | — | <straw-dog question="q-jap5to">not yet</straw-dog> |
| a project putting its own practice in this one's place | — | <straw-dog question="q-qmq6ty">not yet</straw-dog> |
| installing this mechanism into a tree, with the rest of core | `.agents/scripts/gw/harness.py` | |
| removing this mechanism from a tree | — | <straw-dog question="q-qzeuf3">not yet</straw-dog> |

## Install adds, uninstall removes

| part | where |
|---|---|
| tests first | `.agents/skills/tdd/SKILL.md` |
| tests first, its shelf | `.agents/skills/tdd/deep-modules.md` |
| tests first, its shelf | `.agents/skills/tdd/interface-design.md` |
| tests first, its shelf | `.agents/skills/tdd/mocking.md` |
| tests first, its shelf | `.agents/skills/tdd/refactoring.md` |
| tests first, its shelf | `.agents/skills/tdd/tests.md` |
| comments | `.agents/skills/improve-comments/SKILL.md` |
| this doc | `.agents/mechanisms/practice/practice.md` |
| its rules file | `.agents/mechanisms/practice/practice.rules.md` |

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| planning, where its rules are installed | `.agents/skills/plan/SKILL.md` → "## Installed from other mechanisms" | `delivery` |
| doing, where its rules are installed | `.agents/skills/implement/SKILL.md` → "## Installed from other mechanisms" | `delivery` |
| verifying, where its rules are installed | `.agents/skills/verify/SKILL.md` → "## Installed from other mechanisms" | `delivery` |
| the installer | `.agents/scripts/gw/inject_rules.py` | `mechanism-shape` |
| the method's vocabulary | `.agents/glossary.md` | nobody removable |

## What it produces, and who reads it

- **The rules file** — *what must always hold* — read by the installer alone, and by whoever
  amends a rule of practice or overrides one for a project. Its blocks sit in `/plan`,
  `/implement` and `/verify`.

Nothing else. The tests, code and comments it shapes are the project's work, not its records; it
keeps none, so `/maintain` has nothing of it to check beyond its parts.

## Not yet at the shape

<straw-dog question="q-hrfk7l">**How architecture is documented** — the shelves for the
architecture document and ADRs beside `/align`, and the entry file's example of good architecture
documentation — is practice, and comes here with the homes of decisions it sits beside.</straw-dog>

<straw-dog question="q-jap5to">**A pointer is read by eye.** Nothing yet checks that a code
pointer names a rule its record holds.</straw-dog>

<straw-dog question="q-ggpx2r">**Some rules are general in meaning and code in word** — T8, that
planning does not do the work; T10's second sentence, that the work follows its contract — and
return to the steps once delivery has a word for work that is not code.</straw-dog>

<straw-dog question="q-tcnf74">**One practice or several.** Tests and comments are here together,
and architecture documentation will join them; whether each swaps alone is open.</straw-dog>

## What retires this

Nothing in this tree. In a project that builds by another practice, that project's own replaces
it there.

## What would show it working, graded by someone who did not build it

1. **A judge given the three steps before and after the move** says whether any step's own text
   had to change what it says to let a practice rule out — delivery's line drawn wrong — and
   whether any rule left in a step is true of code alone. Run at its declaration.
2. **A project that swaps a rule**: one rule overridden from a local rules file, the steps
   untouched, and the next session following the project's rule, not this one's. Graded by the
   session that first does it.
