# Form W-4R Line-by-Line Reference

Complete lookup for every field on Form W-4R. Use this when the agent needs to confirm what a line means or what the payor expects.

The instructions for Form W-4R are **printed inside the form PDF** (page 2 onward). There is no separate iw4r.pdf — the IRS combined form and instructions when W-4R was introduced for 2022 (effective 2023). When the agent needs the canonical instruction text, fetch <https://www.irs.gov/pub/irs-pdf/fw4r.pdf>.

---

## What changed in 2022 (effective 2023)

Before tax year 2023, Form W-4P was the single form used for both periodic and nonperiodic retirement payments. The W-4R was new for 2022 (with delayed mandatory adoption to give payors time to update systems) and split the function:

- **W-4P** — periodic pension and annuity payments (recurring)
- **W-4R** — nonperiodic payments AND eligible rollover distributions (one-time or unscheduled)

A pre-2023 W-4P that the recipient has on file with a payor for nonperiodic payments is no longer valid as of 2023; the recipient must submit W-4R for nonperiodic payments. Payors were required to transition by Jan 1, 2023.

If the recipient is uncertain whether a prior form is still on file, ask the payor — most payors will request a new W-4R with the next nonperiodic distribution request.

---

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| First name and middle initial | Recipient's first + MI | Match payor records |
| Last name | Recipient's last name | Match payor records (including hyphens, suffixes if used in payor records) |
| Social Security number | 9-digit SSN, format XXX-XX-XXXX | Required; matches Form 1099-R reporting |
| Address | Number, street, apartment | Match payor records or update with payor first |
| City, state, and ZIP code | Same | Foreign addresses use country in the state field |

**Why match payor records exactly?** Form W-4R is matched to the recipient's account at the payor based on the name + SSN combination. A mismatch (e.g., a married filer used a maiden name in payor records but a married name on the form) can cause the payor to reject or hold the form pending verification — delaying the distribution.

---

## Line 1 — Payor identification

### Line 1a — Payor's name

The legal name of the payor. Examples:

- **IRA custodian**: "Fidelity Brokerage Services LLC", "Charles Schwab & Co., Inc.", "Vanguard Marketing Corporation", "Merrill Lynch, Pierce, Fenner & Smith Incorporated", "TD Ameritrade, Inc."
- **401(k) recordkeeper**: "Empower Retirement, LLC", "Voya Financial", "Fidelity Workplace Services LLC", "Principal Life Insurance Company"
- **Employer paying severance**: the legal entity name on the recipient's W-2 (e.g., "Acme Corporation", not the DBA)
- **ESOP trustee**: name of the ESOP trust or trustee bank

Pull from a recent statement or the distribution-request packet.

### Line 1b — Payor's address

Street address of the payor. The address listed on a recent statement or the distribution-request packet. This is informational — it identifies the payor for IRS reporting purposes.

If the payor uses different addresses for different functions (statement mailing vs. distribution request), use the address listed on the distribution-request paperwork.

---

## Line 2 — Withholding rate

A whole percentage from 0 to 100. The recipient's election for federal income tax withholding on the upcoming distribution.

### What rate to enter

| Payment type | Range allowed | Default if blank |
|--------------|---------------|------------------|
| Eligible rollover distribution (ERD) under IRC §3405(c) | 20–100 | 20% |
| Other nonperiodic distribution under IRC §3405(b) | 0–100 | 10% |

**ERD constraint**: The recipient cannot reduce withholding below 20% via Form W-4R. Entering "5" or "10" on Line 2 when the payment is an ERD is invalid; the payor will treat it as 20% (the statutory minimum). If the recipient does not want any actual withholding on an ERD, the only path is a direct trustee-to-trustee rollover (no W-4R needed because the funds never reach the recipient).

**Other nonperiodic constraint**: The recipient may enter "0" to opt out of withholding entirely. This is common for:
- Roth IRA conversions where the recipient pays tax via quarterly estimates from non-IRA cash
- Recipients who are over-withheld via W-2 wages and don't need additional withholding from the distribution
- Recipients whose other income is too low to require withholding at all

Entering 0 does NOT eliminate the recipient's tax liability on the distribution — it only declines withholding. The recipient still owes tax at filing.

### What rate to choose — quick guidance

(Full rate-selection logic is in [`rate-selection.md`](./rate-selection.md).)

The "right" rate matches the recipient's marginal federal income tax bracket on the distribution amount, considering all other income for the year. Common 2026 bracket alignments:

| 2026 ordinary-income bracket (single filer) | Suggested W-4R rate |
|---------------------------------------------|---------------------|
| 10% (taxable income roughly up to $11,925; verify 2026 inflation adjustment) | 10% |
| 12% (up to ~$48,475) | 12% (or 10% default if under-withholding is acceptable) |
| 22% (up to ~$103,350) | 22% |
| 24% (up to ~$197,300) | 24% |
| 32% (up to ~$250,525) | 32% |
| 35% (up to ~$626,350) | 35% |
| 37% (above $626,350) | 37% |

**Verify 2026 brackets against IRS Rev. Proc. 2025-32 (or whichever Rev. Proc. announces 2026 inflation adjustments).** As of 2026-04-29, the 2026 brackets were announced in late 2025 and these figures should be cross-checked against the current IRS publication.

### Common rate-selection patterns

- **Retiree, no other income, taking $40K Traditional IRA distribution**: standard deduction reduces taxable income to ~$25K (for a single filer in 2026 with ~$15K standard deduction), all in the 10–12% bracket. **Suggested: 12%** (or accept the 10% default).
- **Working professional in 24% bracket, taking $20K side IRA distribution**: distribution stacks on top of W-2 wages. **Suggested: 24%** to avoid quarterly estimates.
- **Retiree taking RMD plus collecting Social Security, total income near top of 22% bracket**: SS may become up to 85% taxable due to combined-income calculation. **Suggested: 22%** (default 10% will materially under-withhold).
- **Roth conversion, $50K from Traditional IRA to Roth**: recipient pays tax from non-IRA cash to maximize amount that ends up in Roth. **Suggested: 0%** on W-4R; pay tax via Form 1040-ES quarterly estimate.
- **Severance, $30K, recipient unemployed**: total annual income may be much lower than typical wages. **Suggested**: pick the bracket the severance + any other income lands in (often 12–22%).
- **401(k) lump sum, $80K, indirect rollover within 60 days**: ERD; payor will withhold 20% mandatory ($16K). To complete the rollover whole, recipient must deposit $80K into IRA within 60 days (the $16K withheld must be made up from non-IRA cash). **Suggested**: enter 20% (the minimum) and plan the make-whole cash. Or — much better — switch to direct trustee-to-trustee rollover.

---

## Signature block

The recipient signs and dates the form. Penalties-of-perjury declaration:

> "Under penalties of perjury, I declare that I have examined this certificate and, to the best of my knowledge and belief, it is correct and complete."

The recipient prints their name and dates. The payor does NOT sign.

For severance payments under joint participant-spouse retirement structures (QDRO distributions), each recipient signs their own W-4R.

---

## What's NOT on Form W-4R but matters

### State income tax withholding

Form W-4R covers federal income tax withholding only. Most states have separate state tax withholding rules for retirement distributions:

- Some states require automatic state withholding on retirement distributions to residents (e.g., California 2% default unless the recipient elects out)
- Some states have no state income tax (no withholding needed)
- Some states allow opt-in or opt-out at the same rate as federal

The payor typically provides a state-tax withholding form alongside W-4R (sometimes a single combined form, sometimes a state-specific form). This skill handles federal only.

### §72(t) 10% additional tax on early withdrawals

If the recipient is under 59½ (or applicable exception age) and taking a taxable IRA / 401(k) distribution, IRC §72(t) imposes a 10% additional tax on top of ordinary income tax. This is reported on Form 5329 with the recipient's Form 1040.

**Form W-4R does NOT withhold for §72(t).** The withholding rate the recipient enters covers only ordinary income tax. The 10% §72(t) penalty must be paid via:

- Quarterly estimated taxes (Form 1040-ES) during the year, OR
- Lump-sum payment with the Form 1040 at filing time

If the recipient picks a W-4R rate of, say, 22% and is subject to §72(t), the effective tax on the distribution will be 22% + 10% = 32% (plus any state tax). Plan accordingly.

### §72(t) exceptions

The §72(t) penalty does NOT apply if any of the following exceptions in §72(t)(2) is met:

- Distributions on or after age 59½
- Distributions due to total and permanent disability (§72(m)(7))
- Substantially equal periodic payments (SEPPs) under §72(t)(2)(A)(iv)
- Distributions for qualified medical expenses exceeding 7.5% of AGI
- Distributions to pay health insurance premiums while unemployed (IRA only, with limits)
- Distributions for qualified higher education expenses (IRA only)
- First-time homebuyer distributions up to $10,000 lifetime (IRA only)
- Distributions on death of the participant
- Series of substantially equal periodic payments
- Distributions following separation from service after age 55 (401(k) rule of 55, not IRA)
- Birth or adoption distributions up to $5,000 (SECURE Act §72(t)(2)(H))
- Disaster-related distributions (per applicable disaster-relief act)
- Domestic abuse distributions up to $10,000 or 50% of vested balance (SECURE 2.0)
- Terminal illness distributions (SECURE 2.0)
- Emergency personal expense distributions up to $1,000 (SECURE 2.0, IRA only)
- Long-term care insurance distributions (SECURE 2.0, beginning 2026)

If an exception applies, the recipient files Form 5329 indicating the exception code; the §72(t) penalty is waived on that distribution.

### Form 1099-R reporting

After the distribution is paid, the payor issues Form 1099-R in January of the following year. The 1099-R reports:

- Box 1: Gross distribution
- Box 2a: Taxable amount (may differ from gross for partial after-tax basis recovery)
- Box 4: Federal income tax withheld (the amount based on W-4R election)
- Box 7: Distribution code (1 = early distribution no known exception, 2 = early distribution exception applies, 7 = normal distribution age 59½+, G = direct rollover, etc.)

The recipient uses Form 1099-R to file Form 1040 for the year of distribution. The amount in Box 4 is claimed as withholding on Form 1040 Line 25b.

### Direct trustee-to-trustee rollover (alternative to W-4R)

If the recipient's goal is to move retirement funds from one account to another **without paying tax**, the cleanest path is a direct trustee-to-trustee rollover under IRC §401(a)(31) for 401(k) → IRA, or under §408(d)(3) for IRA → IRA.

- **No W-4R needed** — the funds never reach the recipient
- **No 20% mandatory withholding** — IRC §3405(c) only applies to ERDs paid to the participant
- **No 60-day deadline pressure** — the rollover is completed by the trustees directly
- **Reported on Form 1099-R** with distribution code G (direct rollover, no withholding)

The recipient initiates a direct rollover by:

1. Opening the receiving account (new IRA or 401(k))
2. Requesting a direct rollover from the source plan administrator, providing the receiving account's information
3. The source pays the funds directly to the receiving custodian — never to the recipient

If the recipient's actual goal is moving funds (not consuming them), the agent should surface direct rollover as the preferred path before producing a W-4R for an indirect rollover.

---

## Recipient's options summary

| Goal | W-4R rate | Notes |
|------|-----------|-------|
| Take cash, minimize current withholding (other nonperiodic) | 0% | Owe tax at filing; consider quarterly estimates |
| Take cash, withhold approximately enough to cover tax | Marginal bracket rate | E.g., 22% for typical mid-bracket taxpayer |
| Take cash, over-withhold (forced savings, expect refund) | Above marginal rate | Cash drag until refund |
| Roll over 401(k) → IRA (indirect, 60-day rule) | 20% (mandatory ERD floor) | Must "make whole" with non-IRA cash; consider direct rollover instead |
| Roll over IRA → IRA or 401(k) → IRA (direct trustee-to-trustee) | No W-4R needed | No withholding, no 60-day pressure |
| Roth conversion | 0% | Pay tax from non-IRA cash to maximize Roth balance |
| Severance, lump sum | Bracket rate based on total annual income | Confirm with employer whether classified as W-4R or W-4 wages |
| RMD (over 73, age varies post-SECURE 2.0) | 10% default; adjust to bracket if higher | RMDs are NOT eligible to be rolled over; W-4R applies |
| Hardship withdrawal | 10% default; confirm with plan | Hardship is not an ERD; W-4R applies |
