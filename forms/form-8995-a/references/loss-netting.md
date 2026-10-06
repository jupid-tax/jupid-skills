# Schedule C of Form 8995-A — Loss Netting and Carryforward

If any of the taxpayer's businesses has a negative QBI, Schedule C of Form 8995-A allocates the loss across positive-QBI businesses before applying the W-2/UBIA limit. This reference covers the math.

(Note: this is "Schedule C of Form 8995-A," NOT "Schedule C of Form 1040." Two different forms with the same letter.)

---

## When Schedule C of Form 8995-A applies

You must complete it before Part I when (2025 i8995-A, Schedule C):
- Any trade, business, or aggregation has a qualified business loss for the current year, OR
- You have a qualified business net loss carryforward from prior years (even if the loss was unreported or the business no longer exists)

This includes a single business with a loss: Schedule C line 6 is how the loss carries to next year.

If all businesses have positive QBI and there is no carryforward: skip Schedule C; Part II line 16 flows to Part IV line 27.

---

## The proportional allocation formula

```
For each negative-QBI business, allocate its loss to each positive-QBI business as:
  loss_to_business_i = (positive_QBI_i / sum_of_positive_QBIs) × total_negative_QBI
```

On the schedule: line 3 = negative amounts on line 1(a) plus the line 2 carryforward; line 4 = positive amounts on line 1(a); line 5 = smaller of |line 3| or line 4, apportioned to positive-QBI businesses in column (b); column (c) = (a) + (b), floored at zero → Form 8995-A line 2. After allocation, each positive-QBI business has a reduced QBI, which becomes its Line 2 input for Part II.

If the losses exceed the positive QBI: line 6 (line 3 − line 5) carries forward; this year's QBI component (Line 27) = $0.

---

## Worked Example A — Two businesses, one negative

**Input:**
- Business 1: QBI = $80,000 (positive)
- Business 2: QBI = ($30,000) (negative — a loss)
- Both are non-SSTB; taxable income is above the threshold (Form 8995-A applies)

**Allocation:**
- Sum of positive QBIs: $80,000
- Loss to Business 1: ($30,000) × ($80,000 / $80,000) = ($30,000) — allocated entirely to Business 1
- Business 1 QBI after netting: $80,000 − $30,000 = **$50,000**
- Business 2 QBI: $0 (the loss has been absorbed)

**Part II Line 2 inputs:**
- Business 1: $50,000
- Business 2: $0 (no further computation)

The W-2/UBIA limit then applies to Business 1 on the netted $50,000. Business 1's W-2 wages and UBIA are unchanged by the netting.

---

## Worked Example B — Three businesses, one negative

**Input:**
- Business 1: QBI = $100,000
- Business 2: QBI = $50,000
- Business 3: QBI = ($30,000)

**Allocation of the $30,000 loss:**
- Sum of positive QBIs: $100,000 + $50,000 = $150,000
- Loss to Business 1: $30,000 × (100,000/150,000) = $30,000 × 0.6667 = $20,000
- Loss to Business 2: $30,000 × (50,000/150,000) = $30,000 × 0.3333 = $10,000

**After netting:**
- Business 1 QBI: $100,000 − $20,000 = **$80,000**
- Business 2 QBI: $50,000 − $10,000 = **$40,000**
- Business 3 QBI: $0

**Part II Line 2 inputs:**
- Business 1: $80,000
- Business 2: $40,000
- Business 3: $0 (still report on Part I; Line 2 is $0)

---

## Worked Example C — Aggregate negative

**Input:**
- Business 1: QBI = $30,000
- Business 2: QBI = ($60,000)

**Net QBI: $30,000 − $60,000 = ($30,000) negative.**

This year's QBI component (Part IV Line 27) = $0. Schedule C line 6 shows the ($30,000) carryforward; it goes on next year's Schedule C (Form 8995-A) line 2 (or Form 8995 line 3) and reduces next year's QBI.

**Important:** The QBI loss carryforward does NOT reduce ordinary taxable income directly. It only reduces next year's QBI for §199A purposes. The loss is still deductible against ordinary income through the normal Schedule C / K-1 mechanisms (this is a separate concept).

---

## Interaction with the W-2 / UBIA limit

The loss netting happens FIRST, then the W-2/UBIA limit is applied to each business's netted QBI.

For a business with a negative QBI, the W-2 wages and UBIA of that business are NOT used for the W-2/UBIA limit calculation of any positive-QBI business. They're effectively ignored for the year (and don't carry forward).

---

## Interaction with REIT/PTP loss netting

REIT dividends and PTP income have their OWN loss netting on Part IV Lines 28-30. A negative QBI from a regular trade or business does NOT offset positive REIT/PTP income, and vice versa. They're tracked in two separate buckets.

---

## QBI loss carryforward — practical mechanics

If aggregate QBI is negative:

1. Line 27 = $0 this year
2. Negative amount carries to next year's Form 8995-A
3. Next year, the carryforward enters as a reduction to next year's QBI (treated as a separate qualifying business with negative QBI)
4. Apply the same loss-netting rules to next year's businesses
5. The carryforward continues to roll until offset by positive QBI

This continues indefinitely; there's no expiration on the QBI loss carryforward.

---

## Common mistakes

1. **Forgetting to net at all**: filer with two businesses (one positive, one negative) sums them in their head and enters the net on a single Part II row. Wrong — must use Schedule C of Form 8995-A.

2. **Netting REIT loss against business QBI**: not allowed. REIT/PTP losses are netted against REIT/PTP income only.

3. **Ignoring the carryforward**: if last year's Schedule C (Form 8995-A) line 6 (or Form 8995 line 16) was negative, it goes on this year's Schedule C line 2. (Line 29 of Form 8995-A is only for the REIT/PTP carryforward.) Software sometimes drops this between years.

4. **Allocating the loss disproportionately**: must be proportional to positive QBI, not by business size, age, or any other metric.

5. **Counting an SSTB above the phase-in top in the netting**: above the top of the range, no QBI, W-2 wages, or UBIA from the SSTB are taken into account (2025 i8995-A, "SSTBs excluded from your qualified trades or businesses"), so it is neither a positive nor a negative business on Schedule C. In the phase-in range, use the Schedule A line 11 amount (Schedule A line 11 says to enter it on Schedule C).
