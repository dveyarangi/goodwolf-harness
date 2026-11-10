# Independent API recovery review — 2026-11-10

**Bounded verdict: PASS after repair of a public optional-field omission. No necessary material fix remains within this review scope.**

This review covers the 32 recorded-API public history exports, case/source integration, source provenance, native tool chronology, and retained public hook artifacts. It is a source-recovery and integration verdict. It certifies neither behavioral effects nor semantic sufficiency of every case. No model experiment was performed. Current executor support remains unsupported, with null behavior verdicts.

## Independent coverage

| Check | Result |
|---|---|
| Recorded request histories | 32 cases; 10,963 message positions. Every stored request delta chain reproduces exact hash order and anchors to the selected requestRef, request record, and message count. |
| Public projections | 5,231 unique message/source combinations reproject safely to the saved messages; all 5,732 repeated positions agree. Roles and public content order are preserved. |
| Native canonical hash gates | All 2,594 unique native candidates reproduce the recorded request hash before private-block projection. |
| Native tool chronology | 4,175 calls and 4,175 results pair by ID in call-before-result order with the recorded assistant/user-or-tool roles; no orphan, duplicate, or unreturned ID. |
| Local pointers | All 23,253 local JSON pointers in the 32 case records resolve. |
| Source row provenance | 7,328 specifically referenced original rows hashed opaquely to retained SHA-256 values; 463 selected public source overlaps agree. |
| Native model values | 550 unique original model scalars equal retained source values. Every case model_source pointer agrees with its recorded provenance. |
| Reference evidence | Selected failure rows and all 534 reference-only rows remain outside additional actor source rows. |
| Public hook artifacts | 27 retained artifact references have matching bytes, length, SHA, native evidence references, and captured public preview prefixes. |

The actor sequence consists solely of API-message pointers in recorded request order. Raw transcript line order is not substituted for that sequence. The 92 retained native attachment references and 66 instruction snapshot references remain initial-state evidence, rather than additional actor messages. Public exports account for 2,632 omitted provider-private blocks; no private typed nodes remain in the inspected public API/source structures. No unresolved positions or unsupported public fields remain in these 32 final exports.

## Finding raised and repaired

The initial reader silently dropped message-level output_config in 17 unique original system-role blobs and clear_at in six, while reporting no unsupported field. The known observed shapes are output_config = object with an effort string, and clear_at = string. This was a material reporting/projection defect, rather than evidence of changed request order.

The repaired reader retains both public fields and reports unknown API-blob message key names without decoding their values. Independently constructed fixtures passed six additional assertions, including rejection of private provider content and an unknown-field private sentinel at the JSON decoder. Earlier independent helper reviews supplied 29 and 53 fixture checks, including recovery of ten consecutive tool-result fragments. Built-in probes were not adopted as the review verdict.

The final exports restore 32 output_config positions and 637 clear_at positions. Every restored value was independently compared with its specifically referenced original public metadata. Removing only those restored fields reproduces all 32 pre-repair whole-file SHA-256 values, preserving Windows line endings. Thus request order, roles/content, source provenance and every other byte of the API files remained unchanged by this repair.

Each current API fingerprint matches its repair and context-update report. Artifact-copy fingerprints remain the actual pre-repair fingerprints, explicitly labelled as historical snapshots; the later projection update has a separate current fingerprint. A prior copy event was not rewritten to pretend that a new copy occurred.

## Integration and gap claims

I read integrate_api_context.py. It replaces actor input pointers with the recorded request vector, keeps native attachments/saved snapshots as evidence, and retains unresolved positions or unsupported projection gaps when present. Its removal of the earlier absent/incomplete-context and unpaired-tool export categories is supported here by the recovered vector and independent chronological tool-ID checks. Transport parameters, environment state and executor support remain expressly outside the recovery claim. No unsupported all-case sufficiency or behavioral-success assertion was found in the current recovery reports.

The selected failure/correction records remain reference evidence, without being inserted as distinct actor rows. This does not claim that no historical content resembling a later correction can appear in an earlier native message; source-row identity and the selected request vector determine the tested boundary.

## Hash and historical-diff limits

Recorded API-blob hashes link request keys to exact stored source blobs. Their raw source-row SHA-256 and safe public projections were independently checked. Hashing the entire stored message object reproduced 2,042 unique blob hashes; 595 did not reproduce under that tested field domain/serializer. The provider’s full internal hash domain is not established. This review does not call those 595 mismatches missing input, and does not claim to have recomputed every provider hash from a public projection.

There is no complete pre-integration case snapshot, and these case files were absent from HEAD. Therefore this review cannot prove byte-for-byte preservation of every earlier criterion, bound or replay limit. The integration code writes replay/source_gaps rather than expected/check/provenance. Every expected-source reference and meaningful qualification text from the earlier selection specification remains retained. Two commit-prefix criteria use earlier repaired source-backed wording documented in repair_recovered_context.py and recovery-71-73.json; the selection specification is not an unconditional latest baseline.

Filtering follows the reviewed provider content schemas and private tags; arbitrary public application/tool-input JSON is not universally reclassified by tag names. Primitive serializer spelling, unique keys, inner-role interpretation and the 32-message consecutive search bound remain explicit helper limits. A copied artifact’s checksum authenticates the retained bytes; its recorded hook preview authenticates the captured prefix, not an independently recorded historical checksum of the entire external file.

No full original transcript row was loaded with a JSON decoder. Specifically referenced raw rows were hashed opaquely; model scalars and reviewed public projections alone were decoded. Raw/private source rows were never persisted by this reviewer. Runtime, rules, case artifacts and git state were not edited by this review.

Per-case counts, current API fingerprints, repair checks and remaining limits are in [the accompanying JSON](api-recovery-review-2026-11-10.json).
