# Form 8959 Thresholds and Filing Status

The Additional Medicare Tax thresholds are statutory and **do not adjust for inflation**. This is the single most-confused fact about Form 8959.

## The statutory thresholds

Codified at:

- IRC §3101(b)(2) — wage threshold (for the employee surtax)
- IRC §1401(b)(2) — self-employment threshold (parallel structure)
- IRC §3102(f) — employer withholding threshold (different rule, see below)

| Filing status | Threshold |
|---------------|-----------|
| Single | $200,000 |
| Head of Household | $200,000 |
| Qualifying Surviving Spouse | $200,000 |
| Married Filing Jointly | $250,000 |
| Married Filing Separately | $125,000 |

QSS uses the $200,000 amount on Form 8959 (form lines 5, 9, 15; instructions threshold chart), even though for income tax QSS uses the joint-return brackets and standard deduction. Do not apply the $250,000 MFJ amount to a QSS filer.

## Why the threshold doesn't inflate

The Additional Medicare Tax was added by §9015 of the Patient Protection and Affordable Care Act (P.L. 111-148), amended by §10906 of that Act and §1402(b) of the Health Care and Education Reconciliation Act (P.L. 111-152) (T.D. 9645, 2013-51 I.R.B.), effective for tax years beginning after December 31, 2012. Congress did not include an inflation-adjustment provision; the 2025 Instructions for Form 8959 state: "The threshold amounts below aren't indexed for inflation."

This means:

- A 2013 filer at $200,001 of wages owed $0.01 of Additional Medicare Tax
- A 2026 filer at $200,001 of wages owes $0.01 of Additional Medicare Tax (in nominal dollars)
- In real terms, the threshold falls every year with inflation

The practical effect: each year, more filers cross the threshold. If a filer was just under the threshold a few years ago, they may be over it now without having received a comparable real raise.

## The MFS trap

MFS at $125,000 is the **lowest threshold of any filing status**. This catches couples who:

- Filed jointly historically and don't realize MFS halves the threshold roughly
- Are separated and choose MFS to avoid joint-return liability
- Are filing MFS for income-driven student-loan repayment reasons

A filer with $130,000 of wages who files MFS owes $45 of Additional Medicare Tax ($5,000 × 0.9%). The same filer at the same wages filing single would owe zero. The same couple combined at $250,000 ($130K + $120K) MFJ would owe zero.

The agent should confirm filing status explicitly. Defaulting to "married = $250K" is wrong if MFS.

## The multiple-employer gap

Per IRC §3102(f), employers must withhold 0.9% additional Medicare tax on wages **paid by that single employer in excess of $200,000** — *regardless of the employee's filing status*.

Consequences:

1. **Single employer over $200K**: employer withholds correctly. Filer Form 8959 will reconcile to zero net at filing (assuming no SE income, no RRTA).
2. **Two employers, each $150K (single filer)**: combined $300K is over the $200K single threshold. Neither employer hit $200K from its own payroll, so neither withheld. Filer owes $900 at filing ($100K × 0.9%).
3. **Two employers, each $200K (single filer)**: the employer withholds the additional 0.9% only on wages it pays **in excess of** $200,000, so at exactly $200K from each employer, neither withholds any Additional Medicare Tax. Total wages $400K, threshold $200K → filer owes $200K × 0.9% = $1,800 at filing, all of it unwithheld.

4. **MFJ couple, two earners at $180K + $90K**: neither individual employer is over $200K, so no employer withholding. Combined wages $270K, MFJ threshold $250K, surtax $180. Owed at filing.

The agent should explicitly check this scenario: any time an MFJ couple has total wages over $250K but no single W-2 over $200K, expect a filing balance.

## The wage + SE interaction

The threshold is consumed by wages first, then leftover (if any) absorbs SE income. The form does this in Part II Lines 9–11.

Example: Single filer with $150K wages and $80K SE income.

```
Part I:
  Line 4 = $150,000
  Line 5 = $200,000
  Line 6 = $0
  Line 7 = $0     (no wage Add'l Medicare Tax)

Part II:
  Line 8  = $80,000 × 92.35% = $73,880  (Schedule SE Line 6)
  Line 9  = $200,000
  Line 10 = $150,000
  Line 11 = $200,000 − $150,000 = $50,000  (remaining threshold)
  Line 12 = $73,880 − $50,000 = $23,880
  Line 13 = $23,880 × 0.9% = $215

Part IV:
  Line 18 = $215
```

Filer owes $215 at filing (assuming no employer withholding).

Compare: same filer with $230K wages and $0 SE income would have:

```
Part I:
  Line 6 = $30,000
  Line 7 = $270
```

So: $230K wages alone → $270 surtax. $150K wages + $80K SE → $215 surtax. The structure rewards SE income because the 92.35% multiplier reduces the effective Line 8 figure below gross SE earnings.

## What about RRTA?

Same threshold structure, separate part. A railroad employee with $250K of Tier 1 Medicare-equivalent RRTA compensation files Part III with the same filing-status threshold logic.

If the filer has both wage employment and RRTA compensation in the same year (rare but possible — e.g., a filer who left a railroad job mid-year for a non-railroad job), each part computes against its own full threshold. The Part III threshold (Line 15) is **not** reduced by wages: "There is no equivalent rule for RRTA compensation," and "RRTA compensation should be separately compared to the threshold" (2025 Instructions for Form 8959; Examples 6 and 7 show an MFJ couple with $190,000 of wages and $150,000 of RRTA compensation owing nothing).

## Sources

- IRC §1401(b)(2)
- IRC §3101(b)(2)
- IRC §3102(f)
- [Instructions for Form 8959](https://www.irs.gov/pub/irs-pdf/i8959.pdf) — "Threshold Amounts" table
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf) — Additional Medicare Tax planning chapter
- P.L. 111-148 §9015, as amended by §10906 and by P.L. 111-152 §1402(b) — enactment (per T.D. 9645, https://www.irs.gov/irb/2013-51_IRB)
