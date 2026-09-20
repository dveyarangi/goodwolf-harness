# One physical home for skills, reached by link

Skill bodies live once, under `.agents/skills/`. Each host reaches them through a directory symlink
tracked as mode 120000 — `.claude/skills` and `.cursor/skills`; Codex reads `.agents/skills`
natively. Decided 2026-09-05 with the repository's root, in
[01-0010](../tickets/01-0010-dev-harness-shared-and-local.md#resolutions-and-constraints).

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

The links are the most fragile thing a recipient touches. Git for Windows writes
`core.symlinks=false` on clone, so they arrive as text files needing `git config --local
core.symlinks true` and a re-checkout; creating one needs Developer Mode or an elevated prompt.
[`.agents/README.md`](../../.agents/README.md) carries the recovery steps, and creating the links
becomes the installer's job once one exists.

**Both links are required — observed 2026-09-21** *(the user, in a probe tree holding one skill
under `.agents/skills/` and no link)*: neither Claude Code nor Cursor listed the skill or loaded
it. Codex reads `.agents/skills` natively and needs none. So the links stay, and since Windows
gates creating one on a privilege whatever tool asks — copying a link is creating one — the
deploy makes each link where it can and otherwise hands the person the exact elevated `mklink`
command for that tree; Developer Mode is not asked of anyone *(the user, 2026-09-21)*.
