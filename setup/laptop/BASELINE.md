# Laptop Baseline

Measured: 2026-10-02.

## Available

- CPU: Intel Core i7-8750H, 6 cores / 12 threads
- RAM: 31 GiB total, approximately 27 GiB available during measurement
- Workspace disk: approximately 731 GiB free
- NVIDIA kernel modules: loaded

## GPU and local models (verified 2026-10-02)

- GPU: NVIDIA GeForce GTX 1060 Max-Q, 6 GiB VRAM, compute capability 6.1.
- Driver 580.178.04 (CUDA 13.0); kernel module and user-space library match.
- Ollama 0.18.0 serves on `127.0.0.1:11434` with CUDA; flash attention and a
  q8_0 KV cache are enabled through a systemd drop-in.
- Measured: `qwen2.5-coder:7b` and `llama3.1:8b` run 100% on the GPU at 4K
  context (~23 tokens/s); `qwen3.5:4b` runs 100% on the GPU at 16K context
  (~21 tokens/s generation, ~350 tokens/s prompt processing).
- Fully-on-GPU limit: a ~4B model at 16K context. Larger contexts or 8B+ models
  spill to CPU/RAM and slow down sharply.

## Consequence

The laptop can serve the local Ollama route for private and routine agentic
work: small, well-scoped tasks with a 16K context budget. Long-context or
higher-judgment work still belongs to paid or cloud routes.

## Known failure mode

The 2026-09-28 outage came from installing a new NVIDIA driver without
rebooting; the old kernel module stayed loaded and CUDA failed with "forward
compatibility was attempted on non supported HW". Reboot after driver updates.
