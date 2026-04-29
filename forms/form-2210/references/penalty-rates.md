# Form 2210 — Penalty Rates

The underpayment penalty rate is the **federal short-term rate plus 3 percentage points**, set by IRS Revenue Ruling each calendar quarter under IRC §6621. The rate compounds daily.

## Where the rate comes from

IRC §6621 sets the underpayment rate at:

```
Underpayment rate = federal short-term rate + 3%
```

The federal short-term rate is determined under IRC §1274(d) and announced monthly by the IRS. The penalty rate is set quarterly using the average for the first month of each quarter (October, January, April, July). It applies to the *following* quarter.

## Where to find the current rate

1. **IRS Newsroom announcements** — released roughly mid-month of the second month of each quarter, announcing the rate for the next quarter (e.g., late February announcement for Q2 rates effective April 1).

2. **Form 2210 instructions** — the current-year Form 2210 instructions include a rate table showing the rates that applied during each quarter of the tax year being filed. This is the authoritative source for filers using Form 2210 — read the rate table directly from the current instructions and use those rates verbatim.

3. **Revenue Rulings** — each rate is published in a Revenue Ruling (e.g., Rev. Rul. 2024-25 set Q1 2025 rates; the numbering scheme is "year-issuance number"). The Form 2210 instructions cite the relevant rulings.

## Recent rates (verify before using)

The rates have varied as the federal short-term rate has fluctuated. Approximate recent quarterly underpayment rates:

| Period | Approx. annualized rate (verify against current Form 2210 instructions) |
|--------|----------------|
| Q1 2025 | 8% |
| Q2 2025 | 8% |
| Q3 2025 | 8% |
| Q4 2025 | 8% |
| Q1 2026 | TBD (verify against current Form 2210 instructions) |

**Do not use these as authoritative figures** — the agent must always pull the current rate table from the current-year Form 2210 instructions (https://www.irs.gov/pub/irs-pdf/i2210.pdf) before computing a penalty.

## How daily compounding works

The underpayment penalty compounds *daily*, which means:

```
Daily rate = annual rate / 365
Penalty for an underpayment outstanding for D days = underpayment × ((1 + daily rate)^D − 1)
```

In practice, Form 2210's worksheet uses a simplified linear approximation (`underpayment × annual rate × days/365`) for ease of hand computation, which produces a slightly lower penalty than true daily compounding. The IRS accepts the linear approximation per the form's worksheet — don't try to "improve" it with compound interest.

For computing a quarterly penalty:

```
Penalty = underpayment × annual_rate × (days_late / 365)

days_late = days between quarter due date and the earlier of:
            - the date the underpayment is satisfied, OR
            - April 15 of the year following the tax year
```

## The four quarter due dates (calendar-year individual filers)

| Quarter | Period | Due date |
|---------|--------|----------|
| Q1 | January 1 – March 31 | April 15 |
| Q2 | April 1 – May 31 | June 15 |
| Q3 | June 1 – August 31 | September 15 |
| Q4 | September 1 – December 31 | January 15 of following year |

The Q2 period is only 2 months (April + May), Q3 is 3 months (June, July, August), Q4 is 4 months (September through December). The unequal periods are codified at IRC §6654(c) and have been the same since 1981.

If a due date falls on a weekend or federal holiday, it shifts to the next business day. The current-year Form 2210 instructions list the actual due dates with any weekend/holiday shifts.

## Computing the penalty period

For each quarterly underpayment, the penalty accrues from the quarter's due date until the underpayment is satisfied (by a later payment) or the return is filed by April 15 — whichever is earlier.

**A subtle point**: the penalty stops accruing on April 15 of the following year *regardless of when the return is actually filed*. If the filer files on October 15 (extension), the penalty does not extend to October 15 — it stopped on April 15 because that's when the underpaid tax was *due* in the IRC sense.

If the filer files an extension (Form 4868) and pays additional tax with the extension, that payment date counts as the satisfaction date for any remaining underpayment.

## Example penalty computation

Filer's Q1 underpayment is $3,000. Filer paid $0 in Q1, $0 in Q2, then made up the underpayment with a $3,000 estimated tax payment on June 15 (Q2 due date).

```
Days late for Q1: April 15 to June 15 = 61 days
Annual rate: assume 8%
Penalty = $3,000 × 0.08 × (61 / 365) = $40
```

Now suppose the filer instead paid $0 in Q1 and Q2, and made the $3,000 payment on September 15 (Q3 due date):

```
Days late for Q1: April 15 to September 15 = 153 days
Penalty = $3,000 × 0.08 × (153 / 365) = $101
```

But also: the Q2 required installment was probably also underpaid, which means *additional* penalty for Q2 as well. The penalty stacks across quarters that are underpaid.

## Penalty stacking across quarters

If the filer is underpaid in Q1, Q2, Q3, and Q4 — each quarter accrues its own penalty against its own underpayment from its own due date. The total penalty is the sum.

A late Q4 estimated payment satisfies Q4 but doesn't retroactively undo Q1, Q2, or Q3 penalties. This is the "back-fill misconception" — filers sometimes think a big January 15 payment makes everything right; it doesn't.

## When the rate table changes mid-tax-year

The rate is set quarterly. If a tax year spans multiple rate quarters (which it always does, since the year has four IRS quarterly rate periods), the agent applies the rate that was in effect during the period the underpayment was outstanding.

For example, an underpayment from April 15 outstanding to August 1 would accrue:
- April 15 to June 30: at the Q2 rate
- July 1 to August 1: at the Q3 rate

Form 2210's worksheet handles this by splitting the penalty period into the relevant rate-quarter sub-periods. The current-year instructions show a sample computation.

## What the agent should do

1. Pull the current-year rate table from the Form 2210 instructions PDF
2. For each quarterly underpayment, identify the penalty period (due date → satisfaction date or 4/15)
3. Split the period into rate-quarter sub-periods if the rate changed
4. Compute penalty = underpayment × rate × (days / 365) for each sub-period
5. Sum across sub-periods and quarters

The agent should NOT:
- Use a stale rate from a prior year (rates change)
- Apply true daily compounding (the form uses linear approximation)
- Apply a "blended" rate across the whole year (the form requires period-by-period computation)

## Sources

- IRC §6621 — Determination of penalty rate (federal short-term rate + 3%)
- IRC §1274(d) — Federal short-term rate definition
- IRC §6654(c) — Quarterly installment due dates
- [Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/f2210.pdf) — penalty worksheet
- [Instructions for Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/i2210.pdf) — quarterly rate table for the tax year being filed
- [IRS Underpayment Rates archive](https://www.irs.gov/payments/quarterly-interest-rates) — historical rate announcements
