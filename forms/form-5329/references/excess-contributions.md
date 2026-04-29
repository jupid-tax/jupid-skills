# Excess Contributions — Parts III, IV, V, VI, VII, VIII

The 6% excise tax under IRC §4973 applies to contributions in excess of
the annual limit on traditional IRAs, Roth IRAs, Coverdell ESAs, Archer
MSAs, HSAs, and ABLE accounts. The tax recurs *every year* the excess
remains in the account until corrected.

This reference covers what creates excess, how to correct it, and the
mechanics of computing the 6% tax on the form.

---

## How excess arises

### Traditional IRA (Part III)

Limit per filer per year is the lesser of:
- The contribution dollar limit for the year (verify against most recent
  IRS notice — Notice 2024-80 set the 2025 limit at $7,000 ($8,000 if
  age 50+); 2026 limits announced fall 2025)
- The user's earned income for the year (compensation; for spouse, can use
  the working spouse's income)

Excess = total contributions − limit.

Common causes:
- User contributed more than the dollar limit
- User contributed more than their earned income
- User contributed for a year they had no earned income (retirement)
- User had multiple traditional IRAs and aggregate exceeded the limit

### Roth IRA (Part IV)

Limit is the same dollar amount as traditional IRA, BUT phased out by
modified adjusted gross income (MAGI). For 2025 (per Notice 2024-80):

- Single / HoH: phaseout $150,000 - $165,000 MAGI; no contribution above
  $165,000
- MFJ: phaseout $236,000 - $246,000 MAGI; no contribution above $246,000
- MFS: phaseout $0 - $10,000 MAGI

Verify 2026 phaseouts before filing.

Common causes:
- User contributed early in the year, then their MAGI rose past the
  phaseout (high-earner, equity comp, year-end bonus)
- User and spouse filed MFS without realizing the $0-$10,000 phaseout
- User overlooked the income limits entirely

### Coverdell ESA (Part V)

$2,000 per beneficiary per year, across all contributors. Phaseout for
contributors based on MAGI.

### HSA (Part VII)

Limits depend on HDHP coverage type. For 2025 (Rev. Proc. 2024-25):
- Self-only: $4,300
- Family: $8,550
- Age 55+ catch-up: additional $1,000

For 2026 — verify against Rev. Proc. 2025-XX (issued spring 2025).

### ABLE (Part VIII)

Federal annual gift tax exclusion ($18,000 for 2024, $19,000 for 2025;
verify 2026), plus an ABLE-to-Work additional contribution if the
beneficiary is employed and not contributing to a 401(k)/403(b)/457(b).

---

## Correction options (in priority order)

### Option 1 — Withdraw excess + earnings before tax filing deadline

The cleanest correction. The user contacts the custodian and requests a
"return of excess contribution." The custodian withdraws:
- The excess principal, AND
- The "net income attributable" (NIA) — earnings or losses on the excess
  computed by a formula in §1.408-11 or the relevant ESA / HSA / ABLE
  regulation

**Effects**:
- No 6% excise tax for the year
- The earnings (NIA) are taxable in the year of contribution
- If user is under 59½, the earnings are subject to Part I 10% additional
  tax
- For Roth IRAs: the principal portion comes out tax-free; only the
  earnings portion is taxed

**Deadline**: the user's tax filing deadline including extensions (October
15 for most filers).

### Option 2 — Recharacterization (Roth → traditional or vice versa)

For IRAs only. Treats the contribution as if it had been made to the
other type of IRA from the start. Useful when:
- Roth contribution was over MAGI limit, but a traditional contribution
  is allowed (even if nondeductible)

The user contacts the custodian, who moves the excess + NIA to the other
IRA. Same deadline as Option 1.

Note: Roth conversions cannot be recharacterized (TCJA repealed that for
post-2017 conversions). Only contribution-recharacterizations remain.

### Option 3 — Apply to future year

If next year the user expects to be eligible to contribute, the carried
excess absorbs into next year's contribution space (the user effectively
contributes less new money next year, the carryover plugs the gap). The
6% tax still applies in the year(s) the excess sat in the account.

For Roth IRAs: this only works if next year the user is again Roth-
eligible (MAGI below the phaseout).

### Option 4 — Pay the 6%

When the alternatives are worse:
- Recharacterization to a nondeductible traditional IRA creates basis-
  tracking complexity and pro-rata rule issues for future Roth conversions
- The user expects to be back below MAGI next year and the excess is small
- The earnings would push the user into a higher tax bracket if returned

The 6% is the lesser of (excess) or (6% of account value 12/31). For a
$5,000 excess in an account worth $50,000 at year-end, the tax is $300.

---

## Computing the 6% tax (Parts III/IV/V/VII/VIII)

The form structure for excess-contribution Parts is:

```
Line A — Prior-year excess from prior 5329 (carryover)
Line B — Current-year excess contribution
Line C — Distributions of excess + adjustments (reduces excess)
Line D — Total excess remaining
Line E — Additional tax = 6% × min(Line D, account value 12/31)
```

Specific line numbers vary by Part (Part III: 9-17; Part IV: 18-25, etc.).
See [`line-by-line.md`](./line-by-line.md) for the exact line numbers.

---

## Compounding scenario

A $6,500 excess contribution to a Roth IRA in 2024, uncorrected:

| Year | Account value 12/31 | 6% tax | Cumulative |
|------|---------------------|--------|-----------|
| 2024 | $7,200 | $390 | $390 |
| 2025 | $7,800 | $390 | $780 |
| 2026 | $8,500 | $390 | $1,170 |
| 2027 | $9,200 | $390 | $1,560 |
| 2028 | $10,000 | $390 | $1,950 |

Five years uncorrected: $1,950 in 6% tax on a $6,500 excess. Past some
threshold (typically 2-3 years), correction becomes worthwhile even if
the earnings withdrawal triggers other costs.

---

## Documentation the user should retain

- IRA / Roth / HSA / ABLE statements showing contributions and account
  values at year-end (12/31)
- Custodian correspondence confirming any "return of excess" or
  recharacterization
- Form 1099-R issued for the return of excess (with codes 8 or P) — these
  document the corrective distribution
- Correspondence with the custodian on the NIA computation

---

## Common excess-contribution mistakes

1. **High-earner who contributed $7,000 to a Roth in January, got a
   year-end bonus pushing MAGI over the phaseout, and didn't realize
   until preparing the return.** Standard correction: withdraw excess +
   NIA before April 15 (or extension). The agent should check Roth
   eligibility *every* year for users whose income is volatile.

2. **Couple filing MFS who each contributed to a Roth.** MFS Roth
   phaseout is $0-$10,000. If MAGI > $10,000 and either spouse contributed
   to Roth, that contribution is fully ineligible. Almost always the
   biggest "I didn't know" excess case.

3. **Multiple IRAs at different custodians, totaling above the limit.**
   Custodians don't communicate; the limit is per-filer not per-account.
   $4,000 to Custodian A and $4,000 to Custodian B = $1,000 excess (limit
   $7,000 for under-50 in 2025).

4. **Spousal IRA contribution where the working spouse has insufficient
   earned income to cover both.** Combined IRA contributions can't exceed
   combined earned income.

5. **Contribution after age limit (Roth has no age limit; traditional IRA
   age limit was repealed by SECURE Act in 2019)** — this is no longer a
   live trap but pre-2020 prior-year carryovers may exist.

6. **Excess HSA contribution due to mid-year change in HDHP coverage** —
   user had family HDHP for 6 months ($4,275 prorated), then individual
   for 6 months ($2,150 prorated), but contributed the full family
   $8,550 limit. Excess.
