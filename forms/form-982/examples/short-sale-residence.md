# Example: Short Sale of Primary Residence — $75K Excluded under §108(a)(1)(E)

A complete walkthrough of Form 982 Box 1e (qualified principal residence indebtedness) for a short sale of a primary residence. Pattern: acquisition indebtedness on the main home, discharged in 2025; full canceled amount within the $750K cap; no line 10b basis reduction because the home was sold in the same transaction. Lines follow Form 982 (Rev. March 2018) and its Instructions (Rev. December 2021).

## The filer

- **Name**: Sam Mitchell
- **Filing status**: Married filing jointly
- **Tax year**: 2025 (filing in 2026)
- **Event**: Short sale of primary residence in July 2025; lender forgave the $75,000 of mortgage balance left after the sale
- **1099-C received**: Box 2 = $75,000; Box 1 = 7/22/2025; Box 6 code = F (by agreement; the 1099-A/C instructions list short sales under code F); Box 7 = $300,000 (appraised value; for a short sale, box 7 FMV should include the appraised value)
- **No Form 1099-A**: the lender didn't acquire the home (Form 1099-A reports a lender's acquisition of secured property or an abandonment; Instructions for Forms 1099-A and 1099-C). Sam received Form 1099-S for the sale from the settlement agent.

The discharge date (July 22, 2025) is before Jan. 1, 2026, so §108(a)(1)(E) is available (extended through 2025 by P.L. 116-260, div. EE, §114; i982 Line 1e). A short sale closing in 2026 would need a written arrangement entered into before Jan. 1, 2026; see the 2026 variant at the end.

## Step 1 — Verify the 1099-C and the residence

- Box 2: $75,000 ✓
- Box 4: "Mortgage shortfall on 5847 Oak Street short sale"
- Box 5: Yes (recourse loan; Sam was personally liable)
- Box 6: F (by agreement)
- Box 7: $300,000 (appraised value)

The home was Sam's principal residence:
- Purchased July 2018 for $448,000 (5% down, $22,400, plus a $425,600 mortgage)
- Kitchen renovation in 2020: $18,000, paid in cash
- Refinanced in 2021 for the then-outstanding balance of $405,500 (rate-and-term, no cash out)
- Lived in continuously as the main home through July 2025 (the home where Sam ordinarily lives; i982 Line 1e)
- Sale completed July 2025 for $303,000; $8,000 of selling costs paid from the proceeds; the lender received $295,000 against the $370,000 outstanding balance

The $75,000 forgiven = $370,000 balance − $295,000 net proceeds the lender received.

## Step 2 — Identify exclusion

Walk through:
- (A) Bankruptcy: not in Title 11 → skip
- (E) Principal residence: ✓ continue with this test
- (B) Insolvency: alternative — check separately as comparison
- (C) Farm: not a farmer → skip
- (D) QRPBI: not real property business → skip

### Test (E) Principal residence

Conditions:
1. Property is the main home ✓ (lived in continuously; §108(h)(5))
2. Debt is acquisition indebtedness ✓ (used to BUY the home; the 2021 refinance was no-cash-out, so the new loan is QPRI up to the $405,500 old principal; i982 Line 1e)
3. Debt secured by residence ✓
4. Discharged 7/22/2025, before Jan. 1, 2026 ✓
5. Discharge tied to the home's decline in value and Sam's financial condition, not services for the lender ✓ (§108(h)(3))

§108(a)(1)(E) applies. Cap: QPRI is acquisition debt up to $750K ($375K MFS). The whole $370,000 balance is QPRI, so the §108(h)(4) ordering rule takes nothing away; the $75K is well within the cap.

### Test (B) Insolvency (for comparison)

If Sam elected insolvency instead:
- Liabilities (just before discharge): mortgage $370K + other consumer debt ~$45K = $415K
- Assets: home FMV $300K (appraisal) + 401(k) $180K + cars $35K + cash $8K + other ~$20K = $543K
- Insolvency: $415K − $543K = NEGATIVE → not insolvent

Insolvency does NOT apply. Sam must use Box 1e.

(If Sam had been insolvent, the choice between (B) and (E) would matter — see decision-tree reference. Box 1e generally has lower attribute cost because it only reduces home basis (line 10b, and only if the home is still owned), not NOLs / credits.)

## Step 3 — Compute excluded amount

Box 1e exclusion: full $75,000 (within $750K cap; fully qualified principal residence indebtedness).

**Excluded amount: $75,000** (Form 982 Line 2)

**Schedule 1 Line 8c**: $0 (full amount excluded)

## Step 4 — Basis reduction (§108(h)(1)) and the sale itself

Box 1e requires reducing the basis of the principal residence (§108(h)(1)), but only if the filer continues to own the home after the discharge: line 10b is entered "ONLY if line 1e is checked" (form text), and the instructions call for it only when "box 1e is checked and you continue to own the residence after discharge" (i982 Line 10b and "How To Complete the Form", step 4; Pub. 4681 "Qualified Principal Residence Indebtedness" under Reduction of Tax Attributes). Sam sold the home in the short sale, so **line 10b = $0** and no basis is reduced.

The sale is figured on its own (Pub. 523 worksheet):

| Item | Amount |
|------|--------|
| Purchase price (2018) | $448,000 |
| Improvements (kitchen renovation 2020) | $18,000 |
| **Adjusted basis** | **$466,000** |
| Sale price | $303,000 |
| Selling expenses | ($8,000) |
| Amount realized | $295,000 |
| **Loss on sale** | **−$171,000** |

A loss on the sale of a main home can't be deducted (Pub. 523 worksheet line 7: "You can't deduct this loss"). Because Sam received Form 1099-S, the sale must still be reported on Form 8949 even though there is no taxable gain (Pub. 523 "Reporting Gain or Loss on Your Home Sale"); follow the Form 8949 and Schedule D instructions for the nondeductible loss.

The §121 capital gain exclusion is irrelevant here — there's no gain.

## Step 5 — Form 982 Part II

For Box 1e, the only Part II line that applies is line 10b, and only if the home is still owned (i982 "How To Complete the Form", qualified principal residence step 4). Sam no longer owns it, so line 10b = $0. Lines 4–9, 10a, and 11a–13 don't apply to a QPRI exclusion and are $0. Line 2 ($75,000) need not equal line 10b (i982 Line 2).

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
| 3 | Elect to treat §1221(a)(1) real property as depreciable property? | No |

## Part II — Reduction of Tax Attributes

| Line | Attribute | Amount |
|------|-----------|--------|
| 4 | QRPBI basis reduction | $0 |
| 5 | §108(b)(5) election | $0 |
| 6 | NOL | $0 |
| 7 | General business credit | $0 |
| 8 | Minimum tax credit | $0 |
| 9 | Net capital loss + carryover | $0 |
| 10a | Basis of nondepreciable and depreciable property | $0 |
| 10b | Basis of principal residence | $0 (home sold in the short sale; line 10b applies only if the home is still owned) |
| 11a–11c | Farm debt basis | $0 |
| 12 | Passive activity loss + credit | $0 |
| 13 | Foreign tax credit carryover | $0 |

## Part III
Blank (corporations only)

## Off-form: Short sale gain/loss calculation (Pub. 523)

| Item | Amount |
|------|--------|
| Adjusted basis (purchase $448,000 + improvements $18,000) | $466,000 |
| Amount realized ($303,000 sale price − $8,000 selling expenses) | $295,000 |
| Loss | ($171,000) — NOT deductible (main home); reported on Form 8949 because Form 1099-S was received |

## Required attachments / off-form items
- [x] Form 1099-C (kept with records)
- [x] Form 1099-S (sale) and the Form 8949 entry for the sale
- [x] Mortgage closing documents (proves acquisition indebtedness)
- [x] Refinance documents from 2021 (proves no cash out; debt remained acquisition)
- [x] Short sale closing statement (HUD-1 / closing disclosure)
- [x] Home improvement receipts (basis substantiation)
- [x] Original purchase closing statement (basis substantiation)
- [x] Records showing primary residence use (utility bills, voter registration, driver's license address) — proves main-home use (§108(h)(5))

## Validation summary
- Math: all checks passed
  - Excluded amount $75,000 ≤ Box 2 of 1099-C ($75,000) ✓
  - Excluded amount $75,000 ≤ $750,000 cap (MFJ) ✓
  - All debt was qualified principal residence indebtedness (acquisition debt for purchase + no-cash-out refinance) ✓
- Sanity:
  - Box 1e only (no title 11 case; Sam not insolvent)
  - Home was principal residence at time of discharge (lived in continuously)
  - Discharge 7/22/2025 is before Jan. 1, 2026 ✓
  - $750K MFJ cap not exceeded; no non-QPRI portion for the §108(h)(4) ordering rule
  - Line 10b = $0: home disposed of in the short sale
  - Short-sale loss of $171K is NON-deductible (main home; Pub. 523)
  - Insolvency tested as alternative — Sam was NOT insolvent; Box 1e is the correct path
  - No NOLs, credits, or other attributes affected (Box 1e reduces only home basis, and only for a home still owned)
- Next steps:
  - Retain ALL home documentation (purchase, improvements, mortgage, refinance, short sale, 1099-C, 1099-S) until the period of limitations expires for the 2025 return (https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records)
  - Report the sale on Form 8949 / Schedule D because Form 1099-S was received; the loss is not deductible (Pub. 523)
  - If Sam buys another home, nothing carries over: no basis reduction was made

## Sources cited in this draft
- IRS Form 982 (Rev. March 2018)
- IRS Instructions for Form 982 (Rev. December 2021), Line 1e, Line 10b
- IRS Pub. 4681 (2025) (Canceled Debts, Foreclosures, Repossessions, and Abandonments)
- IRS Pub. 523 (2025) (Selling Your Home: loss not deductible; Form 8949 if Form 1099-S received)
- Instructions for Forms 1099-A and 1099-C (Rev. April 2025) (code F short sales; box 7 appraised value)
- IRC §61(a)(11) (discharge of indebtedness as gross income)
- IRC §108(a)(1)(E) (qualified principal residence indebtedness exclusion; discharges before Jan. 1, 2026)
- IRC §108(h)(1) (basis reduction)
- IRC §108(h)(2) (definition; $750K / $375K MFS cap)
- IRC §108(h)(4) (ordering rule for partly qualified loans)
- IRC §108(h)(5) (principal residence has the §121 meaning)
- IRC §121 (gain exclusion on sale of principal residence — confirmed not relevant here due to loss)
- Form 1099-C from lender, dated 7/22/2025
- P.L. 116-260, div. EE, §114 (QPRI exclusion extended through 2025)
```

## Why each non-obvious choice

**Why Box 1e and not Box 1b (insolvency)?** Sam was tested for insolvency as well — but with substantial 401(k) and other assets, total assets exceeded total liabilities. Insolvency does NOT apply. Box 1e applies because the discharge was on principal residence acquisition debt.

**Why is there no basis reduction?** Line 10b applies only if the filer continues to own the home after the discharge (i982 Line 10b; Pub. 4681). The short sale and the cancellation happened together, so there is no home left to reduce. The basis reduction MATTERS in a different scenario: a loan modification where Sam keeps the home. Then line 10b = the smaller of the $75,000 excluded or the home's basis, and the lower basis raises the gain on a later sale (Pub. 523 basis adjustments, line 5i).

**Why doesn't Sam claim the $171K loss?** A loss on the sale of a main home can't be deducted (Pub. 523 worksheet line 7). The sale is still reported on Form 8949 because a Form 1099-S was issued.

**Why was the refinanced debt still "acquisition indebtedness"?** Acquisition indebtedness is debt to buy, build, or substantially improve the home. A refinance counts as QPRI up to the old mortgage principal just before the refinancing (i982 Line 1e) — the 2021 loan replaced acquisition debt without adding cash. If Sam had cashed out (e.g., $50K cash for a vacation), the cash-out portion would not be QPRI and the ordering rule below would apply.

**Why are Form 982 Part II entries all $0?** Box 1e doesn't trigger the §108(b) attribute-reduction-in-order mechanism (§108(b)(1) covers only 1a–1c). The only Part II line for 1e is line 10b, which is $0 because Sam no longer owns the home.

**What if $40,000 of the loan had not been QPRI** (for example, cash-out in the 2021 refinance spent on credit cards, still part of the balance immediately before the discharge)?
- §108(h)(4) ordering rule: the exclusion covers only the amount discharged in excess of the non-QPRI part: $75,000 − $40,000 = $35,000 on Box 1e
- The other $40,000: test insolvency (Box 1b on the same Form 982, line 2 = the total) — Sam is not insolvent
- So $40,000 is ordinary income on Schedule 1 Line 8c (Pub. 4681 Example 3 works the same way: $115,000 canceled, $110,000 non-QPRI, $5,000 excluded)

**What if the short sale had closed in March 2026?**
- §108(a)(1)(E) covers a 2026 discharge only if it is subject to an arrangement entered into and evidenced in writing before Jan. 1, 2026 (for example, the lender's short-sale approval letter signed in December 2025). Ask for that document.
- With it: same Form 982 as above, on the 2026 return
- Without it: Box 1e is NOT available; Sam tests insolvency only — and as shown, was not insolvent; the full $75K is ordinary income on Schedule 1 Line 8c of the 2026 return

**Documentation Sam retains**:
1. Original purchase documents (2018 closing statement, deed, mortgage)
2. Refinance documents (2021) — proves no cash out
3. Home improvement receipts (kitchen renovation 2020)
4. Short sale closing statement (2025)
5. Form 1099-C from lender
6. Form 1099-S from the settlement agent
7. Lender correspondence about the short sale
8. Records establishing principal-residence use (utility bills, etc.)
9. Form 8949 for the short sale (loss not deductible, but reported)

Retain until the period of limitations expires for the 2025 return (generally 3 years after filing; https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records).
