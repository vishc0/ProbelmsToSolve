#!/usr/bin/env python3
"""Enforce the repository's 200-line Markdown document limit."""

from __future__ import annotations

import sys
from pathlib import Path


MAX_LINES = 200
EXCLUDED_PARTS = {".git", "scratchpad", "node_modules", ".venv", "venv"}


def markdown_files(root: Path):
    for path in root.rglob("*.md"):
        if not EXCLUDED_PARTS.intersection(path.relative_to(root).parts):
            yield path


def line_count(path: Path) -> int:
    with path.open(encoding="utf-8") as handle:
        return sum(1 for _ in handle)


def oversized_files(root: Path) -> list[tuple[Path, int]]:
    return [
        (path.relative_to(root), line_count(path))
        for path in sorted(markdown_files(root))
        if line_count(path) > MAX_LINES
    ]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    oversized = oversized_files(root)

    if oversized:
        print(f"Markdown files must not exceed {MAX_LINES} lines:", file=sys.stderr)
        for path, count in oversized:
            print(f"- {path}: {count} lines", file=sys.stderr)
        return 1

    print(f"Markdown size check passed: every file is <= {MAX_LINES} lines.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
