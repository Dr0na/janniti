# JanNiti Matter Register

Every Bill, law, policy, institutional framework, legal review, or other generation task is a **matter**. Create one numbered matter folder and keep its entire legal record inside it. Do not scatter a matter across type-based directories, and do not place generated work in `commands/`, `templates/`, `references/`, or the repository root.

## Matter naming

```text
outputs/<NNN>-<descriptive-slug>/
```

- `NNN` is the next repository-wide three-digit matter number: `001`, `002`, `003`.
- The slug is lower-case, hyphenated, and identifies the matter.
- A matter number is a permanent audit reference. Never renumber, overwrite, or silently replace a completed matter.
- Use one matter folder for all revisions and follow-on work concerning the same instrument. Create a separate matter only when the target or scope is materially different.

## Required structure

The helper creates this complete, sortable structure:

```text
outputs/001-election-integrity-bill/
├── manifest.json
├── 00-research-and-scope/
├── 01-draft/
├── 02-legal-review/
├── 03-validation/
├── 04-legislative-lint/
├── 05-citation-verification/
├── 06-provenance/
├── 07-constitutional-stress-test/
├── 08-institutional-power-map/
├── 09-democratic-impact-monitor/
├── 10-public-deliberation/
├── 11-public-legal-accessibility/
├── 12-expert-escalation/
├── 13-democratic-quality-scorecard/
└── 14-legal-change-monitoring/
```

Store command results in the matching numbered subfolder. Put related supporting files—such as source tables, redlines, machine reports, public summaries, and structured JSON—beside the primary deliverable for that command. `manifest.json` is an index record, not legal evidence or a provenance ledger.

For a Bill or other formal legislative instrument, `01-draft/` must keep the analytical record separate from the clean circulation text. Use `analysis-and-drafting-record.md` for analysis, sources, options, clause notes, and gate reports, and `introduction-ready-<instrument-name>.md` only for completed operative text and applicable formal memoranda. If a formal-readiness blocker remains, name the clean file `not-ready-for-introduction.md` and record the exact blocker in the analytical record.

## Introduction-ready instrument registry

[`introduction-ready-registry.md`](introduction-ready-registry.md) is the generated public index of final JanNiti Bills, laws, amendments, rules, and regulations that have passed the framework's introduction-ready gate. Each row links directly to its final clean instrument and identifies its matter, type, jurisdiction, and as-of date. The companion JSON file supports machine use.

`/prepare-bill-for-introduction` updates the registry and the **Registered introduction-ready instruments** section of the repository README automatically after a successful gate. `/reconcile-introduction-ready-registry` performs the same update after reconciling missing records. To regenerate or verify both, run:

```text
python3 scripts/update_introduction_ready_registry.py
python3 scripts/update_introduction_ready_registry.py --check
```

To identify unregistered final-file candidates or stale registrations, run `python3 scripts/audit_introduction_ready_registry.py --check`, or use `/reconcile-introduction-ready-registry` to validate and repair them.

The registry is not evidence that a legislature has introduced, accepted, certified, authenticated, or enacted an instrument.

Before marking a clean Bill ready, run `python3 scripts/validate_introduction_ready_format.py <introduction-ready-bill.md>` to catch merged legal list items, Markdown bullets, and code-block indentation.

Run `python3 scripts/build_matter_index.py` after adding or changing a matter manifest. It creates `outputs/matter-index.json`, a deterministic cross-matter index for discovery; it does not replace source verification or a matter's own record.

## Create a matter

Run from the repository root:

```text
python3 scripts/new_output.py "Election Integrity Bill"
```

Use `--dry-run` to preview the next matter path. The helper creates the next matter directory, its manifest, and every numbered artefact subfolder. When continuing existing work, reuse its matter folder and do not run the helper again.

## Command mapping

| Command | Matter subfolder |
|---|---|
| `/research-indian-law` | `00-research-and-scope/` |
| `/draft-democratic-law` | `01-draft/` |
| `/expert-legal-review` | `02-legal-review/` |
| `/validate-law` | `03-validation/` |
| `/legislative-lint` | `04-legislative-lint/` |
| `/verify-legal-citations` | `05-citation-verification/` |
| `/build-legal-provenance` | `06-provenance/` |
| `/constitutional-stress-test` | `07-constitutional-stress-test/` |
| `/map-institutional-power` | `08-institutional-power-map/` |
| `/monitor-democratic-impact` | `09-democratic-impact-monitor/` |
| `/public-deliberation` | `10-public-deliberation/` |
| `/public-legal-accessibility` | `11-public-legal-accessibility/` |
| `/expert-escalation` | `12-expert-escalation/` |
| `/score-democratic-quality` | `13-democratic-quality-scorecard/` |
| `/monitor-legal-change` | `14-legal-change-monitoring/` |

## Legacy folders

The top-level `provenance/`, `power-maps/`, `monitoring/`, `consultations/`, `accessibility/`, `scorecards/`, `changes/`, and `escalations/` directories remain as read-only compatibility locations and framework examples. New work belongs in a matter folder. To migrate older work, copy it into a newly numbered matter, preserve the original, and record the original location in the matter manifest.
