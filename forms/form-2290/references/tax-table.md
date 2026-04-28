# Form 2290 — Tax Table and Computation

Detailed tax computation reference. Use after weight categories are determined per [`weight-categories.md`](./weight-categories.md).

---

## Annual Tax (Full Period)

For a vehicle in service on July 1 of the period start year, used for the full July 1 — June 30 period:

```
Standard tax = $100 + ($22 × thousands of lbs over 55,000)
               (capped at $550 for vehicles over 75,000 lbs)

Logging tax = Standard tax × 0.75
```

See [`weight-categories.md`](./weight-categories.md) for the full Category A-V table with annual amounts.

---

## Partial-Period Tax (Mid-Year First Use)

For a vehicle first used after July of the period start year, the tax is prorated by the number of months from first use through June.

```
Partial-period tax = Annual tax × (months remaining in period ÷ 12)
                     (rounded per IRS table on page 2)
```

The IRS publishes the exact partial-period amounts in the Tax Computation table on page 2 of Form 2290 — do not compute manually for filing. The math below shows the logic, but the published table is authoritative.

### Months Remaining by First-Use Month

| First Use Month | Months Remaining | Fraction |
|-----------------|------------------|----------|
| July | 12 | 12/12 (annual) |
| August | 11 | 11/12 |
| September | 10 | 10/12 |
| October | 9 | 9/12 |
| November | 8 | 8/12 |
| December | 7 | 7/12 |
| January | 6 | 6/12 |
| February | 5 | 5/12 |
| March | 4 | 4/12 |
| April | 3 | 3/12 |
| May | 2 | 2/12 |
| June | 1 | 1/12 |

### Worked Examples

**Example 1: Truck first used August 5**

- Weight: 75,000 lbs (Category U)
- Use: General hauling (non-logging)
- Annual tax: $540
- Partial-period tax: $540 × (11 ÷ 12) = $495.00

**Example 2: Truck first used January 14**

- Weight: 65,000 lbs (Category K)
- Use: General hauling
- Annual tax: $320
- Partial-period tax: $320 × (6 ÷ 12) = $160.00

**Example 3: Logging truck first used October 22**

- Weight: 60,000 lbs (Category F)
- Use: Logging
- Annual standard tax: $210
- Annual logging tax: $210 × 0.75 = $157.50
- Partial-period logging tax: $157.50 × (9 ÷ 12) = $118.13 (rounds per IRS table)

For each example, **the IRS published table is the authoritative number** — small rounding differences are normal between manual math and the table.

---

## Filing Deadline by First-Use Month

| First Use Month | Filing Deadline |
|-----------------|-----------------|
| July | August 31 |
| August | September 30 |
| September | October 31 |
| October | November 30 |
| November | December 31 |
| December | January 31 |
| January | February 28 (or 29 in leap years) |
| February | March 31 |
| March | April 30 |
| April | May 31 |
| May | June 30 |
| June | July 31 |

**Rule:** Last day of the month **following** the month of first use.

---

## Tax Computation per Vehicle — Worksheet

For each vehicle in the user's fleet, compute:

| Step | Input | Result |
|------|-------|--------|
| 1 | Vehicle taxable gross weight | Weight category (A-V or W) |
| 2 | Logging or general use? | Apply 25% reduction if logging |
| 3 | First use month | Determines annual vs. partial-period rate |
| 4 | Look up rate from IRS table | $X.XX |
| 5 | Verify against manual math | If off by more than $1, recheck weight category |

Sum the per-vehicle tax across the fleet → Form 2290 Line 2.

---

## Increased Weight Category Mid-Period (Line 3)

If a vehicle's customary operating weight increases mid-period (e.g., a tractor previously pulling 60,000-lb trailers starts pulling 78,000-lb trailers), the user must file an **Amended Return** (Box B) and pay additional tax on Line 3.

Calculation:

```
Months remaining = 12 − months elapsed since period start (July)

New annual tax  = annual rate for new (higher) weight category
Original tax paid = previously-paid annual tax for that vehicle

Line 3 (additional tax) = (New annual − Original) × (Months remaining ÷ 12)
```

**Example:** Tractor originally filed at Category K (65,000 lbs, $320). In December, it begins pulling heavier trailers, customarily operating at Category U (75,000 lbs, $540). January is the first full month of the new weight.

- Months remaining (Jan-Jun): 6
- Difference: $540 − $320 = $220
- Additional tax: $220 × (6 ÷ 12) = $110

File Amended Return with Box B checked, $110 on Line 3, updated Schedule 1 reflecting Category U.

---

## Credits (Line 5)

Credits reduce the current period's tax owed. Three scenarios:

### Scenario 1: Vehicle Sold During Prior Period

- Compute: Prior-period tax × (months remaining when sold ÷ 12)
- Example: Truck filed at $540 annual on July 1, 2024. Sold January 31, 2025. Months unused: Feb-Jun = 5. Credit = $540 × (5 ÷ 12) = $225.00

### Scenario 2: Vehicle Destroyed or Stolen During Prior Period

Same calculation as Scenario 1, using the date of destruction or theft.

### Scenario 3: Vehicle Used 5,000 Miles or Fewer (7,500 Agricultural) — Tax Was Paid

- Credit = full prior-period tax paid (since the vehicle should have been suspended)
- Example: Truck filed at $540 annual on July 1, 2024 (paid full tax). Mileage at June 30, 2025: 4,200 miles. Credit = $540.00

### Required: Supporting Statement

Attach a statement listing each credit:

| VIN | Reason | Date | Calculation | Credit |
|-----|--------|------|-------------|--------|
| 1XPXXX... | Sold | 01/31/2025 | $540 × 5/12 | $225.00 |
| 2NXXXX... | Under 5K mi | 06/30/2025 | Full | $540.00 |
| | | | **Total Line 5** | **$765.00** |

Without the statement, the IRS holds or denies the credit.

---

## Sanity Checks

When computing tax, verify:

- [ ] Per-vehicle tax never exceeds $550 (the maximum) for a single vehicle, full-period, non-logging
- [ ] Logging tax is exactly 75% of standard tax for the same category
- [ ] Partial-period tax is always less than the annual tax for the same vehicle
- [ ] Suspended (Category W) vehicles contribute $0 to Line 2 but still appear on Schedule 1
- [ ] Total Line 6 (Balance due) is at most Line 4 (Total tax) — Line 5 cannot exceed Line 4
- [ ] If Line 5 is high relative to Line 4, the user should be aware that excess credits may need to be claimed via Form 8849 (Claim for Refund of Excise Taxes) instead
