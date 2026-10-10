# Cursor — Hosts edge

## Integration

- The entry file, `AGENTS.md`, read natively.
- The skills through the loader link `.cursor/skills` → `../.agents/skills`.
- The hooks in `.cursor/hooks.json`, merged from the shelf
  `.agents/skills/questions/hooks/.cursor/hooks.json`, each launching
  `.agents/scripts/gw/hook.sh` as `gw-hook cursor`.
- The host's row `cursor` in `HOSTS`, `.agents/scripts/gw/questions.py`: `conversation_id`,
  `sessionStart`, `preCompact`, and `beforeSubmitPrompt` only as a sign of life; its answers in
  `_cursor_answer`, the session's tag handed on as `env` `QUESTIONS_SESSION`.
- The hook's input is decoded by its byte-order mark in `_hook_input`: on Windows the host wrote
  input the console's code page could not read.
- Its hook cases in `.agents/scripts/gw/test/test_questions.py`, its merge in
  `.agents/scripts/gw/test/test_harness.py`.
- Version in use 2026-10-02: 3.22.7. The host's Hooks output channel is where a hook's run is seen.

## Conformance

- **Entry file** — observed 2026-09-06, in
  [01-0010.0020 live-alignment-across-hosts](../../tickets/done/01-0010.0020-live-alignment-across-hosts.md):
  a fresh session opened with the entry contract line.
- **Skills** — observed 2026-09-06, in the same ticket: the catalog listed `align` and `impact`, and
  `/impact` ran when asked what installing `/ticket` would take.
- **Hook wiring** — observed 2026-10-03, 3.22.7: the Hooks output channel showed the hook run from
  the project root, exit 0 in about 1.5 s, once its input was decoded by its mark.
- **Wake** — absent: `sessionStart`'s `additional_context` never reaches the agent, a host defect
  ([Cursor staff](https://forum.cursor.com/t/sessionstart-hook-additional-context-is-never-injected-into-agents-initial-system-context/158452));
  the entry file's rule stands in, the agent drawing the wake by a bare `--wake`.
- **Registration** — observed 2026-10-03, chat `fb978107`, failing the check's second half: the
  hook registered the chat under its id and the host logged the `env` update, but the `env` reaches
  later hooks, never the agent's shell, so the agent's bare `--wake` mints a second line and works
  under it.
- **Window** — absent: `beforeSubmitPrompt` can only allow or block; the entry file's rule stands
  in, the agent drawing the window itself.
- **Compaction** — documented: `preCompact` in the host's hook documentation.
- **Helper** — unobserved.
- **Silence** — observed 2026-10-10 at 01:06Z, the revival only: a row ended by hand turned running
  on one message, marked seen by the prompt hook; the ending by a wake was not watched.
- **Offline tests** — observed 2026-10-10: the hook cases and the merge passed in the verification
  set.
