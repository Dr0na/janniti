# Paper-Ballot Transition — Validation Record

## Conclusion

**Robust with conditions.** Bill sections 5 and 19 provide a complete high-level route to replace EVM voting and electronic tabulation with paper ballots.[^bill] They materially reduce electronic-system dependence, but create distinct risks of ballot theft, intimidation, invalid-ballot disputes, manual-count error, delayed declaration, disability exclusion and local capture. The safeguards in the Bill address those risks at the statutory level; operational proof and exact rule redlining are still required.

This record does not find that recent EVM manipulation has occurred. The [2024 Supreme Court EVM/VVPAT judgment](https://api.sci.gov.in/supremecourt/2023/10857/10857_2023_2_1501_52646_Judgement_26-Apr-2024.pdf) is relevant primary authority but does not establish that allegation. The paper-ballot transition is treated as a democratic policy choice.

## Current-law and authority record

[^bill]: Internal draft-text reference: `01-draft/not-ready-electoral-democracy-code-bill.md`, version reviewed on 2026-08-11. It is not an external legal authority.

| Authority | Verified relevance | Limitation |
|---|---|---|
| [Representation of the People Act, 1951](https://www.indiacode.nic.in/handle/123456789/2096), s. 61A | Current statutory voting-machine anchor identified for proposed omission. | Exact current wording and every consequential provision remain to be redlined. |
| [Conduct of Elections Rules, 1961](https://www.eci.gov.in/eci-backend/public/api/download?url=LMAhAK6sOPBp%2FNFF0iRfXbEB1EVSLT41NNLRjYNJJP1KivrUxbfqkDatmHy12e%2FzVx8fLfn2ReU7TfrqYobgIvstmQD30kwAPe7FGqLCeBup9Eoxop8TtDc7nr4HrKkXI9Gx%2FzxZtEA0vUPWCQcGHJEPJeGpdyep95JWeuP0brIxP6zeSSVyt7XOHtRZoM8E5IRjQCzojthRKfpJsRg9Wg%3D%3D) | Current delegated-law framework for voting and counting procedures. | Exact rule/form/notification crosswalk remains incomplete. |
| [*ADR v ECI*, 2024 INSC 341](https://api.sci.gov.in/supremecourt/2023/10857/10857_2023_2_1501_52646_Judgement_26-Apr-2024.pdf) | Official judicial treatment of EVM/VVPAT challenges and verification safeguards. | The record before the Court is not a current universal technical assessment. |

## Loophole and solution register

| [ID](https://www.indiacode.nic.in/handle/123456789/2096) | Severity | Exploitation path | Bill safeguard | Remaining implementation proof |
|---|---|---|---|---|
| PB-01 | High | Ballot stuffing, theft or substitution in transit. | Section 5(3)–(5): published custody protocol, seals, reconciliation, observer access, preservation and court remedy.[^bill] | State/UT-specific transport, storage, video, staff and chain-of-custody plan. |
| PB-02 | High | Local intimidation compromises a voter’s choice or an assisted voter’s privacy. | Section 5(2): accessible independent marking; section 5(3): equal observation; sections 8 and 17: anti-retaliation protections.[^bill] | Disability protocol, polling-station layout, training and enforcement plan. |
| PB-03 | High | Manual count is selectively slowed, miscounted or concealed. | Section 5(4): count every valid ballot, reconciliation, candidate-wise publication, reasons for rejection and recount decision.[^bill] | National counting standard, staffing model and time simulation. |
| PB-04 | Medium | A party uses mass recount demands to prevent timely result declaration. | Section 5(5): reasoned recount/scrutiny decision and election-petition remedy.[^bill] | Objective recount threshold, queueing standard and fast court/tribunal process. |
| PB-05 | Medium | Disabled, low-literacy or language-minority voters are excluded. | Section 5(2), (6) and (7): tactile guides, accessible ballots, chosen assistance, equality assessment and review.[^bill] | Usability testing in every official language and disability-access category. |
| PB-06 | Medium | Executive delays the rules so EVM use continues indefinitely. | Section 19(2)–(4): 180-day rule deadline and fixed 365-day statutory transition date.[^bill] | Gazette and rule-laying tracking; remedial route if the deadline is missed. |

## Conditions before introduction

1. Build a verified provision-by-provision amendment and repeal schedule for [section 61A](https://www.indiacode.nic.in/handle/123456789/2096), the 1961 Rules, forms, manuals, procurement rules and record-retention rules.
2. Obtain an independent public technical, accessibility, fiscal, environmental and workforce assessment comparing paper ballots with the current system.
3. Test the system in urban, remote, conflict-affected, multilingual and disability-access contexts without delaying the statutory transition through a discretionary certification gate.
4. Provide public legal aid, election-agent training, polling-officer training, secure storage capacity and expedited recount/election-petition support.
5. Complete public consultation and independent qualified legal review.
