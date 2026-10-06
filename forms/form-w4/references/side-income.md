# Step 4(a) Other Income vs Form 1040-ES

Verified 2026-10-06 against the 2026 Form W-4 (page 2 instructions for Steps 2(a), 4(a), 4(c) and "Self-employment") and Pub. 505 (2026).

When a W-2 employee also has non-wage income (side gig, interest, dividends, rental), they need to either:
1. Have extra federal tax withheld from their W-2 paychecks via W-4 Step 4(a) (non-business income only) and/or Step 4(c), OR
2. Make quarterly estimated tax payments via Form 1040-ES

Both count toward the IRC §6654 underpayment safe harbor. Ask the user which they prefer.

**The form's rule for self-employment income:** Step 4(a) is for "other income (not from jobs)"; "You shouldn't include income from any jobs or self-employment." For self-employment income, "If you want to pay these taxes through withholding from your wages, use the estimator at www.irs.gov/W4App to figure the amount to have withheld," and Step 2(a) says to use the estimator "If you or your spouse have self-employment income." The Estimator's result goes in Step 4(c).

## Decision Tree

```
Does the user have income without withholding?
├─ NO → Step 4(a) and (c) stay $0 (unless multi-job withholding adjustment)
│
└─ YES → Is it self-employment income (Schedule C / SE tax)?
    ├─ YES → NOT Step 4(a). Ask which the user prefers:
    │        • Estimator → extra amount in Step 4(c) (covers income tax + SE tax), or
    │        • quarterly Form 1040-ES
    │
    └─ NO (interest, dividends, retirement income, rental, capital gains) → How regular is it?
        ├─ Stable, predictable (e.g., bond interest, regular rental)
        │   └─ Step 4(a) — automated through payroll
        └─ Irregular, hard to predict (e.g., capital gains)
            └─ Quarterly Form 1040-ES, or a Step 4(c) amount the user is comfortable with
```

## Step 4(a): Other Income on the W-4

### What it does

Step 4(a) adds the user's annual expected other income to the wage amount payroll uses for withholding (Pub. 15-T (2026), Worksheet 1A line 1d). The rate schedule applies to (wages + Step 4(a)), but tax is only withheld from wages — so the extra tax comes out of wage withholding.

### What belongs there

✅ Income not from jobs or self-employment:
- Interest (1099-INT)
- Dividends (1099-DIV)
- Retirement income without its own withholding
- Capital gains (Schedule D)
- Rental net income (Schedule E, non-business)
- Cancellation of debt
- Gambling winnings, prizes, hobby income

❌ NOT here: wages from any job (they withhold on their own) and self-employment income (Schedule C net profit, 1099-NEC/1099-K business income). The 2026 form says not to include them.

### What it does NOT cover

❌ Self-employment tax (15.3% — Social Security + Medicare for self-employed)
❌ Additional Medicare Tax (0.9% over $200K single / $250K MFJ) — Pub. 505 says the user may request extra withholding on Form W-4 for it
❌ Net Investment Income Tax (3.8% on investment income above thresholds) — same
❌ State income tax (separate state withholding form)

### Example

User: single W-2 employee with $80K salary, also rents out a property for $24K/year ($18K net after expenses).

**Option A — Step 4(a):** Enter $18,000 on Step 4(a). Payroll withholds federal income tax as if the user's pay were $98K. 2026 taxable income goes from $63,900 to $81,900 (single, $16,100 standard deduction), all inside the 22% bracket ($50,400–$105,700, Rev. Proc. 2025-32), so about $3,960 of additional withholding spread across the year. No need for 1040-ES for this income.

**Option B — 1040-ES:** Skip Step 4(a). Pay quarterly: $18,000 × 22% / 4 = $990 per quarter (2026 due dates April 15, June 15, September 15, 2026 and January 15, 2027; Pub. 505 (2026), Table 2-1).

Both work. Step 4(a) is easier (automated through payroll); 1040-ES is more flexible (can pause if income drops).

## Step 4(c): Per-Pay-Period Extra Withholding

Step 4(c) is the catch-all for any flat dollar amount per paycheck. Three main use cases:

### Use case 1: Multi-job adjustment

Result from Step 2 method (Estimator or Worksheet) goes on Step 4(c). See [`multi-job.md`](./multi-job.md).

### Use case 2: Cover a side gig through withholding

If the user wants a side gig covered through the W-4 (not 1040-ES), the whole amount — income tax and SE tax — goes in Step 4(c). The form's route is the Estimator. If the user asks the agent to compute it instead, project the tax with and without the self-employment income (Pub. 505 (2026) Worksheets 1-3 and 1-5) and divide the difference by pay periods.

```
Annual SE tax = (Schedule C profit × 0.9235) × 0.153        (Schedule SE; 2026 wage base $184,500)
Income tax on the profit = tax(with profit) − tax(without), after the deduction for half of SE tax
                           and any QBI deduction
Step 4(c) addition = (SE tax + income tax on the profit) / pay periods
```

Example: $14,000 Etsy profit, MFJ household in the 22% bracket (see `../examples/patricia-mfj-kids-side-gig.md`)
- $14,000 × 0.9235 = $12,929 (SE base)
- $12,929 × 15.3% = $1,978 (SE tax)
- Income tax: 22% × ($14,000 − $989 half-SE deduction − $2,602 QBI deduction) = $2,290
- Total $4,268 / 26 biweekly = $164.15 → $165 per check in Step 4(c)

A quick upper bound that skips the two deductions: $14,000 × 22% + $1,978 = $5,058 → $195 per check (over-withholds by about $790 a year).

### Use case 3: Owed taxes last year, fix it without doing math

If user owed $2,000 last year and wants to bump withholding without recalculating everything: $2,000 / pay periods → Step 4(c).

## Form 1040-ES: Quarterly Estimated Payments

### When to prefer 1040-ES over W-4 adjustments

- User's primary income is self-employment (more freelance income than W-2)
- Side-gig income is highly variable quarter-to-quarter
- User wants to keep their W-2 withholding minimal and pay all tax in one place
- Side gig is seasonal (e.g., tax preparer with February-April income spike)

### How 1040-ES works

Four payments per year, due (Pub. 505 (2026), Table 2-1; a due date on a weekend or legal holiday moves to the next business day):
- Q1: April 15, 2026
- Q2: June 15, 2026
- Q3: September 15, 2026
- Q4: January 15, 2027

Each payment covers federal income tax + SE tax + Additional Medicare Tax + NIIT on income for its period.

### Safe harbor (IRC §6654)

To avoid the underpayment penalty, total annual payments (W-4 withholding + 1040-ES) must equal:

- 90% of current year tax liability, OR
- 100% of prior year tax liability (110% if prior year AGI > $150,000, $75,000 MFS)

Whichever is SMALLER. No penalty in any case if the balance due after withholding and credits is under $1,000 (IRC §6654(e)(1); Pub. 505 (2026), chapter 2: estimated tax is required only if you expect to owe at least $1,000). Withholding is treated as paid in equal amounts on the four installment dates unless the taxpayer elects actual dates (Pub. 505 (2026), chapter 2), so extra withholding late in the year counts for earlier quarters too.

If user paid $20,000 in tax last year and AGI was $120,000, they need at least $20,000 of withholding + estimates this year to be safe. If their employer withholds $15,000, they need $5,000 more — split into 4 estimates of $1,250.

### Hybrid: W-4 + 1040-ES

Many users do both:
- W-4 covers W-2 income tax + portion of side income
- 1040-ES covers the rest of side income + SE tax

This is fine — the safe harbor is total payments, regardless of channel.

## Recommendation Algorithm

For the agent producing W-4 advice, recommend in this priority order:

1. **Stable non-business income (interest, dividends, rental), prefers automation** → Step 4(a)
2. **Self-employment income, prefers automation** → Estimator → Step 4(c) (never Step 4(a))
3. **Variable side income, comfortable with quarterly admin** → 1040-ES; Step 4(a) and the self-employment part of 4(c) stay $0
4. **Mixed: predictable W-2 income tax + unpredictable side gig** → Step 4 covers W-2 withholding adjustments only; 1040-ES covers all side income
5. **Heavy primary self-employment with small W-2 side job** → keep W-4 simple; 1040-ES does everything

Present the options and let the user choose; don't pick for them.

## Validation Checks

Before finalizing the W-4, run these checks if the user mentioned other income:

- [ ] Step 4(a) annual amount matches user's stated other (non-job, non-self-employment) income? Within ±10%?
- [ ] No self-employment income on Step 4(a); self-employment income covered via Step 4(c) or 1040-ES, including SE tax?
- [ ] Total expected federal tax from all sources (W-2 wages + side income) covered by W-4 withholding + 1040-ES + spouse's W-4?
- [ ] Safe harbor met: (current year withholding + estimates) ≥ min(90% × current year tax, 100% × prior year tax, or 110% if AGI > $150K)?

## Common Errors

- **Putting side-gig income on Step 4(a).** The 2026 form says not to include self-employment income there. Use the Estimator and Step 4(c), or 1040-ES.
- **Using gross revenue instead of net profit when sizing Step 4(c) or 1040-ES.** Only the profit (after deductible business expenses on Schedule C) is taxable. Don't size withholding on $50,000 of Etsy sales if profit is $14,000.
- **Forgetting SE tax.** SE tax is its own 15.3% liability (on 92.35% of net earnings) and needs coverage in Step 4(c) or 1040-ES.
- **Including W-2 income on Step 4(a).** Step 4(a) is for income NOT from jobs. W-2 wages already withhold themselves; don't add them to Step 4(a).
- **Setting Step 4(a) too high "to be safe".** Over-withholding gives the IRS an interest-free loan. Better to set it accurately and use 1040-ES if income surges.
