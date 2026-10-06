# Example: German GmbH Parent, 100% US C-Corp Subsidiary — Intercompany Loan + Management Fee

A complete walkthrough of Form 5472 for a Type 1 reporting corporation: a Delaware C-corp owned 100% by a German parent. Pattern: Form 1120 with Form 5472 attached; intercompany loan, interest, management fee, and inventory purchases reported on Part IV; one related party so one 5472.

## The filer

- **Reporting entity**: Hartmann Industrial Inc. (Delaware C-corp; the US sub)
- **EIN**: 84-XXXXXXX
- **Date incorporated**: 06/15/2022
- **Tax year**: 2025 (filing in 2026); calendar year
- **State of organization**: Delaware
- **Business activity**: US distribution of industrial precision instruments imported from Germany; Form 1120 principal business activity code 423800 (Machinery, Equipment, & Supplies merchant wholesalers, Instructions for Form 1120 (2025) code list)
- **Total assets at 12/31/2025**: $7,400,000 (book value)
- **Total US-source gross income for 2025**: $14,200,000
- **Foreign parent**: Hartmann Praezisionstechnik GmbH (German GmbH)
  - Headquartered in Stuttgart, Germany
  - Owns 100% of Hartmann Industrial Inc. directly
  - Manufactures the precision instruments that Hartmann Industrial Inc. distributes in the US
  - Has a German tax number (Steuernummer); no US EIN
  - Owned 60% by its founder, Klaus Hartmann (German citizen and resident), 40% by unrelated German investors
  - Files Form 1120-F? No — the GmbH itself does NOT have US ECI; it sells to its US sub at the German factory dock; the US sub takes title and bears US distribution risk

## Step 1 — Confirm Type 1 status

- Is the user a US C-corp? Yes (Delaware C-corp, no S election)
- Does it have at least one 25%+ foreign shareholder? Yes (Hartmann GmbH owns 100%; Klaus Hartmann owns 60% × 100% = 60% indirectly)

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

1. **Hartmann Praezisionstechnik GmbH** — direct 100% foreign parent (Part II lines 4a–4e)
   - Klaus Hartmann is the ultimate indirect 25% foreign shareholder (Part II lines 6a–6e, with an attached attribution explanation); he had no personal transactions with Hartmann Inc., so he gets no Form 5472 of his own
2. (Any §267(b) related party with reportable transactions? Check.)
   - GmbH's other foreign subsidiaries (UK distribution arm, China JV) — Hartmann Inc. had ZERO transactions with them in 2025 → not reportable, no separate 5472
   - GmbH's CEO (founder, family ownership of GmbH) — no personal transactions with US sub → not reportable
   - Any US-owned entities under common foreign control — none

→ One related party (the GmbH) → one Form 5472.

## Step 4 — Classify Part IV transactions

Hartmann Inc. is Type 1, so Part IV is the core. Form 5472 (Rev. December 2023) has a "received" block (lines 9–22) and a separate "paid" block (lines 23–36):

| Line | Category | Amount |
|------|----------|--------|
| 10 | Sales of tangible property other than stock in trade (catalogs sold to GmbH) | $18,000 |
| 17a | Amounts borrowed — beginning balance (outstanding balance method) | $2,000,000 |
| 17b | Amounts borrowed — ending balance | $2,250,000 |
| 22 | Total received (lines 9–21) | $2,268,000 |
| 23 | Purchases of stock in trade (inventory imported from GmbH) | $8,600,000 |
| 29 | Consideration paid for technical, managerial, ... services (shared-services fee) | $480,000 |
| 32 | Interest paid | $135,000 |
| 35 | Other amounts paid (trade-show cost reimbursement) | $42,000 |
| 36 | Total paid (lines 23–35) | $9,257,000 |

Every other line is $0. Notes:
- Inventory purchased from the parent goes on line 23, not on line 9 (line 9 is the corporation's own sales of inventory to the related party).
- The loan is reported as balances on lines 17a/17b, not as advances and repayments. The form puts 17b in the amount column; the plain reading includes it in line 22 (and so in line 1f). The instructions do not say this expressly, so the agent states the convention in the draft and asks the preparer to confirm. Without 17b, line 22 would be $18,000 and line 1f $9,275,000.
- Line 32: report interest paid or accrued, limited to the amount deductible under §163(j). Hartmann Inc.'s average annual gross receipts ($14.2M) are under the 2025 §448(c) threshold of $31,000,000 (Rev. Proc. 2024-40 §2.31), so §163(j) does not limit it and the full $135,000 goes on line 32 (Instructions for Form 5472, Line 32; confirm the small-business exemption with the CPA).

## Step 5 — Loan balance reconciliation

Intercompany loan documentation must support the dollar amounts:

```
Opening balance (1/1/2025):       $2,000,000
+ New advances (2025):            +  $500,000
- Repayments (2025):              - $250,000
= Closing balance (12/31/2025):   $2,250,000
```

Interest accrued and paid 2025: $135,000 (approx 6.35% on average outstanding balance of $2,125,000) → arm's-length test: compare to applicable AFR for USD loans of comparable term and credit (US sub's standalone credit profile, considering parental support letter on file).

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
- **Interest ($135K on $2.125M average balance, ~6.35%)**: benchmarked to AFR + spread for credit profile; loan agreement on file. Part VII line 42a/42b asks whether the rate is inside or outside the 100%–130% of AFR safe-haven range of Treas. Reg. §1.482-2(a)(2)(iii)(B); the CPA compared the rate with the AFR for the loan's term in the month each advance was made and determined it is outside that range (42b Yes), which is why the arm's-length benchmark matters.
- **Reimbursements ($42K)**: pure pass-through, no markup; supported by underlying invoices.

§6662(e)(3)(B) documentation must exist when the return is filed to avoid the transfer-pricing penalty (20% of the underpayment under §6662(e), 40% for a gross valuation misstatement under §6662(h)) on any §482 adjustment.

## Step 8 — Pro-forma considerations

This is a Type 1 filer, so there is no pro-forma 1120. Hartmann Inc. files a regular Form 1120 reporting US operations, with Form 5472 attached. With total assets under $10 million it reconciles book to tax on Schedule M-1 rather than Schedule M-3 (Instructions for Form 1120, Schedule M-3 threshold).

## The completed Form 5472 draft

```markdown
# Form 5472 — DRAFT for tax year 2025
## (Form 5472 #1 of 1 for Hartmann Industrial Inc.)
Form revision: Form 5472 (Rev. December 2023); Instructions (Rev. December 2024)
Tax year: beginning 01/01/2025, ending 12/31/2025

## Part I — Reporting corporation
1a. Name and address: Hartmann Industrial Inc., 1200 Industrial Park Way, Wilmington, DE 19801
1b. EIN: 84-XXXXXXX
1c. Total assets: $7,400,000 (Form 1120 Schedule L, line 15, column (d))
1d. Principal business activity: Machinery, equipment, & supplies merchant wholesaler
1e. Principal business activity code: 423800
1f. Total value of gross payments on this form: $11,525,000 (line 22 $2,268,000 + line 36 $9,257,000; includes the line 17b balance — convention confirmed with preparer)
1g. Total number of Forms 5472 filed: 1
1h. Total value on all Forms 5472: $11,525,000
1i. Consolidated filing: [ ]
1j. Initial year: [ ] (first filed for 2022)
1k. Number of Parts VIII: 0
1l. Country of incorporation: United States
1m. Date of incorporation: 06/15/2022
1n. Country(ies) where it files an income tax return as a resident: United States
1o. Principal country(ies) where business is conducted: United States
2.  Foreign person owned ≥ 50% at any time: [x]
3.  Foreign-owned U.S. DE: [ ]

## Part II — 25% foreign shareholders
Surrogate foreign corporation box: [ ]
4a. Hartmann Praezisionstechnik GmbH, Industriestrasse 47, 70435 Stuttgart, Germany
4b(1) U.S. ID: (none)  4b(2) Reference ID: HARTMANNGMBH01  4b(3) FTIN: German tax number XXXXXXXXXXX
4c. Principal country of business: Germany  4d. Country of organization: Germany  4e. Tax residence: Germany
5a–5e. None
6a. Klaus Hartmann, <home address>, Stuttgart, Germany (ultimate indirect 25% foreign shareholder; 60% through the GmbH — attribution statement attached)
6b(1) U.S. ID: (none)  6b(2) Reference ID: KHARTMANN01  6b(3) FTIN: German tax ID XXXXXXXXXXX
6c. Principal country of business: Germany  6d. Citizenship: Germany  6e. Tax residence: Germany
7a–7e. None

## Part III — Related party
[x] foreign person  [ ] U.S. person
8a. Hartmann Praezisionstechnik GmbH, Industriestrasse 47, 70435 Stuttgart, Germany
8b(1) U.S. ID: (none)  8b(2) Reference ID: HARTMANNGMBH01  8b(3) FTIN: German tax number XXXXXXXXXXX
8c. Principal business activity: Manufacturing of navigational, measuring, and control instruments  8d. Code: 334500
8e. Relationship: [x] 25% foreign shareholder
8f. Principal country of business: Germany  8g. Tax residence: Germany

## Part IV — Monetary transactions
Estimates used: [ ]
| Line | Item | Amount |
|------|------|--------|
| 9 | Sales of stock in trade | $0 |
| 10 | Sales of tangible property other than stock in trade (catalogs) | $18,000 |
| 11–16 | Platform contribution, cost sharing, rents, royalties, intangibles, services, commissions received | $0 |
| 17a | Amounts borrowed — beginning balance | $2,000,000 |
| 17b | Amounts borrowed — ending balance | $2,250,000 |
| 18–21 | Interest, premiums, guarantee fees, other received | $0 |
| 22 | Total received | $2,268,000 |
| 23 | Purchases of stock in trade | $8,600,000 |
| 24–28 | Other tangible property, platform contribution, cost sharing, rents, royalties, intangibles paid | $0 |
| 29 | Consideration paid for managerial and like services | $480,000 |
| 30 | Commissions paid | $0 |
| 31a/31b | Amounts loaned | $0 |
| 32 | Interest paid (not limited by §163(j)) | $135,000 |
| 33–34 | Premiums, loan guarantee fees paid | $0 |
| 35 | Other amounts paid (trade-show reimbursement) | $42,000 |
| 36 | Total paid | $9,257,000 |

## Part V — Foreign-owned U.S. DE transactions
Not applicable (box not checked; Hartmann Inc. is not a DE).

## Part VI — Nonmonetary / less-than-full-consideration transactions
Box not checked — all 2025 intercompany transactions were monetary.

## Part VII — Additional information
37. Imports goods from a foreign related party: Yes
38a. Basis or inventory cost greater than customs value: No (confirmed against the customs entries)
39. Foreign parent in a CSA: No
40a. §267A disallowed interest or royalty: No
41a. FDII deduction: No
42a. Loan within the 100%–130% AFR safe-haven range: No
42b. Loan outside that range: Yes (CPA determination; arm's-length benchmark on file)
43a. §385 covered debt instrument / related distribution or acquisition: No (no distributions or acquisitions in the 36-month window; confirmed with CPA)

## Part VIII — Cost sharing arrangement
N/A (line 1k = 0)

## Part IX — Base erosion payments
Not an applicable taxpayer under §59A (average annual gross receipts far below $500 million); lines 50–52 left blank on the CPA's instruction.

## Currency translation
Books in USD. EUR invoices from GmbH recorded at the spot rate on invoice date; schedule of exchange rates used attached (Instructions for Form 5472, Part IV). Loan is USD-denominated.

## Required attachments / coordination
- [x] Part of the Form 1120 return
- [x] Attribution statement for Klaus Hartmann (Part II line 6a)
- [x] Exchange-rate schedule
- [x] Form 1125-A (cost of goods sold) reflects the $8,600,000 of inventory purchased from GmbH
- [x] Schedule M-3 only if total assets ≥ $10 million (Instructions for Form 1120); Hartmann Inc. ($7.4M) uses Schedule M-1
- [x] Intercompany loan agreement and §6662(e) transfer-pricing documentation on file
- [ ] Form 8975 (country-by-country report) — N/A: filed only by the U.S. ultimate parent of a U.S. MNE group with revenue of $850 million or more (Instructions for Form 8975); Hartmann Inc. is a subsidiary of a German parent

## Filing channel
Form 5472 is part of the Form 1120 return and is e-filed with it.

Due date: April 15, 2026 (15th day of the 4th month after the calendar tax year ends). Extendable 6 months via Form 7004 → October 15, 2026.

## Validation summary
- Math (python, /tmp/jupid-skills-work/calc/g4-5472-hartmann.py):
  - Line 22 = $18,000 + $2,250,000 = $2,268,000 ✓
  - Line 36 = $8,600,000 + $480,000 + $135,000 + $42,000 = $9,257,000 ✓
  - Line 1f = $2,268,000 + $9,257,000 = $11,525,000 ✓; 1h = 1f (one form) ✓
  - Loan: $2,000,000 + $500,000 − $250,000 = $2,250,000 = line 17b ✓
- Sanity:
  - Interest ~6.35% on average balance; outside the AFR safe haven, so the benchmark study carries the arm's-length support
  - Shared-services fee $480K on $14.2M revenue = 3.4%; cost plus 5% per the services study
  - No royalty paid for the Hartmann trademark — flag (see below)
  - Part VII answered line by line; Part II lists the ultimate indirect owner
- Penalty exposure if missed: $25,000 per related party per year (§6038A(d)(1))
- Next steps:
  - Refresh the §482 study for 2026 if material business changes
  - Decide on a trademark license or documented no-royalty analysis for 2026
  - File Form 1120 + 5472 by April 15, 2026 (or extend via Form 7004)

## Sources cited in this draft
- IRS Form 5472 (Rev. December 2023) and Instructions (Rev. December 2024)
- 2025 Form 1120 and Instructions (principal business activity codes; Schedule M-3 threshold)
- IRC §6038A, §6038A(d), §482, §6662(e)/(h), §163(j), §448(c), §385, §59A
- Rev. Proc. 2024-40 §2.31 (2025 §448(c) gross receipts threshold $31,000,000)
- Treas. Reg. §1.482-2(a)(2)(iii)(B) (AFR safe haven), §1.482-1 through §1.482-9
- Instructions for Form 8975 ($850 million threshold)
- Hartmann transfer-pricing study, dated 2024-12-15 (on file)
- Intercompany loan agreement Hartmann GmbH ↔ Hartmann Inc., dated 2022-08-01 (on file)
```

## Why each non-obvious choice

**Why is inventory purchased from GmbH on line 23?** Form 5472 (Rev. December 2023) has a dedicated line for it: line 23, "Purchases of stock in trade (inventory)", in the paid block. Line 9 is the mirror line for the reporting corporation's own sales of inventory to the related party; "other amounts paid" (line 35) is only for amounts not reported on lines 23–34.

**Why is no royalty paid for the Hartmann trademark a flag?** GmbH owns the trademark; US sub uses it freely without royalty. Under §482, the IRS can impute an arm's-length royalty if the use confers economic benefit. The remediation is either (a) a formal license with a benchmarked rate, or (b) a documented analysis explaining why no royalty is appropriate (e.g., the trademark has minimal independent value, or the manufacturer's price already captures the IP rent). Leaving the question unaddressed is the high-risk path.

**Why is the loan reported as balances ($2,000,000 on 17a, $2,250,000 on 17b) and not as $500K advanced / $250K repaid?** The instructions for line 17 say to report amounts borrowed, including borrowings in place at the start of the year, using either the outstanding balance method (17a beginning, 17b ending) or the monthly average method (17b only). Advances and repayments do not get their own lines. Interest paid goes on line 32.

**Why no Form 1120-F for the GmbH itself?** GmbH does not have US ECI under these facts. It sells to Hartmann Inc. at the German factory dock; title and risk pass in Germany; Hartmann Inc. is the US importer of record. GmbH has no US permanent establishment, no US employees, no US fixed place of business. Under the US-Germany treaty, no US ECI = no Form 1120-F obligation. Form 5472 is filed by the US sub (Hartmann Inc.), not by GmbH.

**Why is BEAT (Part IX) not applicable?** §59A(e) reaches only corporations with average annual gross receipts of at least $500 million over the prior 3 years (and a base erosion percentage of 3% or more). Hartmann Inc.'s ~$14M revenue is far below the threshold.

**Why must transfer-pricing documentation be CONTEMPORANEOUS?** §6662(e)(3)(B) requires the documentation to exist when the return is filed and to be provided within 30 days of an IRS request. Documentation produced after an audit notice does not protect against the 20% (§6662(e)) / 40% (§6662(h)) penalty. The 2024 study being on file before the 2025 return's filing is what matters.

**What if Hartmann GmbH had also owned 100% of a Mexican distribution subsidiary that did $0 transactions with Hartmann Inc.?** The Mexican sub would be a §267(b) related party (sister-corp under common control), but with zero reportable transactions in 2025, no separate Form 5472 is required for it. If transactions had occurred, a second Form 5472 would be needed.

**What if a US person owned 30% of Hartmann Inc. and the GmbH owned 70%?** The GmbH (still 25%+) triggers Form 5472. The US 30% shareholder is not relevant to 5472 (only foreign 25%+ owners trigger filing). The 5472 reports transactions between the corp and the GmbH (and any other foreign related party), not transactions with the US shareholder.

**What documentation does Hartmann Inc. retain?**
1. Form 1120 (with Form 5472) e-file acknowledgment
2. 2024 transfer-pricing study (CUP / cost-plus / services analysis)
3. Intercompany loan agreement (2022 original; any 2025 amendments)
4. Loan amortization schedule and interest calculations
5. Management services agreement (terms, scope, billing methodology)
6. Reimbursement back-up (German trade show invoices + allocation methodology)
7. Schedule M-3 reconciliation showing book-to-tax differences for intercompany items
8. Inventory purchase invoices (full year, by date, with EUR / USD translation)

Keep the records as long as they may be relevant or material to the §6038A transactions, and never less than the assessment period (Treas. Reg. §1.6038A-3(g)).
