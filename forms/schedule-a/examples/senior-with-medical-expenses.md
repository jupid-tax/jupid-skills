# Example: Senior with Medical Expenses (Retired, High Out-of-Pocket Medical)

A complete walkthrough of Schedule A for a retired senior couple with significant medical expenses (surgery, ongoing therapy, long-term care insurance), modest mortgage, and small charitable contributions. The medical deduction (which most filers can't claim because the 7.5% AGI floor wipes them out) is the key driver here.

This is the canonical "retiree itemizer" pattern — common in years with major medical events. Math checked in python: taxable social security with the Form 1040 instructions' Social Security Benefits Worksheet method, 2025 MFJ brackets (Rev. Proc. 2024-40 §2.01, Tax Table midpoint), and the 2025 standard deduction.

## The filers

- **Names**: Margaret and Robert Chen
- **Filing status**: Married Filing Jointly
- **State**: Arizona (no state income tax on Social Security benefits; AZ does tax non-SS pension/IRA income)
- **Tax year**: 2025 (filing in 2026)
- **AGI** (Form 1040 line 11b): $92,325
  - Robert: Social Security $24,000 + IRA distribution $30,000 (of which $5,000 is a QCD, so $25,000 taxable) + W-2 wages from part-time work $8,000
  - Margaret: Social Security $19,000 + pension $20,000 (fully taxable) + interest/dividends $4,000
  - Income other than social security: $25,000 + $8,000 + $20,000 + $4,000 = $57,000
  - Taxable social security (MFJ worksheet): provisional income $57,000 + ½ × $43,000 = $78,500; 85% × ($78,500 − $44,000) + $6,000 = $35,325 (less than 85% of benefits, $36,550)
  - AGI = $57,000 + $35,325 = **$92,325**
- **MAGI** (SALT phase-down): $92,325
- **Ages**: Robert 72, Margaret 68; both have SSNs valid for employment
- **Standard deduction MFJ 2025**: $31,500 + age-65+ additions

### Standard deduction with age add-ons

Robert is 72, Margaret is 68. Both qualify for the age-65+ addition.

Standard deduction = $31,500 (base MFJ) + $1,600 (Robert 65+) + $1,600 (Margaret 65+) = **$34,700** (Rev. Proc. 2024-40 §2.15(3) for the $1,600).

Separately, both qualify for the $6,000 enhanced deduction for seniors on Schedule 1-A (born before January 2, 1961; MAGI under $150,000; joint return; valid SSNs), $12,000 in total on Form 1040 line 13b. It applies whether they itemize or not, so it doesn't change the comparison below.

## Inputs gathered

### Medical (Lines 1-4)

This was a difficult year medically. Robert had hip-replacement surgery in March; ongoing physical therapy through October. Margaret has a chronic condition requiring monthly specialist visits and medications.

| Item | Amount |
|------|--------|
| Robert's hip replacement (out-of-pocket after Medicare + supplement) | $7,800 |
| Robert's physical therapy (out-of-pocket portion) | $2,400 |
| Margaret's specialist visits and copays | $1,800 |
| Prescription medications (both) | $4,200 |
| Dental work (Margaret crown + cleanings; Robert cleanings) | $3,400 |
| Vision (eyeglasses for both, exams) | $1,100 |
| Long-term care insurance premiums (Margaret, age 68 → cap $4,810) | $4,810 |
| Long-term care insurance premiums (Robert, age 72 → cap $6,020) | $6,020 |
| Hearing aids (Robert) | $5,500 |
| Medicare Part B premiums (both, deducted from SS; $185.00/month 2025 standard premium × 12 × 2, matching the SSA-1099s) | $4,440 |
| Medicare Part D premiums (both) | $720 |
| Medicare supplement (Medigap) premiums | $4,800 |
| Medical mileage (240 miles × 21¢) | $50 |
| **Total Line 1** | **$47,040** |

7.5% × $92,325 = $6,924 floor.

Line 4 = max(0, $47,040 − $6,924) = **$40,116**.

The 7.5% floor wipes out roughly $7K, but the bulk of the medical spending deducts.

### SALT (Lines 5-7)

Arizona has a state income tax on non-SS retirement income (Social Security is exempt from AZ state tax).

| Item | Amount |
|------|--------|
| Arizona state income tax (W-2 box 17 from Robert's part-time + estimates on pension/IRA income) | $2,800 |
| Real estate (property) tax on their home | $3,200 |
| Personal property tax | $0 |
| **Sum Line 5d** | **$6,000** |

SALT cap = $40,000; well below cap. Line 5e = $6,000.

Line 7 = $6,000.

### Mortgage interest (Lines 8-10)

| Item | Amount |
|------|--------|
| Form 1098 box 1 (interest paid) | $4,200 |
| Form 1098 box 6 (points) | $0 |
| Form 1098 box 5 (PMI) | $0 |
| Loan origination date | 2014-09-10 (pre-12/15/2017, $1M cap grandfathered) |
| Loan current balance Jan 1, 2025 | $145,000 |

Loan is well within both caps. Full $4,200 deducts on Line 8a.

### Charity (Lines 11-14)

| Item | Amount |
|------|--------|
| Cash gifts to church | $2,400 |
| Non-cash to local thrift store (clothing, household goods, books) | $400 |
| QCD from Robert's IRA to a wildlife charity | $5,000 |

**Important: the $5,000 QCD does NOT go on Schedule A.** It's excluded from Robert's gross income: Form 1040 line 4a shows $30,000, line 4b shows $25,000 taxable, and the "QCD" box on line 4c is checked (2025 Form 1040). The QCD bypasses Schedule A entirely.

Schedule A entries:
| Line | Amount |
|------|--------|
| Line 11 (cash to church) | $2,400 |
| Line 12 (non-cash to thrift store; under $500, no Form 8283 needed) | $400 |
| Line 13 (carryover) | $0 |
| **Raw total Line 14** | **$2,800** |

For 2025, no 0.5% AGI floor applies — full $2,800 deducts.

### Casualty (Line 15)

None.

### Other (Line 16)

None.

## The completed Schedule A draft

```markdown
# Schedule A — DRAFT for tax year 2025

## Filing context
Filing status: Married Filing Jointly
Both spouses age 65+ (Robert 72, Margaret 68)
AGI (Form 1040 line 11b): $92,325
MAGI: $92,325
Standard deduction: $31,500 base + $1,600 (Robert) + $1,600 (Margaret) = $34,700
SALT cap applicable: $40,000 (no phase-down; MAGI < $500,000)
Federal marginal bracket: 12%

Note: $5,000 QCD from Robert's IRA NOT on Schedule A — excluded from income on Form 1040 lines 4a/4b (QCD box on line 4c)

## Lines 1-4 — Medical and Dental
1. Medical and dental expenses:        $47,040
   (Hip surgery $7,800; PT $2,400; specialist $1,800; prescriptions $4,200;
    dental $3,400; vision $1,100; LTC insurance $4,810 + $6,020 within age caps;
    hearing aids $5,500; Medicare B $4,440; Medicare D $720; Medigap $4,800;
    medical mileage $50)
2. AGI:                                $92,325
3. 7.5% × AGI:                          $6,924
4. Deductible medical (Line 1 − Line 3, ≥ 0): $40,116

## Lines 5-7 — Taxes
5a. State income tax (AZ; W-2 + estimates): $2,800
5b. Real estate taxes:                   $3,200
5c. Personal property taxes:                 $0
5d. Sum 5a+5b+5c:                        $6,000
5e. SALT capped (smaller of 5d or $40K cap): $6,000
6.  Other taxes:                             $0
7.  Total taxes:                         $6,000

## Lines 8-10 — Interest
8a. Mortgage interest (Form 1098):       $4,200
8b. Mortgage interest not on 1098:           $0
8c. Points not on 1098:                      $0
8d. Reserved for future use (2025 form)       —
8e. Sum 8a-8c:                           $4,200
9.  Investment interest:                     $0
10. Total interest:                      $4,200

## Lines 11-14 — Charity
11. Cash contributions (church):         $2,400
12. Non-cash contributions (thrift store):  $400
13. Carryover from prior year:               $0
14. Total charitable:                    $2,800
    Raw total: $2,800
    0.5% AGI floor (2026+ only): N/A for 2025
    Effective Line 14: $2,800
    (Note: $5,000 QCD excluded from income on 1040 lines 4a/4b, not on Schedule A)

## Line 15 — Casualty and theft
15. Casualty/theft (Form 4684):              $0

## Line 16 — Other
16. Other itemized deductions:               $0

## Line 17 — Total itemized deductions
17. Total: Sum Lines 4+7+10+14+15+16:   $53,116  (→ Form 1040 line 12e)
18. Elect to itemize although less than standard: ☐ (not needed)

## Standard-vs-itemized comparison
Itemized (Line 17):           $53,116
Standard deduction (with age add-ons): $34,700
Recommendation: ITEMIZE
Difference: $18,416 of additional deduction

Federal tax savings at 12% bracket: ~$2,210
(Taxable income: $92,325 − $53,116 − $12,000 Schedule 1-A senior deduction = $27,209; 2025 Tax Table tax $2,790)

## Required attachments
- [ ] Form 8283 — NOT required (Line 12 = $400 < $500 threshold)
- [ ] Form 4684 — NOT required (Line 15 = $0)
- [ ] Form 4952 — NOT required (Line 9 = $0)
- [ ] Long-term care insurance premium statements — retain for substantiation
- [ ] SSA-1099 for Medicare Part B premiums deducted from SS — retain
- [ ] Hospital and pharmacy out-of-pocket records — retain
- [ ] Church giving records — a contemporaneous written acknowledgment is needed for any single gift of $250 or more (separate gifts aren't combined); bank records for the rest — retain
- [ ] QCD records (charity acknowledgment that it received the IRA-direct-transfer) — retain to support the Form 1040 line 4b exclusion

## Validation summary
- Math: all checks passed
- Sanity:
  - Line 17 ($53,116) > standard deduction ($34,700) ✓
  - LTC premiums within age-based caps (Margaret $4,810 cap at age 68; Robert $6,020 cap at age 72) ✓
  - Medicare Part B premiums included on Line 1 (deducted from SS, but premium is medical) ✓
  - QCD correctly NOT on Schedule A ✓
  - No mortgage insurance claimed (not deductible for 2025) ✓
  - Charity gifts non-cash < $500 → no Form 8283 needed ✓
- Next steps: Schedule A attaches to Form 1040; Line 17 flows to 1040 line 12e; Schedule 1-A senior deduction on line 13b

## Sources cited in this draft
- IRS Form 1040 Schedule A (2025 revision)
- IRC §213 (medical and dental, 7.5% AGI floor)
- IRC §164 (SALT)
- IRC §163(h) (mortgage interest)
- IRC §170 (charitable contributions)
- IRC §408(d)(8) (QCDs from IRAs, $108,000 annual limit per person for 2025)
- Rev. Proc. 2024-40 §2.28 and the 2025 Schedule A instructions (LTC insurance premium age caps for 2025)
- CMS 2025 Medicare Part B fact sheet ($185.00 standard monthly premium)
- Pub 502, 526, 590-A/B, 936
```

## Strategic observations for this filer

### 1. Major medical years are when retirees itemize

Most years, Margaret and Robert would take the standard deduction (with age add-ons, $34,700). Their normal SALT + mortgage + charity totals roughly $13,000 — well below $34,700.

But in 2025, Robert's hip surgery plus ongoing high prescription/Medicare costs pushed medical to $47,040. Even after the $6,924 floor, $40,116 of medical deducts. That alone (with no other Schedule A items) would beat the standard deduction.

The lesson for retirees: track medical out-of-pocket carefully every year. In a major medical year, itemizing wins. In normal years, standard deduction.

### 2. QCD beats itemized charity for retirees

Robert's $5,000 QCD is more tax-efficient than donating $5,000 cash and itemizing it:

**If the $5,000 had been taken as a taxable IRA distribution and given in cash (Line 11)**:
- Taxable IRA distribution rises by $5,000, which also makes $1,225 more social security taxable (it hits the 85%-of-benefits ceiling: $36,550)
- AGI: $98,550 (instead of $92,325); medical floor $7,391 (instead of $6,924)
- Line 17: $40,116 − $467 + $6,000 + $4,200 + $7,800 = $57,649
- Taxable income: $98,550 − $57,649 − $12,000 = $28,901; 2025 Tax Table tax $2,994

**With the QCD (as filed)**:
- Taxable income $27,209; tax $2,790

The QCD saves about $204 of federal tax here, because the extra $5,000 of income would also have pulled more social security into income and raised the medical floor, while the $5,000 charitable deduction only offsets the IRA income itself. Lower AGI can also matter for Medicare IRMAA tiers in later years.

For retirees age 70½+ with charitable giving plans, compare a QCD with itemized giving. QCDs are limited to $108,000 per person for 2025 (Notice 2024-80) and $111,000 for 2026 (Notice 2025-67).

### 3. Long-term care insurance premiums are within age caps

The age-based caps for LTC insurance premiums (for 2025, per Rev. Proc. 2024-40 §2.28 and the 2025 Schedule A instructions):

| Age at year-end | 2025 cap |
|------------------|----------|
| 40 or under | $480 |
| 41-50 | $900 |
| 51-60 | $1,800 |
| 61-70 | $4,810 |
| 71+ | $6,020 |

Margaret (age 68): premium $4,810 = exactly at cap. Fully deductible.
Robert (age 72): premium $6,020 = exactly at cap. Fully deductible.

If their premiums were higher (e.g., $7,000 each on a richer policy), only the cap amount would be deductible.

### 4. Medicare premiums deducted from Social Security count as medical

Medicare Part B premiums deducted directly from Robert's and Margaret's Social Security checks are still medical expenses on Line 1. The SSA-1099 lists them in the description of the box 3 amount.

This is often overlooked. For a couple paying $4,440 of combined Medicare Part B premiums plus $720 of Part D plus $4,800 of Medigap, that's $9,960 of medical premiums included on Line 1 — meaningful for the medical deduction.

### 5. State tax treatment of itemized differs

State rules for itemizing differ and are not covered by this skill. Check the Arizona Form 140 instructions for whether and how itemized deductions apply, and don't assume they mirror the federal Schedule A.

For this couple the federal benefit (about $2,210 at 12%) is the primary driver.

## Filing channel

Margaret and Robert use a CPA who specializes in retiree returns. The CPA will:

1. Receive their SSA-1099s, 1099-Rs (IRA, pension), 1099-INT/DIV, W-2 (Robert's part-time), Form 1098, year-end DAF/charity statements, and detailed medical receipt log
2. Compute AGI on Form 1040 (with QCD reducing IRA distribution income) and the Schedule 1-A senior deduction
3. Run Schedule A
4. Verify state itemized return matches
5. E-file federal and state returns

If using FFFF instead, follow `filing.md` Section 1. The Schedule A is moderate complexity but feasible — care needed to handle the QCD outside Schedule A and the Medicare premium calculation.

## Records to retain

- SSA-1099 (3 years)
- Form 1099-R for IRA distribution showing the QCD direct-transfer (3 years)
- Charity acknowledgment for QCD recipient (kept indefinitely as evidence of QCD validity)
- Medical receipts and EOBs (3 years; longer for major procedures with ongoing implications)
- LTC insurance premium statements (3 years)
- Form 1098 (3 years)
- Hearing aid receipt and prescription record (3 years)

## Common variations to watch for

- **QCD limit hit**: Robert's QCD limit for 2025 is $108,000 per person. He used $5,000; plenty of room.
- **Major dental work**: implants, full-mouth restoration — large medical years
- **Long-term care services (not insurance)**: if Margaret needed in-home care, fees for qualified long-term care services (chronic illness certified by physician) are medical expenses without the LTC age caps
- **Casualty loss in federally declared disaster**: would add to Line 15 (2026+: also State declared disasters)
- **Margaret's pension split as non-taxable basis recovery**: AGI computation adjusts; doesn't change Schedule A directly
- **Medicare IRMAA**: high-AGI retirees face higher Medicare premiums; QCD can drop them under IRMAA tiers, indirectly saving thousands
