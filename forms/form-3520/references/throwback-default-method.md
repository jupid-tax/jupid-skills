# Throwback Rules and the Form 3520 Default Method

When a US beneficiary receives a distribution from a **foreign non-grantor
trust**, the throwback rules of IRC §§665-668 apply. The Form 3520
default method (Part III, Schedule A) is the calculation used when the
trust does not provide a Foreign Nongrantor Trust Beneficiary Statement;
Schedule C then computes the tax and the interest charge. This reference
walks the mechanics, line by line, for Form 3520 (Rev. December 2023).

## Why the throwback rules exist

Foreign non-grantor trusts can accumulate income tax-free in their home
jurisdiction for years and then distribute large lumps to US
beneficiaries. Without throwback, the US beneficiary would pay tax only
on the year-of-distribution income (DNI) and the prior-year accumulations
would escape US tax entirely.

The throwback rules close this loophole by:

1. Identifying the portion of a distribution that represents accumulated
   income from prior years (UNI — Undistributed Net Income)
2. Treating that portion as if it had been distributed in the years it
   was earned ("throwing back" to those years)
3. Computing tax with the §667(b) averaging method (Form 4970)
4. Adding an interest charge (IRC §668(a)) for the deferred tax

## DNI vs UNI

- **DNI (Distributable Net Income)** — current-year trust income,
  computed under IRC §643(a). Distributions up to DNI carry out
  current-year income to beneficiaries.
- **UNI (Undistributed Net Income)** — prior-years' accumulated income
  that was not distributed. Distributions in excess of current-year DNI
  carry out UNI under §665(a).

## Actual method (Beneficiary Statement provided)

If the trust provides a Foreign Nongrantor Trust Beneficiary Statement:

- The statement allocates each distribution between current-year income
  (Schedule B lines 40a–42d by character), accumulation distribution (41a),
  and corpus (43)
- The beneficiary uses the statement's allocations directly
- An accumulation distribution on line 41a still goes through Schedule C
  (Form 4970 tax plus interest), with the applicable number of years from
  weighted UNI (lines 45–47)

## Default method (no Beneficiary Statement) — Form 3520 Part III, Schedule A

Without a complete Foreign Nongrantor Trust Beneficiary Statement, the
beneficiary uses Schedule A (lines 31–38). Once Schedule A has been used
for a trust, it must be used in all later years, except that Schedule B
may be used in the year the trust terminates if a statement is received
that year (Instructions for Form 3520, Rev. December 2025, Schedule A).

### Step 1 — Current-year distributions (line 31)

Line 31 = line 27: distributions on line 24 plus loans and uncompensated
use treated as distributions on line 25. Translate to USD (the form
requires USD; document the rate source).

### Step 2 — Years as a foreign trust (line 32)

Number of years the trust has been a foreign trust, including the current
year; any part of a year counts as a full year. Attach the basis for the
number. If this is the trust's first year as a foreign trust, do not
complete the rest of Part III.

### Step 3 — Prior distributions and the 125% average (lines 33–35)

- Line 33: total distributions received from the trust in the 3 preceding
  tax years (or the number of preceding years if the trust is younger),
  counting years with no distribution as zero
- Line 34: line 33 × 1.25
- Line 35: line 34 ÷ 3.0 (or the number of preceding years if fewer)

### Step 4 — Split the distribution (lines 36–37)

- Line 36: the smaller of line 31 or line 35 — treated as **ordinary
  income earned in the current tax year** (reported on the user's income
  tax return)
- Line 37: line 31 − line 36 — the **accumulation distribution**. If
  zero, stop

### Step 5 — Applicable number of years (line 38)

Line 38 = line 32 ÷ 2.0. Schedule C rounds it to the nearest half year on
line 50.

## Schedule C — tax and interest charge (lines 48–53)

### Tax on the accumulation distribution (line 49, Form 4970)

Enter line 48 (= line 37) on line 1 of Form 4970 and work lines 1–28;
line 49 = Form 4970 line 28. Form 4970 is attached to Form 3520 as a
worksheet; it is not filed separately for a foreign trust (Form 4970
instructions, "Foreign trust beneficiaries"). Form 4970's method (§667(b)):

1. Line 9 / line 12: average annual amount = the accumulation
   distribution ÷ the number of earlier years over which it is treated as
   distributed (lines 8 and 11)
2. Line 13: the beneficiary's taxable income for each of the 5 tax years
   immediately before the current year
3. Line 14: drop the highest and the lowest of those 5 years
4. Lines 15–19: for each of the 3 remaining years, add the average annual
   amount to taxable income and recompute that year's tax with that
   year's rates; the increase is the additional tax (lines 20–23 adjust
   for credits and AMT)
5. Lines 24–26: average the 3 increases (÷ 3.0) and multiply by the
   number of years on line 11
6. Lines 27–28: subtract taxes the trust paid on the amount (line 4)

There is no "highest marginal rate" shortcut; the 3-of-5-years averaging
is the statutory method. For a default-method distribution, Form 3520 and
the Form 4970 instructions do not say expressly what number of years goes
on Form 4970 lines 8 and 11. ASK the preparer; the examples in this skill
use the line 38 applicable number of years and say so.

### Interest charge (lines 50–52)

- Line 50: applicable number of years (line 38), rounded to the nearest
  half year
- Line 51: combined interest rate. A calendar-year filer using June 30 of
  the year as the applicable date reads it from the table at
  https://www.irs.gov/CombinedInterestRate for that year. Otherwise
  compute it: 6% simple interest for periods 1977–1995, and the §6621(a)(2)
  underpayment rate compounded daily after 1995 (Instructions, Line 51).
  On 2026-10-06 the newest posted table is for 2024 calendar-year filers;
  for a later year, check the page again before filing
- Line 52: line 49 × line 51
- Line 53: line 49 + line 52 — reported as additional tax on the income
  tax return (Form 1040: Schedule 2, Part II, the "any other taxes" line)

## Why default method usually hurts

1. **The 125% cushion is small** — only distributions up to 125% of the
   prior 3-year average count as current income; a large one-time
   distribution is mostly an accumulation distribution.
2. **Lost character plus interest** — except for tax-exempt interest, an
   accumulation distribution generally loses its character (Form 4970
   instructions; §667(d) has special rules for foreign trusts), so
   long-term gains accumulated in the trust do not keep capital gain
   treatment, and the interest charge grows with the years the trust has
   been foreign.
3. **Consistency rule** — once Schedule A is used, it sticks for that
   trust.

## Recommendation for the US beneficiary

If the user is receiving distributions from a foreign non-grantor trust:

1. **Always request a Beneficiary Statement** from the trustee for the
   current year and going forward (Notice 97-34 lists the required
   contents)
2. **If the trustee won't or can't provide one**, document the request
   and consider working with an international tax practitioner
3. **Otherwise**, complete Schedule A and Schedule C, attach Form 4970 to
   Form 3520, and carry line 53 to Schedule 2 of Form 1040

## Cross-form reconciliation

The numbers must reconcile across:

- Form 3520 Part III lines 24–27 — the distributions
- Schedule A lines 31–38 — the split between current income and
  accumulation distribution
- Form 4970 (attached to Form 3520) — line 28 tax = Schedule C line 49
- Schedule C lines 50–53 — interest charge and total
- Form 1040 — line 36 amount as ordinary income; line 53 on Schedule 2

## A worked numerical example

User received $300,000 from a family non-grantor trust in 2026. No
Beneficiary Statement. The trust has been a foreign trust since 2018.

Prior 3 years of distributions from this trust to this beneficiary:
- 2023: $0
- 2024: $20,000
- 2025: $40,000

| Line | Computation | Amount |
|------|-------------|--------|
| 31 | Total distributions 2026 | $300,000 |
| 32 | Years as a foreign trust, 2018–2026 | 9 |
| 33 | $0 + $20,000 + $40,000 | $60,000 |
| 34 | $60,000 × 1.25 | $75,000 |
| 35 | $75,000 ÷ 3 | $25,000 |
| 36 | Smaller of $300,000 or $25,000 (ordinary income in 2026) | $25,000 |
| 37 | $300,000 − $25,000 (accumulation distribution) | $275,000 |
| 38 | 9 ÷ 2 | 4.5 |

Line 49 needs Form 4970 with the user's 2021–2025 taxable incomes, so it
cannot be computed without asking. Line 51 needs the combined interest
rate table for 2026 calendar-year filers (not posted as of 2026-10-06).
The skill should run this computation whenever the user is forced into
the default method, so the user understands the cost and the value of
obtaining a Beneficiary Statement next year. A fully computed case is in
[`../examples/offshore-trust-distribution.md`](../examples/offshore-trust-distribution.md).
