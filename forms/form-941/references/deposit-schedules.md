# Form 941 Deposit Schedules

How to determine whether an employer is a monthly or semi-weekly depositor, when each schedule's deposits are due, and how to fill Schedule B (Form 941). Use when the agent needs to fill Line 16 or attach Schedule B.

Authority: IRC §6302; IRS Reg. §31.6302-1; IRS Pub. 15 (Circular E), section 11.

---

## Why deposit schedule matters

The IRS does not let employers wait until the quarter ends to remit payroll taxes. Instead, employers must deposit federal employment taxes (Lines 3 + 5e — i.e., FIT withholding + FICA) on a recurring schedule, with the schedule frequency tied to the employer's lookback-period total liability.

Failure to deposit on schedule triggers the Federal Tax Deposit (FTD) penalty under IRC §6656:

| Days late | Penalty rate |
|-----------|--------------|
| 1–5 days | 2% |
| 6–15 days | 5% |
| 16+ days | 10% |
| 10+ days after IRS notice demanding payment | 15% |

Penalties stack with interest on the unpaid amount. Repeated FTD failures can trigger 100% Trust Fund Recovery Penalty (TFRP) against responsible individuals personally (IRC §6672).

---

## Step 1 — Determine the lookback period

The lookback period for a given calendar year is the **12-month period from July 1 of two years prior through June 30 of one year prior**.

| Filing year | Lookback period |
|-------------|----------------|
| 2026 | July 1, 2024 — June 30, 2025 |
| 2027 | July 1, 2025 — June 30, 2026 |

Sum **all four quarters' Line 12** (total taxes after credits) reported on Forms 941 filed during the lookback period.

For new employers without a full lookback period: default to **monthly** depositor.

---

## Step 2 — Apply the threshold

| Lookback Line 12 sum | Schedule for filing year |
|----------------------|--------------------------|
| ≤ $50,000 | Monthly |
| > $50,000 | Semi-weekly |

This determination is made **once at the start of each calendar year** and applies for the entire year (with one exception, below).

### Exception — $100,000 next-day deposit rule

Regardless of the assigned schedule, if accumulated unpaid tax on any single day ≥ $100,000, the employer must deposit it by the **next banking day**. Once this rule is triggered, the employer **automatically becomes semi-weekly** for the rest of the current calendar year and the entire next calendar year (IRS Reg. §31.6302-1(c)(3)).

### Exception — De minimis ($2,500 quarterly)

If total Line 12 for the quarter < $2,500 *and* prior quarter Line 12 < $2,500, deposits are not required — pay the balance with the return (Line 14 amount). This is Box 1 on Line 16. Most very-small employers (1-2 employees, low wages) use this.

---

## Step 3 — Deposit due dates

### Monthly schedule

Deposits are due by the **15th of the following month** for taxes incurred during a calendar month.

| Month | Due date |
|-------|----------|
| January wages | February 15 |
| February wages | March 15 |
| March wages | April 15 |
| April wages | May 15 |
| ... | ... |

If the 15th falls on a weekend or federal holiday, the next banking day applies.

### Semi-weekly schedule

Deposits are due based on the day wages were paid:

| Pay date | Deposit due |
|----------|------------|
| Wednesday, Thursday, Friday | Following Wednesday |
| Saturday, Sunday, Monday, Tuesday | Following Friday |

Special rule: if the deposit period spans a federal holiday, three banking days are added to the deposit due date.

### Where to deposit

All deposits must be electronic via **EFTPS** (Electronic Federal Tax Payment System). Paper coupons (Form 8109) were discontinued in 2011. Sign up at https://www.eftps.gov.

---

## Step 4 — Box selection on Line 16

| Box | When to check | What to fill |
|-----|---------------|--------------|
| 1 | Quarterly liability < $2,500 *and* prior quarter < $2,500 *and* no $100K next-day trigger | Nothing else — pay with return |
| 2 | Monthly depositor | Three month-totals; sum = Line 12 |
| 3 | Semi-weekly depositor (or $100K rule triggered) | Attach Schedule B (Form 941) |

If exactly one of the conditions changes mid-quarter (e.g., the $100K rule triggers in month 2), Box 3 applies retroactively for the whole quarter — fill Schedule B for all three months.

---

## Step 5 — Filling Schedule B (semi-weekly only)

Schedule B (Form 941) is a 3-month grid (one column per month) listing daily liability for each day of the quarter.

```
Month 1 (e.g., January)
Day  1: $X.XX
Day  2: $X.XX
...
Day 31: $X.XX
Total month 1: $X,XXX.XX

Month 2 (e.g., February)
Day  1: $X.XX
...

Month 3 (e.g., March)
Day  1: $X.XX
...

Total quarter (Line 26): $X,XXX.XX  ← MUST equal Form 941 Line 12
```

### What to enter for each day

Enter the **liability** incurred on that day, not the deposit. Liability = FIT withheld + employee FICA + employer FICA on wages paid that day.

If no wages paid that day: leave blank or enter $0 (either is acceptable; software typically blanks).

### Important: liability date vs. deposit date

Schedule B reports liability on the **wage-payment date**, regardless of when the deposit was actually made. If the employer paid wages on January 15 and deposited on January 17, the liability goes on January 15.

### Total at bottom

The grand total at the bottom of Schedule B (sum of all daily entries across all three months) **must equal Form 941 Line 12**. If it doesn't, one of:
- Schedule B has a missing or wrong daily entry
- Form 941 has a math error
- An adjustment on Lines 7–9 wasn't reflected

The IRS cross-checks this; a mismatch generates CP207 / CP207L notices.

---

## Step 6 — Form 945-A (alternative liability schedule)

Form 945-A is for employers who are also semi-weekly depositors of *non-payroll* withholding (e.g., backup withholding on 1099-MISC, withholding on pensions). Most 941 filers don't need it. Only relevant if the employer files Form 945 separately.

For 941, Schedule B is the standard daily liability schedule.

---

## Step 7 — Special situations

### New employers

Default to **monthly** for the first calendar year (no lookback period exists). Switch to semi-weekly the next year if the lookback exceeds $50,000.

### Successor employers (M&A)

If the employer acquired the business of a predecessor, both employers' Line 12 amounts during the lookback period count toward the threshold. See IRS Pub. 15 for predecessor / successor rules and Form 941 line H.

### Quarterly $2,500 threshold mid-year

If the quarterly liability hits $2,500 in any quarter, the employer must deposit per their assigned schedule (monthly or semi-weekly) — Box 1 no longer applies. The quarterly election doesn't carry forward automatically.

### Year-end true-up

At the end of the year, the employer reconciles deposits to actual liability. Any underpayment is paid with Q4 941 (Line 14) — but if total under-deposit > $2,500, it's already past the deposit deadline and FTD penalty applies.

---

## Common deposit-schedule mistakes

1. **Confusing deposit date with liability date on Schedule B.** Liability follows the wage-pay date.
2. **Forgetting to check the lookback period each January.** An employer who grew during the year may be due for a schedule change.
3. **Missing the $100K next-day rule.** A one-time large bonus can trigger semi-weekly status for ~18 months.
4. **Using monthly schedule when previous quarter exceeded the de minimis cap.** Box 1 only applies if both current and prior quarter < $2,500.
5. **Schedule B totals don't match Line 12.** This generates CP207 every time. Cross-check before submission.
6. **Failing to deposit through EFTPS.** Paper or check deposits are not accepted; the IRS treats them as not made.
7. **Forgetting the three-banking-day extension when a federal holiday falls in the semi-weekly period.**

---

## References

- IRC §6302 — mode of collecting tax
- IRC §6656 — failure-to-deposit penalty
- IRC §6672 — Trust Fund Recovery Penalty
- IRS Reg. §31.6302-1 — deposit schedule mechanics
- [Pub. 15 (Employer's Tax Guide)](https://www.irs.gov/pub/irs-pdf/p15.pdf) — section 11 on depositing taxes
- [Schedule B (Form 941)](https://www.irs.gov/pub/irs-pdf/f941sb.pdf) — the form itself
- [Instructions for Schedule B (Form 941)](https://www.irs.gov/pub/irs-pdf/i941sb.pdf) — IRS guidance
- [EFTPS](https://www.eftps.gov) — electronic deposit system
