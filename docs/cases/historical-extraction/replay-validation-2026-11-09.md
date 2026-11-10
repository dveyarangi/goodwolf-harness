# Independent review of the remaining replay-record conversion

- **record of** what happened
- **date** 2026-11-09
- **reviewer** fresh review agent; it did not extract or convert these cases
- **scope** the 211 case folders with `case.json` and `source.json`, excluding the separately reviewed `recall-no-next-step-20261026-093907` pilot
- **basis** the accepted replay boundary in [q-0037.0012.0009.0001 — How is a recorded rule failure replayed as a test against the amended rule?](../../questions/q-0037.0012.0009.0001-how-is-a-recorded-rule-failure-replayed-as-a-test-against-the-amended-rule.md), Where it stands and decisions 8–17

## Result and scope of the result

No remaining structural conversion defect was detected in the retained public records after two findings were repaired and rechecked. This is a bounded review of the conversion, not validation that every case has sufficient context or discriminating checks, and not a behavioural or instruction-effect result. The legacy `discover-material` case and its historical run artifacts were outside this review.

The final corpus contains 198 Claude Code, 10 Codex Desktop and 3 Cursor cases. Its 6,129 actor-input references resolve to retained native public messages or tool calls/results. The review checked all 13,075 source pointers in the case records, source-record order, recorded roles, separation from selected failing outputs, pre-failure boundaries, and declared call/result pairing gaps. It found no authored summary inserted as actor input or experiment instruction variants inserted into these cases. It found no unresolved pointer or unreported pairing defect in those checks.

There are 593 unresolved context references and 625 source-gap entries across 202 cases. The entries comprise 593 incomplete-context diagnoses, 9 prior source qualifications, 3 absent-context diagnoses, 9 preserved check-evidence blocks, 5 unpaired calls, 3 unpaired results and 3 absent pairing identifiers. These are occurrence-level counts: a source record can appear in several cases.

Every one of the 211 dated preparation records separately marks the current executor unsupported and its behaviour verdict null. All nine existing blocked checks are explicitly carried into the gap/status reports. Absence of a gap in the remaining nine cases means no gap was reported by this preparation; it does not certify source sufficiency or check discrimination.

## Findings repaired during review

The initial generic incomplete-context diagnosis overstated which fields were absent. In `rf-a-commit-below-every-dial-was-pu-63aa8532b5/source.json#/records/3724`, the API snapshot explicitly records `payload.message.role = user`; only instruction excerpts, rather than complete message content, are retained. The corrected diagnoses now distinguish this from host attachments whose assembled delivery role is not recorded, Cursor bubbles with retained native type/text, and lists of recovered context fragments. The review rechecked all 593 diagnoses: 523 attachments, 66 API snapshots, 2 bubble objects and 2 fragment lists. None is promoted to an invented actor message.

The September 7 Claude README-write case, `rf-the-straw-dog-rule-sat-at-tier-1-6749bbf867`, already blocked grading because contemporaneous duty exposure was unestablished, but initially had an empty `source_gaps` list. The repair carries that exact existing check status into its source-gap and dated status record. The same preservation was checked in all nine blocked cases; their underlying check statuses and grading limits remain explicit.

## Semantic checks and retained limits

The Codex correction/next-move case keeps host and turn-model metadata outside its actor sequence and excludes the failing correction and later reference records. The Codex running-sessions case retains three native result records without pairing identifiers and reports each identifier gap rather than inventing one. The actor sequences retain their native user/assistant and call/result forms.

The Claude qualified-acceptance case retains the preceding proposal, the user's qualified response and intervening public tool messages, while leaving instruction and hook attachments as unresolved evidence. The API-snapshot example retains exact instruction excerpts and its known user role without reconstructing a complete message from them. This preserves the distinction between available evidence and an assembled replay input.

The three Cursor cases keep their original action evidence and explicit unknown actual model attribution; user-requested model metadata is not promoted to assistant attribution. Their absent instruction/exposure evidence still blocks the asserted instruction-violation checks. The five Claude voice cases retain the later session-level complaint and admission without treating that evidence as proof that every selected reply violated the voice instruction. The September 7 README-write case remains blocked by its missing contemporaneous duty evidence.

The conversion helper does not rewrite the `check`, `expected_behaviour`, `observed_failure` or provenance objects. The review inspected their current blocked qualifications and representative source-backed criteria; it did not independently re-grade every historical check or calibrate constructed controls. The converted files were untracked, so this review has no immutable pre-conversion Git version against which to establish byte-for-byte preservation.

## Independent source-integrity limit

Automatic approval review rejected a proposed raw-transcript hash/completeness audit because reading and parsing entire transcript bytes could include private reasoning outside this public-only review. That command was not executed or retried. This reviewer therefore did not independently establish original-byte hashes or complete public-payload fidelity against raw transcripts. It inspected only retained public text/tool payloads and source metadata. Existing integrity evidence from other work is not represented here as this reviewer's verification.

No runtime, harness instruction, case, source or ticket was edited by this reviewer. This review wrote only this report and its companion JSON record.
