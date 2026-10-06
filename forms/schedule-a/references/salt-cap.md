# SALT Cap (Lines 5-7) — IRC §164(b)(6)–(7) as Amended by OBBBA 2025

The SALT cap is the most-changed Schedule A rule in the past decade. TCJA capped it at $10,000 in 2018. The One Big Beautiful Bill Act (P.L. 119-21 §70120, effective for tax years beginning after December 31, 2024) quadrupled it for 2025 and raised it 1% a year through 2029, before reverting to $10,000 in 2030. This file is the year-by-year reference for the cap, the high-income phase-down, and what counts as a SALT item.

Verified 2026-10-06 against IRC §164(b)(6)–(7) (statute text) and the 2025 Schedule A and instructions (line 5e and the State and Local Tax Deduction Worksheet). Re-check the 2026 form and instructions when released.

---

## Year-by-year cap

| Tax year | SALT cap (Single / MFJ / HoH) | MFS | Statute |
|----------|------------------------------|-----|---------|
| 2017 and earlier | Unlimited | Unlimited | Pre-TCJA |
| 2018-2024 | $10,000 | $5,000 | IRC §164(b)(6) — TCJA |
| 2025 | $40,000 | $20,000 | IRC §164(b)(7)(A)(i) |
| 2026 | $40,400 | $20,200 | IRC §164(b)(7)(A)(ii) |
| 2027 | ≈ $40,804 | ≈ $20,402 | §164(b)(7)(A)(iii): 101% of the prior year's amount |
| 2028 | ≈ $41,212 | ≈ $20,606 | same |
| 2029 | ≈ $41,624 | ≈ $20,812 | same |
| 2030+ | $10,000 | $5,000 | §164(b)(7)(A)(iv); no phase-down after 2029 |

The statute says "101 percent of the dollar amount in effect" for the preceding year and gives no rounding rule; the 2027–2029 figures above are arithmetic, not published amounts. Use the figure the IRS prints on that year's Schedule A.

---

## High-income phase-down (NEW under OBBBA, 2025–2029)

Filers with MAGI above $500,000 ($250,000 MFS) for 2025 have the SALT cap reduced. The 2025 State and Local Tax Deduction Worksheet (Schedule A instructions) works as follows:

```
If line 5d ≤ $10,000 ($5,000 MFS): line 5e = line 5d (no worksheet)
Line 1  $40,000 (the full amount, also for MFS)
Line 4  MAGI = Form 1040 line 11b + excluded Puerto Rico income + Form 2555 lines 45 and 50 + Form 4563 line 15
Line 5  $500,000 ($250,000 MFS)
Line 7  30% × max(0, line 4 − line 5)
Line 8  line 1 − line 7
Line 9  larger of line 8 or $10,000
Line 10 smaller of line 9 (half of line 9 if MFS) or line 5d → line 5e
```

The phase-down cannot reduce the cap below $10,000 ($5,000 MFS, because line 9 is halved).

**Only the threshold is indexed, not the floor.** For 2026 the threshold is $505,000 ($252,500 MFS) (IRC §164(b)(7)(B)(ii)(II)); it rises to 101% of the prior year's amount after 2026. The $10,000 floor is fixed (IRC §164(b)(7)(B)(iii)). The phase-down applies only to tax years beginning before January 1, 2030.

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

MFS (2025): MAGI $300,000 → $40,000 − 30% × $50,000 = $25,000 → half = **$12,500**. MAGI $350,000 or more → $10,000 → half = **$5,000**. (Worksheet arithmetic.)

**Implication**: For a filer between $500K and $600K MAGI, every dollar of MAGI reduction (e.g., 401(k) contribution, HSA contribution, charitable gift via QCD) restores 30¢ of SALT cap room. Useful planning lever.

### MAGI definition for SALT phaseout

MAGI for the SALT phase-down = AGI increased by any amount excluded under IRC §911 (foreign earned income and housing exclusions, Form 2555), §931 (Guam/American Samoa/CNMI, Form 4563) or §933 (Puerto Rico) (IRC §164(b)(7)(B)(iv)). Nothing else is added back. Most domestic filers have MAGI = AGI.

---

## What counts as a SALT item

### Line 5a — State and local income tax OR general sales tax

The filer must pick **one or the other**, not both. Pick the larger.

**Income tax (the typical pick for most states)**:
- W-2 box 17 (state income tax withheld)
- 1099 boxes for state withholding
- State estimated tax payments paid in the tax year
- Prior-year state balance due paid in the tax year (e.g., a 2024 balance due paid in April 2025 deducts on the 2025 return)
- Mandatory contributions to the California, New Jersey, or New York nonoccupational disability funds, the Rhode Island temporary disability fund, or the Washington State supplemental workmen's compensation fund; mandatory contributions to the Alaska, California, New Jersey, or Pennsylvania state unemployment funds; mandatory contributions to state family leave programs (e.g., NJ FLI, California Paid Family Leave) (2025 instructions, line 5a). From 2025, contributions to a governmental paid family leave program are included in income and can be deducted here (2025 Form 1040 instructions, What's New)

**General sales tax (better choice for no-income-tax states or filers with major purchases)**:
- Use the IRS Sales Tax Deduction Calculator (IRS.gov/SalesTax) or the 2025 Optional State and Local Sales Tax Tables with the worksheet in the Schedule A instructions
- OR keep actual receipts and total (receipts required for this method)
- If using the tables, add actual sales tax on specified items: motor vehicles (only at the general rate), aircraft or boats (only if taxed at the general rate), and a home or substantial addition/major renovation in the cases the instructions list (worksheet line 7)
- Local sales tax: the worksheet (lines 2–6) handles it; California and Nevada residents follow the special line 3 rule

**States with no tax on wages** (where sales tax often wins): Alaska, Florida, Nevada, New Hampshire, South Dakota, Tennessee, Texas, Washington, Wyoming.

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

Value-based portion only, imposed on a yearly basis (2025 instructions, line 5c). Examples:

- **Vehicle registration** in states like CA, MA, MN, NV, AZ, where part of the registration fee is value-based ad valorem (the deductible portion). Flat-fee states (e.g., NY) — none deductible.
- **Boat/aircraft** ad valorem registration
- **Mobile home** personal property tax if not classified as real property

NOT deductible: flat license-plate fees, title fees, smog/inspection fees, parking violations, late fees.

### Line 6 — Other taxes

The most common entry is **foreign income tax**, but most filers do better claiming the foreign tax credit on Schedule 3 Line 1 instead of deducting on Line 6. Run both numbers and take the larger benefit.

The only other item the instructions list is generation-skipping transfer (GST) tax imposed on certain income distributions. Enter one total and list the type and amount of each tax.

NOT on Line 6: federal income tax, self-employment tax, FICA on the user's wages, federal excise taxes, foreign real or personal property taxes (not deductible).

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

**Bunching property taxes**: Some jurisdictions allow prepaying next year's property tax in December of the current year. Only taxes paid in the year and assessed before the next year are deductible ("Only taxes paid in 2025 and assessed prior to 2026 can be deducted for 2025," 2025 instructions, line 5b; IRS news release IR-2017-210). Verify the jurisdiction allows prepayment AND has assessed the tax.

**State PTET (Pass-Through Entity Tax) elections**: Many states let partnerships and S corporations pay state income tax at the entity level, where it is deducted as a business expense and not subject to the individual cap (IRS Notice 2020-75). Out of scope for Schedule A; refer the user to a CPA and verify state-by-state rules.

**MFS coordination**: If one spouse itemizes, the other must itemize too (IRC §63(c)(6)(A)). MFS each get half the cap ($20,000 / $20,200). Sometimes splitting deductions across two MFS returns optimizes — usually not, because of bracket compression. Run both.

**Timing state estimated payments**: A January 15 fourth-quarter state estimate counts on the return for the year it's paid. Pay by December 31 to deduct on the current year if cap-room is available; defer to January if cap is already maxed.

---

## Common SALT mistakes

1. **Using the old $10K cap on a 2025/2026 return** — the cap is $40,000 / $40,400. Confirm the year, then confirm the cap.
2. **Including federal taxes** — federal income tax, federal payroll tax, federal SE tax never go on Schedule A.
3. **Counting both income AND sales tax on Line 5a** — pick one.
4. **Deducting special assessments as property tax** — those add to basis, not Line 5b.
5. **Forgetting prior-year state balance due** — paid in current year, deducts in current year.
6. **Forgetting state income tax refund recapture** — if last year you itemized + deducted state income tax + received a refund this year, that refund is income on Schedule 1.
7. **Missing the high-income phase-down** — at MAGI > $500K (2025) / $505K (2026), the cap shrinks. Run the worksheet; don't assume the full cap.
8. **Treating estimated state tax payments paid AFTER year-end as current year** — January 15 estimate counts on the year it's paid, not the year it's for.
9. **Indexing the $10,000 floor** — only the cap and the threshold rise after 2025; the floor stays $10,000 ($5,000 MFS).

---

## Sources

- [IRC §164](https://www.law.cornell.edu/uscode/text/26/164) — Taxes
- [IRC §164(b)(6)–(7)](https://www.law.cornell.edu/uscode/text/26/164) — SALT cap as enacted by TCJA and amended by P.L. 119-21 §70120 (applicable limitation amount, threshold, 30% phase-down, $10,000 floor, MAGI definition)
- [IRS Publication 17](https://www.irs.gov/publications/p17) — Your Federal Income Tax (chapter on itemized deductions)
- [Schedule A Instructions (2025)](https://www.irs.gov/pub/irs-pdf/i1040sca.pdf) — lines 5a–5e, State and Local Tax Deduction Worksheet
- IRS Sales Tax Deduction Calculator — IRS.gov/SalesTax
- [IR-2017-210](https://www.irs.gov/newsroom/irs-advisory-prepaid-real-property-taxes-may-be-deductible-in-2017-if-assessed-and-paid-in-2017) — prepaid property tax must be assessed in the year paid
- IRS Notice 2020-75 — entity-level state tax payments by partnerships and S corporations
- One Big Beautiful Bill Act, P.L. 119-21 (July 4, 2025), §70120 — cap increase, 1% annual increase through 2029, high-income phase-down
