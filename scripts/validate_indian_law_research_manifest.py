#!/usr/bin/env python3
"""Validate structured findings that accompany an Indian law research pack."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    errors = []
    for key in ("matter_id", "topic", "as_of_date", "jurisdictions", "findings", "gaps", "next_step"):
        if key not in data:
            errors.append(f"missing {key}")
    if not isinstance(data.get("jurisdictions"), list) or not data.get("jurisdictions"):
        errors.append("jurisdictions must be non-empty")
    for finding in data.get("findings", []):
        missing = {"id", "instrument_type", "title", "jurisdiction", "status", "official_sources", "limitations"} - set(finding)
        if missing:
            errors.append(f"finding missing fields: {sorted(missing)}")
            continue
        if not finding["official_sources"]:
            errors.append(f"{finding['id']}: official_sources is required")
        for source in finding["official_sources"]:
            if not {"url", "publisher", "pinpoint", "retrieved_at"} <= set(source):
                errors.append(f"{finding['id']}: incomplete official source")
                continue
            parsed = urlparse(source["url"])
            if parsed.scheme != "https" or not parsed.netloc:
                errors.append(f"{finding['id']}: official source must be HTTPS")
    if errors:
        print("Indian law research manifest validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Indian law research manifest validation passed: {len(data['findings'])} finding(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
