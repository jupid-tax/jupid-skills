# Form W-4R Line-by-Line Reference

Complete lookup for every entry on the **2026 Form W-4R** (Cat. No. 75085T, created 12/12/25), verified on 2026-10-06 against the form text. Use this when the agent needs to confirm what a line means or what the payer expects. Re-check the next revision before use: https://www.irs.gov/forms-pubs/about-form-w-4r.

The instructions for Form W-4R are **printed on the form** (page 1 below the signature line, pages 2–3). There is no separate instructions PDF. When the agent needs the canonical text, fetch <https://www.irs.gov/pub/irs-pdf/fw4r.pdf>.

---

## Form history and older elections

Form W-4R covers nonperiodic payments and eligible rollover distributions; periodic pension and annuity payments stay on Form W-4P. The Privacy Act notice refers to changing "a previous Form W-4R (or a previous Form W-4P that you completed with respect to your nonperiodic payments or eligible rollover distributions)", so older W-4P elections for these payments exist.

What carries over: "Generally, for payments that began before 2026, your current withholding election (or your default rate) remains in effect unless you submit a Form W-4R" (2026 Form W-4R, page 2). Withholding choices "will generally apply to any future payment from the same plan or IRA. Submit a new Form W-4R if you want to change your election" (page 1).

If the recipient is unsure what is on file, ask the payer before drafting.

---

## The six entries on the form

| Entry | What goes here | Notes |
|-------|----------------|-------|
| 1a First name and middle initial | Recipient's first name + MI | Match payer records |
| 1a Last name | Recipient's last name | Match payer records (hyphens, suffixes) |
| 1b Social security number | 9-digit SSN | An estate enters its EIN here (form, "Line 1b") |
| Address | Number, street, apartment | Match payer records or update with the payer first |
| City or town, state, and ZIP code | Same | A U.S. or U.S.-territory home address is needed to elect less than 10% on a nonperiodic payment (Pub. 505 (2026), "Payments delivered outside the United States") |
| 2 Rate | Whole number, no decimals | Only if different from the default |

Then the signature and date: "Your signature (This form is not valid unless you sign it.)"

There are **no payer-name or payer-address lines** on the form; the payer is identified by the account the form is delivered with. The fillable PDF has exactly six text fields (see [`../filing.md`](../filing.md), PDF field map).

**Why match payer records?** The payer matches the form to the account by name and SSN. A mismatch can hold the form pending verification. If the recipient doesn't provide an SSN, or the IRS notifies the payer that the SSN is incorrect, the payer must withhold 10% and can't honor a lower rate (form, page 2 Note).

---

## Line 2 — Withholding rate

"Complete this line if you would like a rate of withholding that is different from the default withholding rate." Enter the rate as a whole number (no decimals).

### Allowed range

| Payment type | Default (no W-4R or line 2 blank) | Allowed on line 2 |
|--------------|-----------------------------------|-------------------|
| Eligible rollover distribution (ERD) — IRC §3405(c) | 20% | 20–100; can't choose less than 20% (including "-0-") |
| Other nonperiodic payment — IRC §3405(b) | 10% | 0–100 ("-0-" for none); generally not below 10% for payments delivered outside the United States and its territories |

**ERD rule (form text):** "You can't choose withholding at a rate of less than 20% (including '-0-')... Don't give Form W-4R to your payer unless you want more than 20% withheld." If the recipient wants no withholding on an ERD, the only path is a direct rollover (Pub. 575 (2025), Table 1: "There is no withholding").

**Other nonperiodic rule (form text):** "If you have already paid, or plan to pay, your tax on this payment through other withholding or estimated tax payments, you may want to enter '-0-'." Entering 0 does not eliminate the tax; it only declines withholding. The choice stays in effect until revoked (Pub. 505 (2026), "Choosing Not To Have Income Tax Withheld").

**Terrorist-attack disability payments:** if not taxable, enter "-0-" (form, page 2; Pub. 3920).

### How to pick the rate (form method)

The form prints 2026 Marginal Rate Tables (total income including the standard deduction built in):

| Single or MFS: total income over | MFJ or QSS: total income over | HoH: total income over | Rate for every dollar more |
|---|---|---|---|
| $0 | $0 | $0 | 0% |
| 16,100 | 32,200 | 24,150 | 10% |
| 28,500 | 57,000 | 41,850 | 12% |
| 66,500 | 133,000 | 91,600 | 22% |
| 121,800 | 243,600 | 129,850 | 24% |
| 217,875 | 435,750 | 225,900 | 32% |
| 272,325 | 544,650 | 280,350 | 35% |
| 656,700* | 800,900 | 664,750 | 37% |

\* MFS: use $400,450 for the 37% rate. Each row equals the 2026 bracket start plus the 2026 standard deduction (Rev. Proc. 2025-32 §§4.01, 4.14).

Steps (form, page 2):
1. Find the rate for total income **not including** the payment.
2. Find the rate for total income **plus** the taxable amount of the payment.
3. Same rate → enter it (form Example 1: single, $70,000 + $20,000 → 22%).
4. Different rates → amount in the lower bracket × lower rate + amount in the higher bracket × higher rate, ÷ taxable amount, round up to the next whole number (form Example 2: single, $60,000 + $20,000: $6,500 × 12% + $13,500 × 22% = $3,750 → 18.75% → 19).
5. Simpler but may over-withhold: use the rate for total income including the payment.

The tables "are most accurate if the appropriate amount of tax on all other sources of income, deductions, and credits has been paid through other withholding or estimated tax payments." Otherwise enter a higher rate. Full method and special cases: [`withholding-rates.md`](./withholding-rates.md).

### Common rate-selection patterns (2026)

- **Retiree with Social Security, taking a traditional IRA withdrawal**: the withdrawal can make Social Security taxable and the tables ignore the 65+ deductions; build a with/without projection instead (see [`../examples/ira-lump-sum-withdrawal.md`](../examples/ira-lump-sum-withdrawal.md): 8% computed vs. 10% default).
- **Working professional in the 24% band taking a $20,000 IRA withdrawal**: if wage withholding already covers the wages, the table gives 24%.
- **Under 59½, no §72(t) exception**: table rate plus 10 points covers the additional tax (see [`../examples/laid-off-401k-cash-out.md`](../examples/laid-off-401k-cash-out.md): 24% + 10% = 34%).
- **Roth conversion from a traditional IRA**: nonperiodic, 10% default; ask whether the user wants tax withheld (withholding reduces the amount converted) or paid by estimated tax.
- **401(k) cash-out, 60-day rollover planned**: ERD; 20% is withheld; rolling over the full amount requires replacing the 20% from other funds. A direct rollover avoids this.

---

## Signature block

The recipient signs and dates. The form contains no separate perjury jurat text; the Privacy Act notice warns that "providing fraudulent information may subject you to penalties" and that a form not properly completed leaves the payment at the default rate. The payer does NOT sign.

Each payee (for example, a former spouse receiving a QDRO distribution as alternate payee) gives the payer their own W-4R for their own payment.

---

## What's NOT on Form W-4R but matters

### State income tax withholding

Form W-4R covers federal income tax withholding only. State rules for retirement distributions vary (some states default to or require state withholding, some have no income tax). The payer typically provides its own state election alongside the W-4R. Ask the payer; this skill handles federal only.

### §72(t) 10% additional tax on early distributions

If the recipient is under 59½ and takes a taxable distribution from an IRA or employer plan, IRC §72(t) adds a 10% additional tax unless an exception applies. It is reported on Schedule 2 (Form 1040) line 8; Form 5329 is required unless box 7 of every Form 1099-R shows code 1 and the tax is owed on the full amount, in which case the box on line 8 is checked instead (2025 Schedule 2; 2025 Instructions for Form 5329).

The W-4R default rates don't account for it. Withholding is a credit against total tax, so the recipient can raise line 2 (e.g., 22% + 10% = 32%) or pay estimated tax. If the recipient elects 22% on a $30,000 distribution and owes the §72(t) tax: $6,600 withheld, $3,000 additional tax still due.

### §72(t) exceptions (2025 Instructions for Form 5329, exception numbers)

01 separation from service in or after the year of reaching 55 (50 for qualified public safety employees; plans, not IRAs) · 02 substantially equal periodic payments · 03 total and permanent disability · 04 death · 05 unreimbursed medical expenses over 7.5% of AGI · 06 QDRO payments to an alternate payee (plans, not IRAs) · 07 IRA distributions to certain unemployed individuals for health insurance · 08 IRA distributions for qualified higher education expenses · 09 IRA distributions for a first home, up to $10,000 · 10 IRS levy · 11 qualified reservist distributions · 12 incorrectly coded distributions · 13 section 457 plan distributions not from a rollover · 14 pre-March 1, 1986 elections · 15 §404(k) dividends · 16 annuity investment before August 14, 1982 · 17 federal phased retirement annuity · 18 §414(w) permissible withdrawals · 19 qualified birth or adoption distributions up to $5,000 · 20 terminal illness · 21 corrective distributions of income on excess contributions · 22 domestic abuse victims · 23 emergency personal expense distributions · 99 more than one.

Hardship is not an exception: a hardship distribution is subject to §72(t) unless one of the listed exceptions applies. Ask which exception the user claims; never assume one.

### Form 1099-R reporting

After the payment, the payer reports it on Form 1099-R (Instructions for Forms 1099-R and 5498):

- Box 1: Gross distribution
- Box 2a: Taxable amount
- Box 4: Federal income tax withheld (the W-4R rate applied)
- Box 7: Distribution code (e.g., 1 = early distribution, no known exception; 7 = normal distribution; G = direct rollover)

The recipient reports IRA distributions on Form 1040 lines 4a/4b and pension/plan distributions on lines 5a/5b (box 1 of 5c for a rollover), and claims box 4 on line 25b (2025 Form 1040; Pub. 575 (2025), "How to report").

### Direct rollover (alternative to W-4R withholding on an ERD)

If the goal is to move retirement money without paying tax now:

- **Plan → IRA or plan**: direct rollover under IRC §401(a)(31); no withholding (IRC §3405(c)(2); Pub. 575 (2025), Table 1); 1099-R code G
- **IRA → IRA**: trustee-to-trustee transfer; not a distribution, not reported on Form 1099-R (Pub. 590-B (2025); Instructions for Forms 1099-R and 5498, "Transfers")
- **Plan pre-tax → Roth IRA by direct rollover**: no withholding, but the taxable amount is income (Pub. 575 (2025), "Rollovers to Roth IRAs")

The recipient opens the receiving account, asks the plan for a direct rollover, and the plan pays the receiving custodian. If moving funds (not spending them) is the goal, surface the direct rollover before drafting a W-4R.

---

## Recipient's options summary

| Goal | Line 2 | Notes |
|------|--------|-------|
| Take cash, no current withholding (other nonperiodic, U.S. address) | 0 | Tax still owed; consider estimated tax |
| Take cash, withhold about the tax | Rate from the Marginal Rate Tables or a projection | Add 10 points if §72(t) applies and the user wants it covered |
| Take cash, over-withhold | Above the computed rate | Cash tied up until refund |
| 401(k) 60-day rollover | Blank (20% applies) or more than 20 | Replace the 20% from other funds to roll over the full amount |
| Direct rollover / trustee-to-trustee transfer | No W-4R | No withholding |
| Roth conversion from a traditional IRA | Ask (0–100) | Withholding reduces the amount converted |
| RMD (age 73, Pub. 590-B (2025)) | 10% default; adjust as needed | RMDs are not ERDs |
| Hardship withdrawal | 10% default; adjust as needed | Not an ERD; §72(t) may apply |
| Severance pay | — | Wages; use Form W-4, not W-4R |
