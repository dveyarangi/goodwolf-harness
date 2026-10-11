# Context tax of peer harnesses, as of 2026-10-11

**Kind:** evidence — a dated measurement. What a session pays in context before the person's
first message, in a freshly installed project under Claude Code, for this harness and seven peers.

**Method.** Tokens are characters ÷ 4. *Always-loaded instructions* is the CLAUDE.md or AGENTS.md
text the tool installs, plus whatever its session-start hook injects. *Descriptions* is the
frontmatter `name` and `description` of every skill, command and subagent the host lists at start;
bodies load on invocation and are not counted. Peers were measured from shallow clones of their
public repositories at the named commits, by reading the installer's source and templates; no
installer was run. Each figure is ±10%: the ÷4 convention, the keys counted with the values, and
the host's own listing format are not modelled. Excluded everywhere: context a tool generates
later from the project (BMAD's context block, GSD's generated CLAUDE.md, Pocock's agent-skills
block) and anything that grows with use (beads' memories).

This harness, by the same method: a fresh install's `AGENTS.md` plus the 24 skill descriptions
is about 4,000 tokens; in this repository, with its own installed blocks and local rules,
`AGENTS.md` is 17,008 characters and the descriptions 2,458, about 4,900 tokens.

| tool | always-loaded instructions | skill/command descriptions | before the first message | hook at session start | per message | source |
|---|---|---|---|---|---|---|
| **this harness** | ≈3,400 (`AGENTS.md`, fresh) | ≈600 (24 skills) | **≈4,000** | yes: the wake report, ≈2,700 in this repository after a month | yes: the question window, by a hook | this tree, 2026-10-11 |
| **GSD Core** | 0 — no CLAUDE.md written at install; `generate-claude-md` runs later from `/gsd:new-project` | ≈1,975 (72 skills); plus 35 subagents ≈1,965 in the Agent roster | **≈1,975** (≈3,940 with the subagent roster) | yes, but injects no model context by default; a STATE.md head only with `hooks.community: true` | none for Claude Code; tool-call guards instead | open-gsd/gsd-core b747aca, v1.16.0, 2026-10-11 |
| **BMAD-METHOD** | 0 at install — the `bmad:context` AGENTS.md block is written by `bmad-project-context` later, project-sized (this repo's: ≈550) | ≈343 (the documented minimal 5 skills) to ≈2,267 (all 33) | **≈343–2,267** | none | none | bmad-code-org/BMAD-METHOD bda3c59, 2026-10-06 |
| **superpowers** | ≈850 — the hook injects `using-superpowers/SKILL.md` whole as `additionalContext` | ≈733 (15 skills) | **≈1,580** | yes, on startup, clear and compaction, so it is paid again after each | none | obra/superpowers bb92a77, v7.0.0, 2026-10-09 |
| **spec-kit** | 0 — the constitution is read by command bodies on invocation | ≈370 (10 commands) | **≈370** | none by default | none | github/spec-kit 0443760, 2026-10-09 |
| **beads** | ≈695 — the minimal profile block `bd init` writes into AGENTS.md | 0 for Claude Code (the skill ships for Codex and Cursor) | **≈2,100** (695 + ≈1,400 from the hook) | yes: `bd prime --hook-json`, ≈1,400 by measurement, "~1–2k" by its own docs, plus stored memories; again after compaction | none | steveyegge/beads 7477ec1, 2026-10-11 |
| **Matt Pocock's skills** | 0 — an optional setup skill later adds a ≈100-token block | ≈1,180 (27 skills in the plugin) | **≈1,180** | none | none | mattpocock/skills 49dd158, plugin v1.3.1, 2026-10-09 |
| **OpenSpec** | 0 — `init` no longer writes CLAUDE.md or AGENTS.md | ≈1,145 (12 skills + 12 commands) | **≈1,145** | none | none | Fission-AI/OpenSpec 9111a76, 2026-10-06 |

## Reading it

- Fresh, this harness starts two to ten times heavier than any peer: about 4,000 tokens against
  370–2,100, GSD reaching ≈3,940 only when its 35 subagents are counted.
- The difference is in kind, not only in size. Every peer loads next to nothing before the first
  message and pays inside each command, when its body loads. This harness loads the method's rules
  themselves — the entry file — so that they bind every turn, commands or not; that is the tax of
  rules that reach the agent rather than wait to be invoked.
- Two peers pay a session-start hook as this one does: superpowers (≈850, a skill body) and beads
  (≈1,400, project state). This harness's wake report is the largest of the three and grows with
  the tree; its per-message window has no peer at all.
- What the tax buys has not been measured, here or anywhere in the panel; q-0017 and q-0018.0008
  hold that.

The user asked for this comparison on 2026-10-11, for the front page's cost paragraph. The
figures were gathered by a delegated agent from the repositories named; nothing was taken from a
tool's own claims except where the table says so.
