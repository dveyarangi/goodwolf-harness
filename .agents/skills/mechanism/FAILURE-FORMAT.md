# Failure capture

One `failure.json` under `docs/cases/<slug>/` preserves a noticed failure. It is a record of
**what happened**, read at tier 2 while recording a failure, preparing its experiment or reviewing
the evidence. A capture is immutable. A replay or instruction change does not close it: it
remains evidence until the person retires that case, when its folder moves under
`docs/cases/done/`. The live check excludes that subtree.

## Draft

The draft is a JSON object with exactly these fields:

| field | value |
|---|---|
| `session` | the observing session's identifier |
| `message` | original user message: `{"role":"user","content":"…"}` |
| `context` | needed earlier messages in order, each with `role` and `content`; an empty list is allowed |
| `loaded` | nonempty ordered list of instruction snapshots, each with `path` and `text`; contents are those loaded in the failing turn |
| `observed` | the failed response or textual artifact, preserved as observed |
| `expected` | the behaviour the observation failed to meet |
| `rules` | nonempty list identifying the requirements in play |
| `register` | reference to the rule-failure register's entry or strike |
| `limitations` | list of missing or reconstructed evidence labels; empty when none are known |

All text is nonempty. Context roles are `system`, `developer`, `user`, `assistant` or `tool`.
Paths identify origins; capture does not read them or infer their contents. Repeated loaded paths
remain separate snapshots in their supplied order.

A limitation has exactly `field`, `kind` and `reason`. `field` is the JSON pointer of an evidence
leaf: `/message/content`, `/observed`, `/context/N/content` or `/loaded/N/text`. `kind` is
`missing` or `reconstructed`; `reason` is nonempty text. A missing leaf is `null` and has exactly
one `missing` label. Reconstructed text remains text and has a `reconstructed` label. Other
leaves cannot be null. Labels neither supply missing evidence nor establish its truth.

Amendments, calibration specimens, model prompts and effect verdicts are absent. The draft does
not assert that a fresh model will reproduce its observation, or that a text-only continuation
can reproduce a failure dependent on tools or state.

## Saved record

The script adds `format: "failure-capture-1"`, `captured_at` (UTC ISO timestamp) and `sha256`.
The digest covers every field except `sha256`: UTF-8 JSON with keys sorted, Unicode unescaped,
compact separators and no non-JSON constants. It is stable across file line endings. The draft's
fields are preserved without substitutions. Duplicate JSON keys are invalid.

The format check validates shape and digest, never whether the account is true or its proposed
check distinguishes the behaviour. An executable experiment is a different record.
