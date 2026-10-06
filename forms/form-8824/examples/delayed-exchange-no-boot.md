# Example: Delayed Exchange, Rental SFH for Rental SFH, No Boot, Full Deferral

The canonical "textbook" §1031: a delayed exchange with a Qualified Intermediary, equal values, no debt change, no cash boot. The user defers 100% of the realized gain.

## The filer

- **Name**: Robert Chen
- **Property held**: 3-bedroom single-family rental at 1422 Oak Street, Austin TX
- **Replacement**: 2-bedroom single-family rental at 88 Pinewood Drive, San Antonio TX
- **Tax year**: 2025 (filing Form 8824 in 2026)
- **QI**: Texas Exchange Services, Inc. (independent Qualified Intermediary)

## The exchange story

Robert bought the Austin rental in 2014 for $185,000. Over 11 years he depreciated $52,000 (straight-line MACRS, 27.5-year residential). In April 2025, he decides to consolidate his portfolio in San Antonio where he lives.

Timeline:
- **April 8, 2025** — Robert signs an exchange agreement with Texas Exchange Services. They will act as QI.
- **April 22, 2025** — Robert closes the sale of the Austin rental. Buyer pays $475,000 cash. The QI takes the full $475,000 into a segregated escrow account. Robert never touches the cash.
  - This is **Line 4** (relinquished transferred): 04/22/2025
- **May 30, 2025** — Robert delivers a written, signed identification notice to the QI listing the San Antonio property as his target replacement (one of the three-property rule — he identifies only one).
  - This is **Line 5** (identification): 05/30/2025
  - Day count: 38 days from Line 4. Within the 45-day window. ✓
- **August 4, 2025** — Closing on the San Antonio rental. Purchase price $475,000. The QI pays from escrow. Title transfers to Robert.
  - This is **Line 6** (received): 08/04/2025
  - Day count: 104 days from Line 4. Within the 180-day window. ✓
- Robert has no mortgage on either property (he paid cash for both).
- Closing costs total: $12,000 (combined relinquished + replacement: commissions, title, escrow, recording). Robert paid them from his own funds at the two closings, so the QI's full $475,000 went to the San Antonio purchase.

## Inputs structured

| Item | Value |
|------|-------|
| Adjusted basis of relinquished | $185,000 (cost) − $52,000 (depreciation) = **$133,000** |
| FMV of relinquished at exchange | $475,000 |
| FMV of replacement received | $475,000 |
| Cash boot received | $0 |
| Cash boot paid | $0 |
| Debt on relinquished (assumed by buyer) | $0 |
| Debt on replacement (assumed by Robert) | $0 |
| Net mortgage boot | $0 |
| Exchange expenses (paid by Robert from his own funds) | $12,000 |
| Related party? | No |

## The Form 8824 computation

| Line | Description | Computation | Value |
|------|-------------|-------------|-------|
| 1 | Description of like-kind property given up | "3-bed rental SFH at 1422 Oak Street, Austin TX 78701" | — |
| 2 | Description of like-kind property received | "2-bed rental SFH at 88 Pinewood Drive, San Antonio TX 78201" | — |
| 3 | Date relinquished originally acquired | 06/15/2014 | — |
| 4 | Date relinquished transferred | 04/22/2025 | — |
| 5 | Date replacement identified | 05/30/2025 (38 days after Line 4) | — |
| 6 | Date replacement received | 08/04/2025 (104 days after Line 4) | — |
| 7 | Related-party exchange? | No | — |
| 12 | FMV of OTHER property given up | — | $0 |
| 13 | Basis of OTHER property | — | $0 |
| 14 | (Line 12 − 13) | — | $0 |
| 15 | Boot received: cash + non-like-kind + net debt relief − exchange expenses | 0 + 0 + 0 − 12,000 → floor at 0 | **$0** |
| 16 | FMV of like-kind received | — | $475,000 |
| 17 | Line 15 + Line 16 | 0 + 475,000 | $475,000 |
| 18 | Basis given up + net amount paid + exchange expenses not used on Line 15 | 133,000 + 0 + 12,000 | $145,000 |
| 19 | Realized gain (Line 17 − 18) | 475,000 − 145,000 | **$330,000** |
| 20 | Smaller of (Line 15, Line 19), ≥ 0 | min(0, 330,000), ≥ 0 | $0 |
| 21 | Ordinary recapture (§1245) | None — straight-line §1250 | $0 |
| 22 | max(Line 20 − Line 21, 0) | 0 − 0 | **$0** |
| 23 | Recognized gain (Line 21 + Line 22) | 0 + 0 | $0 |
| 24 | Deferred gain (Line 19 − 23) | 330,000 − 0 | **$330,000** |
| 25 | Basis of replacement (Line 18 + 23 − 15) | 145,000 + 0 − 0 | **$145,000** |
| 25a | Basis of like-kind §1250 property received | All of Line 25 (single-family rental, no §1245 or intangible components; follows the IRS example in the Lines 25a–25c instructions) | $145,000 |

## The completed Form 8824 draft

```markdown
# Form 8824 — DRAFT for tax year 2025

## Header
Name(s) on return: Robert Chen
Identifying number: ***-**-1234

## Part I — Information on the Like-Kind Exchange
1. Description of property given up: 3-bed rental SFH at 1422 Oak Street, Austin TX 78701
2. Description of property received: 2-bed rental SFH at 88 Pinewood Drive, San Antonio TX 78201
3. Date originally acquired:                    06/15/2014
4. Date you transferred property given up:      04/22/2025
5. Date replacement identified:                 05/30/2025  (Day 38 — within 45-day window ✓)
6. Date you received replacement:               08/04/2025  (Day 104 — within 180-day window ✓)
7. Related-party exchange?  No

## Part II — Related-Party Exchange Information
N/A — Line 7 = No

## Part III — Realized Gain, Recognized Gain, and Basis
12. FMV of OTHER property given up:            $0
13. Adjusted basis of OTHER property:          $0
14. Gain/(loss) on OTHER property:             $0
15. Cash + other received + net debt relief
    less exchange expenses (boot):             $0
16. FMV of like-kind property received:        $475,000
17. Add lines 15 and 16:                       $475,000
18. Basis given up + net amount paid
    + exchange expenses not used on line 15:   $145,000
19. Realized gain (Line 17 − 18):              $330,000
20. Smaller of Line 15 or 19, ≥ 0:             $0
21. Ordinary income under recapture rules:     $0  (§1250 straight-line — no §1245 recapture)
22. Line 20 − Line 21 (≥ 0):                   $0
23. Recognized gain (Line 21 + 22):            $0
24. Deferred gain (Line 19 − 23):              $330,000
25. Basis of replacement (Line 18 + 23 − 15):  $145,000
25a. Basis of like-kind §1250 property:        $145,000
25b. Basis of §1245/1252/1254/1255 property:   $0
25c. Basis of like-kind intangible property:   $0

## Required attachments
- [ ] Form 4797 — not required (no recognized gain this year)
- [ ] Schedule D — not required (no recognized gain this year)
- [ ] State filings: Texas has no state income tax — no state form. (If TX-source replacement was out of state, a state form might be needed.)

## Validation summary
- 45-day check: Day 38 ≤ 45 ✓
- 180-day check: Day 104 ≤ 180 ✓
- Math: all checks passed
- Sanity warnings:
  - Robert's depreciation history of $52,000 carries into the replacement property. When eventually sold, up to $52k will be unrecaptured §1250 gain taxed at up to 25% (plus any new depreciation taken on the replacement before sale).
  - Replacement basis ($145,000) is much lower than FMV ($475,000) — Robert should keep this in mind for future estate planning. A future heir would step up the basis to FMV at death (currently $475k+).

## Next steps
- File Form 8824 attached to 2025 Form 1040
- No estimated tax adjustment required for 2025 (no recognized gain)
- Robert should retain the QI exchange agreement, written 45-day identification, both closing statements, and the depreciation schedule from the Austin rental until the period of limitations expires for the year he disposes of the San Antonio property (irs.gov, "How long should I keep records?": records on the old property must be kept as long as those on the new one)
- Depreciation of the San Antonio rental (Form 4562): the carryover part of the $145,000 basis continues on the Austin rental's remaining 27.5-year schedule and any excess basis (for example, capitalized exchange expenses) is treated as newly placed in service, under Treas. Reg. §1.168(i)-6 and the 2025 Form 4562 instructions, unless Robert elects out under §1.168(i)-6(i) on a timely filed return; ask for the land/building split
- Reminder: replacement property basis is $145,000. When Robert eventually sells, gain calculation = sale price − $145,000 − any future depreciation taken − new improvements

## Sources cited in this draft
- IRS Form 8824 (2025)
- IRS Instructions for Form 8824 (2025)
- IRC §1031 (post-TCJA, real-property only)
- IRC §1031(a)(3) (45-day / 180-day deadlines)
- IRC §1031(d) (basis of replacement)
- Treas. Reg. §1.1031(k)-1 (qualified intermediary safe harbor)
- Pub. 544 (Sales and Other Dispositions of Assets)
```

## Why each non-obvious choice

**Why no Form 4797 attachment?** Line 22 = $0. There's no recognized gain to report on Form 4797 this year. The deferred gain is recorded on Form 8824 Line 24 only — it doesn't flow anywhere on the current return.

**Why exchange expenses on Line 18 instead of Line 15?** The instructions reduce Line 15 by all exchange expenses, but never below zero. Robert received no cash, other property, or net debt relief, so Line 15 is $0 before expenses and none of the $12,000 can be used there. The instructions put expenses "not used on line 15" on Line 18, which increases the "give" side and the basis of the replacement.

**Why does basis carry forward at $145,000 and not $475,000?** The whole point of §1031 deferral is that the user does not pay tax now AND does not get a stepped-up basis. The deferred $330,000 of gain is "stored" in the lower basis. When Robert sells the San Antonio rental at, say, $600,000 in 2030, his gain will be $600k − $145k − any further depreciation = $455k+ (subject to depreciation recapture).

**Why was the QI necessary?** Without the QI, Robert would have been in constructive receipt of the $475k in April when he sold Austin. Even if he then put it back into San Antonio in August, the §1031 deferral would have failed. The QI's role is to hold the funds at arm's length so Robert is never in receipt.

**What if Robert is audited?** Audit defense rests on:
1. QI agreement signed before relinquished closing — proves no constructive receipt
2. Written 45-day identification with QI's date stamp — proves timing
3. Both closing statements — prove transaction values
4. Depreciation schedule from Austin — establishes adjusted basis ($133k)
5. Form 8824 with all lines completed — shows the IRS the deferral computation

## What if Robert had received cash boot?

See [`delayed-exchange-with-boot.md`](./delayed-exchange-with-boot.md) for that variant.
