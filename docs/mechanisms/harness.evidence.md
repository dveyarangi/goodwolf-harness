# harness — evidence

Why [the doc](../../.agents/mechanisms/harness/harness.md) is what it is: what was tried, what was
refuted, what it cost. Declared by
[01-0010.0130](../tickets/01-0010.0130-harness-installs-into-another-tree.md) on 2026-09-21, under
[the install spec](../spec/01-0010.0130-harness-installs-into-another-tree.md) accepted 2026-09-14.

## Refuted before a line was written

- **A working tree as the source.** The first plan read the tree the script ran in. The user
  turned it around on 2026-09-20: the source is the repository at a ref, always a fresh clone, so
  that a recipient never receives uncommitted work under a commit that does not hold it, and so
  that a pure core repository published later is one more `--from` with no change to the script.
- **A record file.** `.agents/revision.json` — source, commit, one normalised hash per shipped
  file — was planned as the recipient's mark and its integrity record. The user asked why the
  stamped announce line was not enough. It is: the line names the ref, the check clones the ref
  and compares, and a tree with an `@` on its line is a recipient. One file fewer, at the price of
  a network fetch per check.
- **A default verification set as a core rule.** Planned as a rule with an id so a recipient could
  override it by name. The user asked what it was for: the project's verification set is the
  project's, defined generically in `/verify` already, and what the rule was reaching for was core
  checking itself — which is `harness.py --check`, and needs no rule.
- **A clean-tree rule for updates.** Planned so every overwrite was recoverable from the
  recipient's git. Withdrawn with the record file: the comparison against the announced ref finds
  an edit, and `--overwrite` replaces and names it, which is the injector's own rule for a drifted
  block.
- **A shallow fetch.** GitHub serves no fetch by a short commit, and the line carries the short
  form. The clone is whole and without a checkout — 4.3 MB in two seconds for the real
  repository — and every ref is read through git plumbing, which also keeps a Windows checkout's
  line-ending translation out of what ships.
- **Stopping on a refused link.** The plan stopped the run before writing when the platform could
  not create a symlink, and offered Developer Mode among the answers. The user, 2026-09-21: the
  files, the injection and the gate are worth more to the person than a clean stop, and Developer
  Mode is too cumbersome to ask of anyone; the run finishes and hands over the `mklink` lines.
  Whether a link was needed at all was settled by the user's probe the same day: a skill under
  `.agents/skills/` with no link is invisible to Claude Code and to Cursor.
- **The root README as a part.** A part is what uninstalling removes, and the README never ships;
  listed, it would fail a recipient's shape check or pass against the recipient's own. It is the
  repository's front page, written for an agent handed the link.
- **A mechanism named `install`, then `deploy`.** The first named one mode rather than the
  mechanism; the second, chosen at the align, was refused at `/implement` because *deploy* has
  its own meaning in a real development environment. The user: *our mechanism should be named
  "harness", simple as that.* The word *deploy* is reserved against in the glossary; *install*,
  *update* and *check* name the modes; *release* stays free for the mechanism that will cut one.

## The prior corpus

One copy of core existed outside this repository before the mechanism did: frost_map, installed
by hand on 2026-09-09 at entry contract v8, 41 files behind `1f14d4d` on 2026-09-20, with three
`<project-local>` blocks in its entry file, no local rules file, no line saying which ref it
holds, and one core check left unrun. Every one of those is a refusal or a report the first
update will produce; that update, by the user, is the grade.

## What it cost

The shipped suite runs inside the gate, so an install or a check takes the suite's minute and a
half in the recipient; and the test suite here runs three real gates per install case, which
made its tests the slowest module by an order of magnitude. Accepted: a gate that does not
run the shipped scripts proves nothing about them.
