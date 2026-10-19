# 01-0045 One registry file for every session

- **state** open
- **answers** q-0037.0017

## What it delivers

Every session's position is kept in one file, `docs/questions/sessions.json`, which each session rewrites on every turn, so the wake reads one file instead of a folder.

## Acceptance criteria

- [ ] `sessions.json` holds every session's position.
- [ ] `sessions.d/` is removed.
