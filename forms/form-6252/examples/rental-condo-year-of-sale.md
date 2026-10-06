# Example: Rental Condo Sold on a Seller Note (Year of Sale)

A depreciated residential rental sold in 2025. The buyer assumes the seller's mortgage, pays 10% down, and signs a 10-year note to the seller. Shows Form 4797 Part III run first (zero recapture under straight line), the contract price after an assumed mortgage, unrecaptured §1250 gain reported first, and interest kept off Form 6252. All arithmetic checked in Python.

## The filer

- **Name:** Priya Raman, single, files Form 1040
- **Property:** one-bedroom condo held as a long-term rental since 2016
- **Tax year:** 2025 (year of sale), filed in 2026 on the 2025 Form 6252
- **Buyer:** an unrelated individual who will live in the condo

## Inputs gathered

| Item | Value | Source the agent asked for |
|------|-------|----------------------------|
| Date acquired | 08/17/2016 | Closing statement |
| Placed in service as rental | September 2016 | Prior Schedules E |
| Cost basis (purchase price + acquisition costs) | $286,400 (land $61,350, building $225,050) | Purchase closing statement, depreciation schedule |
| Improvements | None | Asked: "Any improvements since purchase?" → "No" |
| Depreciation allowed or allowable, Sept 2016 – May 2025 | $70,918 (building, 27.5-year straight line, mid-month) | Depreciation schedule; asked: "Was depreciation claimed every year?" → "Yes" |
| Binding written contract signed | 03/28/2025 | Purchase agreement |
| Sale closed | 05/14/2025 | Settlement statement |
| Selling price | $412,500 | Settlement statement |
| Existing mortgage assumed by buyer (lender-approved assumption) | $118,500 | Settlement statement; asked: "Did the buyer take over your loan or get a new one?" → "Took over mine" |
| Cash down payment | $41,250 | Settlement statement |
| Seller note | $252,750, 6.25% interest, 120 level monthly payments of $2,837.88 starting 06/14/2025 | Promissory note |
| Selling expenses (commission, title, transfer tax, legal) | $24,293 | Settlement statement |
| Principal received 06/14/2025 – 12/14/2025 (7 payments) | $10,818 | Amortization schedule |
| Interest received 2025 | $9,047 | Amortization schedule |
| Pledged, sold, or cancelled the note? | No | Asked |
| Other installment notes from 2025 sales | None | Asked |
| Election out | No; she wants the installment method | Asked |

Check: $118,500 assumed + $41,250 down + $252,750 note = $412,500 selling price.

## Step 1 — Form 4797, Part III (year of sale)

```
Line 20 Gross sales price                         412,500
Line 21 Cost or other basis plus expense of sale  286,400 + 24,293 = 310,693
Line 22 Depreciation allowed or allowable          70,918
Line 23 Adjusted basis (21 − 22)                  239,775
Line 24 Total gain (20 − 23)                      172,725
Line 26 §1250 property, straight line:  line 26g = 0
Line 31 (recapture)                                     0  → Form 6252 line 12 = 0; Form 4797 line 13 = 0
Line 32                                               N/A  (Form 4797 used only to figure recapture)
```

## Step 2 — Form 6252 (2025)

```
1.  Code 4 — Residential rental condominium unit (land and building)
2a. 08/17/2016          2b. 05/14/2025
3.  Related party: No
4.  Price determinable by year end: Yes

Part I
5.  Selling price                          412,500
6.  Mortgage assumed by buyer              118,500
7.  Line 5 − line 6                        294,000
8.  Cost or other basis                    286,400
9.  Depreciation allowed or allowable       70,918
10. Adjusted basis                         215,482
11. Selling expenses                        24,293
12. Recapture (Form 4797 line 31)                0
13. Lines 10 + 11 + 12                     239,775
14. Line 5 − line 13                       172,725
15. Excluded gain (main home)                    0
16. Gross profit                           172,725
17. Line 6 − line 13 (118,500 − 239,775)         0
18. Contract price (294,000 + 0)           294,000

Part II
19. Gross profit percentage  172,725 ÷ 294,000 = 0.5875
20. Line 17 (year of sale)                       0
21. Payments received 2025  41,250 + 10,818 = 52,068
22. Line 20 + line 21                       52,068
23. Payments in prior years                      0
24. 52,068 × 0.5875 = 30,589.95             30,590
25. §1252/1254/1255 recapture                    0
26. Line 24 − line 25                       30,590 → Form 4797 line 4

Part III: N/A (buyer not related)
```

The condo (building and its land interest) is one property sold under one contract for one price, so it goes on one Form 6252. Pub. 537 ("Single Sale of Several Assets") reports even separate and unrelated assets of the same type sold under a single contract as one transaction; only assets sold at a loss or ineligible assets must be split out. Only the building was depreciated, and the Form 4797 Part III entry carries that depreciation. If the user's prior preparer split land and building, ask before changing; the total gain is the same.

## Step 3 — Unrecaptured §1250 gain (Schedule D instructions, worksheet line 4)

```
Step 1: smaller of Form 4797 line 22 (70,918) or line 24 (172,725)   = 70,918
Step 2: minus Form 4797 line 26g (0)                                  = 70,918 total to allocate
Step 3: 2025 amount = smaller of line 26 (30,590) or 70,918 remaining = 30,590
Remaining for later years                                             = 40,328
```

All of 2025's gain is unrecaptured §1250 gain (maximum 25% rate, IRC §1(h)(1)(E)). It flows Form 6252 line 26 → Form 4797 line 4 → Form 4797 Part I → Schedule D line 11, and the worksheet result goes to Schedule D line 19.

## Multi-year schedule

Annual principal from the amortization schedule; gain = principal × 0.5875; unrecaptured §1250 gain used first.

| Year | Principal received | Gain (× 0.5875) | Unrecaptured §1250 portion | Cumulative principal |
|------|-------------------:|----------------:|---------------------------:|---------------------:|
| 2025 | 52,068 (incl. 41,250 down) | 30,590 | 30,590 | 52,068 |
| 2026 | 19,486 | 11,448 | 11,448 | 71,554 |
| 2027 | 20,739 | 12,184 | 12,184 | 92,293 |
| 2028 | 22,073 | 12,968 | 12,968 | 114,366 |
| 2029 | 23,493 | 13,802 | 3,728 | 137,859 |
| 2030 | 25,004 | 14,690 | 0 | 162,863 |
| 2031 | 26,612 | 15,635 | 0 | 189,475 |
| 2032 | 28,324 | 16,640 | 0 | 217,799 |
| 2033 | 30,146 | 17,711 | 0 | 247,945 |
| 2034 | 32,085 | 18,850 | 0 | 280,030 |
| 2035 | 13,970 | 8,207 | 0 | 294,000 |
| **Total** | **294,000** (= line 18) | **172,725** (= line 16) | **70,918** | |

The schedule assumes the buyer pays as scheduled; each year's actual principal from the buyer's statement replaces the projection.

## Interest

- 2025 interest $9,047 → Schedule B. The buyer uses the condo as a personal residence, so Priya lists the buyer's name, address, and SSN on Schedule B line 1 (Pub. 537, "Seller-financed mortgage"; ask the buyer for the SSN).
- AFR test: weighted average maturity of the note's principal = 5.56 years → mid-term. Monthly-compounding mid-term AFRs: lowest for Jan–Mar 2025 (contract month March) = 4.16% (January, Rev. Rul. 2025-1); lowest for Mar–May 2025 (sale month May) = 4.03% (May, Rev. Rul. 2025-10). Test rate 4.03%. Stated 6.25% monthly ≥ 4.03% → adequate; no unstated interest. Seller financing $252,750 is under the $7,296,700 limit, so the 9% cap is not the binding figure either way.

## Special rules checked

- §453A interest: price over $150,000, but 2025 notes outstanding at year end total $241,932, not over $5 million → none.
- Pledge rule: price over $150,000; Priya has not borrowed against the note → no deemed payment. Reminder added to the deliverable.
- Related party: no. Electing out: declined.

## Validation summary

- Math: 7 = 5 − 6 ✓; 10 = 8 − 9 ✓; 13 = 10 + 11 + 12 ✓; 14 > 0 ✓; 18 = 7 + 17 ✓; 19 = 16 ÷ 18 = 0.5875 exactly ✓; 24 = 22 × 19 ✓; schedule totals equal lines 18 and 16 ✓.
- Cross-form: Form 6252 line 12 = Form 4797 line 31 = 0 ✓; line 26 on Form 4797 line 4 only ✓; Schedule D worksheet line 4 = 30,590 ✓.
- Sanity: depreciation claimed every year ✓; payments exclude interest ✓.

## Why each non-obvious choice

**Why is the mortgage on line 6 but not the down payment?** Line 6 is only the seller's existing debt that the buyer assumed. The assumed $118,500 never reaches Priya, so it comes out of the contract price. It does not exceed her $239,775 installment sale basis, so line 17 is zero and there is no deemed payment.

**Why zero recapture on a property with $70,918 of depreciation?** Form 4797 line 26 says to enter -0- on line 26g when straight-line depreciation was used (except a corporation subject to §291). The depreciation still matters: it becomes unrecaptured §1250 gain, and the Schedule D instructions apply it to the first payments until it is used up. That is why 2025 through most of 2029 is all 25%-rate gain.

**Why not compare the note rate to an AFR from 2026?** The test rate looks back from the contract month and the sale month (Pub. 537, "Test rate of interest"), not from the filing date.

## Sources cited in this draft

- Form 6252 (2025) and instructions; Form 4797 (2025), Part III and lines 4, 13, 31, 32
- Pub. 537 (2025): "Buyer Assumes Mortgage," "Single Sale of Several Assets," "Depreciation Recapture Income," "Unstated Interest and OID," "Seller-financed mortgage"
- 2025 Instructions for Schedule D, Unrecaptured Section 1250 Gain Worksheet, line 4; IRC §1(h)(1)(E)
- Rev. Rul. 2025-1, 2025-5, 2025-6, 2025-8, 2025-10 (AFRs, January–May 2025)
- IRC §453, §453A
