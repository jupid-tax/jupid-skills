# Form 8959 — Wage vs. SE Interaction

The Additional Medicare Tax threshold is **single, not stacked**. A filer with both W-2 wages and self-employment income does not get a fresh threshold for each income type. This is the highest-leverage rule on the form.

## The mechanic

Part I (wages) consumes the threshold first. Whatever is left (if any) is available to absorb SE income on Part II. If wages alone exceed the threshold, Part II Line 11 = 0 and every dollar of SE income above zero is taxed at 0.9%.

```
Part I (wages):
  threshold consumed by wages: min(Line 4, Line 5)
  wage surtax base: max(Line 4 − Line 5, 0)

Part II (SE):
  remaining threshold: max(Line 9 − Line 10, 0)   = Line 11
  SE surtax base: max(Line 8 − Line 11, 0)        = Line 12
```

The form does NOT take the larger of (wage surtax base, SE surtax base). It does NOT compute them separately on the same threshold. It chains them: wages first, SE second, against one shared threshold.

## Worked examples

### Example A: Pure wage filer, single, $230K

```
Wages = $230,000
SE = $0
Threshold = $200,000

Part I:
  Line 4 = $230,000
  Line 5 = $200,000
  Line 6 = $30,000
  Line 7 = $270

Part II:
  Line 8 = $0
  Line 9 = $200,000
  Line 10 = $230,000
  Line 11 = max($200K − $230K, 0) = $0
  Line 12 = max($0 − $0, 0) = $0
  Line 13 = $0

Part IV:
  Line 18 = $270
```

Surtax = $270 (0.9% × $30K wage excess).

### Example B: Pure SE filer, single, $230K Schedule C net

```
Wages = $0
Schedule C net = $230,000
Schedule SE Line 6 = $230,000 × 92.35% = $212,405
Threshold = $200,000

Part I:
  Line 4 = $0
  Line 6 = max($0 − $200K, 0) = $0
  Line 7 = $0

Part II:
  Line 8 = $212,405
  Line 9 = $200,000
  Line 10 = $0
  Line 11 = $200,000
  Line 12 = $212,405 − $200,000 = $12,405
  Line 13 = $12,405 × 0.9% = $112

Part IV:
  Line 18 = $112
```

Surtax = $112. Lower than Example A on the same gross income because the 92.35% multiplier reduces the Form 8959 base. Important: this is *only* the Form 8959 effect; the regular Schedule SE 15.3% tax (Social Security + Medicare) was already higher than the W-2 employee's 7.65%.

### Example C: Mix — single, $150K wages + $80K Schedule C

```
Wages = $150,000
Schedule C net = $80,000
Schedule SE Line 6 = $80,000 × 92.35% = $73,880
Threshold = $200,000

Part I:
  Line 4 = $150,000
  Line 6 = max($150K − $200K, 0) = $0
  Line 7 = $0

Part II:
  Line 8 = $73,880
  Line 9 = $200,000
  Line 10 = $150,000
  Line 11 = max($200K − $150K, 0) = $50,000
  Line 12 = max($73,880 − $50,000, 0) = $23,880
  Line 13 = $23,880 × 0.9% = $215

Part IV:
  Line 18 = $215
```

Surtax = $215. The filer's wages used $150K of the $200K threshold; the remaining $50K absorbed the first $50K of SE income; the next $23,880 of SE income above that is surtaxed.

### Example D: Mix where wages exceed threshold — single, $230K wages + $80K Schedule C

```
Wages = $230,000
Schedule C net = $80,000
Schedule SE Line 6 = $73,880
Threshold = $200,000

Part I:
  Line 6 = $30,000
  Line 7 = $270

Part II:
  Line 10 = $230,000
  Line 11 = max($200K − $230K, 0) = $0
  Line 12 = max($73,880 − $0, 0) = $73,880
  Line 13 = $73,880 × 0.9% = $665

Part IV:
  Line 18 = $935
```

Surtax = $935. With wages already above the threshold, every dollar of SE income above zero is surtaxed.

### Example E: MFJ couple, both earners + one spouse has SE income

```
Spouse 1 wages = $180,000
Spouse 2 wages = $90,000
Spouse 2 Schedule C net = $40,000  →  Schedule SE Line 6 = $36,940
Threshold = $250,000

Part I:
  Line 4 = $180,000 + $90,000 = $270,000
  Line 6 = $20,000
  Line 7 = $180

Part II:
  Line 8 = $36,940
  Line 10 = $270,000
  Line 11 = max($250K − $270K, 0) = $0
  Line 12 = $36,940
  Line 13 = $332

Part IV:
  Line 18 = $512
```

Surtax = $512. Because combined wages already exhausted the joint threshold, the spouse's full SE earnings are surtaxed.

## Why this matters for planning

Filers with mixed income sometimes assume they have "two thresholds" because they have "two income types". They don't. The chained logic means:

- Adding a side hustle to existing W-2 income above the threshold means **every dollar of side-hustle SE income is surtaxed** at 0.9%
- The 92.35% multiplier on Schedule SE Line 6 partially offsets the surtax (~7.65% reduction in surtax base for SE income)
- The combined effective marginal rate on each new dollar of SE income, for a filer already above the threshold, is:
  - 15.3% × 92.35% = ~14.13% (regular SS + Medicare via Schedule SE)
  - + 0.9% × 92.35% = ~0.83% (Form 8959 surtax)
  - + their ordinary federal income tax marginal rate (e.g., 32% for $230K single)
  - = ~47% federal-only marginal rate on each new dollar of SE income above the threshold (before state tax)

This is not a recommendation to incorporate or to defer income — it's a fact pattern the agent should be able to compute.

## What the agent should do

1. Always pull Schedule SE Line 6, not raw Schedule C net profit. The 92.35% multiplier matters.
2. Always check whether wages alone exceed the threshold. If yes, Line 11 = 0, and the SE surtax computation shortcuts to "0.9% × Line 8".
3. Never invite the user to "use a separate threshold for SE income." There is no such thing.
4. If the user has both W-2 and SE income, surface the marginal-rate fact once during the workflow so the user understands future-year planning consequences.

## Sources

- IRC §1401(b)(2) — Additional Medicare Tax on SE income
- IRC §1402(a)(12) — 92.35% multiplier (the 7.65% deduction representing the employer-equivalent portion of SS/Medicare)
- IRC §3101(b)(2) — Additional Medicare Tax on wages
- [Instructions for Form 8959](https://www.irs.gov/pub/irs-pdf/i8959.pdf) — Lines 8–13 explanation
- [Schedule SE Instructions](https://www.irs.gov/forms-pubs/about-schedule-se-form-1040)
