# Claude Code — Hosts edge

## Integration

- The entry file through `CLAUDE.md`, which loads `AGENTS.md`.
- The skills through the loader link `.claude/skills` → `../.agents/skills`.
- The hooks in `.claude/settings.json`, merged from the shelf
  `.agents/skills/questions/hooks/.claude/settings.json`: `SessionStart` and `UserPromptSubmit`,
  each launching `.agents/scripts/gw/hook.sh` as `gw-hook claude-code`.
- The host's row `claude-code` in `HOSTS`, `.agents/scripts/gw/questions.py`: `session_id`, and
  `transcript_path` for a conversation resumed under a new id.
- A project `settings.json` written mid-session is read without a restart; nothing to approve.

## Conformance

- **Entry file** — observed 2026-10-10, session `58bf3b88`: the first reply opened with the entry
  contract line.
- **Skills** — observed 2026-09-05, in
  [01-0010.0020 live-alignment-across-hosts](../../tickets/done/01-0010.0020-live-alignment-across-hosts.md):
  the host listed the installed skills.
- **Hook wiring** — observed 2026-10-02, in the session that wired it: a `settings.json` written
  mid-session was picked up without a restart.
- **Wake** — observed 2026-10-10, session `58bf3b88`: the start hook's wake, headed
  `registered now` under the host's id, was in context before the first command.
- **Registration** — observed 2026-10-02: the prompt hook registered the session under the host's
  `session_id` at its first message, no start having been seen; again 2026-10-10 from the start
  hook.
- **Window** — observed 2026-10-02: a whole window, then the one-line unchanged notice, each
  reached the agent's context.
- **Compaction** — documented: the host's hook documentation; no compaction event is wired.
- **Helper** — unobserved.
- **Silence** — observed 2026-10-10 at 01:17Z: a row ended by hand turned running on one message.
