# Public source recovery review, 2026-11-10

- **record of** what happened
- **reviewer** independent subagent `judge_public_sources_final`
- **scope** all 212 historical occurrence folders with `case.json` under `docs/cases`, excluding `discover-material`
- **governing acceptance** [How is a recorded rule failure replayed as a test against the amended rule?](../../questions/q-j5s7gp.md#where-it-stands), Where it stands and Decisions

## Verdict

No new public source fidelity, attribution, structured-pointer or retained-artifact integrity defect was found in the examined selections. This is a bounded source review, not a verdict that every case is behaviorally valid or ready to execute. Existing source qualifications remain in the cases.

## What was examined

The corpus contains 198 Claude Code, 11 Codex Desktop and three Cursor occurrence folders. The original-row comparison checked 10,973 selected record references across primary and related sources: 8,468 unique transcript/row pairs in 76 transcripts. Their original row hashes and selected public payloads matched; there were no unsupported comparisons. Transcript snapshot hashes were checked against the recorded original byte lengths where present.

The inspected comparison code uses byte-span field scanning, skips known typed private blocks before decoding, and projects only selected public content and metadata. It does not JSON-decode complete raw provider rows. The Cursor check hashes selected original SQLite values opaque, then reads only selected public metadata, text and tool-action paths. A synthetic private-block decoder probe passed. No old raw extractor or `verify_replay_sources.py` import was used.

All 209 known model identifiers matched their literal source pointers. The 198 Claude cases also matched the selected failing assistant record's message ID, record UUID, native session ID and timestamp. Each Codex model pointer names the latest preserved `turn_context` before its selected failure; the native host, session ID, failure ID and timestamp agree. The additional envelope check matched timestamp and type for 527 selected Codex record references. All 212 case/source chat IDs agree. These checks concern source-reported attribution and do not identify unrecorded provider-side state.

The Cursor comparison matched 50 selected original SQLite value hashes and selected metadata, 11 public texts, eight public tool-action projections, 19 model-field presence/value checks and 27 timestamp fields. The 30 public tool-sequence entries matched their selected native argument fields, and two portable exported write contents hashed to their native content-address identifiers. All three actual assistant models remain `unknown`. Requested user model metadata is retained separately and agrees with its selected original source; it is not promoted into actual-model attribution.

All 33,943 structured case pointers into `source.json` or `api-input.json` resolved. A final pointer-only pass after the API public optional-field refresh resolved those same 33,943 pointers, and the case/source file snapshots remained unchanged. The public API request structural/optional-field semantics and native transport-context semantics were assigned to other judges and are outside this verdict.

For 87 retained ancillary artifact references, the case-relative file stays inside its case folder, its byte count and SHA256 match, its UTF-8 text begins with the preserved native preview, and its full bytes equal the file at the exact recorded original path. Six historical Git blob references matched their revision/path/blob identities and SHA256 values; 15 retained line-range excerpts matched the committed text.

## Qualifications and limits

Eleven referenced full public hook artifacts remain explicitly unavailable, with the original notice and preview retained and a case source gap naming each. Their necessity for the case checks is not established by this review. A retained artifact's current full-byte match and historical preview-prefix match do not supply an independent historical full-content digest that the original notice never recorded.

The row comparison establishes fidelity of the examined public projections. It does not establish that every original public row was selected, that all relevant initial state was recovered, or that a retained sequence is sufficient to reproduce the failure. Private reasoning and hidden provider state remain excluded. Model-source equality does not establish unrecorded provider-side routing.

Nine case check status fields retain a blocked prefix. This review changes none of those statuses, treats no executor inability as a behavioral failure, and supplies no pass/fail result for case behavior, context sufficiency or check discrimination.

The [machine-readable review](public-source-recovery-review-2026-11-10.json) retains the counts, explicit source qualifications and unavailable references, the existing blocked status fields, and SHA256 snapshots of every reviewed `case.json` and `source.json`.
