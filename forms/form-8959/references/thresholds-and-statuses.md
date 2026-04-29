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

The QSS threshold matching single is by design — QSS filing status applies in the two years following a spouse's death and otherwise mirrors single for most calculations.

## Why the threshold doesn't inflate

When the Additional Medicare Tax was enacted as part of the Affordable Care Act (Public Law 111-152, effective tax year 2013), Congress did not include an inflation-adjustment provision. The IRC text fixes the dollar amounts. They have stayed identical since 2013 across every Form 8959 revision.

This means:

- A 2013 filer at $200,001 of wages owed $0.01 of Additional Medicare Tax
- A 2026 filer at $200,001 of wages owes $0.01 of Additional Medicare Tax (in nominal dollars)
- In real terms, the threshold has been falling — a filer at $200K in 2013 had ~$135K of 2026-equivalent purchasing power

The practical effect: each year, more filers cross the threshold. If a filer was just under the threshold a few years ago, they may be over it now without having received a comparable real raise.

## The MFS trap

MFS at $125,000 is the **lowest threshold of any filing status**. This catches couples who:

- Filed jointly historically and don't realize MFS halves the threshold roughly
- Are separated and choose MFS to avoid joint-return liability
- Are filing MFS for student-loan IDR plan reasons (REPAYE / SAVE / IBR / PAYE income calculations)

A filer with $130,000 of wages who files MFS owes $45 of Additional Medicare Tax ($5,000 × 0.9%). The same filer at the same wages filing single would owe zero. The same couple combined at $250,000 ($130K + $120K) MFJ would owe zero.

The agent should confirm filing status explicitly. Defaulting to "married = $250K" is wrong if MFS.

## The multiple-employer gap

Per IRC §3102(f), employers must withhold 0.9% additional Medicare tax on wages **paid by that single employer in excess of $200,000** — *regardless of the employee's filing status*.

Consequences:

1. **Single employer over $200K**: employer withholds correctly. Filer Form 8959 will reconcile to zero net at filing (assuming no SE income, no RRTA).
2. **Two employers, each $150K (single filer)**: combined $300K is over the $200K single threshold. Neither employer hit $200K from its own payroll, so neither withheld. Filer owes $900 at filing ($100K × 0.9%).
3. **Two employers, each $200K (single filer)**: each employer withholds correctly on the over-$200K portion of its own wages, totaling $0 + $0 = $0 withheld additional. Filer's total wages are $400K, threshold $200K, surtax owed $1,800. Net at filing: $1,800 owed because each employer exhausted exactly its own threshold but no employer saw the *combined* wages.

   Wait — that's wrong. Let me redo: each $200K from a single employer means each is *at* the threshold. The employer withholds the additional 0.9% only on wages **above** $200K from that employer. So at exactly $200K, no additional withholding. At $200K + $1, the employer withholds 0.9% on $1.

   So: two employers each at $200K → total wages $400K → no additional employer withholding → filer owes $200K × 0.9% = $1,800 at filing.

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

If the filer has both wage employment and RRTA compensation in the same year (rare but possible — e.g., a filer who left a railroad job mid-year for a non-railroad job), each part computes against its own line, but the threshold for Part III is reduced by Line 4 (wages) just like Line 11 reduces by wages.

See current-year instructions for the exact line-reduction logic — it has been adjusted in some revisions.

## Sources

- IRC §1401(b)(2)
- IRC §3101(b)(2)
- IRC §3102(f)
- [Instructions for Form 8959](https://www.irs.gov/pub/irs-pdf/i8959.pdf) — "Threshold Amounts" table
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf) — Additional Medicare Tax planning chapter
- Public Law 111-152 (Health Care and Education Reconciliation Act of 2010), §1402 — original enactment
