# Standard vs Itemized — When to Itemize, Bunching Strategy, Breakeven

The Schedule A decision is binary: itemize OR take the standard deduction. The IRS doesn't let filers do both. The right answer depends on whether the user's total itemized deductions (Schedule A Line 17) exceed the standard deduction for their filing status.

This file is the operational reference for running the comparison, identifying close cases, and explaining bunching strategy when itemized total is near the standard deduction. Amounts verified 2026-10-06 (2025: P.L. 119-21 §70102 and Rev. Proc. 2024-40; 2026: Rev. Proc. 2025-32).

---

## The decision rule

```
If Line 17 > standard deduction (with any age/blind additions):
  → Itemize. Line 17 flows to Form 1040 line 12e.
Else:
  → Take the standard deduction. Don't file Schedule A (unless the user elects to itemize on line 18, or must because an MFS spouse itemizes).
```

Always run both numbers; since the 2018 standard-deduction increase, most filers take the standard deduction. Two items sit outside the comparison: the Schedule 1-A deductions (tips, overtime, car loan interest, $6,000 per senior) are allowed either way (Form 1040 line 13b), and for 2026+ a non-itemizer may also deduct up to $1,000 ($2,000 joint) of cash gifts to public charities (IRC §170(p)) — add that to the standard side. For 2026+, very high earners (taxable income above the start of the 37% bracket) also have itemized deductions reduced by 2/37 under IRC §68.

---

## Standard deduction by filing status

### Tax year 2025 (P.L. 119-21 §70102; printed on the 2025 Form 1040)

| Filing status | Standard deduction |
|---------------|---------------------|
| Single / Married Filing Separately | $15,750 |
| Married Filing Jointly / Qualifying Surviving Spouse | $31,500 |
| Head of Household | $23,625 |

(Rev. Proc. 2024-40 had set $15,000 / $30,000 / $22,500 before OBBBA raised them; section 3.01 of Rev. Proc. 2025-32 removed section 2.15(1) of Rev. Proc. 2024-40 for that reason.)

### Tax year 2026 (Rev. Proc. 2025-32 §4.14)

| Filing status | Standard deduction |
|---------------|---------------------|
| Single / Married Filing Separately | $16,100 |
| Married Filing Jointly / Qualifying Surviving Spouse | $32,200 |
| Head of Household | $24,150 |

### Additional standard deduction for age and blindness

| Status | 2025 (Rev. Proc. 2024-40 §2.15(3)) | 2026 (Rev. Proc. 2025-32 §4.14(3)) |
|--------|------|------|
| Age 65+ or blind — unmarried (Single, HoH) | $2,000 | $2,050 |
| Age 65+ or blind — married (MFJ, MFS, QSS), per spouse per condition | $1,600 | $1,650 |

A taxpayer who is both 65+ AND blind gets the additions stacked. This effectively shifts the breakeven for older filers. The separate $6,000 senior deduction on Schedule 1-A (2025–2028, phased out above $75,000 / $150,000 MAGI) is available whether or not the user itemizes.

### Dependents

A taxpayer claimed as a dependent on someone else's return has a reduced standard deduction (greater of $1,350 or earned income + $450, capped at the regular standard deduction for the filing status; same figures for 2025 and 2026).

---

## When itemizing typically wins

Patterns where itemized usually beats standard:

### Pattern 1: Homeowner in a high-tax state with a mortgage

The classic itemizer profile:
- Mortgage interest of $10,000+ on Line 8a
- State + local + property taxes hitting or near the SALT cap on Line 5e ($40,000 for 2025, $40,400 for 2026)
- Total around $30,000-$50,000

For MFJ ($31,500 standard for 2025), this beats standard by up to about $18,500. For Single ($15,750), it beats standard handily.

Top states: California, New York, New Jersey, Connecticut, Massachusetts, Maryland, Hawaii, Oregon, Vermont, DC.

### Pattern 2: Major medical year

A taxpayer with high medical expenses (long hospital stay, major surgery, ongoing treatment) plus moderate other itemized deductions. The 7.5% AGI floor consumes a lot, but a single $30K out-of-pocket year at $80K AGI deducts $24K, beating the single standard deduction on its own.

### Pattern 3: Large charitable giver

Cash contributions exceeding 5-10% of AGI. At $200K AGI giving $30K to charity plus typical state income tax, itemizing beats the $31,500 MFJ standard deduction. (Tax year 2026+: the 0.5% floor removes the first $1,000 at $200K AGI.)

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

States with no tax on wages: AK, FL, NV, NH, SD, TN, TX, WA, WY. State sales tax from the optional tables is usually a few thousand dollars at typical incomes (look it up; don't guess). Property tax + sales tax + mortgage interest typically falls short of the $31,500 MFJ standard deduction.

### Pattern 3: Recent retiree before mortgage paid off, no major medical

Mortgage interest declines as principal pays down. Property tax + state income tax (if any) + small charity might total $15K-$25K. Below MFJ standard.

### Pattern 4: Young single with student loans (above-the-line) and rental

Student loan interest is above-the-line on Schedule 1 — doesn't help Schedule A. Rental, no charity, modest state tax: standard wins.

---

## Quick breakeven examples

### Single, $15,750 standard (2025)

| Profile | Total itemized | Result |
|---------|----------------|--------|
| Renter, $2,000 SALT, $1,500 charity | $3,500 | Standard wins by $12,250 |
| Homeowner CA, $3K mortgage, $5K SALT, $1K charity | $9,000 | Standard wins by $6,750 |
| Homeowner NY, $8K mortgage, $14K SALT, $3K charity | $25,000 | Itemize, gain $9,250 |
| $25K medical year at $80K AGI ($25K − $6K floor = $19K), $5K SALT | $24,000 | Itemize, gain $8,250 |

### MFJ, $31,500 standard (2025)

| Profile | Total itemized | Result |
|---------|----------------|--------|
| Renter MFJ, $4K SALT, $2K charity | $6,000 | Standard wins by $25,500 |
| Homeowner TX, $10K mortgage, $9K property tax, $1.2K sales tax (illustrative table amount), $3K charity | $23,200 | Standard wins by $8,300 |
| Homeowner CA, $12K mortgage, $15K state income, $9K property tax, $4K charity | $40,000 | Itemize, gain $8,500 |
| Homeowner NJ, $20K mortgage, $25K SALT (under the cap), $5K charity | $50,000 | Itemize, gain $18,500 |

(SALT cap applied at $40,000 for 2025, not the old $10K; none of these profiles exceeds $500K MAGI.)

---

## Close cases — bunching strategy

Bunching is the practice of concentrating itemizable expenses into alternating years so that itemizing wins in "bunch" years and standard wins in "off" years. The total deduction over multiple years is higher than always taking the standard.

### How bunching works

Imagine an MFJ couple (2026, AGI $180,000) with $14,000 of state and local taxes, $9,000 of mortgage interest, and $8,000 of yearly church giving. Itemized each year: $14,000 + $9,000 + ($8,000 − $900 floor) = $30,100, under the $32,200 standard deduction. Default approach: take $32,200 each year; two-year total $64,400.

Bunching approach: give two years of church money ($16,000) in year 1 and nothing in year 2. Year 1 itemized: $14,000 + $9,000 + ($16,000 − $900) = $38,100. Year 2: $23,000 itemized, so take the $32,200 standard deduction. Two-year total: $70,300. Net gain: $5,900 of additional deduction every two years, worth $1,298 at the 22% bracket. (In the off year the couple could also use the §170(p) non-itemizer deduction for any cash gifts they do make.)

### What's bunchable

- **Charity**: easiest. Donate two years of giving in December of a "bunch" year. Donor-advised funds (DAFs) make this clean — fund the DAF in a bunch year, distribute over multiple years from the DAF.
- **Medical expenses**: harder; you can't postpone surgery, but you can sometimes accelerate elective procedures or large prescriptions.
- **Property tax**: in some jurisdictions, prepay the next year's property tax in December of the current year. Verify the locality permits prepayment AND has actually assessed the tax (only taxes paid in the year and assessed before the next year are deductible: 2025 Schedule A instructions, line 5b; IRS news release IR-2017-210).
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

### Bunching example (2026 rules: $32,200 MFJ standard, 0.5% floor)

MFJ couple, $200K AGI, normally gives $5K to church annually + has $20K SALT (under the cap) + $10K mortgage interest. Itemized each year: $20K + $10K + ($5K − $1K floor) = $34K, which beats the $32,200 standard by $1,800.

Switch to bunching: contribute $25K to a DAF in year 1 (5 years × $5K): $20K + $10K + ($25K − $1K) = $54K itemized in year 1. In years 2-5 itemized is $30K, so take the $32,200 standard.

Five-year totals:
- Always itemize: $34K × 5 = $170,000
- Bunch + DAF: $54,000 + ($32,200 × 4) = $182,800

Bunching wins by $12,800 of deduction (about $2,816 at the 22% bracket). It wins here because the off-year itemized total ($30K) falls below the standard deduction once the giving moves to year 1, and because the floor is taken once instead of five times. Run the math for each user; bunching doesn't always pay.

### Where bunching wins even without itemizing today

MFJ couple, $200K AGI, $5K church + $9K SALT (no income tax state, just property + sales tax) + $4K mortgage = $17K itemized after the $1K floor. Standard MFJ $32,200. Don't itemize at all.

Bunch: give $25K to a DAF in year 1: $9K + $4K + ($25K − $1K) = $37K. Itemize, beat standard by $4,800. In years 2-5, take the $32,200 standard. Five-year total: $37,000 + ($32,200 × 4) = $165,800 vs always-standard $32,200 × 5 = $161,000. Net gain $4,800 from bunching, worth $1,056 at the 22% bracket.

This is the bunching sweet spot: when normal-year itemized < standard, but bunching pushes occasional years above standard. (Gifts to a DAF don't qualify for the §170(p) non-itemizer deduction.)

---

## Always run both — even if you "know" the answer

Software running tax returns should compute both regardless of user assumption. Common surprises:

- "I always took the standard" — until they had a major medical year
- "I'm not a homeowner" — but they paid $15K of state income tax on a high salary in a high-tax state
- "I don't have enough deductions" — until the SALT cap quadrupled under OBBBA for 2025
- "Itemizing is for rich people" — until the user had a federally declared (or, for 2026+, State declared) disaster loss

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
- P.L. 119-21 §70102 (IRC §63(c)(7)) — 2025 standard deduction $15,750 / $31,500 / $23,625
- [Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) §2.15(2)–(3) — 2025 dependent and age/blindness amounts
- [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) §4.14 — 2026 standard deduction and additions; §4.01 — 2026 37% bracket starts for the IRC §68 limitation
- IRC §68 and §170(b)(1)(I), §170(p) as amended by P.L. 119-21 §§70111, 70424, 70425 (2026+)
- [IRS Publication 17](https://www.irs.gov/publications/p17) — Your Federal Income Tax (chapter on standard deduction)
- [IR-2017-210](https://www.irs.gov/newsroom/irs-advisory-prepaid-real-property-taxes-may-be-deductible-in-2017-if-assessed-and-paid-in-2017) — IRS news release: prepaid property tax must be assessed first
- [Schedule A Instructions](https://www.irs.gov/pub/irs-pdf/i1040sca.pdf)
