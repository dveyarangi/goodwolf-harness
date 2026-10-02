# GoodWolf Harness — whole-project evaluation

Evaluated 2026-09-30 against committed revision `924d0b989401d3c4698133735bfbbabe0da4d329`.
Personal utility, readiness for other people and projects, and research value have equal standing.

## Judgment

The project has a useful engineering foundation and a plausible approach to preserving development
knowledge. Its complete workflow has not established a net benefit over a much smaller set of
instructions and records. It is suitable for supervised experimentation; I would not recommend
broad adoption as a dependable shared development method in its present state.

This judgment has three distinct parts:

| Intended use | Judgment | Confidence and limit |
|---|---|---|
| Personal development | Preserve the useful tools and memory practices; treat the full process as an experiment whose cost must earn its place. | Moderate. The records demonstrate concrete uses and corrections, but provide no controlled estimate of saved work or human attention. |
| Adoption by other projects | Significant preparation remains, including fixes for reproduced data-preservation failures. | High for the reproduced failures and documented lifecycle gaps. No independent onboarding cohort was observed. |
| Research into agent work | There are valuable questions, retained negative results and inspectable artifacts. The strongest experiment needs reproducibility repair and narrower conclusions. | High for the replication failures; moderate for transferability, which has not been established. |

The most consequential imbalance is that formalizing the method is ahead of validating its effect.
The next investment should reduce uncertainty about usefulness and protect existing user work.
Completing more of the internal framework does not, on its own, answer either need.

## Scope and method actually executed

The assessment combined inspection of the product's claims and governing contracts, representative
implementation review, the complete committed test suite and verification commands, independent
technical probes, and an audit of historical and experimental evidence.

All major areas were covered: the entry contract and glossary; session and delivery skills;
mechanism declarations and rule injection; the eight shipped Python modules and their test suite;
installation and update; the queue and active question-store design; historical failures, host
observations, recipient-install evidence, adoption panels and the window experiment.

Detailed source review concentrated on mutation boundaries, the shared corpus reader, validators,
and the research generator and scorer. This is not a claim to have reviewed every historical
document or every line of every skill. Supplementary skills were inspected more lightly than the
delivery loop. Existing reviews were treated as hypotheses and checked against primary material.

The question-store files were changing during this audit. An initial live-tree suite run encountered
incomplete implementation; that run is excluded from the shipped-product judgment. The reproducible
assessment uses an archived copy of the exact committed revision in disposable Git repositories.
Work-in-progress behavior is not certified, and the question store's eventual value is not judged
from transient test failures.

Environment: Windows, Python 3.12.14, standard library, Git. The sandbox could not access the configured
`uv` cache, so the bundled interpreter ran the same test and check entry points directly. Temporary
Git configuration handled sandbox ownership without changing the user's global configuration.

No controlled agent-versus-agent productivity trial, independent human usability study, Linux run,
current three-host compatibility trial or recipient production-delivery study was performed. These
limits prevent a causal verdict about the full workflow's benefit. The technical probes below test
specific contracts; they are not estimates of failure frequency in normal use.

## What is working and worth preserving

**The code has meaningful structure.** Shared corpus and citation handling avoid separate readers
quietly disagreeing about the same records. Installation reads committed Git objects rather than
uncommitted working files. The origin's project-specific blocks are stripped before distribution;
the recipient's local rules have an explicit authored home. These are concrete answers to real
portability and drift problems, described in the [architecture](../../architecture.md) and
[installation evidence](../../mechanisms/harness.evidence.md).

**The verification infrastructure works within its scope.** On the pinned snapshot, 319 tests ran
in 54.7 seconds, with no failures and one skip. The four configured checks passed; the maintenance
clock reported all eight declared mechanism levels current. File hashes before and after these
checks matched. These are observations from this environment, not performance comparisons with
earlier runs on different environments. Full output is in [results.json](results.json).

**Integrity checking catches actual changes.** A clean installation and subsequent check succeeded
in disposable repositories. Appending text to the installed recall skill then made the integrity
gate fail and identify that exact file. Local installation took 6.8 seconds and checking 5.4 seconds;
these timings exclude a network source and do not predict public-repository latency.

**The project distinguishes decisions, current work and historical accounts.** That distinction is
useful for handoff and is clearer than treating chat history as current truth. Its effectiveness
still depends on records being accurate and affordable to retrieve.

**The project records counterevidence.** The failure register includes failed assumptions, replays
and repairs. The installation evidence records design choices rejected after contact with a real
recipient. The window report names several limitations. These habits are useful research assets.

## Reproduced engineering findings

### E1 — An update can silently replace recipient-owned work

**Priority: high. Confidence: high.** A recipient had an uncommitted file at
`.agents/evaluation-collision.txt`, outside the installed manifest. The harness's own check
classified it as the recipient's file. A later upstream revision introduced the same path.
An ordinary update, without `--overwrite`, replaced its contents, reported `arrived: true`, and
reported an empty `replaced` list.

The prior-manifest comparison in
[harness.py](../../../.agents/scripts/gw/harness.py#L557) detects edits to previously shipped files;
it does not protect recipient files newly overlapping the incoming manifest. The writer then
replaces that path. This defeats the practical promise that project additions remain the project's
and that overwriting edits requires an explicit choice.

**Required outcome:** detect new-manifest collisions before mutation, preserve the recipient's
bytes, and require an explicit disposition. Add a regression case with independently authored,
uncommitted recipient content. Evidence: `probes.new_path_collision` in [results.json](results.json).

### E2 — A predictable refusal happens after installation writes

**Priority: medium. Confidence: high.** A fresh target containing an invalid `local.rules.md`
was refused by local-rule parsing, but 71 files had already been created. The local file itself
survived. This is a partial installation, despite the
[skill's promise](../../../.agents/skills/harness/SKILL.md#L46) that every refusal writes nothing.

[The run sequence](../../../.agents/scripts/gw/harness.py#L140) copies core and creates the queue
before checking local injection. Invalid local input is detectable in advance; it is different
from an unavoidable mid-write I/O failure.

**Required outcome:** validate the composed installation, including local rules and overrides,
before writing, or explicitly redesign and communicate the partial-install contract. Evidence:
`probes.refusal_side_effects` in [results.json](results.json).

### E3 — A record move can lose an intervening source edit

**Priority: high. Confidence: high for the tested interleaving.** After the mover derived its
operations, a simulated second editor added an uncommitted decision to the source record. The
mover then wrote the older content at the destination and deleted the source. It announced a
successful move and citation repair; the new decision was absent everywhere.

[The source move](../../../.agents/scripts/gw/move_doc.py#L128) checks destination existence but
does not compare the source with the content it read. The neighboring citation-repair operation
does check its input. The [architecture](../../architecture.md#interruption-and-recovery) disclaims
general simultaneous-writer safety but explicitly calls for expected-content rechecks. This
finding concerns that missing check; it does not claim the contract promises database transactions.

**Required outcome:** refuse a changed source and preserve its latest contents. A pre-write check
closes the demonstrated gap; any stronger concurrent-write guarantee needs a separately stated
contract. The probe used a controlled interleaving, not a probabilistic race stress test. See
[record-move-result.json](record-move-result.json).

### E4 — Installation success can coexist with unavailable host links

**Priority: medium for adoption. Confidence: high.** The fresh install reported `arrived: true`
while both host loader links were unresolved and elevated commands remained pending. This follows
the documented implementation contract, so it is not a code deviation. It is a product-readiness
problem if callers interpret the success boolean as ready for all supported hosts.

This is already recognized by
[01-0010.0172-a-first-install-says-what-stopped-it](../../tickets/01-0010.0172-a-first-install-says-what-stopped-it.md).
The report should distinguish copy integrity from host usability. This sandbox's inability to make
the links says nothing about whether an appropriately configured host can discover the skills.

These findings surviving the green suite establish specific coverage gaps, not that the entire
suite is worthless. Existing work already catalogs other weak tests and missing cross-platform
coverage in [01-0011.0090-a-test-catches-what-its-name-promises](../../tickets/01-0011.0090-a-test-catches-what-its-name-promises.md).

## Workflow, human experience and personal value

**The central benefit remains unresolved.** The README promises fewer reopened decisions, better
continuity and less document/code drift. The tree contains examples of these problems and tools
aimed at them, but I found no comparative measurement establishing the complete process's net
effect. The project's own
[01-0010.0168-the-harness-measures-what-it-costs-and-saves](../../tickets/01-0010.0168-the-harness-measures-what-it-costs-and-saves.md)
explicitly identifies this gap. This is absence of proof of benefit, not proof of no benefit.

**There is no operationally defined lighter path.** The README acknowledges the gap. Meanwhile,
the skill set directs extensive interviews, detailed planning, repeated validation and additional
maintenance. The maintenance skill requires checking every due mechanism regardless of the
declared scope. The specification template asks for an extremely extensive list of user stories.
These instructions can turn a small job into substantial process work. Actual frequency and human
cost are unmeasured. Requested approvals and valuable design conversations must not automatically
be counted as waste.

**The self-improvement loop has an attribution weakness.** The entry contract presumes a rule
that did not fire was usually worded wrong and asks for an amendment in the same pass. A failure
could instead come from conflicting instructions, retrieval, context load, a host limitation,
an unsuitable requirement or ordinary variability. Rewording the observed case can help, but
without repeated and held-out cases it can also overfit. The register's entries 13–15 explicitly
say their amendments had not been replayed; entry 12 does record replays. The warranted conclusion
is mixed validation, not either complete absence of testing or proven continuous improvement.

**Record volume creates a retrieval question, not a verdict.** At this revision there are 33,314
whitespace-delimited words in core Markdown, 304,640 under `docs/`, and 4,735 in the delivery queue.
The core total includes format shelves and other material loaded on demand; it is not the startup
context size. Much historical material need never be read for a given task. The measurement that
matters is what sessions actually consume and what decisions that reading improves. Word counts
alone cannot establish either human burden or wasted effort.

## Adoption and architecture

The separation of shared instructions from project-owned answers is coherent and useful. Plain
Python with standard-library dependencies also reduces integration demands; the direct Python
3.12 run in this audit supports that claim.

Adoption remains constrained by concrete lifecycle issues: existing instruction files require
manual reconciliation; ordinary updates lack a recipient-oriented compatibility account;
uninstallation is absent; a light process is undefined; and multi-developer operation is outside
the stated current scope. These are candidly listed in the README. There are no committed GitHub
Actions workflow files at this revision, and the test-strengthening ticket explicitly holds the
Linux/Windows CI work.

The host trial record provides narrow evidence for discovery and selected skills in three hosts
at its recorded dates. It does not certify every skill, today's host versions, or complete delivery
in all three. Recipient-install records demonstrate integration contact; they do not establish
productivity in ordinary software work.

The adoption panels are agent-generated reviews from imagined user situations. Their author
explicitly states the panelists inherited project instructions. They are useful sources of
objections to test; they are not five independent human adoption decisions or market evidence.

The public release design and the actual installer also deserve separate treatment: today's
installer clones the entire source repository on each check and reconstructs the shipped content.
That buys traceability and avoids a second manifest record, at the cost of source availability and
history-dependent work. The evidence records that tradeoff. Its suitability as the repository
grows should be measured rather than assumed.

## Research value and experimental validity

### R1 — The saved window experiment is not reproducible as packaged

**Confidence: high.** A fresh snapshot holds 83 answer files and 83 trial records. Running
`score.py` fails because the required `store100/store.json` is absent. Running `gen.py` succeeds,
but all 83 generated trials lack the `tag` field required by the scorer, which then fails with
`KeyError: 'tag'`. With Python 3.12 and `PYTHONHASHSEED=1`, 59 generated trial truths differ from
the saved truths, so regeneration is not a valid way to attach the old answers to fresh trials.

The generator uses a fixed random seed but also builds sequences from sets; it does not establish
a complete deterministic regeneration contract. This does not invalidate all recorded answers.
It means the claim that the saved experiment can be rerun requires repair. The original inputs and
answer identities should be recoverable without silently substituting new questions. See
[research-result.json](research-result.json) and [probe_research.py](probe_research.py).

### R2 — The window result supports a narrower claim than the design needs

The [experiment report](../window-test-2026-09-28.md) usefully shows promising performance on small,
provided neighborhoods. It also acknowledges one or two trials per cell, repeated tagged copies
of a taxonomy, trivial path/children tasks, and no executed second turn for distant placements.
Different renderings receive newly sampled questions rather than a fully paired task set.

Those observations support further testing of selective retrieval. They do not establish that a
question store preserves decisions, improves work across sessions, or pays for per-turn updates.
Nor do they establish generally constant cost: the stated window grows from roughly 700 to 9,000
tokens, and its renderer includes the current root's open subtree and other roots. A large single
root or many roots can therefore enlarge it. The experimental partitioning keeps local regions
small while total size grows.

### R3 — Existing studies motivate testing rather than settle this project's value

I verified the cited primary abstracts. [Gloaguen et al.](https://arxiv.org/abs/2602.11988) report
that context files do not generally improve success in their issue-resolution settings and add
cost. [Shepard and Albrecht](https://arxiv.org/abs/2606.20512) report gains from empirically refined
guidance under their tested configurations. Neither measures this full cross-session workflow.
Together they strengthen the case for testing the particular instructions and target tasks;
they justify neither wholesale rejection nor assumed effectiveness of this harness.

The project's research contribution would become stronger by turning observations into bounded,
reproducible findings: which record a fresh agent needed, what error a particular check prevented,
what simpler alternative performed as well, and where the approach failed. More analogies or
repeated review panels would add less evidence than such tests.

## Direction and recommended action

The accepted queue puts the question-store/coherence chain ahead of recipient lifecycle work.
I have not reordered it. This audit supplies new evidence relevant to that choice: actual
preservation failures and a reproducibility break, alongside an unresolved outcome claim.

The question store addresses an observed problem—questions getting lost across branching work.
That gives it a legitimate experimental purpose. It does not establish that recording the position
of every turn is the least costly solution, or that further process integration should depend on
it before ordinary development benefits are demonstrated.

My recommended order of investment is:

1. **Protect user work:** fix and retain regression proofs for E1 and E3; settle E2's preflight and
   recovery behavior. These are prerequisites for trusting the tools that persist the memory.
2. **Restore research reproducibility:** make the saved input/trial/answer/scorer chain run from a
   clean checkout, without changing historical questions to fit available answers.
3. **Compare the current workflow with a minimal alternative on real work:** use the same task
   information, tools, authorization and acceptance criteria. Measure correct outcomes, retained
   obligations, human corrections, elapsed time and tokens across fresh-session handoffs.
4. **Use that result to scope the default process:** retain components with demonstrated value;
   simplify or keep optional those that do not earn their cost. Test a question store on actual
   lost-question cases before expanding its role in the method.
5. **For wider adoption, prove one complete recipient lifecycle:** existing-project onboarding,
   ordinary delivery, restart, update and removal, across the environments actually advertised.

A pilot can identify instrumentation problems and large effects. A small pilot should not be
presented as conclusive productivity research; larger comparisons need sample sizes chosen from
observed variability and an agreed meaningful effect. Human judgments should distinguish useful
decisions from avoidable interruptions. The assessment should allow the possibility that selected
tools are valuable while the complete workflow is not the best default.

## Evidence bundle and changes made by this evaluation

- [run_audit.py](run_audit.py): pinned snapshot, full checks, install/update/refusal/drift probes,
  and inventory. Its controlled commits exist only inside disposable fixture repositories.
- [results.json](results.json): full check outputs and installation reports, including exceptions
  to arrival readiness and file-preservation results.
- [probe_record_move.py](probe_record_move.py) and [record-move-result.json](record-move-result.json):
  the controlled intervening-edit reproduction.
- [probe_research.py](probe_research.py) and [research-result.json](research-result.json):
  clean-snapshot rescoring and regeneration results.

Only evaluation artifacts were added to this repository. Product code, governing rules, queue
order and existing records were not changed by this evaluation. No repository commit or push was
made. Concurrent implementation work belongs to its existing session.
