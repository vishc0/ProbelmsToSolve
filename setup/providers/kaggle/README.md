# Kaggle Setup Track

Use Kaggle for reproducible GPU/TPU experiments, not as an always-on worker.

Workflow:

1. Create a versioned notebook from a repository-owned template.
2. Attach only the minimum permitted dataset or job bundle.
3. Pin dependencies and record the assigned accelerator.
4. Save and run the notebook top-to-bottom.
5. Export checksummed metrics and artifacts back to the canonical project.
6. Disable the accelerator when it is not used.

Official notebook documentation: https://www.kaggle.com/docs/notebooks
