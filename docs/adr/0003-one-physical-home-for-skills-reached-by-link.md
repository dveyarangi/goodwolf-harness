# One physical home for skills, reached by link

Skill bodies live once, under `.agents/skills/`. Each host reaches them through a directory symlink
— `.claude/skills` and `.cursor/skills`; Codex reads `.agents/skills` natively. Decided 2026-09-05
with the repository's root, in
[01-0010](../tickets/01-0010-dev-harness-shared-and-local.md#resolutions-and-constraints).

**Amended 2026-09-26: the links are made in each clone and never committed** *(the user)*. They were
tracked as mode 120000 when nothing else could give a clone its links. Since 2026-09-21 the harness
makes them, and tracking them had become the harm: Git for Windows checks a tracked link out as a
17-byte text file, which the harness then refuses as *a file where a link goes*, so a Windows
teammate's clone met a refusal the tracking itself created — found by an adoption panel reader
cloning this repository. Untracked, every clone on every platform behaves alike: it has no links
until the harness makes them, by the light per-clone step
[01-0010.0172](../tickets/01-0010.0172-a-first-install-says-what-stopped-it.md) adds.

## Considered options

**A copy per host.** This is what every audited estate actually had, and the
[audit](../research/audit-2026-09-05/REPORT.md) is the argument against it: independent physical
copies, local loader aliases and divergent bodies across 99 files, with no way to tell an
intentional local change from a missed propagation. The cost of copies is not storage, it is that
divergence is invisible until someone diffs.

**Directory junctions on Windows.** Rejected, and the reason is stronger than *Git tracks it as a
directory*: a junction is not a weaker symlink, it is a different object that nothing can see
through. `Path.is_symlink()` returns false, `rglob` walks into it, and `git ls-files` lists the
files beneath it a second time under the link's path — measured 2026-09-09. That last one is
decisive, because `git ls-files` is what `docs_corpus.corpus()` runs and the corpus is the one view
every script shares: under a junction every skill is enumerated twice and `move_doc.py` would repair
one file's citations through two paths. This holds whether or not the link is tracked, so
gitignoring it changes nothing.

**A junction as a fallback when the platform refuses a symlink.** Rejected 2026-09-09 by the user
after it was tried during [the frost_map probe](../research/separation-probe-frost-map.md). **The
link is a symlink or the install stops and asks** — no fallback, no substitute. A refusal is a human
decision: Developer Mode, an elevated prompt, or a host that reads `.agents/skills` natively and
needs no link.

## Consequences

The links are the most fragile thing a recipient touches. While they were tracked, Git for Windows
checked them out as text files, needing `git config --local core.symlinks true` and a re-checkout;
untracked since 2026-09-26, that case is gone, and what remains is that creating one needs
Developer Mode or an elevated prompt.
[`.agents/README.md`](../../.agents/README.md) carries the recovery steps, and creating the links
is `/harness`'s job since 2026-09-21.

**Both links are required — observed 2026-09-21** *(the user, in a probe tree holding one skill
under `.agents/skills/` and no link)*: neither Claude Code nor Cursor listed the skill or loaded
it. Codex reads `.agents/skills` natively and needs none. So the links stay, and since Windows
gates creating one on a privilege whatever tool asks — copying a link is creating one — the
harness mechanism makes each link where it can and otherwise hands the person the exact elevated `mklink`
command for that tree; Developer Mode is not asked of anyone *(the user, 2026-09-21)*.
