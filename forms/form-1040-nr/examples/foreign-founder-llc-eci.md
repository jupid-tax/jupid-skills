# Example: Foreign Founder With a U.S. Single-Member LLC (ECI, Schedule A, QBI Limit, Treaty Dividends)

A married German resident who owns a Delaware single-member LLC with a Chicago showroom and one U.S. employee. Shows the trade-or-business decision, Schedule C income flowing to page 1, Schedule A (Form 1040-NR), the QBI income limitation, married-filing-separately rates, 15% treaty dividends on Schedule NEC, no self-employment tax under a certificate of coverage, and the Form 5472 handoff. Tax year 2025, filed in 2026. All amounts were checked with a Python script (Tax Table MFS row 84,900–84,950 = $13,598 verified against the 2025 Tax Table).

## The filer

- **Name**: Tobias Brandt; married to Katrin Brandt (German resident, no U.S. income, not a U.S. citizen or resident)
- **Citizenship / tax residence**: Germany / Germany
- **U.S. entity**: Brandt Optics LLC, Delaware, single-member, no Form 8832 or 2553 (disregarded); showroom leased in Chicago, one full-time U.S. employee, sells eyewear frames to U.S. customers
- **Identifying number**: ITIN (issued 2023)
- **Visa**: B-1/B-2 visa valid on December 31, 2025; never applied for a green card
- **Prior returns**: 2024 Form 1040-NR filed on time

## Inputs gathered

| Item | Amount | Source |
|---|---|---|
| Schedule C line 31 net profit (ECI only), prepared with [`../../schedule-c/SKILL.md`](../../schedule-c/SKILL.md) | $112,486 | Gross receipts $268,940 − COGS $97,310 − wages $41,600 − rent $14,400 − other $3,144 |
| Illinois income tax paid in 2025 (2025 estimates $4,980 + balance on 2024 return paid April 2025 $612) | $5,592 | Bank records |
| Gift to a U.S. 501(c)(3) food bank by card (written acknowledgment held) | $750 | Receipt |
| Dividends from U.S. stocks, personal brokerage account with Form W-8BEN (Form 1042-S income code 06, rate 15%) | $3,180 | Form 1042-S |
| Form 1042-S box 10 tax withheld | $477 | Form 1042-S |
| Interest on a personal U.S. savings account | $211 | Bank statement |
| Gain on sale of U.S. stock, personal brokerage account | $2,640 | Broker statement |
| 2025 Form 1040-ES (NR) payments: 06/12/25 $6,400; 09/12/25 $3,200; 01/14/26 $3,200 | $12,800 | EFTPS confirmations |
| Certificate of coverage under the U.S.–Germany social security agreement showing German coverage | on file | Deutsche Rentenversicherung |

Days present in 2025 (item G): 02/09–02/22, 04/27–05/15, 07/06–07/18, 09/14–09/28, 11/30–12/12 = 14 + 19 + 13 + 15 + 13 = **74**. 2024: 88. 2023: 61.

## Step 2 — Residency

- Green card test: no.
- Substantial presence: 74 + 88/3 + 61/6 = 74 + 29.33 + 10.17 = **113.5** < 183 → not met (31-day test passed).
- No dual-status facts. **Nonresident alien for all of 2025.**

## Step 3 — Filing requirement and due date

Engaged in a U.S. trade or business (U.S. office and employee) → must file (Table A item 1). He is the employer, not an employee receiving wages subject to withholding → due **June 15, 2026**. 16-month deadline for deductions: **October 15, 2027**.

## Step 4 — Classification

| Item | Bucket | Line |
|---|---|---|
| LLC profit $112,486 | ECI (disregarded LLC with a U.S. fixed place of business and employee) | Schedule C → Schedule 1 line 3 → 1040-NR line 8 |
| Dividends $3,180 | Not ECI (personal portfolio, not held for the business) | Schedule NEC line 1a, column (b) 15% |
| Savings interest $211 | Exempt U.S. bank deposit interest | Not reported |
| Stock gain $2,640 | Not ECI; present fewer than 183 days | Not taxable; Schedule NEC lines 16–18 left blank |

Agent questions asked: "Is the brokerage account owned by you personally or by the LLC, and is it used for the business?" (personally; not used). "Which country's social security system covers your self-employment?" (Germany; certificate of coverage provided).

## Step 5 — Treaty

U.S.–Germany treaty: dividends paid by U.S. corporations, general rate 15% (IRS Tax Treaty Table 1, Rev. May 2023; treaty Article 10(2)). The broker already withheld 15%. Form 8833: waived (treaty reduces the rate on FDAP income received by an individual, Treas. Reg. §301.6114-1(c)). He does not claim the business profits are outside a permanent establishment, so no Form 8833 for the ECI. Schedule OI item L: none (nothing is exempt; the dividends are taxed at a reduced rate).

## Step 6–8 — Deductions, QBI, tax

**Schedule A (Form 1040-NR)**: 1a $5,592 (Illinois tax on ECI); 1b min($5,592, $20,000 MFS cap) = $5,592 (line 11b far below $250,000 MFS); 2 $750; 5 $750; **8 $6,342** → line 12.

**Form 8995** (taxable income before QBI $106,144 ≤ $197,300):

| Line | Computation | Amount |
|---|---|---|
| 1i(c) | Brandt Optics LLC QBI (no SE tax deduction, health insurance, or retirement adjustments) | $112,486 |
| 2, 4 | Total QBI | $112,486 |
| 5 | 20% × 112,486 | $22,497 |
| 10 | QBI deduction before income limitation | $22,497 |
| 11 | Taxable income before QBI: 112,486 − 6,342 | $106,144 |
| 12 | Net capital gain + qualified dividends on page 1 | $0 |
| 13 | 106,144 − 0 | $106,144 |
| 14 | 20% × 106,144 | $21,229 |
| 15 | Smaller of 10 or 14 → line 13a | **$21,229** |

**Line 16**: married nonresident → MFS column. Taxable income $84,915 → Tax Table row 84,900–84,950, MFS → **$13,598**.

**Schedule NEC**: line 1a column (b) $3,180; line 13(b) $3,180; line 14(b) 15% = $477; **line 15 $477** → line 23a.

**Line 23b**: $0. The certificate of coverage places his self-employment under the German system (Instructions for Schedule 2, line 4: SE tax only when a totalization agreement covers the filer under U.S. social security).

**Line 38**: payments 06/12/25 $6,400, 09/12/25 $3,200, 01/14/26 $3,200 meet the Form 1040-ES (NR) schedule for filers without wages (1/2, 1/4, 1/4) measured against 90% of the 2025 tax ($14,075 × 90% = $12,667.50; required $6,333.75, $3,166.88, $3,166.88). No penalty; confirm with [`../../form-2210/SKILL.md`](../../form-2210/SKILL.md).

## The completed draft

```markdown
# Form 1040-NR — DRAFT for tax year 2025 (filed in 2026)

## Residency determination
- Green card test: No
- Substantial presence: 74 + 88/3 + 61/6 = 113.5 (31-day test: pass) → not met
- Conclusion: Nonresident alien for all of 2025
- Due date: June 15, 2026 (no wages as an employee); 16-month deadline: October 15, 2027

## Header
Name: Tobias Brandt     Identifying number: ITIN 9XX-XX-XXXX
Filing status: Married filing separately   Special boxes: none   Digital assets: No
Dependents: none (resident of Germany: not eligible)

## Page 1 — Effectively connected income
1a–1h. $0 each      1i, 1j. Reserved      1k. $0      1z. $0
2a. $0    2b. $0 (savings interest exempt, not reported)
3a. $0    3b. $0 (portfolio dividends are on Schedule NEC)
4a/4b. $0 / $0    5a/5b. $0 / $0    6. Reserved
7a. Capital gain or (loss):                   $0 (stock gain not ECI; under 183 days)
8.  Schedule 1, line 10 (line 3 business income): $112,486
9.  Total effectively connected income:       $112,486
10. Adjustments:                              $0
11a. AGI:                                     $112,486

## Page 2 — Tax and payments
11b. AGI:                                     $112,486
12.  Itemized deductions (Schedule A NR):     $6,342
13a. QBI deduction (Form 8995):               $21,229
13b. —            13c. Schedule 1-A:          $0
14.  Add 12–13c:                              $27,571
15.  Taxable income:                          $84,915
16.  Tax (Tax Table, MFS column):             $13,598
17.  $0     18. $13,598     19. $0     20. $0     21. $0
22.  Line 18 − line 21:                       $13,598
23a. Schedule NEC tax:                        $477
23b. Schedule 2, line 21 (no SE tax):         $0
23c. $0     23d. $477
24.  Total tax:                               $14,075
25a–25c. $0     25d. $0     25e. $0     25f. $0
25g. Form 1042-S withholding:                 $477
26.  2025 estimated tax payments:             $12,800
27.  Reserved   28. $0   29. $0   30. $0   31. $0   32. $0
33.  Total payments:                          $13,277
34.  Overpaid: $0    35a. $0    36. $0
37.  Amount you owe (by June 15, 2026):       $798
38.  Estimated tax penalty:                   $0

## Schedule NEC
| Line | Item | (a) 10% | (b) 15% | (c) 30% | (d) __% |
| 1a | Dividends paid by U.S. corporations | | $3,180 | | |
| 13 | Totals | $0 | $3,180 | $0 | $0 |
| 14 | Tax | $0 | $477 | $0 | $0 |
15. Total → line 23a: $477
16–18: not taxable — present 74 days (< 183)

## Schedule A (Form 1040-NR)
1a. $5,592   1b. $5,592   2. $750   3. $0   4. $0   5. $750   6. $0   7. $0   8. $6,342

## Schedule OI
A. Germany   B. Germany   C. No   D1. No   D2. No   E. B-1   F. No
G. 02/09/25–02/22/25; 04/27/25–05/15/25; 07/06/25–07/18/25; 09/14/25–09/28/25; 11/30/25–12/12/25
H. 2023: 61   2024: 88   2025: 74
I. Yes — 2024, Form 1040-NR   J. No   K. No   L. none   M. none

## Schedule P
Not applicable: no partnership interest transferred.

## Attachments and companion filings
- [x] Form 1042-S (front); Schedule 1; Schedule C; Form 8995; Schedule A (Form 1040-NR); Schedule NEC; Schedule OI
- [ ] Separate: Brandt Optics LLC pro forma Form 1120 + Form 5472 → ../../form-5472/SKILL.md
- [ ] Separate: the LLC's employer returns for the U.S. employee → ../../form-941/SKILL.md, ../../form-940/SKILL.md
- [ ] Separate: Illinois nonresident individual return (state boundary)
- [ ] 2026 Form 1040-ES (NR): 1/2 by June 15, 2026; 1/4 by September 15, 2026; 1/4 by January 15, 2027

## Validation summary
- Math: all checks passed (9 = 8; 14 = 12 + 13a; 15 = 11b − 14; 24 = 22 + 23d;
  33 = 25g + 26; 37 = 24 − 33; NEC 14(b) = 13(b) × 15%; Schedule A 8 = 1b + 5)
- Classification: LLC profit ECI; dividends NEC at treaty rate; interest and stock gain exempt
- Sanity: MFS column used (married); no standard deduction; no SE tax backed by certificate of coverage;
  QBI limited by the income limitation (line 14 < line 10)

## Sources cited in this draft
- 2025 Form 1040-NR, Schedules NEC, A (Form 1040-NR), OI; Instructions for Form 1040-NR (2025)
- 2025 Instructions for Form 1040 (Tax Table); 2025 Form 8995 and instructions
- Pub. 519 (2025) ch. 4 (trade or business, ECI) and ch. 7 (foreign-owned disregarded entities)
- IRS Tax Treaty Table 1 (Rev. May 2023); Treas. Reg. §301.6114-1(c)
- Form 1040-ES (NR) (2026) payment schedule; IRC §§871, 6072(c); Treas. Reg. §1.874-1(b)
```

## Why each non-obvious choice

**Why is the LLC's profit on his Form 1040-NR?** A single-member LLC that has not elected corporate status is disregarded, so the profit is his. The Chicago showroom and employee make the activity a U.S. trade or business, so the profit is ECI (Pub. 519 ch. 4). Without a U.S. office, employees, or dependent agents, the agent would have asked more questions before treating sales to U.S. customers as ECI.

**Why married filing separately?** He is married and his spouse is a nonresident; Form 1040-NR has no joint status, and the "Single" exception covers only residents of Canada, Mexico, South Korea, U.S. nationals, and India Art. 21(2) students. The resident election isn't available because Katrin is not a U.S. citizen or resident.

**Why is the QBI deduction $21,229 and not $22,497?** Form 8995 limits the deduction to 20% of taxable income before QBI (line 14). His itemized deductions pull taxable income below QBI.

**Why no tax on the $2,640 stock gain?** Non-ECI capital gains are taxed only when the nonresident is present 183 days or more in the year (IRC §871(a)(2)); he was present 74.

**Why no self-employment tax?** Nonresidents owe it only when a totalization agreement puts them in the U.S. system. His certificate of coverage says Germany. Without that certificate the agent would have stopped and asked.

**Why June 15?** He had no wages as an employee subject to U.S. withholding (IRC §6072(c)).

**Filing channel:** ITIN issued in 2023, no W-7, not dual-status → e-file through software that supports Form 1040-NR or a paid preparer ([`../filing.md`](../filing.md)).
