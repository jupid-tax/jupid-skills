# Example: $5,000 Non-Qualified 529 Withdrawal (Taxable + 10% Additional Tax)

The pattern when a 529 owner takes money out for non-education purposes (or the beneficiary changed plans), with no exception available. Demonstrates the Schedule 1 Line 8z + Schedule 2 Line 8 + Form 5329 Part II flow.

## The filer

- **Account owner / 1099-Q recipient**: Marisol Reyes
- **Designated beneficiary**: Diego Reyes (her son, who decided not to pursue higher education and instead joined a non-registered trade program that doesn't qualify as an eligible institution)
- **Plan**: Utah's my529 (a state 529)
- **Tax year**: 2025 (filing in 2026)
- **Marisol's filing status**: Single; AGI $78,000

Marisol pulled $5,000 from the 529 to use for a kitchen renovation, knowing it was non-qualified. She wants the worksheet to confirm the tax owed.

## 1099-Q received

```
Box 1 (Gross distribution):        $5,000
Box 2 (Earnings):                  $1,750
Box 3 (Basis):                     $3,250
Box 4 (Trustee-to-trustee):        Unchecked
Box 5 (Program type):              State 529
Box 6 (Designated beneficiary):    Unchecked (recipient is account owner)
Recipient: Marisol Reyes
Payer: Utah my529
```

Verification: Box 1 = Box 2 + Box 3 → $5,000 = $1,750 + $3,250 ✓

## Qualified Education Expenses (Step 3)

Diego had no qualified expenses in 2025. He attended a six-week non-registered trade program at a non-Title-IV-eligible school. Per the agent's check at fafsa.gov, that program is not on the Department of Education's eligible list.

```
Total QHEE = $0
```

## AAQEE Adjustment (Step 4)

```
AAQEE = $0 − $0 (scholarships) − $0 (other adjustments) = $0
```

## Step 5 — Compute taxable earnings

```
Box 1 = $5,000
AAQEE = $0

Non-qualified portion = $5,000 − $0 = $5,000  (the entire distribution)
Earnings ratio = $1,750 / $5,000 = 0.35

Taxable earnings = $5,000 × 0.35 = $1,750
                 = Box 2 (the entire earnings portion)
```

The full earnings portion is taxable because the entire distribution is non-qualified.

## Step 6 — 10% additional tax

No exceptions apply:
- Diego is alive and not disabled
- He didn't receive a tax-free scholarship
- He didn't attend a U.S. service academy
- The distribution wasn't taxable solely because of AOTC/LLC coordination — it's just non-qualified

```
10% additional tax = $1,750 × 10% = $175
```

## Step 7 — SECURE 2.0 rollover

Not applicable. The withdrawal is to Marisol for personal use, not a Roth IRA rollover.

## The completed worksheet

```markdown
# Form 1099-Q — DRAFT WORKSHEET for tax year 2025

## 1099-Q received
- Recipient: Marisol Reyes (account owner)
- Trustee/custodian: Utah my529
- Box 1 (Gross distribution): $5,000
- Box 2 (Earnings): $1,750
- Box 3 (Basis): $3,250
- Box 4 (Trustee-to-trustee transfer): No
- Box 5 (Program type): State 529
- Box 6 (Designated beneficiary is recipient): No

## Qualified Education Expenses
Total QHEE: $0 (Diego did not enroll in an eligible institution in 2025)

## AAQEE Adjustment
- Tax-free scholarships:               −$0
- Employer education assistance:       −$0
- Expenses used for AOTC:              −$0
- Expenses used for LLC:               −$0
- **Adjusted QHEE (AAQEE)**:           $0

## Taxable amount calculation
- Box 1:                          $5,000
- AAQEE:                          $0
- Non-qualified portion:          $5,000
- Earnings ratio (Box 2 / Box 1): 0.35
- **Taxable earnings**:           $1,750

## 10% additional tax
- Subject to 10% additional tax: Yes
- Exception applied:             None (no scholarship, no disability, no AOTC coordination)
- **Additional tax owed**:       $175

## Where this goes on the return
- Schedule 1 Line 8z: $1,750 (description: "Taxable 529 distribution")
- Schedule 2 Line 8 via Form 5329 Part II: $175 (10% additional tax on $1,750)
- 1040 Line 8: includes $1,750 from Schedule 1 Line 10
- 1040 Line 23: includes $175 from Schedule 2

## Total federal tax impact
At 22% marginal rate (single filer, $78K AGI):
- Income tax on $1,750: ~$385
- Additional 10% tax: $175
- **Total federal cost: $560**
- Effective tax rate on the $1,750 of earnings: 32% (22% income + 10% additional)

(State tax also applies. Utah may also recapture any prior state tax deduction
on the non-qualified portion — verify with state tax skill or professional.)

## Validation summary
- Math: all checks passed
  - Box 1 = Box 2 + Box 3: ✓
  - AAQEE ≤ Total QHEE: ✓ (both are $0)
  - Taxable earnings = Box 2 (full earnings, fully non-qualified): ✓
  - 10% additional tax = Taxable earnings × 10%: $175 ✓
- Sanity:
  - Entire distribution non-qualified — confirmed with user that no expenses qualified
  - No SECURE 2.0 rollover claimed
- Next steps:
  - Marisol files Schedule 1, Schedule 2, and Form 5329 with her single 1040
  - No Form 8863 (no AOTC/LLC available — Diego didn't enroll in eligible institution)
  - Marisol retains 1099-Q and worksheet for 3+ years
  - Consider: should Diego be removed as beneficiary and a different beneficiary
    designated to avoid future non-qualified distributions? (Planning question — refer to a CPA.)

## Sources cited in this draft
- IRS Form 1099-Q (Rev. 2025)
- IRC §529 (Qualified Tuition Programs)
- IRC §529(c)(3)(D) — Earnings allocation rule
- IRC §529(c)(6) — 10% additional tax
- IRC §529(c)(6)(B) — Exceptions (none applied here)
- Pub 970 chapter 8
- Form 5329 (Additional Taxes on Qualified Plans), Part II
```

## Why each non-obvious choice

**Why is the entire $1,750 taxable rather than a fraction?** AAQEE = $0 means *no portion* of the $5,000 distribution corresponds to qualified expenses. The non-qualified portion = the entire $5,000. The earnings ratio (0.35) applied to $5,000 gives $1,750 = the full Box 2 earnings.

**Why no exception to the 10% additional tax?** None of the IRC §529(c)(6)(B) exceptions apply. Marisol used the money for a kitchen renovation, not any qualifying purpose. The "AOTC coordination" exception requires the distribution be taxable *because of* the credit — here, no credit is involved.

**Why didn't Marisol consider a beneficiary change instead?** A beneficiary change to a "member of the family" of Diego (e.g., a younger sibling, a niece) under IRC §529(e)(2) is non-taxable. If Marisol had a younger child or a niece/nephew, she could have transferred Diego's account balance to that person and avoided this entire tax bill. This is a planning consideration, but the agent should mention it for next time.

**Why did the trade program not qualify?** IRC §529(e)(5) requires an "eligible educational institution" — one eligible for federal student aid under HEA Title IV. The trade program in question wasn't accredited under HEA, wasn't on the FAFSA school code list, and didn't participate in federal student aid. So distributions to pay for it would not have been qualified anyway.

**Could Marisol have used it for student loan repayment instead?** Yes, IRC §529(c)(9) allows up to $10,000 lifetime per beneficiary for qualified student loan repayment. If Diego had qualifying student loans from a prior period, Marisol could have used the $5,000 against those. But since Diego had no qualifying loans, this option didn't apply.

**Could she have done a Roth rollover instead?** IRC §529(c)(3)(E) requires the 529 to be 15+ years old and the beneficiary (Diego) to have earned income at least equal to the rollover amount. The agent didn't ask about account age, but assuming the 529 was opened when Diego was young (let's say 2015 — 10 years old), the account is only 10 years old in 2025 — failing the 15-year test. Not available.

**Audit defense**: Marisol's records show no QHEE and a clear non-qualified use. The IRS will not contest this — it's a clean reporting of a non-qualified distribution. The 1099-Q matches the return.
