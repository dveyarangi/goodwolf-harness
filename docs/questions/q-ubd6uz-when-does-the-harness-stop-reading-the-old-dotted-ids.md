# q-ubd6uz When does the harness stop reading the old dotted ids?

- **record of** what it intends to become
- **part of** q-7ebz2f
- **state** open
- **rung** development: load-bearing, self-improvement: the method
- **opened** 2026-11-15T18:18:28Z
- **struck** 0, last 2026-11-15T18:18Z

The residue of [01-0010.0250.0100](../tickets/done/01-0010.0250.0100-a-questions-id-never-changes.md): its
stage 6, set apart so the ticket closes without waiting on every tree *(the user, 2026-11-15: "давай
не будем ждать остальных, продолжаем работу")*. Core reads the dotted form beside the new one
while a tree of the person's may still hold it, because `migrate_ids.py` reads another tree's store
through the store's own reader; the stage's work is in [the RFC](../rfc/done/01-0010.0250.0100-a-questions-id-never-changes.md#stages).

## Where the trees stand, 2026-11-15

- Migrated: this tree, game-delta, research-harness, codename_japaka, game-gamma, jobs; each found
  a gap the script then closed.
- Waiting, the note `HARNESS-MIGRATION.md` left at their root: frost_map and
  DriftSense/workspace/agents, each with a core update left uncommitted to sort out with the person
  first; xuanxue-workshop, whose session has not started on it.
- Not migrated, by the person's word: studies, reinstalled for each test of the install; ai-game-1
  and game_beta; meteoscape, whose install was reverted on 2026-10-15.

It closes when the waiting trees have run, or the person lets them go, and the dotted half of the
pattern, its `TODO`s and the painted door for `docs/questions/done/` have left.

## What stage 6 must keep in mind

Found by the verification of 01-0010.0250.0100, 2026-11-15:
- `at` answers an old id with its new one through `_existing`, after the id pattern has accepted it.
  Dropping the dotted half of the pattern refuses `at q-0037…` as no id, and that answer is lost
  unless the lookup moves ahead of the pattern, in `_question_id` and in `--hold`/`--take`.
- The dotted half of `QUESTION_ID` has no closing lookahead: `q-2345ab7` reads as the dotted
  `q-2345`. It leaves with the dotted half; the all-digit test comes in then.
- The table of former ids stays: history is read through it for good. What leaves is reading the
  old form in the store, its `done/` and the `TODO`s bound here.
