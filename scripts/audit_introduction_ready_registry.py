#!/usr/bin/env python3
"""Audit final-instrument files against the introduction-ready registry."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="exit non-zero when unregistered candidates or dangling entries exist")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    outputs = root / "outputs"
    records: set[str] = set()
    candidates: set[str] = set()
    for manifest_path in sorted(outputs.glob("[0-9][0-9][0-9]-*/manifest.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        matter_dir = manifest_path.parent
        for item in manifest.get("introduction_ready_instruments", []):
            file_name = item.get("file")
            if isinstance(file_name, str):
                records.add(str((matter_dir / file_name).relative_to(outputs)))
        for instrument in (matter_dir / "01-draft").glob("introduction-ready-*.md"):
            candidates.add(str(instrument.relative_to(outputs)))

    unregistered = sorted(candidates - records)
    dangling = sorted(records - candidates)
    report = {
        "schema_version": "1.0",
        "candidate_count": len(candidates),
        "registered_count": len(records),
        "unregistered_candidates": unregistered,
        "dangling_registry_entries": dangling,
    }
    print(json.dumps(report, indent=2))
    if args.check and (unregistered or dangling):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
