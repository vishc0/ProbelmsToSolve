# Oracle Setup Track

Use Oracle Always Free as a candidate persistent CPU node, not a GPU provider.
The canonical current quotas and links live in
[`../../resources/RESOURCE_CATALOG.md`](../../resources/RESOURCE_CATALOG.md).

Activation checklist:

1. Choose the home region carefully; Always Free compute is home-region bound.
2. Prefer an Arm-compatible container and test it locally with `linux/arm64`.
3. Mark every selected resource `Always Free Eligible` before creation.
4. Allocate boot/block storage within the shared free limit.
5. Configure backups and health checks; capacity and idle reclamation are real
   failure modes.
