#!/usr/bin/env python3
"""Validate source-registry structure and optionally check official-source URLs."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse


ENTRY = re.compile(r"^\s{2}- id: ([a-z0-9-]+)$")
URL = re.compile(r'^\s{4}url: "(https://[^\"]+)"$')
OFFICIAL_HOSTS = {
    "indiacode.nic.in", "www.indiacode.nic.in", "egazette.nic.in",
    "sansad.in", "www.sansad.in", "elibrary.sansad.in", "eparlib.sansad.in",
    "sci.gov.in", "www.sci.gov.in", "scr.sci.gov.in",
    "eci.gov.in", "www.eci.gov.in", "rashtrapatibhavan.gov.in",
    "www.rashtrapatibhavan.gov.in", "legislative.gov.in", "www.legislative.gov.in",
}


def load_entries(path: Path) -> list[tuple[str, str]]:
    current_id: str | None = None
    entries: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        entry = ENTRY.match(line)
        if entry:
            current_id = entry.group(1)
            continue
        url = URL.match(line)
        if url:
            if current_id is None:
                raise ValueError("source URL appears before a collection id")
            entries.append((current_id, url.group(1)))
    if not entries:
        raise ValueError("no source collections found")
    return entries


def check_url(identifier: str, url: str, timeout: float) -> str:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Legal-Agent-Source-Health/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return f"OK {identifier}: HTTP {response.status} {url}"
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403, 405}:
            return f"WARN {identifier}: HTTP {exc.code}; source may require browser/CAPTCHA/manual access {url}"
        return f"FAIL {identifier}: HTTP {exc.code} {url}"
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return f"FAIL {identifier}: {exc} {url}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the official-source registry.")
    parser.add_argument("--offline", action="store_true", help="Validate only registry structure and URL format")
    parser.add_argument("--timeout", type=float, default=15.0, help="Seconds per URL check")
    args = parser.parse_args()

    registry = Path(__file__).resolve().parents[1] / "knowledge-base" / "sources.yaml"
    try:
        entries = load_entries(registry)
    except (OSError, ValueError) as exc:
        print(f"FAIL registry: {exc}", file=sys.stderr)
        return 2

    errors: list[str] = []
    seen_ids: set[str] = set()
    for identifier, url in entries:
        host = urlparse(url).hostname or ""
        if identifier in seen_ids or not (host in OFFICIAL_HOSTS or host.endswith(".gov.in") or host.endswith(".nic.in")):
            errors.append(f"FAIL {identifier}: duplicate id or non-official host {url}")
        seen_ids.add(identifier)

    if errors:
        print("\n".join(errors))
        return 1
    if args.offline:
        print(f"Source-health offline validation passed: {len(entries)} official collection(s)")
        return 0

    results = [check_url(identifier, url, args.timeout) for identifier, url in entries]
    print("\n".join(results))
    return 1 if any(result.startswith("FAIL") for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
