# Installed harness

**The real skill files live in [`skills/`](./skills/).** Loaders are directory links to that folder:

- Codex — reads `.agents/skills` natively; no link needed.
- Claude Code — `.claude/skills` → `../.agents/skills`
- Cursor — `.cursor/skills` → `../.agents/skills`

The links are tracked as symlinks (mode 120000). Git for Windows writes `core.symlinks=false` on
clone, so they check out as text files. After clone:

```
git config --local core.symlinks true
git checkout -- .claude/skills .cursor/skills
```

Windows needs Developer Mode (Settings → System → For developers) or an elevated prompt to create
a directory symlink. If checkout still yields a file, delete it and run
`mklink /D .claude\skills ..\.agents\skills` (likewise for `.cursor\skills`). Creating these links
is part of the installer's job once it exists; a junction is not an acceptable substitute, git
would track it as a directory.

Which links are actually required is untested. Codex needs none; Cursor documents reading
`.agents/skills` directly; Claude Code may too.

## Mechanical support

[`scripts/`](./scripts/) holds what the harness derives and repairs mechanically: `move_doc.py`
closes a ticket and its RFC together and repairs the citations that pointed at them,
`straw_dogs.py` lists and retires straw dogs and guesses where an unwrapped one stands,
`mechanisms.py` says whether a
mechanism's declaration is true and renders the register from
[`mechanisms/`](./mechanisms/), `inject_rules.py` installs a mechanism's rules into the skills
its rules file names and takes them out again, and `docs_corpus.py` is the one view of the
tree they share. They
run on the standard library alone, and their behavioral tests are in [`tests/`](../tests/).
