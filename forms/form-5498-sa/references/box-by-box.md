# Form 5498-SA — Box-by-Box Reference

Detailed reference for every box on Form 5498-SA. Load this when the user has a question about a specific box. Verified against the 2025 Form 5498-SA and the 2025 Instructions for Forms 1099-SA and 5498-SA; the continuous-use Form 5498-SA (Rev. December 2026) used for 2026 contributions keeps the same six boxes. Re-check https://www.irs.gov/forms-pubs/about-form-5498-sa.

---

## Header — Identifying Information

The top of Form 5498-SA contains:

### Trustee/Custodian Block (left side)

- **Trustee's or custodian's name**
- **Address**
- **TIN (Taxpayer Identification Number)** — the custodian's EIN
- **Telephone number** (sometimes)

This is the financial institution holding the HSA: Fidelity, Lively, HealthEquity, Optum Bank, HSA Bank, Bank of America, etc.

### Recipient Block (right side)

- **Recipient's name** — the account holder
- **Recipient's TIN** — usually their SSN
- **Address**
- **Account number** — the custodian's internal HSA account identifier (last 4 digits often shown)

### Verification rules

| Field | Verify against | If mismatch |
|-------|----------------|-------------|
| Recipient name | Official ID | Contact custodian for corrected form |
| Recipient SSN | SSA card | Contact custodian IMMEDIATELY — wrong SSN means IRS can't match contributions |
| Address | Current address | Contact custodian; not urgent unless multiple discrepancies |
| Account number | Custodian online portal | Verify it matches the HSA you expected to receive a 5498-SA for |

---

## Box 1 — Employee or Self-Employed Person's Archer MSA Contributions

**What it reports:** Regular contributions made by the employee or self-employed person to an Archer Medical Savings Account in the calendar year and through April 15 of the next year for that year, gross of any excess contributions even if withdrawn (2025 Instructions for Forms 1099-SA and 5498-SA, Box 1).

**Account types:** Archer MSA only.

**For HSA holders:** Box 1 is blank or $0. Do not confuse with Box 2.

**Legal basis:** IRC §220(h) requires Archer MSA trustees to file Form 5498-SA for Archer MSAs.

**Why it exists separately:** Archer MSAs and HSAs have different contribution rules and different downstream forms (Form 8853 vs. Form 8889). Separating Box 1 from Box 2 lets the IRS route reconciliation to the correct form.

**Note:** Archer MSAs have been closed to new enrollees since 2007 (under the Tax Relief and Health Care Act of 2006). Most filers in 2026 do not have an Archer MSA.

---

## Box 2 — Total Contributions Made in Current Year

**What it reports:** Total contributions to the HSA or Archer MSA made during the calendar year — i.e., contributions received by the custodian between January 1 and December 31 of the year on the form, whatever tax year they were designated for. Reporting MA MSA contributions made by the Secretary of HHS is optional for the custodian (2025 Instructions for Forms 1099-SA and 5498-SA, Box 2).

**Includes:**

- Direct contributions (check, ACH, wire) by the account holder
- Cafeteria plan / Section 125 contributions routed through payroll
- Employer-only contributions (those the employer makes without payroll withholding)
- Contributions made on the account holder's behalf by a family member
- Qualified HSA funding distribution from an IRA (one-time, lifetime; the instructions put it in Box 2)
- Contributions made in this year **for the prior year** (January 1–April 15); the prior year's form also shows them in its Box 3

**Excludes:**

- Rollovers from another HSA or an Archer MSA (those go in Box 4)
- Earnings inside the HSA (capital gains, dividends, interest)
- Excess employer contributions (and earnings) withdrawn by the employer under Notice 2008-59 Q&A-24
- Repayments of mistaken distributions

**Timing rule:** Box 2 covers contributions **received by the custodian during the calendar year**. A contribution mailed December 28 but received January 3 lands on the **next year's** Box 2, not the current year's.

**Reconciliation against Form 8889:**

```
Form 8889 Line 2 + Line 9 + Line 10
  = this year's Box 2 − last year's Box 3 + this year's Box 3
```

If they don't match, see [reconciliation.md](./reconciliation.md).

**Common pitfall:** Treating Box 2 as the Form 8889 Line 2 number directly. Box 2 includes employer/cafeteria contributions that already came out pre-tax on the W-2, IRA funding distributions, and contributions for the prior year. Apply the Box 3 adjustments, then subtract W-2 Box 12 code W and any Line 10 amount to get the direct portion.

---

## Box 3 — Total HSA or Archer MSA Contributions Made in the Following Year for This Year

**What it reports:** Contributions made between January 1 and April 15 (the unextended due date; an extension does not extend it) of the year **after** the year on the form, designated by the account holder for the year on the form (2025 Instructions for Forms 1099-SA and 5498-SA, Box 3; IRC §223(d)(4)(B) applying §219(f)(3)).

**Example:** Tax year 2025. You contribute $1,500 to your HSA on March 15, 2026, telling the custodian "this is for tax year 2025." That $1,500 lands on:

- The **2025** Form 5498-SA, Box 3 (furnished by June 1, 2026)
- The **2026** Form 5498-SA, Box 2 (money received in 2026)
- Your **2025** Form 8889, Line 2 (filed in April 2026)

**Why this is confusing:** When you reconcile your 2026 Form 8889 next year, the 2026 Box 2 includes this $1,500 even though it belongs to 2025. Subtract the 2025 form's Box 3.

**Designation rules:**

- The account holder must tell the custodian a contribution is for the prior year; the instructions tell the custodian to obtain that designation for contributions made January 1–April 15
- Without a designation, custodians treat the contribution as current-year
- Designation must happen by April 15 of the year after the tax year

**Reconciliation:**

```
Form 8889 Line 2 = (this year's Box 2 − last year's Box 3 + this year's Box 3)
                 − W-2 Box 12 code W (Line 9) − Line 10
```

For most filers both Box 3 amounts are $0 and the formula collapses to Box 2 − code W.

---

## Box 4 — Rollover Contributions

**What it reports:** Rollovers received by this HSA from another HSA or an Archer MSA (2025 Instructions for Forms 1099-SA and 5498-SA, Box 4 and "Rollovers").

**Includes:**

- HSA-to-HSA rollovers (where money flows out of one HSA, through the account holder, and into another HSA — must be redeposited within 60 days)
- Archer MSA-to-HSA rollovers

Not here: IRA-to-HSA qualified funding distributions go in Box 2.

**Excludes:**

- Custodian-to-custodian transfers (these are not rollovers in the legal sense; they don't appear in Box 4 and aren't subject to the one-rollover-per-12-months rule)
- New direct contributions (those go in Box 2)

**Limit:** Under IRC §223(f)(5), an HSA can receive only **one rollover contribution in a 1-year period** (not by calendar year). Custodian-to-custodian transfers don't count.

**Tax treatment:** Rollovers are **not deductible** — they are tax-free transfers. Box 4 amounts are not entered on Form 8889 Line 2 and do not increase Line 13.

**Common pitfall:** Some custodians lump everything into Box 2 and leave Box 4 blank, even when a rollover occurred. If you executed a rollover but don't see it in Box 4, contact the custodian to verify the categorization.

---

## Box 5 — Fair Market Value of HSA, Archer MSA, or Medicare Advantage MSA

**What it reports:** Total balance in the account on December 31 of the tax year, including:

- Cash
- Mutual fund holdings (at year-end NAV)
- ETF holdings (at year-end closing price)
- Money market positions
- Any other invested assets at year-end market value

**What it does NOT do:**

- Box 5 does not flow to any line on Form 8889
- Box 5 is not used to compute the HSA deduction
- Box 5 is not used to compute distributions

**Why it matters:**

1. **The IRS receives Box 5 every year.** If Box 5 grows by more than (Box 2 + Box 4 + plausible market growth − distributions), look for an unrecorded contribution or a custodian error before anyone else does.
2. **Estate planning and net-worth tracking** — Box 5 is the canonical year-end balance for the HSA.
3. **Mortgage and loan applications** — underwriters accept 5498-SA Box 5 as proof of HSA assets.
4. **Long-horizon planning** — for filers who treat the HSA as a stealth retirement account, Box 5 tracks compound growth over decades.

**Reconciliation:**

Box 5 should match the user's December custodian statement (the year-end statement, typically issued in January). If it differs by more than rounding, contact the custodian.

---

## Box 6 — Type of Account

**What it reports:** Check-box indicating the account type:

- **HSA** — Health Savings Account (IRC §223)
- **Archer MSA** — Archer Medical Savings Account (IRC §220, closed to new enrollees since 2007)
- **Medicare Advantage MSA** — for Medicare beneficiaries enrolled in MA MSA plans (IRC §138)

**Verification:** The box checked should match what the user expected. If a Medicare Advantage MSA box is checked but the user thought they had an HSA, that's a critical custodian error — contact them immediately. The downstream forms differ:

| Box 6 says | Account holder files |
|------------|----------------------|
| HSA | Form 8889 |
| Archer MSA | Form 8853 (Section A) |
| Medicare Advantage MSA | Form 8853 (Section B) |

If the user has both an HSA and an Archer MSA, they receive separate 5498-SAs and file both Form 8889 and Form 8853.

---

## A note on CORRECTED 5498-SAs

If the custodian discovers an error after issuing the original 5498-SA, they issue a **CORRECTED** 5498-SA with the "CORRECTED" box at the top checked. The corrected form **supersedes** the original. Treat it as the authoritative version for reconciliation.

If the user receives both an original and a corrected form for the same tax year, file both with their tax records but reconcile only against the corrected version.
