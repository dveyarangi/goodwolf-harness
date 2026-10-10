# Claude Code — Hosts edge

## Integration

- The entry file through `CLAUDE.md`, which loads `AGENTS.md`.
- The skills through the loader link `.claude/skills` → `../.agents/skills`.
- The hooks in `.claude/settings.json`, merged from the shelf
  `.agents/skills/questions/hooks/.claude/settings.json`: `SessionStart` and `UserPromptSubmit`,
  each launching `.agents/scripts/gw/hook.sh` as `gw-hook claude-code`.
- The host's row `claude-code` in `HOSTS`, `.agents/scripts/gw/questions.py`: `session_id`, and
  `transcript_path` for a conversation resumed under a new id.
- Its hook cases in `.agents/scripts/gw/test/test_questions.py`, its merge in
  `.agents/scripts/gw/test/test_harness.py`.
- A project `settings.json` written mid-session is read without a restart; nothing to approve.

## Conformance

- **Entry file** — observed 2026-09-06, desktop app, in
  [01-0010.0020 live-alignment-across-hosts](../../tickets/done/01-0010.0020-live-alignment-across-hosts.md):
  a fresh session's first reply opened with the entry contract line; again 2026-10-10, session
  `58bf3b88`.
- **Skills** — observed 2026-09-06, in the same ticket: the catalog listed `align` and `impact`, and
  an explicit `/align` request reached the installed skill.
- **Hook wiring** — observed 2026-10-02, in the session that wired it, the merge and the hook's run
  only: a `settings.json` written mid-session was picked up without a restart and its output
  reached the agent; the host's own log was not read.
- **Wake** — observed 2026-10-10, session `58bf3b88`: the start hook's wake, headed
  `registered now` under the host's id, was in context before the first command.
- **Registration** — observed 2026-10-02: the prompt hook registered the session under the host's
  `session_id` at its first message, no start having been seen; again 2026-10-10 from the start
  hook.
- **Window** — observed 2026-10-02: a whole window, then the one-line unchanged notice, each
  reached the agent's context.
- **Compaction** — unobserved; the host's row in `HOSTS` wires no compaction event, so nothing
  makes the window after one whole.
- **Helper** — unobserved.
- **Silence** — observed 2026-10-10 at 01:17Z, the revival only: a row ended by hand turned running
  on one message; the ending by a wake was not watched.
- **Offline tests** — observed 2026-10-10: the hook cases and the merge passed in the verification
  set.
