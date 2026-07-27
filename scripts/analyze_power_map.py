#!/usr/bin/env python3
"""Detect structural concentration and circular control in an institutional power map."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

CRITICAL_LEVERS = {"appointment", "removal", "funding", "direction", "investigation", "prosecution", "adjudication", "audit", "information", "emergency", "rulemaking", "contracting"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze institutional power-map concentration.")
    parser.add_argument("file", type=Path, help="Institutional power-map JSON")
    parser.add_argument("--strict", action="store_true", help="Return 1 on High or Critical finding")
    args = parser.parse_args()
    try:
        data = json.loads(args.file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read power map: {exc}", file=sys.stderr)
        return 2
    actors = {actor.get("id"): actor.get("name", actor.get("id")) for actor in data.get("actors", [])}
    relations = data.get("relationships", [])
    errors, findings = [], []
    if data.get("schema_version") != "1.0" or not actors or not isinstance(relations, list):
        errors.append("map requires schema_version 1.0, actors, and relationships")
    controls = defaultdict(set)
    directed = defaultdict(set)
    for index, relation in enumerate(relations, start=1):
        source, target, power = relation.get("from"), relation.get("to"), relation.get("power")
        if source not in actors or target not in actors or not power:
            errors.append(f"relationship {index}: unknown actor or missing power")
            continue
        if power in CRITICAL_LEVERS:
            controls[(source, target)].add(power)
        directed[source].add(target)
    for (source, target), powers in controls.items():
        if len(powers) >= 4:
            severity = "Critical"
        elif len(powers) >= 3:
            severity = "High"
        else:
            continue
        findings.append({"severity": severity, "type": "concentration", "controller": actors[source], "target": actors[target], "powers": sorted(powers), "fix": "Split appointment/funding/direction/removal or add plural independent checks and public review."})
    for source, targets in directed.items():
        for target in targets:
            if source in directed.get(target, set()):
                findings.append({"severity": "High", "type": "circular_control", "controller": actors[source], "target": actors[target], "powers": [], "fix": "Break the reciprocal control loop with an external appointment, budget, audit, or appeal body."})
    if errors:
        print("Power-map validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 2
    if findings:
        print(f"Power-map analysis: {len(findings)} concentration/circularity finding(s)")
        for finding in findings:
            lever_text = ", ".join(finding["powers"]) or "reciprocal control"
            print(f"{finding['severity']} {finding['type']}: {finding['controller']} → {finding['target']} ({lever_text})")
            print(f"  Fix: {finding['fix']}")
    else:
        print("Power-map analysis: no mechanical concentration/circularity findings")
    return 1 if args.strict and any(item["severity"] in {"High", "Critical"} for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
