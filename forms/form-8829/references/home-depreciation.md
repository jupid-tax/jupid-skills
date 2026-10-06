# Depreciation of the Home (Form 8829, Part III) and What Happens at Sale

Owners only. Renters skip Part III (rent is on line 19). Sources: 2025 Form 8829 lines 37–42; 2025 Instructions for Form 8829, Part III and Line 42; Pub. 587 (2025), "Depreciating Your Home" and "Sale or Exchange of Your Home"; Pub. 523 (2025); 2025 Form 4562 line 19j; IRC §168(c) (39-year nonresidential real property), §121(d)(6), §1(h)(1)(E).

## Inputs to ask for

1. Month and year the home was **first used for business** (not the purchase date).
2. Purchase price and the cost of permanent improvements made **before** business use began, minus any casualty losses deducted or depreciation from earlier business or rental use. That is the adjusted basis (Pub. 587, Adjusted basis defined; Pub. 551).
3. Fair market value of the home on the first-business-use date (Pub. 587: sales of similar property around that date help).
4. Land: cost or other basis of the land, and its FMV on the first-business-use date if lower. A county assessment split is one way users estimate it; ask what source they used and record it.
5. Improvements placed in service **after** business use began, with dates and costs (depreciated separately).
6. Prior Forms 8829 (or depreciation schedules) showing depreciation already claimed, and years the simplified method was used.

If any of 1–4 is missing, stop and ask. Do not plug a land percentage.

## Line-by-line computation

```
Line 37  = smaller of (adjusted basis incl. land) or (FMV incl. land) on the first-business-use date
Line 38  = land: smaller of its cost/basis or its FMV on that date
Line 39  = line 37 − line 38                      (building basis)
Line 40  = line 39 × line 7                       (business basis)
Line 41  = percentage from the table below
Line 42  = line 40 × line 41  (+ improvements statement) → also on line 30
```

Lines 37 and 38 are fixed on the first-business-use date: "Do not adjust this amount for depreciation claimed or changes in fair market value after the year you first used your home for business" (i8829).

## Why the percentages look the way they do

A home office is depreciated as **nonresidential real property**: MACRS, straight line, **39 years**, **mid-month convention** (Pub. 587; Form 4562 line 19j "39 yrs., MM, S/L"). Mid-month means the first year counts half a month for the month placed in service plus the remaining full months, so a January start gets roughly 11.5 ÷ 12 of a full year and a December start roughly 0.5 ÷ 12. Full years are 1 ÷ 39 ≈ 2.564%. The published percentages are rounded table values (the first-year figure absorbs the rounding), so always enter the table percentage, never a recomputed one.

| First used in 2025 | % | First used in 2025 | % |
|---|---|---|---|
| January | 2.461 | July | 1.177 |
| February | 2.247 | August | 0.963 |
| March | 2.033 | September | 0.749 |
| April | 1.819 | October | 0.535 |
| May | 1.605 | November | 0.321 |
| June | 1.391 | December | 0.107 |

First used after May 12, 1993 and before 2025: **2.564%**. Earlier dates, mid-1993 binding contracts, and business use that stopped during the year: use Pub. 946 (or Pub. 534 for pre-1987), per the line 41 table in the instructions.

Pub. 587 worked check: business use began in May; 8% business; building adjusted basis $115,000 (below FMV) → $9,200 business basis × 1.605% = $147.66.

### Simplified-method years in between

- In a simplified year, home depreciation is deemed zero (Pub. 587).
- Returning to Form 8829: the 2025 instructions say to use the line 41 table (example: first used 2024 under the simplified method → 2.564% for 2025). Pub. 587 says later actual-expense years use the MACRS optional table in Pub. 946. For a home whose business use began years ago with simplified years in between, compute from the Pub. 946 table and flag the computation for CPA review.

### Improvements after business use began

Business percentage of the improvement's cost, depreciated as if the home were first used for business when the improvement was placed in service: 39 years; for improvements placed in service in 2025, the month percentage above (Pub. 587, Depreciating permanent improvements; i8829 Line 42 table). Attach a statement showing the computation, include the result in line 42, and write "See attached" below the entry space. Do not put these amounts on lines 37–40.

### Form 4562

Attach Form 4562 only if (a) the home was first used for business in 2025, or (b) additions or improvements were placed in service in 2025 (i8829 Line 42). First-year home: Form 4562 line 19j, column (b) = month and year first used, (c) = Form 8829 line 40, (g) = Form 8829 line 42. Improvements: line 19j with their own month/year, business basis, and depreciation. Do not include these amounts on Schedule C line 13. Hand the Form 4562 entries to [../../form-4562/SKILL.md](../../form-4562/SKILL.md), and tell it to use row 19j (2025 Form 4562: 19h = 50-year, 19i = residential rental 27.5-year, 19j = nonresidential real 39-year).

## Allowed or allowable

Basis is reduced by the depreciation **allowed or allowable**, even if the filer did not claim it (Pub. 587, Adjusting for depreciation deducted in earlier years; Basis Adjustment). If the user owns the home, uses it for business, and never claimed depreciation, say so plainly in the draft: the basis reduction and the tax on sale happen anyway, and fixing missed depreciation (amended return or accounting method change, Pub. 946) is a CPA task.

## Line 30 vs line 42

Line 42 is the depreciation computed. Line 30 copies it. Whether it is deducted this year depends on line 28: anything above the line 28 room carries forward on line 44. Carried-over depreciation that was never deducted because of the income limit is still part of the record; ask a CPA how it affects basis if the home is sold before it is used.

## Sale of the home: the boundary

Form 8829 does not report a sale. When the user sells a home that had an office in it, route the sale and give these facts:

| Situation | Treatment | Source |
|---|---|---|
| Office was **inside** the dwelling (a room, part of a room) | No allocation of gain between business and home parts; no Form 4797 needed for the business part. The §121 exclusion ($250,000; $500,000 for certain joint filers) can apply, **but not to the part of the gain equal to depreciation allowed or allowable after May 6, 1997** | Pub. 587, Part of Home Used for Business; Pub. 523, Space within the living area |
| Office was a **separate structure** (detached studio) and the use test is not met for it, or it was used for business in the year of sale | Treat as two properties: allocate selling price, expenses and basis; report the business part on Form 4797 | Pub. 587, Separate Part of Property Used for Business |
| Separate structure, no business use in the year of sale, use test met for both parts | No allocation, no Form 4797 | Pub. 587 |
| Loss on the personal part | Not deductible | Pub. 587, Reporting the Sale |

The depreciation portion is **unrecaptured section 1250 gain**, taxed at a maximum 25% rate (IRC §1(h)(1)(E)), computed on the Unrecaptured Section 1250 Gain Worksheet in the Schedule D instructions. Pub. 523's example: depreciation of $2,000 and a $13,000 gain → $2,000 recognized as unrecaptured section 1250 gain, $11,000 excludable.

Hand-offs: home sale reporting → [../../form-8949/SKILL.md](../../form-8949/SKILL.md) and [../../schedule-d/SKILL.md](../../schedule-d/SKILL.md); separate-structure business part → [../../form-4797/SKILL.md](../../form-4797/SKILL.md); sold on a seller note → [../../form-6252/SKILL.md](../../form-6252/SKILL.md). This skill only supplies the cumulative depreciation figure from the user's Forms 8829.
