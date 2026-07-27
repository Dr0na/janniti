#!/usr/bin/env python3
"""Validate JanNiti's State and Union Territory research-coverage registry."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse


def main() -> int:
    registry_path = Path(__file__).resolve().parents[1] / "knowledge-base/state-ut-source-registry.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    jurisdictions = registry.get("jurisdictions", [])
    codes = [item.get("code") for item in jurisdictions]
    states = [item for item in jurisdictions if item.get("kind") == "State"]
    uts = [item for item in jurisdictions if item.get("kind") == "Union Territory"]
    errors = []
    if registry.get("schema_version") != "1.0":
        errors.append("unsupported schema_version")
    if len(states) != 28 or len(uts) != 8:
        errors.append(f"expected 28 States and 8 Union Territories; found {len(states)} and {len(uts)}")
    if len(codes) != len(set(codes)) or any(not code for code in codes):
        errors.append("jurisdiction codes must be present and unique")
    parsed = urlparse(registry.get("official_directory", ""))
    if parsed.scheme != "https" or not parsed.netloc:
        errors.append("official_directory must be an HTTPS URL")
    if registry.get("required_source_types") != ["legislature", "law_department", "official_gazette", "high_court_judgments"]:
        errors.append("required source types are incomplete")
    if errors:
        print("State/UT source registry validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("State/UT source registry validation passed: 28 States and 8 Union Territories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
