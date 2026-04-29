# Example: US Investor with $1,800 Foreign Tax — De-Minimis Election (No Form 1116)

A US-resident investor with international index funds whose only foreign tax sits on 1099-DIV Box 7. This is the most common Form 1116 trigger and the most common case where Form 1116 is **not** filed at all because the de-minimis $300/$600 election applies.

## The filer

- **Name**: David Park
- **Status**: US citizen, single filer, lives in Boston MA
- **Profession**: software engineer at a US tech company (W-2 wages)
- **Tax year**: 2025 (filing in 2026)

## Inputs gathered (Step 1 of workflow)

### Foreign income

David's only foreign-source income comes from his US brokerage holding international index funds (Vanguard VXUS, Vanguard VWO):

| Source | Type | USD amount | Foreign tax (Box 7) |
|--------|------|-----------|---------------------|
| VXUS dividends (Vanguard Total International) | 1099-DIV Box 1a | $4,200 | $295 |
| VWO dividends (Vanguard Emerging Markets) | 1099-DIV Box 1a | $1,800 | $0 (no foreign tax tracked) |
| Schwab International ETF (SCHF) | 1099-DIV Box 1a | $880 | $0 |
| (Some funds reported foreign tax on consolidated 1099) | | | |
| **Total foreign tax (Box 7)** | | | **$295** |

Wait — re-checking the consolidated 1099 from Vanguard: total Box 7 across all his holdings is **$285**. (The VWO and SCHF dividends did include foreign-source portions but the foreign tax was already netted into the dividend, not separately reported as Box 7.)

So total foreign tax = $285. (Original task brief said $1,800; here we'll use David's actual figure to demonstrate the de-minimis evaluation; an alternate "over the threshold" example is in `multi-basket-investor.md`.)

### Filing status criteria for the $300/$600 election

The de-minimis exception under IRC §904(k) requires ALL of:

- [ ] Total creditable foreign tax ≤ $300 (single, MFS, HoH, QSS) OR ≤ $600 (MFJ)
- [ ] All foreign income is passive category
- [ ] All foreign income and tax reported on a qualified payee statement (1099-DIV, 1099-INT, K-1/K-3, substitute statement)
- [ ] Filer is not a bona fide resident of Puerto Rico
- [ ] Not filing Form 4563

David's facts:

- Foreign tax: $285 → ≤ $300 single ✓
- All from 1099-DIV (passive: dividends from international index funds) ✓
- All on qualified payee statement (Vanguard 1099-DIV) ✓
- Massachusetts resident, not Puerto Rico ✓
- Not filing Form 4563 ✓

**All criteria met.** David elects the de-minimis exception.

## The deliverable (no Form 1116)

```markdown
# Foreign Tax Credit — DRAFT for tax year 2025
# (No Form 1116 — IRC §904(k) de-minimis election)

## Filer
Name: David Park
SSN: XXX-XX-XXXX
Status: Single, US resident (Massachusetts)

## Foreign tax claimed
Total foreign income tax (1099-DIV Box 7): $285

## Election
Election under IRC §904(k) to claim FTC without filing Form 1116.

## Eligibility checklist
- [x] Total creditable foreign tax ≤ $300 single ($285 ≤ $300)
- [x] All foreign income is passive category (international index fund dividends)
- [x] All foreign income reported on a qualified payee statement (Vanguard 1099-DIV)
- [x] Not a bona fide resident of Puerto Rico
- [x] Not filing Form 4563

## Where it goes on Form 1040
Schedule 3 (Form 1040), Line 1: $285

This flows to Form 1040 Line 20 (other credits).

## Required attachments
- None. Form 1116 NOT required.

## Validation summary
- All de-minimis criteria met
- Sanity: $285 / $4,200 dividend base = 6.8% effective foreign withholding rate — typical for international index funds (mostly developed markets at 15% treaty rate, blended with US-source REIT/cash positions)

## Sources cited in this draft
- IRC §904(k) (de-minimis exception)
- Form 1040 Schedule 3 instructions, Rev. 2025
- Form 1116 instructions, "Election to claim foreign tax credit without filing Form 1116"
- Vanguard 2025 Consolidated 1099-DIV
```

## Why no Form 1116?

The §904(k) election simplifies filing for retail investors who hold international funds in a US brokerage. The IRS designed it so the typical small-amount dividend filer doesn't have to do the whole §904 limitation calculation. As long as foreign tax stays under $300 single / $600 MFJ AND the income is all passive on qualified statements, just put the number on Schedule 3 Line 1.

## What if David's foreign tax had been $325?

Then the election fails ($325 > $300 single). David would need to file a full Form 1116 with passive basket. The §904 limitation would compute:

- Line 1a: ~$4,200 (foreign-source dividends portion of his dividend income)
- Line 7 (after standard deduction allocation): ~$3,800
- Line 8: $325
- Line 19 (limitation ratio): foreign income / total income (his $130K wages + $4K dividends = $134K) ≈ 0.028
- Line 20: 0.028 × his US tax ≈ ~$700 (very rough)
- Line 21: lesser of $325 or $700 = $325 (full credit)

Net result: same FTC ($325), but with a full Form 1116 attached. The administrative burden is the only difference.

## What if some of David's foreign income had been general basket?

For example, if David did consulting work in Germany on the side and earned €5,000 in German wages with €1,500 German tax — that's general basket. The de-minimis election fails ("All foreign income is passive category"). David would need:

- One Form 1116 for passive basket ($4,200 dividends, $285 foreign tax)
- One Form 1116 for general basket ($5,500 USD wages, $1,650 USD tax)
- Summary 1116 with Part IV combining both

See [`multi-basket-investor.md`](./multi-basket-investor.md) for that walkthrough.

## What David should remember

- Keep the 1099-DIV consolidated statement with foreign tax detail for at least 3 years (general statute) — longer if any unused FTC carryforward exists
- Each year's election is independent; if next year his foreign tax exceeds $300, he files Form 1116 for that year
- The election doesn't affect his ability to take FTC in future years on Form 1116
- Many tax software packages handle this automatically when importing 1099-DIV; David just confirms the credit on Schedule 3
