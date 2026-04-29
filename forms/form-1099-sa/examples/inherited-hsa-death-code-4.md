# Example: Inherited HSA — Non-Spouse Beneficiary (Code 4)

A beneficiary inherits an HSA after the original account holder dies. The beneficiary is **not the spouse** (in this example, an adult child), so the HSA loses its tax-favored status and the entire balance becomes ordinary income to the beneficiary.

This case demonstrates Code 4 distribution treatment, the pre-death QME deduction, the absence of the 20% penalty (death exception), and the practical estate-planning ramifications.

## The filers

- **Decedent**: Robert Hayes (HSA account holder)
  - Died: March 18, 2025
  - Age at death: 67
  - HSA balance on date of death: $48,500
- **Beneficiary**: Sophie Hayes (Robert's adult daughter)
  - Age: 34
  - Filing status: Single
  - Tax year: 2025 (filing in 2026)
- **HSA custodian**: Lively (Robert's HSA was at Lively)
- **Robert's pre-death medical bills paid by Sophie**: $2,800 (specifically: a March 10 emergency room visit, prescription costs from January-March, and an unpaid co-pay from late February)

## Inputs gathered

### 1099-SA from Lively (issued in Sophie's name as beneficiary)

```
PAYER: Lively Inc., EIN 81-XXXXXXX
RECIPIENT: Sophie Hayes, SSN ***-**-XXXX
(Note: Sophie's SSN; not Robert's — the 1099-SA issues in the recipient's name)

Box 1 (Gross distribution):                $48,500
Box 2 (Earnings on excess):                $0
Box 3 (Distribution code):                 4 (Death — non-spouse beneficiary)
Box 4 (FMV on date of death):              $48,500 (matches Box 1; distributed shortly after death)
Box 5 (Account type):                      [HSA checked]
```

### Distribution mechanics

Robert had named Sophie as his sole HSA beneficiary on his Lively beneficiary designation form. After Robert's death:

1. Sophie provided Lively with a death certificate (March 25, 2025)
2. Lively closed Robert's HSA and distributed $48,500 in cash to Sophie on April 8, 2025
3. The distribution arrived in Sophie's bank account; she now has it as ordinary cash

Sophie cannot roll the inherited HSA into her own HSA — that option is **only available to a spouse beneficiary** (Code 6 treatment). For non-spouse beneficiaries (children, parents, siblings), the HSA is fully distributed at death and the tax-favored status ends.

### Pre-death qualified medical expenses

Sophie used $2,800 of her own funds to pay Robert's pre-death medical bills:

| Date | Provider | Amount | What |
|------|----------|--------|------|
| Apr 5, 2025 | Memorial Hospital | $2,400 | Robert's March 10 ER visit (post-billing) |
| May 12, 2025 | CVS | $250 | Robert's January-March prescription refills (final bill) |
| Apr 22, 2025 | Dr. Patel | $150 | Unpaid co-pay from Feb 28 visit |
| **Total** | | **$2,800** | |

These are **Robert's** medical expenses incurred before his death (or for services rendered before death). Sophie paid them after his death using non-HSA funds.

Per IRC §223(f)(8)(A), Sophie can subtract the deceased's pre-death QME (paid within 1 year of death) from her taxable inheritance.

## Step-by-step computation

### Step 1 — Confirm Box 5 = HSA → Form 8889

Yes.

### Step 2 — Box 3 = Code 4 (Death distribution to non-spouse beneficiary)

Treatment:
- Box 1 ($48,500) is **fully taxable as ordinary income** to Sophie
- Sophie can subtract pre-death QME paid within 1 year of death (here: $2,800)
- **No 20% additional tax** (death exception per IRC §223(f)(4)(B))
- **No 6% excise** (no excess contribution at issue)

### Step 3-5 — Form 8889 Part II computation

The standard Form 8889 Part II structure handles non-spouse beneficiary inheritance with a special notation. Sophie reports:

```
Line 14a (Total distributions):              $48,500
Line 14b (Rollovers):                        $0  (rollovers not available to non-spouse)
Line 14c (14a − 14b):                        $48,500
Line 15 (QME paid using HSA):                $2,800  (deceased's pre-death QME within 1 year)
Line 16 (Taxable distributions):             $45,700  (= $48,500 − $2,800)
Line 17a (Exception):                        Death exception
Line 17b (20% additional tax):               $0  (death exception applies)
```

The $2,800 QME on Line 15 is unusual — it's not "QME paid using HSA" in the traditional sense; it's Sophie's payment of Robert's pre-death QME with non-HSA funds. The Form 8889 instructions and IRS Notice 2008-59 allow the deduction here as a special rule for non-spouse beneficiary scenarios. Sophie should attach a statement explaining the deduction and providing Robert's death date and the QME breakdown.

## The completed Form 8889 Part II draft

```markdown
# Form 8889 Part II — DRAFT for tax year 2025
(Beneficiary's tax return — Sophie Hayes, inheritor of Robert Hayes's HSA)

## 1099-SA(s) received

| Custodian | Box 1   | Box 2 | Box 3 | Box 4   | Box 5 |
|-----------|---------|-------|-------|---------|-------|
| Lively    | $48,500 | $0    | 4     | $48,500 | HSA   |
| **Total** | $48,500 |       |       |         |       |

## Pre-death QME breakdown (deceased's medical expenses paid by beneficiary within 1 year of death)

| Provider           | Date Paid | Amount | Service Date | Receipts? |
|--------------------|-----------|--------|--------------|-----------|
| Memorial Hospital  | Apr 5, 2025 | $2,400 | March 10, 2025 (pre-death) | Yes |
| CVS Pharmacy       | May 12, 2025 | $250 | Jan-Mar 2025 (pre-death)   | Yes |
| Dr. Patel          | Apr 22, 2025 | $150 | Feb 28, 2025 (pre-death)   | Yes |
| **Total**          |           | **$2,800** |                       |           |

## Form 8889 Part II — line-by-line

14a. Total distributions:                        $48,500
14b. Rollovers:                                  $0  (not available to non-spouse beneficiary)
14c. Subtract 14b from 14a:                      $48,500
15.  Qualified medical expenses (Robert's
     pre-death QME paid within 1 year):          $2,800
16.  Taxable HSA distributions (14a − 15):       $45,700  → Schedule 1 Line 8f
17a. Exception reason:                           Death of HSA holder (Robert Hayes, March 18, 2025)
17b. Additional 20% tax:                         $0  (death exception, IRC §223(f)(4)(B))

## Statement attached to Form 8889 (per IRS instructions)
"Sophie Hayes (SSN ***-**-XXXX) is the named beneficiary of the HSA of Robert Hayes
(deceased March 18, 2025). The HSA balance of $48,500 was distributed in full
to Sophie on April 8, 2025 by custodian Lively. Sophie subsequently paid
$2,800 in qualified medical expenses incurred by Robert before his death,
within 1 year of the date of death, per IRC §223(f)(8)(A). Receipts retained.
The death exception to the 20% additional tax under IRC §223(f)(4)(B) applies."

## Required attachments
- [x] Form 8889
- [x] Statement explaining inherited HSA and pre-death QME deduction
- [ ] Form 5329 — N/A
- [ ] Form 8853 — N/A

## Validation summary
- Math: all checks passed
  - Line 14c = $48,500 ✓
  - Line 15 = $2,800 (substantiated, all within 1 year of death) ✓
  - Line 16 = $45,700 ✓
  - Line 17b = $0 (death exception) ✓
- Sanity:
  - Box 3 = 4 → non-spouse beneficiary; no rollover available ✓
  - Box 4 = $48,500 (FMV on date of death) — informational, used for any later disputes about income recognition timing ✓
  - 20% penalty waived under death exception ✓
  - Pre-death QME within 1 year of death — all paid by April-May 2025, well within 1 year of March 18 death ✓
- Next steps:
  - Schedule 1 Line 8f: $45,700 (added to Sophie's AGI as ordinary income for tax year 2025)
  - Sophie's marginal rate: at her income (~$85K) she'll pay ~24% federal on the $45,700 = ~$10,968 in federal income tax
  - State income tax: depends on Sophie's state; most states tax ordinary income similarly
  - Schedule 2 Line 17c: $0 (no additional tax)
  - **Estate tax**: separately, Robert's estate may owe estate tax on Form 706 if his total estate exceeds the federal exemption ($13.99M for 2025) — likely not applicable, but the executor confirms

## Sources cited in this draft
- IRS Form 1099-SA, Rev. 2025
- IRS Instructions for Forms 1099-SA and 5498-SA, Rev. 2025
- IRS Form 8889, Rev. 2025
- IRS Pub 969 (HSAs and Other Tax-Favored Health Plans)
- IRC §223(f)(8)(A) (deceased's QME within 1 year)
- IRC §223(f)(8)(B) (spouse rollover — not applicable here)
- IRC §223(f)(4)(B) (death exception to 20% tax)
- IRS Notice 2008-59 (special rules for inherited HSAs)
```

## Why each non-obvious choice

**Why is the entire $48,500 taxable to Sophie?** When a non-spouse beneficiary inherits an HSA, the HSA's tax-favored status ends at the date of the account holder's death (IRC §223(f)(8)(A)). The full balance becomes ordinary income to the beneficiary in the year received. Compare to a spouse beneficiary (Code 6) who can keep the HSA as their own — non-spouse beneficiaries have no such option.

**Why no 20% additional tax?** IRC §223(f)(4)(B) waives the 20% additional tax in the case of death. Sophie's 20% would have been $9,140 — significant savings, but the exception only applies to the 20% penalty, not to the underlying income tax.

**Why does the $2,800 reduction work?** IRC §223(f)(8)(A) explicitly allows the beneficiary to subtract amounts used for the deceased's QME (paid within 1 year of death) from the taxable inheritance. This is a one-time, narrow rule designed to ease the tax burden when the deceased had unpaid medical bills at death.

**Why does Sophie attach a statement?** Form 8889 doesn't have a dedicated line for "I'm a non-spouse beneficiary of a deceased HSA holder," and Line 15 is normally "QME paid using HSA distributions." Sophie's $2,800 wasn't paid from the HSA — it was paid from her own funds. The statement clarifies the situation for the IRS.

**Why does the death certificate matter?** It's the substantiation for the death exception. If audited, the IRS will request the death certificate. Sophie should retain a certified copy.

**Could Sophie disclaim the inheritance?** Yes, under IRC §2518 a beneficiary can disclaim within 9 months of death. The HSA would then pass to the contingent beneficiary or to Robert's estate. But this is rarely advisable for an HSA — disclaiming sends the asset to the estate where it's still fully taxable to the estate (and no QME deduction is available to the estate).

**What if Sophie hadn't paid Robert's pre-death medical bills?** She'd lose the $2,800 reduction. Line 16 would be the full $48,500. She'd pay tax on the full amount.

**What about state tax?** Most states tax inherited HSA distributions as ordinary income (matching federal treatment). California, New York, etc., conform. Verify Sophie's state's specific rule.

**Could Robert have done estate planning to avoid this?** Several options exist:
1. **Spend down the HSA before death**: if Robert knew his health was failing, he could have used the HSA aggressively for QME, reducing the balance.
2. **Name his spouse as beneficiary** (if he had one — Robert was apparently single or widowed, so this didn't apply).
3. **Name a charity as beneficiary**: a charity inherits the HSA tax-free at the entity level (charities don't pay income tax).
4. **Name his estate**: doesn't help — the estate still pays tax.
5. **Convert to a life annuity** (some custodians offer this): would have shifted income recognition over time.

This is **estate planning advice** — out of scope for Form 1099-SA / Form 8889 reporting. Refer Sophie or the family to an estate planner.

## Audit defense

If the IRS questioned Sophie's Form 8889:
1. Sophie presents Robert's death certificate (showing March 18, 2025)
2. Sophie presents the Lively account statement showing the $48,500 distribution to her bank account on April 8, 2025
3. Sophie presents receipts for the $2,800 in pre-death QME, all paid by her in April-May 2025 (within 1 year of death)
4. Sophie's Schedule 1 Line 8f shows $45,700 added to AGI
5. Sophie's Schedule 2 Line 17c shows $0 (death exception applied)

The audit would close without changes. Sophie's record retention — death certificate, bank statements, QME receipts, beneficiary designation form — is the model for inherited-HSA reporting.
