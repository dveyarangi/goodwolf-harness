# Claude Code — Hosts edge

## Integration

- The entry file through `CLAUDE.md`, which loads `AGENTS.md`.
- The skills through the loader link `.claude/skills` → `../.agents/skills`.
- The hooks in `.claude/settings.json`, merged from the shelf
  `.agents/skills/questions/hooks/.claude/settings.json`: `SessionStart` and `UserPromptSubmit`,
  each launching `.agents/scripts/gw/hook.sh` as `gw-hook claude-code`.
- The host's row `claude-code` in `HOSTS`, `.agents/scripts/gw/questions.py`: `session_id`, and
  the desktop app's `CLAUDE_CODE_HOST_SESSION_ID`, read first where it is set, since the app gives
  a resumed conversation a new `session_id` and keeps its own id; the terminal keeps the
  `session_id` on resume, a new one only under `--fork-session`.
- Its hook cases in `.agents/scripts/gw/test/test_sessions.py`, its merge in
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
- **Helper** — observed 2026-10-10, session `58bf3b88`: a helper agent ran some five minutes; the
  sessions file gained no row, and the session's next message carried a true unchanged notice.
  The helper's own hook input was not seen; no helper event is wired. Observed 2026-10-25: a
  helper's context carried the entry file as its parent session had loaded it at its start, v110,
  where the file on disk stood at v117; a helper that must follow the entry file reads it from disk.
- **Messaging** — observed 2026-10-23, desktop app: a message sent from one session to another
  reached it, and the receiving session answered and acted on it — the close of a ticket handed
  over with the results of its checks.
- **Silence** — observed 2026-10-10 at 01:17Z, the revival only: a row ended by hand turned running
  on one message; the ending by a wake was not watched.
- **Offline tests** — observed 2026-10-10: the hook cases and the merge passed in the verification
  set.
- **Resume** — observed 2026-10-10, desktop app, failing before the fix: reopened, the
  conversation `58bf3b88` came back as `d0abdc88`, and the start hook ran 3 s before the new
  transcript existed, so the transcript match found nothing and registered a new session; the
  session is now keyed on the app's own id. Observed 2026-10-10 in the terminal, passing: a
  session `6408d73c` exited and reopened by `claude --continue` got *already registered* under
  the same id, one row in the sessions file. Observed 2026-10-10 in the desktop app after the
  fix, passing: with the app quit and relaunched, the conversation came back as `3a5196da` in a
  new process, and the start hook answered *already registered* under the app's
  `local_48db9702…`, its position kept and no row added.
- **Edit refusal** — documented: a PreToolUse hook on `Write` or `Edit` gets the absolute
  `file_path` and refuses with `permissionDecision: "deny"` and a reason shown to the agent, or exit
  code 2 ([hooks](https://code.claude.com/docs/en/hooks), 2026-10-24).
- **Skill load** — documented: a PreToolUse on `Skill` when the agent calls one, a
  `UserPromptExpansion` with `command_name` when the person types it, each with `session_id`; a
  subagent does not see the skills its parent invoked, save a fork, and whether its PreToolUse
  carries `agent_id` is not stated ([hooks](https://code.claude.com/docs/en/hooks),
  [sub-agents](https://code.claude.com/docs/en/sub-agents), 2026-10-24).
- **Skill lifetime** — documented: an invoked skill's text stays across later turns, and a second
  invocation of an unchanged skill adds only a note that it is loaded; at compaction the most recent
  invocation of each skill is re-attached, its first 5,000 tokens, within 25,000 for all together,
  filled from the most recent, so an older skill can be dropped; `PreCompact`, `PostCompact` and
  `SessionStart` with source `compact` carry `session_id`
  ([skills](https://code.claude.com/docs/en/skills), quotes checked, 2026-10-24).
- **Entry notice** — observed 2026-11-24, desktop app, session `1981de0e`, which did not build
  it: two hand edits of the entry file at 19:26:28Z came eight seconds later with the next
  message, another session's, as two passages, each as it was and as it is now, both exact; the
  installer rewrote a block of the file at 19:27:07Z, and the person's next message, at 21:27Z,
  carried that one passage, exact; the three messages after it carried none. The host compacted
  the context on that same message, after the hook had run, so a change made before a compaction
  was shown at it. Not seen: a fresh chat's first message, and a notice cut short.
  Documented, read 2026-11-22: `CLAUDE.md` is loaded at launch and
  after a compaction *re-injected from disk*, which the line takes as the context holding the file
  as it stands ([context window](https://code.claude.com/docs/en/context-window.md),
  [memory](https://code.claude.com/docs/en/memory.md)); a hook's output past 10,000 characters is
  saved to a file and its first 2,000 placed in context, which is why the notice leads the window
  and asks for a read past 8,000 ([hooks](https://code.claude.com/docs/en/hooks)). Seen
  2026-11-22, desktop app, of the window alone: a hook's output of 58 KB was saved as the
  context's own text, line by line, under the session's folder, and its path and first 2 KB were
  what stood in context.
- **Call refusal** — unobserved; the try of 2026-11-26 did not run, the terminal's `claude` not
  being signed in. Of the host's search alone, seen 2026-11-27, desktop app, session `1981de0e`, on
  a scratch folder of fake values: `Grep` over a folder skipped a file named by a `.gitignore`
  inside a repository, by a `.ignore` and by a `.rgignore`, a parent folder's `.ignore` included;
  a `glob` that matched the file printed it though ignored, a `glob` that only excluded did not;
  a `path` naming the file printed it; `Glob` listed every one. Documented, read 2026-11-27: the
  call before a tool gets `tool_name`, `tool_input`, `cwd` and, in a helper, `agent_id`, and fires
  for a helper's calls; it refuses with `permissionDecision: "deny"` or exit 2; a hook that exits
  otherwise, cannot start or times out lets the call through, `onFailure: "block"` turning that
  round from 2.1.295; a file the person mentions with `@` passes no hook; the host's own
  `Read(path)` deny rules cover its file tools, its search on a best effort, and the shell's file
  commands it recognises ([hooks](https://code.claude.com/docs/en/hooks),
  [permissions](https://code.claude.com/docs/en/permissions),
  [sub-agents](https://code.claude.com/docs/en/sub-agents)).
