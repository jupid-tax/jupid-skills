# Form 4562 Line-by-Line Reference

Complete lookup for every line on Form 4562. Use this when the agent needs to confirm what a line means or where a number flows.

## Header

| Line | Field | What goes here | Notes |
|------|-------|----------------|-------|
| (top) | Name(s) shown on return | Filer or entity name exactly as on related return | Schedule C filer: filer's personal name. Entity: entity name. |
| (top) | Identifying number | SSN (sole prop), or EIN | Match the related return |
| (top) | Business or activity to which this form relates | Name of the trade/business | If user has Schedule C + rental Schedule E, that's TWO Form 4562s, one per activity |

---

## Part I — Election To Expense Certain Property Under Section 179

| Line | Field | Rule | Source |
|------|-------|------|--------|
| 1 | Maximum amount | $2,500,000 for 2025; $2,560,000 for 2026 | IRC §179(b)(1) as amended by P.L. 119-21 §70306; 2025 Form 4562 instructions, Line 1; Rev. Proc. 2025-32 §4.24 |
| 2 | Total cost of §179 property placed in service | Sum of cost (after business-use %) of all assets eligible for §179, even those not elected | |
| 3 | Threshold cost of §179 property | $4,000,000 for 2025; $4,090,000 for 2026 | IRC §179(b)(2); 2025 Form 4562 instructions, Line 3; Rev. Proc. 2025-32 §4.24 |
| 4 | Reduction in limitation | max(0, Line 2 − Line 3) | Phase-out: dollar-for-dollar above threshold |
| 5 | Dollar limitation for tax year | max(0, Line 1 − Line 4); married filing separately: 50% of result | Married filing separately allocates the dollar limit; consult IRC §179(b)(4) |
| 6 | (a) Description / (b) Cost / (c) Elected cost | Per asset row | Cost (column b) is **business-use-adjusted**: $40K truck × 80% = $32K; not full cost |
| 7 | Listed property §179 from Line 29 | Computed in Part V | Prevents double-counting of vehicles, etc. |
| 8 | Total elected cost of §179 property | Line 6 (column c) total + Line 7 | |
| 9 | Tentative deduction | min(Line 5, Line 8) | The dollar-limited election |
| 10 | Carryover from prior year | From Line 13 of last year's Form 4562 | Track per-taxpayer, aggregate across activities |
| 11 | Business income limitation | Aggregate active business income (Schedule C profit + W-2 wages + active K-1 earned income) | IRC §179(b)(3). NOT investment income, capital gains, rental income (unless real-estate-pro). |
| 12 | §179 deduction | min(Line 9 + Line 10, Line 11) | The actually-deductible amount this year |
| 13 | Carryover to next year | (Line 9 + Line 10) − Line 12 | Carries forward indefinitely; subject to income limit each year |

**Critical**: Line 6 (b) cost must be the business-use portion. A $40,000 truck at 80% business use is $32,000 on Line 6 (b). The full $40,000 isn't recoverable as §179 because the personal portion isn't deductible.

**Critical**: Line 11 includes wages from a W-2 job (yes, even unrelated). It does NOT include passive rental income, capital gains, or interest/dividends.

---

## Part II — Special Depreciation Allowance and Other Depreciation

| Line | Field | Rule |
|------|-------|------|
| 14 | Special depreciation allowance for qualified property (other than listed) placed in service during the tax year | Bonus rate × (basis after §179). 2025: 100% for property acquired after Jan 19, 2025 (election to use 40% available for the first tax year ending after Jan 19, 2025); 40% for property acquired before Jan 20, 2025 and placed in service in 2025 (2025 Form 4562 instructions, Line 14). 2026: 100% for property acquired after Jan 19, 2025. |
| 15 | Property subject to section 168(f)(1) election | Unit-of-production or another method not based on a term of years; rare |
| 16 | Other depreciation (including ACRS) | Pre-1987 ACRS assets, income-forecast property, computer software over 36 months (§167(f)(1)); not listed property |

**Bonus eligibility**: tangible personal property with MACRS recovery period ≤20 years; off-the-shelf software; qualified improvement property (QIP — interior improvements to nonresidential buildings post-2017). NOT eligible: real property other than QIP; listed property used 50% or less in a qualified business use; property required to use ADS.

**Bonus is NOT income-limited** (unlike §179). It can create a loss.

**Opt-out**: an irrevocable election by class on a written statement attached to the timely-filed return. Once elected for a class in a year, applies to all assets in that class for that year.

---

## Part III — MACRS Depreciation

### Section A — prior-year assets and the GAA election

| Line | Field | Rule |
|------|-------|------|
| 17 | MACRS deductions for assets placed in service in tax years before current | Carries the cumulative depreciation for prior-year assets. Computed via MACRS tables in Pub 946. |
| 18 | Election to group current-year assets in a general asset account (GAA) | Rare; allows simpler bookkeeping but limits flexibility on disposition |

### Section B — current-year assets by class (GDS)

| Line | Class | Recovery | Convention default | Method default | Examples |
|------|-------|----------|--------------------|----------------|----------|
| 19a | 3-year | 3 yrs | HY (or MQ if >40% Q4) | 200DB → SL switchover | Special tools, race horses |
| 19b | 5-year | 5 yrs | HY/MQ | 200DB | Cars, trucks, computers, copiers, office machines |
| 19c | 7-year | 7 yrs | HY/MQ | 200DB | Office furniture, fixtures, most equipment |
| 19d | 10-year | 10 yrs | HY/MQ | 200DB | Vessels, certain agricultural |
| 19e | 15-year | 15 yrs | HY/MQ | 150DB | Qualified improvement property, fences, roads |
| 19f | 20-year | 20 yrs | HY/MQ | 150DB | Farm buildings |
| 19g | 25-year | 25 yrs | HY/MQ | SL | Water utility property |
| 19h | 50-year (new for 2025) | 50 yrs | MM | SL | Certain improvements necessary to construct or improve railroad grading and tunnel bores |
| 19i | 27.5-year residential rental | 27.5 yrs | MM | SL | Apartment buildings, single-family rentals |
| 19j | 39-year nonresidential | 39 yrs | MM | SL | Office buildings, retail, warehouses |

**Conventions**:
- **Half-year (HY)**: assumes asset placed in service mid-year; typical for personal property
- **Mid-quarter (MQ)**: required if >40% of total annual personal-property purchases happened in Q4; spreads first-year depreciation by quarter
- **Mid-month (MM)**: for real property; assumes asset placed in service mid-month of the actual month

**Methods**:
- **200% DB → SL**: 200% declining balance switching to straight-line when SL gives larger deduction (years 5-year and 7-year)
- **150% DB → SL**: 150% declining balance for 15-year and 20-year property
- **SL**: straight-line; required for all real property (27.5-year, 39-year)

### Section C — Alternative Depreciation System (ADS)

| Line | Class | Method | When ADS required |
|------|-------|--------|-------------------|
| 20a | Class life | SL | Listed property used ≤50% business; certain tax-exempt-use; certain foreign |
| 20b | 12-year | SL | Personal property with no class life under GDS |
| 20c | 30-year | SL | Residential rental property under ADS |
| 20d | 40-year | SL | Nonresidential real property under ADS |
| 20e | 50-year (new for 2025) | SL | Water utility property, railroad grading and tunnel bores |

Filers can also *elect* ADS; the election is irrevocable for that asset class.

---

## Part IV — Summary

| Line | Field | Rule |
|------|-------|------|
| 21 | Listed property | From Line 28 of Part V |
| 22 | Total | Sum: Line 12 + 14 + 15 + 16 + 17 + 19 (column g totals) + 20 (column g totals) + 21 |
| 23a | Basis attributable to interest capitalized under §263A(f) | Only for Part III assets placed in service this year with §263A-capitalized costs; rare for solo filers |
| 23b | Basis attributable to other §263A capitalized costs | Same scope as 23a, costs other than §263A(f) interest |

A partnership or S corporation does not include Line 12 (§179) in Line 22; the §179 deduction passes through on Schedule K (Form 1065 Line 12; Form 1120-S Line 11).

Line 22 is the number that flows to:
- Schedule C Line 13
- Schedule E Line 18
- Schedule F Line 14
- Form 1120 Line 20
- Form 1120-S Line 14
- Form 1065 Line 16a

---

## Part V — Listed Property

Listed property under IRC §280F. Computers and peripheral equipment are listed property only if placed in service before 2018. Section A is for §179 + depreciation; Section B is for vehicles specifically; Section C is for employer-provided vehicles (rare for solo).

### Section A — depreciation and §179 for listed property

| Line | Field | Rule |
|------|-------|------|
| 24a | "Do you have evidence to support the business/investment use claimed?" Yes/No | Substantiation question. No → deduction at audit risk. |
| 24b | "If 'Yes,' is the evidence written?" Yes/No | Written = contemporaneous log. Mental records insufficient. |
| 24c | "Do you own, lease, or charter an aircraft?" Own / Lease / Charter checkboxes (new for 2025) | Check all that apply; leave blank if no aircraft |
| 25 | Special depreciation allowance for qualified listed property | Bonus depreciation on listed property used more than 50% in a qualified business use; included in Line 28, which carries to Line 21 (not Line 16) |
| 26 | Property used >50% in qualified business use — depreciation, §179 | Per-asset rows: (a) description / (b) date in service / (c) bus% / (d) cost or basis / (e) basis for depreciation / (f) recovery / (g) method/convention / (h) deduction / (i) §179 |
| 27 | Property used ≤50% — ADS only | Cannot use §179, bonus, or accelerated MACRS; ADS straight-line over class life |
| 28 | Total — column h, Lines 25+26+27 | Carries to Line 21 |
| 29 | Total §179 — column i Line 26 only (not Line 27) | Carries to Line 7 |

### Section B — Information on use of vehicles (per vehicle)

| Line | Field | Rule |
|------|-------|------|
| 30 | Total business/investment miles driven during year (don't include commuting) | Substantiated business miles |
| 31 | Total commuting miles | Home-to-regular-workplace miles; never deductible |
| 32 | Total other personal (noncommuting) miles | Errands, family trips |
| 33 | Total miles | 30 + 31 + 32 |
| 34 | Was vehicle available for personal use during off-duty hours? | Y/N |
| 35 | Was vehicle used primarily by a more-than-5% owner or related person? | Y/N |
| 36 | Is another vehicle available for personal use? | Y/N |

### Section C — Questions for employers who provide vehicles to employees

Lines 37–41. Almost always inapplicable to solo filers. Applies to entities (S-corp, C-corp, partnership) that provide vehicles to employees.

---

## Part VI — Amortization

| Line | Field | Rule |
|------|-------|------|
| 42 | Amortization of costs that begin during the current tax year | Per-intangible rows: (a) description / (b) date amortization begins / (c) amortizable amount / (d) IRC code section / (e) period or % / (f) deduction |
| 43 | Amortization of costs that began before current tax year | Continuing amortization from prior years; one aggregate number |
| 44 | Total | Line 42 + Line 43 |

Common (d) IRC codes:
- **§197**: 15-year SL for goodwill, going concern, customer lists, workforce, covenants not to compete, franchises, trademarks (when acquired with a trade or business)
- **§195**: start-up costs, $5,000 first-year deduction with phase-out, excess amortized over 180 months
- **§248**: organizational costs of a corporation, $5,000 first-year + 180-month amortization
- **§709**: organizational costs of a partnership, $5,000 first-year + 180-month
- **§174 / §174A**: research and experimental expenditures. Domestic R&E paid or incurred in tax years beginning after 2024 is deductible currently under §174A, or the taxpayer elects to amortize it over 60+ months or over 10 years; foreign R&E is amortized over 15 years (2025 Form 4562 instructions, Line 42; Rev. Proc. 2025-28)
- **§167(a)**: depreciable intangibles not under §197 (some patents, copyrights, customer-based intangibles created by the user, off-the-shelf computer software not §197) — useful life or 36 months for software

Amortization Line 44 flows to:
- Schedule C Line 27b on the 2025 form (with itemization in Part V Line 48 as "Amortization — [description]"); Line 27a is now the energy efficient commercial buildings deduction
- Schedule E Line 18 (rental amortization, e.g., loan costs)
- Form 1120 Line 26, Form 1120-S Line 20, Form 1065 Line 21 ("Other deductions" on the 2025 forms)

---

## Cross-form flow

Form 4562 doesn't compute tax; it just totals depreciation and amortization. The numbers flow:

```
Form 4562 Line 22  →  Schedule C Line 13 (or Schedule E/F, or 1120/1120-S/1065 line)
Form 4562 Line 44  →  Schedule C Line 27b (itemized in Part V Line 48)
                       OR Schedule E Line 18
                       OR entity equivalent
```

The total Schedule C Line 13 = total depreciation (Line 22) only. Amortization is reported on Line 27b (2025 Schedule C) with Part V breakdown, not Line 13.

---

## Common cross-line errors

- **Line 6 cost not adjusted for business-use %**: filer puts full asset cost; fix by multiplying cost × bus%
- **§179 elected on Line 6 but never carried to Line 12**: forgot to apply income limit; check Line 11
- **Line 22 doesn't equal Schedule C Line 13**: typing mismatch; one is wrong
- **Listed property §179 on both Line 6 AND Line 29**: double-counted; Line 7 / Line 29 mechanism prevents this — use one path
- **Bonus depreciation on Line 14 for a 39-year nonresidential building (not QIP)**: ineligible asset; remove
- **Amortization on Line 22**: amortization belongs on Line 44, not Line 22; depreciation and amortization are separate lines on Form 4562 even though both flow to the income tax return
- **Line 11 includes investment income**: should only include active business income
