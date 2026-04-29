# Common Schedule SE Mistakes

The 10 most common audit-trip and IRS-notice mistakes on Schedule SE, with citations and fixes.

---

## 1. Filing Schedule SE when net earnings are below $400

**Mistake**: Filer attaches Schedule SE with Line 4a < $400 and Line 12 = $0, treating the form as informational.

**Why it's wrong**: Schedule SE is not required when net SE earnings are below $400 (IRC §1402(b)). Filing it anyway clutters the return; some tax software flags it as an error.

**Fix**: Remove Schedule SE if Line 4a < $400 AND no optional method is elected. Keep Schedule C / F separately — the income still flows to Form 1040 even without SE tax.

**Exception**: If electing an optional method to keep accruing SS credits, Schedule SE IS required even with low earnings.

**Citation**: IRC §1402(b); Schedule SE Instructions, "Who Must File."

---

## 2. Forgetting the 0.9235 multiplier

**Mistake**: Applying 15.3% directly to Schedule C Line 31 (e.g., $50,000 × 0.153 = $7,650) instead of $50,000 × 0.9235 × 0.153 = $7,065.

**Why it's wrong**: The statute (IRC §1402(a)(12)) requires the 0.9235 factor on Line 4a. Skipping it overstates SE tax by ~8.3%.

**Fix**: Always apply 0.9235 to Line 3 to get Line 4a. Then apply 12.4% (capped at the wage base) and 2.9% to Line 6.

**Sanity check**: SE tax × 1.0828 (= 1/0.9235) should approximately equal "net SE income × 15.3%" if you forgot the factor.

**Citation**: IRC §1402(a)(12); Schedule SE Line 4a.

---

## 3. Ignoring W-2 Box 3 wages on Line 8a

**Mistake**: Filer has both a W-2 job ($120K Box 3) and a side gig ($50K Schedule C). They put $0 on Line 8a, paying full 12.4% SS on the SE earnings.

**Why it's wrong**: The W-2 wages already consumed $120K of the SS wage base via FICA. The remaining base on Line 9 should be $176,100 − $120,000 = $56,100 (2025), and SE earnings get the SS portion only up to that remaining base.

**Fix**: Always pull W-2 Box 3 from every W-2 the filer received and sum on Line 8a. Even if the filer thinks "the W-2 doesn't matter for SE," it does — through Lines 8 and 9.

**Worst case**: filer with $200K W-2 wages already exceeds the wage base. Line 9 = 0. SS portion of SE tax = 0. Filer only owes Medicare 2.9% on SE earnings.

**Citation**: Schedule SE Line 8a, Line 9.

---

## 4. Combining both spouses on one Schedule SE

**Mistake**: Married filing jointly with SE income from both spouses, filer sums both on a single Schedule SE in one spouse's name.

**Why it's wrong**: SE tax is computed per individual. The wage base, the 2-of-3 optional method test, and the W-2 wage offset are all per-spouse. Combining inflates one spouse's SS wage base usage and may underpay overall.

**Fix**: File two separate Schedule SEs, one per spouse. Each spouse's name and SSN go on their own form. Each gets their own wage base and W-2 wage offset.

**Citation**: Schedule SE Instructions, "Joint Returns."

---

## 5. Limited partner Box 14 included in Line 2

**Mistake**: Filer is a limited partner in a real estate LP. K-1 Box 14 Code A shows $40K. Filer puts it on Schedule SE Line 2 and pays SE tax.

**Why it's wrong**: Limited partner distributive share is excluded from SE earnings under IRC §1402(a)(13). The K-1 issuer should have left Box 14 blank or zeroed; if they didn't, the filer must override.

**Fix**: Confirm partner status with the K-1 issuer. If truly a limited partner, exclude Box 14 from Line 2. If the K-1 has Box 14 incorrectly populated, attach a statement explaining the override.

**Exception**: **Guaranteed payments** to a limited partner (K-1 Box 4a) for services ARE SE earnings. Include those on Line 2 even if the partner is otherwise limited.

**Citation**: IRC §1402(a)(13); Renkemeyer v. Commissioner, 136 T.C. 137 (2011).

---

## 6. Reducing SE base by Form 2555 foreign earned income exclusion

**Mistake**: Filer is a US citizen living abroad with $100K in Schedule C income. They claim the Form 2555 foreign earned income exclusion ($100K excluded from regular income tax) and reduce Schedule SE Line 2 to $0.

**Why it's wrong**: IRC §911(d)(4) explicitly states the Form 2555 exclusion does NOT reduce SE tax. The filer owes SE tax on the full $100K even though they owe no income tax on it.

**Fix**: Report full SE earnings on Line 2 unreduced. Note in the deliverable: "Foreign earned income subject to SE tax per IRC §911(d)(4)."

**Exception**: If the filer has a totalization agreement Certificate of Coverage from a foreign country, they may exclude the covered SE income.

**Citation**: IRC §911(d)(4); Schedule SE Instructions, "Foreign Earned Income."

---

## 7. Optional method election when ineligible

**Mistake**: Filer has $5K net SE earnings and elects the non-farm optional method to claim 4 SS credits. But they had no SE earnings in any of the prior 3 years.

**Why it's wrong**: Non-farm optional method requires net SE earnings ≥ $400 in 2 of the prior 3 years (IRC §1402(l)). The filer fails the regularity test.

**Fix**: Remove the optional method election. The filer pays SE tax on the actual $5K × 0.9235 = $4,617 base.

**Citation**: IRC §1402(l); Schedule SE Part II Section B Line 16.

---

## 8. Optional method elected for the 6th time in lifetime

**Mistake**: Filer has used the non-farm optional method in 5 prior tax years. Their 6th attempt is rejected by the IRS.

**Why it's wrong**: Lifetime cap of 5 elections under IRC §1402(l)(2). The 6th invocation is invalid.

**Fix**: Remove the election. Suggest filer pull a Social Security earnings statement (https://www.ssa.gov/myaccount/) to track prior elections — the SSA records reflect any year the optional method was used.

**Citation**: IRC §1402(l)(2).

---

## 9. Forgetting to add SE tax to Schedule 2 Line 4

**Mistake**: Filer completes Schedule SE Line 12 = $9,464 but forgets to carry it to Schedule 2 Line 4. The SE tax doesn't show up on Form 1040 Line 23.

**Why it's wrong**: Schedule SE is not self-executing — the user must transcribe Line 12 to Schedule 2 Line 4, which then flows to Form 1040 Line 23. Skipping this means the filer doesn't actually pay the SE tax even though they computed it.

**Fix**: Check Schedule 2 Line 4 = Schedule SE Line 12 before submitting. Tax software does this automatically; paper / FFFF filers must verify.

**Citation**: Form 1040 Instructions, Schedule 2 Part I.

---

## 10. Forgetting the §164(f) deduction on Schedule 1 Line 15

**Mistake**: Filer pays full SE tax but doesn't claim the deductible half on Schedule 1 Line 15. They overpay income tax by the deduction × marginal rate.

**Why it's wrong**: Half of SE tax is an above-the-line deduction (IRC §164(f)) — Schedule 1 Line 15. Skipping it inflates AGI and overpays income tax.

**Fix**: Always carry Schedule SE Line 13 to Schedule 1 Line 15. Worth $1,000+ for a typical SE filer.

**Sanity check**: After completing Schedule SE, the filer's AGI should be lower than (gross income − Schedule C expenses) by exactly the §164(f) amount.

**Citation**: IRC §164(f); Schedule 1 Line 15.

---

## 11. Bonus mistake — Additional Medicare Tax (Form 8959) ignored

**Mistake**: Filer has $300K W-2 + $50K SE in 2025. They compute Schedule SE correctly but forget Form 8959.

**Why it's wrong**: The Additional Medicare Tax of 0.9% applies on wages + SE earnings above $200K (single) / $250K (MFJ) / $125K (MFS). Schedule SE does not handle this — Form 8959 does. Missing it underpays by ~$1,350 in this example.

**Fix**: When Schedule SE Line 6 + W-2 Box 5 (Medicare wages) > the threshold, attach Form 8959. This is also a common audit trigger because the IRS cross-matches W-2 Box 5 with SE earnings.

**Citation**: IRC §3101(b)(2), §1401(b)(2); Form 8959.

---

## 12. Bonus mistake — Statutory employee income flowed to Line 2

**Mistake**: Filer has Form W-2 with "Statutory employee" checked (Box 13). They report the income on Schedule C and let it flow to Schedule SE Line 2.

**Why it's wrong**: Statutory employees have FICA withheld at the W-2 stage. They deduct business expenses on Schedule C but do NOT owe SE tax on those earnings.

**Fix**: Schedule C net profit from statutory-employee income is excluded from Schedule SE Line 2. If the filer has only statutory-employee Schedule C income, no Schedule SE is needed.

**Citation**: IRC §3121(d)(3); Schedule SE Instructions, "Statutory Employees."

---

## Summary table

| # | Mistake | Form line | Fix |
|---|---------|-----------|-----|
| 1 | SE filed below $400 | Line 4a | Remove SE unless optional method |
| 2 | Skipping 0.9235 | Line 4a | Multiply Line 3 × 0.9235 |
| 3 | W-2 Box 3 omitted | Line 8a | Pull from every W-2 |
| 4 | Both spouses on one form | Header | One Schedule SE per SE-earning spouse |
| 5 | Limited partner Box 14 | Line 2 | Exclude unless guaranteed payments |
| 6 | Form 2555 reduced SE | Line 2 | Don't reduce; FEIE doesn't apply |
| 7 | Optional method ineligible | Line 4b | Verify 2-of-3 prior years |
| 8 | Optional method 6th time | Line 4b | Lifetime cap = 5 elections |
| 9 | Schedule 2 Line 4 missing | Schedule 2 | Carry Line 12 to Schedule 2 |
| 10 | §164(f) deduction missing | Schedule 1 | Carry Line 13 to Schedule 1 Line 15 |
| 11 | Form 8959 ignored | (separate form) | If wages + SE > threshold, file 8959 |
| 12 | Statutory employee on Line 2 | Line 2 | Exclude statutory-employee Schedule C |
