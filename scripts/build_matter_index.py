#!/usr/bin/env python3
"""Build a deterministic cross-matter index from JanNiti matter manifests."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def collect(outputs: Path) -> list[dict]:
    matters = []
    for manifest_path in sorted(outputs.glob("[0-9][0-9][0-9]-*/manifest.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        matters.append({
            "matter_id": manifest.get("matter_id"),
            "title": manifest.get("title"),
            "status": manifest.get("status"),
            "jurisdiction": manifest.get("jurisdiction"),
            "as_of_date": manifest.get("as_of_date"),
            "path": str(manifest_path.parent.relative_to(outputs)),
            "related_matters": manifest.get("related_matters", []),
        })
    return matters


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the index is absent or stale")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    outputs = root / "outputs"
    index_path = outputs / "matter-index.json"
    index = {"schema_version": "1.0", "matters": collect(outputs)}
    rendered = json.dumps(index, indent=2) + "\n"
    if args.check:
        if not index_path.is_file() or index_path.read_text(encoding="utf-8") != rendered:
            print("Matter index is absent or stale; run python3 scripts/build_matter_index.py")
            return 1
        print(f"Matter index is current: {len(index['matters'])} matter(s)")
        return 0
    index_path.write_text(rendered, encoding="utf-8")
    print(f"Matter index written: {len(index['matters'])} matter(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
