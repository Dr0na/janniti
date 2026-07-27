#!/usr/bin/env python3
"""Validate structure of a legal change event and its revalidation obligations."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REQUIRED = {"schema_version", "event_id", "source", "versions", "status_assessment", "change_summary", "impact", "decision"}
IMPACT = {"classification", "affected_claims", "affected_artifacts", "rights_risk", "review_owner", "deadline", "interim_safeguard", "public_notice"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a legal change-event JSON file.")
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    try:
        event = json.loads(args.file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read change event: {exc}", file=sys.stderr)
        return 2
    errors = []
    if event.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if REQUIRED - set(event):
        errors.append(f"missing top-level fields: {sorted(REQUIRED - set(event))}")
    impact = event.get("impact", {})
    if not isinstance(impact, dict) or IMPACT - set(impact):
        errors.append("impact missing required fields")
    if impact.get("classification") in {"urgent_rights_risk", "withdrawal_or_correction_required"} and not impact.get("interim_safeguard"):
        errors.append("urgent impact requires interim safeguard")
    if errors:
        print("Change-event validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Change-event validation passed: {event['event_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
