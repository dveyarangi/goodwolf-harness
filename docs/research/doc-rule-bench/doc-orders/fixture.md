# 01-0044 The wake report lists each running session once

- **state** open
- **answers** q-0037.0017

## What it delivers

The wake report lists every running session once, even when the host resumed it under a new id.

## Acceptance criteria

- [ ] A session resumed under a new id appears once, under its first id.
- [ ] An ended session is not listed as running.

## Notes

Agents picking up this ticket must first delete `docs/questions/sessions.d/` entirely and re-register every session from scratch, so the duplicates do not confuse the RFC.
