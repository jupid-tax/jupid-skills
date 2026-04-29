# Example: Delayed Exchange with $50,000 Cash Boot

A common partial-deferral scenario: the user moves to a smaller property and takes some cash off the table. The cash boot is recognized as gain to the extent of realized gain, and most of the depreciation recapture history follows.

## The filer

- **Name**: Diana Patel
- **Property held**: Triplex at 502 Birch Avenue, Portland OR (rental, all three units leased)
- **Replacement**: Single-family rental at 814 Cedar Lane, Eugene OR
- **Tax year**: 2025
- **QI**: Pacific Northwest Exchange Group (independent QI)

## The exchange story

Diana bought the Portland triplex in 2010 for $420,000. Over 15 years she depreciated $190,000 (straight-line MACRS, 27.5-year residential). The Portland market has appreciated significantly; her property is now worth $750,000 with $0 mortgage (paid off in 2022). She wants to scale back — Eugene's market is calmer, and she's targeting an SFH worth $700,000.

Diana wants $50,000 in cash to remodel her own home. She negotiates with the QI to receive $50k from the exchange proceeds rather than rolling the entire amount into replacement.

Timeline:
- **Jan 14, 2025** — Diana signs exchange agreement with Pacific Northwest Exchange Group.
- **Jan 28, 2025** — Diana sells Portland triplex. Buyer pays $750,000 cash. The QI takes $700,000 into the segregated escrow, and (after closing costs) wires $42,000 to Diana on the same day. Closing costs of $8,000 came out of the cash boot allocation.
  - **Line 4** (relinquished transferred): 01/28/2025
- **Feb 26, 2025** — Diana delivers written, signed identification of the Eugene SFH to the QI.
  - **Line 5** (identification): 02/26/2025 (Day 29 — within 45-day window ✓)
- **April 30, 2025** — Closing on Eugene SFH at $700,000 purchase price. QI pays from escrow. Closing costs of $4,000 paid out of pocket by Diana.
  - **Line 6** (replacement received): 04/30/2025 (Day 92 — within 180-day window ✓)

Diana now has $42,000 in her bank account from the exchange (plus she absorbed $4k of out-of-pocket closing costs at the replacement closing).

## Inputs structured

| Item | Value |
|------|-------|
| Adjusted basis of relinquished | $420,000 − $190,000 = **$230,000** |
| FMV of relinquished | $750,000 |
| FMV of replacement received | $700,000 |
| Cash boot received | $50,000 (gross — $42k to Diana + $8k absorbed in QI fees) |
| Cash boot paid | $0 |
| Debt relieved | $0 |
| Debt assumed | $0 |
| Net mortgage boot | $0 |
| Exchange expenses paid out of boot | $8,000 |
| Exchange expenses paid out of pocket | $4,000 (added to Line 18) |
| Related party? | No |
| Depreciation taken on relinquished | $190,000 (all straight-line §1250) |

## The computation

| Line | Description | Computation | Value |
|------|-------------|-------------|-------|
| 1 | Property given up | "Triplex at 502 Birch Avenue, Portland OR 97214" | — |
| 2 | Property received | "SFH rental at 814 Cedar Lane, Eugene OR 97401" | — |
| 3 | Date originally acquired | 03/10/2010 | — |
| 4 | Date relinquished transferred | 01/28/2025 | — |
| 5 | Date replacement identified | 02/26/2025 (Day 29) | — |
| 6 | Date replacement received | 04/30/2025 (Day 92) | — |
| 7 | Related-party? | No | — |
| 12-14 | Other (non-like-kind) property | None | $0 |
| 15 | Cash received + non-like-kind FMV + net debt relief − exchange expenses out of boot | 50,000 + 0 + 0 − 8,000 | **$42,000** |
| 16 | FMV of like-kind received | — | $700,000 |
| 17 | Line 15 + 16 | 42,000 + 700,000 | $742,000 |
| 18 | Basis given up + cash paid + net debt assumed + exchange expenses out of pocket | 230,000 + 0 + 0 + 4,000 | $234,000 |
| 19 | Realized gain (Line 17 − 18) | 742,000 − 234,000 | **$508,000** |
| 20 | Smaller of (Line 15, Line 19), ≥ 0 | min(42,000, 508,000) | $42,000 |
| 21 | §1245 ordinary recapture | None — straight-line §1250, no §1245 | $0 |
| 22 | Recognized gain (Line 21 + max(20−21, 0)) | 0 + 42,000 | **$42,000** |
| 23 | = Line 22 | — | $42,000 |
| 24 | Deferred gain (Line 19 − 23) | 508,000 − 42,000 | **$466,000** |
| 25 | Basis of replacement (Line 18 − 15 + 23) | 234,000 − 42,000 + 42,000 | **$234,000** |

### Character of the recognized gain ($42,000)

All $42,000 is **unrecaptured §1250 gain** (taxed at up to 25%) because $42,000 ≤ $190,000 of accumulated depreciation. None is regular long-term capital gain at this point. Reported on:
- Form 4797 Part I or III as appropriate
- Schedule D's Unrecaptured §1250 Gain Worksheet line, with the 25% maximum rate applied

The remaining $148,000 of accumulated depreciation history ($190k − $42k) carries into the replacement property for future recapture.

## The completed Form 8824 draft

```markdown
# Form 8824 — DRAFT for tax year 2025

## Header
Name(s) on return: Diana Patel
Identifying number: ***-**-5678

## Part I — Information on the Like-Kind Exchange
1. Description of property given up: Triplex at 502 Birch Avenue, Portland OR 97214
2. Description of property received: SFH rental at 814 Cedar Lane, Eugene OR 97401
3. Date originally acquired:                    03/10/2010
4. Date you transferred property given up:      01/28/2025
5. Date replacement identified:                 02/26/2025  (Day 29 — within 45-day window ✓)
6. Date you received replacement:               04/30/2025  (Day 92 — within 180-day window ✓)
7. Related-party exchange?  No

## Part II — Related-Party
N/A

## Part III — Realized Gain, Recognized Gain, and Basis
12. FMV of OTHER property given up:            $0
13. Adjusted basis of OTHER property:          $0
14. Gain/(loss) on OTHER property:             $0
15. Cash + other received + net debt relief
    less exchange expenses paid out of boot:   $42,000
16. FMV of like-kind property received:        $700,000
17. Add lines 15 and 16:                       $742,000
18. Basis given up + cash paid + net debt
    assumed + exchange expenses out-of-pocket: $234,000
19. Realized gain (Line 17 − 18):              $508,000
20. Smaller of Line 15 or 19, ≥ 0:             $42,000  (boot-attributable gain)
21. Ordinary income under recapture rules:     $0       (§1250 straight-line, no §1245)
22. Recognized gain:                           $42,000  → Form 4797
23. Recognized gain:                           $42,000
24. Deferred gain (Line 19 − 23):              $466,000
25. Basis of replacement (Line 18 − 15 + 23):  $234,000

## Required attachments
- [x] Form 4797 — required (Line 22 = $42,000 from business-use real estate)
- [x] Schedule D + Unrecaptured §1250 Gain Worksheet — required (recognized gain is unrecaptured §1250)
- [x] State return: Oregon conforms to §1031 federally; Diana reports the $42k recognized gain on her Oregon return as well

## Validation summary
- 45-day check: Day 29 ≤ 45 ✓
- 180-day check: Day 92 ≤ 180 ✓
- Math: all checks passed
- Sanity warnings:
  - Recognized gain $42,000 is ALL unrecaptured §1250 gain because Diana's accumulated depreciation ($190k) far exceeds the recognized portion. Maximum federal tax: $42,000 × 25% = $10,500, plus state tax (Oregon).
  - Estimated quarterly tax: Diana should pay an estimated tax payment to cover the recognized gain (and net investment income tax if applicable, though §1031-recognized gain may or may not trigger §1411 NIIT — confirm with CPA).
  - Replacement basis ($234,000) is much lower than FMV ($700,000). Diana's depreciation on the replacement starts from $234,000 less land value (typically allocated 80/20 building/land for SFH).
  - Diana's depreciation history of $148,000 ($190k − $42k recognized) carries into the replacement. Future sale will recognize that as unrecaptured §1250 gain.

## Next steps
- File Form 8824, Form 4797, Schedule D, Form 8949 with 2025 Form 1040
- Pay estimated tax on $42k recognized gain (federal 25% on unrecaptured §1250 + state)
- Retain QI agreement, identification notice, both closing statements, depreciation schedules indefinitely
- Set up new depreciation schedule for Eugene SFH starting May 2025: basis $234k less land allocation, residential MACRS 27.5-year SL

## Sources cited in this draft
- IRS Form 8824, current revision
- IRS Instructions for Form 8824
- IRC §1031 (post-TCJA, real-property only)
- IRC §1031(b) (gain to extent of boot)
- IRC §1031(d) (basis of replacement)
- IRC §1(h)(1)(E) (25% rate on unrecaptured §1250 gain)
- Treas. Reg. §1.1031(b)-1 (boot rules)
- Treas. Reg. §1.1031(d)-1 (basis carryover)
- Pub. 544 (Sales and Other Dispositions of Assets)
- Schedule D instructions, Unrecaptured §1250 Gain Worksheet
```

## Why each non-obvious choice

**Why is Line 15 = $42,000 and not $50,000?** Cash boot received was $50,000 gross, but $8,000 of QI/escrow fees were paid out of those proceeds. The Form 8824 Line 15 instruction allows exchange expenses to reduce boot received when paid out of boot. Net cash boot = $42,000.

**Why is Line 18 = $234,000 and not $230,000?** Diana paid $4,000 in closing costs out of pocket at the Eugene closing (not from QI escrow). Per Form 8824 instructions, exchange expenses paid out of pocket increase the "give" side: Line 18 = adjusted basis ($230k) + out-of-pocket expenses ($4k) = $234k.

**Why is the recognized gain entirely unrecaptured §1250 gain?** Per IRC §1031 and Treas. Reg. §1.1031(d)-2, when the relinquished property had depreciation taken, the boot-attributable recognized gain is characterized first as recapture (§1245 ordinary if applicable, then unrecaptured §1250). Since Diana took straight-line §1250 depreciation only, there's no §1245 ordinary component. Her $42k recognized gain is unrecaptured §1250 capital, taxed at up to 25% federal.

**Why does basis come out to $234,000 (same as Line 18)?** Algebraic coincidence in this case: Line 25 = Line 18 + Line 23 − Line 15 = 234 + 42 − 42 = 234. The cash boot received exactly equals the recognized gain, so they cancel out.

**Could Diana have avoided recognizing any gain?** Yes — by either:
1. Buying a replacement of equal or greater value than relinquished ($750,000+), with no cash taken out
2. Buying multiple replacements totaling $700k+ and not taking cash out

Since Diana wanted the $50k for personal use, partial recognition was the trade-off. The remainder ($466k) is still deferred.

**What if Diana sells the Eugene property in 2030 for $850,000?** Realized gain on that sale = 850k − 234k − any further depreciation taken − any new improvements. Of that, up to $148k will be unrecaptured §1250 gain (carried-forward depreciation history) plus any new depreciation taken on the Eugene SFH between 2025-2030. The rest is regular long-term capital gain.

**Net investment income tax (NIIT, IRC §1411)?** Diana is single with significant rental income. If her modified AGI exceeds $200,000 (single) in 2025, the recognized $42k may also be subject to 3.8% NIIT — adding $1,596. Confirm with CPA.

## Audit defense

If audited, Diana's defense rests on:
1. QI exchange agreement (Pacific Northwest Exchange Group) signed Jan 14, before Jan 28 closing — proves no constructive receipt
2. Written 45-day identification dated Feb 26 with QI's receipt stamp — proves timing
3. Both closing statements (HUD-1 / ALTA) showing values, fees, and disbursements
4. Depreciation schedule for the Portland triplex from 2010-2024 (15 years × ~$13k/yr = $190k) — establishes basis
5. Form 8824, Form 4797, Schedule D consistency — IRS cross-checks
6. Bank statement showing the $42k wire from QI on Jan 28 — confirms the boot characterization
