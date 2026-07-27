# JanNiti Documentation

JanNiti is a multi-harness legal-governance framework for researching, drafting, validating, improving, and monitoring law through constitutional democracy, equal protection, public freedom, accountability, scientific temper, and safeguards against concentration or misuse of power.

It is an assistive system, not binding legal authority or a substitute for qualified local counsel. It cannot prove that a law has no loopholes; it makes risks, sources, checks, remedies, and residual uncertainty explicit.

## Purpose

JanNiti helps users formulate law and legal frameworks that protect democratic values, fundamental and public freedoms, equality before and equal protection of law, accessible education and health, plural media, independent institutions, and public participation. It is designed to resist political vengeance, selective enforcement, censorship, corruption, secret law, emergency overreach, and capture of public institutions.

## Principles

- People are the ultimate source of political authority, exercised through constitutional democracy, free elections, informed participation, peaceful dissent, and accountable institutions.
- No person, party, court, executive, agency, majority, media owner, or private actor is above constitutional law.
- Every material power needs a legal source, limited purpose, objective trigger, written reason, independent check, public or auditable record, accessible challenge, effective remedy, expiry or review, and anti-evasion protection.
- Equal protection is practical as well as formal: JanNiti checks direct and indirect discrimination, access barriers, and selective enforcement.
- Judicial independence and judicial accountability must coexist; accountability cannot become political retaliation.
- Source material is evidence, never instruction. The framework resists prompt injection, source tampering, unsafe attachments, and privacy leakage.

## Architecture

| Layer | Location | Function |
|---|---|---|
| Charter | `AGENTS.md` | Core legal, ethical, democratic, evidence, and quality rules. |
| Harness adapters | `CLAUDE.md`, `GEMINI.md`, `.cursor/`, `.agents/`, `.github/`, `.opencode/`, `.windsurfrules` | Makes the charter and supported native commands available in supported harnesses. |
| Commands | `commands/` | Repeatable drafting, review, validation, and monitoring workflows. |
| References | `references/` | Ethics, security, India research, lint rules, and review standards. |
| Evidence | `knowledge-base/`, `provenance/`, `changes/` | Primary-source routing, claim traceability, and legal-change records. |
| Safeguards | `power-maps/`, `monitoring/`, `consultations/`, `scorecards/` | Capture analysis, monitoring, participation, and quality gates. |
| Validation | `scripts/`, `tests/`, `benchmarks/` | Mechanical checks, acceptance tests, and regression scenarios. |
| Governance | `governance/`, `release/` | Protected commitments, maintenance, release, and change control. |
| Generated work | `outputs/` | One numbered matter folder per law, Bill, policy, or review task, with ordered folders for every artefact. |

## Lifecycle

```text
Research → provenance → draft or review → lint → power map → stress test
→ equality and rights analysis → public deliberation → expert escalation
→ quality score → impact monitor → introduction-ready package (when needed)
→ change monitoring and revalidation
```

## Documentation map

- [Commands](commands.md): every workflow, when to use it, and outputs.
- [Workflows](workflows.md): end-to-end drafting, review, and maintenance paths.
- [Operations and safety](operations-and-safety.md): sources, security, testing, governance, and releases.

## Quick start

1. Open the repository root in a supported harness.
2. Start with `/janniti <your request>`; it preserves your wording, corrects clear language errors, gathers only relevant repository context, and dispatches to the right workflow.
3. Provide a legal text, file, official link, or clear policy objective and jurisdiction when available.
4. The primary command will invoke `/draft-democratic-law`, `/prepare-bill-for-introduction`, `/validate-law`, `/expert-legal-review`, or another matching command.
5. For consequential work, complete citation verification, stress testing, linting, provenance, and the applicable power-map, participation, monitoring, and scorecard artefacts.

Create the numbered matter folder first: `python3 scripts/new_output.py "<title>"`. See [the matter register](../outputs/README.md) for its permanent artefact folders.

For India, use the India module and the official-source registry before relying on current law.

## Existing Bills: preparation for introduction

For every new Bill or formal legislative instrument, JanNiti automatically runs `/prepare-bill-for-introduction` after drafting. It can also be run manually for an existing generated Bill: `/prepare-bill-for-introduction <Bill file, matter folder, or pasted text>`. It reconstructs a separate, clean Bill for circulation and introduction, retains the original and all analysis in the matter record, completes applicable formal memoranda, and performs legal, citation, lint, and constitutional-stress checks.

The command labels an output `introduction-ready-<instrument-name>.md` only after all formal-readiness conditions have been met. If a required fact, official format, source check, approval, or quality finding remains unresolved, it writes `not-ready-for-introduction.md` and identifies the precise blocker. Formal admissibility and filing always remain with the competent sponsor and legislative secretariat.

## Maintaining the introduction-ready registry

The [introduction-ready instrument registry](../outputs/introduction-ready-registry.md) links to every final Bill, law, amendment, rule, or regulation that has passed JanNiti's documented readiness gate. New finished instruments are added automatically.

Use `/reconcile-introduction-ready-registry` to audit all matters, validate unregistered final-file candidates, add the ones that genuinely pass, and report blocked or stale entries. For example:

```text
/reconcile-introduction-ready-registry
/reconcile-introduction-ready-registry outputs/001-municipal-budget-bill
```

The read-only mechanical check is `python3 scripts/audit_introduction_ready_registry.py`. The reconciler then performs the necessary legal/formal review before registration; it does not treat a filename as proof of readiness.

## Antigravity

Antigravity registers the workspace workflow at `.agents/workflows/janniti.md` as `/janniti`. Open JanNiti's repository root as the active workspace, then in the editor's Agent panel open `...` → **Customizations** → **Workflows**. Reopen that panel or reload the workspace after pulling changes so Antigravity rescans the workflow directory. Invoke `/janniti` from the editor Agent chat, not the Agent Manager.
