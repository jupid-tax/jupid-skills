# Form 8959 — Common Mistakes

Audit-trip patterns the agent should watch for. Each mistake includes a citation, a worked failure mode, and the correct fix.

## 1. Confusing the 0.9% Additional Medicare Tax (Form 8959) with the 3.8% NIIT (Form 8960)

**Mistake**: Filer reports investment income surtax on Form 8959, or earned-income surtax on Form 8960.

**Why it happens**: Both surtaxes have the same threshold dollar amounts ($200K / $250K / $125K) and were enacted together in the Affordable Care Act. They are commonly described as "the Medicare surtaxes" in tax press.

**Fix**: Form 8959 covers earned income only — wages, SE income, RRTA compensation. Form 8960 covers investment income — interest, dividends, capital gains, rental income, passive K-1 income. They are separate IRC sections (§3101/§1401 vs. §1411) and may both apply to the same filer in the same year.

**Citation**: IRC §1411 (NIIT); IRC §3101(b)(2), §1401(b)(2) (Add'l Medicare Tax).

## 2. Using the wrong threshold for filing status

**Mistake**: Defaulting to "married = $250K" when the filer is MFS ($125K).

**Why it happens**: MFS is uncommon and the threshold is the lowest of any status — not intuitive.

**Fix**: Always confirm filing status explicitly. The agent's prerequisites step requires it. The threshold table:

| Status | Threshold |
|--------|-----------|
| Single, HoH, QSS | $200,000 |
| MFJ | $250,000 |
| **MFS** | **$125,000** |

**Citation**: IRC §3101(b)(2); IRC §1401(b)(2).

## 3. Using Schedule C net profit instead of Schedule SE Line 6 on Form 8959 Line 8

**Mistake**: Filer puts $200K Schedule C net profit directly on Line 8.

**Why it happens**: Filer assumes "self-employment income" means Schedule C bottom line.

**Fix**: Form 8959 Line 8 is **Schedule SE Part I Line 6** — the figure after the 92.35% multiplier per IRC §1402(a)(12). $200K Schedule C net = $184,700 on Schedule SE Line 6. Using the wrong figure inflates the surtax.

**Citation**: IRC §1402(a)(12); Form 8959 Instructions, Line 8.

## 4. Forgetting that wages reduce the SE threshold (Line 11)

**Mistake**: Filer with $150K wages and $80K SE income computes "$80K SE income, threshold $200K, no surtax owed" — treating the wage and SE thresholds as separate.

**Why it happens**: Each part of the form has a "threshold" line; filer reads them as independent.

**Fix**: Part II Line 11 = Line 9 − Line 10, where Line 10 is the wages from Part I Line 4. The threshold is single, consumed by wages first, with leftover available to absorb SE income.

**Citation**: Form 8959 Instructions, Lines 9–11. See `wage-vs-se-interaction.md` for worked examples.

## 5. Not filing Form 8959 because the employer already withheld

**Mistake**: Filer with $260K W-2 wages from one employer assumes "the employer withheld the additional 0.9% so I don't need to file Form 8959."

**Why it happens**: True that net at filing is zero, but the form still must be filed.

**Fix**: Form 8959 must be filed any time Part I, II, or III has a non-zero entry, OR Part V Line 21 (additional Medicare tax withheld by employer) is non-zero. The reconciliation is the entire point — without Form 8959, the filer cannot claim the Line 24 withholding credit on Form 1040 Line 25c.

**Citation**: Form 8959 Instructions, "Who Must File."

## 6. Missing the Line 24 credit on Form 1040 Line 25c

**Mistake**: Filer files Form 8959, computes Line 18 = $1,800, transfers it to Schedule 2 Line 11, then forgets to transfer Line 24 = $1,800 to Form 1040 Line 25c. Result: filer is double-charged the surtax.

**Why it happens**: Tax software usually handles this auto-flow, but paper filers and FFFF users sometimes miss it. Also happens when the filer pulls the form mid-process and resumes later.

**Fix**: Always cross-check that Line 24 (additional Medicare tax withheld) is on Form 1040 Line 25c. If missing, the filer pays the surtax twice — once via the Box 6 employer withholding and again via Schedule 2 Line 11.

**Citation**: Form 8959 Instructions, Part V; Form 1040 Instructions, Line 25c.

## 7. Counting the same income twice (W-2 Box 5 and Schedule C)

**Mistake**: Filer with statutory-employee status (W-2 Box 13 checked) reports the wages on both Line 1 (W-2 Box 5) and Line 8 (via Schedule C → Schedule SE).

**Why it happens**: Statutory employees report wages on a W-2 but their expenses on Schedule C, which can look like SE income.

**Fix**: Statutory-employee wages are reported only on Line 1 (Medicare wages). They do NOT generate Schedule SE income — the W-2 already withholds SS and Medicare. Schedule C for a statutory employee shows only the expense deduction; net profit (or loss) does not flow to Schedule SE.

**Citation**: Schedule SE Instructions, "Who Must File"; Statutory Employee box on Form W-2.

## 8. Misreading W-2 Box 6 against W-2 Box 5

**Mistake**: Filer assumes W-2 Box 6 (Medicare tax withheld) = 1.45% × W-2 Box 5, and any difference is an error.

**Why it happens**: The math is roughly right for filers under $200K but breaks above the threshold.

**Fix**: For wages above $200K from a single employer, Box 6 = 1.45% × Box 5 + 0.9% × (Box 5 − $200,000). If Box 6 doesn't match this formula, *then* there may be a W-2 reporting error.

**Citation**: IRC §3102(f); Treasury Reg. §31.3102-4.

## 9. Filing Form 8959 standalone without Form 1040

**Mistake**: Filer files Form 8959 alone, hoping to "report the surtax separately."

**Why it happens**: New filers unfamiliar with the attachment-form structure.

**Fix**: Form 8959 always attaches to Form 1040 (or Form 1040-NR for nonresident filers, where applicable). It cannot be filed standalone. The IRS will reject a standalone Form 8959 submission.

**Citation**: Form 8959 instructions header.

## 10. Treating mid-year filing-status change as a partial threshold

**Mistake**: Filer who married in October computes Form 8959 using "9 months at $200K threshold + 3 months at $250K threshold."

**Why it happens**: Intuition that thresholds prorate.

**Fix**: The threshold is by *filing status used on the return* applied to *full-year* wages and SE income. A couple married in October who files MFJ for the year uses $250K against full-year combined wages. A couple who files MFS uses $125K each against their own full-year wages. No proration.

**Citation**: IRC §3101(b)(2) — threshold is annual, not pro-rata; IRS Pub. 505.

## 11. Computing the surtax on the SS wage base ceiling

**Mistake**: Filer applies the Social Security wage base ($176,100 for 2025) as the Form 8959 threshold.

**Why it happens**: Confusing the SS wage base (which is inflation-adjusted and caps the 12.4% SS tax) with the Additional Medicare Tax threshold (which is statutory and uncapped).

**Fix**: Medicare tax (regular 1.45% and additional 0.9%) has **no wage base ceiling**. It applies to every dollar of wages and SE income. The Form 8959 threshold ($200K / $250K / $125K) is unrelated to the SS wage base.

**Citation**: IRC §3121(a) (no wage base on Medicare tax); IRC §3101(b)(2).

## 12. Forgetting the surtax on year-end bonuses

**Mistake**: Filer at $190K base salary plus $30K Q4 bonus assumes their employer is withholding correctly.

**Why it happens**: Throughout the year, the filer was under $200K from this employer. Q4 bonus pushes year-to-date wages over $200K, triggering the employer's obligation under IRC §3102(f).

**Fix**: The employer is responsible for catching this — payroll systems should compute year-to-date wages on each payroll run and trigger the additional 0.9% withholding once the YTD total exceeds $200K. If the W-2 Box 6 reflects this correctly, Line 21 on Form 8959 will show the additional withholding. If it doesn't (employer error), the filer still owes via Line 18 and must pay at filing — separate question of whether the employer owes a payroll correction.

**Citation**: IRC §3102(f); Treasury Reg. §31.3102-4(a).

## Sources

- IRC §1401(b)(2), §3101(b)(2), §3102(f), §1402(a)(12), §1411
- Treasury Reg. §31.3102-4
- [Form 8959 (latest)](https://www.irs.gov/pub/irs-pdf/f8959.pdf)
- [Instructions for Form 8959 (latest)](https://www.irs.gov/pub/irs-pdf/i8959.pdf)
- [Publication 505](https://www.irs.gov/pub/irs-pdf/p505.pdf)
- [About Form 8959](https://www.irs.gov/forms-pubs/about-form-8959)
