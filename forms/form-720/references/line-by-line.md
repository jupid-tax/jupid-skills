# Form 720 Line-by-Line Reference

Complete walkthrough of every section on Form 720 (Quarterly Federal Excise Tax Return).

Form 720 has a header, three numbered Parts, and three Schedules (A, C, T). Most filers use only a handful of lines.

---

## Header

| Field | What goes here | Notes |
|-------|----------------|-------|
| Quarter ending | MM/DD/YYYY (last day of quarter) | Q1=Mar 31, Q2=Jun 30, Q3=Sep 30, Q4=Dec 31 |
| Name | Legal name of business | Match IRS records exactly |
| Trade name (if any) | DBA | Optional |
| Address | Street, room/suite | |
| City, State, ZIP | | |
| Final return checkbox | Check only if this is the LAST Form 720 | |
| Address change checkbox | Check if address changed since last filing | |
| Employer ID Number (EIN) | 9 digits | Required |

---

## Part I — Excise taxes paid by the filer

Part I lists categories of excise tax sorted by IRS Number. Each line has columns:

- (a) IRS No. — preprinted on the form
- (b) Type of tax (description) — preprinted
- (c) Tax — the amount the filer computed

**Filers enter amounts only on lines that apply.** Most filers leave 90% of Part I blank.

### Common Part I categories (not exhaustive)

| IRS No. | Category | Tax base | Rate (verify each year) | IRC § |
|---------|----------|----------|-------------------------|-------|
| 14 | Communications tax (local telephone) | Amount paid | 3% | §4251 |
| 22 | Air transportation of persons (domestic) | Amount paid | 7.5% + segment fee ($5.20 in 2025; verify) | §4261 |
| 26 | Air transportation of property | Amount paid | 6.25% | §4271 |
| 27 | International air travel facilities (departure) | Per passenger | $22.20 (2025) | §4261(c) |
| 28 | Use of international air travel facilities (arrival/departure within Hawaii/Alaska) | Per passenger | $11.10 (2025) | §4261(c) |
| 29 | Transportation by water | Per passenger | $5.00 | §4471 |
| 41 | Sport fishing equipment | Sales price | 10% | §4161(a) |
| 42 | Fishing tackle boxes | Sales price | 3% | §4161(a) |
| 44 | Bows of draw weight ≥ 30 lbs | Sales price | 11% | §4161(b)(1) |
| 106 | Arrows | Sales price | 11% / per arrow shaft $0.59 (verify) | §4161(b)(2) |
| 51 | LUST tax (Leaking Underground Storage Tank) | Per gallon fuel | $0.001 | §4081(a)(2)(B) |
| 60 | Diesel fuel — sold but not exempt | Per gallon | $0.244 | §4081(a) |
| 62 | Gasoline — sold but not exempt | Per gallon | $0.184 | §4081(a) |
| 64 | Inland waterways fuel use tax | Per gallon | $0.29 + LUST $0.001 (verify) | §4042 |
| 79 | Diesel/Kerosene at terminal rack | Per gallon | $0.244 | §4081 |
| 104 | Foreign insurance — casualty/indemnity | Premium | 4% | §4371(1) |
| 105 | Foreign insurance — life/sickness/accident | Premium | 1% | §4371(2) |
| 107 | Foreign reinsurance | Premium | 1% | §4371(3) |
| 117 | Coal — underground mined | Per ton | varies (verify Pub. 510) | §4121 |
| 118 | Coal — surface mined | Per ton | varies | §4121 |
| 121 | Vaccines | Per dose | $0.75 per disease | §4131 |
| 125 | Ozone-depleting chemicals (ODC) | Per pound | varies by chemical | §4681 |
| 140 | Indoor tanning services | Amount paid | 10% (verify status — subject to repeal proposals) | §5000B |

The full list has 100+ entries. Load `references/irs-number-catalog.md` for the complete table.

---

## Part II — Other excise taxes

Part II covers categories that don't fit cleanly in Part I, including patient-centered fees, special fuel taxes, and surtaxes.

| IRS No. | Category | Notes |
|---------|----------|-------|
| 19 | Tobacco products | Per category (cigarettes, cigars, etc.) |
| 30 | Inland waterways fuel | Per gallon |
| 64 | Inland waterways fuel use tax | (same as above; some filers use Part II) |
| 91 | Bow strings | per IRS Number list |
| 102 | Sport fishing equipment imported | Sales price |
| 108 | Foreign insurance — premium taxes | |
| 133 | **PCORI fee** | **Annual, on Q2 form**. $3.22/covered life for plan years ending Oct 1 2024 – Sep 30 2025 (Notice 2024-83); verify successor notice. |
| 150 | Section 4181 firearms tax (handled on Form 11; NOT 720) | NOT a Form 720 item — illustrative |

PCORI (IRS No. 133) is the most common Part II line for small businesses.

---

## Part III — Totals and balance due

The math summary.

| Line | Field | Computation |
|------|-------|-------------|
| 1 | Total tax — Part I | Sum of all Part I (c) column entries |
| 2 | Total tax — Part II | Sum of all Part II (c) column entries |
| 3 | Total tax | Line 1 + Line 2 |
| 4 | Claims (from Schedule C) | Sum of Schedule C credits |
| 5 | Net tax | Line 3 − Line 4 |
| 6 | Total deposits for the quarter | EFTPS deposits made during the quarter |
| 7 | Overpayment from prior quarter | Carried from prior Form 720 Line 11, if any |
| 8 | Add Lines 6 and 7 | |
| 9 | Balance due | Line 5 − Line 8 (if positive) |
| 10 | Overpayment | Line 8 − Line 5 (if positive) — applied to next quarter or refunded |

The agent computes each line precisely and surfaces both Line 9 and Line 10 (only one will be > 0).

---

## Schedule A — Excise tax liability for semi-monthly periods

Required for filers with **regular method** liability under §6011(a) — primarily fuel, alcohol, and tobacco categories.

Schedule A reports liability **incurred** during each semi-monthly period:

| Period | Date range |
|--------|-----------|
| 1 | Day 1 – 15 of first month of quarter |
| 2 | Day 16 – end of first month |
| 3 | Day 1 – 15 of second month |
| 4 | Day 16 – end of second month |
| 5 | Day 1 – 15 of third month |
| 6 | Day 16 – end of third month |

Each period has columns for IRS Number and amount of liability. Sum across periods must match the corresponding Part I/II line.

**Why it matters**: the IRS uses Schedule A to verify deposit timing. Deposits are due 14 days after the end of each semi-monthly period for filers required to deposit. A liability incurred in period 1 with no deposit by day 29 of that month = §6656 penalty (2%–15% by lateness).

**PCORI does NOT use Schedule A.** PCORI-only filers leave Schedule A blank.

---

## Schedule C — Claims (refunds and credits)

Schedule C is for refundable claims that reduce total tax (Part III Line 4). Common claims:

| CRN | Type of claim | Underlying |
|-----|---------------|-----------|
| 360 | Nontaxable use of gasoline | §6421 |
| 362 | Nontaxable use of aviation gasoline | §6421 |
| 346 | Nontaxable use of diesel fuel | §6427 |
| 347 | Nontaxable use of kerosene | §6427 |
| 365 | Diesel fuel used in trains | §6427 |
| 309 | Biodiesel mixture credit | §6426 |
| 310 | Renewable diesel mixture credit | §6426 |
| 415 | Sustainable aviation fuel (SAF) credit | §6426 (verify; new under IRA) |
| 396 | Alternative fuel credit | §6426 |
| 397 | Alternative fuel mixture credit | §6426 |
| 365 | Form 2290 HVUT credit (sold/destroyed/stolen vehicle) | §4481 prorated |

**CRN** = Claim Reference Number, a 3-digit code that identifies the claim type. Each claim row needs the CRN, a description, the period, and the amount.

For HVUT credits specifically: when a tractor-trailer subject to Form 2290 is sold, destroyed, or stolen mid-year, the prorated HVUT for the remaining months is refundable. The user files Form 8849 Schedule 6 OR claims on Form 720 Schedule C with CRN 365 (verify the CRN against current Form 720 instructions).

For alternative fuel credits, the filer must hold a current Form 637 registration in the relevant activity letter (M for alternative fuel mixture, AL for alternative fueler, etc.). Without registration, the credit is denied.

---

## Schedule T — Two-party exchanges (terminal operators)

Schedule T applies only to licensed terminal operators in the position-holder distribution chain for fuels. Most Form 720 filers are not terminal operators.

If applicable, Schedule T reports the volume of fuel exchanged in two-party transactions, used to coordinate liability between position holders. The agent should not attempt Schedule T without confirming the user is a registered terminal operator (TR position on Form 637).

---

## Signature block

- Signature of officer / authorized person
- Title
- Date
- Phone number
- Print name
- Paid preparer's section (if applicable)

For e-file, signature is via Form 8453-EX upload OR ERO PIN OR Self-Select PIN, depending on the provider.

---

## Filing schedule

| Quarter | Period covered | Due date |
|---------|----------------|----------|
| Q1 | January – March | April 30 |
| Q2 | April – June | July 31 (also PCORI annual) |
| Q3 | July – September | October 31 |
| Q4 | October – December | January 31 (next year) |

When a due date falls on a Saturday, Sunday, or DC/federal holiday, the deadline shifts to the next business day per IRC §7503.

---

## Special timing rules

1. **PCORI fee**: filed once per year on the Q2 Form 720 (due July 31). Even if the plan year ends in Q1 or Q4, the filing is on the Q2 form for the year the plan-year ended. Plan year ending Oct 1, 2024 – Sep 30, 2025 → file by July 31, 2026.

2. **No-tax-due quarters**: a filer who has filed Form 720 in the past but has no excise liability for the current quarter generally still files a Form 720 marked "no tax due" — UNLESS they file a "Final return" once and stop. Check the prior-year final-return checkbox.

3. **Final return**: when the filer ceases the activity giving rise to the excise tax, they file one last Form 720 with the "Final return" box checked. After that, no quarterly filings are required for that EIN.

4. **Combined returns**: a single Form 720 covers all categories for the same EIN. A filer with both PCORI fee and sport fishing manufacturer's tax files ONE Form 720 with both lines completed.

5. **Successor businesses**: when the filer's business is acquired or merged, the new entity files under its own EIN; the prior entity files a final return.
