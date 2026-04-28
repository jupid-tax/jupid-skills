# REIT Section 199A Dividends and PTP Income

Section 199A applies not only to qualified business income from sole props, partnerships, and S-corps, but also to qualified dividends from real estate investment trusts (REITs) and qualified income from publicly traded partnerships (PTPs). These are reported on Form 8995 separately from QBI on Lines 5-7.

---

## REIT Section 199A dividends

### What they are

REITs (publicly traded or non-traded) distribute dividends to shareholders. A portion of those dividends — generally the portion attributable to the REIT's qualified business income — is designated as "Section 199A dividends" and qualifies for the 20% deduction.

### Where reported on 1099-DIV

**Form 1099-DIV, Box 5: Section 199A dividends**

This is the figure to use on Form 8995 Line 5. It is a subset of Box 1a (total ordinary dividends) — Box 5 ≤ Box 1a.

### Common REIT examples

- Public REITs: Realty Income (O), Vanguard REIT ETF (VNQ), Schwab US REIT ETF (SCHH)
- Non-traded REITs distributed through brokers
- Mortgage REITs (mREITs)

### Pitfall: Using Box 1a instead of Box 5

Box 1a is total ordinary dividends, including non-§199A portions (e.g., dividends from C-corp investments held by the REIT). Only Box 5 qualifies for the §199A deduction. Always use Box 5.

### Multiple 1099-DIVs

If the filer has multiple brokerage accounts (Schwab, Fidelity, Vanguard, etc.), each issues a separate 1099-DIV with its own Box 5. Sum all Box 5 amounts into a single Line 5 entry on Form 8995.

### Holding period requirement

Per IRC §199A(e)(3), Section 199A dividends qualify for the 20% deduction only if the taxpayer has held the REIT shares for **more than 45 days** during the 91-day period beginning 45 days before the ex-dividend date.

The brokerage applies this rule before reporting Box 5 — Box 5 already excludes dividends on shares that didn't meet the holding period. The agent does not need to re-check holding periods unless the filer has unusual circumstances (recent share lending, hedging, etc.).

### REIT capital gain distributions

REIT capital gain distributions (Box 2a of 1099-DIV) are **not** Section 199A dividends. They are taxed as long-term capital gains separately. Do not include in Line 5.

---

## Publicly Traded Partnership (PTP) income

### What they are

PTPs are partnerships whose interests are publicly traded on a securities exchange. Common examples include energy MLPs (Enterprise Products Partners — EPD, Energy Transfer — ET, MPLX) and some real estate partnerships.

### How qualified PTP income is reported

Unlike REIT 1099-DIVs, PTP income is reported on a Schedule K-1 issued by the PTP. The K-1 Section 199A statement (Box 20 code Z for partnership K-1) reports the qualified PTP income separately.

### What to put on Form 8995 Line 5

Sum of qualified PTP income from all PTP K-1s, plus REIT Section 199A dividends from all 1099-DIV Box 5 amounts.

### PTP losses

If a PTP K-1 reports a loss in the §199A statement, enter it as a negative number aggregated into Line 5. If the total Line 5 + Line 6 is negative, the form's mechanics push the loss to Line 7 = 0 and the negative carries to next year's Line 6.

### Pitfall: Treating PTP K-1 ordinary income as QBI

PTP income goes on **Line 5** of Form 8995, not Line 1. PTPs are explicitly carved out from QBI in §199A(c)(3) and have their own line.

Symmetrically: ordinary partnership K-1 (non-PTP) goes on Line 1 as QBI, not Line 5.

---

## Combining REIT dividends and PTP income

Form 8995 combines both into Line 5 with no separation. The 20% rate applies equally. Line 7 (after carryforward) is multiplied by 20% on Line 11.

Example:

- REIT Box 5 (broker A): $200
- REIT Box 5 (broker B): $150
- PTP K-1 §199A income (EPD): $80
- PTP K-1 §199A income (ET): $40

Line 5 = $200 + $150 + $80 + $40 = $470
Line 7 = $470 (assuming no prior-year loss)
Line 11 = $470 × 0.20 = $94

That $94 is a small but real addition to Line 12.

---

## REIT/PTP loss carryforward mechanics

Per IRC §199A(c)(2), if Line 5 + Line 6 is negative, that negative amount is treated as a "qualified REIT dividends and qualified PTP loss carryforward" and carries to next year. The loss does not offset current-year QBI on Line 4 — REIT/PTP and QBI are siloed.

Tracking:
- Year 1: Line 5 = $100, Line 6 = $0 → Line 7 = $100, Line 11 = $20. Carryforward = $0.
- Year 2: Line 5 = -$50 (PTP K-1 loss), Line 6 = $0 → sum -$50 → Line 7 = $0, Line 11 = $0. Carryforward = -$50 to Year 3 Line 6.
- Year 3: Line 5 = $80, Line 6 = -$50 → Line 7 = $30, Line 11 = $6.

The agent must record the carryforward in workpapers and surface it to the user for next year's filing.

---

## Common mistakes

### Mistake 1: Putting REIT dividends on Line 1 instead of Line 5

REIT income is **not** QBI. It has its own line. Putting it on Line 1 gives the same numerical result mathematically (still 20%), but the IRS line items will be wrong and the form may be rejected.

### Mistake 2: Using 1099-DIV Box 1a (total dividends) on Line 5

Box 1a includes non-§199A ordinary dividends. Only Box 5 qualifies. Always use Box 5.

### Mistake 3: Including REIT capital gain distributions on Line 5

Box 2a (long-term capital gain distributions) is taxed separately and does not qualify for §199A. Exclude.

### Mistake 4: Treating non-traded REIT distributions as Line 5 income

Non-traded REIT distributions may include return of capital, capital gain, or ordinary dividends. Only the Section 199A portion (typically reported on the brokerage 1099-DIV Box 5 if the broker custody-holds the non-traded REIT) qualifies. If the non-traded REIT issues its own statement directly to the investor (no brokerage intermediary), use the §199A figure from that statement.

### Mistake 5: Skipping Line 5 when REIT income is small

Even $50 of REIT Section 199A dividends produces $10 of additional deduction on Line 11. It compounds with QBI. Always include if reported on 1099-DIV Box 5.
