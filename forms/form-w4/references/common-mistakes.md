# Top 10 W-4 Mistakes

The most common W-4 mistakes the agent should watch for. Rules verified 2026-10-06 against the 2026 Form W-4, Pub. 15 (2026), Pub. 15-T (2026) and Pub. 505 (2026).

## 1. Never updating after a life change

**Mistake:** User completed W-4 at hire 5 years ago. Since then they got married, had two kids, and their spouse started working. The W-4 still says "Single, no dependents."

**Impact:** Wildly under- or over-withheld depending on direction of the life changes. Common to be off by $5,000+ annually.

**Fix:** Submit a new W-4 when the household changes. It is required within 10 days when a change reduces the withholding the user is entitled to (e.g., filing status changes from MFJ to Single, an expected Child Tax Credit is lost, credits drop by more than $500, deductions drop by more than $2,300) (Pub. 505 (2026), chapter 1). Recheck with the Estimator at the start of each year (2026 Form W-4, page 1 TIP).

**Trigger events for a new W-4:**
- Marriage, divorce, legal separation
- Birth or adoption of a child
- Child turning 17 (loses CTC, drops to $500 ODC)
- Spouse starts or stops working
- Take a second job
- Side gig over $1,000/year starts
- Significant raise (changes which bracket the household sits in)
- Buy a house (potential Schedule A itemizing)

**Citation:** IRC §3402(f)(2) (furnishing a new certificate after a change in status); Pub. 505 (2026), chapter 1.

---

## 2. Both spouses claim dependents on Step 3

**Mistake:** Marcus claims $4,400 (2 kids × $2,200) on his W-4 Step 3. Jenna also claims $4,400 on hers. Combined household withholding is reduced by $8,800, but only $4,400 of CTC actually exists.

**Impact:** Under-withholding by $4,400 → tax bill plus underpayment penalty (interest at the IRC §6621 underpayment rate on each late installment).

**Fix:** Only one W-4 carries Step 3 — the highest-paying job's for best accuracy. The other spouse leaves Step 3 blank. The form is explicit: "Complete Steps 3–4(b) on Form W-4 for only ONE of these jobs."

**Citation:** 2026 Form W-4, Step 2 note and page 2 "Multiple jobs" caution. IRC §24(a) — CTC is per child, not per parent.

---

## 3. Forgetting Step 2 in multi-job households

**Mistake:** User has two jobs at $40K each. Each W-4 claims "Single, no other income." Each employer withholds as if $40K is the only income.

**Impact:** $40K + $40K = $80K combined, taxed in higher brackets than $40K. Pub. 15-T (2026) withholding on each job: $2,620, total $5,240; 2026 tax on $80,000 single (taxable $63,900): $8,770. Under-withheld by about $3,530. The 2026 Single table (page 5, row $40,000–59,999, column $40,000–49,999) calls for $6,080 of extra withholding because it uses $10,000 bands.

**Fix:** Use Step 2 option (a) IRS Tax Withholding Estimator (most accurate), (b) Multiple Jobs Worksheet → Step 4(c) of the highest-paying job's W-4, or (c) the Step 2(c) box on both W-4s (two equal jobs: the form says (c) is generally more accurate than (b) when the lower pay is more than half the higher pay).

**Citation:** 2026 Form W-4, Step 2 and page 2. See [`multi-job.md`](./multi-job.md).

---

## 4. Confusing W-4 with W-9

**Mistake:** Freelancer gets onboarded by a new client and is sent a W-4. Or W-2 employee mistakenly fills out a W-9 thinking it's the new-hire form.

**Impact:**
- W-4 from a contractor → client misclassifies them as an employee, withholds taxes incorrectly, generates wrong year-end form
- W-9 from an employee → no taxes withheld all year, huge surprise at filing

**Fix:** Verify classification before filling out:
- W-2 employee → W-4
- 1099 contractor → W-9
- Question to ask: "Will you be withholding income tax, Social Security, and Medicare from my pay?" Yes = employee. No = contractor.

**Citation:** IRS Form W-9 Instructions; common-law employee tests in IRC §3121(d) and Rev. Rul. 87-41.

---

## 5. Side-gig income left out of withholding (or put on Step 4(a))

**Mistake:** User has a $20,000/year side gig and neither adjusts the W-4 nor pays estimated tax. Or the user enters the side-gig profit on Step 4(a), which the 2026 form says not to do ("You shouldn't include income from any jobs or self-employment").

**Impact:** Federal income tax on $20K (roughly $2,400 at 12% to $4,800 at 24%) plus SE tax ($20,000 × 0.9235 × 15.3% = $2,826) goes uncollected → a tax bill plus underpayment penalty. Step 4(a) would at best cover the income tax, never the SE tax.

**Fix:** Either use the IRS Tax Withholding Estimator (the form's instruction for self-employment income) and enter its result in Step 4(c), OR set up quarterly Form 1040-ES payments. See [`side-income.md`](./side-income.md).

**Citation:** IRC §6654 — estimated tax payment requirement. IRC §1401 — self-employment tax.

---

## 6. Inflating Step 3 to get a bigger paycheck

**Mistake:** User wants more cash now so they enter $10,000 on Step 3 even though they have no children.

**Impact:**
- Tax bill in April plus underpayment penalty
- IRS can issue a "lock-in letter" that tells the employer which filing status and maximum withholding to use; the employer must follow it until the IRS releases it (Pub. 15 (2026), section 9; Pub. 505 (2026), chapter 1)
- Civil penalty of $500 for a W-4 statement with no reasonable basis that decreases withholding (IRC §6682), plus possible criminal penalties

**Fix:** Don't fabricate dependents. If withholding is too high relative to income, lower Step 4(c), claim only LEGITIMATE Step 3 amounts, ensure filing status is correct.

**Citation:** Form W-4 jurat (signed under penalties of perjury). IRC §6682 — civil penalty for false withholding statement.

---

## 7. Claiming Head of Household when not eligible

**Mistake:** A married user claims HoH on Step 1(c) because it has a higher standard deduction. Or a single user claims HoH without a qualifying person.

**Impact:** On examination the return is moved to the correct status (Single or MFS). Tax bill plus interest and penalties.

**Fix:** HoH requires ALL THREE:
1. Unmarried (or "considered unmarried" — separated 6+ months)
2. Paid more than half the cost of keeping up a home
3. Qualifying person (usually a child or dependent parent) lived with you more than half the year

**Citation:** IRC §2(b) — HoH definition. Pub 501 has worked examples.

---

## 8. Not signing Step 5

**Mistake:** User completes all five steps but forgets to sign Step 5.

**Impact:** "This form is not valid unless you sign it" (2026 Form W-4, Step 5). The employer keeps using the employee's earlier valid W-4; if there is none, it withholds as if the employee checked Single or Married filing separately with no entries in Steps 2, 3, or 4 (Pub. 15 (2026), section 9).

**Fix:** Always sign and date. For electronic submission, click through the e-signature flow (the employer's electronic system must meet Treas. Reg. §31.3402(f)(5)-1(c)).

**Citation:** 2026 Form W-4, Step 5; Pub. 15 (2026), section 9; Treas. Reg. §31.3402(f)(5)-1.

---

## 9. Not coordinating W-4 with state withholding

**Mistake:** User submits a federal W-4 with new dependent claims but forgets to update the state withholding form (CA DE-4, NY IT-2104, etc.).

**Impact:** State withholding stays at the old levels, so federal vs state withholding diverges. Could result in a state tax bill or refund.

**Fix:** When updating the federal W-4, also update the state form. Many payroll platforms (Workday, Gusto) prompt for both at the same time. Paper requires two separate forms.

**Citation:** State-specific; check the state revenue agency's withholding form instructions (e.g., California Form DE 4, New York Form IT-2104).

---

## 10. Setting Step 4(c) too high "for safety"

**Mistake:** User wants to "definitely not owe taxes" so they enter $300/pay-period on Step 4(c) on top of normal withholding. Adds $7,800 of withholding annually.

**Impact:** Massive over-withholding. Get a $5,000+ refund in April. That's $5,000 of cash flow loaned to the IRS at 0% interest for up to 16 months. Not a "savings" — an opportunity cost.

**Fix:** Set Step 4(c) to the precise amount needed (from Estimator or Worksheet). If you want a slight buffer, add $20-50/check, not $200-300. If you want forced savings, use a savings account, not the IRS.

**Citation:** Behavioral, not legal. Pub. 505 (2026), chapter 1: "If too much tax is withheld, you will lose the use of that money until you get your refund."

---

## Bonus: Mistakes specific to certain life events

### Newly married

- Both new to MFJ; both should use Step 2 method
- Coordinate Step 3 — only one W-4 carries dependents
- Filing status changes mid-year — submit new W-4 with updated 1(c) ASAP

### Newly divorced

- Filing status: Single (or HoH if qualifying person lives with you >half year)
- Coordinate dependent claims with ex-spouse (Form 8332 if non-custodial parent claims)
- Filing status change from MFJ to Single or HoH: new W-4 within 10 days if withholding for the rest of the year would fall short; if it only affects next year, a new W-4 by December 1 (Pub. 505 (2026), chapter 1). Update beneficiary designations too

### New baby

- A child born during the year is treated as living with you more than half the year if your home was the child's home for more than half the time the child was alive (Pub. 501)
- SSN valid for employment must be obtained by the return due date — apply at the hospital or ASAP after birth
- Add $2,200 to Step 3 on a new W-4 now (not next year)

### Child turns 17

- Lose CTC for that child → reduce Step 3 by $2,200
- May still qualify for $500 ODC → add $500 to Step 3 (net change: -$1,700)
- Update W-4 in January of the year the child will turn 17 (losing an expected CTC triggers the 10-day rule in Pub. 505 (2026), chapter 1)

### Spouse starts working (MFJ)

- Both jobs need Step 2 coordination
- Run Estimator to compute new Step 4(c) on higher-paying job
- Lower-paying spouse files W-4 with Steps 2 through 4(b) blank (or Step 2(c) checked if both W-4s use the checkbox)

### Big bonus / equity vest

- Bonuses can be withheld at the 22% optional flat rate; supplemental wages over $1 million in the year are withheld at a mandatory 37% (Pub. 15 (2026), section 7)
- For taxpayers in 22% bracket, supplemental rate matches → no adjustment needed
- For taxpayers in 24%+ bracket, supplemental rate under-withholds → add Step 4(c) to bridge the gap, OR pay extra via 1040-ES
- For RSU vests withheld at the 22% flat rate, high earners often end up under-withheld — refer large equity situations to a CPA
