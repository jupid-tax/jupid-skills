# Form 5498-SA — Box-by-Box Reference

Detailed reference for every box on Form 5498-SA. Load this when the user has a question about a specific box.

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

**What it reports:** Contributions made by the account holder (or, for a self-employed person's Archer MSA, by themselves) to an Archer Medical Savings Account during the calendar year.

**Account types:** Archer MSA only.

**For HSA holders:** Box 1 is blank or $0. Do not confuse with Box 2.

**Legal basis:** IRC §220(h) requires Archer MSA trustees to file Form 5498-SA for Archer MSAs.

**Why it exists separately:** Archer MSAs and HSAs have different contribution rules and different downstream forms (Form 8853 vs. Form 8889). Separating Box 1 from Box 2 lets the IRS route reconciliation to the correct form.

**Note:** Archer MSAs have been closed to new enrollees since 2007 (under the Tax Relief and Health Care Act of 2006). Most filers in 2026 do not have an Archer MSA.

---

## Box 2 — Total Contributions Made in Current Year

**What it reports:** Total contributions to the HSA, Archer MSA, or Medicare Advantage MSA during the calendar year — i.e., contributions received by the custodian between January 1 and December 31 of the tax year on the form.

**Includes:**

- Direct contributions (check, ACH, wire) by the account holder
- Cafeteria plan / Section 125 contributions routed through payroll
- Employer-only contributions (those the employer makes without payroll withholding)
- Contributions made on the account holder's behalf by a family member
- Qualified HSA funding distribution from an IRA (one-time, lifetime; some custodians flag this in Box 4 instead — verify with the custodian)

**Excludes:**

- Rollovers from another HSA (those go in Box 4)
- Earnings inside the HSA (capital gains, dividends, interest)
- Prior-year-designated contributions made between January 1 and April 15 (those go in Box 3 of the **next year's** 5498-SA)

**Timing rule:** Box 2 covers contributions **received by the custodian during the calendar year**. A contribution mailed December 28 but cleared January 3 lands on the **next year's** Box 2, not the current year's.

**Reconciliation against Form 8889:**

```
Box 2 = Form 8889 Line 2 (direct) + Form 8889 Line 9 (employer + cafeteria)
```

If they don't match, see [reconciliation.md](./reconciliation.md).

**Common pitfall:** Treating Box 2 as the Form 8889 Line 2 number directly. Box 2 includes employer/cafeteria contributions that already came out pre-tax on the W-2. Subtract W-2 Box 12 code W to get the direct portion.

---

## Box 3 — Total HSA or Archer MSA Contributions Made in Following Year for Current Year

**What it reports:** Contributions made between January 1 and April 15 (or the extended tax filing deadline) of the year **after** the tax year on the form, designated by the account holder as prior-year contributions.

**Example:** Tax year 2025. You contribute $1,500 to your HSA on March 15, 2026, telling Fidelity "this is for tax year 2025." That $1,500 lands on:

- The **2026** Form 5498-SA, Box 3 (issued in May 2027)
- Your **2025** Form 8889, Line 2 (filed in April 2026)

**Why this is confusing:** When you reconcile your 2025 Form 8889 against your 2025 Form 5498-SA, the prior-year contribution **is not on the 2025 form**. You need to also pull the 2026 Form 5498-SA to see it.

**Designation rules:**

- The account holder must explicitly tell the custodian a contribution is for the prior year (online form, paper form, or phone call)
- Default is current-year if no designation is made
- Once designated, the custodian usually cannot recharacterize without a documented exception
- Designation must happen by April 15 of the year after the tax year (or the extended deadline if the holder filed for an extension)

**Reconciliation:**

```
Form 8889 Line 2 = (current year's 5498-SA Box 2 contributions made by account holder − employer/cafeteria portion)
                 + (next year's 5498-SA Box 3, if applicable)
                 − (prior year's 5498-SA Box 3, if you previously designated a prior-year contribution that's now on this year's Form 8889)
```

In practice, only the first two lines apply to most filers.

---

## Box 4 — Rollover Contributions

**What it reports:** Rollovers received by this HSA from another HSA, Archer MSA, or (in a one-time qualified HSA funding distribution) from an IRA.

**Includes:**

- HSA-to-HSA rollovers (where money flows out of one HSA, through the account holder, and into another HSA — must be redeposited within 60 days)
- IRA-to-HSA qualified funding distributions (one-time, lifetime, capped at the annual HSA contribution limit)

**Excludes:**

- Custodian-to-custodian transfers (these are not rollovers in the legal sense; they don't appear in Box 4 and aren't subject to the one-rollover-per-12-months rule)
- New direct contributions (those go in Box 2)

**Limit:** Under IRC §223(f)(5), a taxpayer may roll over an HSA only **once per 12-month period** (counted from the date of the prior rollover, not by calendar year). Custodian-to-custodian transfers don't count.

**Tax treatment:** Rollovers are **not deductible** — they are tax-free transfers. Box 4 amounts do not increase Form 8889 Line 13. They do, however, count against the testing period if a qualified HSA funding distribution from an IRA is involved.

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

1. **IRS uses Box 5 trends** to flag potential excess contributions and untracked rollovers. If Box 5 grows by more than (Box 2 + Box 4 + plausible market growth), the IRS may issue a query asking what happened.
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
| Medicare Advantage MSA | Form 8853 (Section C) |

If the user has both an HSA and an Archer MSA, they receive separate 5498-SAs and file both Form 8889 and Form 8853.

---

## A note on CORRECTED 5498-SAs

If the custodian discovers an error after issuing the original 5498-SA, they issue a **CORRECTED** 5498-SA with the "CORRECTED" box at the top checked. The corrected form **supersedes** the original. Treat it as the authoritative version for reconciliation.

If the user receives both an original and a corrected form for the same tax year, file both with their tax records but reconcile only against the corrected version.
