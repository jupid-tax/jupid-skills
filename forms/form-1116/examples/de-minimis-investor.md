# Example: US Investor with $285 Foreign Tax — De-Minimis Election (No Form 1116)

A US-resident investor with international index funds whose only foreign tax sits on 1099-DIV Box 7. This is the most common Form 1116 trigger and the most common case where Form 1116 is **not** filed at all because the de-minimis $300/$600 election applies.

## The filer

- **Name**: David Park
- **Status**: US citizen, single filer, lives in Boston MA
- **Profession**: software engineer at a US tech company (W-2 wages)
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered (Step 1 of workflow)

### Foreign income

David's only foreign-source income comes from his US brokerage holding international index funds (Vanguard VXUS, Vanguard VWO, Schwab SCHF):

| Source | Type | USD amount | Foreign tax (Box 7) |
|--------|------|-----------|---------------------|
| VXUS dividends (Vanguard Total International) | 1099-DIV Box 1a (all qualified, Box 1b) | $4,200 | $285 |
| VWO dividends (Vanguard Emerging Markets) | 1099-DIV Box 1a (all qualified, Box 1b) | $1,800 | $0 (none passed through) |
| Schwab International ETF (SCHF) | 1099-DIV Box 1a (all qualified, Box 1b) | $880 | $0 (none passed through) |
| **Total foreign tax (Box 7)** | | | **$285** |

Persona facts: the consolidated 1099-DIV from David's brokerage shows $285 in Box 7, all from VXUS, and the VXUS supplemental statement reports the full $4,200 as foreign-source income. VWO and SCHF passed no foreign tax through this year, so there is nothing to credit from them (a fund passes the credit through only if it chooses to and reports it on Form 1099-DIV; Pub. 514, "Mutual fund shareholder"). An "over the threshold" case is in `multi-basket-investor.md`.

### Filing status criteria for the $300/$600 election

The election under IRC §904(j) (2025 i1116, "Election To Claim the Foreign Tax Credit Without Filing Form 1116"; 2025 Form 1040 instructions, Schedule 3 line 1 "Exception") requires ALL of:

- [ ] Filer is an individual (not an estate or trust)
- [ ] Total creditable foreign tax ≤ $300 (single, MFS, HoH, QSS) OR ≤ $600 (MFJ)
- [ ] All foreign-source gross income is passive category (interest and dividends)
- [ ] All foreign income and tax reported on a qualified payee statement (1099-DIV, 1099-INT, Schedule K-1 (Form 1041), Schedule K-3 (Form 1065 or 1120-S), substitute statement)
- [ ] The shares or bonds were held at least 16 days and the filer wasn't obligated to pay the amounts to someone else
- [ ] Not filing Form 4563 or excluding income from sources within Puerto Rico
- [ ] All foreign taxes legally owed, not eligible for a refund or reduced treaty rate, and paid to countries the US recognizes that don't support terrorism

David's facts:

- Individual filer ✓
- Foreign tax: $285 → ≤ $300 single ✓
- All from 1099-DIV (passive: dividends from international index funds) ✓
- All on qualified payee statement (brokerage consolidated 1099-DIV) ✓
- Fund shares held all year (well over 16 days); no obligation to pass the dividends on ✓ (asked David)
- Massachusetts resident; not filing Form 4563; no Puerto Rico income ✓
- Fund-level withholding reported in Box 7 as foreign tax paid; no treaty refund claim available to David ✓ (confirm with the fund statement)

**All criteria met.** David elects the de-minimis exception.

## The deliverable (no Form 1116)

```markdown
# Foreign Tax Credit — DRAFT for tax year 2025
# (No Form 1116 — IRC §904(j) election)

## Filer
Name: David Park
SSN: XXX-XX-XXXX
Status: Single, US resident (Massachusetts)

## Foreign tax claimed
Total foreign income tax (1099-DIV Box 7): $285

## Election
Election under IRC §904(j) to claim FTC without filing Form 1116 (made by entering the credit on Schedule 3 line 1).

## Eligibility checklist
- [x] Individual filer
- [x] Total creditable foreign tax ≤ $300 single ($285 ≤ $300)
- [x] All foreign income is passive category (international index fund dividends)
- [x] All foreign income reported on a qualified payee statement (consolidated 1099-DIV)
- [x] 16-day holding period met; no related-payment obligation
- [x] Not filing Form 4563; no excluded Puerto Rico income
- [x] Taxes legally owed, not refundable, not paid to a sanctioned country

## Where it goes on Form 1040
Schedule 3 (Form 1040), Line 1: $285 (the smaller of total foreign tax, $285, or Form 1040 line 16 plus Schedule 2 line 1a)

This flows to Schedule 3 line 8 and then Form 1040 Line 20.

## Required attachments
- None. Form 1116 NOT required.

## Validation summary
- All de-minimis criteria met
- Sanity: $285 / $4,200 foreign-source dividends = 6.8% effective foreign withholding rate — plausible for an international index fund (rates vary by country and fund)

## Sources cited in this draft
- IRC §904(j) (election to claim the credit without Form 1116)
- 2025 Instructions for Form 1040, Schedule 3 line 1 "Exception"
- 2025 Instructions for Form 1116, "Election To Claim the Foreign Tax Credit Without Filing Form 1116"
- Brokerage 2025 consolidated Form 1099-DIV and VXUS supplemental foreign-source statement
```

## Why no Form 1116?

The §904(j) election simplifies filing for retail investors who hold international funds in a US brokerage. The IRS designed it so the typical small-amount dividend filer doesn't have to do the whole §904 limitation calculation. As long as foreign tax stays under $300 single / $600 MFJ AND the income is all passive on qualified statements, just put the number on Schedule 3 Line 1.

## What if David's foreign tax had been $325?

Then the election fails ($325 > $300 single). David would need to file a full Form 1116 with passive basket (line i "RIC", Part II column (l) "1099 taxes"). Assume $130,000 of wages, no other income, and all $6,880 of fund dividends qualified (2025, single, standard deduction $15,750). He qualifies for the adjustment exception (Qualified Dividends and Capital Gain Tax Worksheet line 5 = $114,250 ≤ $197,300; foreign qualified dividends $4,200 < $20,000), so no line 1a or line 18 adjustment. The §904 limitation would compute:

- Line 1a: $4,200 (foreign-source dividends)
- Line 3e: $136,880 ($130,000 + $6,880); Line 3f: 0.0307; Line 3g: $15,750 × 0.0307 = $484
- Line 7 (after standard deduction allocation): $4,200 − $484 = $3,716
- Line 8 / Line 14: $325
- Line 18: $136,880 − $15,750 = $121,130
- Line 19 (limitation ratio): $3,716 / $121,130 = 0.0307
- Line 20: Form 1040 line 16 = $21,299 (Qualified Dividends and Capital Gain Tax Worksheet: $20,267 ordinary tax on $114,250 + $1,032 at 15% on $6,880)
- Line 21 / 23: $21,299 × 0.0307 = $654
- Line 24: smaller of $325 or $654 = $325 (full credit); Part IV lines 27, 32, 33, 35 = $325

Net result: same FTC ($325), but with a full Form 1116 attached. The administrative burden is the only difference.

## What if some of David's foreign income had been general basket?

For example, if David did consulting work in Germany on the side and earned €5,000 in German wages with €1,500 German tax — that's general basket. The de-minimis election fails ("All foreign income is passive category"). David would need:

- One Form 1116 for passive basket ($4,200 dividends, $285 foreign tax)
- One Form 1116 for general basket (€5,000 wages ≈ $5,643 at the IRS 2025 yearly average of 0.886; the €1,500 tax translated at the rate on each date it was paid or withheld)
- Part IV completed on the Form 1116 with the larger line 24

See [`multi-basket-investor.md`](./multi-basket-investor.md) for that walkthrough.

## What David should remember

- Keep the 1099-DIV consolidated statement with foreign tax detail for at least 3 years (general statute) — longer if any unused FTC carryforward exists
- Each year's election is independent; if next year his foreign tax exceeds $300, he files Form 1116 for that year
- The election doesn't affect his ability to take FTC in future years on Form 1116, but unused foreign tax can't be carried into or out of an election year (2025 i1116, Line 10)
- Many tax software packages handle this automatically when importing 1099-DIV; David just confirms the credit on Schedule 3
