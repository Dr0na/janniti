#!/usr/bin/env python3
"""Create an immutable, hash-pinned snapshot from an authorised local legal source file."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import UTC, datetime
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_id")
    parser.add_argument("file", type=Path, help="authorised local copy of the official source")
    parser.add_argument("--url", required=True, help="direct official URL")
    parser.add_argument("--publisher", required=True)
    parser.add_argument("--output-dir", type=Path, required=True, help="matter's 14-legal-change-monitoring/snapshots directory")
    args = parser.parse_args()
    if not args.file.is_file():
        raise SystemExit(f"snapshot: source file not found: {args.file}")
    content = args.file.read_bytes()
    checksum = hashlib.sha256(content).hexdigest()
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    destination = args.output_dir / f"{args.source_id}-{timestamp}{args.file.suffix}"
    if destination.exists():
        raise SystemExit(f"snapshot: refusing to overwrite {destination}")
    shutil.copyfile(args.file, destination)
    metadata = {"source_id": args.source_id, "url": args.url, "publisher": args.publisher, "retrieved_at": datetime.now(UTC).replace(microsecond=0).isoformat(), "file": destination.name, "sha256": checksum, "acceptance_status": "pending_human_review"}
    destination.with_suffix(destination.suffix + ".json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
