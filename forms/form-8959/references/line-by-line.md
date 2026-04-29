# Form 8959 Line-by-Line Reference

Complete lookup for every line on Form 8959. Use this when the agent needs to confirm where an input belongs or what a line means.

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name(s) shown on return | Same as Form 1040 header (joint string for MFJ) | Even if only one spouse triggers the surtax |
| Your social security number | Filer's SSN | The spouse's SSN does not appear on Form 8959 separately; both spouses' wages and SE income combine on the same form for MFJ |

---

## Part I — Additional Medicare Tax on Medicare Wages

The wage portion. Threshold is reduced by **nothing** in this part — the full statutory threshold applies.

### Line 1 — Medicare wages and tips

Sum of **Box 5** ("Medicare wages and tips") across every W-2 received during the year.

| Belongs here | Belongs elsewhere |
|--------------|-------------------|
| All filer W-2 Box 5 amounts | Self-employment income (goes to Line 8) |
| All spouse W-2 Box 5 amounts (if MFJ) | RRTA compensation (goes to Line 14) |
| Statutory employee wages reported on a W-2 | 1099-NEC contractor income (becomes SE income on Line 8) |

**Key rule**: Box 5 may differ from Box 1 (federal taxable wages) and Box 3 (Social Security wages). Box 5 includes 401(k) deferrals (which Box 1 excludes) and is uncapped (Box 3 is capped at the SS wage base). Always use Box 5.

### Line 2 — Unreported tips from Form 4137

Form 4137 Line 6 (the Medicare-wage portion of unreported tips).

Most filers: zero. Applies only to filers who received tip income their employer did not include in W-2 Box 7. Filing Form 4137 separately reports the tips for SS/Medicare purposes; the Medicare-wage portion flows to Form 8959 Line 2.

### Line 3 — Wages from Form 8919

Form 8919 Line 6. Form 8919 is filed when a worker was misclassified as an independent contractor and is paying their share of SS/Medicare on what should have been wages. The Medicare-wage portion flows here.

Most filers: zero.

### Line 4 — Add Lines 1, 2, 3

Sum of the three wage components.

### Line 5 — Threshold

Statutory under IRC §3101(b)(2):

| Filing status | Threshold |
|---------------|-----------|
| Single | $200,000 |
| Head of Household | $200,000 |
| Qualifying Surviving Spouse | $200,000 |
| Married Filing Jointly | $250,000 |
| Married Filing Separately | $125,000 |

**Not inflation-adjusted.** The threshold has been the same since the Additional Medicare Tax was enacted in 2013 (effective tax year 2013). Verify current-year instructions before transcribing — the rule is statutory but if Congress amends it, the instructions will reflect the change.

### Line 6 — Subtract Line 5 from Line 4

Floor at zero. If Line 4 ≤ Line 5, Line 6 is zero and the wage Additional Medicare Tax is zero.

### Line 7 — Multiply Line 6 by 0.9%

Wage Additional Medicare Tax. Round per IRS conventions (usually nearest dollar).

---

## Part II — Additional Medicare Tax on Self-Employment Income

The SE portion. Threshold is **reduced by Part I Line 4** (gross wages, not the wage portion above the threshold). This is the key non-obvious rule.

### Line 8 — Self-employment income

From **Schedule SE Part I Line 6** — the figure after the 92.35% multiplier per IRC §1402(a)(12). Do NOT use raw Schedule C net profit.

If the filer has multiple Schedule Cs or Schedule F + Schedule C, Schedule SE consolidates them; use the consolidated Line 6.

If MFJ and both spouses have SE income, each spouse's Schedule SE Line 6 sums into Form 8959 Line 8.

### Line 9 — Threshold

Same as Line 5 — depends on filing status, statutory.

### Line 10 — Wages from Part I Line 4

Pulls directly from above. The full wage figure, not just the over-threshold portion.

### Line 11 — Subtract Line 10 from Line 9

The "remaining threshold" available to absorb SE income before the 0.9% tax kicks in.

If Line 10 ≥ Line 9 (wages already exceeded the threshold), Line 11 = 0 and every dollar of SE income above zero is taxed at 0.9%.

### Line 12 — Subtract Line 11 from Line 8

Floor at zero. The SE income above the remaining threshold.

### Line 13 — Multiply Line 12 by 0.9%

SE Additional Medicare Tax.

---

## Part III — Additional Medicare Tax on Railroad Retirement (RRTA) Compensation

Almost always zero outside the railroad industry. Mirrors Part I but uses Tier 1 RRTA Medicare-equivalent compensation.

### Line 14 — RRTA compensation

Tier 1 Medicare-equivalent RRTA compensation. From Form W-2 Box 14 (RRTA compensation often reported there for railroad employees) or from RRB-1099-R if applicable.

### Line 15 — Threshold

Same as Lines 5 and 9.

### Line 16 — Subtract Line 15 from Line 14

Floor at zero.

### Line 17 — Multiply Line 16 by 0.9%

RRTA Additional Medicare Tax.

---

## Part IV — Total Additional Medicare Tax

### Line 18 — Add Lines 7, 13, 17

Total Additional Medicare Tax owed for the year.

**Flows to Schedule 2 Line 11** (verify line number against current-year Schedule 2 — line numbers on Schedule 2 have changed between revisions; the *label* "Additional Medicare Tax. Attach Form 8959" is stable).

From Schedule 2, the total flows to **Form 1040 Line 23** (Other taxes).

---

## Part V — Withholding Reconciliation

The reconciliation between what the employer withheld (W-2 Box 6) and what is actually owed.

### Line 19 — Medicare tax withheld

Sum of **Box 6** ("Medicare tax withheld") across every W-2 received during the year.

### Line 20 — Regular 1.45% Medicare tax on Line 1

```
Line 20 = Line 1 × 0.0145
```

This is what the employer *should* have withheld at the regular rate before any Additional Medicare Tax kicks in.

### Line 21 — Subtract Line 20 from Line 19

The Additional Medicare Tax already withheld by the employer.

If Line 19 < Line 20: the W-2 Box 6 reports less than 1.45% of Box 5. This is unusual and usually indicates a W-2 error (or a §125 cafeteria plan reduction that should not have applied to Medicare wages). Reconcile with the W-2 issuer before filing.

If Line 19 > Line 20: the excess is the Additional Medicare Tax withheld. Per IRC §3102(f), the employer is required to withhold 0.9% additional on each employee's wages above $200,000 paid by that single employer regardless of filing status.

### Line 22 — Additional Medicare Tax withholding from Form W-2

Line 21 with adjustments per current-year instructions for combined railroad/wage cases. For non-railroad filers, Line 22 = Line 21.

### Line 23 — Additional Medicare Tax withholding on RRTA compensation

From RRTA W-2 box (varies by tax year). Most filers: zero.

### Line 24 — Total Additional Medicare Tax withheld

```
Line 24 = Line 22 + Line 23
```

**Flows to Form 1040 Line 25c** (Other federal income tax withheld). This is a withholding *credit* — without it, a high earner whose employer correctly withheld the 0.9% surtax above $200K would owe again at filing.

---

## The reconciliation, end to end

For a single filer with $260,000 W-2 wages and no SE income or RRTA:

```
Part I:
  Line 1 = $260,000   (Box 5)
  Line 4 = $260,000
  Line 5 = $200,000   (single threshold)
  Line 6 = $60,000
  Line 7 = $540

Part II: zero (no SE income)
Part III: zero (no RRTA)

Part IV:
  Line 18 = $540  → Schedule 2 Line 11

Part V (employer correctly withheld 0.9% on $60K above $200K):
  Line 19 = $260,000 × 1.45% + $60,000 × 0.9% = $3,770 + $540 = $4,310
  Line 20 = $260,000 × 1.45% = $3,770
  Line 21 = $540
  Line 22 = $540
  Line 24 = $540  → Form 1040 Line 25c

Net at filing: Line 18 − Line 24 = $0
```

Employer correctly absorbed the surtax through payroll. The filer files Form 8959 to **document the reconciliation** but owes nothing additional at filing.

For an MFJ couple with one spouse at $180K and the other at $90K (combined $270K, neither over the $200K employer-trigger):

```
Part I:
  Line 1 = $270,000   (Box 5 sum across both W-2s)
  Line 4 = $270,000
  Line 5 = $250,000   (MFJ threshold)
  Line 6 = $20,000
  Line 7 = $180

Part V (no employer hit the $200K trigger, so neither withheld extra):
  Line 19 = $270,000 × 1.45% = $3,915
  Line 20 = $270,000 × 1.45% = $3,915
  Line 21 = $0
  Line 24 = $0

Net at filing: Line 18 − Line 24 = $180 owed
```

Couple owes $180 at filing because employer withholding doesn't see joint income.

---

## Edge cases

- **Mid-year filing status change**: divorce, marriage, or death of spouse during the year does not split the threshold. The threshold is by *filing status used on the return*, applied to *full-year* wages and SE income. If a couple divorced in November and files single (or HoH) for the year, each former spouse uses the $200K threshold against their own wages.
- **Multiple W-2s, none individually at $200K, combined over $200K**: no employer was required to withhold the additional 0.9% (each saw < $200K from itself). Filer owes the full surtax at filing. Common for filers with W-2 + 1099-NEC, or W-2 plus a part-time W-2 from a second employer.
- **Statutory employees** (W-2 Box 13 "Statutory employee" checked): wages are reported on a W-2 but expenses go on Schedule C. Box 5 still reports as Medicare wages. No double-counting on Form 8959 — wages enter only on Line 1, not on Line 8.
- **Nonresident aliens**: certain visa categories (F, J, M, Q) are exempt from Medicare tax during the substantial-presence-test exclusion period. If exempt, the worker should not have Medicare tax withheld in Box 6, and Line 1 should not include the exempt wages. Consult IRC §3121 totalization rules — out of scope for this skill.
- **High SE income with Schedule SE optional methods**: filers using farm or nonfarm optional methods on Schedule SE Part II have an adjusted Line 6. The optional methods rarely benefit high earners but can shift Line 8 — use whatever Line 6 ultimately reports on Schedule SE.

---

## Sources

- [Form 8959 (latest)](https://www.irs.gov/pub/irs-pdf/f8959.pdf)
- [Instructions for Form 8959 (latest)](https://www.irs.gov/pub/irs-pdf/i8959.pdf)
- IRC §1401(b)(2) — Additional Medicare Tax on self-employment income
- IRC §3101(b)(2) — Additional Medicare Tax on wages
- IRC §3102(f) — Employer withholding obligation
- IRC §1402(a)(12) — 92.35% multiplier for SE income
