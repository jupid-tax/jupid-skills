# Top Schedule A Mistakes

Real mistakes filers make on Schedule A, ranked by how often they trigger IRS notices, audit adjustments, or under-deducting. Each entry has the mistake, the consequence, and the fix.

The IRS audits itemizers at roughly 3-4× the rate of standard-deduction filers. Schedule A line items are the most-questioned section after Schedule C.

---

## 1. Itemizing when the standard deduction is higher

**The mistake**: Filling out Schedule A out of habit without comparing to the standard deduction.

**Why it happens**: Either auto-pilot from prior years (when itemized worked) or assumption that "homeowners always itemize." Post-TCJA, many homeowners take the standard deduction, especially in low-tax states.

**Consequence**: You under-deduct. If Line 17 = $25,000 but standard MFJ = $30,000, itemizing costs you $5,000 of deduction = ~$1,100 at 22% bracket.

**Fix**: Always run both numbers. Write the standard deduction next to Schedule A Line 17 and compare. See [`standard-vs-itemized-decision.md`](./standard-vs-itemized-decision.md).

---

## 2. Using the wrong SALT cap for the year

**The mistake**: Using the old $10,000 SALT cap on a 2025 or 2026 return; or using the new $40,000 cap on a 2024 return.

**Why it happens**: OBBBA (2025) raised the cap retroactively for 2025 and indexed it through 2029. Many tax software products and reference materials lagged in updating. Some prior-year forms were never updated.

**Consequence**: Either under-deducting (using $10K when $40K applies — leaves up to $30K of deduction on the table) or over-deducting (using $40K on a year before it applied — IRS will adjust and may assess penalties).

**Fix**: Verify the cap by year:
- 2024 and earlier: $10,000 ($5,000 MFS)
- 2025: $40,000 ($20,000 MFS)
- 2026: $40,400 ($20,200 MFS)
- 2027-2029: 1% annual increase
- 2030: reverts to $10,000

See [`salt-cap.md`](./salt-cap.md) for the year-by-year table and high-income phaseout.

---

## 3. Missing the SALT high-income phaseout (MAGI > $500K)

**The mistake**: A taxpayer with MAGI $600K claims the full $40K SALT cap on a 2025 return.

**Why it happens**: OBBBA's high-income phaseout is new for 2025 — wasn't part of pre-OBBBA SALT (which was a flat $10K with no phaseout).

**Consequence**: IRS adjustment. At $600K MAGI, $100K excess × 30% phaseout = $30K reduction; effective cap = $10K floor. The filer claimed $40K but only $10K was allowed; $30K of disallowed deduction.

**Fix**: For any filer with MAGI > $500K, compute the phaseout: `Excess MAGI × 30%`, subtract from base cap, floor at $10K. See [`salt-cap.md`](./salt-cap.md).

---

## 4. Deducting cosmetic surgery as medical

**The mistake**: Counting elective cosmetic procedures, gym memberships, vitamins, or wellness purchases as medical on Line 1.

**Why it happens**: User confuses "health-improving" with "medical care for diagnosis/treatment of disease." IRC §213 is specific.

**Consequence**: Disallowance in audit. Repeat patterns invite expanded examination.

**Fix**: Pub 502 has the specific list. If the procedure is purely elective (not deformity, congenital abnormality, or trauma), it doesn't qualify. When in doubt, get a doctor's letter establishing medical necessity (especially for borderline procedures like reconstructive surgery, dental implants beyond function, weight-loss programs).

See [`medical-expenses.md`](./medical-expenses.md).

---

## 5. Including HSA/FSA-paid medical on Line 1

**The mistake**: User includes the full $10,000 surgery bill on Line 1 even though their HSA reimbursed $6,000 of it.

**Why it happens**: HSA/FSA distributions feel like out-of-pocket because the user paid into the account. But contributions were already pre-tax — deducting the reimbursed amount on Schedule A is double-dipping.

**Consequence**: Disallowance and accuracy penalties.

**Fix**: Line 1 is the OUT-OF-POCKET amount only. Subtract HSA distributions, FSA reimbursements, and HRA reimbursements before entering Line 1.

---

## 6. Missing substantiation for charitable gifts ≥ $250

**The mistake**: Claiming a $500 gift with only the canceled check, no contemporaneous written acknowledgment (CWA) from the charity.

**Why it happens**: User assumes a bank record is enough. For gifts ≥ $250, the IRS requires a CWA — a letter from the charity stating the amount and whether goods/services were provided in return, received before the return is filed.

**Consequence**: Disallowance, even if the gift is real. The "contemporaneous" requirement is strict — a letter obtained after filing doesn't count.

**Fix**: Keep every charity acknowledgment letter. Most charities send year-end statements automatically; if yours doesn't, request one before filing.

See [`charitable-contributions.md`](./charitable-contributions.md).

---

## 7. Skipping Form 8283 for non-cash charity > $500

**The mistake**: Donating $2,000 of clothing to Goodwill and not attaching Form 8283.

**Consequence**: IRS auto-adjusts the deduction down or disallows entirely. Form 8283 isn't optional.

**Fix**: Total non-cash > $500 → Form 8283 Section A. Single item > $5,000 → Form 8283 Section B + qualified appraisal (except publicly traded securities).

---

## 8. Donating cryptocurrency > $5,000 without an appraisal

**The mistake**: Donating $20,000 of Bitcoin to a charity, claiming FMV deduction, no qualified appraisal.

**Why it happens**: User assumes crypto is "publicly traded" since it has live market quotes — and publicly traded securities are exempt from the appraisal requirement.

**Consequence**: IRS Memorandum CCA 202302012 clarified that crypto is NOT publicly-traded-securities for the appraisal exception. Multiple Tax Court cases have disallowed the entire deduction for failing this rule.

**Fix**: For crypto donations > $5,000, get a qualified appraisal. Some platforms (Fidelity Charitable, etc.) handle appraisal for you when you donate through them.

---

## 9. Putting PMI on Line 8d for a 2025 return

**The mistake**: Including mortgage insurance premiums on Line 8d on a 2025 return.

**Why it happens**: OBBBA reinstated the PMI deduction effective tax year 2026+. The deduction was unavailable 2022-2025. Some tax software / reference material conflated the OBBBA enactment year (2025) with the deduction's effective year (2026+).

**Consequence**: IRS adjustment. PMI premium is non-deductible for 2025 returns regardless of income.

**Fix**: For 2025 returns, leave Line 8d blank. For 2026+ returns, enter PMI premiums (with phaseout starting at $100K MAGI).

See [`mortgage-interest.md`](./mortgage-interest.md).

---

## 10. Deducting HELOC interest used for non-home purposes

**The mistake**: User has a $50,000 HELOC. They used $30,000 to renovate the kitchen and $20,000 to pay off credit cards. They deduct all the interest on Line 8a.

**Why it happens**: Pre-TCJA (before 2018), HELOC interest was deductible regardless of use up to the home equity debt limit. TCJA restricted to buy/build/improve only — many filers haven't updated their tracking.

**Consequence**: 40% of the interest in the example is non-deductible. IRS catches via Form 1098 cross-matching of HELOC balances against Schedule A interest claimed.

**Fix**: Trace HELOC proceeds. Deductible only if used to buy, build, or substantially improve the home that secures the loan. Document with contractor invoices, bank statements showing the trace. See [`mortgage-interest.md`](./mortgage-interest.md).

---

## 11. Claiming a casualty loss from a non-federally-declared event

**The mistake**: User's car was vandalized in their driveway. Or a tree fell on their house in a non-disaster storm. They claim the loss on Line 15.

**Why it happens**: Pre-TCJA, casualty losses were broadly deductible. TCJA (2018) restricted to federally declared disasters only — and OBBBA made this permanent.

**Consequence**: Disallowance. Schedule A Line 15 is exclusively for federally declared disaster losses.

**Fix**: Verify the event is in a federally declared disaster zone at [FEMA Disaster Declarations](https://www.fema.gov/disaster/declarations). If not federally declared, the loss is non-deductible on Schedule A. Personal theft losses outside disaster contexts are similarly non-deductible.

For business property (Schedule C, E), casualty losses retain their normal deductibility on Form 4684 separately.

---

## 12. Treating the SALT cap as the deduction (forgetting Lines 5d vs 5e)

**The mistake**: User has $25,000 of state and local taxes (income + property + personal property). They write $40,000 on Line 5e because that's the cap.

**Why it happens**: Misunderstanding what "cap" means. The cap is a maximum, not a minimum. Line 5e is the **smaller** of Line 5d or the cap.

**Consequence**: Over-deducting by $15,000 in this example. IRS adjusts and may assess accuracy penalty.

**Fix**: Line 5e = min(Line 5d, applicable cap). The cap is a ceiling, not a floor.

---

## 13. Counting both income tax AND sales tax on Line 5a

**The mistake**: User writes $14,000 (state income tax) + $2,000 (state sales tax) = $16,000 on Line 5a.

**Why it happens**: The user thinks both qualify as SALT. They do — but you pick one or the other, not both.

**Consequence**: IRS adjusts; double-counting is caught easily.

**Fix**: Pick the larger: state income OR state sales tax. Check the box if entering sales tax. See [`salt-cap.md`](./salt-cap.md).

---

## 14. Forgetting state income tax refund recapture

**The mistake**: Last year, user itemized and deducted $14,000 of state income tax. This year, the user receives a $2,000 state refund for last year. The refund isn't reported anywhere.

**Why it happens**: User doesn't realize the refund is taxable income (subject to tax-benefit rule).

**Consequence**: CP2000 notice. The state sends a 1099-G showing the refund; the IRS matches and assesses tax + interest.

**Fix**: If the user itemized AND deducted state income tax in the prior year, the refund is income on **Schedule 1 Line 1** (subject to the tax-benefit rule). Report as income; don't put on Schedule A.

---

## 15. Using the business mileage rate for medical or charity

**The mistake**: User claims 1,000 miles of medical-related driving at 70¢ per mile (business rate). Or 500 miles of volunteer driving at 70¢.

**Consequence**: Over-deducting; IRS catches via the rate not matching Pub 502 / IRC §170(i).

**Fix**: Use the right rate:
- Business: 70¢ for 2025 (per IRS Notice 2025-5)
- Medical: 21¢ for 2025
- Charity: 14¢ (statutory; never indexed)

---

## 16. Treating commute as medical mileage

**The mistake**: User's job is at a hospital. They count their daily commute as medical mileage because medical things happen there.

**Consequence**: Disallowance. Commuting is never deductible regardless of destination.

**Fix**: Medical mileage is for trips primarily for the user's (or family member's) own medical care. The user's job at a hospital is commuting, not medical care for themselves.

---

## 17. Forgetting the 0.5% AGI charity floor (tax year 2026+)

**The mistake**: For a 2026 return, user's $200K AGI and $4K of charitable contributions, deducted as $4K.

**Why it happens**: The 0.5% floor is new under OBBBA (IRC §170(p)) and effective tax year 2026+. Many filers and software haven't internalized it.

**Consequence**: Over-deducting by $1,000 (0.5% × $200K). IRS adjusts.

**Fix**: For tax year 2026+, subtract 0.5% × AGI from the raw charitable total. For tax year 2025 and earlier, no floor applies — full deductibility (subject to AGI ceilings).

See [`charitable-contributions.md`](./charitable-contributions.md).

---

## 18. Putting QCDs on Schedule A

**The mistake**: User is 72, makes a $10,000 QCD from their IRA to a charity, and lists it on Line 11 as a cash charitable contribution.

**Why it happens**: User thinks of it as a charity gift. It is — but the tax treatment is different.

**Consequence**: Double tax benefit attempted. If user excludes from IRA distribution AND deducts on Schedule A, IRS catches and disallows the Schedule A entry.

**Fix**: QCDs are excluded from gross income on **Form 1040 Line 4b**, not deducted on Schedule A. Don't put them on Line 11. The exclusion is a better tax outcome anyway (lowers AGI, indirectly improves multiple Schedule A floors and ceilings).

---

## 19. Including escrow tax payments as mortgage interest

**The mistake**: User's Form 1098 shows $11,800 mortgage interest in box 1 plus $9,500 in box 10 (real estate taxes paid through escrow). User adds these together and puts $21,300 on Line 8a.

**Why it happens**: Form 1098 boxes confuse filers. Property tax shouldn't be on Line 8a.

**Consequence**: Over-deducting interest, under-deducting property tax. May trigger IRS adjustment.

**Fix**: Form 1098 box 1 (interest) → Line 8a. Form 1098 box 6 (points) → Line 8a. Form 1098 box 10 (real estate taxes via escrow) → **Line 5b**. Box 5 (mortgage insurance, 2026+) → Line 8d.

---

## 20. Self-employed deducting health insurance on Schedule A

**The mistake**: A self-employed user deducts their $9,000 of health insurance premiums on Schedule A Line 1 (medical).

**Consequence**: Wrong place. The deduction is allowed but as an above-the-line adjustment, not a Schedule A item. Putting it on Schedule A requires meeting the 7.5% AGI floor — much harder to qualify, much smaller deduction.

**Fix**: Self-employed health insurance goes on **Schedule 1 Line 17** (above-the-line). Don't put it on Schedule A. The above-the-line deduction is more favorable for everyone.

---

## 21. Filing Schedule A unnecessarily (when standard wins)

**The mistake**: User itemized $25,000, standard MFJ is $30,000. User files Schedule A anyway.

**Consequence**: Inefficiency only — the IRS uses the standard deduction in this case (Form 1040 Line 12 takes the larger value automatically). But filing Schedule A:
- Increases audit profile
- Locks in itemized status if MFS spouse needs to coordinate
- Wastes time

**Fix**: Don't file Schedule A unless Line 17 > standard deduction. Just enter standard deduction on Form 1040 Line 12.

---

## 22. Forgetting to attach Form 4684 for casualty / Form 4952 for investment interest

**The mistake**: Claiming $5,000 on Line 15 (casualty) without attaching Form 4684. Or $2,000 on Line 9 without Form 4952.

**Consequence**: IRS auto-correspondence requesting the missing form. Delayed processing or notice with penalty.

**Fix**: Always attach the cross-referenced form:
- Line 9 (investment interest) → Form 4952
- Line 12 (non-cash charity > $500) → Form 8283
- Line 15 (casualty/theft) → Form 4684

---

## 23. Pre-paying property tax in December that hasn't been assessed

**The mistake**: User mails the assessor's office $9,000 in December for next year's property tax, before the assessment is finalized. Claims on Line 5b in the current year.

**Why it happens**: Bunching strategy that looks legitimate.

**Consequence**: IRS notice IR-2017-210 disallowed pre-assessment "prepayments." If the tax has not been formally assessed, the payment is a deposit, not a deduction.

**Fix**: Verify the locality has assessed the tax (sent the bill) before the December payment. Many localities assess late in the calendar year, allowing year-end prepayment of the next year's bill that's already on the books.

---

## 24. Mixing personal and business deductions on Schedule A

**The mistake**: A self-employed taxpayer with a home office deducts the entire mortgage interest and property tax on Schedule A.

**Why it happens**: Easier than splitting.

**Consequence**: Either over-deducting (claiming home office on Schedule C plus full mortgage interest on Schedule A — double dip) or under-deducting (missing the home office deduction entirely).

**Fix**: If using home office on Schedule C with regular method, allocate mortgage interest and property tax between Form 8829 (business portion) and Schedule A (personal portion). Don't double-count. See `schedule-c` skill, `home-office.md`.

---

## Sources

- [Schedule A Instructions](https://www.irs.gov/pub/irs-pdf/i1040sca.pdf)
- [IRS Publication 17](https://www.irs.gov/publications/p17) — Your Federal Income Tax
- [IRS Publication 502](https://www.irs.gov/publications/p502) — Medical and Dental
- [IRS Publication 526](https://www.irs.gov/publications/p526) — Charitable Contributions
- [IRS Publication 547](https://www.irs.gov/publications/p547) — Casualties, Disasters, and Thefts
- [IRS Publication 936](https://www.irs.gov/publications/p936) — Home Mortgage Interest Deduction
- [IRS Notice IR-2017-210](https://www.irs.gov/newsroom/irs-advisory-prepaid-real-property-taxes-may-be-deductible-in-2017-if-assessed-and-paid-in-2017) — prepayment must be assessed
- IRS Memorandum CCA 202302012 — cryptocurrency appraisal requirement
- One Big Beautiful Bill Act of 2025 — SALT cap changes, PMI reinstatement (2026+), 0.5% charity floor (2026+)
