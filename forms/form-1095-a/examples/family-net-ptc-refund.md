# Example: Marcus and Elena Family — Income Lower than Estimated, Net PTC Refund

## Persona

- Marcus (38, photographer/freelancer) and Elena (36, part-time graphic designer)
- Married Filing Jointly
- Two dependents: kids ages 8 and 5
- Resident of Florida (48 states+DC FPL table)
- Enrolled in Florida Marketplace silver plan all 12 months of 2025
- Estimated 2025 income at enrollment: $90,000 (about 290% FPL for HH of 4)
- Actual 2025 AGI: $68,000 (Marcus had a slow first half; both had higher self-employed health insurance and SEP-IRA contributions reducing AGI)

## Form 1095-A Received

### Part I — Recipient Information
- Recipient: Marcus
- Policy issuer: Florida Blue
- Coverage: 01/01/2025 – 12/31/2025

### Part II — Covered Individuals
- Marcus, Elena, kid 1 (age 8), kid 2 (age 5)

All four on the joint tax return. No shared policy. No allocation needed.

### Part III — Coverage Information

Family of 4 silver plan, identical premium and benchmark all year. APTC was set based on the $90,000 income estimate, so was relatively low (Marketplace assumed they'd contribute more).

| Month | Col A (Premium) | Col B (SLCSP) | Col C (APTC) |
|-------|-----------------|---------------|--------------|
| Jan–Dec each | $1,650 | $1,580 | $830 |
| **Annual** | **$19,800** | **$18,960** | **$9,960** |

## Form 8962 Reconciliation

### Part I — Annual Contribution

| Line | Description | Amount |
|------|-------------|--------|
| 1 | Tax family size | 4 |
| 2a | Modified AGI | $68,000 |
| 2b | Dependent modified AGI | $0 |
| 3 | Household income | $68,000 |
| 4 | FPL (HH of 4, 48 states+DC, 2024 FPL) | $31,200 |
| 5 | Income % of FPL = 68,000 ÷ 31,200 × 100 | 217% |
| 7 | Applicable Figure (200% → 250% interpolation under ARPA/IRA: 0.0200 + (17/50) × 0.0200) | 0.0268 (2.68%) |
| 8a | Annual contribution = 68,000 × 0.0268 | $1,822 |
| 8b | Monthly contribution = 1,822 ÷ 12 | $152 |

(Verify exact applicable figure for the year being filed.)

### Part II — Annual Calculation

Coverage was identical all year, so Line 10 = Yes → Line 11 (annual).

| Line | Description | Amount |
|------|-------------|--------|
| 11(a) | Annual enrollment premium | $19,800 |
| 11(b) | Annual SLCSP | $18,960 |
| 11(c) | Annual contribution | $1,822 |
| 11(d) | Max premium assistance = max(0, 18,960 − 1,822) | $17,138 |
| 11(e) | Annual PTC = lesser of $19,800 or $17,138 | $17,138 |
| 11(f) | Annual APTC | $9,960 |
| 24 | Total PTC | $17,138 |
| 25 | Total APTC | $9,960 |
| 26 | Net Premium Tax Credit = 17,138 − 9,960 | $7,178 |

**Result: Marcus and Elena are owed an additional $7,178 in Premium Tax Credit** as a refundable credit, flowing to Schedule 3 Line 9.

## Validation

- [x] Math: Line 11(d) = max(0, b − c). Line 11(e) = lesser of (a) and (d). Line 26 = Line 24 − Line 25.
- [x] No shared policy (all covered individuals on the joint return).
- [x] Column B nonzero all 12 months.
- [x] MFJ filing status, eligible for PTC.
- [x] Income % FPL within ARPA/IRA range.

## Filing Steps for Marcus and Elena

1. Form 8962 attached to Form 1040
2. Schedule 3 Line 9 = $7,178 (Net Premium Tax Credit) → refundable credit
3. Form 1040 Line 31 (Total Schedule 3) increases by $7,178
4. The credit flows through to Form 1040 Line 33 (Total payments + refundable credits)
5. Refund increases by $7,178 (or balance due decreases by $7,178)
6. Form 1095-A kept in records (NOT attached to return)

## Key Lesson

Marcus and Elena's income came in $22,000 lower than the Marketplace estimate. Because they didn't update the Marketplace mid-year, they paid more out-of-pocket each month than they needed to. The good news: Form 8962 lets them recover the PTC they should have received as APTC. A $7,178 net credit becomes part of their refund.

If they had updated the Marketplace in summer (when Marcus's slow Q1 was clear), the Marketplace would have increased APTC monthly, reducing what they paid out of pocket each month. The end result is the same total credit — $17,138 — but the cash-flow timing improves. For households relying on PTC for affordability, mid-year updates are the difference between waiting 12 months for a refund and paying less monthly all year.

Even at $68,000 / 217% FPL, this family qualifies for a substantial PTC because their benchmark plan is expensive ($1,580/month for family of 4) and their contribution ceiling under ARPA/IRA is low (2.68% of income = $1,822/year). The system was designed so that family-of-4 silver coverage is broadly affordable across most income ranges.
