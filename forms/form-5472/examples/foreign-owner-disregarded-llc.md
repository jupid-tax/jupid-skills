# Example: Foreign Individual Owns 100% of Delaware SMLLC for E-Commerce — Pro-Forma 1120 + 5472

A complete walkthrough of the most common Form 5472 scenario: a non-US individual who formed a Delaware single-member LLC to run an e-commerce / dropshipping business and is now realizing they must file pro-forma Form 1120 + Form 5472 even with $0 US-source income. Pattern: Type 3 disregarded entity (DE); Part V transactions only; paper / fax filing.

## The filer

- **Reporting entity**: Lumiere Studio LLC (Delaware single-member LLC)
- **EIN**: 92-XXXXXXX (obtained 2024 via Form SS-4 with reason "foreign-owned U.S. disregarded entity")
- **Date formed**: 03/02/2024
- **Foreign owner**: Camille Bernard, French citizen, resident of Lyon, France; 100% direct ownership; no US ITIN, no US ECI
- **Business**: Dropshipping European-design home goods to non-US customers via Shopify; uses Stripe Atlas registered agent in Delaware; no US warehouse, no US employees, no US customers
- **Tax year**: 2025 (filing in 2026)
- **US-source gross income**: $0 (all customers and suppliers are non-US; sales platforms route through non-US Stripe accounts where possible)
- **Form 1040-NR**: Camille has none — no US ECI, no US-source FDAP income on her facts

Camille was unaware of the filing requirement until her registered agent flagged it in late 2024. She is filing 2024 (formation year) and 2025 together — late on 2024.

## Step 1 — Confirm Type 3 status

- Single member: Camille (only owner)
- Foreign owner: yes, French individual
- Check-the-box election (Form 8832) to be taxed as corporation: NO (default disregarded)
- Date Treas. Reg. §301.7701-2(c)(2)(vi) requirement applies: tax years beginning on or after 1/1/2017 — applies

→ Lumiere Studio LLC is a **Type 3** foreign-owned US disregarded entity. It must file pro-forma Form 1120 + Form 5472 annually starting with formation year 2024, regardless of income or activity level.

## Step 2 — Determine reportable transactions for 2025

For Type 3 DEs, the rules are stricter than for Type 1/2 reporters. Reportable transactions include:

- Capital contributions from the foreign owner
- Distributions to the foreign owner
- Loans between the DE and the foreign owner (year-end balance changes)
- Any other amounts paid or received between the DE and any related party

Walk through Camille's 2025 books:

| Date | Description | Amount | Direction |
|------|-------------|--------|-----------|
| 02/14/2025 | Wire from Camille's French personal account → Lumiere LLC bank account (working capital top-up) | $8,500 | Capital contribution received |
| 06/30/2025 | Reimbursement to Camille for personal credit card paying Shopify ads (she fronted it; LLC reimbursed) | $3,200 | Other amounts paid to RP |
| 11/12/2025 | Distribution from Lumiere LLC bank account → Camille's French personal account | $15,000 | Capital distribution paid |
| 12/31/2025 | No outstanding loans between DE and Camille | n/a | n/a |

The $3,200 reimbursement is a Part V "other amount paid to related party" — Camille pre-paid an LLC expense and was reimbursed. Even though it's not income to Camille and not a deduction issue (the underlying ad expense is the LLC's), the cash flow between DE and owner is reportable.

## Step 3 — Identify related parties

Only one: Camille Bernard (100% direct foreign owner). One Form 5472 needed.

No siblings, no foreign sister-corps, no foreign trusts in the structure. Camille's husband (also French) holds no LLC interest and has no transactions with the DE in 2025 → he is not a related party for 5472 purposes. (If he had loaned the LLC money or received a payment, he would be a §267(b) related party and a separate 5472 would be needed.)

## Step 4 — Classify Part V transactions

| Part V category | 2025 USD amount |
|-----------------|-----------------|
| Capital contributions received from foreign owner | $8,500 |
| Capital distributions paid to foreign owner | $15,000 |
| Amounts paid to related party (reimbursement) | $3,200 |
| Amounts received from related party | $0 |
| Loans from foreign owner (year-end balance) | $0 |
| Loans to foreign owner (year-end balance) | $0 |

Total reportable transactions for Line 1i (Part I): $26,700 (gross flows in both directions, summed; do not net the $8,500 contribution against the $15,000 distribution).

## Step 5 — Currency translation

Camille's books are kept in USD (Lumiere LLC's bank account is USD-denominated, opened with Mercury). The 02/14/2025 wire arrived as $8,500 USD after conversion at the sending bank's rate; book value is $8,500. The 11/12/2025 distribution went out as a USD wire of $15,000; Camille received approximately €13,820 after her French bank's conversion, but the Form 5472 reports the USD amount = $15,000.

No multi-currency translation needed for the form. Document the wire receipts as evidence.

## Step 6 — Pro-forma 1120

The pro-forma 1120 is the chassis for the 5472. Lumiere LLC's pro-forma 1120 looks like this:

- Top of form: "Foreign-owned U.S. DE" handwritten or typed across the top (per Form 5472 instructions)
- Item B: check "1. Initial return" if 2024 was the first year (already filed late); for 2025, do NOT check initial — this is a continuation
- Item E (Total assets): book value of LLC at year-end, e.g., $4,300 in Mercury account
- Lines 1-30 (income / deductions / tax): all zeros — the DE has no separate US tax obligation; income (if any) would flow through to Camille's personal French tax filings (Camille has no US filing obligation since no US-source ECI)
- Schedule attachments: just the Form 5472

The pro-forma 1120 itself does not generate tax. It's purely the vehicle.

## The completed Form 5472 draft

```markdown
# Form 5472 — DRAFT for tax year 2025
## (Form 5472 #1 of 1 for Lumiere Studio LLC)

## Reporting corporation identity (Part I)
1a. Name of reporting corporation: Lumiere Studio LLC
1b. EIN: 92-XXXXXXX
1c. Address: c/o Stripe Atlas, 254 Chapman Rd, Ste 208 #14454, Newark, DE 19702
1d. Total assets (book value at year-end): $4,300
1e. Principal business activity / NAICS: E-commerce retail of home goods, 454110
1f. Total US-source gross income: $0
1g. Total payments / receipts in reportable transactions: $26,700
1h. Country(ies) where return also filed: France (Camille's personal filings; LLC itself has no separate French filing)
1i. Type of reporting corporation:
    [ ] Type 1 — US C-corp, 25% foreign-owned
    [ ] Type 2 — Foreign corp engaged in US trade/business
    [x] Type 3 — Foreign-owned US disregarded entity

## Related party (Part II)
2a. Name: Camille Bernard
2b. Address: 14 Rue de la Republique, 69002 Lyon, France
2c. Country: France
2d. US ID # (if any): None
2e. Foreign ID # / reference ID: French TIN (numero fiscal) XX-XXXXXXXXXXX
2f. Principal country where business conducted: France
2g. Ownership percentage: 100% direct | 0% indirect | 100% total
2h. Principal business activity of related party: Individual (not a business; investor / owner)

## Direct vs indirect ownership (Part III)
N/A — Camille is the direct 100% owner; no intermediate entities.

## Part IV — Monetary transactions (Type 1 or Type 2)
N/A — Lumiere is Type 3. See Part V.

## Part V — Type 3 DE reportable transactions
| Line | Transaction                                       | Amount  |
|------|---------------------------------------------------|---------|
|      | Capital contribution received from foreign owner  | $8,500  |
|      | Capital distribution paid to foreign owner        | $15,000 |
|      | Loans from foreign owner (year-end balance)       | $0      |
|      | Loans to foreign owner (year-end balance)         | $0      |
|      | Amounts paid to related party (reimbursement)     | $3,200  |
|      | Amounts received from related party               | $0      |
|      | Other reportable transactions                     | $0      |

## Part VI — Nonmonetary / less-than-FMV transactions
N/A — all 2025 transactions were cash at face value; no IP transfers, no equipment transfers, no below-FMV services.

## Part VII — Additional information
- Yes/No items completed per current-year instructions; key item: yes, the DE is a foreign-owned US disregarded entity per Treas. Reg. §301.7701-2(c)(2)(vi).

## Part VIII — Cost-sharing arrangement
N/A

## Part IX — Base Erosion Payments (BEAT)
N/A — average annual gross receipts well under $500M.

## Currency translation
Source: USD throughout. Lumiere LLC's books are USD-denominated; all transactions settled in USD via Mercury. Camille's underlying Euro conversions occurred outside the LLC's books and are not reported on Form 5472.

## Required attachments / coordination
- [x] Attached to pro-forma Form 1120 (Type 3)
- [x] Pro-forma 1120 has "Foreign-owned U.S. DE" notation across the top
- [ ] Form 8832 — N/A (no entity classification election made; DE by default)
- [x] Wire confirmations and Mercury bank statements retained (transaction support)

## Filing channel
Pro-forma 1120 + Form 5472 are paper-filed by **fax to the IRS Ogden office (verify current fax number against latest Form 5472 instructions before sending) OR by mail** to:

  Internal Revenue Service
  1973 N Rulon White Blvd.
  M/S 6112, Attn: PIN Unit
  Ogden, UT 84404

E-filing is generally NOT available for the pro-forma 1120 + 5472 combination as of the latest instructions. Verify current procedures.

Due date: April 15, 2026 (15th day of 4th month after end of DE's calendar tax year). Extendable 6 months via Form 7004 — file 7004 by April 15 to push deadline to October 15.

## Validation summary
- Math: all checks passed
  - Sum of Part V reportable transactions = $26,700 = Part I Line 1g ✓
  - Single related party = single Form 5472 ✓
- Sanity:
  - Part V populated (not blank); Type 3 DEs that report no transactions get IRS scrutiny — confirm legitimacy
  - Capital contribution + distribution shown gross, not netted ✓
  - Reimbursement reported even though small — correct (no de minimis exception in §6038A)
  - Camille's personal French tax filings are out of scope for this form
- Cross-form: pro-forma 1120 Total Receipts = $0; Total Assets = $4,300; both reconcile to Mercury bank statement at 12/31/2025
- Penalty exposure if missed: $25,000 statutory minimum per §6038A(d)(1) — 2024 late filing should be filed ASAP with reasonable-cause statement attached
- Next steps:
  - File 2024 pro-forma 1120 + 5472 immediately (late) with reasonable-cause statement
  - File 2025 pro-forma 1120 + 5472 by April 15, 2026 (or extend via Form 7004)
  - Confirm 2026 plan: if Camille intends additional contributions / distributions, set up bookkeeping to capture each transaction by date and category

## Sources cited in this draft
- IRS Form 5472, latest revision
- IRS Instructions for Form 5472, latest revision
- IRC §6038A (information returns by 25%-foreign-owned corporations)
- IRC §6038A(d) ($25,000 statutory minimum penalty)
- Treas. Reg. §301.7701-2(c)(2)(vi) (foreign-owned US DE rules; effective 2017)
- Treas. Reg. §1.6038A-2 (Form 5472 mechanics for DEs)
- IRS Form SS-4 (used to obtain EIN with foreign-owned US DE reason)
- IRS Form 7004 (6-month extension for pro-forma 1120)
```

## Why each non-obvious choice

**Why does a $0-revenue entity with a foreign owner have to file anything?** Treas. Reg. §301.7701-2(c)(2)(vi), effective 1/1/2017, classifies foreign-owned US DEs as corporations FOR THE LIMITED PURPOSE OF §6038A reporting. The DE remains disregarded for income tax (income flows through to the foreign owner), but the §6038A obligation is independent. The IRS imposed this rule specifically to close the anonymity loophole that previously let foreign owners use Delaware DEs as opaque shells.

**Why must even the formation contribution be reported?** Treas. Reg. §1.6038A-2(b) defines reportable transactions broadly. Capital contributions are explicitly reportable under Part V for Type 3 DEs. The 2024 formation wire from Camille was a reportable transaction in 2024; failure to file 2024's 5472 is a $25,000 penalty.

**Why is the $3,200 reimbursement reportable?** Cash flowed between DE and owner. §6038A's reportable-transaction definition has no de minimis threshold. Even small cross-border flows must be reported. The economic substance is irrelevant — it's an information return.

**Why is gross flow reported (not net)?** Form 5472 Part V instructions require gross amounts in each direction. A user reporting net $6,500 ($15K − $8.5K) instead of $8,500 contribution + $15,000 distribution would understate the form. Tax court has consistently treated mis-reported 5472s as "substantially incomplete" — same penalty as not filing at all.

**Why no Form 1040-NR for Camille?** No US-source ECI (no customers in US, no warehouse in US, no employees in US, no fixed place of business in US). Dropshipping with non-US customers does not by itself create US ECI. If facts changed (US customers, US fulfillment center, US-resident contractors), an analysis under the US-France treaty's permanent-establishment article would be needed.

**Why the late 2024 filing?** Many foreign-owned DE owners learn of the requirement after formation. The IRS will assess a $25,000 penalty by default but may waive on reasonable-cause grounds for a first-time filer who comes forward proactively. A reasonable-cause statement should accompany the late filing — citing reliance on the registered agent, lack of US tax presence, and prompt action upon discovery.

**Why no transfer-pricing concerns?** All 2025 transactions are owner equity / reimbursement flows, not arm's-length goods or services exchanged for compensation. §482 transfer-pricing applies to controlled transactions where one side is providing value; pure equity capital movements aren't transfer-pricing transactions.

**What if Camille had bought inventory FROM her own French sole proprietorship?** Then the French sole proprietorship would be a related party (controlled by her under §267(b) constructive ownership). A separate Form 5472 would be required for that related party, classifying inventory purchases on Part V.

**What documentation does Camille retain?**
1. Form SS-4 application and EIN assignment letter
2. Delaware Certificate of Formation
3. Mercury bank statements (full year)
4. Stripe / Shopify transaction reports (proves no US customers)
5. Wire confirmations for the 02/14 contribution and 11/12 distribution
6. Reimbursement documentation (Shopify ad invoice + Camille's personal credit card statement + LLC reimbursement record)
7. Filed 2024 and 2025 pro-forma 1120 + 5472 packages
8. Reasonable-cause statement for 2024 late filing

Retain at least 3 years post filing — 6 years is safer given the 5472's sensitivity to omissions.
