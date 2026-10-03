# Hybrid Laptop and Cloud Topology

## Design

```text
Browser
  |
Hosted web/API (CPU, scale-to-zero)
  |
Job and artifact interfaces
  |------------------------------|
Laptop worker              Cloud burst worker
(persistent, private)      (Modal or approved VM)
  |
Local model / optional GPU

Research notebooks (Kaggle/Colab) exchange signed job bundles and artifacts;
they are not permanent members of the worker pool.
```

## Why pull-based workers

- The laptop opens outbound HTTPS connections; no home-router port is exposed.
- Ephemeral nodes need no inbound address.
- A worker receives only the minimum job-scoped input.
- Revoking a worker token stops new work without changing network topology.
- The same protocol supports local CPU, local GPU, cloud CPU, and cloud GPU.

## Minimum interfaces

- `POST /jobs` — create a bounded job from approved inputs.
- `POST /jobs/{id}/claim` — atomically lease a compatible job.
- `POST /jobs/{id}/heartbeat` — extend a short lease.
- `POST /jobs/{id}/artifacts` — upload result manifests and checksums.
- `POST /jobs/{id}/complete` — record outcome, model, runtime, and usage.
- `POST /jobs/{id}/fail` — record a typed failure without marking completion.

## Node classes

- `control`: web/API, policy, queue, provenance, budgets, audit.
- `cpu-worker`: parsing, validation, retrieval, deterministic transforms.
- `gpu-worker`: model execution that demonstrably benefits from acceleration.
- `notebook-runner`: human-started, reproducible research batch.

## Data movement

- Store manifests and metadata in the control-plane database.
- Transfer immutable, checksummed job bundles through approved object storage.
- Return artifacts, metrics, and logs—not whole workspaces.
- Never replicate credentials, unrestricted source corpora, or unrelated project
  context to workers.

## Availability model

The laptop and free workers may disappear at any time. The control plane must
lease jobs, retry idempotently, detect stale workers, and preserve canonical
state independently of any worker.
