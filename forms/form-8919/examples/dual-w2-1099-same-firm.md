# Example: Joel — Dual W-2 + 1099 from Same Firm (Code C)

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

This is **textbook code C**: same firm, same job, split between W-2 and 1099.

---

## Common-Law Test Applied to the 1099 Portion

| Category | Indicators | Result |
|----------|-----------|--------|
| Behavioral control | Same office, same equipment, same supervisors, same procedures, same clients | Strong employee |
| Financial control | No expense risk, no other clients, no tool investment, fixed hourly rate | Strong employee |
| Type of relationship | Indefinite, integral to Acme's business, simply additional hours of normal work | Strong employee |

**Result:** The 1099 portion is identical in nature to the W-2 portion. Code C applies — no SS-8 needed because the misclassification is documented by Acme's own forms.

---

## Filing Steps

### Step 1: No SS-8 Needed (Code C Path)

Code C does not require SS-8. The W-2 from the same firm is itself sufficient evidence of an employment relationship; the firm split a single job's compensation across two forms.

Joel could optionally file SS-8 anyway (defensive move), but it's not required for code C. He chooses not to file SS-8.

### Step 2: Prepare Form 8919

**Line 1, Row 1:**

| Column | Entry |
|--------|-------|
| (a) Firm name | Acme Studios LLC |
| (b) EIN | 87-6543210 |
| (c) Reason code | C |
| (d) Date of determination | (blank) |
| (e) SS-8 filed? | ☐ (unchecked — not required for code C) |
| (f) Total wages | $18,000 |

**Lines 2-11:**

| Line | Computation | Amount |
|------|-------------|--------|
| 2 | Total wages from Line 1 | $18,000 |
| 3 | 2026 SS wage base | $176,100 |
| 4 | Total SS wages (Line 2 + W-2 Box 3 + Box 7) = $18,000 + $60,000 + $0 | $78,000 |
| 5 | Line 3 − Line 4 = $176,100 − $78,000 | $98,100 |
| 6 | MIN(Line 2, Line 5) = MIN($18,000, $98,100) | $18,000 |
| 7 | SS tax = Line 6 × 6.2% | $1,116 |
| 8 | Wages subject to Medicare = Line 2 | $18,000 |
| 9 | Medicare tax = Line 8 × 1.45% | $261 |
| 10 | (Reserved) | $0 |
| 11 | Total = Line 7 + Line 9 | **$1,377** |

### Step 3: Route to Form 1040 and Schedule 2

**Form 1040, Line 1a:** $60,000 (W-2 wages from Acme)
**Form 1040, Line 1g:** $18,000 (wages from Form 8919)
**Form 1040, Line 1z:** $78,000 (total wages)

**Schedule 2, Line 5:** $1,377 (FICA from Form 8919)
**Form 1040, Line 23:** $1,377 (flows from Schedule 2)

### Step 4: Joint Return Considerations

Joel's spouse Priya has her own W-2 income of $90,000. They file jointly.

**Combined wages (joint):** $60,000 (Joel W-2) + $18,000 (Joel 8919) + $90,000 (Priya W-2) = $168,000.

**Additional Medicare Tax check (MFJ threshold = $250,000):** $168,000 < $250,000 → no additional Medicare tax. Form 8959 not needed.

### Step 5: File 1040 by April 15, 2027

Joint return e-filed via paid software (TurboTax). The 8919 entry is in the "Other income / less common situations / Form 8919" path. TurboTax auto-routes Line 11 to Schedule 2 Line 5 and Line 2 to 1040 Line 1g.

---

## Tax Savings vs. Schedule SE Alternative

If Joel had filed Schedule SE on the $18,000:

```
Net SE earnings = $18,000 × 0.9235 = $16,623
SE tax = $16,623 × 15.3% = $2,543
Half SE tax deduction = $1,272
```

8919 vs Schedule SE:

| Form | FICA / SE Tax | Half-tax Deduction | Net Tax Cost |
|------|---------------|---------------------|--------------|
| Form 8919 (code C) | $1,377 | $0 (no deduction available for FICA) | $1,377 |
| Schedule SE | $2,543 | $1,272 (reduces income tax by ~$280 at 22% bracket) | $2,543 − $280 = $2,263 |

**Form 8919 saves Joel: $2,263 − $1,377 = $886** in net tax for 2026.

---

## What Joel Should Do for 2027 Going Forward

Filing Form 8919 with code C signals to Acme (when Joel discusses payroll with HR, or when Acme's CPA reviews 1099 obligations) that Acme's W-2/1099 split practice is incorrect. Joel has options:

**Option A:** Continue receiving W-2 + 1099 split, file 8919 every year. Saves money but the practice continues.

**Option B:** Ask Acme to reclassify all his pay as W-2 going forward. Acme avoids future 8919 filings (and back-FICA exposure on past years if audited). Joel gets the convenience of single-form reporting.

**Option C:** File SS-8 for prior years to formally establish the misclassification. This may trigger an IRS audit of Acme's broader 1099 practices. High-stakes move; consult employment attorney.

Joel chooses Option B. He has a frank conversation with Acme's COO; Acme agrees to W-2 all hours starting January 2027.

---

## Lessons

1. **Code C is straightforward when same firm issues both forms.** No SS-8 needed.
2. **W-2 wages count toward the SS wage base on Line 4.** Without the wage base check, SS tax could be overpaid if total wages exceed the cap.
3. **8919 saves money even at small wage amounts.** Joel saved $886 on $18,000 of misclassified income — about 5% of the misclassified amount.
4. **No half-tax deduction with 8919.** Schedule SE has the half-SE-tax deduction; 8919 does not (because there's no employer share to credit). This narrows but doesn't eliminate the savings.
5. **MFJ Medicare threshold matters.** Joel's joint income ($168,000) was below the $250,000 threshold; if it had been higher, Form 8959 would be required.
6. **The fix is upstream.** Filing 8919 is the worker's tactical fix. The strategic fix is convincing the firm to W-2 all the work.

---

## Sources Used in This Example

- [Form 8919 (2026 revision)](https://www.irs.gov/pub/irs-pdf/f8919.pdf)
- [Form 8959](https://www.irs.gov/pub/irs-pdf/f8959.pdf) — Additional Medicare Tax
- IRC §3101 (employee FICA), §3121(a)(1) (SS wage base)
- IRS Pub 15-A (worker classification)
