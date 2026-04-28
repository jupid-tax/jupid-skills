# Standard vs Itemized — When to Itemize, Bunching Strategy, Breakeven

The Schedule A decision is binary: itemize OR take the standard deduction. The IRS doesn't let filers do both. The right answer depends on whether the user's total itemized deductions (Schedule A Line 17) exceed the standard deduction for their filing status.

This file is the operational reference for running the comparison, identifying close cases, and explaining bunching strategy when itemized total is near the standard deduction.

---

## The decision rule

```
If Line 17 > standard deduction:
  → Itemize. Line 17 flows to Form 1040 Line 12.
Else:
  → Take the standard deduction. Don't file Schedule A.
```

Always run both numbers. The standard deduction beats itemized for roughly **90% of filers** post-TCJA (the 2018 standard-deduction doubling shifted the breakeven sharply).

---

## Standard deduction by filing status

### Tax year 2025 (Rev. Proc. 2024-40)

| Filing status | Standard deduction |
|---------------|---------------------|
| Single / Married Filing Separately | $15,000 |
| Married Filing Jointly / Qualifying Surviving Spouse | $30,000 |
| Head of Household | $22,500 |

### Tax year 2026

The 2026 standard deduction is set by the inflation adjustment (typically announced October 2025 in a Revenue Procedure). Verify against the current Rev. Proc. before filing. Approximate placeholders pending the official release.

### Additional standard deduction for age and blindness

| Status | Additional amount (2025) |
|--------|--------------------------|
| Age 65+ (single, HoH, MFS) | $1,950 |
| Age 65+ (MFJ each spouse over 65, MFS) | $1,550 per spouse |
| Blind (single, HoH, MFS) | $1,950 |
| Blind (MFJ, MFS) | $1,550 per spouse |

A taxpayer who is both 65+ AND blind gets the additions stacked. This effectively shifts the breakeven for older filers.

### Dependents

A taxpayer claimed as a dependent on someone else's return has a reduced standard deduction (greater of $1,350 or earned income + $450, capped at the regular standard deduction for the filing status, for 2025).

---

## When itemizing typically wins

Patterns where itemized usually beats standard:

### Pattern 1: Homeowner in a high-tax state with a mortgage

The classic itemizer profile:
- Mortgage interest of $10,000+ on Line 8a
- State + local + property taxes hitting or near the SALT cap on Line 5e ($40K for 2025/2026 under OBBBA)
- Total around $30,000-$50,000

For MFJ ($30K standard), this beats standard by $0-$20K. For Single ($15K standard), it beats standard handily.

Top states: California, New York, New Jersey, Connecticut, Massachusetts, Maryland, Hawaii, Oregon, Vermont, DC.

### Pattern 2: Major medical year

A taxpayer with high medical expenses (long hospital stay, major surgery, ongoing treatment) plus moderate other itemized deductions. The 7.5% AGI floor consumes a lot, but a single $30K out-of-pocket year at $80K AGI deducts $24K, easily beating standard.

### Pattern 3: Large charitable giver

Cash contributions exceeding 5-10% of AGI. At $200K AGI giving $30K to charity, even with no other itemized deductions, $30K easily beats $30K MFJ standard. (Note: tax year 2026+ subtracts $1,000 floor, but $29K still wins.)

### Pattern 4: Combined moderate amounts in multiple categories

Few of the categories individually justify itemizing, but the sum does. Common in:
- Retirees with Medicare premiums on Line 1, property tax on Line 5b, modest mortgage on Line 8a, and church donations on Line 11
- High-earners with no mortgage but state income tax > $10K and meaningful charity

---

## When standard typically wins

Patterns where standard almost always beats itemizing:

### Pattern 1: Renter

No mortgage interest (Line 8a). State income tax alone almost never reaches the standard deduction. Charitable + medical alone rarely close the gap. Standard wins.

### Pattern 2: Homeowner in a no-income-tax state

States: AK, FL, NV, SD, TN, TX, WA, WY (NH and NV with limited tax). State sales tax via the optional table tops out at maybe $1,500-$3,000 for typical incomes. Property tax + sales tax + mortgage interest typically falls short of $30K MFJ.

### Pattern 3: Recent retiree before mortgage paid off, no major medical

Mortgage interest declines as principal pays down. Property tax + state income tax (if any) + small charity might total $15K-$25K. Below MFJ standard.

### Pattern 4: Young single with student loans (above-the-line) and rental

Student loan interest is above-the-line on Schedule 1 — doesn't help Schedule A. Rental, no charity, modest state tax: standard wins.

---

## Quick breakeven examples

### Single, $15,000 standard

| Profile | Total itemized | Result |
|---------|----------------|--------|
| Renter, $2,000 SALT, $1,500 charity | $3,500 | Standard wins by $11,500 |
| Homeowner CA, $3K mortgage, $5K SALT, $1K charity | $9,000 | Standard wins by $6,000 |
| Homeowner NY, $8K mortgage, $14K SALT, $3K charity | $25,000 | Itemize, gain $10,000 |
| $25K medical year at $80K AGI ($25K − $6K floor = $19K), $5K SALT | $24,000 | Itemize, gain $9,000 |

### MFJ, $30,000 standard

| Profile | Total itemized | Result |
|---------|----------------|--------|
| Renter MFJ, $4K SALT, $2K charity | $6,000 | Standard wins by $24,000 |
| Homeowner TX, $10K mortgage, $9K property tax, $1.2K sales tax (optional table), $3K charity | $23,200 | Standard wins by $6,800 |
| Homeowner CA, $12K mortgage, $15K state income, $9K property tax, $4K charity | $40,000 | Itemize, gain $10,000 |
| Homeowner NJ, $20K mortgage, $25K SALT (capped), $5K charity | $50,000 | Itemize, gain $20,000 |

(SALT cap applied at $40K for 2025/2026 under OBBBA, not the old $10K.)

---

## Close cases — bunching strategy

Bunching is the practice of concentrating itemizable expenses into alternating years so that itemizing wins in "bunch" years and standard wins in "off" years. The total deduction over multiple years is higher than always taking the standard.

### How bunching works

Imagine an MFJ couple with $15,000 of recurring annual itemized deductions (under the $30K standard). Default approach: take $30K standard each year. Five-year deduction: $150K.

Bunching approach: in "bunch" years, accelerate two years of charity, prepay property tax, etc., to push the bunched year over $30K (say $35K bunched). In "off" years, deductions drop to $0 (or close), but standard kicks in at $30K. Five-year deduction: $35K + $30K + $35K + $30K + $35K = $165K. Net gain: $15K of additional deduction over five years, worth $3,300 at 22% bracket.

### What's bunchable

- **Charity**: easiest. Donate two years of giving in December of a "bunch" year. Donor-advised funds (DAFs) make this clean — fund the DAF in a bunch year, distribute over multiple years from the DAF.
- **Medical expenses**: harder; you can't postpone surgery, but you can sometimes accelerate elective procedures or large prescriptions.
- **Property tax**: in some jurisdictions, prepay the next year's property tax in December of the current year. Verify the locality permits prepayment AND has actually assessed the tax (the IRS disallowed pre-assessment "prepayments" in 2018; see IRS notice IR-2017-210).
- **State estimated tax**: Q4 state estimate due January 15 can be paid by December 31 of the current year if SALT cap-room is available.

### What's not easily bunchable

- Mortgage interest (locked to monthly accrual)
- Sales tax (when using the optional table — not bunchable)
- Most non-cash charity unless the donor controls timing of donations of appreciated property

### Bunching with a Donor-Advised Fund

The cleanest bunching tool. Steps:
1. In bunch year, contribute, say, 3-5 years of intended giving to a DAF (Fidelity Charitable, Schwab Charitable, community foundation)
2. Take the full deduction in the bunch year (subject to AGI ceilings; 5-year carryforward for excess)
3. In off years, the DAF distributes to chosen charities; no deduction needed
4. Repeat the contribution every 3-5 years

Particularly powerful when the donor has appreciated stock to contribute (no capital gain recognition + FMV deduction).

### Bunching example

MFJ couple, $200K AGI, normally gives $5K to church annually + has $20K SALT (capped) + $10K mortgage interest = $35K itemized. Standard MFJ = $30K. Itemizing gains $5K/year.

Switch to bunching: contribute $25K to DAF in year 1 (5 years × $5K) + $20K SALT + $10K mortgage = $55K itemized in year 1. Take $30K standard in years 2-5.

Five-year totals:
- Always itemize: $35K × 5 = $175K
- Bunch + DAF: $55K + ($30K × 4) = $175K

Tied. The bunch wins only if **the recurring giving is below the gap between itemized and standard** in non-bunch years — i.e., when normal-year itemized total falls below standard. Run the math; bunching doesn't always pay.

### Where bunching DOES win

MFJ couple, $200K AGI, $5K church + $9K SALT (no income tax state, just property + sales tax) + $4K mortgage = $18K itemized. Standard MFJ $30K. Don't itemize at all.

Bunch: give $25K to DAF in year 1, take $25K + $9K + $4K = $38K. Itemize, beat standard by $8K. In years 2-5, take $30K standard. Five-year total: $38K + ($30K × 4) = $158K vs always-standard $30K × 5 = $150K. Net gain $8K from bunching, worth $1,760 at 22% bracket.

This is the bunching sweet spot: when normal-year itemized < standard, but bunching pushes occasional years above standard.

---

## Always run both — even if you "know" the answer

Software running tax returns should compute both regardless of user assumption. Common surprises:

- "I always took the standard" — until they had a major medical year
- "I'm not a homeowner" — but they paid $15K of state income tax on a high salary in a high-tax state
- "I don't have enough deductions" — until the SALT cap quadrupled under OBBBA
- "Itemizing is for rich people" — until the user had a federally declared disaster loss

Always compute Line 17. Always compare to standard. Surface the gap. Take the higher.

---

## MFS coordination rule

If one spouse files MFS and itemizes, the other spouse **must also itemize** — even if the standard deduction would be higher (IRC §63(c)(6)(A)). This applies regardless of which spouse has the deductions. Plan MFS returns together.

The result: MFS rarely makes sense for tax savings. It's used when spouses are separated, when one spouse is responsibility-shielding from the other's tax issues, or for state-tax optimization in community property states.

---

## When close to the standard, consider

- Bunching charitable contributions into alternating years
- Prepaying property tax (if the locality allows and the tax is assessed)
- Paying state Q4 estimates by December 31 instead of January 15
- Making a QCD from an IRA (if 70½+) — reduces AGI, may make the standard easier to hit anyway, doesn't go on Schedule A
- Contributing appreciated stock to a DAF (FMV deduction + no capital gain)

---

## Sources

- [IRC §63](https://www.law.cornell.edu/uscode/text/26/63) — Standard deduction
- [IRC §63(c)(6)(A)](https://www.law.cornell.edu/uscode/text/26/63) — MFS coordination rule
- [Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) — 2025 standard deduction (Single $15,000, MFJ $30,000, HoH $22,500); age/blindness add-ons
- [IRS Publication 17](https://www.irs.gov/publications/p17) — Your Federal Income Tax (chapter on standard deduction)
- [IRS Notice IR-2017-210](https://www.irs.gov/newsroom/irs-advisory-prepaid-real-property-taxes-may-be-deductible-in-2017-if-assessed-and-paid-in-2017) — prepaid property tax must be assessed first
- [Schedule A Instructions](https://www.irs.gov/pub/irs-pdf/i1040sca.pdf)
