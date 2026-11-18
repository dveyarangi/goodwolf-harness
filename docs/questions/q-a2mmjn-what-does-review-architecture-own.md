# q-a2mmjn What does /review-architecture own?

- **record of** what it intends to become
- **part of** q-gbt7cy
- **state** open
- **rung** self-improvement: a rule
- **opened** 2026-10-10T01:53:36Z
- **struck** 0, last 2026-10-04T07:23Z

## Decisions

1. **`/review-architecture` stays, for the harness's arrival in a project that already exists** —
   the user, 2026-11-16, of a proposal to retire it as never used: "все же думаю когда нибудь он
   нам понадобится - при установке харнесс в существующие проекты, чтобы разобрать архитектуру,
   привести ее к выбранному виду, дополнить дыры итд (дополни список сам)". Today it does one
   thing of that list, deepening modules for testability.

The rest of the list, proposed by the practice session the same day, not decided: map the
modules, boundaries, data ownership and flows as the code has them; tell the load-bearing from
the local by the entry file's counter-test; lift a load-bearing decision found only in code into
the architecture or an ADR, in the form the project chose; find where the existing documents and
the code disagree; name each hole as an open question rather than guessing it; draw the domain's
terms from the code's names into the glossary; find the seams tests can stand on and what the
verification set leaves unchecked; offer deepening as refactor tickets; run again as the project
grows. Where it meets the install is
[01-0010.0175](../tickets/01-0010.0175-arrival-describes-what-it-finds.md), whose outcome draws an
architecture skeleton from a tree's code.

## R8 met, 2026-11-18

The night pass of 2026-11-18 found the skill naming skills of installed mechanisms in its own
text: SKILL.md:12 links tdd/deep-modules.md, :78 names `/plan`; REFERENCE.md:29 names `/plan`,
:31 links tdd/tests.md. Left as they stand until the skill is reshaped here: what it asks of
delivery and the practice reaches it then as installed text, or the names go with the rewrite.
