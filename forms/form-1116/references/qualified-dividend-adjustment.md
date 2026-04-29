# Line 15 — Qualified Dividend / Long-Term Capital Gain Rate Adjustment

The §904(b)(2)(B) adjustment is one of the most-skipped lines on Form 1116. It prevents over-claiming the FTC when foreign-source qualified dividends or long-term capital gains are taxed at preferential US rates (0% / 15% / 20%) instead of ordinary rates.

## Why the adjustment exists

The §904 limitation fraction is:

```
Line 19 = Foreign-source taxable income / Total taxable income
```

When foreign income includes QD or LTCG taxed at, say, 15% (instead of 24% ordinary), the foreign income's share of US tax is smaller than its share of taxable income. Without an adjustment, Line 19 would over-credit — the limitation would let the user claim FTC against US tax that wasn't actually owed on the foreign income.

The adjustment scales down foreign-source taxable income on Line 17 to reflect the effective US tax rate on QD/LTCG.

## When to make the adjustment

The user must adjust Line 15 if:

- They have foreign-source qualified dividends, **AND/OR**
- They have foreign-source net long-term capital gains, **AND**
- Either is taxed at a US preferential rate (0% / 15% / 20%)

There's a **de-minimis exception**: if all of the following are true, the user can skip the adjustment (per Pub 514 / Form 1116 instructions):

- Foreign-source net QD + LTCG ≤ $20,000 (in some years; verify the current threshold in the latest Form 1116 instructions before relying)
- Filer's tentative US tax (line 16 of 1040) ≤ approximately the 24% bracket threshold (verify current year)
- Filer is in the 32% bracket or lower

Most retail filers with modest 1099-DIV box 7 amounts ($300-$1,800) and ordinary brackets qualify for the de-minimis exception and Line 15 is 0.

## The adjustment formula (when required)

Per Form 1116 instructions, the Line 15 adjustment effectively reduces foreign-source taxable income by the rate differential.

Simplified mechanics for a filer with **foreign QD only** taxed at 15%:

```
Adjustment ratio = (Highest ordinary rate) / 15% − 1
                 = approximately 24/15 − 1 = 0.6 (for a filer in the 24% bracket)
```

Wait — the actual mechanic in the IRS worksheet inverts this. The instructions provide a worksheet that does the following:

1. Compute "remaining" foreign QD/LTCG after de-minimis tests
2. Multiply by an adjustment factor based on the user's bracket
3. Subtract from foreign-source taxable income on Line 17

The math comes out so that the foreign QD/LTCG effectively appears in Line 17 at its **rate-equivalent** — i.e., $1,000 of foreign QD at 15% effective rate counts as ~$625 in the limitation numerator (when the user is in the 24% bracket).

**Example**: filer has $10,000 foreign QD, all at 15% rate, filer is in 24% bracket.

- Adjustment = $10,000 × (1 − 15/24) = $10,000 × 0.375 = $3,750
- Line 15 = $3,750
- Line 17 = Line 14 − $3,750

The exact factors are in the Form 1116 instructions worksheet for Line 18 — verify each year. The IRS occasionally changes the bracket thresholds.

## Practical agent workflow

1. **Ask** if the user has any foreign-source qualified dividends OR foreign-source net LTCG
2. If yes, **ask** the total amount and verify it's reported on the 1099-DIV / 8949 / Schedule D in the qualified-rate category
3. Check the de-minimis exception:
   - Total foreign QD + LTCG ≤ $20,000?
   - Filer's bracket ≤ ~32%?
   - If both yes → Line 15 = 0; document why
4. If the de-minimis doesn't apply, follow the Line 18 worksheet in the Form 1116 instructions step by step. Don't try to derive it; the worksheet handles edge cases.

## Why this matters

- If the agent skips Line 15 when required, the user's FTC is overstated. The IRS recomputes on audit and assesses tax + interest.
- If the agent makes the adjustment when it wasn't required (e.g., filer is in 32% bracket but has only $5,000 foreign QD), the agent under-credits and the user loses some FTC. Less catastrophic but still wrong.
- Tax software handles this correctly when the user marks foreign QD on the 1099-DIV import. Manual filers (FFFF, paper) often miss it.

## What the agent should NOT do

- Do not default to Line 15 = 0 without checking the de-minimis criteria
- Do not apply the adjustment to ordinary foreign dividends (those are taxed at ordinary rates; no rate differential)
- Do not apply the adjustment to short-term capital gains (taxed at ordinary rates)
- Do not apply the adjustment to foreign qualified dividends that are taxed in the US at 0% (filer in the lowest bracket; no adjustment because the US rate is below the foreign rate, no over-credit risk)

## Cross-reference

- Form 1116 Instructions, "Worksheet for Determining the Adjustment for Foreign Source Qualified Dividends and Capital Gains" (IRS revises annually)
- Pub 514, chapter on §904(b) adjustments
- IRC §904(b)(2)(B)
- Reg. §1.904(b)-1
