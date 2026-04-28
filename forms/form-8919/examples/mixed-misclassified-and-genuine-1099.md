# Example: Maya — Mixed Misclassified + Genuine Self-Employment (Code G + Schedule C)

End-to-end worked filing for the most complex misclassification scenario: a worker with both 8919-eligible misclassified income and legitimate Schedule C self-employment income in the same year.

---

## Persona

**Maya Garcia**, age 29, lives in Brooklyn, NY. Files single. SSN: 345-67-8901.

**Engagement:** Maya has two distinct income streams in 2026.

### Stream 1: Misclassified Employee (8919-Eligible)

**Firm:** Northstar Marketing LLC (EIN: 11-2345678)

**Compensation:** $54,000 in 2026, reported on 1099-NEC Box 1.

**Work pattern:**
- 30 hours/week, set schedule (Tuesday through Friday, 10 AM-6 PM)
- Northstar's office in Brooklyn (Maya commutes)
- Northstar provides her workstation, Adobe Creative Cloud subscription, and a cell phone
- Reports to Northstar's Creative Director who assigns and reviews work
- Maya's email signature: "Maya Garcia, Designer, Northstar Marketing"
- Indefinite engagement, started January 2025
- No benefits

### Stream 2: Genuine Freelance (Schedule C)

**Multiple clients:** Maya runs an Etsy shop selling custom illustrations and takes occasional freelance projects from a separate client (Riverside Books).

**Compensation:** $11,000 from Etsy + $4,500 from Riverside Books = $15,500 in 2026.

**Work pattern:**
- Maya works on Etsy and Riverside projects on Mondays, weekends, and evenings
- Uses her own iPad Pro and Apple Pencil
- Sets her own hours, prices, and creative direction
- Riverside paid via 1099-NEC ($4,500)
- Etsy reported via 1099-K (gross sales $11,000)
- Maya keeps separate Etsy bank account for the freelance income
- Has business cards and an Instagram portfolio

**Common-law test on Riverside Books:** Maya sets prices, picks projects she wants, uses her own equipment, has Etsy as another client. **Genuinely self-employed.**

---

## Common-Law Test Result on Northstar (8919-Eligible)

| Category | Indicators | Result |
|----------|-----------|--------|
| Behavioral control | Set hours, set location, Northstar's tools, Creative Director directs work | Strong employee |
| Financial control | No expense risk, fixed pay, equipment provided | Strong employee |
| Type of relationship | Indefinite, integral to Northstar's design work, has the title "Designer" on her email | Strong employee |

**Result:** Northstar income is 8919-eligible. Etsy + Riverside income is Schedule C.

---

## The Critical Distinction

The agent must keep these two streams **completely separate** on the return:

| Income | Form Used | Tax Treatment |
|--------|-----------|---------------|
| Northstar $54,000 | Form 8919 | 7.65% FICA → Schedule 2 Line 5; wage on 1040 Line 1g |
| Etsy $11,000 + Riverside $4,500 = $15,500 | Schedule C → Schedule SE | 15.3% SE tax × 92.35%; net profit on Schedule 1 Line 3 |

**Common pitfall:** putting all $69,500 on either Schedule C or Form 8919. Both are wrong. The streams must be split based on classification.

---

## Filing Steps

### Step 1: File Form SS-8 for Northstar (February 2027)

Maya files SS-8 for Northstar only. Etsy and Riverside are obviously self-employment; she does not file SS-8 for them.

Mail to Holtsville, NY. Certified mail with return receipt.

### Step 2: Prepare Form 8919

**Line 1, Row 1:**

| Column | Entry |
|--------|-------|
| (a) Firm name | Northstar Marketing LLC |
| (b) EIN | 11-2345678 |
| (c) Reason code | G |
| (d) Date of determination | (blank) |
| (e) SS-8 filed? | ☑ |
| (f) Total wages | $54,000 |

**Lines 2-11:**

| Line | Computation | Amount |
|------|-------------|--------|
| 2 | Total wages | $54,000 |
| 3 | 2026 SS wage base | $176,100 |
| 4 | Total SS wages = Line 2 + W-2 Box 3; Maya has no W-2 | $54,000 |
| 5 | Line 3 − Line 4 | $122,100 |
| 6 | MIN(Line 2, Line 5) | $54,000 |
| 7 | SS tax = Line 6 × 6.2% | $3,348 |
| 8 | Wages subject to Medicare | $54,000 |
| 9 | Medicare tax = Line 8 × 1.45% | $783 |
| 10 | (Reserved) | $0 |
| 11 | Total | **$4,131** |

### Step 3: Prepare Schedule C (Etsy + Riverside)

**Schedule C, Line 1:** Gross receipts = $11,000 (Etsy) + $4,500 (Riverside) = $15,500

**Maya's expenses related to Etsy + Riverside only:**

| Schedule C Line | Description | Amount |
|-----------------|-------------|--------|
| 18 (Office expense) | Etsy listing fees, shipping supplies | $400 |
| 22 (Supplies) | Drawing supplies, paper, ink | $620 |
| 27a (Other expenses) | Apple Pencil ($129), Procreate license ($12.99/year, prorated), Etsy seller transaction fees | $850 |
| **Line 28 total** |  | **$1,870** |

(Maya does NOT deduct her commute to Northstar — that's misclassified-employee work, not on Schedule C. Her home office for Etsy work is too small to qualify for Line 30.)

**Line 31 (Net profit):** $15,500 − $1,870 = $13,630

### Step 4: Prepare Schedule SE (on the Schedule C income only)

**Line 1b (from Schedule C Line 31):** $13,630

**Line 4 (×0.9235):** $13,630 × 0.9235 = $12,587

**Line 5 (×15.3%):** $12,587 × 0.153 = $1,926

**Line 6 (half SE tax deduction):** $1,926 / 2 = $963

### Step 5: Combine on Form 1040

| Line | Description | Amount |
|------|-------------|--------|
| 1a | W-2 wages | $0 |
| 1g | Wages from Form 8919 | $54,000 |
| 1z | Total wages | $54,000 |
| 8 | Other income (Schedule 1) | $13,630 (Schedule C net profit, flows from Schedule 1 Line 3) |
| 9 | Total income | $67,630 |
| 10 | Adjustments (Schedule 1 includes half SE tax deduction) | $963 |
| 11 | AGI | $66,667 |
| 12 | Standard deduction (single, 2026) | $15,700 |
| 15 | Taxable income | $50,967 |
| 16 | Income tax (rough) | ~$6,300 |
| 23 | Other taxes (Schedule 2: $4,131 from 8919 + $1,926 from Schedule SE) | $6,057 |
| 24 | Total tax | ~$12,357 |

### Step 6: File 1040 by April 15, 2027

Maya uses paid software because the mixed 8919 + Schedule C scenario benefits from guided interview. She enters:

1. Northstar 1099-NEC under "Form 8919" path (NOT under Schedule C)
2. Riverside 1099-NEC under "Schedule C / freelance income"
3. Etsy 1099-K under "Schedule C / Etsy"

She manually verifies the software did NOT auto-populate Northstar onto Schedule C.

---

## What If Maya Got It Wrong?

### Wrong Way 1: All on Schedule C

If Maya put all $69,500 ($54,000 + $15,500) on Schedule C:

- Schedule C net profit: $69,500 − $1,870 (her freelance expenses) = $67,630
  - But she'd also fail to deduct legitimate expenses related to commuting and Northstar work because those wouldn't apply to her freelance business
- Schedule SE: $67,630 × 0.9235 × 15.3% = $9,558 SE tax
- Compare to actual: $4,131 (8919 FICA) + $1,926 (SE on $13,630) = $6,057

**Loss from putting it all on Schedule C: $9,558 − $6,057 = $3,501 in extra tax.**

### Wrong Way 2: All on Form 8919

If Maya put all $69,500 on Form 8919 (claiming all of it was misclassified):

- This is fraudulent — Etsy and Riverside are clearly self-employment
- IRS audit would reclassify the Etsy/Riverside portion as SE income, assess tax + interest + accuracy penalty (20%) under IRC §6662
- Potential criminal exposure if intentional under IRC §7201

**The right way is to split the streams.** Form 8919 for genuinely misclassified income only.

---

## Tax Savings vs. All-Schedule-SE Alternative

If Maya had put all $69,500 on Schedule C/SE (Wrong Way 1):

- SE tax: $9,558
- Half SE tax deduction: $4,779
- Net tax cost: ~$8,500 (after income-tax savings from the deduction)

Maya's actual filing:

- 8919 FICA: $4,131
- Schedule SE on $13,630: $1,926
- Half SE tax deduction (only on Schedule C portion): $963
- Net tax cost: ~$5,094

**Savings from correct treatment: ~$3,400 for 2026.**

---

## Lessons

1. **Streams must be separated.** Misclassified-employee income on 8919; genuine SE income on Schedule C. Never both, never the wrong one.
2. **Separate the expense allocation too.** Schedule C expenses only relate to Schedule C income. Maya can't deduct iPad costs against Northstar wages on 8919 — wages aren't netted.
3. **SS-8 only for the misclassified firm.** No need to file SS-8 for genuinely self-employed engagements.
4. **The half-SE-tax deduction only applies to the Schedule SE portion.** No half-FICA deduction for 8919 income.
5. **Software can mis-route 1099s.** When using paid tax software, manually verify each 1099-NEC ended up on the right form (8919 vs. Schedule C).
6. **The IRS sees both filings.** On the same return, the IRS sees Maya filed both 8919 and Schedule C. This is the right answer; mixed scenarios are common and expected.

---

## Sources Used in This Example

- [Form 8919](https://www.irs.gov/pub/irs-pdf/f8919.pdf)
- [Schedule C (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sc.pdf)
- [Schedule SE (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf)
- [Form SS-8](https://www.irs.gov/pub/irs-pdf/fss8.pdf)
- IRS Pub 15-A (common-law test)
- IRC §3101 (employee FICA), §1401 (SE tax)
- IRC §61 (gross income — counted once)
- IRC §6662 (accuracy penalty)
