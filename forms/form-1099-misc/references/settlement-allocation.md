# Settlement Allocation — Splitting Across Boxes 3, 10, and 1099-NEC

The trickiest 1099-MISC scenario is reporting a legal settlement that flowed through an attorney's trust account. Multiple forms can be required to a single transaction, going to multiple recipients.

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

- **Through trust account**: Box 10 reporting applies (gross proceeds to attorney)
- **Directly to plaintiff**: only the plaintiff gets a 1099-MISC Box 3 (no Box 10 to attorney because attorney didn't receive the funds)

### Q2: Is the underlying claim for personal physical injury?

- **Personal physical injury** (e.g., car accident, medical malpractice, slip-and-fall causing bodily harm): the plaintiff's portion may be excluded from gross income under **IRC §104(a)(2)**. Even so, the defendant still issues a 1099-MISC to the attorney for Box 10 (gross proceeds) and may or may not need to issue Box 3 to the plaintiff (more on this below).
- **Non-physical injury** (employment dispute, breach of contract, defamation, emotional distress not arising from physical injury, lost wages, punitive damages): the plaintiff's portion is taxable as ordinary income; report on Box 3.

### Q3: Is the attorney a corporation?

- **Corporate attorney (PC, PLLC, LLC taxed as corp)**: Box 10 still reportable (special rule for attorneys). 1099-NEC for the fee component — NOT reportable (general corporate exemption applies to 1099-NEC).
- **Non-corporate attorney**: Box 10 reportable. 1099-NEC for the fee component — also reportable.

### Q4: How to allocate fee vs. plaintiff portion?

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

The **defendant / payor** issues all 1099-MISC forms in a settlement. The plaintiff doesn't issue 1099s; the attorney doesn't issue 1099s back to the defendant.

### Q6: What about §104 exclusions?

Under IRC §104(a)(2), damages received "on account of personal physical injuries or physical sickness" are excluded from gross income. The IRS treats this exclusion as applying to:
- Compensatory damages for medical expenses, lost wages (related to physical injury), pain and suffering arising from physical injury

But NOT to:
- Punitive damages (always taxable)
- Pre-judgment interest (always taxable)
- Damages for non-physical injuries (defamation, age discrimination, etc.)
- Damages for emotional distress NOT arising from physical injury

The defendant still issues a 1099-MISC to the attorney for Box 10 (gross proceeds reporting is informational, regardless of the recipient's tax treatment). Whether to issue a Box 3 to the plaintiff is more nuanced:

- If the defendant has reason to believe the plaintiff's portion is fully excluded under §104, they may not issue Box 3 (the safe-harbor approach). However, defendants often issue Box 3 to the plaintiff anyway and let the plaintiff exclude it on their return. Conservative practice: issue.
- For mixed claims (some physical injury + some non-physical), the safest approach is to allocate based on the settlement agreement and issue Box 3 only for the non-§104 portion.

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

2. **1099-NEC to attorney**:
   - Box 1 (nonemployee compensation — the attorney's fee for services): **$20,000**
   - The partnership is non-corporate, so 1099-NEC applies (would be exempted only if the attorney were a corporation)

3. **1099-MISC to plaintiff Jordan Lee**:
   - **Optional / debated**: Many insurers issue Box 3 = $38,500 to the plaintiff regardless, on the theory that gross-proceeds reporting protects the payor from later IRS challenges. Other insurers don't issue if the §104 exclusion clearly applies to the entire settlement.
   - Conservative: issue Box 3 = $38,500 with a note that the plaintiff may exclude under §104.
   - Aggressive: don't issue.
   - In practice: most insurers issue. Plaintiff excludes on their return if §104 applies.

### What each party reports

- **Attorney (the partnership)**: Reports $20,000 (1099-NEC) on the partnership's Form 1065 as gross receipts. The Box 10 $60,000 is informational; the partnership recognizes $20,000 as fee income and records $40,000 as a fiduciary disbursement (not their income). The partnership records the $1,500 cost reimbursement as cost recovery, not income.
- **Plaintiff Jordan Lee**: If §104 applies, excludes the $38,500 from income. May need to attach an explanatory statement if a Box 3 was issued.
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

2. **1099-NEC to attorney**:
   - **Not issued**. Rivera Law PC is a corporation; standard corporate exemption applies to 1099-NEC.

3. **1099-MISC to plaintiff Sam Rivera**:
   - Box 3 (other income): **$60,000** (plaintiff's portion, taxable)
   - Sam reports on Schedule 1 Line 8z.

   But wait — there's a question of whether the **entire $100,000** is income to Sam (gross-up theory) or just the $60,000 net. In employment cases involving lost wages, the IRS sometimes argues the full settlement (including attorney fees paid by Sam) is income, with Sam claiming the attorney fee as an "above-the-line" deduction under §62(a)(20) (for discrimination cases specifically). For age discrimination under ADEA, §62(a)(20) provides an above-the-line deduction for attorney fees, so:
   - Sam reports $100,000 as income (Schedule 1 Line 8z)
   - Sam deducts $40,000 attorney fees on Schedule 1 Line 24h (above-the-line)
   - Net taxable: $60,000

   The 1099-MISC Box 3 reflects the gross income recognized by Sam. Practice varies — some payors issue $100,000, some $60,000. Conservative: $100,000 (matches the actual gross income recognition), let Sam claim the offsetting deduction.

## When backup withholding applies

If the attorney or plaintiff doesn't have a valid W-9 / TIN, the defendant must apply 24% backup withholding (IRC §3406) on:
- Settlement disbursements to the attorney's trust account (the gross proceeds in Box 10 — withhold from the entire $S amount before depositing in trust)
- Direct disbursements to the plaintiff (if any)

Box 4 (federal tax withheld) reports the withholding amount. Form 945 reconciles annually.

In practice, defendants insist on W-9s before disbursing settlements. Sloppy W-9 hygiene at this stage creates expensive cleanup.

## State considerations

State 1099 reporting may parallel federal but with different thresholds. California, New York, and others have specific rules for settlement reporting. Verify with each state's department of revenue.

## Audit defense

For the defendant / payor:
- Retain settlement agreements showing the allocation of damages (physical injury vs. non-physical, fees vs. plaintiff portion)
- Retain W-9s for attorney and plaintiff
- Retain Form 1099-MISC and 1099-NEC copies
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

- **IRC §6041** — General requirement to file information returns for $600+ payments
- **IRC §6045(f)** — Returns relating to payments to attorneys (statutory authority for Box 10 reporting)
- **Reg. §1.6041-1(d)(2)** — Special rule that the corporate exemption does NOT apply to attorney legal-services payments
- **IRC §104(a)(2)** — Exclusion from income for damages received on account of personal physical injuries
- **IRC §62(a)(20)** — Above-the-line deduction for attorney fees in discrimination cases
- **IRS Publication 4345** — Settlements — Taxability
