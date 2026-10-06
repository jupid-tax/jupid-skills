# Common Form 1099-Q Mistakes (with Citations)

The audit-trip mistakes filers make when handling 529 / Coverdell distributions, with the IRC, Pub 970, or form authority showing why each is wrong.

---

## 1. Not reporting a 1099-Q at all because the distribution was used for tuition

**The mistake**: user assumes "fully qualified means I don't need to do anything."

**Why it matters**: the IRS receives the 1099-Q from the trustee and matches it against the user's return. If no return entry corresponds, the IRS may issue a CP2000 notice 12-18 months after filing, proposing additional tax on the *full* earnings portion plus 10% additional tax plus penalties + interest.

**Correct approach**: even when the distribution is fully qualified (taxable amount = $0), the user retains the 1099-Q, the QHEE documentation, and the worksheet for at least 3 years (IRC §6501). This is the audit defense if the IRS asks. The return itself shows nothing for fully qualified distributions, but the user has the paper trail.

**Authority**: IRC §6501 (3-year statute of limitations on assessment); CP2000 mismatch process.

---

## 2. Counting the same expense for both 529 and AOTC

**The mistake**: user pays $4,000 of tuition with a 529 distribution AND claims the same $4,000 for AOTC (which would yield a $2,500 credit).

**Why it's wrong**: IRC §529(c)(3)(B)(v) — qualified expenses taken into account for AOTC reduce the amount that can be applied to a tax-free 529 distribution. Pub. 970 (2025) chapter 7 has the formula.

**Correct approach**: allocate $4,000 of tuition to AOTC, then use the 529 distribution to cover *other* qualified expenses (room and board, fees beyond the $4K, books). See [`aaqee-adjustment.md`](./aaqee-adjustment.md).

**Authority**: IRC §529(c)(3)(B)(v); Pub. 970 (2025) chapter 7, Coordination With American Opportunity and Lifetime Learning Credits.

---

## 3. Including the basis (Box 3) as taxable

**The mistake**: user reports Box 1 (or Box 1 minus QHEE) as taxable income on Schedule 1 Line 8z.

**Why it's wrong**: Box 3 (basis) is return of contributions — already-taxed money — and is **never taxable**. Only Box 2 (earnings) is potentially taxable, and only the proportion allocated to the non-qualified portion of the distribution.

**Correct approach**: use the formula `Taxable earnings = Box 2 × (1 − AQEE / Box 1)`, capped at Box 2.

**Authority**: IRC §529(c)(3)(A)-(B) (taxed under §72; exclusion ratio); Pub. 970 (2025) chapter 7, Figuring the Taxable Portion of a Distribution.

---

## 4. Reporting the taxable portion on the wrong person's return

**The mistake**: parent receives a 1099-Q where the recipient is the parent (Box 6 checked: recipient is not the designated beneficiary), and the parent assumes the *student's* return reports the taxable amount.

**Why it's wrong**: the taxable portion goes on the **recipient's** return — whoever's name is on the "Recipient" line. If the parent is the recipient, the parent reports it. If the student is the recipient, the student reports it.

**Correct approach**: read the recipient name carefully. Box 6 indicates whether the recipient is not the beneficiary, but the recipient name controls who reports.

**Authority**: Instructions for Form 1099-Q (Rev. April 2025), "Recipient's Name and TIN" and "Box 6"; Pub. 970 (2025) ch. 7, Are Distributions Taxable.

---

## 5. Forgetting room and board cap

**The mistake**: user claims $20,000 in off-campus rent against a 529 distribution when the school's published cost-of-attendance allowance for off-campus housing is $11,000.

**Why it's wrong**: IRC §529(e)(3)(B)(ii) — room and board qualified expenses are capped at the school's cost-of-attendance allowance for room and board or, if greater, the actual amount charged for housing owned or operated by the school. For off-campus housing only the allowance applies, so rent above it is not qualified.

**Correct approach**: get the school's published cost-of-attendance figures from the financial aid office or school website. Cap room and board at that figure.

**Authority**: IRC §529(e)(3)(B)(ii); Pub 970.

---

## 6. Counting "recommended" books or "optional" fees

**The mistake**: user counts "recommended" textbooks (not actually required by the syllabus) or optional fees (gym membership, optional health insurance) as qualified.

**Why it's wrong**: only **required** books, supplies, and equipment qualify under IRC §529(e)(3)(A)(i). "Recommended" doesn't meet the statutory standard.

**Correct approach**: confirm with the course syllabus or bookstore "required" list. When in doubt, exclude.

**Authority**: IRC §529(e)(3)(A)(i); Pub 970.

---

## 7. Treating K-12 expenses as fully qualified for a 529 plan

**The mistake**: user takes a $25,000 distribution from a 529 in 2025 to pay K-12 tuition for one beneficiary and claims it's all qualified.

**Why it's wrong**: IRC §529(e)(3)(A) caps 529 K-12 qualified expenses per beneficiary per year at **$10,000 for 2025** and **$20,000 for taxable years beginning after Dec. 31, 2025**. Non-tuition K-12 costs (curricular materials, books, online materials, qualifying tutoring, test fees, dual enrollment, educational therapies) count only for distributions after July 4, 2025, and only within the same cap; room and board does not count.

**Correct approach**: cap at $10,000 of K-12 expenses for 2025 ($20,000 for 2026). For 2025 the remaining $15,000 is non-qualified: its earnings share is taxable and subject to the 10% additional tax (subject to no other exception).

**Authority**: IRC §529(c)(7), added by TCJA 2018 and amended by P.L. 119-21 §70413(a); IRC §529(e)(3)(A) as amended by P.L. 119-21 §70413(b).

---

## 8. Confusing 529 K-12 limits with Coverdell K-12

**The mistake**: user with a Coverdell ESA caps K-12 expenses at $10,000/year, thinking the 529 cap applies.

**Why it's wrong**: Coverdell K-12 expenses are NOT capped at the federal level (the $10,000 for 2025 / $20,000 for 2026+ cap is for 529 plans only). Coverdell K-12 also covers a much broader expense list: tuition, fees, books, supplies, equipment, tutoring, special needs services, room and board if living away from home, uniforms, transportation, computer technology.

**Correct approach**: read Boxes 5a-5c carefully. If 5c "Coverdell ESA," apply the §530(b)(3) qualified expense list, not §529(c)(7).

**Authority**: IRC §530(b)(3); IRC §529(c)(7); Pub 970.

---

## 9. Claiming SECURE 2.0 Roth rollover without verifying all 5 conditions

**The mistake**: user assumes a 529-to-Roth rollover is automatically tax-free.

**Why it's wrong**: IRC §529(c)(3)(E) requires **all five** conditions: 15-year account age, beneficiary is Roth owner, within annual Roth limit (and beneficiary has earned income), 5-year contribution age, $35,000 lifetime cap not exceeded.

**Correct approach**: verify each condition explicitly. The most common failure is the 15-year account age. See [`secure-2-roth-rollover.md`](./secure-2-roth-rollover.md).

**Authority**: IRC §529(c)(3)(E); SECURE 2.0 Act §126.

---

## 10. Not using the trustee's Box 2 figure

**The mistake**: user (or agent) recomputes the earnings portion themselves and uses a different number than Box 2.

**Why it's wrong**: the trustee's Box 2 is computed using account-specific data the user doesn't have (every contribution date, every market value at that date), with the earnings ratio in Prop. Reg. §1.529-3, Notice 2001-81, and Notice 2016-13.

**Correct approach**: use Box 2 as given. If Box 1 ≠ Box 2 + Box 3, the form is wrong; ask the trustee for a corrected 1099-Q. Don't override. Exception: a Coverdell 1099-Q may leave boxes 2 and 3 blank and show the year-end FMV in Box 7; then use the Pub. 970 ch. 6 Coverdell worksheet.

**Authority**: Instructions for Form 1099-Q (Rev. April 2025), Box 1 caution, Box 2, Box 3.

---

## 11. Forgetting the 10% additional tax exception for AOTC coordination

**The mistake**: user has a taxable earnings portion solely because they used $4,000 of expenses for AOTC, and they assume both income inclusion AND 10% additional tax apply.

**Why it's wrong**: IRC §530(d)(4)(B)(v), applied to QTPs by §529(c)(6) — the 10% additional tax does NOT apply when the distribution is taxable solely because of AOTC/LLC coordination. The earnings portion is still in income, but no 10% additional tax.

**Correct approach**: on Form 5329 Part II, enter the AOTC-coordination amount on Line 6 (distributions included on line 5 that are not subject to the additional tax). Document the exception.

**Authority**: IRC §530(d)(4)(B)(v); §529(c)(6); Pub. 970 (2025) ch. 7, Exceptions, item 5; 2025 Instructions for Form 5329, Line 6.

---

## 12. Not retaining records of "fully qualified" distributions

**The mistake**: user has a fully qualified distribution, reports nothing on the return, and discards the 1099-Q + receipts after April 15.

**Why it's wrong**: under IRC §6501, the IRS has 3 years to assess additional tax (6 years for substantial under-reporting). If the IRS issues a CP2000 in year 2 alleging non-qualified distribution, the user must produce the QHEE documentation. Without records, they lose.

**Correct approach**: retain the 1099-Q, Form 1098-T (from the school), receipts for room and board / books / computer, and the AQEE worksheet for at least 3 years (6 to be safe).

**Authority**: IRC §6501(a) (3-year general statute), §6501(e) (6 years for >25% understatement).
