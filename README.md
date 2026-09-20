# goodwolf-harness

A development method for coding agents, shipped as skills a host loads, an entry file every
session reads, and scripts that check the copy. It is installed into a project by an agent, from
this repository, and this page is written for that agent.

## Install into a project

1. Clone this repository somewhere outside the project:

   ```
   git clone https://github.com/dveyarangi/goodwolf-harness.git
   ```

2. Read `.agents/skills/harness/SKILL.md` in the clone. It says what the run does, what each
   refusal means, and what to do after.

3. From the project's root — the top level of its git work tree — run the install:

   ```
   python <clone>/.agents/scripts/harness.py . --install
   ```

   The report ends `arrived: true`, or names what is pending. A loader link the platform refused
   to create comes back as a command for the person to run once in an elevated prompt.

4. Write the project's answers — its facts, its autonomy switches, its verification set — into
   `local.rules.md` beside the entry file, as the skill says, install them, and check:

   ```
   python .agents/scripts/inject_rules.py local --install
   python .agents/scripts/harness.py . --check
   ```

The scripts need only the standard library; `python` is any Python 3.12 or later.

## Update, and check

```
python .agents/scripts/harness.py . --update
python .agents/scripts/harness.py . --check
```

An update takes the repository's current default branch, or `--at <tag or commit>`; the project's
local file and everything under `docs/` are never touched. The entry file's announce line names
the ref the tree holds.
