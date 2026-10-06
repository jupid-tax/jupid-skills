# Example: Third Year of a Land Sale Note

A later-year Form 6252. Investment land was sold in 2023 on a 5-year note; 2025 is the third Form 6252. Shows Part I carried forward unchanged, line 20 = 0, line 23 cumulative, a principal prepayment, and the lost-prior-form situation. All arithmetic checked in Python.

## The filer

- **Name:** Walt Henley, married filing jointly
- **Property:** 4.2-acre vacant parcel held for investment (never used in a business, never depreciated)
- **Tax year:** 2025 (third year of the note), filed in 2026 on the 2025 Form 6252
- **Buyer:** an unrelated neighbor

## What the agent asked first

Walt's request: "Do my land payments go on my taxes again this year?" The agent asked for the 2023 and 2024 Forms 6252. Walt had the 2024 form but not the 2023 one. The agent asked for the 2023 return copy from his preparer rather than rebuilding Part I from memory; if that copy had not existed, it would have asked for the 2023 settlement statement and the land's purchase records and shown the reconstruction to Walt for confirmation, flagging that it must match what was filed in 2023.

## Inputs gathered

| Item | Value | Source |
|------|-------|--------|
| Date acquired | 05/03/2011 | 2023 Form 6252 line 2a |
| Date sold | 09/12/2023 | 2023 Form 6252 line 2b |
| Selling price | $186,750 | 2023 Form 6252 line 5 |
| Debt assumed by buyer | $0 | 2023 line 6 |
| Basis | $41,920 | 2023 line 8 |
| Selling expenses | $11,117 | 2023 line 11 |
| Gross profit percentage (year of sale) | 0.7160 | 2023 line 19 |
| Note | $158,750 at 7% annual interest; principal $31,750 due each Sept. 12, 2024–2028, with interest | Promissory note |
| Down payment 2023 | $28,000 | 2023 line 21 |
| Principal 2024 | $31,750 | 2024 Form 6252 line 21 |
| Principal 2025 | $31,750 scheduled + $9,415 voluntary prepayment on 09/12/2025 = $41,165 | Buyer's 2025 statement |
| Interest received 2025 | $8,890 (7% × $127,000 balance outstanding Sept. 2024 – Sept. 2025) | Buyer's 2025 statement |
| Note pledged, sold, cancelled; price reduced? | No | Asked |

## Form 6252 (2025)

```
1.  Code 4 — 4.2-acre vacant land held for investment
2a. 05/03/2011          2b. 09/12/2023
3.  Related party: No
4.  Price determinable by year end: Yes (same answer as 2023)

Part I (year-of-sale amounts, unchanged since 2023)
5.  Selling price                          186,750
6.  Debt assumed by buyer                        0
7.  Line 5 − line 6                        186,750
8.  Cost or other basis                     41,920
9.  Depreciation allowed or allowable            0
10. Adjusted basis                          41,920
11. Selling expenses                        11,117
12. Recapture                                    0
13. Lines 10 + 11 + 12                      53,037
14. Line 5 − line 13                       133,713
15. Excluded gain                                0
16. Gross profit                           133,713
17. Line 6 − line 13                             0
18. Contract price                         186,750

Part II
19. Gross profit percentage (2023 figure)   0.7160   (133,713 ÷ 186,750 = 0.716 exactly)
20. Not year of sale                             0
21. Payments received 2025                  41,165
22. Line 20 + line 21                       41,165
23. Payments in prior years  28,000 + 31,750 = 59,750
24. 41,165 × 0.7160 = 29,474.14             29,474
25. Recapture                                    0
26. Line 24 − line 25                       29,474 → Schedule D line 11 (long-term; held more than 1 year at sale)

Part III: N/A (buyer not related)
```

## History and projection

| Year | Principal | Gain (× 0.7160) | Cumulative principal |
|------|----------:|----------------:|---------------------:|
| 2023 | 28,000 | 20,048 | 28,000 |
| 2024 | 31,750 | 22,733 | 59,750 |
| 2025 | 41,165 | 29,474 | 100,915 |
| 2026–2028 (remaining) | 85,835 | 61,458 | 186,750 |
| **Total** | **186,750** (= line 18) | **133,713** (= line 16) | |

The prepayment does not change the percentage; it moves $9,415 of principal (and $6,741 of gain) into 2025. The remaining balance is $85,835; Walt files Form 6252 each year until the final payment, including any year with no payment.

## Interest

$8,890 → Schedule B as interest income, not on Form 6252. The 2023 return already settled whether the note's 7% rate was adequate; the agent noted it should not redo the AFR test in a later year unless the note terms were modified.

## Special rules checked

- §453A interest: 2023 sale price over $150,000, but obligations arising in 2023 and outstanding at the end of 2023 were $158,750, not over $5 million → none in any year.
- Pledge rule: asked whether Walt borrowed against the note → no.
- §453B: prepayment at face value is a payment, not a disposition. No forgiveness or sale of the note.

## Validation summary

- Math: Part I identical to the 2023 form ✓; line 19 = year-of-sale figure ✓; line 20 = 0 ✓; line 23 = sum of prior lines 21 (and 2023 line 20 = 0) ✓; line 24 = 41,165 × 0.7160 ✓; cumulative gain plus remaining projected gain = line 16 ✓.
- Cross-form: line 26 on Schedule D line 11 only ✓ (capital asset, long-term; not Form 4797 because the land was investment property, not used in a trade or business).
- Sanity: 2025 principal exceeds the scheduled installment → confirmed with the buyer's statement that $9,415 was principal, not interest ✓.

## Why each non-obvious choice

**Why not recompute the percentage?** Line 19 instructions: in later years enter the year-of-sale percentage even if Form 6252 was not filed that year. Only a reduction of the selling price changes it (Pub. 537, Worksheet B).

**Why does Part I appear again?** The form says "Complete this part for all years of the installment agreement." Its amounts are the 2023 amounts.

**Why Schedule D and not Form 4797?** Line 26 instructions and Pub. 537 ("Other forms"): Form 4797 line 4 is for trade or business property held more than 1 year; capital assets go to Schedule D (line 11 when long-term). Long-term character from the year of sale carries into later years.

## Sources cited in this draft

- Form 6252 (2025) and instructions: "Purpose of Form," lines 19, 21, 23, 26
- Pub. 537 (2025): "Figuring Installment Sale Income," "Other forms," "Selling Price Reduced," "Disposition of an Installment Obligation," "Interest on Deferred Tax," "Installment Obligation Used as Security (Pledge Rule)"
- Schedule D (Form 1040) (2025), line 11
