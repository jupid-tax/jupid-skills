# Example: Short Sale of Primary Residence — $75K Excluded under §108(a)(1)(E)

A complete walkthrough of Form 982 Box 1e (qualified principal residence indebtedness) for a short sale of a primary residence. Pattern: acquisition indebtedness on principal residence; full canceled amount within $750K cap; basis reduction to the home.

## The filer

- **Name**: Sam Mitchell
- **Filing status**: Married filing jointly
- **Tax year**: 2025 (filing in 2026)
- **Event**: Short sale of primary residence in July 2025; lender forgave $75,000 of mortgage shortfall
- **1099-C received**: Box 2 = $75,000; Box 1 = 7/22/2025; Box 6 code = F (creditor settlement); Box 7 = $295,000 (FMV)
- **1099-A also received**: showed the foreclosure-like disposition

The qualified principal residence exclusion under §108(a)(1)(E) was extended through tax year 2025 (Inflation Reduction Act + later legislation). For 2025, the exclusion is in effect. Verify status for any year past 2025.

## Step 1 — Verify the 1099-C and the residence

- Box 2: $75,000 ✓
- Box 4: "Mortgage shortfall on 5847 Oak Street short sale"
- Box 5: Yes (recourse loan; Sam was personally liable)
- Box 6: F (creditor settlement)
- Box 7: $295,000 (FMV at time of disposition)

The home was Sam's principal residence:
- Purchased July 2018 for $385,000 (with 20% down + $308,000 mortgage)
- Refinanced in 2021 for the same balance (no cash out)
- Lived in continuously as primary home through July 2025 — clearly meets §121's "2 of last 5" test
- Sale completed July 2025 for $295,000 (short sale; less than the $370,000 outstanding mortgage)

The $75,000 forgiven amount = approximately the gap between mortgage balance ($370K) and short sale price ($295K).

## Step 2 — Identify exclusion

Walk through:
- (A) Bankruptcy: not in Title 11 → skip
- (E) Principal residence: ✓ continue with this test
- (B) Insolvency: alternative — check separately as comparison
- (C) Farm: not a farmer → skip
- (D) QRPBI: not real property business → skip

### Test (E) Principal residence

Conditions:
1. Property is principal residence ✓ (lived in continuously)
2. Debt is acquisition indebtedness ✓ (used to BUY the home; refinance was no-cash-out, preserving acquisition status)
3. Debt secured by residence ✓
4. Exclusion in effect for tax year 2025 ✓ (extended through 2025)

§108(a)(1)(E) applies. Cap: $750K of qualified principal residence debt ($375K MFS). Sam's $75K is well within the cap.

### Test (B) Insolvency (for comparison)

If Sam elected insolvency instead:
- Liabilities (just before discharge): mortgage $370K + other consumer debt ~$45K = $415K
- Assets: home FMV $295K + 401(k) $180K + cars $35K + cash $8K + other ~$20K = $538K
- Insolvency: $415K − $538K = NEGATIVE → not insolvent

Insolvency does NOT apply. Sam must use Box 1e.

(If Sam had been insolvent, the choice between (B) and (E) would matter — see decision-tree reference. Box 1e generally has lower attribute cost because it only reduces home basis, not NOLs / credits.)

## Step 3 — Compute excluded amount

Box 1e exclusion: full $75,000 (within $750K cap; fully qualified principal residence indebtedness).

**Excluded amount: $75,000** (Form 982 Line 2)

**Schedule 1 Line 8c**: $0 (full amount excluded)

## Step 4 — Basis reduction (§108(h)(1))

Box 1e exclusion requires reducing basis of the principal residence by the excluded amount.

Wait — there's a subtlety. The home was SOLD in the short sale. The basis reduction normally applies to the home's basis going forward, but if the home is gone, there's nothing to reduce going forward.

Per §108(h)(1) and Pub 4681: the basis reduction is to the home's basis IMMEDIATELY BEFORE the discharge. This affects the gain/loss on the short sale itself.

Sam's home sale calculation:

| Item | Amount |
|------|--------|
| Original purchase price | $385,000 |
| Improvements (kitchen renovation 2020) | $18,000 |
| **Adjusted basis before §108(h) reduction** | $403,000 |
| **Less §108(h)(1) basis reduction** | $75,000 |
| **Adjusted basis after reduction** | **$328,000** |
| Selling price (short sale net) | $295,000 |
| Selling expenses | ($8,000) |
| Net selling price | $287,000 |
| **Realized loss on sale** | **−$41,000** |

But for personal-use property (primary residence), losses are NOT deductible (§165(c) doesn't permit personal-use casualty losses except in federally declared disasters, and §1041 / §165 doesn't allow ordinary loss on home sale). Sam cannot deduct the $41K loss.

The §121 capital gain exclusion is irrelevant here — there's no gain.

## Step 5 — Form 982 Part II

For Box 1e exclusion, the attribute reduction is the BASIS REDUCTION ITSELF (handled off-form in the home records). Form 982 Part II is NOT used for Box 1e — that's the bankruptcy/insolvency mechanism.

The Form 982 Part II is left BLANK or marked "N/A" for Box 1e filings. Some software / paper forms still ask for entries; in those cases, all Lines 4-11 are zero.

## The completed Form 982 draft

```markdown
# Form 982 — DRAFT for tax year 2025

## Header
Name(s) shown on return: Sam Mitchell and [Spouse]
Identifying number: XXX-XX-XXXX

## Part I — General Information

| Line | Description | Value |
|------|-------------|-------|
| 1a | Discharge in a Title 11 case | [ ] |
| 1b | Discharge to extent insolvent | [ ] |
| 1c | Discharge of qualified farm indebtedness | [ ] |
| 1d | Discharge of qualified real property business indebtedness | [ ] |
| 1e | Discharge of qualified principal residence indebtedness | [x] |
| 2 | Total amount of discharged indebtedness excluded from gross income | $75,000 |
| 3 | Election under §108(b)(5) | [ ] (N/A for Box 1e) |

## Part II — Reduction of Tax Attributes

| Line | Attribute | Amount reduced |
|------|-----------|----------------|
| 4 | Basis under §108(b)(5) or §108(c) | $0 |
| 5 | NOL | $0 |
| 6 | General business credit | $0 |
| 7 | Minimum tax credit | $0 |
| 8 | Net capital loss + carryover | $0 |
| 9 | Other basis | $0 |
| 10 | Passive activity loss + credit | $0 |
| 11 | Foreign tax credit carryover | $0 |
| | **Note**: Box 1e basis reduction is to the principal residence per §108(h)(1) — recorded off-form in user's home records | |

## Off-form: Principal residence basis reduction

| Item | Amount |
|------|--------|
| Original basis (purchase + improvements) | $403,000 |
| §108(h)(1) basis reduction | ($75,000) |
| **Adjusted basis after reduction** | **$328,000** |

## Off-form: Short sale gain/loss calculation

| Item | Amount |
|------|--------|
| Adjusted basis (post-reduction) | $328,000 |
| Net selling price ($295K − $8K closing costs) | $287,000 |
| Realized loss | ($41,000) — NOT deductible (personal-use property) |

## Required attachments / off-form items
- [x] Form 1099-C (kept with records)
- [x] Form 1099-A (also kept; documents disposition)
- [x] Mortgage closing documents (proves acquisition indebtedness)
- [x] Refinance documents from 2021 (proves no cash out; debt remained acquisition)
- [x] Short sale closing statement (HUD-1 / closing disclosure)
- [x] Home improvement receipts (basis substantiation)
- [x] Original purchase closing statement (basis substantiation)
- [x] Records showing primary residence use (utility bills, voter registration, driver's license address) — proves §121 / §108(h) qualifying use

## Validation summary
- Math: all checks passed
  - Excluded amount $75,000 ≤ Box 2 of 1099-C ($75,000) ✓
  - Excluded amount $75,000 ≤ $750,000 cap (MFJ) ✓
  - All debt was qualified principal residence indebtedness (acquisition debt for purchase + no-cash-out refinance) ✓
- Sanity:
  - Box 1e checked alone (not combined with other boxes)
  - Home was principal residence at time of discharge (lived in continuously)
  - §108(a)(1)(E) verified in effect for tax year 2025
  - $750K MFJ cap not exceeded
  - Basis reduction recorded for home: $403K → $328K
  - Short-sale loss of $41K is NON-deductible (personal-use property)
  - Insolvency tested as alternative — Sam was NOT insolvent; Box 1e is the correct path
  - No NOLs, credits, or other attributes affected (Box 1e doesn't trigger §108(b) Part II reduction)
- Next steps:
  - Retain ALL home documentation (purchase, improvements, mortgage, refinance, short sale, 1099-C, 1099-A) for at least 7 years (longer than usual due to home-sale records)
  - File Schedule D / Form 8949 for the short sale: realized loss not deductible (personal-use), but the disposition should still be reported on Form 8949 (some software auto-handles this)
  - Document basis reduction permanently — useful if future home transactions need basis tracking
  - Consider replacing the home; if Sam buys another principal residence, no basis carryover (the §108(h) reduction was to the OLD home, now gone)

## Sources cited in this draft
- IRS Form 982, 2025 revision
- IRS Instructions for Form 982, 2025 revision
- IRS Pub 4681 (Canceled Debts, Foreclosures, Repossessions, and Abandonments)
- IRC §61(a)(11) (discharge of indebtedness as gross income)
- IRC §108(a)(1)(E) (qualified principal residence indebtedness exclusion)
- IRC §108(h)(1) (basis reduction)
- IRC §108(h)(2) ($750K / $375K MFS cap)
- IRC §108(h)(5) (definition of qualified principal residence indebtedness)
- IRC §121 (gain exclusion on sale of principal residence — confirmed not relevant here due to loss)
- IRC §165(c) (loss on sale of personal-use property — NOT deductible)
- Form 1099-C from lender, dated 7/22/2025
- Form 1099-A from lender (disposition reporting)
- Inflation Reduction Act / extension legislation (verifying §108(a)(1)(E) in effect for 2025)
```

## Why each non-obvious choice

**Why Box 1e and not Box 1b (insolvency)?** Sam was tested for insolvency as well — but with substantial 401(k) and other assets, total assets exceeded total liabilities. Insolvency does NOT apply. Box 1e applies because the discharge was on principal residence acquisition debt.

**Why is the basis reduction to $328K significant if the home is gone?** The basis reduction affects the SHORT SALE calculation itself. By reducing basis from $403K to $328K, the realized loss on the sale changes from $116K to $41K. But personal-use losses aren't deductible anyway, so the math doesn't actually save Sam taxes — the basis reduction is essentially a wash here.

The basis reduction MATTERS more in a different scenario: if the home had appreciated and the §121 exclusion would otherwise zero out the gain, the basis reduction could push gain above the $500K MFJ §121 cap. Sam doesn't have that issue (loss, not gain), but the reduction still must be recorded.

**Why doesn't Sam claim a $41K loss?** Personal-use property losses are NOT deductible (§165(c) limits losses to those from a trade/business, transactions for profit, or federally declared casualties). The home was personal-use; the loss is not deductible.

**Why was the refinanced debt still "acquisition indebtedness"?** Acquisition indebtedness is debt to buy, build, or substantially improve the home. A no-cash-out refinance preserves the original debt's character — the new debt is still "acquisition" because it replaced acquisition debt without adding cash. If Sam had cashed out (e.g., $50K cash for a vacation), only the original acquisition portion would qualify under §108(h); the cash-out portion would not.

**Why doesn't Form 982 Part II have entries?** Box 1e (principal residence) doesn't trigger the §108(b) attribute-reduction-in-order mechanism. The "attribute reduction" for Box 1e is the basis reduction to the home itself, recorded off-form in the user's records per §108(h)(1).

**What if the canceled amount had been $850K (above the cap)?**
- $750K excluded under Box 1e (capped at MFJ limit)
- $100K either:
  - Excluded under insolvency (Box 1b) IF Sam was insolvent at that level — file second Form 982 with Box 1b
  - Otherwise, ordinary income on Schedule 1 Line 8c

**What if §108(a)(1)(E) had lapsed for 2025?**
- Box 1e would NOT be available
- Sam would test insolvency only — and as shown, was not insolvent
- The full $75K would be ordinary income on Schedule 1 Line 8c

**Documentation Sam retains**:
1. Original purchase documents (2018 closing statement, deed, mortgage)
2. Refinance documents (2021) — proves no cash out
3. Home improvement receipts (kitchen renovation 2020)
4. Short sale closing statement (2025)
5. Form 1099-C from lender
6. Form 1099-A from lender
7. Lender correspondence about the short sale
8. Records establishing principal-residence use (utility bills, etc.)
9. Form 8949 for the short sale (loss not deductible, but reported)

Retain for at least 7 years (home-sale records often need longer retention than other tax records due to lookback periods).
