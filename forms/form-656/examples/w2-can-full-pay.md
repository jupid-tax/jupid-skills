# Example: Wage Earner Who Can Pay in Full — Stop and Route to an Installment Agreement

A salaried employee asks for an offer in compromise after seeing "settle for less" ads. The eligibility screen passes, but the full-pay screen shows he can pay the balance from liquid assets and monthly income long before the collection statute ends. The agent stops, explains why the IRS would generally not accept an offer, and routes him to an installment agreement. No Form 656 is prepared.

> **Placeholder warning.** Lines (39) and (45) use **PLACEHOLDER** figures ($1,040 and $84) instead of the live Collection Financial Standards table effective June 29, 2026 (https://www.irs.gov/businesses/small-businesses-self-employed/collection-financial-standards). The conclusion below holds by a wide margin, but a real draft must use the table values.

## The user

- **Name:** Kevin Brandt, single, household of 1, rents in Minneapolis, Hennepin County, Minnesota
- **Job:** software QA engineer; gross pay $9,850 per month
- **Why he owes:** RSU income in 2023 and 2024 with too little withholding
- **Debt (account transcript):**

| Form | Period end | Assessment date | Balance | CSED |
|---|---|---|---|---|
| 1040 | 12-31-2023 | 05-27-2024 | $21,904 | 05-27-2034 |
| 1040 | 12-31-2024 | 05-19-2025 | $16,512 | 05-19-2035 |
| **Total** | | | **$38,416** | |

## Eligibility screen

All returns filed through 2025; bills received; 2026 withholding increased (W-4 updated) so no estimated payments are required; no bankruptcy, audit, or innocent spouse claim; he agrees he owes the tax. The screen passes, so the agent continues to the numbers before discussing an offer.

## Form 433-A (OIC) — Section 3, as the form computes it

| Line | Inputs (statements dated September 2026) | Computation | Amount |
|---|---|---|---|
| (1) | Checking $6,212 + savings $3,105 | 9,317 − 1,000 | $8,317 |
| (2) | Brokerage account $12,640, no margin loan | 12,640 − 0 | $12,640 |
| (3) | 401(k) $86,300, no loan | 86,300 × .8 | $69,040 |
| (4) | No cash-value life insurance | | $0 |
| (5) | No real property | | $0 |
| (6a) | 2021 Mazda CX-5, value $21,400, loan $13,980 | 21,400 × .8 − 13,980 | $3,140 |
| (6b) | | 3,140 − 3,450 → negative | $0 |
| (6) | | | $0 |
| (7) | Furniture and effects $9,000 → 7,200 | 7,200 − 11,980 → negative | $0 |
| **Box A** | | | **$89,997** |

## Section 7

| Line | Item | Amount |
|---|---|---|
| (30) | Gross wages | $9,850 |
| **Box D** | | **$9,850** |
| (39) | **PLACEHOLDER** National Standard, 1 person | $1,040 |
| (40) | Rent and utilities, actual (compare to Hennepin County standard) | $2,140 |
| (41) | Car loan | $486 |
| (42) | Vehicle operating, actual | $231 |
| (43) | Public transportation | $0 |
| (44) | Health insurance (payroll deduction) | $212 |
| (45) | **PLACEHOLDER** out-of-pocket health, under 65 | $84 |
| (46)–(48) | None | $0 |
| (49) | Federal, state, FICA withholding per pay stub | $2,733 |
| (50) | Federal student loan minimum payment, with proof | $318 |
| (51) | None | $0 |
| **Box E** | | **$7,244** |
| **Box F** | 9,850 − 7,244 | **$2,606** |

His 6% 401(k) contribution is not listed: voluntary retirement contributions are not an allowable expense (IRM 5.8.5.10; IRM 5.8.5.23).

Box G = 2,606 × 12 = $31,272. A "minimum offer" would be 89,997 + 31,272 = $121,269, more than three times the $38,416 balance. That alone shows an offer is not appropriate.

## Full-pay screen (without allowances)

| Measure | Amount |
|---|---|
| Liquid assets: cash 9,317 + brokerage 12,640 | $21,957 |
| Balance after applying liquid assets: 38,416 − 21,957 | $16,459 |
| Months of Box F needed: 16,459 / 2,606 | about 6.3 months (before accruing interest) |
| Months to the earlier CSED (May 2034) | 91 |
| Even excluding the 401(k) entirely (in case the plan cannot be accessed while employed, IRM 5.8.5.10): 9,317 + 12,640 + 3,140 + 2,606 × 91 | $262,243 capacity |

Result: he can pay in full well within the collection period. Form 656-B, page 1: "Generally, the IRS will not accept an offer if you can pay your tax debt in full through an installment agreement and/or equity in assets."

## What the agent tells Kevin

1. An offer in compromise would very likely be rejected, and the $205 fee and 20% initial payment (or first periodic payment) are generally kept and applied to the debt, not refunded (Form 656, Section 7(c)).
2. Options that fit his numbers: pay part from the brokerage account and savings, and set up a payment plan for the rest. His $38,416 balance is within the $50,000 limit for the IRS online payment plan application (https://www.irs.gov/payments/payment-plans-installment-agreements). Hand off to [`../../form-9465/SKILL.md`](../../form-9465/SKILL.md) for plan types, fees, and the direct-debit rules.
3. Selling brokerage holdings may create capital gains tax; he should ask a tax professional before selling.
4. Penalty relief is a separate question: if any failure-to-pay penalties qualify, see [`../../form-843/SKILL.md`](../../form-843/SKILL.md).

## Deliverable

```markdown
# Offer in Compromise — NOT RECOMMENDED (screen result)

Eligibility: passed.
Form 433-A (OIC) Box A: $89,997; Box F: $2,606 (lines 39 and 45 are placeholders pending the live tables).
Calculated minimum offer (lump sum): $121,269 vs balance $38,416.
Full-pay screen: liquid assets $21,957 + about 6.3 months of remaining income clears the balance; earlier CSED is 91 months away.
Conclusion: the IRS generally will not accept an offer when the debt can be paid in full (Form 656-B, page 1).
Next step: installment agreement → form-9465. No Form 656 prepared.
```

## Validation summary

- Math: recomputed in Python; pass.
- Flags: placeholders on lines (39) and (45); 401(k) access depends on plan terms; capital gains on any sale is outside this skill.
- No forms filed.
