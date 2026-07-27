#!/usr/bin/env python3
"""Validate structural completeness of a public participation and deliberation plan."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REQUIRED = {"schema_version", "title", "jurisdiction", "as_of", "proposal", "publication", "schedule", "participation", "integrity", "deliberation", "response_to_comments", "remedies"}
NESTED = {
    "publication": {"plain_language_summary", "full_draft", "impact_notes", "evidence_register", "languages", "accessible_formats"},
    "participation": {"channels", "accessibility", "affected_groups", "anti_retaliation"},
    "integrity": {"lobbying_disclosure", "anti_capture", "privacy", "automated_analysis_disclosure"},
    "response_to_comments": {"publication", "fields", "deadline"},
    "remedies": {"complaint_route", "reconsultation_trigger", "public_notice"},
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a public deliberation plan JSON file.")
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    try:
        plan = json.loads(args.file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read consultation plan: {exc}", file=sys.stderr)
        return 2
    errors = []
    missing = REQUIRED - set(plan)
    if plan.get("schema_version") != "1.0" or missing:
        errors.append(f"missing/invalid top-level fields: {sorted(missing)}")
    for name, required in NESTED.items():
        value = plan.get(name)
        if not isinstance(value, dict):
            errors.append(f"{name} must be an object")
        else:
            gap = required - set(value)
            if gap:
                errors.append(f"{name}: missing {sorted(gap)}")
    if errors:
        print("Public-deliberation validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Public-deliberation validation passed: {len(plan['participation']['channels'])} channel(s), {len(plan['publication']['languages'])} language(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
