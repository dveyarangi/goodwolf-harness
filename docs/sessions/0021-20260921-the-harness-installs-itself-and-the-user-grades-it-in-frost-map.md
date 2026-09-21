# The harness installs itself, and the user grades it in frost_map

Session twenty-one, the evening of 2026-09-20 into 2026-09-21, after
[session twenty](0020-20260920-the-local-file-lands-and-the-candidate-turns-out-to-be-a-chain.md).
It opened with "good evening again", ran `/recall` first by rule, took the nod for
[01-0010.0130](../tickets/done/01-0010.0130-harness-installs-into-another-tree.md), and ran it
through the whole ring — `/plan`, a second `/align`, two more `/plan` passes, `/implement`,
`/verify`, a live run that refuted four things, `/maintain` — to a close graded by the user in
frost_map. Then it minted the next slice and landed one tier-1 rule. Nine commits of mine plus
this record; `origin/main` took them in three pushes, the last before this record.

## Work completed

Details are on the records named; the mechanism's evidence holds what was refuted and why.

- **The `harness` mechanism** ([the ticket](../tickets/done/01-0010.0130-harness-installs-into-another-tree.md),
  [the RFC](../rfc/done/01-0010.0130-harness-installs-into-another-tree.md),
  [the evidence](../mechanisms/harness.evidence.md)): `harness.py` with `--install`, `--update`
  and `--check`, the skill `/harness`, the declaration, and a root README for an agent handed the
  link. The source is always a fresh whole no-checkout clone of the repository at a ref, read
  through one `git archive`; the manifest is `.agents/` plus the entry file and stub; local
  blocks stripped, straw dogs and `TODO` bindings sheared, the announce line stamped
  `<repository>@<ref>` as the recipient's only revision; every refusal writes nothing; a loader
  link the platform refuses is handed to the person as the `mklink` lines while everything else
  lands; arrival is three checks in seconds, the links reported beside the verdict. The shape
  check reads the line's `@` and lifts the unbound `not yet` rule in a recipient.
- **The second align** moved the source from a working tree to the repository, named the
  mechanism, made the announce line the revision with no record file, dropped a default-set
  rule and a clean-tree rule, and landed the Occam rule at tier 1 (v14). The mechanism was named
  `deploy` there and renamed `harness` at `/implement` on the user's word; the test helper
  `harness.py` became `repository.py`.
- **The user's probe** settled that both loader links are needed — Claude Code and Cursor read
  only their own directory — on ADR-0003; and that Developer Mode is asked of nobody.
- **The live run** from the pushed repository into an empty tree took six minutes and reported
  the links twice; the shipped suite left the gate, the links left the parts table and the
  verdict, one archive replaced sixty-five `cat-file` spawns, and the archive is read with
  conversion off. Then: five to seven seconds, 65 files, `arrived: true`.
- **The grade.** frost_map moved its three `<project-local>` blocks into `local.rules.md` as
  four rules, took the update to `goodwolf-harness@2c733f0`, and its own check reported
  `arrived: true` with both links resolving and its blocks re-injected last. The ticket closed on
  it; the `tickets.py` override the box expected was a guess about a state the project no longer
  has.
- **[01-0010.0150](../tickets/01-0010.0150-harness-meets-a-tree-with-a-method.md)** minted: the
  install meets a tree that already has a method — the refusal carries an inventory, the skill
  states the flow, the README shrinks to a front page, the skill names the repository on the one
  line the script derives from and stamps into a recipient. Graded by a stranger tree.
- **The tiering rule** at tier 1 (v15), hand-written and wrapped on
  [01-0018](../tickets/01-0018-reachability-coherent.md) under R5: a skill's description is its
  tier-1 surface, every occasion and nothing else; every rule at the tier its occasion reads.
- **The shape's evidence** records its fourth application: the harness passed the check
  unedited and sharpened one word — a part is what ships.

## What the user corrected, kept as evidence

- **"install should actually not use any local repo folder"** — the whole first plan read the
  tree the script ran in. Turned around in one sentence.
- **"did not you just suggest to add git hash as entry name in agents.md? can't we use that?"** —
  the record file, the default-set rule and the clean-tree rule went with it. The line is the
  record.
- **"most important principle is clarity and simplicity. occam razor. we should actually add it
  as core rule"** — v14, the same turn.
- **"nope, this is still horribly slow"** and **"what is 'three-gates arrival'?"** — the suite
  was the six minutes and a made-up noun was the answer. The suite left the gate; the noun left
  my replies.
- **"you do not test it by cloning the repo. you test it by running the scripts. why do you
  need to clone?"** — I had begun a hand clone to test a script whose whole point is that it
  clones for itself. Stopped and rerun the right way.
- **"I now think that 'deploy' is the wrong name. it will have meaning in real dev env."**
  Renamed mid-implementation; the word is reserved against in the glossary.
- **"exclude the checks from failing the test"** — the links and the suite stopped deciding
  arrival; the report names them beside it.
- **"switching to dev mode is too cumbersome"** — the refused link became the command in the
  report, not a stop and not a setting asked of anyone.

## Open, with owners

- **`.0150`'s `/plan`** is the queue's candidate; first by the ordering rule, since it hands every
  later install into an existing estate its flow. `next-cycle=ask`.
- **Whether the pacer still waits behind the four coherence refactors** —
  [01-0020](../tickets/01-0020-pacer.md)'s, and the first thing to decide after the nod.
- **01-0018 owes the tiering rule a rules file and an owner**, and carries the `/maintain` skill
  pass — holding bodies to `/skill-up`'s rules and descriptions to the tiering rule — as a handed
  input no mechanism instructs yet.
- **The repository line in the skill** is `.0150`'s; until it lands, the URL lives in the
  script's `HOME` constant alone and the skill does not name it.
- **The test module for the install** takes about two minutes for its real clone and two real
  checks per case; accepted on the evidence, not optimised.
- **The repoint and the created-link paths** are proved only on a machine that creates symlinks;
  here the case skips with its reason. The `keep` path was proved read-only against both real
  trees.
- **Concern 1** gained one more observation without a driver: the tiering rule and the local
  block are two more things the entry file holds that a mechanism could render.
- **Carried from twenty, unchanged:** sibling blocks at one anchor in install order; the
  remover and inline wrappers; the user's grade on the mechanism shape; contribution back and
  releases, parked on the spec; the audit report's one legacy citation.

## Housekeeping

Ten commits of mine on `main` today, this record the last; three pushes, the last after this
record (`push=ask`, given). Verification set green at the close: 304 tests, one skipped where the
platform makes no symlink, three checks clean; 64 straw dogs, all bound, no condition met. Entry
contract v15. The tree holds four declared mechanisms, one local rules file, and twelve installed
blocks from four sources. The user's external review of 2026-09-20 sits untracked at
`docs/research/external-review.md`, theirs to commit.
