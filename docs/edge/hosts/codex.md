# Codex — Hosts edge

## Integration

- The entry file, `AGENTS.md`, read natively.
- The skills under `.agents/skills`, read natively; no loader link.
- The hooks in `.codex/hooks.json`, merged from the shelf
  `.agents/skills/questions/hooks/.codex/hooks.json`, each launching
  `.agents/scripts/gw/hook.sh` as `gw-hook codex`.
- The host's row `codex` in `HOSTS`, `.agents/scripts/gw/questions.py`: `session_id`, and
  `PostCompact` as its compaction.
- From outside the tree: `features.hooks=true`, and each hook definition trusted
  ([OpenAI's hook trust guidance](https://learn.chatgpt.com/docs/hooks#review-and-trust-hooks)).
  The host in use is the ChatGPT desktop app's Codex mode, sharing `~/.codex` with the Codex CLI;
  the `codex` on PATH is a stale May 2025 build and not the host.

## Conformance

- **Entry file** — observed 2026-09-05, in
  [01-0010.0020 live-alignment-across-hosts](../../tickets/done/01-0010.0020-live-alignment-across-hosts.md):
  the host read `AGENTS.md`.
- **Skills** — observed 2026-09-05, in the same ticket: the host listed the installed skills.
- **Hook wiring** — observed 2026-10-03, chat `01a0fee7`: no hook context until the user approved
  the hooks; the runtime's `hooks/list` then reported all three enabled and trusted, and approval
  took effect in the open chat.
- **Wake** — observed 2026-10-03, fresh chat `01a0fef1`: the wake's read, under the host's id, was
  in context before the first command. The rollout keeps no event name, so whether the start hook
  or the first prompt's fallback delivered it is not settled.
- **Registration** — observed 2026-10-03: registered under the host's own `session_id`.
- **Window** — observed 2026-10-03, chat `01a0fef1`: the unchanged notice, then after `at` the
  changed window, each before any agent command.
- **Compaction** — documented: `PostCompact` in the host's hook documentation.
- **Helper** — documented: a helper inherits its parent's `session_id`.
- **Silence** — observed 2026-10-10 at 01:16Z: a row ended by hand turned running on one message.
