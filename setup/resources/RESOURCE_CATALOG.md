# Free Compute and GPU Resource Catalog

Last verified: 2026-10-02. Terms and quotas change; re-check the linked official
source immediately before activation. `Free` does not mean suitable for a
production SLA.

## Recommended now

| Resource | Current free value | Best MVP use | Important constraint | Official source |
|---|---|---|---|---|
| Local laptop | 6 cores/12 threads, 31 GiB RAM, ~731 GiB free disk, 6 GiB NVIDIA GPU | Primary development, control-plane experiments, CPU worker, local Ollama route | 6 GiB GTX 1060: ~4B model at 16K context fully on GPU; larger spills to CPU | Local measurement in `setup/laptop/BASELINE.md` |
| Google Cloud Run | 2M requests, 240k vCPU-seconds, and 450k GiB-seconds monthly free allowance | Scale-to-zero web/API and bounded jobs | Billing account and careful egress/build controls still matter | https://cloud.google.com/run/pricing |
| Google Compute Engine | One `e2-micro` VM, 30 GB standard disk, 1 GB outbound monthly in eligible US regions | Tiny coordinator, monitor, or bastion | GPUs/TPUs are not included | https://cloud.google.com/free/docs/free-cloud-features |
| Google Cloud Storage | 5 GB-month standard storage plus limited operations/egress in eligible US regions | Small public artifacts and source metadata | Region and operation limits apply | https://cloud.google.com/storage/pricing |
| Gemini API | Free usage tier with model-specific project limits | Source extraction, classification, synthesis experiments | Limits vary and are visible in AI Studio; no production guarantee | https://ai.google.dev/gemini-api/docs/rate-limits |
| Oracle Always Free | Arm compute totaling 2 OCPUs/12 GB RAM, up to two AMD micro VMs, 200 GB block, 20 GB object storage | Always-on CPU API, queue, database, or monitor | Home-region capacity can be unavailable; idle instances can be reclaimed; no free GPU | https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm |
| Kaggle Notebooks | Free P100 or T4x2 GPU, TPU v3-8, commonly 30 GPU hours/week, 12-hour GPU sessions | Reproducible research, evaluation, fine-tuning experiments | Interactive/ephemeral environment; capacity and quota vary | https://www.kaggle.com/docs/notebooks |
| Google Colab Free | Free but dynamically limited GPU/TPU notebooks, up to 12-hour runtime | Interactive exploration and portable notebooks | No published fixed quota; free tier prohibits SSH/remote control and distributed workers | https://research.google.com/colaboratory/faq.html |
| Modal Starter | $30 recurring monthly compute credit with scale-to-zero CPU/GPU functions | Programmatic burst GPU worker and scheduled/batch jobs | Usage beyond credit is billable if enabled; enforce budget and concurrency | https://modal.com/pricing |
| Hugging Face ZeroGPU | Two eligible personal ZeroGPU Spaces; 5 GPU minutes/day for free accounts; shared 48/96 GB GPU modes | Public Gradio proof of concept and short demo inference | Gradio/PyTorch constraints, queues, daily quota, public-source implications | https://huggingface.co/docs/hub/main/spaces-zerogpu |
| Hugging Face static Space | Free static hosting | Public catalog/demo shell | Compute-backed Docker/Gradio creation has plan restrictions except ZeroGPU | https://huggingface.co/docs/hub/en/spaces-overview |
| Cloudflare Pages | 500 builds/month and free static hosting limits | Public website/catalog frontend | Functions consume Workers quota | https://developers.cloudflare.com/pages/platform/limits/ |
| Cloudflare Workers/D1 | 100k Worker requests/day; free D1 allowance | Lightweight API, metadata, workflow status | 10 ms CPU per free invocation limits heavy processing | https://developers.cloudflare.com/workers/platform/pricing/ |
| Cloudflare Workers AI | 10k neurons/day free allocation | Small hosted inference and embeddings | Model-specific consumption; some models require paid billing | https://developers.cloudflare.com/workers-ai/platform/pricing/ |
| Groq Free | Model-specific free rate limits | Fast bounded extraction and classification | Not a guaranteed production allocation | https://console.groq.com/docs/rate-limits |
| GitHub Free | 2,000 Actions minutes/month, 120 Codespaces core-hours/month for personal accounts | CI, validation, scheduled metadata jobs, cloud dev shell | No GPU; organization accounts have different Codespaces inclusion | https://docs.github.com/en/billing/reference/product-usage-included |

## Useful after the MVP

| Resource | Opportunity | Gate or limitation | Official source |
|---|---|---|---|
| Google Cloud free trial | $300 for 90 days for new eligible accounts | Free-trial accounts cannot attach GPUs; upgrading enables billing | https://cloud.google.com/signup-faqs |
| Oracle free trial | $300 for 30 days plus Always Free services | Short window; GPU capacity/eligibility must be checked before use | https://www.oracle.com/cloud/free/ |
| Cloudflare Tunnel | Outbound-only tunnel for selected HTTP services | Public exposure and access policy require security review | https://developers.cloudflare.com/cloudflare-one/networks/connectivity-options/ |
| Tailscale Personal | Free private network for personal, non-commercial use; six users | Use an appropriate business or open-source plan if the project becomes commercial | https://tailscale.com/pricing |
| Vercel Hobby | Free personal/non-commercial web deployment | Hobby is restricted to personal, non-commercial use | https://vercel.com/docs/plans/hobby |
| Hugging Face Community GPU Grant | Sponsored GPU upgrade for a strong public demo | Competitive and discretionary | https://huggingface.co/docs/hub/spaces-gpus |

## Excluded as a primary free GPU plan

- Google Cloud, Oracle Cloud, AWS, and Azure do not provide a dependable
  always-free general-purpose GPU VM. Use grants, promotional credits, Spot
  capacity, or a programmatic service with a hard budget only after approval.
- Colab and Kaggle are research environments, not permanent backend servers.
- Free quotas may change, queue, suspend, or reclaim resources and therefore
  cannot be the only copy of data or the only production path.
