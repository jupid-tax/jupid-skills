# Example: Vacation Cabin Used as a Home (§280A, Worksheet 5-1)

A mountain cabin rented part of the season, used by the owners and a relative rent-free. Shows: day counting (including repair days that are not personal days), the "used as a home" test, expense division, Worksheet 5-1 ordering, an exact-zero line 21, and carryovers. All math checked in Python. Tax year 2025 (filed in 2026).

## The filers

- **Names**: Adaeze and Martin Okafor (fictional), married filing jointly
- **Itemize** on Schedule A; total state and local taxes $11,840, below $40,000, so Worksheet 5-1 Line 2b Step 1 applies; cabin mortgage is within the home mortgage interest limits (confirmed by their preparer's Schedule A worksheet)
- **Property**: cabin, Blue Ridge, GA; bought 2019; building basis $286,450 (land excluded)
- **No Worksheet 5-1 carryover from 2024** (cabin was not rented before 2025)

## Day count (asked date by date)

| Use | Days | Bucket |
|---|---|---|
| Listed at a fair rental price, June 1 – Aug 30 | 91 | available |
| Of those, not booked | 30 | available but not rented: not rental days |
| Rented to unrelated guests at the listed rate | 61 | fair rental days |
| Okafor family stays (May and September) | 15 | personal |
| Martin's sister, rent free (October) | 4 | personal (family, below fair rent) |
| Adaeze and Martin replacing rotted deck boards and re-staining, full working days (April) | 3 | neither: substantially full-time repair and maintenance |

- Personal days = 15 + 4 = **19**
- Threshold = max(14, 10% × 61 = 6.1) = **14**
- 19 > 14 → **used as a home**; rented 61 days (15 or more) → report on Schedule E with Worksheet 5-1 if expenses exceed rent. Not a passive activity, so no Form 8582 for the cabin.

Repair or improvement? The agent asked before classifying the three April days: rotted boards replaced like-for-like on the existing deck, no expansion. That is repair and maintenance (Instructions, Line 14), so the three days are not personal days (Pub. 527). Had it been an improvement, the agent would have asked the CPA how to count the days rather than guess.

Schedule E line 2: fair rental days **61**, personal use days **19**, QJV not checked (the QJV election requires both spouses to materially participate in a rental real estate business; mere joint ownership of property that is not a trade or business does not qualify, per the Instructions, QJV).

## Annual expenses (whole cabin)

| Item | Amount | Worksheet 5-1 line |
|---|---|---|
| Mortgage interest (Form 1098) | $9,486 | 2a (rental share) |
| Real estate taxes | $3,712 | 2b (rental share) |
| Listing advertising | $215 | 2d direct |
| Platform host service fee | $1,147 | 2d direct |
| Insurance | $1,388 | 4a (rental share) |
| Utilities | $2,164 | 4a |
| Repairs (incl. deck boards) | $1,047 | 4a |
| Cleaning and maintenance (gutters, snow plowing) | $612 | 4a |
| Depreciation, full year: $286,450 × 3.636% | $10,415.32 | 6b (rental share) |

## Worksheet 5-1

```
PART I
A  Days available at fair rental price              91
B  Available but not rented                         30
C  Rental use (A − B)                               61
D  Personal use                                     19
E  Total use (C + D)                                80
F  Rental percentage (C ÷ E)                    0.7625

PART II
1   Rents received                              14,335.00
2a  Mortgage interest × F (9,486 × 0.7625)       7,233.08
2b  Real estate taxes × F (3,712 × 0.7625)       2,830.40
2c  Casualty losses                                  0.00
2d  Direct rental expenses (215 + 1,147)         1,362.00
2e  Total 2a–2d                                 11,425.48
3   Line 1 − 2e                                  2,909.52
4a  Operating × F ((1,388+2,164+1,047+612) × F)  3,973.39
4b  Excess mortgage interest                         0.00
4c  Excess real estate taxes                         0.00
4d  Operating carryover from 2024                    0.00
4e  Total 4a–4d                                  3,973.39
4f  Smaller of 3 or 4e                           2,909.52
5   Line 3 − 4f                                      0.00
6a  Excess casualty losses                           0.00
6b  Depreciation × F (10,415.32 × 0.7625)        7,941.68
6c  Casualty/depreciation carryover from 2024        0.00
6d  Total 6a–6c                                  7,941.68
6e  Smaller of 5 or 6d                               0.00

PART III (carry to 2026)
7a  Operating expenses (4e − 4f)                 1,063.87
7b  Excess casualty losses and depreciation (6d − 6e)  7,941.68
```

Whole dollars on Schedule E: 2a $7,233, 2b $2,830, 2d $1,362; allowed operating expenses = $14,335 − $7,233 − $2,830 − $1,362 = $2,910. Pub. 527 lets the limited amount be allocated among the 4e expenses in any way; the agent allocated it pro rata to the rental shares: insurance $775, utilities $1,208, repairs $585, cleaning and maintenance $342 (total $2,910). Carryovers in whole dollars, consistent with the whole-dollar Schedule E entries: 7a = $3,973 (4e) − $2,910 (allowed) = $1,063; 7b $7,942. (Cents shown in the worksheet are rounded half-up.)

## The completed Schedule E, Part I (cabin column only)

```
Line A  Payments requiring 1099s in 2025: No (all vendors corporations; no $600 payments to individuals)
Line B  (blank)

                                     A (Blue Ridge cabin)
1a  Address                          [street], Blue Ridge, GA [ZIP]
1b  Type                             3 (Vacation/Short-Term Rental)
2   Fair rental days / Personal / QJV  61 / 19 / no

3   Rents received                   14,335
4   Royalties received                    0
5   Advertising                         215
6   Auto and travel                       0
7   Cleaning and maintenance            342
8   Commissions (platform fee)        1,147
9   Insurance                           775
10  Legal and other professional          0
11  Management fees                       0
12  Mortgage interest (banks)         7,233
13  Other interest                        0
14  Repairs                             585
15  Supplies                              0
16  Taxes                             2,830
17  Utilities                         1,208
18  Depreciation                          0   (limited by Worksheet 5-1; 7,942 carried to 2026)
19  Other                                 0
20  Total expenses                   14,335
21  Income or (loss)                      0
22  Deductible rental RE loss         blank (no loss)

23a 14,335   23b 0   23c 7,233   23d 0   23e 14,335
24  0   25  0   26  0  → Schedule 1, line 5
```

Average stay: 61 nights over 17 bookings = 3.6 days, so this would not be a "rental activity" under the passive rules either, but that question does not matter here: a dwelling unit used as a home is outside the passive rules (Instructions, Other activities). Services: self check-in, linens set out before arrival, turnover cleaning by a cleaning company; no cleaning or linen changes during stays, no meals. The agent flagged the services question for CPA review rather than deciding Schedule C vs E alone (see `../references/passive-loss-and-at-risk.md`); the Okafors' CPA confirmed Schedule E.

## Personal share to Schedule A

- Mortgage interest: $9,486 − $7,233 = $2,253
- Real estate taxes: $3,712 − $2,830 = $882 (inside their SALT total)
- Personal share of insurance, utilities, repairs, cleaning and depreciation: not deductible.

Route to `../../schedule-a/SKILL.md`.

## Validation summary

- Math: line 20 = 215 + 342 + 1,147 + 775 + 7,233 + 585 + 2,830 + 1,208 = 14,335; line 21 = 0; Worksheet 5-1 lines tie (2e + 4f + 6e = line 1 before rounding).
- §280A: personal days 19 > 14 = max(14, 6.1) → home; 61 rental days ≥ 15 → reportable.
- Line 21 not negative for a used-as-home unit with 2e < rent. Pass.
- Attachments: none required for the cabin (depreciation is on property placed in service before 2025, not listed property). Keep Worksheet 5-1 with the records.
- Carry to 2026: Worksheet 5-1 line 7a $1,063, line 7b $7,942, tied to this cabin.

## Sources cited in this draft

- 2025 Instructions for Schedule E: Line 2 (personal use days, 14-day/10% test, fewer than 15 days), Line 3, Line 14, Other activities
- Pub. 527 (2025) ch. 5: Dividing Expenses, Dwelling Unit Used as a Home, Days used for repairs and maintenance, Worksheet 5-1 and instructions (including Line 2b Step 1 $40,000 test and the allocation footnote)
- Pub. 527 (2025) Table 2-2d: 3.636% for later years
- IRC §280A(c)(5), (d)(1), (g)
