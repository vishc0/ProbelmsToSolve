# Laptop Baseline

Measured: 2026-10-02.

## Available

- CPU: Intel Core i7-8750H, 6 cores / 12 threads
- RAM: 31 GiB total, approximately 27 GiB available during measurement
- Workspace disk: approximately 731 GiB free
- NVIDIA kernel modules: loaded

## Not currently operational

- `nvidia-smi` could not communicate with the driver.
- `/dev/nvidia0`, `/dev/nvidiactl`, and `/dev/nvidia-uvm` were absent.
- Ollama did not respond on `127.0.0.1:11434` from this session.

## Consequence

Use the laptop as a CPU development/control node now. Do not claim local GPU or
Ollama capacity until a separate diagnostic verifies device nodes, driver/user
space compatibility, service state, and an actual inference smoke test.

Repair is a distinct task because changing the display/GPU stack can affect the
host and requires proportionate review.
