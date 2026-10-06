# Form 1116 — Common Mistakes (Audit-Tripping)

The IRS audits FTC claims because the rules are complex and software handles them imperfectly. The mistakes below recur in audits and tax-court cases. Each entry shows the mistake, the rule it violates, and how the agent should prevent it.

## Mistake 1 — Skipping Form 1116 entirely when the de-minimis exception doesn't apply

**Pattern**: User puts foreign tax directly on Schedule 3 Line 1 without filing Form 1116, but they don't qualify for the $300/$600 election (e.g., they have foreign general-basket income, or amounts exceed the cap).

**Rule violated**: IRC §904(j) and the 2025 Form 1116 instructions ("Election To Claim the Foreign Tax Credit Without Filing Form 1116"): all foreign-source gross income must be passive category income, all of it and the tax on it must be reported on a qualified payee statement (Form 1099-DIV, 1099-INT, Schedule K-1 (Form 1041), Schedule K-3 (Form 1065 or 1120-S), or a substitute statement), and total creditable foreign taxes must be $300 or less ($600 married filing jointly). The election isn't available to estates or trusts.

**How to prevent**: Step 1 of the workflow tests every criterion. If ANY fails, the agent must produce Form 1116, not the bare Schedule 3 entry.

## Mistake 2 — Putting foreign earned income on Form 1116 when FEIE was used

**Pattern**: User takes FEIE on Form 2555 to exclude $130K of wages, then puts the same $130K on Form 1116 Line 1a. This double-dips: excludes the income from US tax AND credits the foreign tax against (zero) US tax on that income.

**Rule violated**: IRC §911(d)(6) and Reg. §1.911-6(c) — no double benefit. Foreign tax allocable to excluded income is non-creditable.

**How to prevent**: Coordination check in Step 2 / [`coordination-with-2555.md`](./coordination-with-2555.md). Excluded wages do NOT go on Line 1a (they still count in Lines 3d and 3e). Only the non-excluded portion (wages above the FEIE cap) goes on Line 1a. The full foreign tax goes on Line 8, and the part allocable to the excluded income comes out on Line 12 as a negative (2025 i1116, Line 12).

## Mistake 3 — Wrong basket assignment

**Pattern**: User puts foreign wages in passive basket, or foreign dividends in general basket. The §904 limitation computes against the wrong denominator and either over- or under-credits.

**Rule violated**: IRC §904(d) — separate categories.

**How to prevent**: Use [`baskets.md`](./baskets.md) routing rules. Wages and SE income are general (d). Income behind foreign tax in 1099-DIV box 7 or 1099-INT box 6 is passive (c) by default unless high-tax kickout applies.

## Mistake 4 — Skipping the qualified dividend / capital gain adjustment (Lines 1a and 18)

**Pattern**: User has foreign qualified dividends (e.g., from a foreign stock taxed at 15% in the US) but enters them on Line 1a at full value and uses unadjusted taxable income on Line 18 without qualifying for the adjustment exception. The §904 limitation over-credits.

**Rule violated**: IRC §904(b)(2)(B) and the 2025 Form 1116 instructions ("Qualified Dividends and Capital Gains (Losses)" and the Worksheet for Line 18).

**How to prevent**: Check the adjustment exception in [`qualified-dividend-adjustment.md`](./qualified-dividend-adjustment.md): it applies only if line 5 of the Qualified Dividends and Capital Gain Tax Worksheet is not more than $197,300 (single, HOH, MFS) or $394,600 (MFJ, QSS) AND foreign qualified dividends plus capital gain distributions are less than $20,000. If either test fails (or the user doesn't elect it), multiply foreign amounts taxed at 15% by 0.4054 and at 20% by 0.5405 on Line 1a, leave 0%-rate amounts off, and figure Line 18 with the Worksheet for Line 18.

## Mistake 5 — Translating using the wrong rate

**Pattern**: User uses today's spot rate (the day they're filing) to translate a foreign tax paid 6 months ago. Or applies the IRS yearly average rate to taxes claimed on the paid basis.

**Rule violated**: IRC §986(a), the 2025 Form 1116 instructions ("Foreign Currency Conversion") and Pub. 514 — taxes claimed on the paid basis use the rate on the day paid or withheld; taxes claimed on the accrued basis generally use the average rate for the tax year they relate to (spot rate on the payment date if paid more than 2 years after that year, paid before it, or in an inflationary currency). Attach an explanation of the conversion.

**How to prevent**: Ask the user upfront whether they claim taxes paid or accrued. Pull rates from the IRS yearly average page (accrued taxes, and income when used consistently) or a documented spot source (paid taxes). See [`currency.md`](./currency.md).

## Mistake 6 — Including non-creditable taxes on Line 8

**Pattern**: User includes foreign VAT, foreign property tax, foreign social security tax (Totalization country), or excess withholding (above treaty rate) on Line 8.

**Rule violated**: IRC §901 / Reg. §1.901-2 — only foreign income tax is creditable.

**How to prevent**: Run the [`non-creditable-taxes.md`](./non-creditable-taxes.md) checklist. Ask the user the kind of tax for each amount. Subtract VAT, property tax, social security tax paid to a totalization-agreement country, refundable amounts.

## Mistake 7 — Missing the carryforward / not tracking unused FTC

**Pattern**: User has $25,000 unused FTC in year 1 and forgets it by year 3. Free File Fillable Forms starts blank each year, so nothing is carried unless the user enters it.

**Rule violated**: IRC §904(c) — 1 year carryback, 10 year carryforward, but only if the user claims it.

**How to prevent**: Output of every Form 1116 deliverable includes a "Carryover tracking" line. The user should keep a running schedule by basket. The agent should enter prior-year carryover on Line 10 each year from Schedule B (Form 1116), line 3, column (xiv), and attach Schedule B for each category with a carryover in or a new carryover out (2025 i1116, Line 10).

## Mistake 8 — Not allocating deductions to foreign-source income

**Pattern**: User puts $0 on Lines 2-4. The §904 limitation uses gross foreign income (Line 1a) without subtracting any deductions. Limitation is too generous; FTC is overstated.

**Rule violated**: Reg. §1.861-8 — deductions allocate to income.

**How to prevent**: Use [`deduction-allocation.md`](./deduction-allocation.md). At minimum, allocate the standard deduction on Line 3a using the gross-income ratio.

## Mistake 9 — Filing once and never reviewing for change in residence / facts

**Pattern**: User used FTC for 5 years in Germany, then moves to UAE. They keep using FTC in UAE despite zero foreign tax — they should have switched to FEIE. Or they keep using FEIE after moving to a high-tax country, leaving FTC carryforward unused.

**Rule violated**: Not a rule violation per se; just suboptimal. But the FEIE 5-year revocation lock-out (IRC §911(e)(2)) traps users who can't easily switch.

**How to prevent**: Each year, re-run the choice. Tax software often defaults to last year's election; verify it still makes sense.

## Mistake 10 — Treating the FTC limitation as the FTC

**Pattern**: User reports Line 21 or Line 23 (the limitation amount) on Schedule 3 instead of the credit. Line 24 is the smaller of Line 14 (foreign taxes available) or Line 23 (limitation), and Part IV Line 35 is what goes to Schedule 3 line 1. When foreign tax is less than the limitation, the FTC equals the foreign tax, not the limitation.

**Rule violated**: IRC §904(a) — the FTC is the lesser of foreign tax or the limitation.

**How to prevent**: Math validation in workflow Step 9. Line 24 = smaller of Line 14 or Line 23; Line 33 = smaller of Line 20 or Line 32; Line 35 = Line 33 − Line 34.

## Mistake 11 — Forgetting that the Part II accrual election is binding

**Pattern**: User checks "Accrued" (Part II box (k)) to credit foreign tax not yet paid. Two years later, they check "Paid" (box (j)) because their accountant changed software. The IRS rejects.

**Rule violated**: IRC §905(a) and the 2025 Form 1116 instructions (Part II) — a cash-basis filer can choose accrued only on a timely filed original return (not an amended return), and once chosen must credit foreign taxes in the year they accrue on all future returns.

**How to prevent**: Surface the binding nature when the user first elects accrual. The agent should not allow a switch back to "Paid": the instructions give no way back once accrual is chosen.

## Mistake 12 — Not filing one Form 1116 per basket

**Pattern**: User has both passive and general foreign income but combines them on a single Form 1116. The §904 limitation is computed against the wrong category mix; FTC overstated.

**Rule violated**: IRC §904(d) — separate limitation per category.

**How to prevent**: After basket assignment in Step 2, the agent ensures one 1116 per basket, with Part IV completed on the form with the largest Line 24 (for 2025 Part IV is required even with one Form 1116). In Free File Fillable Forms, Form 1116 line 35 does not transfer to Schedule 3 line 1; enter it there directly (FFFF known limitations).

## Audit defense — what the user needs to retain

Keep these while any credit, carryover, or refund claim for the year can still change (the IRC §6511(d)(3) claim period for the credit is 10 years). Pub. 514 ("Records To Keep") lists the first three:

- A receipt for each foreign tax payment, and the foreign tax return if the credit is for accrued taxes (with a certified translation if in a foreign language)
- Payee statements showing foreign tax (Form 1099-DIV, 1099-INT)
- Currency translation worksheet with rate source
- Schedule K-3 from partnerships and S corporations
- FEIE allocation worksheet if used
- Carryover schedule by basket (running across years)

If the user can't produce documentation in audit, the FTC is disallowed and tax + interest assessed.

## Citations

- IRC §901 (allowance of foreign tax credit)
- IRC §904(a)-(g) (limitation, separate categories, carryback/carryforward)
- IRC §904(j) (election to claim the credit without Form 1116)
- IRC §905 (accrual election timing)
- IRC §911(d)(6) (no credit on excluded income), §911(e)(2) (FEIE revocation lock-out)
- Reg. §1.861-8, §1.861-9 (deduction allocation and apportionment)
- Reg. §1.901-2 (creditable tax tests)
- Reg. §1.901-2(e)(6) (soak-up taxes)
- Reg. §1.904-4 (basket rules; high-tax kickout)
- Reg. §1.911-6(c) (foreign taxes on excluded income)
- IRC §986(a) (translation of foreign taxes); 2025 Form 1116 instructions, "Foreign Currency Conversion"
- Pub. 514 (Foreign Tax Credit for Individuals), including "Records To Keep"
- 2025 Form 1116 and Instructions for Form 1116 (Dec 23, 2025)
- Free File Fillable Forms known limitations (Form 1116), https://www.irs.gov/e-file-providers/free-file-fillable-forms
