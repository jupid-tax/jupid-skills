# Schedule A Line-by-Line Reference

Complete lookup for every line on Schedule A (Form 1040). Use this when the agent needs to confirm where an itemized deduction belongs or what a line means. The form has 18 numbered lines (line 18 is a checkbox) plus subletters.

Verified on 2026-10-06 against the **2025 Schedule A** (Cat. No. 17145C, created 11/20/25) and the 2025 Instructions for Schedule A (Dec 8, 2025). The 2026 form was not yet released; re-check it at https://www.irs.gov/forms-pubs/about-schedule-a-form-1040 before a 2026 return. The official IRS source is the [Schedule A instructions](https://www.irs.gov/pub/irs-pdf/i1040sca.pdf) for the relevant tax year.

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
| 2 | Enter amount from Form 1040 or 1040-SR, line 11b | AGI | |
| 3 | Multiply line 2 by 7.5% (0.075) | (computed) | |
| 4 | Subtract line 3 from line 1 (≥ 0) | Deductible medical | |

**Critical rule for Line 1**: Only the *out-of-pocket* portion. If insurance paid $8,000 of a $10,000 surgery, only $2,000 goes on Line 1. Premiums paid through an employer cafeteria plan (pre-tax) are NOT deductible on Schedule A — they were already excluded from W-2 box 1. If advance premium tax credit was paid or the user may claim the premium tax credit, complete Form 8962 before line 1 (2025 instructions, line 1).

**Medical mileage** (21¢/mile for 2025; 20.5¢ for January–June 2026 and 23.5¢ for July–December 2026, IR-2025-128 / IR-2026-29) is added to Line 1, not separately. Keep a contemporaneous mileage log.

See [`medical-expenses.md`](./medical-expenses.md) for the full Pub 502 qualifying-expense list.

---

## Lines 5-7 — Taxes You Paid (SALT)

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 5a | State and local income taxes OR general sales taxes | One or the other, whichever is larger. Check the box if entry is sales tax. | Federal income tax; state income tax refunds (those are income on Schedule 1 if itemized prior year); Social Security or Medicare tax |
| 5b | State and local real estate taxes | Property tax on personal-use real estate, value-based, uniformly assessed | Special assessments for local improvements (sidewalks, sewers); HOA fees; transfer taxes paid at closing (those go to basis) |
| 5c | State and local personal property taxes | Value-based portion of vehicle registration, boat registration, etc. | Flat-fee registration; license-plate fees with no value component |
| 5d | Add lines 5a through 5c | (computed) | |
| 5e | Smaller of line 5d or $40,000 ($20,000 MFS) for 2025 | Use the State and Local Tax Deduction Worksheet if Form 1040 line 11b exceeds $500,000 ($250,000 MFS) or Form 2555/4563/Puerto Rico exclusion applies; cap is $10K (2024), $40,000 (2025), $40,400 (2026, IRC §164(b)(7)); MFS halved | U.S. territory taxes (they go on 5a–5c); federal estate tax on IRD (line 16) |
| 6 | Other taxes | Income taxes paid to a foreign country (if not claimed as a credit on Schedule 3); generation-skipping tax on certain income distributions. Enter one total and list each type | Foreign real property taxes (not deductible); most foreign income tax is better as a Schedule 3 credit — compare |
| 7 | Add lines 5e and 6 | (computed) | |

**Critical rule for Line 5a**: Pick income OR sales, never both. Use the higher amount. Sales tax is the better choice for filers in states with no income tax (Alaska, Florida, Nevada, South Dakota, Tennessee, Texas, Washington, Wyoming). Use the IRS Sales Tax Deduction Calculator (IRS.gov/SalesTax) or the 2025 optional sales tax tables and worksheet in the Schedule A instructions.

See [`salt-cap.md`](./salt-cap.md) for the year-by-year cap and high-income phaseout.

---

## Lines 8-10 — Interest You Paid

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 8 (checkbox) | Check if any home mortgage proceeds were not used to buy, build, or improve the home | Then figure deductible interest with Pub 936 | |
| 8a | Home mortgage interest and points reported on Form 1098 | Box 1 (interest) + Box 6 (points) of Form 1098 from each lender, on a qualified residence, limited to the deductible amount (Pub 936) | Interest on debt over the acquisition cap ($750K post-12/15/2017 or $1M grandfathered); HELOC interest used for non-home purposes; don't reduce for a box 4 refund (Schedule 1 line 8z instead) |
| 8b | Home mortgage interest not reported on Form 1098 | Seller-financed mortgages where the lender is an individual (list payee name + SSN/EIN + address on the dotted lines; $50 penalty if omitted); your share of interest reported on someone else's 1098 | |
| 8c | Points not reported on Form 1098 | Points paid at closing on the purchase of a main home, deductible in full year of purchase if Pub 936 conditions met; otherwise amortized | Points paid on refinance — those amortize over the new loan's life |
| 8d | **Reserved for future use** (2025 form) | Nothing for 2025. Mortgage insurance premiums are not deductible for 2025; for 2026+ they are qualified residence interest again (IRC §163(h)(3)(E), P.L. 119-21 §70108) with an AGI phase-out from $100,000 to $109,000 ($50,000–$54,500 MFS). Confirm the 2026 form's line | Mortgage insurance premiums on a 2025 return |
| 8e | Add lines 8a through 8c | (computed) | |
| 9 | Investment interest | Form 4952 attached if required (not required if investment interest is less than interest + ordinary dividends minus qualified dividends, no other investment expenses, and no 2024 carryover). Limited to net investment income | Margin interest used to buy tax-exempt bonds; personal-use interest; interest allocable to passive activities |
| 10 | Add lines 8e and 9 | (computed) | |

**Critical rule for Line 8a**: Start from Form 1098 box 1. If the user paid more deductible interest to the lender than the 1098 shows, enter the larger deductible amount and explain the difference (paper return: attached statement and "See attached" next to line 8a) (2025 instructions, line 8a). If the user claims the mortgage interest credit, subtract Form 8396 line 3.

See [`mortgage-interest.md`](./mortgage-interest.md) for the $750K cap, HELOC rules, refinance rules, and the average-balance method for over-cap loans.

---

## Lines 11-14 — Gifts to Charity

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 11 | Gifts by cash or check | Cash, check, credit card, electronic transfer, payroll deduction to qualified organizations, plus out-of-pocket volunteer costs; 60% AGI ceiling for cash to public charities (see Pub 526 if over 30% of line 11b) | QCDs from IRA (excluded from income on Form 1040 lines 4a/4b with the "QCD" box on line 4c); gifts to political campaigns; gifts to individuals; "GoFundMe" gifts to individuals |
| 12 | Other than by cash or check | Non-cash: clothing, household goods, appreciated stock, real estate, vehicles. Form 8283 if over $500. Ceilings depend on property type and donee (30% for capital gain property to public charities; see Pub 526 if over 20% of line 11b) | Time/services (never deductible); blood donations; partial-interest gifts (with exceptions) |
| 13 | Carryover from prior year | Excess from prior years that exceeded the AGI ceiling; 5-year carryforward | |
| 14 | Add lines 11 through 13 | 2025: the sum. 2026+: reduced by the 0.5% floor on the contribution base (confirm how the 2026 form shows it) | |

**Critical rule for Line 12**: Form 8283 is required if non-cash deductions exceed $500. A qualified appraisal is required for any item or group of similar items deducted at more than $5,000 (Form 8283 Section B), except publicly traded securities.

**Critical rule for tax year 2026+**: A 0.5% floor applies under IRC §170(b)(1)(I) (P.L. 119-21 §70425): contributions are deductible only to the extent they exceed 0.5% of the contribution base (AGI figured without NOL carrybacks). At $200K AGI, the first $1,000 of charitable contributions is non-deductible. The statute applies the floor across contribution categories in a set order, so apply it to the total, not line by line. Non-itemizers get a separate deduction for up to $1,000 ($2,000 joint) of cash gifts to public charities (IRC §170(p)); that is not a Schedule A item.

See [`charitable-contributions.md`](./charitable-contributions.md) for substantiation requirements, AGI ceilings by donee type, QCDs, and the 0.5% floor.

---

## Line 15 — Casualty and Theft Losses

| Line | Field | What goes here | What does NOT go here |
|------|-------|----------------|------------------------|
| 15 | Casualty and theft losses from a federally declared disaster (other than net qualified disaster losses) | Form 4684 line 18, after the $100 per-event floor and 10% AGI floor | A net qualified disaster loss (Form 4684 line 15 goes on line 16); personal theft losses outside disaster zones; auto-accident damage (unless in a declared disaster); decline in market value without an event |

**Critical rule**: For 2018–2025, only **federally declared disaster** losses are deductible on line 15 (2025 instructions, line 15). For 2026+, P.L. 119-21 §70109 made the limitation permanent and also allows losses from a **State declared disaster** (IRC §165(h)(5)(A), (C)). Verify a federal declaration at [FEMA Disaster Declarations](https://www.fema.gov/disaster/declarations).

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
| 16 | Other — list type and amount | Only the instructions' list: gambling losses (capped at gambling winnings on Schedule 1 line 8b); casualty and theft losses of income-producing property (Form 4684 lines 32 and 38b, Form 4797 line 18a); federal estate tax on IRD; amortizable bond premium; ordinary loss on a contingent payment or inflation-indexed debt instrument; claim-of-right repayment > $3,000; certain unrecovered investment in a pension; impairment-related work expenses of a disabled person; net qualified disaster loss (from Form 4684 line 15, labeled "Net Qualified Disaster Loss") | Unreimbursed employee expenses; tax preparation fees; investment advisory fees; union dues; safe deposit box (all miscellaneous itemized deductions, suspended by IRC §67(h)) |

The 2%-of-AGI floor miscellaneous deductions remain suspended with no end date (IRC §67(h)). Don't enter them on Line 16. From 2026, unreimbursed educator expenses are excluded from "miscellaneous itemized deductions" (IRC §67(b)(13), (g)); check the 2026 instructions for their line.

**Non-itemizer with a net qualified disaster loss**: the increased standard deduction is also claimed on line 16 (both amounts listed on the dotted line; no other Schedule A lines; total to Form 1040 line 12e) (2025 instructions, line 16).

---

## Line 17 — Total Itemized Deductions

```
Line 17 = Line 4 + Line 7 + Line 10 + Line 14 + Line 15 + Line 16
```

Flows to **Form 1040 line 12e** in place of the standard deduction.

If Line 17 ≤ standard deduction for the user's filing status, **take the standard deduction and don't file Schedule A**. Exceptions: MFS where one spouse itemizes and forces the other to itemize regardless (IRC §63(c)(6)(A)), and a user who elects to itemize for state or other purposes (line 18).

2026+: itemized deductions may be reduced by 2/37 under IRC §68 (as amended by P.L. 119-21 §70111) when taxable income exceeds the start of the 37% bracket.

## Line 18 — Election to itemize

| Line | Field | What goes here |
|------|-------|----------------|
| 18 | Checkbox | Check only if the user elects to itemize even though the itemized total is less than the standard deduction (e.g., for state tax purposes) |

---

## Quick reference: Schedule A line → form/publication

| Schedule A line | Primary IRC section | Primary IRS publication | Required attachments |
|-----------------|---------------------|--------------------------|----------------------|
| 1-4 (Medical) | §213 | Pub 502 | Form 8962 first if premium tax credit involved |
| 5-7 (SALT) | §164 (cap at §164(b)(6)–(7)) | Pub 17 | None |
| 8-10 (Interest) | §163(h) | Pub 936 | Form 4952 if Line 9 > 0; statement if Line 8b used |
| 11-14 (Charity) | §170 (2026+ floor at §170(b)(1)(I)) | Pub 526 | Form 8283 if non-cash > $500; appraisal if an item or group > $5,000 (not publicly traded securities) |
| 15 (Casualty) | §165(h) | Pub 547 | Form 4684 |
| 16 (Other) | varies | Pub 17, 529 | varies |

---

## Sequence number

Schedule A is **attachment sequence 07**. When stapling a paper return, Schedule A goes ahead of Schedule B (sequence 08), Schedule C (09), Schedule D (12), etc.

---

## What was eliminated (don't put these on Schedule A)

The following used to be deductible on Schedule A pre-2018 and remain non-deductible (IRC §67(h), §165(h)(5); P.L. 119-21 removed the 2025 sunset):

- Unreimbursed employee business expenses (former Form 2106) — only specific categories survive (impairment-related, qualified performing artists per §62(b), DOE/national-guard travel)
- Tax preparation fees
- Investment advisory fees, IRA custodial fees
- Safe deposit box rental
- Union dues (employees)
- Hobby expenses (capped at hobby income)
- Personal casualty losses outside federally declared disasters (2026+: outside federally or State declared disasters)
- Personal theft losses outside declared-disaster contexts

If a user asks where any of these go: they don't. Self-employed taxpayers may be able to deduct similar items on Schedule C, but employees cannot deduct them anywhere.
