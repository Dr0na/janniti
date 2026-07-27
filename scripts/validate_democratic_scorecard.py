#!/usr/bin/env python3
"""Validate scorecard structure and block critical democratic-quality deficits."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REQUIRED_IDS = {"rights", "equality", "accountability", "power_concentration", "transparency", "enforceability", "accessibility", "public_participation"}
BLOCKING = {"rights", "equality", "accountability", "power_concentration"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a democratic-quality scorecard.")
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read scorecard: {exc}", file=sys.stderr)
        return 2
    dimensions = {item.get("id"): item for item in data.get("dimensions", [])}
    errors = []
    if data.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if REQUIRED_IDS - set(dimensions):
        errors.append(f"missing dimensions: {sorted(REQUIRED_IDS - set(dimensions))}")
    blocked = []
    for identifier, item in dimensions.items():
        score = item.get("score")
        if not isinstance(score, int) or not 0 <= score <= 5:
            errors.append(f"{identifier}: score must be an integer from 0 to 5")
        for field in ("evidence", "uncertainty", "corrective_action"):
            if not item.get(field):
                errors.append(f"{identifier}: missing {field}")
        if identifier in BLOCKING and isinstance(score, int) and score <= 1:
            blocked.append(identifier)
    if errors:
        print("Scorecard validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Scorecard validation passed: {len(dimensions)} dimension(s)")
    if blocked:
        print(f"NOT READY: blocking scores in {', '.join(blocked)}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
