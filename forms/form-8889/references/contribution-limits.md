# HSA Contribution Limits

Comprehensive reference for computing Form 8889 Line 3 (annual contribution limit). Authority: IRC §223(b); annual Revenue Procedure for inflation adjustments.

---

## Annual limits

| Tax year | Self-only | Family | Catch-up (55+) | Source |
|----------|-----------|--------|----------------|--------|
| 2024 | $4,150 | $8,300 | $1,000 | Rev. Proc. 2023-23 |
| 2025 | $4,300 | $8,550 | $1,000 | Rev. Proc. 2024-25 |
| 2026 | $4,400 | $8,750 | $1,000 (statutory) | Rev. Proc. 2025-19 |
| 2027 | $4,500 | $9,000 | $1,000 (statutory) | Rev. Proc. 2026-24 |

The catch-up amount is set by **statute** at $1,000 and does not adjust for inflation (IRC §223(b)(3)(B)). The self-only and family amounts adjust annually per IRC §223(g).

**Verify before filing**: For later years, search the IRS site for "HSA inflation-adjusted amounts" or the most recent Revenue Procedure published in the preceding May–June.

---

## Computing Line 3

### Case 1: Eligible all 12 months, same coverage type

`Line 3 = annual limit for that coverage type`

Example (2025): family coverage all year → Line 3 = $8,550.

### Case 2: Not eligible on December 1 (Line 3 Limitation Chart and Worksheet)

Sum of monthly allowances:

```
For each month:
  Monthly allowance = (annual limit for that month's coverage) / 12
  (55+ at year-end: self-only $5,300; family $9,550 only if unmarried — 2025)
Line 3 = sum of all 12 monthly allowances
```

Example (2025): self-only Jan–Jun (no coverage Jul–Dec), age 40 → 6 × ($4,300 / 12) = 6 × $358.33 = $2,150.

### Case 3: Mixed coverage type during the year, eligible all year

The worksheet sum, month by month on the first day:

```
Self-only month  : $4,300 / 12 = $358.33  (2025)
Family month     : $8,550 / 12 = $712.50  (2025)
No-coverage month: $0
```

Example (2025): self-only Jan–Apr, family May–Dec, all eligible →
4 × $358.33 + 8 × $712.50 = $1,433.33 + $5,700.00 = $7,133.33.

But Line 3 is the **greater** of the worksheet result or the full amount for the December 1 coverage (Case 5). Family coverage on December 1 → Line 3 = $8,550. Contributions above $7,133.33 depend on the last-month rule and are exposed to the testing period.

### Case 4: Last-month rule

Eligible on December 1, regardless of earlier months:

`Line 3 = full annual limit for the coverage type held on December 1`

Example (2025): no HDHP Jan–Oct, family HDHP Nov–Dec, eligible on Dec 1 → Line 3 = $8,550.

**Testing period**: the user must remain HSA-eligible from December 1 of the contribution year through December 31 of the following calendar year (example: December 1, 2025 – December 31, 2026).

If eligibility breaks during the testing period (other than death or disability), the contributions made above what the worksheet would have allowed without the last-month rule become:

- **Income** in the year of failure, Schedule 1, Line 8f (via Form 8889 Part III, Line 18 → Line 20)
- **Plus 10% additional tax** (Form 8889 Part III, Line 21 → Schedule 2, Line 17d)

### Case 5: Coverage type changed, eligible (or treated as eligible) all year

Line 3 is the **greater of** (2025 Instructions for Form 8889, Line 3 rule 4; Pub. 969 (2025), Limit on Contributions):

- The Line 3 Limitation Chart and Worksheet result (sum of monthly allowances ÷ 12), OR
- The full annual amount for the coverage held on the first day of the last month (December 1)

Family coverage on December 1 → enter the full family amount; no worksheet needed. Self-only on December 1 after earlier family months → the worksheet usually wins. Document the comparison.

---

## Catch-up (additional) contribution — Line 3 or Line 7

- $1,000, statutory, no inflation adjustment
- Available to anyone age 55 or older by end of tax year **and** HSA-eligible (not enrolled in Medicare)
- Unmarried, or married with self-only coverage all year: included on **Line 3** (worksheet months use $5,300 self-only / $9,550 family for 2025)
- Married and the user or spouse had family coverage: entered on **Line 7** = $1,000 × eligible months ÷ 12
- Each spouse age 55+ can take their own $1,000 — but it must go into **their own** HSA

**Common error**: Spouse A is 55+ with no HSA of their own. They cannot make a catch-up into Spouse B's HSA. To use the catch-up, Spouse A must open their own HSA.

If a person age 55+ has only a few months of HSA-eligibility, the catch-up is **also prorated** unless the last-month rule applies.

---

## MFJ family-limit splitting

When either spouse has family HDHP coverage and both are eligible individuals, the family contribution limit is **shared** between them, not doubled. It is split equally unless they agree on a different division, documented on each spouse's Line 6.

Example (2025, family HDHP, both spouses HSA-eligible all 12 months):

| Spouse | Line 6 (allocated share) | Line 7 (catch-up if 55+) | Line 8 |
|--------|--------------------------|---------------------------|--------|
| A | $5,000 | $0 (under 55) | $5,000 |
| B | $3,550 | $0 (under 55) | $3,550 |
| Total | $8,550 | — | — |

The allocation can be 100/0 if only one spouse has an HSA, or any split that totals to $8,550. Each spouse's Line 7 catch-up is added separately to their own Line 8.

---

## Prior-year designation (the April 15 rule)

Contributions made between January 1 and April 15 of the next year can be designated for **either** the prior year or the current year. The designation must be communicated to the custodian on the deposit slip — most custodians default to the current year if not specified.

Example: User contributes $4,000 on March 15, 2026, and tells the custodian it's for tax year 2025. The 2025 Form 5498-SA box 3 will show the $4,000 contribution made in 2026 for 2025. Form 8889 for 2025 (filed by April 15, 2026) will include the $4,000 on Line 2.

The cutoff is the **unextended** filing deadline (typically April 15). Filing an extension on Form 4868 does **not** extend the HSA contribution deadline.

---

## Excess contribution mechanics

If `Line 2 + Line 9 > Line 8`, the excess is subject to a **6% excise tax every year** until removed. Computed on Form 5329 Part VII.

To avoid the excise tax, withdraw the excess plus the **earnings on the excess** by the due date of the return, including extensions, and do not deduct the withdrawn amount. The custodian has a procedure for this (usually a "return of excess contribution" form).

The earnings withdrawn are included in "Other income" for the year the contributions and earnings are withdrawn (2025 Instructions for Form 8889, Line 13).

If the user already filed on time without withdrawing, they have two choices:

1. **Withdraw within 6 months of the original due date (excluding extensions) and amend** — file an amended return with "Filed pursuant to section 301.9100-2" at the top and an explanation; earnings still taxable
2. **Leave the excess in and pay 6% per year** — the excess is absorbed when a later year's contributions are below that year's limit (Form 5329 Part VII, Line 43), and it remains subject to the 6% each year it sits

---

## Worked examples

### Example A: Self-only, full year

User had self-only HDHP all 12 months of 2025, age 30, contributed $5,000 directly.

```
Line 1: Self-only
Line 2: $5,000  (but capped — actual deduction limited)
Line 3: $4,300
Line 8: $4,300
Line 12: $4,300 − $0 = $4,300
Line 13: smaller of $5,000 or $4,300 = $4,300
```

Excess = $5,000 − $4,300 = $700. Must withdraw $700 + earnings or pay 6% excise tax.

### Example B: Mid-year coverage start, no last-month rule

User started family HDHP on July 1, 2025 (eligible on first of July), age 35, contributed $3,000 directly.

Eligible months: Jul, Aug, Sep, Oct, Nov, Dec = 6 months
Monthly allowance: $8,550 / 12 = $712.50
Worksheet amount: 6 × $712.50 = $4,275

The user is eligible on December 1, so the last-month rule applies and Line 3 = $8,550 (Example C). The $3,000 contribution is below the $4,275 worksheet amount, so none of it depends on the last-month rule.

```
Line 1: Family (coverage on Dec 1)
Line 2: $3,000
Line 13: $3,000  (within limit)
```

### Example C: Mid-year coverage with last-month rule

Same facts as Example B.

```
Line 1: Family
Line 2: $3,000
Line 3: $8,550  (full annual via last-month rule)
Line 8: $8,550
Line 12: $8,550
Line 13: $3,000
```

If the user loses eligibility in 2026 (e.g., switches to a non-HDHP), Part III on the 2026 return uses the amount actually contributed: Line 18 = $3,000 − $4,275 → $0. No income, no 10% tax.

Had the user contributed the full $8,550, the 2026 Part III would show:

```
Line 18 (2026): $8,550 − $4,275 = $4,275 (contributed above the worksheet amount)
Line 20 (2026): $4,275 → Schedule 1, Line 8f
Line 21 (2026): $4,275 × 10% = $427.50 → $428 → Schedule 2, Line 17d
```

### Example D: MFJ family HDHP, both with HSAs

Both spouses age 35, family HDHP all year, split 50/50 (the default when they make no other agreement).

| Spouse | Line 1 | Line 2 | Line 6 | Line 8 | Line 13 |
|--------|--------|--------|--------|--------|---------|
| A | Family | $4,275 | $4,275 | $4,275 | $4,275 |
| B | Family | $4,275 | $4,275 | $4,275 | $4,275 |

Total combined deduction = $8,550 = family limit. Each files their own Form 8889.

### Example E: Both spouses age 55+

Family HDHP, agreed 50/50 split, both age 56.

| Spouse | Line 1 | Line 2 | Line 6 | Line 7 | Line 8 | Line 13 |
|--------|--------|--------|--------|--------|--------|---------|
| A | Family | $5,275 | $4,275 | $1,000 | $5,275 | $5,275 |
| B | Family | $5,275 | $4,275 | $1,000 | $5,275 | $5,275 |

Total combined = $10,550. Each catch-up went into the contributor's own HSA.

If only Spouse A had an HSA, Spouse B could not contribute their $1,000 catch-up into Spouse A's HSA. To take advantage, Spouse B must open their own HSA.
