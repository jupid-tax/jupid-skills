# Example: 2025 Joint Return That Skipped the Senior Deduction (Refund)

A retired couple filed their 2025 return in February 2026 without Schedule 1-A. Both were born before January 2, 1961, so each qualifies for the enhanced deduction for seniors introduced for tax year 2025. The amendment uses line 4b, the line added to Form 1040-X in the December 2025 revision. All 2025 figures come from the 2025 Instructions for Form 1040 and the 2025 Schedule 1-A. Math checked in Python (see notes file).

## The filers

- **Names**: Raymond and Lorna Whitfield, married filing jointly, Arizona residents
- **Born**: Raymond March 9, 1956; Lorna November 22, 1958 (both before January 2, 1961)
- **SSNs**: both valid for employment, issued decades ago (agent asked)
- **Tax year amended**: 2025 (amendment prepared October 2026)
- **Original return**: e-filed February 21, 2026; accepted; refund of $649 received March 2026
- **IRS contact so far**: none; no prior amendment

## Inputs gathered

### From the filed 2025 return (column A)

| Item | Amount |
|---|---|
| AGI (2025 Form 1040, line 11a; pensions, IRA distributions, taxable Social Security, interest) | $100,875 |
| Standard deduction, MFJ, both born before January 2, 1961 (2025 Standard Deduction Chart: 2 boxes checked) | $34,700 |
| QBI deduction | $0 |
| Schedule 1-A | not filed |
| Taxable income (line 15) | $66,175 |
| Tax (line 16), 2025 Tax Table row $66,150–$66,200, Married filing jointly | $7,464 |
| Nonrefundable credits / other taxes | $0 / $0 |
| Total tax (line 24) | $7,464 |
| Federal income tax withheld, Forms 1099-R (line 25b) | $8,113 |
| Overpayment (line 34) | $649 |

### The new information

The couple's preparer did not complete Schedule 1-A, Part V. Nothing else changes: AGI is unchanged because the Schedule 1-A deductions are taken after AGI (Form 1040 line 13b), so taxable Social Security and every AGI-based item stay the same.

## Step 1 — Should this be an amendment?

Yes. A missed deduction changes taxable income and tax (row 13 of [`../references/when-not-to-amend.md`](../references/when-not-to-amend.md)). The original refund has already been received, so the "wait for the original refund" rule (row 4) is satisfied.

## Step 2 — Deadline check (refund claim)

| Test | Result |
|---|---|
| Original filed | February 21, 2026 (before the due date) |
| Deemed filed (§6513(a)) | April 15, 2026, the 2025 due date per the 2025 Instructions for Form 1040 |
| 3-year window ends | April 15, 2029. That date is a Sunday, so IRC §7503 moves the last day to the next day that is not a Saturday, Sunday, or District of Columbia legal holiday; the agent does not plan around the extra days |
| Tax paid in lookback | Withholding $8,113, deemed paid April 15, 2026 (§6513(b)(1)): inside the lookback |
| Result | Timely; no cap issue |

## Step 3 — Schedule 1-A (2025), Part V

| Line | Computation | Amount |
|---|---|---|
| 1 / 3 | Form 1040 line 11b (no excluded income on line 2e) | $100,875 |
| 31 | from line 3 | $100,875 |
| 32 | MFJ | $150,000 |
| 33 | $100,875 − $150,000 ≤ 0 → enter $6,000 on line 35 | — |
| 35 | | $6,000 |
| 36a | Raymond: valid SSN, born before 01/02/1961 | $6,000 |
| 36b | Lorna: MFJ, valid SSN, born before 01/02/1961 | $6,000 |
| 37 | Enhanced deduction for seniors | $12,000 |
| 38 | Total → Form 1040 line 13b and Form 1040-X line 4b | **$12,000** |

Corrected taxable income: $66,175 − $12,000 = **$54,175**. Tax: 2025 Tax Table row $54,150–$54,200, MFJ = **$6,024**.

## The completed Form 1040-X draft

```markdown
# Form 1040-X — DRAFT amending tax year 2025
Form revision used: Form 1040-X (Rev. December 2025)

## Header
Tax year amended: 2025
Names / SSNs: Raymond Whitfield XXX-XX-XXXX; Lorna Whitfield XXX-XX-XXXX (original order)
Current address: <current address>
Presidential Election Campaign: no change
Amended return filing status: Married filing jointly (original: Married filing jointly)

## Lines 1–23
| Line | Description | A | B | C |
|---|---|---:|---:|---:|
| 1 | Adjusted gross income | 100,875 | 0 | 100,875 |
| 2 | Standard deduction | 34,700 | 0 | 34,700 |
| 3 | Line 1 − line 2 | 66,175 | 0 | 66,175 |
| 4a | QBI deduction | 0 | 0 | 0 |
| 4b | Schedule 1-A deductions | 0 | 12,000 | 12,000 |
| 5 | Taxable income | 66,175 | (12,000) | 54,175 |
| 6 | Tax (method: Table) | 7,464 | (1,440) | 6,024 |
| 7 | Nonrefundable credits | 0 | 0 | 0 |
| 8 | Line 6 − line 7 | 7,464 | (1,440) | 6,024 |
| 9 | Reserved | — | — | — |
| 10 | Other taxes | 0 | 0 | 0 |
| 11 | Total tax | 7,464 | (1,440) | 6,024 |
| 12 | Withholding | 8,113 | 0 | 8,113 |
| 13 | Estimated tax payments | 0 | 0 | 0 |
| 14 | Earned income credit | 0 | 0 | 0 |
| 15 | Refundable credits | 0 | 0 | 0 |
| 16 | Paid with extension/original/after filing | | | 0 |
| 17 | Total payments | | | 8,113 |
| 18 | Overpayment on original | | | 649 |
| 19 | Line 17 − line 18 | | | 7,464 |
| 20 | Amount you owe | | | 0 |
| 21 | Overpayment on this return | | | 1,440 |
| 22 | Refunded to you | | | 1,440 |
| 23 | Applied to 2026 estimated tax | | | 0 |

## Part I — Dependents
No change.

## Part II — Explanation of changes
We did not claim the enhanced deduction for seniors on our original 2025 return.
Both of us were born before January 2, 1961 and have valid Social Security numbers,
and our modified AGI of $100,875 is below $150,000, so each of us qualifies for the
full $6,000. We attached Schedule 1-A showing $12,000 on line 38 (line 4b). Taxable
income falls from $66,175 to $54,175 and tax from $7,464 to $6,024 using the 2025
Tax Table (line 6). No other items changed.

## Part III — Direct deposit (e-filed only)
Routing / account / type: collected at submission inside the software; not stored
in this draft.

## Statute check
- Original filed 02/21/2026 → deemed filed 04/15/2026
- 3-year window ends 04/15/2029 (a Sunday; IRC §7503 next-business-day rule applies; not relied on)
- Tax paid in lookback: $8,113 withholding → maximum refundable $8,113
- Result: timely; full $1,440 refundable

## Attachments
- Complete corrected 2025 Form 1040 (line 13b $12,000) with Schedule 1-A

## Filing channel
E-file through tax software (2025 is the current tax period); request direct deposit
(available for e-filed 1040-X for tax year 2021 and later).

## Validation summary
- Math: all checks passed (line 21 = 7,464 − 6,024 = 1,440; line 22 = line 21)
- Sanity: AGI unchanged as expected; 2025 standard deduction for two seniors used;
  Schedule 1-A attached; both spouses sign with Self-Select PINs
- Next steps: Arizona return — ask the Arizona Department of Revenue whether the
  federal change affects the state return; track at Where's My Amended Return

## Sources cited in this draft
- Form 1040-X (Rev. December 2025) and Instructions (Rev. December 2025): line 4b
- 2025 Schedule 1-A, Part V ($6,000 per person; $150,000 MFJ; 6% reduction;
  born before January 2, 1961; valid SSN; joint return required)
- 2025 Instructions for Form 1040 (standard deduction chart $34,700; Tax Table;
  due date April 15, 2026)
- IRC §6511(a), §6513(a), §6513(b)(1), §7503
- irs.gov Amended return FAQs (e-file, direct deposit)
```

## Why each non-obvious choice

**Why does line 1 not change?** The Schedule 1-A deductions are not adjustments to income; they are subtracted after AGI (Form 1040 line 13b, Form 1040-X line 4b). Because AGI is unchanged, taxable Social Security and other AGI-based items do not need refiguring.

**Why is line 21 only $1,440 when the corrected return shows a $2,089 overpayment?** The corrected Form 1040 would show $8,113 − $6,024 = $2,089 overpaid, but $649 of that was already refunded. Line 18 removes it, leaving the $1,440 that is new.

**Why check MAGI on Schedule 1-A instead of assuming the full deduction?** Line 33 reduces the $6,000 per person by 6% of MAGI over $150,000 for joint filers. The agent always computes lines 31–35; it never assumes the cap.
