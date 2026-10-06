# Example: S Corporation with a Shareholder-Officer and One Employee (Tax Year 2025)

An S corporation pays its sole shareholder a salary and health insurance, employs one part-time worker, and paid one quarter of state unemployment tax late to the state but before the Form 940 due date. The example then runs the line 10 worksheet for two what-if cases. Line map: 2025 Form 940 (Created 6/2/25) and the 2025 Instructions for Form 940 (I940).

## The filer

- **Name:** Halyard Marine Survey, Inc., Tampa, Florida; S corporation (Form 2553 on file); EIN 5X-XXXXXXX (masked)
- **Officer:** Renata Vos, president and 100% shareholder. Corporate officers who work in the business are employees (Pub. 15 (2026), section 2).
  - Salary $75,000 ($6,250 a month)
  - Health insurance premiums paid by the corporation for her, $9,288, included in her W-2 box 1. For a more-than-2% shareholder these premiums are excluded from Social Security, Medicare, and FUTA wages (Pub. 15 (2026), section 5; Announcement 92-16).
  - Distributions of $40,000. Not wages; not on Form 940 (Pub. 15 (2026), section 15 table).
- **Employee:** Theo Marsh, part-time surveyor's assistant, $18,460 ($4,615 a quarter)
- **State:** Florida only. Florida's 2025 taxable wage base is $7,000 and its experience-rated range is 0.10% to 5.40% with a 2.70% new-employer base rate (DOL, Significant Provisions of State UI Laws, July 2025). The corporation's 2025 rate notice shows 2.70% (user document). Florida's reports covered both Renata's and Theo's wages (user confirmed; no exclusion).
- **Florida tax by quarter (from the user's state reports):** Q1 (7,000 + 4,615) × 0.027 = $313.61; Q2 2,385 × 0.027 = $64.40; Q3 and Q4 $0 (both employees reached $7,000 by Q2). Total $378.01.
- **Payment history:** Q2 paid July 2025. Q1 was missed when the payroll provider was set up in April; the corporation found it at year-end and paid $313.61 on January 20, 2026, with a Florida penalty and interest that are excluded from contributions (I940, "Credit for State Unemployment Tax Paid to a State Unemployment Fund").
- **FUTA deposits:** none.

## Step-by-step

Per-employee table (I940, lines 3–7):

| Employee | Line 3 payments | Line 4 exempt | Excess over $7,000 (line 5) | FUTA wages |
|---|---:|---:|---:|---:|
| Renata Vos | 75,000 + 9,288 = 84,288.00 | 9,288.00 (4a) | 84,288 − 9,288 − 7,000 = 68,000.00 | 7,000.00 |
| Theo Marsh | 18,460.00 | 0.00 | 11,460.00 | 7,000.00 |
| **Total** | **102,748.00** | **9,288.00** | **79,460.00** | **14,000.00** |

Line 8 = 14,000 × 0.006 = 84.00.

**Is line 10 needed?** The decision rule: line 10 applies if SOME FUTA wages were excluded from state tax or ANY state tax was paid after the Form 940 due date (I940, line 10). Neither is true. The Q1 payment was late under Florida's schedule but was made on January 20, 2026, before the February 2, 2026 Form 940 due date, and "on time" for FUTA means paid by the Form 940 due date. Line 10 stays blank.

Cross-check with the worksheet: line 1 = 14,000 × 0.054 = 756.00; line 2 (paid on time) = 313.61 + 64.40 = 378.01; line 3 = 14,000 × (0.054 − 0.027) = 378.00; line 4 = 756.01 ≥ line 1 → stop, line 10 blank.

**Deposits and due date.** Line 12 is $84.00, never above $500, so no deposit was required and Part 5 is blank. Pay the $84.00 with the return. Because no deposit was made, plan on the regular due date, Monday February 2, 2026, rather than February 10.

## The completed draft

```markdown
# Form 940 — DRAFT for tax year 2025

Form revision used: Form 940 (2025), Created 6/2/25

## Header
EIN: 5X-XXXXXXX
Name: Halyard Marine Survey, Inc.
Address: <user>, Tampa, FL
Type of return: none checked

## Part 1
1a. FL
1b. blank
2.  blank

## Part 2
3. Total payments to all employees:            102,748.00
4. Payments exempt from FUTA tax:                9,288.00   [X]4a
5. Payments in excess of $7,000:                79,460.00
6. Subtotal (4 + 5):                            88,748.00
7. Total taxable FUTA wages (3 − 6):            14,000.00
8. FUTA tax before adjustments (7 × 0.006):         84.00

## Part 3
9.  blank
10. blank (all Florida tax paid by Feb 2, 2026; no wages excluded)
11. blank

## Part 4
12. Total FUTA tax after adjustments:               84.00
13. FUTA tax deposited for the year:                blank
14. Balance due:                                    84.00   (≤ $500: may be paid with the return)
15a. Overpayment:                                   blank

## Part 5 — blank (line 12 not more than $500)
## Part 6 — No designee
## Part 7 — Renata Vos, President; phone; date

## Validation summary
- Line 7 = 2 × 7,000 = 14,000.00 ✓; line 8 = 84.00 ✓
- 2% shareholder health premiums on lines 3 and 4 (4a) ✓; distributions excluded ✓
- Line 10 decision documented; worksheet line 4 (756.01) ≥ line 1 (756.00) ✓
- Payment: $84.00 by Direct Pay or EFTPS (then file at the "Without a payment" address), or EFW if e-filing, or check with Form 940-V
- Due Feb 2, 2026
```

## What-if A: the Q1 Florida tax is still unpaid when Form 940 is filed

Facts change: on February 2, 2026 only the Q2 $64.40 has been paid. Now some state tax is unpaid at the due date, so the worksheet runs (I940, Worksheet—Line 10):

| Line | Computation | Result |
|---|---|---:|
| 1 | 14,000.00 × 0.054 | 756.00 |
| 2 | Paid on time | 64.40 |
| 3 | 14,000 × (0.054 − 0.027) | 378.00 |
| 4 | 64.40 + 378.00 | 442.40 (< line 1, continue) |
| 5a | 756.00 − 442.40 | 313.60 |
| 5b | Paid late | 0.00 |
| 5c | Smaller of 5a, 5b | 0.00 |
| 5d | 5c × 0.900 | 0.00 |
| 6 | 442.40 + 0.00 | 442.40 |
| 7 | 756.00 − 442.40 | **313.60 → Form 940 line 10** |

Line 12 = 84.00 + 313.60 = 397.60. Still $500 or less, so it may be paid with the return.

## What-if B: Florida is paid on March 12, 2026, after What-if A was filed

The corporation may file an amended 2025 Form 940 (box a, the 2025 form, all amounts as they should be, an attached explanation) to claim the 90% credit for state tax paid late; the instructions name this as a reason to amend (I940, "Can You Amend a Return?").

| Line | Computation | Result |
|---|---|---:|
| 1–4 | as in What-if A | 756.00 / 64.40 / 378.00 / 442.40 |
| 5a | 756.00 − 442.40 | 313.60 |
| 5b | Paid late (Mar 12, 2026) | 313.61 |
| 5c | Smaller of 5a, 5b | 313.60 |
| 5d | 313.60 × 0.900 | 282.24 |
| 6 | 442.40 + 282.24 | 724.64 |
| 7 | 756.00 − 724.64 | **31.36 → amended line 10** |

Amended line 12 = 84.00 + 31.36 = 115.36. The $397.60 already paid exceeds this by $282.24. Line 13 reports FUTA deposits only, and the payment sent with the original return was not a deposit. Before filing, ask the user's CPA or the e-file provider how the amended return should present lines 13 to 15 for an amount paid with the original return, and say so in the draft rather than guessing. Paper amended returns go to the "Without a payment" address even if a payment is enclosed (I940).

## Why each non-obvious choice

**Officer wages are FUTA wages.** The officer works in the business and is an employee of the corporation (Pub. 15 (2026), section 2). Only the first $7,000 counts.

**Health premiums on line 3 and line 4.** They are part of W-2 box 1 for the 2% shareholder and are payments for services, so they belong on line 3; they are excluded from FUTA wages, so they go on line 4, box 4a.

**State "late" versus FUTA "late."** Florida's own deadline passed, but the FUTA credit test looks only at the Form 940 due date. The state penalty and interest are not contributions and are not counted anywhere on the worksheet.

**Line 3 of the worksheet uses Florida taxable wages.** Taxable state wages equal FUTA wages here ($7,000 each) because Florida's 2025 base is $7,000; in a state with a higher base, line 3 can be larger than line 1 by itself.

## Handoffs

- Forms 941 for each quarter, and W-2/W-3 showing the health premiums in box 1 but not in boxes 3 and 5 (see [`../../form-941/SKILL.md`](../../form-941/SKILL.md)).
- Reasonable compensation for the shareholder-officer is a judgment for the user's CPA; the S corporation return is in [`../../form-1120-s/SKILL.md`](../../form-1120-s/SKILL.md).
- Paper return for a Florida filer: without a payment, Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0046; with a payment, Internal Revenue Service, P.O. Box 932000, Louisville, KY 40293-2000 (I940, "Where Do You File?"). See [`../filing.md`](../filing.md).
