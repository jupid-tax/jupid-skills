# Example: K-1 Investor (S Corporation Owner-Operator Plus Two Passive Partnerships)

No rental real estate. Part II only. Shows: nonpassive S corporation income with a distribution (column (e), Form 7203), a prior-year basis-limited loss released this year (line 27 "Yes", PYA line), and a passive partnership loss limited by Form 8582 against passive income from another partnership, with a prior-year unallowed passive loss carried on Form 8582. All math checked in Python. Tax year 2025 (filed in 2026).

## The filer

- **Name**: Priya Raman (fictional), single
- **S corporation**: Brightline Fabrication, Inc., 40% shareholder; works there full time (about 2,000 hours) → material participation (Pub. 925 test 1) → nonpassive
- **Partnership 1**: Harbor Street Restaurant Partners LP, limited partner, no hours → passive (limited partners generally do not materially participate)
- **Partnership 2**: Cedar Ridge Storage Partners LP, limited partner, no hours → passive. The K-1 shows an ordinary business activity (self-storage operated with on-site staff); the agent asked the partnership's tax contact whether the K-1 activity is a rental activity and got "trade or business, box 1". Either way it is passive for Priya.
- **Prior-year items** (from her 2024 return and the CPA's carryforward schedule): $2,640 Brightline loss from 2023 disallowed for lack of stock basis, still suspended at the start of 2025; $3,118 Harbor Street passive loss unallowed on her 2024 Form 8582

## K-1 amounts

| Entity | Item | Amount |
|---|---|---|
| Brightline (K-1 1120-S) | Box 1 ordinary business income | $83,417 |
| Brightline | Box 16, code D distributions | $30,000 |
| Harbor Street (K-1 1065) | Box 1 ordinary business loss | ($9,764) |
| Cedar Ridge (K-1 1065) | Box 1 ordinary business income | $5,231 |

Box 14 code A (self-employment) is blank on both partnership K-1s (limited partners), so nothing goes to Schedule SE. S corporation income is not subject to self-employment tax (Instructions for Schedule E).

## Gate 1: S corporation basis (Form 7203 worksheet)

Beginning 2025 stock basis $0; suspended loss carryover $2,640; no shareholder loans. Order per the Instructions for Form 7203 (no §1.1367-1(g) election):

```
Beginning stock basis                      0
+ income (box 1)                      83,417  → 83,417
− distributions (box 16 D)            30,000  → 53,417   (not in excess of basis: no capital gain)
− nondeductible expenses                   0  → 53,417
− losses incl. 2023 carryover          2,640  → 50,777   (carryover fully allowed)
Ending stock basis                    50,777
```

The $2,640 is allowed in 2025 → PYA line in column (i). Column (e) is checked for Brightline because of the distribution and the loss. Attach Form 7203.

## Gate 2: at-risk

No nonrecourse debt or guarantees in either partnership (asked; the partner-share-of-liabilities section of both K-1s shows $0 for Priya). Column (f) not checked.

## Gate 3: passive (Form 8582 worksheet)

Rental real estate is not involved, so there is no special allowance (Part II skipped).

```
Part V (all other passive activities)
  Activity        (a) Net income  (b) Net loss  (c) Prior unallowed  (d) Gain   (e) Loss
  Cedar Ridge          5,231                                          5,231
  Harbor Street                       9,764         3,118                       12,882

Part I   2a  5,231   2b  (9,764)   2c  (3,118)   2d  (7,651)
         1d  0
         3   (7,651)   → line 2d is a loss and 1d is zero: skip Part II, go to line 10
Part III 10  5,231    11  5,231   (total losses allowed)

Part VII Harbor Street: (a) 12,882, ratio 1.00, (c) unallowed = (7,651 − 0) × 1.00 = 7,651
Part VIII Harbor Street: (a) 12,882  (b) unallowed 7,651  (c) allowed 5,231
```

Allowed passive loss for Harbor Street = $5,231 (equal to the passive income). It includes current and prior-year amounts; because the prior-year loss is reported on Form 8582, it is not a separate PYA line (Instructions for Schedule E, Line 27 covers only prior-year passive losses not reported on Form 8582). Carryforward to 2026: $7,651.

## Gate 4: excess business loss

Net business result from these activities is income, not a loss. Form 461 not needed (2025 threshold $313,000 single, Instructions for Form 461).

## The completed Schedule E, Part II

```
27  Reporting prior-year at-risk/basis loss, prior-year passive loss not on Form 8582, or UPE?  Yes

28   (a) Name                                   (b)  (c)  (d) EIN       (e)  (f)
 A   Brightline Fabrication, Inc.                S    -    XX-XXXXXXX    X    -
 B   PYA Brightline Fabrication, Inc.            S    -    XX-XXXXXXX    X    -
 C   Harbor Street Restaurant Partners LP        P    -    XX-XXXXXXX    -    -
 D   Cedar Ridge Storage Partners LP             P    -    XX-XXXXXXX    -    -

       (g) Passive loss  (h) Passive income  (i) Nonpassive loss  (j) §179  (k) Nonpassive income
 A            0                 0                   0                0          83,417
 B            0                 0               2,640                0               0
 C        5,231                 0                   0                0               0
 D            0             5,231                   0                0               0

29a  Totals                     (h) 5,231                                  (k) 83,417
29b  Totals   (g) 5,231                     (i) 2,640     (j) 0
30   Add (h) and (k) of 29a                                   88,648
31   Add (g), (i), (j) of 29b                                 (7,871)
32   Total partnership and S corporation income               80,777
```

Parts I, III, IV: not used (lines 1–26, 33–39 all 0 / blank). Part V:

```
40  Net farm rental income (Form 4835)       0
41  Total income: 0 + 80,777 + 0 + 0 + 0    80,777  → Schedule 1, line 5
42  Farming and fishing reconciliation       0
43  Real estate professional reconciliation  blank (not a real estate professional)
```

## Validation summary

- Math: 30 = 5,231 + 83,417 = 88,648; 31 = 5,231 + 2,640 + 0 = 7,871; 32 = 88,648 − 7,871 = 80,777; 41 = 80,777. Form 8582: line 11 (5,231) = column (g) total.
- Basis: ending stock basis $50,777 ≥ 0; distribution did not exceed basis, so no gain on Form 8949.
- Separate lines: PYA on its own line in column (i); not netted with line A.
- K-1 match: line A column (k) equals Brightline box 1; line C plus the Form 8582 carryforward ($5,231 + $7,651 = $12,882) equals Harbor Street box 1 plus the 2024 carryforward ($9,764 + $3,118).
- Attachments: Form 7203 (Brightline), Form 8582. Not needed: Form 6198, Form 461.
- Carry to 2026: Harbor Street suspended passive loss $7,651. Brightline: no basis carryover.
- Boundary items handed off: QBI from all three K-1s → `../../form-8995/SKILL.md` (Priya's taxable income decides 8995 vs 8995-A; the agent did not compute QBI here). Net investment income tax on passive income: Form 8960, flagged for the return preparer.

## Sources cited in this draft

- 2025 Schedule E page 2; 2025 Instructions for Schedule E: Part II (Basis rules for S corporations, At-risk rules, Passive activity loss rules), Line 27, Line 28, S Corporations
- 2025 Form 8582 and Instructions: Part I line 3 routing, Parts V, VII, VIII; How To Report Allowed Losses (Schedule E, Parts II and III)
- Instructions for Form 7203 (Rev. Dec. 2022): basis ordering; Limitations on Losses order
- 2025 Instructions for Form 461: 2025 threshold amount
- Pub. 925 (2025): material participation tests; limited partners
