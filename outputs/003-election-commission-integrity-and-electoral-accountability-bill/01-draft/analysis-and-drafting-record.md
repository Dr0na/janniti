# Analysis and Drafting Record: Election Commission Integrity, Voter Protection, and Electoral Accountability Bill, 2026

## 1. Filing Target and Legislative Authority

- **Target Legislature**: Parliament of India (Lok Sabha / Rajya Sabha).
- **Competence**: Article 368 of the Constitution of India (Constitutional Amendment requiring 2/3rd majority in Parliament + ratification by 50%+ State Assemblies under Article 368(2) Proviso), Schedule VII List I Entry 72, amending Articles 324, 325, 326, 368, RPA 1950, RPA 1951, and repealing Act 49 of 2023.
- **Year**: 2026 (Seventy-Seventh Year of the Republic of India).

---

## 2. Problem, Evidence, and Existing-Law Map

Existing Indian legal frameworks governing election administration face critical vulnerabilities:
- **Executive Selection Panel Dominance (2023 Act)**: The 2023 Act replaced the CJI with a Cabinet Minister on the Selection Committee, giving the ruling government a 2:1 majority (*Anoop Baranwal* 2023 SC).
- **Intra-Commission Vulnerability**: Article 324(5) protects only the CEC from executive removal, leaving ECs vulnerable to executive pressure.
- **Mass Voter Roll Deletions**: RPA 1950 lacks mandatory prior notice or judicial appeal before deleting voters, enabling systemic exclusion.
- **Lack of 100% Physical Audit**: Current rules permit sample counting of VVPAT slips (5 polling stations per segment), leaving 95%+ of polling stations without physical paper audit (*ADR v. ECI* 2024 SC).

---

## 3. Core Legal Reform Refinements

1. **Independent Selection Panel (PM, LOP, CJI)**: Re-establishes the 3-member Selection Committee in Article 324(2) requiring 2/3rd consensus and public candidate shortlists.
2. **Equal Constitutional Security for ECs**: Amends Article 324(5) to grant Election Commissioners the exact same impeachment protection as the CEC.
3. **Voter Roll Integrity & Anti-Exclusion Penalties**: Mandates 30-day registered written notice before voter deletion. Arbitrary voter deletion carries **7 to 14 years rigorous imprisonment** for complicit election officers.
4. **Voting System Integrity & 100% Paper Audit**: Mandates 100% VVPAT paper slip counting and paper ballot voting options. Physical paper slip count overrides EVM count in case of discrepancy.
5. **Retrospective Criminal Accountability**: Preserves forensic investigation and prosecution for past electoral fraud under PCA 1988 and RPA 1951.
6. **Supermajority Entrenchment**: Entrenches election laws under Article 368 requiring 2/3rd total parliamentary seats (calculated without deducting suspended MPs) + 2/3rd State Assemblies ratification.

---

## 4. Quality Gate and Verification Summary

- **Legislative Linting (`lint_legislation.py`)**: Verified penalty clauses, non-obstante clauses, and entrenchment language.
- **Legal Claim Provenance (`validate_claim_provenance.py`)**: Claims verified against primary constitutional and Supreme Court authorities (*Anoop Baranwal*, *Subramanian Swamy*, *ADR v. ECI*).
- **Institutional Power Map (`analyze_power_map.py`)**: Checked relationships between Selection Committee, ECI, Special Courts, Supreme Court, and Voters; no circularity or unchecked power concentration found.
- **Democratic Quality Scorecard (`validate_democratic_scorecard.py`)**: Passed on all 8 dimensions (Rights, Equality, Accountability, Power Concentration, Transparency, Enforceability, Accessibility, Public Participation).
