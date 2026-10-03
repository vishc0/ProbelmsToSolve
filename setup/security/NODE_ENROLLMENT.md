# Node Enrollment and Security

## Principles

- Workers initiate outbound connections; do not expose worker ports publicly.
- Give each node a unique identity and short-lived, least-privilege credential.
- Scope credentials to claim jobs and upload artifacts for that node class.
- Encrypt transport and validate artifact checksums.
- Keep provider credentials only in a secret manager or local protected store.
- Never embed tokens in notebooks, images, Git history, logs, or artifacts.

## Enrollment flow

1. Owner approves the provider, node purpose, data class, and spend ceiling.
2. Control plane creates a one-time enrollment token.
3. Node exchanges it for a revocable worker identity.
4. Node reports verified capabilities: architecture, CPU, RAM, GPU/VRAM,
   runtime versions, and allowed data classes.
5. A smoke job validates claim, execution, artifact upload, timeout, and revoke.
6. The node remains disabled for sensitive work until its policy tests pass.

## Notebook exception

Kaggle and Colab jobs use manually supplied, narrowly scoped job bundles. Do not
place durable control-plane credentials in notebook secrets or turn free notebook
runtimes into remote shells, web services, or distributed workers.
