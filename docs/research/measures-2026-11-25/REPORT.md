# What wakes a session, and what it costs — 2026-11-17 to 2026-11-24

- **record of** what happened

Read by [cost.py](cost.py) over Claude Code's transcripts of every project on the machine, from
2026-11-17T00:00Z to 2026-11-24T22:08Z. Units are input tokens at the API's price ratios — a cache
read 0.1, a one-hour cache write 2, a five-minute one 1.25, an output token 5; models are not told
apart, and how the plan counts is not published. A request is charged to what last woke its
session: the person's message, another session's, the session's own subagent returning, or a
compaction; a subagent's own requests are counted apart.

| | all | this tree | fimonitor | DriftSense's `agents` |
|---|---|---|---|---|
| units, millions | 527.6 | 152.9 | 262.1 | 26.7 |
| woken by the person | 44 % | 28 % | 58 % | 57 % |
| woken by another session | 21 % | 37 % | 4 % | 10 % |
| subagents | 28 % | 25 % | 34 % | 27 % |
| own subagent returning | 5 % | 6 % | 1 % | 1 % |
| after a compaction | 3 % | 4 % | 2 % | 5 % |
| re-reading above 200 thousand, across the rows above | 21 % | 15 % | 27 % | 21 % |
| requests writing over 150 thousand to the cache, across the rows above | 11 % | 18 % | 4 % | 1 % |

- In this tree the requests woken by another session cost 56.4 M, of which 22.3 M, 15 % of the
  tree, are single requests writing over 150 thousand to the cache: a sleeping chat woken by a
  letter.
- Of 150 turns in this tree woken by another session, 63 wrote a file or committed; 87 did
  neither, by the edit tools and git in their calls. A file written by a script from the shell
  counts among the 87, so the 87 is a ceiling.
- fimonitor, which holds the harness, is half of the week; its share from letters is small, and
  its largest two are subagents and long contexts.
