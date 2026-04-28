# Form W-4 — Step-by-Step Reference

Complete walkthrough of the 2026 Form W-4. The form has 5 steps. Most filers complete Steps 1 and 5 only.

## Step 1 — Personal Information (REQUIRED for everyone)

### Step 1(a) — Name and Address

Enter your full legal name, current mailing address (street, city, state, ZIP).

**Common gotchas:**
- Use legal name as on Social Security card. Maiden vs married name mismatch causes W-2 SSA rejection.
- If recently moved, use the new address — your W-2 mails to whatever address is on file when payroll prints W-2s.

### Step 1(b) — Social Security Number

Enter your 9-digit SSN. Must match Social Security card exactly.

If you don't have an SSN yet (recently arrived in US, immigrant worker awaiting card), you can use an ITIN — but that's only for nonresident aliens, not for US citizens or resident aliens.

### Step 1(c) — Filing Status

Check exactly one:

- **Single or Married Filing Separately**: Use this if unmarried, divorced, or married but filing separately
- **Married Filing Jointly or Qualifying Surviving Spouse**: Use if married and filing one return; or if a widow(er) with a dependent child within 2 years of spouse's death
- **Head of Household**: Use ONLY if all three are true:
  1. Unmarried (or "considered unmarried" — lived apart from spouse last 6 months of year)
  2. Paid more than half the cost of keeping up a home
  3. A qualifying person (usually child or dependent parent) lived with you more than half the year (for parents, can live elsewhere)

The IRS audits HoH claims often. Don't claim HoH if uncertain — see [Pub 501](https://www.irs.gov/publications/p501).

---

## Step 2 — Multiple Jobs or Spouse Works (CONDITIONAL)

Complete Step 2 if **any** is true:
- You hold 2+ jobs at once
- You file MFJ and your spouse also works
- You took a second job mid-year

**Why it's needed:** Each employer's withholding table assumes their salary is the worker's only income. Two jobs of $50K each → each withholds at $50K bracket, but actual income is $100K (taxed in higher brackets) → ~$3,500 under-withheld.

### Three options (pick ONE)

**Option (a) — IRS Tax Withholding Estimator (RECOMMENDED for accuracy)**

Go to https://www.irs.gov/individuals/tax-withholding-estimator. The estimator asks for:
- YTD pay stubs from all jobs
- Expected total wages by year-end
- Filing status, dependents
- Other income, deductions
- Already-withheld amount YTD

Output: an exact dollar amount for Step 4(c) on the higher-paying job's W-4. Most precise option, especially for unequal-pay jobs and mid-year changes.

**Option (b) — Multiple Jobs Worksheet (Page 3 of W-4)**

Use the table on Page 3. Three sub-tables:
- Single/MFS table (Page 3 top)
- MFJ/QSS table (Page 3 middle)
- HoH table (Page 3 bottom)

Look up the row for the higher-paying job's annual wages and the column for the lower-paying job's annual wages. The cell value = additional annual withholding needed. Divide by pay periods on the higher-paying job → enter on Step 4(c).

Example (MFJ):
- Higher job $95,000, lower job $68,000
- MFJ table: row "75,001-100,000", column "65,001-75,000" → $7,610
- $7,610 / 26 biweekly = $293/check on Step 4(c)

**Option (c) — Step 2(c) Checkbox (SIMPLEST)**

Only use if:
- Exactly two jobs total in household
- Both jobs pay roughly similar wages (within ~10%)

Each spouse checks Step 2(c) on their own W-4. Each employer applies an "approximately accurate" withholding by pretending the worker is at a higher bracket.

**Tradeoff:** Simplest, but tends to over-withhold by $500-$1,500 for unequal pay.

### Coordination rule

If completing Step 2, **only complete Steps 3 and 4 on the highest-paying job's W-4.** Other jobs get a W-4 with only Steps 1 and 5. Otherwise dependent credits and adjustments are double-counted across employers.

---

## Step 3 — Claim Dependents (CONDITIONAL)

**Skip if total expected income is above:**
- $200,000 (Single, HoH, MFS)
- $400,000 (MFJ)

Above those thresholds, the Child Tax Credit phases out by $50 per $1,000 of AGI above the threshold (IRC §24(b)). Including Step 3 above the threshold causes under-withholding.

### The math

```
Qualifying children under 17 with SSN × $2,000  = $___
Other dependents                      × $500    = $___
Other expected credits (rare)                   = $___
                                                 ━━━━━━
Total — Step 3                                  = $___
```

### Qualifying child (CTC at $2,000)

All five tests must pass:
1. **Relationship**: Son, daughter, stepchild, foster child, sibling, half-sibling, step-sibling, or descendant of any (grandchild, niece, nephew)
2. **Age**: Under 17 at end of tax year
3. **Residency**: Lived with you more than half the year (with exceptions for school, illness, military service, etc.)
4. **Support**: Did not provide more than half of own support
5. **SSN**: Has a valid SSN issued before the return's due date (not an ITIN, not an ATIN)

### Other dependents (Credit for Other Dependents at $500)

Includes:
- Children 17 or older (lost CTC eligibility but still qualify as dependents)
- Parents you support (don't need to live with you)
- Qualifying relatives (must meet income, support, and relationship tests)

### Coordination

In MFJ, only ONE spouse claims dependents on Step 3 — typically the higher-paying spouse so the credit reduces withholding from a higher-bracket paycheck. The other spouse leaves Step 3 blank.

In divorced/separated households, only the parent claiming the child as a dependent on the tax return enters them on Step 3. Custodial parent typically; non-custodial parent only with signed Form 8332.

---

## Step 4 — Other Adjustments (OPTIONAL)

Three independent fields. Complete any subset.

### Step 4(a) — Other Income (not from jobs)

Enter the **annual** expected amount of non-wage income that won't have its own withholding:
- Side gig / 1099-NEC / freelance net profit
- Interest (1099-INT)
- Dividends (1099-DIV)
- Capital gains (sales of stock, real estate)
- Rental income
- Gambling winnings
- Cancellation of debt income

**What this does:** Increases your federal income tax withholding so the W-2 covers the tax owed on this income too. You won't need quarterly Form 1040-ES for this income.

**What this does NOT do:** Cover self-employment tax (15.3%) on side-gig profit. SE tax is a separate liability under IRC §1401. To cover SE tax via W-4, you need a higher Step 4(c) amount.

### Step 4(b) — Deductions

Enter the **annual** dollar amount of expected itemized deductions ABOVE the standard deduction. Use the Deductions Worksheet on Page 3:

```
Estimated itemized deductions (Schedule A items): $___
- Standard deduction for filing status:           $___
+ "Above the line" adjustments (1040-ES estimate): $___
                                                  ━━━━━
= Step 4(b) entry:                                 $___
```

Schedule A items:
- Medical above 7.5% of AGI
- SALT capped at $10,000
- Home mortgage interest (up to $750K of debt)
- Charitable contributions
- Casualty losses in federally-declared disaster areas

Most filers leave Step 4(b) at $0 because they take the standard deduction. Only matters for filers with large mortgages in high-tax states or large charitable giving.

### Step 4(c) — Extra Withholding

Enter a **per-pay-period** flat dollar amount added to every paycheck's withholding.

Use cases:
- Result from Step 2 multi-job method (Estimator or Worksheet)
- Cover SE tax on side-gig income (15.3% × profit, divided by pay periods)
- Owed taxes last year and want to bump withholding without doing the math
- Have irregular bonuses or commissions and want a buffer

**Example:** Want $2,600 of additional annual withholding, paid biweekly (26 periods) → $100 per check on Step 4(c).

---

## Step 5 — Sign and Date (REQUIRED)

Sign and date the form. Without your signature:
- The form is INVALID
- Employer must withhold at the highest rate (single, no adjustments, no dependents)
- This is the IRS default per IRC §3402(f)(2)

Submit to your employer's HR or payroll department. Don't send to the IRS.

The employer must implement the new W-4 by the start of the first payroll period ending on or after the **30th day** after they receive it.

---

## Filing Status Decision Tree

```
Are you legally married on December 31?
├─ YES
│   ├─ Filing one return with spouse? → MFJ
│   └─ Filing separate returns? → MFS
│
└─ NO (single, divorced, legally separated)
    ├─ Did your spouse die in the last 2 years AND do you have a dependent child?
    │   └─ YES → QSS (Qualifying Surviving Spouse)
    │
    ├─ Are all THREE true: unmarried + paid >half home costs + qualifying person lived with you >half year?
    │   └─ YES → HoH
    │
    └─ Otherwise → Single
```

## Step Coordination for MFJ Two-Earner Households

| Spouse | Step 1 | Step 2 | Step 3 | Step 4 | Step 5 |
|--------|--------|--------|--------|--------|--------|
| Higher-paying job | ✅ Required | ✅ Apply method (a/b/c) | ✅ Claim all dependents here | ✅ Side gig, deductions, extra | ✅ Sign |
| Lower-paying job | ✅ Required | ☐ Skip (or check 2(c) only if equal pay) | ☐ Leave $0 | ☐ Leave $0 | ✅ Sign |

The whole point: only ONE W-4 in the household carries the dependent credit and adjustments. The OTHER W-4 (lower-paying job) just identifies the worker and filing status.

## Effective Date Rules

- W-4 signed today → employer must implement by start of first payroll period ending on or after 30 days from receipt
- New hire W-4 → implement before first paycheck (no 30-day delay)
- W-4 with future effective date → most platforms honor the date; paper W-4s usually take effect on the 30-day rule
