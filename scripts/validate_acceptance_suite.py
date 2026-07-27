#!/usr/bin/env python3
"""Validate the structure of the legal-agent acceptance suite."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1] / "tests" / "acceptance"
    manifest_path = root / "manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot load {manifest_path}: {exc}", file=sys.stderr)
        return 2

    required = manifest.get("required_headings", [])
    errors: list[str] = []
    for case in manifest.get("cases", []):
        path = root / case["file"]
        if not path.is_file():
            errors.append(f"missing case file: {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        for heading in required:
            if heading not in text:
                errors.append(f"{path.name}: missing required heading fragment {heading!r}")
        if not case.get("command", "").startswith("/"):
            errors.append(f"{path.name}: command must start with '/'")

    if errors:
        print("Acceptance-suite validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Acceptance-suite validation passed: {len(manifest['cases'])} case(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
