#!/usr/bin/env python3
"""Build the auditable State/UT official-source verification queue."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    registry = json.loads((root / "knowledge-base/state-ut-source-registry.json").read_text(encoding="utf-8"))
    output = root / "knowledge-base/state-ut-source-verification-queue.json"
    existing = {}
    if output.is_file():
        existing = {(item["jurisdiction_code"], item["source_type"]): item for item in json.loads(output.read_text(encoding="utf-8")).get("items", [])}
    items = []
    for jurisdiction in registry["jurisdictions"]:
        for source_type in registry["required_source_types"]:
            key = (jurisdiction["code"], source_type)
            item = existing.get(key, {
                "jurisdiction_code": jurisdiction["code"],
                "jurisdiction": jurisdiction["name"],
                "kind": jurisdiction["kind"],
                "source_type": source_type,
                "status": "pending_verification",
                "direct_official_url": None,
                "publisher": None,
                "verified_at": None,
                "verified_by": None,
                "health_status": "not_checked",
                "access_language_archive_limitations": None,
                "evidence_url": registry["official_directory"],
            })
            items.append(item)
    queue = {"schema_version": "1.0", "generated_at": datetime.now(UTC).replace(microsecond=0).isoformat(), "items": items}
    output.write_text(json.dumps(queue, indent=2) + "\n", encoding="utf-8")
    print(f"State/UT source queue written: {len(items)} item(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
