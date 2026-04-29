# Upstream Forms Decision Tree

Schedule 2 is a router. Every nonzero line corresponds to an upstream form that the filer must compute first and attach to the return. Use this file when triaging a filer's situation: walk through each upstream form with a yes/no question and route to the right Schedule 2 line.

## Decision tree

### Did you exercise ISOs or have AMT preference items in the year?

| Likely answer | Next step |
|---------------|-----------|
| Yes, exercised ISOs and held the shares past year-end | Compute Form 6251. Bargain element = (FMV at exercise − strike) × shares; this is an AMT preference. |
| Yes, large state and local taxes deducted (>$10K) | Compute Form 6251. SALT add-back is the most common AMT trigger after TCJA's $10K SALT cap. |
| No clear AMT preference items | Skip Form 6251 unless your tax software flags AMT. |

→ Result of Form 6251 Line 11 → **Schedule 2 Line 1**.

### Did you receive Form 1095-A from a Health Insurance Marketplace?

| Likely answer | Next step |
|---------------|-----------|
| Yes, received APTC in advance | Compute Form 8962 to reconcile. |
| Yes, claimed marketplace coverage but paid full premium (no APTC) | Compute Form 8962 to claim PTC at filing. |
| No (covered by employer / Medicare / Medicaid / no insurance) | Skip Form 8962 entirely. |

→ If Form 8962 Line 29 > 0 (excess APTC repayment) → **Schedule 2 Line 2**.
→ If Form 8962 Line 26 > 0 (refundable PTC) → **Schedule 3 Line 9** (NOT Schedule 2).

These two outcomes are mutually exclusive — every Form 8962 either generates a repayment OR a credit, never both.

### Did you have self-employment income ≥ $400 net?

| Likely answer | Next step |
|---------------|-----------|
| Yes, Schedule C / F net profit ≥ $400 | Compute Schedule SE. |
| Yes, partnership K-1 with self-employment earnings (Box 14 Code A) ≥ $400 | Compute Schedule SE. |
| Yes, but net was < $400 (or net loss) | No Schedule SE required. |
| No, all W-2 wages | No Schedule SE. |

→ Result of Schedule SE Line 12 → **Schedule 2 Line 4**.

Half of SE tax is also deductible on Schedule 1 Line 15 — handled separately.

### Did you receive tip income that wasn't reported to your employer?

| Trigger | Result |
|---------|--------|
| Cash tips received but not reported on the daily / monthly tip report to employer | Form 4137. Result → **Schedule 2 Line 5**. |
| All tips reported to employer (W-2 Box 7) | Skip. |

### Were you treated as an independent contractor by an employer when you should have been an employee?

| Trigger | Result |
|---------|--------|
| Filer received a 1099-NEC but the work was supervised, scheduled, and controlled by the payer (employee-like) | Form 8919. Result → **Schedule 2 Line 6**. |
| Filer is genuinely self-employed | Skip 8919; SE tax via Schedule SE. |

Form 8919 also flags the misclassification to the IRS for SS-8 follow-up.

### Did you take an early distribution, miss an RMD, or make an excess contribution to a tax-favored account?

| Trigger | Form 5329 part | Result |
|---------|----------------|--------|
| IRA / 401(k) / 403(b) distribution before age 59½ without an exception | Part I (10% under §72(t)) | → Line 8 |
| Excess traditional IRA contribution | Part III (6% under §4973) | → Line 8 |
| Excess Roth IRA contribution | Part IV (6% under §4973) | → Line 8 |
| Excess Coverdell contribution | Part V (6% under §4973) | → Line 8 |
| Excess HSA contribution | Part VII | → Line 8 |
| Excess ABLE contribution | Part VIII | → Line 8 |
| Missed RMD | Part IX (25%, reduced to 10% if corrected timely under SECURE 2.0) | → Line 8 |

→ Result of Form 5329 → **Schedule 2 Line 8**.

### Did you pay a household employee?

| 2025 trigger | Result |
|--------------|--------|
| Cash wages ≥ $2,800 to any one household employee in 2025 (FICA threshold) | Compute Schedule H. |
| Cash wages ≥ $1,000 in any calendar quarter to all household employees combined (FUTA threshold) | Compute Schedule H. |

→ Result of Schedule H Line 8 (or Line 26) → **Schedule 2 Line 9**.

The 2026 FICA threshold is announced ~October 2025 by SSA; verify before filing.

### Did you claim the original 2008 first-time homebuyer credit?

| Trigger | Result |
|---------|--------|
| Yes, claimed credit on 2008 return (refundable up to $7,500) and still owe annual installments | Form 5405 → Line 10 ($500/year for 15 years; most filers' obligation ended 2023) |
| Claimed in 2009 or 2010 (different credit, no repayment unless home sold within 3 years) | Generally no repayment due |

### Did your wages + SE earnings exceed the Additional Medicare Tax threshold?

| Filing status | 2026 threshold (statutory, not indexed) | Action |
|--------------|-----------------------------------------|--------|
| Single / HoH / QSS | $200,000 | If exceeded, Form 8959 |
| MFJ | $250,000 | If exceeded, Form 8959 |
| MFS | $125,000 | If exceeded, Form 8959 |

→ Result of Form 8959 Line 18 → **Schedule 2 Line 11**.

The W-2 employer also withholds 0.9% on wages > $200,000 single (regardless of filing status). Form 8959 reconciles withholding against actual liability — withheld amounts go on Form 8959 Line 24 and flow to Form 1040 Line 25c, not Schedule 2.

### Do you have investment income and MAGI above the NIIT threshold?

| Filing status | 2026 threshold (statutory, not indexed) | Action |
|--------------|-----------------------------------------|--------|
| Single / HoH / QSS | $200,000 | If exceeded AND have net investment income, Form 8960 |
| MFJ | $250,000 | If exceeded AND have net investment income, Form 8960 |
| MFS | $125,000 | If exceeded AND have net investment income, Form 8960 |

Investment income includes interest, dividends, capital gains, rental and royalty (passive), non-qualified annuities, passive business income.

→ Result of Form 8960 Line 17 → **Schedule 2 Line 12**.

### Do you have a Section 965 transition tax obligation?

| Trigger | Result |
|---------|--------|
| Filer made a §965(h) election in 2017 to pay the transition tax in 8 annual installments | Form 965-A. Final installment for most filers was 2025. Verify before populating Lines 13/20. |
| No US shareholder interest in CFC or §965-eligible foreign corp | Skip. |

### Other recapture / additional-tax events?

If the filer mentions any of the following, route to Line 17 sub-item:

| Event | Sub-line | Source |
|-------|----------|--------|
| Non-qualified HSA distribution | 17c (or 17m via Form 8889 Line 17b) | Form 8889 |
| Non-qualified ABLE distribution | 17k | (per current-year instructions) |
| Recapture of education credit, EV credit, residential energy credit | 17a | computation per credit form |
| §72(p) loan from qualified plan deemed distribution | 17i | computation |
| Look-back interest under §167(g) or §460(b) | 17h | computation |
| Recapture of charitable deduction (fractional interest in tangible property) | 17f | computation |

See [`line-17-subitems.md`](./line-17-subitems.md) for the full list.

## Order of operations

Always compute upstream forms before Schedule 2:

1. **Schedule SE** (depends on Schedule C / F / K-1 net SE earnings)
2. **Form 8962** (depends on Form 1095-A and AGI from rest of return)
3. **Form 8959** (depends on W-2 Medicare wages and SE earnings — needs Schedule SE complete)
4. **Form 8960** (depends on AGI from rest of return + investment income from Schedule B/D/E)
5. **Form 5329** (depends on 1099-R distribution data + IRA contribution data)
6. **Form 6251** (depends on full Form 1040 calculation; computed last among AMT-relevant forms)
7. **Schedule H, 4137, 8919, 5405, 8611, 965-A, 8889** as triggered

Schedule 2 is filled *after* all upstream forms because every line is a transcription, not a computation.
