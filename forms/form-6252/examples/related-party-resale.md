# Example: Lot Sold to a Son Who Resells Within 2 Years

A related-party installment sale. A mother sells a vacant lot to her son on an 8-year note; seven months later the son sells the lot to an unrelated buyer for cash. Form 6252 Part III treats the rest of the son's unpaid price as paid to the mother in the year of the resale. All arithmetic checked in Python.

## The filer

- **Name:** Helen Ostrowski, single, files Form 1040
- **Property:** residential building lot held for investment since 2012 (never depreciated)
- **Buyer:** her son, Marco Ostrowski (lineal descendant: related party under §453(f)(1) and the Form 6252 instructions)
- **Tax year:** 2025; the sale and the resale both happened in 2025

## Inputs gathered

| Item | Value | Source |
|------|-------|--------|
| Date acquired | 06/30/2012 | Deed |
| Binding written contract | 03/24/2025 | Purchase agreement |
| Date sold to Marco | 04/08/2025 | Settlement statement |
| Selling price | $248,750 (appraised FMV) | Settlement statement, appraisal |
| Basis | $92,184 | Purchase closing statement |
| Selling expenses (survey $1,140, attorney $1,895, recording $500) | $3,535 | Invoices |
| Down payment at closing | $31,090 | Settlement statement |
| Note | $217,660 at 5.25% annual interest; 8 equal annual principal payments of $27,207.50 with interest, due each April 8, 2026–2033 | Promissory note |
| Payments received in 2025 | $31,090 (down payment only); no interest due until April 2026 | Asked |
| Marco's resale | 11/19/2025 to an unrelated buyer, $279,400 cash, no installment terms | Asked: "Has Marco sold, given away, or otherwise disposed of the lot?" → "He sold it in November." Then the settlement statement. |
| Any line 29 exception? | Asked about each: resale was 7 months after the first sale (29a no); land, not stock redeemed by an issuer (29b no); voluntary sale, no condemnation (29c no); both alive (29d no); Helen has no facts showing a non-tax-avoidance purpose beyond "Marco got a good offer" and declines to claim 29e | Asked |
| Is the lot depreciable in Marco's hands? | No (land) → §453(g) does not apply | Asked |

## Form 6252 (2025)

```
1.  Code 4 — Vacant residential building lot held for investment
2a. 06/30/2012          2b. 04/08/2025
3.  Related party: Yes
4.  Price determinable by year end: Yes

Part I
5.  Selling price                          248,750
6.  Debt assumed by buyer                        0
7.  Line 5 − line 6                        248,750
8.  Cost or other basis                     92,184
9.  Depreciation allowed or allowable            0
10. Adjusted basis                          92,184
11. Selling expenses                         3,535
12. Recapture                                    0
13. Lines 10 + 11 + 12                      95,719
14. Line 5 − line 13                       153,031
15. Excluded gain                                0
16. Gross profit                           153,031
17. Line 6 − line 13                             0
18. Contract price                         248,750

Part II
19. Gross profit percentage  153,031 ÷ 248,750 = 0.6152 (exact)
20. Line 17 (year of sale)                       0
21. Payments received 2025                  31,090
22. Line 20 + line 21                       31,090
23. Payments in prior years                      0
24. 31,090 × 0.6152 = 19,126.57             19,127
25. Recapture                                    0
26. Line 24 − line 25                       19,127 → Schedule D line 11

Part III
27. Marco Ostrowski, <address>, <SSN>
28. Second disposition this year: Yes
29. Exception box: none
30. Amount realized by Marco               279,400
31. Contract price, year of first sale     248,750
32. Smaller of 30 or 31                    248,750
33. Payments received by year end (lines 22 + 23)  31,090
34. Line 32 − line 33                      217,660
35. 217,660 × 0.6152 = 133,904.43          133,904
36. Recapture                                    0
37. Line 35 − line 36                      133,904 → Schedule D line 11
```

Total 2025 gain: 19,127 + 133,904 = **153,031**, the entire gross profit on line 16. Both amounts are long-term capital gain (held since 2012; investment land is a capital asset).

On line 30: Marco received $279,400 cash, which is his amount realized under the line 30 instructions (money + FMV of property + liabilities assumed). Whatever Marco's own selling costs were, line 32 takes the smaller of line 30 or $248,750, so they do not change the result here. If the resale price had been below Helen's contract price, ask Marco for his settlement statement and enter his amount realized.

## Later years

| Year | Marco pays (principal) | Line 21 | Line 23 | Line 24 | Part III |
|------|-----------------------:|--------:|--------:|--------:|----------|
| 2025 | 31,090 down | 31,090 | 0 | 19,127 | Lines 27–37 (above) |
| 2026 | 27,207.50 | 0 | 248,750 | 0 | Required (year 1 after sale); line 28 "No" |
| 2027 | 27,207.50 | 0 | 248,750 | 0 | Required (year 2 after sale); line 28 "No" |
| 2028–2033 | 27,207.50 each | 0 | 248,750 | 0 | Not required |

Line 21 instructions: an amount entered on the equivalent of line 34 in a prior year goes on line 23, not line 21. Marco's later principal payments were already counted in 2025, so they produce no further gain. Helen still files Form 6252 each year through the year of the final payment (2033), and reports Marco's interest each year on Schedule B.

## Interest

- AFR test: 8 equal annual principal payments → weighted average maturity (8 + 1) ÷ 2 = 4.5 years → mid-term. Annual-compounding mid-term AFRs: lowest for Jan–Mar 2025 (contract month March) = 4.24% (January, Rev. Rul. 2025-1); lowest for Feb–Apr 2025 (sale month April) = 4.21% (April, Rev. Rul. 2025-8). Test rate 4.21%.
- This is a land sale between family members with stated principal of $217,660 (not over $500,000), so §483 governs and the test rate cannot exceed 6% compounded semiannually (Pub. 537). 4.21% is lower than 6%, so 4.21% applies.
- Stated 5.25% annual ≥ 4.21% → adequate. No unstated interest; line 5 stays at $248,750.
- 2025 interest received: $0. Interest begins with the April 2026 payment.

## Special rules checked

- §453(g): not applicable; land is not depreciable in Marco's hands.
- §453A: obligations from 2025 sales outstanding at year end were $217,660, not over $5 million.
- Pledge rule: Helen has not borrowed against the note.
- Gift-related questions (below-market price): the sale was at appraised FMV with adequate interest; anything else is outside this skill, refer to a CPA.

## Validation summary

- Math: 13 = 10 + 11 + 12 ✓; 16 = 153,031 ✓; 19 = 0.6152 exactly ✓; 24 = 31,090 × 0.6152 ✓; 32 = min(279,400, 248,750) ✓; 33 = 22 + 23 ✓; 34 = 248,750 − 31,090 ✓; 35 = 217,660 × 0.6152 ✓; lines 24 + 35 = line 16 ✓.
- Cross-form: lines 26 and 37 both to Schedule D line 11 ✓.
- Sanity: Part III completed because a related-party resale occurred within 2 years and before Marco finished paying ✓; no line 29 box checked without facts ✓.

## Why each non-obvious choice

**Why does the resale tax Helen?** §453(e): when a related buyer disposes of the property within 2 years of the first sale and before paying in full, the seller is treated as receiving the related party's amount realized at the time of the second disposition, up to the contract price minus payments already received (Form 6252 instructions, "Installment Sales to Related Party"; Pub. 537, "Sale and Later Disposition").

**Why not check box 29e?** It requires establishing to the IRS's satisfaction that tax avoidance was not a principal purpose of either sale, with an attached explanation. The instructions point to involuntary dispositions or installment resales on equal or longer terms. Marco's quick cash resale fits neither. The agent does not check 29e on the user's say-so; it asks for facts and, if the user wants to claim it, refers the explanation to a CPA.

**Why does Part III continue in 2026 and 2027?** Line 3 and the Part III header: complete Part III for the year of sale and 2 years after, unless the final payment was received during the tax year.

## Sources cited in this draft

- Form 6252 (2025) and instructions: line 3, lines 21, 23, Part III lines 29, 30, 33, "Installment Sales to Related Party," "Sale of Depreciable Property to Related Person"
- Pub. 537 (2025): "Sale to a Related Person," "Sale and Later Disposition," "Unstated Interest and OID" (test rate; land transfers between related persons)
- Rev. Rul. 2025-1, 2025-5, 2025-6, 2025-8 (AFRs, January–April 2025)
- IRC §453(e), §453(f)(1), §453(g), §483
