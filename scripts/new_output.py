#!/usr/bin/env python3
"""Create a numbered JanNiti matter folder with ordered artefact subfolders."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


ARTEFACT_FOLDERS = (
    "00-research-and-scope",
    "01-draft",
    "02-legal-review",
    "03-validation",
    "04-legislative-lint",
    "05-citation-verification",
    "06-provenance",
    "07-constitutional-stress-test",
    "08-institutional-power-map",
    "09-democratic-impact-monitor",
    "10-public-deliberation",
    "11-public-legal-accessibility",
    "12-expert-escalation",
    "13-democratic-quality-scorecard",
    "14-legal-change-monitoring",
)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("title must contain at least one letter or number")
    return slug


def next_number(outputs_dir: Path) -> int:
    numbers = []
    for child in outputs_dir.iterdir() if outputs_dir.exists() else []:
        match = re.match(r"^(\d{3})-", child.name)
        if match and child.is_dir():
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="short descriptive title for the Bill, law, review, or other matter")
    parser.add_argument("--dry-run", action="store_true", help="print the next path without creating it")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    outputs_dir = root / "outputs"
    number = next_number(outputs_dir)
    matter_id = f"{number:03d}"
    matter_dir = outputs_dir / f"{matter_id}-{slugify(args.title)}"

    if args.dry_run:
        print(matter_dir.relative_to(root))
        return 0

    outputs_dir.mkdir(parents=True, exist_ok=True)
    matter_dir.mkdir()
    for folder in ARTEFACT_FOLDERS:
        (matter_dir / folder).mkdir()
    manifest = {
        "matter_id": matter_id,
        "title": args.title,
        "status": "in_progress",
        "created_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "jurisdiction": None,
        "as_of_date": None,
        "source_or_instruction": None,
        "related_matters": [],
        "legacy_source_location": None,
        "notes": "Complete this index record; do not treat it as legal evidence.",
    }
    (matter_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(matter_dir.relative_to(root))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileExistsError, ValueError) as exc:
        print(f"new_output: {exc}", file=sys.stderr)
        raise SystemExit(1)
