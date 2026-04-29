# Example: S-Corp with Single Shareholder-Employee (Q1 2026)

A complete walkthrough of Form 941 for an S-corp with one shareholder-employee paying themselves $80,000 annual reasonable compensation plus $50,000 in shareholder distributions. This is the canonical "S-corp owner W-2 + K-1" pattern.

## The filer

- **Business name**: Whitney Consulting Inc.
- **EIN**: 88-XXXXXXX
- **Trade name**: Whitney Consulting (also legal name)
- **Entity**: S-corporation (Form 1120-S filer; Form 2553 election effective Jan 1, 2024)
- **Filer**: Owner is sole shareholder, sole employee, sole officer
- **Quarter**: Q1 2026 (January–March)
- **Due date**: April 30, 2026
- **Deposit schedule**: Monthly (lookback period totaled $14,800 < $50,000)

## Reasonable compensation context

The owner provides management consulting services. Industry data (BLS, Glassdoor, RC Reports) suggests the role of "Solo Management Consultant, mid-Atlantic" carries a market wage of $75K–$110K. The owner set $80,000 W-2 wages for the year ($20,000/quarter), with the balance taken as distributions when the corporation has retained earnings.

This is documented in the corporate minute book (resolution dated December 2025 establishing 2026 compensation) — important if the IRS ever challenges under the *Watson, P.C. v. United States* (8th Cir. 2012) and similar reasonable comp cases.

## Inputs gathered (Step 2 of workflow)

### Pay periods in Q1 2026

The S-corp runs **monthly payroll** (the 28th of each month):

- January 28, 2026: $6,667 gross
- February 27, 2026 (28th was Saturday): $6,667 gross
- March 27, 2026 (28th was Saturday): $6,666 gross

Total gross Q1 wages: $20,000

### Pretax deductions (none)

The owner does not run a §125 plan and does not contribute to a 401(k) at the corporate level for Q1 (planning to set up SEP-IRA at year-end via personal contribution).

So:
- Line 2 (FIT wages) = $20,000
- Line 5a col 1 (SS wages) = $20,000
- Line 5c col 1 (Medicare wages) = $20,000

### Federal income tax withholding

Owner submitted Form W-4 with conservative withholding (married filing jointly, $0 from other jobs, $24,000 estimated other deductions). Per the 2026 percentage method, FIT withholding on $6,667/month wage = approximately $580/month. Q1 total Line 3: $1,740.

### Distributions

Separately, the owner took $12,000 in shareholder distributions in Q1 (capital draws for personal expenses). These are **NOT on Form 941** — they appear only on the year-end Schedule K-1 (Form 1120-S) and aren't subject to FICA or FIT withholding. They reduce shareholder basis under IRC §1367.

### Deposits

Monthly deposits via EFTPS:

| Liability month | FIT W/H | Employer SS (6.2%) | Employer Medicare (1.45%) | Employee SS (6.2%) | Employee Medicare (1.45%) | Total deposit | Deposit date |
|----------------|---------|--------------------|--------------------------|--------------------|--------------------------|---------------|--------------|
| January | $580.00 | $413.35 | $96.67 | $413.35 | $96.67 | $1,600.04 | February 17, 2026* |
| February | $580.00 | $413.35 | $96.67 | $413.35 | $96.67 | $1,600.04 | March 16, 2026* |
| March | $580.00 | $413.31 | $96.66 | $413.31 | $96.66 | $1,599.94 | April 15, 2026 |
| **Total** | **$1,740.00** | **$1,240.01** | **$290.00** | **$1,240.01** | **$290.00** | **$4,800.02** | |

*Feb 15 was a Sunday → next banking day Feb 17 (Monday after Presidents' Day). March 15 was a Sunday → March 16 (Monday).

(Roughly: $20,000 × 0.124 = $2,480 total SS, split $1,240 employer + $1,240 employee. $20,000 × 0.029 = $580 total Medicare, split $290 / $290.)

## The completed Form 941 draft

```markdown
# Form 941 — DRAFT for Q1 2026

## Header
Employer name (legal):       Whitney Consulting Inc.
Trade name (if any):         (same)
EIN:                         88-XXXXXXX
Address:                     456 Oak Ln, Bethesda, MD 20814
Quarter:                     [X] 1  [ ] 2  [ ] 3  [ ] 4

## Part 1 — Quarter Taxes

 1. Employees on pay period including March 12:       1
 2. Wages, tips, other compensation:                  $20,000.00
 3. Federal income tax withheld:                      $1,740.00
 4. [ ] Check if line 2 wages not subject to SS/Medicare

 5a. Taxable SS wages:           $20,000.00 × 0.124 = $2,480.00
 5a(i). Sick leave wages:        $0.00 × 0.062 = $0.00
 5a(ii). Family leave wages:     $0.00 × 0.062 = $0.00
 5b. Taxable SS tips:            $0.00 × 0.124 = $0.00
 5c. Taxable Medicare wages:     $20,000.00 × 0.029 = $580.00
 5d. Add'l Medicare wages:       $0.00 × 0.009 = $0.00
 5e. Total (5a–5d col 2):                             $3,060.00
 5f. §3121(q) Notice and Demand:                      $0.00
 6.  Total taxes before adjustments:                  $4,800.00

 7.  Fractions-of-cents adjustment:                   $0.02
 8.  Sick pay third-party adjustment:                 $0.00
 9.  Tips & group-term life adjustment:               $0.00
10.  Total taxes after adjustments:                   $4,800.02

11a. Qualified small business R&D credit (Form 8974): $0.00
11b–f. (Residual COVID credit lines):                 $0.00
11g. Total nonrefundable credits:                     $0.00
12.  Total taxes after credits:                       $4,800.02

13a. Total deposits this quarter:                     $4,800.02
13b–z. (Residual COVID refundable credits):           $0.00
13g. Total:                                           $4,800.02

14.  Balance due:                                     $0.00
15.  Overpayment:                                     $0.00

## Part 2 — Deposit Schedule (Line 16)
[ ] Box 1: Liability < $2,500
[X] Box 2: Monthly depositor
       Month 1 (January):  $1,600.04
       Month 2 (February): $1,600.04
       Month 3 (March):    $1,599.94
       Total = Line 12:    $4,800.02
[ ] Box 3: Semi-weekly depositor

## Part 3 — Business closure / seasonal
17. [ ] Final return
18. [ ] Seasonal employer

## Part 4 — Third-party designee
Name: (none)

## Part 5 — Sign here
Title: President
Phone: 301-555-0107
Date: April 25, 2026
Signature: __________

## Required attachments
- [ ] Schedule B — N/A (monthly depositor)
- [ ] Form 8974 — N/A
- [ ] Form 945-A — N/A

## Validation summary
- Math: all checks passed
  - Line 5a col 2 = 20,000 × 0.124 = 2,480.00 ✓
  - Line 5c col 2 = 20,000 × 0.029 = 580.00 ✓
  - Line 6 = 1,740 + 3,060 = 4,800.00 ✓
  - Line 7 = +0.02 fractions adjustment (per-paycheck rounding accumulated to $0.02 over 3 months)
  - Line 10 = 4,800.02 ✓
  - Line 12 − Line 13g = 0 ✓ (deposits exactly matched liability)
  - Line 16 monthly totals = 1,600.04 + 1,600.04 + 1,599.94 = 4,800.02 ✓
- Sanity:
  - Line 5a col 1 = Line 2 ($20,000): consistent — no pretax deductions
  - Line 5c col 1 = Line 5a col 1 = $20,000: consistent — no SS cap hit
  - Line 5d = $0: no Additional Medicare (YTD comp $20K << $200K threshold)
  - Line 14 = $0: deposits exactly matched liability — clean filing
  - Reasonable compensation reminder: $80K annual W-2 + $50K projected distributions (via $12,500/quarter) — keep documentation of industry comp survey + corporate minute book to defend in audit
- Next steps:
  - File Q2 2026 941 by July 31, 2026 (assuming same wage cadence)
  - At year-end: file Form 940 (FUTA) by January 31, 2027 (S-corp owner-employee subject to FUTA — single-employer, $7,000 wage base, $42 max FUTA per year per employee)
  - File W-2 + W-3 by January 31, 2027 (Box 1 = $80,000; Box 3 SS = $80,000; Box 5 Medicare = $80,000)
  - Form 1120-S (corporate return) for tax year 2026 due March 15, 2027 → reports total wages on Line 8 (Salaries and wages); reasonable comp specifically called out on Line 7 if applicable
  - At Form 1120-S filing: Schedule K-1 to owner shows W-2 wages separately from K-1 distributions

## Sources cited in this draft
- IRS Form 941, Rev. March 2026
- IRS Instructions for Form 941, Rev. March 2026
- IRC §3101 (employee FICA), §3111 (employer FICA), §3402 (FIT withholding)
- IRC §1366, §1367 (S-corp pass-through and basis)
- Rev. Rul. 74-44 (S-corp reasonable compensation principle)
- IRS Fact Sheet 2008-25 (S-corp wage compensation issues)
- Watson, P.C. v. United States, 668 F.3d 1008 (8th Cir. 2012)
- Pub. 15 (Employer's Tax Guide), 2026 edition
```

## Why each non-obvious choice

**Why $80K W-2 wages and $50K distributions?** The owner consulted RC Reports / industry comp surveys; comparable solo management consultants in the mid-Atlantic earn $75K–$110K. Setting reasonable comp below industry comp risks IRS reclassification of distributions as wages (subject to FICA + back interest). $80K is conservative-defensible.

**Why monthly depositor and not Box 1?** Q1 Line 12 = $4,800.02 > $2,500 → not Box 1. Lookback period (Jul 2024–Jun 2025) totaled $14,800 < $50,000 → Box 2 monthly.

**Why are FIT and FICA wages identical ($20,000)?** No pretax deductions in Q1 (no §125 cafeteria, no 401(k) deferrals). When the owner sets up a SEP-IRA at year-end, those employer contributions don't reduce W-2 wages (SEP is employer-funded, not deferral). If the owner had set up a solo 401(k) with elective deferral, that would reduce Line 2 only.

**Why is the fractions-of-cents adjustment $0.02?** Per-paycheck FICA computed in cents accumulates rounding error. Over three monthly paychecks, the difference between (sum-of-rounded-amounts) and (rounded-sum) totals $0.02. Form 941 line 7 absorbs this. Always small, always within ±$1.

**Why doesn't the $12,000 distribution appear anywhere on 941?** Distributions are not wages. The owner's basis decreases by $12,000, the corporation's retained earnings decreases by $12,000, but no payroll mechanic touches it. Reported on Schedule K-1 (Form 1120-S) at year-end, taxed to the owner as part of pass-through ordinary income (or capital gain to the extent of distributions in excess of basis under IRC §1368(b)).

**What if the IRS challenges reasonable comp?** Defense pack:
1. Industry comp survey (RC Reports, BLS, Glassdoor) showing $75K–$110K for the role
2. Corporate minute book resolution setting compensation
3. Documentation of services performed and hours worked
4. Comparison to compensation for non-shareholder employees in similar roles (none here, since solo)

The IRS has won several recent cases (Watson, Sean McAlary, etc.) reclassifying distributions as wages where comp was unreasonably low. $80K is in the lower half of market range — defensible but not bulletproof. If audited and reclassified, additional FICA on say $20K of reclassified comp = ~$3,060, plus interest and possibly accuracy penalty.

**Audit defense for Q1 941:**
1. Payroll register showing the three $6,667 (approx.) paychecks
2. EFTPS deposit confirmations matching the three monthly amounts
3. Form W-4 on file
4. Bank statement showing wage transfers from corporate to personal account
5. Reasonable compensation documentation (separate file)
6. Corporate minute book with 2026 compensation resolution
