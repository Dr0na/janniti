# Release Checklist

## Static release gate

- Run `python3 scripts/validate_harness_adapters.py`.
- Run `python3 scripts/validate_acceptance_suite.py`.
- Run `python3 scripts/check_source_health.py --offline`.
- Run `python3 scripts/lint_legislation.py <legal-deliverable.md>` and `python3 scripts/validate_claim_provenance.py <ledger.json>` for each consequential release artifact.
- Run `git diff --check`.
- Verify `release/manifest.json` version and entrypoints.

## Live release gate

- Run the full cross-harness procedure in `tests/harness/README.md` for every claimed supported harness/version.
- Save one completed `results-template.md` record per harness.
- Do not list a harness as live-tested unless its result record exists and has passed the adversarial override test.
- Review any Conditional pass or Fail before release; update adapters and rerun affected cases.

## Version and publication

- Update `governance/CHANGELOG.md` with version, date, source/harness changes, and known limitations.
- Create a Git tag only after a reviewed commit exists. A release manifest version is not a Git tag.
- Publish the known live-test matrix and source-health date with any released copy.
