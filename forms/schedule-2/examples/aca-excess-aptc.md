# Example: Marketplace Enrollee with Excess APTC Repayment

A complete walkthrough of Schedule 2 for a freelance writer who enrolled in marketplace coverage based on a low-income estimate, then earned more than expected (Q4 contract surge), creating excess advance premium tax credit (APTC) that must be repaid on Schedule 2 Line 1a.

## The filer

- **Name**: Marcus Reilly
- **Filing status**: Single
- **Occupation**: Freelance writer
- **Tax year**: 2025 (filing in 2026)
- **Coverage**: Self-only marketplace plan, full year, with APTC

## Inputs gathered

### Income reality vs. estimate

When Marcus enrolled in the marketplace in November 2024, he estimated 2025 income of **$32,000**. Based on that estimate, the marketplace computed APTC of **$420/month** ($5,040/year) which paid the insurer directly.

Marcus's actual 2025 income (Schedule C net profit + small interest income):

- Schedule C gross receipts: $66,400
- Schedule C expenses: $14,200
- Schedule C net profit: **$52,200**
- Bank interest: $180
- AGI = $52,200 + $180 − half-of-SE-tax adjustment ($3,688) = **$48,692**
- MAGI for PTC = AGI + tax-exempt interest + non-taxable SS = $48,692 (no adjustments needed)

### FPL situation

Marcus is a household of 1. For 2025 returns, the IRS uses 2024 HHS poverty guidelines. 2024 FPL for household of 1 (lower 48): **$15,060**.

- 100% FPL: $15,060
- 200% FPL: $30,120
- 300% FPL: $45,180
- 400% FPL: $60,240

Marcus's MAGI of $48,692 is **323% of FPL** ($48,692 / $15,060 = 3.2332; Worksheet 2 of the Form 8962 instructions drops the decimals).

### Form 1095-A data

Form 1095-A from the marketplace shows for each month:

- Column A — Monthly enrollment premiums: $618
- Column B — Monthly second lowest cost silver plan (SLCSP): $585
- Column C — Monthly APTC: $420

For all 12 months: Total enrollment $7,416 / Total SLCSP $7,020 / Total APTC $5,040.

### Form 8962 computation (annual method)

Marcus's income did not change mid-year and his household size stayed at 1 — annual method is appropriate.

**Step 1 — Applicable figure** (Form 8962 Line 7):

For 2025, IRC §36B(b)(3)(A) applicable percentages by household income as % of FPL:

| % of FPL | Applicable figure |
|----------|-------------------|
| < 150% | 0.00 |
| 150% – 200% | sliding 0.00 to 0.02 |
| 200% – 250% | sliding 0.02 to 0.04 |
| 250% – 300% | sliding 0.04 to 0.06 |
| 300% – 400% | sliding 0.06 to 0.085 |
| ≥ 400% | 0.085 (under IRA extension through 2025) |

Marcus at 323% FPL → applicable figure from Table 2 of the 2025 Form 8962 instructions = **0.0658** (do not interpolate; read the table).

**Note on 2026**: the applicable percentage table is set in IRC §36B(b)(3)(A) but was modified by ARPA / IRA through 2025. The IRS Premium Tax Credit Q&A (Q7, updated Feb. 19, 2026) describes the above-400% expansion as covering 2021–2025 only, so the 400% limit applies again for 2026 unless later legislation changes it; re-check before a 2026 computation. Separately, P.L. 119-21 removed the repayment cap for tax years after 2025 (Q31).

**Step 2 — Annual contribution amount** (Form 8962 Line 8a):

$48,692 × 0.0658 = **$3,204**

**Step 3 — Annual maximum premium assistance** (Form 8962 Line 11d):

Annual SLCSP $7,020 − Annual contribution $3,204 = **$3,816**

But the credit cannot exceed the actual premiums paid. Annual enrollment premium $7,416 > $3,816, so PTC = $3,816.

**Step 4 — Reconcile** (Form 8962 Line 24 vs. Line 25):

- Line 24: Total PTC = $3,816
- Line 25: Total APTC paid = $5,040
- Line 27: Excess APTC = $5,040 − $3,816 = **$1,224**

**Step 5 — Repayment limitation** (Form 8962 Line 28, Table 5 of the 2025 Form 8962 instructions):

For 2025 (Table 5, single filers):

| % FPL | Limit (single) |
|-------|----------------|
| < 200% | $375 |
| 200% – 300% | $975 |
| 300% – 400% | $1,625 |
| ≥ 400% | no limit |

Marcus at 323% FPL → repayment cap = **$1,625**.

**Step 6 — Repayment due** (Form 8962 Line 29):

Lesser of excess ($1,224) or cap ($1,625) = **$1,224**.

→ **Schedule 2 Line 1a = $1,224**

(Note: Marcus's full $1,224 excess is below the cap, so the cap doesn't bite. If his income had been higher and the excess larger, the cap would have limited the repayment. For a 2026 return there is no cap at all: P.L. 119-21; IRS Premium Tax Credit Q&A, Q31.)

### Other Schedule 2 lines

- No AMT (modest income, no preference items): Line 2 = $0
- SE tax on Schedule C profit: Schedule SE Line 12 = $7,376 (detail below)
- No tip / misclassified wage / household employee / 4255 / 965 / 8611 / 17x items: Lines 5, 6, 8, 9, 13, 14, 15, 16, 17, 19, 20 = $0; Line 10 is reserved
- Additional Medicare Tax: SE earnings = $52,200 × 0.9235 = $48,207 < $200,000 threshold → Line 11 = $0
- NIIT: MAGI $48,692 < $200,000 threshold → Line 12 = $0

## Schedule SE detail (used for Line 4)

- Net SE earnings: $52,200 × 0.9235 = $48,207
- SS portion: 12.4% × min($48,207, $176,100) = $5,978
- Medicare portion: 2.9% × $48,207 = $1,398
- Total SE tax: $5,978 + $1,398 = **$7,376**

→ **Schedule 2 Line 4 = $7,376**

Half of SE tax = $3,688 deducts on Schedule 1 Line 15.

## The completed Schedule 2 draft

```markdown
# Schedule 2 (Form 1040) — DRAFT for tax year 2025

## Header
Name(s) shown on Form 1040: Marcus Reilly
Your social security number: XXX-XX-XXXX

## Part I — Tax
 1a. Excess advance premium tax credit repayment.
     Attach Form 8962:                                    $1,224
 1b–1y. Other additions to tax:                           $0
 1z. Add lines 1a through 1y:                             $1,224
 2.  Alternative minimum tax. Attach Form 6251:           $0
 3.  Add lines 1z and 2. Enter here and on Form 1040,
     1040-SR, or 1040-NR, line 17:                        $1,224

## Part II — Other Taxes
 4.  Self-employment tax. Attach Schedule SE:             $7,376
 5.  SS/Medicare on unreported tips. Form 4137:           $0
 6.  Uncollected SS/Medicare on wages. Form 8919:         $0
 7.  Total of lines 5 and 6:                              $0
 8.  Additional tax on IRAs. Form 5329 if required:       $0
 9.  Household employment taxes. Schedule H:              $0
10.  Reserved for future use:                             —
11.  Additional Medicare Tax. Form 8959:                  $0
12.  Net investment income tax. Form 8960:                $0
13.  Uncollected SS/Medicare tax on tips or GTL:          $0
14.  Interest on installment income (residential lots
     and timeshares):                                     $0
15.  Interest on deferred tax on installment sales
     > $150,000:                                          $0
16.  Recapture of low-income housing credit:              $0
17.  Other additional taxes:                              $0
18.  Total additional taxes (17a–17z):                    $0
19.  Recapture of net EPE from Form 4255:                 $0
20.  Section 965 installment from Form 965-A:             $0
21.  Add lines 4, 7 through 16, 18, and 19. Enter here
     and on Form 1040 or 1040-SR, line 23:                $7,376

## Form 1040 routing
Form 1040 Line 17 (from Schedule 2 Line 3):               $1,224
Form 1040 Line 23 (from Schedule 2 Line 21):              $7,376

## Required upstream forms attached
- [x] Form 8962 (Line 1a = $1,224 from Form 8962 Line 29)
- [x] Schedule SE (Line 4 = $7,376 from Schedule SE Line 12)
- [x] Form 1095-A retained in records

## Validation summary
- Math:
  - Line 1z = $1,224; Line 3 = $1,224 + $0 = $1,224 ✓
  - Line 21 = $7,376 + $0 + $0 + $0 + $0 + $0 + $0 + $0 + $0 + $0 + $0 + $0 + $0 = $7,376 ✓
- Cross-form: Form 8962 attached, 1095-A in records, Schedule SE attached
- Sanity:
  - Excess APTC ($1,224) < repayment cap ($1,625 for 323% FPL single) — cap doesn't apply
  - Form 8962 Line 26 (net PTC) = $0; Form 8962 Line 29 (excess APTC) = $1,224 (mutual exclusion confirmed)
  - SE tax $7,376 on $48,207 net SE earnings = 15.3% effective (under SS wage base, full both portions) ✓
  - MAGI $48,692 well below $200K NIIT and Additional Medicare Tax thresholds ✓

## Sources cited in this draft
- IRS Form 1040 Schedule 2, Rev. 2025
- IRS Form 8962, Rev. 2025
- IRS Instructions for Form 8962 (2025): Table 1-1 (FPL), Table 2 (applicable figure), Table 5 (repayment limitation)
- IRC §36B (PTC); §36B(b)(3)(A) (applicable percentage table); §36B(f)(2)(B) (repayment limitation)
- IRC §1401 (SE tax)
- HHS 2024 Poverty Guidelines (used for 2025-tax-year PTC calculations)
- SSA Fact Sheet (2025 SS wage base $176,100)
- Schedule SE Instructions (i1040sse), 2025 revision
- Form 8962 Instructions (i8962), 2025 revision
```

## Why each non-obvious choice

**Why annual method, not monthly?** Marcus's household size and coverage didn't change all year. Annual is simpler and produces the same result. Monthly is required only if family size, marital status, eligibility for marketplace coverage, or applicable SLCSP changed during the year (e.g., divorce mid-year, job change mid-year that ended marketplace coverage).

**Why use 2024 FPL on a 2025 return?** Per IRC §36B(d)(3)(C), PTC uses the FPL in effect on **the first day of the open enrollment period for the year**. For 2025 plan year (open enrollment Nov 2024), the relevant FPL is the 2024 HHS guidelines. Same pattern next year: 2026 returns use 2025 FPL.

**Why isn't Marcus eligible for additional PTC (Schedule 3 Line 9)?** Because his actual entitled PTC ($3,816) is *less* than the APTC he received ($5,040). When entitled < received, the result is a repayment (Line 29), not a refundable credit. He can never have both a Line 26 and a Line 29 on the same return.

**Why didn't the repayment cap save Marcus more?** The cap protects filers whose excess APTC exceeds the cap. Marcus's excess ($1,224) is already below the cap ($1,625 for 323% FPL single), so the cap is non-binding. If Marcus's actual income had been $80,000 (531% FPL), the cap would not have applied at all (no cap above 400% FPL pre-IRA; under IRA modifications through 2025, no cliff but applicable percentage caps at 8.5%) — and the repayment could have been larger.

**What about the ARPA suspension of excess APTC repayment?** It applied to tax year 2020 only and does not apply to 2025. Repayment is fully required for 2025 returns subject to the Table 5 cap, and for 2026 returns without any cap (IRS Premium Tax Credit Q&A, Q30–Q31).

**Why is excess APTC repayment on Schedule 2 (a tax) rather than Schedule 3 (a credit reduction)?** The IRS treats excess APTC repayment as an additional tax, not a reduction of the original credit, because the APTC was paid to the insurer in real time. The reconciliation creates a tax liability that increases income tax owed. The mirror — refundable PTC — is a tax credit that reduces tax (Schedule 3).

## What if Marcus were audited?

His audit defense would be:

1. Form 1095-A from the marketplace showing actual APTC paid month-by-month
2. Form 8962 worksheet with FPL calculation and applicable figure interpolation
3. Schedule C documentation supporting the $52,200 net profit
4. Schedule SE supporting the SE tax
5. Bank statements showing the marketplace insurer received the APTC payments
6. Table 5 of the 2025 Form 8962 instructions for the repayment cap
