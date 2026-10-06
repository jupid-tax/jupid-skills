# Qualified Dividend / Capital Gain Rate Adjustments (Lines 1a, 5, and 18)

The §904(b)(2)(B) adjustments are among the most-skipped steps on Form 1116. They prevent over-claiming the FTC when qualified dividends or capital gains are taxed at preferential US rates (0% / 15% / 20%) instead of ordinary rates. On the 2025 form there is **no separate "adjustment line"**: foreign amounts are scaled down where they enter Part I (line 1a for gains and dividends, line 5 for losses), and worldwide amounts are scaled down on line 18 through the Worksheet for Line 18 (2025 Instructions for Form 1116, "Foreign Qualified Dividends and Capital Gains (Losses)" and "Line 18").

## Why the adjustment exists

The §904 limitation fraction is:

```
Line 19 = Line 17 (net foreign-source taxable income) / Line 18 (taxable income)
```

When foreign income includes qualified dividends or long-term gains taxed at 15% instead of up to 37%, the foreign income's share of US tax is smaller than its share of taxable income. Without an adjustment, line 19 would let the user claim credit against US tax that the foreign income never generated. The factors in the instructions convert each preferential-rate dollar into its ordinary-rate equivalent: 0.4054 ≈ 15/37 and 0.5405 ≈ 20/37.

## When adjustments are required

Individuals who used the Qualified Dividends and Capital Gain Tax Worksheet (QDCGTW) and don't file Schedule D must adjust foreign qualified dividends and capital gain distributions if **both**:

- QDCGTW line 5 is greater than zero, and
- QDCGTW line 23 is less than line 24.

Schedule D filers have parallel tests (QDCGTW line 5 / lines 23-24, or Schedule D Tax Worksheet line 18 > 0 and line 45 < line 46). Estates and trusts use the Form 1041 worksheet tests. Foreign capital gains and losses of Schedule D filers are adjusted with Worksheet A or Worksheet B (or Pub. 514 when neither applies).

## The adjustment exception (2025 amounts)

The filer can elect not to adjust (by simply not adjusting any item) if **both** are true:

1. QDCGTW line 5 (or Schedule D Tax Worksheet line 18) doesn't exceed **$394,600** (married filing jointly or qualifying surviving spouse) or **$197,300** (single, head of household, married filing separately); and
2. Foreign-source qualified dividends plus foreign-source capital gain distributions (Schedule D filers: foreign-source net capital gain) total **less than $20,000**.

Rules that come with the election:

- It is all or nothing: if the filer elects not to adjust, no foreign qualified dividend or capital gain is adjusted on line 1a, and the Worksheet for Line 18 is not completed (line 18 = plain taxable income as defined for line 18).
- If any foreign item was adjusted on line 1a or line 5, the exception can't be used for line 18; complete the Worksheet for Line 18.
- AMT filers: special rules in Reg. §1.904(b)-1(b)(3).
- Ignore amounts the filer elected to include on Form 4952 line 4g; those enter line 1a unadjusted.

The dollar thresholds are year-specific (they track the start of the 32% bracket). Re-check them in the current Instructions for Form 1116.

## How to adjust foreign amounts (line 1a and line 5)

| Foreign item taxed at | Enter on line 1a |
|-----------------------|------------------|
| 0% rate | Nothing (leave it off line 1a) |
| 15% rate | Amount × 0.4054 |
| 20% rate | Amount × 0.5405 |
| Ordinary rates (non-qualified dividends, short-term gains) | Full amount, no adjustment |

Foreign capital losses go on line 5 after the Worksheet A / Worksheet B adjustments (long-term losses × 0.4054 in Worksheet B line 15). Lines 3d and 3e still use the **unadjusted** amounts.

## Worksheet for Line 18 (worldwide adjustment)

When required (QDCGTW line 5 > 0 and line 23 < line 24, and no exception), line 18 comes from this worksheet instead of plain taxable income:

```
1.  Form 1040 line 11b − line 14 + Schedule 1-A line 37
2.  Worldwide 28% gains                         × 0.2432 = line 3
4.  Worldwide 25% gains                         × 0.3243 = line 5
6.  Worldwide 20% gains and qualified dividends × 0.4595 = line 7
8.  Worldwide 15% gains and qualified dividends × 0.5946 = line 9
10. Worldwide 0% gains and qualified dividends  (full amount)
11. Lines 3 + 5 + 7 + 9 + 10
12. Line 1 − line 11 → Form 1116 line 18 (zero or less: 0)
```

For QDCGTW filers: line 6 = QDCGTW line 20, line 8 = QDCGTW line 17, line 10 = QDCGTW line 9 (lines 2-5 skipped). Schedule D Tax Worksheet filers take lines 2, 4, 6, 8, 10 from Schedule D Tax Worksheet lines 42, 39, 33, 30, 22.

**Worked example (illustrative, 2025 single, all qualified dividends taxed at 15%):**

- Case A: taxable income $150,000, of which $20,000 is qualified dividends ($12,000 foreign). QDCGTW line 5 = $130,000 (≤ $197,300) and foreign qualified dividends $12,000 (< $20,000), so both exception tests pass. If the filer elects the exception, line 1a includes the $12,000 unadjusted and line 18 is plain taxable income.
- Case B: same filer but $33,000 of qualified dividends, $25,000 foreign. Test 2 fails ($25,000 ≥ $20,000). Line 1a gets $25,000 × 0.4054 = $10,135. Worksheet for Line 18: line 1 = $150,000; line 8 = $33,000 (QDCGTW line 17); line 9 = $33,000 × 0.5946 = $19,622; line 12 = $150,000 − $19,622 = $130,378 → Form 1116 line 18.

## Practical agent workflow

1. **Ask** if the user has any foreign-source qualified dividends, capital gain distributions, or foreign capital gains/losses, and which rate bracket (0/15/20%) applies. Get the QDCGTW or Schedule D Tax Worksheet from the return.
2. Check the two adjustment-exception tests above. If both pass, ask the user whether to use the exception; document the choice.
3. If the exception doesn't apply or isn't elected: adjust each foreign item on line 1a / line 5 per the table, and complete the Worksheet for Line 18.
4. Keep lines 3d and 3e unadjusted.

## What the agent should NOT do

- Do not put a separate "QD adjustment" on line 16; line 16 is for loss allocations and recaptures
- Do not adjust ordinary (non-qualified) foreign dividends or short-term gains
- Do not include 0%-rate foreign qualified dividends on line 1a when adjusting; leaving them off is the adjustment
- Do not mix: adjusting some foreign items and electing the exception for others is not allowed

## Cross-reference

- 2025 Instructions for Form 1116: "Foreign Qualified Dividends and Capital Gains (Losses)" (pp. 9-16) and "Line 18" with the Worksheet for Line 18 (pp. 23-24)
- Pub. 514, "Qualified Dividends" and "Capital Gains and Losses"
- IRC §904(b)(2)(B)
- Reg. §1.904(b)-1
