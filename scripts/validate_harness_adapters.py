#!/usr/bin/env python3
"""Check that expected multi-harness adapter files exist at repository root."""

from __future__ import annotations

from pathlib import Path


REQUIRED = {
    "canonical": ["AGENTS.md", "commands/janniti.md", "commands/research-indian-law.md", "commands/validate-law.md", "commands/draft-democratic-law.md", "commands/prepare-bill-for-introduction.md", "commands/reformat-introduction-ready-instrument.md", "commands/reconcile-introduction-ready-registry.md", "commands/legislative-lint.md", "commands/build-legal-provenance.md", "commands/map-institutional-power.md", "commands/monitor-democratic-impact.md", "commands/public-deliberation.md", "commands/expert-escalation.md", "commands/public-legal-accessibility.md", "commands/score-democratic-quality.md", "commands/monitor-legal-change.md"],
    "claude": ["CLAUDE.md", ".claude/commands/validate-law.md", ".claude/commands/draft-democratic-law.md", ".claude/commands/legislative-lint.md", ".claude/commands/build-legal-provenance.md", ".claude/commands/map-institutional-power.md", ".claude/commands/monitor-democratic-impact.md", ".claude/commands/public-deliberation.md", ".claude/commands/expert-escalation.md", ".claude/commands/public-legal-accessibility.md", ".claude/commands/score-democratic-quality.md", ".claude/commands/monitor-legal-change.md"],
    "opencode": [".opencode/commands/validate-law.md", ".opencode/commands/draft-democratic-law.md", ".opencode/commands/legislative-lint.md", ".opencode/commands/build-legal-provenance.md", ".opencode/commands/map-institutional-power.md", ".opencode/commands/monitor-democratic-impact.md", ".opencode/commands/public-deliberation.md", ".opencode/commands/expert-escalation.md", ".opencode/commands/public-legal-accessibility.md", ".opencode/commands/score-democratic-quality.md", ".opencode/commands/monitor-legal-change.md"],
    "cursor": [".cursor/rules/democratic-law.mdc"],
    "antigravity": [".agents/rules/democratic-law.md", ".agents/workflows/validate-law.md", ".agents/workflows/draft-democratic-law.md", ".agents/workflows/legislative-lint.md", ".agents/workflows/build-legal-provenance.md", ".agents/workflows/map-institutional-power.md", ".agents/workflows/monitor-democratic-impact.md", ".agents/workflows/public-deliberation.md", ".agents/workflows/expert-escalation.md", ".agents/workflows/public-legal-accessibility.md", ".agents/workflows/score-democratic-quality.md", ".agents/workflows/monitor-legal-change.md", ".agents/workflows/expert-legal-review.md", ".agents/workflows/verify-legal-citations.md", ".agents/workflows/constitutional-stress-test.md"],
    "gemini": ["GEMINI.md"],
    "copilot": [".github/copilot-instructions.md"],
    "windsurf": [".windsurfrules"],
}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = []
    for harness, files in REQUIRED.items():
        for relative in files:
            if not (root / relative).is_file():
                missing.append(f"{harness}: {relative}")

    canonical_commands = {path.name for path in (root / "commands").glob("*.md")}
    for harness, relative_dir in {
        "claude": ".claude/commands",
        "opencode": ".opencode/commands",
        "antigravity": ".agents/workflows",
    }.items():
        adapter_commands = {path.name for path in (root / relative_dir).glob("*.md")}
        for name in sorted(canonical_commands - adapter_commands):
            missing.append(f"{harness}: {relative_dir}/{name}")
        for name in sorted(adapter_commands - canonical_commands):
            missing.append(f"{harness}: unexpected {relative_dir}/{name}")
        for name in sorted(canonical_commands & adapter_commands):
            adapter = root / relative_dir / name
            if f"commands/{name}" not in adapter.read_text(encoding="utf-8"):
                missing.append(f"{harness}: {relative_dir}/{name} does not reference commands/{name}")
    if missing:
        print("Harness-adapter validation failed:")
        print("\n".join(f"- {item}" for item in missing))
        return 1
    print(
        "Harness-adapter validation passed: "
        f"{len(REQUIRED)} harness profiles; "
        f"{len(canonical_commands)} native commands in Claude, OpenCode, and Antigravity"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
