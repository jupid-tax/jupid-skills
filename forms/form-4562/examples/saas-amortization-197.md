# Example: SaaS Startup Amortizes $50,000 of §197 Intangibles

A complete walkthrough of Form 4562 Part VI for a small software company that acquired customer-list and goodwill intangibles when buying a competitor's book of business.

## The filer

- **Entity**: BrightStack Analytics, Inc. (S-corporation, files Form 1120-S)
- **Tax year**: 2025 (filing in 2026)
- **EIN**: 87-XXXXXXX
- **Activity**: SaaS B2B analytics platform

## The acquisition

In June 2025, BrightStack bought a competitor's customer relationships and brand assets in an asset-purchase transaction. Total purchase price: **$200,000**. Allocated per Form 8594:

| Acquired asset | Class | Allocation | Tax treatment |
|----------------|-------|------------|---------------|
| Cash | I | $0 | n/a |
| Marketable securities | II | $0 | n/a |
| Accounts receivable | III | $5,000 | Recognized when collected |
| Inventory | IV | $0 | n/a |
| Tangible personal property (laptop, monitor) | V | $3,000 | 5-year MACRS or §179 |
| §197 intangibles (Class VI) | VI | $50,000 | 15-year SL §197 amortization |
| Goodwill / going concern (Class VII) | VII | $142,000 | 15-year SL §197 amortization |

The Class VI intangibles ($50,000) include:
- Customer list and customer relationships: $30,000
- Trade name "DataPulse": $10,000
- Workforce in place (1 contractor moved over): $5,000
- Covenant not to compete (seller can't start another competing service for 2 years): $5,000

Class VII goodwill: $142,000.

Both Class VI and Class VII are **§197 intangibles** — same 15-year SL treatment. They're presented separately on Form 8594 only for IRS reporting; for Form 4562, they all amortize the same way.

For this example, we'll focus on the $50,000 Class VI bundle. The $142,000 Class VII goodwill amortizes the same way (separate row on Form 4562 Part VI).

## Acquisition closing date

- Asset purchase agreement signed: June 1, 2025
- Closing: June 15, 2025
- **§197 amortization begins**: June 15, 2025 (placed-in-service date of the intangibles)

For amortization, the IRS uses the **first month rule**: amortization begins in the month the intangible is placed in service. So June counts as the first amortization month.

## §197 amortization computation

```
Amortizable amount:                              $50,000
Period:                                          180 months (15 years × 12)
Monthly amortization:                            $50,000 / 180 = $277.78

Year 2025 (June - December = 7 months):          7 × $277.78 = $1,944
Year 2026 (Jan - Dec = 12 months):               12 × $277.78 = $3,333
Year 2027 (Jan - Dec = 12 months):               12 × $277.78 = $3,333
... (years 3-14, full $3,333 each)
Year 2040 (Jan - May = 5 months):                5 × $277.78 = $1,389
Total over 15 years:                             $50,000
```

For the goodwill ($142,000), same mechanics:
```
Monthly:                                         $142,000 / 180 = $788.89
Year 2025 (7 months):                            $5,522
Years 2026-2039 (full):                          $9,467 each
Year 2040 (5 months):                            $3,944
Total:                                           $142,000
```

## Form 4562 Part VI — Year 2025

```
Header:
Name: BrightStack Analytics, Inc.
Identifying number: 87-XXXXXXX
Business activity: B2B SaaS analytics

Part VI — Amortization

42. Amortization of costs that begin during 2025:
| (a) Description                              | (b) Date begins | (c) Amortizable amount | (d) IRC § | (e) Period | (f) 2025 deduction |
|----------------------------------------------|-----------------|------------------------|-----------|-----------|--------------------|
| Customer list & §197 intangibles — Acme acquisition | 06/15/2025 | $50,000             | 197       | 180 mo    | $1,944             |
| Goodwill — Acme acquisition                  | 06/15/2025      | $142,000              | 197       | 180 mo    | $5,522             |

43. Amortization of costs that began before 2025:                          $0  (first year of amortization for these)

44. Total (Line 42 + Line 43):                                             $7,466
```

Line 44 = $7,466 → flows to **Form 1120-S Line 19** (or for a sole prop, Schedule C Line 27a; for a partnership, Form 1065 Line 20).

## Other Form 4562 entries for the acquisition

The $3,000 of tangible personal property (laptop, monitor) handled separately. If BrightStack elects §179 (and has the income to absorb it):

### Part I (§179)

```
1.  Maximum amount:                    $1,250,000
2.  Total cost of §179 property:       $3,000
3.  Threshold:                         $3,130,000
4.  Reduction:                         $0
5.  Dollar limit:                      $1,250,000
6.  (a) Laptop / (b) $3,000 / (c) $3,000
7.  Listed property §179:              $0
8.  Total elected:                     $3,000
9.  Tentative deduction:               $3,000
10. Carryover from 2024:               $0
11. Business income limit:             (S-corp passes through; uses S-corp's pre-§179 ordinary income)
12. §179 deduction:                    $3,000  (assuming income covers)
13. Carryover to 2026:                 $0
```

### Part IV summary

```
21. Listed property:        $0
22. Total:                  $3,000  → Form 1120-S Line 14 (depreciation)
```

## Year 2026 Form 4562 — continuing amortization

In year 2 (2026), the same intangibles continue amortizing. They no longer go on Line 42 (current-year start); they go on Line 43 (prior-year continuation) as an aggregate:

```
42. Amortization of costs that begin during 2026:               $0  (no new intangibles)
43. Amortization of costs that began before 2026:               $12,800  ($3,333 + $9,467)
44. Total:                                                      $12,800
```

The supporting detail (which intangibles, which amounts) is kept in BrightStack's accounting records but not on the form.

## Why §197 vs. other treatment

§197 mandates 15-year SL for any intangible acquired in connection with a trade or business. **No other choice is available** for these intangibles:

- Cannot §179 — §179 is for tangible personal property (and certain real property), not intangibles.
- Cannot bonus-depreciate — bonus is for tangible property (and computer software, but only if not §197).
- Cannot use a shorter useful life — even if customers are expected to churn out in 5 years, §197 is a statutory 15-year rule.

The only flexibility: allocate purchase price among Class VI vs. Class VII vs. other classes carefully on Form 8594. Allocations to Class V (tangible) get faster recovery; allocations to Classes VI/VII get §197's slower 15-year SL.

A well-structured acquisition allocation maximizes Class V (tangible property) and minimizes Class VI/VII (§197 intangibles), for the buyer's tax benefit. The seller wants the opposite (Class V is ordinary income via §1245 recapture; Class VI/VII is capital gain). The buyer and seller's allocations on Form 8594 must match (or each invites an IRS adjustment).

## Form 8594 — Asset Acquisition Statement

Filed by both buyer and seller for the year of acquisition. Reports the agreed-upon allocation of purchase price among the seven asset classes. Required when:
- The transferor and transferee transfer assets that constitute a trade or business
- The transferee's basis is determined wholly by the consideration paid

BrightStack files Form 8594 with its 2025 Form 1120-S. The seller files it with their 2025 return.

## Audit defense

If audited:
1. Form 8594 documents the allocation between buyer and seller (matched)
2. Asset purchase agreement supports the $50,000 Class VI total
3. Independent valuation (or contractual allocation) supports the customer list / trade name / workforce / non-compete sub-allocations
4. §197 statutory 15-year period applied — no flexibility taken

## Common §197 pitfalls

1. **Self-created intangibles aren't §197**: BrightStack's own customer list (built up over years of marketing) isn't §197. Only acquired customer lists are.
2. **Software developed in-house** isn't §197. It's §174 (5-year domestic R&E amortization, post-TCJA).
3. **Stock acquisitions** of a business don't trigger §197 amortization at the buyer level (the buyer acquired stock, not assets). §197 amortization only on asset purchases or §338 elections.
4. **Self-rental of real property**: not §197.
5. **Patents & copyrights bought separately from a business**: §167, not §197. Different mechanics.

## Sources cited in this draft

- IRS Form 4562, Rev. 2025
- IRS Instructions for Form 4562, Rev. 2025
- IRS Form 8594 (Asset Acquisition Statement)
- IRC §197 (15-year amortization of acquired intangibles)
- IRC §1060 (allocation of purchase price in applicable asset acquisitions)
- Reg. §1.197-2 (§197 intangibles definitions)
- IRS Pub. 535 (Business Expenses, including §197 amortization rules — note: Pub. 535 has been retired and content moved to Pub. 334 and other publications; verify current consolidation)
- For S-corp tax return mechanics: Form 1120-S instructions, Line 19 (Other deductions, including amortization)
