#!/usr/bin/env python3
"""Validate an independent-review and conflict-of-interest register."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("register", type=Path)
    args = parser.parse_args()
    data = json.loads(args.register.read_text(encoding="utf-8"))
    errors = []
    if data.get("schema_version") != "1.0" or not data.get("matter_id"):
        errors.append("missing schema_version or matter_id")
    reviewers = data.get("reviewers")
    if not isinstance(reviewers, list) or not reviewers:
        errors.append("at least one reviewer is required")
    for reviewer in reviewers or []:
        missing = {"id", "role", "selection_basis", "conflicts_declared", "conflict_disposition", "independence_status", "review_date"} - set(reviewer)
        if missing:
            errors.append(f"reviewer missing {sorted(missing)}")
        elif reviewer["independence_status"] not in {"eligible", "recused", "ineligible"}:
            errors.append(f"{reviewer['id']}: invalid independence_status")
    for issue in data.get("issues", []):
        if not {"id", "severity", "issue", "response", "status"} <= set(issue):
            errors.append("incomplete issue record")
    if errors:
        print("Independent review validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Independent review validation passed: {len(reviewers)} reviewer(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
