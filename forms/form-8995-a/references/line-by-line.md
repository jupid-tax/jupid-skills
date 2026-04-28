# Form 8995-A — Line by Line Reference

Complete reference for every line on Form 8995-A and its four schedules. Use as a lookup when implementing Step 6 (Part II per business) or Step 8 (Part IV) of the workflow.

---

## Part I — Trade, business, or aggregation information

### Line 1, columns (a)-(c)

For each business or aggregation, record:

- **(a) Name** — Business name as it appears on Schedule C, K-1, or aggregation election
- **(b) SSTB checkbox** — Check if the business is a Specified Service Trade or Business per IRC §199A(d)(2)(A) and Treas. Reg. §1.199A-5(b)(2). See `references/sstb-classification.md`.
- **(c) Taxpayer Identification Number** — EIN if the business has one; SSN if not (Schedule C filers without an EIN).

The form provides three rows. Additional businesses go on continuation pages — same format, attach to the form.

---

## Part II — Determine your adjusted qualified business income

Computed once per row from Part I. Lines 2-13.

### Line 2 — Qualified business income (loss)

The net QBI from this business. Sources and adjustments:

| Source | What goes on L2 |
|--------|-----------------|
| Schedule C (sole prop) | Line 31 net profit MINUS (allocable ½ SE tax + SE health insurance + SE retirement contribution) |
| S-corp K-1 | Box 1 ordinary business income MINUS reasonable comp paid to owner-shareholder |
| Partnership K-1 | Box 1 ordinary income (no further reduction; guaranteed payments already excluded) |
| Schedule E rental rising to §162 trade/business | Net rental income (must qualify as a trade or business) |
| §1.199A-1(b)(14) safe harbor rental | Net rental income (must meet 250-hour, separate-books, contemporaneous-records tests) |

Excluded from QBI per Treas. Reg. §1.199A-3(b)(2):
- Capital gains and losses
- Dividends (other than qualified REIT dividends)
- Interest income not allocable to a trade or business
- Reasonable compensation paid by S-corp to owner
- Guaranteed payments to a partner
- Foreign-source income that doesn't rise to a US trade or business

### Line 3 — Multiply Line 2 by 20%

Tentative deduction at the maximum rate.

### Line 4 — Allocable share of W-2 wages

W-2 wages paid by the business in the calendar year ending in the tax year. Per Treas. Reg. §1.199A-2(b):

- Includes: wages reported in W-2 Box 1, plus elective deferrals to 401(k)/403(b)/457(b)/SIMPLE/SEP, plus designated Roth contributions
- Excludes: amounts not subject to FICA, guaranteed payments, payments to independent contractors (1099)
- For S-corps: includes the owner's reasonable comp (which is itself W-2 wages from the corp)
- For partnerships: actual W-2 wages paid to employees only — NOT guaranteed payments

If multiple businesses share employees, allocate W-2 wages to each business based on time/effort/services.

### Line 5 — Multiply Line 4 by 50%

The "50% W-2" branch of the W-2/UBIA limit.

### Line 6 — Multiply Line 4 by 25%

First component of the alternative limit.

### Line 7 — UBIA of qualified property

Unadjusted Basis Immediately after Acquisition of qualified property. Per Treas. Reg. §1.199A-2(c):

- Includes: tangible depreciable property (buildings, equipment, vehicles, furniture, machinery)
- Excludes: land, intangibles (goodwill, patents, trademarks), inventory, intellectual property
- Property must be within its **depreciable period** = longer of 10 years or its MACRS recovery period from when first placed in service
- Use original purchase price (basis), not current adjusted basis
- For property contributed to a partnership/S-corp by an owner, special rules apply per §1.199A-2(c)(3)

### Line 8 — Multiply Line 7 by 2.5%

Second component of the alternative limit.

### Line 9 — Add Lines 6 and 8

The "25% W-2 + 2.5% UBIA" alternative limit.

### Line 10 — Greater of Line 5 or Line 9

The W-2/UBIA limit. The taxpayer chooses the more favorable of the two formulas.

### Line 11 — Smaller of Line 3 or Line 10

The W-2/UBIA limit applied: tentative QBI deduction capped at the limit.

### Line 12 — Phased-in reduction (from Schedule A, if applicable)

Only nonzero if (a) the business is SSTB AND (b) taxable income is in the phase-in zone. Pull from Schedule A Line 13.

### Line 13 — Subtract Line 12 from Line 11

The adjusted QBI for this business after the phase-in reduction (if any). This is what flows to Part IV Line 27 (after possible loss netting on Schedule C of Form 8995-A).

---

## Part III — Phased-in reduction

Used as the on-form summary of Schedule A. Lines 14-26 mirror Schedule A's reduction computation. If Schedule A wasn't needed (no SSTB or above the top of phase-in), Part III is blank.

(In practice, the IRS form has Part III computed identically to Schedule A; recent versions of the instructions point users at Schedule A directly for the formal computation.)

---

## Part IV — Determine your QBI deduction

### Line 27 — Total QBI component

Sum of all Part II Line 13 amounts. If Schedule C of Form 8995-A was used (loss netting), use the Schedule C result instead.

### Line 28 — Qualified REIT dividends and qualified PTP income

- Qualified REIT dividends: 1099-DIV Box 5 (Section 199A dividends)
- Qualified PTP income: from K-1 of a publicly traded partnership

### Line 29 — Prior-year qualified REIT/PTP loss carryforward

Negative amount; reduces L28.

### Line 30 — Add Lines 28 and 29

If negative, enter zero (loss carries forward to next year on L29).

### Line 31 — Multiply Line 30 by 20%

REIT/PTP component. NOT subject to the W-2/UBIA limit.

### Line 32 — Add Lines 27 and 31

Combined QBI + REIT/PTP deduction before the overall taxable-income cap.

### Line 33 — Taxable income before QBI deduction

Form 1040 Line 11 (AGI) MINUS Line 12 (standard or itemized deduction). Do NOT subtract Line 13.

### Line 34 — Net capital gains

Net LTCG (Schedule D Line 16, if positive) PLUS qualified dividends (Form 1040 Line 3a).

### Line 35 — Subtract Line 34 from Line 33

Taxable income excluding net capital gains.

### Line 36 — Multiply Line 35 by 20%

Overall cap on the QBI deduction.

### Line 37 — Smaller of Line 32 or Line 36

The §199A deduction is the lesser of (a) QBI + REIT/PTP component, or (b) 20% of taxable income excluding capital gains.

### Line 38 — DPAD reduction (from Schedule D, if applicable)

Cooperative patron reduction.

### Line 39 — Final QBI deduction

L37 minus L38. Flows to Form 1040 Line 13.

---

## Schedule A — Specified Service Trades or Businesses

Used only for SSTBs in the phase-in zone.

### Line 1 — Trade or business name

Must match Part I Line 1(a).

### Line 2 — Taxable income before QBI deduction

Same as Part IV Line 33.

### Line 3 — Threshold

For 2025: $241,950 single/HoH/MFS, $483,900 MFJ/QSS.

### Line 4 — Subtract Line 3 from Line 2

Excess over threshold.

### Line 5 — Phase-in range

$50,000 single/HoH/MFS; $100,000 MFJ/QSS.

### Line 6 — Phase-in percentage

L4 ÷ L5. The fraction of QBI you LOSE. Compute to at least 4 decimal places per the instructions.

### Line 7 — Applicable percentage

1 − L6. The fraction you KEEP.

### Lines 8-12 — Reduced QBI / W-2 / UBIA computation

Apply L7 to QBI, W-2 wages, and UBIA. Recompute the W-2/UBIA limit on the reduced amounts:

- L8 = QBI × L7
- L9 = W-2 wages × L7
- L10 = UBIA × L7
- L11 = max(50% × L9, 25% × L9 + 2.5% × L10)  (the W-2/UBIA limit on reduced amounts)
- L12 = min(20% × L8, L11)  (tentative deduction at reduced amounts)

### Line 13 — Phase-in reduction

L11 (Part II) − L12 (Schedule A). The amount by which the original W-2/UBIA-limited deduction is reduced. Carries to Part II Line 12.

---

## Schedule B — Aggregation

Lists the businesses being aggregated under Treas. Reg. §1.199A-4. For each business:

- Name and EIN
- The factors satisfied (out of: same products/services, shared facilities, operating coordination)
- Confirmation of common ownership (50%+, attribution rules apply)
- Confirmation that none is an SSTB

Once the election is made, it's binding for that year and all subsequent years until the businesses are no longer eligible to aggregate or a major event (sale, merger) breaks the aggregation.

---

## Schedule C — Loss Netting and Carryforward

If any business has a negative QBI:

1. Sum positive QBIs across all businesses (call this P)
2. For each positive-QBI business, allocate the loss × (positive QBI of business / P)
3. Reduce each business's positive QBI by the allocated loss
4. If aggregate is still negative after netting, total carries to next year as a "QBI loss carryover"

The W-2/UBIA limit computation in Part II uses the POST-NETTING positive QBI as L2.

---

## Schedule D — Patrons of Cooperatives

Only for filers who received Section 199A(g) information from an agricultural or horticultural cooperative. Computes the §199A(g) DPAD reduction. Most filers skip Schedule D entirely.

---

## Cross-references

- See [`sstb-classification.md`](./sstb-classification.md) for SSTB rules
- See [`sstb-phase-in.md`](./sstb-phase-in.md) for Schedule A walkthroughs
- See [`qbi-computation.md`](./qbi-computation.md) for QBI mechanics by income type
- See [`aggregation.md`](./aggregation.md) for Schedule B election rules
- See [`loss-netting.md`](./loss-netting.md) for Schedule C of Form 8995-A
