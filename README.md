# JanNiti

A portable, multi-harness legal-governance framework for researching, formulating, reviewing, validating, and improving laws and constitutional frameworks in favour of democratic values, people as the ultimate source of political authority, fundamental and public freedoms, free and accountable media, equality before and equal protection of law, anti-discrimination, safeguards against political vengeance and selective enforcement, scientific temper, accountable education and health systems, public accountability, public interest, national interest, and rights.

It is a high-standard drafting and review charter, not a substitute for a licensed lawyer or binding local authority. It deliberately does not support partisan advocacy, suppression of lawful opposition, unchecked state power, judicial self-insulation, or any institution claiming supremacy over constitutional law.

Start with the [full documentation](docs/README.md), [command reference](docs/commands.md), and [workflow guide](docs/workflows.md).

## Primary command

Use `/janniti <your request>` for every new request. It is JanNiti's single primary entry point: it preserves the original request, corrects clear language errors, loads only relevant repository and source context, and invokes the appropriate research, drafting, review, or monitoring workflow.

`/refine-and-route <your request>` remains available as a backward-compatible alias.

For Antigravity, open this repository as the active workspace and invoke `/janniti` in the editor Agent chat. Its workspace workflow is [`.agents/workflows/janniti.md`](.agents/workflows/janniti.md); refresh **Customizations → Workflows** after updating the repository.

### Examples

| Input type | Example |
|---|---|
| Existing Indian law or reform baseline | `/janniti what laws india and states have for whistleblower protection?` |
| New law, Bill, rule, amendment, or institution | `/janniti draft a Karnataka Bill to make municipal budgeting more transparent` |
| Existing generated Bill needs Parliament-ready repair | `/janniti make this generated Bill ready for introduction in Parliament: <Bill file or matter folder>` |
| Review, audit, loopholes, or redline | `/janniti check this procurement rule for corruption loopholes and give exact redlines: <file or text>` |
| Independent legal or policy review | `/janniti independently review this proposed media-regulation framework: <file or link>` |
| Citation, authority, version, or later-history check | `/janniti verify whether these citations are current and accurately support the claims: <file>` |
| Legal-source or version change | `/janniti compare this amended rule with the previous Gazette version and identify affected work: <old> <new>` |
| Institutional power or capture analysis | `/janniti map who appoints, funds, directs, and can remove this anti-corruption body: <proposal>` |
| Post-enactment monitoring | `/janniti design a public impact monitor for this education law: <law or proposal>` |
| Public consultation | `/janniti create an accessible consultation plan for this housing policy: <policy>` |
| Plain-language public legal communication | `/janniti explain this tenancy-rights rule for residents in plain English and Hindi: <text>` |
| Democratic-quality assessment | `/janniti score this election-finance proposal for democratic safeguards: <proposal>` |
| High-risk proposal | `/janniti review this emergency surveillance Bill and prepare the required independent-review brief: <Bill>` |
| Short or error-prone request | `/janniti pls chek new media bill 4 free speech loophols` |
| Non-legal task | `/janniti summarise this meeting note and list the decisions: <text>` |

For copy-ready examples of every direct command, see [the command run examples](docs/commands.md#run-examples).

## Use

Open this repository as the legal/policy workspace. The source of truth is `AGENTS.md`; the adapters direct each harness to it. To reuse the pack elsewhere, copy the repository’s instruction and support files into the target repository root.

Generated work is stored in numbered, matter-based folders under [outputs/](outputs/README.md). Use `python3 scripts/new_output.py --help` to create the next auditable matter folder.

| Harness | File it reads | Included adapter |
|---|---|---|
| Codex / OpenCode / many AGENTS-compatible agents | `AGENTS.md` | `AGENTS.md` |
| Claude Code | `CLAUDE.md` | imports `AGENTS.md` |
| Cursor | `.cursor/rules/*.mdc` | `.cursor/rules/democratic-law.mdc` |
| Google Antigravity | `.agents/rules/*.md` | `.agents/rules/democratic-law.md` |
| Gemini CLI | `GEMINI.md` | `GEMINI.md` |
| GitHub Copilot | `.github/copilot-instructions.md` | included |
| Windsurf | `.windsurfrules` | included |

For systems without a listed convention, attach or paste `AGENTS.md` as the project/system instruction and make the `references/` directory available. The folders are intentionally self-contained so they can be copied into an existing repository without a runtime dependency.

For an Indian law, Bill, amendment, ordinance, or reform topic, `/janniti` starts with `/research-indian-law <topic>` before drafting or validation. It maps relevant Union and State/UT instruments, status, legislative history, delegated law, judicial treatment, and official sources.

## Contents

- `AGENTS.md` — canonical operating charter and required workflow.
- `references/review-checklist.md` — adversarial legal and democratic-integrity review.
- `references/legal-ethics.md` — non-negotiable independence, truthfulness, rights, and anti-corruption rules.
- `references/india-constitutional-research.md` — India-specific research and drafting module.
- `templates/` — constitutional-amendment and legal-framework review structures.

## Expert legal-review command

Use `/expert-legal-review <file, link, bill name, or question>` where the harness supports project commands. A portable command definition is at `commands/expert-legal-review.md`; native adapters are included for Claude Code (`.claude/commands/`) and OpenCode (`.opencode/commands/`). In other harnesses, paste the command file’s contents or ask the agent to apply it to the named material.

## Quality gates

- `/constitutional-stress-test <target>` tests a proposal against capture, emergency abuse, selective enforcement, media manipulation, and inaccessible remedies.
- `/verify-legal-citations <target>` verifies primary-source support, pinpoint, version, status, and subsequent history. For local Markdown preflight, run `python3 scripts/verify_legal_citations.py <file>`.
- `/draft-democratic-law <objective>` formulates a statute, rule, bill, amendment, or institutional framework and automatically applies both quality gates. For every new Bill or formal legislative measure, it automatically runs `/prepare-bill-for-introduction` to create a separate clean instrument for introduction and circulation; analysis, sources, options, and clause notes remain outside that file.
- `/prepare-bill-for-introduction <Bill>` runs automatically for each new Bill/formal instrument and can also be run manually to repair an existing generated Bill. It completes the applicable introduction/circulation package and returns either a clean introduction-ready file or a precise blocker list.
- `/validate-law <target>` validates a legal instrument, exposes exploitable loopholes, and returns a severity-ranked loophole-and-solution register with exact redlines.
- `/legislative-lint <target>` mechanically flags common drafting risks and turns them into contextual legal findings; `/build-legal-provenance <target>` creates a source-pinned claim ledger in the matter's `06-provenance/` folder.
- `/map-institutional-power <target>` maps appointments, budgets, directions, enforcement, adjudication, information, audit, and removal power to expose institutional capture and single points of failure.
- `/monitor-democratic-impact <target>` creates a post-enactment monitor for outcomes, rights, equality, complaints, audits, public reporting, review triggers, and correction or repeal.
- `/public-deliberation <target>` designs accessible, anti-capture public participation with transparent decision responses and remedies for sham consultation.
- `/public-legal-accessibility <target>`, `/expert-escalation <target>`, and `/score-democratic-quality <target>` add public accessibility, independent high-risk review, and explainable democratic-quality gating.
- `/monitor-legal-change <target>` preserves source versions, diffs legal change, and forces revalidation of dependent work.

## Preparing an existing Bill for introduction

JanNiti automatically runs `/prepare-bill-for-introduction` as the final stage for every new Bill or formal legislative instrument. Use `/prepare-bill-for-introduction <Bill file, matter folder, or pasted text>` manually when an already-generated Bill needs to become a formal circulation or introduction package. The command preserves the original Bill, applies current official format requirements for the target legislature, repairs the operative text, and keeps all explanations and sources in a separate filing record.

The completed matter contains a clean `introduction-ready-<instrument-name>.md` only when the formal-readiness gate passes. Otherwise it produces `not-ready-for-introduction.md` and names the outstanding fact, approval, format requirement, or legal defect. It never invents a sponsor, signature, presidential recommendation, certificate, financial determination, or legislative-secretariat acceptance.

Every instrument that passes the gate is automatically added to [the introduction-ready instrument registry](outputs/introduction-ready-registry.md), which links directly to its final Bill, law, amendment, rule, or regulation. The registry records JanNiti readiness only; it does not assert legislative acceptance or enactment. This README section is regenerated whenever an instrument is registered or the registry is reconciled.

<!-- BEGIN INTRODUCTION-READY REGISTRY -->

### Registered introduction-ready instruments

| Instrument | Type | Jurisdiction | Final file |
|---|---|---|---|
| Forest Protection, Anti-Mining, Public Official Deterrence, and Ecological Restoration Bill, 2026 | Bill | India | [001-forest-protection-and-mining-prohibition-bill/01-draft/introduction-ready-forest-protection-and-mining-prohibition-bill.md](outputs/001-forest-protection-and-mining-prohibition-bill/01-draft/introduction-ready-forest-protection-and-mining-prohibition-bill.md) |
| The Constitution (One Hundred and Thirty-Sixth Amendment) Bill, 2026 | Constitutional Amendment | India | [002-anti-defection-reform-and-electoral-integrity-bill/01-draft/introduction-ready-anti-defection-reform-bill.md](outputs/002-anti-defection-reform-and-electoral-integrity-bill/01-draft/introduction-ready-anti-defection-reform-bill.md) |
| The Constitution (One Hundred and Thirty-Seventh Amendment) Bill, 2026 | Constitutional Amendment | India | [003-election-commission-integrity-and-electoral-accountability-bill/01-draft/introduction-ready-election-commission-integrity-bill.md](outputs/003-election-commission-integrity-and-electoral-accountability-bill/01-draft/introduction-ready-election-commission-integrity-bill.md) |
| The Constitution (One Hundred and Thirty-Eighth Amendment) Bill, 2026 | Constitutional Amendment | India | [004-judicial-reform-social-representation-and-accountability-bill/01-draft/introduction-ready-judicial-reform-bill.md](outputs/004-judicial-reform-social-representation-and-accountability-bill/01-draft/introduction-ready-judicial-reform-bill.md) |
| Wealth Decentralization and Economic Concentration Reform Ideas | Bill | India | [005-wealth-decentralization-and-economic-concentration-reform-ideas/01-draft/introduction-ready-national-wealth-and-human-capital-decentralization-bill.md](outputs/005-wealth-decentralization-and-economic-concentration-reform-ideas/01-draft/introduction-ready-national-wealth-and-human-capital-decentralization-bill.md) |
| National Universal Free and Research Oriented Education Reform Bill | Bill | India | [006-national-universal-free-and-research-oriented-education-reform-bill/01-draft/introduction-ready-national-education-reform-bill.md](outputs/006-national-universal-free-and-research-oriented-education-reform-bill/01-draft/introduction-ready-national-education-reform-bill.md) |

<!-- END INTRODUCTION-READY REGISTRY -->

Use `/reconcile-introduction-ready-registry` to scan every matter, validate final-instrument candidates, add valid missing registry entries, and report blockers or stale links. For example: `/reconcile-introduction-ready-registry outputs/001-municipal-budget-bill`. See [the registry reconciliation runbook](docs/commands.md#reconciling-the-introduction-ready-registry).

Use `/reformat-introduction-ready-instrument <instrument>` to fix merged list items, indentation, or Markdown presentation in an existing clean Bill without changing its legal meaning. For example: `/reformat-introduction-ready-instrument outputs/001-municipal-budget-bill/01-draft/introduction-ready-municipal-budget-bill.md`.

## Governance and local research index

- [Governance Charter](governance/CHARTER.md) protects the repository’s democracy, equality, freedom, evidence, and integrity commitments from quiet dilution.
- [Maintenance protocol](governance/MAINTENANCE.md) establishes quarterly source and harness review.
- [Local authorised index](knowledge-base/local/README.md) provides a provenance-preserving, opt-in cache for documents the repository owner may lawfully retain.

## Verification suite

- [Acceptance suite](tests/acceptance/README.md) tests emergency powers, selective enforcement, media integrity, equality/public goods, constitutional amendments, and citation integrity across harnesses.
- Run `python3 scripts/validate_acceptance_suite.py` to validate the test pack.
- Run `python3 scripts/check_source_health.py --offline` to validate the official-source registry; use online mode only where network access is approved.
- [Cross-harness protocol](tests/harness/README.md), [compatibility matrix](tests/harness/compatibility-matrix.md), and [results template](tests/harness/results-template.md) provide repeatable live testing without fabricating external-harness results.

## Release kit

- [Release manifest](release/manifest.json) identifies version `0.1.0` and the required entrypoints/quality gates.
- [Release checklist](release/CHECKLIST.md) separates static readiness from required live harness testing.

## Starter prompts

- “Use JanNiti to review this bill for constitutional rights, democratic accountability, and enforceability. Cite primary law.”
- “Using the India module, formulate a constitutional amendment that limits emergency powers while preserving necessary disaster response.”
- “Redline this enforcement-agency statute to prevent selective prosecution and ensure independent oversight.”

## Harness notes

Cursor project rules are `.mdc` files in `.cursor/rules`; Claude Code supports importing `AGENTS.md` from `CLAUDE.md`; OpenCode supports `AGENTS.md`; and Antigravity uses `.agents/rules` (with legacy `.agent/rules` compatibility). Check the linked official documentation when a harness changes its configuration format.
