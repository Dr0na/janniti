#!/usr/bin/env python3
"""Validate the direct official-source registry used for acquisition and monitoring."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

OFFICIAL_HOSTS = {"sansad.in", "www.sansad.in", "allahabadhighcourt.in", "www.allahabadhighcourt.in"}


def main() -> int:
    path = Path(__file__).resolve().parents[1] / "knowledge-base/verified-source-registry.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    errors, identifiers = [], set()
    for source in data.get("sources", []):
        missing = {"id", "scope", "source_type", "url", "publisher", "verification_status", "last_verified", "verified_by"} - set(source)
        if missing:
            errors.append(f"source missing {sorted(missing)}")
            continue
        if source["id"] in identifiers:
            errors.append(f"duplicate source id {source['id']}")
        identifiers.add(source["id"])
        parsed = urlparse(source["url"])
        if parsed.scheme != "https" or not parsed.netloc or not (parsed.netloc in OFFICIAL_HOSTS or parsed.netloc.endswith(".gov.in") or parsed.netloc.endswith(".nic.in")):
            errors.append(f"{source['id']}: URL is not a direct official Indian HTTPS host")
    if errors:
        print("Verified source registry validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Verified source registry validation passed: {len(identifiers)} source(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
