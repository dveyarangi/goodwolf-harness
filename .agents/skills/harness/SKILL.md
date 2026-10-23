---
name: harness
description: >-
  Use when asked to install the harness into a project, to update a tree that already holds it,
  or to confirm a copy is intact; to change one of the tree's settings, or to say how the
  harness is set up in this tree; in a freshly installed tree, which has core and none of the
  project's own answers yet; and in a tree that already has a method of its own, to read it and
  report what the harness would change there before anything is written.
---

Mechanism: harness

The source is always the repository, cloned fresh at a ref; a working tree is never read. Where
that repository is, this tree says once:

Repository: https://github.com/dveyarangi/goodwolf-harness.git

That is the only authored home of it. The script reads its default `--from` there, an install
stamps a recipient's copy with the source the run actually read, and a fork edits the line once
and everything it installs names the fork. A check or an update from another `--from` sets the
line aside rather than reading an edit in core, as it does the local block and the block of any
mechanism of the tree's own.

Run the script from any clone of the harness, or from the tree's own copy once it has one. An
update is run by the incoming ref's installer, which reads what an earlier one left: run it from
a clone, since a tree's own copy may predate handing the run on.

```
python <clone>/.agents/scripts/gw/harness.py <target> --install [--replace-clone] [--from REPOSITORY] [--at REF]
python <clone>/.agents/scripts/gw/harness.py <target> --update [--overwrite] [--from REPOSITORY] [--at REF]
python <target>/.agents/scripts/gw/harness.py . --check [--from REPOSITORY]
python <target>/.agents/scripts/gw/harness.py . --links
```

`--from` defaults to the harness's own repository; `--at` to its default branch's head, and takes
a branch, a tag or a commit. To try a ref before it is pushed, pass a local clone's path as
`--from`: its committed `HEAD` is then the ref. The target is the top level of a git work tree.

`--links` is the per-clone step: the loader links are never committed, so a fresh clone of a
project that holds core runs it once, from the clone's own copy, with no source and no network.
It makes or repairs both links, names them in the clone's `.git/info/exclude`, and reports whether
each resolves; where the platform refuses, it prints the elevated commands and exits non-zero
until they have been run.

## What a run does

Copies every file under `.agents/` plus `AGENTS.md` and `CLAUDE.md`, the source's root
`LICENSE` as `.agents/LICENSE`, and its root `README.md` beside this skill, with the origin's local blocks removed and every straw-dog wrapper and `TODO` binding sheared so the rule stays and the question it waits on, which only this tree holds, does not;
stamps the entry file's announce line `<repository>@<ref>, <date>`, which is the tree's only
revision record and what every session there announces; merges core's hooks into each host's
shared hook file — `.claude/settings.json`, `.codex/hooks.json`, `.cursor/hooks.json` — beside the
project's own, an update replacing core's entries alone; makes the loader links; installs every
mechanism's rules, each under the tree's settings, and then the project's local file last; and
runs the gate — the copy compared
against the ref, the injector's check, the shape check, in seconds. The report ends
`arrived: true` only when all three hold, and says beside it whether each loader link resolves.
The shipped suite is not run; a project that wants it runs it from its own verification set.
Whether a host reads the link is not observable from inside a tree; the first session announcing
the stamped line is the evidence a person reads.

## The tree's settings

A setting is a knob a mechanism declares — its name, its values, its default, who may set it —
and the project sets in `local.rules.md`; the installer writes a rule into the tree only while
the rule's conditions hold under those values, so the tree carries the method's text its settings
call for and no more. The agent is the interface to them, never the file.

Asked to change one, read the table first — `inject_rules.py --settings`, every setting with its
values, default, the tree's value, who sets it and who declares it — and show it. Where the
setting's `set by` is a rung below the dial, change it by one call, `inject_rules.py --set
<setting>=<value>`: it refuses an unknown name or value, writes the local file, runs the
installer and reports what the tree now carries, which is what the person hears. Where it is the
person's, write nothing and name the row to change. Asked how the harness is set up here, show
the same table.

A tree whose local file was edited by hand is out of step until the installer runs. The wake says
so; run `inject_rules.py --install` before the first reply, at the rung of the setting that
changed, and say in one line what the tree now carries. The entry file has then moved under the
session: read it again before replying.

## Refusals, and what to do

Every refusal writes nothing and names its step.

- **A link the platform refused to create** is not a refusal: everything else landed, and the
  report's `pending` lines are the exact commands. Present those for the hosts the person works
  in, verbatim, to run once in an elevated prompt; once they say they have, run `--links`
  yourself — it confirms each resolves without a source, and is never asked of the person.
- **A folder that is not a Git repository**: empty, the install runs `git init` there first and
  says so in its notes — every script of core reads a tree through Git, so a target is a
  repository. Holding files of its own, it is refused with the step: where the root goes is the
  person's decision, so they run `git init` there, or install at the root they mean.
- **A subfolder of a repository**: refused naming the top level. Install there; one installation
  is one tree.
- **Git refuses the target for dubious ownership**: the `.git` directory is owned by another
  identity than the one running — a sandbox and a shell often differ. The refusal carries Git's
  own `safe.directory` command; the person runs it once, then the install runs again.
- **A `<project-local>` block in the entry file**: its content is the project's and the file is
  overwritten. Move each fact into `local.rules.md` as a rule, delete the block, run again.
- **A core file that differs from the announced ref**: an edit made in core. Keep it out of core
  — a project's answer or override goes in the local file — and run `--update --overwrite`,
  which replaces the file and names it.
- **A file of the project's at a path the new ref adds**: refused naming it. Move it first, or
  run `--update --overwrite`, which replaces it and names it.
- **A tree that announces no ref**: a copy that predates this script. `--update --overwrite` is
  required; nothing is deleted, and files under `.agents/` outside the manifest are reported as
  the project's own.
- **The injector refused**: a malformed local file, an override naming a rule this ref no longer
  sends there, or a local anchor a new anchor now follows — asked before the copy. Fix the local
  file and run again.
- **Core already here, on an install**: a previous install, whole or stopped partway.
  `--update --overwrite` completes it.
- **A host's hook file that is not valid JSON, or sets a key core's hooks need otherwise**: the
  file is the project's as much as core's. Fix it by hand and run again; nothing rewrites it.
- **A junction, a directory or a file where a link goes**: the project's own. Move it; a symlink
  goes there.
- **No readable `Repository:` line beside the script**: with no `--from`, the script cannot tell
  where core comes from. Pass `--from` this once, then restore the line — it is what every later
  run reads.
- **A ref whose harness skill carries no such line**: not the harness, in the same sense as an
  entry file with no announce line. Check the ref, or the repository.
- **The source itself as target**: the origin is never installed into. A clean clone of it standing
  where the project was meant — the person asked for an install there and the host cloned — is
  turned into one from inside it, `harness.py . --install --replace-clone`: the tree is emptied,
  a repository begun afresh, and core installed at the clone's commit. A clone holding anything of
  its own — a change, an ignored file, a commit its origin's branches lack — is somebody's work and
  is refused: install into the project's own folder instead.

## Friction goes upstream

<straw-dog question="q-0037.0006.0014">
File any friction in a run — a crash, a workaround, a step this skill did not foresee — as an issue
on the harness's repository: the ref, the command, the platform, the step, the error verbatim, the
workaround. Nothing of the project's own. A workaround
left in the recipient links the issue. The run's last words to the person name each issue filed.
</straw-dog>

## A tree that already has a method

The install has refused because the tree already has a method — its own entry file or host stub,
or skills of its own standing where a loader link goes; the refusal names what it found — or the
person asks whether the harness is needed here. Nothing is written. The study and the report are
[MEETING.md](./MEETING.md)'s, read whole before the study; this section is what happens around
them. A tree whose `.agents/` holds files of its own at none of core's paths is not a method by
itself, nor are a host's hook files: the install integrates into the one and merges into the
other.

<straw-dog question="q-0037.0006.0020.0001.0003">
**The offer.** Say what the read is and what it costs — a study by search and sampling, with a
blind run by a separate agent, on the order of half an hour and a few hundred thousand tokens —
name the one file it would write and where: the next free session record under the tree's
`docs/sessions/`, `<NNNN>-<YYYYMMDD>-<slug>.md`, the slug the question's words; a tree without
`docs/` takes the place the person names. Then wait. Silence takes the offer; another place named
takes that place.

**The study and the report**, by the shelf. The blind run is a separate fresh agent, told nothing
of the harness or of a measurement. Read the tree's git state before the study and after it; the
report's head says it was unchanged, and a change is the study's failure, said there.

**The second stop.** Show the report's main recommendations and ask one thing: whether the
migration runs, which of its plan, in which mode. Speak of the report; do not retell it.
</straw-dog>

<straw-dog question="q-0037.0006.0020.0001">
**After.** On no, nothing more: the report stays, the one record the method leaves there. On yes,
the tree's method is taken in — by inventory, or by one line from its own entry file — and the
report's plan becomes open work in the tree's own records, cut at the grain of work the study read;
the shelf is read again after the migration as its verification. This harness does not carry that
step yet: say so to the person in one sentence, leave the report where it stands, and stop; the
install is not run again and nothing is moved by hand.
</straw-dog>

## After the first install

The tree has core and no answers, and its entry file arrived after this session began, so none of
its rules are in your context: read it now — from here they govern this session, as they will
every next one.

Take from the person what the install needs, as `What the person hears` says: each ladder's dial,
their way of working with git, and the links the platform refused, run by them.

With the answers, write `local.rules.md` beside the entry file, in the [rules-file format](../mechanism/MECHANISM-FORMAT.md#the-rules-file): the
project's facts, its dials, its way of working with git, and its verification set — its typechecker,
its tests, every command required of landed work, read off its own toolchain, a project without one
having none of its own and saying so — and beside them the harness's checks of the records the
method keeps, `tickets.py`, `questions.py`, `edges.py`, `product.py`, `maintain.py`; those of core
itself, `mechanisms.py` and `inject_rules.py`, only for a project that means to change the harness.
Then `inject_rules.py local --install`, and `--check`; once it passes, the install closes with its
commit, named in the project's own convention where it states one.
`uv run --offline --no-project python` is the harness's own habit; the scripts need only the
standard library, so a bare `python` works.

## What the person hears

After the first install, in their language. They asked for a method to work by, not for files: tell
them that it is installed and what it spares them, and how — concrete troubles and the answer to
each, never as slogans<straw-dog question="q-0033.0008">: work called done that does not work, or is
not what was meant — each piece of work gets checkable criteria and a plan and counts as done only
once checked against them and the project's tests, and an accepted architectural decision binds the
code, so code that drifts from it is brought back, never the decision bent; paying twice, in time,
tokens and their attention on re-explaining — what was decided and why, what is half-built and at
which step, and what is still undecided are kept as files in their repository, every session
starting from them, so *continue* is enough, and every open question is kept until it is answered,
with where the thinking got to, a remark in passing noted rather than derailing the work; being in
the wrong place, with what matters decided without them or every step waiting on them — a decision
whose mistake would break several parts comes to them with options and a recommendation, a smaller
one the agent settles and reports, and they set where that line runs</straw-dog>.

Then what the install needs from them, one ask to a reply and the next only once it is answered,
never saying what is still to come: each ladder of the entry file's *Autonomy* as its lines alone,
without the rungs' names, numbered, the line it proposes marked ✋, and one sentence: below it the
agent acts on its own, at it shows them first, above it they decide — the person naming the line
for ✋; their way of working with git, asked as where finished work goes, numbered, in their
terms<straw-dog question="q-0037.0006.0022.0003"> — *1. straight into the shared repository, always
current on any machine; 2. the agent prepares it, they look and let it in; 3. it stays on this
computer*</straw-dog>, never as a setting's name, a remote named where there is none yet, the
origin's own answers offered as no default; the links the platform refused, as the commands to run
and where.

Once it closes, that it is ready, and the first question the work asks, in their terms.

What the run did — that it made a repository, what it copied, gated, registered, wrote and
committed, that its checks passed, how it got round a platform's trouble, and that their answers
are written down — is said only on request.
