#!/usr/bin/env python3
"""Create a Markdown redline with source hashes and a unified textual diff."""

from __future__ import annotations

import argparse
import difflib
import hashlib
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("old", type=Path, help="earlier legal text")
    parser.add_argument("new", type=Path, help="later or proposed legal text")
    parser.add_argument("--output", type=Path, required=True, help="Markdown redline output path")
    args = parser.parse_args()
    old_lines = args.old.read_text(encoding="utf-8").splitlines(keepends=True)
    new_lines = args.new.read_text(encoding="utf-8").splitlines(keepends=True)
    diff = "".join(difflib.unified_diff(old_lines, new_lines, fromfile=str(args.old), tofile=str(args.new)))
    report = "\n".join((
        "# Legal Text Redline",
        "",
        f"- Earlier text: `{args.old}`",
        f"- Earlier SHA-256: `{digest(args.old)}`",
        f"- Later text: `{args.new}`",
        f"- Later SHA-256: `{digest(args.new)}`",
        "",
        "## Unified diff",
        "",
        "```diff",
        diff.rstrip() or "No textual difference detected.",
        "```",
        "",
        "This is a textual comparison. Verify legal effect, commencement, amendments, schedules, cross-references, and official publication separately.",
    )) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
