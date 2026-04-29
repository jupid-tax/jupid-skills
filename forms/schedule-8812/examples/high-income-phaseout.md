# Example: High-Income MFJ with 3 Children, AGI $450,000 (Partial Phase-Out)

The MAGI phase-out in action. MFJ couple with three qualifying children, MAGI $50,000 above the threshold. The CTC is reduced by $250, but most of the credit remains.

## The filers

- **Names**: Caroline and Marcus Thornton
- **Filing status**: MFJ
- **AGI**: $450,000
- **MAGI**: $450,000 (no foreign income)
- **Earned income**: $440,000 (W-2 wages: Caroline $260K + Marcus $180K)
- **Tax year**: 2025 (filing in 2026)

## Dependents

| Dependent             | Relationship | Age 12/31 | SSN by due date | Classification |
|-----------------------|--------------|-----------|------------------|----------------|
| Charlotte Thornton    | Daughter     | 14        | Yes              | Qualifying child (CTC) |
| Henry Thornton        | Son          | 11        | Yes              | Qualifying child (CTC) |
| Eleanor Thornton      | Daughter     | 7         | Yes              | Qualifying child (CTC) |

All three pass the qualifying child tests.

- **N_CTC** = 3
- **N_ODC** = 0

## Step 3 — Tentative credit

```
Tentative CTC = 3 × $2,000 = $6,000
Tentative ODC = 0 × $500 = $0
Tentative total = $6,000
```

## Step 4 — MAGI phase-out

```
MAGI = $450,000
Threshold (MFJ) = $400,000
Excess MAGI (raw) = $50,000
Excess (rounded UP to nearest $1,000) = $50,000  (already at exact $1,000 boundary)
Phase-out reduction = $50,000 / $1,000 × $5 = $250

Allowed credit = $6,000 − $250 = $5,750
```

The Thorntons lose $250 of credit due to the phase-out. They retain $5,750 of the $6,000 tentative.

### What if their MAGI were $450,500?

```
Excess (raw) = $50,500
Excess (rounded UP) = $51,000  (round $500 up to next $1,000)
Reduction = $51,000 / $1,000 × $5 = $255
Allowed = $6,000 − $255 = $5,745
```

Notice: the $500 of additional MAGI rounds up to a full $1,000 of excess, costing $5 of credit. This is how the "round up" rule bites — even a tiny amount over a threshold costs $5.

## Step 5 — Non-refundable credit (1040 Line 19)

The Thorntons' tax computation (rough):

- Standard deduction (MFJ 2025): $29,200
- Taxable income: $450,000 − $29,200 = $420,800
- Tax (MFJ 2025 brackets, computed at the high end including 32% / 35% portions): approximately $89,500
- Other adjustments not factored here for simplicity

Pre-credit tax (Form 1040 Line 18): $89,500.

```
Non-refundable credit = min($5,750, $89,500) = $5,750
```

The full $5,750 fits within tax liability. **Form 1040 Line 19 = $5,750**.

## Step 6 — Refundable ACTC (1040 Line 28)

```
Leftover = $5,750 − $5,750 = $0
```

No leftover → no ACTC. **Form 1040 Line 28 = $0**.

(Even if there were leftover, the alternative SS-tax method would be considered because N_CTC = 3. But with $0 leftover, the question is moot.)

## The completed worksheet

```markdown
# Schedule 8812 — DRAFT WORKSHEET for tax year 2025

## Filing facts
- Filing status: MFJ
- Filer's MAGI: $450,000
- Earned income: $440,000
- Tax before credits (1040 Line 18): $89,500
- Phase-out threshold: $400,000 (MFJ)

## Dependents classified
| Dependent             | Relationship | Age 12/31 | SSN/ITIN | Classification |
|-----------------------|--------------|-----------|----------|----------------|
| Charlotte Thornton    | Daughter     | 14        | SSN      | Qualifying child (CTC) |
| Henry Thornton        | Son          | 11        | SSN      | Qualifying child (CTC) |
| Eleanor Thornton      | Daughter     | 7         | SSN      | Qualifying child (CTC) |

- N_CTC: 3
- N_ODC: 0

## Step 3 — Tentative credit
- CTC tentative: 3 × $2,000 = $6,000
- ODC tentative: 0 × $500 = $0
- **Tentative total**: $6,000

## Step 4 — MAGI phase-out
- MAGI: $450,000
- Threshold: $400,000
- Excess (raw): $50,000
- Excess (rounded up to next $1,000): $50,000
- Phase-out reduction: $50,000 × $5 / $1,000 = $250
- **Allowed credit**: $6,000 − $250 = $5,750

## Step 5 — Non-refundable credit (1040 Line 19)
- Tax before credits: $89,500
- Non-refundable credit: min($5,750, $89,500) = $5,750
- **1040 Line 19**: $5,750

## Step 6 — Refundable ACTC (1040 Line 28)
- Leftover: $5,750 − $5,750 = $0
- ACTC: $0 (no leftover)
- **1040 Line 28**: $0

## Verification
- Allowed credit = Non-refundable + ACTC: $5,750 = $5,750 + $0 ✓
- Each dependent classified once: ✓
- SSN-by-due-date verified for each: ✓
- Phase-out calculation: ($450,000 − $400,000) / $1,000 × $5 = $250 ✓

## Validation summary
- Math: all checks passed
- Sanity:
  - All 3 children qualify for CTC (under 17, SSN, etc.)
  - MAGI $50K above MFJ threshold → $250 phase-out reduction
  - Tax liability ($89,500) easily absorbs $5,750 → no ACTC
  - PATH Act delay: not applicable (no ACTC claimed)
- Next steps:
  - Form 1040 Line 19: $5,750
  - Form 1040 Line 28: $0
  - Net tax after CTC: $89,500 − $5,750 = $83,750
  - Phase-out fully eliminates the $6,000 tentative credit at MFJ MAGI = $400,000 + ($6,000 / $5 × $1,000) = $1,600,000
  - The Thorntons should be aware: each $1,000 of MAGI growth above $400K costs $5 of credit until full elimination at $1,600,000 MFJ MAGI

## Sources cited in this draft
- IRS Schedule 8812 (Rev. 2025)
- IRC §24(a) — base $2,000 credit
- IRC §24(b) — phase-out ($5 per $1,000 over threshold)
- IRC §24(c) — qualifying child definition
- IRC §24(h)(7) — SSN-by-due-date requirement
- IRS Schedule 8812 Instructions (Rev. 2025) — Worksheet for phase-out
```

## Why each non-obvious choice

**Why does the credit fully phase out at MFJ MAGI $1,600,000?** Each $1,000 of excess MAGI costs $5 of credit. With $6,000 of tentative credit, the credit is fully eliminated when:

```
Reduction = excess × $5 / $1,000
$6,000 = excess × $5 / $1,000
excess = $6,000 × $1,000 / $5 = $1,200,000

Full-phase-out point = Threshold + excess
                     = $400,000 + $1,200,000
                     = $1,600,000 MFJ MAGI
```

For comparison: a one-child family ($2,000 tentative credit) fully phases out at threshold + $400,000 = $600K single / $800K MFJ. A two-child family fully phases out at threshold + $800,000 = $1.0M single / $1.2M MFJ. The Thornton family's full-phase-out point ($1.6M MFJ) is far above their actual MAGI; they retain $5,750 of the $6,000 tentative.

**Why no ACTC even though tax was high?** Tax liability ($89,500) is much larger than the credit ($5,750), so the full credit is non-refundable. No leftover for ACTC. ACTC is for filers whose tax liability is too small to absorb the full CTC.

**Why use the alternative SS-tax method here even with N_CTC = 3?** The alternative method is **only** considered when there's a leftover from the non-refundable computation. Here, leftover is $0, so neither method runs. If the Thorntons had a tax liability of, say, $3,000 (hypothetically), the leftover would be $5,750 − $3,000 = $2,750. Then both methods would compute, and the larger would yield the ACTC (capped at the per-child $1,700 × 3 = $5,100 or the leftover, whichever is smaller).

**Why is the standard deduction $29,200?** This is the MFJ 2025 standard deduction (Rev. Proc. 2024-40). For 2026, the inflation-adjusted figure must be verified (likely $30,000-$30,500 range, but check the latest Rev. Proc.).

**Audit defense**: the Thorntons' high income makes them a more typical audit candidate. Their files should include:
1. Birth certificates and SSNs for all three children
2. Proof of residency (lease, school enrollment)
3. The Schedule 8812 worksheet showing the phase-out computation
4. MAGI computation showing AGI = MAGI (no foreign income exclusion)
5. The Form 1040 Line 18 tax liability computation

The phase-out reduction of $250 is a small adjustment to a high-income return; the IRS is unlikely to question the math, but the documentation should be available.
