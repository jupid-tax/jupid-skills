# REIT Section 199A Dividends and PTP Income

Section 199A applies not only to qualified business income from sole props, partnerships, and S-corps, but also to qualified dividends from real estate investment trusts (REITs) and qualified income from publicly traded partnerships (PTPs). These are reported on Form 8995 separately from QBI on Lines 6–9 (2025 Form 8995).

---

## REIT Section 199A dividends

### What they are

REITs (publicly traded or non-traded) distribute dividends to shareholders. A portion of those dividends — generally the portion attributable to the REIT's qualified business income — is designated as "Section 199A dividends" and qualifies for the 20% deduction.

### Where reported on 1099-DIV

**Form 1099-DIV, Box 5: Section 199A dividends**

This is the starting figure for Form 8995 Line 6. It is a subset of Box 1a (total ordinary dividends), separate from Box 1b: a qualified REIT dividend is never a qualified dividend under §1(h)(11), so Box 1b + Box 5 ≤ Box 1a.

### Common REIT examples

- Public REITs: Realty Income (O), Vanguard REIT ETF (VNQ), Schwab US REIT ETF (SCHH)
- Non-traded REITs distributed through brokers
- Mortgage REITs (mREITs)

### Pitfall: Using Box 1a instead of Box 5

Box 1a is total ordinary dividends, including non-§199A portions (e.g., dividends from C-corp investments held by the REIT). Only Box 5 qualifies for the §199A deduction. Always use Box 5.

### Multiple 1099-DIVs

If the filer has multiple brokerage accounts (Schwab, Fidelity, Vanguard, etc.), each issues a separate 1099-DIV with its own Box 5. Sum all Box 5 amounts into a single Line 6 entry on Form 8995.

### Holding period requirement

Per Treas. Reg. §1.199A-3(c)(2)(ii), a REIT dividend is not a qualified REIT dividend if the share was held for **45 days or less** during the 91-day period beginning 45 days before the ex-dividend date, or to the extent the holder is obligated to make related payments (short sales, hedges).

Box 5 does not apply this test for the taxpayer: the 1099-DIV recipient instructions say Box 5 "shows the portion of the amount in box 1a that may be eligible" for the deduction. Ask whether any REIT shares (or REIT fund shares) were bought and sold around a dividend date; if yes, exclude dividends on positions held 45 days or less.

### REIT capital gain distributions

REIT capital gain distributions (Box 2a of 1099-DIV) are **not** Section 199A dividends. They are taxed as long-term capital gains separately. Do not include in Line 6.

---

## Publicly Traded Partnership (PTP) income

### What they are

PTPs are partnerships whose interests are publicly traded on a securities exchange. Common examples include energy MLPs (Enterprise Products Partners — EPD, Energy Transfer — ET, MPLX) and some real estate partnerships.

### How qualified PTP income is reported

Unlike REIT 1099-DIVs, PTP income is reported on a Schedule K-1 issued by the PTP. The K-1 Section 199A statement (Box 20 code Z for partnership K-1) reports the qualified PTP income separately.

### What to put on Form 8995 Line 6

Sum of qualified PTP income from all PTP K-1s, plus REIT Section 199A dividends from all 1099-DIV Box 5 amounts.

### PTP losses

If a PTP K-1 reports a loss in the §199A statement, enter it as a negative number aggregated into Line 6. If Line 6 + Line 7 is negative, Line 8 = 0 and the negative amount goes on Line 17, which carries to next year's Line 7.

### Pitfall: Treating PTP K-1 ordinary income as QBI

PTP income goes on **Line 6** of Form 8995, not Line 1. Qualified PTP income is excluded from QBI by §199A(c)(1) and has its own line.

Symmetrically: ordinary partnership K-1 (non-PTP) goes on Line 1 as QBI, not Line 6.

---

## Combining REIT dividends and PTP income

Form 8995 combines both into Line 6 with no separation. The 20% rate applies equally. Line 8 (after carryforward) is multiplied by 20% on Line 9.

Example:

- REIT Box 5 (broker A): $200
- REIT Box 5 (broker B): $150
- PTP K-1 §199A income (EPD): $80
- PTP K-1 §199A income (ET): $40

Line 6 = $200 + $150 + $80 + $40 = $470
Line 8 = $470 (assuming no prior-year loss)
Line 9 = $470 × 0.20 = $94

That $94 is a small but real addition to Line 10.

---

## REIT/PTP loss carryforward mechanics

Per Treas. Reg. §1.199A-1(c)(2)(ii), if Line 6 + Line 7 is negative, the REIT/PTP component is zero and the negative amount carries forward to offset REIT dividends and PTP income in later years. The loss does not offset current-year QBI on Line 4 — REIT/PTP and QBI are siloed.

Tracking:
- Year 1: Line 6 = $100, Line 7 = $0 → Line 8 = $100, Line 9 = $20. Line 17 = $0.
- Year 2: Line 6 = -$50 (PTP K-1 loss), Line 7 = $0 → sum -$50 → Line 8 = $0, Line 9 = $0. Line 17 = -$50, to Year 3 Line 7.
- Year 3: Line 6 = $80, Line 7 = -$50 → Line 8 = $30, Line 9 = $6.

The agent must record the carryforward in workpapers and surface it to the user for next year's filing.

---

## Common mistakes

### Mistake 1: Putting REIT dividends on Line 1 instead of Line 6

REIT income is **not** QBI. It has its own line. Putting it on Line 1 gives the same numerical result mathematically (still 20%), but the IRS line items will be wrong and the form may be rejected.

### Mistake 2: Using 1099-DIV Box 1a (total dividends) on Line 6

Box 1a includes non-§199A ordinary dividends. Only Box 5 qualifies. Always use Box 5.

### Mistake 3: Including REIT capital gain distributions on Line 6

Box 2a (total capital gain distributions) is taxed separately and does not qualify for §199A. Exclude.

### Mistake 4: Treating non-traded REIT distributions as Line 6 income

Non-traded REIT distributions may include return of capital, capital gain, or ordinary dividends. Only the Section 199A portion (typically reported on the brokerage 1099-DIV Box 5 if the broker custody-holds the non-traded REIT) qualifies. If the non-traded REIT issues its own statement directly to the investor (no brokerage intermediary), use the §199A figure from that statement.

### Mistake 5: Skipping Line 6 when REIT income is small

Even $50 of REIT Section 199A dividends produces $10 of additional deduction on Line 9. It compounds with QBI. Always include if reported on 1099-DIV Box 5.
