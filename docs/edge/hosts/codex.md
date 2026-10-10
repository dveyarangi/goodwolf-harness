# Codex — Hosts edge

## Integration

- The entry file, `AGENTS.md`, read natively.
- The skills under `.agents/skills`, read natively; no loader link.
- The hooks in `.codex/hooks.json`, merged from the shelf
  `.agents/skills/questions/hooks/.codex/hooks.json`, each launching
  `.agents/scripts/gw/hook.sh` as `gw-hook codex`.
- The host's row `codex` in `HOSTS`, `.agents/scripts/gw/questions.py`: `session_id`, and
  `PostCompact` as its compaction.
- Its hook cases in `.agents/scripts/gw/test/test_questions.py`, its merge in
  `.agents/scripts/gw/test/test_harness.py`.
- From outside the tree: `features.hooks=true`, and each hook definition trusted
  ([OpenAI's hook trust guidance](https://learn.chatgpt.com/docs/hooks#review-and-trust-hooks)).
  The host in use is the ChatGPT desktop app's Codex mode, sharing `~/.codex` with the Codex CLI;
  the `codex` on PATH is a stale May 2025 build and not the host.

## Conformance

- **Entry file** — documented: Codex reads `AGENTS.md` natively, the premise of
  [01-0010.0020 live-alignment-across-hosts](../../tickets/done/01-0010.0020-live-alignment-across-hosts.md);
  no first reply opening with the line is recorded.
- **Skills** — observed 2026-09-06 by the user, the listing only, in the same ticket: Codex listed
  the installed skills; none was recorded run by name.
- **Hook wiring** — observed 2026-10-03, chat `01a0fee7`, approval and trust only: no hook context
  until the user approved the hooks; the runtime's `hooks/list` then reported all three enabled
  and trusted, and approval took effect in the open chat; a hook's clean exit was not read.
- **Wake** — observed 2026-10-03, fresh chat `01a0fef1`: the wake's read, under the host's id, was
  in context before the first command. The rollout keeps no event name, so whether the start hook
  or the first prompt's fallback delivered it is not settled.
- **Registration** — observed 2026-10-03: registered under the host's own `session_id`.
- **Window** — observed 2026-10-03, chat `01a0fef1`: the unchanged notice, then after `at` the
  changed window, each before any agent command.
- **Compaction** — documented: `PostCompact` in the host's hook documentation.
- **Helper** — observed 2026-10-10, chat `01a12615`: a helper, thread `01a12617`, carried its
  parent's `session_id` in its own record, as documented, yet its turn received no hook context and
  the sessions file gained no row; the parent had moved to q-0021 before the helper started, and
  its next message still carried the whole changed window, so no helper hook took it.
- **Silence** — observed 2026-10-10 at 01:16Z, the revival only: a row ended by hand turned running
  on one message; the ending by a wake was not watched.
- **Offline tests** — observed 2026-10-10: the hook cases and the merge passed in the verification
  set.
- **Resume** — unobserved; a resumed chat keeps its thread and rollout, `session_id` with them.
