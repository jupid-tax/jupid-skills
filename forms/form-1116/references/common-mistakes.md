# Form 1116 — Common Mistakes (Audit-Tripping)

The IRS audits FTC claims because the rules are complex and software handles them imperfectly. The mistakes below recur in audits and tax-court cases. Each entry shows the mistake, the rule it violates, and how the agent should prevent it.

## Mistake 1 — Skipping Form 1116 entirely when the de-minimis exception doesn't apply

**Pattern**: User puts foreign tax directly on Schedule 3 Line 1 without filing Form 1116, but they don't qualify for the $300/$600 election (e.g., they have foreign general-basket income, or amounts exceed the cap).

**Rule violated**: IRC §904(k) limits the election to passive-only income on a qualified payee statement, ≤$300 single / $600 MFJ.

**How to prevent**: Step 1 of the workflow tests every criterion. If ANY fails, the agent must produce Form 1116, not the bare Schedule 3 entry.

## Mistake 2 — Putting foreign earned income on Form 1116 when FEIE was used

**Pattern**: User takes FEIE on Form 2555 to exclude $130K of wages, then puts the same $130K on Form 1116 Line 1a. This double-dips: excludes the income from US tax AND credits the foreign tax against (zero) US tax on that income.

**Rule violated**: Reg. §1.911-6 — no double benefit. Foreign tax allocable to excluded income is non-creditable.

**How to prevent**: Coordination check in Step 2 / [`coordination-with-2555.md`](./coordination-with-2555.md). Excluded wages do NOT appear on Form 1116. Only the non-excluded portion (wages above the FEIE cap) goes on Line 1a; only the foreign tax allocable to non-excluded portion goes on Line 8.

## Mistake 3 — Wrong basket assignment

**Pattern**: User puts foreign wages in passive basket, or foreign dividends in general basket. The §904 limitation computes against the wrong denominator and either over- or under-credits.

**Rule violated**: IRC §904(d) — separate categories.

**How to prevent**: Use [`baskets.md`](./baskets.md) routing rules. Wages and SE income are general (d). 1099-DIV/INT box 7 is passive (c) by default unless high-tax kickout applies.

## Mistake 4 — Skipping the Line 15 QD/LTCG adjustment

**Pattern**: User has foreign qualified dividends (e.g., from a foreign stock taxed at 15% in the US) but leaves Line 15 = 0. The §904 limitation over-credits.

**Rule violated**: IRC §904(b)(2)(B) and the Form 1116 instructions worksheet.

**How to prevent**: Check the de-minimis criteria in [`qualified-dividend-adjustment.md`](./qualified-dividend-adjustment.md). If the user has > $20,000 of foreign QD/LTCG OR is in a higher bracket, run the worksheet.

## Mistake 5 — Translating using the wrong rate

**Pattern**: User uses today's spot rate (the day they're filing) to translate a foreign tax paid 6 months ago. Or mixes spot rate for some items and yearly average for others without consistency.

**Rule violated**: Reg. §1.985-3 and Pub 514 — must use spot rate on date of transaction OR yearly average, consistently.

**How to prevent**: Ask the user upfront which method they're using. Pull rates from the IRS yearly average page or a documented spot source. See [`currency.md`](./currency.md).

## Mistake 6 — Including non-creditable taxes on Line 8

**Pattern**: User includes foreign VAT, foreign property tax, foreign social security tax (Totalization country), or excess withholding (above treaty rate) on Line 8.

**Rule violated**: IRC §901 / Reg. §1.901-2 — only foreign income tax is creditable.

**How to prevent**: Run the [`non-creditable-taxes.md`](./non-creditable-taxes.md) checklist. Ask the user the kind of tax for each amount. Subtract VAT, property tax, SS-equivalent, refundable amounts.

## Mistake 7 — Missing the carryforward / not tracking unused FTC

**Pattern**: User has $25,000 unused FTC in year 1 and forgets it by year 3. Tax software doesn't auto-track across years; FFFF doesn't track at all.

**Rule violated**: IRC §904(c) — 1 year carryback, 10 year carryforward, but only if the user claims it.

**How to prevent**: Output of every Form 1116 deliverable includes a "Carryover tracking" line. The user should keep a running schedule by basket. The agent should enter prior-year carryover on Line 10 each year.

## Mistake 8 — Not allocating deductions to foreign-source income

**Pattern**: User puts $0 on Lines 2-4. The §904 limitation uses gross foreign income (Line 1a) without subtracting any deductions. Limitation is too generous; FTC is overstated.

**Rule violated**: Reg. §1.861-8 — deductions allocate to income.

**How to prevent**: Use [`deduction-allocation.md`](./deduction-allocation.md). At minimum, allocate the standard deduction on Line 3a using the gross-income ratio.

## Mistake 9 — Filing once and never reviewing for change in residence / facts

**Pattern**: User used FTC for 5 years in Germany, then moves to UAE. They keep using FTC in UAE despite zero foreign tax — they should have switched to FEIE. Or they keep using FEIE after moving to a high-tax country, leaving FTC carryforward unused.

**Rule violated**: Not a rule violation per se; just suboptimal. But the FEIE 5-year revocation lock-out (IRC §911(e)(2)) traps users who can't easily switch.

**How to prevent**: Each year, re-run the choice. Tax software often defaults to last year's election; verify it still makes sense.

## Mistake 10 — Treating the FTC limitation as the FTC

**Pattern**: User reports Line 20 (the limitation amount) on Schedule 3 instead of Line 21 (the lesser of Line 13 or Line 20). When foreign tax is less than the limitation, the FTC equals foreign tax paid, not the limitation.

**Rule violated**: IRC §904(a) — the FTC is the lesser of foreign tax or the limitation.

**How to prevent**: Math validation in workflow Step 9. Line 21 = lesser of 13 or 20, period.

## Mistake 11 — Forgetting Line h election binding nature

**Pattern**: User checks "Accrued" on Line h to deduct foreign tax not yet paid. Two years later, they check "Paid" because their accountant changed software. The IRS rejects.

**Rule violated**: IRC §905(a) — accrual election is binding for all future years.

**How to prevent**: Surface the binding nature when the user first elects accrual. The agent should not allow a switch back to "Paid" without acknowledging the user must request IRS consent (rare).

## Mistake 12 — Not filing one Form 1116 per basket

**Pattern**: User has both passive and general foreign income but combines them on a single Form 1116. The §904 limitation is computed against the wrong category mix; FTC overstated.

**Rule violated**: IRC §904(d) — separate limitation per category.

**How to prevent**: After basket assignment in Step 2, the agent ensures one 1116 per basket, with Part IV summary. FFFF allows multiple 1116s; some paid software requires the user to add each manually.

## Audit defense — what the user needs to retain

For 10 years (carryforward window):

- Foreign tax payment receipts (or foreign return) by country and year
- Currency translation worksheet with rate source
- 1099-DIV / 1099-INT / Schedule K-3 from brokers and partnerships
- FEIE allocation worksheet if used
- Carryover schedule by basket (running across years)

If the user can't produce documentation in audit, the FTC is disallowed and tax + interest assessed.

## Citations

- IRC §901 (allowance of foreign tax credit)
- IRC §904(a)-(g) (limitation, separate categories, carryback/carryforward)
- IRC §904(j)/(k) (de-minimis exception)
- IRC §905 (accrual election timing)
- IRC §911(e)(2) (FEIE revocation lock-out)
- Reg. §1.861-8, §1.861-9 (deduction allocation and apportionment)
- Reg. §1.901-2 (creditable tax tests)
- Reg. §1.901-2(c) (soak-up taxes)
- Reg. §1.904-4 (basket rules; high-tax kickout)
- Reg. §1.911-6 (FEIE coordination)
- Reg. §1.985-3 (currency translation)
- Pub. 514 (Foreign Tax Credit for Individuals)
