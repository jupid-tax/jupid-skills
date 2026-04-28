# Computing QBI from Schedule C — §199A Adjustments

The most common Form 8995 mistake is using Schedule C Line 31 (net profit) directly as QBI. This overstates QBI and the resulting deduction. The §199A regulations require subtracting certain adjustments.

---

## The mandatory subtractions

For each Schedule C source, QBI = Schedule C Line 31 minus:

1. **One-half of self-employment tax** (Schedule SE Line 13 / Schedule 1 Line 15)
2. **Self-employed health insurance deduction** (Schedule 1 Line 17)
3. **Self-employed retirement contributions** (Schedule 1 Line 16) — SEP, SIMPLE, solo 401(k)

Authority: Treas. Reg. §1.199A-3(b)(1)(vi).

The reasoning: these amounts are already deducted on the filer's Form 1040 because they reduce the income from the trade or business for federal income tax purposes. §199A does not let you double-count them.

---

## Allocation when filer has multiple Schedule Cs

If the filer has two or more Schedule Cs, each is treated as a separate trade or business (unless aggregated). The §199A adjustments must be allocated across them.

**Allocation formula:**

```
Adjustment for Business X = (Net profit of Business X / Total net profit of all Schedule Cs)
                            × Total adjustment amount
```

**Example:**

- Schedule C #1 (consulting): $40,000 net profit
- Schedule C #2 (Etsy shop): $10,000 net profit
- Total net profit: $50,000
- ½ SE tax: $3,532
- SE health insurance: $4,200
- SEP-IRA: $1,500
- Total adjustments: $9,232

Allocation:

| Business | Net profit | Share | ½ SE tax | SE health | SEP | Total adj | QBI |
|----------|------------|-------|----------|-----------|-----|-----------|-----|
| #1 Consulting | $40,000 | 80% | $2,826 | $3,360 | $1,200 | $7,386 | $32,614 |
| #2 Etsy | $10,000 | 20% | $706 | $840 | $300 | $1,846 | $8,154 |

Both QBI figures go on separate lines (1a and 1b) of Form 8995.

---

## When a Schedule C has a loss

If a Schedule C has a loss (negative Line 31), the §199A adjustments still apply but they are constrained:

- **½ SE tax** — only computed if SE earnings are positive. If a loss-making Schedule C is the only SE source, ½ SE tax = 0 and there is no adjustment for SE tax.
- **SE health insurance** — limited to net SE earnings from the business. If the business has a loss, the SE health insurance deduction may be limited or zero (and the unused portion may go to Schedule A as itemized medical, subject to 7.5% AGI floor).
- **SE retirement** — limited to net SE earnings. Same logic as SE health insurance.

In practice, a loss-making Schedule C means the QBI for that source is just the loss itself (Line 31), with no adjustments to subtract.

---

## When the filer has K-1 income alongside Schedule C

K-1 QBI is reported separately by the partnership or S-corp and includes the entity's own §199A adjustments where applicable. The Schedule C §199A adjustments do **not** reduce K-1 QBI.

Example with both:

- Schedule C profit: $50,000 → ½ SE tax $3,532, SE health $4,200, SEP $1,500 → QBI = $40,768
- Partnership K-1 (Box 20 code Z): $15,000 QBI
- S-corp K-1 (Box 17 code V): $20,000 QBI

Form 8995 Line 1a-1c:
- 1a: Garcia Design (Schedule C) — QBI $40,768
- 1b: Acme LLC (partnership K-1) — QBI $15,000
- 1c: XYZ Inc (S-corp K-1) — QBI $20,000

Line 2 total: $75,768.

---

## When SE health insurance has been allocated to W-2 income

If the filer also has W-2 income with employer-subsidized health insurance, the SE health insurance deduction is limited to the difference between total premiums and the employer subsidy. Make sure the deduction on Schedule 1 Line 17 reflects only what the SE business funded — that's the amount that subtracts from QBI.

---

## When the filer has a spouse with SE income (MFJ)

If both spouses have Schedule Cs:

1. Each spouse's Schedule C is a separate trade or business
2. Each spouse's ½ SE tax is allocated to their own Schedule C(s)
3. SE health insurance is allocated to whichever spouse paid the premium
4. SE retirement contributions are allocated to whichever spouse made the contribution

On Form 8995, list each Schedule C separately in Lines 1a-1e with the QBI net of that spouse's adjustments.

---

## Sanity check after computing QBI

For a typical solo Schedule C filer with no employees:

```
QBI / Schedule C net profit ≈ 0.85 to 0.93
```

If your computed QBI is above 95% of Schedule C net profit, you likely missed an adjustment. If below 80%, you may have over-subtracted (e.g., subtracted both halves of SE tax instead of just half).

---

## Common allocation mistakes

### Mistake: Using full SE tax instead of ½

The adjustment is **half** of the SE tax (the deductible "employer" portion), not the full amount. The SE tax itself is on Schedule SE Line 12; the deductible half is on Line 13.

### Mistake: Using gross health insurance premiums instead of the SE deduction

If the filer's income is below the threshold for the full deduction or if there's a Marketplace subsidy reconciliation, the deduction on Schedule 1 Line 17 may be less than the gross premiums. Use the actual deducted amount, not gross.

### Mistake: Subtracting employer 401(k) match as if it were SE retirement

W-2 401(k) employee contributions and employer match are not SE retirement contributions. They reduce W-2 wages on Form W-2, not Schedule 1. Don't subtract them from QBI.

### Mistake: Including state income tax in adjustments

State income tax on business profit is **not** a §199A QBI adjustment. It's a separate Schedule A deduction (subject to SALT cap) and does not reduce QBI.

### Mistake: Allocating adjustments by revenue instead of net profit

Allocate by net profit (Line 31), not gross revenue. Two businesses with equal revenue but different expense structures will have different shares of the adjustments.
