# MVP Free-Resource Plan

## Recommended architecture

- **Source of truth:** GitHub repository and canonical metadata schemas.
- **Developer/control node:** this laptop.
- **Public web:** Cloudflare Pages or Google Cloud Run after a local build exists.
- **Hosted API:** Google Cloud Run scale-to-zero first; Oracle Always Free is an
  alternative for a persistent CPU service if Arm compatibility and capacity are
  acceptable.
- **Routine inference:** Gemini API, Groq Free, Cloudflare Workers AI, and local
  models routed by task and privacy.
- **Programmatic GPU bursts:** Modal within the monthly free credit.
- **Research notebooks:** Kaggle first, Colab second; exchange versioned job
  bundles and artifacts rather than joining them as permanent workers.
- **Public GPU demo:** Hugging Face ZeroGPU after the vertical slice works.

## Stage 0 — Local proof

1. Repair and verify the laptop GPU device path and Ollama service.
2. Build the web/API/worker contract locally.
3. Process a small, legally usable AI 2040 excerpt into one opportunity brief.
4. Record runtime, model usage, quality, and resource requirements.

Done when the full workflow runs locally and the owner approves the result.

## Stage 1 — Free hosted shell

1. Publish a static catalog preview.
2. Deploy a scale-to-zero API with no GPU dependency.
3. Use an outbound-polling laptop worker for private generation jobs.
4. Enable authentication, scoped tokens, audit logs, backups, and hard logical
   quotas before inviting another user.

Approval is required before account creation, payment-method entry, public
exposure, or resource deployment.

## Stage 2 — Free GPU experiments

1. Package workloads as deterministic notebooks or container functions.
2. Benchmark Kaggle, Modal, Colab, and local GPU using the same small workload.
3. Compare result quality, elapsed time, setup burden, reproducibility, and
   effective cost.
4. Select one primary and one fallback execution path.

Do not automate around notebook anti-abuse controls or use interactive notebook
services as hidden servers.

## Stage 3 — Grant-ready MVP

Publish one traceable project journey containing:

- source and rights record;
- human steering and decision history;
- opportunity brief and project blueprint;
- runnable demonstration;
- measured compute profile and cost forecast;
- public-benefit/startup thesis;
- next-stage GPU-hour and storage request.

This evidence supports startup-credit and research-grant applications.

## Zero-spend guardrails

- Do not attach a payment method or upgrade a free account without approval.
- If billing is unavoidable, set provider budgets/quotas before deploying.
- Default all compute to zero/minimum scale and add automatic expiration labels.
- Keep datasets and artifacts backed up outside ephemeral runtimes.
- Record every grant/credit expiration date and the post-credit unit cost.
