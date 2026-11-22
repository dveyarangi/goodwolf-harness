# q-47f7je What keeps a tracked file from bringing the person's home path, address or name back?

- **record of** what happened
- **part of** q-mhwbg3
- **state** closed:decided
- **answer** [the mechanism shape](../../.agents/mechanisms/mechanism-shape/mechanism-shape.md) — the user, 2026-11-22: a check before a commit
- **rung** development: a feature, self-improvement: a script
- **lean** 2026-11-21: three things to keep out, each scrubbed on the person's word — the home path, the email address and the name (q-mhwbg3, decisions 1 to 3) — and perhaps the commit-author address (q-ct5gnb, open); cases are written under the rule-failure register's mechanism, the keeper's; a check that refuses a tracked file holding any of them, each read at run time from the environment and git's own configuration so the check names no one — in rule_failures.py --check or at pre-push, over the pushed files alone; found trailing by the judge of the night pass of 2026-11-21
- **opened** 2026-11-20T18:39:55Z
- **struck** 1, last 2026-11-21T14:24Z

## A case, 2026-11-21: the path came back a day after the scrub

A search over every tracked file, made while the design below was drawn: one holds the home path
again — [the pathfinder's corrections](../research/pathfinder-session-corrections-2026-11-21.md),
its `Source` line naming a transcript under the person's home, committed e013aba1 the day after
decision 1 of [q-mhwbg3](q-mhwbg3-what-of-the-trees-own-records-session-cases-transcripts-local-paths-may-stand-in-its-public-repository.md)
and pushed. Told to the session whose file it is. The account address stands in no tracked file.
The search took a third of a second over 3131 files, so the whole tree is read, not the pushed
files alone.

## The design put to the person, 2026-11-21

- **What is refused**: a tracked file holding the person's home folder written as a path, read
  from the machine at run time, or any line of a list the person keeps in the clone's Git
  directory, outside every commit — the address, the name. The script holds none of them.
- **When**: with the checks of the verification set, so before a commit; and at push, by the hook
  that already runs those checks over each commit sent — a commit that adds a string and a later
  one that removes it publish it all the same.
- **What it does not hold**: the history already pushed; a name spelled otherwise; a path from
  another machine.

## Decisions

1. The check is built and runs before a commit *(the user, 2026-11-22: "проверку строй перед
   коммитом")* — with the checks of this tree's verification set. The run at push the design
   offered beside it was not asked for and is not built. Landed in the line on
   `personal.py --check`'s report and in L3 of [the local rules](../../local.rules.md)
   → [the mechanism shape](../../.agents/mechanisms/mechanism-shape/mechanism-shape.md)

## Built and judged, 2026-11-22

`personal.py --check`, the mechanism shape's, the ninth line of this tree's verification set
(L3 of the local rules). The script ships with core and runs in a tree only where that tree
names it in its own set. A judge the builder started read it three times:

- **First: fails.** The path as the cases write it most — JSON inside JSON, four and eight
  backslashes — passed; a listed name in Cyrillic was met only in lower case; a list saved with a
  byte-order mark lost its first line; and one tracked archive,
  `docs/case-runs/discover-material/2026-10-26-raw.zip`, still held the home path in 73 of its
  466 members, 521 places, which the scrub of 2026-11-20 had not reached and a read of raw bytes
  could not see. The archive was told to the session that does the scrubs and rewritten, 26bcbbfc.
- **Second: passes with findings.** Left: the archive unread, and a list in an ANSI code page read
  as noise.
- **Third: passes.** A zip archive is read member by member, to any depth; a list that is not
  UTF-8 fails the check with one sentence. Run with the scrub's placeholder as the home's name
  the check names every file that holds it, 330, and the 73 members of the archive as it was.

What it does not hold, by the judge's last report: the history already pushed; the index, where
it differs from the working tree; gzip and tar; UTF-16 with no byte-order mark; a name spelled,
spaced or broken across a line otherwise than listed; a path whose separators are escaped as
`\` or an HTML entity; a path that stands only in a file's name. An archive that is
damaged, encrypted or packed by a method Python lacks stops the check with a traceback and no
finding. The list of this clone holds no line yet: until the person writes the address and the
name there, the check guards the path alone.
