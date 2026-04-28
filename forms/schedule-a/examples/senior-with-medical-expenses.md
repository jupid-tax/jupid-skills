# Example: Senior with Medical Expenses (Retired, High Out-of-Pocket Medical)

A complete walkthrough of Schedule A for a retired senior couple with significant medical expenses (surgery, ongoing therapy, long-term care insurance), modest mortgage, and small charitable contributions. The medical deduction (which most filers can't claim because the 7.5% AGI floor wipes them out) is the key driver here.

This is the canonical "retiree itemizer" pattern — common in years with major medical events.

## The filers

- **Names**: Margaret and Robert Chen
- **Filing status**: Married Filing Jointly
- **State**: Arizona (no state income tax on Social Security benefits; AZ does tax non-SS pension/IRA income)
- **Tax year**: 2025 (filing in 2026)
- **AGI** (Form 1040 Line 11): $85,000
  - Robert: Social Security $24,000 (85% taxable = $20,400) + IRA RMD $30,000 + small W-2 from part-time consulting $8,000
  - Margaret: Social Security $19,000 (85% taxable = $16,150) + pension $20,000 + interest/dividends $4,000
  - Joint AGI = $20,400 + $30,000 + $8,000 + $16,150 + $20,000 + $4,000 + tax-deferred QCD adjustments ≈ $85,000 (numbers approximate; exact AGI computation runs through Form 1040 Lines 1-11)
- **MAGI**: $85,000
- **Ages**: Robert 72, Margaret 68
- **Standard deduction MFJ 2025**: $30,000 + age-65+ additions

### Standard deduction with age add-ons

Robert is 72, Margaret is 68. Both qualify for the age-65+ addition.

Standard deduction = $30,000 (base MFJ) + $1,550 (Robert 65+) + $1,550 (Margaret 65+) = **$33,100**.

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
| Medicare Part B premiums (both, deducted from SS) | $3,710 ($183.40/mo × 12 × 2 ≈ $4,400; verify exact) — using $3,710 actual from SSA-1099 |
| Medicare Part D premiums (both) | $720 |
| Medicare supplement (Medigap) premiums | $4,800 |
| Medical mileage (240 miles × 21¢) | $50 |
| **Total Line 1** | **$46,310** |

7.5% × $85,000 = $6,375 floor.

Line 4 = max(0, $46,310 − $6,375) = **$39,935**.

The 7.5% floor wipes out roughly $6K, but the bulk of the medical spending deducts.

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

**Important: the $5,000 QCD does NOT go on Schedule A.** It's excluded from Robert's gross income on Form 1040 Line 4b (already reflected in the $30,000 IRA distribution being only $25,000 taxable). The QCD bypasses Schedule A entirely.

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
AGI (Form 1040 Line 11): $85,000
MAGI: $85,000
Standard deduction: $30,000 base + $1,550 (Robert) + $1,550 (Margaret) = $33,100
SALT cap applicable: $40,000 (no phaseout; MAGI < $500,000)
Federal marginal bracket: 12%

Note: $5,000 QCD from Robert's IRA NOT on Schedule A — excluded from income at Form 1040 Line 4b

## Lines 1-4 — Medical and Dental
1. Medical and dental expenses:        $46,310
   (Hip surgery $7,800; PT $2,400; specialist $1,800; prescriptions $4,200;
    dental $3,400; vision $1,100; LTC insurance $4,810 + $6,020 within age caps;
    hearing aids $5,500; Medicare B $3,710; Medicare D $720; Medigap $4,800;
    medical mileage $50)
2. AGI:                                $85,000
3. 7.5% × AGI:                          $6,375
4. Deductible medical (Line 1 − Line 3, ≥ 0): $39,935

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
8d. Mortgage insurance premiums:             $0  (not available 2025)
8e. Sum 8a-8d:                           $4,200
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
    (Note: $5,000 QCD excluded from income on 1040 Line 4b, not on Schedule A)

## Line 15 — Casualty and theft
15. Casualty/theft (Form 4684):              $0

## Line 16 — Other
16. Other itemized deductions:               $0

## Line 17 — Total itemized deductions
17. Total: Sum Lines 4+7+10+14+15+16:   $52,935

## Standard-vs-itemized comparison
Itemized (Line 17):           $52,935
Standard deduction (with age add-ons): $33,100
Recommendation: ITEMIZE
Difference: $19,835 of additional deduction

Federal tax savings at 12% bracket: ~$2,380

## Required attachments
- [ ] Form 8283 — NOT required (Line 12 = $400 < $500 threshold)
- [ ] Form 4684 — NOT required (Line 15 = $0)
- [ ] Form 4952 — NOT required (Line 9 = $0)
- [ ] Long-term care insurance premium statements — retain for substantiation
- [ ] SSA-1099 for Medicare Part B premiums deducted from SS — retain
- [ ] Hospital and pharmacy out-of-pocket records — retain
- [ ] Church year-end giving statement (CWA — gifts ≥ $250 in aggregate received) — retain
- [ ] QCD records (charity acknowledgment that it received the IRA-direct-transfer) — retain to support the Form 1040 Line 4b exclusion

## Validation summary
- Math: all checks passed
- Sanity:
  - Line 17 ($52,935) > standard deduction ($33,100) ✓
  - LTC premiums within age-based caps (Margaret $4,810 cap at age 68; Robert $6,020 cap at age 72) ✓
  - Medicare Part B premiums included on Line 1 (deducted from SS, but premium is medical) ✓
  - QCD correctly NOT on Schedule A ✓
  - Line 8d = 0 (correct for 2025) ✓
  - Charity gifts non-cash < $500 → no Form 8283 needed ✓
- Next steps: Schedule A attaches to Form 1040; Line 17 flows to 1040 Line 12

## Sources cited in this draft
- IRS Form 1040 Schedule A (2025 revision)
- IRC §213 (medical and dental, 7.5% AGI floor)
- IRC §164 (SALT)
- IRC §163(h) (mortgage interest)
- IRC §170 (charitable contributions)
- IRC §408(d)(8) (QCDs from IRAs, $108,000 annual limit per person for 2025)
- Rev. Proc. 2024-40 §3.27 (LTC insurance premium age caps for 2025)
- Pub 502, 526, 590-A/B, 936
```

## Strategic observations for this filer

### 1. Major medical years are when retirees itemize

Most years, Margaret and Robert would take the standard deduction (with age add-ons, $33,100). Their normal SALT + mortgage + charity totals roughly $13,000 — well below $33,100.

But in 2025, Robert's hip surgery plus ongoing high prescription/Medicare costs pushed medical to $46,310. Even after the $6,375 floor, $39,935 of medical deducts. That alone (with no other Schedule A items) would beat the standard deduction.

The lesson for retirees: track medical out-of-pocket carefully every year. In a major medical year, itemizing wins. In normal years, standard deduction.

### 2. QCD beats itemized charity for retirees

Robert's $5,000 QCD is more tax-efficient than donating $5,000 cash and itemizing it:

**If $5,000 had been a cash donation on Line 11 instead of a QCD**:
- $5,000 added to Line 11 → Line 17 increases by $5,000 to $57,935
- Federal tax savings: $5,000 × 12% = $600
- But Robert would have had to take an additional $5,000 of taxable IRA distribution → $5,000 × 12% = $600 additional tax
- Net effect: $0 change

**With QCD**:
- $5,000 stays out of income (Form 1040 Line 4b shows the $5,000 QCD reduces taxable IRA distribution)
- AGI is $5,000 lower than it would have been without QCD
- Lower AGI also reduces:
  - Medical 7.5% floor ($375 less floor → $375 more medical deductible)
  - Possibly Medicare IRMAA tier in subsequent years
  - Potentially more Social Security taxable (if AGI was at the threshold) — actually QCD lowering AGI here helps
- Net effect: $5,000 stays out of income (savings $600) + $375 × 12% = $45 in additional medical deduction = ~$645 total

QCD is incrementally better — and the AGI reduction has cascading benefits across the return.

For retirees age 70½+ with charitable giving plans, **QCD before itemizing**. Up to $108,000 per person allowed for 2025.

### 3. Long-term care insurance premiums are within age caps

The age-based caps for LTC insurance premiums (for 2025, per Rev. Proc. 2024-40 §3.27):

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

Medicare Part B premiums deducted directly from Robert's and Margaret's Social Security checks are still medical expenses on Line 1. The amount appears on the year-end SSA-1099 form (Box 3).

This is often overlooked. For a couple paying ~$3,700 of combined Medicare Part B premiums plus ~$720 of Part D plus ~$4,800 of Medigap, that's $9,220 of medical premiums deductible at Line 1 — meaningful for the medical deduction.

### 5. State tax treatment of itemized differs

Arizona allows itemized deductions to mirror federal; many states do not. Verify state-specific rules:
- AZ: itemized allowed; mirrors federal Schedule A with adjustments
- States that don't tax SS: SS not added to state AGI
- States with own SALT cap (or deductibility of state income tax against itself): some have peculiar rules

For a couple with $85K joint income in Arizona, the federal benefit ($2,380 at 12%) is the primary driver. State tax savings at AZ's flat 2.5% rate adds roughly $500 more.

## Filing channel

Margaret and Robert use a CPA who specializes in retiree returns. The CPA will:

1. Receive their SSA-1099s, 1099-Rs (IRA, pension), 1099-INT/DIV, W-2 (Robert's part-time), Form 1098, year-end DAF/charity statements, and detailed medical receipt log
2. Compute AGI on Form 1040 (with QCD reducing IRA distribution income)
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
- **Casualty loss in federally declared disaster**: would add to Line 15
- **Margaret's pension split as non-taxable basis recovery**: AGI computation adjusts; doesn't change Schedule A directly
- **Medicare IRMAA**: high-AGI retirees face higher Medicare premiums; QCD can drop them under IRMAA tiers, indirectly saving thousands
