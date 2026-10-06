# Example — Offshore Trust Distribution (Default Method, Throwback)

End-to-end Form 3520 for a US beneficiary receiving a distribution from
a foreign non-grantor trust that does NOT provide a Beneficiary
Statement. Part III: Schedule A (default calculation), Form 4970 as a
worksheet, and Schedule C (interest charge). Form 3520 (Rev. December
2023). Math: /tmp/jupid-skills-work/calc/g4-3520-offshore.py.

## Filer profile

- **Name**: Sarah Patel (US citizen)
- **SSN**: 345-67-8901 (illustrative)
- **Address**: 1840 Madison Avenue, New York, NY 10029
- **Filing status**: Single
- **Tax year**: 2026 (calendar year)

## Background

Sarah is the US-citizen beneficiary of a Cayman Islands trust established
in 2015 by her late father (UK citizen, never a US resident). The trust:

- Was established in Cayman Islands under Cayman law
- Has discretionary distribution provisions (trustees decide who gets
  what, when)
- Has Sarah's siblings (UK and Singapore residents) and Sarah herself as
  beneficiaries
- Is administered by Cayman Trust Company Ltd.
- Has accumulated approximately $4,200,000 of undistributed income since
  2015 (per the trust's available accounting)

Sarah has been a beneficiary since 2015. She received NO distributions
prior to 2024.

## §679 status — N/A

Sarah's father set up the trust; he was not a US person. §679 applies
only when a **US person** transfers property to a foreign trust that has
a US beneficiary. Sarah did not transfer property to this trust; her
father did, and he was not a US person.

Therefore Sarah is NOT a US owner of this trust. The trust is a **foreign
non-grantor trust** as to Sarah. She has no Part II obligation, only
Part III when she receives a distribution.

## Distribution history

- 2023: $0 received from trust
- 2024: $40,000 cash distribution from trust to Sarah
- 2025: $80,000 cash distribution
- 2026: **$500,000 cash distribution** received on August 30, 2026

Sarah filed Form 3520 Part III for 2024 ($40,000) and 2025 ($80,000).
The trust did not provide a Beneficiary Statement in those years either.

For 2024 and 2025 her preparer used Schedule A (default calculation).
Under the consistency rule she must keep using Schedule A for this trust
in later years anyway (Instructions for Form 3520, Schedule A).

The 2026 $500,000 is a different scale and the default method math gets
ugly.

## Beneficiary Statement availability

Sarah has asked Cayman Trust Company Ltd. for a Foreign Nongrantor Trust
Beneficiary Statement for 2026. The trustee responded that they do not
prepare such statements and that doing so would "violate the trust's
confidentiality obligations under Cayman law."

Sarah has no practical way to compel a Beneficiary Statement, so she
uses the default method (and the instructions say trust provisions that
prevent disclosure are not reasonable cause).

## Default calculation — Part III, Schedule A (lines 31–38)

| Line | Computation | Amount |
|------|-------------|--------|
| 31 | Line 27: $500,000 cash received 08/30/2026 (USD wire; no conversion) | $500,000 |
| 32 | Years the trust has been a foreign trust, 2015–2026 inclusive | 12 |
| 33 | Distributions in the 3 preceding years: $0 (2023) + $40,000 (2024) + $80,000 (2025) | $120,000 |
| 34 | $120,000 × 1.25 | $150,000 |
| 35 | $150,000 ÷ 3.0 | $50,000 |
| 36 | Smaller of line 31 or line 35 — ordinary income earned in 2026 | $50,000 |
| 37 | $500,000 − $50,000 — accumulation distribution | $450,000 |
| 38 | 12 ÷ 2.0 — applicable number of years | 6.0 |

The $50,000 on line 36 is ordinary income on Sarah's 2026 Form 1040.

## Form 4970 worksheet (tax on the accumulation distribution)

The agent asked Sarah for her taxable income for the 5 preceding years:
2021 $96,400; 2022 $104,800; 2023 $111,250; 2024 $187,300; 2025
$123,600 (single each year). The trust paid no tax (line 4 = $0), and
none of the income was accumulated before she reached 21 (line 2 = $0).
For Form 4970 lines 8 and 11 (number of years), the preparer uses the
line 38 applicable number of years, 6 — an assumption, because neither
instruction states which number to use for a default-method foreign
distribution.

| Form 4970 line | Computation | Amount |
|----------------|-------------|--------|
| 1, 3, 5, 7 | Accumulation distribution (Form 3520 line 48) | $450,000 |
| 8, 11 | Number of years (assumption above) | 6 |
| 9, 12 | $450,000 ÷ 6 | $75,000 |
| 10 | $75,000 × 25% | $18,750 |
| 13 | Taxable income 2021–2025 | see above |
| 14 | Drop highest (2024) and lowest (2021): 2022, 2023, 2025 | $104,800 / $111,250 / $123,600 |
| 16 | Add $75,000 to each | $179,800 / $186,250 / $198,600 |
| 17 | Tax on line 16 (2022, 2023, 2025 single rate schedules) | $37,767.50 / $38,432 / $40,615 |
| 18 | Tax on line 14 | $18,987.50 / $20,100 / $22,511 |
| 19–23 | Additional tax (no credit or AMT changes) | $18,780 / $18,332 / $18,104 |
| 24 | Sum | $55,216 |
| 25 | ÷ 3.0 | $18,405.33 |
| 26 | × 6 years | $110,431.98 |
| 28 | Less line 4 ($0) — partial tax | $110,431.98 |

Rate schedules: 2022 Rev. Proc. 2021-45 Table 3; 2023 Rev. Proc. 2022-38
Table 3; 2025 Rev. Proc. 2024-40 Table 3.

## Interest charge — Part III, Schedule C (lines 48–53)

| Line | Computation | Amount |
|------|-------------|--------|
| 48 | From line 37 | $450,000 |
| 49 | Form 4970 line 28 | $110,432 |
| 50 | Line 38, rounded to the nearest half year | 6.0 |
| 51 | Combined interest rate for 6.0 years from the IRS.gov/CombinedInterestRate table for 2026 calendar-year filers (June 30, 2026 applicable date) | look up when posted |
| 52 | Line 49 × line 51 | — |
| 53 | Line 49 + line 52 → additional tax on Form 1040 Schedule 2 | — |

On 2026-10-06 the newest posted table is for 2024 calendar-year filers
(6.0 years: 0.3876). For scale only: at that rate, line 52 would be
$110,432 × 0.3876 = $42,803 and line 53 $153,235 (30.6% of the
distribution, on top of the regular tax on the $50,000 line 36 amount).
Do not file with the 2024 rate; use the 2026 table or compute the rate as
the line 51 instructions describe.

If Sarah had obtained a Beneficiary Statement, the actual calculation
(Schedule B) would have split the distribution by character, but the
consistency rule would still have required Schedule A because she used it
in 2024 and 2025.

## Filled draft

```markdown
# Form 3520 (Rev. December 2023) — DRAFT for tax year 2026

## Page 1
A. Initial / Final / Amended: none (3rd Form 3520 for this trust; first was 2024)
B. Filer type: Individual
C. Counted on Form 8938: No
Trigger box checked: Part III (distribution from a foreign trust)
1a. Name: Sarah Patel     1b. TIN: 345-67-8901
1c, 1e–1h. Address: 1840 Madison Avenue, New York, NY 10029, United States
1i–1k: not checked
2a. Foreign trust: [Father's name] Family Settlement   2b. EIN: none
2c, 2e–2h. c/o Cayman Trust Company Ltd., P.O. Box XXXX, Grand Cayman KY1-XXXX, Cayman Islands
2d. Date created: 2015 (exact date from the trust deed)
3. U.S. agent: No

## Part III — Distributions
24. | (a) 08/30/2026 | (b) Cash (USD wire) | (c) $500,000 | (d) none | (e) $0 | (f) $500,000 |
25. Loans / uncompensated use: No
27. Total distributions: $500,000
28. Trust holds Sarah's qualified obligation: No
29. Foreign Grantor Trust Beneficiary Statement: N/A (nongrantor trust)
30. Foreign Nongrantor Trust Beneficiary Statement: No

Schedule A: 31 $500,000 | 32 12 | 33 $120,000 | 34 $150,000 | 35 $50,000 | 36 $50,000 | 37 $450,000 | 38 6.0
Schedule C: 48 $450,000 | 49 $110,432 (Form 4970 line 28) | 50 6.0 | 51 <2026 table> | 52 <49 × 51> | 53 <49 + 52>

## Currency translation
Wire received in USD; no conversion needed

## Required attachments
- [x] Form 4970 worksheet (attached to Form 3520, not filed separately)
- [x] Explanation of the 12 years on line 32 (trust deed date, 2015)
- [ ] Correspondence with Cayman Trust Company Ltd. requesting a
      Beneficiary Statement (kept with the file)

## Mailing address (for Form 3520)
Internal Revenue Service Center
P.O. Box 409101
Ogden, UT 84409

## Validation summary
- Math (python): 33 = $0 + $40,000 + $80,000 = $120,000 ✓; 34 = $150,000 ✓;
  35 = $50,000 ✓; 36 = $50,000 ✓; 37 = $450,000 ✓; 38 = 6.0 ✓
- Math: Form 4970 line 28 = $110,431.98 (3-of-5 years, 6 years) ✓
- Sanity: consistency rule — Schedule A used in 2024–2025, so Schedule A again ✓
- Sanity: line 51 must come from the 2026 table (not yet posted) — open item
- Sanity: Form 4970 line 8/11 number of years is an assumption — confirm with the preparer
- Cross-form: line 36 $50,000 as ordinary income on Form 1040; line 53 on
  Schedule 2 (Form 1040), Part II, "any other taxes" line
- Next steps:
  1. Sarah signs Form 3520
  2. Mail Form 3520 to Ogden by April 15, 2027 (or October 15, 2027 if
     Form 4868 is filed and line 1k checked)
  3. File Form 1040 with the line 36 income and the line 53 additional tax
  4. For 2027 onward: keep asking the trustee for a Beneficiary Statement;
     engage an international tax practitioner

## Sources cited in this draft
- IRS Form 3520 (Rev. December 2023) and Instructions (Rev. December 2025), Part III Schedules A and C
- IRS Form 4970 (2025) and its instructions ("Foreign trust beneficiaries")
- IRS combined interest rate tables: https://www.irs.gov/CombinedInterestRate
- IRC §665, §667, §668; IRC §6048(c); IRC §6677
- Rev. Proc. 2021-45, 2022-38, 2024-40 (single rate schedules)
```

## Why this case is painful

- Only $50,000 of the $500,000 counts as current income; the rest is an
  accumulation distribution
- Sarah has no leverage with the Cayman trustee
- The accumulation distribution generally loses its character (Form 4970
  instructions), and the interest charge is based on 6.0 applicable years
- The consistency rule keeps her on Schedule A for this trust

## Mitigation strategies (out of scope for this skill, redirect to a CPA)

- Negotiate with the trustee for a Beneficiary Statement (sometimes
  successful when escalated to senior trust officers or via legal
  counsel)
- Request a US tax accounting reconstruction from the trustee — even
  partial accountings can support an actual-method position
- Consider whether the trust could be restructured (e.g., decanted into
  a new trust with a cooperative US-aware trustee) — this is a
  practitioner-level project
- For Sarah personally: under the default method, distributions up to
  125% of the prior 3-year average are current income rather than
  accumulation distributions, so the timing and size of distributions
  matter; that planning belongs to a practitioner

## What would simplify this case

- A Beneficiary Statement → actual method in later years only if Schedule
  A had never been used (here, only in the termination year)
- A trustee willing to provide a Foreign Nongrantor Trust Beneficiary
  Statement with the contents listed in Notice 97-34 and the Form 3520
  line 30 instructions (Form 3520-A does not apply to a nongrantor trust
  with no U.S. owner)
- Sarah being a UK or Singapore tax resident instead of US — the entire
  problem disappears outside the US tax net
