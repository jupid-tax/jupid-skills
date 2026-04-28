# SSTB Phase-In Computation (Schedule A)

When an SSTB owner's taxable income is in the phase-in zone (between the threshold and the threshold + phase-in width), the §199A deduction is REDUCED by an applicable percentage. This reference walks through the math with worked examples.

---

## Phase-in zones (2025; verify 2026 figures)

| Filing status | Threshold | Phase-in width | Top of phase-in |
|---------------|-----------|----------------|------------------|
| Single / HoH / MFS | $241,950 | $50,000 | $291,950 |
| MFJ / QSS | $483,900 | $100,000 | $583,900 |

If taxable income before QBI is:
- ≤ threshold → no phase-in; use Form 8995 (simplified)
- In zone → Schedule A applies; partial deduction
- ≥ top → SSTB deduction = $0

---

## The applicable percentage formula

```
phase_in_pct = (taxable_income_before_QBI − threshold) / phase_in_width
applicable_pct = 1 − phase_in_pct
```

`phase_in_pct` is the fraction of QBI you LOSE. `applicable_pct` is the fraction you KEEP.

Compute to at least 4 decimal places per the instructions; commercial software typically uses 6.

---

## Schedule A line walkthrough

| Line | Item | Formula |
|------|------|---------|
| 1 | Trade name | (text) |
| 2 | Taxable income before QBI | from Form 1040 |
| 3 | Threshold for status | from table |
| 4 | Excess (L2 − L3) | math |
| 5 | Phase-in range | $50K or $100K |
| 6 | Phase-in % | L4 / L5 |
| 7 | Applicable % | 1 − L6 |
| 8 | Reduced QBI | original QBI × L7 |
| 9 | Reduced W-2 wages | original W-2 × L7 |
| 10 | Reduced UBIA | original UBIA × L7 |
| 11 | W-2/UBIA limit on reduced amounts | max(50% × L9, 25% × L9 + 2.5% × L10) |
| 12 | Tentative deduction on reduced amounts | min(20% × L8, L11) |
| 13 | Phase-in reduction → Part II L12 | (Part II L11) − L12 |

---

## Worked Example A — Lawyer in Phase-In, Wages Don't Bind

**Inputs:**
- Filing status: Single
- Taxable income before QBI: $260,000
- Business: SSTB (law firm)
- QBI: $200,000
- W-2 wages paid by firm (paralegal + receptionist): $120,000
- UBIA: $30,000 (computers, furniture)

**Schedule A:**
- L3 threshold: $241,950
- L4 excess: $260,000 − $241,950 = $18,050
- L5 width: $50,000
- L6 phase-in %: 18,050 / 50,000 = 0.3610
- L7 applicable %: 1 − 0.3610 = 0.6390
- L8 reduced QBI: $200,000 × 0.6390 = $127,800
- L9 reduced W-2: $120,000 × 0.6390 = $76,680
- L10 reduced UBIA: $30,000 × 0.6390 = $19,170
- L11 W-2/UBIA limit on reduced: max(50% × 76,680, 25% × 76,680 + 2.5% × 19,170) = max(38,340, 19,170 + 479) = max(38,340, 19,649) = $38,340
- L12 tentative on reduced: min(20% × 127,800, 38,340) = min(25,560, 38,340) = $25,560

**Part II for the same business (without Schedule A):**
- L2 QBI: $200,000
- L3 20% × QBI: $40,000
- L4 W-2: $120,000
- L5 50% × W-2: $60,000
- L9 25%×W2 + 2.5%×UBIA: 30,000 + 750 = $30,750
- L10 max(L5, L9): $60,000
- L11 min(L3, L10): $40,000

**L13 phase-in reduction (Schedule A → Part II L12):**
L11 (Part II) − L12 (Schedule A) = $40,000 − $25,560 = **$14,440**

**Adjusted QBI (Part II L13):**
L11 − L12 = $40,000 − $14,440 = **$25,560**

The deduction was reduced from a possible $40,000 to $25,560 — a $14,440 (36.1%) loss matching the phase-in percentage. Wages and UBIA were ample, so the W-2/UBIA limit didn't bind.

---

## Worked Example B — Solo Doctor in Phase-In, Wages Bind

**Inputs:**
- Filing status: Single
- Taxable income before QBI: $275,000
- Business: SSTB (medical practice)
- QBI: $254,684 (after SE-tax / SE-HI / SEP-IRA reductions to Schedule C profit of $300,000)
- W-2 wages paid: $80,000
- UBIA: $50,000

**Schedule A:**
- L4 excess: $275,000 − $241,950 = $33,050
- L6 phase-in %: 33,050 / 50,000 = 0.6610
- L7 applicable %: 0.3390
- L8 reduced QBI: $254,684 × 0.3390 = $86,338
- L9 reduced W-2: $80,000 × 0.3390 = $27,120
- L10 reduced UBIA: $50,000 × 0.3390 = $16,950
- L11 W-2/UBIA on reduced: max(50% × 27,120, 25% × 27,120 + 2.5% × 16,950) = max(13,560, 7,204) = $13,560
- L12 tentative: min(20% × 86,338, 13,560) = min(17,268, 13,560) = $13,560

**Part II without Schedule A:**
- L3 20% × QBI: $254,684 × 20% = $50,937
- L11 = min(50,937, max(40,000, 21,250)) — assume W-2/UBIA limit = $40,000 (50% × $80,000) — so L11 = $40,000

Wait — let me recheck. With $80,000 W-2 and $50,000 UBIA:
- 50% × $80,000 = $40,000
- 25% × $80,000 + 2.5% × $50,000 = $20,000 + $1,250 = $21,250
- Greater = $40,000

So L11 = min($50,937, $40,000) = $40,000.

**L13 phase-in reduction:** $40,000 − $13,560 = **$26,440**

**Adjusted QBI:** $40,000 − $26,440 = **$13,560**

The doctor lost $26,440 of deduction. Note that BOTH the phase-in AND the W-2/UBIA limit are biting here — the wages aren't enough to support the full 20% deduction.

---

## Worked Example C — At the top of the phase-in window

**Inputs:**
- Filing status: MFJ
- Taxable income before QBI: $580,000
- Business: SSTB (consulting)
- QBI: $200,000
- W-2 wages: $0 (solo consultant, no employees)

**Schedule A:**
- L3 threshold: $483,900
- L4 excess: $580,000 − $483,900 = $96,100
- L5 width: $100,000
- L6 phase-in %: 96,100 / 100,000 = 0.9610
- L7 applicable %: 0.0390
- L8 reduced QBI: $200,000 × 0.0390 = $7,800
- L9 reduced W-2: $0
- L11 W-2/UBIA on reduced: max(50% × 0, 25% × 0) = $0
- L12 tentative: min(20% × 7,800, $0) = $0

**Adjusted QBI: $0.** A solo SSTB consultant with no W-2 wages is wiped out near the top of the phase-in even with significant QBI, because there are no wages to support any deduction.

If the consultant had paid himself and his spouse W-2 wages from an S-corp, the result would differ. This is one of the structural arguments for the S-corp election among high-income SSTB owners.

---

## Worked Example D — Above the top of phase-in

**Inputs:**
- Filing status: Single
- Taxable income before QBI: $300,000
- Business: SSTB (financial advisor)
- QBI: $250,000

$300,000 > $291,950 (top of single phase-in), so the SSTB QBI deduction = $0. List the business in Part I (with SSTB checked) but report zero contribution to Line 27. No Schedule A needed (it would just produce zero anyway).

---

## Common errors

1. **Forgetting Schedule A entirely**: filing software may default to applying the W-2/UBIA limit without the SSTB phase-in. Always confirm Schedule A is generated for SSTB businesses in the zone.

2. **Using the wrong phase-in width**: $50K is single only; MFJ is $100K. MFS uses the same $50K as single.

3. **Phase-in calculated on AGI instead of taxable income before QBI**: it's taxable income (AGI − standard or itemized deduction), NOT AGI directly.

4. **Rounding too early**: the applicable percentage should retain at least 4 decimals through the computation. Software issues sometimes drop to 2 decimals and produce $1-50 errors.

5. **Applying Schedule A to non-SSTB businesses**: only SSTBs phase in. Non-SSTBs above the threshold use the W-2/UBIA limit in full but don't phase in.
