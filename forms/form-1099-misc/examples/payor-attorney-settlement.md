# Example: Settlement Payment Through Attorney's Trust Account

A complete walkthrough of a $3,500 settlement paid through an attorney's trust account, illustrating the Box 10 (gross proceeds to attorney) and Box 3 (plaintiff's portion) split. Shows the corporate-exception rule for attorneys.

## The setup

- **Defendant / Payor**: Riverstone Industries Inc. (C-corp; defendant in a wage-related dispute)
- **Plaintiff**: Marcus Chen (former contractor; claim was for unpaid invoices, treated as a contract dispute — NOT a personal physical injury, so no §104 exclusion)
- **Plaintiff's attorney**: Park & Sussman LLC (multi-member LLC taxed as a partnership; based in CA)
- **Settlement amount**: $3,500
- **Attorney's contingency fee**: 30% = $1,050
- **Plaintiff's net portion**: $3,500 − $1,050 = $2,450 (no costs / liens to subtract)
- **Date of settlement check**: November 4, 2026
- **Tax year**: 2026

## Money flow

1. Riverstone Industries cuts a $3,500 check made out to "Park & Sussman LLC, Trustee for Marcus Chen"
2. Attorney deposits in trust account
3. Attorney disburses:
   - $2,450 to Marcus Chen
   - $1,050 retained as fee (transfers to firm's operating account)

## Decision: which forms does Riverstone issue?

Per [`settlement-allocation.md`](../references/settlement-allocation.md):

### Form 1: 1099-MISC to Park & Sussman LLC (the attorney)

- **Box 10 (gross proceeds paid to attorney)**: $3,500 — the full amount that passed through the trust account
- **Box 1**: $0
- **Box 3**: $0
- **Box 4**: $0 (no backup withholding; valid W-9 on file)

**Why issue to a corporate / non-individual attorney?** Reg. §1.6041-1(d)(2) carves out attorneys from the standard corporate exemption. Box 10 is reportable regardless of attorney's entity type. Even a professional corporation (PC) attorney gets a 1099-MISC Box 10.

In this case Park & Sussman is a partnership, but it would matter if they were a PC: same outcome (Box 10 reportable).

### Form 2: 1099-NEC to Park & Sussman LLC (the attorney's fee component)

- **Box 1 (nonemployee compensation)**: $1,050 — the attorney's fee for legal services

**Why issue?** The $1,050 is compensation to the attorney for legal services; it falls under §6041A. Park & Sussman is a partnership (non-corporate), so the standard corporate exemption does NOT apply.

If Park & Sussman were a **corporation**, no 1099-NEC would be issued for the fee (corporate exemption applies to 1099-NEC). Only Box 10 would be issued (because Box 10 has the special anti-exemption rule for attorneys). 

For a partnership: both 1099-MISC Box 10 ($3,500) and 1099-NEC Box 1 ($1,050).

### Form 3: 1099-MISC to Marcus Chen (the plaintiff)

- **Box 3 (other income)**: $2,450 — the plaintiff's portion

**Why Box 3?** Marcus's portion is taxable income. The underlying claim is a contract dispute (not personal physical injury), so IRC §104(a)(2) does NOT exclude it. Marcus reports $2,450 on Schedule 1 Line 8z ("Settlement of contract dispute") with description.

If the claim had been for personal physical injury: §104(a)(2) might exclude Marcus's portion, but Riverstone could still issue Box 3 to be safe. Marcus would exclude on his return with an explanatory statement.

## W-9 verification before issuance

Before filing, Riverstone confirmed:
- W-9 from Park & Sussman LLC: shows Line 3 box "Limited liability company — P (Partnership)"; TIN is the LLC's EIN
- W-9 from Marcus Chen: shows Line 3 "Individual / sole proprietor or single-member LLC"; TIN is Marcus's SSN

TIN matching:
- Park & Sussman LLC EIN matched IRS records
- Marcus Chen SSN matched IRS records

## Filing checklist

| Form | Issued to | Box 1 / 3 / 10 | Recipient deadline | IRS deadline |
|------|-----------|----------------|--------------------|--------------|
| 1099-MISC | Park & Sussman LLC | Box 10 = $3,500 | Feb 1, 2027 | Mar 31, 2027 (electronic) |
| 1099-NEC | Park & Sussman LLC | Box 1 = $1,050 | Jan 31, 2027 | Jan 31, 2027 (electronic) |
| 1099-MISC | Marcus Chen | Box 3 = $2,450 | Feb 1, 2027 | Mar 31, 2027 (electronic) |

Note the deadline asymmetry: 1099-NEC is January 31 for both recipient and IRS; 1099-MISC is February 1 / March 31.

## How each party reports

### Park & Sussman LLC (the partnership)

The partnership recognizes only the **fee income** ($1,050) as gross receipts on Form 1065. Box 10's $3,500 is informational gross-proceeds reporting; the partnership's accounting books show:

- Inflow to trust account: $3,500 (asset; not income)
- Disbursement to client: $2,450 (decrease in asset; not expense)
- Transfer of fee to operating account: $1,050 (income recognized at this point)

The partnership reports $1,050 on Form 1065 Line 1a (gross receipts). Schedule K-1 to each partner allocates their share.

The 1099-NEC Box 1 ($1,050) cross-checks the partnership's reported income.

The 1099-MISC Box 10 ($3,500) is informational; doesn't represent partnership income beyond the $1,050 fee already captured.

### Marcus Chen (the plaintiff)

Marcus reports $2,450 on **Schedule 1 Line 8z** with description "Settlement of contract dispute, Riverstone Industries v. Chen". Total flows to Form 1040 Line 8 (additional income).

No SE tax (this isn't a trade-or-business — Marcus's contracting was the underlying activity, but the settlement compensates him for unpaid invoices, taxable as ordinary income but not SE income because it's a settlement, not new earnings from a continuing business).

If Marcus's underlying contracting WAS a trade or business and the settlement was directly compensating him for unpaid services revenue, an argument could be made for Schedule C treatment (with SE tax). The payor's classification (Box 3) is informational; the recipient determines the proper return treatment.

### Riverstone Industries Inc.

Riverstone deducts the $3,500 settlement as a business expense on its Form 1120 (subject to ordinary deductibility rules under IRC §162). The deduction is for the full $3,500, regardless of how it was split between Marcus and Park & Sussman.

## What if §104 had applied (personal physical injury)?

Suppose the underlying claim was Marcus suing Riverstone for an injury at Riverstone's facility (broken ankle).

- §104(a)(2) would exclude Marcus's $2,450 from gross income
- Riverstone still issues 1099-MISC Box 10 = $3,500 to Park & Sussman (gross-proceeds reporting is independent of recipient tax treatment)
- Riverstone might or might not issue Box 3 to Marcus:
  - **Conservative practice**: issue Box 3 = $2,450, let Marcus exclude under §104 with explanatory statement
  - **Some payors**: don't issue Box 3 if §104 clearly applies and the settlement agreement explicitly allocates to physical injury

Either way, the Box 10 to attorney = $3,500.

## What if Park & Sussman had been a professional corporation (PC)?

- 1099-MISC Box 10 = $3,500 (still reportable; attorney special rule)
- 1099-NEC Box 1 = NOT issued (PC is a corporation; standard corporate exemption applies to 1099-NEC; only 1099-MISC has the attorney exception)

The PC reports the full $1,050 fee as corporate income on Form 1120 / 1120-S regardless of 1099-NEC issuance.

## Sources cited
- IRS Form 1099-MISC, Rev. 2026
- IRS Form 1099-NEC, Rev. 2026
- IRS Instructions for Forms 1099-MISC and 1099-NEC, Rev. 2026
- IRC §6041, §6041A, §6045(f) (gross proceeds to attorney)
- Reg. §1.6041-1(d)(2) (special rule for attorneys; corporate exemption does not apply to Box 10)
- Reg. §1.6041-3(c) (general corporate exemption — applies to standard payments to corporations)
- IRC §104(a)(2) (exclusion for personal physical injury damages)
- IRS Pub. 4345 (Settlements — Taxability)
