# Independent case validation, 2026-11-09

Reviewer: `/root/judge_replay_pilot_v2`, independent of the case extraction and control author.
Scope: this case's source fidelity, sufficient public context at its continuation point,
provenance, boundaries and three response checks. This review did not use the old
validation's verdict as evidence and did not run an instruction-effect experiment.

Verdict: **valid recovered continuation case for its three checks; execution unsupported
by the current adapter**. No source gap was found within that declared scope. This does
not establish autonomous recall from the greeting, whole-harness compliance, runner
compatibility or the effectiveness of an amendment.

The governing boundary is the [accepted case scheme](../../questions/q-j5s7gp-how-is-a-recorded-rule-failure-replayed-as-a-test-against-the-amended-rule.md),
Where it stands and Decisions 8–17. Case and source references below are folder-local.

## Source fidelity and provenance

- The original transcript's SHA-256 is
  `3937cb023550a79dcbc5401a103fe54d675be789e3a26e7d1e7a170186314f50`, matching
  [source.json](source.json). All 20 retained records' `original_record_sha256` values
  match their original JSONL lines, excluding the line delimiter.
- The complete public payloads of records 3, 4, 5, 6, 7, 8, 12, 13, 14, 15, 16, 18,
  22, 23, 26, 30, 36 and 41 match the originals exactly as parsed JSON values.
  Records 1 and 10 are expressly labelled selected metadata; every selected field,
  timestamp and record type matches the original.
- Record 1 supplies Codex Desktop and chat `01a17792-eb83-75d1-9fc4-dedb2eed8589`.
  Record 10 supplies model `gpt-6.1-sol` and turn
  `01a17793-050a-7690-a156-6f2aef7b9750`; record 41 carries the same turn identifier.
  Its timestamp is `2026-10-26T09:39:07.128Z` and its message identifier is
  `msg_0505564a4178f9c7016adf1fb661f08191a62f5caee679b560`.
  The trigger identifier in [case.json](case.json) matches record 16. These are
  source-reported identifiers, not an attestation of the resolved model backend.
- Internal evidence references resolve to the local source or control file. The original
  transcript basename identifies the recovery source; inspecting this case's necessary
  evidence does not require reopening that machine-local transcript. Historical absolute
  paths inside verbatim payloads identify the commands and environment that were recorded;
  their returned contents are retained locally rather than fetched from those paths.

## Context and replay boundary

The input list is in original order: 4, 5, 6, 7, 8, 12, 13, 14, 15, 16, 18, 22, 23,
26, 30, 36. It preserves the original message roles and native tool record types.
Records 23/26 share `call_98fcf803d6e44eff890167c8bad53851`; records 30/36 share
`call_3ae7b7b0839a41e9ab36a184234d60b9`. Tool definitions remain in record 3,
referenced by initial state. All public messages and tool payloads before the final
response are present. Only public payloads and session/turn metadata were inspected;
private reasoning contents were not inspected.

After record 36 and before record 41 is an honest public continuation boundary. The
intervening records are token/item events and a private reasoning record, with no new
public message or tool result. The next assistant response is record 41. Its recorded
text matches `observed_failure.response` and is excluded from `replay.input_records`.
There are no records after 41 in the extracted evidence; later corrections and the
constructed control are therefore absent from actor input. The original instructions
remain historical evidence; the case contains no standing/amended experiment variants.

Record 8 requires recall in every conversation, whatever the first message says.
Record 26 contains the original recall skill, including a compact summary of current
state and “recommend one and say why.” Record 36 contains the work path, ready
candidates, session positions, status and recent commits. That is sufficient public
evidence to answer the three checks at this checkpoint. It does not establish that
every deeper investigation called for by the original skill had been completed.

## Independent response assessment

| Response | State | Next candidate | Reason |
|---|---|---|---|
| Recorded final, source record 41 | false | false | false |
| Authored specimen, control.json | true | true | true |

The recorded final's body is “Привет! Контекст прочитал, я здесь.” It states no work
status, proposes no next candidate and supplies no reason. Its session-position table
alone does not describe the current work state requested by this check.

The control says “В работе четыре направления” and names assessment before installation,
contradiction sweeping, reply voice and README. These correspond to record 36's four
in-work entries. It says “Следующим я рекомендую взять удаление harness из проекта”;
the recorded ready path contains “A project can remove the harness.” Its reason is
“эта задача уже стоит среди готовых кандидатов, и она даст проекту возможность
отказаться от установленного harness.” Eligibility and intended outcome are supported
by that same path. This is a minimally explicit reason for its recommendation, not
evidence that removal uniquely outranks the other ready candidates; the source ranks
none above another. The specimen passes these three checks without being the uniquely
correct response or a specimen of complete harness compliance.

## Execution limitation

In `.agents/scripts/gw/amendment.py`, `validate_case` requires combined experiment
fields, including `common`, `standing`, `amended`, `paragraph`, `situation`, `discovery`
and `message` (lines 27–45). `run_case` forms one text prompt from situation, discovery
and message (line 155), and `CodexHost.run` submits that text through CLI stdin
(lines 75–81). There is no input path there for the ordered native messages and paired
tool history this case requires. No executor run was attempted, and no successful or
failed model-behaviour result is assigned. This is an execution limitation, not missing
source evidence. The recovered case remains available in the corpus.

The historical `validation.md`, `control.json`, `case.json` and `source.json` were
left unchanged. This report and an appended independent result in
`validation-2026-11-09.json` are the only case files written by this reviewer.
