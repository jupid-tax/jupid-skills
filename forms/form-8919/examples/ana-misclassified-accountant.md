# Example: Ana the Misclassified Accountant (Single Firm, Code G)

End-to-end worked Form 8919 for the most common misclassification scenario: a full-time misclassified employee with one firm, no W-2, and a pending SS-8.

---

## Persona

**Ana Rodriguez**, age 31, lives in Austin, TX. Files single. SSN: 123-45-6789.

**Engagement:** Ana works at ABC Consulting LLC, a 25-person consulting firm headquartered in Austin. She started in March 2025 and worked all of 2026.

**Compensation:** $6,000/month flat retainer = $72,000 in 2026. Reported on Form 1099-NEC, Box 1 = $72,000. ABC's EIN: 12-3456789.

**Work pattern:**
- Ana works in ABC's office Monday-Friday, 9 AM to 5 PM
- ABC supplies her laptop, accounting software (QuickBooks Online subscription), and office space
- ABC's senior partners (Robert and Linda) assign her work and review her output
- Ana attended ABC's training week in March 2025
- Ana has no other clients; ABC is her sole source of income
- Ana's email signature reads "Ana Rodriguez, Senior Accountant, ABC Consulting"
- Ana receives no benefits (no health insurance, no retirement, no PTO)

---

## Common-Law Test Result

| Category | Indicators | Result |
|----------|-----------|--------|
| **Behavioral control** | Set hours, set location, ABC dictates methods, ABC trained her, ABC reviews work | Strong employee |
| **Financial control** | No equipment investment, no other clients, no profit/loss risk, fixed retainer | Strong employee |
| **Type of relationship** | Indefinite engagement, integral to ABC's accounting service, no benefits but consistent role | Employee (despite no benefits) |

**Conclusion:** Three of three categories point to employee. Form 8919 applies.

---

## Filing Steps

### Step 1: File Form SS-8 (February 2027)

Ana mails Form SS-8 (separately from her return) to the address in the Instructions for Form SS-8 (Rev. January 2024):

```
Internal Revenue Service
Form SS-8 Determinations
P.O. Box 630
Stop 631
Holtsville, NY 11742-0630
```

**Enclosures:**
- Completed Form SS-8 (8 pages)
- Copies of her 1099-NECs from ABC for 2025 and 2026 (2026: $72,000)
- Copy of her engagement letter from March 2025
- 6 selected emails showing ABC assigning specific tasks with deadlines
- Copy of ABC's "team handbook" she received during training
- Cover letter noting she will file Form 8919 with code G on her 2026 1040

**Mail method:** USPS Certified Mail with Return Receipt. The receipt comes back signed February 18, 2027.

### Step 2: Prepare Form 8919 for 2026 1040

Line numbers follow the 2025 Form 8919 (created 10/22/25); re-check them on the 2026 revision when it is released. The 2026 wage base is $184,500 (SSA, https://www.ssa.gov/oact/cola/cbb.html).

**Line 1:**

| Column | Entry |
|--------|-------|
| (a) Firm name | ABC Consulting LLC |
| (b) Federal ID number | 12-3456789 |
| (c) Reason code | G |
| (d) Date of determination or correspondence | (blank — only for codes A and C) |
| (e) Form 1099-MISC/NEC received | ☑ |
| (f) Total wages | $72,000 |

**Lines 6-13:**

| Line | Computation | Amount |
|------|-------------|--------|
| 6 | Total wages (sum of column f) | $72,000 |
| 7 | 2026 SS wage base | $184,500 |
| 8 | Other SS wages (W-2 Box 3 + Box 7, RRTA, Form 4137 line 10); Ana has no W-2 | $0 |
| 9 | Line 7 − Line 8 | $184,500 |
| 10 | Smaller of Line 6 or Line 9 | $72,000 |
| 11 | SS tax = Line 10 × 6.2% | $4,464 |
| 12 | Medicare tax = Line 6 × 1.45% | $1,044 |
| 13 | Total = Line 11 + Line 12 | **$5,508** |

Additional Medicare Tax: Ana's $72,000 of Medicare wages is under the $200,000 single threshold, so no Form 8959.

### Step 3: Route to Form 1040 and Schedule 2

**Form 1040, Line 1g:** $72,000 (wages from Form 8919, line 6)

**Schedule 2, Line 6:** $5,508 (Form 8919, line 13)

**Form 1040, Line 23:** flows from Schedule 2 line 21 = $5,508

### Step 4: Complete Rest of Form 1040

Ana has no W-2, no other income. Her 1040 (line numbers from the 2025 Form 1040):

| Line | Description | Amount |
|------|-------------|--------|
| 1a | W-2 wages | $0 |
| 1g | Wages from Form 8919 | $72,000 |
| 1z | Total wages (sum 1a-1h) | $72,000 |
| 9 | Total income | $72,000 |
| 10 | Adjustments (none — Ana doesn't deduct half SE tax because she didn't pay SE tax) | $0 |
| 11a | AGI | $72,000 |
| 12e | Standard deduction (single, 2026) | $16,100 (Rev. Proc. 2025-32 §4.14) |
| 13a | QBI deduction | $0 (wages are not qualified business income) |
| 15 | Taxable income | $55,900 |
| 16 | Income tax (2026 single rate schedule, Rev. Proc. 2025-32 §4.01; the Tax Table can differ by a few dollars) | $7,010 |
| 23 | Other taxes (from Schedule 2, includes Form 8919 line 13) | $5,508 |
| 24 | Total tax | $12,518 |

### Step 5: File 1040 by April 15, 2027

E-file through an IRS Free File partner (AGI $72,000 is under the $89,000 guided Free File limit for the 2026 filing season; re-check the limit for the 2027 season and confirm the partner supports Form 8919) or Free File Fillable Forms.

---

## Tax Savings vs. Schedule SE Alternative

If Ana had instead filed Schedule SE on the same $72,000:

```
Net SE earnings (Schedule SE line 4a) = $72,000 × 0.9235 = $66,492
SE tax (line 12) = $66,492 × 12.4% + $66,492 × 2.9% = $8,245 + $1,928 = $10,173
Half SE tax deduction (line 13 → Schedule 1 line 15) = $5,087
```

Ana's 1040 with Schedule C and Schedule SE (2026 rates):

| Line | Amount |
|------|--------|
| Total income | $72,000 |
| Half SE tax deduction | -$5,087 |
| AGI | $66,913 |
| Standard deduction | -$16,100 |
| Taxable income before QBI deduction | $50,813 |
| QBI deduction (Form 8995): smaller of 20% × ($72,000 − $5,087) = $13,383 or 20% × $50,813 = $10,163. Accounting is a specified service business, but her income is below the §199A threshold | -$10,163 |
| Taxable income | $40,650 |
| Income tax (2026 single rate schedule) | $4,630 |
| SE tax (Schedule 2 line 4) | $10,173 |
| **Total tax** | **$14,803** |

**Form 8919 saves Ana $2,285** in 2026 ($14,803 − $12,518). The payroll-tax difference alone is $4,665 ($10,173 − $5,508), but the Schedule SE route would also have given her the half-SE-tax deduction and a QBI deduction, which Form 8919 wages do not get. The savings recur for each year she is misclassified.

---

## What Happens Next

### IRS Contacts ABC Consulting (2027)

The IRS sends ABC a blank Form SS-8 to complete and may share Ana's information with ABC. ABC may:

- Acknowledge the misclassification (rare)
- Argue Ana was a contractor (most common — ABC will likely dispute)
- Not respond (the SS-8 instructions say a non-response won't stop the IRS from issuing an information letter based on the facts it has)

Ana's relationship with ABC may be strained — ABC will know she filed. Many workers in Ana's situation file SS-8 only after the engagement ends.

### IRS Determination (late 2027 or later)

The IRS says a determination may take at least six months. It generally issues the determination to ABC and sends a copy to Ana. Three outcomes:

**Outcome 1: Favorable (Ana = employee).** Ana's 8919 filing stands. She can amend 2025 (also misclassified) within the IRC §6511 refund period. ABC may face back-FICA exposure (or may qualify for Section 530 relief).

**Outcome 2: Adverse (Ana = contractor).** Ana must amend her 2026 1040, replacing 8919 with Schedule C and Schedule SE. She owes about $2,285 of additional tax plus interest from April 15, 2027, and Form 8919 warns she may also be billed penalties.

**Outcome 3: Information letter instead of a formal determination.** It is advisory and not binding on the IRS. If it states she is an employee, ask whether code C fits; otherwise her code G filing stands on her documentation.

---

## Documentation Ana Retains

- Copy of Form SS-8 mailed February 2027
- Certified mail receipt and return receipt
- Copies of all 1099-NECs from ABC (2025, 2026)
- Fax or mail proof for the SS-8 filing
- Engagement letter
- 6 emails showing ABC's direction
- Team handbook
- Time logs (Ana kept her own time tracker even though ABC didn't require one)
- Performance review email from December 2026

Retention: 3 years from filing the 2026 1040 = until April 2030 minimum. Ana keeps for 7 years to be safe.

---

## Lessons

1. **The common-law test was clear.** Three of three categories pointed to employee. Ana's 8919 case is strong.
2. **No W-2 means full wage base available for SS.** Line 9 had $184,500 of room; the full $72,000 fit under the SS cap.
3. **No double-counting.** Ana doesn't put the $72,000 on Schedule C. It's only on Form 8919 + Form 1040 line 1g.
4. **SS-8 first, then 8919.** Ana mailed SS-8 in February, before filing the 1040 in April (code G requires SS-8 on or before the return date). The certified mail receipt is her proof.
5. **Tax savings = $2,285 for 2026, not the full $4,665 payroll-tax difference.** The Schedule SE route carries the half-SE-tax and QBI deductions; Form 8919 wages carry neither.
6. **Documentation is everything.** Without the engagement letter and the 6 emails, Ana's case would be weaker. With them, the IRS has a clear factual record.

---

## Sources Used in This Example

- [Form 8919](https://www.irs.gov/pub/irs-pdf/f8919.pdf) (line map from the 2025 revision; re-check the 2026 revision)
- [Form SS-8 (Rev. December 2023)](https://www.irs.gov/pub/irs-pdf/fss8.pdf) and [Instructions (Rev. January 2024)](https://www.irs.gov/pub/irs-pdf/iss8.pdf)
- [SSA Contribution and Benefit Base](https://www.ssa.gov/oact/cola/cbb.html) — 2026 wage base $184,500
- Rev. Proc. 2025-32 §4.01 (2026 rate schedule), §4.14 (2026 standard deduction $16,100 single)
- IRC §199A (QBI deduction; employee wages excluded under §199A(d)(1)(B))
- [IRS Publication 15-A](https://www.irs.gov/pub/irs-pdf/p15a.pdf) — Common-law test
- IRC §3101 (employee FICA), §3121(d) (employee definition)
- Rev. Rul. 87-41 (20-factor test, refined into Pub 15-A)
