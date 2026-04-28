# HSA Contribution Limits

Comprehensive reference for computing Form 8889 Line 3 (annual contribution limit). Authority: IRC §223(b); annual Revenue Procedure for inflation adjustments.

---

## Annual limits

| Tax year | Self-only | Family | Catch-up (55+) | Source |
|----------|-----------|--------|----------------|--------|
| 2024 | $4,150 | $8,300 | $1,000 | Rev. Proc. 2023-23 |
| 2025 | $4,300 | $8,550 | $1,000 | Rev. Proc. 2024-25 |
| 2026 | TBD | TBD | $1,000 (statutory) | Rev. Proc. 2025-XX (expected May–Jun 2025) |

The catch-up amount is set by **statute** at $1,000 and does not adjust for inflation. The self-only and family amounts adjust annually per IRC §223(g).

**Verify before filing**: For tax years 2026 and beyond, search the IRS site for "HSA inflation-adjusted amounts" or the most recent Revenue Procedure published in the preceding May–June.

---

## Computing Line 3

### Case 1: Eligible all 12 months, same coverage type

`Line 3 = annual limit for that coverage type`

Example (2025): family coverage all year → Line 3 = $8,550.

### Case 2: Partial-year eligibility, no last-month rule

Sum of monthly allowances:

```
For each month:
  Monthly allowance = (annual limit for that month's coverage) / 12
Line 3 = sum of all 12 monthly allowances
```

Example (2025): self-only Jan–Jun (no coverage Jul–Dec) → 6 × ($4,300 / 12) = 6 × $358.33 = $2,150.

### Case 3: Mixed coverage type during the year (no last-month rule)

For each month, take coverage on the first day:

```
Self-only month  : $4,300 / 12 = $358.33  (2025)
Family month     : $8,550 / 12 = $712.50  (2025)
No-coverage month: $0
```

Example (2025): self-only Jan–Apr, family May–Dec, all eligible →
4 × $358.33 + 8 × $712.50 = $1,433.33 + $5,700.00 = $7,133.33 → $7,133 (rounded).

### Case 4: Last-month rule

Eligible on December 1, regardless of earlier months:

`Line 3 = full annual limit for the coverage type held on December 1`

Example (2025): no HDHP Jan–Oct, family HDHP Nov–Dec, eligible on Dec 1 → Line 3 = $8,550.

**Testing period**: the user must remain HSA-eligible from December 1 of the contribution year through December 31 of the following calendar year (12 months from December 1 to November 30 of the next year, plus the requirement to be eligible on the testing-period anniversary).

If eligibility breaks during the testing period, the contribution amount that exceeded what proration would have allowed becomes:

- **Taxable income** on next year's Schedule 1, Line 8f (via Form 8889 Part III, Line 20)
- **Plus 10% additional tax** (Form 8889 Part III, Line 21 → Schedule 2, Line 17c)

### Case 5: Greater Coverage Rule

If the user has both self-only and family coverage during the year (changes mid-year), the **greater of**:

- Sum of monthly allowances per actual coverage, OR
- Family limit prorated by months of family coverage only

The IRS form instructions include this in the Limitation Chart. In practice, if the user had family coverage at any point and is eligible on December 1 with family coverage, the last-month rule + family limit usually wins — but document the comparison.

---

## Catch-up contribution (Line 7)

- $1,000, statutory, no inflation adjustment
- Available to anyone age 55 or older by end of tax year **and** HSA-eligible
- Each spouse age 55+ can take their own $1,000 catch-up — but it must go into **their own** HSA

**Common error**: Spouse A is 55+ with no HSA of their own. They cannot make a catch-up into Spouse B's HSA. To use the catch-up, Spouse A must open their own HSA.

If a spouse age 55+ has only a few months of HSA-eligibility, the catch-up is **also prorated** unless they invoke the last-month rule.

---

## MFJ family-limit splitting

When both spouses are covered under a single family HDHP, the family contribution limit is **shared** between them, not doubled. The split is by agreement, documented on each spouse's Line 6.

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

Example: User contributes $4,000 on March 15, 2026, and tells the custodian it's for tax year 2025. The 5498-SA for 2025 will reflect the $4,000 prior-year contribution. Form 8889 for 2025 (filed by April 15, 2026) will include the $4,000 on Line 2.

The cutoff is the **unextended** filing deadline (typically April 15). Filing an extension on Form 4868 does **not** extend the HSA contribution deadline.

---

## Excess contribution mechanics

If `Line 2 + Line 9 > Line 8`, the excess is subject to a **6% excise tax every year** until removed. Computed on Form 5329 Part VII.

To avoid the excise tax, withdraw the excess plus the **earnings on the excess** before the unextended filing deadline (with extensions). The custodian has a procedure for this (usually a "return of excess contribution" form).

The earnings withdrawn are taxable income for the year of the original excess (not the year of withdrawal). Report on Schedule 1, Line 8f.

If the user has already filed and discovers the excess after April 15, they have two choices:

1. **Withdraw and amend** (file 1040-X) — earnings still taxable
2. **Leave the excess in and pay 6% per year** — and apply the excess against future-year contributions until used up (but they remain subject to the 6% each year the excess sits)

---

## Worked examples

### Example A: Self-only, full year

User had self-only HDHP all 12 months of 2025, age 30, contributed $5,000 directly.

```
Line 1: Self-only
Line 2: $5,000  (but capped — actual deduction limited)
Line 3: $4,300
Line 8: $4,300
Line 12: min($5,000 + $0, $4,300) = $4,300
Line 13: min($5,000, $4,300 − $0) = $4,300
```

Excess = $5,000 − $4,300 = $700. Must withdraw $700 + earnings or pay 6% excise tax.

### Example B: Mid-year coverage start, no last-month rule

User started family HDHP on July 1, 2025 (eligible on first of July), age 35, contributed $3,000 directly.

Eligible months: Jul, Aug, Sep, Oct, Nov, Dec = 6 months
Monthly allowance: $8,550 / 12 = $712.50
Line 3 (prorated): 6 × $712.50 = $4,275

```
Line 1: Family (coverage on Dec 1)
Line 2: $3,000
Line 3: $4,275
Line 8: $4,275
Line 13: $3,000  (within limit)
```

### Example C: Mid-year coverage with last-month rule

Same facts as Example B, but user opts into last-month rule.

```
Line 1: Family
Line 2: $3,000
Line 3: $8,550  (full annual via last-month rule)
Line 8: $8,550
Line 13: $3,000
```

User now must remain HSA-eligible through December 31, 2026. If they lose eligibility (e.g., switch to non-HDHP in 2026), Part III applies on the 2026 return:

```
Line 18 (2026): $8,550 − $4,275 = $4,275 (excess over what proration would have allowed)
Line 20 (2026): $4,275 → Schedule 1, Line 8f
Line 21 (2026): $4,275 × 10% = $428 → Schedule 2, Line 17c
```

### Example D: MFJ family HDHP, both with HSAs

Both spouses age 35, family HDHP all year, agreed split: 50/50.

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
