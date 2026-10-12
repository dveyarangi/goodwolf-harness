# The judge bench — sixteen drafts a judge is graded on, 2026-10-12

A bench for the judge of
[q-0001.0020.0001 does-a-judge-outside-the-agent-flag-the-drafts-that-hid-parts](../questions/done/q-0001.0020.0001-does-a-judge-outside-the-agent-flag-the-drafts-that-hid-parts-and-pass-the-ones-that-did-not-on-the-recorded-cases.md):
a reader outside the agent, given one of the agent's draft replies, says whether the draft commits
to a shape while leaving a load-bearing part of it unexamined. Built while probing that question,
preliminary to [01-0011.0100.0050 a-question-branches-before-it-is-answered](../tickets/01-0011.0100.0050-a-question-branches-before-it-is-answered.md),
and kept so a changed judge is graded on the same drafts *(the user, 2026-10-12)*. The bench's
files are in [`judge-bench/`](./judge-bench/); what each run found is in the question's body.

## The set

Sixteen drafts cut from the transcripts, each with the two exchanges before it, labelled `U1`–`U16`
in an order that hides their verdict. [`key.json`](./judge-bench/key.json) holds, per label, the
transcript and lines it came from, the commit its tree stood at, the verdict going in and the
evidence for it:

- **Failure** — four drafts the person later corrected: rule failure 25 twice, rule failure 11, and
  a deferral resting on a second case nobody had looked for.
- **Hid** — four accepted drafts later shown to hide a part, or doubtfully so.
- **Clean** — seven accepted drafts nothing has amended since.
- **Unknown** — one accepted draft whose part a judge flags and nobody has checked.

A person's acceptance is no clean label: two drafts first taken as controls were found to hide a
part. A verdict moves with new evidence, and the key is edited when it does. A draft whose result
proved wrong or misleading missed a part, whether or not it hedged; a ticket's size counts, since
it matters to the model *(the user, 2026-10-12)*.

## Candidates

Sixteen drafts hold four failures: one draft moves recall by a quarter, below the judge's own
variance. [`candidates.json`](./judge-bench/candidates.json) holds eighty more, labelled but not
yet checked by the person *(the user, 2026-10-12)*:

- `pairs.py` lists every agent reply and the person's next message across the transcripts —
  4,684 pairs.
- 122 replies the person answered with a correction, and 60 sampled from those answered with
  agreement, were triaged by Sonnet agents reading each with `show.py` and the tree as it is
  today: a correction pointed at a hidden load-bearing part, a local fix, the reply's form, who
  decides, or nothing; an accepted draft stayed clean, was later shown to hide a part, or was a
  report.
- Forked and resumed sessions repeat a conversation, so copies of one draft are merged; 181
  labels fell to 125 drafts. Seven drafts drew different labels from different agents; three of
  them are kept, marked `disputed`.

Kept: 45 hid — 35 found by a correction, 10 by an accepted draft later amended — and 35 clean;
each with the commit before it, the part, and the person's words. The triage was one model's
reading: a candidate joins the key once its label is checked.

## Running it

1. Lay out the trees: `snapshot.py <directory>` writes each label's repository at its commit, the
   last before the draft, into a directory outside the repository.
2. For each label, run three judges — fresh subagents, Sonnet, one per run — each given
   [`prompt.txt`](./judge-bench/prompt.txt) with `{specimen}`, `{snapshot}` and `{out}` filled in.
   A host runs twenty at once.
3. Read the `FLAG` lines: a draft is flagged by the majority of its three runs. Then read the
   `PART` against the key's evidence — a flag on a failure counts when it names the person's part.

`build.py` rebuilds `specimens/` from the transcripts, and reruns only on the machine that holds
them. A judge reads 65,000 to 100,000 tokens; a full run is forty-eight judges.

## The prompts run so far

[`results/`](./judge-bench/results/) holds every answer written to a file, by run; the first three
runs answered in the conversation and are summarised in the question alone.

| run | what changed | where |
|---|---|---|
| 1–2 | any part that could be named; one exchange; no tree | the question |
| 3 | load-bearing parts alone, the counter-test, the contract change named, reasoning; two exchanges before | `3-load-bearing` |
| 4–5 | the tree at the draft's commit | `4-5-tree` |
| 6 | a claim of absence stays unexamined until its search covers it; the machine and the web | `6-absence` |
| 7 | verify each claim of absence independently; a choice put to the person leaves its premises unexamined | `7-absence-independent` |
| 8 | absence stated or implied — `prompt.txt` as it stands | `8-absence-implied` |
| 9 | the same prompt over the other nine drafts | `9-all-sixteen` |
| 10 | the counter-test *given how the project evolves*; the live repository closed to the judge — `prompt.txt` as it stands | `10-evolution` |
| 11 | run 10's prompt and the same without *given how the project evolves*, five runs a draft each | `11-five-runs-A`; `11-five-runs-B` holds runs 4–5, runs 1–3 are `10-evolution` |
| 12 | run 10's prompt over `V1`–`V66`, three runs each; trees under `D:/jt` | `12-sixty-six` |

Run 10 won back rule failure 25's fourth draft (2/3) and lost the deferral (0/3, 2/3 in run 8),
and two drafts taken as clean drew a majority. Between runs 8–9 and 10, three drafts moved across
the majority line in each direction under a one-clause change: at three runs a draft, the bench
does not separate a prompt's effect from the judge's own variance. Run 11 compared the two at five
runs a draft: the same catches, the clause flagging less.

Run 12 is the judge as it stands, recorded so *(the user, 2026-10-12)*: over `V1`–`V66` it flags
18 of 33 hidden parts and 5 of 33 clean drafts, right three times in four when it flags. Most of
what it never flags is what a shape is for, which only the person's intent settles; if the judge
cannot generalize to that, it is taught later and graded on the same drafts.
