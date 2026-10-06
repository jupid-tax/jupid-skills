# Example: Calendar-Year C Corporation With a Balance Due (Form 1120, code 12)

A C corporation that owes income tax, has made estimated payments, and needs six more months to finish its return. The hard parts are line 6 and the 90% relief rule.

## The filer

- **Entity**: Kestrel Fieldworks Inc., a Delaware corporation, principal office in Austin, Texas
- **Return**: Form 1120 for calendar year 2026
- **EIN**: 8X-XXXXXXX (placeholder; the agent uses the real EIN at filing time)
- **Name on the 2025 Form 1120**: Kestrel Fieldworks Inc. (no change)
- **Total assets at the end of 2026**: about $6.3 million (only matters for the paper address in Kansas City states; Texas is not one)
- **Filing channel**: e-file through the corporation's tax software, with Electronic Funds Withdrawal
- **Date of drafting**: March 22, 2027

## Inputs gathered

| Input | Value | Source the user gave |
|---|---|---|
| Projected 2026 taxable income | $287,450 | Controller's year-end close draft |
| Nonrefundable credits | $8,912 research credit (Form 6765 via Form 3800) | Preparer's estimate |
| Other Schedule J taxes | None (no CAMT, no PHC tax, no recapture) | User confirmed |
| 2026 estimated tax payments | 4 × $10,750 = $43,000 | EFTPS history |
| 2025 overpayment credited to 2026 | $1,236 | 2025 Form 1120 line 37a |
| Refundable credits, withholding | None | User confirmed |

## Deadlines

- Original due date: 15th day of the 4th month after December 31, 2026 = Thursday, April 15, 2027 (IRC §6072(a); 2025 Instructions for Form 1120). Form 7004 and the line 8 payment are due that day.
- Extended due date: 6 months = Friday, October 15, 2027 (i7004, Extension Period; Treas. Reg. §1.6081-3(a)).

## Line 6, step by step

```
Income tax: $287,450 × 21%                    = $60,364.50   (IRC §11(b); Schedule J line 1a)
Less nonrefundable credit                     −  $8,912.00   (Schedule J line 5c)
Tentative total tax                           = $51,452.50
Rounded (add with cents, round the total)     = $51,453      (i7004, Rounding)
```

## Line 7

```
2026 estimated payments                       $43,000
2025 overpayment credited                     + $1,236
Total payments and credits                    $44,236
```

## Line 8

```
$51,453 − $44,236 = $7,217
```

Paid by Electronic Funds Withdrawal with the e-filed Form 7004, settlement date April 15, 2027. The corporation's treasurer signs Form 8878-A with a PIN; the ERO keeps it.

## The completed Form 7004 draft

```markdown
# Form 7004 — DRAFT for Kestrel Fieldworks Inc. (tax year 2026)

## Filing summary
- Return extended: Form 1120 (code 12)
- Tax year: calendar year 2026
- Form 7004 due: Thursday, April 15, 2027
- Extended return due: Friday, October 15, 2027
- Channel: e-file (MeF) with EFW; Form 8878-A retained by ERO
- Payment due with this form: $7,217 by April 15, 2027

## Identification
Name: Kestrel Fieldworks Inc.  (matches 2025 Form 1120)
Identifying number: 8X-XXXXXXX
Address: <street>, Austin, TX <ZIP>

## Part I
1. Form code: 12

## Part II
2. Foreign corporation without U.S. office: ☐ (not checked)
3. Common parent of consolidated group: ☐ (not checked)
4. Qualifies under Reg. §1.6081-5: ☐ (not checked)
5a. Calendar year 2026
5b. Short tax year: N/A (12-month year)
6. Tentative total tax:                 $51,453
7. Total payments and credits:          $44,236
8. Balance due:                         $7,217
```

## What happens when the return is finished

The corporation files Form 1120 on September 14, 2027. Its total tax (page 1, line 31) is $55,880.

90% test (i7004, Payment of Tax):

```
90% of final total tax: $55,880 × 0.90           = $50,292
Line 6 on Form 7004                                = $51,453
Tax paid by April 15, 2027: $44,236 + $7,217       = $51,453
$51,453 ≥ $50,292 → relief applies
Balance due with the return: $55,880 − $51,453     = $4,427
```

No failure-to-pay penalty applies to the $4,427 if it is paid by October 15, 2027. Interest on $4,427 still runs from April 15, 2027 until paid (i7004, Interest), at the IRC §6621 rate for each quarter (https://www.irs.gov/payments/quarterly-interest-rates).

The return reports the $7,217 on Schedule J, line 17 ("Tax deposited with Form 7004") (2025 Form 1120).

## Counterfactual: line 6 set equal to payments, nothing paid with Form 7004

```
Line 6 = $44,236, line 8 = $0, nothing paid on April 15
Tax paid by the original due date: $44,236 → 44,236 / 55,880 = 79.2% < 90%
Unpaid on April 15, 2027: $55,880 − $44,236       = $11,644
Paid with the return on September 14, 2027: 5 months or part of a month
  (Apr 16–May 15, May 16–Jun 15, Jun 16–Jul 15, Jul 16–Aug 15, Aug 16–Sep 14)
Failure-to-pay penalty: $11,644 × 0.5% × 5        = $291.10
```

Plus interest on $11,644 from April 15. A deliberately low line 6 also puts the extension itself at risk, because the corporation must remit the properly estimated unpaid tax by the due date (Treas. Reg. §1.6081-3(a)(3)).

## Why each non-obvious choice

**Why include the research credit in line 6?** i7004 defines line 6 as total tax "including any nonrefundable credits," that is, the figure the return's total tax line will show after Schedule J credits.

**Why not round each step?** i7004 says to include cents when adding amounts for one line and round only the total: $51,452.50 becomes $51,453.

**Why flag estimated tax?** The corporation's 2026 installments ($44,236 including the overpayment credit) are below its final 2026 tax. Form 7004 does not affect the separate estimated tax penalty (IRC §6655; Form 2220; Form 1120 line 34). The agent flags it for the return preparer and does not compute it here.

**Why no paper address?** The form is e-filed. If it had to go on paper, Texas is in the Ogden group for Form 1120 regardless of assets: Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0045 (i7004, Where To File).

## Sources cited in this example

- Form 7004 (Rev. December 2025) and Instructions for Form 7004 (Rev. December 2025)
- 2025 Form 1120 (page 1 line 31; Schedule J lines 1a, 5c, 12, 17) and 2025 Instructions for Form 1120 (When To File)
- IRC §11(b), §6072(a), §6081, §6621, §6651(a)(2), §6655
- Treas. Reg. §1.6081-3(a)
- Form 8878-A (Rev. December 2008)
