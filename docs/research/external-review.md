# External review — 2026-09-20

An outside read of the repository at `1f14d4d` (113 commits, the close of session nineteen),
written by Claude Fable 5.1 on request, from a fresh clone. The reviewer read the entry file,
both glossaries, the ADRs, the architecture, the three mechanism declarations, the skills, the
scripts and their tests, the research reports and the session records, and ran the verification
set. It is evidence about how the tree reads to someone who did not build it, not a decision
about anything.

> **Since this review (noted 2026-09-26).** Several of its findings no longer hold. The installer
> exists — `harness.py` installs, updates and checks a copy, landed 2026-09-21 — and the harness
> has since been installed into other projects, among them a large existing codebase with no agent
> setup and a project with a smaller harness of its own. The repository has a front page and an MIT
> license. Four of its twenty-three skills are now declared mechanisms. The review below is left as
> it was written.

## What it is

`goodwolf-harness` is a self-hosted development method for coding agents: 22 skills under
`.agents/skills/`, reachable by Claude Code, Codex and Cursor through symlinks, a tier-1 entry
file, and six standard-library Python scripts that mechanically check and repair the tree. The
method is a two-ring loop — a session ring (recall, align, conclude) and a delivery ring (ticket,
plan, implement, verify, maintain) — with tickets, RFCs, ADRs and a glossary as records.

Its distinguishing idea is that the harness treats its own rules as engineering artifacts. A
mechanism must declare its parts, its moments of human action, what it produces and who reads it,
and a script verifies the declaration is true. Rules live in one file and are injected into skills
as owned blocks a checker can detect drift in. Provisional text is wrapped in `<straw-dog>` tags
bound to a ticket so it can be found and retired. A rule-failures register records post-mortems on
rules that were present but did not fire.

The repository is built with itself: one author, sixteen days, nineteen recorded sessions at the
reviewed revision. It grew out of an audit of four divergent skill copies across the author's
other projects.

| Measure at `1f14d4d` | Value |
|---|---|
| Skills / declared mechanisms | 22 / 3 |
| Core prose vs construction prose | 28k words vs 172k words |
| Tests, all passing | 243 in 108 s |
| Straw dogs live in the tree | 67 |
| Entry file | 1,384 words |
| License | none |

## What is genuinely strong

- **The scripts are well engineered.** Explicit repository root, one shared corpus view through
  `git ls-files`, refuse-rather-than-guess everywhere, byte-identical retraction, no rollback
  promises that cannot be kept, and every test builds a real Git repository in a temp directory.
  The verification set passes cleanly on a fresh clone.
- **The rule-failures register is the best idea here.** Each entry names the rule that was loaded,
  why it did not fire, and the phrasing amendment. The diagnoses are sharp: descriptive rules with
  the verb buried, rules scoped to one skill while the behaviour happens everywhere, rules living
  in diagrams. This is a real feedback loop on instruction quality, which almost no agent setup
  has.
- **Core versus instance separation is enforced, not merely stated.** The leak check fails at home
  on any core citation of a document only this repository has. The frost_map probe that found 35
  breakages was turned into a check and a spec within days.
- **Honest records.** Session notes list what the user corrected. Mechanism docs pre-register what
  would show them working and who grades it. Absence of diagnostics is explicitly not treated as
  clearance.

## What worries the reviewer

- **It has never installed anywhere successfully.** The installer does not exist. The one probe
  into another tree broke 35 ways, and the recipient dropped a check rather than duplicate its
  Notion state. The install spec is accepted but its two tickets are open. Until then, the
  "shared across projects" outcome is unproven.
- **Only 3 of 22 skills are declared mechanisms.** The other 19 carry a `Mechanism: not yet` line
  bound to 01-0017, which sits behind a chain of four HITL coherence tickets. The shape has thin
  evidence, and the docs say so.
- **Process mass dwarfs product.** Construction prose is six times the core. Sixteen days produced
  a method, not software. That is defensible for a method repository, but there is no measurement
  of whether an agent working under this harness produces better code than one without it. The
  self-development loop generates its own work.
- **Tier-1 cost.** Every session loads about 1,400 words of entry file, and the heavy skills run
  1,000 to 1,600 words each, written in dense idiosyncratic vocabulary — some 45 defined terms:
  straw dog, painted door, shear, moment, tier. An agent or person arriving cold pays a real
  comprehension tax, and the rule-failure entries show even the author's own sessions misread
  rules repeatedly.
- **Windows fragility is structural.** Skills reach hosts through symlinks that need Developer
  Mode. ADR-0003 rejects junctions for good measured reasons, but the result is that the most
  load-bearing link is the one most likely to arrive broken.
- **Hand-held lists remain.** The painted-doors list in `mechanisms.py` is hardcoded under four
  `TODO`s, and two entries, `docs/edge/` and `docs/cicd.md`, are declared by no mechanism. The
  queue table is still a hand-copied index the method's own R4 argues against.
- **Housekeeping gaps.** No license; no root README, so GitHub renders the docs index; the dream
  skill writes records in a random language, which is charming but unsearchable.

## Verdict

A serious, unusually self-critical attempt at making agent instructions maintainable as code, and
the mechanical half is solid enough to reuse on its own. The injector, the drift checker and the
rule-failures practice would each transfer to another project today. The method as a whole is
pre-alpha for its stated purpose: it has not shipped to a second tree, most of its skills are
undeclared, and its value over a plain well-written entry file is asserted rather than measured.

**Recommendation.** Land the installer and run it into one real project before any more coherence
tickets, and write one comparison, even informal, of a task done with and without the harness.
That is the evidence the whole edifice is waiting for.
