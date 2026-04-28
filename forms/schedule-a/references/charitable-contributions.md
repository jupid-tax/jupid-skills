# Charitable Contributions (Lines 11-14) — IRC §170 and Pub 526

Charitable contributions to qualified 501(c)(3) organizations are deductible on Schedule A subject to:

1. **Substantiation rules** (acknowledgment letters for ≥ $250; Form 8283 for non-cash > $500; appraisal for non-cash > $5,000)
2. **AGI ceilings** (60% for cash to public charity, 30% for non-cash to public charity, 30%/20% for gifts to private foundations)
3. **5-year carryforward** for contributions exceeding the AGI ceilings
4. **NEW for tax year 2026+: 0.5% AGI floor** under IRC §170(p) added by OBBBA

This file is the operational reference for Lines 11-14, including the new floor mechanics, substantiation rules, valuation methods for non-cash gifts, QCDs, and donor-advised funds.

---

## The 0.5% AGI floor — NEW for tax year 2026+

OBBBA introduced a 0.5% AGI floor on itemized charitable contributions, effective tax year 2026 onward. **This floor does NOT apply to tax year 2025 returns.**

Mechanics:

```
Floor          = AGI × 0.005
Raw total      = Line 11 + Line 12 + Line 13
Line 14 effective = max(0, Raw total − Floor)
```

Examples:

| AGI | Floor | Raw charity | Line 14 deductible |
|-----|-------|-------------|---------------------|
| $50,000 | $250 | $1,000 | $750 |
| $100,000 | $500 | $3,000 | $2,500 |
| $200,000 | $1,000 | $5,000 | $4,000 |
| $500,000 | $2,500 | $20,000 | $17,500 |
| $1,000,000 | $5,000 | $40,000 | $35,000 |
| $200,000 | $1,000 | $800 | $0 (floor wipes everything) |

**Implication**: For low-charity-volume itemizers, the floor can wipe out the deduction entirely. End-of-2025 charitable giving was widely encouraged as a planning move because tax year 2025 retains full deductibility (no floor applies).

The floor does NOT affect the 60%/30%/20% AGI ceilings — those apply at the gross-contribution level, then the floor reduces the post-ceiling deductible amount.

---

## Line 11 — Cash contributions

Includes payments by:
- Cash (rare; usually not best practice — bank record required)
- Check
- Credit card / debit card
- Electronic transfer (PayPal, Venmo, Stripe routed to charity, ACH)
- Payroll deduction to a charity (W-2 box 14 may show; otherwise via paystubs)
- Out-of-pocket expenses for volunteer work (mileage, supplies for the charity, uniforms required for the volunteer activity)

Note: time and services are **never deductible** — only the user's out-of-pocket expenses.

### AGI ceiling for cash to public charity: 60%

For cash contributions to **public charities** (the bulk of charitable giving), the deduction is capped at 60% of AGI. Excess carries forward 5 years.

Cash to **private foundations**: 30% AGI ceiling.

### Volunteer mileage

Volunteer mileage is at **14¢ per mile** (statutory rate, set by IRC §170(i); not indexed for inflation; unchanged for decades). Don't confuse with:
- Business mileage (70¢ for 2025)
- Medical mileage (21¢ for 2025)

Plus parking and tolls while volunteering for charity.

---

## Line 12 — Non-cash contributions

Includes:
- Used clothing and household goods
- Appreciated stock or mutual fund shares
- Real estate
- Vehicles (cars, boats, planes)
- Inventory or business assets (special rules)
- Cryptocurrency

### Valuation: Fair Market Value (FMV)

For most non-cash gifts, deduct the **FMV** at the time of donation.

**Used clothing and household goods**: must be in **good used condition or better** (IRC §170(f)(16) added by Pension Protection Act 2006). FMV is typically what a thrift store would sell the item for. Use:
- Salvation Army or Goodwill valuation guides
- ItsDeductible (TurboTax tool) or similar
- Photos of donated items if more than $250 in value

**Appreciated long-term capital gain property** (stock, mutual funds held > 1 year): deduct FMV at date of gift, *no recognition of capital gain*. This is the most tax-efficient charity move for high-bracket donors.

**Short-term capital gain property** (held ≤ 1 year): deduct **basis**, not FMV.

**Ordinary-income property** (inventory of a business; self-created art): deduct **basis**.

**Vehicles**: deduction generally limited to gross sale proceeds the charity receives. Form 1098-C from the charity within 30 days of donation/sale states the deductible amount. Exception: if the charity uses the vehicle in its operations or gives it to a needy person, the FMV (capped at $5,000 unless higher with appraisal) deducts.

### AGI ceilings for non-cash

| Type | To public charity | To private foundation |
|------|-------------------|------------------------|
| Cash | 60% | 30% |
| Non-cash, capital gain LT | 30% | 20% |
| Non-cash, ordinary income | 50% | 30% |
| All non-cash combined | 50% (with 30% cap on LT capital gain non-cash) | 30% |

These ceilings are applied **in a specific stacking order** per IRC §170(b). Most filers don't approach the limits; tax software handles the ordering. For high-net-worth donors, model the limits explicitly using the IRC §170(b) waterfall.

### Election to take basis instead of FMV

For appreciated long-term capital gain property, the user can **elect to take basis instead of FMV** to get the higher 50% (vs 30%) AGI ceiling. Useful only if the user is bumping against the 30% ceiling and the basis is close to FMV.

### Cryptocurrency

Cryptocurrency held > 1 year and donated to a public charity: deduct FMV (no capital gain recognized). Held ≤ 1 year: deduct basis.

For cryptocurrency donations > $5,000: **qualified appraisal required**. Crypto is NOT publicly-traded-securities for the appraisal exception (IRS clarified in CCA 202302012 / Memorandum 2023). Many large donations have been disallowed for failing this rule. Get the appraisal.

### Form 8283

Required if total non-cash contributions exceed $500.
- **Section A**: items > $500 but ≤ $5,000
- **Section B**: items > $5,000 (with qualified appraisal attached for non-publicly-traded)

The signed Form 8283 must accompany the return (paper or e-file attachment).

### Qualified appraisal — for any single non-cash item > $5,000

A qualified appraisal must:
- Be made no earlier than 60 days before the donation date and no later than the return's due date including extensions
- Be performed by a qualified appraiser (specific IRS criteria — designations, education, experience)
- State the FMV, methodology, and any reduction for restrictions

Exception: **publicly traded securities** (stocks, mutual funds with daily quotes) do NOT require an appraisal. Use the average of high and low on the donation date for FMV.

---

## Line 13 — Carryover from prior year

Excess contributions over the AGI ceiling carry forward for **up to 5 tax years**. Track per year and per ceiling category (60%, 30%, 20%, etc.) — a worksheet is in Pub 526.

Carryover is used in the year carried forward only after current-year contributions to the same category are deducted (FIFO within a category, current-year before carryover).

---

## Substantiation rules

The IRS regularly audits charitable deductions, especially when they're a high percentage of AGI. Substantiation is required to win an audit.

### Single gift under $250

Bank record (canceled check, credit card statement) OR receipt from the charity stating the gift amount and date.

### Single gift $250 or more

**Contemporaneous written acknowledgment (CWA)** from the charity. The CWA must:
- State the amount of the gift (or describe the non-cash gift)
- State whether goods/services were provided in return, and if so describe and value them
- Be received before the earlier of (a) the date the return is filed, or (b) the return's due date including extensions

The IRS strictly enforces "contemporaneous" — getting the letter after filing the return doesn't count. Disallowance is common.

### Cash gifts

Always need at least a bank record. Cash put into a Salvation Army kettle without a receipt is non-deductible (no documentation possible).

### Payroll deduction

Pay stub showing the deduction OR W-2 box 14 OR pledge card OR a written statement from the charity acknowledging the year's total. Treat each payroll deduction as a separate gift for the $250 CWA threshold.

### Non-cash > $500

Form 8283 (Section A or B as applicable). Records of how FMV was determined.

### Non-cash > $5,000 (single item)

Qualified appraisal + Form 8283 Section B + signed appraiser declaration.

### Donated vehicles

Form 1098-C from the charity within 30 days, attached to the return.

### Out-of-pocket volunteer expenses

Letter from the charity acknowledging the volunteer service plus receipts for expenses.

---

## QCDs — NOT on Schedule A

A **Qualified Charitable Distribution** is a direct transfer from a traditional IRA (or inherited IRA) to a qualified public charity. The QCD is excluded from gross income on Form 1040 Line 4b — it does **NOT** flow to Schedule A.

### Why QCDs matter

- The amount is excluded from AGI, lowering AGI for purposes of:
  - Medical 7.5% floor on Schedule A
  - SALT 0.5% floor on Schedule A (2026+)
  - Charity 0.5% floor on Schedule A (2026+)
  - SALT high-income phaseout above $500K MAGI
  - Net Investment Income Tax (NIIT) thresholds
  - Medicare IRMAA premium tiers
- Counts toward the IRA owner's Required Minimum Distribution (RMD)
- Doesn't require itemizing to benefit (works equally well for standard-deduction filers)

### QCD requirements

- IRA owner must be **age 70½ or older** at the time of the QCD
- Distribution must go **directly** from the IRA custodian to a qualified public charity (no intermediate stop in the donor's account)
- Maximum **$108,000 per person for 2025** (indexed annually; verify 2026 figure)
- Cannot go to a donor-advised fund, supporting organization, or private foundation
- Cannot be in exchange for benefits (e.g., raffle tickets, dinner) — strictly no quid pro quo

For high-bracket retirees, QCDs are typically more tax-efficient than itemized charity donations because they reduce AGI rather than just the deduction.

---

## Donor-Advised Funds (DAFs)

Contributions to a DAF (Fidelity Charitable, Schwab Charitable, community foundations, etc.) deduct in the year contributed to the DAF, not the year the DAF distributes to a charity.

DAFs allow:
- Bunching multiple years of charitable giving into one tax year (useful for itemize/standard deduction strategy)
- Donating appreciated securities for FMV deduction without selling
- Time-shifting grantmaking decisions independently from the deduction year

DAF rules:
- Public charity status, so 60% AGI ceiling for cash, 30% for non-cash long-term capital gain
- Excess over ceiling carries forward 5 years
- DAF cannot fulfill a personal pledge, sponsor a non-charity benefit, or pay for goods/services to the donor

---

## Common charity mistakes

1. **Missing CWA for ≥ $250 gift** — contemporaneous written acknowledgment is required, not optional. If filed without it, the IRS can disallow even if the gift is real.
2. **Listing time/services** — never deductible. Only out-of-pocket expenses.
3. **Skipping Form 8283 for non-cash > $500** — commonly missed, and easily caught by software/IRS matching.
4. **Skipping appraisal for non-cash > $5,000** — single biggest cause of disallowance for large gifts. No appraisal = no deduction (except publicly traded securities).
5. **Crypto > $5,000 without appraisal** — see Memorandum 2023; crypto isn't a publicly-traded security for this purpose.
6. **Deducting "donations" to political campaigns** — never deductible.
7. **Deducting GoFundMe to an individual** — gifts to individuals are not charitable contributions. GoFundMe campaigns to certified 501(c)(3)s are deductible if the platform routes through the charity.
8. **Vehicle deduction at "Blue Book" instead of charity's gross proceeds** — IRC §170(f)(12) post-2004 generally limits deduction to the proceeds the charity receives.
9. **Forgetting to carry over excess** — track 5-year carryover by ceiling category.
10. **Tax year 2026+ deducting a small gift before the 0.5% floor wipes it out** — the floor is real; small gifts may not produce any deduction.
11. **QCD listed on Schedule A** — wrong place. QCDs go on Form 1040 Line 4b as exclusions, not on Schedule A.
12. **Donating short-term appreciated stock** — deducts at basis, not FMV. Hold > 1 year before donating to get FMV.

---

## Sources

- [IRC §170](https://www.law.cornell.edu/uscode/text/26/170) — Charitable, etc., contributions and gifts
- [IRC §170(p)](https://www.law.cornell.edu/uscode/text/26/170) — 0.5% AGI floor (added by OBBBA 2025)
- [IRS Publication 526](https://www.irs.gov/publications/p526) — Charitable Contributions (definitive guide)
- [IRS Publication 561](https://www.irs.gov/publications/p561) — Determining the Value of Donated Property
- [Form 8283](https://www.irs.gov/pub/irs-pdf/f8283.pdf) — Noncash Charitable Contributions
- [Form 1098-C](https://www.irs.gov/pub/irs-pdf/f1098c.pdf) — Contributions of Motor Vehicles, Boats, and Airplanes
- [Schedule A Instructions](https://www.irs.gov/pub/irs-pdf/i1040sca.pdf) — lines 11-14 guidance
- IRS Memorandum CCA 202302012 (cryptocurrency appraisal requirement)
- One Big Beautiful Bill Act of 2025 — IRC §170(p) 0.5% AGI floor (effective 2026+). Verify the public-law citation once enrolled.
