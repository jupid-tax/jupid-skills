# Example: Single Parent, 1 Qualifying Child + 1 Elderly Parent Dependent

A single parent (Head of Household) with one qualifying child (CTC) and one elderly parent claimed as a dependent (ODC). Modest income → ACTC kicks in. Demonstrates mixed CTC + ODC + ACTC computation.

## The filer

- **Name**: DeShawn Williams
- **Filing status**: Head of Household
- **AGI**: $42,000
- **MAGI**: $42,000 (no foreign income)
- **Earned income**: $42,000 (W-2 wages, no self-employment)
- **Tax year**: 2025 (filing in 2026)

## Dependents

DeShawn lives with his 6-year-old son and his 71-year-old mother (who has Alzheimer's and lives with him).

| Dependent       | Relationship | Age 12/31 | SSN by due date | Classification |
|-----------------|--------------|-----------|------------------|----------------|
| Marcus Williams | Son          | 6         | Yes              | Qualifying child (CTC) |
| Linda Williams  | Mother       | 71        | Yes              | Qualifying relative (ODC) |

### Marcus — qualifying child for CTC

- Relationship: son ✓
- Age: 6 (under 17) ✓
- Residency: lives with DeShawn full-time ✓
- Support: did not provide own support ✓
- Joint return: never married ✓
- Citizenship: U.S. citizen ✓
- SSN by due date: yes ✓

All seven tests pass → qualifying child.

### Linda — qualifying relative for ODC

- Not a qualifying child (parents aren't qualifying children) ✓
- Relationship: mother (in §152(d)(2) list) ✓
- Gross income: $9,200 Social Security only. Social Security is excluded from gross income for §152(d) purposes → effective gross income $0 < $5,200 ✓
- Support: DeShawn provides housing, food, medical care, etc. — clearly > 50% ✓

Linda qualifies as Other Dependent for ODC.

- **N_CTC** = 1 (Marcus)
- **N_ODC** = 1 (Linda)

## Step 3 — Tentative credit

```
Tentative CTC = 1 × $2,000 = $2,000
Tentative ODC = 1 × $500 = $500
Tentative total = $2,500
```

## Step 4 — MAGI phase-out

```
MAGI = $42,000
Threshold (HoH) = $200,000
Excess = $0
Reduction = $0
Allowed credit = $2,500
```

DeShawn's MAGI is far below threshold. Full credit available.

## Step 5 — Non-refundable credit (1040 Line 19)

DeShawn's tax computation:

- Standard deduction (HoH 2025): $21,900 (verify 2026)
- Taxable income: $42,000 − $21,900 = $20,100
- Tax (HoH 2025 brackets, computed via tax tables): ~$2,194 (10% bracket fully + small portion of 12% bracket)

Pre-credit tax (Form 1040 Line 18): $2,194.

```
Non-refundable credit = min($2,500, $2,194) = $2,194
```

The non-refundable portion is capped at the tax liability ($2,194). **Form 1040 Line 19 = $2,194**.

There's leftover credit: $2,500 − $2,194 = $306. This may be refundable as ACTC for the qualifying child (Marcus only; ODC is non-refundable).

## Step 6 — Refundable ACTC (1040 Line 28)

```
Leftover = $2,500 − $2,194 = $306
```

Earned income method:

```
Earned income = $42,000
Earned income excess = $42,000 − $2,500 = $39,500
EI method ACTC = $39,500 × 15% = $5,925
```

Per-child cap:

```
Per-child cap = 1 × $1,700 = $1,700  (verify 2026 figure)
```

Alternative method (3+ qualifying children only): not applicable (N_CTC = 1).

```
ACTC = min(Leftover, EI method, Per-child cap)
     = min($306, $5,925, $1,700)
     = $306
```

The ACTC is capped by the **leftover** ($306), not the per-child cap. Because the non-refundable already absorbed most of the credit, only $306 remains potentially refundable.

**Form 1040 Line 28 = $306**.

Note: the **ODC** ($500 for Linda) is **never refundable**. It went into the $2,500 tentative total, but only the $2,000 CTC for Marcus contributes to refundability. In this case, the $306 leftover happens to be ≤ $2,000 (the CTC portion), so it works out — DeShawn gets $306 refundable from his CTC.

If the leftover had been larger than the CTC contribution (e.g., the ODC of $500 was the only leftover), the ODC portion would be lost, not refundable.

## The completed worksheet

```markdown
# Schedule 8812 — DRAFT WORKSHEET for tax year 2025

## Filing facts
- Filing status: Head of Household
- Filer's MAGI: $42,000
- Earned income: $42,000
- Tax before credits (1040 Line 18): $2,194
- Phase-out threshold: $200,000 (HoH)

## Dependents classified
| Dependent       | Relationship | Age 12/31 | SSN/ITIN | Classification |
|-----------------|--------------|-----------|----------|----------------|
| Marcus Williams | Son          | 6         | SSN      | Qualifying child (CTC) |
| Linda Williams  | Mother       | 71        | SSN      | Qualifying relative (ODC) |

- N_CTC: 1
- N_ODC: 1

## Step 3 — Tentative credit
- CTC tentative: 1 × $2,000 = $2,000
- ODC tentative: 1 × $500 = $500
- **Tentative total**: $2,500

## Step 4 — MAGI phase-out
- MAGI: $42,000
- Threshold: $200,000
- Excess: $0
- Phase-out reduction: $0
- **Allowed credit**: $2,500

## Step 5 — Non-refundable credit (1040 Line 19)
- Tax before credits: $2,194
- Non-refundable credit: min($2,500, $2,194) = $2,194
- **1040 Line 19**: $2,194

## Step 6 — Refundable ACTC (1040 Line 28)
- Leftover: $2,500 − $2,194 = $306
- Earned income: $42,000
- Earned income excess: $39,500
- Earned income method ACTC: $5,925
- Per-child cap (1 × $1,700): $1,700
- Alternative SS-tax method: N/A (only 1 qualifying child)
- ACTC = min($306, $5,925, $1,700) = $306
- **1040 Line 28**: $306

## Verification
- Allowed credit = Non-refundable + ACTC: $2,500 = $2,194 + $306 ✓
- Each dependent classified once: ✓
- SSN-by-due-date verified for Marcus: ✓
- Linda has SSN (qualifies for ODC TIN requirement): ✓

## Validation summary
- Math: all checks passed
- Sanity:
  - Marcus (age 6) qualifies for CTC
  - Linda's $9,200 Social Security excluded from §152(d) gross income → passes test
  - DeShawn provides > 50% support of Linda (lives with him, he pays bills) → passes test
  - Earned income $42K > $2,500 threshold → ACTC available
- Next steps:
  - DeShawn files Schedule 8812 with his HoH 1040
  - 1040 Line 19: $2,194 (reduces tax)
  - 1040 Line 28: $306 (refundable; adds to refund)
  - Total credit benefit: $2,194 + $306 = $2,500 (full credit utilized)
  - PATH Act: refund will not issue before mid-February (returns claiming ACTC)

## Sources cited in this draft
- IRS Schedule 8812 (Rev. 2025)
- IRC §24(a) — base $2,000 credit
- IRC §24(d) — Refundable ACTC
- IRC §24(d)(1)(B) — Earned income > $2,500 requirement
- IRC §24(h)(4) — Credit for Other Dependents ($500)
- IRC §24(h)(5) — Refundable cap $1,700 (2025)
- IRC §152(d) — Qualifying relative definition
- IRC §152(f)(5) — Social Security excluded from §152(d) gross income
- Pub 501 — Dependents
- Rev. Proc. 2024-40 — 2025 inflation adjustments
```

## Why each non-obvious choice

**Why is Linda's Social Security excluded from her gross income?** Per IRC §152(d)(1)(B), the test is "gross income" — and Social Security benefits are not "gross income" for this purpose unless a portion is taxable. Per the Tier I + Tier II analysis under IRC §86, if Linda's only income is Social Security and her total falls below the base amount ($25,000 for single in 2025), none of her benefits are taxable, and her gross income for §152(d) is $0.

If Linda also had $5,000 of pension income, her gross income would be $5,000 — still below the $5,200 limit, so she'd still pass.

If Linda had $6,000 of pension income, gross income = $6,000 > $5,200 → fail. She couldn't be claimed as a dependent and the ODC wouldn't apply.

**Why does DeShawn get $306 refundable when his leftover is $306?** The ACTC is the smallest of three caps:
1. Leftover from non-refundable: $306
2. Earned income method: $5,925
3. Per-child cap: $1,700

The leftover is the binding constraint here — only $306 remains after non-refundable. If DeShawn had had higher tax liability ($2,500+), the entire CTC + ODC would be non-refundable; ACTC = $0. If DeShawn had had lower tax liability ($1,000), the non-refundable would be $1,000, leftover would be $1,500, and ACTC would be min($1,500, $5,925, $1,700) = $1,500.

**Why is the ODC ($500 for Linda) not refundable?** IRC §24(h)(4) — the Credit for Other Dependents is non-refundable only. It can reduce tax liability but cannot create a refund. Only the CTC portion (per qualifying child) is refundable as ACTC.

**What if DeShawn's tax liability were $0 (very low income)?** Non-refundable would be $0, leftover would be $2,500. ACTC = min($2,500, $5,925, $1,700) = $1,700. The $500 ODC would be lost (no tax to reduce, not refundable). DeShawn would get $1,700 refundable.

**What about EITC?** With 1 qualifying child and HoH filing, AGI $42K is in the phase-out range for 2025 EITC (verify 2026 figure). DeShawn might get a small EITC of perhaps $500-$1,500 — separate computation on Schedule EIC. The agent should refer DeShawn to the EITC skill (forthcoming).

**Audit defense**:
1. Marcus's birth certificate and SSN
2. Linda's SSN and proof of relationship
3. Documentation that Linda lives with DeShawn (lease showing both names, or DeShawn as sole tenant with Linda as occupant)
4. Documentation that DeShawn provides > 50% of Linda's support (rent receipts, grocery receipts, medical bills paid by DeShawn)
5. Linda's Social Security statement showing $9,200 (no other income)
