# Example: Two Long-Term Rentals, Single Filer Inside the $25,000 Phase-Out

Two residential rentals, one placed in service in 2025, both showing losses, MAGI between $100,000 and $150,000. Shows: first-year mid-month depreciation, Form 4562 triggers, the Form 8582 phase-out, and allocation of the allowed loss between properties. All math checked in Python. Tax year 2025 (filed in 2026), 2025 forms.

## The filer

- **Name**: Tomás Herrera (fictional)
- **Filing status**: Single
- **Job**: W-2 QA engineer; wages $133,915; bank interest $263; no IRA deduction, student loan interest, social security, or other Form 8582 line 6 adjustments
- **Other passive activities**: none; no prior-year suspended passive losses (confirmed: no 2024 Form 8582)
- **Participation**: self-manages Property A; approves tenants, rent and repairs for Property B (manager handles day-to-day). Owns 100% of both. Active participation: yes. Real estate professional: no (full-time W-2 job)

## Inputs gathered

### Property A: single-family house, Columbus, OH (code 1)

- Placed in service 2019; building basis $171,950 (land excluded per county assessor split)
- Rented all year at a fair rental price: 365 fair rental days, 0 personal days
- Rent $1,585 × 12 = $19,020; kept $410 of the former tenant's deposit for wall damage (Pub. 527: kept deposit is income) → line 3 $19,430
- 412 miles driven for the rental, standard mileage used since the car's first rental year, contemporaneous log
- Form 1098 interest $6,872; property tax $3,318; insurance $1,214; lawn service $640; furnace igniter and roof-leak patch $1,947 paid to one unincorporated contractor (confirmed repairs, not replacements); filters and hardware $163; tax-prep fee allocated to the rental $385

### Property B: condo, Dayton, OH (code 1)

- Bought April 2025; cleaned, listed and available for rent May 12, 2025 → placed in service May 2025
- Building basis $163,486 (purchase price plus closing costs, less land per assessor split)
- First tenant June 1, 2025: 214 fair rental days (June 1–Dec 31), 0 personal days; rent $1,395 × 7 = $9,765
- Listing fee $89; leasing commission $698 and management fees paid to the management company (a corporation, per its Form W-9); insurance $806; property manager 10% of rent $976.50 → $977; Form 1098 interest $6,421; garbage disposal repair $312; property tax $1,689; May utilities while vacant and listed $214; condominium association dues $265 × 8 = $2,120 (regular monthly dues, no special assessment; the agent asked)

## Depreciation (line 18) and Form 4562

| Property | Basis | Rate | Source | Line 18 |
|---|---|---|---|---|
| A (2019, year 7) | $171,950 | 3.636% | Pub. 527 Table 2-2d | $6,252 |
| B (May 2025, year 1) | $163,486 | 2.273% | Pub. 527 Table 2-2d, May row | $3,716 |

- $171,950 × 0.03636 = $6,252.10 → $6,252
- $163,486 × 0.02273 = $3,716.04 → $3,716
- Form 4562 required for B (placed in service in 2025): line 19i, Residential rental property, 05/2025, basis $163,486, 27.5 yrs, MM, S/L, $3,716.
- Form 4562 required for A because of the auto expense (Part V). File a separate Form 4562 for each activity that needs one (Instructions for Form 4562). Hand both to `../../form-4562/SKILL.md`.
- Line 6, Property A: 412 × $0.70 = $288.40 → $288.

## The completed Schedule E, Part I

```
Line A  Payments requiring 1099s in 2025: Yes ($1,947 to a sole-proprietor repair contractor)
Line B  Filed required 1099s: Yes (1099-NEC filed January 2026; see ../../form-1099-nec/SKILL.md)

                                     A (Columbus)     B (Dayton)
1a  Address                          [street], Columbus, OH [ZIP]   [street], Dayton, OH [ZIP]
1b  Type                             1                1
2   Fair rental days / Personal / QJV  365 / 0 / no   214 / 0 / no

3   Rents received                   19,430           9,765
4   Royalties received                    0               0
5   Advertising                           0              89
6   Auto and travel                     288               0
7   Cleaning and maintenance            640               0
8   Commissions                           0             698
9   Insurance                         1,214             806
10  Legal and other professional        385               0
11  Management fees                       0             977
12  Mortgage interest (banks)         6,872           6,421
13  Other interest                        0               0
14  Repairs                           1,947             312
15  Supplies                            163               0
16  Taxes                             3,318           1,689
17  Utilities                             0             214
18  Depreciation                      6,252           3,716
19  Other (condo assoc. dues)             0           2,120
20  Total expenses                   21,079          17,042
21  Income or (loss)                 (1,649)         (7,277)
22  Deductible rental RE loss        (1,461)         (6,450)

23a Total rents                      29,195
23b Total royalties                       0
23c Total mortgage interest          13,293
23d Total depreciation                9,968
23e Total expenses                   38,121
24  Income (positive line 21)             0
25  Losses                           (7,911)
26  Total rental RE and royalty      (7,911)  → Schedule 1, line 5 (Parts II–V not used)
```

## Form 8582 worksheet (passive loss limit)

Form 8582 is required: MAGI is over $100,000, so the Exception for Certain Rental Real Estate Activities fails (Instructions for Schedule E).

```
MAGI (line 6): 133,915 + 263 = 134,178   (no line 6 adjustments)

Part I   1a  0      1b  (8,926)   1c  0      1d  (8,926)
         3   (8,926)
Part II  4   8,926   (smaller of loss on 1d or 3)
         5   150,000
         6   134,178
         7   15,822
         8   7,911   (50% of line 7; not over 25,000)
         9   7,911   (smaller of line 4 or 8)
Part III 10  0       11  7,911

Part VI allocation of line 9
  Activity     Loss (a)   Ratio (b)   Special allowance (c)   Unallowed (d)
  Property A    1,649     0.1847            1,461                 188
  Property B    7,277     0.8153            6,450                 827
  Total         8,926     1.0000            7,911               1,015
```

Ratio A = 1,649 ÷ 8,926 = 0.184741; 0.184741 × 7,911 = 1,461.49 → 1,461; B = 7,911 − 1,461 = 6,450. Unallowed $1,015 (A $188, B $827) carries to 2026 on Form 8582 (Parts VII–VIII). Phase-out check: $25,000 − 50% × ($134,178 − $100,000) = $25,000 − $17,089 = $7,911. Same answer as line 8.

## Validation summary

- Math: line 20 = sum of lines 5–19 for each column; line 21 = line 3 − line 20; 23a–23e equal the column totals; line 25 = sum of line 22; line 26 = 24 + 25. All pass.
- Form 8582: line 9 ≤ $25,000 and ≤ total loss; Part VI column (c) total = line 9.
- Sanity: no personal days, so no §280A allocation; Property B line 21 loss is driven by first-year interest, association dues and partial-year rent, consistent with a May placed-in-service date.
- Attachments: Form 4562 (two), Form 8582.
- Carry to 2026: suspended passive loss A $188, B $827.

## Sources cited in this draft

- 2025 Schedule E (Form 1040) and 2025 Instructions for Schedule E (Lines 3, 6, 18, 22; Exception for Certain Rental Real Estate Activities)
- 2025 Form 8582 and Instructions (Part II, Line 6, Parts VI–VIII)
- Pub. 527 (2025): ch. 1 (security deposits), Table 2-2d (27.5-year percentages), Pre-rental expenses
- Pub. 925 (2025): Special $25,000 allowance, Phaseout rule
- Instructions for Form 4562 (2025): separate Form 4562 per activity; Form 4562 line 19i

## Why the non-obvious choices

- **Placed in service in May, not June.** Depreciation starts when the property is available and ready for use (Instructions, Line 18), and expenses are deductible from the time it is made available for rent (Pub. 527, Pre-rental expenses). The May utilities and the 2.273% rate follow from the May 12 listing date. The agent asked for the listing date rather than using the lease start.
- **Association dues on line 19.** No line 5–18 category fits, and line 19 takes ordinary and necessary expenses not listed elsewhere (Instructions, Line 19). The agent confirmed the dues were regular operating dues, not a special assessment for an improvement, which would be capitalized.
- **Kept deposit on line 3.** Only the $410 kept is income; the rest of the deposit is not.
- **Form 8582 even though the total loss is under $25,000.** The skip exception also requires MAGI of $100,000 or less.
