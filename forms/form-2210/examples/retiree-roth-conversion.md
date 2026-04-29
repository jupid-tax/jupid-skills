# Example: Retiree with Steady Income + Q4 Roth Conversion (Prior-Year Safe Harbor Saves Penalty)

A complete walkthrough of Form 2210 for a retiree with steady Social Security and IRA distributions plus a large Q4 Roth conversion. The prior-year safe harbor exempts the entire penalty without needing Schedule AI.

## The filer

- **Name**: Eleanor Park
- **Filing status**: Married Filing Jointly (spouse Bill, both retired)
- **Income**:
  - Social Security: $48,000 combined ($28,000 Eleanor + $20,000 Bill)
  - Traditional IRA distributions: $60,000 ($40,000 Eleanor + $20,000 Bill)
  - Taxable interest: $4,500
  - Ordinary dividends: $7,500
  - Q4 Roth conversion (Eleanor's IRA → Roth): $150,000 in November 2025
- **Tax year**: 2025 (filing in 2026)
- **Prior year**: similar income mix without Roth conversion; prior-year tax $14,200, prior AGI $135,000

## Inputs gathered

```
Current-year income summary:
  Taxable SS (85%):        $40,800
  IRA distributions:        $60,000
  Interest:                 $4,500
  Dividends:                $7,500
  Roth conversion (taxable): $150,000
  Total income:             $262,800

Standard deduction (MFJ, both 65+, 2025): $32,000 (verify against current year)
                                          (basic $30,000 MFJ + $1,000 each for age 65)
Taxable income:                          $230,800
Federal income tax (MFJ brackets):       ~$43,800 (rough; depends on capital gains
                                          treatment of dividends and exact brackets)

Withholding:
  IRA distributions: 10% withheld at source = $6,000
  Roth conversion: 24% withheld at source = $36,000
  Social Security: 0% withheld (Eleanor and Bill didn't elect withholding)
  Total withholding: $42,000

Estimated tax payments: $0 (Eleanor was confident the conversion withholding covered everything)

Prior-year tax (Line 22): $14,200
Prior-year AGI: $135,000  → 100% safe harbor multiplier (AGI ≤ $150K)
```

## Step 1 — Run the page 1 flowchart

```
Test 1 — De minimis:
  Unpaid balance = $43,800 − $42,000 = $1,800 > $1,000. Fails.

Test 2 — First-year exception:
  Prior-year tax = $14,200 ≠ $0. Fails.

Test 3 — 90% current:
  Required: $43,800 × 90% = $39,420. Paid: $42,000. PASSES ✓
```

Wait, that's a clean current-year safe harbor pass. Let me re-examine — withholding alone of $42,000 exceeds 90% of current-year tax ($39,420). No penalty.

But also worth checking the prior-year:

```
Test 4 — 100% prior:
  Required: $14,200. Paid: $42,000. PASSES easily ✓
```

**Both safe harbors are met. No penalty. No Form 2210 needed.**

The Roth conversion's 24% mandatory federal withholding ($36,000 on the $150,000 conversion) was the key — it pushed total withholding above both safe harbor thresholds.

## What if Eleanor had elected zero withholding on the Roth conversion?

Suppose Eleanor told the custodian to skip federal withholding on the Roth conversion (some platforms allow this). Then:

```
Withholding:
  IRA distributions: $6,000
  Roth conversion: $0
  Total: $6,000

Test 1 — De minimis: unpaid $43,800 − $6,000 = $37,800 > $1,000. Fails.
Test 3 — 90% current: required $39,420; paid $6,000. Fails.
Test 4 — 100% prior: required $14,200; paid $6,000. Fails.

Penalty owed.
Required annual payment = smaller of $39,420 or $14,200 = $14,200.
```

Now it matters whether the income was uneven enough for Schedule AI to help. The Roth conversion happened in November 2025 (Q4). The other income (SS, IRA distributions, interest, dividends) was relatively even.

```
Income by quarter (cumulative):
  Q1 (through 3/31): $20,000 (SS + IRA dist + small portion of interest/div)
  Q2 (through 5/31): $35,000
  Q3 (through 8/31): $80,000
  Q4 (through 12/31): $262,800 (full year, including Roth conversion)
```

Schedule AI would help significantly here because Q1–Q3 income is modest relative to Q4.

But: the *binding constraint* is the prior-year safe harbor at $14,200, which is the smaller of the two safe harbor amounts. Even with Schedule AI, the per-quarter required installment can't go below the regular method's $14,200 / 4 = $3,550/quarter (because the smaller-of-the-two rule applies per quarter).

Let me walk through the penalty computation under the modified scenario (Eleanor skipped Roth withholding):

```
Required quarterly installments under regular method (using $14,200 required annual):
  Q1: $14,200 × 25% = $3,550
  Q2: $14,200 × 50% = $7,100
  Q3: $14,200 × 75% = $10,650
  Q4: $14,200 × 100% = $14,200

Withholding allocated evenly: $6,000 / 4 = $1,500 per quarter
  (cumulative: $1,500 / $3,000 / $4,500 / $6,000)

Underpayment per quarter:
  Q1: $3,550 − $1,500 = $2,050
  Q2: $7,100 − $3,000 = $4,100  (incremental: $2,050)
  Q3: $10,650 − $4,500 = $6,150  (incremental: $2,050)
  Q4: $14,200 − $6,000 = $8,200  (incremental: $2,050)

Penalty (assume 8%, days from quarter due to next 4/15):
  Q1: $2,050 × 8% × 365/365 = $164
  Q2: +$2,050 × 8% × 304/365 = $137
  Q3: +$2,050 × 8% × 213/365 = $96
  Q4: +$2,050 × 8% × 90/365 = $40
  Total ≈ $437
```

Schedule AI might reduce this because Q1–Q3 cumulative income is well under the prior-year safe harbor figure. But the smaller-of-the-two rule caps Schedule AI per quarter at the regular method's $3,550 / $7,100 / $10,650 / $14,200, and Schedule AI's column-by-column computations using current-year tax may be higher than these caps. Walking through:

- Schedule AI column (a): annualized AGI $80,000, annualized tax (rough) $9,000 — de-annualized $2,250 — × 22.5% = $506
- Schedule AI column (b): annualized AGI $84,000, similar — column installment ~$2,000
- Schedule AI column (c): annualized AGI $120,000, larger — column installment ~$5,000
- Schedule AI column (d): annualized AGI $262,800 (full year) → 90% of $43,800 = $39,420

Per quarter, the smaller of Schedule AI vs. regular:
- Q1: min($506, $3,550) = $506
- Q2: min($2,000, $7,100) = $2,000
- Q3: min($5,000, $10,650) = $5,000
- Q4: min($39,420, $14,200) = $14,200

Underpayments:
- Q1: $506 − $1,500 = max(–$994, 0) = $0 (no underpayment in Q1)
- Q2: $2,000 − $3,000 = max(–$1,000, 0) = $0 (no underpayment in Q2)
- Q3: $5,000 − $4,500 = $500
- Q4: $14,200 − $6,000 = $8,200

Schedule AI penalty:
- Q3: $500 × 8% × 213/365 = $23
- Q4 incremental: $7,700 × 8% × 90/365 = $152
- Total ≈ $175

**Schedule AI saves ~$262** vs. regular method ($437 → $175).

In this modified scenario, Eleanor would file Form 2210 with Schedule AI.

## Returning to the original scenario (Eleanor withheld 24% on Roth conversion)

In the original scenario, withholding alone covered both safe harbors. The flowchart on page 1 resolves to "no penalty, no Form 2210" without needing Schedule AI or even computing penalty.

**This is the most important lesson from this example: withholding at the source on Roth conversions and IRA distributions is the easiest way to lock in the safe harbor.** Many retirees don't realize that custodians offer withholding elections on these distributions; many platforms default to zero or a low percentage. A retiree with a one-time large income event (Roth conversion, RMD that triggers SS taxation jumps, capital gain on a stock sale, sale of a business) should consider directing extra federal withholding at the source.

## The completed Form 2210 draft (original scenario — no penalty)

```markdown
# Form 2210 — DRAFT for tax year 2025

## Filing decision
- [x] No Form 2210 needed (safe harbor met)

## Header
Name(s) shown on return:    Eleanor and Bill Park
Your SSN:                   XXX-XX-XXXX (Eleanor, first-listed)
Filing status:              Married Filing Jointly
Prior-year AGI:             $135,000  → safe-harbor multiplier: 100%

## Page 1 flowchart result

| Test | Required | Paid | Result |
|------|----------|------|--------|
| 1. De minimis ($1,000) | unpaid balance | $1,800 | Fails |
| 2. First-year exception | prior-year tax = $0 | $14,200 ≠ 0 | Fails |
| 3. 90% current safe harbor | $39,420 | $42,000 (W/H only) | **MET** ✓ |

## Result
- No penalty under IRC §6654.
- No Form 2210 needs to be filed.
- Form 1040 Line 38 (Estimated tax penalty) is $0; leave blank or $0 per current-year guidance.

## Validation summary
- Withholding alone ($42,000) exceeds 90% of current-year tax ($39,420).
- The 24% mandatory federal withholding on the Q4 Roth conversion ($36,000) was the
  decisive factor — it brought total withholding from $6,000 (without conversion W/H)
  up to $42,000.
- For 2026 planning: if Eleanor and Bill expect another large income event (Roth conversion, RMD jump, asset sale), continue to use source withholding rather than relying on quarterly estimates.

## Sources cited in this draft
- IRS Form 2210, Rev. 2025
- IRS Instructions for Form 2210, Rev. 2025
- IRC §6654(d)(1)(B)(i) — 90% current-year safe harbor
- IRC §6654(d)(1)(B)(ii) — 100% prior-year safe harbor
- IRC §3405 — Withholding on retirement plan and IRA distributions (mandatory unless waived)
```

## Why each non-obvious choice

**Why does the 24% Roth conversion withholding count toward Form 2210 safe harbor?** All federal income tax withheld during the year — whether from W-2 wages, 1099 distributions, IRA conversions, Social Security, etc. — is treated as "withholding" for IRC §6654 purposes. It allocates evenly across quarters by default under IRC §6654(g)(1), regardless of when the withholding actually occurred.

This is critical for retirees: a single large Roth conversion in Q4 with 24% federal withholding effectively "pre-pays" the tax for the conversion plus extra cushion for the rest of the year's income, all from a single Q4 transaction. This is the clean way to handle a Roth conversion for safe-harbor purposes.

**Why doesn't the timing of the conversion (November) hurt for safe harbor purposes?** Because the withholding allocates evenly across quarters by default. The November $36,000 withholding is treated as $9,000/quarter for safe harbor purposes — even though it actually arrived in IRS coffers in November.

**Why is this NOT the same as making a $36,000 estimated payment in November?** Estimated payments are credited to the quarter when actually paid; they don't allocate evenly. A $36,000 estimated payment on November 15 would credit Q4 only, leaving Q1/Q2/Q3 short of their cumulative required installments. By using *withholding* at the source, Eleanor gets the more favorable even-allocation treatment.

**What about the 110% safe harbor?** Eleanor's prior-year AGI was $135,000, under the $150,000 threshold. So 100% of prior-year tax applies, not 110%. Even if Eleanor's prior-year AGI had been $200,000, the 110% × $14,200 = $15,620 prior-year safe harbor would still be far below the $42,000 actual withholding, so the safe harbor would still be met.

**What if Eleanor had received a notice incorrectly assessing a penalty?** She would respond to the notice by filing Form 2210 retroactively to demonstrate the safe harbor calculation, OR file Form 843 (Claim for Refund and Request for Abatement) if the penalty was already paid.

**What audit defense does Eleanor have?** Form 1099-R from the IRA custodian shows the Roth conversion gross distribution ($150,000) and the 24% withholding ($36,000); Form 1099-R from the IRA distributions also shows the 10% withholding ($6,000); these match Form 1040 Line 25b (1099 federal income tax withheld). Form 5498 confirms the Roth conversion. Total withholding flows to Form 1040 Line 25 totals. The Form 2210 page 1 flowchart confirms safe harbor met. Clean trail.

**Planning recommendation for 2026 Roth conversions**: continue using source withholding at the time of the conversion, ideally at a percentage that covers the marginal tax bracket on the conversion plus a 5-10% buffer. If converting $200,000 in 2026 expecting it to land in the 24% bracket, withhold 28-30% to be safe. The buffer becomes a partial "estimated tax payment" via withholding allocation.
