# /reconcile-introduction-ready-registry

Audit every JanNiti matter for final-instrument files, verify whether each genuinely passes the introduction-ready gate, and reconcile the registry. This is a repair and verification command, not permission to register a file merely because its name begins `introduction-ready-`.

Read `AGENTS.md`, `commands/prepare-bill-for-introduction.md`, `commands/draft-democratic-law.md`, `references/legal-ethics.md`, `references/review-checklist.md`, and `outputs/README.md`.

## Input

`/reconcile-introduction-ready-registry`

Optionally scope the command to a named matter folder. Without a scope, inspect every matter under `outputs/`.

## Method

1. Run `python3 scripts/audit_introduction_ready_registry.py` and retain its JSON report in the reconciliation record.
2. For every `unregistered_candidate`, locate its matter, preserve the supplied file, and run the complete `/prepare-bill-for-introduction` readiness process. Check current official legislature guidance, legal competence, completed ancillary memoranda, source/version support, cross-references, required quality gates, and absence of placeholders or unresolved choices.
3. If the instrument passes, save or retain the clean final file under `01-draft/introduction-ready-<instrument-name>.md`, then register it with `scripts/update_introduction_ready_registry.py --register ... --instrument ... --instrument-type ... --ready`.
4. If it fails, do not register it. Rename or supersede it with `not-ready-for-introduction.md` where appropriate, preserve the original, and record exact blockers and repair actions in the matter's analytical record.
5. For every `dangling_registry_entry`, correct the matter record or remove the stale registration only after confirming that the final file is unavailable or no longer satisfies the gate. Do not silently discard a historical instrument.
6. Regenerate and verify the registry with:

   ```text
   python3 scripts/update_introduction_ready_registry.py
   python3 scripts/update_introduction_ready_registry.py --check
   python3 scripts/audit_introduction_ready_registry.py --check
   ```

7. Save `registry-reconciliation.md` in each affected matter's `01-draft/` folder, and save a cross-matter summary at `outputs/introduction-ready-registry-reconciliation.md`.

## Required deliverable

1. Candidate, registered, corrected, blocked, and dangling-entry counts.
2. A table listing each instrument, matter, readiness result, registry action, exact blockers if any, and final-file link.
3. The updated [introduction-ready registry](../outputs/introduction-ready-registry.md).
4. A clear statement that registration reflects JanNiti's documented readiness gate only, not legislative filing, acceptance, certification, or enactment.
