# Reasonable Collection Potential (RCP) — How the Minimum Offer Is Built

The minimum offer on Form 433-A (OIC) Section 8 (or Form 433-B (OIC) Section 5) is the taxpayer's version of what the IRS calls reasonable collection potential: net realizable equity in assets plus the value of future income. The IRS recomputes it during the investigation under IRM 5.8.5, Financial Analysis (effective 04-23-2026), https://www.irs.gov/irm/part5/irm_05-008-005r. This file explains each component so the agent can compute it, flag the soft spots, and ask the right questions.

---

## 1. The formula

```
RCP (individual) = Box A (personal equity) + Box B (business equity, sole proprietor)
                   + Box F × 12 (lump-sum offer)  or  Box F × 24 (periodic offer)

RCP (entity)     = Box A (Form 433-B (OIC)) + Box D × 12  or  Box D × 24
```

Sources: Form 433-A (OIC) Section 8; Form 433-B (OIC) Section 5; IRM 5.8.5.25 (future income: "realizable value of assets plus the amount that could be collected in 12 months" for offers paid in 5 months or less and 5 or fewer payments; 24 months for offers payable in 6 to 24 months).

The Form 656-B booklet, page 5, Step 5: "Your offer amount must be equal to or greater than the amount calculated in Form 433-A(OIC) or 433-B(OIC)." An offer below it needs a special-circumstances explanation (Form 656, Section 3) with documents.

---

## 2. Net realizable equity (NRE)

IRM 5.8.5.4.1: assets are valued at net realizable equity, defined as quick sale value (QSV) less amounts owed to secured lien holders with priority over the federal tax lien, and applicable exemption amounts.

- **Quick sale value.** "Normally, QSV is calculated at 80 percent of FMV." The IRS may use a higher or lower percentage depending on the asset and market, including full fair market value where property sells quickly. The forms build in × .8 for retirement accounts, real property, vehicles, valuables and personal effects, and business assets. Bank accounts, investment accounts, digital assets, and life insurance cash value are entered without the × .8 factor.
- **Asset sold to fund the offer.** No QSV reduction; the IRS uses the actual arm's-length sale price, less costs of sale and expected current-year tax (IRM 5.8.5.4.1).
- **Retirement accounts.** IRM 5.8.5.10: equity is the cash value less tax consequences of liquidation and any early-withdrawal penalty. The form uses × .8 and notes the reduction may be larger. If the user wants a larger reduction, ask for the expected tax and penalty figures and attach the computation. Voluntary contributions are not an allowable expense; significant voluntary contributions after assessment or within three years before the offer can be treated as a dissipated asset.
- **Cash.** IRM 5.8.5.7: bank balance less $1,000 (individual accounts only). The IRS reviews statements (generally three months for wage earners, six for non-wage earners) and may exclude balances needed for the month's allowable expenses when balances fluctuate.
- **Vehicles.** IRM 5.8.5.12: private-party value, usually × .8, then exclude $3,450 per car used for work, production of income, or family welfare (one car single, two cars joint).
- **Furniture and personal effects.** IRM 5.8.5.11: declared value usually accepted unless items of extraordinary value; the statutory levy exemption is subtracted ($11,980 for 2026 under IRC §6334(a)(2), Rev. Proc. 2025-32 §4.49; printed on line (7)).
- **Income-producing assets.** IRM 5.8.5.15: equity in income-producing assets is generally not added to RCP for a viable ongoing business unless the assets are not critical to operations; real property equity is included. The forms enter 0 for assets used in the production of income (Form 433-A (OIC) line (9a)/(9b); Form 433-B (OIC) line (5a) and its footnote).
- **Tools of the trade.** IRM 5.8.5.16: statutory levy exemption for an individual's tools used in a trade or business, updated annually, not available to entities. 2026 amount under IRC §6334(a)(3): $5,990 (Rev. Proc. 2025-32 §4.49). The form's line (10) prints no amount; disclose and let the user choose (see `collection-information-statements.md`).
- **Do not zero out assets** just because the taxpayer cannot borrow against them (IRM 5.8.5.4).

Asset values are subject to IRS adjustment (Form 433-A (OIC) Section 3 heading). If the IRS values an asset higher, it asks the taxpayer to raise the offer.

---

## 3. Future income and allowable expenses

### Income (Box D)

IRM 5.8.5.20: use current income as a rule. Exceptions in that section include temporarily unemployed or underemployed taxpayers (use expected income), irregular or fluctuating self-employment income (average the three prior years; not for wage earners), imminent and documented retirement, regular overtime, and income that will stop (e.g., child support ending in 18 months). Ask the user about each that might apply; do not choose one silently.

Gifts that support the household are generally not income unless there is a right to them; a gap between stated income and expenses is discussed, not automatically added (IRM 5.8.5.20).

### Allowable expenses (Box E)

The IRS allows necessary expenses using the Collection Financial Standards (IRM 5.8.5.22, 5.8.5.22.1; IRC §7122(d)(2) requires published national and local allowances).

**Never estimate a standard amount.** Retrieve the current tables from https://www.irs.gov/businesses/small-businesses-self-employed/collection-financial-standards. The page states the standards are effective June 29, 2026 and are updated periodically. What to look up and what to ask:

| Line | Standard to look up | What to ask the user first | Rule |
|---|---|---|---|
| (39) Food, clothing, misc. | National Standards: food, clothing and other items, by household size | Household size | Enter the full standard even if actual spending is less (form note; CFS page: allowed "without questioning the amount actually spent") |
| (40) Housing and utilities | Local Standards: housing and utilities, by state, county, household size | County, household size, actual rent/mortgage + taxes + insurance + utilities + phones + internet | Enter actual; the IRS generally allows the lesser of actual or standard (CFS page; IRM 5.8.5.22.2) |
| (41) Vehicle ownership | Local Standards: transportation, ownership costs (nationwide) | Number of vehicles, monthly loan or lease payment | Lesser of actual or standard (IRM 5.8.5.22.3). No payment, no ownership allowance |
| (42) Vehicle operating | Local Standards: transportation, operating costs by Census Region or MSA | Region/metro area, actual monthly operating cost, vehicle age and mileage | Lesser of actual or standard; IRM 5.8.5.22.3 generally allows an extra $200 per month per vehicle over nine years old or with 125,000 miles or more (up to two vehicles on a joint offer) |
| (43) Public transportation | Public transportation standard (nationwide, per household) | Actual fares | No vehicle: standard allowed without verification; with a vehicle, lesser of actual or standard |
| (45) Out-of-pocket health care | National Standards: out-of-pocket health care, per person, under 65 / 65 and older | Ages of household members | Enter the full standard |

If the table for the user's county cannot be retrieved, stop at Box E and tell the user. Present lines (39) and (45) as "standard, table effective June 29, 2026, household of N" with the page URL, so a reviewer can trace them.

### Expenses that generally do not count

- Private school, college, and other tuition for dependents; charitable contributions; unsecured debt payments (Form 656-B, page 5). Credit card payments are already inside the line (39) miscellaneous standard (IRM 5.8.5.22.4).
- Voluntary retirement contributions, payroll savings, whole life premiums bought as investments (IRM 5.8.5.23).
- Conditional expenses and the one-year rule used for installment agreements do not apply to offers (IRM 5.8.5.23).
- Unsubstantiated court-ordered payments, child care, life insurance, other secured debt, or other expenses are treated as not paid (IRM 5.8.5.22.4).
- Student loans: minimum payments on federally guaranteed loans for the taxpayer's own post-high-school education are allowed with proof of payment (IRM 5.8.5.22.4); they go on line (50).
- Current taxes are allowed even if not paid in the past; for wage earners, the pay stub amount (IRM 5.8.5.22.4).
- Delinquent state or local tax payments may be limited to a proportional share of disposable income (IRM 5.8.5.22.4); ask for the state balance and any existing state agreement.

### Shared households and non-liable spouses

IRM 5.8.5.24: when the taxpayer shares expenses with a non-liable person, the IRS determines the taxpayer's percentage of household income and applies it to shared expenses; community property and domestic partnership states follow state law. Ask: Who lives in the household? Who pays which bills? Does the non-liable spouse agree to have income considered? Was the user married and living in a community property state in the last ten years? Do not decide the allocation without those answers; flag it for a representative if the facts are mixed.

### Business income (Box C)

Non-cash expenses (depreciation, depletion) are not allowed; actual cash payments, including principal on loans for income-producing assets, are allowed (IRM 5.8.5.26). Add Schedule C depreciation back. Ask whether vehicle costs used the standard mileage rate.

---

## 4. The multiplier and the collection statute

- **Lump sum (5 or fewer payments within 5 months):** Box F × 12.
- **Periodic (6 to 24 months):** Box F × 24.
- **Limit:** "For lump sum cash and periodic payment offers, when there are less than 12 or 24 months remaining on the statutory period for collection on all tax periods, use the number of months remaining on the statutory period for collection" (IRM 5.8.5.25). Its examples: an offer covering only 2012 with 10 months left uses 10 months; an offer covering 2012, 2015, and 2021 with 3, 40, and 111 months left is **not** limited to 3 months.

Collection statute expiration date (CSED): the IRS has 10 years after assessment to collect (IRC §6502(a)). The CSED can be suspended or extended (for example while an offer is pending, per Form 656 Section 7(p); while an installment agreement request is pending, per the Form 9465 instructions; or for time the taxpayer spent outside the U.S., per IRM 5.8.5.25.1), so assessment date plus 10 years is a starting point, not a final answer. Ask the user for an account transcript ([`../../form-4506-t/SKILL.md`](../../form-4506-t/SKILL.md) or the IRS online account) and read each period's assessment date. Do not compute a CSED without it, and tell the user the IRS's own CSED may be later.

Submitting an offer suspends the collection period while the offer is pending, for 30 days after a rejection, and during Appeals, and extends the assessment period by the pending time plus one year if the offer fails (Form 656, Section 7(p)).

---

## 5. The full-pay screen

Form 656-B, page 1: "Generally, the IRS will not accept an offer if you can pay your tax debt in full through an installment agreement and/or equity in assets." The $1,000 bank and $3,450 vehicle allowances apply only after that determination (same page; IRM 5.8.5.7; IRM 5.8.5.12).

Screen, as an approximation the user should confirm with the IRS Offer in Compromise Pre-Qualifier (https://irs.treasury.gov/oic_pre_qualifier/) or the Individual Online Account:

```
Equity without allowances = Box A recomputed with no $1,000 and no $3,450
                            (+ Box B)
Months available          = months from today to the latest CSED among the periods
Capacity                  = equity without allowances + Box F × months available
If capacity ≥ current balance (tax + penalties + interest), the user can likely full pay.
```

This screen ignores the interest that keeps accruing, so a "cannot full pay" result with little margin is not conclusive. When the screen says the user can full pay, stop the offer workflow, explain why, and route to [`../../form-9465/SKILL.md`](../../form-9465/SKILL.md). When it says the user cannot, continue, and state the margin in the validation summary.

---

## 6. After computing: special circumstances and ETA

- **Below RCP for doubt as to collectibility with special circumstances:** allowed only with a written explanation and documents (Form 656, Section 3; checklist page 29).
- **Effective tax administration (economic hardship or public policy/equity):** the taxpayer could pay in full. Whether the facts support ETA is a judgment call; refer the user to a CPA, enrolled agent, attorney, or Low Income Taxpayer Clinic. Still complete Form 433-A (OIC) in full.

Never present an offer amount without the line-by-line computation behind it.
