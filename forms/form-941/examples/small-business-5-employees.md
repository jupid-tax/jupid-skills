# Example: Small Business with 5 W-2 Employees (Q2 2026, Monthly Depositor)

A complete walkthrough of Form 941 for a service business with five W-2 employees, modest payroll, no tipped wages, and monthly deposit schedule. This is the canonical "small employer Q2 filing" pattern.

## The filer

- **Business name**: Brightside Marketing LLC
- **EIN**: 84-XXXXXXX
- **Trade name**: Brightside (DBA)
- **Entity**: Multi-member LLC, taxed as a partnership (filed Form 1065). The LLC has 5 W-2 employees plus the two members (who take K-1 distributions, no W-2).
- **Filer**: One of the members, signing as Managing Member
- **Quarter**: Q2 2026 (April–June)
- **Due date**: July 31, 2026
- **Deposit schedule**: Monthly (lookback period 2024 Q3 + 2024 Q4 + 2025 Q1 + 2025 Q2 totaled $38,200 < $50,000)

## Inputs gathered (Step 2 of workflow)

### Pay periods in Q2 2026

The company runs semi-monthly payroll: 15th and last day of each month. Six pay dates in Q2:

- April 15, 2026
- April 30, 2026
- May 15, 2026
- May 29, 2026 (May 31 was a Sunday → paid Friday May 29; deposit period mechanics apply)
- June 15, 2026
- June 30, 2026

### Per-employee summary for Q2

| Employee | Role | Q2 Gross | 401(k) deferral | §125 Health | Q2 FIT W/H | Q2 SS Wages | Q2 Medicare Wages |
|----------|------|----------|-----------------|-------------|------------|-------------|--------------------|
| A. Patel | Account Manager | $18,000 | $1,440 | $300 | $2,100 | $17,700 | $17,700 |
| B. Chen | Designer | $15,000 | $750 | $300 | $1,650 | $14,700 | $14,700 |
| C. Reyes | Junior strategist | $12,500 | $0 | $300 | $1,050 | $12,200 | $12,200 |
| D. Okafor | Account Manager | $19,000 | $1,520 | $0 | $2,400 | $19,000 | $19,000 |
| E. Smith | Office admin (PT) | $7,200 | $0 | $0 | $360 | $7,200 | $7,200 |
| **Totals** | | **$71,700** | **$3,710** | **$900** | **$7,560** | **$70,800** | **$70,800** |

Wage logic:
- §125 cafeteria plan deductions reduce **both** FIT wages and FICA wages
- 401(k) deferrals reduce FIT wages only (not FICA)
- Line 2 (FIT wages) = $71,700 − $3,710 (401k) − $900 (§125) = $67,090
- Line 5a/5c col 1 (FICA wages) = $71,700 − $900 (§125) = $70,800

(Verifying per employee: A. Patel Line 2 contribution = $18,000 − $1,440 − $300 = $16,260; sum across all five = $67,090. ✓)

No employee crossed $200K YTD → Line 5d = $0. No tipped wages → Line 5b = $0.

### Deposits made

The company deposited via EFTPS on the 15th of the following month for each prior month's payroll:

| Month liability | Amount | Deposit date |
|----------------|--------|--------------|
| April 2026 | $4,330.40 | May 15, 2026 |
| May 2026 | $4,330.40 | June 15, 2026 |
| June 2026 | $4,330.40 | July 15, 2026 |
| **Total deposits** | **$12,991.20** | |

(Each month total = month FIT W/H + employer FICA + employee FICA. Roughly evenly distributed across three months.)

## The completed Form 941 draft

```markdown
# Form 941 — DRAFT for Q2 2026

## Header
Employer name (legal):       Brightside Marketing LLC
Trade name (if any):         Brightside
EIN:                         84-XXXXXXX
Address:                     123 Main St, Austin, TX 78701
Quarter:                     [ ] 1  [X] 2  [ ] 3  [ ] 4

## Part 1 — Quarter Taxes

 1. Employees on pay period including June 12:        5
 2. Wages, tips, other compensation:                  $67,090.00
 3. Federal income tax withheld:                      $7,560.00
 4. [ ] Check if line 2 wages not subject to SS/Medicare

 5a. Taxable SS wages:           $70,800.00 × 0.124 = $8,779.20
 5a(i). Sick leave wages:        $0.00 × 0.062 = $0.00
 5a(ii). Family leave wages:     $0.00 × 0.062 = $0.00
 5b. Taxable SS tips:            $0.00 × 0.124 = $0.00
 5c. Taxable Medicare wages:     $70,800.00 × 0.029 = $2,053.20
 5d. Add'l Medicare wages:       $0.00 × 0.009 = $0.00
 5e. Total (5a–5d col 2):                             $10,832.40
 5f. §3121(q) Notice and Demand:                      $0.00
 6.  Total taxes before adjustments:                  $18,392.40

 7.  Fractions-of-cents adjustment:                   $0.00
 8.  Sick pay third-party adjustment:                 $0.00
 9.  Tips & group-term life adjustment:               $0.00
10.  Total taxes after adjustments:                   $18,392.40

11a. Qualified small business R&D credit (Form 8974): $0.00
11b–f. (Residual COVID credit lines):                 $0.00
11g. Total nonrefundable credits:                     $0.00
12.  Total taxes after credits:                       $18,392.40

13a. Total deposits this quarter:                     $12,991.20
13b–z. (Residual COVID refundable credits):           $0.00
13g. Total:                                           $12,991.20

14.  Balance due (12 − 13g):                          $5,401.20
15.  Overpayment:                                     —

## Part 2 — Deposit Schedule (Line 16)
[ ] Box 1: Liability < $2,500
[X] Box 2: Monthly depositor
       Month 1 (April): $6,130.80
       Month 2 (May):   $6,130.80
       Month 3 (June):  $6,130.80
       Total = Line 12: $18,392.40
[ ] Box 3: Semi-weekly depositor

## Part 3 — Business closure / seasonal
17. [ ] Final return — last wages paid date: __________
18. [ ] Seasonal employer

## Part 4 — Third-party designee
Name: (none)

## Part 5 — Sign here
Title: Managing Member
Phone: 512-555-0142
Date: July 28, 2026
Signature: __________

## Required attachments
- [ ] Schedule B — N/A (monthly depositor)
- [ ] Form 8974 — N/A
- [ ] Form 945-A — N/A

## Validation summary
- Math: all checks passed
  - Line 5a col 2 = 70,800 × 0.124 = 8,779.20 ✓
  - Line 5c col 2 = 70,800 × 0.029 = 2,053.20 ✓
  - Line 6 = 7,560 + 10,832.40 = 18,392.40 ✓
  - Line 12 − Line 13g = 18,392.40 − 12,991.20 = 5,401.20 ✓
  - Line 16 monthly totals: 3 × $6,130.80 = $18,392.40 ✓ matches Line 12
- Sanity:
  - Line 14 = $5,401.20 — large balance due. Confirm: deposits totaled $12,991.20 but liability was $18,392.40. Why the gap?
    - Possible cause: deposit amounts were rounded down or omitted some withholding
    - Recommend: review June deposit. If June pay was slightly higher than estimated, FTD penalty risk (5% if 6-15 days late, 10% if 16+)
  - All other checks within normal ranges
- Next steps:
  - Pay $5,401.20 balance via EFTPS by July 31, 2026 (or with the return via Form 941-V check)
  - Late deposits penalty (FTD) likely on June liability — consider IRS waiver request if first occurrence
  - File Q3 2026 941 by October 31, 2026
  - File Form 940 (FUTA) annually by January 31, 2027
  - File W-2s for all 5 employees + W-3 transmittal by January 31, 2027 (SSA Business Services Online)

## Sources cited in this draft
- IRS Form 941, Rev. March 2026
- IRS Instructions for Form 941, Rev. March 2026
- IRC §3101 (employee FICA), §3111 (employer FICA), §3402 (FIT withholding)
- Pub. 15 (Employer's Tax Guide), 2026 edition
- SSA Annual Wage Base — $176,100 for 2025; verify 2026 announcement
```

## Why each non-obvious choice

**Why Line 2 ($67,090) ≠ Line 5a col 1 ($70,800)?** Pretax 401(k) deferrals reduce federal income tax wages but not Social Security or Medicare wages. The $3,710 difference is exactly the four employees' aggregate 401(k) contributions for the quarter. §125 health is the same for both ($900), so it cancels.

**Why monthly depositor and not Box 1?** Quarterly Line 12 = $18,392.40 is far above the $2,500 de minimis. Lookback period was $38,200 < $50,000 → monthly. If lookback had exceeded $50K, Box 3 (semi-weekly) would apply with Schedule B attached.

**Why is Line 5d = $0?** No employee earned more than $200,000 YTD at this employer. Highest earner (D. Okafor) is at $19K × 4 quarters = ~$76K annualized → nowhere near the threshold.

**Why is the Q2 deposit total under-estimated?** The bookkeeper used Q1's per-month deposit amount ($4,330.40 average) without recomputing for Q2. Q2 actually had slightly different overtime / bonus mix. This produces a $5,401.20 under-deposit. Recommendation: compute deposit from each pay period's actual liability, not prior-quarter average.

**What happens at year-end?** Sum of four quarters' Line 2 should equal sum of W-2 Box 1 wages. Sum of four quarters' Line 3 should equal sum of W-2 Box 2 wages. Q2's $67,090 + other quarters → annual Box 1. The IRS automatically reconciles via SSA wage matching; mismatches generate CP207 / CP207L within ~12 months.

**Audit defense for Q2 941:**
1. Payroll register from QuickBooks Payroll showing per-paycheck wages and withholding
2. EFTPS deposit confirmations (PDF) matching dates and amounts
3. Form W-4s on file for each employee (substantiates Line 3 logic)
4. §125 plan documents (substantiates Line 2 reduction)
5. 401(k) plan documents (substantiates Line 2 reduction)
6. State withholding return cross-references (CA / TX have no income tax → no state withholding here)
