# Withholding rates on Form W-4R — defaults, mandatory minimums, and overrides

Form W-4R sets the federal income tax withholding rate on a nonperiodic payment or an eligible rollover distribution. The right rate depends on whether the payment is an **eligible rollover distribution (ERD)** or an **other nonperiodic payment** under IRC §3405. Verified 2026-10-06 against the 2026 Form W-4R (rates, Marginal Rate Tables, Examples 1–2), Pub. 505 (2026) chapter 1 and Pub. 575 (2025).

This reference covers the rate mechanics in depth.

---

## The two rate regimes

### Regime A — Eligible rollover distribution (ERD)

Authority: IRC §3405(c).

**Default rate and floor: 20%** of the taxable amount. "You can't choose withholding at a rate of less than 20% (including '-0-')" (2026 Form W-4R, page 2).

The recipient may **increase** the rate above 20% on line 2 — up to 100%. Common reasons to increase:

- Recipient's marginal rate is above 20%
- Recipient is under 59½ and wants the §72(t) 10% additional tax covered
- Recipient wants this withholding to cover tax on other income that has no withholding

"Don't give Form W-4R to your payer unless you want more than 20% withheld." A blank line 2 or a "0" leaves the 20% in place.

**The only way to avoid the 20% on an ERD**: a **direct rollover** to another plan or an IRA. "There is no withholding" on a direct rollover (Pub. 575 (2025), Table 1; IRC §3405(c)(2)). The plan reports it on Form 1099-R with **code G**.

Exceptions where no withholding is required even when paid to the participant: ERDs from the same plan totaling less than $200 for the year; a distribution consisting solely of employer securities plus $200 or less cash; the net unrealized appreciation part of employer securities (Pub. 575 (2025)).

### Regime B — Other nonperiodic payment

Authority: IRC §3405(b).

**Default: 10%.** Applied if no W-4R is given or line 2 is blank.

The recipient may enter any whole-number rate from 0 to 100. To opt out, enter "-0-". The choice stays in effect for future payments from the same plan or IRA until changed (form, page 1; Pub. 505 (2026)).

Limits on going below 10%:

- **Delivered outside the U.S.**: "Generally, you are not permitted to elect to have federal income tax withheld at a rate of less than 10% (including '-0-') on any payments to be delivered outside the United States and its territories" (form, page 2). A U.S. citizen or resident alien can opt out only by giving the payer a U.S. or territory home address (Pub. 505 (2026); Pub. 575 (2025)).
- **No SSN / incorrect SSN**: if the recipient doesn't give the payer an SSN, or the IRS notifies the payer it is incorrect, the payer withholds 10% and can't honor a lower rate (form, page 2 Note).

---

## Which distributions are ERDs vs. other nonperiodic?

Full classification, with the form's non-ERD list and the wage and no-form cases: [`distribution-types.md`](./distribution-types.md). Short version:

### ERDs (20%)

- Lump-sum or partial cash-out from a 401(k), profit-sharing, money purchase, or ESOP plan paid to the participant
- 403(b) or governmental 457(b) distribution paid to the participant
- Defined benefit lump-sum cash-out
- Surviving spouse's rollover-eligible distribution from a deceased participant's plan

### Other nonperiodic (10% default)

- **IRA distributions** (traditional, SEP, SIMPLE), including IRA distributions payable on demand
- **RMDs**, **hardship distributions**, **substantially equal payment series**, **corrective distributions** (not ERDs; §402(c)(4); Pub. 575 (2025))
- The form's other non-ERD items: PLESA distributions, domestic abuse victim distributions, qualified disaster recovery distributions, qualified birth or adoption distributions, qualified long-term care distributions, emergency personal expense distributions
- Nonperiodic commercial annuity payments

### Not W-4R at all

- **Periodic payments** (installments over more than 1 year) → W-4P (IRC §3405(a))
- **Wages, including severance pay** → W-4 (Pub. 15 (2026): severance payments are wages)
- **Nonresident aliens and foreign estates** → Pub. 515 / Pub. 519

---

## How to override the default

### To increase ERD withholding above 20%

Enter the desired whole number on line 2 (e.g., "24", "34").

The payer applies the rate to the taxable amount. Example: $50,000 fully taxable ERD with line 2 = "30":

- Gross distribution: $50,000
- Federal withholding: $50,000 × 30% = $15,000
- Net to recipient: $35,000

Form 1099-R reports box 1 $50,000, box 4 $15,000.

### To opt out of nonperiodic withholding (other than ERD)

Enter "-0-" on line 2 (U.S. or territory home address on file).

Example: $20,000 IRA cash withdrawal with line 2 = "-0-":

- Gross distribution: $20,000
- Federal withholding: $0
- Net to recipient: $20,000

The recipient still owes the tax on the $20,000 (and may need estimated tax to avoid a §6654 penalty).

### To set a custom nonperiodic rate

Any whole number 0–100. Example: $30,000 IRA cash withdrawal with line 2 = "22":

- Gross distribution: $30,000
- Federal withholding: $30,000 × 22% = $6,600
- Net to recipient: $23,400

---

## Rate selection: the form's Marginal Rate Tables (2026)

Printed on page 1 of the 2026 Form W-4R. "Add your income from all sources and use the column that matches your filing status." Each threshold equals the 2026 bracket start plus the 2026 standard deduction (Rev. Proc. 2025-32 §§4.01, 4.14; checked in python).

| Rate for every dollar more | Single or MFS: total income over | MFJ or QSS: total income over | HoH: total income over |
|---|---|---|---|
| 0% | $0 | $0 | $0 |
| 10% | $16,100 | $32,200 | $24,150 |
| 12% | $28,500 | $57,000 | $41,850 |
| 22% | $66,500 | $133,000 | $91,600 |
| 24% | $121,800 | $243,600 | $129,850 |
| 32% | $217,875 | $435,750 | $225,900 |
| 35% | $272,325 | $544,650 | $280,350 |
| 37% | $656,700 (MFS: $400,450) | $800,900 | $664,750 |

### The form's two-step method

1. **Step 1**: rate for total income **not including** the payment.
2. **Step 2**: rate for total income **plus** the taxable amount of the payment.
3. Same → enter it. Form Example 1 (single, $20,000 payment, $70,000 other income): both 22% → enter "22".
4. Different → (amount in lower bracket × lower rate) + (amount in higher bracket × higher rate), ÷ taxable amount, round up to the next whole number. Form Example 2 (single, $20,000 payment, $60,000 other income): $6,500 × 12% = $780; $13,500 × 22% = $2,970; $3,750 ÷ $20,000 = 18.75% → enter "19".
5. Simpler alternative (may over-withhold): the rate for total income including the payment.

If the payment spans more than two bands, extend the split to every band it crosses.

### When the tables are wrong for the user

The tables assume the tax on all other income is already covered by other withholding or estimated tax ("If the appropriate amount of tax on those sources of income has not been paid... enter a rate that is greater than the rate in the Marginal Rate Tables"). They also don't model:

- Social Security benefits that become taxable because of the payment (Pub. 915)
- The additional standard deduction for age 65+ or blind ($1,650 married / $2,050 unmarried for 2026, Rev. Proc. 2025-32 §4.14(3)) and the Schedule 1-A senior deduction (up to $6,000 per eligible person, 2025–2028; P.L. 119-21)
- Capital gains and qualified dividends taxed at 0/15/20%
- Credits

In those cases build a with/without projection on the 2026 rate schedule and divide the extra tax by the taxable amount (worked in [`../examples/ira-lump-sum-withdrawal.md`](../examples/ira-lump-sum-withdrawal.md)). Show the math; let the user choose.

---

## Special cases

### Roth IRA distribution

Withholding applies only to the taxable part; "There will be no withholding on any part of a distribution where it is reasonable to believe that it won't be includible in gross income" (Pub. 575 (2025)). A **qualified** Roth distribution (5-year period met AND age 59½, death, disability, or first home up to $10,000; IRC §408A(d)(2)) is not taxable, so no withholding applies. A **nonqualified** distribution can have a taxable earnings part (ordering rules in Pub. 590-B: contributions first, then conversions, then earnings). Ask the custodian how it withholds.

### Roth conversion

A traditional IRA → Roth IRA conversion is a taxable IRA distribution (reported on Form 1099-R even when done trustee-to-trustee), so the 10% default applies unless the recipient elects otherwise. Points to put to the user (ask; don't decide for them):

- Any amount withheld is not converted, so less ends up in the Roth
- The withheld amount is a distribution; if the user is under 59½ it can also be subject to the §72(t) 10% additional tax (Pub. 590-B)
- Paying the tax from other funds with estimated tax keeps the full amount in the Roth

A direct rollover of pre-tax plan money to a Roth IRA is not subject to withholding at all (Pub. 575 (2025), "Rollovers to Roth IRAs"; Table 1).

### §72(t) additional tax (not in the default rates)

If the recipient is under 59½ and no exception applies, IRC §72(t) adds 10% of the taxable amount, reported on Schedule 2 (Form 1040) line 8 (Form 5329 when required). The W-4R default rates and the Marginal Rate Tables don't include it. Withholding is a credit against total tax, so the recipient can add 10 points to line 2 or pay estimated tax.

If the recipient elects 22% on a $30,000 IRA distribution at age 40 with no exception:

- Federal income tax withholding: $6,600
- §72(t) additional tax: $3,000 (10% of $30,000) — not withheld at 22%; due with the return
- Net to recipient: $23,400; after paying the $3,000 at filing: $20,400

Common mistake: recipient assumes 22% covers everything; ends up owing $3,000 plus any underpayment penalty.

### State withholding

W-4R covers federal only. State withholding on retirement distributions is set by state law and varies (some states default to or require withholding for residents; some have no income tax). The payer's distribution request usually has a separate state section. Ask the payer which state rules it applies; do not guess.

---

## Summary

| Payment type | Default withholding | Min | Max |
|-------------------|---------------------|-----|-----|
| Eligible rollover distribution (ERD) | 20% | 20% | 100% |
| Other nonperiodic | 10% | 0% (10% if delivered outside the U.S.) | 100% |
| Periodic | (use W-4P, not W-4R) | — | — |
| Wages, including severance | (use W-4, not W-4R) | — | — |
| Direct rollover / trustee-to-trustee transfer | none (W-4R not needed) | — | — |
| Payment reasonably believed nontaxable (e.g., qualified Roth) | none | — | — |

The recipient's job: classify the payment correctly, then pick a rate within the allowed range.
