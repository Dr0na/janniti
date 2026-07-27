#!/usr/bin/env python3
"""Flag likely unsourced legal claims in Markdown as a preflight check.

This program does not determine whether a legal proposition is correct. It detects
likely legal assertions that lack a nearby Markdown link or footnote reference and
reports non-official links for human review.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

OFFICIAL_HOSTS = {
    "indiacode.nic.in", "www.indiacode.nic.in", "egazette.nic.in",
    "sansad.in", "www.sansad.in", "elibrary.sansad.in", "eparlib.sansad.in",
    "sci.gov.in", "www.sci.gov.in", "api.sci.gov.in", "scr.sci.gov.in",
    "eci.gov.in", "www.eci.gov.in", "rashtrapatibhavan.gov.in",
    "www.rashtrapatibhavan.gov.in", "legislative.gov.in", "www.legislative.gov.in",
    "gov.in", "www.gov.in",
}
CLAIM_PATTERN = re.compile(
    r"\b(Article|section|subsection|clause|Schedule|Act|Bill|Constitution|Supreme Court|High Court|"
    r"judgment|judgement|held|holds|requires|prohibits|permits|is in force|was enacted|was repealed|"
    r"was amended|right to|fundamental right)\b",
    re.IGNORECASE,
)
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
FOOTNOTE_PATTERN = re.compile(r"\[\^[^\]]+\]")


def urls_in(line: str) -> list[str]:
    return [match.group(1) for match in LINK_PATTERN.finditer(line)]


def is_official(url: str) -> bool:
    host = urlparse(url).hostname
    if not host:
        return False
    return host in OFFICIAL_HOSTS or host.endswith(".gov.in") or host.endswith(".nic.in")


def main() -> int:
    parser = argparse.ArgumentParser(description="Preflight-check Markdown legal citations.")
    parser.add_argument("file", type=Path, help="Markdown file to inspect")
    parser.add_argument("--strict", action="store_true", help="Return 1 when warnings are found")
    args = parser.parse_args()

    try:
        lines = args.file.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        print(f"ERROR: cannot read {args.file}: {exc}", file=sys.stderr)
        return 2

    warnings: list[str] = []
    all_urls: list[tuple[int, str]] = []
    in_fence = False
    for number, line in enumerate(lines, start=1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        urls = urls_in(line)
        all_urls.extend((number, url) for url in urls)
        local_context = " ".join(lines[max(0, number - 2):min(len(lines), number + 1)])
        has_citation = bool(urls or FOOTNOTE_PATTERN.search(local_context))
        if CLAIM_PATTERN.search(line) and not has_citation:
            warnings.append(f"L{number}: possible legal claim without nearby citation: {line.strip()}")

    for number, url in all_urls:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            warnings.append(f"L{number}: non-web citation target needs manual verification: {url}")
        elif not is_official(url):
            warnings.append(f"L{number}: non-official source; verify against a primary authority: {url}")

    if warnings:
        print(f"Citation preflight: {len(warnings)} warning(s) in {args.file}")
        print("\n".join(warnings))
    else:
        print(f"Citation preflight: no mechanical warnings in {args.file}")
    return 1 if warnings and args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
