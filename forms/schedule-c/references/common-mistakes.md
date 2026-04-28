# Top 10 Schedule C Mistakes

Real mistakes filers make on Schedule C, ranked by how often they trigger IRS notices or audit adjustments. Each entry has the mistake, the consequence, and the fix.

## 1. Underreporting income that wasn't on a 1099

**The mistake**: The user adds up their 1099-NEC and 1099-K totals and calls that Line 1. Cash payments, checks, and clients who didn't issue a 1099 get omitted.

**Why it happens**: Filers think "if there's no 1099, the IRS doesn't know." Wrong — the IRS cross-matches 1099s but also runs bank deposit analyses and lifestyle audits. Underreporting is the most common Schedule C audit trigger.

**Consequence**: CP2000 notice (under-reporter inquiry), tax + 20% accuracy penalty + interest, possible fraud penalty (75%) for egregious cases.

**Fix**: Total ALL business income — 1099s, cash, checks, crypto at FMV, barter at FMV. Line 1 should be ≥ the sum of all 1099s received. If it's less, that's the error.

---

## 2. Mixing personal and business expenses

**The mistake**: Personal lunch with a friend deducted as a business meal. Family vacation deducted as business travel. Personal Netflix subscription deducted as software.

**Consequence**: Disallowed deductions. If pattern is widespread, IRS expands audit scope (multiple years).

**Fix**: Apply the IRC §162 "ordinary and necessary" test honestly. Keep a separate business bank account and credit card — using a personal card for everything muddies the audit trail.

---

## 3. Claiming the home office without exclusive use

**The mistake**: Deducting a corner of the living room as a home office. Or deducting a guest room that's also a guest room.

**Consequence**: IRS disallows Line 30 entirely; sometimes opens questions about other deductions.

**Fix**: Strict exclusive use. The space is *only* used for business. If there's a couch where guests sleep, it's not a home office. If the kids do homework on the desk, it's not a home office. A converted closet, a partitioned room, or a separate structure all qualify.

---

## 4. No mileage log

**The mistake**: User claims 12,000 business miles but has no contemporaneous log.

**Consequence**: In audit, the IRS often disallows the entire Line 9 deduction. Reconstruction logs are accepted skeptically; "I drove a lot" is not.

**Fix**: Use an app (Jupid, MileIQ, Hurdlr) or a simple spreadsheet. Log: date, destination, business purpose, miles. Update at least weekly. If the user already missed the log for prior months, reconstruct from calendar entries and document the reconstruction.

---

## 5. Personal vehicle business-use percentage too high

**The mistake**: Claiming 90%+ business use of a vehicle that's also the user's only car.

**Consequence**: IRS sees a sole-vehicle household and is skeptical of high business %. Adjustment downward in audit.

**Fix**: Be honest. If the user has only one vehicle and lives somewhere requiring driving for groceries, kids, errands, business use is more like 40-60%. If business use is genuinely high, document with a daily log showing every trip.

---

## 6. §179'd vehicle then dropped business use below 50%

**The mistake**: Year 1, user takes Section 179 on a $35,000 SUV at 80% business use ($28,000 deduction). Year 2, business use drops to 40% (life changes — new commute, less travel). User keeps depreciating but doesn't recapture.

**Consequence**: §179 recapture in the year business use drops to ≤50%. The recapture is reported on Form 4797 and adds back to income. Plus penalties if the IRS catches it via vehicle audit.

**Fix**: When taking §179 or bonus on a vehicle, project ahead. If business use is shaky, use straight MACRS instead — no recapture trigger from a use-percentage drop.

---

## 7. Categorizing expenses on the wrong line

**The mistake**: Putting payment processor fees (Stripe, Square) on Line 8 (Advertising) instead of Line 10 (Commissions and fees). Or putting a CPA's fee on Line 11 (Contract labor) instead of Line 17 (Legal & professional).

**Consequence**: No tax difference (the deduction lands either way), but it makes the return look unprofessional and may flag for review. The IRS expects certain expense ratios per NAICS code — wrong categorization distorts those.

**Fix**: Use [`line-by-line.md`](./line-by-line.md) to map each expense to its actual line. When in doubt, ask.

---

## 8. Section 179 deduction larger than business income

**The mistake**: User has $40,000 net profit before §179 and takes a $50,000 §179 deduction on a new piece of equipment.

**Consequence**: §179 is income-limited. The excess $10,000 doesn't reduce current-year tax — it carries forward. Many filers don't realize this and over-claim, then discover the limitation when their tax software flags it.

**Fix**: Project the §179 against expected taxable business income. If §179 would exceed income, consider MACRS or bonus depreciation (which can create a loss) instead.

---

## 9. Not filing Schedule SE when profit > $400

**The mistake**: Schedule C shows a $25,000 net profit. User files Schedule C correctly, files Form 1040, doesn't file Schedule SE.

**Consequence**: IRS notice. Self-employment tax of ~$3,500 plus penalties and interest. Schedule SE is *required* if profit > $400 (IRC §1402(a)).

**Fix**: Schedule SE is mandatory whenever profit exceeds $400. The skill should remind the user at handoff.

---

## 10. Hobby loss patterns

**The mistake**: User reports a Schedule C loss every year for 5+ years on what's actually a hobby (e.g., a horse farm, a side project that never makes money).

**Consequence**: IRS may reclassify the activity as a hobby under IRC §183. Expenses become non-deductible (post-TCJA, hobby expenses can't be deducted at all by individuals). The user pays tax on hobby income with no offsetting deductions.

**Fix**: A real business has profit motive. The IRS uses 9 factors (Reg. §1.183-2) to assess: businesslike conduct, expertise, time invested, expectation of profit, history of income/losses, occasional profitability, financial status, elements of personal pleasure. If the user has lost money 3 of 5 years (or 2 of 7 for horse activities), the IRS can presumptively call it a hobby — burden shifts to the user to prove profit motive.

---

## Less common but worth flagging

### 11. Claiming gifts as advertising

Customer gifts are limited to $25 per recipient per year (IRC §274(b)). Items > $25 → only $25 deductible per recipient. Some filers put gifts on Line 8 (Advertising) thinking they avoid the cap. They don't — and the IRS knows.

### 12. Double-deducting items inside the standard mileage rate

Standard mileage already includes gas, repairs, insurance, depreciation. Don't deduct those separately when using standard mileage. Common error: deducting vehicle insurance on Line 15 while also using standard mileage on Line 9.

### 13. Reporting health insurance as Schedule C Line 14

The owner's health insurance is NOT a Schedule C expense. It's Schedule 1 Line 17 (self-employed health insurance deduction). Putting it on Line 14 mixes employee benefits with owner benefits — disallowed in audit.

### 14. Capitalizing what should be expensed (and vice versa)

A $1,800 laptop is under the de minimis $2,500 threshold — expense it on Line 18, no Form 4562 needed. A $4,500 laptop must be depreciated or §179'd.

A roof replacement is an improvement, not a repair — capitalize it. Patching the roof is a repair — Line 21.

### 15. Forgetting Part V detail for Line 27a

Putting a lump sum on Line 27a without itemizing Part V (Line 48). The IRS expects Part V to detail every expense aggregated into 27a. Tax software handles this, but paper filers and some DIY users miss it.

### 16. Mismatched Part IV vehicle dates

Line 43 (date placed in service) is the date the vehicle was *first used for business*, not the purchase date. Filers often write the purchase date, which is an inconsistency the IRS notices if business use began later.

### 17. Inventory shrinkage without explanation

Year-over-year ending inventory drops 50% without a corresponding spike in COGS (sales). Sometimes legit (write-off of obsolete inventory), but the IRS notices. Document write-offs with dated photos and a written log.

### 18. EIN on the return when the user is a sole prop with no employees

Putting an EIN on Line D when the user is a true sole prop without employees is fine — it actually protects the SSN. But if the EIN is from an LLC the user no longer operates, that's a mismatch the IRS will question. Match the EIN to the business actually being reported.

### 19. Hobby expenses over hobby income

Even before the §183 reclassification, the IRS limits hobby expenses to hobby income (and post-TCJA, hobby expenses are simply not deductible by individuals). Don't run a Schedule C loss from a hobby — the IRS will reclassify, and the user loses the entire deduction stack.

### 20. Filing as Schedule C when actually a partnership

If two or more people share ownership of the business, it's a partnership (Form 1065), not a sole proprietorship — *unless* they're a married couple electing Qualified Joint Venture status (each spouse files their own Schedule C for their share). One Schedule C with two owners is the wrong form. The IRS will catch this when SSNs cross-match.
