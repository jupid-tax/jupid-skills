# Mortgage Interest (Lines 8-10) — IRC §163(h) and Pub 936

Mortgage interest is the largest itemized deduction for most homeowners. The post-TCJA rules narrowed what counts:

- **Acquisition debt cap**: $750,000 (post-Dec 15, 2017) or $1,000,000 (grandfathered) — made permanent by OBBBA
- **HELOC / home equity loan**: deductible only if proceeds used to buy/build/improve the home that secures the loan — made permanent by OBBBA
- **Mortgage insurance premiums (Line 8d)**: eliminated 2022-2025, **reinstated for tax year 2026+** by OBBBA, with phaseout at $100K MAGI
- **Investment interest (Line 9)**: still subject to net-investment-income limitation via Form 4952

This file is the operational reference for Lines 8-10, including the $750K cap math, HELOC use-tracing, refinance rules, points, and the 2026+ PMI deduction.

---

## Form 1098 — the source of truth for Line 8a

Each lender sends a Form 1098 (Mortgage Interest Statement) by January 31. Boxes:

- **Box 1**: Mortgage interest received from payer in the calendar year
- **Box 2**: Outstanding mortgage principal as of January 1 (or origination date if newer)
- **Box 3**: Mortgage origination date
- **Box 4**: Refund of overpaid interest (from the lender) — adjusts Line 8a downward
- **Box 5**: Mortgage insurance premiums (only relevant 2026+; blank for 2025)
- **Box 6**: Points paid on purchase of principal residence
- **Box 7**: Property address (matches Form 1040 address — flag if not)
- **Box 8**: Number of properties securing the mortgage
- **Box 11**: Acquisition date (added to support cap-grandfathering since TCJA)

**Line 8a = Box 1 + Box 6** for the typical case. Box 4 (refund) reduces Line 8a or, if it puts Line 8a < 0, the excess is income on Schedule 1.

---

## Acquisition debt cap

**Acquisition indebtedness** is debt used to **buy, build, or substantially improve** your main home or one second home, secured by that home.

| Loan origination date | Acquisition debt cap (single / MFJ / HoH) | MFS |
|----------------------|--------------------------------------------|-----|
| On or before October 13, 1987 | Unlimited (pre-TRA grandfathered) | Unlimited |
| October 14, 1987 – December 15, 2017 | $1,000,000 | $500,000 |
| After December 15, 2017 | $750,000 | $375,000 |

OBBBA made the $750K cap **permanent**. Pre-OBBBA, the $750K cap was scheduled to revert to $1M after 2025. That sunset was eliminated.

### When the loan exceeds the cap

Only the portion of interest attributable to debt within the cap is deductible. Pub 936 walks through the **average balance method**:

```
Average balance = (sum of monthly principal balances) / number of months
Deductible % = min(1, cap / average balance)
Deductible interest = Box 1 interest × deductible %
```

Worked example: A 2020-originated loan with average 2025 balance of $900,000 and Box 1 interest of $42,000:

```
Cap            = $750,000
Avg balance    = $900,000
Deductible %   = $750,000 / $900,000 = 83.33%
Deductible int = $42,000 × 83.33% = $35,000
```

$35,000 goes on Line 8a; $7,000 is non-deductible.

### Multiple loans

If a filer has loans on a primary home and a second home, the $750K cap applies to the **combined** acquisition debt. Decide which loan to allocate the cap to (no statutory ordering rule — use whichever benefits the taxpayer).

### Grandfathered $1M loans plus new $750K loans

If the user has a pre-12/15/2017 loan with $1M balance grandfathered, **and** takes out a new acquisition loan after that date, the new loan's cap is reduced. Specifically: the $750K post-2017 limit is reduced by the principal of the pre-2017 loan up to $750K. Pub 936 has the worksheet.

---

## HELOC / Home Equity Loan rules

Interest on a home equity line of credit (HELOC) or home equity loan is deductible **only if** the loan proceeds were used to **buy, build, or substantially improve** the home that secures the loan.

This restriction has been in place since TCJA (2018) and was made permanent by OBBBA.

### Deductible use cases

- HELOC used to renovate the kitchen of the home securing the loan ✓
- HELOC used to add a room to the home securing the loan ✓
- HELOC used to install solar panels on the home securing the loan ✓
- HELOC used to refinance an existing acquisition mortgage on the home ✓
- HELOC used to buy a different vacation home — **only if** the HELOC is also secured by that vacation home (rare; usually the HELOC is secured by the primary)

### NOT deductible use cases

- HELOC used to pay off credit card debt ✗
- HELOC used to fund a vacation ✗
- HELOC used to buy a car ✗
- HELOC used to invest in stocks (this might be investment interest on Line 9 instead — see below)
- HELOC used to start a business (this might be business interest on Schedule C — see below)
- HELOC used to buy a vacation home that doesn't secure the HELOC ✗

### Mixed use

If the HELOC was partially used for home improvement and partially for non-deductible purposes, allocate interest pro rata based on the proceeds use. Maintain a tracing log.

### Substantiation

Required records:
- HELOC closing statement
- Records showing how proceeds were used (contractor invoices, receipts for materials, escrow statements for any home purchase)
- Bank statements showing the deposits and corresponding payments to qualifying purposes

---

## Refinance rules

When the user refinances:

- The new loan retains its **acquisition-debt status** up to the principal balance of the old loan at the time of refinancing
- Any **cash-out** portion is treated like a HELOC: deductible only if used for qualifying buy/build/improve purposes

### Worked example

User refinances at $500,000 when the old loan balance was $400,000. $100,000 cash-out used to:
- $60,000 for kitchen remodel (qualifying improvement)
- $40,000 for paying off credit card debt (not qualifying)

Acquisition portion of new loan = $400,000 (refinanced) + $60,000 (improvement) = $460,000.
Non-acquisition = $40,000.

Deductible interest = total interest × ($460,000 / $500,000) = 92%.

### Refinancing across the $750K boundary

If the user had a pre-12/15/2017 loan at $900K (grandfathered to $1M cap) and refinances after 12/15/2017, the new loan is grandfathered up to the **balance** at refinance, but the cap drops to $750K for any new acquisition. Specifically:

- The refinanced loan retains the $1M cap up to the old balance ($900K in this example)
- Any additional new acquisition debt has the $750K cap, reduced by the grandfathered balance

This is rare and requires Pub 936's worksheets.

### Lengthening or shortening the term

Refinancing into a longer or shorter term doesn't break the grandfather provision, as long as the loan is secured by the same residence and the principal balance doesn't exceed the prior balance immediately before refinance.

---

## Points

**Points paid on the original purchase of a main home**: deductible **in full in the year paid** if Pub 936 conditions are met:
- Loan is used to buy or build the main home
- Paying points is an established business practice in the area
- Points charged are reasonable for the area
- Points are computed as a percentage of the loan principal
- Points are clearly shown on the closing statement (HUD-1 / Closing Disclosure)
- Funds the user provided at closing (down payment + closing costs) are at least as much as the points

**Points paid on a refinance**: amortize over the **life of the new loan**, *unless* the refinance proceeds were used for substantial home improvements (then the portion of points attributable to those improvements is deductible in the year paid).

**Points paid on a second home**: amortize over the life of the loan, even if otherwise meeting purchase-of-main-home conditions.

**Points reported in Form 1098 box 6** typically already reflect the appropriate treatment per the lender. Verify against closing statement.

**If the user paid off the loan early** (refinance, sale, payoff): any remaining unamortized points are deductible in the year of payoff.

---

## Line 8d — Mortgage Insurance Premiums (Tax Year 2026+ Only)

The mortgage insurance premium deduction was eliminated for tax years 2022-2025. **OBBBA reinstated it permanently effective tax year 2026.**

For tax year 2025 returns: **leave Line 8d blank**. The deduction is unavailable.

For tax year 2026 returns and later: include qualified mortgage insurance premiums on Line 8d.

### What qualifies

- Private mortgage insurance (PMI) on conventional loans
- FHA mortgage insurance
- VA funding fees
- Rural Housing Service (RHS) guarantee fees

The premium must relate to **acquisition debt** on a qualified residence (main home or one second home) — same residence-and-purpose rules as Line 8a.

### Phaseout (2026+)

Premium deduction phases out as MAGI rises:
- **Below $100,000 MAGI ($50,000 MFS)**: full premium deductible
- **$100,000 to $109,000 MAGI ($50,000-$54,500 MFS)**: phased out 10% per $1,000 over threshold
- **$109,000+ MAGI ($54,500+ MFS)**: fully phased out, no deduction

Verify phaseout indexing in IRS Rev. Proc. for tax year 2026 once published; OBBBA's reinstatement may include indexing.

### Mortgage insurance prepaid

If the user prepaid PMI at closing (a lump-sum upfront premium), allocate the premium over **84 months or the loan term, whichever is shorter**, and deduct the current year's portion only.

### Source

[Form 1098 Box 5](https://www.irs.gov/pub/irs-pdf/f1098.pdf) — the lender reports premiums received. For 2026 returns, this box will populate; for 2025 it remains blank.

---

## Line 9 — Investment Interest

Interest on debt used to **purchase or carry property held for investment** (taxable bonds, taxable stocks, taxable real estate not held as a passive activity).

Limited to **net investment income** (taxable interest, taxable dividends, short-term capital gains; long-term capital gains and qualified dividends only count if elected at the lower-tax rate).

**Form 4952** is required to compute the limit. Excess investment interest carries forward indefinitely.

NOT investment interest:
- Margin interest used to buy tax-exempt municipal bonds (never deductible)
- Interest on debt for passive activity assets (subject to passive loss rules instead)
- Interest on debt for personal-use property (not deductible at all)

---

## Two homes — main home and second home

The taxpayer can include mortgage interest on **two qualified residences**: main home + one designated second home.

A "second home" can be:
- A vacation home not rented out at all
- A vacation home rented part-year but the user occupies it personally for **more than 14 days OR 10% of rental days, whichever is greater** (otherwise it's a rental, and interest goes on Schedule E)
- A boat or RV with sleeping, cooking, and toilet facilities

Designation of "the" second home is annual — if the user has 3 homes, pick one to designate as second each year. Mortgage interest on the third home is non-deductible personal interest.

---

## Common mortgage interest mistakes

1. **Deducting interest on a HELOC used for non-home purposes** — deductible only for buy/build/improve.
2. **Deducting interest beyond the $750K acquisition cap** — apply the average-balance method.
3. **Including PMI on a 2025 return** — Line 8d is for 2026+ only. Leave blank for 2025.
4. **Forgetting to amortize points on a refinance** — purchase-points are full-year deductible only on a *purchase* of main home; refinance points amortize.
5. **Deducting both Line 8a and the same interest on Schedule C** — pick one. If a portion of the home is used for business and the user takes home office on Schedule C, allocate property tax and mortgage interest between Line 8a (personal portion) and Form 8829 (business portion).
6. **Treating a third home's interest as deductible** — only main + designated second.
7. **Counting mortgage principal payments as interest** — only Box 1 of Form 1098 is interest.
8. **Forgetting the seller-financed mortgage payee disclosure** — Line 8b requires the seller's name, address, and SSN/EIN.
9. **Including escrow property tax payments on Line 8a** — those go on Line 5b. Form 1098 sometimes shows escrow real estate taxes; allocate to the right line.
10. **Refinance with cash-out used for non-improvement purposes deducted in full** — allocate pro rata.

---

## Sources

- [IRC §163](https://www.law.cornell.edu/uscode/text/26/163) — Interest
- [IRC §163(h)](https://www.law.cornell.edu/uscode/text/26/163) — Disallowance of personal interest, with qualified residence interest exception
- [IRC §163(h)(4)(E)](https://www.law.cornell.edu/uscode/text/26/163) — Mortgage insurance premiums (reinstated 2026+ by OBBBA)
- [IRS Publication 936](https://www.irs.gov/publications/p936) — Home Mortgage Interest Deduction (definitive guide)
- [IRS Publication 530](https://www.irs.gov/publications/p530) — Tax Information for Homeowners
- [Form 1098](https://www.irs.gov/pub/irs-pdf/f1098.pdf) — Mortgage Interest Statement
- [Form 4952](https://www.irs.gov/pub/irs-pdf/f4952.pdf) — Investment Interest Expense Deduction
- [Schedule A Instructions](https://www.irs.gov/pub/irs-pdf/i1040sca.pdf) — lines 8-10 guidance
- One Big Beautiful Bill Act of 2025 — making $750K acquisition cap permanent and reinstating PMI deduction effective 2026+. Verify the public-law citation once enrolled.
