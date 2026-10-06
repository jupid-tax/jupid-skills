# Settlement Allocation — Boxes 3 and 10

The trickiest 1099-MISC scenario is reporting a legal settlement that flowed through an attorney's trust account. Multiple forms can be required for a single payment, going to multiple recipients.

Authority: Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026), "Payments to attorneys", "Gross proceeds paid to attorneys", Box 3 item 6, Box 10; IRC §6045(f); Reg. §1.6045-5 (Examples 1–4 in paragraph (f)); Reg. §1.6041-1(f).

This file walks through the allocation logic.

## The basic setup

Three parties:

1. **Defendant / payor** — issues the settlement check (often via an insurance company)
2. **Plaintiff** — the recipient of the settlement (the person who was harmed / had a claim)
3. **Attorney** — represents the plaintiff; receives the settlement check into their trust account, takes their fee, remits the rest to the plaintiff

Money flow:

```
Defendant → Attorney's trust account → (split) → Plaintiff (most) + Attorney (fee)
```

## Reporting decision tree

For each settlement, the agent answers six questions in order:

### Q1: Did the settlement pass through the attorney's trust account, or directly to the plaintiff?

- **Paid to the attorney (or a check payable jointly to attorney and plaintiff, delivered to the attorney)**: Box 10 reporting applies (gross proceeds to attorney, $600 or more)
- **Directly to plaintiff**: only the plaintiff gets a 1099-MISC Box 3, if the damages are taxable (no Box 10 because the attorney didn't receive the funds)

### Q2: Is the underlying claim for personal physical injury?

- **Personal physical injury** (e.g., car accident, medical malpractice, slip-and-fall causing bodily harm): compensatory damages are excluded under **IRC §104(a)(2)**. The defendant still issues a 1099-MISC to the attorney for Box 10 (gross proceeds) and does **not** report the non-punitive damages to the plaintiff (Instructions, Box 3 item 6a; Reg. §1.6045-5(f), Example 2). Punitive damages are reported in Box 3 even when they relate to physical injury.
- **Non-physical injury** (breach of contract, defamation, discrimination, emotional distress not arising from physical injury, punitive damages): taxable; report the **full** amount in Box 3. Back pay that is wages goes on Form W-2 instead (Instructions, Box 3 tip; Pub. 957).

### Q3: Does the attorney's entity type matter?

- **No.** Box 10 is reportable to corporate and non-corporate attorneys alike (Instructions, "Payments to corporations for legal services").
- **The payer does not issue a 1099-NEC for the claimant's attorney's fee**, whatever the firm's entity type: "Generally, you are not required to report the claimant's attorney's fees" (Instructions, "Gross proceeds paid to attorneys"). A 1099-NEC box 1a goes only to the payer's **own** attorney for legal services provided to the payer.

### Q4: How to allocate fee vs. plaintiff portion? (plaintiff's own records only)

The payer does not need this split for its forms: Box 10 is the amount paid to the attorney and Box 3 is the full taxable damages. The split matters for the plaintiff's return (deductibility of the fee) and the attorney's books.

Standard contingency-fee math:

- Total settlement: $S
- Attorney's contingency %: f (e.g., 33.33%)
- Attorney's fee: F = S × f
- Plaintiff's portion: P = S − F (minus any costs / expenses if reimbursed to attorney)

For simple contingency: P + F = S.

For more complex arrangements (hourly + contingency, costs advanced by attorney, multiple lien claims):
- Subtract attorney's cost reimbursements from S first (those aren't attorney's fee, they're cost recovery)
- Subtract any third-party liens (Medicare set-aside, ERISA recovery, etc.)
- Net to plaintiff: P_net

### Q5: Who issues each form?

The **defendant / payor** (or its insurer, if the insurer makes the payment) issues the 1099-MISC forms in a settlement. The plaintiff doesn't issue 1099s; the attorney doesn't issue 1099s back to the defendant.

### Q6: What about §104 exclusions?

Under IRC §104(a)(2), damages received "on account of personal physical injuries or physical sickness" are excluded from gross income. The IRS treats this exclusion as applying to:
- Compensatory damages for medical expenses, lost wages (related to physical injury), pain and suffering arising from physical injury

But NOT to:
- Punitive damages (always taxable)
- Pre-judgment interest (always taxable)
- Damages for non-physical injuries (defamation, age discrimination, etc.)
- Damages for emotional distress NOT arising from physical injury

The defendant still issues a 1099-MISC to the attorney for Box 10 (gross proceeds reporting is informational, regardless of the recipient's tax treatment). For the plaintiff:

- Damages (other than punitive) received on account of personal physical injury or physical sickness: **do not report** in Box 3 (Instructions, Box 3 item 6a). Also not reportable: amounts not over the medical care paid for emotional distress, and damages for replacement of capital (items 6b–6d).
- For mixed claims (some physical, some non-physical), allocate per the settlement agreement and report in Box 3 only the taxable portion (e.g., the punitive or nonphysical part), in full, not net of the attorney's fee. If the agreement doesn't allocate, ask the user to get the allocation from counsel before filing.

## Worked example: typical contingency settlement

### Scenario

- Defendant: ABC Insurance Co. (paying on behalf of its insured)
- Plaintiff: Jordan Lee (slipped on a wet floor at insured's grocery store, broke ankle)
- Attorney: Lee, Park, & Associates LLP (partnership)
- Settlement amount: $60,000
- Attorney's contingency: 33.33% = $20,000
- Attorney's costs (medical record retrieval, depositions): $1,500 reimbursed
- Plaintiff's net: $60,000 − $20,000 − $1,500 = $38,500

### §104 analysis

- The injury is a physical injury (broken ankle). §104(a)(2) applies to compensatory damages.
- All $60,000 is allocated to physical injury (no punitive component, no emotional distress component).
- Plaintiff's $38,500 portion: **excluded from income** under §104(a)(2). The plaintiff doesn't include this on their tax return as income.

### Forms ABC Insurance issues

1. **1099-MISC to attorney (Lee, Park, & Associates LLP)**:
   - Box 10 (gross proceeds paid to attorney): **$60,000**
   - All other boxes: $0 (or blank)

2. **No 1099-NEC to the attorney.** ABC does not report the claimant's attorney's fees.

3. **No 1099-MISC to plaintiff Jordan Lee.** The $60,000 is compensatory damages for a physical injury, which the instructions say not to report (Box 3 item 6a; Reg. §1.6045-5(f), Example 2).

### What each party reports

- **Attorney (the partnership)**: Reports its $20,000 fee as gross receipts on Form 1065. The Box 10 $60,000 is informational; the $38,500 paid to the client is not partnership income, and the $1,500 cost reimbursement is recovery of costs advanced. The partnership keeps the client distribution statement to reconcile Box 10.
- **Plaintiff Jordan Lee**: Excludes the damages under §104(a)(2); nothing to report and no form to reconcile.
- **Defendant / Insurer**: Records the $60,000 as a settlement expense (deductible per IRC §162 or as ordinary and necessary business expense for self-insured payors; or as an insurance claim payment for ABC).

## Worked example: employment discrimination settlement (no §104 exclusion)

### Scenario

- Defendant: XYZ Corp.
- Plaintiff: Sam Rivera (former employee, age discrimination claim)
- Attorney: Rivera Law PC (professional corporation)
- Settlement: $100,000
- Attorney's contingency: 40% = $40,000
- Plaintiff net: $60,000

### §104 analysis

- Age discrimination is NOT a physical injury → no §104 exclusion.
- All $100,000 is taxable somewhere.

### Forms XYZ Corp. issues

1. **1099-MISC to attorney (Rivera Law PC)**:
   - Box 10 (gross proceeds): **$100,000**
   - Reportable even though attorney is a corporation (special attorney rule).

2. **No 1099-NEC to the attorney.** Not because Rivera Law PC is a corporation (legal-services fees are reportable to corporations), but because XYZ does not report the claimant's attorney's fees.

3. **1099-MISC to plaintiff Sam Rivera**:
   - Box 3 (other income): **$100,000** — the full taxable damages, including the part paid to Sam's attorney (Reg. §1.6045-5(f), Example 3; Reg. §1.6041-1(f)). Assumes the agreement allocates the $100,000 to nonwage damages (e.g., ADEA liquidated damages, which the instructions list for Box 3); any back-pay portion that is wages goes on Form W-2.

   Sam's return: $100,000 of income (Schedule 1 Line 8z) and, because this is an unlawful-discrimination claim, the $40,000 attorney fee as an above-the-line deduction under IRC §62(a)(20) (Schedule 1 Line 24h on the 2025 form). Net: $60,000.

## When backup withholding applies

If the attorney or plaintiff doesn't provide a TIN, the defendant must apply 24% backup withholding (IRC §3406) on the reportable payment. The instructions: an attorney must promptly supply its TIN whether it is a corporation or other entity (it need not certify it); if it fails to, "you must backup withhold on the reportable payments." This covers:
- Gross proceeds paid to the attorney (Box 10)
- Taxable damages reportable to the plaintiff (Box 3)

Box 4 (federal tax withheld) reports the withholding amount. Form 945 reconciles annually.

In practice, defendants insist on W-9s before disbursing settlements. Sloppy W-9 hygiene at this stage creates expensive cleanup.

## State considerations

State 1099 reporting may parallel federal but with different thresholds and filing channels. Verify with each state's department of revenue; ask the user which states are involved.

## Audit defense

For the defendant / payor:
- Retain settlement agreements showing the allocation of damages (physical injury vs. non-physical, fees vs. plaintiff portion)
- Retain W-9s for attorney and plaintiff
- Retain Form 1099-MISC copies
- Retain attorney's certified statement of trust-account disbursements

For the plaintiff:
- Retain settlement agreement
- Retain attorney's distribution statement (showing fee, costs, net to plaintiff)
- If claiming §104 exclusion, retain medical records substantiating physical injury

For the attorney:
- Retain settlement check copy
- Retain trust-account ledger showing disbursements
- Retain client distribution statement

## Citations

- **IRC §6041** — General requirement to file information returns ($600 for 2025 payments; $2,000 for 2026 payments, P.L. 119-21 §70433)
- **IRC §6045(f)** — Returns relating to payments to attorneys (statutory authority for Box 10 reporting; $600)
- **Reg. §1.6045-5** — Gross proceeds paid to attorneys; Examples 1–4 (joint checks, separate checks, excludable damages)
- **Reg. §1.6041-1(f)** — Reporting the claimant's full taxable amount
- **Reg. §1.6041-3(p)(1)** — Corporate exemption, which does NOT apply to attorneys' fees or medical providers
- **Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026)** — "Gross proceeds paid to attorneys", Box 3 item 6
- **IRC §104(a)(2)** — Exclusion from income for damages received on account of personal physical injuries
- **IRC §62(a)(20)** — Above-the-line deduction for attorney fees in discrimination cases
- **IRS Publication 4345** — Settlements — Taxability
