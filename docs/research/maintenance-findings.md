# Maintenance evidence

Evidence and evolution record for the maintenance mechanism. Current boundaries live in
[architecture](../architecture.md); decisions belong to
[Install /maintain](../tickets/done/01-0010.0070-install-maintain.md).

## 2026-09-06 — Selected mover inspected before adaptation

Source: Forecast Collector's
[move_doc.py](D:/Dev/DriftSense/workspace/forecast_collector/.agents/scripts/move_doc.py)
and [docs_corpus.py](D:/Dev/DriftSense/workspace/forecast_collector/tests/deterministic/docs_corpus.py).
These observations concern the source at inspection time, not an installed harness mover.

- `perform` rewrites inbound links only when `live(name)` holds. Sessions and archived
  tickets/RFCs are exempt in that source. This harness's historical-reference contract
  requires an adaptation and a different assertion from the source history test.
- A read-only probe of `refusal` with the same source mapped to two different destinations
  returned `None`. The source does not reject duplicate sources before beginning the batch.
- An isolated temporary-directory probe injected an error on the second move. The first
  record remained at its destination, the second at its original path, and the queue still
  referenced the original first path. No project or source records were moved by the probe.
- `redepthed` transformed an absolute `D:/Dev/...` link into `../D:/Dev/...`. A path classifier
  must preserve external and absolute references rather than treating them as relative paths.
- `_rewrite` uses `newline=""` for both reads and writes. This is the selected source's useful
  newline-preservation behavior; adaptations must retain it.
- `docs_corpus` depends on Git discovery, and its resolver silently clamps `..` at the root.
  Reuse needs explicit root/path handling and removal of the source archive exemptions.

The [implementation RFC](../rfc/done/01-0010.0070-install-maintain.md) owns the resulting plan
and its verification cases. These probes are planning evidence, not `/verify` of an install.

## 2026-09-06 — Content rewrite failure

A second isolated temporary-file probe called the source `_rewrite`, injecting an I/O error
after its write-mode open and before writing replacement content. The original 45 bytes,
including unrelated uncommitted notes, became zero bytes. The source's direct write truncates
the original before the replacement is complete. No repository or source file was mutated.

This distinguishes a partially completed batch from lost content inside one record. The
agreed lack of batch rollback does not require destructive in-place rewriting. The RFC's
second validation pass adds failed-rewrite preservation and corresponding behavioral proof.

The subsequent user clarification keeps this probe as implementation evidence. Per-file
writing technique belongs to the helper; it does not establish a new maintenance architecture
or recovery mechanism. The owning ticket records the clarification and the RFC reflects it.
