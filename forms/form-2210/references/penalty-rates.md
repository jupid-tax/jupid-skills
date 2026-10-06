# Form 2210 — Penalty Rates

The underpayment penalty rate is the **federal short-term rate plus 3 percentage points**, set by IRS Revenue Ruling each calendar quarter under IRC §6621. The §6654 penalty is simple interest: the daily compounding rule of IRC §6622(a) does not apply to it (IRC §6622(b)).

## Where the rate comes from

IRC §6621 sets the underpayment rate at:

```
Underpayment rate = federal short-term rate + 3%
```

The federal short-term rate is determined under IRC §1274(d) and announced monthly by the IRS. The penalty rate is set quarterly using the federal short-term rate for the first month of each quarter (October, January, April, July), rounded to the nearest full percent. It applies to the *following* quarter (IRC §6621(b)(1)–(3)). For the §6654 penalty, the rate in effect for March also applies to April 1–15 of the following year (IRC §6621(b)(2)(B)), which is why the last rate period on the worksheet runs January 1–April 15.

## Where to find the current rate

1. **IRS Newsroom announcements** — released roughly mid-month of the second month of each quarter, announcing the rate for the next quarter (e.g., late February announcement for Q2 rates effective April 1).

2. **Form 2210 instructions** — the penalty worksheet in the current-year instructions (Worksheet for Form 2210, Part III, Section B) prints the rate for each rate period. This is the authoritative source for filers using Form 2210 — read the rates directly from the worksheet and use them verbatim. The 2025 worksheet uses 0.07 for all four periods.

3. **Revenue Rulings** — each rate is published in a Revenue Ruling (e.g., Rev. Rul. 2024-25, IRB 2024-49, set the Q1 2025 underpayment rate at 7%; the numbering scheme is "year-issuance number"). The IRS quarterly interest rates page lists the bulletin for each quarter.

## Recent rates

Underpayment rates (non-corporate) from https://www.irs.gov/payments/quarterly-interest-rates, checked 2026-10-06:

| Period | Underpayment rate | Source |
|--------|-------------------|--------|
| Q1 2025 | 7% | IRB 2024-49 (Rev. Rul. 2024-25) |
| Q2 2025 | 7% | IRB 2025-13 |
| Q3 2025 | 7% | IRB 2025-23 |
| Q4 2025 | 7% | IRB 2025-37 |
| Q1 2026 | 7% | IRB 2025-48 |
| Q2 2026 | 6% | IRB 2026-8 |
| Q3 2026 | 7% | IRB 2026-22 (Rev. Rul. 2026-10) |
| Q4 2026 | 7% | IRB 2026-36 (Rev. Rul. 2026-15) |
| Q1 2027 | not yet published | |

For 2025 underpayments the 2025 Form 2210 worksheet uses 0.07 in every rate period. For 2026 underpayments, use the 2026 Form 2210 instructions when they are published; until then the rates above apply and the January–April 15, 2027 rate is unknown.

## Simple interest, not compounding

The §6654 penalty is figured as simple interest on each underpayment for the days it is unpaid. IRC §6622(a) compounds interest daily, but §6622(b) excludes the §6654 addition to tax. The worksheet formula is exact, not an approximation — don't compound it.

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

The Q2 period is only 2 months (April + May), Q3 is 3 months (June, July, August), Q4 is 4 months (September through December). The due dates are codified at IRC §6654(c); the annualization periods follow from IRC §6654(d)(2)(B) (months ending before each due date).

If a due date falls on a Saturday, Sunday, or legal holiday, a payment on the next business day counts as made on the due date. The 2025 form keeps 6/15/25 as the column (b) date even though June 15, 2025 was a Sunday, and the instructions treat a June 16 payment as timely.

## Computing the penalty period

For each quarterly underpayment, the penalty accrues from the quarter's due date until the underpayment is satisfied (by a later payment) or the return is filed by April 15 — whichever is earlier.

**A subtle point**: the penalty stops accruing on April 15 of the following year *regardless of when the return is actually filed*. If the filer files on October 15 (extension), the penalty does not extend to October 15 — it stopped on April 15 because that's when the underpaid tax was *due* in the IRC sense.

If the filer files an extension (Form 4868) and pays additional tax with the extension, that payment date counts as the satisfaction date for any remaining underpayment.

## Example penalty computation

Filer's Q1 underpayment is $3,000. Filer paid $0 in Q1, $0 in Q2, then made up the underpayment with a $3,000 estimated tax payment on June 15 (Q2 due date).

```
Days late for Q1: April 15 to June 15 = 61 days
Annual rate: 7% (2025 worksheet rate)
Penalty = $3,000 × 0.07 × (61 / 365) = $35.10
```

Now suppose the filer instead paid $0 in Q1 and Q2, and made the $3,000 payment on September 15 (Q3 due date):

```
Days late for Q1: April 15 to September 15 = 153 days
Penalty = $3,000 × 0.07 × (153 / 365) = $88.03
```

But also: the Q2 required installment was probably also underpaid, which means *additional* penalty for Q2 as well. The penalty stacks across quarters that are underpaid.

## Penalty stacking across quarters

If the filer is underpaid in Q1, Q2, Q3, and Q4 — each quarter accrues its own penalty against its own underpayment from its own due date. The total penalty is the sum.

A late payment is applied first to the oldest unpaid installment (IRC §6654(b)(3)), so a big January 15 payment stops the Q1, Q2, and Q3 underpayments from accruing further, but the penalty they accrued up to January 15 stays. This is the "back-fill misconception" — filers sometimes think a big January 15 payment makes everything right; it doesn't.

## When the rate table changes mid-tax-year

The rate is set quarterly. If a tax year spans multiple rate quarters (which it always does, since the year has four IRS quarterly rate periods), the agent applies the rate that was in effect during the period the underpayment was outstanding.

For example, an underpayment from April 15 outstanding to August 1 would accrue:
- April 15 to June 30: at the Q2 rate
- July 1 to August 1: at the Q3 rate

Form 2210's worksheet handles this by splitting the penalty period into the relevant rate-quarter sub-periods. The current-year instructions show a sample computation.

## What the agent should do

1. Pull the rates from the current-year Form 2210 instructions penalty worksheet (or the IRS quarterly interest rates page if the worksheet is not yet published)
2. For each quarterly underpayment, identify the penalty period (due date → satisfaction date or 4/15)
3. Split the period into rate-quarter sub-periods if the rate changed
4. Compute penalty = underpayment × rate × (days / 365) for each sub-period
5. Sum across sub-periods and quarters

The agent should NOT:
- Use a stale rate from a prior year (rates change)
- Apply daily compounding (IRC §6622(b) excludes the §6654 penalty from it)
- Apply a "blended" rate across the whole year (the form requires period-by-period computation)

## Sources

- IRC §6621(a)(2), (b) — Underpayment rate (federal short-term rate + 3 points), set each calendar quarter
- IRC §6622(b) — No daily compounding for the §6654 penalty
- IRC §1274(d) — Federal short-term rate definition
- IRC §6654(b)(3) — Order of crediting payments
- IRC §6654(c) — Quarterly installment due dates
- [Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/f2210.pdf) — penalty worksheet
- [Instructions for Form 2210 (latest)](https://www.irs.gov/pub/irs-pdf/i2210.pdf) — penalty worksheet with the rate for each rate period of the tax year being filed
- [IRS Underpayment Rates archive](https://www.irs.gov/payments/quarterly-interest-rates) — historical rate announcements
