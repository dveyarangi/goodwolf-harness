# Red and green — `/harness`'s first install and `/maintain`'s report, 2026-10-18

The second slice of [q-0037.0010.0012.0001](../../../questions/q-0037.0010.0012.0001-how-does-a-rule-tell-the-work-an-agent-does-unseen-from-what-it-says-to-the-person-about-that-work-and-how-is-a-reply-tested-for-keeping-them-apart.md).
Rules at `0e3233f` for red; the two skills' `What the person hears` for green.

## The bench as run

- **writer.txt** now names no skill: each case holds `context.txt` — the moment, the skill, and what
  the session holds — beside `message.txt`. `morning` gained its `context.txt`; its
  `session-start.txt` is unchanged. Opus, debug off, reading only.
- **reader.txt** unchanged. Each run's reader got the template filled with the message and the
  reply, as a file it was told to read and nothing else. Sonnet.
- **Cases**, from [rule failure 51](../../../rule-failures.md#51-an-installs-introduction-told-the-person-what-was-copied-and-asked-everything-at-once--2026-10-15)'s
  sessions in `codename_japaka`, 2026-10-15, under today's installer (its output from a fresh
  install of `0e3233f` into an empty folder, paths renamed):
  - `install-first` — the original: an empty folder, a clone fast-forwarded, a fresh clone failing
    on long paths and got round, two links refused.
  - `install-plain` — the fourth install: an empty folder made a repository, nothing else wrong.
  - `install-close` — the first strike, which reported the commit and every line of
    `local.rules.md`: the last answer given, the links run, local rules written, checks green,
    the install committed.
  - `maintain-tree` — the scheduled whole-tree pass of 2026-10-14 (`e9e8acc`), its findings as
    the session held them.

## Red — the rules at `0e3233f`

| case | flagged | what the reader quoted |
|---|---|---|
| install-first | 1 / 5 | the method's own description — *files are only its carrier*, stored as files, noted — and the issue row in the ⚖️ table |
| install-plain | 1 / 5 | the method's description and the ⚙️ row |
| install-close | 3 / 5 | *your answers are written into the project's rules*, *saved by a commit*, *recorded here, nothing sent out*; the 🪶 Commits table |
| maintain-tree | 5 / 5 | every report, 5–8 sentences each: four mechanisms moved, each doc read against its decision, three agreed, the guess's candidates judged or not, the store's flags, *the pass did not re-read it*, checks pass, main matches origin |

Today's install opening was already near green: *what the run did … is said only on request* had
held since failure 51's third amendment. The close and the maintain report were not.

## Green

`/harness`: *After the first install* keeps the work — read the entry file, take what the install
needs, write the local rules, install, check, commit. Its speech moved to `What the person hears`:
what it spares them, the asks one at a time, and, new, at the close *that it is ready, and the first
question the work asks*; the on-request list gains *wrote* and *that their answers are written
down*.

| case | flagged | what the reader quoted |
|---|---|---|
| install-first | 1 / 5 | the method's description again; the issue ask |
| install-plain | 1 / 5 | the method's description; the ⚙️ row |
| install-close | 2 / 5 | the 🪶 Commits table (both); *your answers are written down*, once |

`/maintain`: F2 removed and B1's *write it into the report* with it; the report is the section.
Three wordings were run.

| wording | flagged | length | what the reader quoted |
|---|---|---|---|
| 1 — *what it went over; what was out of agreement and how it stands; what is left open — found and not settled, or not looked at* | 5 / 5 | as red | the same course as red: writers took *what it went over* and *not looked at* as leave to tell the pass |
| 2 — *in a few lines: done, over what; each thing out of agreement, now right; what is left, as where it stands; nothing else of the pass is told* | 5 / 5 | half of red, three short paragraphs | the repair described, *the pass did not re-read it* (4 of 5), how the store's check finds its pairs, the 🪶 Commits table |
| 3 — *each thing out of agreement, in a line; each said as where the work stands, never as what the pass did or did not do, nor how a check found it* — the section as landed | 3 / 5 | 1,000–1,250 characters: done, the one repair, the one question left, the one decision | the repair's one line, the store's word *suspect*, the pairs' *overlapping wording* in the decision itself, the 🪶 Commits table; nothing of what the pass did or skipped |

`morning` under the generalised writer, five runs: a greeting and one line each — *Сейчас посмотрю /
вспомню, на чём мы остановились* — none flagged. The first slice holds.

## The user's rulings, and v95

The user, on the rounds above: *commits is told as the table in the debug mode*; *maintain report
can tell what was fixed in debug mode*. The entry file's reply form, v95, now says as a sentence of
its own that *a commit is machinery: with debug off, a reply shows no commit table and no commit's
hash*; `/maintain`'s section names what it put right in a few words, what was wrong in it told only
under `debug=on`. The question the user asked about *the method's description* is answered in the
reply, not here.

**A flaw in the bench, found here.** A writer spawned by this session inherits the entry file as
the session loaded it at its start, and reads that copy instead of the disk. Two rounds under v95 —
[`stale/`](stale/) — kept the commits table in 19 of 20 replies; asked why, a writer quoted v94's
sentence from its context. `writer.txt` now tells the writer to read the entry file from disk, the
copy in its context perhaps older. The skills were never in that context, so every round above,
run on an unchanged entry file, stands.

| case | before v95 | v95 | what the reader quoted |
|---|---|---|---|
| install-close | 2 / 5 | 0 / 5 | nothing |
| maintain-tree | 3 / 5 | 2 / 5 | the store's own words, *suspect*, *superseded*; once, the four mechanisms that moved |

No reply under v95 carries a commit table or a hash.

## What the bench left to the user, and how it was settled

- **The method's description at the install.** In both runs one opening in five was flagged for
  the three troubles and their answers — *kept as files in their repository*, *a remark noted* —
  the text the q-0033.0008 straw dog prescribes; four in five readers called the same text what
  the person gains. The reader splits on prescribed content, and the bench does not tune it.
- **The 🪶 Commits table.** Under `debug=on` alone, v95 *(the user)*.
- **How much of a repair is told.** In a few words; what was wrong, under `debug=on` *(the user)*.
