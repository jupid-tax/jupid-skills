# Example: Retiree with Steady Income + Q4 Roth Conversion (Prior-Year Safe Harbor Saves Penalty)

A complete walkthrough of Form 2210 for retirees with steady Social Security and IRA distributions plus a large Q4 Roth conversion. Withholding they elected on the conversion meets the prior-year safe harbor, so there is no penalty without needing Schedule AI.

All figures use the 2025 Form 2210 and its instructions (2025 returns filed in 2026), the 2025 Form 1040 standard deduction, Rev. Proc. 2024-40 (2025 brackets, $1,600 additional standard deduction per spouse 65 or older), and the 2025 Schedule 1-A.

## The filer

- **Name**: Eleanor Park
- **Filing status**: Married Filing Jointly (spouse Bill, both retired, both 65 or older)
- **Income**:
  - Social Security: $48,000 combined ($28,000 Eleanor + $20,000 Bill)
  - Traditional IRA distributions: $60,000 ($40,000 Eleanor + $20,000 Bill), paid monthly
  - Taxable interest: $4,500
  - Ordinary dividends: $7,500 (none qualified: money market fund and REIT dividends)
  - Q4 Roth conversion (Eleanor's traditional IRA → Roth): $150,000 distributed in November 2025
- **Tax year**: 2025 (filing in 2026)
- **Prior year (2024)**: no Roth conversion; 2024 tax for Form 2210 line 8 $14,200, 2024 AGI $135,000

## Inputs gathered

```
Current-year income summary:
  Taxable SS (85% cap):     $40,800
  IRA distributions:        $60,000
  Interest:                 $4,500
  Dividends:                $7,500
  Roth conversion (taxable): $150,000
  Total income / AGI:       $262,800

Standard deduction (MFJ, both 65+, 2025): $34,700
                                          ($31,500 MFJ + $1,600 × 2)
Enhanced deduction for seniors (Schedule 1-A): $0
  ($6,000 each, reduced by 6% of MAGI over $150,000: $112,800 × 6% = $6,768 > $6,000)
Taxable income:                          $228,100
Federal income tax (2025 MFJ schedule):  $40,438  ($35,302 + 24% × $21,400)
NIIT (Form 8960, Schedule 2 line 12):    $456     (3.8% × $12,000 investment income;
                                                   MAGI exceeds $250,000 by $12,800)
Current-year tax (Form 2210 line 4):     $40,894

Withholding:
  IRA distributions: 10% default withholding = $6,000
  Roth conversion: Eleanor elected 20% on Form W-4R = $30,000
    (the $30,000 withheld is not converted; $120,000 reached the Roth IRA,
     and the full $150,000 is taxable)
  Social Security: 0% withheld (Eleanor and Bill didn't elect withholding)
  Total withholding: $36,000

Estimated tax payments: $0 (Eleanor counted on the conversion withholding)

Prior-year tax (line 8 basis): $14,200
Prior-year AGI: $135,000  → 100% safe harbor multiplier (AGI ≤ $150K)
```

## Step 1 — Run the page 1 flowchart

```
Test 1 — De minimis (line 7):
  $40,894 − $36,000 = $4,894, not less than $1,000. Fails.

Test 2 — No prior-year liability:
  Prior-year tax = $14,200 ≠ $0. Fails.

Test 3 — 90% current:
  Required: $40,894 × 90% = $36,805. Paid: $36,000. Fails.

Test 4 — 100% prior:
  Required: $14,200. Paid: $36,000 (withholding alone). PASSES ✓
```

Line 9 = smaller of $36,805 or $14,200 = $14,200. Line 6 ($36,000) is more than line 9, so there is no penalty and no Form 2210 is filed.

The withholding Eleanor elected on the Roth conversion ($30,000) was the key — together with the IRA withholding it cleared the prior-year safe harbor by a wide margin, even though it fell just short of 90% of the current-year tax.

## What if Eleanor had elected zero withholding on the Roth conversion?

IRA distributions are nonperiodic payments: the default federal withholding is 10%, and the recipient can elect a different rate, including 0%, on Form W-4R (IRC §3405(b)). Suppose Eleanor elected 0% on the conversion. Then:

```
Withholding:
  IRA distributions: $6,000
  Roth conversion: $0
  Total: $6,000

Test 1 — De minimis: $40,894 − $6,000 = $34,894, not less than $1,000. Fails.
Test 3 — 90% current: required $36,805; paid $6,000. Fails.
Test 4 — 100% prior: required $14,200; paid $6,000. Fails.

Penalty owed.
Required annual payment = smaller of $36,805 or $14,200 = $14,200.
```

Now it matters whether the income was uneven enough for Schedule AI to help. The Roth conversion happened in November 2025 (Q4). The other income (SS, IRA distributions, interest, dividends) arrived evenly: $4,000 of benefits, $5,000 of IRA distributions, and $1,000 of interest and dividends each month.

### Regular method

```
Line 10, each column: $14,200 × 25% = $3,550
Line 11, each column: withholding $6,000 ÷ 4 = $1,500

Line 17 (payments go to the earliest underpayment first):
  (a) $3,550 − $1,500 = $2,050
  (b) the $1,500 goes to (a) → line 16 $550 still unpaid from (a); line 17 $3,550
  (c) the $1,500 pays (a)'s $550, then $950 of (b) → (b) $2,600 left; line 17 $3,550
  (d) the $1,500 goes to (b) → (b) $1,100 left; line 17 $3,550
  Everything left is paid with the return on April 15, 2026.

Penalty (0.07 in every 2025 rate period):
  (a) $1,500 × 61 days (4/15–6/15/25)    = $17.55
      $550 × 153 days (4/15–9/15/25)     = $16.14
  (b) $950 × 92 days (6/15–9/15/25)      = $16.76
      $1,500 × 214 days (6/15/25–1/15/26) = $61.56
      $1,100 × 304 days (6/15/25–4/15/26) = $64.13
  (c) $3,550 × 212 days (9/15/25–4/15/26) = $144.33
  (d) $3,550 × 90 days (1/15–4/15/26)    = $61.27
  (each: amount × 0.07 × days ÷ 365)
  Total ≈ $382
```

### Schedule AI

Columns (a)–(c) contain only the even income, so their annualized income is the same: $112,800 ($60,000 IRA + $12,000 interest and dividends + $40,800 taxable SS, the taxable SS figured on the annualized amounts). Period AGI on line 1: $28,200 / $47,000 / $75,200; column (d) is the full year, $262,800.

```
Columns (a)–(c):
  Line 3 annualized income:         $112,800
  Line 7 standard deduction:        $34,700
  Senior deduction (line 14 adjustment per the 2025 instructions):
    annualized MAGI $112,800 < $150,000 → $6,000 × 2 = $12,000
  Taxable income:                   $66,100 → tax $7,458 (2025 Tax Table, MFJ)
  NIIT: $0 (annualized MAGI under $250,000)
  Line 21: $7,458 × 22.5% = $1,678.05;  × 45% = $3,356.10;  × 67.5% = $5,034.15
Column (d):
  Taxable income $228,100 → tax $40,438 + NIIT $456 = $40,894
  Line 21: $40,894 × 90% = $36,804.60

Lines 22–27 (line 24 = 25% × $14,200 = $3,550):
  (a) line 23 $1,678.05; line 26 $3,550.00 → line 27 $1,678.05
  (b) line 23 $1,678.05; line 26 $3,550 + $1,871.95 = $5,421.95 → line 27 $1,678.05
  (c) line 23 $1,678.05; line 26 $3,550 + $3,743.90 = $7,293.90 → line 27 $1,678.05
  (d) line 23 $31,770.45; line 26 $3,550 + $5,615.85 = $9,165.85 → line 27 $9,165.85
  Total $14,200.00 (the savings in (a)–(c) are recaptured in (d))

Part III with these installments (line 11 still $1,500 per column):
  Line 17: (a) $178.05  (b) $356.10  (c) $534.15  (d) $8,200.00
  Penalty: (a) $178.05 × 61 days = $2.08;  (b) $356.10 × 92 days = $6.28;
           (c) $534.15 × 122 days = $12.50; (d) $8,200 × 90 days = $141.53
  Total ≈ $162
```

**Schedule AI saves ~$220** vs. the regular method (~$382 → ~$162). Schedule AI can go below the regular installment in a column; the reduction is recaptured in later columns, here in column (d), where it accrues for only 90 days.

In this modified scenario, Eleanor would check box C and file Form 2210 with Schedule AI.

## Returning to the original scenario (Eleanor withheld 20% on the Roth conversion)

In the original scenario, withholding alone covered the prior-year safe harbor. The flowchart on page 1 resolves to "no penalty, no Form 2210" without needing Schedule AI or even computing penalty.

**This is the most important lesson from this example: withholding at the source on Roth conversions and IRA distributions is the easiest way to lock in the safe harbor.** Many retirees don't realize that custodians accept a withholding election (Form W-4R) on these distributions; the default for nonperiodic IRA distributions is 10%. A retiree with a one-time large income event (Roth conversion, RMD that triggers SS taxation jumps, capital gain on a stock sale, sale of a business) should consider directing extra federal withholding at the source.

## The completed Form 2210 draft (original scenario — no penalty)

```markdown
# Form 2210 — DRAFT for tax year 2025

## Filing decision
- [x] No Form 2210 needed (line 6 withholding ≥ line 9 required annual payment)

## Header
Name(s) shown on return:    Eleanor and Bill Park
Identifying number:         XXX-XX-XXXX (Eleanor, first-listed)
Filing status:              Married Filing Jointly
Prior-year AGI:             $135,000  → safe-harbor multiplier: 100%

## Part I (worksheet only)
1. Form 1040 line 22:                $40,438
2. Other taxes (Schedule 2 line 12): $456
3. Refundable credits:               $0
4. Current-year tax:                 $40,894
5. Line 4 × 90%:                     $36,805
6. Withholding:                      $36,000
7. Line 4 − line 6:                  $4,894
8. Prior-year tax × 100%:            $14,200
9. Required annual payment:          $14,200

## Page 1 flowchart result

| Test | Required | Paid | Result |
|------|----------|------|--------|
| 1. De minimis (line 7 < $1,000) | under $1,000 | $4,894 | Fails |
| 2. No prior-year liability | prior-year tax = $0 | $14,200 ≠ 0 | Fails |
| 3. 90% current | $36,805 | $36,000 (W/H only) | Fails |
| 4. 100% prior (line 9) | $14,200 | $36,000 (W/H only) | **MET** ✓ |

## Result
- No penalty under IRC §6654.
- No Form 2210 needs to be filed (no Part II box applies).
- Form 1040 line 38 (Estimated tax penalty): leave blank.

## Validation summary
- Withholding alone ($36,000) exceeds the required annual payment ($14,200, 100% of 2024 tax).
- The 20% withholding Eleanor elected on the Q4 Roth conversion ($30,000) was the
  decisive factor — it brought total withholding from $6,000 up to $36,000.
- For 2026 planning: the 2026 prior-year safe harbor rises to 110% of 2025 tax
  ($40,894 × 110% = $44,983) because 2025 AGI ($262,800) is over $150,000. Without another
  conversion, 90% of the lower 2026 tax will usually be the smaller target. If Eleanor and
  Bill expect another large income event, continue to use source withholding rather than
  relying on quarterly estimates.

## Sources cited in this draft
- IRS Form 2210 (2025)
- IRS Instructions for Form 2210 (2025)
- IRC §6654(d)(1)(B)(i) — 90% current-year required annual payment
- IRC §6654(d)(1)(B)(ii) — 100% prior-year safe harbor
- IRC §6654(g)(1) — Withholding treated as paid evenly
- IRC §3405(b) — Withholding on nonperiodic distributions (10% default; Form W-4R election)
- 2025 Schedule 1-A, lines 31–37 (enhanced deduction for seniors)
- Rev. Proc. 2024-40 (2025 brackets and additional standard deduction)
```

## Why each non-obvious choice

**Why does the Roth conversion withholding count toward the Form 2210 safe harbor?** All federal income tax withheld during the year — whether from W-2 wages, 1099 distributions, IRA conversions, Social Security, etc. — is treated as "withholding" for IRC §6654 purposes. It allocates evenly across quarters by default under IRC §6654(g)(1), regardless of when the withholding actually occurred.

This is critical for retirees: a single large Roth conversion in Q4 with elected federal withholding effectively "pre-pays" the tax for the conversion plus a cushion for the rest of the year's income, all from a single Q4 transaction. This is the clean way to handle a Roth conversion for safe-harbor purposes.

**Why doesn't the timing of the conversion (November) hurt for safe harbor purposes?** Because the withholding allocates evenly across quarters by default. The November $30,000 withholding is treated as $7,500 per quarter — even though it actually arrived in IRS coffers in November.

**Why is this NOT the same as making a $30,000 estimated payment in November?** Estimated payments are credited on the date actually paid; they don't allocate evenly. A $30,000 estimated payment on November 15 would count only from November 15, leaving the April, June, and September installments underpaid until then. By using *withholding* at the source, Eleanor gets the more favorable even-allocation treatment.

**What about the 110% safe harbor?** Eleanor's prior-year AGI was $135,000, under the $150,000 threshold. So 100% of prior-year tax applies, not 110%. Even if Eleanor's prior-year AGI had been $200,000, the 110% × $14,200 = $15,620 prior-year safe harbor would still be far below the $36,000 actual withholding, so the safe harbor would still be met.

**What if Eleanor had received a notice incorrectly assessing a penalty?** She would respond to the notice by filing Form 2210 retroactively to demonstrate the safe harbor calculation, OR file Form 843 (Claim for Refund and Request for Abatement) if the penalty was already paid.

**What audit defense does Eleanor have?** Form 1099-R from the IRA custodian shows the Roth conversion gross distribution ($150,000) and the 20% withholding ($30,000); Form 1099-R for the IRA distributions shows the 10% withholding ($6,000); these match Form 1040 line 25b (1099 federal income tax withheld). Form 5498 confirms the $120,000 Roth conversion contribution. The Form 2210 page 1 flowchart confirms the safe harbor was met. Clean trail.

**Planning recommendation for 2026 Roth conversions**: continue using source withholding at the time of the conversion, at a percentage that covers the marginal bracket on the conversion plus a buffer. If converting $200,000 in 2026 expecting it to land in the 24% bracket, withholding 28-30% covers the tax and leaves a cushion. The buffer counts toward the safe harbor through even allocation.
