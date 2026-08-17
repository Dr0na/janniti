# Food Integrity Legal-Change Monitoring Routine

## Sources

Monitor India Code and Gazette for the FSS Act, BNS, BNSS, Consumer Protection, Legal Metrology, DPDP and Environment Acts; FSSAI regulations; e-Gazette rules; State/UT sources listed in `knowledge-base/state-ut-source-registry.json`; and official Supreme Court/High Court decisions.

## Event workflow

1. Retrieve only from authorised official routes and make a hash-pinned snapshot.
2. Record identity, version/stage, publication/commencement, pinpoint, hash, limitation and affected package file.
3. Create a redline and impact assessment; never silently replace an authority.
4. Mark `pending_human_review`; a designated reviewer accepts/rejects under `governance/SOURCE-ACCEPTANCE.md`.
5. On acceptance, update schedules, provenance, lint, citation verification, power map and dashboard documentation.

Critical events—repeal, commencement, court stay/invalidity, new criminal/emergency power, material data-rights change or recall rule—pause affected claims and prompt immediate review. Material events are updated within ten working days; routine events are logged monthly.
