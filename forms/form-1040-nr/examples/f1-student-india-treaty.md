# Example: F-1 Student From India (Article 21(2) Standard Deduction, Form 8843, Refund)

A graduate student with on-campus wages. Shows the exempt-individual day exclusion, the one treaty case that allows a standard deduction on Form 1040-NR, and a refund of over-withheld federal income tax. Tax year 2025, filed in 2026. All amounts were checked with a Python script (Tax Table midpoint method verified against the 2025 Tax Table row 2,475–2,500 = $249).

## The filer

- **Name**: Meera Iyer (single)
- **Citizenship / tax residence**: India / India (resident of India immediately before arriving)
- **Status**: F-1 student, master's program at a public university in Ohio; first entered the U.S. on August 14, 2023
- **Visa history**: no U.S. presence 2019–2022; F-1 in 2023, 2024, 2025; never a J or Q teacher or trainee; no green card application
- **Identifying number**: SSN (issued for on-campus employment)
- **Prior returns**: 2024 Form 1040-NR with Form 8843; 2023 Form 8843 only

## Inputs gathered

| Document | Amount |
|---|---|
| Form W-2 (university), box 1 wages | $18,240 |
| Form W-2 box 2 federal income tax withheld | $1,032 |
| Form W-2 boxes 3–6 (social security and Medicare) | $0 |
| Form W-2 box 17 Ohio income tax withheld | $412 |
| U.S. bank savings interest (Form 1099-INT) | $37 |

Days present (Schedule OI item G/H): in the U.S. on January 1, 2025; departed May 16, 2025; entered June 12, 2025; departed December 17, 2025. 2025: 136 + 189 = **325** days. 2024: 338 days. 2023: 140 days (August 14–December 31).

## Step 2 — Residency

- Green card test: no.
- Substantial presence before exclusions: 325 + 338/3 + 140/6 = 325 + 112.67 + 23.33 = **461** → would be a resident.
- Exempt individual: F-1 student substantially complying with the visa, exempt in 2023, 2024, and 2025 (3 calendar years, not more than 5). All days are excluded with Form 8843 Part III. Counted days: 0.
- Result: **Nonresident alien for all of 2025.** No dual-status facts.

Agent questions asked and answered: "Which visa did you hold each year from 2019 to 2025?" (none 2019–2022, F-1 since 2023). "Did you take any step toward a green card in 2025?" (no; Form 8843 line 13 = No).

## Step 3 — Filing requirement and due date

- Exception 1 (F/J/M/Q with no taxable income) does not apply: she had wages.
- Exception 2 (India Art. 21(2), single, gross income ≤ $15,750) does not apply: gross income $18,240.
- She must file. Wages subject to withholding → due **April 15, 2026**. 16-month deadline for deductions: August 15, 2027 (not at risk).

## Step 4 — Classification

| Item | Bucket | Reason |
|---|---|---|
| $18,240 wages | ECI, line 1a | Personal services performed in the U.S. |
| $37 bank interest | Exempt, not reported | U.S. bank deposit interest is exempt under §871(i) and not ECI (line 2b exception 3) |

## Step 5 — Treaty

Article 21(2) of the U.S.–India treaty: she confirmed residence in India immediately before arriving and student status. Benefit used: standard deduction on line 12 (Pub. 519 ch. 5, Worksheet 5-1). Nothing is treaty-exempt income, so Schedule OI item L is empty and line 1k is $0. Form 8833: the position concerns income of a student, which is in the reporting waiver list (Treas. Reg. §301.6114-1(c); Instructions for Form 1040-NR, item L exceptions); recorded as waived, CPA may confirm.

Worksheet 5-1: line 1 $15,750 (single); line 2 not a dependent → line 4 $15,750; line 5 $0 (under 65, not blind); line 6 $0; **line 7 $15,750**.

She cannot also itemize the $412 of Ohio tax. Because she takes the standard deduction, any 2025 Ohio refund she receives in 2026 is not taxable on her 2026 return (Schedule 1 line 1, exception 2 in the 1040-NR instructions).

FICA check: W-2 boxes 4 and 6 are $0, consistent with Pub. 519 chapter 8 for a nonresident F-1 student. Had they been withheld, the fix would be Form 843 ([`../../form-843/SKILL.md`](../../form-843/SKILL.md)), not this return.

## The completed draft

```markdown
# Form 1040-NR — DRAFT for tax year 2025 (filed in 2026)

## Residency determination
- Green card test: No
- Substantial presence: 325 + 338/3 + 140/6 = 461 before exclusions; all days excluded as an
  exempt F-1 student (Form 8843 Part III) → counted days 0
- Conclusion: Nonresident alien for all of 2025
- Due date: April 15, 2026 (wages subject to withholding); 16-month deadline: August 15, 2027

## Header
Name: Meera Iyer        Identifying number: SSN XXX-XX-XXXX
Filing status: Single   Special boxes: none   Digital assets: No
Dependents: none

## Page 1 — Effectively connected income
1a.  W-2 box 1 wages:                         $18,240
1b–1h.                                        $0 each
1i, 1j. Reserved
1k.  Treaty-exempt income:                    $0
1z.  Add 1a–1h:                               $18,240
2a.  Tax-exempt interest:                     $0
2b.  Taxable interest:                        $0   (bank interest exempt, not reported)
3a.  Qualified dividends:                     $0
3b.  Ordinary dividends:                      $0
4a/4b. IRA distributions:                     $0 / $0
5a/5b. Pensions and annuities:                $0 / $0
6.   Reserved
7a.  Capital gain or (loss):                  $0
8.   Schedule 1, line 10:                     $0
9.   Total effectively connected income:      $18,240
10.  Adjustments (Schedule 1, line 26):       $0
11a. Adjusted gross income:                   $18,240

## Page 2 — Tax and payments
11b. AGI:                                     $18,240
12.  Standard deduction (U.S.–India Art. 21(2)): $15,750
     "Standard Deduction Allowed Under U.S.-India Income Tax Treaty"
13a. QBI deduction:                           $0
13b. Estates and trusts only:                 —
13c. Schedule 1-A, line 38:                   $0
14.  Add 12–13c:                              $15,750
15.  Taxable income:                          $2,490
16.  Tax (Tax Table, row 2,475–2,500, Single): $249
17.  Schedule 2, line 3:                      $0
18.  Add 16 and 17:                           $249
19.  CTC / ODC:                               $0
20.  Schedule 3, line 8:                      $0
21.  Add 19 and 20:                           $0
22.  Line 18 − line 21:                       $249
23a. Schedule NEC tax:                        $0
23b. Schedule 2, line 21:                     $0
23c. Transportation tax:                      $0
23d. Add 23a–23c:                             $0
24.  Total tax:                               $249
25a. Withheld, Form W-2:                      $1,032
25b. Withheld, Form 1099:                     $0
25c. Other forms:                             $0
25d. Add 25a–25c:                             $1,032
25e. Form 8805:                               $0
25f. Form 8288-A:                             $0
25g. Form 1042-S:                             $0
26.  2025 estimated payments:                 $0
27.  Reserved
28.  ACTC:                                    $0
29.  Form 1040-C:                             $0
30.  Refundable adoption credit:              $0
31.  Schedule 3, line 15:                     $0
32.  Add 28–31:                               $0
33.  Total payments:                          $1,032
34.  Overpaid:                                $783
35a. Refund:                                  $783 (direct deposit, U.S. checking account)
36.  Applied to 2026 estimated tax:           $0
37.  Amount you owe:                          $0
38.  Estimated tax penalty:                   $0

## Schedule NEC
Not filed: no U.S.-source income outside page 1.

## Schedule A (Form 1040-NR)
Not filed: standard deduction under U.S.–India treaty Art. 21(2).

## Schedule OI
A. India   B. India   C. No   D1. No   D2. No   E. F-1   F. No
G. 01/01/25 entered; 05/16/25 departed; 06/12/25 entered; 12/17/25 departed
H. 2023: 140   2024: 338   2025: 325
I. Yes — 2024, Form 1040-NR   J. No   K. No   L. none (line 1k $0)   M. none

## Attachments and companion filings
- [x] Form W-2 (front of return)
- [x] Form 8843 (2025): line 1a "Information provided on Form 1040-NR"; line 4b 325; Part III lines 9–14
      (line 12 No; line 13 No)
- [ ] Ohio and local returns: state boundary, outside this skill

## Validation summary
- Math: all checks passed (1z = 1a; 9 = 1z; 11a = 9 − 10; 14 = 12; 15 = 11b − 14;
  24 = 22 + 23d; 33 = 25d; 34 = 33 − 24)
- Classification: wages ECI; bank interest exempt
- Sanity: standard deduction supported by Art. 21(2) eligibility; Single status (unmarried);
  no credits claimed

## Sources cited in this draft
- 2025 Form 1040-NR, Schedule OI; Instructions for Form 1040-NR (2025): Filing Requirements,
  Substantial Presence Test, line 2b exception 3, line 12
- 2025 Instructions for Form 1040, Tax Table
- Pub. 519 (2025) ch. 1 (exempt individuals), ch. 5 (Worksheet 5-1), ch. 8 (FICA for students)
- Form 8843 (2025) and instructions; Treas. Reg. §301.6114-1(c)
```

## Why each non-obvious choice

**Why Form 1040-NR when her raw day count is 461?** Days as an exempt F-1 student don't count for the substantial presence test (IRC §7701(b)(5)), but only with Form 8843. Without it, she would be a resident filing Form 1040.

**Why the standard deduction?** Nonresidents normally get none. Article 21(2) of the U.S.–India treaty is the single exception the Instructions for Form 1040-NR name for line 12. A Chinese or Brazilian student with the same wages would itemize (or enter $0) and owe tax on $18,240.

**Why isn't the $37 of bank interest on line 2b?** Interest on a U.S. bank deposit that is not connected with a U.S. business is exempt from the 30% tax and is excluded from line 2b by the instructions.

**Why April 15 and not June 15?** She received wages as an employee subject to U.S. income tax withholding.

**Filing channel:** she has an SSN and a single-status nonresident return with no W-7, so commercial software that supports Form 1040-NR can e-file it ([`../filing.md`](../filing.md)).
