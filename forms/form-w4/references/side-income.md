# Step 4(a) Other Income vs Form 1040-ES

When a W-2 employee also has non-wage income (side gig, interest, dividends, rental), they need to either:
1. Have extra federal tax withheld from their W-2 paychecks via W-4 Step 4(a) and/or Step 4(c), OR
2. Make quarterly estimated tax payments via Form 1040-ES

Both satisfy the IRC §6654 underpayment safe harbor. Pick the easier one.

## Decision Tree

```
Does the user have non-wage income?
├─ NO → Step 4(a) and (c) stay $0 (unless multi-job withholding adjustment)
│
└─ YES → How regular is the income?
    ├─ Stable, predictable (e.g., bond interest, regular rental)
    │   └─ Use Step 4(a) — easier, automated through payroll
    │
    └─ Irregular, hard to predict (e.g., one-off freelance jobs, capital gains)
        └─ Use quarterly Form 1040-ES — adjust each quarter as income materializes

  Add: Is the income from self-employment with SE tax?
    ├─ Yes — small ($<5,000/year) → Step 4(c) covers SE tax via extra withholding
    └─ Yes — larger or unpredictable → 1040-ES is cleaner; SE tax + income tax in one payment
```

## Step 4(a): Other Income on the W-4

### What it does

Step 4(a) adds the user's annual expected non-wage income to the income amount the employer's payroll software uses for withholding. The withholding table looks up tax for the (wages + Step 4(a)) amount, but only withholds from wages — so the extra tax effectively comes out of wage withholding.

### What it covers

✅ Federal income tax on:
- Side-gig profit (Schedule C net)
- 1099-K, 1099-NEC, 1099-MISC income
- Interest (1099-INT)
- Dividends (1099-DIV)
- Capital gains (Schedule D)
- Rental net income (Schedule E)
- Cancellation of debt
- Gambling winnings, prizes

### What it does NOT cover

❌ Self-employment tax (15.3% — Social Security + Medicare for self-employed)
❌ Additional Medicare Tax (0.9% over $200K single / $250K MFJ)
❌ Net Investment Income Tax (3.8% on investment income above thresholds)
❌ State income tax (separate state withholding form)

For self-employed side-gig income, Step 4(a) only covers the federal income tax portion. SE tax is separate and must be covered by either:
- A higher Step 4(c) amount (calculate: SE profit × 15.3% / pay periods)
- Quarterly Form 1040-ES payments

### Example

User: W-2 employee with $80K salary, also rents out a property for $24K/year ($18K net after expenses).

**Option A — Step 4(a):** Enter $18,000 on Step 4(a). Payroll withholds federal income tax as if user's salary were $98K. At a 22% bracket effective rate, that's ~$3,960 of additional withholding spread across the year. No need for 1040-ES.

**Option B — 1040-ES:** Skip Step 4(a). Pay quarterly: $18,000 × 22% / 4 = $990 per quarter on April 15, June 15, September 15, January 15.

Both work. Step 4(a) is easier (automated through payroll); 1040-ES is more flexible (can pause if income drops).

## Step 4(c): Per-Pay-Period Extra Withholding

Step 4(c) is the catch-all for any flat dollar amount per paycheck. Three main use cases:

### Use case 1: Multi-job adjustment

Result from Step 2 method (Estimator or Worksheet) goes on Step 4(c). See [`multi-job.md`](./multi-job.md).

### Use case 2: Cover SE tax on side gig

If using W-4 (not 1040-ES) to handle a side gig, calculate SE tax separately and add to Step 4(c).

```
Annual SE tax = (Schedule C profit × 0.9235) × 0.153
Step 4(c) addition for SE tax = Annual SE tax / pay periods
```

Example: $14,000 Etsy profit
- $14,000 × 0.9235 = $12,929 (SE base)
- $12,929 × 15.3% = $1,978 (SE tax)
- $1,978 / 26 biweekly = $76 per check

Combined with federal income tax via Step 4(a) ($14,000 at 22% = $3,080 / 26 = $118), total Step 4(c) for side gig = $76 + $118 = $194.

OR easier: enter $14,000 on Step 4(a) for income tax, add $76 to Step 4(c) for SE tax.

### Use case 3: Owed taxes last year, fix it without doing math

If user owed $2,000 last year and wants to bump withholding without recalculating everything: $2,000 / pay periods → Step 4(c).

## Form 1040-ES: Quarterly Estimated Payments

### When to prefer 1040-ES over W-4 adjustments

- User's primary income is self-employment (more freelance income than W-2)
- Side-gig income is highly variable quarter-to-quarter
- User wants to keep their W-2 withholding minimal and pay all tax in one place
- Side gig is seasonal (e.g., tax preparer with February-April income spike)

### How 1040-ES works

Four payments per year, due:
- Q1: April 15
- Q2: June 15
- Q3: September 15
- Q4: January 15 of following year

Each payment covers federal income tax + SE tax + Additional Medicare Tax + NIIT for the previous quarter.

### Safe harbor (IRC §6654)

To avoid the underpayment penalty, total annual payments (W-4 withholding + 1040-ES) must equal:

- 90% of current year tax liability, OR
- 100% of prior year tax liability (110% if prior year AGI > $150,000)

Whichever is SMALLER.

If user paid $20,000 in tax last year and AGI was $120,000, they need at least $20,000 of withholding + estimates this year to be safe. If their employer withholds $15,000, they need $5,000 more — split into 4 estimates of $1,250.

### Hybrid: W-4 + 1040-ES

Many users do both:
- W-4 covers W-2 income tax + portion of side income
- 1040-ES covers the rest of side income + SE tax

This is fine — the safe harbor is total payments, regardless of channel.

## Recommendation Algorithm

For the agent producing W-4 advice, recommend in this priority order:

1. **Stable side income, prefers automation** → Step 4(a) for income tax + Step 4(c) for SE tax (if applicable)
2. **Variable side income, comfortable with quarterly admin** → leave Step 4(a) at $0, set up 1040-ES
3. **Mixed: predictable W-2 income tax + unpredictable side gig** → Step 4 covers W-2 withholding adjustments only; 1040-ES covers all side income
4. **Heavy primary self-employment with small W-2 side job** → keep W-4 simple (no Step 4); 1040-ES does everything

## Validation Checks

Before finalizing the W-4, run these checks if the user mentioned other income:

- [ ] Step 4(a) annual amount matches user's stated other income? Within ±10%?
- [ ] If Step 4(a) > 0 from a side gig, did the agent address SE tax separately (Step 4(c) or 1040-ES)?
- [ ] Total expected federal tax from all sources (W-2 wages + side income) covered by W-4 withholding + 1040-ES + spouse's W-4?
- [ ] Safe harbor met: (current year withholding + estimates) ≥ min(90% × current year tax, 100% × prior year tax, or 110% if AGI > $150K)?

## Common Errors

- **Counting GROSS revenue on Step 4(a) instead of net profit.** For a side gig, only the profit (after deductible business expenses on Schedule C) is taxable income. Don't enter $50,000 of Etsy sales if profit is $14,000.
- **Forgetting SE tax.** Step 4(a) covers income tax only. SE tax is its own 15.3% liability and needs separate coverage.
- **Including W-2 income on Step 4(a).** Step 4(a) is for income NOT from jobs. W-2 wages already withhold themselves; don't add them to Step 4(a).
- **Setting Step 4(a) too high "to be safe".** Over-withholding gives the IRS an interest-free loan. Better to set it accurately and use 1040-ES if income surges.
