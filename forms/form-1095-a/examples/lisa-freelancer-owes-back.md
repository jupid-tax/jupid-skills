# Example: Lisa, Freelance Writer — Income Higher than Estimated, Owes Back Capped Excess APTC

## Persona

- Lisa, age 34, single, no dependents
- Freelance content writer; client roster grew during 2025
- Resident of Texas (48 contiguous states + DC FPL table)
- Enrolled in healthcare.gov silver plan all 12 months of 2025
- Estimated 2025 income at enrollment: $30,000 (about 200% FPL)
- Actual 2025 AGI: $42,000 (Schedule C net profit minus self-employed health insurance and SE tax deduction)

## Form 1095-A Received

### Part I — Recipient Information
- Recipient: Lisa, SSN ###-##-####
- Policy issuer: Ambetter Health Plans
- Policy number: ABC123456789
- Coverage period: 01/01/2025 – 12/31/2025

### Part II — Covered Individuals
- Lisa (only enrollee)

No shared policy. No allocation needed.

### Part III — Coverage Information

Same amounts every month (no plan changes, no family changes):

| Month | Col A (Premium) | Col B (SLCSP) | Col C (APTC) |
|-------|-----------------|---------------|--------------|
| Jan | $480 | $420 | $380 |
| Feb | $480 | $420 | $380 |
| Mar | $480 | $420 | $380 |
| Apr | $480 | $420 | $380 |
| May | $480 | $420 | $380 |
| Jun | $480 | $420 | $380 |
| Jul | $480 | $420 | $380 |
| Aug | $480 | $420 | $380 |
| Sep | $480 | $420 | $380 |
| Oct | $480 | $420 | $380 |
| Nov | $480 | $420 | $380 |
| Dec | $480 | $420 | $380 |
| **Annual** | **$5,760** | **$5,040** | **$4,560** |

All Column B values are nonzero — no SLCSP lookup needed.

## Form 8962 Reconciliation

### Part I — Annual Contribution

| Line | Description | Amount |
|------|-------------|--------|
| 1 | Tax family size | 1 |
| 2a | Modified AGI | $42,000 |
| 2b | Dependent modified AGI | $0 |
| 3 | Household income | $42,000 |
| 4 | FPL (HH of 1, 48 states+DC, 2024 FPL) | $15,060 |
| 5 | Income % of FPL = 42,000 ÷ 15,060 × 100, rounded down | 278% |
| 7 | Applicable Figure (interpolated, 250% → 300% under ARPA/IRA: 0.0400 + (28/50) × 0.0200) | 0.0512 (5.12%) |
| 8a | Annual contribution = 42,000 × 0.0512 | $2,150 |
| 8b | Monthly contribution = 2,150 ÷ 12 | $179 |

(Verify exact applicable figure against current Form 8962 Table 2; this example uses interpolation.)

### Part II — Annual Calculation (Line 11)

Lisa's coverage and APTC didn't change all year, so Line 10 = Yes → Line 11 (annual).

| Line | Description | Amount |
|------|-------------|--------|
| 11(a) | Annual enrollment premium | $5,760 |
| 11(b) | Annual SLCSP | $5,040 |
| 11(c) | Annual contribution (= Line 8a) | $2,150 |
| 11(d) | Max premium assistance = max(0, 5,040 − 2,150) | $2,890 |
| 11(e) | Annual PTC = lesser of $5,760 or $2,890 | $2,890 |
| 11(f) | Annual APTC | $4,560 |
| 24 | Total PTC | $2,890 |
| 25 | Total APTC | $4,560 |

### Part III — Repayment of Excess APTC

| Line | Description | Amount |
|------|-------------|--------|
| 27 | Excess APTC = 4,560 − 2,890 | $1,670 |
| 28 | Repayment limit (Single, 200–300% FPL, 2025 Pub 974 Table 5) | $975 |
| 29 | Excess APTC repayment = lesser of 1,670 or 975 | $975 |

**Result: Lisa owes back $975** to the IRS via Schedule 2 Line 1a. The remaining $695 of excess APTC is forgiven under the repayment cap.

## Validation

- [x] Math: Line 3 = Line 2a (no dependents). Line 5 calculated correctly. Line 11(e) = lesser of (a) and (d). Line 27 = Line 25 − Line 24. Line 29 = lesser of 27 or 28.
- [x] No shared policy (Part II had only Lisa).
- [x] Column B was nonzero for all 12 months — no SLCSP lookup needed.
- [x] Filing status (Single) eligible for PTC.
- [x] Income % FPL within range.

## Filing Steps for Lisa

1. Form 8962 attached to Form 1040
2. Schedule 2 Line 1a = $975 (Excess APTC repayment) → adds to total tax
3. Form 1040 Line 23 (Total Schedule 2 amount) increases by $975
4. Lisa pays $975 with the return (or it reduces her refund by $975)
5. Lisa keeps Form 1095-A in her records (NOT attached to return)

## Key Lesson

Lisa's income drift from $30,000 estimate to $42,000 actual cost her $975 in cash plus the loss of additional PTC she would have received at the lower income. Updating the Marketplace mid-year — every time a new client signed on or her rates increased — would have either increased her contribution share monthly (smoothing the year-end repayment) or, if her income spike came late, at least reduced the excess APTC accruing.

For self-employed filers with volatile income, real-time AGI tracking (e.g., via Jupid) is the difference between a small expected payment and a surprise tax bill.
