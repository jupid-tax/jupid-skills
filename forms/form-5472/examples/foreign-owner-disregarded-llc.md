# Example: Foreign Individual Owns 100% of Delaware SMLLC for E-Commerce — Pro-Forma 1120 + 5472

A complete walkthrough of the most common Form 5472 scenario: a non-US individual who formed a Delaware single-member LLC to run an e-commerce / dropshipping business and is now realizing they must file pro-forma Form 1120 + Form 5472 even with $0 US-source income. Pattern: Type 3 disregarded entity (DE); Part V contribution and distribution plus one Part IV payment; paper / fax filing.

## The filer

- **Reporting entity**: Lumiere Studio LLC (Delaware single-member LLC)
- **EIN**: 92-XXXXXXX (obtained 2024 via Form SS-4: line 9a "Other: Foreign-owned U.S. disregarded entity-Form 5472", line 10 "Other: Foreign-owned U.S. disregarded entity filing Form 5472")
- **Date formed**: 03/02/2024
- **Foreign owner**: Camille Bernard, French citizen, resident of Lyon, France; 100% direct ownership; no US ITIN, no US ECI
- **Business**: Dropshipping European-design home goods to non-US customers via Shopify, run by Camille from Lyon; uses a commercial registered agent in Delaware; no US warehouse, no US employees, no US customers
- **Tax year**: 2025 (filing in 2026)
- **US-source gross income**: $0 (all customers and suppliers are non-US; sales platforms route through non-US Stripe accounts where possible)
- **Form 1040-NR**: Camille has none — no US ECI, no US-source FDAP income on her facts

Camille was unaware of the filing requirement until her registered agent flagged it in late 2024. She is filing 2024 (formation year) and 2025 together — late on 2024.

## Step 1 — Confirm Type 3 status

- Single member: Camille (only owner)
- Foreign owner: yes, French individual
- Check-the-box election (Form 8832) to be taxed as corporation: NO (default disregarded)
- Date Treas. Reg. §301.7701-2(c)(2)(vi) requirement applies: tax years beginning on or after 1/1/2017 and ending on or after 12/13/2017 — applies

→ Lumiere Studio LLC is a **Type 3** foreign-owned US disregarded entity. It must file pro-forma Form 1120 + Form 5472 for every year with a reportable transaction, starting with formation year 2024, regardless of income. (A year with no reportable transactions at all would have no filing requirement under the Instructions for Form 5472, Exceptions from filing, item 1; 2024 and 2025 both have transactions.)

## Step 2 — Determine reportable transactions for 2025

For Type 3 DEs, the rules are stricter than for Type 1/2 reporters. Reportable transactions include:

- Capital contributions from the foreign owner (Part V statement)
- Distributions to the foreign owner (Part V statement)
- Loans between the DE and the foreign owner (Part IV lines 17/31, balances)
- Any other amounts paid or received between the DE and any related party (Part IV)

Walk through Camille's 2025 books:

| Date | Description | Amount | Direction |
|------|-------------|--------|-----------|
| 02/14/2025 | Wire from Camille's French personal account → Lumiere LLC bank account (working capital top-up) | $8,500 | Capital contribution received |
| 06/30/2025 | Reimbursement to Camille for personal credit card paying Shopify ads (she fronted it; LLC reimbursed) | $3,200 | Other amounts paid to RP |
| 11/12/2025 | Distribution from Lumiere LLC bank account → Camille's French personal account | $15,000 | Capital distribution paid |
| 12/31/2025 | No outstanding loans between DE and Camille | n/a | n/a |

The $3,200 reimbursement is a monetary payment from the DE to Camille: Part IV line 35 ("Other amounts paid"). Camille pre-paid an LLC expense and was reimbursed. Even though it's not income to Camille (the underlying ad expense is the LLC's), the cash flow between DE and owner is reportable. The agent asked how to treat it; the CPA chose line 35 for the repayment and did not report Camille's original card payment as a separate contribution. Some preparers instead describe both legs in the Part V statement. Pick one treatment and use it every year.

## Step 3 — Identify related parties

Only one: Camille Bernard (100% direct foreign owner). One Form 5472 needed.

No siblings, no foreign sister-corps, no foreign trusts in the structure. Camille's husband (also French) holds no LLC interest. As her spouse he is a related party (§267(b)(1), §267(c)(4)), but he had no transactions with the DE in 2025, so no Form 5472 is filed for him. (If he had loaned the LLC money or received a payment, a separate 5472 naming him in Part III would be needed.)

## Step 4 — Classify transactions (Part IV and Part V)

| Where | Item | 2025 USD amount |
|-------|------|-----------------|
| Part V statement | Capital contribution received from Camille (02/14/2025) | $8,500 |
| Part V statement | Distribution paid to Camille (11/12/2025) | $15,000 |
| Part IV line 35 | Other amounts paid (reimbursement of ad spend, 06/30/2025) | $3,200 |
| Part IV lines 17, 31 | Loans with Camille (no balances at 1/1 or 12/31) | $0 |
| Part IV line 22 | Total received | $0 |
| Part IV line 36 | Total paid | $3,200 |

Line 1f (Part I) = line 22 + line 36 + Part V items = $0 + $3,200 + $23,500 = $26,700 (gross amounts, summed; do not net the $8,500 contribution against the $15,000 distribution). Check: 8,500 + 15,000 + 3,200 = 26,700.

## Step 5 — Currency translation

Camille's books are kept in USD (Lumiere LLC's bank account is USD-denominated, opened with Mercury). The 02/14/2025 wire arrived as $8,500 USD after conversion at the sending bank's rate; book value is $8,500. The 11/12/2025 distribution went out as a USD wire of $15,000; Camille received approximately €13,820 after her French bank's conversion, but the Form 5472 reports the USD amount = $15,000.

No multi-currency translation needed for the form. Document the wire receipts as evidence.

## Step 6 — Pro-forma 1120

The pro-forma 1120 is the chassis for the 5472. The Instructions for Form 5472 require only the name and address and items B and E on page 1. Lumiere LLC's 2025 pro-forma 1120:

- Across the top: "Foreign-owned U.S. DE"
- Name and address: Lumiere Studio LLC, c/o its registered agent's Delaware address
- Item B (EIN): 92-XXXXXXX
- Item E: no box checked for 2025. (The late 2024 pro forma 1120 checks item E(1) "Initial return", and the 2024 Form 5472 checks line 1j.)
- Everything else (item C, item D, income, deduction, tax lines): blank — the DE has no separate US tax obligation; income (if any) is Camille's (she has no US filing obligation since no US ECI)
- Attachments: the Form 5472 and the Part V statement
- Signature: the instructions do not address it; on the CPA's advice Camille signs as the LLC's sole member

The pro-forma 1120 itself does not generate tax. It's purely the vehicle.

## The completed Form 5472 draft

```markdown
# Form 5472 — DRAFT for tax year 2025
## (Form 5472 #1 of 1 for Lumiere Studio LLC)
Form revision: Form 5472 (Rev. December 2023); Instructions (Rev. December 2024)
Tax year: beginning 01/01/2025, ending 12/31/2025

## Part I — Reporting corporation
1a. Name and address: Lumiere Studio LLC, c/o <registered agent>, <street address>, Newark, DE 19702
1b. EIN: 92-XXXXXXX
1c. Total assets: $4,300 (Mercury balance at 12/31/2025)
1d. Principal business activity: Online retail of home furnishings
1e. Principal business activity code: 449129 (All Other Home Furnishings Retailers; nonstore retailers use the code for the product sold, Instructions for Form 1120)
1f. Total value of gross payments on this form: $26,700 (line 22 $0 + line 36 $3,200 + Part V $23,500)
1g. Total number of Forms 5472 filed: 1
1h. Total value on all Forms 5472: $26,700
1i. Consolidated filing: [ ]
1j. Initial year: [ ] (checked on the 2024 form)
1k. Number of Parts VIII: 0
1l. Country of incorporation: United States (Delaware)
1m. Date of incorporation: 03/02/2024
1n. Country(ies) where it files an income tax return as a resident: None (entry confirmed with Camille's preparer; the LLC files no income tax return of its own)
1o. Principal country(ies) where business is conducted: France
2.  Foreign person owned ≥ 50%: [x]
3.  Foreign-owned U.S. DE: [x]

## Part II — 25% foreign shareholders
Surrogate foreign corporation box: [ ]
4a. Camille Bernard, 14 Rue de la Republique, 69002 Lyon, France
4b(1) U.S. ID: (none)  4b(2) Reference ID: CBERNARD01  4b(3) FTIN: French numéro fiscal XXXXXXXXXXXXX
4c. Principal country of business: France  4d. Citizenship: France  4e. Tax residence: France
5a–7e. None

## Part III — Related party
[x] foreign person  [ ] U.S. person
8a. Camille Bernard, 14 Rue de la Republique, 69002 Lyon, France
8b(1) U.S. ID: (none)  8b(2) Reference ID: CBERNARD01  8b(3) FTIN: French numéro fiscal XXXXXXXXXXXXX
8c. Principal business activity: Individual owner (left 8d blank, confirmed with preparer)
8e. Relationship: [x] 25% foreign shareholder
8f. Principal country of business: France  8g. Tax residence: France

## Part IV — Monetary transactions
Estimates used: [ ]
| Line | Item | Amount |
|------|------|--------|
| 9–21 | No amounts received from Camille | $0 |
| 17a/17b, 31a/31b | No loan balances at 1/1 or 12/31 | $0 |
| 22 | Total received | $0 |
| 35 | Other amounts paid (06/30/2025 reimbursement of Shopify ad spend Camille paid by personal card) | $3,200 |
| 36 | Total paid | $3,200 |

## Part V — Foreign-owned U.S. DE transactions
Box checked: [x]  Attached statement:
| Date | Description | USD |
|------|-------------|-----|
| 02/14/2025 | Capital contribution from Camille Bernard (wire to LLC account) | $8,500 |
| 11/12/2025 | Distribution to Camille Bernard (wire from LLC account) | $15,000 |

## Part VI — Nonmonetary / less-than-full-consideration transactions
Box not checked — all 2025 transactions were cash at face value; no IP transfers, no equipment transfers, no unbilled services.

## Part VII — Additional information
37. Imports goods from Camille: No
39. Foreign parent in a CSA: No
40a. §267A disallowed interest or royalty: No
41a. FDII deduction: No
42a. Loan inside AFR safe-haven range: No (no loans)
42b. Loan outside the range: No
43a–43b. Not completed (foreign-owned DE)

## Part VIII — Cost sharing arrangement
N/A (line 1k = 0)

## Part IX — Base erosion payments
Not an applicable taxpayer under §59A; on the CPA's instruction lines 50–52 are left blank.

## Currency translation
USD throughout. Lumiere LLC's books are USD-denominated; all transactions settled in USD via Mercury. Camille's euro conversions happened outside the LLC's books and are not reported on Form 5472. No exchange-rate schedule needed.

## Required attachments / coordination
- [x] Attached to pro-forma Form 1120 (Type 3): name, address, item B, item E; "Foreign-owned U.S. DE" across the top; nothing else
- [x] Part V statement attached
- [ ] Form 8832 — N/A (no entity classification election made; DE by default)
- [x] Wire confirmations and Mercury bank statements retained (transaction support)

## Filing channel
Not e-fileable ("If you are a foreign-owned U.S. DE, you cannot file Form 5472 electronically"). Fax (300 DPI or higher) to 855-887-7737, or mail to:

  Internal Revenue Service
  1973 Rulon White Blvd
  M/S 6112 Attn: PIN Unit
  Ogden, UT 84201

(Instructions for Form 5472, Rev. December 2024, Dedicated mailing address.)

Due date: April 15, 2026 (due date of Form 1120 for a calendar-year DE). Extendable 6 months via Form 7004 faxed or mailed to the same unit by April 15, with "Foreign-owned U.S. DE" across the top and the Form 1120 code on Part I, line 1.

## Validation summary
- Math: all checks passed
  - Line 22 = $0; line 36 = $3,200 ✓
  - Line 1f = $0 + $3,200 + $23,500 (Part V) = $26,700 ✓; line 1h = $26,700 (one form) ✓
  - Single related party with transactions = single Form 5472; line 1g = 1 ✓
- Sanity:
  - Part V checked and statement attached; Parts I, II, III, IV, VII completed
  - Capital contribution + distribution shown gross, not netted ✓
  - Reimbursement reported even though small — correct (the "$50,000 or less" convention is a way to report small amounts, not an exemption)
  - Camille's personal French tax filings are out of scope for this form
- Cross-form: pro-forma 1120 carries only name, address, items B and E; line 1c total assets $4,300 reconciles to the Mercury statement at 12/31/2025
- Penalty exposure if missed: $25,000 for the year (§6038A(d)(1)) — 2024 late filing should be filed ASAP with a reasonable-cause statement attached
- Next steps:
  - File 2024 pro-forma 1120 (item E(1) Initial return) + 5472 (line 1j checked) immediately (late) with reasonable-cause statement
  - File 2025 pro-forma 1120 + 5472 by April 15, 2026 (or extend via Form 7004)
  - Confirm 2026 plan: if Camille intends additional contributions / distributions, set up bookkeeping to capture each transaction by date and category

## Sources cited in this draft
- IRS Form 5472 (Rev. December 2023)
- IRS Instructions for Form 5472 (Rev. December 2024): When and Where To File, Electronic Filing, Part V, Lines 4b(3)–7b(3)
- Instructions for Form 1120 (2025): principal business activity codes
- IRC §6038A (information returns by 25%-foreign-owned corporations)
- IRC §6038A(d) ($25,000 penalty per taxable year)
- Treas. Reg. §301.7701-2(c)(2)(vi) (foreign-owned US DE rules)
- Treas. Reg. §1.6038A-2(b)(3)(xi) (DE formation, contribution, distribution transactions)
- IRS Form SS-4 (EIN obtained with the foreign-owned U.S. DE write-ins)
- IRS Form 7004 (6-month extension for pro-forma 1120)
```

## Why each non-obvious choice

**Why does a $0-revenue entity with a foreign owner have to file anything?** Treas. Reg. §301.7701-2(c)(2)(vi), effective for tax years beginning on or after 1/1/2017 and ending on or after 12/13/2017, classifies foreign-owned US DEs as corporations FOR THE LIMITED PURPOSE OF §6038A reporting. The DE remains disregarded for income tax (income flows through to the foreign owner), but the §6038A obligation is independent. The IRS imposed this rule specifically to close the anonymity loophole that previously let foreign owners use Delaware DEs as opaque shells.

**Why must even the formation contribution be reported?** Treas. Reg. §1.6038A-2(b)(3)(xi) makes formation, dissolution, contribution, and distribution amounts reportable for a foreign-owned DE, and Example 1 in §1.6038A-2(b)(11) treats a foreign owner's formation contribution as a reportable transaction. Part V of the form carries them. The 2024 formation wire from Camille was a reportable transaction in 2024; failure to file 2024's 5472 is a $25,000 penalty.

**Why is the $3,200 reimbursement reportable?** Cash flowed between DE and owner. There is no de minimis exemption for reporting; the instructions only allow an amount of $50,000 or less to be entered as "$50,000 or less". Even small cross-border flows must be reported.

**Why is gross flow reported (not net)?** Part V asks for a description of each transaction, and Part IV has separate lines for each category and direction. A user reporting net $6,500 ($15K − $8.5K) instead of the $8,500 contribution and the $15,000 distribution would misdescribe both. The instructions say a substantially incomplete Form 5472 counts as a failure to file — same $25,000 penalty as not filing at all.

**Why no Form 1040-NR for Camille?** No US ECI (no customers in US, no warehouse in US, no employees in US, no fixed place of business in US). Dropshipping run from France to non-US customers does not by itself create US ECI. If facts changed (US customers, US fulfillment center, US-resident contractors), the trade-or-business and treaty permanent-establishment analysis in [`form-1040-nr`](../../form-1040-nr/SKILL.md) would be needed.

**Why the late 2024 filing?** Many foreign-owned DE owners learn of the requirement after formation. The IRS will assess a $25,000 penalty by default but may waive on reasonable-cause grounds for a first-time filer who comes forward proactively. A reasonable-cause statement should accompany the late filing — citing reliance on the registered agent, lack of US tax presence, and prompt action upon discovery.

**Why no transfer-pricing concerns?** All 2025 transactions are owner equity / reimbursement flows, not arm's-length goods or services exchanged for compensation. §482 transfer-pricing applies to controlled transactions where one side is providing value; pure equity capital movements aren't transfer-pricing transactions.

**What if Camille had bought inventory FROM her own French sole proprietorship?** A sole proprietorship is not a separate person: the purchases are transactions with Camille herself. They go on the same Form 5472 (Part III = Camille), Part IV line 23 (purchases of stock in trade), and Part VII line 37 (imports goods from a foreign related party) becomes Yes. If instead she sold through a French company she owns (an SARL, for example), that company would be a separate related party (§267(b)(2)) with its own Form 5472.

**What documentation does Camille retain?**
1. Form SS-4 application and EIN assignment letter
2. Delaware Certificate of Formation
3. Mercury bank statements (full year)
4. Stripe / Shopify transaction reports (proves no US customers)
5. Wire confirmations for the 02/14 contribution and 11/12 distribution
6. Reimbursement documentation (Shopify ad invoice + Camille's personal credit card statement + LLC reimbursement record)
7. Filed 2024 and 2025 pro-forma 1120 + 5472 packages
8. Reasonable-cause statement for 2024 late filing

Keep the records as long as they may be relevant or material, and never less than the assessment period (Treas. Reg. §1.6038A-3(g)). For a year in which Form 5472 was not filed, the assessment period stays open until 3 years after the information is furnished (IRC §6501(c)(8)).
