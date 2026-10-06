---
name: form-9465
description: >
  Use this skill when an individual or a sole proprietor (including one whose
  business has closed) cannot pay a federal tax balance in full and wants a
  monthly IRS payment plan, either by Form 9465 or by deciding that the online
  application is the better channel. Triggers on phrases like "Form 9465",
  "installment agreement", "IRS payment plan", "can't pay my tax bill", "pay
  the IRS monthly", "set up a payment plan with the IRS", "streamlined
  installment agreement", "Online Payment Agreement", "OPA", "direct debit
  installment agreement", "Form 433-F with 9465", "balance due notice and I
  can't pay". Do NOT use for: settling the debt for less than the full amount
  (offer in compromise) — use form-656; removing penalties or interest — use
  form-843; amending a return to reduce the tax — use form-1040-x; an
  operating business that owes payroll taxes, or a corporation or
  partnership (they call the IRS; Form 9465 does not apply); anyone in
  bankruptcy or with an offer in compromise pending (call 800-829-1040).
form: Form 9465 (Installment Agreement Request)
audience: [individual, solo, freelance, llc1]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f9465.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i9465.pdf
---

# Form 9465 — Installment Agreement Request

This skill produces a filled, line-numbered draft of Form 9465 plus a routing decision: whether the user should file the form at all, or use the IRS Online Payment Agreement (OPA), a short-term plan, or a phone call instead. The arithmetic is three subtractions and one division. The judgment concentrates in four places: the channel (online vs paper changes the fee by up to $109), the $25,000 and $50,000 thresholds that trigger direct debit, payroll deduction, or Form 433-F, the line 10 benchmark that decides whether a financial statement is needed, and the eligibility stops (unfiled returns, bankruptcy, a pending offer, an operating business with payroll tax).

**Companion guide for end users:** [Form 9465 (2026): How to Set Up an IRS Installment Agreement](https://jupid.com/blog/form-9465-installment-agreement-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

**Revision verified:** the line map was built from the PDF text of **Form 9465 (Rev. September 2020)** and **Instructions for Form 9465 (Rev. July 2024)**, the current revisions on 2026-10-06. User fees come from the irs.gov payment plans page (fee section "updated March 3, 2026"; page last reviewed 13-Aug-2026), **not** from the fee table in the July 2024 instructions, which is out of date ($22 online direct debit and $10 online reinstatement there, vs $29 and $6 on irs.gov). Before use, re-check https://www.irs.gov/forms-pubs/about-form-9465 for a new form or instructions revision and https://www.irs.gov/payments/payment-plans-installment-agreements for fees. If either changed, rebuild the line map and fee table from the new text.

### Key numbers (year-dependent; re-check on the pages named)

| Item | Value | Source |
|------|-------|--------|
| Guaranteed agreement limit | Tax-only balance ≤ $10,000, paid within 3 years | IRC §6159(c); i9465 |
| Streamlined, no payment-method condition | Assessed balance ≤ $25,000 | i9465 "Streamlined installment agreement" |
| Streamlined with direct debit or payroll deduction | $25,001–$50,000 | i9465; Form 9465 line 11b |
| Form 433-F required | Line 9 > $50,000, or payment below line 10 that cannot be raised | Form 9465 line 11b |
| Benchmark payment (line 10) | Line 9 ÷ 72.0 | Form 9465 line 10 |
| Payment term limit (streamlined) | 72 months or the CSED, whichever is less | i9465 |
| Payment day | 1st–28th | Form 9465 line 12 |
| Online long-term eligibility | ≤ $50,000 combined tax, penalties, interest; all returns filed | OPA page |
| Short-term plan | ≤ 180 days; "less than $100,000" (irs.gov) / "$100,000 or less" (i9465) | irs.gov; i9465 |
| Fees, direct debit | $29 online / $107 phone, mail, in person | irs.gov payment plans page (updated March 3, 2026) |
| Fees, non-direct debit | $69 online / $178 phone, mail, in person | same |
| Low-income | AGI ≤ 250% of federal poverty guidelines; DDIA fee waived; otherwise $43, reimbursable via line 13c | i9465; irs.gov; Form 13844 (Rev. 2-2026) |
| Failure-to-pay rate during an agreement | 0.25%/month instead of 0.5%, only if the return was filed on time | IRC §6651(h) |

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user mentions Form 9465, an installment agreement, a payment plan, or paying the IRS monthly.
- The user has a balance on a return they are filing, or a balance-due notice, and says they cannot pay it all.
- The user asks whether they need Form 433-F, or what the IRS payment plan fee is.
- The user closed a sole proprietorship and owes Form 941, 943, or 940 balances from it, plus or minus income tax.
- The user owes a trust fund recovery penalty as an individual.

Do **not** engage this skill (and say why) when:

- The user wants to settle for less than the full balance → offer in compromise, `../form-656/SKILL.md`. If line 11a cannot pay the balance before the collection statute ends, mention that skill as an alternative a CPA should compare; do not choose for the user.
- The user wants penalties or interest removed → `../form-843/SKILL.md`. Recommend checking abatement **before** fixing the payment, because an abated penalty shrinks the balance the plan is built on.
- The user's business is still operating and owes employment or unemployment taxes → not Form 9465; the business calls the number on its most recent notice (i9465, "Who should not use this form?").
- The debtor is a corporation, partnership, or multi-member LLC → business accounts cannot apply online and must call the notice number or 800-829-4933 (OPA page). Form 9465 is for individuals and out-of-business sole proprietors.
- The user is in bankruptcy, or has a pending or accepted offer in compromise → do not file; call 800-829-1040 (i9465, "Bankruptcy or offer in compromise").
- The user can pay within 180 days → short-term plan, $0 setup (irs.gov payment plans page); no Form 9465.
- The user wants to change the tax itself → `../form-1040-x/SKILL.md`.

Sibling skills used along the way:
- `../form-4506-t/SKILL.md` — account transcript to confirm balances, assessment dates, and tax-only amounts.
- `../form-1040/SKILL.md` — when Form 9465 rides on the front of a return being filed now.
- `../form-1040-es/SKILL.md` — keeping next year's estimated tax current so the agreement does not default.
- `../form-941/SKILL.md` — reading the employment-tax periods of a closed business.

---

## Prerequisites

Before producing anything, get these inputs. If any is missing, ask for it explicitly and stop until answered. Never estimate a balance, an income figure, or a bank number.

1. **Every balance, by form and period**, read from the return being filed, from IRS notices, or from an account transcript / IRS Online Account. Ask: "Please read me the balance on each IRS notice (or the amount-you-owe line of the return), with the form number and year or quarter." These become the header, line 5, and line 6.
2. **Any other IRS balance not on those documents**, including balances already in an existing installment agreement (line 6).
3. **All required returns filed?** Ask for each of the last several years. If any is missing, stop: the request will be denied (i9465).
4. **Bankruptcy or offer in compromise pending or accepted?** If yes, stop and route.
5. **Business status** if any balance is employment tax: is the business still operating? If yes, stop and route. If closed, get the business name and EIN (line 2).
6. **Filing status and both spouses' names and SSNs** in the order they appear on the return (joint return → both sign).
7. **Whether any year in the request was filed with Schedule C, E, or F**, and the **state of residence** (or foreign/APO/territory status). These pick the mailing address.
8. **Payment sent with the request** (line 8), if any.
9. **Monthly payment the user can afford** (line 11a), stated by the user.
10. **Payment day**, 1st–28th (line 12).
11. **Payment method**: direct debit, payroll deduction (Form 2159 with employer signature), or monthly payments by other means. Collect bank numbers only at the moment of filling lines 13a/13b, after the user consents to the printed ACH authorization.
12. **Default on an installment agreement in the last 12 months?** (Part II trigger.)
13. **Low-income check inputs**: AGI from the most recent return and family unit size (dependents claimed including the user and spouse), and residence (48 states/DC/territories, Alaska, Hawaii). Compare with the Form 13844 table; do not assume.
14. **Online account**: can and will the user use an IRS Online Account? Determines whether OPA is offered as the main path.
15. **For balances over $50,000 or a payment below line 10**: every Form 433-F figure (accounts, real estate, other assets, credit cards, business data, employment, non-wage income, monthly living expenses). Collect from the user's statements; never fill from assumptions.
16. **Phone numbers and best times to call** (lines 3 and 4).

---

## Workflow

Execute in order. Do not skip ahead.

### Step 1 — Eligibility stops

Run these checks and stop with a plain explanation at the first failure:
- Any required return unfiled → file first.
- Bankruptcy, or offer in compromise pending/accepted → call 800-829-1040.
- Operating business with employment/unemployment tax, or an entity → call the notice number or 800-829-4933.

### Step 2 — Confirm the balance from documents

Build a table: form, period, balance, source document. Total it. If the user only has a memory of the amount, have them retrieve the notice, log in to their IRS Online Account, or request an account transcript (`../form-4506-t/SKILL.md`). Ask whether any penalties might qualify for abatement and offer `../form-843/SKILL.md` before locking in the plan.

### Step 3 — Choose the channel

Use the decision tree in [`filing.md`](./filing.md):
- Full payment possible → pay; $0.
- 180 days or less → short-term plan; $0 (balance "less than $100,000" on irs.gov, "$100,000 or less" in i9465; flag if the balance is near the line).
- Individual, all returns filed, combined balance ≤ $50,000, can use an Online Account → **offer OPA first**: $29 with direct debit or $69 without, vs $107 or $178 on paper (irs.gov payment plans page). Record the user's choice.
- Otherwise → Form 9465.

### Step 4 — Classify the agreement (for the user's understanding, not a label on the form)

See [`references/agreement-types-and-fees.md`](./references/agreement-types-and-fees.md):
- **Guaranteed** (IRC §6159(c)): income tax, tax-only balance ≤ $10,000 (excluding penalties and interest), clean 5-year filing/paying/no-IA history, full payment within 3 years. Ask for the tax-only amount; the IRS decides financial inability.
- **Streamlined** (i9465): ≤ $25,000; or $25,001–$50,000 with direct debit or payroll deduction; full payment within 72 months or by the CSED, whichever is less.
- **Over $50,000**: Form 433-F required.
- **Partial payment (PPIA)**: payment will not clear the balance before the CSED; financial statement and periodic reviews.

### Step 5 — Compute lines 5–10

```
Line 7  = Line 5 + Line 6
Line 9  = Line 7 − Line 8
Line 10 = Line 9 ÷ 72.0   (round to cents)
```

### Step 6 — Set lines 11a and 11b

- Enter the user's stated amount on 11a. If the user leaves it blank, tell them the IRS will divide the line 9 balance by 72 (form text).
- If 11a < line 10, ask: "Can you raise the payment to at least $[line 10]?" Yes → enter the new amount on 11b. No → check the box under 11b and require Form 433-F.
- If line 9 > $50,000 → Form 433-F regardless.
- If $25,000 < line 9 ≤ $50,000 and 11a (or 11b) ≥ line 10 → no Form 433-F, but line 13 or line 14 is required.
- If the user defaulted on an agreement in the last 12 months, $25,000 < line 9 ≤ $50,000, and 11a/11b < line 10 → complete Part II as well.

### Step 7 — Payment day and method (lines 12–14)

See [`references/payment-methods.md`](./references/payment-methods.md). Day 1–28. For direct debit, read the ACH authorization to the user and get explicit consent, then validate the routing number (9 digits, first two 01–12 or 21–32) and account number (≤ 17 characters, hyphens kept). For payroll deduction, line 14 plus Form 2159 with the employer's portion signed. Line 13c only for a low-income user who cannot pay electronically.

### Step 8 — Fee and low-income status

State the user fee for the chosen channel and method from the irs.gov table. Run the low-income comparison against the Form 13844 (Rev. 2-2026) table using the user's AGI and family unit size. Low-income + direct debit → fee waived; low-income without direct debit → $43, reimbursable on completion only if 13c is checked. If the IRS charges the full fee to a user who qualifies, Form 13844 must be filed within 30 days of the acceptance letter date.

### Step 9 — Part II and attachments

Complete Part II (lines 15–27) only under the three-condition test. Lines 21–22 only for a married user who lives with and shares household expenses with the spouse, or lives in a community property state. List required attachments: Form 433-F, Form 2159, payment check.

### Step 10 — Validate, then produce the deliverable

Run **Validation** below. Emit the **Output format** draft with every line shown, including blanks and zeros, a mailing address, the fee, and the sources list.

### Step 11 — Hand off to filing

Follow [`filing.md`](./filing.md): attach to the front of a return being filed, or mail standalone to the i9465 table address (pick the Schedule C/E/F table if any year in the request included those schedules), or walk the user through OPA. The user signs and submits. Tell the user what happens next, each point from i9465 unless noted:

- The IRS usually replies within 30 days; a request for tax due on a return filed after March 31 can take longer.
- The approval notice states the terms, the first due date, and the user fee.
- If no reply arrives by the chosen payment day, send the first payment to the same service center address or pay at IRS.gov/Payments.
- While the request is pending and while the agreement is in effect, the IRS generally does not levy; the collection period is suspended or prolonged.
- Interest and the failure-to-pay penalty continue until the balance is paid (0.25% a month during the agreement only if the return was filed on time, IRC §6651(h)).
- Refunds are applied to the balance; the monthly payment is still due that month.
- Missing a payment, or not paying a later year's balance, can default the agreement (see IRS.gov/CP523 for terminated agreements).
- If the user is low-income and the IRS charged the full fee: Form 13844 within 30 days of the acceptance letter date (Form 13844, Rev. 2-2026).

---

## Line-by-line guidance

Full map with every field: [`references/line-by-line.md`](./references/line-by-line.md). Key rules:

| Line | Entry | Rule (source: Form 9465 Rev. 9-2020 / i9465 Rev. 7-2024) |
|------|-------|-------------------------------------------------------------|
| Header | Form(s); tax year(s) or period(s) | Every form type and period included on lines 5–6 |
| 1a | Names, SSNs, address | Joint: same order as on the return. Foreign address: city on the city line, then the three foreign fields |
| 1b | New address box | Check if the address is new since the last return |
| 2 | Business name and EIN | Only for a business that is no longer operating |
| 3, 4 | Home and work phone, best time | |
| 5 | Total owed per return(s)/notice(s) | From documents; may span several years |
| 6 | Other balances | Include amounts already in an existing agreement and charges not on a return or notice |
| 7 | 5 + 6 | |
| 8 | Payment sent now | Standalone: check/money order to "United States Treasury" with name, address, SSN/EIN, phone, year and return |
| 9 | 7 − 8 | Thresholds: $25,000 and $50,000 |
| 10 | 9 ÷ 72.0 | Benchmark; ignores future interest |
| 11a | Monthly payment | Total for all liabilities if an agreement exists; blank → IRS uses balance ÷ 72 |
| 11b | Revised payment / 433-F box | Box + Form 433-F if the user cannot reach line 10 |
| 12 | Payment day | 1st–28th |
| 13a, 13b | Routing, account | 9 digits, prefix 01–12 or 21–32; ≤ 17 characters |
| 13c | Low-income, cannot pay electronically | Fee reimbursed on completion |
| 14 | Payroll deduction | Attach Form 2159; employer signs its part |
| Signatures | Taxpayer; spouse if joint | Both must sign a joint request; direct debit not approved otherwise |
| Part II | Lines 15–27 | Only if: default in last 12 months AND $25,000 < owed ≤ $50,000 AND 11a/11b < line 10 |

### Edge cases

- **Existing agreement plus a new balance**: put the new balance on line 5 and the balance already in the agreement on line 6; line 11a is the proposed total monthly payment for everything (form text, lines 6 and 11a). Ask whether the user would rather revise the existing agreement online (irs.gov lists $6 online, $89 by phone or mail).
- **Trust fund recovery penalty owed as an individual**: eligible to use Form 9465 (i9465, "Who should use this form?"). List the penalty periods in the header the way the notice shows them.
- **Individual shared responsibility payment**: eligible; it is not subject to penalties, liens, or levies, but interest accrues and refunds are applied (i9465).
- **Closed sole proprietorship with Forms 941/943/940**: use line 2 for the business name and EIN; the header lists each employment-tax period.
- **Foreign address, APO/FPO, U.S. territory, Form 2555 or 4563 filer, dual-status alien**: standalone requests go to the Austin address in [`filing.md`](./filing.md); residents of American Samoa, Puerto Rico, Guam, the U.S. Virgin Islands, or the Northern Mariana Islands follow Pub. 570.
- **Married, non-liable spouse in the household**: lines 21–22 apply in Part II when the couple shares household expenses or lives in a community property state, whatever the filing status (i9465, "Lines 21 and 22").
- **Return filed after March 31**: the IRS may take longer than 30 days to reply (i9465). If no reply by the chosen payment day, send the first payment anyway (see payment-methods reference).

---

## Validation

Run every check. Surface failures; do not silently fix.

### Math checks

- [ ] Line 5 equals the sum of the balance table built in Step 2
- [ ] Line 7 = line 5 + line 6
- [ ] Line 9 = line 7 − line 8
- [ ] Line 10 = line 9 ÷ 72.0, rounded to cents
- [ ] 11a compared with line 10; 11b and its box set consistently

### Threshold checks

- [ ] Line 9 > $50,000 → Form 433-F listed as an attachment
- [ ] $25,000 < line 9 ≤ $50,000 and no Form 433-F → line 13a/13b completed or line 14 checked with Form 2159
- [ ] 11a/11b < line 10 and cannot increase → 11b box checked and Form 433-F listed
- [ ] Part II completed only when all three conditions hold; lines 21–22 only under the spouse conditions
- [ ] Line 12 is between 1 and 28

### Field checks

- [ ] Header lists every form type and period on lines 5–6
- [ ] Joint request: both names and SSNs in return order; two signature lines
- [ ] Line 2 filled only for a closed business
- [ ] Routing number: 9 digits, first two 01–12 or 21–32; account number ≤ 17 characters, no spaces or symbols other than hyphens; both read back to the user and masked in the draft
- [ ] Line 13c checked only for a low-income user who cannot pay electronically, and not together with 13a/13b

### Sanity checks (warn, do not block)

- [ ] OPA was available (individual, returns filed, ≤ $50,000) and the user chose paper → record the fee difference shown to the user
- [ ] Balance within 180-day reach → short-term plan offered
- [ ] Penalties on the balance not yet reviewed for abatement → offer `../form-843/SKILL.md`
- [ ] Line 11a equals line 10 exactly → tell the user interest and penalties continue, so the balance will not be gone in 72 months
- [ ] Months-to-pay without interest (line 9 ÷ payment) exceeds months left to the earliest CSED (from the transcript) → PPIA likely; mention `../form-656/SKILL.md` and a CPA
- [ ] Return filed late → the 0.25% failure-to-pay rate under IRC §6651(h) does not apply
- [ ] User underpaid estimated tax this year → a new balance can default the agreement; route to `../form-1040-es/SKILL.md`
- [ ] Low-income user charged the full fee → Form 13844 within 30 days of the acceptance letter

---

## Output format

```markdown
# Form 9465 — DRAFT (Rev. September 2020)

## Routing decision
Channel: Form 9465 attached to return | Form 9465 standalone | OPA (no form) | Short-term plan | Phone
Why: <one line>
Fee: $XX (<online|phone/mail>, <direct debit|non-direct debit>; irs.gov payment plans page, updated March 3, 2026)
Low-income: Yes | No (AGI $X, family unit size N, Form 13844 Rev. 2-2026 threshold $X)

## Balance table
| Form | Period | Balance | Source document |
|------|--------|---------|-----------------|

## Header
This request is for Form(s): <1040 | 1040, 941 | ...>
Tax year(s) or period(s): <...>

## Part I
1a. Name / SSN: <name> •••-••-XXXX ; Spouse: <name or blank> •••-••-XXXX
    Address: <street, apt, city, state, ZIP> ; Foreign fields: <or blank>
1b. New address: [ ] / [X]
2.  Business (no longer operating) / EIN: <or blank>
3.  Home phone / best time: <...>
4.  Work phone / ext. / best time: <...>
5.  Total owed per return(s)/notice(s):   $X.XX
6.  Additional balances:                   $X.XX
7.  Line 5 + line 6:                       $X.XX
8.  Payment with request:                  $X.XX
9.  Amount owed:                           $X.XX
10. Line 9 ÷ 72.0:                         $X.XX
11a. Monthly payment:                      $X.XX
11b. Revised payment:                      $X.XX | blank ; 433-F box: [ ] / [X]
12. Payment day:                           NN
13a. Routing:                              •••••XXXX | blank
13b. Account:                              •••••XXXX | blank
13c. Low-income, unable to pay electronically: [ ] / [X]
14. Payroll deduction (Form 2159):         [ ] / [X]
Signatures: <taxpayer> ; <spouse if joint>

## Part II (lines 15–27): <completed values | "Not required — <reason>">

## Attachments
- [ ] Form 433-F  - [ ] Form 2159  - [ ] Check for line 8

## Mailing
<"Attach to front of <year> Form <...>, mail to the return's address" | full i9465 table address>

## Validation summary
- Math: <pass | failures>
- Thresholds: <pass | failures>
- Fields: <pass | failures>
- Sanity warnings: <list>
- Status: READY FOR USER SIGNATURE | NOT READY — <missing item>

## Next steps for the user
- <reply timing, first payment, refunds offset, interest/penalty continue, future compliance>

## Sources cited in this draft
- Form 9465 (Rev. 9-2020); Instructions for Form 9465 (Rev. 7-2024)
- IRS payment plans page (fees updated March 3, 2026); IRS OPA page
- <IRC §6159(c), §6651(h), Form 13844 Rev. 2-2026, Form 433-F Rev. 7-2024, as used>
```

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — every field of Form 9465, Parts I and II, with the exact conditions from the form and instructions
- [`references/agreement-types-and-fees.md`](./references/agreement-types-and-fees.md) — guaranteed, streamlined, PPIA, over-$50,000; current fee table; low-income rules and the Form 13844 table; what an agreement does not stop
- [`references/payment-methods.md`](./references/payment-methods.md) — direct debit, payroll deduction, line 13c, payment day, line 8 check details, default, modification fees
- [`references/common-mistakes.md`](./references/common-mistakes.md) — errors that delay, deny, or overcharge a request
- [`filing.md`](./filing.md) — channel decision tree, OPA and phone paths, both i9465 address tables plus the Austin address, consent and security rules

## Examples

- [`examples/w2-side-gig-attached-to-return.md`](./examples/w2-side-gig-attached-to-return.md) — single filer, $9,818 after a payment, form attached to a paper return on extension; OPA offered and declined
- [`examples/closed-sole-prop-941-balance.md`](./examples/closed-sole-prop-941-balance.md) — closed café, Form 1040 plus two Form 941 quarters, $31,046.13; direct debit required; Schedule C address table (Memphis)
- [`examples/joint-balance-over-50k-433f.md`](./examples/joint-balance-over-50k-433f.md) — married couple, $64,122.74, payment below line 10; Form 433-F required; possible PPIA; agent stops to collect financial data

## Sources

Re-verify each source every year and before every filing; fees and thresholds change.

- [Form 9465 (Rev. September 2020)](https://www.irs.gov/pub/irs-pdf/f9465.pdf)
- [Instructions for Form 9465 (Rev. July 2024)](https://www.irs.gov/pub/irs-pdf/i9465.pdf)
- [About Form 9465](https://www.irs.gov/forms-pubs/about-form-9465) — current revision check
- [IRS — Payment plans; installment agreements](https://www.irs.gov/payments/payment-plans-installment-agreements) — current fees (updated March 3, 2026), eligibility, Form 13844 address as listed there
- [IRS — Online payment agreement application](https://www.irs.gov/payments/online-payment-agreement-application) — online eligibility ($50,000 long-term, less than $100,000 short-term), business accounts, POA rules
- [Form 433-F (Rev. July 2024)](https://www.irs.gov/pub/irs-pdf/f433f.pdf) — Collection Information Statement
- [Form 2159](https://www.irs.gov/pub/irs-pdf/f2159.pdf) — Payroll Deduction Agreement
- [Form 13844 (Rev. February 2026)](https://www.irs.gov/pub/irs-pdf/f13844.pdf) — low-income user fee application and AGI table (2026 HHS guidelines)
- [IRS Collection Financial Standards](https://www.irs.gov/businesses/small-businesses-self-employed/collection-financial-standards) — living-expense standards used on Form 433-F
- [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) — needed only if the user asks for a payoff projection
- IRC §6159 (installment agreements; §6159(c) guaranteed agreements) — https://www.law.cornell.edu/uscode/text/26/6159
- IRC §6651(h) (0.25% failure-to-pay rate during an agreement for timely filed individual returns) — https://www.law.cornell.edu/uscode/text/26/6651
- 26 CFR 300.1 (installment agreement fee regulation; prints older amounts than irs.gov) — https://www.ecfr.gov/current/title-26/part-300/section-300.1
- Publication 594 (The IRS Collection Process) and Publication 1660 (Collection Appeal Rights), linked from the About Form 9465 page

## Disclaimer

This skill encodes the mechanics of IRS Form 9465 and the published IRS payment plan rules. It is not tax advice and does not create a CPA-client relationship. Choosing between an installment agreement, a partial payment agreement, and an offer in compromise depends on facts a licensed professional should review. Remind the user that the draft is a starting point and that the IRS decides whether to approve the request and on what terms.
