# Schedule 2 Line-by-Line Reference

Complete lookup for every line on Schedule 2 (Form 1040). Use this when the agent needs to confirm what amount belongs on a line and which upstream form sources it.

The form has two parts:

- **Part I — Tax** (Lines 1–3) → totals to **Form 1040 Line 17**
- **Part II — Other Taxes** (Lines 4–21) → totals to **Form 1040 Line 23**

All amounts originate from upstream forms or worksheets. Schedule 2 is a transcription target, not a calculation.

## Header

| Field | What goes here | Source |
|-------|----------------|--------|
| Name(s) shown on return | Filer's legal name as on Form 1040 | Form 1040 header |
| Your social security number | Filer's SSN or ITIN | Form 1040 header |

For MFJ returns, only the *primary* filer's SSN — same as Form 1040 page 1.

---

## Part I — Tax (Lines 1–3) → Form 1040 Line 17

### Line 1 — Alternative minimum tax

| Field | Detail |
|-------|--------|
| Source form | Form 6251 |
| Source line | Form 6251 Line 11 |
| IRC | §55, §59 |
| Threshold trigger | Form 6251 worksheet shows tentative minimum tax > regular tax |
| Common triggers | ISO exercise (the bargain element is an AMT preference), large state and local tax deduction (added back for AMT), large miscellaneous itemized deductions (pre-TCJA — most no longer relevant), depreciation method differences, private activity bond interest |
| 2025 AMT exemption | Single/HoH: $88,100; MFJ: $137,000; MFS: $68,500 (Rev. Proc. 2024-40). Phaseout starts at $626,350 single / $1,252,700 MFJ. |
| 2026 AMT exemption | Set by inflation adjustment in fall 2025 Revenue Procedure — verify before filing. |
| OBBBA 2025 changes | Permanent AMT exemption increases retained from TCJA; verify exact phaseout thresholds for 2026 against current Revenue Procedure. |

If Line 1 > 0, Form 6251 must be attached.

### Line 2 — Excess advance premium tax credit repayment

| Field | Detail |
|-------|--------|
| Source form | Form 8962 |
| Source line | Form 8962 Line 29 |
| IRC | §36B |
| Trigger | Filer received APTC during the year (reported on Form 1095-A) and reconciliation shows actual income made them entitled to *less* PTC than was advanced |
| Repayment limitation | Capped per Pub 974 Table 5 if AGI is below 400% of FPL. Above 400% FPL, limitation may not apply (verify post-IRA / post-OBBBA rules for 2026). |
| Routing alternative | If Form 8962 instead shows *unused* PTC (Line 26 > 0), that goes on **Schedule 3 Line 9** as a refundable credit, NOT Schedule 2 Line 2. The two can never both be nonzero. |

If Line 2 > 0, Form 8962 must be attached.

### Line 3 — Total Part I

| Field | Detail |
|-------|--------|
| Computation | Line 1 + Line 2 (plus any 1a–1z sub-lines per current-year form revision) |
| Routes to | Form 1040, 1040-SR, or 1040-NR Line 17 |

Verify the destination line on Form 1040 against the current-year revision; the line number has been stable since the 2018 redesign but could shift.

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
| 2026 SS wage base | Announced ~October 2025 — verify before filing |
| Threshold | Required if net SE earnings ≥ $400 |
| Half-of-SE-tax adjustment | Half of Schedule 2 Line 4 is deductible above-the-line on Schedule 1 Line 15 |

If Line 4 > 0, Schedule SE must be attached.

### Line 5 — Social security and Medicare tax on unreported tip income

| Field | Detail |
|-------|--------|
| Source form | Form 4137 |
| Source line | Form 4137 Line 13 |
| IRC | §3101 (employee share of FICA) |
| Trigger | Filer received tips not reported to the employer (so employer didn't withhold FICA on them); the employee owes the missing FICA share |

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
| Trigger | Filer paid a household employee (nanny, housekeeper, eldercare worker) cash wages above the FICA threshold ($2,800 in 2025; verify 2026) OR ≥ $1,000 in any quarter triggering FUTA |
| 2025 FICA threshold | $2,800 per employee per year (Notice 2024-90 / SSA announcement) |
| 2026 FICA threshold | Verify against 2026 IRS announcement |

If Line 9 > 0, Schedule H must be attached.

### Line 10 — Repayment of first-time homebuyer credit

| Field | Detail |
|-------|--------|
| Source form | Form 5405 |
| Source line | Form 5405 Line 16 |
| IRC | §36 (now repealed for new credits; repayment provisions remain) |
| Trigger | Filer claimed the original 2008 first-time homebuyer credit (refundable up to $7,500 with 15-year interest-free repayment) and owes the annual installment of $500. The 2008 credit was unique — 2009/2010 credits had no repayment unless the home was sold within 3 years. |
| Note | Repayment ends after 15 installments; most filers' obligation expired after 2023. Only filers who claimed in 2008 and still owe partial installments report here. |

If Line 10 > 0, Form 5405 must be attached.

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
| Thresholds (statutory, not indexed) | Single / HoH / QSS: $200,000; MFJ / QSS-with-spouse: $250,000; MFS: $125,000 |
| Investment income includes | Interest, dividends, capital gains, rental and royalty income (passive), non-qualified annuities, business income from passive activities |
| Investment income excludes | Wages, SE income from active trades, distributions from qualified retirement plans, IRA distributions, tax-exempt interest, Social Security benefits |

If Line 12 > 0, Form 8960 must be attached.

### Line 13 — Section 965 deferred foreign income transition tax

| Field | Detail |
|-------|--------|
| Source form | Form 965-A |
| IRC | §965 |
| Trigger | TCJA-era transition tax on accumulated foreign earnings; most original obligations have been paid via 8-year installment schedule (2017–2025). Final installment for many filers was 2025. Verify current-year applicability. |

If Line 13 > 0 or Line 20 > 0, Form 965-A must be attached.

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
| Source form | Form 8611 |
| IRC | §42 |
| Trigger | Filer claimed §42 LIHTC and the property failed compliance during the recapture period. |

If Line 16 > 0, Form 8611 must be attached.

### Line 17 — Other additional taxes (sub-items 17a–17z)

See [`line-17-subitems.md`](./line-17-subitems.md) for the complete sub-item list with citations and triggers.

### Line 18 — Total Other Additional Taxes

Computed: sum of Lines 17a through 17z.

### Line 19 — Reserved for future use

Leave blank.

### Line 20 — Section 965 net tax liability installment from Form 965-A

| Field | Detail |
|-------|--------|
| Source | Form 965-A |
| Note | This is the *current installment* and is paid separately. Verify whether the current-year form revision rolls Line 20 into Line 21 (it has not in recent revisions; Section 965 installment is tracked separately on a different IRS account). |

### Line 21 — Total Part II

| Field | Detail |
|-------|--------|
| Computation | Line 4 + Line 7 + Line 8 + Line 9 + Line 10 + Line 11 + Line 12 + Line 13 + Line 14 + Line 15 + Line 16 + Line 18 |
| Excludes | Line 20 (Section 965 installment is paid separately, not added to general income tax due) |
| Routes to | Form 1040, 1040-SR, or 1040-NR Line 23 |

Always verify the exact Line 21 formula against the current-year form revision — line numbering in Part II has shifted in past revisions.
