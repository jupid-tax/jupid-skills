# Example: 60/40 US-Foreign C-Corp Joint Venture — Multiple Part IV Transactions

A complete walkthrough of Form 5472 for a Type 1 reporting corporation that is majority US-owned but has a 40% Canadian shareholder. Pattern: Form 1120 with Form 5472 attached for the 40% Canadian related party; Part IV captures multiple intercompany transactions (services, royalties, loans, equipment lease).

The 40% foreign ownership is enough to trigger Form 5472 — not just 50%+. Many users miss this.

## The filer

- **Reporting entity**: NorthCoast Software Inc. (Delaware C-corp; the joint venture)
- **EIN**: 87-XXXXXXX
- **Date incorporated**: 04/12/2023
- **Tax year**: 2025 (filing in 2026); calendar year
- **State of organization**: Delaware
- **Business activity**: B2B SaaS for logistics fleet management; NAICS 511210
- **Total assets at 12/31/2025**: $4,200,000 (book value)
- **Total US-source gross income for 2025**: $6,800,000

### Cap table

| Shareholder | Country | Ownership |
|-------------|---------|-----------|
| HarborCap Ventures LLC (Delaware VC; all US LPs) | US | 60% |
| Maple Tech Holdings Inc. (Ontario, Canada; private holdco of Canadian founder Marc Tremblay) | Canada | 40% |

Maple Tech is a Canadian-controlled private corporation (CCPC) wholly owned by Marc Tremblay (Canadian citizen and resident). Maple Tech contributed Canadian-developed core IP (the original software platform) to NorthCoast at formation in 2023 in exchange for 40% common stock plus an ongoing royalty.

## Step 1 — Confirm Type 1 status

- Is the user a US C-corp? Yes (Delaware C-corp, no S election)
- Does it have at least one 25%+ foreign shareholder? Yes (Maple Tech 40%)

→ NorthCoast Software Inc. is a **Type 1** reporter. It files Form 1120 with Form 5472 attached.

The 60% US ownership is irrelevant for the 5472 trigger — any foreign shareholder at 25%+ is enough. HarborCap (60% US) does NOT need a 5472 for itself; only foreign related parties do.

## Step 2 — Determine reportable transactions for 2025

Walk through the 2025 ledger between NorthCoast and Maple Tech:

| Category | 2025 USD amount | Direction |
|----------|-----------------|-----------|
| Royalty paid to Maple Tech for IP licensed (8% of subscription revenue) | $544,000 | Paid to RP |
| Engineering services paid to Maple Tech (Canadian engineers seconded under MSA) | $720,000 | Paid to RP |
| Equipment lease: NorthCoast leases data-center hardware from Maple Tech (Toronto colo) | $96,000 | Paid to RP |
| Intercompany loan: opening balance 1/1/2025 | $300,000 | (balance) |
| Loan repayment during 2025 | $100,000 | Loan repayment |
| Outstanding principal at 12/31/2025 | $200,000 | (balance) |
| Interest paid to Maple Tech on intercompany loan | $18,000 | Paid to RP |
| Sales of US-developed customer success playbooks licensed to Maple Tech | $24,000 | Received from RP |
| Capital contribution from Maple Tech (no — already done at 2023 formation) | $0 | n/a |
| Distributions to Maple Tech (no dividends declared in 2025) | $0 | n/a |

Year-end intercompany A/P to Maple Tech at 12/31/2025: $115,000 (royalty Q4 unpaid + October service invoices).

## Step 3 — Identify related parties

NorthCoast's related parties for 2025:

1. **Maple Tech Holdings Inc.** — direct 40% foreign shareholder
2. **Marc Tremblay** — sole shareholder of Maple Tech; under §318 / §6038A constructive ownership rules, Marc indirectly owns 40% of NorthCoast through Maple Tech. Did Marc himself transact with NorthCoast in 2025?
   - Marc serves on NorthCoast's board (uncompensated for 2025; director's fees waived per board resolution)
   - No direct loans, no direct payments → Marc as an INDIVIDUAL had zero reportable transactions with NorthCoast in 2025
   - No separate Form 5472 needed for Marc (no transactions)

3. HarborCap Ventures LLC — US shareholder, not foreign → no 5472 obligation regardless of transactions

→ One Form 5472 needed (for Maple Tech only).

If Marc's family trust had transacted with NorthCoast, a separate 5472 for the trust might be required. If Maple Tech's other Canadian subsidiaries had transacted with NorthCoast, separate 5472s for those subs would be required. Always test each potential related party independently.

## Step 4 — Classify Part IV transactions

Map 2025 flows to Part IV categories:

| Part IV line | Category | Received from RP | Paid to RP |
|--------------|----------|------------------|------------|
| 8 | Sales of stock in trade (inventory) | $0 | $0 |
| 9 | Sales of tangible property other than inventory | $0 | $0 |
| 10 | Platform contribution | $0 | $0 |
| 11 | Cost-sharing arrangement | $0 | $0 |
| 12 | Rents and royalties | $0 | $544,000 |
| 13 | Sales of intangible property | $24,000 | $0 |
| 14 | Use of property (equipment lease from Maple Tech) | $0 | $96,000 |
| 15 | Commissions | $0 | $0 |
| 16 | Amounts borrowed during year | n/a | $0 |
| 17 | Amounts loaned during year | $0 | n/a |
| 18 | Interest | $0 | $18,000 |
| 19 | Premiums received/paid | $0 | $0 |
| 20 | Other amounts (engineering services + reimbursements) | $0 | $720,000 |

**Royalties on Line 12**: $544,000 paid to Maple Tech for trademark + software IP licensed. The royalty is calculated as 8% of subscription revenue per a 2023 license agreement.

**Equipment lease on Line 14 ("Use of property")**: $96,000 paid for the Toronto data-center hardware Maple Tech owns and leases to NorthCoast. The lease is at arm's-length monthly rates supported by a third-party comparable colocation pricing study.

**Engineering services on Line 20**: $720,000 paid for Canadian engineers seconded to NorthCoast under a master services agreement. Cost-plus 8% per §1.482-9. Not a Line 14 (use of property) item — services are personal effort, not property use.

**Sales of intangibles (Line 13)**: $24,000 received from Maple Tech for customer-success playbooks NorthCoast developed and licensed back. Small but reportable.

## Step 5 — Loan balance reconciliation

```
Opening balance (1/1/2025):       $300,000
+ New advances (2025):            +$0
- Repayments (2025):              -$100,000
= Closing balance (12/31/2025):   $200,000
```

Interest paid 2025: $18,000 (approx 7.2% on average outstanding balance of $250,000) — benchmarked to AFR + spread for NorthCoast's standalone credit. Loan agreement on file dated 2024-09-01; original advance was made by Maple Tech to support working capital pre-Series A.

## Step 6 — Currency translation

NorthCoast keeps books in USD (its functional currency under ASC 830). Maple Tech invoices in CAD; NorthCoast translates each invoice at the spot rate on invoice date. The $544K royalty, $720K services, $96K lease, and $18K interest are sums of USD-translated CAD amounts.

The intercompany loan was advanced in USD per agreement → no translation issue on loan principal.

For the year-end intercompany A/P balance ($115,000), books reflect USD per spot rates on invoice dates. ASC 830 FX adjustments are recorded in the income statement separately and are NOT a Form 5472 item.

## Step 7 — Transfer-pricing analysis

Each major flow has §482 documentation:

- **Royalty (8% of subscription revenue, $544K)**: comparable license agreements in B2B SaaS yield royalty rates of 5-12% for core platform IP; 8% is within the range. CUP method primary; Profit Split as secondary check given the IP is critical to the business model.
- **Engineering services ($720K, cost+8%)**: cost-plus method per §1.482-9; benchmarked against comparable arms-length SaaS engineering services contracts.
- **Equipment lease ($96K, ~$8K/month)**: comparable colo pricing studies support the rate; lease term and equipment specs documented.
- **Loan interest ($18K, ~7.2%)**: AFR + 200bp spread for NorthCoast's standalone credit profile (Series A startup, limited operating history).

§6662(e) contemporaneous documentation is on file: 2024 study (covering 2024 and projected forward to 2025) plus 2025 update memo signed by NorthCoast's tax director and Maple Tech's controller.

A specific TP risk to flag: **the 8% royalty + 8% cost-plus services + lease + interest** combine to extract roughly 20% of subscription revenue from NorthCoast to Canada. The IRS may examine whether this aggregate burden produces an arm's-length result for NorthCoast. Documentation should specifically address the cumulative effect, not just per-transaction defenses.

## The completed Form 5472 draft

```markdown
# Form 5472 — DRAFT for tax year 2025
## (Form 5472 #1 of 1 for NorthCoast Software Inc.)

## Reporting corporation identity (Part I)
1a. Name of reporting corporation: NorthCoast Software Inc.
1b. EIN: 87-XXXXXXX
1c. Address: 1209 N Orange St, Wilmington, DE 19801 (registered) / 500 Howard St #800, San Francisco, CA 94105 (operations)
1d. Total assets (book value at year-end): $4,200,000
1e. Principal business activity / NAICS: Software publishers, 511210
1f. Total US-source gross income: $6,800,000
1g. Total payments / receipts in reportable transactions: $1,402,000
1h. Country(ies) where return also filed: None (US-only filing for NorthCoast)
1i. Type of reporting corporation:
    [x] Type 1 — US C-corp, 25% foreign-owned
    [ ] Type 2 — Foreign corp engaged in US trade/business
    [ ] Type 3 — Foreign-owned US disregarded entity

## Related party (Part II)
2a. Name: Maple Tech Holdings Inc.
2b. Address: 100 King St W, Suite 5300, Toronto, ON M5X 1C7, Canada
2c. Country: Canada
2d. US ID # (if any): None
2e. Foreign ID # / reference ID: Canadian Business Number (BN) XXXXXXXXX RC0001
2f. Principal country where business conducted: Canada
2g. Ownership percentage: 40% direct | 0% indirect | 40% total
2h. Principal business activity of related party: Holding company; original developer of NorthCoast software platform IP

## Direct vs indirect ownership (Part III)
N/A — Maple Tech is the direct 40% shareholder. (Marc Tremblay, the ultimate individual owner of Maple Tech, has no separate transactions with NorthCoast in 2025; constructive ownership disclosed informationally but no separate 5472 required.)

## Part IV — Monetary transactions
| Line | Category                                        | Received from RP | Paid to RP |
|------|-------------------------------------------------|------------------|------------|
| 8    | Sales of stock in trade (inventory)             | $0               | $0         |
| 9    | Sales of tangible property                      | $0               | $0         |
| 10   | Platform contribution                           | $0               | $0         |
| 11   | Cost-sharing arrangement                        | $0               | $0         |
| 12   | Rents and royalties                             | $0               | $544,000   |
| 13   | Sales of intangible property (playbooks)        | $24,000          | $0         |
| 14   | Use of property (equipment lease)               | $0               | $96,000    |
| 15   | Commissions                                     | $0               | $0         |
| 16   | Amounts borrowed during year                    | n/a              | $0         |
| 17   | Amounts loaned during year                      | $0               | n/a        |
| 18   | Interest                                        | $0               | $18,000    |
| 19   | Premiums received/paid                          | $0               | $0         |
| 20   | Other amounts (engineering services)            | $0               | $720,000   |

## Part V — Type 3 DE reportable transactions
N/A — NorthCoast is Type 1, not Type 3.

## Part VI — Nonmonetary / less-than-FMV transactions
N/A for 2025 — original 2023 IP contribution at formation was reported in 2023's Form 5472. No nonmonetary transactions in 2025.

## Part VII — Additional information
- Yes/No items completed per current-year instructions
- Key item: yes, transfer-pricing documentation (§6662(e)) maintained for all categories above
- Marc Tremblay disclosed as ultimate individual owner of Maple Tech for constructive-ownership transparency

## Part VIII — Cost-sharing arrangement
N/A — no formal CSA between NorthCoast and Maple Tech. The royalty + services structure intentionally avoids CSA mechanics (which would require platform contribution allocations under §1.482-7).

## Part IX — Base Erosion Payments (BEAT)
N/A — average annual gross receipts ($6.8M in 2025; similar prior years) are far below the §59A $500M threshold.

## Loan balance reconciliation (supporting Part IV Lines 16-18)

| Item | Amount |
|------|--------|
| Opening principal balance (1/1/2025) | $300,000 |
| + New advances during year | $0 |
| - Repayments during year | $100,000 |
| Closing principal balance (12/31/2025) | $200,000 |
| Interest paid during 2025 | $18,000 |
| Average outstanding balance | $250,000 |
| Implied rate | ~7.2% |

## Currency translation
Source: USD functional currency. CAD-denominated invoices from Maple Tech translated at spot rate on invoice date per ASC 830. Intercompany loan is USD-denominated (no translation). FX gain/loss recorded in book income statement outside Form 5472 scope.

## Required attachments / coordination
- [x] Attached to Form 1120
- [x] Schedule M-3 reconciliation includes intercompany items
- [x] Royalty license agreement (2023, Maple Tech ↔ NorthCoast) on file
- [x] Master services agreement (engineering secondment) on file
- [x] Equipment lease agreement (Toronto colo hardware) on file
- [x] Intercompany loan agreement (2024-09-01) on file
- [x] §6662(e) contemporaneous transfer-pricing study (2024) + 2025 update memo
- [ ] Form 8975 (CbC report) — N/A; group revenue under €750M
- [ ] Form 5471 — N/A (NorthCoast does not own a foreign sub)

## Filing channel
Form 1120 with Form 5472 attached is e-filed via standard corporate e-file procedures.

Due date: April 15, 2026 (15th day of 4th month after end of calendar tax year). Extendable 6 months via Form 7004 → October 15, 2026.

## Validation summary
- Math: all checks passed
  - Part IV totals: $24,000 received + $1,378,000 paid ✓
  - Part I Line 1g = $1,402,000 (gross flows in both directions, summed) ✓
  - Loan balance: $300,000 - $100,000 = $200,000 ✓
  - Royalty rate: $544,000 / $6,800,000 = 8.0% — matches 2023 license agreement ✓
- Sanity:
  - Interest rate ~7.2% — within reasonable range for arm's-length intercompany USD lending; AFR + 200bp spread documented
  - Aggregate cross-border outflows to Maple Tech ($1,378K) ≈ 20% of US revenue — high; ensure cumulative-effect TP analysis is in documentation
  - Sale of customer-success playbooks (intangible) on Line 13 received $24K — small, but reported correctly (no de minimis)
  - Royalty on Line 12 (rents AND royalties) — confirm against current-year instructions whether royalties have a dedicated line or share with rents
  - HarborCap (US 60% shareholder) correctly excluded from 5472 (US owners do not trigger 5472 reporting)
  - Marc Tremblay as constructive 40% owner: no separate 5472 (no transactions); constructive ownership disclosed in Part VII
- Cross-form: Form 1120 Schedule L intercompany A/P at 12/31/2025 = $115,000 reconciles to general ledger
- Penalty exposure if missed: $25,000 statutory minimum per §6038A(d)(1) per related party
- Next steps:
  - Refresh §482 transfer-pricing study annually (NorthCoast is growing; rate benchmarks may shift)
  - Confirm Q1 2026 the cumulative-effect TP analysis adequately defends 20% aggregate outflow
  - Prepare Form 1120 + 5472 e-file package by April 15, 2026 (or extend via Form 7004)

## Sources cited in this draft
- IRS Form 5472, latest revision
- IRS Instructions for Form 5472, latest revision
- IRS Form 1120 and instructions, latest revision
- IRC §6038A (information returns by 25%-foreign-owned corporations)
- IRC §6038A(d) ($25,000 statutory minimum penalty)
- IRC §318 (constructive ownership)
- IRC §482 (allocation of income among controlled taxpayers)
- IRC §6662(e) (transfer-pricing penalty / contemporaneous documentation)
- IRC §59A (BEAT — confirmed not applicable)
- Treas. Reg. §1.482-1 through §1.482-9
- Treas. Reg. §1.482-7 (cost-sharing arrangements — confirmed CSA not used)
- NorthCoast / Maple Tech royalty license agreement (2023) on file
- NorthCoast / Maple Tech master services agreement on file
- NorthCoast / Maple Tech intercompany loan agreement (2024-09-01) on file
- 2024 transfer-pricing study + 2025 update memo on file
```

## Why each non-obvious choice

**Why does 40% foreign ownership trigger Form 5472, not just 50%+?** §6038A applies to any "reporting corporation," defined as a US corporation that is 25% foreign-owned. The 25% threshold counts BOTH direct and indirect ownership. Maple Tech directly owns 40% — well above the 25% trigger. Many users assume 50%+ is the magic number (because that's the control threshold); 5472's threshold is 25%, lower than expected.

**Why is the 60% US shareholder (HarborCap) irrelevant for 5472?** Form 5472 is a foreign-owner information return. Only foreign 25%+ shareholders generate 5472 obligations. US shareholders, regardless of percentage, do not. HarborCap's 60% does not produce a 5472 even though it dwarfs Maple Tech's 40%.

**Why is one Form 5472 sufficient even though Marc Tremblay is a constructive 40% owner?** §6038A requires a separate 5472 per related party with reportable transactions. Maple Tech (the direct shareholder) had transactions in 2025 → 5472 for Maple Tech. Marc (constructive owner via §318) had ZERO transactions with NorthCoast in 2025 → no 5472 for Marc. If Marc had received $1 of compensation, lent $1, or done any other reportable transaction, a separate 5472 for him would be required.

**Why are royalties and equipment lease on different lines?** §1.482-9 (services) vs. §1.482-3 (tangible property) vs. §1.482-4 (intangible property) are distinct transfer-pricing regimes. Form 5472 follows the same distinction — Line 12 is royalties (intangible property licensing); Line 14 is "use of property" (tangible property leasing); Line 20 is "other amounts" (catches services and reimbursements). Misclassifying services as royalties (or vice versa) creates §482 documentation problems.

**Why is the cumulative TP burden a flag?** When intercompany outflows hit ~20% of revenue, the IRS focus shifts from per-transaction reasonableness to the aggregate result. Even if each individual rate is defensible, the cumulative effect can leave the US reporting corp with abnormally low margins. Documentation should explicitly defend the OVERALL pricing — typically via a transactional net margin method (TNMM / CPM) check that compares NorthCoast's net margin to comparable independent US SaaS companies.

**Why no Form 8975 (CbC report)?** §6038(g) and Treas. Reg. §1.6038-4 require country-by-country reporting only for multinational groups with consolidated revenue ≥ €750M (~$850M). NorthCoast is far below; no 8975. Maple Tech's Canadian filings may have a Canadian CbC equivalent, but that is Canadian, not US.

**What if the Canadian shareholder were a Canadian individual (not a holding company)?** A Canadian individual at 40% direct ownership is also a foreign related party under §6038A. The 5472 would have Marc personally as the Part II shareholder (with his Canadian SIN as foreign reference ID, no US ID). Same Part IV transactions, same $25,000 penalty for missed filing.

**What if the JV had been formed as an LLC taxed as a partnership instead of a C-corp?** Form 5472 would NOT apply (it's only for corporations). Instead, the partnership would file Form 8865 with respect to the foreign partner (and the foreign partner would face their own partnership filings). Different regime, different forms, similar information goal.

**What documentation does NorthCoast retain?**
1. Form 1120 + 5472 e-file confirmation
2. Cap table snapshot showing Maple Tech's 40% as of 12/31/2025
3. 2023 royalty license agreement and 2025 royalty calculations
4. Master services agreement and 2025 services billing detail
5. Equipment lease agreement and monthly invoices
6. Intercompany loan agreement, amortization schedule, interest calculations
7. 2024 transfer-pricing study + 2025 update memo
8. CAD/USD spot rates used for invoice translation
9. Schedule M-3 reconciliation showing all intercompany items

Retain at least 6 years given §482 audit cycle and statute extensions for transfer-pricing matters.
