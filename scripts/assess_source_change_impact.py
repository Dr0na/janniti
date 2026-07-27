#!/usr/bin/env python3
"""Report JanNiti matters whose manifests or research findings reference a changed URL."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def contains_url(path: Path, url: str) -> bool:
    try:
        return url in path.read_text(encoding="utf-8")
    except OSError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="changed official source URL")
    parser.add_argument("--output", type=Path, required=True, help="impact-report JSON path in the active matter")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    impacted = []
    for matter in sorted((root / "outputs").glob("[0-9][0-9][0-9]-*")):
        files = list(matter.rglob("*.json")) + list(matter.rglob("*.md"))
        matches = [str(path.relative_to(root)) for path in files if contains_url(path, args.url)]
        if matches:
            impacted.append({"matter": str(matter.relative_to(root)), "artifacts": matches, "status": "revalidation_required"})
    report = {"schema_version": "1.0", "changed_url": args.url, "acceptance_status": "pending_human_review", "impacted_matters": impacted, "required_action": "Verify the official change, create a legal-change event, and revalidate every listed artifact before relying on it."}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Source-change impact report written: {len(impacted)} impacted matter(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
