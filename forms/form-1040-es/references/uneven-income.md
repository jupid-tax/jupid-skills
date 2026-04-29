# Uneven Income and the Annualized Income Installment Method

When a taxpayer's income is concentrated in one or two quarters rather than spread evenly, the equal-installments method (¼ each quarter) can trigger underpayment penalties even when the year-end total is paid in full. The annualized income installment method (Form 2210 Schedule AI) addresses this.

This file explains when uneven income matters and how the agent advises the user — without executing Schedule AI itself (that's the `form-2210` skill).

---

## When uneven income matters

The default §6654 rule requires 25% of the annual safe-harbor amount paid by each quarter due date. If a taxpayer earns 80% of their annual income in Q4 (e.g., a year-end bonus, a Q3 capital-gain realization, a Q4 Roth conversion), they owe a penalty for under-paying Q1, Q2, Q3 — even though their full year-end tax is paid by Q4.

**Examples that trigger annualization**:
- Software engineer with December RSU vest worth $200K — most of the year's income lands in Q4
- Retiree converts $100K of traditional IRA to Roth in March — Q1 income spike
- Real estate investor sells a rental property in August — Q3 capital gain
- S-corp owner takes most distributions in November after year-end review — Q4 spike
- Author receives a $50K advance in January, royalty trickles thereafter — Q1 spike

**Examples that do NOT trigger annualization** (income is even enough):
- Schedule C consultant with monthly invoicing — even
- W-2 employee with bonus paid 50/50 in March and September — close enough to even
- Rental property income spread monthly — even

---

## Two paths the agent should offer

When the agent detects lumpy income in the user's projection, surface both options:

### Path 1 — Pay the safe harbor evenly anyway

Use the prior-year safe harbor (Safe Harbor B). The agent recommends 25% of `prior_year_tax × 1.10` (or × 1.00) per quarter regardless of when current-year income lands. This is **certain**: as long as the user pays this fixed schedule, no §6654 penalty regardless of where current-year income falls.

**Trade-off**: the user may overpay quarterly until the IRS settles up at year-end refund. But there's no penalty risk.

### Path 2 — Use the annualized income method

Pay smaller installments in early quarters when income is genuinely lower, larger installments when income is realized. Compute on Form 2210 Schedule AI when filing.

**Trade-off**: lower cash outflow early in the year, but Schedule AI is 30+ lines per quarter and easy to mess up. Auditors look at it more carefully than equal-installment filings.

---

## Schedule AI cumulative periods

The annualization periods are cumulative, not discrete:

| Installment | Income period | Months | Annualization factor |
|-------------|---------------|--------|---------------------|
| 1 | Jan 1 – Mar 31 | 3 | 4 (12/3) |
| 2 | Jan 1 – May 31 | 5 | 2.4 (12/5) |
| 3 | Jan 1 – Aug 31 | 8 | 1.5 (12/8) |
| 4 | Jan 1 – Dec 31 | 12 | 1 (full year) |

For each period:
1. Sum income, deductions, credits earned **through that date**
2. Multiply by the annualization factor → annualized AGI
3. Compute tax on annualized AGI
4. Multiply by `period_months / 12` → required cumulative installment as of that due date
5. Subtract prior installments → required current installment

This produces a payment that scales with actual earnings.

---

## Operational guidance the agent gives

When the user describes lumpy income, the agent says:

```
Your income looks uneven across the year:
- <list of lumpy events with dates and amounts>

You have two options:

Option A (Safe and Simple): Pay the prior-year safe harbor evenly.
- Required: $X per quarter (4 equal installments)
- Pro: certain no §6654 penalty
- Con: may overpay early in the year if current-year income is lower

Option B (Annualized): Pay smaller early-quarter installments matched to
actual income earned, computed on Form 2210 Schedule AI at filing time.
- Required Q1: ~$Y (estimated)
- Required Q2-Q4: rises with realized income
- Pro: smoother cash flow if income is genuinely back-loaded
- Con: Schedule AI is complex; easier to mess up; sometimes audited

For a one-off lumpy event, Option A is usually cleaner.
For a structurally uneven income pattern (e.g., seasonal business),
Option B saves on early-quarter cash.
```

The agent does NOT compute Schedule AI in this skill. It surfaces the choice and produces Option A by default.

---

## Special pre-quarter timing windows

The annualization periods end **on the date** of the installment, not the prior month-end:

- Period 1 ends March 31 (not April 14)
- Period 2 ends May 31 (not June 14)
- Period 3 ends August 31 (not September 14)
- Period 4 ends December 31

This means if a $100K capital gain hits on April 1, it's in Period 2, not Period 1 — even though the Q1 voucher isn't due until April 15. The user has 14 days of "advance look-ahead" income that lands in Period 2.

This timing matters when scheduling income realization (e.g., when to close a sale, when to do a Roth conversion).

---

## Q4 catch-up via withholding (the magic trick)

A taxpayer who realizes by November they're underpaid can request additional federal withholding from any remaining W-2 wages or 1099-R distributions:

- W-2: file Form W-4 with employer specifying "additional withholding per pay period" (Line 4(c))
- 1099-R: file Form W-4P with the payer specifying additional withholding
- Social Security: file Form W-4V (only flat percentages: 7%, 10%, 12%, 22%)

Because of IRC §6654(g), withholding is treated as paid evenly across the year — so a December lump-sum of withholding retroactively cures Q1, Q2, Q3 underpayment. Estimated payments cannot do this.

**Limitation**: this only works if the taxpayer has wages or a pension being paid. Pure 1099 / Schedule C taxpayers with no W-2 income cannot use this trick.

---

## What this skill produces for uneven-income users

The default plan output assumes equal installments (Option A). If the user has lumpy income and wants Option B, the skill emits this guidance:

```
## Income evenness assessment
- Detected lumpy event: <description, amount, expected date>
- Recommended method: [equal installments using prior-year safe harbor]
                  OR [annualized — see form-2210 skill at filing time]
- Reason: <why this method>

## Q4 catch-up planning (if applicable)
- If user has W-2 wages: increase withholding via Form W-4 Line 4(c) by $X
  per remaining paycheck. This counts as paid evenly across all four quarters.
- If user has pension: increase withholding via Form W-4P
- If pure 1099: no catch-up trick available; must pay estimated by Q4 (Jan 15)
```

---

## Cross-skill handoffs

- For penalty computation on a year that's already underpaid → `form-2210` skill
- For Schedule AI line-by-line annualization → `form-2210` skill
- For Form W-4 withholding adjustment → forthcoming `form-w4` skill

This skill is prospective. It plans the payment schedule. It does not compute penalties retrospectively or work the Schedule AI math.
