#!/usr/bin/env python3
"""Validate structural completeness of a Democratic Impact and Implementation Monitor."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

TOP_LEVEL = {"schema_version", "title", "jurisdiction", "as_of", "objective", "affected_groups", "indicators", "oversight", "complaints", "triggers", "review"}
INDICATOR = {"id", "name", "category", "definition", "data_source", "frequency", "publication", "independent_validation", "privacy_safeguard"}
TRIGGER = {"id", "condition", "detector", "responsible_body", "deadline", "interim_protection", "correction", "public_notice"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a democratic-impact monitor JSON plan.")
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    try:
        plan = json.loads(args.file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read monitor plan: {exc}", file=sys.stderr)
        return 2
    errors = []
    missing = TOP_LEVEL - set(plan)
    if plan.get("schema_version") != "1.0" or missing:
        errors.append(f"missing/invalid top-level fields: {sorted(missing)}")
    if not plan.get("affected_groups") or not plan.get("indicators") or not plan.get("triggers"):
        errors.append("affected_groups, indicators, and triggers must be non-empty")
    for kind, required in (("indicators", INDICATOR), ("triggers", TRIGGER)):
        for index, item in enumerate(plan.get(kind, []), start=1):
            gap = required - set(item)
            if gap:
                errors.append(f"{kind} {index}: missing {sorted(gap)}")
    for name in ("oversight", "complaints", "review"):
        if not isinstance(plan.get(name), dict):
            errors.append(f"{name} must be an object")
    if errors:
        print("Monitor validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Monitor validation passed: {len(plan['indicators'])} indicator(s), {len(plan['triggers'])} trigger(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
