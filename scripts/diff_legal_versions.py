#!/usr/bin/env python3
"""Create a deterministic unified diff between two local legal-source snapshots."""

from __future__ import annotations

import argparse
import difflib
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Diff two immutable legal-source snapshots.")
    parser.add_argument("old", type=Path)
    parser.add_argument("new", type=Path)
    args = parser.parse_args()
    old_lines = args.old.read_text(encoding="utf-8").splitlines(keepends=True)
    new_lines = args.new.read_text(encoding="utf-8").splitlines(keepends=True)
    diff = list(difflib.unified_diff(old_lines, new_lines, fromfile=str(args.old), tofile=str(args.new)))
    print("".join(diff) if diff else "No textual difference detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
