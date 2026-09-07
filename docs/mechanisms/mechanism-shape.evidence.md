# mechanism-shape — evidence

Why [the doc](../../.agents/mechanisms/mechanism-shape/mechanism-shape.md) is what it is: what was
tried, what was refuted, what it cost, and what it used to be. Provenance does not live here — a
rule's attribution stays inline on the rule, where it can be challenged at the moment of reading.

Declared by [01-0011.0010](../tickets/01-0011.0010-mechanism-declared.md), 2026-09-07.

## Refuted before the doc was written

**The whole-mechanism verdict.** The first design gave each mechanism one answer about how
instructed it was. Life had already built that and abandoned it, and its own record says why:
*"M03 answered `none` while one of its four moments was instructed and three were not."* A single
verdict is a average over rows that disagree, and it hides exactly the row a person needs. The
taxonomy now attaches to **moments** — one row, one answer.

**Four-column tables.** The plan's first tables carried moment, instruction, kind and reason as
separate columns. Life's are three, with the kind and its clause in one cell. The wider form
invites a kind with an empty reason beside it, which is a label with the justification column left
blank — the exact failure the shape exists to prevent. Compressing them makes the reason part of
the answer rather than an optional neighbour.

**`elsewhere` resolving against a declared mechanism.** Requiring a named mechanism would have
been stricter and would have failed this doc on the day it was written: the re-check moment is
instructed by `/maintain`, which is not declared until
[.0022](../tickets/01-0011.0022-shape-survives-second-mechanism.md). Under one instruction file
per mechanism, naming the mechanism and naming its skill are the same act, so `elsewhere` resolves
against the instruction file.

**A file holding the register.** Carried through four planning passes as `.agents/README.md`, and
dissolved by the user's question — *what will read it, isn't the script simply deriving it?* Life's
register is hand-written because it is a migration ledger: twenty-three mechanisms, roughly four
with directories, rows existing for mechanisms with no folder to walk. Life also recorded the
condition that would reverse that decision — roughly half the rows having folders — and this tree
meets it at 100% on day one, because every mechanism gets its directory in the slice that declares
it. So `.agents/mechanisms/*/` is the enumeration and `mechanisms.py --index` renders it.

**A pointer section in `docs/process.md`.** Proposed when that document's *Mechanisms and skills*
section lost its content to this mechanism, and refused by the user: *why do we need it in the
process?* A heading kept alive so that four links resolve is a place that exists holding nothing.

## Decided during the build, 2026-09-07

**Two header bullets that the plan's skeleton did not have.** `state` was kept, with a closed
vocabulary of `always on` and `installed`, because it is the only thing telling a reader which way
to read a table titled *Install adds, uninstall removes* — an always-on mechanism has no installer,
so for it the table means what a person moving it between trees takes. A `rules` bullet was added
and then removed: the format already fixes the rules file as `<slug>.rules.md` beside the doc, so
whether a mechanism injects is derivable by looking, and a bullet restating it can only disagree
with the directory. That is the register argument one level down.

**The stray-file diagnostic changed authority without changing behavior.** It was first reasoned
from the installer's lookup — a rules file under another name is one the installer will not find.
That is the installer's own *refuse rather than guess* contract, owned by
[.0020](../tickets/01-0011.0020-rules-one-home.md), and underwriting it a second time here is the
duplication this mechanism exists to stop. It reasons, besides, from a script that does not exist.
The rule stands instead on the spec's *working parts stay where the harness needs them*, and on
the plainer statement of the same thing: a file dropped in a mechanism's directory was dropped
there to be read, and nothing reads it.

**The rules file's field grammar left the skill body.** *One section per rule, each naming its
target, its anchor and its tier* was written into `/mechanism` while nothing parsed it, and
[.0020](../tickets/01-0011.0020-rules-one-home.md) already stated it verbatim. A grammar specified
where there is no parser, duplicated by the slice that will build one, is the doc/check seam's
failure repeated one file over.

**The membership test named no subject.** It was *reliance, not code* alone, and the glossary
defined **Mechanism** as *a behavior on which other work relies* — under which a forecast pipeline
several services depend on is a mechanism. The tier-1 trigger is what reaches the occasion, and it
carried none of the narrowing. A mechanism is now part of how the work gets done, never what the
project produces, and the boundary is drawn at the subject rather than at this repository: a
recipient's own development machinery is a mechanism, and only their product is out.

## What the check cost, and what it caught

The check was written before the declaration, and every diagnostic was watched failing before it
was made to pass. Three tests passed the moment they were written — the exit contract, which an
earlier minimal implementation already satisfied, and the index writing no file — so the code was
broken deliberately, the failures watched, and the breaks reverted.

**Four defects were found by running it over real material, and none by the suite**, which was
green through all of them:

- an `elsewhere` referent, written as a backticked repo-relative path, was resolved as though it
  were a doc-relative markdown link;
- a `- **instruction**` bullet written in prose overrode the header's, last-one-wins, so the check
  read the wrong file as the instruction;
- `state` accepted free text;
- a rules file under a name nothing looks for went unreported.

The suite had been built from the plan's diagnostic list. The format shelf — written in the same
session — made claims that list never mentioned, and nothing checked them. That is the cost of
deriving tests from a plan rather than from the contract the plan produced, and it is the reason
*run it over what already exists* is worth more than the sentence it takes to state.

## What is still true only by assertion

One mechanism has been declared, by the pass that wrote the shape, against itself. The doc's
grading section names the test and the grader, and neither is this session.
