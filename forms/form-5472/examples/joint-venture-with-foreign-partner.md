# Example: 60/40 US-Foreign C-Corp Joint Venture — Multiple Part IV Transactions

A complete walkthrough of Form 5472 for a Type 1 reporting corporation that is majority US-owned but has a 40% Canadian shareholder. Pattern: Form 1120 with Form 5472 attached for the 40% Canadian related party; Part IV captures multiple intercompany transactions (services, royalties, loans, equipment lease).

The 40% foreign ownership is enough to trigger Form 5472 — not just 50%+. Many users miss this.

## The filer

- **Reporting entity**: NorthCoast Software Inc. (Delaware C-corp; the joint venture)
- **EIN**: 87-XXXXXXX
- **Date incorporated**: 04/12/2023
- **Tax year**: 2025 (filing in 2026); calendar year
- **State of organization**: Delaware
- **Business activity**: B2B SaaS for logistics fleet management; Form 1120 principal business activity code 513210 (Software Publishers, Instructions for Form 1120 (2025) code list)
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

1. **Maple Tech Holdings Inc.** — direct 40% foreign shareholder (Part II lines 4a–4e)
2. **Marc Tremblay** — sole shareholder of Maple Tech; under the §318 constructive ownership rules as modified by §6038A(c)(5), Marc indirectly owns 40% of NorthCoast through Maple Tech, so he is listed in Part II lines 6a–6e as the ultimate indirect 25% foreign shareholder, with an attached explanation of the attribution. Did Marc himself transact with NorthCoast in 2025?
   - Marc serves on NorthCoast's board (uncompensated for 2025; director's fees waived per board resolution)
   - No direct loans, no direct payments → Marc as an INDIVIDUAL had zero reportable transactions with NorthCoast in 2025
   - No separate Form 5472 needed for Marc (no transactions)

3. HarborCap Ventures LLC — US shareholder, not foreign → no 5472 obligation regardless of transactions

→ One Form 5472 needed (for Maple Tech only).

If Marc's family trust had transacted with NorthCoast, a separate 5472 for the trust might be required. If Maple Tech's other Canadian subsidiaries had transacted with NorthCoast, separate 5472s for those subs would be required. Always test each potential related party independently.

## Step 4 — Classify Part IV transactions

Map 2025 flows to the Form 5472 (Rev. December 2023) lines; the received block is lines 9–22, the paid block lines 23–36:

| Line | Category | Amount |
|------|----------|--------|
| 14 | Sales, leases, licenses, etc., of intangible property rights — received (playbooks licensed to Maple Tech) | $24,000 |
| 17a | Amounts borrowed — beginning balance | $300,000 |
| 17b | Amounts borrowed — ending balance | $200,000 |
| 22 | Total received (lines 9–21) | $224,000 |
| 27a | Rents paid (for other than intangible property rights) — equipment lease | $96,000 |
| 28 | Purchases, leases, licenses, etc., of intangible property rights — paid (software IP and trademark royalty) | $544,000 |
| 29 | Consideration paid for technical, managerial, engineering ... services | $720,000 |
| 32 | Interest paid | $18,000 |
| 36 | Total paid (lines 23–35) | $1,378,000 |

All other lines are $0.

**Royalty on line 28**: $544,000 paid to Maple Tech for trademark + software IP licensed, calculated as 8% of subscription revenue per a 2023 license agreement. Line 27b ("royalties paid for other than intangible property rights") does not fit: this royalty is for intangible property rights.

**Equipment lease on line 27a**: $96,000 paid for the Toronto data-center hardware Maple Tech owns and leases to NorthCoast, at arm's-length monthly rates supported by a third-party comparable colocation pricing study.

**Engineering services on line 29**: $720,000 paid for Canadian engineers seconded to NorthCoast under a master services agreement. Cost-plus 8% per §1.482-9.

**License of playbooks on line 14**: $24,000 received from Maple Tech for customer-success playbooks NorthCoast developed and licensed to it. Small but reportable.

**Loan on lines 17a/17b**: the outstanding balance method reports the beginning and ending balances; the $100,000 repayment has no line of its own. The form puts 17b in the amount column, so the plain reading includes it in line 22 (state this convention in the draft and confirm it with the preparer).

**Interest on line 32**: NorthCoast's average annual gross receipts are under the 2025 §448(c) threshold of $31,000,000 (Rev. Proc. 2024-40 §2.31), so §163(j) does not limit the deduction and the full $18,000 is reported (Instructions for Form 5472, Line 32).

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
Form revision: Form 5472 (Rev. December 2023); Instructions (Rev. December 2024)
Tax year: beginning 01/01/2025, ending 12/31/2025

## Part I — Reporting corporation
1a. Name and address: NorthCoast Software Inc., 500 Howard St #800, San Francisco, CA 94105
1b. EIN: 87-XXXXXXX
1c. Total assets: $4,200,000 (Form 1120 Schedule L, line 15, column (d))
1d. Principal business activity: Software publishers
1e. Principal business activity code: 513210
1f. Total value of gross payments on this form: $1,602,000 (line 22 $224,000 + line 36 $1,378,000; includes the line 17b balance — convention confirmed with preparer)
1g. Total number of Forms 5472 filed: 1
1h. Total value on all Forms 5472: $1,602,000
1i. Consolidated filing: [ ]
1j. Initial year: [ ] (first filed for 2023)
1k. Number of Parts VIII: 0
1l. Country of incorporation: United States
1m. Date of incorporation: 04/12/2023
1n. Country(ies) where it files an income tax return as a resident: United States
1o. Principal country(ies) where business is conducted: United States
2.  Foreign person owned ≥ 50% at any time: [ ] (Maple Tech 40%)
3.  Foreign-owned U.S. DE: [ ]

## Part II — 25% foreign shareholders
Surrogate foreign corporation box: [ ]
4a. Maple Tech Holdings Inc., 100 King St W, Suite 5300, Toronto, ON M5X 1C7, Canada
4b(1) U.S. ID: (none)  4b(2) Reference ID: MAPLETECH01  4b(3) FTIN: Canadian Business Number XXXXXXXXX
4c. Principal country of business: Canada  4d. Country of incorporation: Canada  4e. Tax residence: Canada
5a–5e. None
6a. Marc Tremblay, <home address>, Toronto, ON, Canada (ultimate indirect 25% foreign shareholder; 40% through Maple Tech — attribution statement attached)
6b(1) U.S. ID: (none)  6b(2) Reference ID: MTREMBLAY01  6b(3) FTIN: Canadian SIN XXXXXXXXX
6c. Principal country of business: Canada  6d. Citizenship: Canada  6e. Tax residence: Canada
7a–7e. None

## Part III — Related party
[x] foreign person  [ ] U.S. person
8a. Maple Tech Holdings Inc., 100 King St W, Suite 5300, Toronto, ON M5X 1C7, Canada
8b(1) U.S. ID: (none)  8b(2) Reference ID: MAPLETECH01  8b(3) FTIN: Canadian Business Number XXXXXXXXX
8c. Principal business activity: Holding company  8d. Code: 551112
8e. Relationship: [x] 25% foreign shareholder
8f. Principal country of business: Canada  8g. Tax residence: Canada

## Part IV — Monetary transactions
Estimates used: [ ]
| Line | Item | Amount |
|------|------|--------|
| 9–13b | Inventory, tangible property, platform contribution, cost sharing, rents, other royalties received | $0 |
| 14 | Licenses of intangible property rights — received (playbooks) | $24,000 |
| 15–16 | Services, commissions received | $0 |
| 17a | Amounts borrowed — beginning balance | $300,000 |
| 17b | Amounts borrowed — ending balance | $200,000 |
| 18–21 | Interest, premiums, guarantee fees, other received | $0 |
| 22 | Total received | $224,000 |
| 23–26 | Inventory, tangible property, platform contribution, cost sharing paid | $0 |
| 27a | Rents paid (equipment lease) | $96,000 |
| 27b | Royalties paid (other than intangible property rights) | $0 |
| 28 | Licenses of intangible property rights — paid (software IP and trademark royalty) | $544,000 |
| 29 | Consideration paid for engineering services | $720,000 |
| 30 | Commissions paid | $0 |
| 31a/31b | Amounts loaned | $0 |
| 32 | Interest paid (not limited by §163(j)) | $18,000 |
| 33–35 | Premiums, guarantee fees, other paid | $0 |
| 36 | Total paid | $1,378,000 |

## Part V — Foreign-owned U.S. DE transactions
Not applicable (box not checked).

## Part VI — Nonmonetary / less-than-full-consideration transactions
Box not checked for 2025. (The 2023 contribution of IP for stock was reported on the 2023 Form 5472.)

## Part VII — Additional information
37. Imports goods from a foreign related party: No (leased hardware stays in Toronto)
39. Foreign parent in a CSA: No
40a. §267A disallowed interest or royalty: No (confirmed with CPA)
41a. FDII deduction: No
42a. Loan within the 100%–130% AFR safe-haven range: No
42b. Loan outside that range: Yes (CPA determination; arm's-length benchmark on file)
43a. §385 covered debt instrument / related distribution or acquisition: No (confirmed with CPA)

## Part VIII — Cost sharing arrangement
N/A (line 1k = 0). No CSA between NorthCoast and Maple Tech.

## Part IX — Base erosion payments
Not an applicable taxpayer under §59A (average annual gross receipts far below $500 million); lines 50–52 left blank on the CPA's instruction.

## Currency translation
USD functional currency. CAD invoices from Maple Tech translated at the spot rate on invoice date; schedule of exchange rates used attached (Instructions for Form 5472, Part IV). Loan is USD-denominated.

## Required attachments / coordination
- [x] Part of the Form 1120 return
- [x] Attribution statement for Marc Tremblay (Part II line 6a)
- [x] Exchange-rate schedule
- [x] Schedule M-1 (total assets under $10 million, so Schedule M-3 is not required — Instructions for Form 1120)
- [x] Royalty license, master services, equipment lease, and loan agreements on file
- [x] §6662(e) transfer-pricing documentation (2024 study + 2025 update memo)
- [ ] Form 8975 (country-by-country report) — N/A: filed only by the U.S. ultimate parent of a U.S. MNE group with revenue of $850 million or more (Instructions for Form 8975)
- [ ] Form 5471 — N/A (NorthCoast owns no foreign corporation)

## Filing channel
Form 5472 is part of the Form 1120 return and is e-filed with it.

Due date: April 15, 2026 (15th day of 4th month after end of calendar tax year). Extendable 6 months via Form 7004 → October 15, 2026.

## Validation summary
- Math (python, /tmp/jupid-skills-work/calc/g4-5472-northcoast.py):
  - Line 22 = $24,000 + $200,000 = $224,000 ✓
  - Line 36 = $96,000 + $544,000 + $720,000 + $18,000 = $1,378,000 ✓
  - Line 1f = $224,000 + $1,378,000 = $1,602,000 ✓; 1h = 1f (one form) ✓
  - Loan: $300,000 − $100,000 = $200,000 = line 17b ✓
  - Royalty rate: $544,000 / $6,800,000 = 8.0% — matches 2023 license agreement ✓
- Sanity:
  - Interest ~7.2% on the $250,000 average balance; outside the AFR safe haven, so the benchmark carries the support
  - Aggregate paid to Maple Tech ($1,378K) ≈ 20.3% of US revenue — ensure the documentation covers the cumulative effect
  - License of playbooks on line 14 — small, but reported (no de minimis; "$50,000 or less" is only a way to report small amounts)
  - HarborCap (US 60% shareholder) not a 25% foreign shareholder; Marc Tremblay listed in Part II line 6a, no separate Form 5472 (no transactions with him)
- Cross-form: Form 1120 Schedule L intercompany A/P at 12/31/2025 = $115,000 reconciles to general ledger
- Penalty exposure if missed: $25,000 per related party per year (§6038A(d)(1))
- Next steps:
  - Refresh §482 transfer-pricing study annually
  - Confirm the cumulative-effect analysis supports the ~20% aggregate outflow
  - File Form 1120 + 5472 by April 15, 2026 (or extend via Form 7004)

## Sources cited in this draft
- IRS Form 5472 (Rev. December 2023) and Instructions (Rev. December 2024)
- 2025 Form 1120 and Instructions (principal business activity codes; Schedule M-3 threshold)
- IRC §6038A, §6038A(c)(5), §6038A(d), §318, §482, §6662(e), §163(j), §448(c), §59A
- Rev. Proc. 2024-40 §2.31 (2025 §448(c) threshold $31,000,000)
- Treas. Reg. §1.482-1 through §1.482-9; §1.482-2(a)(2)(iii)(B) (AFR safe haven)
- Instructions for Form 8975 ($850 million threshold)
- NorthCoast / Maple Tech royalty license (2023), master services agreement, loan agreement (2024-09-01), 2024 TP study + 2025 memo (on file)
```

## Why each non-obvious choice

**Why does 40% foreign ownership trigger Form 5472, not just 50%+?** §6038A applies to any "reporting corporation," defined as a US corporation that is 25% foreign-owned. The 25% threshold counts BOTH direct and indirect ownership. Maple Tech directly owns 40% — well above the 25% trigger. Many users assume 50%+ is the magic number (because that's the control threshold); 5472's threshold is 25%, lower than expected.

**Why is the 60% US shareholder (HarborCap) irrelevant for 5472?** Form 5472 is a foreign-owner information return. Only foreign 25%+ shareholders generate 5472 obligations. US shareholders, regardless of percentage, do not. HarborCap's 60% does not produce a 5472 even though it dwarfs Maple Tech's 40%.

**Why is one Form 5472 sufficient even though Marc Tremblay is a constructive 40% owner?** A separate 5472 is filed per related party with reportable transactions (Instructions for Form 5472, Line 1g). Maple Tech (the direct shareholder) had transactions in 2025 → 5472 for Maple Tech. Marc had no transactions with NorthCoast in 2025 → no 5472 for Marc, but he still appears in Part II lines 6a–6e as the ultimate indirect 25% foreign shareholder. If Marc had received compensation, lent money, or had any other reportable transaction, a separate 5472 naming him in Part III would be required.

**Why are royalties, equipment lease, and services on different lines?** §1.482-9 (services) vs. §1.482-2(c) (use of tangible property) vs. §1.482-4 (intangible property) are distinct transfer-pricing regimes, and Form 5472 follows a similar split: line 28 for licenses of intangible property rights, line 27a for rents for other than intangible property rights, line 29 for technical, managerial, engineering and like services. Misclassifying services as royalties (or vice versa) creates §482 documentation problems.

**Why is the cumulative TP burden a flag?** When intercompany outflows hit ~20% of revenue, the IRS focus shifts from per-transaction reasonableness to the aggregate result. Even if each individual rate is defensible, the cumulative effect can leave the US reporting corp with abnormally low margins. Documentation should explicitly defend the OVERALL pricing — typically via a transactional net margin method (TNMM / CPM) check that compares NorthCoast's net margin to comparable independent US SaaS companies.

**Why no Form 8975 (CbC report)?** Treas. Reg. §1.6038-4 requires Form 8975 only from the U.S. ultimate parent entity of a U.S. multinational enterprise group with revenue of $850 million or more in the preceding reporting period (Instructions for Form 8975). NorthCoast is neither; no 8975.

**What if the Canadian shareholder were a Canadian individual (not a holding company)?** A Canadian individual at 40% direct ownership is also a 25% foreign shareholder and related party under §6038A. The 5472 would show Marc personally on Part II line 4a and in Part III, with his Canadian SIN as the FTIN on 4b(3)/8b(3), a corporation-assigned reference ID on 4b(2)/8b(2), and no U.S. ID. Same Part IV transactions, same $25,000 penalty for a missed filing.

**What if the JV had been formed as an LLC taxed as a partnership instead of a C-corp?** Form 5472 would not apply (it covers corporations and foreign-owned DEs). Form 8865 would not apply either: it is for U.S. persons with interests in foreign partnerships. A U.S. partnership with a foreign partner deals with §1446 withholding on effectively connected income allocable to that partner (Forms 8804, 8805, 8813) and reports to the partner on Schedule K-1 (and K-3). Different regime, different forms; route to a practitioner.

**What documentation does NorthCoast retain?**
1. Form 1120 (with Form 5472) e-file acknowledgment
2. Cap table snapshot showing Maple Tech's 40% as of 12/31/2025
3. 2023 royalty license agreement and 2025 royalty calculations
4. Master services agreement and 2025 services billing detail
5. Equipment lease agreement and monthly invoices
6. Intercompany loan agreement, amortization schedule, interest calculations
7. 2024 transfer-pricing study + 2025 update memo
8. CAD/USD spot rates used for invoice translation
9. Schedule M-1 reconciliation and the general-ledger detail for all intercompany items

Keep the records as long as they may be relevant or material to the §6038A transactions, and never less than the assessment period (Treas. Reg. §1.6038A-3(g)).
