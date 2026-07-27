#!/usr/bin/env python3
"""Maintain the registry of JanNiti instruments ready for legislative introduction."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import UTC, datetime
from pathlib import Path


REGISTRY_JSON = "introduction-ready-registry.json"
REGISTRY_MD = "introduction-ready-registry.md"
VALID_TYPES = ("Bill", "Law", "Constitutional Amendment", "Rule", "Regulation")
README_START = "<!-- BEGIN INTRODUCTION-READY REGISTRY -->"
README_END = "<!-- END INTRODUCTION-READY REGISTRY -->"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def collect(outputs: Path) -> list[dict]:
    entries = []
    for manifest_path in sorted(outputs.glob("[0-9][0-9][0-9]-*/manifest.json")):
        manifest = load_json(manifest_path)
        matter_dir = manifest_path.parent
        for item in manifest.get("introduction_ready_instruments", []):
            relative_file = item.get("file")
            if not isinstance(relative_file, str):
                continue
            instrument = matter_dir / relative_file
            if not instrument.is_file() or not instrument.name.startswith("introduction-ready-"):
                continue
            entries.append({
                "matter_id": manifest.get("matter_id"),
                "matter_title": manifest.get("title"),
                "jurisdiction": manifest.get("jurisdiction"),
                "as_of_date": manifest.get("as_of_date"),
                "instrument_title": item.get("title"),
                "instrument_type": item.get("instrument_type"),
                "file": str(instrument.relative_to(outputs)),
                "registered_at": item.get("registered_at"),
            })
    return sorted(entries, key=lambda entry: (entry["matter_id"] or "", entry["file"]))


def render(entries: list[dict]) -> tuple[str, str]:
    registry = {"schema_version": "1.0", "instruments": entries}
    json_text = json.dumps(registry, indent=2) + "\n"
    lines = [
        "# Introduction-Ready Instrument Registry",
        "",
        "This generated registry links only to JanNiti instruments whose matter record confirms that the introduction-ready gate passed. It is not evidence that Parliament has accepted, introduced, enacted, certified, or authenticated an instrument.",
        "",
    ]
    if entries:
        lines.extend([
            "| Matter | Instrument | Type | Jurisdiction | As-of date | Ready file |",
            "|---|---|---|---|---|---|",
        ])
        for entry in entries:
            lines.append(
                "| {matter_id} — {matter_title} | {instrument_title} | {instrument_type} | {jurisdiction} | {as_of_date} | [{file}]({file}) |".format(
                    **{key: value if value is not None else "—" for key, value in entry.items()}
                )
            )
    else:
        lines.append("No instruments have yet passed the introduction-ready gate.")
    lines.extend([
        "",
        "To register a newly completed instrument, run `python3 scripts/update_introduction_ready_registry.py --register <matter-folder> --instrument <01-draft/introduction-ready-file.md> --instrument-type <type> --ready` after the readiness gate passes.",
        "",
    ])
    return json_text, "\n".join(lines)


def render_readme_registry(entries: list[dict]) -> str:
    lines = [README_START, "", "### Registered introduction-ready instruments", ""]
    if entries:
        lines.extend(["| Instrument | Type | Jurisdiction | Final file |", "|---|---|---|---|"])
        for entry in entries:
            values = {key: value if value is not None else "—" for key, value in entry.items()}
            lines.append(
                "| {instrument_title} | {instrument_type} | {jurisdiction} | [{file}](outputs/{file}) |".format(**values)
            )
    else:
        lines.append("No instruments have yet passed the introduction-ready gate.")
    lines.extend(["", README_END])
    return "\n".join(lines)


def update_readme(root: Path, entries: list[dict], check: bool) -> bool:
    readme_path = root / "README.md"
    existing = readme_path.read_text(encoding="utf-8")
    replacement = render_readme_registry(entries)
    pattern = re.escape(README_START) + r".*?" + re.escape(README_END)
    updated, replacements = re.subn(pattern, replacement, existing, count=1, flags=re.DOTALL)
    if replacements != 1:
        print("README.md is missing introduction-ready registry markers", file=sys.stderr)
        return False
    if check:
        return existing == updated
    readme_path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", metavar="MATTER", help="matter folder, relative to outputs or repository root")
    parser.add_argument("--instrument", help="instrument path, relative to the matter folder")
    parser.add_argument("--instrument-title", help="completed title of the instrument")
    parser.add_argument("--instrument-type", choices=VALID_TYPES)
    parser.add_argument("--ready", action="store_true", help="confirm that the introduction-ready gate has passed")
    parser.add_argument("--check", action="store_true", help="fail if the generated registry is absent or stale")
    args = parser.parse_args()

    if args.register and (not args.instrument or not args.instrument_type or not args.ready):
        parser.error("--register requires --instrument, --instrument-type, and --ready")
    if not args.register and any((args.instrument, args.instrument_title, args.instrument_type, args.ready)):
        parser.error("--instrument options require --register")

    root = Path(__file__).resolve().parents[1]
    outputs = root / "outputs"
    if args.register:
        candidate = Path(args.register)
        matter_dir = candidate if candidate.is_absolute() else root / candidate
        if not matter_dir.is_dir():
            matter_dir = outputs / args.register
        manifest_path = matter_dir / "manifest.json"
        if not manifest_path.is_file() or matter_dir.parent != outputs:
            print("Registry registration requires a valid direct matter folder under outputs/", file=sys.stderr)
            return 1
        instrument = matter_dir / args.instrument
        if not instrument.is_file() or instrument.parent != matter_dir / "01-draft" or not instrument.name.startswith("introduction-ready-"):
            print("Instrument must be an existing introduction-ready-* file directly in the matter's 01-draft/ folder", file=sys.stderr)
            return 1
        manifest = load_json(manifest_path)
        records = manifest.setdefault("introduction_ready_instruments", [])
        relative_file = str(instrument.relative_to(matter_dir))
        records[:] = [record for record in records if record.get("file") != relative_file]
        records.append({
            "title": args.instrument_title or manifest.get("title") or instrument.stem,
            "instrument_type": args.instrument_type,
            "file": relative_file,
            "registered_at": datetime.now(UTC).replace(microsecond=0).isoformat(),
        })
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    entries = collect(outputs)
    json_text, markdown_text = render(entries)
    json_path, markdown_path = outputs / REGISTRY_JSON, outputs / REGISTRY_MD
    readme_current = update_readme(root, entries, args.check)
    if args.check:
        if not readme_current or not json_path.is_file() or not markdown_path.is_file() or json_path.read_text(encoding="utf-8") != json_text or markdown_path.read_text(encoding="utf-8") != markdown_text:
            print("Introduction-ready registry or README section is absent or stale; run python3 scripts/update_introduction_ready_registry.py", file=sys.stderr)
            return 1
        print(f"Introduction-ready registry is current: {len(entries)} instrument(s)")
        return 0
    json_path.write_text(json_text, encoding="utf-8")
    markdown_path.write_text(markdown_text, encoding="utf-8")
    print(f"Introduction-ready registry written: {len(entries)} instrument(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
