# Official Primary-Source Retrieval Jobs — 18 August 2026

**Use:** retrieve one item at a time from the stated official route; confirm that the downloaded bytes are the expected official document before running `scripts/snapshot_legal_source.py`. A response that is HTML, an access page, a compendium, an index, a draft, or an unofficial reproduction fails the job.

| Job | Official route | Expected source | Acceptance scope | Target route |
|---|---|---|---|---|
| FSS-01 | <https://fssai.gov.in/cms/food-safety-and-standards-regulations.php> | Original Gazette text and amendment list for Packaging Regulations, 2018. | Base regulation and each amendment separately. | FSS Packaging plastic schedule. |
| FSS-02 | <https://egazette.gov.in/WriteReadData/2025/262130.pdf> | Packaging First Amendment Regulations, 2025. | Already accepted; recheck only if changed. | FSS Packaging plastic schedule. |
| FSS-03 | <https://fssai.gov.in/cms/Amendment-FSS-Packaging.php> | Each Packaging amendment and any direction/guideline to be relied on. | Each final, in-force original notification only. | FSS Packaging plastic schedule. |
| FSS-04 | <https://fssai.gov.in/cms/amendments-fss-licensing-registration.php> | Licensing and Registration Regulations, 2011 and complete amendment history. | Base regulation and every final amendment separately. | Licensing/hygiene/expiry schedule. |
| FSS-05 | <https://egazette.gov.in/WriteReadData/2026/273797.pdf> | Licensing and Registration Second Amendment Regulations, 2026. | Already accepted; recheck only if changed. | Licensing/hygiene/expiry schedule. |
| FSS-06 | <https://fssai.gov.in/cms/food-safety-and-standards-regulations.php> | Labelling and Display Regulations, 2020; Advertising and Claims Regulations, 2018; all amendments. | Every final Gazette notification, not a compendium. | Labelling/advertising/claims schedule. |
| FSS-07 | <https://www.fssai.gov.in/upload/notifications/2025/08/689d8d163d422coffee%20chicory_gazette.pdf> | Labelling and Display First Amendment Regulations, 2025. | Final Gazette PDF; the prior attempt returned HTML and must be retried through a verifiable official route. | Labelling/advertising/claims schedule. |
| FSS-08 | <https://www.fssai.gov.in/upload/notifications/2026/04/69cca2b3f3ce9Notification%20dt%2024.03.2026_NRC.pdf> | Labelling and Display First Amendment Regulations, 2026. | Final Gazette PDF; the prior attempt returned HTML and must be retried through a verifiable official route. | Labelling/advertising/claims schedule. |
| CON-01 | <https://consumeraffairs.nic.in/acts-and-rules/consumer-protection/consumer-protection> | Consumer Protection Act, 2019; E-Commerce Rules, 2020; corrigendum; 2021 amendment; any material CCPA instrument. | Each downloadable official attachment and commencement record. | Consumer food-delivery rule. |
| LM-01 | <https://consumeraffairs.nic.in/sites/default/files/file-uploads/latestnews/LM_PCR_All_Amendements.pdf> | Legal Metrology (Packaged Commodities) Rules, 2011 consolidated official publication. | Verify whether it is a controlling official consolidation; otherwise acquire original Gazettes for every amendment. | Legal Metrology declaration rule. |
| DPDP-01 | <https://www.indiacode.nic.in/indiacode/handle/123456789/22037?view_type=browse> | DPDP Act, 2023 and linked Rules/notifications. | Act, Rules and each commencement notification separately. | Privacy/kitchen-view schedule. |
| DPDP-02 | <https://egazette.gov.in/WriteReadData/2025/267647.pdf> | G.S.R. 843(E), 13 November 2025. | Already accepted; recheck only if changed. | Privacy/kitchen-view schedule. |
| ENV-01 | <https://www.indiacode.nic.in/handle/123456789/18574> | Environment (Protection) Act, 1986 and linked instruments. | Act and controlling Rules separately. | Environment/waste schedule. |
| ENV-02 | <https://upload.indiacode.nic.in/showfile?actid=AC_RJ_83_1096_00001_00001_1563872109827&filename=plastic_waste_management_rules%2C_2016.pdf&type=rule> | Plastic Waste Management Rules, 2016 base text. | Base Rules plus every final amendment separately. | Environment/waste schedule. |
| ENV-03 | <https://egazette.gov.in/writeReadData/2026/271465.pdf> | Plastic Waste Management (Amendment) Rules, 2026. | Already accepted; recheck only if changed. | Environment/waste schedule. |
| STATE-01 | `knowledge-base/state-ut-source-verification-queue.json` | State/UT legislature, law department, Gazette and High Court routes for every adoption jurisdiction. | Matter-specific instrument, version, Gazette/commencement and relevant decision. | Model State/UT/local package. |

## Snapshot command pattern

After verifying a downloaded local file is the intended official source, use:

```text
python3 scripts/snapshot_legal_source.py <source-id> <authorised-local-file> --url <direct-official-url> --publisher <official-publisher> --output-dir outputs/035-food-health-and-product-integrity-code-consolidation/14-legal-change-monitoring/snapshots
```

Then record the identity, status, pinpoint, language/completeness, hash, impact and designated-human acceptance in the matter’s source-acceptance decision. Never accept a retrieved source automatically.
