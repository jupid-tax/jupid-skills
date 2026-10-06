# Alternative Calculation for Year of Marriage (Form 8962 Part V)

When two filers marry during a tax year, the standard calculation uses the couple's combined household income and year-end family size for every month, including months before the marriage. That can turn APTC each spouse received while single into a large excess. Part V offers an elective alternative that recomputes the pre-marriage months with each spouse's pre-marriage family size and one-half of the couple's household income. It can only reduce the excess APTC repayment; it never increases the net PTC (Treas. Reg. §1.36B-4(b)(2)(ii)(A); Line 26 is -0- when Part V is elected).

## When Part V applies

Per Table 4 and Worksheet 3 in the 2025 Form 8962 instructions, all of the following must be true:

1. Both spouses were unmarried on January 1 of the tax year
2. They were married on December 31 and file a joint return
3. Someone in the tax family was enrolled in a qualified health plan before the first full month of marriage (married July 15 → first full month is August)
4. APTC was paid for someone in the tax family during the year
5. Worksheet 3 shows excess APTC (total column (e) less than total column (f))

The alternative calculation is **elective**. Pub 974 Worksheet V shows whether it reduces the repayment; elect it (Line 9 = Yes, complete Lines 35–36) only if it does.

## How the alternative calculation works

Per Treas. Reg. §1.36B-4(b)(2) and Pub 974 (Alternative Calculation for Year of Marriage, Worksheets I–V):

For pre-marriage months (every month before the first full month of marriage, including the month of the wedding):
- **Alternative family size** = that spouse plus anyone who qualifies as that spouse's dependent for the year (a dependent goes in one spouse's alternative family size, not both)
- **Household income** = one-half of the couple's household income for the year (Form 8962 Line 3 ÷ 2), for each spouse
- FPL table = the same table used on Line 4, at the alternative family size
- Alternative applicable figure = Table 2 at the alternative % FPL
- Alternative monthly contribution = (one-half household income × alternative applicable figure, rounded) ÷ 12, rounded

For full months of marriage:
- Use Line 8b (combined household income and year-end family size) as in the standard calculation

```
alternative_FPL_pct            = floor((Line 3 / 2) / FPL[alternative_family_size] × 100)
alternative_monthly_contribution = round(round((Line 3 / 2) × applicable_figure[alternative_FPL_pct]) / 12)
```

Each spouse's alternative monthly contribution is applied to the months that spouse's alternative family had coverage before marriage (Pub 974 Worksheets II and IV).

## Worked example

### The filer

- Alex married Jordan on July 15, 2025
- Filing status: MFJ
- Tax year: 2025

### Facts

- Both unmarried on January 1, 2025; no dependents
- Alex and Jordan each had their own marketplace policy with APTC from January
- Joint household income for 2025 (Form 8962 Line 3): $64,000
- Pre-marriage months: January–July (July is the wedding month); full months of marriage: August–December

### Standard calculation (no Part V)

- Household income: $64,000; family size 2
- 2024 FPL for size 2: $20,440
- Line 5 = ($64,000 / $20,440) × 100 = 313.1 → 313
- Applicable figure (Table 2, 313): 0.0633
- Line 8a: $64,000 × 0.0633 = $4,051.20 → $4,051
- Line 8b: $4,051 / 12 = $337.58 → $338 per month, used for every month including January–July

### Alternative calculation (Part V)

For each spouse (alternative family size 1, no dependents):
- One-half household income: $64,000 / 2 = $32,000
- 2024 FPL for size 1: $15,060
- Alternative %FPL: ($32,000 / $15,060) × 100 = 212.5 → 212
- Alternative applicable figure (Table 2, 212): 0.0248
- $32,000 × 0.0248 = $793.60 → $794
- Alternative monthly contribution: $794 / 12 = $66.17 → $66

Alex and Jordan each get a $66 monthly contribution for January–July on their own pre-marriage coverage, instead of the $338 combined contribution. August–December use the standard $338.

### Result comparison

- Pre-marriage months: a lower contribution means a larger allowed credit for those months and a smaller excess APTC
- Full months of marriage: same as the standard calculation
- Line 26 stays -0- under Part V; the benefit shows up only as a lower Line 27/29 (Pub 974, Step 8)

Run Pub 974 Worksheet V with the actual 1095-A amounts. Elect Part V only if Worksheet V shows a lower repayment.

## How Part V is filled

| Line | Detail |
|------|--------|
| 35 | Filer: (a) alternative family size, (b) alternative monthly contribution amount, (c) alternative start month, (d) alternative stop month (Pub 974 Worksheet I, lines 1, 7, 8, 9) |
| 36 | Spouse: same four columns (Pub 974 Worksheet III, lines 1, 7, 8, 9) |

In the example: Line 35 = 1, $66, 01, 07; Line 36 = 1, $66, 01, 07.

Then Lines 12–23 are completed using (Pub 974, Step 7):
- Column (c): the alternative monthly contributions (summed across both spouses' worksheets) for pre-marriage months; Line 8b for full months of marriage
- Column (e): the Worksheet V amounts for pre-marriage months; the smaller of (a) or (d) for full months of marriage

This requires careful month-by-month bookkeeping and is best done with worksheet reference.

## Pitfalls

1. **Forgetting that Part V is elective** — filers must affirmatively elect on the form
2. **Mixing pre/post marriage months** — pre-marriage months use the alternative; full months of marriage use the standard. The wedding month counts as a pre-marriage month.
3. **Using the wrong alternative family size** — each spouse's alternative family size is that spouse plus anyone who qualifies as that spouse's dependent for the year; a dependent can be counted for only one spouse. If a spouse has no dependents, alternative family size = 1.
4. **Using each spouse's own income** — the alternative uses one-half of the couple's full-year household income (Line 3 ÷ 2) for each spouse, not each spouse's own or annualized pre-marriage income.
5. **Not running both calculations** — the agent should compute both standard and alternative (Pub 974 Worksheet V) and elect Part V only if it lowers the excess APTC repayment. It cannot raise the net PTC.

## Citation

- IRC §36B(h)(2) (regulations for changes in filing status)
- Treas. Reg. §1.36B-4(b)(2)
- Form 8962 Instructions, Line 9, Table 4, Worksheet 3, Part V
- IRS Pub 974 (2025), Alternative Calculation for Year of Marriage, Worksheets I–V

## Pointer

Always run both calculations side-by-side before choosing. The alternative helps only when it lowers excess APTC. Choosing the standard calculation when the alternative would be better is a missed opportunity, not an error the IRS penalizes.
