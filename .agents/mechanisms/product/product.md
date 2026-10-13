# product — keeps one account of what the project is for, and reads from the work how much of it is built

- **instruction** `.agents/skills/product/SKILL.md` — the act: keeping the product document, seeing each answer's coverage
- **state** installed
- **record of** what must always hold

## How it works

A project's **product document** says what the project is for: the pains it relieves, the goals
it must not lose, the causes, and the answers — each answer a row with an id never renumbered and
a name. It is the home of the decisions taken under the purpose root, as the architecture and the
ADRs are the structure root's.

**The account is linked to the work through the question store, never through tickets.** A
question that builds an answer carries a trace link to it, by id and name; its sub-questions carry
it by trace propagation. The store keeps the link as written and never resolves it, so the
development method knows nothing of the product. An answer's coverage — absent, in progress,
present — is read from the questions that realize it, never written; the maintainer script renders
it on request, and the document holds no status of its own.

**The maintainer holds the document's form.** Every answer carries an id and a name, and no id is
written twice. A tree with no product document has nothing to check and passes.

It is **installed**. <straw-dog question="q-0018.0024">It ships with core like every mechanism,
since a project cannot yet take one alone; where a project keeps no product document, it finds
nothing.</straw-dog>

**Who decided each rule.**

| rule | decided by |
|---|---|
| the document is the purpose root's home, linked to the work through the store | the user, 2026-10-12/13, q-0035 decisions 1, 2 and 4 |
| a trace link names an answer by id and name | the user, 2026-10-13, q-0035.0006 decision 1 |
| only open and decided questions realize | settled at the plan, 2026-10-13, q-0035.0006 decision 2 |
| U1 — the document is checked by `product.py` | the user, 2026-10-13, q-0035 decision 3, owed to `/maintain`'s M1 |
| one mechanism tells the account to every reader; in core for now | the user, 2026-10-13, q-0035 decisions 10 and 11 |

## Moments

| moment | instructed by | kind, and why |
|---|---|---|
| keeping the product document | `.agents/skills/product/SKILL.md` | |
| writing the document to its shape | `.agents/skills/product/PRODUCT-FORMAT.md` | |
| seeing each answer's coverage | `.agents/skills/product/SKILL.md` | |
| checking the document's form | `.agents/scripts/gw/product.py` | |
| checking the document in a maintenance pass | `.agents/skills/maintain/SKILL.md` | |
| a purpose decision landing as an answer, its building question opened with a trace link | — | <straw-dog question="q-0035.0008">not yet</straw-dog> |
| the root README told from the document | — | <straw-dog question="q-0035.0005">not yet</straw-dog> |
| a release note's product half gathered from the coverage that moved | — | <straw-dog question="q-0018.0020.0002.0002">not yet</straw-dog> |
| installing this mechanism into a tree, with the rest of core | `.agents/scripts/gw/harness.py` | |
| removing this mechanism from a tree | — | <straw-dog question="q-0018.0013.0002">not yet</straw-dog> |

## Install adds, uninstall removes

| part | where |
|---|---|
| instruction file | `.agents/skills/product/SKILL.md` |
| format shelf | `.agents/skills/product/PRODUCT-FORMAT.md` |
| this doc | `.agents/mechanisms/product/product.md` |
| its rules file | `.agents/mechanisms/product/product.rules.md` |
| the maintainer | `.agents/scripts/gw/product.py` |
| the maintainer's tests | `.agents/scripts/gw/test/test_product.py` |

## Relies on, and does not own

| part | where | owner |
|---|---|---|
| the trace link and what a question realizes | `.agents/scripts/gw/questions.py` → "def realizes(" | `questions` |
| test harness | `.agents/scripts/gw/test/repository.py` | `mechanism-shape` |
| the installer | `.agents/scripts/gw/inject_rules.py` | `mechanism-shape` |
| the pass that checks the document | `.agents/skills/maintain/SKILL.md` | `maintain` |
| the method's vocabulary | `.agents/glossary.md` | nobody removable |

## What it produces, and who reads it

- **The product document** — *what must always hold* — read by the person deciding what the
  project is for, and by whoever opens a building question for an answer.
- **The coverage rendering** — *what exists* — read by the person ordering the work, on request;
  never committed.
- **The maintainer's report** — *what exists* — read by `/maintain` under U1. Its exit status is
  the verdict; its JSON is for the person reading a failure. It writes nothing.
- **The rules file** — *what must always hold* — read by the installer alone, and by whoever amends
  a rule of this mechanism that another skill reads. Its block sits in `/maintain`.

Nothing else; no index.

## Not yet at the shape

**Four `not yet` rows of its own**, each bound to an open question: allocation from a purpose
decision, the README, the release note, and removal. Drift between the document and the work —
an orphan, an unrealized answer, a link naming no answer or an outdated name — is not found yet.

## What retires this

A project that keeps no account of what it is for: then no answer exists to realize, and coverage
reads nothing.

## What would show it working, graded by someone who did not build it

Pre-registered 2026-10-13. **The session that brings this tree's product document onto the
mechanism** grades it: did the format and the coverage rendering let it number the answers, link
the building questions and read each answer's coverage, without reading the history the format was
designed in? Each time it had to go back to that history for something the format or the skill
should have said is a miss, named in the evidence.
