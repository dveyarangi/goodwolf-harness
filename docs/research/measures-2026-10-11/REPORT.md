# First measures of what the work costs — 2026-10-11

- **record of** what happened

Read once, at the reality check that opened the work on
[q-0018.0008](../../questions/q-0018.0008-what-does-the-harness-cost-and-save-counted-rather-than-guessed.md)
"What does the harness cost and save, counted rather than guessed?" and
[q-0017](../../questions/q-0017-does-working-under-the-harness-deliver-software-better-than-working-without-it-measured-on-the-same-tasks.md).
Evidence for the align of
[01-0010.0168 the-harness-measures-what-it-costs-and-saves](../../tickets/01-0010.0168-the-harness-measures-what-it-costs-and-saves.md),
not a decision. The scripts are one-off reads, kept so the numbers can be read again; none is a
mechanism.

## The scripts

Each runs as `uv run --offline --no-project python <script> <args>`.

| script | reads | gives |
|---|---|---|
| `by_skill.py <transcripts>` | Claude Code transcripts | tokens per session and per typed turn, by week; the share of tokens by skill (`attributionSkill`) |
| `anatomy.py <transcripts>` | Claude Code transcripts | tokens by usage field; model calls by the tool each ends in |
| `per_work.py <transcripts> <tickets/done>` | transcripts, done tickets | tokens and turns per closed ticket and per checked box, by week |
| `per_day.py <transcripts>` | transcripts | model calls, output tokens, typed turns and all tokens, by day |
| `project_weeks.py <transcripts> <repo>` | transcripts, the repo's git, its question store | per week: sessions, typed turns, steps, tokens, commits, FIX commits, lines of code and of method changed, questions closed |
| `codex_weeks.py <cwd>…` | Codex sessions under `~/.codex/sessions` | per week: sessions, turns (a turn is a `task_started`), tokens, cached, output, reasoning |

Claude Code's transcripts are `~/.claude/projects/<path with dashes>/*.jsonl`; a step is one model
call, counted once though the host splits it over several lines. Subagents, in subdirectories, are
not read. Cursor keeps turns and tool calls under `~/.cursor/projects/<path>/agent-transcripts` and
no tokens; no script reads it yet.

## What they found

**This tree, 187 Claude Code sessions, 2026-09-05 to 2026-10-11.** 7.9B tokens: 98.1% context read
again from the cache, 1.6% new material, 0.3% generated, thinking included. The median call reads
257k tokens of context, the 90th percentile 522k, so a token counts steps times context length and
cannot tell thought from mechanics. Calls ending in Edit took 29% of tokens, in a harness script or
the tests 17%, in git 4%, in a reply to the person 19%. No skill attributed: 63%; implement 12.6%;
the method's other skills about 23%.

**Questions as the unit, 2026-10-02 to 2026-10-10.** 192 opened, 47 closed; 32 of the closings name
the user. Per closing: 47M tokens, 130k generated, 145 steps, 22 typed turns. 2026-10-10 the first
day closing more than it opened, and the cheapest: 30M tokens, 103 steps, 12 turns per closing.
The ratio reads the project's stage, not the work's worth (the user, 2026-10-11), and is carried by
[q-0001.0022.0001](../../questions/q-0001.0022.0001-how-does-the-weight-of-each-root-shift-as-a-project-moves-from-choosing-its-direction-to-building-it.md).

**Product projects.** JSON and lock files are left out of code.

| | meteoscape | frost_map |
|---|---|---|
| span | July–August, before this harness | 2026-09-09 to 2026-10-10, under it from v8 |
| Claude Code | 226 sessions, 3852 turns, 5.37B tokens | 60 sessions, 1430 turns, 2.44B tokens |
| Codex | 26 sessions, 125 turns, 0.19B tokens | 69 sessions, 905 turns, 0.70B tokens |
| Cursor | 45 sessions, not counted | none under its path |
| code changed | ~36.9k lines, Python | ~13.6k lines, TypeScript, CSS, Python |
| method text changed | 78k lines | 55k lines |
| turns per 1000 lines of code, Claude Code + Codex | 108 | 172 |

frost_map's work fell almost whole in one week, 38. The two differ in domain, stage, months and
models, so they compare nothing causal.

## Limits

- Typed turns are told from host notices by their text; a notice that does not open with `<`
  counts as a turn.
- Tickets, checked boxes and questions are cut by the agent that is measured.
- Lines of code count deletions and generated files the filter misses.
- Commit prefixes differ: meteoscape writes DOCS, CODE, SKILL and no FIX.
- A session started in a governing tree whose commits land in another repository —
  forecast_collector under frost_map, DriftSense's repositories under its `agents` tree — is not
  joined to them.
