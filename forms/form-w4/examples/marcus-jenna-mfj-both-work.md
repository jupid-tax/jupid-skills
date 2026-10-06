# Example — Marcus & Jenna, MFJ, Both Work

The classic two-earner MFJ trap. Without Step 2, the household under-withholds by thousands.

All numbers use the 2026 Form W-4 (page 5 MFJ table), Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method schedules, and the 2026 rate schedule and standard deduction from Rev. Proc. 2025-32. Math checked in python.

## Background

- Marcus Chen, age 34, software engineer
  - Salary: $95,000/year
  - Biweekly pay (26 checks/year)
- Jenna Chen, age 33, registered nurse
  - Salary: $68,000/year
  - Biweekly pay (26 checks/year)
- Married, filing MFJ; both have SSNs valid for employment
- No children
- No other income, no self-employment income
- Standard deduction; no Deductions Worksheet items (no tips, overtime, car loan interest, student loan interest, IRA, charity)
- Prior-year return: balance due of $3,200 plus a small penalty (each W-4 was filed as if it were the only job)
- Updating W-4s on January 9, 2026, so the worksheet's full-year amounts apply

## The Problem

If Marcus and Jenna each submit a W-4 with only Steps 1 and 5 (filing status MFJ, nothing else), each employer's payroll treats that salary as the household's only wages and applies the full MFJ amounts to each job.

- Marcus's employer: $95,000 − $12,900 (Worksheet 1A line 1g) = $82,100 → $2,480 + 12% × ($82,100 − $44,100) = **$7,040/year**
- Jenna's employer: $68,000 − $12,900 = $55,100 → $2,480 + 12% × ($55,100 − $44,100) = **$3,800/year**
- Total withheld: **$10,840**

Projected 2026 federal tax on $163,000 of wages (MFJ):
- Taxable income: $163,000 − $32,200 standard deduction = $130,800
- Tax: $11,600 + 22% × ($130,800 − $100,800) = **$18,200**

Under-withholding: $18,200 − $10,840 = **$7,360 shortfall** for 2026 if nothing changes.

## Agent Conversation Flow

**Agent:** Marcus and Jenna, what was your tax situation last year?

**Marcus:** We owed $3,200 plus a small penalty.

**Agent:** That fits two W-4s each written as if it were the only job. We'll fix that with Step 2. Three options:

(a) IRS Tax Withholding Estimator (www.irs.gov/W4App) — the form calls it the most accurate
(b) Multiple Jobs Worksheet (page 3 of the W-4, tables on page 5) — no internet needed; result goes in Step 4(c) of Marcus's W-4
(c) Step 2(c) checkbox on both W-4s — only for exactly two jobs

The form's rule for choosing between (b) and (c): (c) "is generally more accurate than Step 2(b) if pay at the lower paying job is more than half of the pay at the higher paying job." Jenna's $68,000 is more than half of Marcus's $95,000 ($47,500), so (c) should beat (b) for you. Which do you want?

**Marcus:** We'd rather not do the online tool. Show us (b) and (c) side by side.

**Agent:**

| | (b) Worksheet | (c) Checkbox on both |
|---|---|---|
| Lookup / schedule | MFJ table, row "$80,000 - 99,999", column "$60,000 - 69,999" = $7,610 | Pub. 15-T "Form W-4, Step 2, Checkbox" MFJ schedule, no line 1g subtraction |
| Marcus withholding | $7,040 + $293 × 26 = $14,658 | $5,800 + 22% × ($95,000 − $66,500) = $12,070 ($464.23/check) |
| Jenna withholding | $3,800 | $5,800 + 22% × ($68,000 − $66,500) = $6,130 ($235.77/check) |
| Household total | $18,458 | $18,200 |
| vs projected tax $18,200 | $258 over | $0 |

**Jenna:** The checkbox, then.

## Marcus's W-4 Draft (higher-paying job)

```markdown
# Form W-4 — Marcus Chen — DRAFT for tax year 2026

## Step 1
1(a) Marcus Chen, 1547 Oak Avenue, Seattle WA 98103
1(b) SSN: XXX-XX-5678
1(c) ☑ Married Filing Jointly or Qualifying Surviving Spouse

## Step 2 — Multiple Jobs
Method: (c) Step 2(c) checkbox
Step 2(c) box: ☑ Checked (Jenna's W-4 checks it too)

## Step 3 — Dependents
$0 — no children, no other dependents

## Step 4 — Other Adjustments
4(a) Other income: $0
4(b) Deductions: $0 (Deductions Worksheet line 15 = $0: lines 1a–7 $0; 8a $163,000; 8b $163,000; 9 $768,700; 10 $0; 11 $32,200; 12 $0; 13 $32,200; 14 $0)
4(c) Extra withholding: $0

## Exempt from withholding: ☐ not claimed

## Step 5
Signed: Marcus Chen
Date: 2026-01-09

## Pay frequency: biweekly (26)

## Estimated annual federal income tax withheld:
- Pub. 15-T checkbox schedule, MFJ: $5,800 + 22% × ($95,000 − $66,500) = $12,070
- Per check: $464.23

## Validation summary
- Math: $12,070 ÷ 26 = $464.23 ✓
- Sanity: Step 3 = $0 (no dependents) ✓; 2(c) appropriate (two jobs; $68,000 > ½ × $95,000) ✓
- Coordination: Steps 3–4(b) are blank on both W-4s, so the one-W-4 rule is met; Step 2(c) checked on both ✓
```

## Jenna's W-4 Draft (lower-paying job)

```markdown
# Form W-4 — Jenna Chen — DRAFT for tax year 2026

## Step 1
1(a) Jenna Chen, 1547 Oak Avenue, Seattle WA 98103
1(b) SSN: XXX-XX-9012
1(c) ☑ Married Filing Jointly or Qualifying Surviving Spouse

## Step 2 — Multiple Jobs
Method: (c) Step 2(c) checkbox
Step 2(c) box: ☑ Checked (must match Marcus's W-4)

## Step 3 — Dependents
$0 — no dependents (if they had any, only one of the two W-4s would carry them)

## Step 4
4(a) $0
4(b) $0
4(c) $0

## Exempt from withholding: ☐ not claimed

## Step 5
Signed: Jenna Chen
Date: 2026-01-09

## Estimated annual federal income tax withheld: $6,130 ($235.77 per check; Pub. 15-T checkbox schedule, MFJ)
```

## Combined Result

- Marcus withholding: $12,070
- Jenna withholding: $6,130
- **Combined: $18,200 vs projected 2026 tax $18,200**

Both salaries sit in the 22% band of the halved MFJ schedule, so the checkbox reproduces the joint tax exactly here. With a wider pay gap it over-withholds (form text: "the greater the difference in pay is between the two jobs").

## Alternative Kept on File: Step 2(b)

If one of them changes jobs and the pay gap widens past the half-pay test, switch to the worksheet:

- Marcus's W-4: Step 2(c) unchecked; Step 4(c) = $7,610 ÷ 26 = $292.69 → **$293** per check
- Jenna's W-4: Step 2(c) unchecked; Steps 3–4 blank
- Projected withholding: $14,658 + $3,800 = $18,458 ($258 over the $18,200 projection, because the table uses $10,000 bands)

## Key Takeaways

- Two-earner MFJ households under-withhold without Step 2 ($7,360 here)
- The form's half-pay rule decides between (b) and (c); compute both when the user won't use the Estimator
- Step 2(c) must be checked on both W-4s or on neither
- Steps 3 through 4(b) go on only one W-4
- Recheck with the Estimator early each year, and submit new W-4s if either salary changes
