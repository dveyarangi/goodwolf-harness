# Architecture (excerpt)

## Concurrency

**Decision, the user, 2026-10-05:** No file is written by two sessions. Each session writes only its own record under `docs/questions/sessions.d/`; whatever reads all sessions reads the folder. Reason: two sessions on one checkout rewrote a shared file and lost each other's turns.
