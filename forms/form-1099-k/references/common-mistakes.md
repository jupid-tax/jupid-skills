# Common 1099-K Mistakes

Top filer mistakes the agent should explicitly check for. Each entry has the mistake, why it matters, and the correct path.

---

## Mistake 1: Subtracting platform fees from Box 1a before reporting

**The mistake**: User receives a 1099-K showing Box 1a = $52,000. They look at their net deposits ($48,000 after $4,000 in platform fees) and report $48,000 on Schedule C Line 1.

**Why it matters**: The IRS document-matching system compares Box 1a to the user's reported gross. $48,000 reported < $52,000 on the IRS copy → automatic CP2000 alleging $4,000 of unreported income.

**Correct path**: Report $52,000 (gross) on Schedule C Line 1. Deduct the $4,000 in platform fees as a separate Schedule C Line 10 (Commissions and fees) entry. Net is the same to the user; the IRS sees Box 1a fully reported.

**Citation**: IRC §6050W (gross reporting); Schedule C instructions Line 10.

---

## Mistake 2: Treating personal Venmo payments as business income

**The mistake**: User has a single Venmo account used for both freelance income and friends/family payments. 1099-K shows Box 1a = $25,000 — actually $5,000 freelance + $20,000 personal reimbursements. User reports $25,000 on Schedule C Line 1 and pays SE tax (15.3%) on the full amount.

**Why it matters**: $20,000 of "income" was never income — it was friends paying back for shared dinners, group gifts, and split rent. The user pays about $2,826 in unnecessary SE tax (15.3% × 92.35% × $20,000), plus federal income tax on the $20,000 phantom income.

**Correct path**:
- Schedule C Line 1: $5,000 (the actual freelance portion)
- Entry space at the top of Schedule 1: $20,000 (amount included in error)
- The personal portion is not added to income; freelance portion runs through Schedule C correctly

**Citation**: IRS FS-2025-08, What to do Q4 (roommate rent example) and Common situations Q3; 2025 Form 1040 instructions, Schedule 1 "Form(s) 1099-K"; IRC §61 (gross income).

---

## Mistake 3: Omitting personal portion entirely

**The mistake**: User recognizes the personal portion isn't income but doesn't report it on the return at all. Reports only the business portion on Schedule C Line 1.

**Why it matters**: IRS document matching sees Box 1a = $25,000 and only $5,000 accounted for on the return. That gap can produce a CP2000 proposing tax on $20,000.

**Correct path**: Same as Mistake 2 — enter the $20,000 in the entry space at the top of Schedule 1. The return then accounts for all of Box 1a, even though the net taxable income is just the business portion.

**Citation**: IRS FS-2025-08; 2025 Schedule 1 (Form 1040), entry space above Part I.

---

## Mistake 4: Reporting Etsy / eBay sales as hobby instead of business

**The mistake**: Etsy seller with steady $20,000-$50,000 annual sales reports the income on Schedule 1 Line 8j (Activity not engaged in for profit) to "avoid" Schedule C. User believes Schedule C is "harder" or doesn't realize the activity has crossed into trade-or-business.

**Why it matters**:
1. Hobby reporting blocks all expense deductions (miscellaneous itemized deductions are disallowed under IRC §67(g), made permanent by P.L. 119-21 §70110). Etsy's 6.5% transaction fee, materials cost, shipping, and home studio expenses all become non-deductible.
2. The user pays full federal income tax on gross instead of net.
3. If the IRS later reclassifies the activity as a trade or business, it can also assess SE tax retroactively (15.3% of net) — but by then the deductible expenses may be lost to the statute of limitations.

**Correct path**: Apply the IRC §183 / Treas. Reg. §1.183-2(b) 9-factor test. For a regular Etsy seller with profit motive, business-like records, repeated activity, and intent to earn money, the activity is a trade or business. File Schedule C. Pay SE tax on net profit. Deduct all ordinary and necessary business expenses.

**Citation**: IRC §183; Treasury Regulation §1.183-2(b); IRC §67(g); Schedule C instructions.

---

## Mistake 5: Reporting personal-item resale at a loss as business income

**The mistake**: User cleans out their closet and sells $3,000 worth of used clothing on Poshmark — every item below original cost. 1099-K from Poshmark shows Box 1a = $3,000. User reports $3,000 on Schedule C Line 1 and tries to deduct the original cost of the clothing.

**Why it matters**:
1. The clothing wasn't "purchased for resale" — it was personal-use property. IRC §165 doesn't allow loss deductions on personal-use property dispositions.
2. The user can't take a Schedule C COGS deduction for the clothing's original cost (it wasn't business inventory).
3. Net effect: user pays SE tax + income tax on $3,000 that's not income at all.

**Correct path** (per IRS FS-2025-08, What to do Q6):
- Entry space at the top of Schedule 1: $3,000 (personal items sold at a loss)
- Nothing on Schedule C; no SE tax; no income tax on the loss sales
- If any item sold above its cost, that item goes on Form 8949 / Schedule D instead

**Citation**: IRC §165 (losses); IRC §1221 (capital asset); IRS FS-2025-08; 2025 Form 1040 instructions, Schedule 1 "Form(s) 1099-K".

---

## Mistake 6: Forgetting backup withholding (Box 4) credit

**The mistake**: User's 1099-K shows Box 4 = $1,200 (backup withholding because the user's W-9 had a TIN mismatch earlier in the year). User doesn't notice and files without claiming the $1,200.

**Why it matters**: That $1,200 was withheld from the user's payments and remitted to the IRS. It's a refundable credit identical in treatment to W-2 withholding. Not claiming it overpays federal tax by $1,200.

**Correct path**: Form 1040 Line 25b (Form(s) 1099) — enter the Box 4 amount. The credit applies against total federal tax liability and refunds any excess.

**Citation**: IRC §3406 (backup withholding); 2025 Form 1040, line 25b.

---

## Mistake 7: Double-reporting income that appears on both 1099-K and 1099-NEC

**The mistake**: User has a $5,000 client payment that flowed through PayPal. PayPal issued a 1099-K covering it (alongside other PayPal income); the client also (incorrectly) issued a 1099-NEC for the same $5,000. User adds both to Schedule C Line 1, reporting $10,000 instead of $5,000.

**Why it matters**: The user is paying federal income tax + SE tax on $5,000 of phantom income.

**Correct path**: Report the $5,000 once on Schedule C Line 1. Keep records showing the overlap. If the IRS sends a CP2000 alleging missing $5,000 (because their system saw both 1099s and only one reported), respond with the reconciliation worksheet showing the overlap.

The general rule (Instructions for Forms 1099-MISC and 1099-NEC, "Form 1099-K"): payments made by payment card or through a third party network are reported on Form 1099-K under IRC §6050W and are not subject to reporting on Form 1099-NEC. In practice, many clients issue 1099-NEC anyway. Document the overlap; report once; if Forms 1099-NEC box 1 total more than Schedule C line 1, attach a statement explaining the difference (Schedule C instructions, line 1).

**Citation**: IRC §6041 (1099-NEC reporting); IRC §6050W (1099-K reporting); Instructions for Forms 1099-MISC and 1099-NEC.

---

## Mistake 8: Filing with a known-wrong 1099-K instead of requesting a correction

**The mistake**: 1099-K Box 1a shows $30,000. Platform's own dashboard for the year shows $24,000. User notices the discrepancy but files using $30,000 because "it's faster" and plans to "fix it later."

**Why it matters**: Filing with the higher number means paying tax on $6,000 of phantom income. Dropping the $6,000 silently leaves an unexplained gap against the IRS copy.

**Correct path**:
1. Request a corrected 1099-K from the filer (the IRS can't correct it; FS-2025-08, What to do Q4)
2. If the correction won't arrive in time, don't wait: report the correct $24,000 where it belongs and enter the $6,000 included in error in the entry space at the top of Schedule 1, keeping the platform records that prove it
3. Form 4868 (extension to October 15) is an option if the user prefers to wait; it extends time to file, not time to pay

The user should NOT report a known-wrong amount as income.

**Citation**: IRS FS-2025-08, What to do Q4; 2025 Form 1040 instructions, Schedule 1 "Form(s) 1099-K"; Form 4868 instructions.

---

## Mistake 9: Treating short-term rental as Schedule C when it's Schedule E

**The mistake**: Airbnb host receives a 1099-K covering passive rental income. Reports on Schedule C and pays SE tax (15.3%) on the net profit.

**Why it matters**: Passive rental of real property without substantial services is reported on Schedule E. Schedule E income is NOT subject to SE tax. The user is overpaying by 15.3% of net profit unless the activity meets the substantial-services exception (daily cleaning, meals, concierge — most STR hosts don't qualify).

**Correct path**: Default to Schedule E for short-term rental real estate. Report rental income on Line 3, expenses on Lines 5-19. Net profit flows to Schedule 1 Line 5. Substantial-services exception requires hotel-like services per Treas. Reg. §1.1402(a)-4 — see [`examples/airbnb-host.md`](../examples/airbnb-host.md).

**Citation**: IRC §1402(a)(1); Treasury Regulation §1.1402(a)-4; IRS Pub 527.

---

## Mistake 10: Not splitting state-trigger 1099-K from federal-only activity

**The mistake**: User in Massachusetts runs a small Etsy shop with $1,200 in annual sales. Etsy issues a 1099-K because Massachusetts requires TPSOs to report $600 or more (mass.gov, Form 1099 Filing Requirements). User panics, thinking they've crossed a federal threshold, and over-reports.

**Why it matters**: The state-trigger 1099-K just means there's documentation. The federal reporting on Schedule C is the same regardless: $1,200 gross on Line 1, expenses deducted, net flows to Schedule 1 Line 3 + Schedule SE. No special federal treatment for sub-federal-threshold 1099-Ks.

**Correct path**: Treat the 1099-K as documentation of business income. Reconcile, report on Schedule C, deduct expenses, file. The state-level filing (state tax return) uses the same numbers.

**Citation**: State 1099-K requirements vary; see [`phased-thresholds.md`](./phased-thresholds.md) for state thresholds.

---

## Sources

- IRC §61, §162, §165, §183, §1221, §3406, §6041, §6050W, §67(g), §1402(a)(1)
- Treasury Regulation §1.183-2(b), §1.1402(a)-4
- [IRS Fact Sheet FS-2025-08, Form 1099-K FAQs](https://www.irs.gov/pub/taxpros/fs-2025-08.pdf) (Oct. 23, 2025)
- 2025 Instructions for Form 1040, Schedule 1 "Form(s) 1099-K"
- [IRS Pub 527](https://www.irs.gov/publications/p527)
- [IRS Pub 525](https://www.irs.gov/publications/p525)
- Schedule C / Schedule E / Schedule 1 instructions (current revisions)
- 2025 Form 1040, line 25b
