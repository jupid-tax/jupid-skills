# Example: Reverse Exchange via Exchange Accommodation Titleholder

A reverse §1031 exchange under the Rev. Proc. 2000-37 safe harbor: the user closes on the replacement property BEFORE selling the relinquished property. An Exchange Accommodation Titleholder (EAT) parks title to the replacement until the user disposes of the relinquished property.

This pattern is used when (a) the user finds the perfect replacement and doesn't want to lose it before their relinquished property sells, or (b) the relinquished property hasn't sold yet but the user is committed to the new acquisition.

## The filer

- **Name**: Marcus Williams
- **Property held**: 4-unit apartment building at 220 Riverside Avenue, Brooklyn NY (rental, fully occupied)
- **Replacement**: 6-unit apartment building at 144 Lakefront Drive, Hoboken NJ
- **Tax year**: 2025
- **EAT**: Atlantic Title Holdings LLC (independent EAT, established under Rev. Proc. 2000-37)
- **QI**: Same parent firm, separate entity (Atlantic Exchange Services LLC)

## The exchange story

Marcus has been hunting for a larger building. In late February 2025, he finds a 6-unit in Hoboken at $1,800,000 — but the seller wants to close in 30 days, and Marcus's Brooklyn building hasn't sold yet (he hasn't even listed it).

Marcus structures a **reverse exchange**:
1. Atlantic Title Holdings LLC (the EAT) acquires the Hoboken building on March 25, 2025
2. EAT holds title under a written Qualified Exchange Accommodation Agreement (QEAA) per Rev. Proc. 2000-37, as modified by Rev. Proc. 2004-51 (the agreement must be signed no later than 5 business days after the EAT takes title)
3. Marcus has 45 days (from 03/25) to identify the property to be relinquished — he identifies his Brooklyn building on April 5
4. Marcus has 180 days (from 03/25) to complete the transfers, and Hoboken may not sit with the EAT for more than 180 days in total
5. Brooklyn closes on July 18, 2025; QI receives proceeds; EAT conveys Hoboken title to Marcus on the same day in a swap

Timeline:
- **March 1, 2025** — Marcus signs Qualified Exchange Accommodation Agreement (QEAA) with Atlantic Title Holdings (the EAT) and exchange agreement with Atlantic Exchange Services (the QI). EAT will buy and hold Hoboken; QI will handle the eventual swap.
- **March 25, 2025** — EAT closes on the Hoboken purchase. EAT pays $1,800,000: a $700,000 mortgage loan from Marcus's lender (made to the EAT, guaranteed by Marcus) plus a $1,100,000 advance from Marcus to the EAT. EAT holds title. Marcus did not own Hoboken in the 180 days before the EAT acquired it (Rev. Proc. 2004-51).
  - **EAT acquisition date**: 03/25/2025 (this starts the reverse-exchange clocks)
- **April 5, 2025** — Marcus delivers written identification to the QI: the property to be relinquished is 220 Riverside Avenue, Brooklyn NY.
  - Identification date: 04/05/2025 (Day 11 — within reverse 45-day window ✓)
- **June 30, 2025** — Marcus lists the Brooklyn building.
- **July 18, 2025** — Brooklyn closes for $1,200,000: the buyer assumes the $400,000 mortgage and pays $800,000 cash to the QI. The QI pays the $800,000 to the EAT to acquire Hoboken for Marcus, the EAT uses it to repay $800,000 of Marcus's advance, and the EAT conveys Hoboken title to Marcus subject to the $700,000 mortgage. Marcus has now "exchanged" — and for tax reporting, **Line 4 (relinquished transferred) is 07/18/2025**.
  - Day count from EAT acquisition (03/25) to relinquished disposition (07/18): 115 days — within reverse 180-day window ✓
- Net result: Marcus took on the $700,000 Hoboken mortgage, was relieved of the $400,000 Brooklyn mortgage, and is out $300,000 of his own cash ($1,100,000 advanced − $800,000 repaid). Sources for Hoboken: $700,000 loan + $800,000 Brooklyn equity + $300,000 Marcus cash = $1,800,000.

## Inputs structured

| Item | Value |
|------|-------|
| Adjusted basis of relinquished (Brooklyn) | $1,200,000 cost − $380,000 depreciation = **$820,000** |
| FMV of relinquished | $1,200,000 |
| FMV of replacement (Hoboken) | $1,800,000 |
| Cash boot received | $0 (Marcus put cash IN, not out) |
| Cash boot paid | $300,000 (Marcus's net cash into Hoboken) |
| Debt relieved (Brooklyn mortgage assumed by buyer) | $400,000 |
| Debt assumed (Hoboken mortgage) | $700,000 |
| Net liabilities assumed by other party (Line 15) | max(0, 400k − (700k + 300k)) = **$0** |
| Net amount paid (Line 18) | (700k + 300k) − 400k = $600,000 |
| Exchange expenses paid by Marcus | $32,000 (out of pocket — EAT and QI fees, broker, escrow, etc.) |
| Related party? | No (EAT is independent under Rev. Proc. 2000-37) |
| Depreciation taken on Brooklyn | $380,000 (straight-line §1250) |

## The computation

| Line | Description | Computation | Value |
|------|-------------|-------------|-------|
| 12-14 | Other (non-like-kind) property given up | None | $0 |
| 15 | Cash received + non-like-kind FMV + net liabilities assumed by other party − exchange expenses (not below 0) | 0 + 0 + 0 − 32,000 → floor at 0 | **$0** |
| 16 | FMV of like-kind received (Hoboken) | — | $1,800,000 |
| 17 | Line 15 + 16 | 0 + 1,800,000 | $1,800,000 |
| 18 | Basis given up + net amount paid + exchange expenses not used on Line 15 | 820,000 + 600,000 + 32,000 | $1,452,000 |
| 19 | Realized gain (Line 17 − 18) | 1,800,000 − 1,452,000 | **$348,000** |
| 20 | Smaller of (15, 19), ≥ 0 | min(0, 348,000) | $0 |
| 21 | Ordinary recapture | None — straight-line §1250 | $0 |
| 22 | max(Line 20 − Line 21, 0) | 0 − 0 | $0 |
| 23 | Recognized gain (Line 21 + 22) | 0 + 0 | $0 |
| 24 | Deferred gain (Line 19 − 23) | 348,000 − 0 | **$348,000** |
| 25 | Basis of replacement (Line 18 + 23 − 15) | 1,452,000 + 0 − 0 | **$1,452,000** |
| 25a | Basis of like-kind §1250 property received | All of Line 25 (apartment building, no §1245 or intangible components; follows the IRS example in the Lines 25a–25c instructions) | $1,452,000 |

Checks: Line 16 − Line 24 = 1,800,000 − 348,000 = 1,452,000 = Line 25. Realized gain cross-check: $1,200,000 Brooklyn value − $32,000 expenses − $820,000 basis = $348,000.

Marcus received no cash and no net debt relief (the $400k Brooklyn mortgage is more than covered by the $700k Hoboken mortgage and his $300k cash), so Line 15 is $0 and the full $348,000 realized gain is deferred. His Hoboken basis is $1,452,000, which is $348,000 below its FMV of $1,800,000.

## The completed Form 8824 draft

```markdown
# Form 8824 — DRAFT for tax year 2025

## Header
Name(s) on return: Marcus Williams
Identifying number: ***-**-9012

## Part I — Information on the Like-Kind Exchange
1. Description of property given up: 4-unit rental at 220 Riverside Avenue, Brooklyn NY 11201
2. Description of property received: 6-unit rental at 144 Lakefront Drive, Hoboken NJ 07030
3. Date originally acquired (Brooklyn):         05/22/2008
4. Date you transferred property given up:      07/18/2025
5. Date replacement identified:                 07/18/2025
   (Note: the replacement was received within 45 days after Line 4, so under the Line 5 instructions it is treated as identified and the receipt date is entered. Keep the 04/05/2025 Rev. Proc. 2000-37 identification of the relinquished property, Day 11 from the EAT's 03/25/2025 acquisition, in the file.)
6. Date you actually received replacement:      07/18/2025
   (Note: in a reverse exchange, "received" is the date EAT conveys to user; same as Line 4 here)
7. Related-party exchange?  No

## Part II — Related-Party
N/A

## Part III — Realized Gain, Recognized Gain, and Basis
12. FMV of OTHER property given up:            $0
13. Adjusted basis of OTHER property:          $0
14. Gain/(loss) on OTHER property:             $0
15. Cash + other received + net liabilities
    assumed by other party, less exchange
    expenses (not below 0):                    $0
15a. Description of other property received:   None
16. FMV of like-kind property received:        $1,800,000
17. Add lines 15 and 16:                       $1,800,000
18. Basis given up ($820k) + net amount paid
    ($600k) + exchange expenses not used on
    line 15 ($32k):                            $1,452,000
19. Realized gain/(loss) (Line 17 − 18):       $348,000
20. Smaller of Line 15 or 19, ≥ 0:             $0
21. Ordinary income under recapture rules:     $0
22. Line 20 − Line 21 (≥ 0):                   $0
23. Recognized gain (Line 21 + 22):            $0
24. Deferred gain/(loss) (Line 19 − 23):       $348,000
25. Basis of replacement (Line 18 + 23 − 15):  $1,452,000
25a. Basis of like-kind §1250 property:        $1,452,000
25b. Basis of §1245/1252/1254/1255 property:   $0
25c. Basis of like-kind intangible property:   $0

## Required attachments
- [ ] Form 4797 — not required this year (no recognized gain or loss)
- [ ] Schedule D — not required this year
- [ ] State filings:
  - NY: Marcus's Brooklyn relinquished property is NY-source. Verify NY treatment with the NY Department of Taxation and Finance.
  - NJ: Hoboken replacement is NJ-source going forward.
  - This skill does not cover NY or NJ rules on out-of-state replacement property or later sales; ask a preparer who handles both states.
- [ ] Reverse-exchange specific records to retain (not filed):
  - Qualified Exchange Accommodation Agreement (QEAA) with EAT
  - Settlement statements from EAT's acquisition (03/25/2025)
  - Settlement statement from Marcus's relinquished sale (07/18/2025)
  - Settlement statement from EAT's conveyance to Marcus (07/18/2025)
  - Loan documents showing Marcus's mortgage assumption from EAT
  - Identification notice dated 04/05/2025

## Validation summary
- Reverse 45-day check: identification on Day 11 ≤ 45 (from EAT acquisition 03/25) ✓
- Reverse 180-day check: relinquished disposed and Hoboken conveyed on Day 115 ≤ 180 (from EAT acquisition 03/25); Hoboken held by the EAT 115 days in total ✓
- QEAA signed 03/01/2025, before the EAT took title (deadline: 5 business days after) ✓
- Math: all checks passed
- Sanity warnings:
  - Realized gain of $348,000 is fully deferred: no cash or net debt relief came back to Marcus. The gain is carried in Hoboken's basis (Line 25 = $1,452,000 vs. FMV $1,800,000).
  - Marcus's depreciation history of $380,000 from Brooklyn carries into Hoboken's basis. On a future sale, up to $380k could be unrecaptured §1250 gain (plus any new depreciation taken on Hoboken before sale).
  - The QEAA must satisfy the Rev. Proc. 2000-37 safe harbor: written agreement within 5 business days, 45-day identification, 180-day limits, and an EAT that holds qualified indications of ownership, is not Marcus or a disqualified person, and is subject to federal income tax (Pub. 544 (2025), "Exchange accommodation titleholder (EAT)"). Marcus should confirm Atlantic Title Holdings meets these.
  - Loan structure: the Hoboken mortgage was originally on EAT, then assumed by Marcus. Lender consent and assumption documents must be in order.

## Next steps
- File Form 8824 with 2025 Form 1040
- No estimated tax adjustment for the exchange (no recognized gain)
- Set up Hoboken on Form 4562 under Treas. Reg. §1.168(i)-6: the carryover basis continues on Brooklyn's remaining 27.5-year schedule and the excess basis (the $600k net paid plus capitalized expenses) is treated as newly placed in service, unless Marcus elects out under §1.168(i)-6(i) on a timely filed return (2025 Instructions for Form 4562); total basis $1,452,000 less the land allocation
- No §1031(f) 2-year rule applies (not a related-party exchange). A quick resale can undercut the "held for investment" requirement; Marcus should talk to a CPA before any sale
- Retain all QEAA, EAT settlement statements, and loan documents until the period of limitations expires for the year Hoboken is sold

## Sources cited in this draft
- IRS Form 8824 (2025)
- IRS Instructions for Form 8824 (2025), Lines 5, 15, 18, and "Exchanges Using a QEAA"
- IRC §1031 (post-TCJA, real-property only)
- IRC §1031(b) (gain recognized only to the extent of boot)
- IRC §1031(d) (basis of replacement)
- Rev. Proc. 2000-37 (reverse exchange safe harbor)
- Rev. Proc. 2004-51 (modifications to Rev. Proc. 2000-37)
- Treas. Reg. §1.1031(k)-1 (general §1031 deferred-exchange rules)
- Treas. Reg. §1.168(i)-6 (depreciation of replacement property)
- Pub. 544 (2025) (Sales and Other Dispositions of Assets), "Like-Kind Exchanges Using Qualified Exchange Accommodation Arrangements"
```

## Why each non-obvious choice

**Why does the EAT qualify?** Under Rev. Proc. 2000-37 (as summarized in Pub. 544 (2025)) the EAT must:
- Hold qualified indications of ownership (legal title, other beneficial ownership indications, or interests in a disregarded entity that holds title) from acquisition until transfer
- Be someone other than the taxpayer or a disqualified person
- Be subject to federal income tax (if a partnership or S corporation, more than 90% of its interests owned by partners or shareholders subject to federal income tax)

The safe harbor does not require the EAT to bear economic risk: the user may lend to or guarantee for the EAT, lease or manage the property, and the arrangements need not be at arm's length (Rev. Proc. 2000-37, sec. 4.03 "Permissible Agreements"; Pub. 544, "Other permissible arrangements"). That is why Marcus's $1,100,000 advance and loan guarantee do not break it.

Atlantic Title Holdings LLC is a single-member LLC owned by the exchange firm's taxable parent, formed to hold reverse-exchange properties for clients. Its owner is not Marcus or a disqualified person (exchange services alone do not make a firm Marcus's agent, Treas. Reg. §1.1031(k)-1(k)(2)).

**Why does Line 5 show 07/18/2025 and not the 04/05/2025 identification?** Form 8824 line 5 asks when the property *received* was identified. The Line 5 instructions say that if the replacement was received before the end of the 45-day period after Line 4, it is treated as identified and the receipt date goes on line 5. Here the receipt date equals Line 4. The reverse-exchange identification under Rev. Proc. 2000-37 runs the other way: Marcus identified the property to be *relinquished* within 45 days of the EAT's acquisition (04/05/2025, Day 11), and the 180-day clock also runs from the EAT acquisition. Keep that notice in the file. The instructions do not address reverse exchanges directly, so confirm the Line 5 entry with the user's preparer.

**Why are Line 4 and Line 6 the same date (07/18/2025)?** In the reverse-exchange swap on the closing day, the relinquished is sold AND the EAT conveys the replacement to Marcus simultaneously. The form requires both dates; in practice they're often the same.

**Why is Marcus's $300k net cash on Line 18 and not netted against Line 15?** Cash paid by the user is part of the "net amount paid" on Line 18, together with the $300k of extra debt he took on (2025 instructions, Line 18). Cash paid can offset debt relief, but Marcus had no net debt relief and received no cash, so Line 15 is $0 either way.

**Why is no gain recognized?** IRC §1031(b) recognizes gain only to the extent of boot received. Marcus traded up in value and debt and took no cash out, so there is no boot and the whole $348,000 is deferred.

**Why are the $32,000 of exchange expenses on Line 18?** The instructions reduce Line 15 by exchange expenses, but not below zero. Line 15 was already $0, so all $32,000 is "not used on line 15" and goes on Line 18, raising Hoboken's basis.

**What if Marcus needs cash later from the deferral?** He can refinance Hoboken (cash-out refi, taking equity out as a loan, NOT a sale). Loan proceeds aren't taxable. There is no safe-harbor waiting period: a refinance arranged as part of the exchange can be treated as cash received, so have a CPA review the timing.

**What if Marcus dies before selling Hoboken?** His heirs generally take a basis equal to FMV at death (IRC §1014). The $348k deferred gain and the $380k depreciation history are not taxed to them. (This is the "swap till you drop" estate planning strategy.)

## Audit defense

Reverse exchanges face heightened IRS scrutiny because of the EAT structure. Marcus's defense:
1. QEAA signed before EAT acquisition (within the 5-business-day limit) — shows the Rev. Proc. 2000-37 safe harbor applies
2. EAT's HUD-1 from 03/25/2025 — proves EAT (not Marcus) acquired Hoboken
3. Evidence that the EAT (or its owner) is subject to federal income tax and is not Marcus or a disqualified person
4. Identification notice dated 04/05/2025 — within the 45-day window
5. Brooklyn closing on 07/18/2025 — within the 180-day window
6. Loan assumption documents from lender — proves clean transfer of mortgage
7. Form 8824 with all dates and computations
8. Depreciation schedule for Brooklyn (2008-2024) — establishes adjusted basis ($820k)

Reverse exchanges that fall outside the Rev. Proc. 2000-37 safe harbor (e.g., EAT held title for >180 days, EAT was a related party, no QEAA) can still potentially qualify for §1031 under common-law principles, but the burden is on the taxpayer and audit risk is high. The safe harbor exists to make these exchanges defensible.
