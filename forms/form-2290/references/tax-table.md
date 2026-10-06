# Form 2290 — Tax Table and Computation

Detailed tax computation reference. Use after weight categories are determined per [`weight-categories.md`](./weight-categories.md).

Verified against Form 2290 (Rev. July 2026) page 2 and the Partial-Period Tax Tables (Table I and Table II) on page 14 of the Instructions for Form 2290 (Rev. July 2026), period July 1, 2026, through June 30, 2027. Re-check both for each new July revision ([About Form 2290](https://www.irs.gov/forms-pubs/about-form-2290)).

---

## Annual Tax (Full Period)

For a vehicle first used on public highways in July (column (1) of page 2):

```
Standard tax = $100 + ($22 × each 1,000 lbs or fraction over 55,000)
               (capped at $550 for vehicles over 75,000 lbs; IRC §4481(a))

Logging tax = Standard tax × 0.75
```

See [`weight-categories.md`](./weight-categories.md) for the full Category A-V table with annual amounts.

---

## Partial-Period Tax (Mid-Year First Use)

For a vehicle first used after July of the period start year, the tax is prorated by the number of months from the first day of the first-use month through June 30 (IRC §4481(c)(1)).

```
Partial-period tax = Annual tax × (months remaining in period ÷ 12)
```

The IRS publishes the exact partial-period amounts in **Table I** (non-logging, enter in column (2)(a)) and **Table II** (logging, enter in column (2)(b)) at the end of the Instructions for Form 2290, not on the form. Copy the table amount. Table I matches the formula rounded to the cent; Table II amounts can be $0.01 lower than the formula (e.g., Category A logging, September: table $62.49, formula $62.50).

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
- Partial-period tax: $540 × (11 ÷ 12) = $495.00 (Table I, Category U, AUG (11) = $495.00)

**Example 2: Truck first used January 14**

- Weight: 65,000 lbs (Category K)
- Use: General hauling
- Annual tax: $320
- Partial-period tax: $320 × (6 ÷ 12) = $160.00 (Table I, Category K, JAN (6) = $160.00)

**Example 3: Logging truck first used October 22**

- Weight: 60,000 lbs (Category F)
- Use: Logging
- Annual standard tax: $210
- Annual logging tax: $210 × 0.75 = $157.50
- Partial-period logging tax: formula $157.50 × (9 ÷ 12) = $118.125; **Table II, Category F, OCT (9) = $118.12**. Enter $118.12.

For each example, **the IRS published table is the authoritative number** — small rounding differences are normal between manual math and the table.

---

## Filing Deadline by First-Use Month

| First Use Month | General rule | 2026-27 period (instructions chart) | Line 1 |
|-----------------|--------------|-------------------------------------|--------|
| July | August 31 | August 31, 2026 | 202607 |
| August | September 30 | September 30, 2026 | 202608 |
| September | October 31 | November 2, 2026 | 202609 |
| October | November 30 | November 30, 2026 | 202610 |
| November | December 31 | December 31, 2026 | 202611 |
| December | January 31 | February 1, 2027 | 202612 |
| January | February 28 (or 29 in leap years) | March 1, 2027 | 202701 |
| February | March 31 | March 31, 2027 | 202702 |
| March | April 30 | April 30, 2027 | 202703 |
| April | May 31 | June 1, 2027 | 202704 |
| May | June 30 | June 30, 2027 | 202705 |
| June | July 31 | August 2, 2027 | 202706 |

**Rule:** Last day of the month **following** the month of first use; if that day is a Saturday, Sunday, or legal holiday, the next business day. The deadline is not tied to the state registration date.

---

## Tax Computation per Vehicle — Worksheet

For each vehicle in the user's fleet, compute:

| Step | Input | Result |
|------|-------|--------|
| 1 | Vehicle taxable gross weight | Weight category (A-V or W) |
| 2 | Logging or general use? | Apply 25% reduction if logging |
| 3 | First use month | Determines annual vs. partial-period rate |
| 4 | Look up rate: page 2 column (1) for July, Table I / Table II for later months | $X.XX |
| 5 | Verify against manual math | If off by more than $1, recheck weight category |

Sum the per-vehicle tax across the fleet → Form 2290 Line 2.

---

## Increased Weight Category Mid-Period (Line 3)

If a vehicle's taxable gross weight increases mid-period and it falls into a new category (e.g., a tractor previously pulling lighter loads starts customarily carrying heavier ones), the user files Form 2290 with the **Amended Return** box checked (month of increase written next to it) and pays additional tax on Line 3, by the last day of the month following the month of the increase.

Calculation (Line 3 worksheet, instructions p. 6):

```
Month of increase = the month the taxable gross weight increased
New tax  = Partial-Period Tax Table amount, new category, month-of-increase column
Old tax  = Partial-Period Tax Table amount, previous category, same column
Line 3 (additional tax) = New tax − Old tax
(If the increase is in July, after the return was filed, use the page 2 annual amounts.)
```

**Example:** Tractor first used in July 2026 and filed at Category K (65,000 lbs, $320). In December 2026 its taxable gross weight rises to 75,000 lbs (Category U).

- New tax: Table I, Category U, DEC (7) = $315.00
- Old tax: Table I, Category K, DEC (7) = $186.67
- Additional tax: $315.00 − $186.67 = **$128.33**

File Form 2290 with the Amended Return box checked ("December" written next to it), $128.33 on Line 3, Schedule 1 listing the VIN under Category U, worksheet attached. Due January 31, 2027, which is a Sunday, so February 1, 2027.

---

## Credits (Line 5)

Credits reduce the tax on the return they are claimed on. Three scenarios:

### Scenario 1: Vehicle Sold Before June 1

- Compute (credit worksheet, instructions p. 7): tax previously reported on line 4 for the vehicle − partial-period tax for the months of use (first-use month through the month of sale; use the table column whose parenthesized month count equals the months of use)
- Example: Truck (Category U) first used July 2025, $540 paid for the 2025-26 period. Sold January 20, 2026, not used again by the seller. Months of use: July–January = 7. Partial-period tax for 7 months, Category U: $315.00. Credit = $540.00 − $315.00 = $225.00 (same as $540 × 5/12)
- Claim on the next Form 2290 filed (e.g., the 2026-27 return due August 31, 2026) or as a refund on Form 8849, Schedule 6. Include the purchaser's name and address.

### Scenario 2: Vehicle Destroyed or Stolen Before June 1

Same calculation as Scenario 1, using the month of destruction or theft. "Destroyed" means damaged so it isn't economical to rebuild (IRC §4481(c)(2)(B)).

### Scenario 3: Vehicle Used 5,000 Miles or Less (7,500 Agricultural) — Tax Was Paid

- Credit = full tax paid for that period (IRC §4483(d)(3))
- Can't be claimed until the period ends; claim it on the first Form 2290 filed for the next period, or on Form 8849
- Example: Truck filed at $540 annual for July 1, 2025 – June 30, 2026 (paid full tax). Highway mileage for that period: 4,200. Credit = $540.00 on the 2026-27 Form 2290

### Required: Supporting Statement

Attach a statement listing each credit:

| VIN | Reason | Date | Calculation | Credit |
|-----|--------|------|-------------|--------|
| 1XPXXX... | Sold (buyer name, address) | 01/20/2026 | $540.00 − $315.00 (7 months of use) | $225.00 |
| 2NXXXX... | Under 5,000 mi in 2025-26 | 06/30/2026 | Full tax paid | $540.00 |
| | | | **Total Line 5** | **$765.00** |

Line 5 can't exceed line 4 on the return; claim any excess on Form 8849 with Schedule 6. The instructions warn that a claim may be disallowed without the required information.

---

## Sanity Checks

When computing tax, verify:

- [ ] Per-vehicle tax never exceeds $550 (the maximum) for a single vehicle, full-period, non-logging
- [ ] Annual logging tax is exactly 75% of standard tax for the same category (partial-period logging amounts come from Table II and can be $0.01 below 75% × the Table I amount)
- [ ] Partial-period tax is always less than the annual tax for the same vehicle
- [ ] Suspended (Category W) vehicles contribute $0 to Line 2 but still appear on Schedule 1
- [ ] Total Line 6 (Balance due) is at most Line 4 (Total tax) — Line 5 cannot exceed Line 4
- [ ] If Line 5 is high relative to Line 4, the user should be aware that excess credits may need to be claimed via Form 8849 (Claim for Refund of Excise Taxes) instead
