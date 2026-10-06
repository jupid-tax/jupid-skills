# Example: Joel — Dual W-2 + 1099 from Same Firm (Code H)

End-to-end worked Form 8919 for the second-most-common misclassification scenario: a worker who received both a W-2 and a 1099 from the same firm for the same job, where the 1099 portion should have been wages.

---

## Persona

**Joel Patel**, age 38, lives in Denver, CO. Files married filing jointly. SSN: 234-56-7890.

**Engagement:** Joel has been an in-house graphic designer at Acme Studios for 4 years. Acme is a 60-person creative agency.

**Compensation in 2026:**
- W-2 from Acme: $60,000 (Box 1) / $60,000 (Box 3) / $0 tips. Withholding: $9,000 federal, $3,720 SS, $870 Medicare.
- 1099-NEC from Acme: $18,000. Acme calls these payments "extra project compensation" for work Joel did "outside his core 40 hours."
- Acme's EIN: 87-6543210

**Why the 1099 portion should be wages:**

Joel worked his 40-hour week creating campaigns for Acme's clients (W-2 work). In addition, Acme sometimes asked Joel to do additional design work for the same clients in the same Acme office on the same Acme equipment — and paid for those hours via 1099 instead of payroll. Acme's logic was "we don't want to pay overtime so we'll 1099 the extra hours." The work itself was indistinguishable from his W-2 work.

This is **code H** on the 2025 Form 8919: "I received a Form W-2 and a Form 1099-MISC and/or 1099-NEC from this firm ... The amount on Form 1099-MISC and/or 1099-NEC should have been included as wages on Form W-2." (Code C is a different code: other IRS correspondence stating the worker is an employee.)

---

## Common-Law Test Applied to the 1099 Portion

| Category | Indicators | Result |
|----------|-----------|--------|
| Behavioral control | Same office, same equipment, same supervisors, same procedures, same clients | Strong employee |
| Financial control | No expense risk, no other clients, no tool investment, fixed hourly rate | Strong employee |
| Type of relationship | Indefinite, integral to Acme's business, simply additional hours of normal work | Strong employee |

**Result:** The 1099 portion is identical in nature to the W-2 portion. Code H applies, and the form says not to file Form SS-8 for code H.

---

## Filing Steps

### Step 1: No SS-8 (Code H Path)

The 2025 Form 8919 says twice: "Don't file Form SS-8 if you select reason code H." Joel does not file Form SS-8. He keeps the W-2, the 1099-NEC, and records showing the 1099 hours were the same work under the same supervision.

### Step 2: Prepare Form 8919

Line numbers follow the 2025 Form 8919; re-check the 2026 revision. 2026 wage base: $184,500 (SSA).

**Line 1:**

| Column | Entry |
|--------|-------|
| (a) Firm name | Acme Studios LLC |
| (b) Federal ID number | 87-6543210 |
| (c) Reason code | H |
| (d) Date of determination or correspondence | (blank — only for codes A and C) |
| (e) Form 1099-MISC/NEC received | ☑ |
| (f) Total wages | $18,000 |

**Lines 6-13:**

| Line | Computation | Amount |
|------|-------------|--------|
| 6 | Total wages (column f) | $18,000 |
| 7 | 2026 SS wage base | $184,500 |
| 8 | Other SS wages: W-2 Box 3 + Box 7 = $60,000 + $0 (the Form 8919 wages are not included) | $60,000 |
| 9 | Line 7 − Line 8 = $184,500 − $60,000 | $124,500 |
| 10 | Smaller of Line 6 or Line 9 = MIN($18,000, $124,500) | $18,000 |
| 11 | SS tax = Line 10 × 6.2% | $1,116 |
| 12 | Medicare tax = Line 6 × 1.45% | $261 |
| 13 | Total = Line 11 + Line 12 | **$1,377** |

### Step 3: Route to Form 1040 and Schedule 2

**Form 1040, Line 1a:** $150,000 ($60,000 Joel's W-2 from Acme + $90,000 Priya's W-2)
**Form 1040, Line 1g:** $18,000 (wages from Form 8919, line 6)
**Form 1040, Line 1z:** $168,000 (total wages)

**Schedule 2, Line 6:** $1,377 (Form 8919, line 13)
**Form 1040, Line 23:** $1,377 (flows from Schedule 2 line 21)

### Step 4: Joint Return Considerations

Joel's spouse Priya has her own W-2 income of $90,000. They file jointly.

Form 8919 carries only Joel's name and SSN; Priya has no misclassified pay, so she files no Form 8919.

**Combined Medicare wages (joint):** $60,000 (Joel W-2) + $18,000 (Joel 8919) + $90,000 (Priya W-2) = $168,000.

**Additional Medicare Tax check (MFJ threshold = $250,000):** $168,000 < $250,000 → no additional Medicare tax. Form 8959 not needed.

### Step 5: File 1040 by April 15, 2027

Joint return e-filed via paid software. Joel enters the Acme 1099-NEC in the software's Form 8919 (uncollected Social Security and Medicare tax) interview, not as business income, then checks that line 13 landed on Schedule 2 line 6 and line 6 on Form 1040 line 1g.

---

## Tax Savings vs. Schedule SE Alternative

If Joel had filed Schedule SE on the $18,000:

```
Net SE earnings = $18,000 × 0.9235 = $16,623
SE tax = $16,623 × 15.3% = $2,543
Half SE tax deduction = $1,272
QBI deduction = 20% × ($18,000 − $1,272) = $3,346
```

8919 vs Schedule SE (2026 MFJ rate schedule, standard deduction $32,200, Rev. Proc. 2025-32):

| Route | Payroll / SE tax | Taxable income | Income tax | Total |
|-------|------------------|----------------|------------|-------|
| Form 8919 (code H) | $1,377 | $168,000 − $32,200 = $135,800 | $19,300 | $20,677 |
| Schedule C + SE | $2,543 | $168,000 − $1,272 − $32,200 − $3,346 = $131,182 | $18,284 | $20,827 |

**Form 8919 saves Joel $20,827 − $20,677 = $150** for 2026. At the 22% bracket, the half-SE-tax deduction and the QBI deduction on the Schedule C route cut income tax by $1,016, which offsets most of the $1,166 payroll-tax difference. The main reason to use Form 8919 here is correct reporting (the $18,000 was wages), not savings.

---

## What Joel Should Do for 2027 Going Forward

Filing Form 8919 with code H signals to Acme (when Joel discusses payroll with HR, or when Acme's CPA reviews 1099 obligations) that Acme's W-2/1099 split practice is incorrect. Joel has options:

**Option A:** Continue receiving W-2 + 1099 split, file 8919 every year. Reports the pay correctly but the practice continues.

**Option B:** Ask Acme to reclassify all his pay as W-2 going forward. Acme avoids future 8919 filings (and back-FICA exposure on past years if audited). Joel gets the convenience of single-form reporting.

**Option C:** For prior open years with the same W-2/1099 split, amend with Form 1040-X and Form 8919 (code H). Code H still means no Form SS-8. Raising the issue may draw IRS attention to Acme's broader 1099 practices; a high-stakes move worth an employment attorney's review.

Joel chooses Option B. He has a frank conversation with Acme's COO; Acme agrees to W-2 all hours starting January 2027.

---

## Lessons

1. **Code H is straightforward when the same firm issues both forms.** No SS-8; in fact the form says not to file one.
2. **W-2 wages go on line 8, the Form 8919 wages do not.** Line 8 is the other SS wages already counted; the room on line 9 caps line 10.
3. **Savings can be small.** Joel saved $150 on $18,000 of misclassified income once the half-SE-tax and QBI deductions are counted.
4. **No half-tax deduction and no QBI deduction with 8919.** Schedule SE gives the half-SE-tax deduction and Schedule C income can qualify for the QBI deduction; employee wages get neither (IRC §199A(d)(1)(B)). At higher brackets this can erase most of the payroll-tax difference.
5. **MFJ Medicare threshold matters.** Joel's joint income ($168,000) was below the $250,000 threshold; if it had been higher, Form 8959 would be required.
6. **The fix is upstream.** Filing 8919 is the worker's tactical fix. The strategic fix is convincing the firm to W-2 all the work.

---

## Sources Used in This Example

- [Form 8919](https://www.irs.gov/pub/irs-pdf/f8919.pdf) (line map and code H text from the 2025 revision)
- [SSA Contribution and Benefit Base](https://www.ssa.gov/oact/cola/cbb.html) — 2026 wage base $184,500
- Rev. Proc. 2025-32 §4.01 (2026 MFJ rate schedule), §4.14 (standard deduction $32,200 MFJ)
- IRC §199A(d)(1)(B) (employee services are not a qualified trade or business)
- [Form 8959](https://www.irs.gov/pub/irs-pdf/f8959.pdf) — Additional Medicare Tax
- IRC §3101 (employee FICA), §3121(a)(1) (SS wage base)
- IRS Pub 15-A (worker classification)
