# Example: Delayed Exchange with $50,000 Cash Boot

A common partial-deferral scenario: the user moves to a smaller property and takes some cash off the table. The cash boot, reduced by exchange expenses, is recognized as gain, and most of the depreciation recapture history follows.

## The filer

- **Name**: Diana Patel
- **Property held**: Triplex at 502 Birch Avenue, Portland OR (rental, all three units leased)
- **Replacement**: Single-family rental at 814 Cedar Lane, Eugene OR
- **Tax year**: 2025
- **QI**: Pacific Northwest Exchange Group (independent QI)

## The exchange story

Diana bought the Portland triplex in 2010 for $420,000. Over 15 years she depreciated $190,000 (straight-line MACRS, 27.5-year residential). The Portland market has appreciated significantly; her property is now worth $750,000 with $0 mortgage (paid off in 2022). She wants to scale back — Eugene's market is calmer, and she's targeting an SFH worth $700,000.

Diana wants $50,000 in cash to remodel her own home. She arranges to take $50k at the Portland closing, before the rest of the proceeds go to the QI, rather than rolling the entire amount into replacement. (Taking the cash from the QI after it holds the funds would need to fit the QI agreement's limits on access to exchange funds; see Treas. Reg. §1.1031(k)-1(g)(6) and Pub. 544, "Additional restrictions on safe harbors".)

Timeline:
- **Jan 14, 2025** — Diana signs exchange agreement with Pacific Northwest Exchange Group.
- **Jan 28, 2025** — Diana sells Portland triplex. Buyer pays $750,000 cash. The closing agent sends $700,000 to the QI's segregated escrow, pays $8,000 of closing costs, and wires the remaining $42,000 to Diana at closing.
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
| Cash boot received | $50,000 (gross — $42k to Diana + $8k of closing costs paid from it) |
| Cash boot paid | $0 |
| Debt relieved | $0 |
| Debt assumed | $0 |
| Net mortgage boot | $0 |
| Exchange expenses paid out of boot | $8,000 (Portland closing) |
| Exchange expenses paid out of pocket | $4,000 (Eugene closing) |
| Total exchange expenses | $12,000 (all reduce Line 15, not below zero) |
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
| 15 | Cash received + non-like-kind FMV + net debt relief − all exchange expenses | 50,000 + 0 + 0 − 12,000 | **$38,000** |
| 15a | Description of other property received | "Cash" | — |
| 16 | FMV of like-kind received | — | $700,000 |
| 17 | Line 15 + 16 | 38,000 + 700,000 | $738,000 |
| 18 | Basis given up + net amount paid + exchange expenses not used on Line 15 | 230,000 + 0 + 0 | $230,000 |
| 19 | Realized gain (Line 17 − 18) | 738,000 − 230,000 | **$508,000** |
| 20 | Smaller of (Line 15, Line 19), ≥ 0 | min(38,000, 508,000) | $38,000 |
| 21 | Ordinary income under recapture rules | None — straight-line §1250, no §1245 | $0 |
| 22 | max(Line 20 − Line 21, 0) | 38,000 − 0 | **$38,000** |
| 23 | Recognized gain (Line 21 + Line 22) | 0 + 38,000 | $38,000 |
| 24 | Deferred gain (Line 19 − 23) | 508,000 − 38,000 | **$470,000** |
| 25 | Basis of replacement (Line 18 + 23 − 15) | 230,000 + 38,000 − 38,000 | **$230,000** |
| 25a | Basis of like-kind §1250 property received | All of Line 25 (single-family rental, no §1245 or intangible components) | $230,000 |

Check: Line 16 − Line 24 = 700,000 − 470,000 = 230,000 = Line 25. Realized gain cross-check: 750,000 sale price − 12,000 expenses − 230,000 basis = 508,000.

### Character of the recognized gain ($38,000)

All $38,000 is **unrecaptured §1250 gain** (taxed at up to 25%) because $38,000 ≤ $190,000 of accumulated straight-line depreciation (IRC §1(h)(6)). None is regular long-term capital gain at this point. Reported on:
- Form 4797, line 5 (§1231 gain from like-kind exchanges; the triplex was held more than 1 year)
- Schedule D, via the Unrecaptured Section 1250 Gain Worksheet (line 19), with the 25% maximum rate applied

The remaining $152,000 of accumulated depreciation history ($190k − $38k) carries into the replacement property for future recapture.

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
    less exchange expenses ($8k + $4k):        $38,000
15a. Description of other property received:   Cash
16. FMV of like-kind property received:        $700,000
17. Add lines 15 and 16:                       $738,000
18. Basis given up + net amount paid
    + exchange expenses not used on line 15:   $230,000
19. Realized gain (Line 17 − 18):              $508,000
20. Smaller of Line 15 or 19, ≥ 0:             $38,000  (boot-attributable gain)
21. Ordinary income under recapture rules:     $0       (§1250 straight-line, no §1245)
22. Line 20 − Line 21 (≥ 0):                   $38,000  → Form 4797, line 5
23. Recognized gain (Line 21 + 22):            $38,000
24. Deferred gain (Line 19 − 23):              $470,000
25. Basis of replacement (Line 18 + 23 − 15):  $230,000
25a. Basis of like-kind §1250 property:        $230,000
25b. Basis of §1245/1252/1254/1255 property:   $0
25c. Basis of like-kind intangible property:   $0

## Required attachments
- [x] Form 4797 — required (Line 22 = $38,000 on line 5, business-use real estate held more than 1 year)
- [x] Schedule D + Unrecaptured §1250 Gain Worksheet — required (Form 4797 line 7 gain flows to Schedule D line 11; the recognized gain is unrecaptured §1250)
- [x] State return: Diana reports the $38k recognized gain on her Oregon return as well (both properties are in Oregon)

## Validation summary
- 45-day check: Day 29 ≤ 45 ✓
- 180-day check: Day 92 ≤ 180 ✓
- Math: all checks passed
- Sanity warnings:
  - Recognized gain $38,000 is ALL unrecaptured §1250 gain because Diana's accumulated depreciation ($190k) far exceeds the recognized portion. Maximum federal tax: $38,000 × 25% = $9,500, plus state tax (Oregon).
  - Estimated quarterly tax: Diana should pay an estimated tax payment to cover the recognized gain (and net investment income tax if applicable, though §1031-recognized gain may or may not trigger §1411 NIIT — confirm with CPA).
  - Replacement basis ($230,000) is much lower than FMV ($700,000). Depreciation of the Eugene SFH follows Treas. Reg. §1.168(i)-6 (carryover basis on the triplex's remaining 27.5-year schedule) unless Diana elects out under §1.168(i)-6(i); ask for the land/building split (county assessor ratio or appraisal) rather than assuming one.
  - Diana's depreciation history of $152,000 ($190k − $38k recognized) carries into the replacement. Future sale will recognize that as unrecaptured §1250 gain.

## Next steps
- File Form 8824, Form 4797, and Schedule D with 2025 Form 1040 (no Form 8949 entry for this gain)
- Pay estimated tax on $38k recognized gain (federal up to 25% on unrecaptured §1250 + state)
- Retain QI agreement, identification notice, both closing statements, and depreciation schedules until the period of limitations expires for the year the Eugene property is sold
- Set up the Eugene SFH on Form 4562 under Treas. Reg. §1.168(i)-6 (or the §1.168(i)-6(i) election), total basis $230k less the land allocation

## Sources cited in this draft
- IRS Form 8824 (2025)
- IRS Instructions for Form 8824 (2025), Lines 15, 18, 22
- Form 4797 (2025), line 5
- IRC §1031 (post-TCJA, real-property only)
- IRC §1031(b) (gain to extent of boot)
- IRC §1031(d) (basis of replacement)
- IRC §1(h)(1)(E) (25% rate on unrecaptured §1250 gain)
- Treas. Reg. §1.1031(b)-1 (boot rules)
- Treas. Reg. §1.1031(d)-1 (basis carryover)
- IRC §1(h)(6) (unrecaptured §1250 gain)
- Pub. 544 (Sales and Other Dispositions of Assets), "Exchange expenses"
- Schedule D instructions, Unrecaptured §1250 Gain Worksheet
```

## Why each non-obvious choice

**Why is Line 15 = $38,000 and not $50,000?** Cash boot received was $50,000 gross. The 2025 instructions reduce Line 15 (but not below zero) by "any exchange expenses you incurred", however they were paid: the $8,000 paid from the sale proceeds and the $4,000 Diana paid out of pocket at the Eugene closing. $50,000 − $12,000 = $38,000. Pub. 544 treats closing costs on both the disposition and the acquisition as exchange expenses.

**Why is Line 18 = $230,000 and not $234,000?** Line 18 only picks up exchange expenses "not used on line 15". All $12,000 was absorbed on Line 15, so Line 18 is the adjusted basis alone. Splitting expenses by how they were paid (out of boot vs. out of pocket) would put $4,000 on Line 18 and overstate recognized gain by $4,000.

**Why is the recognized gain entirely unrecaptured §1250 gain?** Under IRC §1(h)(6), gain on depreciable real property is unrecaptured §1250 gain to the extent of the straight-line depreciation taken. Since Diana took straight-line §1250 depreciation only, there's no ordinary recapture on Line 21. Her $38k recognized gain is unrecaptured §1250 gain, taxed at up to 25% federal.

**Why does basis come out to $230,000 (same as Line 18)?** Line 25 = Line 18 + Line 23 − Line 15 = 230 + 38 − 38 = 230. When the recognized gain equals Line 15 (boot was smaller than realized gain), the two cancel and the basis equals Line 18.

**Could Diana have avoided recognizing any gain?** Yes — by reinvesting all of the net proceeds and taking no cash out, for example:
1. Buying a replacement of equal or greater value than the relinquished property net of selling costs ($742,000+), with no cash taken out
2. Buying multiple replacements totaling at least the net proceeds, with no cash taken out

Since Diana wanted the $50k for personal use, partial recognition was the trade-off. The remainder ($470k) is still deferred.

**What if Diana sells the Eugene property in 2030 for $850,000?** Realized gain on that sale = $850k − adjusted basis, where adjusted basis = $230k − further depreciation + new improvements. Of the gain, up to $152k will be unrecaptured §1250 gain (carried-forward depreciation history) plus any new depreciation taken on the Eugene SFH between 2025-2030. The rest is regular long-term capital gain.

**Net investment income tax (NIIT, IRC §1411)?** Diana is single with significant rental income. If her modified AGI exceeds $200,000 (single) in 2025, the recognized $38k may also be subject to 3.8% NIIT — adding $1,444. Confirm with CPA.

## Audit defense

If audited, Diana's defense rests on:
1. QI exchange agreement (Pacific Northwest Exchange Group) signed Jan 14, before Jan 28 closing — proves no constructive receipt
2. Written 45-day identification dated Feb 26 with QI's receipt stamp — proves timing
3. Both closing statements (HUD-1 / ALTA) showing values, fees, and disbursements
4. Depreciation schedule for the Portland triplex from 2010-2024 (15 years × ~$13k/yr = $190k) — establishes basis
5. Form 8824, Form 4797, Schedule D consistency — IRS cross-checks
6. Bank statement showing the $42k wire from the closing agent on Jan 28 — confirms the boot characterization (the other $8k of the $50k boot paid Portland closing costs)
