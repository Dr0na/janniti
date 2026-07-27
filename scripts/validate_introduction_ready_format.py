#!/usr/bin/env python3
"""Check Markdown presentation rules for a clean introduction-ready instrument."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ENUMERATED = re.compile(r"^\s{0,3}(?:\([a-z]+\)|\([ivxlcdm]+\)|\d+\.)\s", re.IGNORECASE)
CODE_INDENTED_ENUMERATED = re.compile(r"^ {4,}(?:\([a-z]+\)|\([ivxlcdm]+\)|\d+\.)\s", re.IGNORECASE)
BULLET = re.compile(r"^\s*[-*+]\s+")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="clean introduction-ready Markdown instrument")
    args = parser.parse_args()
    try:
        lines = args.file.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        print(f"ERROR: cannot read {args.file}: {exc}", file=sys.stderr)
        return 2

    findings: list[str] = []
    for index, line in enumerate(lines):
        line_number = index + 1
        if CODE_INDENTED_ENUMERATED.match(line):
            findings.append(f"L{line_number}: four-space indentation renders a legal item as a code block")
        if BULLET.match(line):
            findings.append(f"L{line_number}: Markdown bullet found; use legal clause designators instead")
        if ENUMERATED.match(line) and index and ENUMERATED.match(lines[index - 1]):
            findings.append(f"L{line_number}: consecutive legal items need a blank line so they render separately")

    if findings:
        print(f"Introduction-ready format: {len(findings)} finding(s) in {args.file}")
        print("\n".join(findings))
        return 1
    print(f"Introduction-ready format: passed for {args.file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
