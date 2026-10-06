# Example: Settlement Payment Through Attorney's Trust Account

A complete walkthrough of a $3,500 settlement paid to the claimant's attorney, illustrating Box 10 (gross proceeds to the attorney) and Box 3 (the claimant's full taxable damages). Shows why the payer issues no 1099-NEC for the attorney's fee, and that the attorney rule applies to corporate firms too.

Rules used: Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026), "Payments to attorneys", "Gross proceeds paid to attorneys", Box 3, Box 10; IRC §6045(f); Reg. §1.6045-5(f), Examples 2–3; Reg. §1.6041-1(f).

## The setup

- **Defendant / Payor**: Riverstone Industries Inc. (C-corp; defendant in a contract dispute)
- **Plaintiff**: Marcus Chen (former independent contractor; claim was for unpaid invoices for his contracting services — a contract dispute, NOT a personal physical injury, so no §104 exclusion)
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

- **Box 10 (gross proceeds paid to attorney)**: $3,500 — the full amount paid to the attorney ($3,500 ≥ $600, the §6045(f) threshold, unchanged for 2026)
- **Box 1**: $0
- **Box 3**: $0
- **Box 4**: $0 (no backup withholding; attorney supplied its TIN on a W-9)

**Would it matter if the firm were a corporation?** No. The exemption for payments to corporations does not apply to payments for legal services, so Box 10 is reportable whether the firm is a partnership, LLC, or professional corporation (Instructions, "Payments to corporations for legal services").

### No 1099-NEC to Park & Sussman for the $1,050 fee

The $1,050 is the claimant's attorney's fee, paid out of the settlement. The instructions: "Generally, you are not required to report the claimant's attorney's fees." A 1099-NEC box 1a goes only to an attorney the payer itself engaged for legal services (e.g., Riverstone's own defense counsel, if paid $2,000 or more in 2026). The answer is the same whatever the plaintiff's firm's entity type.

### Form 2: 1099-MISC to Marcus Chen (the plaintiff)

- **Box 3 (other income)**: $3,500 — the **full** taxable damages, not the $2,450 net. The payer reports the claimant's gross amount even though part of it was paid to the attorney (Reg. §1.6045-5(f), Example 3; Reg. §1.6041-1(f)). $3,500 ≥ $2,000, the 2026 §6041 threshold.

**Why Box 3?** The damages are taxable (contract dispute, not personal physical injury), so IRC §104(a)(2) does not exclude them, and taxable damages go in Box 3 (Instructions, Box 3 item 6).

If the claim had been for personal physical injury with no punitive damages: Box 10 = $3,500 to the attorney and **no** form to Marcus (Instructions, Box 3 item 6a; Reg. §1.6045-5(f), Example 2).

## W-9 verification before issuance

Before filing, Riverstone confirmed:
- W-9 from Park & Sussman LLC: Line 3a "Limited liability company" with tax classification "P" (partnership); TIN is the LLC's EIN
- W-9 from Marcus Chen: Line 3a "Individual/sole proprietor"; TIN is Marcus's SSN

TIN matching:
- Park & Sussman LLC EIN matched IRS records
- Marcus Chen SSN matched IRS records

## Filing checklist

| Form | Issued to | Box | Recipient deadline | IRS deadline |
|------|-----------|-----|--------------------|--------------|
| 1099-MISC | Park & Sussman LLC | Box 10 = $3,500 | Feb 16, 2027 (Box 10 statements are due February 15, which is Presidents' Day in 2027) | Mar 31, 2027 (electronic) / Mar 1, 2027 (paper) |
| 1099-MISC | Marcus Chen | Box 3 = $3,500 | Feb 1, 2027 (January 31 is a Sunday) | Mar 31, 2027 (electronic) / Mar 1, 2027 (paper) |

Sources for the dates: Instructions, "Statements to Recipients"; Pub. 1099 (2026), Reminders (February 15 for Boxes 8 and 10); next business day rule.

## How each party reports

### Park & Sussman LLC (the partnership)

The partnership recognizes only the **fee income** ($1,050) as gross receipts on Form 1065. Copy B, Box 10: "Report only the taxable part as income on your return." The partnership's books show:

- Inflow to trust account: $3,500 (asset; not income)
- Disbursement to client: $2,450 (decrease in asset; not expense)
- Transfer of fee to operating account: $1,050 (income recognized at this point)

The partnership reports $1,050 on Form 1065 Line 1a (gross receipts). Schedule K-1 to each partner allocates their share. The 1099-MISC Box 10 ($3,500) is reconciled with the client distribution statement.

### Marcus Chen (the plaintiff)

Marcus received a 1099-MISC with $3,500 in Box 3, so his return must account for $3,500, not $2,450. Where it goes depends on facts the agent must ask about:

- **If his contracting is an ongoing trade or business and the claim was for unpaid business invoices**: Copy B, Box 3 says to report trade or business income on Schedule C. Schedule C Line 1 includes $3,500; the $1,050 attorney fee is a business legal expense (Schedule C Line 17). Net profit is subject to SE tax.
- **If not a trade or business**: Schedule 1 Line 8z, $3,500 ("Settlement, Riverstone Industries"). The $1,050 fee is not deductible: it is not a discrimination or whistleblower claim (IRC §62(a)(20)–(21)), and miscellaneous itemized deductions are disallowed (IRC §67(g)).

The payer's choice of Box 3 does not decide the schedule; the character of the claim does. Ask the user and flag the choice for a CPA.

### Riverstone Industries Inc.

Riverstone deducts the $3,500 settlement as a business expense on its Form 1120 (subject to ordinary deductibility rules under IRC §162). The deduction is for the full $3,500, regardless of how it was split between Marcus and Park & Sussman.

## What if §104 had applied (personal physical injury)?

Suppose the underlying claim was Marcus suing Riverstone for an injury at Riverstone's facility (broken ankle), with no punitive damages.

- §104(a)(2) excludes the damages from Marcus's gross income
- Riverstone still issues 1099-MISC Box 10 = $3,500 to Park & Sussman (gross-proceeds reporting is independent of recipient tax treatment)
- Riverstone does **not** issue a Box 3 to Marcus (Instructions, Box 3 item 6a; Reg. §1.6045-5(f), Example 2: "P does not file an information return with respect to tax-free damages paid to C")

## What if Park & Sussman had been a professional corporation (PC)?

- 1099-MISC Box 10 = $3,500 (still reportable; no corporate exemption for legal services)
- No 1099-NEC (same as for the partnership: the payer does not report the claimant's attorney's fees)

The PC reports the $1,050 fee as corporate income on Form 1120 / 1120-S.

## Sources cited
- IRS Form 1099-MISC, Rev. December 2026
- IRS Instructions for Forms 1099-MISC and 1099-NEC, Rev. December 2026 ("Payments to attorneys", "Gross proceeds paid to attorneys", "Payments to corporations for legal services", Box 3, Box 10)
- Pub. 1099 (2026), Reminders (February 15 statement date for Boxes 8 and 10)
- IRC §6041 (as amended by P.L. 119-21 §70433), §6045(f) (gross proceeds to attorney), §104(a)(2), §62(a)(20)–(21), §67(g), §162
- Reg. §1.6045-5(f), Examples 2–3; Reg. §1.6041-1(f); Reg. §1.6041-3(p)(1)
- IRS Pub. 4345 (Settlements — Taxability)
