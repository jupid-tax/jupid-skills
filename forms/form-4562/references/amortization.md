# Amortization (Form 4562 Part VI)

Amortization spreads the cost of an intangible asset over its useful life or a statutory period. Reported on Part VI of Form 4562.

---

## §197 — 15-year amortization of acquired intangibles

IRC §197 covers **intangibles acquired in connection with the acquisition of a trade or business** (or a substantial portion of one). Amortized straight-line over **15 years (180 months)** regardless of the asset's actual useful life.

### §197 intangibles

- Goodwill
- Going concern value
- Workforce in place
- Information base (customer lists, technical manuals, training programs)
- Patents, copyrights, formulas, designs (when acquired with a business)
- Customer-based intangibles (relationships, customer lists)
- Supplier-based intangibles (favorable supply contracts)
- Licenses, permits
- Covenants not to compete (including non-competes from sellers in an asset purchase)
- Franchises, trademarks, trade names
- Government licenses

### What's NOT a §197 intangible

- Self-created goodwill (not acquired)
- Self-created customer lists, designs, etc. (not acquired)
- Computer software readily available for purchase (off-the-shelf software amortizes under §167 over 36 months)
- Interests in a partnership, corporation, trust (these are equity, not intangibles)
- Sports franchises (acquired as part of a sports team purchase)
- Land

### §197 mechanics

- Cost basis = purchase price allocated to the §197 intangible per Form 8594 (asset acquisition statement)
- Period = 15 years exactly (180 months); doesn't matter what the asset's "real" useful life is
- Method = straight line; no acceleration, no §179, no bonus
- Begin date = when the intangible is placed in service (usually the acquisition closing date)
- First and last year prorated by month: a $50,000 §197 intangible placed in service July 15, 2025 amortizes:
  - 2025: 6 months × ($50,000 ÷ 180) = $1,667 (July counted as full month)
  - 2026–2039: 12 months × ($50,000 ÷ 180) = $3,333 each
  - 2040: 6 months × ($50,000 ÷ 180) = $1,667

### §197 reporting on Form 4562

Part VI Line 42 (current-year amortization) for the year the intangible is first placed in service. Each subsequent year, the same intangible's amortization goes on Line 43 (continuing amortization).

| Column | Content |
|--------|---------|
| (a) | Description of intangible (e.g., "Customer list — Acme Corp acquisition") |
| (b) | Date amortization begins (acquisition closing date) |
| (c) | Amortizable amount (the cost basis) |
| (d) | IRC code section: "197" |
| (e) | Amortization period or percentage: "180 months" |
| (f) | Current-year deduction |

---

## §195 — start-up costs

IRC §195 covers expenses incurred **before the active trade or business begins** that would have been deductible if the business were already operating.

Examples:
- Market research
- Advertising for the launch
- Travel to investigate potential locations
- Salaries for training employees pre-launch
- Professional fees for setting up the business

### §195 mechanics

- **First-year deduction**: up to $5,000 of start-up costs deductible in the year the business begins, REDUCED by total start-up costs over $50,000 (phase-out $50K to $55K)
- **Excess**: amortize over 180 months starting the month the business begins
- Election: deemed elected unless the taxpayer affirmatively elects out by attaching a statement

Example: $12,000 start-up costs, business begins August 2025.

```
First-year deduction:                           $5,000
Excess to amortize:                             $7,000
Amortization months:                            180
Per-month amortization:                         $38.89
Year 2025 (5 months: Aug-Dec):                  $194
Year 2026 (12 months):                          $467
...
```

The $5,000 first-year deduction goes on Schedule C Line 27a (with itemization on Part V Line 48 as "Start-up costs — current expense"). The $194 amortization goes on Form 4562 Part VI Line 42, then carries to Schedule C Line 27a as "Amortization of start-up costs §195".

---

## §248 / §709 — organizational costs

- **§248**: corporation organizational costs (incorporation fees, legal fees for charter, organizational meeting costs)
- **§709**: partnership organizational costs

Same structure as §195: $5,000 first-year deduction with phase-out at $50K, excess amortized over 180 months.

These rules apply to entity-level returns (1120, 1120-S, 1065). Sole proprietors and SMLLCs don't have §248/§709 items because they have no separate organizational costs. (LLC formation fees go on Schedule C Line 27a as legal fees, not amortized.)

---

## §174 — research and experimental expenditures

Post-TCJA changes (effective 2022), research expenditures must be capitalized and amortized:

- Domestic R&E: 5-year SL amortization
- Foreign R&E: 15-year SL amortization

This was a TCJA change from immediate deduction. Multiple legislative attempts to revert to immediate expensing have been made; **verify current rules** — OBBBA 2025 may have addressed this; check the latest IRS guidance.

§174 amortization is reported on Form 4562 Part VI similarly to §197 — IRC code "174" in column (d), amortization period in column (e).

---

## §167 — depreciable intangibles outside §197

For intangibles NOT acquired with a trade or business (so not §197), amortization is under IRC §167:

- **Off-the-shelf computer software** purchased separately: 36 months SL (IRC §167(f)(1))
- **Custom software** developed by the user: capitalize as §174 R&E if cost meets the test
- **Patents and copyrights** with a determinable useful life, NOT acquired with a business: useful life or 15-year fallback under §167

Off-the-shelf software example: $3,600 Adobe Premier purchase placed in service June 2025.

```
36 months SL:                                    $100/month
Year 2025 (7 months: Jun-Dec):                   $700
Year 2026 (12 months):                           $1,200
Year 2027 (12 months):                           $1,200
Year 2028 (5 months: Jan-May):                   $500
Total:                                           $3,600
```

Note: most off-the-shelf software is also eligible for §179 expensing (so a taxpayer can fully deduct in year 1 instead of 36-month amortization). Software that's not §179-eligible (or where §179 has hit limits) goes through §167 amortization.

---

## Lease acquisition costs

Costs paid to acquire a business lease (broker fees, legal fees, key money) are amortized over the lease term, including renewal options if there's a high probability of renewal.

Reported on Form 4562 Part VI; IRC code section is "Lease".

---

## Loan acquisition costs

Costs to obtain a business loan (origination fees, points) are amortized over the loan term using the straight-line method (or constant-yield for points on home-equity loans where applicable).

For rental property loans, this goes on Schedule E Line 18 via Form 4562 Part VI.

---

## Form 4562 Part VI mechanics

Line 42: per-row entry for each intangible whose amortization began **during the current year**.

Line 43: aggregate amortization for all intangibles whose amortization began **before** the current year. Single number; supporting detail kept in user records but not on the form itself.

Line 44 = Line 42 + Line 43.

Line 44 flows to:
- Schedule C Line 27a, listed in Part V Line 48 (sole prop / SMLLC)
- Schedule E Line 18 for rental real estate
- Schedule F Line 32 for farm
- Form 1120 Line 26
- Form 1120-S Line 19
- Form 1065 Line 20

Note: Form 4562 has a separate flow for amortization vs. depreciation. Line 22 (total depreciation) and Line 44 (total amortization) end up on different lines of the income tax return.

---

## Common mistakes with amortization

1. **Combining §197 intangibles into one row when they have different acquisition dates** — separate rows; different begin dates yield different prorations
2. **Using the asset's "useful life" instead of 15 years for §197** — §197 is statutory 15 years, not actual life
3. **Missing the prior-year continuation on Line 43** — every year for 15 years, the intangible's amortization continues; forgetting it loses the deduction
4. **Putting amortization on Line 22** — Line 22 is depreciation only; amortization is Line 44
5. **Treating a self-created customer list as §197** — must be acquired
6. **Treating §195 start-up costs as fully deductible in year 1** — only $5,000 + amortization of excess
7. **Amortizing organizational costs of an LLC taxed as disregarded entity** — those go on Schedule C as legal fees (Line 17), not amortized

---

## Citations

- IRC §197: 15-year amortization of intangibles
- IRC §195: start-up costs
- IRC §248: corporate organizational costs
- IRC §709: partnership organizational costs
- IRC §174: research and experimental expenditures
- IRC §167(f): software and other intangibles
- Reg. §1.197-2: §197 intangibles
- Reg. §1.195-1: start-up cost election
- Reg. §1.174-2: R&E expenditures
- Form 8594: Asset Acquisition Statement (allocation of purchase price among acquired assets, including §197 intangibles)
- Form 4562 Instructions Part VI
