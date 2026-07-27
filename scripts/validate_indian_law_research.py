#!/usr/bin/env python3
"""Check that an Indian law landscape research pack has required sections."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_HEADINGS = (
    "## 1. Scope and search record",
    "## 2. Executive finding and reliance limits",
    "## 3. Constitutional and legislative-competence map",
    "## 4. Union legal landscape",
    "## 5. State and Union Territory coverage",
    "## 6. Bills, amendments, ordinances, history, and Gazette",
    "## 7. Delegated law and implementation",
    "## 8. Judicial and administrative treatment",
    "## 9. Rights, equality, federalism, and public-interest assessment",
    "## 10. Gaps and reform options",
    "## 11. Source register and limitations",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("research_pack", type=Path)
    args = parser.parse_args()
    text = args.research_pack.read_text(encoding="utf-8")
    missing = [heading for heading in REQUIRED_HEADINGS if heading not in text]
    if missing:
        print("Indian law research validation failed:")
        print("\n".join(f"- Missing: {heading}" for heading in missing))
        return 1
    if "Official URL" not in text or "Retrieved" not in text:
        print("Indian law research validation failed: source register lacks official URL or retrieval fields")
        return 1
    print("Indian law research validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
