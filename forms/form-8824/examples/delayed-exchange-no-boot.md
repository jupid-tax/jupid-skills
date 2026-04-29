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
- **April 22, 2025** — Robert closes the sale of the Austin rental. Buyer pays $475,000 cash. The QI takes the proceeds (after closing costs) into a segregated escrow account. Robert never touches the cash.
  - This is **Line 4** (relinquished transferred): 04/22/2025
- **May 30, 2025** — Robert delivers a written, signed identification notice to the QI listing the San Antonio property as his target replacement (one of the three-property rule — he identifies only one).
  - This is **Line 5** (identification): 05/30/2025
  - Day count: 38 days from Line 4. Within the 45-day window. ✓
- **August 4, 2025** — Closing on the San Antonio rental. Purchase price $475,000. The QI pays from escrow. Title transfers to Robert.
  - This is **Line 6** (received): 08/04/2025
  - Day count: 104 days from Line 4. Within the 180-day window. ✓
- Robert has no mortgage on either property (he paid cash for both).
- Closing costs total: $12,000 (combined relinquished + replacement). The QI paid these out of escrow.

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
| Exchange expenses (paid by QI from escrow) | $12,000 |
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
| 18 | Basis given up + cash paid + net debt assumed + exchange expenses | 133,000 + 0 + 0 + 12,000 | $145,000 |
| 19 | Realized gain (Line 17 − 18) | 475,000 − 145,000 | **$330,000** |
| 20 | Smaller of (Line 15, Line 19), ≥ 0 | min(0, 330,000), ≥ 0 | $0 |
| 21 | Ordinary recapture (§1245) | None — straight-line §1250 | $0 |
| 22 | Recognized gain (Line 21 + max(20−21, 0)) | 0 | **$0** |
| 23 | Recognized gain | = Line 22 | $0 |
| 24 | Deferred gain (Line 19 − 23) | 330,000 − 0 | **$330,000** |
| 25 | Basis of replacement (Line 18 − 15 + 23) | 145,000 − 0 + 0 | **$145,000** |

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
18. Basis given up + cash paid + net debt
    assumed + exchange expenses:               $145,000
19. Realized gain (Line 17 − 18):              $330,000
20. Smaller of Line 15 or 19, ≥ 0:             $0
21. Ordinary income under recapture rules:     $0  (§1250 straight-line — no §1245 recapture)
22. Recognized gain:                           $0
23. Recognized gain:                           $0
24. Deferred gain (Line 19 − 23):              $330,000
25. Basis of replacement (Line 18 − 15 + 23):  $145,000

## Required attachments
- [ ] Form 4797 — not required (no recognized gain this year)
- [ ] Schedule D — not required (no recognized gain this year)
- [ ] State filings: Texas has no state income tax — no state form. (If TX-source replacement was out of state, a state form might be needed.)

## Validation summary
- 45-day check: Day 38 ≤ 45 ✓
- 180-day check: Day 104 ≤ 180 ✓
- Math: all checks passed
- Sanity warnings:
  - Robert's depreciation history of $52,000 carries into the replacement property. When eventually sold, up to $52k will be unrecaptured §1250 gain at 25% rate (plus any new depreciation taken on the replacement before sale).
  - Replacement basis ($145,000) is much lower than FMV ($475,000) — Robert should keep this in mind for future estate planning. A future heir would step up the basis to FMV at death (currently $475k+).

## Next steps
- File Form 8824 attached to 2025 Form 1040
- No estimated tax adjustment required for 2025 (no recognized gain)
- Robert should retain QI exchange agreement, written 45-day identification, both closing statements, and the depreciation schedule from the Austin rental indefinitely (audit window for §1031 effectively never closes — the deferred gain is preserved in basis)
- Reminder: replacement property basis is $145,000. When Robert eventually sells, gain calculation = sale price − $145,000 − any future depreciation taken − new improvements

## Sources cited in this draft
- IRS Form 8824, Rev. 2024-12 (most recent)
- IRS Instructions for Form 8824, Rev. 2024-12
- IRC §1031 (post-TCJA, real-property only)
- IRC §1031(a)(3) (45-day / 180-day deadlines)
- IRC §1031(d) (basis of replacement)
- Treas. Reg. §1.1031(k)-1 (qualified intermediary safe harbor)
- Pub. 544 (Sales and Other Dispositions of Assets)
```

## Why each non-obvious choice

**Why no Form 4797 attachment?** Line 22 = $0. There's no recognized gain to report on Form 4797 this year. The deferred gain is recorded on Form 8824 Line 24 only — it doesn't flow anywhere on the current return.

**Why exchange expenses on Line 18 instead of Line 15?** The $12,000 was paid out of QI escrow (essentially out of the exchange proceeds). Per Form 8824 instructions, exchange expenses paid out of cash received reduce Line 15. But since there was no cash received (all proceeds went straight to replacement purchase), the $12k goes to Line 18 instead — increasing the user's "give" side and thus the basis of replacement.

The IRS instructions allow either treatment, but the Line 18 placement is cleaner here because Line 15 cannot go negative.

**Why does basis carry forward at $145,000 and not $475,000?** The whole point of §1031 deferral is that the user does not pay tax now AND does not get a stepped-up basis. The deferred $330,000 of gain is "stored" in the lower basis. When Robert sells the San Antonio rental at, say, $600,000 in 2030, his gain will be $600k − $145k − any further depreciation = $455k+ (subject to depreciation recapture).

**Why was the QI necessary?** Without the QI, Robert would have been in constructive receipt of the $475k in April when he sold Austin. Even if he then put it back into San Antonio in August, the §1031 deferral would have failed. The QI's role is to hold the funds at arm's length so Robert is never in receipt.

**What if Robert had not been audited?** Audit defense rests on:
1. QI agreement signed before relinquished closing — proves no constructive receipt
2. Written 45-day identification with QI's date stamp — proves timing
3. Both closing statements — prove transaction values
4. Depreciation schedule from Austin — establishes adjusted basis ($133k)
5. Form 8824 with all lines completed — shows the IRS the deferral computation

## What if Robert had received cash boot?

See [`delayed-exchange-with-boot.md`](./delayed-exchange-with-boot.md) for that variant.
