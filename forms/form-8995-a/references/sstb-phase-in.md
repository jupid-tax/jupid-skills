# SSTB Phase-In Computation (Schedule A and Part III)

When taxable income before the QBI deduction is in the phase-in range (between the threshold and the threshold plus the phase-in range), two separate reductions can apply:

1. **Schedule A (SSTBs only):** only an applicable percentage of the SSTB's QBI, W-2 wages, and UBIA is taken into account (IRC §199A(d)(3); Treas. Reg. §1.199A-1(d)(2), referenced in §1.199A-5(a)).
2. **Part III (any business, SSTB or not):** if the W-2/UBIA limit (line 10) is less than 20% of QBI (line 3), the limit is phased in rather than applied in full (IRC §199A(b)(3)(B)).

This reference walks through both with worked examples. Sources: 2025 Form 8995-A Parts II–III, 2025 Schedule A (Form 8995-A), 2025 Instructions for Form 8995-A.

---

## Phase-in ranges

| Tax year | Filing status | Threshold | Phase-in range | Top of phase-in |
|----------|---------------|-----------|----------------|------------------|
| 2025 | All except MFJ | $197,300 | $50,000 | $247,300 |
| 2025 | MFJ | $394,600 | $100,000 | $494,600 |
| 2026 | Single / HOH / QSS | $201,750 | $75,000 | $276,750 |
| 2026 | MFS | $201,775 | $75,000 | $276,775 |
| 2026 | MFJ | $403,500 | $150,000 | $553,500 |

Sources: Rev. Proc. 2024-40 §2.27; Rev. Proc. 2025-32 §4.26; P.L. 119-21 §70105 (range widened for tax years beginning after 2025).

If taxable income before QBI is:
- ≤ threshold → no limits; use Form 8995 unless a cooperative patron
- In the range → Schedule A for SSTBs; Part III for any business with line 10 < line 3
- > top → SSTB's QBI, W-2 wages, and UBIA are not taken into account at all; non-SSTBs take the W-2/UBIA limit in full

---

## Schedule A (Part I) line walkthrough

| Line | Item | Formula |
|------|------|---------|
| 1a / 1b | Trade name / TIN | (text) |
| 2 | QBI | from the business |
| 3 | W-2 wages | from the business |
| 4 | UBIA | from the business |
| 5 | Taxable income before QBI | Form 1040 line 11a − 12e − 13b (2025) |
| 6 | Threshold | from table |
| 7 | Excess | L5 − L6 |
| 8 | Phase-in range | $50,000 or $100,000 (2025) |
| 9 | Ratio | L7 ÷ L8 |
| 10 | Applicable percentage | 100% − L9 |
| 11 | QBI × L10 | → Form 8995-A line 2 (or Schedule C (Form 8995-A)) |
| 12 | W-2 wages × L10 | → Form 8995-A line 4 |
| 13 | UBIA × L10 | → Form 8995-A line 7 |

The instructions do not prescribe decimal places for the percentage. Keep full precision (at least 5 decimals) and state the precision in the draft.

## Part III line walkthrough

| Line | Formula |
|------|---------|
| 17 | Line 3 |
| 18 | Line 10 |
| 19 | L17 − L18 |
| 20 | Taxable income before QBI |
| 21 | Threshold |
| 22 | L20 − L21 |
| 23 | Phase-in range |
| 24 | L22 ÷ L23 |
| 25 | L19 × L24 |
| 26 | L17 − L25 → line 12 |

Then line 13 = greater of line 11 or line 12.

---

## Worked Example A — Lawyer in Phase-In, Wages Don't Bind (2025, single)

**Inputs:**
- Taxable income before QBI: $215,350
- Business: SSTB (law firm)
- QBI: $200,000
- W-2 wages paid by firm (paralegal + receptionist): $120,000
- UBIA: $30,000 (computers, furniture)

**Schedule A:**
- L6 threshold: $197,300
- L7 excess: $215,350 − $197,300 = $18,050
- L8 range: $50,000
- L9: 18,050 / 50,000 = 0.36100
- L10 applicable %: 63.900%
- L11 QBI: $200,000 × 0.639 = $127,800
- L12 W-2: $120,000 × 0.639 = $76,680
- L13 UBIA: $30,000 × 0.639 = $19,170

**Part II:**
- L2 $127,800; L3 $25,560
- L4 $76,680; L5 $38,340; L6 $19,170
- L7 $19,170; L8 $479; L9 $19,649
- L10 $38,340; L11 min($25,560, $38,340) = $25,560
- Line 10 ≥ line 3 → Part III not used; L12 $0
- L13 = max($25,560, $0) = **$25,560**

The deduction from this business fell from $40,000 (20% of $200,000) to $25,560: exactly the 36.1% phase-in. Wages were ample, so the W-2/UBIA limit didn't bind.

---

## Worked Example B — Solo Doctor in Phase-In, Wages Bind (2025, single)

**Inputs:**
- Taxable income before QBI: $230,350
- Business: SSTB (medical practice)
- QBI: $254,684
- W-2 wages paid: $80,000
- UBIA: $50,000

**Schedule A:**
- L7 excess: $230,350 − $197,300 = $33,050
- L9: 33,050 / 50,000 = 0.66100; L10 applicable %: 33.900%
- L11 QBI: $254,684 × 0.339 = $86,338
- L12 W-2: $80,000 × 0.339 = $27,120
- L13 UBIA: $50,000 × 0.339 = $16,950

**Part II:**
- L2 $86,338; L3 $17,268
- L4 $27,120; L5 $13,560; L6 $6,780
- L7 $16,950; L8 $424; L9 $7,204
- L10 $13,560; L11 min($17,268, $13,560) = $13,560

**Part III** (line 10 < line 3, taxable income in range):
- L17 $17,268; L18 $13,560; L19 $3,708
- L22 $33,050; L23 $50,000; L24 66.100%
- L25 $3,708 × 0.661 = $2,451
- L26 $17,268 − $2,451 = $14,817 → L12

**L13** = max($13,560, $14,817) = **$14,817**

Both reductions apply: Schedule A cut QBI, wages, and UBIA to 33.9%, then Part III phased in the wage limit instead of applying it in full.

---

## Worked Example C — Near the Top of the Range, No Wages (2025, MFJ)

**Inputs:**
- Taxable income before QBI: $490,700
- Business: SSTB (consulting)
- QBI: $200,000
- W-2 wages: $0 (solo consultant, no employees); UBIA $0

**Schedule A:**
- L7 excess: $490,700 − $394,600 = $96,100
- L8 range: $100,000; L9 0.96100; L10 3.900%
- L11 QBI: $200,000 × 0.039 = $7,800; L12 $0; L13 $0

**Part II:** L2 $7,800; L3 $1,560; L10 $0; L11 $0

**Part III:** L17 $1,560; L18 $0; L19 $1,560; L24 96.100%; L25 $1,499; L26 $61 → L12

**L13** = max($0, $61) = **$61**

A solo SSTB consultant with no W-2 wages keeps almost nothing near the top of the range, but not zero: Part III still allows the unphased remainder.

---

## Worked Example D — Above the Top of the Range (2025, single)

**Inputs:**
- Taxable income before QBI: $300,000
- Business: SSTB (financial advisor)
- QBI: $250,000

$300,000 > $247,300 (top of the 2025 range for all returns other than MFJ). The SSTB is not a qualified trade or business: no QBI, W-2 wages, or UBIA from it are taken into account (2025 i8995-A, "SSTBs excluded from your qualified trades or businesses"). No Schedule A. Its contribution to the deduction is $0.

---

## Common errors

1. **Forgetting Schedule A entirely**: filing software may apply only the W-2/UBIA limit. Confirm Schedule A is generated for every SSTB in the range.

2. **Using the wrong phase-in range**: 2025 is $50,000 for all returns except MFJ ($100,000); 2026 is $75,000 / $150,000 MFJ.

3. **Phase-in calculated on AGI instead of taxable income before QBI**: it's taxable income (2025 Form 1040 line 11a − 12e − 13b), NOT AGI.

4. **Rounding the percentage early**: keep at least 5 decimals; a 2-decimal percentage can move the result by tens of dollars.

5. **Applying Schedule A to non-SSTB businesses**: only SSTBs use Schedule A. Non-SSTBs in the range still use Part III when line 10 < line 3.

6. **Skipping Part III**: line 13 is the greater of line 11 or line 12, so leaving Part III blank when it applies understates the deduction (Example B: $13,560 instead of $14,817).
