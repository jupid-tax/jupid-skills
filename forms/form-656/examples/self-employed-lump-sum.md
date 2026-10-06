# Example: Self-Employed HVAC Technician — Lump-Sum Offer

A sole proprietor with three years of income tax debt, business assets that are used to produce income, and a sister willing to lend part of the offer. Shows Form 433-A (OIC) Sections 3 to 8 with business Sections 4 to 6, the line (10) question, the full-pay screen, and Form 656 Sections 1 to 6.

> **Placeholder warning.** Lines (39) and (45) must come from the IRS Collection Financial Standards table effective June 29, 2026 (https://www.irs.gov/businesses/small-businesses-self-employed/collection-financial-standards). This example uses **PLACEHOLDER** figures ($1,040 on line (39), $84 on line (45)) so the arithmetic can be shown. They are not the official table values. An agent must replace them with the live table amounts for the user's household before producing a real draft, and then recompute Box E onward.

## The user

- **Name:** Dmitri Kovac, single, no dependents, household of 1
- **Residence:** rents an apartment in Pittsburgh, Allegheny County, Pennsylvania; never lived in a community property state
- **Business:** sole proprietorship, Kovac Heating & Cooling (DBA), residential HVAC repair; no employees; files Schedule C
- **Debt (from his IRS account transcript, pulled October 2026):**

| Form | Period end | Assessment date | Balance (tax, penalties, interest) | CSED (assessment + 10 years) |
|---|---|---|---|---|
| 1040 | 12-31-2021 | 05-23-2022 | $24,906 | 05-23-2032 |
| 1040 | 12-31-2022 | 06-12-2023 | $26,215 | 06-12-2033 |
| 1040 | 12-31-2023 | 06-17-2024 | $20,317 | 06-17-2034 |
| **Total** | | | **$71,438** | |

## Eligibility screen (agent's questions and his answers)

| Check | Answer | Evidence requested |
|---|---|---|
| All required returns filed (2021 to 2025) | Yes; 2025 filed 04-14-2026 | Transcript shows returns posted |
| Bill received for at least one period | Yes, CP14s and CP501s | Notices |
| 2026 estimated payments current | Yes, Q1 to Q3 paid | EFTPS confirmations |
| Employer deposits | Not required; no employees | — |
| Open bankruptcy, audit, innocent spouse claim | None | — |
| Disputes the tax? | No; says he owes it | → doubt as to collectibility, Form 656 |

Penalty abatement was checked first through [`../../form-843/SKILL.md`](../../form-843/SKILL.md): the user said first-time abatement was already granted for 2021 in 2023, so no further abatement is available on that basis. The balance above is after that abatement.

## Form 433-A (OIC) — Section 3, personal assets

| Line | Inputs (all from user statements dated September 2026) | Computation | Amount |
|---|---|---|---|
| (1a) | Personal checking, First Commonwealth | balance | $2,847 |
| (1b) | Personal savings, same bank | balance | $1,210 |
| (1c) | No other accounts | — | $0 |
| **(1)** | | 2,847 + 1,210 + 0 − 1,000 | **$3,057** |
| (2a)–(2d) | No brokerage or digital assets (asked about Coinbase, Robinhood, PayPal balances: none) | — | $0 |
| **(2)** | | | **$0** |
| (3a) | Traditional IRA, Fidelity, market value $14,380, no loan | 14,380 × .8 − 0 | $11,504 |
| (3b) | None | — | $0 |
| **(3)** | | | **$11,504** |
| **(4)** | Term life only, no cash value | | **$0** |
| **(5)** | Rents; owns no real property | | **$0** |
| (6a) | 2019 Honda CR-V, 61,400 miles, private-party value $17,650, loan $9,876 | 17,650 × .8 − 9,876 = 14,120 − 9,876 | $4,244 |
| (6b) | | 4,244 − 3,450 | $794 |
| (6c) | No second personal vehicle | — | $0 |
| (6d) | Not a joint offer → (6c) unchanged | — | $0 |
| (6e) | None | — | $0 |
| **(6)** | | 794 + 0 + 0 | **$794** |
| (7a) | No art, jewelry, collections, or private business interests | — | $0 |
| (7b) | Furniture and personal effects, user's estimate $6,200 | 6,200 × .8 − 0 | $4,960 |
| (7c) | None | — | $0 |
| **(7)** | | 0 + 4,960 + 0 − 11,980 → negative | **$0** |
| **Box A** | | 3,057 + 0 + 11,504 + 0 + 0 + 794 + 0 | **$15,355** |

Flag on line (3): the × .8 factor may understate the income tax and early-withdrawal cost of liquidating a 41-year-old's IRA; the form allows a larger reduction with support (IRM 5.8.5.10). The user chose not to compute it.

## Sections 4 and 5 — business information and assets

Section 4: sole proprietorship, Yes; no EIN; no employees; no other business interests.

| Line | Inputs | Computation | Amount |
|---|---|---|---|
| (8a) | Business checking, PNC | balance (no $1,000 allowance) | $4,126 |
| (8b)–(8d) | None | — | $0 |
| **(8)** | | | **$4,126** |
| (9a) | 2020 Ford Transit work van; value $23,900, loan $18,060; used in the production of income | form: enter 0 | $0 |
| (9b) | Refrigerant recovery machine, vacuum pumps, gauges, hand tools; value $5,100; no loan; used in the production of income | form: enter 0 | $0 |
| (9c) | None | — | $0 |
| **(9)** | | | **$0** |
| **(10)** | Tools-of-trade deduction; no amount printed on the form | line (9) is 0, so no effect | **$0** |
| **(11)** | | 0 − 0 | **$0** |
| Receivables | Accounts receivable: Yes. Three open invoices totaling $2,940 (ages 12, 26, 41 days); list attached | no line value | — |
| **Box B** | | 4,126 + 0 | **$4,126** |

Flags shown to the user:

- The van ($23,900 × .8 − $18,060 = $1,060 equity) and tools ($5,100 × .8 = $4,080) are entered as 0 because the form says to. IRM 5.8.5.15 lets the IRS add that equity if it decides the assets are not critical to the business.
- The $2,940 of receivables is attached as a list; the IRS can treat collectible receivables as an asset (IRM 5.8.5.14).

## Section 6 — business income and expenses (12-month average, Oct 2025 to Sep 2026)

Built from his bookkeeping, not from the 2025 Schedule C, because his customer mix changed in 2026. Depreciation on the van ($4,780 on the 2025 Schedule C) is excluded as a non-cash expense.

| Line | Item | Amount |
|---|---|---|
| (12) | Gross receipts | $9,412 |
| (13)–(16) | Rental, interest, dividends, other | $0 each |
| **(17)** | Total income | **$9,412** |
| (18) | Materials purchased (parts, refrigerant) | $2,186 |
| (19) | Inventory purchased | $0 |
| (20) | Gross wages | $0 |
| (21) | Rent | $0 |
| (22) | Supplies | $214 |
| (23) | Utilities/telephones (business phone line, dispatch app) | $128 |
| (24) | Vehicle costs, van (fuel, oil, repairs) | $671 |
| (25) | Business insurance (general liability) | $236 |
| (26) | Current business taxes | $0 |
| (27) | Secured debt: van loan payment | $487 |
| (28) | Other business expenses | $0 |
| **(29)** | Total expenses | **$3,922** |
| **Box C** | 9,412 − 3,922 | **$5,490** |

## Section 7 — household income and expenses

| Line | Item | Source | Amount |
|---|---|---|---|
| (30) | Primary taxpayer wages, Social Security, pension, other | none | $0 |
| (31) | Spouse | single | $0 |
| (32)–(35) | Other contributors, interest, distributions, rental | none | $0 |
| (36) | Net business income from Box C | Section 6 | $5,490 |
| (37)–(38) | Child support, alimony received | none | $0 |
| **Box D** | | | **$5,490** |
| (39) | Food, clothing, misc. | **PLACEHOLDER** for the National Standard, 1 person; replace from the live table | $1,040 |
| (40) | Housing and utilities: rent $1,410 + electric/gas $151 + internet $64 + cell $60 | user actuals; compare to the Allegheny County, 1-person housing and utilities standard before finalizing | $1,685 |
| (41) | Vehicle loan, CR-V | user actual; compare to the ownership standard | $412 |
| (42) | Vehicle operating, CR-V (insurance, fuel, registration) | user actual; compare to the Northeast/Pittsburgh operating standard | $268 |
| (43) | Public transportation | none | $0 |
| (44) | Health insurance premiums (marketplace plan) | user actual | $447 |
| (45) | Out-of-pocket health care | **PLACEHOLDER** for the per-person under-65 standard; replace from the live table | $84 |
| (46)–(47) | Court-ordered payments, child care | none | $0 |
| (48) | Life insurance premiums (term, $250,000 policy) | user actual | $31 |
| (49) | Current monthly taxes: 2026 federal estimated payments plus Pennsylvania and Pittsburgh local estimates, monthly equivalent | user's 2026 vouchers | $1,118 |
| (50) | Secured debts/other | none | $0 |
| (51) | Delinquent state/local tax payments | none owed | $0 |
| **Box E** | 1,040 + 1,685 + 412 + 268 + 0 + 447 + 84 + 0 + 0 + 31 + 1,118 + 0 + 0 | | **$5,085** |
| **Box F** | 5,490 − 5,085 | | **$405** |

## Section 8 — minimum offer

| Box | Computation | Amount |
|---|---|---|
| Box G (lump sum) | 405 × 12 | $4,860 |
| Box H (periodic) | 405 × 24 | $9,720 |
| Lump-sum offer | A + B + G = 15,355 + 4,126 + 4,860 | **$24,341** |
| Periodic offer | A + B + H = 15,355 + 4,126 + 9,720 | $29,201 |

CSED check for the multiplier: the shortest remaining collection period is 67 months (2021 period, to May 2032), more than 24, so the 12 and 24 multipliers apply unchanged (IRM 5.8.5.25).

## Full-pay screen (without the $1,000 and $3,450 allowances)

| Component | Amount |
|---|---|
| Box A without allowances: 4,057 + 11,504 + 4,244 + 0 | $19,805 |
| Box B | $4,126 |
| Box F × 92 months (to the latest CSED, June 2034) = 405 × 92 | $37,260 |
| Capacity | **$61,191** |
| Worst case, adding van equity $1,060, tools $4,080, receivables $2,940 | $69,271 |
| Current balance | $71,438 |

Result: cannot full pay, even in the worst case, before accrued interest. The margin in the worst case is only $2,167, so the agent tells Dmitri the result is close and asks him to confirm with the IRS Pre-Qualifier (https://irs.treasury.gov/oic_pre_qualifier/) before paying the fee.

## Low-Income Certification

2025 AGI $61,212 and household gross monthly income × 12 = 5,490 × 12 = $65,880; both above $39,900 for a household of 1 in the 48 states. Does not qualify; fee and initial payment are due.

## Form 656 draft

**Top:** Pre-Qualifier used? Yes (after confirming the screen above).

**Section 1:** Dmitri Kovac, SSN XXX-XX-XXXX; physical address in Pittsburgh, PA, Allegheny County; not a new address; no EIN. Form 1040 periods: 12-31-2021, 12-31-2022, 12-31-2023. No TFRP, 941, 940, or other. Low-Income Certification: neither box checked.

**Section 2:** blank.

**Section 3:** ☒ Doubt as to Collectibility.

**Section 4:** ☒ Lump Sum.

| Field | Entry |
|---|---|
| Total offer amount | $24,341 |
| 20% initial payment | $4,869 (20% = $4,868.20, rounded up so it is not below 20%; user told) |
| Remaining balance | $19,472 |
| Payment 1 | $9,736 payable within 1 month after acceptance |
| Payment 2 | $9,736 payable within 3 months after acceptance |

**Section 5:** designate the initial payment to tax period 12-31-2021 (user's choice). Fee and initial payment paid by EFTPS on the mailing date; record both 15-digit EFT numbers and dates.

**Section 6:** Source of funds: initial payment from personal and business checking; remaining $19,472 from a loan by his sister, Irena Kovac, under a signed promissory note (copy attached). ☒ All required returns filed; 2025 return filed within 10 weeks? No (filed 04-14-2026, more than 10 weeks before submission), so no copy required. ☒ Made all required 2026 estimated payments. ☒ Not required to make federal tax deposits.

**Section 8:** Dmitri signs and dates; voicemail box per his choice. **Section 9:** blank (no paid preparer).

## Package and filing

- Form 656, Form 433-A (OIC) signed, attachments: three months of personal bank statements, six months of business bank statements, IRA statement, CR-V and van loan statements, receivables list, 12-month P&L, promissory note.
- Pays $205 fee and $4,869 initial payment by EFTPS (separately) on the mailing date.
- Pennsylvania resident → Brookhaven IRS Center COIC Unit, P.O. Box 9007, Holtsville, NY 11742-9007 (Form 656-B, page 29). Or submit through his Individual Online Account instead; not both.

## Validation summary

- Math: all lines recomputed in Python; pass.
- Flags: lines (39) and (45) are placeholders in this example; lines (40) to (42) must be compared with the local standards; van and tools equity and receivables may be added by the IRS; full-pay margin is small; retirement reduction kept at × .8.
- Open questions: none after the user's answers above.
