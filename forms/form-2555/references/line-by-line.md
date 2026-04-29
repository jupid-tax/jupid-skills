# Form 2555 Line-by-Line Reference

Complete lookup for every line on Form 2555. Use when the agent needs to confirm where a value belongs or what a line means.

## Header

| Line | Field | What goes here | Notes |
|------|-------|----------------|-------|
| (top) | Name | Filer's legal name | Match Form 1040 |
| (top) | SSN | Filer's SSN | Or ITIN if no SSN |

---

## Part I — General Information

### Line 1 — Foreign address

The filer's foreign address during the qualifying period. If the filer has multiple foreign addresses (moved within country, between countries), use the principal one or the most-recent. Specific format: street, city, postal code, country.

### Line 2 — Occupation

Plain-English description of the work performed abroad: "Software engineer", "Independent management consultant", "International school teacher".

### Line 3 — Filer's US employer (if any)

If the filer's employer is a US company that sent them abroad, enter the US employer's name and address. If the filer is paid by a foreign entity directly, leave blank.

### Line 4a — Employer name (foreign address if applicable)

The actual employer paying the wages. Could be the same as Line 3 or different.

### Line 4b — US address of employer

If the employer is a US company. Otherwise blank.

### Line 4c — Foreign address of employer

If the employer is a foreign entity. Otherwise blank.

### Line 4d — Type of employer

Radio: A foreign entity / A US company / Self / A foreign affiliate of a US company / Other.

### Line 5 — Last year FEIE was claimed

Enter the most recent year the filer claimed FEIE. If first time, enter "Never".

### Line 6 — Test used last year (and revocation history)

- **6a** — Test used last year (BFR / PPT)
- **6b** — Have you ever revoked the FEIE election?
- **6c** — Date of revocation (if 6b = Yes)
- **6d** — Country of citizenship

If 6b = Yes and 6c is within last 5 years, the user is in the **5-year lock-out** under IRC §911(e)(2). They cannot re-elect FEIE without IRS consent (request via private letter ruling — costs ~$30,000 IRS user fee, generally not worth it).

### Line 7 — Bona fide residence or physical presence?

The user picks one test and fills the corresponding part:
- BFR → fill Part II
- PPT → fill Part III

### Line 8 — Family in foreign country

- **8a** — Yes/No
- **8b** — If 8b = No, location of family

### Line 9 — Tax home

Address and date the filer's tax home was established in the foreign country. The "tax home" concept under §911(d)(3) is the filer's regular or principal place of business. It must be in a foreign country to qualify for FEIE.

The "abode" rule disqualifies filers whose abode (i.e., their domestic life — home, family, social ties) remains in the US even if they work abroad. A US person who works abroad but spends weekends back home in the US, with family staying in US, may have abode in US and fail this test.

---

## Part II — Bona Fide Residence Test

The user must be a bona fide resident of one or more foreign countries for an **uninterrupted period that includes an entire tax year** (Jan 1 to Dec 31). US citizens only (resident aliens of countries with US tax treaties may also qualify).

### Line 10 — Bona fide residence began

Date the filer became a bona fide resident. Importantly, this date can be from a prior year — what matters is that the BFR period covers an entire current tax year. So a filer who established BFR on August 15, 2024 can claim BFR for the entire 2025 tax year (because they were a BFR for all of 2025 even though BFR started in 2024).

### Line 11 — Type of living quarters

Radio: rented house, rented room, leased apartment, owned house, etc.

### Lines 12-15 — Bona fide residence factors

- **12a/b** — Did family live with you in foreign country?
- **13a/b** — Did you submit a statement to foreign authorities you weren't a tax resident? (If Yes, BFR likely fails — being a BFR means you ARE a tax resident of the foreign country)
- **14** — Required to pay foreign country income tax? (Should be Yes for BFR)
- **15a-d** — Other factors (visa type, ties to foreign country, type of business presence, etc.)

The IRS uses these factors to evaluate the bona fide-ness of residence. A filer claiming BFR but with family still in the US, no foreign tax filed, and a tourist visa is at risk of disqualification.

---

## Part III — Physical Presence Test

The user is physically present in foreign countries for at least 330 full days during any 12 consecutive months. Available to US citizens AND resident aliens.

### Line 16 — 12-month qualifying period

Start date and end date of the 12-month period the user picked. Doesn't have to be the calendar year.

Example: filer arrived in Mexico on March 15, 2024. They count their 12-month period as March 15, 2024 to March 14, 2025. If they spent ≥ 330 days outside the US during this window, they qualify.

The exclusion is then pro-rated to the portion of the 2024 tax year covered (March 15, 2024 to Dec 31, 2024 = 292 days; 292/365 = 0.8 — exclusion capped at 80% of the FEIE annual cap for 2024).

### Line 17 — Principal country of employment

The country where the user did most of their work in the qualifying period.

### Line 18 — Travel summary table

Every period of physical presence by country. Format:

| Name of country | Date arrived | Date left | Number of days in country | Income earned in country | Tax paid to country |
|-----------------|--------------|-----------|---------------------------|--------------------------|---------------------|
| Mexico | 03/15/2024 | 06/30/2024 | 107 | $30,000 | $4,500 |
| Argentina | 07/01/2024 | 09/15/2024 | 76 | $22,000 | $3,200 |
| ...

**Critical: counting full days**

A "full day" abroad means a 24-hour period (midnight to midnight) entirely spent in a foreign country. If the user is in transit between the US and a foreign country, the day in transit (over international airspace/waters) is NOT a full day abroad. It's typically counted as a US day or a "no man's day" for FEIE purposes.

Travel days between two foreign countries (e.g., London to Tokyo via international airspace) are typically full days abroad if the filer doesn't transit through the US.

The qualifying period must contain ≥ 330 such full days.

---

## Part IV — All Filers — Foreign Earned Income

Foreign earned income (FEI) per IRC §911(b): payments for personal services performed in a foreign country during the qualifying period.

### Line 19 — Wages, salaries, bonuses, commissions

The largest category. Includes base salary, year-end bonuses, commissions on sales while in foreign country, hardship/cost-of-living allowances paid in cash. Translate from foreign currency to USD using yearly average or spot rate.

### Line 20 — Allowable share of income for personal services performed (mixed services + capital)

For SE filers where the income is partly compensation for services and partly return on capital (e.g., a business owner whose Schedule C income reflects both their services AND their invested capital). Only the services portion qualifies for FEIE. A reasonable allocation is required (Reg. §1.911-3(b)). For most consultant SE filers, services are the primary income-generating factor and 100% of net SE income is FEI.

### Line 21 — Allowable share of income for personal services rendered

Subset/refinement of Line 20. Some Form 2555 versions consolidate; check the current form.

### Line 22 — Noncash income

Fair market value of:
- Employer-provided housing (the FMV of housing is FEI; the housing exclusion offsets this on the same form)
- Employer-provided meals
- Employer-provided car or transportation
- Tuition reimbursement
- Tax equalization payments

### Line 23 — Other foreign earned income

Catchall for items not on Lines 19-22 that still qualify as FEI: book advance for services performed abroad, royalties tied to services, etc.

### Line 24 — Total foreign earned income

Sum of Lines 19-23. This is the total FEI subject to potential exclusion.

### Lines 25-26 — Compensation from US-employer-paid in US for services in foreign country

Informational. The user reports the breakdown of pay from a US employer (W-2) for services performed abroad. This is included in Line 19 / 24 if it's for foreign services.

---

## Part V — All Filers

### Line 27 — Foreign earned income (= Line 24)

Most filers: Line 27 = Line 24. If the user excludes a portion under §911 and a portion under another rule, refinements may apply, but rare.

### Lines 28a-c — Misc apportionment

Form-specific sub-allocations; usually mechanical. Refer to the current-year instructions.

---

## Part VI — Foreign Housing Exclusion (Employees)

Only for employees. SE filers use Part IX (deduction).

### Line 28 — Foreign housing expenses

Includable: rent, utilities (other than telephone), property/personal property insurance, parking (residential), repairs, residential furniture rental, residential security.

NOT includable: lavish/extravagant amounts, telephone, mortgage interest (use Schedule A), purchase price of house, capital improvements, deductible interest/taxes, depreciation, domestic labor, pay TV, leased furniture, food, alcohol.

### Line 29 — Housing reimbursements from employer

If the employer paid or reimbursed the housing, the FMV is in Line 22 (noncash). Line 29 captures the cash reimbursement portion.

### Line 30 — Housing expenses paid by filer

Out-of-pocket housing expenses paid by the filer (not employer-reimbursed).

### Line 31 — Housing expense limit

```
Limit = 30% × FEIE cap × (qualifying days / 365) [+ city-specific high-cost adjustment]
```

For 2025: 30% × $130,000 = $39,000 default. With high-cost city adjustments, can be much higher (London ~$78,400, Hong Kong ~$114,300, Tokyo ~$74,200 — illustrative; verify current Notice).

The IRS publishes the city-specific table annually. See [`housing.md`](./housing.md).

### Line 32 — Lesser of Line 28 or Line 31

The capped housing expense.

### Line 33 — Base housing amount

```
Base = 16% × FEIE cap × (qualifying days / 365)
```

For 2025: 16% × $130,000 = $20,800 (full year qualifying).

The base represents what the IRS assumes the filer would have spent on housing in the US even without the foreign assignment.

### Line 34 — Excess housing expense

Line 32 − Line 33.

### Line 35 — Employer-provided housing

The portion of Line 32 that was provided or reimbursed by the employer (i.e., employer-paid housing). Only this portion is eligible for the housing **exclusion** (vs. deduction).

### Line 36 — Housing exclusion

= Lesser of Line 34 or Line 35

This is the amount excluded from income (in addition to the Part VII earned income exclusion).

---

## Part VII — Foreign Earned Income Exclusion

### Line 37 — Maximum exclusion (annual cap, pro-rated if partial year)

```
Max exclusion = FEIE cap × (qualifying days in tax year / total days in tax year)
```

For full-year qualifying filers, Line 37 = the FEIE cap ($130,000 for 2025).

For partial-year filers (e.g., started qualifying mid-March): apportion. The 12-month qualifying period overlaps the tax year — count overlapping days.

### Lines 38-43 — Sub-mechanic

Various form-version-specific calculations. The result:

```
Excluded earned income = lesser of (FEI net of housing exclusion, max exclusion)
                       = lesser of (Line 24 − Line 36, Line 37)
```

### Line 44 — (worksheet line for tax-stacking; refer to instructions)

### Line 45 — Total exclusion

= Housing exclusion (Line 36) + Earned income exclusion (Line 42 or equivalent)

This is the negative adjustment that flows to **Schedule 1 Line 8d** (or current-year line for "Other income — adjustments"; verify line number on the current Schedule 1).

The exclusion appears as a NEGATIVE number on Schedule 1, reducing total income on Form 1040.

---

## Part VIII — Disallowed Deductions

When foreign earned income is excluded, deductions, expenses, and losses related to that excluded income are NOT deductible (IRC §911(d)(6)). This prevents double benefit.

### Lines 46-50

Sum of:
- Schedule A itemized deductions allocable to excluded income (e.g., foreign moving expenses if itemized)
- Schedule C expenses allocable to excluded SE income
- Other expenses

The amount on Lines 46-50 is the disallowed amount — it's NOT subtracted on the deductions schedule.

For most W-2 employees claiming FEIE, this is a small amount or zero. For SE filers, it's significant: Schedule C expenses tied to excluded SE earnings get disallowed.

The mechanic in tax software: if Schedule C net SE income is $130K (all excluded), and the gross was $200K with $70K of expenses, the $70K of expenses is disallowed against the excluded income. Effectively the user reports $0 on Schedule C (after FEIE) and gets no expense deduction.

---

## Part IX — Foreign Housing Deduction (Self-Employed Only)

For SE filers (Schedule C), the housing benefit is a **deduction** (above-the-line on Schedule 1) rather than an exclusion. Mechanically similar but flows differently.

### Lines 51-53

```
Housing deduction = Lesser of (excess housing expense, FEI net of FEIE)
                  = Lesser of (Line 34, Line 24 − FEIE excluded amount)
```

This is limited to the SE income remaining after the FEIE. Excess can carry forward one year (IRC §911(c)(4)).

The deduction goes on Schedule 1 (current line for "Foreign housing deduction"; verify on current schedule). It reduces AGI, similar to other above-the-line deductions.

---

## Special situations

### Filer changes country mid-year

For BFR: the filer must remain a BFR somewhere for the entire tax year. Moving from Germany to UK mid-year is fine if they're a BFR of UK by the end of the year. Moving back to the US breaks BFR.

For PPT: doesn't matter where in the foreign world, only that 330 full days are abroad in the 12-month period.

### Filer's spouse also has foreign earned income

Each spouse files their OWN Form 2555 if both qualify. Each gets their own FEIE cap. Joint return; separate Forms 2555.

### Bona fide resident under treaty

Resident aliens who are tax residents of a country with a US tax treaty CAN use the BFR test. Without a treaty, they must use PPT.

### Combat zone / waiver of time requirements

Filers in combat zones or war zones get automatic extensions and may have time-requirement waivers (IRC §911(d)(4)). Specific Service notice usually applies.

### Federal employees abroad

US federal civilian employees stationed abroad may not qualify for FEIE on their federal compensation (the "abode in US" disqualifier often applies). Check facts carefully.

### Income from the US for services performed abroad

If the filer is paid by a US employer (W-2) for services performed in the foreign country, the income is FEI (assuming all other tests pass). The W-2 reports it normally; the FEIE excludes it on Form 2555. The employer's withholding is recovered as part of the refund.

### Income from a foreign country for services performed in the US

Not FEI. Source rule: services are sourced where performed. If the user worked in the US for 30 days and earned $20,000 of that period's salary, that $20,000 is US-source and not FEI. The user must allocate.
