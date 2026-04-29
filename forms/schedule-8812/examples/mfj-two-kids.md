# Example: MFJ Couple with 2 Qualifying Children, AGI $150K (Full $4,000 CTC)

The "everything works as intended" pattern. Married couple filing jointly, two young children, AGI well below the phase-out threshold, sufficient tax liability to absorb the full non-refundable CTC. No ACTC needed.

## The filers

- **Names**: Jordan and Priya Mehta
- **Filing status**: MFJ
- **AGI**: $150,000
- **MAGI**: $150,000 (no foreign earned income exclusion)
- **Earned income**: $148,000 (Jordan's $90K W-2 + Priya's $58K W-2)
- **Tax year**: 2025 (filing in 2026)

## Dependents

| Dependent     | Relationship | Age 12/31 | SSN by due date | Classification |
|---------------|--------------|-----------|------------------|----------------|
| Aanya Mehta   | Daughter     | 8         | Yes              | Qualifying child (CTC) |
| Rohan Mehta   | Son          | 5         | Yes              | Qualifying child (CTC) |

Both children:
- Lived with the Mehtas all year
- Did not provide their own support
- Are U.S. citizens
- Did not file joint returns
- Have SSNs issued at birth

Both are qualifying children for CTC.

- **N_CTC** = 2
- **N_ODC** = 0

## Step 3 — Tentative credit

```
Tentative CTC = 2 × $2,000 = $4,000
Tentative ODC = 0 × $500 = $0
Tentative total = $4,000
```

## Step 4 — MAGI phase-out

```
MAGI = $150,000
Threshold (MFJ) = $400,000
Excess MAGI = max(0, $150,000 − $400,000) = $0
Phase-out reduction = $0
Allowed credit = $4,000
```

The Mehtas are well below the phase-out threshold. Full credit available.

## Step 5 — Non-refundable credit (1040 Line 19)

The Mehtas' tax computation:

- Standard deduction (MFJ 2025): $29,200 (2026 figure inflation-adjusted; verify)
- Taxable income: $150,000 − $29,200 = $120,800
- Tax (MFJ 2025 brackets, computed via tax tables or formula): ~$17,500

Pre-credit tax (Form 1040 Line 18): $17,500.

```
Non-refundable credit = min($4,000, $17,500) = $4,000
```

The full $4,000 fits within tax liability. **Form 1040 Line 19 = $4,000**.

## Step 6 — Refundable ACTC

```
Leftover = Allowed credit − Non-refundable credit
         = $4,000 − $4,000 = $0
```

No leftover → no ACTC. **Form 1040 Line 28 = $0**.

The Mehtas don't need ACTC because their tax liability fully absorbed the non-refundable CTC. They get the full $4,000 benefit.

## The completed worksheet

```markdown
# Schedule 8812 — DRAFT WORKSHEET for tax year 2025

## Filing facts
- Filing status: MFJ
- Filer's MAGI: $150,000
- Earned income: $148,000
- Tax before credits (1040 Line 18): $17,500
- Phase-out threshold: $400,000 (MFJ)

## Dependents classified
| Dependent     | Relationship | Age 12/31 | SSN/ITIN | Classification |
|---------------|--------------|-----------|----------|----------------|
| Aanya Mehta   | Daughter     | 8         | SSN      | Qualifying child (CTC) |
| Rohan Mehta   | Son          | 5         | SSN      | Qualifying child (CTC) |

- N_CTC: 2
- N_ODC: 0

## Step 3 — Tentative credit
- CTC tentative: 2 × $2,000 = $4,000
- ODC tentative: 0 × $500 = $0
- **Tentative total**: $4,000

## Step 4 — MAGI phase-out
- MAGI: $150,000
- Threshold: $400,000
- Excess: $0
- Phase-out reduction: $0
- **Allowed credit**: $4,000

## Step 5 — Non-refundable credit (1040 Line 19)
- Tax before credits: $17,500
- Non-refundable credit: min($4,000, $17,500) = $4,000
- **1040 Line 19**: $4,000

## Step 6 — Refundable ACTC (1040 Line 28)
- Leftover: $4,000 − $4,000 = $0
- ACTC: $0 (no leftover)
- **1040 Line 28**: $0

## Verification
- Allowed credit = Non-refundable + ACTC: $4,000 = $4,000 + $0 ✓
- Each dependent classified once: ✓
- SSN-by-due-date verified for each qualifying child: ✓

## Validation summary
- Math: all checks passed
- Sanity:
  - Both children under 17 with SSN → CTC eligible
  - MAGI well below $400K threshold → no phase-out
  - Tax liability ($17,500) fully absorbs $4,000 non-refundable credit → no ACTC
- Next steps:
  - Form 1040 Line 19: $4,000
  - Form 1040 Line 28: $0
  - Net tax after CTC: $17,500 − $4,000 = $13,500
  - Refund or balance due depends on withholding (1040 Line 25a)

## Sources cited in this draft
- IRS Schedule 8812 (Rev. 2025)
- IRC §24(a) — base $2,000 credit
- IRC §24(b) — phase-out (no impact at $150K MFJ)
- IRC §24(c) — qualifying child definition
- IRC §24(h)(7) — SSN-by-due-date requirement
- IRS Schedule 8812 Instructions (Rev. 2025)
```

## Why each non-obvious choice

**Why $2,000 per child (and not the 2021 ARPA $3,000-$3,600)?** The American Rescue Plan Act of 2021 expanded CTC for tax year 2021 only. For 2022 onward, the rules reverted to the TCJA $2,000 base, made permanent by OBBBA 2025. The Mehtas get $2,000/child, not the higher 2021 amount.

**Why isn't there any ACTC?** ACTC is the refundable portion of CTC. It only matters when the non-refundable CTC was capped by tax liability. The Mehtas' $17,500 tax liability is much larger than the $4,000 credit, so the full credit is non-refundable. ACTC = $0 by design.

**Why not also claim Earned Income Tax Credit?** EITC has its own phase-out and AGI limits. For MFJ with 2 children, the EITC fully phases out around $59,478 AGI (2025; verify 2026). The Mehtas' AGI of $150K is far above the EITC phase-out — not eligible. EITC is on Schedule EIC, not Schedule 8812.

**Why not also claim Childcare Credit?** Form 2441 (Child and Dependent Care Credit) is a separate credit for daycare expenses while both parents work. The Mehtas may or may not qualify (they didn't mention childcare expenses). If they do, that credit goes on Schedule 3 Line 6, separate from Schedule 8812.

**Audit defense**: the Mehtas' return shows:
1. Both children listed as dependents on Form 1040 with SSNs
2. CTC checkbox marked for both children
3. Schedule 8812 properly completed
4. MAGI well below phase-out → no risk of phase-out adjustment
5. Birth certificates and Social Security cards in the file (audit defense materials)

The IRS may match the children's SSNs against records to confirm they weren't claimed on another return. As long as the Mehtas were the only claimants, no issue.
