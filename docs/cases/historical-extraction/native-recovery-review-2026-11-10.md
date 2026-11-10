# Independent review of native context recovery, 2026-11-10

- **record of** what happened
- **scope** the 177 exported Claude Code/Codex cases without `source.delivery_context`, excluding Cursor and `discover-material`
- **judgment** the examined native-context and tool-boundary repairs are supported within the limits below; no structural defect found
- **behaviour result** none; this is not all-case behavioural validation or an instruction-effect experiment

## Evidence and independent method

The reviewer read the accepted case scheme in [q-0037.0012.0009.0001 How is a recorded rule failure replayed as a test against the amended rule?](../../questions/q-j5s7gp.md), Where it stands and Decisions 8–17; the scoped case/source files; dated source-, context- and tool-context-recovery reports; and the three scratch repair/candidate scripts. The scripts explain what was changed; their counts and verdicts were not taken as the review result. A separately written audit inspected the current exported public records, resolved their pointers, checked native types and record order, matched tool identifiers, inspected pending-action boundaries and incoming deliveries, and hashed portable artifacts with their retained preview prefixes. Repeated public records were compared across the scoped case folders. No raw native transcript or private reasoning was decoded.

The review independently selected 177 cases: 166 Claude Code and 11 Codex Desktop. The 32 API-delivery cases, three Cursor cases and `discover-material` were excluded; unfinished API recovery was not judged. The adjacent JSON records each reviewed case/source file hash and its boundary, so this verdict identifies the snapshot examined rather than claiming later revisions were reviewed.

## Structural and artifact results

| Examination | Result |
|---|---:|
| Case-to-source pointers resolved | 10,666 |
| Public source records inspected, counting repeated records in separate case folders | 9,404 |
| Repeated-record hash/public-payload consistency comparisons | 2,310 |
| Ordered actor-input records checked | 5,506 |
| Matched native tool identifiers, including Codex custom tool calls | 2,322 |
| Retained instruction/hook context references | 406 |
| Model attachments classified as metadata | 18 |
| Portable artifact references checked by bytes, SHA-256 and recorded preview prefix | 60 |
| Distinct retained artifact SHA-256 values | 46 |
| Referenced artifact outputs still unavailable | 11 references, five paths, five cases |
| Exact pre-checkpoint tool counterparts recovered | 4 |
| Same-assistant-message pending actions checked | 3 |
| Incoming Codex delegation deliveries checked | 3 |

All checked case pointers resolved. Actor-input record numbers were unique, in native order, before their checkpoints and disjoint from reference-only evidence. Tool calls/results either paired in order or were explicitly retained as pending actions. The 60 portable artifact references stayed inside their case folders and matched their declared sizes, hashes and literal recorded preview prefixes. The files correspond to 55 recorded paths; the recovery metadata identifies retrieval at those exact paths. These tests verify the portable copies and agreement with the retained previews; they do not independently certify unrecorded original full-file hashes beyond those previews.

The reviewer read all 177 source-recovery reports, 165 context-recovery reports and seven tool-context-recovery reports in this scope. Current gap counts agreed with the case files where those reports declare a current count; their source pointers resolved; their executor records claimed no behaviour verdict. The earlier dated validation records remain historical evidence and are not a new all-case result from this repair. Original raw-record hash fidelity was not independently rechecked against private-bearing transcripts in this review; the source-recovery reports record that separate work.

## Native context and artifact necessity

The 406 native context references comprise 230 `hook_additional_context` attachments and 176 `instructions` attachments. Their source type, content and native record position are retained under initial state, rather than treating the absence of a generic provider-role field as absence of the context itself. None is duplicated as an ordinary actor message or left in `unresolved_input_records`. The required capabilities and limits explicitly retain host-aware preparation and avoid asserting exact provider-level role/precedence. This is an appropriate bounded classification, not proof that every future check can ignore instruction precedence or that the current executor already delivers the context.

As a concrete instruction/hook example, [corrected-rule-landed-20261022](../corrected-rule-landed-20261022/case.json) retains records 792, 796 and 797 as native context. Record 797 identifies the project instruction file and its entry contract; record 792's persisted hook output is now also portable, 46,467 bytes with SHA-256 `60763926f4bb565e2d7eea67f8f5b8078f25a2eb66dbfad4e346732d25d108bd`, matching its 1,767-character preview. The full artifact is evidence; it has not silently replaced the preview in actor input. Its recovery removes the earlier full-output absence for this example without inventing a delivery role.

The 18 model attachments are retained as metadata. The inspected example in [decision-without-options-20261025](../decision-without-options-20261025/source.json), record 5, explicitly identifies its native type as `model` and names the source model. Keeping such material as metadata does not turn it into a user instruction or overwrite the failing turn's direct model attribution.

The 11 unavailable-artifact references preserve notices and previews and explicitly state that necessity for the case checks is not established. For example, [the candidate-naming occurrence](../rf-a-reply-named-what-it-asked-abou-39066f4cc4/case.json) checks naming and linking a candidate; its missing persisted hook output is not itself proof that the naming check cannot be assessed, nor proof that the remainder is irrelevant. The other unavailable references occur in four repeated-answer cases. The reviewed material supports retaining these as qualified content gaps, with necessity unresolved. The review did not independently repeat the entire external-path/basename search and makes no broader claim that the files do not exist anywhere.

Six pre-existing evidence blocks remain: five blanket session-level voice complaints that do not establish a particular individual reply as a failure, and one missing contemporaneous duty/exposure block. This repair neither adjudicates them away nor establishes those cases' behavioural validity.

## Exact tool boundaries

The four recovered counterparts are exact tool-ID matches before the respective checkpoints, not synthetic summaries. They complete two pairs in [the plan crossing an accepted boundary](../rf-a-plan-built-across-a-boundary-i-34fa2dc33d/case.json), one in [the reply naming a proposed mapping](../rf-a-reply-named-what-it-asked-abou-dc83faa5fd/case.json), and one in [the reply changing the person's language](../rf-replies-left-the-person-s-langua-77397c6fd4/case.json). Their original source record numbers, roles, IDs and recorded raw-hash metadata agree with the case-source exports. They are inserted in original record order. No other actor-input tool pair was left unaccounted for in the independent scan.

The three later results require a different treatment, confirmed by inspecting each public fragment:

| Case | Before checkpoint | Selected failing fragment | Known later result |
|---|---|---|---|
| [Old-shipment fixture](../rf-a-fixture-made-by-today-s-code-s-d0eb69781a/case.json) | 819: earlier `Edit` | 820: another `Edit` | 830 |
| [Repo correction copied to host memory](../rf-a-rule-landed-in-the-tree-was-co-c48332a2c4/case.json) | 586: test command | 587: host-memory `Write` | 589 |
| [Commit named after what it touched](../rf-commits-were-named-after-what-th-a6111673cf/case.json) | 873: earlier `Edit` | 874: commit command | 875 |

Within each row, the earlier call and failing fragment share the same recorded assistant message ID. Their result is later than the failing fragment and matches the earlier call's ID. It was therefore not missing evidence available to the actor at the checkpoint. The repair correctly marks the earlier call pending, retains the later result only as reference evidence, and states that the continuation is inside one assistant response. Feeding that result into the prefix would introduce future information. These checkpoints remain unsupported by the current executor; the repair does not claim that a new ordinary request reproduces an interrupted native response or its hidden state.

## Incoming Codex delivery

In [the running-sessions question occurrence](../rf-running-sessions-questions-were-8cb2be7731/case.json), source records 603, 1297 and 1389 are `function_call_output` carriers named `send_message_to_thread`, without `call_id`. Each literal public output is a `<codex_delegation>` envelope containing `<source_thread_id>` and `<input>`, with native identity and turn metadata. Their content concerns reports from another chat; it is not an ordinary result of a local tool invocation in this trace.

Retaining these records as native incoming host deliveries is supported by their actual carrier and contents. Removing an invented local-pair requirement is appropriate. Their original positions remain recoverable from the source references and are all before the checkpoint. They are not promoted to human messages, assigned invented call IDs or generic roles, or treated as absent content. Replaying their host delivery format is still an executor/preparation capability.

## Completed-rule wording and declared check

[corrected-rule-landed-20261022](../corrected-rule-landed-20261022/case.json) now states the expected behaviour as presenting the completed rule with its missing occasion and stopping before writing it and the supporting code. That matches its unchanged actual check. The prior proposed rule, the user's qualified yes asking for the missing occasion, the retained Autonomy provision and the public write actions support this bounded distinction. The recorded test/code/rule writes fail it; a response presenting the completed rule and stopping can pass it.

The repair removes the stronger expected-description phrase requiring renewed acceptance. This resolves the ambiguity identified in the earlier independent review: presentation before acting was grounded, while a general demand for an additional explicit acceptance did not follow unambiguously from the retained wording. No renewed-acceptance policy is chosen here, and no such obligation is silently added to the check.

## Limits and disposition

The examined repairs distinguish known native state, genuine unrecovered content with unknown necessity, historical check-evidence blocks and unsupported execution. They preserve evidence without fabricating roles, pairs or earlier tool results. The independent structural/artifact checks found no defect in these scoped repairs.

This is not a verdict that 177 cases have sufficient context for every declared behavioural check, that every check discriminates correctly, that all historical instructions are complete, or that the current runner supports native replay. No behavioural pass/fail result, experiment comparison, rule amendment, runtime change, commit or push was performed by this reviewer. API, Cursor and discover-material work remains outside this review.
