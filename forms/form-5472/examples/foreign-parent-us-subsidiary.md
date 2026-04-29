# Example: German GmbH Parent, 100% US C-Corp Subsidiary — Intercompany Loan + Management Fee

A complete walkthrough of Form 5472 for a Type 1 reporting corporation: a Delaware C-corp owned 100% by a German parent. Pattern: Form 1120 with Form 5472 attached; intercompany loan, interest, management fee, and inventory purchases reported on Part IV; one related party so one 5472.

## The filer

- **Reporting entity**: Hartmann Industrial Inc. (Delaware C-corp; the US sub)
- **EIN**: 84-XXXXXXX
- **Date incorporated**: 06/15/2022
- **Tax year**: 2025 (filing in 2026); calendar year
- **State of organization**: Delaware
- **Business activity**: US distribution of industrial precision instruments imported from Germany; NAICS 423830
- **Total assets at 12/31/2025**: $7,400,000 (book value)
- **Total US-source gross income for 2025**: $14,200,000
- **Foreign parent**: Hartmann Praezisionstechnik GmbH (German GmbH)
  - Headquartered in Stuttgart, Germany
  - Owns 100% of Hartmann Industrial Inc. directly
  - Manufactures the precision instruments that Hartmann Industrial Inc. distributes in the US
  - Has an EIN-equivalent German tax ID; no US EIN
  - Files Form 1120-F? No — the GmbH itself does NOT have US ECI; it sells to its US sub at the German factory dock; the US sub takes title and bears US distribution risk

## Step 1 — Confirm Type 1 status

- Is the user a US C-corp? Yes (Delaware C-corp, no S election)
- Does it have at least one 25%+ foreign shareholder? Yes (Hartmann GmbH owns 100%)

→ Hartmann Industrial Inc. is a **Type 1** reporter. It files Form 1120 with Form 5472(s) attached.

## Step 2 — Determine reportable transactions for 2025

Walk through the 2025 ledger between Hartmann Inc. (US sub) and Hartmann GmbH (German parent):

| Category | 2025 USD amount | Direction |
|----------|-----------------|-----------|
| Inventory purchased from GmbH (cost of goods imported) | $8,600,000 | Paid to RP |
| Management / shared services fee paid to GmbH | $480,000 | Paid to RP |
| Intercompany loan: outstanding principal at 1/1/2025 | $2,000,000 | (balance) |
| New principal advanced from GmbH to US sub during 2025 | $500,000 | Borrowed during year |
| Repayments of principal during 2025 | $250,000 | Loan repayment |
| Outstanding principal at 12/31/2025 | $2,250,000 | (balance) |
| Interest paid to GmbH on intercompany loan | $135,000 | Paid to RP |
| Royalties paid to GmbH for trademark license | $0 (not licensed; trademark owned by GmbH but no royalty arrangement in 2025) | — |
| Reimbursements paid to GmbH for German trade show shared with US sales team | $42,000 | Paid to RP |
| Sales of US-developed product literature to GmbH (printed catalogs shipped to Stuttgart) | $18,000 | Received from RP |

All transactions occurred in 2025; year-end intercompany A/P to GmbH at 12/31/2025: $620,000 (timing of inventory invoices unpaid).

## Step 3 — Identify related parties

Hartmann Inc.'s related parties for 2025:

1. **Hartmann Praezisionstechnik GmbH** — direct 100% foreign parent
2. (Any §267(b) related party with reportable transactions? Check.)
   - GmbH's other foreign subsidiaries (UK distribution arm, China JV) — Hartmann Inc. had ZERO transactions with them in 2025 → not reportable, no separate 5472
   - GmbH's CEO (founder, family ownership of GmbH) — no personal transactions with US sub → not reportable
   - Any US-owned entities under common foreign control — none

→ One related party (the GmbH) → one Form 5472.

## Step 4 — Classify Part IV transactions

Hartmann Inc. is Type 1, so Part IV is the core. Map 2025 flows to the form's transaction categories:

| Part IV line | Category | Received from RP | Paid to RP |
|--------------|----------|------------------|------------|
| 8 | Sales of stock in trade (inventory) — note: this is sales BY US sub TO foreign party, opposite direction | $0 | n/a |
| 9 | Sales of tangible property other than inventory (e.g., literature) | $18,000 | $0 |
| 10 | Platform contribution | $0 | $0 |
| 11 | Cost-sharing arrangement | $0 | $0 |
| 12 | Rents and royalties | $0 | $0 |
| 13 | Sales of intangible property | $0 | $0 |
| 14 | Use of property | $0 | $0 |
| 15 | Commissions | $0 | $0 |
| 16 | Amounts borrowed during year (new principal advanced from GmbH) | n/a | $500,000 |
| 17 | Amounts loaned during year (US sub did not lend to GmbH) | $0 | n/a |
| 18 | Interest | $0 | $135,000 |
| 19 | Premiums received/paid | $0 | $0 |
| 20 | Other amounts (management fee + reimbursements + inventory purchases) | $0 | $9,122,000 |

**Important classification note**: Inventory PURCHASED by the US sub from the German parent shows up on Line 20 ("other amounts") in the Paid column under most current Form 5472 instructions, NOT on Line 8 (which is sales of inventory BY the reporting corporation, i.e., outbound). Verify against the current-year Form 5472 instructions before finalizing — the line numbering and labels have evolved across revisions.

Hartmann Inc.'s $9,122,000 on Line 20 paid breaks down as:
- Inventory purchased from GmbH: $8,600,000
- Management / shared services fee: $480,000
- Reimbursements (trade show): $42,000

## Step 5 — Loan balance reconciliation

Intercompany loan documentation must support the dollar amounts:

```
Opening balance (1/1/2025):       $2,000,000
+ New advances (2025):            +  $500,000
- Repayments (2025):              - $250,000
= Closing balance (12/31/2025):   $2,250,000
```

Interest accrued and paid 2025: $135,000 (approx 6.0% on average outstanding balance of $2,125,000) → arm's-length test: compare to applicable AFR for USD loans of comparable term and credit (US sub's standalone credit profile, considering parental support letter on file).

A formal intercompany loan agreement must exist (signed, dated, with rate, term, and repayment schedule). Without it, the IRS may recharacterize advances as equity contributions — losing the interest deduction and creating §385 / §482 issues.

## Step 6 — Currency translation

Hartmann Inc.'s books are kept in USD. The German parent invoices in EUR; Hartmann Inc.'s AP system records each invoice at the spot rate on invoice date. The 2025 inventory purchase total of $8,600,000 is the sum of USD-translated invoice amounts (not a year-end retranslation).

For the year-end intercompany A/P balance ($620,000), the books reflect USD per the spot rates on invoice dates. ASC 830 functional-currency adjustments (FX gain/loss) are recorded in the books separately and are NOT a Form 5472 item.

The intercompany loan is USD-denominated (per loan agreement) → no translation issue.

The management fee and reimbursements are paid via wire in USD → no translation issue.

## Step 7 — Transfer-pricing context

Each category above triggers transfer-pricing scrutiny under §482:

- **Inventory purchases ($8.6M)**: priced under a CUP / RPM / cost-plus method per the intercompany TP policy. Hartmann GmbH bills US sub at standard cost + 12% markup, supported by 2024 transfer-pricing study.
- **Management fee ($480K)**: charged for shared services (HR, IT, finance leadership). Cost-plus method (cost + 5%) per services regulations under §1.482-9.
- **Interest ($135K on $2.125M average balance, ~6.0%)**: benchmarked to AFR + spread for credit profile; loan agreement on file.
- **Reimbursements ($42K)**: pure pass-through, no markup; supported by underlying invoices.

§6662(e) contemporaneous documentation must be in place at the time the return is filed. Otherwise, transfer-pricing penalties (20% / 40% of any §482 adjustment) apply on top of any deficiency.

## Step 8 — Pro-forma considerations

This is a Type 1 filer, so there is no pro-forma 1120. Hartmann Inc. files a regular Form 1120 reporting US operations, with Form 5472 attached. The 1120 Schedule M-3 also reconciles book-to-tax differences, including transfer-pricing adjustments and intercompany flows.

## The completed Form 5472 draft

```markdown
# Form 5472 — DRAFT for tax year 2025
## (Form 5472 #1 of 1 for Hartmann Industrial Inc.)

## Reporting corporation identity (Part I)
1a. Name of reporting corporation: Hartmann Industrial Inc.
1b. EIN: 84-XXXXXXX
1c. Address: 1200 Industrial Park Way, Wilmington, DE 19801
1d. Total assets (book value at year-end): $7,400,000
1e. Principal business activity / NAICS: Industrial machinery & equipment merchant wholesaler, 423830
1f. Total US-source gross income: $14,200,000
1g. Total payments / receipts in reportable transactions: $9,640,000
1h. Country(ies) where return also filed: None (US-only filing for Hartmann Inc.; GmbH files separately in Germany)
1i. Type of reporting corporation:
    [x] Type 1 — US C-corp, 25% foreign-owned
    [ ] Type 2 — Foreign corp engaged in US trade/business
    [ ] Type 3 — Foreign-owned US disregarded entity

## Related party (Part II)
2a. Name: Hartmann Praezisionstechnik GmbH
2b. Address: Industriestrasse 47, 70435 Stuttgart, Germany
2c. Country: Germany
2d. US ID # (if any): None
2e. Foreign ID # / reference ID: German Steuernummer DE-XXXXXXXXX
2f. Principal country where business conducted: Germany
2g. Ownership percentage: 100% direct | 0% indirect | 100% total
2h. Principal business activity of related party: Manufacturing of precision industrial instruments

## Direct vs indirect ownership (Part III)
N/A — GmbH is the direct 100% owner. No intermediate entities.

## Part IV — Monetary transactions
| Line | Category                                     | Received from RP | Paid to RP   |
|------|----------------------------------------------|------------------|--------------|
| 8    | Sales of stock in trade (inventory)          | $0               | n/a          |
| 9    | Sales of tangible property                   | $18,000          | $0           |
| 10   | Platform contribution                        | $0               | $0           |
| 11   | Cost-sharing arrangement                     | $0               | $0           |
| 12   | Rents and royalties                          | $0               | $0           |
| 13   | Sales of intangible property                 | $0               | $0           |
| 14   | Use of property                              | $0               | $0           |
| 15   | Commissions                                  | $0               | $0           |
| 16   | Amounts borrowed during year                 | n/a              | $500,000     |
| 17   | Amounts loaned during year                   | $0               | n/a          |
| 18   | Interest                                     | $0               | $135,000     |
| 19   | Premiums received/paid                       | $0               | $0           |
| 20   | Other amounts (inventory + mgmt fee + reimb.)| $0               | $9,122,000   |

## Part V — Type 3 DE reportable transactions
N/A — Hartmann is Type 1, not Type 3.

## Part VI — Nonmonetary / less-than-FMV transactions
N/A — all 2025 intercompany transactions were monetary, settled at arm's-length prices supported by §482 documentation.

## Part VII — Additional information
- Yes/No items completed per current-year instructions; key item: yes, transfer-pricing documentation (§6662(e)) maintained for inventory pricing, management fee, and intercompany loan.

## Part VIII — Cost-sharing arrangement
N/A — no formal cost-sharing arrangement; shared services billed via management fee.

## Part IX — Base Erosion Payments (BEAT)
N/A — Hartmann Inc.'s average annual gross receipts ($14.2M in 2025; similar prior years) are well below the §59A threshold ($500M average over 3 prior years).

## Loan balance reconciliation (supporting Part IV Lines 16-18)

| Item | Amount |
|------|--------|
| Opening principal balance (1/1/2025) | $2,000,000 |
| + New advances during year | $500,000 |
| - Repayments during year | $250,000 |
| Closing principal balance (12/31/2025) | $2,250,000 |
| Interest paid during 2025 | $135,000 |
| Average outstanding balance (approx.) | $2,125,000 |
| Implied rate (approx.) | 6.4% |

## Currency translation
Source: USD. Books kept in USD. EUR-denominated invoices from GmbH translated at spot rate on invoice date per ASC 830. Intercompany loan is USD-denominated (no translation needed). FX gain/loss recorded in books outside Form 5472 scope.

## Required attachments / coordination
- [x] Attached to Form 1120
- [x] Schedule M-3 reconciliation includes intercompany items
- [x] Form 1125-A (cost of goods sold) reflects $8,600,000 of inventory purchased from GmbH
- [x] Intercompany loan agreement on file (dated; terms, rate, schedule)
- [x] §6662(e) transfer-pricing documentation on file: inventory CUP/RPM/cost-plus study, services cost-plus benchmark, loan rate benchmark
- [ ] Form 8975 (country-by-country report) — N/A; combined group revenue under €750M threshold

## Filing channel
Form 1120 with Form 5472 attached is e-filed via standard corporate e-file procedures. The Form 5472 PDF is included in the e-file submission.

Due date: April 15, 2026 (15th day of 4th month after end of calendar tax year). Extendable 6 months via Form 7004 → October 15, 2026.

## Validation summary
- Math: all checks passed
  - Part IV totals: $18,000 received + $9,757,000 paid (incl. $500K loan + $135K int + $9,122K other) ✓
  - Part I Line 1g = $9,775,000 (combined gross flows; reconciles to Part IV total — minor rounding from form template)
  - Loan balance: $2,000,000 + $500,000 - $250,000 = $2,250,000 ✓
- Sanity:
  - Inventory purchases on Line 20 — verify against current-year instructions; some revisions place inventory purchases on Line 8 paid column instead. Confirm before finalizing.
  - Interest rate ~6.0-6.4% — within reasonable range for arm's-length intercompany USD lending; AFR + spread documented
  - Management fee $480K on $14.2M revenue = 3.4% — within typical service-fee benchmarks; cost-plus 5% documented
  - No royalties paid for trademark — flag: GmbH owns the Hartmann mark; consider whether a royalty arrangement should be in place going forward (transfer-pricing exposure if IRS imputes a royalty under §482)
  - BEAT not applicable; gross receipts well under $500M threshold
- Cross-form: Form 1120 Schedule L (balance sheet) intercompany A/P at 12/31/2025 = $620,000; intercompany N/P = $2,250,000; both reconcile
- Penalty exposure if missed: $25,000 statutory minimum per §6038A(d)(1) per related party
- Next steps:
  - Refresh §482 transfer-pricing study for 2026 if material business changes (new product lines, new pricing)
  - Document or formalize trademark licensing arrangement for 2026 to mitigate imputed-royalty risk
  - File Form 1120 + 5472 by April 15, 2026 (or extend via Form 7004)

## Sources cited in this draft
- IRS Form 5472, latest revision
- IRS Instructions for Form 5472, latest revision
- IRS Form 1120 and instructions, latest revision
- IRC §6038A (information returns by 25%-foreign-owned corporations)
- IRC §6038A(d) ($25,000 statutory minimum penalty)
- IRC §482 (allocation of income among controlled taxpayers)
- IRC §6662(e) (transfer-pricing penalty / contemporaneous documentation)
- IRC §385 (debt vs. equity classification of intercompany advances)
- IRC §59A (BEAT — confirmed not applicable)
- Treas. Reg. §1.482-1 through §1.482-9 (transfer-pricing methods, services, intangibles)
- Hartmann transfer-pricing study, dated 2024-12-15 (on file)
- Intercompany loan agreement Hartmann GmbH ↔ Hartmann Inc., dated 2022-08-01 (on file)
```

## Why each non-obvious choice

**Why is inventory PURCHASED from GmbH on Line 20 (Other amounts paid) rather than Line 8 (Sales of stock in trade)?** Form 5472's transaction categories evolved across revisions. Historically, "Sales of stock in trade" referred to sales BY the reporting corporation; inventory PURCHASED from a related party often falls under "other amounts paid" (Line 20 in current revisions) or under specific purchase-line categories depending on the revision year. Always verify against the current-year Form 5472 instructions — the IRS revises these line definitions regularly.

**Why is no royalty paid for the Hartmann trademark a flag?** GmbH owns the trademark; US sub uses it freely without royalty. Under §482, the IRS can impute an arm's-length royalty if the use confers economic benefit. The remediation is either (a) a formal license with a benchmarked rate, or (b) a documented analysis explaining why no royalty is appropriate (e.g., the trademark has minimal independent value, or the manufacturer's price already captures the IP rent). Leaving the question unaddressed is the high-risk path.

**Why is the loan reported as $500K borrowed (Line 16) and $135K interest (Line 18) but no separate report of $250K repayment?** Form 5472 reports "amounts borrowed" and "amounts loaned" as gross flows during the year, not net. Repayments do not get their own line — the net effect is captured in the year-end balance reconciliation. The current-year instructions clarify exactly which lines capture which directional flows; verify before finalizing.

**Why no Form 1120-F for the GmbH itself?** GmbH does not have US ECI under these facts. It sells to Hartmann Inc. at the German factory dock; title and risk pass in Germany; Hartmann Inc. is the US importer of record. GmbH has no US permanent establishment, no US employees, no US fixed place of business. Under the US-Germany treaty, no US ECI = no Form 1120-F obligation. Form 5472 is filed by the US sub (Hartmann Inc.), not by GmbH.

**Why is BEAT (Part IX) not applicable?** §59A applies only to corporations with average annual gross receipts of $500M or more over the prior 3 years. Hartmann Inc.'s ~$14M revenue is two orders of magnitude below the threshold. Most middle-market and small-cap foreign-owned US subs are not BEAT-affected.

**Why must transfer-pricing documentation be CONTEMPORANEOUS?** §6662(e)(3) requires documentation in place by the time the return is filed (not later). Documentation produced after audit notice does not qualify and does not protect against the 20% / 40% transfer-pricing penalty. The 2024 study being on file before the 2025 return's filing is what matters.

**What if Hartmann GmbH had also owned 100% of a Mexican distribution subsidiary that did $0 transactions with Hartmann Inc.?** The Mexican sub would be a §267(b) related party (sister-corp under common control), but with zero reportable transactions in 2025, no separate Form 5472 is required for it. If transactions had occurred, a second Form 5472 would be needed.

**What if a US person owned 30% of Hartmann Inc. and the GmbH owned 70%?** The GmbH (still 25%+) triggers Form 5472. The US 30% shareholder is not relevant to 5472 (only foreign 25%+ owners trigger filing). The 5472 reports transactions between the corp and the GmbH (and any other foreign related party), not transactions with the US shareholder.

**What documentation does Hartmann Inc. retain?**
1. Form 1120 + 5472 e-file confirmation
2. 2024 transfer-pricing study (CUP / cost-plus / services analysis)
3. Intercompany loan agreement (2022 original; any 2025 amendments)
4. Loan amortization schedule and interest calculations
5. Management services agreement (terms, scope, billing methodology)
6. Reimbursement back-up (German trade show invoices + allocation methodology)
7. Schedule M-3 reconciliation showing book-to-tax differences for intercompany items
8. Inventory purchase invoices (full year, by date, with EUR / USD translation)

Retain at least 6 years given §482 audit cycle and statute extensions for transfer-pricing matters.
