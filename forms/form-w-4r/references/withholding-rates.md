# Withholding rates on Form W-4R — defaults, mandatory minimums, and overrides

Form W-4R sets the federal income tax withholding rate on a nonperiodic distribution. The right rate depends on whether the distribution is an **eligible rollover distribution (ERD)** or **other nonperiodic** under IRC §3405.

This reference covers the rate mechanics in depth.

---

## The two rate regimes

### Regime A — Eligible rollover distribution (ERD)

Authority: IRC §3405(c).

**Default and mandatory minimum: 20%.** Withholding cannot be reduced below 20% on an ERD paid to the participant.

The recipient may **increase** the rate above 20% via Form W-4R Line 2 — up to 100%. Common reasons to increase:

- Recipient is in a high marginal bracket and 20% would under-withhold
- Recipient wants to "front-load" withholding to avoid quarterly estimates
- Recipient has other income (capital gains, business income) and wants the distribution withholding to cover it

The recipient may **NOT** decrease below 20% on the W-4R. Even if Line 2 is left blank or "0" is entered, the payor will apply 20% by force of §3405(c).

**The only way to avoid 20% withholding on an ERD**: do a **direct trustee-to-trustee rollover**. The funds are transferred directly between qualified plans / IRAs without the participant taking constructive receipt. No withholding applies because the money never reaches the participant. The transferring trustee codes the Form 1099-R with **Code G** (direct rollover) and reports $0 federal withholding.

### Regime B — Other nonperiodic distribution

Authority: IRC §3405(b).

**Default: 10%.** Applied if Form W-4R Line 2 is blank.

The recipient may **increase or decrease** the rate from 0% to 100%. The 10% is a default, not a mandatory minimum.

To opt out entirely (0% withholding), enter "0" on Line 2.

To request a higher rate (e.g., 22% to match the marginal bracket), enter the desired percentage.

---

## Which distributions are ERDs vs. other nonperiodic?

This is the most important classification call. The wrong call leads to wrong default rate, wrong recipient expectations, and possible payor error.

### ERDs (20% mandatory)

Under IRC §402(c) (definition) and IRC §3405(c) (withholding):

- **Lump-sum distribution from a 401(k) plan** to participant after separation from service
- **Partial 401(k) distribution** to participant (cash withdrawal, not rollover)
- **Distribution from a profit-sharing plan, money-purchase plan, ESOP** (cash, not stock)
- **403(b) plan distribution** to participant after separation
- **457(b) governmental plan distribution** to participant
- **Defined benefit lump-sum cash-out** (rare, but happens for small accrued benefits)
- **Surviving spouse rollover-eligible distribution** from a deceased participant's qualified plan (paid to spouse, then rolled over)

### NOT ERDs — other nonperiodic (10% default)

Under IRC §402(c)(4) — items excluded from ERD definition:

- **IRA distributions** (Traditional, SEP, SIMPLE) — IRA distributions are not ERDs (IRA-to-IRA transfers exist but use different mechanics; a cash IRA withdrawal is "other nonperiodic")
- **Required Minimum Distributions (RMDs)** — explicitly excluded from ERD definition
- **Hardship withdrawals from a 401(k)** — excluded because hardship distributions are not eligible to be rolled over
- **Substantially equal periodic payments (SEPP)** under §72(t)(2)(A)(iv) — series of substantially equal payments
- **Severance** (when treated as nonperiodic and not as wages)
- **ESOP cash distribution after a §1042 election** — special case
- **Distributions to a non-spouse beneficiary** — generally NOT ERDs (with an exception for inherited IRAs being rolled to another inherited IRA via direct trustee-to-trustee transfer)
- **Excess contributions / excess deferrals returned** — corrective distribution, not ERD

### Periodic (use W-4P, not W-4R)

Under IRC §3405(a):

- **Pension annuity payments** — monthly / quarterly / annual scheduled payments for life or for more than one year
- **Substantially equal periodic payments under §72(t)** — though this is a §72(t) construct, the withholding form depends on whether the payments span more than one year (if yes, periodic → W-4P; if not, nonperiodic → W-4R)

---

## How to override the default

### To increase ERD withholding above 20%

Enter the desired percentage on W-4R Line 2 (e.g., "22" for 22%, "37" for 37%).

The payor applies the higher rate to the gross distribution. Example: $50,000 ERD with W-4R Line 2 = "30":

- Gross distribution: $50,000
- Federal withholding: $50,000 × 30% = $15,000
- Net to recipient: $35,000

Form 1099-R reports gross $50,000, federal withholding $15,000.

### To opt out of nonperiodic withholding (other than ERD)

Enter "0" on W-4R Line 2.

Example: $20,000 IRA cash withdrawal with W-4R Line 2 = "0":

- Gross distribution: $20,000
- Federal withholding: $0
- Net to recipient: $20,000

The recipient is responsible for paying the tax on the $20,000 via Form 1040 (or quarterly estimates if needed to avoid §6654 underpayment penalty).

### To set a custom nonperiodic rate

Enter any percentage 0–100 on W-4R Line 2. Example: $30,000 IRA cash withdrawal with W-4R Line 2 = "22" (matching the recipient's marginal bracket):

- Gross distribution: $30,000
- Federal withholding: $30,000 × 22% = $6,600
- Net to recipient: $23,400

---

## Rate selection by income bracket (informational)

For 2026 federal income tax brackets (single filer, ordinary income):

| Marginal bracket | Bracket boundary (single) | Reasonable W-4R rate |
|------------------|---------------------------|----------------------|
| 10% | $0 – $11,925 | 0% (low total income; covered by standard deduction) |
| 12% | $11,925 – $48,475 | 0–10% (depending on other income) |
| 22% | $48,475 – $103,350 | 10–22% |
| 24% | $103,350 – $197,300 | 22–24% |
| 32% | $197,300 – $250,525 | 24–32% |
| 35% | $250,525 – $626,350 | 32–35% |
| 37% | $626,350+ | 35–37% |

(2026 brackets are estimates pending IRS release; verify against IRS Rev. Proc. for the actual year. 2025 brackets shown are placeholder approximations — re-verify before relying.)

The recipient's actual marginal rate depends on filing status, total taxable income, and any phase-outs / credits. The above is a starting guide.

---

## Special cases

### Roth IRA distribution

If the Roth distribution is **qualified** (account ≥ 5 years old AND distribution after age 59½, after death, after disability, or for first-home purchase up to $10K), the distribution is **not taxable**. No withholding applies; W-4R typically not needed.

If the distribution is **non-qualified** (account < 5 years OR participant under 59½ etc.), the **earnings portion** is taxable. The earnings are subject to default 10% withholding under §3405(b). The basis (contributions) is not taxable and not subject to withholding. Most custodians treat the distribution per the ordering rules: contributions out first (basis, no tax, no withholding), conversions next (potentially taxable if 5-year rule for conversions not met), earnings last (taxable, withholding applies).

### Roth conversion

A Roth conversion (Traditional → Roth IRA) is a taxable event: the converted amount is income in the year of conversion. Withholding via W-4R is technically allowed but **strongly discouraged** because:

- Withholding from the Traditional IRA reduces the amount converted to Roth
- The withheld amount is itself a taxable distribution (and may be subject to §72(t) penalty if recipient is under 59½)

Best practice: convert with **0% withholding via W-4R**, then pay the tax via Form 1040-ES from non-IRA cash. This keeps the full converted amount in the Roth and avoids accidental §72(t) penalty.

### §72(t) early-withdrawal penalty (separate from W-4R)

If the recipient is under 59½ (or applicable exception age), the additional 10% penalty under §72(t) applies to the taxable distribution. **W-4R does NOT withhold for §72(t).** The recipient pays the §72(t) penalty separately on Form 5329.

If the recipient elects 22% on W-4R for a $30,000 IRA distribution at age 40 with no exception:

- Federal income tax withholding: $6,600
- §72(t) penalty: $3,000 (10% of $30,000) — NOT withheld; paid by recipient on Form 5329
- Net to recipient before §72(t): $23,400
- Net to recipient after §72(t) paid at filing: $20,400 (effectively)

Common mistake: recipient assumes 22% covers everything; ends up owing $3,000 plus underpayment penalty at filing.

### State withholding

W-4R covers federal only. State income tax withholding on retirement distributions is governed by state law, varies widely:

- **No state income tax**: AK, FL, NV, NH, SD, TN, TX, WA, WY (no state withholding required)
- **Mandatory state withholding states**: CA, CT, KS, MA, ME, MI, MN, NE, NC, OK, OR, VT, VA — state-specific rates and forms
- **Voluntary state withholding states**: most others — recipient can elect

The payor's distribution-request form usually has a separate state-tax section. Coordinate with the payor on state-specific requirements.

---

## Summary

| Distribution type | Default withholding | Min | Max |
|-------------------|---------------------|-----|-----|
| Eligible rollover distribution (ERD) | 20% | 20% | 100% |
| Other nonperiodic | 10% | 0% | 100% |
| Periodic | (use W-4P, not W-4R) | — | — |
| Direct trustee-to-trustee rollover | 0% (no withholding; W-4R not needed) | 0% | 0% |
| Roth qualified distribution | (typically no withholding; W-4R not needed) | — | — |

The recipient's job: classify the distribution correctly, then pick the right rate within the allowed range.
