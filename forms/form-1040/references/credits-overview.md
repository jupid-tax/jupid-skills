# Credits Overview

Federal tax credits available to individual filers, organized by where they land on Form 1040. A credit reduces tax dollar-for-dollar (better than a deduction, which only saves the marginal-rate fraction). Refundable credits can produce a refund larger than tax paid; non-refundable credits cap at the tax owed.

**Legal basis**: IRC §21–35 (non-refundable personal credits), §32 (EITC), §24 (CTC), §25A (education), §25B (Saver's), §25D (residential energy), §901 (foreign tax), §36B (PTC).

---

## Where credits land on Form 1040

| 1040 Line | Type | Credits |
|-----------|------|---------|
| 19 | Non-refundable | CTC + ODC (non-refundable portion) |
| 20 | Non-refundable | All other non-refundable credits via Schedule 3 Line 8 |
| 27 | Refundable | EITC |
| 28 | Refundable | Additional CTC (refundable portion of CTC) |
| 29 | Refundable | AOTC refundable portion (40% of AOTC) |
| 31 | Refundable | Net PTC, fuel tax credits, withholding excess via Schedule 3 Line 15 |

Non-refundable credits on Line 20 come from Schedule 3 Lines 1-7:
- L1 Foreign tax credit (Form 1116)
- L2 Credit for child and dependent care expenses (Form 2441)
- L3 Education credits (Form 8863, non-refundable portion)
- L4 Retirement savings contributions credit (Form 8880)
- L5 Residential energy credits (Form 5695)
- L6a-L6z Other specific credits

---

## 1. Child Tax Credit (CTC) and Credit for Other Dependents (ODC)

**Form**: Schedule 8812.
**Lands on**: 1040 Line 19 (non-refundable portion) and Line 28 (refundable portion).

### CTC

- $2,000 per qualifying child under 17 at end of year (2025; verify 2026)
- Refundable portion: up to $1,700 per child for 2025 (verify 2026)
- Qualifying child must have a valid SSN issued before the return's due date
- Phaseout: $50 per $1,000 of AGI over $200,000 single / $400,000 MFJ
- Phases out completely at AGI $240,000 single / $440,000 MFJ for one child

### ODC

- $500 per qualifying dependent who doesn't qualify for CTC (older children, qualifying relatives, parents)
- Non-refundable
- Same phaseout thresholds as CTC

### Qualifying child for CTC (stricter than dependent test)

ALL must be true:
1. Under age 17 at end of year
2. Filer's child, stepchild, foster child, sibling, half-sibling, step-sibling, or descendant
3. Lived with filer > half the year
4. Did NOT provide > half their own support
5. Claimed as dependent on filer's return
6. Did not file a joint return for the year (except to claim a refund)
7. US citizen, US national, or US resident alien
8. **Has a valid SSN issued before the return's due date** (this is the strictest test — ITINs don't qualify for CTC, only ODC)

### Computation flow on Schedule 8812

1. List qualifying children with SSNs and ages
2. Compute tentative credit ($2,000 × number of qualifying children + $500 × number of ODC dependents)
3. Apply phaseout based on AGI
4. Compare to tax liability — non-refundable portion fills tax liability up to limit
5. Compute refundable portion (Additional CTC) = lesser of (1) earned income × 15%, (2) $1,700 per qualifying child, (3) excess of total CTC over non-refundable portion

For most filers with at least $20,000 earned income, the full refundable portion applies.

---

## 2. Earned Income Tax Credit (EITC)

**Form**: 1040 directly (with EIC tables in 1040 instructions). Schedule EIC if claiming a qualifying child.
**Lands on**: 1040 Line 27.
**Refundable**: yes.

A credit for low-to-moderate income workers, designed to reduce tax burden and encourage work.

### Maximum credit (2025)

| Qualifying children | Max EITC |
|---------------------|----------|
| 0 | $649 |
| 1 | $4,328 |
| 2 | $7,152 |
| 3+ | $8,046 |

### AGI / earned income limits (2025; phaseouts)

EITC phases in, plateaus, then phases out. Approximate single filer thresholds for 2025 (verify; varies by status and number of children):

| Children | Max earnings to claim any EITC |
|----------|-------------------------------|
| 0 (single, age 25-64) | ~$19,104 |
| 1 | ~$50,434 |
| 2 | ~$57,310 |
| 3+ | ~$61,555 |

MFJ thresholds are about $7,000 higher. **Verify all 2026 figures against Rev. Proc. 2025-XX.**

### Disqualifiers

- Investment income > $11,950 (2025; verify 2026)
- MFS filing status (rarely allowed; only if separated and lived apart > 6 months and qualifying child lived with filer)
- Cannot claim if also claiming Foreign Earned Income Exclusion (Form 2555)
- Must have valid SSN (ITIN disqualifies)
- Must be US citizen or resident alien for the entire year

### Qualifying child for EITC (slightly different from CTC)

- Same age tests as dependent qualifying child (under 19, or under 24 + full-time student, or any age if disabled)
- Same relationship test
- Same residency test (> half year)
- NO support test
- NO joint return test (different from CTC)
- Doesn't need a valid SSN issued before due date if the child has SSN by the time the return is filed (but SSN required, not ITIN)

A child can be a "qualifying child for EITC" but NOT a "qualifying child for CTC" — e.g., 18-year-old non-student living with filer. Filer gets EITC for the child but not the $2,000 CTC.

---

## 3. American Opportunity Tax Credit (AOTC) and Lifetime Learning Credit (LLC)

**Form**: Form 8863.
**Lands on**: 1040 Line 29 (refundable AOTC portion), Schedule 3 Line 3 → 1040 Line 20 (non-refundable portion).

### AOTC

- 100% of first $2,000 of qualified education expenses + 25% of next $2,000 = max $2,500 per eligible student
- 40% of AOTC is refundable (up to $1,000) — lands on Line 29
- 60% non-refundable — lands on Line 20 via Schedule 3 Line 3
- Available for the first 4 years of post-secondary education
- Student must be enrolled at least half-time, pursuing a degree, no felony drug conviction
- Income phaseout: $80,000–$90,000 single / $160,000–$180,000 MFJ (verify 2026)

### LLC (Lifetime Learning Credit)

- 20% of up to $10,000 of qualified expenses = max $2,000 per return (not per student)
- Non-refundable only
- No 4-year limit; can be used for graduate school, professional development, single courses
- Same phaseout thresholds as AOTC
- Cannot claim AOTC and LLC for the same student in the same year, but can claim AOTC for one child and LLC for another

Most undergrad students qualify for AOTC (better credit). Graduate students and continuing-ed filers use LLC.

---

## 4. Saver's Credit (Retirement Savings Contributions Credit)

**Form**: Form 8880.
**Lands on**: Schedule 3 Line 4 → 1040 Line 20.
**Non-refundable**.

A credit of 10%, 20%, or 50% of up to $2,000 of retirement contributions (IRA, 401(k), 403(b), etc.). Maximum credit: $1,000 ($2,000 MFJ).

### 2025 AGI limits

| Status | 50% credit | 20% credit | 10% credit | $0 credit above |
|--------|-----------|-----------|-----------|-----------------|
| Single | up to $23,750 | $23,751–$25,500 | $25,501–$39,500 | $39,500 |
| MFJ | up to $47,500 | $47,501–$51,000 | $51,001–$79,000 | $79,000 |
| HoH | up to $35,625 | $35,626–$38,250 | $38,251–$59,250 | $59,250 |

**Verify 2026 limits** against the latest Rev. Proc.

### Disqualifiers

- Under age 18
- Full-time student during 5+ months of the year
- Claimed as a dependent on someone else's return

The Saver's Credit is the most commonly missed credit for low-to-moderate income filers who contribute to a 401(k) or IRA. Worth checking whenever the filer has retirement contributions and AGI under the threshold.

---

## 5. Foreign Tax Credit

**Form**: Form 1116 (or directly if total foreign tax paid ≤ $300 / $600 MFJ).
**Lands on**: Schedule 3 Line 1 → 1040 Line 20.
**Non-refundable**.

Credit for income tax paid to foreign countries (typically through 1099-DIV box 6 or K-1). Avoids double taxation on foreign income.

If foreign tax ≤ $300 ($600 MFJ) and from passive category only (dividends, interest), can claim directly on Schedule 3 without filing Form 1116 — simpler.

For higher amounts or complex situations, Form 1116 computes the credit limit (US tax on foreign income) and any carryback/carryforward.

Alternative: deduct foreign tax as itemized on Schedule A. Credit usually beats deduction; run the math both ways for large amounts.

---

## 6. Premium Tax Credit (PTC)

**Form**: Form 8962.
**Lands on**: Schedule 3 Line 9 → 1040 Line 31 (refundable). Or Schedule 2 Line 1a (excess advance PTC repayment) if advance was too high.

Refundable credit for ACA marketplace health insurance. If filer received advance PTC (premium reduced upfront) on a 1095-A, must reconcile on Form 8962 against actual income.

If actual income < projected, additional PTC owed to filer (refundable, Line 31).
If actual income > projected, excess advance PTC must be repaid (capped based on income; lands on Line 17 via Schedule 2 Line 1a).

Common pain point for self-employed filers whose income is hard to project.

---

## 7. Dependent Care Credit (Child and Dependent Care)

**Form**: Form 2441.
**Lands on**: Schedule 3 Line 2 → 1040 Line 20.
**Non-refundable**.

20%–35% of up to $3,000 (one qualifying person) or $6,000 (two or more) of qualifying childcare/dependent care expenses paid so the filer (and spouse if MFJ) could work or look for work.

Qualifying person: child under 13, or disabled spouse / dependent of any age.

Both spouses (if MFJ) must have earned income. The credit is the smaller of the qualifying expense or each spouse's earned income.

Care provider's name, address, and TIN required on Form 2441 — informational return for the IRS to cross-check.

---

## 8. Residential Clean Energy Credit + Energy Efficient Home Improvement Credit

**Form**: Form 5695.
**Lands on**: Schedule 3 Line 5 → 1040 Line 20.
**Non-refundable** (mostly).

- **Residential Clean Energy Credit**: 30% of cost of solar panels, solar water heaters, geothermal, wind, fuel cells. No annual cap (for most categories).
- **Energy Efficient Home Improvement Credit**: 30% of cost of qualifying insulation, windows, doors, HVAC, with annual caps ($1,200 for most + $2,000 for heat pumps/biomass stoves).

Both made permanent / extended via the Inflation Reduction Act (IRA 2022) and unaffected by OBBBA 2025.

---

## 9. Adoption Credit

**Form**: Form 8839.
**Lands on**: Schedule 3 Line 6c → 1040 Line 20.
**Non-refundable**, but unused portion carries forward 5 years.

Up to ~$17,280 (2025; verify 2026) per adoption for qualifying expenses. Income phaseout starts ~$259,190 (2025).

---

## Summary table for the agent

| Credit | Form | Refundable? | Income limit | Notes |
|--------|------|-------------|--------------|-------|
| CTC | Sch 8812 | Partly | $200K/$400K phaseout | $2,000/child under 17 with SSN |
| ODC | Sch 8812 | No | Same as CTC | $500/other dependent |
| EITC | EIC tables | Yes | varies, low to moderate | Up to $8,046 for 3+ children |
| AOTC | 8863 | 40% refundable | $80K/$160K phaseout | First 4 yrs college |
| LLC | 8863 | No | Same as AOTC | Grad / continuing ed |
| Saver's | 8880 | No | $39,500/$79,000 | Up to $1,000 ($2,000 MFJ) |
| Foreign tax | 1116 | No | none | Direct on Sch 3 if ≤ $300/$600 |
| PTC | 8962 | Yes | based on FPL % | ACA marketplace; 1095-A required |
| Dep care | 2441 | No | none, but rate varies w/ AGI | $3,000/$6,000 max expense |
| Residential energy | 5695 | No | none | 30% solar/wind etc. |
| Adoption | 8839 | No | $259K phaseout | ~$17,280 per adoption |

---

## Sources

- IRC §21 — Child and dependent care expenses
- IRC §22 — Credit for elderly / disabled
- IRC §23 — Adoption credit
- IRC §24 — Child Tax Credit
- IRC §25A — Education credits (AOTC, LLC)
- IRC §25B — Saver's Credit
- IRC §25D — Residential clean energy
- IRC §32 — EITC
- IRC §36B — Premium Tax Credit
- IRC §901 — Foreign tax credit
- [Publication 596](https://www.irs.gov/publications/p596) — EITC
- [Publication 970](https://www.irs.gov/publications/p970) — Tax Benefits for Education
- [Schedule 8812 Instructions](https://www.irs.gov/pub/irs-pdf/i1040s8.pdf) — CTC / ACTC
- Rev. Proc. 2024-40 — 2025 figures
