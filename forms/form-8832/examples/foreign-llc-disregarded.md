# Example: Foreign Eligible Entity Electing Disregarded for US Tax

A complete walkthrough of Form 8832 for a US person owning a foreign eligible entity (UK Private Limited Company, Ltd.) who wants disregarded-entity treatment for US tax purposes. This is the canonical "expat owner consolidates foreign passthrough" pattern.

## The filer

- **Entity**: Pennine Consulting Ltd., a UK private company limited by shares
- **Owner**: Sarah Chen (sole shareholder), US citizen residing in the UK on long-term assignment
- **Formation date**: 2024-09-15 (registered with UK Companies House)
- **Tax year**: Calendar year for US purposes; UK uses 5-April fiscal year — managed via Form 1118 / FTC mechanics outside this skill
- **Current classification for US tax**: Default association (C-corporation) under §301.7701-3(b)(2)(i)(B) — UK Ltd. has limited liability for all members, defaults to corporation
- **Reason for election**: Sarah is filing US returns as a US citizen on worldwide income. The UK Ltd. defaulted to C-corporation, which means CFC reporting (Form 5471), Subpart F / GILTI inclusions, and complex foreign tax credit mechanics. Disregarded treatment would let her report the UK consulting income directly on Schedule C, with foreign tax credits via Form 1116 — much simpler.
- **Desired effective date**: 2025-01-01 (start of the US tax year that the UK Ltd. would have been treated as a CFC; aim is to avoid CFC reporting from inception)

## Eligibility check (Step 1)

- Foreign eligible entity (UK Private Limited Company): need to confirm not on per-se list
- 26 CFR §301.7701-2(b)(8)(i) per-se list for United Kingdom: **Public Limited Company**. UK *private* limited company (Ltd.) is NOT on the per-se list.
- ✓ Eligible to elect.
- Sole shareholder (Sarah, 100%): single-owner → can elect Box 6(d) association or Box 6(f) disregarded
- Default classification: association (limited liability for all members per §301.7701-3(b)(2)(i)(B))
- Desired: disregarded → Box 6(f) foreign eligible electing disregarded
- No prior Form 8832 elections: ✓ initial classification election

## Effective-date calculation (Step 3)

- Filing date target: 2026-04-29 (today, mailing date)
- Earliest valid effective date without late relief: 2026-04-29 − 75 days = 2026-02-13
- Latest valid effective date: 2026-04-29 + 12 months = 2027-04-29
- Desired effective date: **2025-01-01** → falls **outside** the 75-day-back window
- Late relief required: ✓ Part II under Rev. Proc. 2009-41

## Rev. Proc. 2009-41 eligibility (Step 5)

Walk the four requirements:

1. **Failure to obtain desired classification solely because Form 8832 was not timely filed**: ✓ Sarah did not realize the UK Ltd. defaulted to corporation for US purposes; she intended pass-through treatment from formation.
2. **Return-consistency test**:
   - 2024 return: filed 2025-04 with the UK Ltd. NOT included on Form 5471 (Sarah didn't know it should have been)
   - 2025 return: filed 2026-04 with consulting income reported on Schedule C (consistent with disregarded treatment)
   - This is a **mixed** consistency picture — the 2024 omission is technically inconsistent (no Form 5471 filed for what was a CFC under default classification)
   - Sarah will need to amend 2024 to either (a) include Form 5471 for 2024 (consistent with the prior default classification, then have the election effective 2025-01-01 going forward) or (b) treat 2024 consistently with the requested 2025-01-01 effective date — meaning no Form 5471 needed because the election is requested effective the start of 2025
3. **Reasonable cause**: ✓ Sarah, as a US citizen residing abroad and owning a foreign entity, was unfamiliar with the federal entity classification election requirement until consulting a US-international CPA in 2026
4. **Three years and 75 days from requested effective date**: 2025-01-01 + 3 years + 75 days = 2028-03-17. Today (2026-04-29) is well within. ✓

Decision: Sarah's CPA confirms the cleanest approach is **request effective date 2025-01-01**. The 2024 default-classification year stands on its own (no amendment needed because the election does not change 2024 retroactively). Sarah will need to file Form 5471 for the 2024 short period as a CFC of a US person — this is independent of Form 8832.

For 2025 and beyond, the disregarded treatment means: UK consulting income on Schedule C, UK Ltd. invisible for US income tax, FTC for UK taxes via Form 1116 on Sarah's 1040.

## §301.7701-3(g) deemed-transaction analysis

The conversion from association to disregarded under §301.7701-3(g)(1)(iii) is treated as if the corporation distributes all assets and liabilities to its single shareholder in complete liquidation.

UK Ltd. balance sheet on 2025-01-01 (per UK accounts):

| Asset | Tax basis (US$) | FMV (US$) |
|-------|------------------|-----------|
| Cash and bank accounts | $32,000 | $32,000 |
| Accounts receivable | $14,000 | $14,000 |
| Computer equipment | $4,500 | $3,500 |
| Liabilities | ($8,000) | ($8,000) |
| **Net** | **$42,500** | **$41,500** |

§331 / §332 analysis:

- Sarah's basis in the UK Ltd. stock (her capital contributions plus retained earnings inside the entity through 2024): approximately $40,000 per her records
- §332 (tax-free liquidation of subsidiary into parent corporation) does not apply — Sarah is an individual, not a corporate parent
- §331 (taxable distribution in complete liquidation) applies: Sarah recognizes gain or loss = (FMV of distributed property − basis in stock)
- Calculation: ($41,500 net assets distributed) − ($40,000 stock basis) = **$1,500 capital gain**
- Holding period of stock (held since 2024-09-15): >1 year → long-term capital gain
- The corporation recognizes gain or loss as if it sold the assets at FMV: small loss on equipment ($3,500 FMV − $4,500 basis = −$1,000)

CPA recommendation: yes, before filing. Specific items:

- Confirm stock basis of $40,000 (capital contributions + earnings & profits accumulated through 2024)
- §367(b) outbound foreign liquidation rules — when a CFC liquidates into a US individual shareholder, §367(b) may require the US shareholder to include the all earnings and profits amount as a deemed dividend
- Subpart F / GILTI inclusions for 2024 (the year the entity defaulted as a CFC) — separately required regardless of the 2025 election
- UK tax consequences of the deemed liquidation: HMRC does not recognize the §301.7701-3(g) deemed transaction; UK tax treatment is unchanged. Sarah may have a US-UK timing mismatch.

## The completed Form 8832 draft

```markdown
# Form 8832 — DRAFT for Pennine Consulting Ltd.

## Filing summary
- Entity name: Pennine Consulting Ltd.
- EIN: 98-7654321 (obtained Dec 2025)
- Election type: Initial classification (Box 1(a))
- Current classification: Default association (foreign limited-liability)
- Elected classification: Disregarded entity
- Effective date: 01/01/2025 (LATE — Part II completed)
- Filing channel: USPS Certified Mail to Kansas City service center
  (foreign principal place of business → Kansas City, MO 64999)
- Late relief requested: Yes (Rev. Proc. 2009-41)

## Header
Name of eligible entity: Pennine Consulting Ltd.
EIN: 98-7654321
Address: 14 Kingsmead Park, Manchester, M3 5BL, United Kingdom
Address change: ☐ (not checked)

[At top of form, write: "FILED PURSUANT TO REV. PROC. 2009-41"]

## Part I — Election Information
1. Type of election:                      ☒ (a) Initial classification
2a. Prior election within last 60 months: ☐ Yes  ☒ No
2b. Was prior election the first?         (skipped)
3. More than one owner:                   ☐ Yes  ☒ No
4. (Single individual owner)
   Name: Sarah Chen
   ID number: ***-**-**** (SSN, redacted)
5. (Parent corporation)                   N/A
6. Type of entity:
   ☐ (a) Domestic eligible — elect association
   ☐ (b) Domestic eligible — elect partnership
   ☐ (c) Domestic eligible — elect disregarded
   ☐ (d) Foreign eligible — elect association
   ☐ (e) Foreign eligible — elect partnership
   ☒ (f) Foreign eligible — elect disregarded
7. (Foreign) Country of organization:     United Kingdom
8. Election effective date:               01/01/2025
9. Contact person: Sarah Chen
   Phone: +44-7700-900142
10. ☐ (Not checked)
11. Consent Statement and Signatures
    [Sarah Chen, sole shareholder, signs here]
    [Print name: Sarah Chen]
    [Title: Sole Shareholder]
    [Date: 04/29/2026]

## Part II — Late Election Relief

Line 11 (Part II) — Reasonable-cause statement:
[Attached as separate signed statement, summarized:
 "Sarah Chen, a US citizen residing in the United Kingdom, formed Pennine
  Consulting Ltd. on 09/15/2024 to conduct her consulting business. At
  formation, she was unfamiliar with the US federal entity classification
  election requirement and was not advised of it by her UK accountant or
  US tax preparer at that time. She intended pass-through tax treatment
  for US purposes from the entity's first day of operations. She first
  learned of Form 8832 on 03/14/2026 when she engaged a US-international
  CPA, [Name], to review her cross-border tax position. She acted promptly
  to file this Form 8832 within 47 days of discovery."]

Line 12 (Part II) — Statement of consistent returns:
[Attached as separate signed declaration:
 "Pennine Consulting Ltd. has filed no federal tax or information returns
  for the period from the requested effective date (01/01/2025) through
  the date of this filing. Sarah Chen has filed her individual Form 1040
  for tax year 2025, with the UK consulting income reported on Schedule C,
  consistent with the disregarded-entity classification requested herein.
  No inconsistent returns have been filed by or with respect to the
  entity for any year covered by this election. Signed under penalties
  of perjury, Sarah Chen, 04/29/2026."]

## Required attachments
- [x] Sole shareholder signature (Line 11) — collected 04/29/2026
- [x] Part II reasonable-cause statement
- [x] Part II consistent-returns declaration
- [x] Form 5471 separately filed for 2024 (independent obligation; not part
       of Form 8832 packet but acknowledged in working papers)
- [ ] Officer/manager authority — not applicable (sole shareholder signs)

## Validation summary
- Eligibility: pass (UK Ltd. NOT on per-se list; eligible foreign entity)
- Effective-date window: 01/01/2025 outside 75-day window → Part II completed
- Rev. Proc. 2009-41 eligibility: pass (within 3 years 75 days, no
  inconsistent returns, reasonable cause documented)
- 60-month rule: not applicable (initial classification, no prior election)
- Consents: complete (sole shareholder)
- Sanity warnings:
  - §301.7701-3(g) deemed liquidation: ~$1,500 capital gain to Sarah,
    review with CPA
  - §367(b) outbound liquidation rules: deemed-dividend inclusion of all
    earnings and profits accumulated through 2024-12-31
  - 2024 Form 5471 still required for the year the entity was classified
    as a CFC (before this election's effective date)
  - UK-US timing mismatch: HMRC does not recognize §301.7701-3(g) deemed
    transactions; track separately
  - State conformity: Sarah's US state of domicile (assume California)
    may not conform to federal disregarded election for foreign entities;
    confirm with California FTB

## Filing instructions
Mail to:
  Department of the Treasury
  Internal Revenue Service Center
  Kansas City, MO 64999
  (Foreign principal place of business → Kansas City)

At top of Form 8832: "FILED PURSUANT TO REV. PROC. 2009-41"

Method: USPS Certified Mail with Return Receipt (international mail from UK)
        OR private delivery service per IRC §7502(f) for faster delivery
Postmark deadline: As soon as practicable; latest 03/17/2028 (3 years and
                    75 days from 01/01/2025 effective date)

Expected IRS acknowledgment: 60-90 days for late-relief filings (longer than
                              typical 60 days because Part II review)

## Next steps after IRS acceptance
- File Form 5471 for tax year 2024 (independent CFC obligation; severe
  penalties for non-filing — $10,000 per return per year under §6038(b))
- For 2025 forward: report UK consulting income on Schedule C of Form 1040
- Foreign tax credit on UK income tax via Form 1116
- Discontinue Form 5471 obligations from 2025-01-01 (entity is disregarded
  for US purposes)
- Maintain UK Companies House filings (UK tax treatment unchanged)
- Track UK-US timing differences in working papers
- Confirm California (or other state) disregarded conformity

## Sources cited in this draft
- IRS Form 8832 (Rev. December 2013)
- 26 CFR §301.7701-2(b)(8) (foreign per-se list — UK Public Limited
  Company is per-se; UK *private* Limited Company is NOT)
- 26 CFR §301.7701-3(b)(2)(i)(B) (foreign default classification:
  association if all members have limited liability)
- 26 CFR §301.7701-3(g)(1)(iii) (deemed liquidation on association →
  disregarded transition)
- IRC §331 (taxable distribution in complete liquidation)
- IRC §367(b) (outbound foreign liquidation gain recognition)
- IRC §6038(b) (Form 5471 penalties for CFC non-filing)
- Rev. Proc. 2009-41 §4 (late entity classification election relief)
```

## Why each non-obvious choice

**Why Box 6(f) and not 6(d)?** UK Ltd. defaults to association under §301.7701-3(b)(2)(i)(B) (limited liability for all members). Box 6(d) "elect association" would be a no-op. Box 6(f) "elect disregarded" is the actual change Sarah wants.

**Why request 2025-01-01 effective date and not 2024-09-15 (formation date)?** Going back to formation would require amending 2024 — which would mean rescinding the Form 5471 already filed for 2024 and asserting that the entity was disregarded from day one. Sarah's CPA judges this is messier than a clean break: keep 2024 as a CFC year (Form 5471 stands), elect disregarded as of 2025-01-01. The request still requires Part II late relief because 2025-01-01 is well beyond the 75-day window from the 2026-04-29 filing date.

**Why does the 2024 inconsistency NOT defeat Rev. Proc. 2009-41 relief?** The "consistent returns" requirement applies to **affected years** — years from the requested effective date forward. 2024 is before the requested 2025-01-01 effective date and is not "affected" by the election. The 2024 default classification stands; Sarah's 2024 Form 5471 obligation is independent.

**Why mail to Kansas City when the entity is in the UK?** Per Form 8832 "Where to File" instructions: foreign principal place of business → Kansas City service center. Ogden does not handle foreign-PPB filings.

**What if Sarah sells the UK Ltd. to a non-US buyer?** Disregarded treatment means the UK Ltd. is invisible for US tax — Sarah is treated as selling the underlying assets directly. Asset-sale tax treatment applies (different from stock sale). Counsel should advise on character of gain (capital vs. ordinary), §1245 / §1250 recapture if any, and whether §367(b) ramifications recur.

**What if Sarah moves back to the US?** Disregarded treatment continues; the Schedule C reporting just becomes simpler (no foreign tax credit needed for non-UK income). The §301.7701-3(g) deemed liquidation is a one-time event tied to the 2025-01-01 effective date, not an ongoing analysis.

**Why is §367(b) flagged?** §367(b)(2) requires a US shareholder of a foreign corporation undergoing a §332 / §351 / §361 transaction to include in income certain amounts attributable to E&P. The §301.7701-3(g) deemed liquidation triggers this analysis. The all-E&P inclusion can be material if the UK Ltd. accumulated significant earnings through 2024 — it can also reset basis and create FTC opportunities. CPA review essential.
