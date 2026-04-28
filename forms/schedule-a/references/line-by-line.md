# Schedule A Line-by-Line Reference

Complete lookup for every line on Schedule A (Form 1040). Use this when the agent needs to confirm where an itemized deduction belongs or what a line means. The form has 17 numbered lines plus subletters.

The official IRS source is the [Schedule A instructions](https://www.irs.gov/pub/irs-pdf/i1040sca.pdf) for the relevant tax year.

---

## Header (identifies you)

| Field | What goes here | Notes |
|-------|----------------|-------|
| Name(s) shown on Form 1040 | Filer's legal name(s) | If MFJ, both names |
| Your SSN | Filer's SSN | If MFJ, primary filer's SSN (matches Form 1040) |

---

## Lines 1-4 — Medical and Dental Expenses

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 1 | Medical and dental expenses | Out-of-pocket payments for qualified medical care for filer, spouse, dependents (see Pub 502) | Amounts reimbursed by insurance, HSA, FSA, HRA; cosmetic surgery; OTC drugs without prescription; gym memberships |
| 2 | Enter amount from Form 1040 line 11 (AGI) | AGI | |
| 3 | Multiply line 2 by 7.5% (0.075) | (computed) | |
| 4 | Subtract line 3 from line 1 (≥ 0) | Deductible medical | |

**Critical rule for Line 1**: Only the *out-of-pocket* portion. If insurance paid $8,000 of a $10,000 surgery, only $2,000 goes on Line 1. Premiums paid through an employer cafeteria plan (pre-tax) are NOT deductible on Schedule A — they were already excluded from W-2 box 1.

**Medical mileage** (21¢/mile for 2025; 2026 rate announced ~December 2025) is added to Line 1, not separately. Keep a contemporaneous mileage log.

See [`medical-expenses.md`](./medical-expenses.md) for the full Pub 502 qualifying-expense list.

---

## Lines 5-7 — Taxes You Paid (SALT)

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 5a | State and local income taxes OR general sales taxes | One or the other, whichever is larger. Check the box if entry is sales tax. | Federal income tax; state income tax refunds (those are income on Schedule 1 if itemized prior year); Social Security or Medicare tax |
| 5b | State and local real estate taxes | Property tax on personal-use real estate, value-based, uniformly assessed | Special assessments for local improvements (sidewalks, sewers); HOA fees; transfer taxes paid at closing (those go to basis) |
| 5c | State and local personal property taxes | Value-based portion of vehicle registration, boat registration, etc. | Flat-fee registration; license-plate fees with no value component |
| 5d | Add lines 5a through 5c | (computed) | |
| 5e | Smaller of line 5d or SALT cap | Capped at $10K (2024), $40K (2025), $40,400 (2026); MFS halved; phaseout if MAGI > $500K | |
| 6 | Other taxes | Foreign income tax (if not claimed as credit on Schedule 3); occupational taxes paid for the privilege of working in a profession | Most foreign tax should be on Schedule 3 as a credit, not here as a deduction — credit is usually better |
| 7 | Add lines 5e and 6 | (computed) | |

**Critical rule for Line 5a**: Pick income OR sales, never both. Use the higher amount. Sales tax is the better choice for filers in states with no income tax (Alaska, Florida, Nevada, South Dakota, Tennessee, Texas, Washington, Wyoming). Use the [IRS Sales Tax Deduction Calculator](https://apps.irs.gov/app/stdc/) or the optional sales tax tables in the Schedule A instructions.

See [`salt-cap.md`](./salt-cap.md) for the year-by-year cap and high-income phaseout.

---

## Lines 8-10 — Interest You Paid

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 8a | Home mortgage interest and points reported on Form 1098 | Box 1 (interest) + Box 6 (points) of Form 1098 from each lender, on a qualified residence | Interest on debt over the acquisition cap ($750K post-12/15/2017 or $1M grandfathered); HELOC interest used for non-home purposes |
| 8b | Home mortgage interest not reported on Form 1098 | Seller-financed mortgages where the lender is an individual; must list payee name + address + SSN/EIN | |
| 8c | Points not reported on Form 1098 | Points paid at closing on the purchase of a main home, deductible in full year of purchase if Pub 936 conditions met; otherwise amortized | Points paid on refinance — those amortize over the new loan's life |
| 8d | Mortgage insurance premiums | **Tax year 2026+ only** under OBBBA reinstatement; PMI/FHA/VA/RHS premiums; phaseout starts at $100K MAGI | **Leave blank for 2025 and earlier** — the deduction was eliminated 2022-2025 |
| 8e | Add lines 8a through 8d | (computed) | |
| 9 | Investment interest | From Form 4952. Limited to net investment income | Margin interest used to buy tax-exempt bonds; personal-use interest |
| 10 | Add lines 8e and 9 | (computed) | |

**Critical rule for Line 8a**: Form 1098 box 1 is the source of truth. If the user paid more than is on the 1098 (e.g., year-end accrued interest), only what's on the 1098 is automatically accepted. Discrepancies invite IRS notices.

See [`mortgage-interest.md`](./mortgage-interest.md) for the $750K cap, HELOC rules, refinance rules, and the average-balance method for over-cap loans.

---

## Lines 11-14 — Gifts to Charity

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 11 | Gifts by cash or check | Cash, check, credit card, electronic transfer, payroll deduction to 501(c)(3) public charities; 60% AGI ceiling | QCDs from IRA (those go on Form 1040 Line 4b as exclusions); gifts to political campaigns; gifts to individuals; "GoFundMe" gifts to individuals |
| 12 | Other than by cash or check | Non-cash: clothing, household goods, appreciated stock, real estate, vehicles. 30% AGI ceiling typically | Time/services (never deductible); blood donations; partial-interest gifts (with exceptions) |
| 13 | Carryover from prior year | Excess from prior years that exceeded the AGI ceiling; 5-year carryforward | |
| 14 | Add lines 11 through 13 | For tax year 2026+: subtract 0.5% × AGI from this total; only the excess is deductible | |

**Critical rule for Line 12**: Form 8283 is required if non-cash > $500. Qualified appraisal is required for any single non-cash item > $5,000 (except publicly traded securities).

**Critical rule for tax year 2026+**: A 0.5% AGI floor applies under new IRC §170(p). At $200K AGI, the first $1,000 of charitable contributions is non-deductible. Run the floor at Line 14, not at Line 11 or 12 individually.

See [`charitable-contributions.md`](./charitable-contributions.md) for substantiation requirements, AGI ceilings by donee type, QCDs, and the 0.5% floor.

---

## Line 15 — Casualty and Theft Losses

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 15 | Casualty and theft losses | Loss from a federally declared disaster, computed on Form 4684, after $100 per-event floor and 10% AGI floor | Personal theft losses outside disaster zones; auto-accident damage (unless in a federally declared disaster); decline in market value without an event |

**Critical rule**: Since TCJA (2018), only **federally declared disaster** losses are deductible on Schedule A. OBBBA made this restriction permanent. Verify the disaster's federal declaration at [FEMA Disaster Declarations](https://www.fema.gov/disaster/declarations).

**Computation per casualty**:
1. Loss = lesser of (a) decrease in FMV, or (b) adjusted basis
2. Subtract insurance reimbursement
3. Subtract $100 per casualty event
4. Sum all events
5. Subtract 10% × AGI
6. Remainder → Line 15

Form 4684 is required.

---

## Line 16 — Other Itemized Deductions

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 16 | Other — list type and amount | Gambling losses (capped at gambling winnings on Schedule 1 Line 8b); IRD federal estate tax; amortizable bond premium on taxable bonds; claim-of-right repayment > $3,000; unrecovered investment in pension at annuity end; impairment-related work expenses for disabled | Unreimbursed employee expenses (eliminated by TCJA, made permanent by OBBBA); tax preparation fees (eliminated); investment advisory fees (eliminated); union dues (eliminated); safe deposit box (eliminated) |

The 2%-of-AGI floor miscellaneous deductions are gone permanently. Don't enter them on Line 16.

---

## Line 17 — Total Itemized Deductions

```
Line 17 = Line 4 + Line 7 + Line 10 + Line 14 + Line 15 + Line 16
```

Flows to **Form 1040 Line 12** in place of the standard deduction.

If Line 17 ≤ standard deduction for the user's filing status, **take the standard deduction and don't file Schedule A**. The only exception: MFS where one spouse itemizes and forces the other to itemize regardless (IRC §63(c)(6)(A)) — even at a smaller deduction.

---

## Quick reference: Schedule A line → form/publication

| Schedule A line | Primary IRC section | Primary IRS publication | Required attachments |
|-----------------|---------------------|--------------------------|----------------------|
| 1-4 (Medical) | §213 | Pub 502 | None |
| 5-7 (SALT) | §164 (cap at §164(b)(6)) | Pub 17 | None |
| 8-10 (Interest) | §163(h) | Pub 936 | Form 4952 if Line 9 > 0; statement if Line 8b used |
| 11-14 (Charity) | §170 (floor at §170(p)) | Pub 526 | Form 8283 if non-cash > $500; appraisal if > $5,000 |
| 15 (Casualty) | §165(h) | Pub 547 | Form 4684 |
| 16 (Other) | varies | Pub 17, 529 | varies |

---

## Sequence number

Schedule A is **attachment sequence 07**. When stapling a paper return, Schedule A goes ahead of Schedule B (sequence 08), Schedule C (09), Schedule D (12), etc.

---

## What was eliminated (don't put these on Schedule A)

The following used to be deductible on Schedule A pre-2018 and remain non-deductible permanently after OBBBA:

- Unreimbursed employee business expenses (former Form 2106) — only specific categories survive (impairment-related, qualified performing artists per §62(b), DOE/national-guard travel)
- Tax preparation fees
- Investment advisory fees, IRA custodial fees
- Safe deposit box rental
- Union dues (employees)
- Hobby expenses (capped at hobby income)
- Personal casualty losses outside federally declared disasters
- Personal theft losses outside federally declared disaster contexts

If a user asks where any of these go: they don't. Self-employed taxpayers may be able to deduct similar items on Schedule C, but employees cannot deduct them anywhere.
