# SALT Cap (Lines 5-7) — IRC §164(b)(6) as Amended by OBBBA 2025

The SALT cap is the most-changed Schedule A rule in the past decade. TCJA capped it at $10,000 in 2018. OBBBA quadrupled it for 2025 and indexed it through 2029, before reverting to $10,000 in 2030. This file is the definitive year-by-year reference for the cap, the high-income phaseout, and what counts as a SALT item.

**Verify the OBBBA amendments before each filing season.** The bill was passed in mid-2025; some IRS forms and software lagged in updating. The numbers below reflect the statute as enacted.

---

## Year-by-year cap

| Tax year | SALT cap (Single / MFJ / HoH) | MFS | Statute |
|----------|------------------------------|-----|---------|
| 2017 and earlier | Unlimited | Unlimited | Pre-TCJA |
| 2018-2024 | $10,000 | $5,000 | IRC §164(b)(6) — TCJA |
| 2025 | $40,000 | $20,000 | OBBBA amendment to IRC §164(b)(6) |
| 2026 | $40,400 | $20,200 | OBBBA amendment (1% annual increase) |
| 2027 | $40,804 | $20,402 | OBBBA amendment (1% annual increase) |
| 2028 | $41,212 | $20,606 | OBBBA amendment (1% annual increase) |
| 2029 | $41,624 | $20,812 | OBBBA amendment (1% annual increase) |
| 2030+ | $10,000 | $5,000 | Reverts to TCJA cap (sunset) |

Calculation rule: `Cap_year = round(prior_year_cap × 1.01, nearest dollar)`. Verify rounding against IRS guidance once published; the rounding convention may follow Rev. Proc. inflation-adjustment rules.

---

## High-income phaseout (NEW under OBBBA, effective 2025)

Filers with MAGI above $500,000 ($250,000 MFS) have the SALT cap reduced. The phaseout works as follows:

```
Excess MAGI = max(0, MAGI − $500,000)   [MFS: $250,000 threshold]
Phaseout    = Excess MAGI × 30%
Effective cap = max($10,000, base cap − Phaseout)   [MFS: floor $5,000]
```

The phaseout cannot reduce the cap below $10,000 ($5,000 MFS) — that's the hard floor.

**Threshold and floor both increase 1% annually through 2029** (matching the cap's indexing). For 2026, threshold = $505,000 / $252,500 MFS; floor = $10,100 / $5,050 MFS (verify against IRS guidance once published).

### Worked phaseout examples (2025)

| MAGI | Excess | Phaseout | Base cap | Effective cap |
|------|--------|----------|----------|----------------|
| $400,000 | $0 | $0 | $40,000 | $40,000 |
| $500,000 | $0 | $0 | $40,000 | $40,000 |
| $525,000 | $25,000 | $7,500 | $40,000 | $32,500 |
| $550,000 | $50,000 | $15,000 | $40,000 | $25,000 |
| $600,000 | $100,000 | $30,000 | $40,000 | $10,000 (floor reached) |
| $700,000 | $200,000 | $60,000 | $40,000 | $10,000 (floor) |
| $1,000,000 | $500,000 | $150,000 | $40,000 | $10,000 (floor) |

**Implication**: For a filer between $500K and $600K MAGI, every dollar of MAGI reduction (e.g., 401(k) contribution, HSA contribution, charitable gift via QCD) restores 30¢ of SALT cap room. Useful planning lever.

### MAGI definition for SALT phaseout

MAGI for SALT phaseout = AGI + foreign earned income exclusion (IRC §911) + foreign housing exclusion + Puerto Rico/possession exclusions + adoption assistance excluded from income. Most domestic filers have MAGI = AGI.

---

## What counts as a SALT item

### Line 5a — State and local income tax OR general sales tax

The filer must pick **one or the other**, not both. Pick the larger.

**Income tax (the typical pick for most states)**:
- W-2 box 17 (state income tax withheld)
- 1099 boxes for state withholding
- State estimated tax payments paid in the tax year
- Prior-year state balance due paid in the tax year (e.g., a 2024 balance due paid in April 2025 deducts on the 2025 return)
- Mandatory state disability insurance contributions in CA, NJ, NY, PA, RI, WA (some states only — check)

**General sales tax (better choice for no-income-tax states or filers with major purchases)**:
- Use the [IRS Sales Tax Deduction Calculator](https://apps.irs.gov/app/stdc/) — enters ZIP, income, dependents, and returns the optional table amount
- OR keep actual receipts and total
- Plus actual sales tax on big purchases (vehicles, boats, aircraft, home building materials) if using the optional table — these are added on top
- Local sales tax counted only if levied at the same rate as state, or if the locality conforms to the state base

**No-income-tax states** (where sales tax often wins): Alaska, Florida, Nevada, South Dakota, Tennessee, Texas, Washington, Wyoming.

**Tax refund recapture rule**: If the user received a state income tax refund in the tax year for a prior year in which they itemized and deducted state income tax, the refund is income on Schedule 1 Line 1 (subject to the tax-benefit rule). Choosing sales tax this year breaks the chain — no refund recapture next year if next year's refund relates to a sales-tax-pick year.

### Line 5b — Real estate taxes

Only the portion that is:
- Charged uniformly against all real property in the jurisdiction at a like rate
- Based on assessed value (ad valorem)
- Used for general public welfare

NOT deductible:
- Special assessments for local improvements (sidewalks, sewers, streetlights, paving) — these add to the property's basis
- Trash/water service fees billed with property tax
- Transfer taxes / stamp taxes paid at closing — those add to basis
- HOA fees
- Property tax on real estate held for business — that goes on Schedule C Line 23 or Schedule E

If the closing statement shows the seller paid property tax for the year and was reimbursed by the buyer, only the portion attributable to the buyer's ownership period is deductible by the buyer.

### Line 5c — Personal property tax

Value-based portion only. Examples:

- **Vehicle registration** in states like CA, MA, MN, NV, AZ, where part of the registration fee is value-based ad valorem (the deductible portion). Flat-fee states (e.g., NY) — none deductible.
- **Boat/aircraft** ad valorem registration
- **Mobile home** personal property tax if not classified as real property

NOT deductible: flat license-plate fees, title fees, smog/inspection fees, parking violations, late fees.

### Line 6 — Other taxes

The most common entry is **foreign income tax**, but most filers do better claiming the foreign tax credit on Schedule 3 Line 1 instead of deducting on Line 6. Run both numbers and take the larger benefit.

Other items: certain occupational taxes if mandatory for the privilege of working in a profession (rare in modern practice).

NOT on Line 6: federal income tax, self-employment tax, FICA on the user's wages, federal excise taxes.

---

## What is NOT subject to the cap

The cap applies to Line 5e (the sum of state/local income+sales, real estate, personal property). It does **NOT** apply to:

- Foreign income tax on Line 6 — uncapped (but compare to credit)
- Real estate taxes on a rental property — those go on Schedule E and are uncapped
- Real estate taxes on a business property — those go on Schedule C / Form 8829 and are uncapped
- Self-employment tax — that's not on Schedule A at all (deductible above the line on Schedule 1 at half)

The cap is a quirk of personal-itemizer SALT only. Business filers route around it.

---

## SALT planning around the cap

**Bunching property taxes**: Some jurisdictions allow prepaying next year's property tax in December of the current year. This bunches two years of property tax into one Schedule A, useful if standard deduction would otherwise win. Verify the jurisdiction allows prepayment AND that it's been actually assessed (the IRS disallowed pre-assessment "prepayments" after the original 2017 SALT cap workaround attempts — see IRS notice IR-2017-210).

**State PTET (Pass-Through Entity Tax) elections**: 36+ states allow pass-through businesses (S-corps, partnerships) to pay state income tax at the entity level, deducting it as a federal business expense (uncapped) instead of as an SALT itemized deduction (capped). Common workaround for high-income owners — verify state-by-state rules. PTET regimes were broadly preserved by OBBBA.

**MFS coordination**: If one spouse itemizes, the other must itemize too (IRC §63(c)(6)(A)). MFS each get half the cap ($20,000 / $20,200). Sometimes splitting deductions across two MFS returns optimizes — usually not, because of bracket compression. Run both.

**Timing state estimated payments**: A January 15 fourth-quarter state estimate counts on the return for the year it's paid. Pay by December 31 to deduct on the current year if cap-room is available; defer to January if cap is already maxed.

---

## Common SALT mistakes

1. **Using the old $10K cap on a 2025/2026 return** — the cap is $40K / $40,400. Confirm the year, then confirm the cap.
2. **Including federal taxes** — federal income tax, federal payroll tax, federal SE tax never go on Schedule A.
3. **Counting both income AND sales tax on Line 5a** — pick one.
4. **Deducting special assessments as property tax** — those add to basis, not Line 5b.
5. **Forgetting prior-year state balance due** — paid in current year, deducts in current year.
6. **Forgetting state income tax refund recapture** — if last year you itemized + deducted state income tax + received a refund this year, that refund is income on Schedule 1.
7. **Missing the high-income phaseout** — at MAGI > $500K, the cap shrinks. Compute the phaseout, don't assume the full cap.
8. **Treating estimated state tax payments paid AFTER year-end as current year** — January 15 estimate counts on the year it's paid, not the year it's for.

---

## Sources

- [IRC §164](https://www.law.cornell.edu/uscode/text/26/164) — Taxes
- [IRC §164(b)(6)](https://www.law.cornell.edu/uscode/text/26/164) — SALT cap as enacted by TCJA and amended by OBBBA 2025
- [IRS Publication 17](https://www.irs.gov/publications/p17) — Your Federal Income Tax (chapter on itemized deductions)
- [Schedule A Instructions](https://www.irs.gov/pub/irs-pdf/i1040sca.pdf) — line 5 guidance
- [IRS Sales Tax Deduction Calculator](https://apps.irs.gov/app/stdc/)
- [Bipartisan Policy Center — SALT Deduction Changes in OBBBA](https://bipartisanpolicy.org/explainer/salt-deduction-changes-in-the-one-big-beautiful-bill-act/) — accessible summary of the OBBBA SALT amendments
- One Big Beautiful Bill Act of 2025 — text governing the cap increase, indexing, and high-income phaseout. Verify the public-law citation once enrolled.
