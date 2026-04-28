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

Ana mails Form SS-8 to:

```
Department of the Treasury
Internal Revenue Service
Stop 631
Holtsville, NY 11742-0631
```

**Enclosures:**
- Completed Form SS-8 (8 pages)
- Copy of 1099-NEC for 2026 from ABC ($72,000)
- Copy of her engagement letter from March 2025
- 6 selected emails showing ABC assigning specific tasks with deadlines
- Copy of ABC's "team handbook" she received during training
- Cover letter noting she will file Form 8919 with code G on her 2026 1040

**Mail method:** USPS Certified Mail with Return Receipt. She gets the green card back stamped with February 18, 2027.

### Step 2: Prepare Form 8919 for 2026 1040

**Line 1, Row 1:**

| Column | Entry |
|--------|-------|
| (a) Firm name | ABC Consulting LLC |
| (b) EIN | 12-3456789 |
| (c) Reason code | G |
| (d) Date of determination | (blank — pending) |
| (e) SS-8 filed? | ☑ |
| (f) Total wages | $72,000 |

**Lines 2-11:**

Assuming 2026 SS wage base = $176,100 (verify with SSA when filing):

| Line | Computation | Amount |
|------|-------------|--------|
| 2 | Total wages (sum of column f) | $72,000 |
| 3 | 2026 SS wage base | $176,100 |
| 4 | Total SS wages (Line 2 + W-2 Box 3 + W-2 Box 7); Ana has no W-2 | $72,000 |
| 5 | Line 3 − Line 4 | $104,100 |
| 6 | MIN(Line 2, Line 5) | $72,000 |
| 7 | SS tax = Line 6 × 6.2% | $4,464 |
| 8 | Wages subject to Medicare = Line 2 | $72,000 |
| 9 | Medicare tax = Line 8 × 1.45% | $1,044 |
| 10 | (Reserved or Form 8959 reference) | $0 (Ana is below $200,000 single threshold) |
| 11 | Total = Line 7 + Line 9 | **$5,508** |

### Step 3: Route to Form 1040 and Schedule 2

**Form 1040, Line 1g:** $72,000 (wages from Form 8919, Line 2)

**Schedule 2, Line 5:** $5,508 (FICA from Form 8919, Line 11)

**Form 1040, Line 23:** flows from Schedule 2 total = $5,508

### Step 4: Complete Rest of Form 1040

Ana has no W-2, no other income. Her 1040:

| Line | Description | Amount |
|------|-------------|--------|
| 1a | W-2 wages | $0 |
| 1g | Wages from Form 8919 | $72,000 |
| 1z | Total wages (sum 1a-1h) | $72,000 |
| 9 | Total income | $72,000 |
| 10 | Adjustments (none — Ana doesn't deduct half SE tax because she didn't pay SE tax) | $0 |
| 11 | AGI | $72,000 |
| 12 | Standard deduction (single, 2026) | $15,700 (verify 2026 figure) |
| 15 | Taxable income | $56,300 |
| 16 | Income tax (2026 brackets, single) | ~$7,500 (rough estimate; verify with current brackets) |
| 23 | Other taxes (from Schedule 2, includes 8919 FICA) | $5,508 |
| 24 | Total tax | $13,008 |

### Step 5: File 1040 by April 15, 2027

E-file via FFFF (Ana's situation is simple enough; AGI well under the IRS Free File threshold).

---

## Tax Savings vs. Schedule SE Alternative

If Ana had instead filed Schedule SE on the same $72,000:

```
Net SE earnings = $72,000 × 0.9235 = $66,492
SE tax = $66,492 × 15.3% = $10,173
Half SE tax deduction (Schedule 1 Line 15) = $5,086
```

Ana's 1040 with Schedule SE:

| Line | Amount |
|------|--------|
| Total income | $72,000 |
| Half SE tax deduction | -$5,086 |
| AGI | $66,914 |
| Standard deduction | -$15,700 |
| Taxable income | $51,214 |
| Income tax (rough) | ~$6,400 |
| SE tax (Line 23) | $10,173 |
| **Total tax** | **~$16,573** |

**Form 8919 saves Ana ~$3,565** in 2026 ($16,573 − $13,008). Across multiple years of misclassification, this compounds.

---

## What Happens Next

### IRS Sends SS-8 to ABC Consulting (March 2027)

The IRS mails a copy of Ana's SS-8 to ABC with a 30-day response window. ABC may:

- Acknowledge the misclassification (rare)
- Argue Ana was a contractor (most common — ABC will likely dispute)
- Not respond (the IRS proceeds with Ana's facts only)

Ana's relationship with ABC may be strained — ABC will know she filed. Many workers in Ana's situation file SS-8 only after the engagement ends.

### IRS Determination (Summer 2027 - early 2028)

After 6-12 months, the IRS issues a determination letter to both Ana and ABC. Three outcomes:

**Outcome 1: Favorable (Ana = employee).** Ana's 8919 filing stands. She can amend prior years (2024 and 2025 if also misclassified) within the 3-year statute. ABC may face back-FICA exposure (or may qualify for Section 530 relief).

**Outcome 2: Adverse (Ana = contractor).** Ana must amend her 2026 1040, replacing 8919 with Schedule SE. Owes ~$3,565 additional tax + interest from April 15, 2027. Likely no penalty (good-faith filing).

**Outcome 3: No determination.** Rare. Ana's filing stands by default but is not bulletproof against future audit.

---

## Documentation Ana Retains

- Copy of Form SS-8 mailed February 2027
- Certified mail receipt and green card
- Copies of all 1099-NECs from ABC (2025, 2026)
- Engagement letter
- 6 emails showing ABC's direction
- Team handbook
- Time logs (Ana kept her own time tracker even though ABC didn't require one)
- Performance review email from December 2026

Retention: 3 years from filing the 2026 1040 = until April 2030 minimum. Ana keeps for 7 years to be safe.

---

## Lessons

1. **The common-law test was clear.** Three of three categories pointed to employee. Ana's 8919 case is strong.
2. **No W-2 means full wage base available for SS.** Line 5 had $104,100 of room; full $72,000 fit under the SS cap.
3. **No double-counting.** Ana doesn't put the $72,000 on Schedule C. It's only on Form 8919 + Form 1040 Line 1g.
4. **SS-8 first, then 8919.** Ana mailed SS-8 in February before filing the 1040 in April. The certified mail receipt is her proof.
5. **Tax savings = $3,565 for 2026.** Compounded across 2 years of misclassification, ~$7,100 saved.
6. **Documentation is everything.** Without the engagement letter and the 6 emails, Ana's case would be weaker. With them, the IRS has a clear factual record.

---

## Sources Used in This Example

- [Form 8919 (2026 revision)](https://www.irs.gov/pub/irs-pdf/f8919.pdf)
- [Form SS-8](https://www.irs.gov/pub/irs-pdf/fss8.pdf)
- [IRS Publication 15-A](https://www.irs.gov/pub/irs-pdf/p15a.pdf) — Common-law test
- IRC §3101 (employee FICA), §3121(d) (employee definition)
- Rev. Rul. 87-41 (20-factor test, refined into Pub 15-A)
