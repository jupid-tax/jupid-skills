# SS Wage Base, FICA Rate Composition, and the 0.9235 Factor

This file explains where the numbers on Schedule SE come from. Use it when the agent or user wants to understand *why* a multiplier is what it is, or to verify the figures for a tax year.

---

## The 15.3% SE tax rate

```
12.4% (Social Security) + 2.9% (Medicare) = 15.3%
```

Source: IRC §1401(a) (12.4% SS) and §1401(b) (2.9% Medicare).

The 12.4% combines the employee share (6.2%) + employer share (6.2%). The 2.9% combines the employee share (1.45%) + employer share (1.45%). The self-employed filer pays both halves because they are simultaneously the employer and the employee. The §164(f) above-the-line deduction (Schedule SE Line 13) gives back income tax on the "employer" half to mathematically equalize with W-2 employees.

---

## The 0.9235 factor

```
0.9235 = 1 − 0.0765 = 1 − (1/2 × 0.153)
```

Source: IRC §1402(a)(12).

The factor approximates removing the "employer's share" of FICA from the SE tax base. The intuition: a W-2 employee earns $100 of wages and pays FICA on $100. Their employer pays a separate 7.65% (= 0.5 × 0.153) on top. The employee's federal income tax is computed on $100 — they don't pay income tax on the employer's $7.65.

A self-employed filer earning $100 of net profit, by contrast, would otherwise pay both halves of FICA on the full $100 AND pay income tax on $100. The 0.9235 multiplier reduces the SE tax base to $92.35, so the filer pays SE tax of:

```
$92.35 × 0.153 = $14.13
```

This roughly equals what the employer + employee combined pay on a $100 wage:

```
$100 × 0.0765 (employee) + $100 × 0.0765 (employer) = $15.30
```

(There's still a small gap; the §164(f) income tax deduction closes most of the rest.)

---

## Social Security wage base history

The wage base only applies to the 12.4% SS portion. Medicare's 2.9% has no cap (and the additional 0.9% Medicare for high earners on Form 8959 also has no cap, just a floor).

| Tax year | SS wage base | Source |
|----------|--------------|--------|
| 2020 | $137,700 | SSA Press Release Oct 2019 |
| 2021 | $142,800 | SSA Press Release Oct 2020 |
| 2022 | $147,000 | SSA Press Release Oct 2021 |
| 2023 | $160,200 | SSA Press Release Oct 2022 |
| 2024 | $168,600 | SSA Press Release Oct 2023 |
| 2025 | $176,100 | SSA Press Release Oct 2024 |
| 2026 | (verify with SSA — typically announced October 2025) | — |

Always check https://www.ssa.gov/oact/cola/cbb.html for the current year's figure. The Schedule SE form pre-prints Line 7 with the figure for that tax year.

The base is indexed to the National Average Wage Index. Year-over-year increases run roughly 3–5% in normal years.

---

## Maximum SE tax owed (SS portion only)

When a filer has no W-2 wages and net SE earnings exceed the wage base, the SS portion of SE tax is capped:

```
Max SS portion = wage base × 0.124
```

For 2025: $176,100 × 0.124 = **$21,836.40 maximum SS portion** of SE tax for the year.

Medicare keeps applying past the wage base, so total SE tax keeps growing. For example, a filer with $300,000 net SE earnings in 2025:

```
Line 6 (post-0.9235): $300,000 × 0.9235 = $277,050
Line 9 (no W-2): $176,100 (full wage base available)
Line 10 (SS): min($277,050, $176,100) × 0.124 = $176,100 × 0.124 = $21,836
Line 11 (Medicare): $277,050 × 0.029 = $8,034
Line 12 (total): $29,870
```

(Plus Form 8959 Additional Medicare Tax 0.9% on the excess above $200K threshold.)

---

## Interaction with W-2 wages

If the filer also has W-2 wages, FICA is already withheld on the wages (employee 7.65% + employer 7.65%). The W-2 wages consume part of the SS wage base on Line 8a / Line 9.

Worked example: filer with $100,000 W-2 wages (Box 3 = $100,000) AND $80,000 Schedule C net profit, tax year 2025.

```
Line 6 (SE): $80,000 × 0.9235 = $73,880
Line 7: $176,100 (2025 wage base)
Line 8a: $100,000 (W-2 SS wages)
Line 8d: $100,000
Line 9: $176,100 − $100,000 = $76,100 (remaining base)
Line 10 (SS): min($73,880, $76,100) × 0.124 = $73,880 × 0.124 = $9,161
Line 11 (Medicare): $73,880 × 0.029 = $2,143
Line 12: $11,304
```

The full SE earnings stay within the remaining wage base, so no SS portion is "wasted" — but if SE earnings were $90,000 (post-0.9235 = $83,115), Line 10 would cap at $76,100 × 0.124 = $9,436, and the excess $7,015 of SE earnings would only owe Medicare.

---

## Multi-employer over-withholding

If a filer has multiple W-2 jobs and total Box 3 across all W-2s **exceeds the SS wage base**, the filer has overpaid Social Security tax on the W-2 side. They claim an excess SS tax credit on **Schedule 3 Line 11**, not on Schedule SE.

The excess does not reduce the SE tax — it just refunds the W-2 over-withholding.

This is rare but real for high earners with two simultaneous jobs (e.g., a consultant with a part-time C-suite advisory + W-2 executive role).

---

## Authority cited

- IRC §1401(a) — 12.4% SS rate
- IRC §1401(b) — 2.9% Medicare rate
- IRC §1402(a)(12) — 0.9235 factor
- IRC §164(f) — deductible half of SE tax
- SSA Contribution and Benefit Base — https://www.ssa.gov/oact/cola/cbb.html
- Schedule SE Instructions — annual wage base printed on Line 7

## Verify before filing

- 2026 SS wage base (the figure on the 2026 Schedule SE Line 7)
- 2026 SS quarter-of-coverage threshold (for credit accrual decisions)
- That the 0.9235 factor is unchanged (it has been stable since the 1990 SECA reforms; would only change with new legislation)
- That the FICA rates (6.2% / 1.45%) are unchanged (also stable; legislative change would be major news)
