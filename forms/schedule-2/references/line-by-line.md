# Schedule 2 Line-by-Line Reference

Complete lookup for every line on Schedule 2 (Form 1040). Use this when the agent needs to confirm what amount belongs on a line and which upstream form sources it. Line map verified against the **2025 Schedule 2 (created 5/8/25) and the 2025 Instructions for Form 1040**, filed in 2026; re-check the next revision at https://www.irs.gov/forms-pubs/about-schedule-2-form-1040.

The form has two parts:

- **Part I — Tax** (Lines 1a–3) → totals to **Form 1040 Line 17**
- **Part II — Other Taxes** (Lines 4–21) → totals to **Form 1040 Line 23**

All amounts originate from upstream forms or worksheets. Schedule 2 is a transcription target, not a calculation.

## Header

| Field | What goes here | Source |
|-------|----------------|--------|
| Name(s) shown on return | Filer's legal name as on Form 1040 | Form 1040 header |
| Your social security number | Filer's SSN or ITIN | Form 1040 header |

For MFJ returns, only the *primary* filer's SSN — same as Form 1040 page 1.

---

## Part I — Tax (Lines 1a–3) → Form 1040 Line 17

### Line 1a — Excess advance premium tax credit repayment

| Field | Detail |
|-------|--------|
| Source form | Form 8962 |
| Source line | Form 8962 Line 29 |
| IRC | §36B |
| Trigger | Filer received APTC during the year (reported on Form 1095-A) and reconciliation shows actual income made them entitled to *less* PTC than was advanced |
| Repayment limitation (2025 returns) | Capped per Table 5 of the 2025 Form 8962 instructions if household income is below 400% of FPL: $375 / $750 (under 200%), $975 / $1,950 (200%–under 300%), $1,625 / $3,250 (300%–under 400%) for single / other filing statuses; no cap at 400% or more. |
| Repayment limitation (2026 and later) | None. P.L. 119-21 removed the cap for tax years beginning after Dec. 31, 2025 (IRS Premium Tax Credit Q&A, Q31). |
| Routing alternative | If Form 8962 instead shows net PTC (Line 26 > 0), that goes on **Schedule 3 Line 9** as a refundable credit, NOT Schedule 2. The two can never both be nonzero. |

If Line 1a > 0, Form 8962 must be attached.

### Lines 1b–1c — Repayment of clean vehicle credits transferred to a dealer

| Field | Detail |
|-------|--------|
| Source | Schedule A (Form 8936): Part II (new vehicle) → Line 1b; Part IV (previously owned vehicle) → Line 1c; amount from Part I line 4a |
| Trigger | User transferred the credit to a registered dealer at purchase and no longer qualifies (e.g., income above the limit) |

### Lines 1d–1f — Elective payment election (EPE) items

| Line | Source |
|------|--------|
| 1d | Recapture of net EPE: Form 4255, line 2a, column (l) |
| 1e | Excessive payments on gross EPE: Form 4255, column (n)(1); check the box for the Form 4255 line |
| 1f | 20% excessive payment: Form 4255, column (n)(3); check the box |

### Line 1y — Other additions to tax

Items listed in the 2025 Schedule 2 instructions, each identified by a code: "ARPCR" (recapture of the alternative fuel vehicle refueling property credit, Form 8911), "EPE8933", "NEPE8933", "EPGEPE", "6418(g)(2)".

### Line 1z — Add Lines 1a through 1y

Computed only.

### Line 2 — Alternative minimum tax

| Field | Detail |
|-------|--------|
| Source form | Form 6251 |
| Source line | Form 6251 Line 11 |
| IRC | §55, §59 |
| Threshold trigger | Form 6251 shows tentative minimum tax (line 9) greater than line 10 (Form 1040 line 16 tax + Schedule 2 line 1z − Schedule 3 line 1) |
| Common triggers | ISO exercise (the bargain element is an AMT adjustment), state and local taxes deducted on Schedule A (added back on Form 6251 line 2a; the standard deduction is added back too), depreciation method differences, private activity bond interest |
| 2025 AMT exemption | Single/HoH: $88,100; MFJ/QSS: $137,000; MFS: $68,500. Phaseout starts at $626,350 single and MFS / $1,252,700 MFJ (2025 Form 6251 and instructions; Rev. Proc. 2024-40). 26% rate on the first $239,100 ($119,550 MFS) of line 6. |
| 2026 AMT exemption | Single/HoH: $90,100; MFJ/QSS: $140,200; MFS: $70,100. Phaseout starts at $500,000 single and MFS / $1,000,000 MFJ, and the exemption phases out at 50 cents per dollar (complete at $680,200 / $1,280,400 / $640,200). 28% rate above $244,500 ($122,250 MFS). Source: Rev. Proc. 2025-32 §4.10, reflecting P.L. 119-21. |
| 2025 form change | Form 6251 line 1 is split into 1a/1b (the Schedule 1-A senior deduction is added back) — 2025 Instructions for Form 6251, What's New. |

If Line 2 > 0, Form 6251 must be attached.

### Line 3 — Total Part I

| Field | Detail |
|-------|--------|
| Computation | Line 1z + Line 2 |
| Routes to | Form 1040, 1040-SR, or 1040-NR Line 17 |

Verify the destination line on Form 1040 against the current-year revision.

---

## Part II — Other Taxes (Lines 4–21) → Form 1040 Line 23

### Line 4 — Self-employment tax

| Field | Detail |
|-------|--------|
| Source form | Schedule SE |
| Source line | Schedule SE Line 12 |
| IRC | §1401 |
| Rate | 15.3% on net SE earnings up to the SS wage base (12.4% Social Security + 2.9% Medicare); 2.9% Medicare-only on SE earnings above the SS wage base |
| 2025 SS wage base | $176,100 (SSA announcement October 2024) |
| 2026 SS wage base | $184,500 (https://www.ssa.gov/oact/cola/cbb.html) |
| Threshold | Required if net SE earnings ≥ $400 |
| Half-of-SE-tax adjustment | Half of Schedule 2 Line 4 is deductible above-the-line on Schedule 1 Line 15 |

If Line 4 > 0, Schedule SE must be attached.

### Line 5 — Social security and Medicare tax on unreported tip income

| Field | Detail |
|-------|--------|
| Source form | Form 4137 |
| Source line | Form 4137 Line 13 |
| IRC | §3101 (employee share of FICA) |
| Trigger | Filer received cash tips of $20 or more in a month that were not reported to the employer (so employer didn't withhold FICA on them); the employee owes the missing FICA share. Tips reported to the employer but not fully withheld on are Line 13, not Line 5. |

If Line 5 > 0, Form 4137 must be attached.

### Line 6 — Uncollected social security and Medicare tax on wages

| Field | Detail |
|-------|--------|
| Source form | Form 8919 |
| Source line | Form 8919 Line 13 |
| IRC | §3121, §3401 |
| Trigger | Filer was treated as an independent contractor by an employer when the filer believes they should have been an employee; FICA wasn't withheld and the filer owes the employee share. Filing 8919 also reports the misclassification to the IRS. |
| Reason codes | Form 8919 requires a reason code (A–G) explaining why the filer was actually an employee |

If Line 6 > 0, Form 8919 must be attached.

### Line 7 — Total of Lines 5 + 6

Computed only.

### Line 8 — Additional tax on IRAs or other tax-favored accounts

| Field | Detail |
|-------|--------|
| Source form | Form 5329 (multi-part) |
| Common parts | Part I (early distribution from IRA before 59½ — 10% additional tax under IRC §72(t)); Part III (excess IRA contributions); Part IV (excess Roth IRA contributions); Part V (excess Coverdell contributions); Part VII (excess HSA contributions); Part VIII (excess ABLE contributions); Part IX (missed RMD — 25% additional tax, reduced to 10% if corrected timely under SECURE 2.0) |
| IRC | §72(t), §4973, §4974 |
| 10% rate exceptions | Death, disability, qualified higher education expenses, first-time home purchase up to $10,000, substantially equal periodic payments, etc. — see Form 5329 Part I instructions |
| Missed RMD relief | SECURE 2.0 reduced the §4974 excise from 50% to 25% (or 10% if corrected within the correction window) for tax years beginning after 2022 |

If Line 8 > 0, Form 5329 must be attached.

### Line 9 — Household employment taxes

| Field | Detail |
|-------|--------|
| Source form | Schedule H |
| Source line | Schedule H Line 8 (or Line 26 if applicable) |
| IRC | §3510, §3102 |
| Trigger | Filer paid any one household employee cash wages of $2,800 or more in 2025, withheld federal income tax at the employee's request, OR paid total cash wages of $1,000 or more in any calendar quarter of 2024 or 2025 (FUTA) |
| 2025 FICA threshold | $2,800 per employee per year (2025 Schedule 2 instructions, line 9; SSA coverage thresholds) |
| 2026 FICA threshold | $3,000 per employee per year (https://www.ssa.gov/oact/cola/CovThresh.html) |

If Line 9 > 0, Schedule H must be attached.

### Line 10 — Reserved for future use

On the 2025 revision Line 10 is "Reserved for future use." Through 2024 returns it carried the repayment of the 2008 first-time homebuyer credit (Form 5405, Rev. November 2024, directs the amount to the 2024 Schedule 2 line 10); the 15 annual installments ended with 2024 returns. Leave blank. If a user insists they owe a homebuyer-credit repayment, stop and refer them to a CPA.

### Line 11 — Additional Medicare Tax

| Field | Detail |
|-------|--------|
| Source form | Form 8959 |
| Source line | Form 8959 Line 18 |
| IRC | §3101(b)(2), §1401(b)(2) |
| Rate | 0.9% on wages + SE earnings above the filing-status threshold |
| Thresholds (statutory, not indexed) | Single / HoH / QSS: $200,000; MFJ: $250,000; MFS: $125,000 |

If Line 11 > 0, Form 8959 must be attached.

### Line 12 — Net Investment Income Tax (NIIT)

| Field | Detail |
|-------|--------|
| Source form | Form 8960 |
| Source line | Form 8960 Line 17 |
| IRC | §1411 |
| Rate | 3.8% on the lesser of (a) net investment income or (b) MAGI above threshold |
| Thresholds (statutory, not indexed) | Single / HoH: $200,000; MFJ / QSS: $250,000; MFS: $125,000 (filers with Form 2555 use lower AGI screens; see the 2025 Schedule 2 instructions, line 12) |
| Investment income includes | Interest, dividends, capital gains, rental and royalty income (passive), non-qualified annuities, business income from passive activities |
| Investment income excludes | Wages, SE income from active trades, distributions from qualified retirement plans, IRA distributions, tax-exempt interest, Social Security benefits |

If Line 12 > 0, Form 8960 must be attached.

### Line 13 — Uncollected social security and Medicare or RRTA tax on tips or group-term life insurance

| Field | Detail |
|-------|--------|
| Source | Form W-2 box 12, codes A and B (tips) or M and N (group-term life insurance for former employees) |
| IRC | §3101, §3102 |
| Trigger | The employer could not collect the employee share of FICA/RRTA on reported tips or on group-term life insurance coverage, and reported the uncollected amounts on the W-2 |

### Line 14 — Interest on installment income from sale of certain residential lots and timeshares

| Field | Detail |
|-------|--------|
| IRC | §453(l)(3) |
| Trigger | Dealer in residential lots or timeshares used the installment method on a sale and now owes interest on deferred tax. Rare for individual filers. |

### Line 15 — Interest on deferred tax on installment sales > $150,000

| Field | Detail |
|-------|--------|
| IRC | §453A |
| Trigger | Filer used the installment method on a sale > $150,000 (other than personal-use property or farm property) and the deferred obligation > $5,000,000. Rare for individuals. |

### Line 16 — Recapture of low-income housing credit

| Field | Detail |
|-------|--------|
| Source form | Form 8611 (line 14) |
| IRC | §42 |
| Trigger | Filer claimed §42 LIHTC and the property failed compliance during the recapture period. |

If Line 16 > 0, Form 8611 must be attached.

### Line 17 — Other additional taxes (sub-items 17a–17z)

See [`line-17-subitems.md`](./line-17-subitems.md) for the complete sub-item list with citations and triggers.

### Line 18 — Total Other Additional Taxes

Computed: sum of Lines 17a through 17z.

### Line 19 — Recapture of net EPE from Form 4255

| Field | Detail |
|-------|--------|
| Source | Form 4255, line 1d, column (l) — recapture of net elective payment election amount related to the Form 3468, Part IV credit |
| Trigger | Rare for individuals |

### Line 20 — Section 965 net tax liability installment from Form 965-A

| Field | Detail |
|-------|--------|
| Source | Form 965-A |
| IRC | §965 |
| Note | The *current installment* of a §965(h) election. It is not added into Line 21 (2025 form: "Add lines 4, 7 through 16, 18, and 19"). If Line 20 > 0, Form 965-A must be attached. |

### Line 21 — Total Part II

| Field | Detail |
|-------|--------|
| Computation | Line 4 + Lines 7 through 16 + Line 18 + Line 19 (Line 10 is reserved and blank) |
| Excludes | Line 20 (Section 965 installment) |
| Routes to | Form 1040 or 1040-SR Line 23; Form 1040-NR Line 23b |

Always verify the exact Line 21 formula against the current-year form revision — line numbering in Part II has shifted in past revisions.
