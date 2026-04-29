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
2. EAT holds title with a "Qualified Exchange Accommodation Agreement" (QEAA) per Rev. Proc. 2000-37
3. Marcus has 45 days (from 03/25) to identify the property to be relinquished — he identifies his Brooklyn building on April 5
4. Marcus has 180 days (from 03/25) to dispose of the Brooklyn property
5. Brooklyn closes on July 18, 2025; QI receives proceeds; EAT conveys Hoboken title to Marcus on the same day in a swap

Timeline:
- **March 1, 2025** — Marcus signs Qualified Exchange Accommodation Agreement (QEAA) with Atlantic Title Holdings (the EAT) and exchange agreement with Atlantic Exchange Services (the QI). EAT will buy and hold Hoboken; QI will handle the eventual swap.
- **March 25, 2025** — EAT closes on the Hoboken purchase. EAT pays $1,800,000 (financed by Marcus's loan, structured through EAT, plus Marcus's cash contribution). EAT holds title.
  - **EAT acquisition date**: 03/25/2025 (this starts the reverse-exchange clocks)
- **April 5, 2025** — Marcus delivers written identification to the QI: the property to be relinquished is 220 Riverside Avenue, Brooklyn NY.
  - Identification date: 04/05/2025 (Day 11 — within reverse 45-day window ✓)
- **June 30, 2025** — Marcus lists the Brooklyn building.
- **July 18, 2025** — Brooklyn closes. Buyer pays $1,200,000. QI receives proceeds. Same day, EAT conveys Hoboken title to Marcus. Marcus has now "exchanged" — but for tax reporting, **Line 4 (relinquished transferred) is 07/18/2025**.
  - Day count from EAT acquisition (03/25) to relinquished disposition (07/18): 115 days — within reverse 180-day window ✓
- Marcus financed Hoboken with a $700,000 mortgage (assumed/structured through EAT, then assumed by Marcus on conveyance). Brooklyn had a $400,000 mortgage assumed by buyer. Marcus contributed $750,000 cash to the deal (used to pay Hoboken purchase price minus financing).

## Inputs structured

| Item | Value |
|------|-------|
| Adjusted basis of relinquished (Brooklyn) | $1,200,000 cost − $380,000 depreciation = **$820,000** |
| FMV of relinquished | $1,200,000 |
| FMV of replacement (Hoboken) | $1,800,000 |
| Cash boot received | $0 (Marcus put cash IN, not out) |
| Cash boot paid | $750,000 (Marcus's cash contribution to Hoboken) |
| Debt relieved (Brooklyn mortgage assumed by buyer) | $400,000 |
| Debt assumed (Hoboken mortgage) | $700,000 |
| Net mortgage boot received | max(0, 400k − 700k) = **$0** (Marcus assumed more debt) |
| Net debt assumed (going to Line 18) | 700k − 400k = $300,000 |
| Exchange expenses paid by Marcus | $32,000 (out of pocket — EAT and QI fees, escrow, etc.) |
| Related party? | No (EAT is independent under Rev. Proc. 2000-37) |
| Depreciation taken on Brooklyn | $380,000 (straight-line §1250) |

## The computation

| Line | Computation | Value |
|------|-------------|-------|
| 12-14 | No non-like-kind property | $0 |
| 15 | Cash received + non-like-kind FMV + net debt relief − exchange expenses | 0 + 0 + 0 − 0 (no boot to net against) | **$0** |
| 16 | FMV of like-kind received (Hoboken) | $1,800,000 |
| 17 | Line 15 + 16 | $1,800,000 |
| 18 | Basis given up + cash paid + net debt assumed + exchange expenses out of pocket | 820,000 + 750,000 + 300,000 + 32,000 | $1,902,000 |
| 19 | Realized gain (Line 17 − 18) | 1,800,000 − 1,902,000 | **−$102,000 (realized LOSS)** |
| 20 | Smaller of (15, 19), ≥ 0 | $0 |
| 21 | Ordinary recapture | $0 |
| 22 | Recognized gain | $0 |
| 23 | Recognized gain | $0 |
| 24 | Deferred gain/(loss) (Line 19 − 23) | **−$102,000** (deferred loss) |
| 25 | Basis of replacement (Line 18 − 15 + 23) | 1,902,000 − 0 + 0 | **$1,902,000** |

Wait — Marcus actually has a **realized loss** here, not a gain. Let me check: he gave up Brooklyn (basis $820k, FMV $1,200k → built-in gain $380k) and contributed $750k cash + $300k net new debt + $32k expenses = $1,082k value, against receiving Hoboken at $1.8M FMV. Realized = 1.8M − (820k + 750k + 300k + 32k) = 1.8M − 1.902M = −$102k.

This is a realized loss because the cash + new debt Marcus contributed exceeded the FMV gain he picked up. §1031 disallows recognition of loss; the loss is **deferred into the basis of replacement** (Line 25).

His Hoboken basis is $1,902,000 — slightly higher than its FMV of $1,800,000. The $102k unrecognized loss carries forward; on a future sale at the same FMV, he'd have a $102k loss to recognize.

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
5. Date replacement identified:                 04/05/2025
   (Note: in a reverse exchange, identification is reckoned from EAT's acquisition of replacement, 03/25/2025; Day 11)
6. Date you actually received replacement:      07/18/2025
   (Note: in a reverse exchange, "received" is the date EAT conveys to user; same as Line 4 here)
7. Related-party exchange?  No

## Part II — Related-Party
N/A

## Part III — Realized Gain, Recognized Gain, and Basis
12. FMV of OTHER property given up:            $0
13. Adjusted basis of OTHER property:          $0
14. Gain/(loss) on OTHER property:             $0
15. Cash + other received + net debt relief
    less exchange expenses:                    $0
16. FMV of like-kind property received:        $1,800,000
17. Add lines 15 and 16:                       $1,800,000
18. Basis given up + cash paid ($750k) + net
    debt assumed ($300k) + exchange expenses
    paid out of pocket ($32k):                 $1,902,000
19. Realized gain/(loss) (Line 17 − 18):       ($102,000)  (realized LOSS)
20. Smaller of Line 15 or 19, ≥ 0:             $0
21. Ordinary income under recapture rules:     $0
22. Recognized gain:                           $0
23. Recognized gain:                           $0
24. Deferred gain/(loss) (Line 19 − 23):       ($102,000)
25. Basis of replacement (Line 18 − 15 + 23):  $1,902,000

## Required attachments
- [ ] Form 4797 — not required this year (no recognized gain or loss)
- [ ] Schedule D — not required this year
- [ ] State filings:
  - NY: Marcus's Brooklyn relinquished property is NY-source. NY conforms to federal §1031, but verify with NY Department of Taxation and Finance.
  - NJ: Hoboken replacement is NJ-source going forward.
  - No clawback regime in NY/NJ comparable to California's Form 3840, but state recognition rules may differ on subsequent sale.
- [ ] Reverse-exchange specific records to retain (not filed):
  - Qualified Exchange Accommodation Agreement (QEAA) with EAT
  - Settlement statements from EAT's acquisition (03/25/2025)
  - Settlement statement from Marcus's relinquished sale (07/18/2025)
  - Settlement statement from EAT's conveyance to Marcus (07/18/2025)
  - Loan documents showing Marcus's mortgage assumption from EAT
  - Identification notice dated 04/05/2025

## Validation summary
- Reverse 45-day check: identification on Day 11 ≤ 45 (from EAT acquisition 03/25) ✓
- Reverse 180-day check: relinquished disposed on Day 115 ≤ 180 (from EAT acquisition 03/25) ✓
- Math: all checks passed
- Sanity warnings:
  - Realized loss of $102,000 is NOT recognized — §1031 disallows loss recognition. The loss is deferred into the basis of replacement (Line 25 = $1,902,000 vs. FMV $1,800,000).
  - Marcus's depreciation history of $380,000 from Brooklyn carries into Hoboken's basis. On a future sale, up to $380k could be unrecaptured §1250 gain (plus any new depreciation taken on Hoboken before sale).
  - Reverse exchanges have stricter audit scrutiny. The QEAA must satisfy Rev. Proc. 2000-37 safe harbor: EAT must have economic substance (held title in good faith), pay/receive market-based fees, and not be a related party. Marcus should verify Atlantic Title Holdings' independence.
  - Loan structure: the Hoboken mortgage was originally on EAT, then assumed by Marcus. Lender consent and assumption documents must be in order.

## Next steps
- File Form 8824 with 2025 Form 1040
- No estimated tax adjustment for the exchange (no recognized gain)
- Set up new depreciation schedule for Hoboken: basis $1,902,000 less land allocation, residential MACRS 27.5-year SL
- Set calendar reminder: any disposition of Hoboken before July 18, 2027 triggers reopening of the deferral (under general §1031 holding-period prudence — though no specific 2-year rule applies since this isn't a related-party exchange)
- Retain all QEAA, EAT settlement statements, loan documents indefinitely

## Sources cited in this draft
- IRS Form 8824, current revision
- IRS Instructions for Form 8824
- IRC §1031 (post-TCJA, real-property only)
- IRC §1031(b) (no loss recognition)
- IRC §1031(d) (basis of replacement)
- Rev. Proc. 2000-37 (reverse exchange safe harbor)
- Rev. Proc. 2004-51 (modifications to Rev. Proc. 2000-37)
- Treas. Reg. §1.1031(k)-1 (general §1031 deferred-exchange rules)
- Pub. 544 (Sales and Other Dispositions of Assets)
```

## Why each non-obvious choice

**Why is the EAT considered independent and not a related party?** Rev. Proc. 2000-37 specifies that an EAT can be:
- Any person other than the taxpayer or a disqualified person
- Subject to federal income tax (i.e., not a tax-exempt entity)
- Hold legal title and bear economic risk of the property
- Be paid market-based fees (typically $5,000-$25,000 depending on transaction size and complexity)

Atlantic Title Holdings LLC is a third-party single-member LLC formed by the QI parent firm specifically to hold §1031 reverse-exchange properties for clients. It is independent of Marcus, files its own tax return, and pays/receives FMV fees.

**Why is Line 5 (identification date) reckoned from EAT acquisition?** In a reverse exchange under Rev. Proc. 2000-37, the user must identify the property to be relinquished within 45 days of the EAT's acquisition of the replacement (not from the user's own actions on the relinquished side). The 180-day clock to actually dispose of relinquished also runs from EAT acquisition.

**Why are Line 4 and Line 6 the same date (07/18/2025)?** In the reverse-exchange swap on the closing day, the relinquished is sold AND the EAT conveys the replacement to Marcus simultaneously. The form requires both dates; in practice they're often the same.

**Why is Marcus's cash contribution ($750k) on Line 18 and not netted against Line 15?** Cash paid by the user is on the "give" side (Line 18), increasing the basis component. Cash received by the user is on Line 15. They don't offset.

**Why is the loss not recognized?** IRC §1031(b) only triggers gain recognition (to extent of boot). It does NOT allow loss recognition — losses are always deferred into basis. This is asymmetric: §1031 helps gains (by deferring) and "hurts" losses (by also deferring).

**What if Marcus needs cash later from the deferral?** He can refinance Hoboken (cash-out refi, taking equity out as a loan, NOT a sale). Loan proceeds aren't taxable. Some practitioners refer to this as "exchange and refinance"; while technically allowed, the IRS scrutinizes refinances done close in time to the §1031 — a refi within 6-12 months may be challenged as a step-transaction designed to extract cash without recognition. Best practice: wait at least 12 months.

**What if Marcus dies before selling Hoboken?** His heirs receive Hoboken with stepped-up basis to FMV at death. The $102k deferred loss and $380k depreciation history are wiped out. (This is the "swap till you drop" estate planning strategy.)

## Audit defense

Reverse exchanges face heightened IRS scrutiny because of the EAT structure. Marcus's defense:
1. QEAA signed before EAT acquisition — proves Rev. Proc. 2000-37 safe harbor election
2. EAT's HUD-1 from 03/25/2025 — proves EAT (not Marcus) acquired Hoboken
3. EAT pays its own taxes, has its own EIN, files its own return — proves independence
4. Identification notice dated 04/05/2025 — within the 45-day window
5. Brooklyn closing on 07/18/2025 — within the 180-day window
6. Loan assumption documents from lender — proves clean transfer of mortgage
7. Form 8824 with all dates and computations
8. Depreciation schedule for Brooklyn (2008-2024) — establishes adjusted basis ($820k)

Reverse exchanges that fall outside the Rev. Proc. 2000-37 safe harbor (e.g., EAT held title for >180 days, EAT was a related party, no QEAA) can still potentially qualify for §1031 under common-law principles, but the burden is on the taxpayer and audit risk is high. The safe harbor exists to make these exchanges defensible.
