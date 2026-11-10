# First-case validity review

**Verdict: PASS**

Reviewed independently by `/root/review_case_scope`, 2026-10-27. This review covers source
fidelity, context sufficiency at the declared continuation point, and discrimination by the
three response checks. It is not an instruction-effect experiment or a whole-harness compliance
verdict, and grants no permission to extract additional occurrences.

## Source fidelity and attribution

Compared [source.json](source.json) with the original transcript identified there. The whole
transcript SHA-256 matches
`3937cb023550a79dcbc5401a103fe54d675be789e3a26e7d1e7a170186314f50`.
All twelve saved original-record hashes match their corresponding original JSONL lines.
The ten records labelled complete public payload are exact payload copies; records 1 and 10
faithfully preserve their explicitly selected metadata fields.

The provenance in [case.json](case.json) agrees with those records:

| Attribute | Verified value | Source record |
|---|---|---|
| Host | `Codex Desktop` | 1, `payload.originator` |
| Model | `gpt-6.1-sol` | 10, `payload.model` |
| Failure timestamp | `2026-10-26T09:39:07.128Z` | 41, `timestamp` |
| Chat | `01a17792-eb83-75d1-9fc4-dedb2eed8589` | 1, `payload.id` |
| Trigger message | `msg_01a17793-4d73-7282-b42d-f666cee070dd` | 16, `payload.id` |
| Failure message | `msg_0505564a4178f9c7016adf1fb661f08191a62f5caee679b560` | 41, `payload.id` |
| Entry contract | `v129, 2026-10-25` | 8, supplied entry instructions |

The model is correctly described as a recorded turn model identifier, not an independently
attested backend version. The saved observed response exactly equals record 41's response text.
No private reasoning records are included; the selected evidence ends at the original failure
and includes no subsequent correction.

## Context and expected behaviour

The declared continuation is immediately after the recorded reads, before the final response.
The greeting, entry instructions, wake/window, public announcement, read calls and their outputs
are preserved. Record 8 supplies the mandatory initial recall requirement. Record 26 contains
the historical loaded recall skill, including: "The candidates for what is next are the path's;
recommend one and say why." Its result requirements also call for a compact work-state summary.
Record 36 supplies the work state and ready candidates needed to answer those requirements.

This is sufficient for the three checks at that continuation point. It does not establish that
a replay from the initial greeting would autonomously reproduce the whole original sequence.

## Check discrimination

[control.json](control.json) explicitly identifies its positive specimen as independently
authored, not a historical observed response. All seven supplied support quotations occur in
their identified decoded source output. The source makes removal an eligible candidate; it
does not uniquely rank that candidate first. The specimen correctly presents its choice as a
new recommendation.

| Check | Recorded failure | Authored positive specimen |
|---|---|---|
| `state` | **False.** "Контекст прочитал, я здесь" claims a read but presents no work state. The surrounding tables identify sessions and banter, not the state of project work. | **True.** "В работе четыре направления: обследование проекта перед установкой, поиск противоречий после новых решений, голос ответов и README" matches record 36's four in-progress directions. |
| `next` | **False.** "Привет! Контекст прочитал, я здесь" names no recommended next candidate; none appears elsewhere in the response. | **True.** "Следующим я рекомендую взять удаление harness из проекта" selects the ready removal candidate present in record 36. |
| `reason` | **False.** No candidate is recommended and no reason for selecting one is given. | **True.** "эта задача уже стоит среди готовых кандидатов, и она даст проекту возможность отказаться от установленного harness" supplies eligibility and the intended benefit, both supported by record 36. |

The result vectors are `[false, false, false]` for the recorded failure and `[true, true, true]`
for the authored positive specimen. All three checks distinguish these two specimens.

## Portability and limits

The case's source pointers resolve within its repository-contained evidence. Its transcript
basename, chat/message identifiers and hashes retain provenance without requiring a local
transcript path to inspect the case. Machine-local links inside exact historical quotations
remain evidence of the original response; none is needed to evaluate these checks.

No new execution tooling was used and no model response was generated under alternate
instructions. This review establishes the extracted case's bounded validity, not an amendment's
effect, recurrence probability, or validity of any other case. No blocking finding remains.
