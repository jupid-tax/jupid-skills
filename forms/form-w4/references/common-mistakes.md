# Top 10 W-4 Mistakes

The IRS estimates roughly 20% of W-4s are filled out incorrectly enough to cause a tax-time surprise (refund > $2,000 or balance due > $1,000). These are the most common mistakes the agent should watch for.

## 1. Never updating after a life change

**Mistake:** User completed W-4 at hire 5 years ago. Since then they got married, had two kids, and their spouse started working. The W-4 still says "Single, no dependents."

**Impact:** Wildly under- or over-withheld depending on direction of the life changes. Common to be off by $5,000+ annually.

**Fix:** Submit a new W-4 within 30 days of any life event. Set a calendar reminder for January 15 each year to verify the W-4 still matches the current household.

**Trigger events for a new W-4:**
- Marriage, divorce, legal separation
- Birth or adoption of a child
- Child turning 17 (loses CTC, drops to $500 ODC)
- Spouse starts or stops working
- Take a second job
- Side gig over $1,000/year starts
- Significant raise (changes which bracket the household sits in)
- Buy a house (potential Schedule A itemizing)

**Citation:** IRC §3402(f)(2) — employee must provide accurate W-4 information.

---

## 2. Both spouses claim dependents on Step 3

**Mistake:** Marcus claims $4,000 (2 kids × $2,000) on his W-4 Step 3. Jenna also claims $4,000 on hers. Combined household withholding is reduced by $8,000, but only $4,000 of CTC actually exists.

**Impact:** Under-withholding by $4,000 → tax bill plus underpayment penalty (~4-8% annualized).

**Fix:** Only the highest-paying spouse claims dependents on Step 3. The other spouse leaves Step 3 blank. The form instructions are explicit: "If your total income will be ≤ $400,000 (MFJ)…"

**Citation:** Form W-4 Instructions, Step 3 ("If your total income will be…"). IRC §24(a) — CTC is per child, not per parent.

---

## 3. Forgetting Step 2 in multi-job households

**Mistake:** User has two jobs at $40K each. Each W-4 claims "Single, no other income." Each employer withholds as if $40K is the only income.

**Impact:** $40K + $40K = $80K combined, taxed in higher brackets than $40K. Without Step 2, under-withheld by $2,000-$3,500.

**Fix:** Use Step 2 method (a) IRS Tax Withholding Estimator (recommended), (b) Multiple Jobs Worksheet, or (c) Step 2(c) box if jobs pay similarly. Apply result to Step 4(c) of the higher-paying job's W-4.

**Citation:** IRC §3402(f)(2)(A) — withholding must reflect "actual withholding allowance" given household structure. See [`multi-job.md`](./multi-job.md).

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

## 5. Side-gig income missing from Step 4(a)

**Mistake:** User has a $20,000/year side gig but doesn't mention it on the W-4. Employer only withholds based on the W-2 wage.

**Impact:** Federal income tax on $20K (~$2,400-$5,000) plus 15.3% SE tax (~$2,826) goes uncollected → $5,000-$8,000 tax bill plus underpayment penalty.

**Fix:** Either enter the $20K on Step 4(a) AND add a Step 4(c) amount for SE tax, OR set up quarterly Form 1040-ES payments. See [`side-income.md`](./side-income.md).

**Citation:** IRC §6654 — estimated tax payment requirement. IRC §1401 — self-employment tax.

---

## 6. Inflating Step 3 to get a bigger paycheck

**Mistake:** User wants more cash now so they enter $10,000 on Step 3 even though they have no children.

**Impact:**
- Tax bill in April plus underpayment penalty
- IRS can require employer to apply "lock-in letter" — highest withholding rate (single, no adjustments) — for the rest of the year, possibly into next year
- For egregious cases, civil penalty under IRC §6682 ($500 per false W-4 statement) or fraud referral

**Fix:** Don't fabricate dependents. If withholding is too high relative to income, lower Step 4(c), claim only LEGITIMATE Step 3 amounts, ensure filing status is correct.

**Citation:** IRC §3402(f)(2)(B) — accuracy required. IRC §6682 — civil penalty for false withholding statement.

---

## 7. Claiming Head of Household when not eligible

**Mistake:** A married user claims HoH on Step 1(c) because it has a higher standard deduction. Or a single user claims HoH without a qualifying person.

**Impact:** Tax return gets reclassified to correct status (Single or MFS), often years later via CP2000 notice. Tax bill plus interest and penalties.

**Fix:** HoH requires ALL THREE:
1. Unmarried (or "considered unmarried" — separated 6+ months)
2. Paid more than half the cost of keeping up a home
3. Qualifying person (usually a child or dependent parent) lived with you more than half the year

**Citation:** IRC §2(b) — HoH definition. Pub 501 has worked examples.

---

## 8. Not signing Step 5

**Mistake:** User completes all five steps but forgets to sign Step 5.

**Impact:** Form is INVALID. Employer must withhold at the highest rate (single, no adjustments, no dependents) per IRC §3402(f)(2)(B).

**Fix:** Always sign and date. For electronic submission, click through the e-signature flow.

**Citation:** IRC §3402(f)(2)(B); Treas. Reg. §31.3402(f)(5)-1.

---

## 9. Not coordinating W-4 with state withholding

**Mistake:** User submits a federal W-4 with new dependent claims but forgets to update the state withholding form (CA DE-4, NY IT-2104, etc.).

**Impact:** State withholding stays at the old levels, so federal vs state withholding diverges. Could result in a state tax bill or refund.

**Fix:** When updating the federal W-4, also update the state form. Many payroll platforms (Workday, Gusto) prompt for both at the same time. Paper requires two separate forms.

**Citation:** State-specific (CA Rev. & Tax. Code §§13020-13088, NY Tax Law §671, etc.)

---

## 10. Setting Step 4(c) too high "for safety"

**Mistake:** User wants to "definitely not owe taxes" so they enter $300/pay-period on Step 4(c) on top of normal withholding. Adds $7,800 of withholding annually.

**Impact:** Massive over-withholding. Get a $5,000+ refund in April. That's $5,000 of cash flow loaned to the IRS at 0% interest for up to 16 months. Not a "savings" — an opportunity cost.

**Fix:** Set Step 4(c) to the precise amount needed (from Estimator or Worksheet). If you want a slight buffer, add $20-50/check, not $200-300. If you want forced savings, use a savings account, not the IRS.

**Citation:** Behavioral, not legal. But see Pub 505 ("Don't have too much withheld").

---

## Bonus: Mistakes specific to certain life events

### Newly married

- Both new to MFJ; both should use Step 2 method
- Coordinate Step 3 — only one W-4 carries dependents
- Filing status changes mid-year — submit new W-4 with updated 1(c) ASAP

### Newly divorced

- Filing status: Single (or HoH if qualifying person lives with you >half year)
- Coordinate dependent claims with ex-spouse (Form 8332 if non-custodial parent claims)
- Update beneficiary designations and W-4 within 30 days of the divorce decree

### New baby

- Newborn = qualifying child for full year if born by Dec 31
- SSN must be obtained — apply at the hospital or ASAP after birth
- Add $2,000 to Step 3 on next paycheck (not the next year)

### Child turns 17

- Lose CTC for that child → reduce Step 3 by $2,000
- May still qualify for $500 ODC → add $500 to Step 3 (net change: -$1,500)
- Update W-4 in January of the year the child will turn 17

### Spouse starts working (MFJ)

- Both jobs need Step 2 coordination
- Run Estimator to compute new Step 4(c) on higher-paying job
- Lower-paying spouse files W-4 with only Steps 1 + 5

### Big bonus / equity vest

- Bonuses use 22% supplemental rate for amounts ≤ $1M (38.6% above $1M)
- For taxpayers in 22% bracket, supplemental rate matches → no adjustment needed
- For taxpayers in 24%+ bracket, supplemental rate under-withholds → add Step 4(c) to bridge the gap, OR pay extra via 1040-ES
- For RSU vests with single-trigger withholding, often the default 22% under-withholds dramatically — talk to a CPA
