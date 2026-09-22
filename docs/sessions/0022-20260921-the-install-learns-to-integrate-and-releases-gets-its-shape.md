# The install learns to integrate, and releases gets its shape

Session twenty-two, 2026-09-21 into the small hours of the 22nd, after
[session twenty-one](0021-20260921-the-harness-installs-itself-and-the-user-grades-it-in-frost-map.md).
It opened with *"I think we should look at 0150"*, ran `/recall` first by rule, and went
`/plan` → `/ticket` → `/mechanism` → `/plan` → `/implement` → `/verify` → `/align`, turning one
slice's plan into four and one refusal into an integration. Six commits of mine; none pushed
(`push=ask`, not given).

## Work completed

Details are on the records named.

- **[01-0010.0150](../tickets/01-0010.0150-harness-meets-a-tree-with-a-method.md)'s RFC**
  authored, then twice rewritten on the user's answers. A foreign `.agents/` is **integrated, not
  refused** — only a file at a path the manifest writes is a collision — so the slice adds the
  inventory rather than a new refusal. Skill collisions go to `/align` by name *and* by
  responsibility; a process of the project's own is met step by step; the flow's section is the
  anchor a mechanism's own meet-block installs under. The repository line left for its own slice.
- **Three slices minted** and the fourth narrowed:
  [01-0010.0145](../tickets/01-0010.0145-core-scripts-under-one-directory.md) (AFK, landed
  below), [01-0010.0155](../tickets/01-0010.0155-a-tree-names-the-repository-its-core-comes-from.md)
  (AFK, the repository line), [01-0010.0160](../tickets/01-0010.0160-harness-edge-changes-reach-an-update.md)
  (HITL, aligned below). The `/impact` of the split is on the parent.
- **P9, the first mechanism block in the entry file's general rules** — *name a ticket by a link
  to its record; one that has no record yet, by a slug and its state word* — installed from
  `ticket.rules.md` after the user read two bare ids in a reply. Entry contract v16. Written fat,
  trimmed to one line on *"the injected rule is too fat :)"*.
- **The injector places a block at the end of its anchor's section** ([the evidence](../mechanisms/mechanism-shape.evidence.md)),
  not directly after the anchor line: P9 had landed above the rules it joins. Five blocks in four
  files were re-placed by retract-and-install; `--check` had called them all `present`, because
  position is not something it reads, and still is not. The format shelf lost the restatement —
  placement is the installer's behaviour, not the rules-file author's business.
- **[01-0010.0145](../tickets/01-0010.0145-core-scripts-under-one-directory.md) landed and
  verified**: core's seven scripts and their tests under `.agents/scripts/gw/`, one constant
  `SCRIPTS` in `docs_corpus.py` from which the tests prefix and the harness's gate path derive,
  five roots one level deeper, ~20 live files' citations by hand. A new case proves the move as a
  recipient meets it. Install into a scratch tree from this clone: `arrived: true`, three gates at
  the new path, then the tree's own check passes. Two spec statements the move outran were
  repaired at `/verify`.
- **[01-0010.0160](../tickets/01-0010.0160-harness-edge-changes-reach-an-update.md) aligned**:
  the installation edge defined, its two homes, registration at the occasion and derivation at the
  release, *releases* publishing the clean core to a repository of its own, and the installing
  agent deciding whether to take one. Landed in [the architecture](../architecture.md#installing),
  the install spec's parked item, and the method glossary.

## What the user corrected, kept as evidence

- **"we should not refuse the foreign `.agents/`, we should integrate"** — the plan's first
  finding proposed refusing on the directory. The rule stayed today's; what makes integration
  smooth is the namespace and an explicit `/align`, not a bigger refusal.
- **"loop is not swappable is too hard a rule"** — the cut
  [01-0017.0020](../tickets/01-0017.0020-practice-swaps-in-one-edit.md) drew is relaxed; ceremony
  and granularity become switchable, which is [01-0020](../tickets/01-0020-pacer.md)'s.
- **"plain text ids like .0145 in your output are no good"** — became P9, at tier 1, installed.
- **"the injected rule is too fat :)"** — four lines to one.
- **"the installation should be to the end of the anchor section, not beginning."**
- **"why does mechanism format needs this description, if the injection is done mechanically?"** —
  the shelf says only what a rules-file author needs; the contract has one home.
- **"why is this unique to frost_map???"** — I had read one recipient and written its
  dependencies as if they were that tree's. They are every recipient's.
- **"docs/edge is architecture and engineering doc... 'manifested' edge for the client instance is
  the README"** — I had collapsed the engineering record and what a client meets into one home.
- **"isn't it up for installing agent to align on those changes and then handle what to do with
  them?"** — I had been designing whether the *script* lands or refuses. It is the agent's call,
  which is why `--check` must name pending releases before anything is written.

## Open, with owners

- **`.0160`'s `/ticket`** is the queue's candidate: six parts, too big for one RFC. Two open
  issues on the ticket — the split itself, and what the first publish does about history, since
  frost_map announces `goodwolf-harness@2c733f0`, a ref the core repository will not contain.
- **frost_map's update is the first release's case.** `.0145`'s last box. Either hold it until
  releases exists and it arrives with a note, or take it blind and record what the report did not
  say. The user's call; nothing is scheduled.
- **The old copy's gate.** A recipient updating from its own copy runs the old script, whose gate
  looks under the path the update just deleted: `arrived: false` on two gates, every file landed,
  and a check from the new copy passes. Refused as a thing to fix — a change to the old script
  cannot reach a tree that already holds it.
- **`.0150` and `.0155`** wait on nothing now but each other's ordering and the published core;
  `.0150`'s RFC is authored and wants one more validation pass over the moved scripts.
- **Six commits unpushed**, and the user's external review of 2026-09-20 still untracked at
  `docs/research/external-review.md`.
- **Carried, unchanged:** the two decisions waiting at `/align` in the queue; concern 1; the
  coherence chain behind the install work.

## Housekeeping

Verification set green at the close: 311 tests, one skipped where the platform makes no symlink;
the shape, injector and ticket checks clean; 66 straw dogs, all bound, no condition met. Entry
contract v16. The tree holds four declared mechanisms; `releases` will be the fifth.
