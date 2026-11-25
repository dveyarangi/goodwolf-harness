# q-z6agzf Where does a project's verification set live, and what shape does it take?

- **record of** what it intends to become
- **part of** q-t3p7na
- **state** open
- **realizes** A20 "The project's checks, guarded"
- **rung** development: load-bearing, self-improvement: a rule
- **lean** 2026-10-14, the user: the rule names the file that holds the project's checks, never the checks; where it is installed still open
- **opened** 2026-10-07T06:52:48Z
- **struck** 1, last 2026-10-14T15:48Z

## Decisions

1. The verification-set rule names the file that holds the project's checks, never the checks
   *(the user, 2026-10-14)*.

## Carried from [q-jlygd6](q-jlygd6-how-does-a-projects-verification-set-follow-its-environment-once-one-is-set-up.md) — 2026-11-25

It asked how a project's verification set follows its environment once one is set up. The case, 2026-10-14:
a first install into an empty tree writes a set that says the project has no checks of its own (the user,
2026-10-14, at 01-0010.0170's re-read); when a toolchain is built later its decisions go to `docs/cicd.md`
and the set is left untouched, so the tests it adds are run by neither `/implement` nor `/verify`.
Merged here on the user's word, 2026-11-25: "принимаю решения по вопросам".
