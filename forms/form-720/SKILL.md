---
name: form-720
description: >
  Use this skill when a business needs to file IRS Form 720, the Quarterly
  Federal Excise Tax Return. Triggers on phrases like "Form 720", "PCORI fee",
  "federal excise tax return", "quarterly excise tax", "sport fishing
  manufacturer tax", "arrow shaft tax", "self-insured health plan fee",
  "indoor tanning tax", "remittance transfer tax", "ozone-depleting chemicals
  tax", "Schedule A excise", "Schedule C excise". Do NOT use for: state excise
  tax (state DOR forms); state sales/use tax; Heavy Highway Vehicle Use Tax or
  HVUT credits for sold, destroyed, or stolen vehicles (use the form-2290
  skill; refunds go on Form 8849 Schedule 6); alcohol, tobacco, or firearms
  excise (TTB forms); wagering taxes (Forms 730 and 11-C); ACA employer
  reporting (Forms 1094-C / 1095-C).
form: Form 720 (Quarterly Federal Excise Tax Return)
audience: [scorp, ccorp, partnership, llcm, llc1]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f720.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i720.pdf
---

# Form 720 — Quarterly Federal Excise Tax Return

This skill produces an audit-grade draft of Form 720 covering the federal excise taxes a business is liable for in a given quarter. Most filers only owe one or two specific taxes (the PCORI fee for self-insured health plans being the most common), so the skill spends most of its time on the handful of common categories and provides pointers for the rest.

The math is per-line mechanical. The judgment is in **identifying which IRS Nos. (about 60 preprinted tax lines in Parts I and II) apply to the filer's business**, **whether the tax sits in Part I (Schedule A and semimonthly deposits) or Part II (paid with the return)**, and **distinguishing Form 720 obligations from adjacent forms (Form 2290, Form 8849, Form 4136, TTB forms, state excise)**. When liability is unclear, the agent must ASK rather than guess. Omitting an excise tax produces compounding penalties under §6651 and §6656.

**Revision verified:** the line map in this skill was verified on 2026-10-06 against Form 720 (Rev. June 2026) and the Instructions for Form 720 (Rev. June 2026), the revisions posted on irs.gov on that date. Form 720 is not annual: before using this skill for a later quarter, check https://www.irs.gov/forms-pubs/about-form-720 for a newer revision and re-check every IRS No., rate, and CRN.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 720, "quarterly excise tax", "Schedule A excise", "Schedule C excise"
- The user has a **self-insured group health plan or HRA** and asks about the **PCORI fee** (patient-centered outcomes research fee under IRC §4375/§4376, IRS No. 133)
- The user manufactures, produces, or imports **sport fishing equipment, fishing rods and poles, electric outboard motors, fishing tackle boxes, bows, quivers, broadheads, points, or arrow shafts** (IRC §4161; IRS Nos. 41, 110, 42, 114, 44, 106)
- The user operates **indoor tanning services** (IRC §5000B; IRS No. 140, still on the Rev. June 2026 form)
- The user has **fuel tax** liability as a position holder, enterer, blender, or retailer of alternative fuel (IRC §4081, §4041; IRS Nos. 60, 62, 35, 69, 77, 79, 112–124) or wants a Schedule C claim alongside a Part I or II liability
- The user makes or imports **ozone-depleting chemicals (ODCs)**, taxable chemicals, or petroleum subject to Superfund taxes (Form 6627; IRS Nos. 98, 19, 20, 54, 17, 53, 16)
- The user **pays premiums to a foreign insurer** for coverage of U.S. risks (IRC §4371; IRS No. 30)
- The user is a **remittance transfer provider** collecting the 1% tax on cash-funded remittances after 2025 (IRC §4475; IRS No. 155)
- The user operates **passenger ships**, collects **air transportation** or **local telephone** taxes, sells **heavy trucks, trailers, or tractors** at retail, or makes **taxable tires, coal, vaccines**, or imports a **gas guzzler** (IRS Nos. 29, 26, 27, 28, 22, 33, 108/109/113, 36–39, 97, 40)

Do **not** engage this skill when:

- The user owes **state** excise tax (different forms; varies by state: gasoline tax, alcohol tax, tobacco tax at state level)
- The user owes **Heavy Highway Vehicle Use Tax** for vehicles with taxable gross weight of 55,000 pounds or more, or wants a **credit or refund of HVUT** for a vehicle sold, destroyed, or stolen → use the [`form-2290`](../form-2290/SKILL.md) skill. HVUT credits go on the next Form 2290 (line 5) or on Form 8849 Schedule 6, never on Form 720 Schedule C (Instructions for Form 2290, Rev. July 2026, "Line 5")
- The user only wants a **refund of fuel tax** with no Form 720 liability to report → Form 8849 or Form 4136 (Form 720 Schedule C may be used only if the filer reports a liability in Part I or II; i720 "Schedule C. Claims")
- The user owes **alcohol, tobacco, or firearms** excise → TTB forms, not Form 720
- The user is filing **occupational tax on wagering** → use Form 11-C
- The user is filing **wagering excise** → use Form 730
- The user is reporting the **ACA employer mandate** (1094-C / 1095-C), which is not Form 720
- The user is a small business asking about general sales tax: sales tax is state, not federal

If the user is unsure which excise taxes apply to their industry, the agent walks the IRS Number list (see `references/irs-number-catalog.md`) and asks targeted yes/no questions.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Filing entity name and EIN.** Form 720 requires an EIN. The only exception is a one-time gas guzzler filing (IRS No. 40) by an individual, who may enter an SSN or ITIN (i720 "Gas guzzler tax (IRS No. 40)", step 3). Single-owner disregarded entities and QSubs file under their own EIN, not the owner's (i720 "Disregarded entities and qualified subchapter S subsidiaries").
2. **Quarter being filed.** Form 720 is quarterly (i720 "When To File"; a due date on a weekend or legal holiday moves to the next business day):
   - Q1 = Jan, Feb, Mar; due **April 30**
   - Q2 = Apr, May, Jun; due **July 31**
   - Q3 = Jul, Aug, Sep; due **October 31**
   - Q4 = Oct, Nov, Dec; due **January 31** (next year)
   - **PCORI fee is annual on the Q2 form, due July 31.**
3. **Business address** — street, city, state, ZIP. Used in the Form 720 header.
4. **Final return flag** — is this the last Form 720 the entity will file? (Triggers a "Final return" checkbox.)
5. **Address change flag** — has the address changed since the last filing?
6. **Excise tax categories** — which IRS Nos. apply? See `references/irs-number-catalog.md`. Common ones:
   - **133** — PCORI fee (Part II; annual, on the Q2 form)
   - **41 / 110 / 42 / 114** — Sport fishing equipment, fishing rods and poles, electric outboard motors, tackle boxes (Part II)
   - **44 / 106** — Bows, quivers, broadheads, and points; arrow shafts (Part II)
   - **140** — Indoor tanning services (Part II)
   - **30** — Policies issued by foreign insurers (Part I)
   - **98 / 19 / 20** — Ozone-depleting chemicals, ODC imported products, ODC floor stocks (Form 6627)
   - **60 / 62 / 35** — Diesel, gasoline, kerosene (Part I)
   - **33** — Retail tax on heavy trucks, trailers, and tractors (Part I)
   - **155** — Remittance transfers (Part I)
7. **For PCORI specifically** — the agent needs:
   - Plan year ending date (determines the applicable rate row on line 133)
   - Average number of covered lives during the plan year
   - Counting method. Self-insured plan sponsors: actual count, snapshot, or Form 5500 method (Treas. Reg. §46.4376-1(c)(2)). Insurers: actual count, snapshot, member months, or state form method (i720 "Specified health insurance policies")
8. **For fuel taxes** — the agent needs gallons by IRS No. and event (removal at the terminal rack or another taxable event), and for Schedule C claims the type of use and CRN.
9. **For sport fishing / archery** — the agent needs the sale price of each article (or constructive sale price for related-party sales, §4216(b)), the category, and for rods and poles the per-article price (the tax is capped at $10 per rod or pole, §4161(a)(1)(B)); for arrow shafts, the shaft count.
10. **Prior overpayments** applied from the previous Form 720 (Part III line 6) and any Form 720-X amount included in it (line 7).

For first-time filers, ask whether the entity has previously filed Form 720; if not, an EIN is required and a registration may be needed for fuel activities, tax-free sales, and ultimate vendor claims (Form 637, Application for Registration; i720 "Information for Claims on Lines 7–11").

---

## Workflow

Execute these steps in order.

### Step 1 — Confirm Form 720 is the right form

Walk through the anti-trigger list. If the user describes:
- Heavy highway vehicle use, or an HVUT credit for a sold, destroyed, or stolen vehicle → Form 2290 / Form 8849 Schedule 6 ([`form-2290`](../form-2290/SKILL.md))
- Alcohol, tobacco, firearms → TTB
- Wagering / gambling business → Form 11-C / 730
- State excise → state DOR
- ACA reporting → Forms 1094-C / 1095-C
- Sales tax → state DOR

…redirect.

### Step 2 — Identify applicable IRS Numbers

Open `references/irs-number-catalog.md`. Walk the categories with the user. Most filers only have 1–2 IRS Numbers. The most common pattern is a single PCORI-fee filing on the Q2 form.

The IRS No. is a 2- or 3-digit code preprinted in the left column of Parts I and II of Form 720 (and repeated in the right column). Each tax line corresponds to one IRS No.; some lines have sub-rows, such as 60(a)–(c) for diesel and 133(a)–(d) for PCORI rate bands. Record for each applicable IRS No. whether it sits in Part I or Part II: that decides Schedule A and deposits (Steps 4 and 8).

### Step 3 — Compute the tax for each applicable IRS Number

Use `references/line-by-line.md` for the canonical computation per category. Common patterns:

- **PCORI (133)**: `average covered lives × applicable rate`, entered on the row for the plan year's end date. Plan years ending Oct 1, 2024 – Sep 30, 2025: **$3.47** (Notice 2024-83; rows 133(a) and 133(c)). Plan years ending Oct 1, 2025 – Sep 30, 2026: **$3.84** (Notice 2025-61; rows 133(b) and 133(d)). The fee ends for plan years ending after Sep 30, 2029 (§4375(e), §4376(e)).
- **Sport fishing equipment (41)**: 10% of sale price, §4161(a)(1)(A). **Fishing rods and poles (110)**: 10% capped at $10 per article, §4161(a)(1)(B). **Electric outboard motors (42)** and **fishing tackle boxes (114)**: 3%, §4161(a)(2)–(3).
- **Bows, quivers, broadheads, and points (44)**: 11% of sale price, bows with a peak draw weight of 30 pounds or more, §4161(b)(1). **Arrow shafts (106)**: per shaft, inflation-adjusted: $0.63 for 2025 (Rev. Proc. 2024-40 §2.44), $0.65 for 2026 (Rev. Proc. 2025-32 §4.43).
- **Indoor tanning (140)**: 10% of the amount paid, collected by the provider, §5000B.
- **Fuel taxes (60, 62, 35, etc.)**: taxable gallons × the rate printed on Form 720 (e.g., diesel $.244, gasoline $.184). Alternative fuels use gasoline or diesel gallon equivalents (i720 "Alternative fuel").
- **Remittance transfers (155)**: 1% of cash-funded remittance transfers made after Dec 31, 2025, collected by the provider, §4475.

### Step 4 — Complete Schedule A (Part I liability per semimonthly period)

Schedule A records the net tax liability for **Part I taxes only**, by semimonthly period (boxes A–F, plus G for the special September rule; boxes M–S for communications and air transportation taxes under the alternative method). Complete it whenever Part I shows a liability, even if the net liability is under $2,500. Do not complete it for Part II taxes or for a one-time gas guzzler filing (Form 720 Schedule A note; i720 "Schedule A. Excise Tax Liability").

PCORI, sport fishing, archery, and indoor tanning are Part II taxes: no Schedule A.

### Step 5 — Complete Schedule C (claims) only if a Part I or II liability is reported

Schedule C (lines 1–15) claims credits for fuel used or sold for nontaxable uses, ultimate vendor and credit card issuer claims, exported fuel, tire credits, and certain manufacturers tax credits. The total goes to Part III line 4. Rules:
- Use Schedule C only if the filer reports a liability in Part I or II; otherwise use Form 8849 or Form 4136 (i720 "Schedule C. Claims").
- Lines 12 and 13 are "Reserved for future use": the biodiesel/renewable diesel mixture credit and the alternative fuel and alternative fuel mixture credits expired for fuel sold or used after Dec 31, 2024, and OBBBA ended the SAF mixture credit after Sep 30, 2025 (Pub. 510, Rev. Dec. 2025, "What's New" and "Reminders").
- There is no HVUT line on Schedule C. HVUT credits belong on Form 2290 line 5 or Form 8849 Schedule 6.
- Claims on lines 1–6 and 14b–14d must total at least $750 for the quarter (or aggregate quarters of the income tax year); otherwise they become annual claims on Form 4136 (i720 "Claim requirements for lines 1–6 and lines 14b–14d").

### Step 6 — Complete Schedule T (two-party exchanges) only for taxable fuel registrants

Schedule T reports gallons of diesel, kerosene, gasoline, and aviation gasoline received or delivered in a two-party exchange within a terminal, where both parties are taxable fuel registrants and the receiving person is liable for the rack removal tax (i720 "Schedule T. Two-Party Exchange Information Reporting"). Most Form 720 filers leave it blank.

### Step 7 — Compute Part III

```
Line 3  = Part I line 1 + Part II line 2            (total tax)
Line 4  = Schedule C line 15                        (claims)
Line 5  = deposits made for the quarter (check the box if the safe harbor rule was used)
Line 6  = overpayment from previous quarters (prior Form 720 line 11 applied + Form 720-X line 5b)
Line 7  = the Form 720-X amount included on line 6, if any
Line 8  = line 5 + line 6
Line 9  = line 4 + line 8
Line 10 = line 3 − line 9 if line 3 > line 9       (balance due; not payable if under $1.00)
Line 11a = line 9 − line 3 if line 9 > line 3      (overpayment; 11b apply to next return or refund; 11c–11e direct deposit)
```

Source: Form 720 (Rev. June 2026) page 3; i720 "Part III".

### Step 8 — Verify deposit requirements

Semimonthly deposits by electronic funds transfer are generally required. No deposit is required, and the tax is paid with the return, when (i720 "Payment of Taxes"):
- the net liability for **Part I** taxes for the quarter does not exceed $2,500;
- the tax is the gas guzzler tax on a one-time filing;
- the tax is the PCORI fee on the Q2 return;
- the tax is a **Part II** tax other than the ODC floor stocks tax.

Regular method deposits are due by the 14th day after each semimonthly period (generally the 29th for the 1st–15th, the 14th of the next month for the 16th–last day), with a special additional September deposit (in 2026, liability for Sept. 16–26 due Sept. 29). Each deposit must be at least 95% of the period's net liability unless the safe harbor (1/6 of the lookback quarter's net liability) applies. Load `references/line-by-line.md` for the full rules.

If deposits were required and not made on time, the §6656 failure-to-deposit penalty (2%, 5%, 10%, or 15%) applies in addition to any §6651 penalties. The IRS granted limited deposit penalty relief for remittance transfer tax deposits for Q1–Q3 2026 (Notice 2025-55). Surface this in the validation summary.

### Step 9 — Run validation checks

See **Validation** below.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next steps:

- **Filing channel:** e-filing Form 720 is optional; paper is still accepted (IRS Form 720 e-file FAQ). See `filing.md`.
- **Pay any balance due** (line 10) by EFTPS, IRS Direct Pay, electronic funds withdrawal when e-filing, or check or money order with Form 720-V. Deposits themselves must be made by electronic funds transfer (i720 "Electronic deposit requirement").
- **Set up calendar reminders** for the next quarterly deadline and, for Part I taxes, the semimonthly deposit dates.
- **For PCORI**: this is the only excise tax for many filers; if Form 720 is filed only for PCORI, no Q1, Q3, or Q4 return is required (i720 "How To File"). Remind the user of next year's Q2 / July 31 filing.
- **Form 637 registration** is required for some activities (tax-free sales, ultimate vendor and credit card issuer claims on Schedule C lines 7–11 and 14e). See the Form 637 instructions.

### Step 12 — File (optional)

If the agent has IRS-authorized e-file tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). Form 720 e-filing goes through an IRS-approved 720 Modernized e-File (MeF) provider; the IRS has no free direct e-file portal for Form 720. The provider list is at https://www.irs.gov/e-file-providers/720-mef-providers.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level structure of Form 720:

### Header

- Quarter ending (month and year)
- Name, address (P.O. box only if the post office does not deliver to the street address), EIN
- Final return checkbox
- Address change checkbox

### Part I — Environmental, communications and air, fuel, retail, ship passenger, other, foreign insurance, and manufacturers taxes

Each IRS No. has its own line. Selected lines (full map in `references/line-by-line.md`; rates from Form 720 Rev. June 2026 and i720):

| IRS No. | Category | Tax base | Rate |
|---------|----------|----------|------|
| 22 | Local telephone service and teletypewriter exchange service | Amount paid | 3% |
| 26 | Transportation of persons by air | Amount paid + per segment | 7.5% + $5.30 per domestic segment (2026; $5.20 in 2025) |
| 28 | Transportation of property by air | Amount paid | 6.25% |
| 27 | Use of international air travel facilities | Per person | $23.40 (2026; $22.90 in 2025); Alaska/Hawaii departures $11.70 (2026; $11.40 in 2025) |
| 60 | Diesel (a) rack removal, (b) other events, (c) biodiesel mixture | Per gallon | $.244 |
| 62 | Gasoline (a) rack removal, (b) other events | Per gallon | $.184 |
| 35 | Kerosene (a) rack removal, (b) other events | Per gallon | $.244 |
| 33 | Retail tax: truck, trailer, and semitrailer chassis and bodies, and tractor | Sale price | 12% |
| 29 | Transportation by water | Per passenger | $3 |
| 155 | Remittance transfers (after 2025) | Amount of transfer | 1% |
| 30 | Policies issued by foreign insurers | Premiums paid | 4% casualty/indemnity bonds; 1% life, sickness, accident, annuity; 1% reinsurance |
| 98 | Ozone-depleting chemicals (Form 6627) | Pounds | Form 6627 rates |

IRS Nos. 18 and 21 (oil spill liability taxes) expired after 2025; leave them blank unless Congress extends them (i720 "What's New").

### Part II — PCOR fee, sport fishing and archery, indoor tanning, and other taxes

| IRS No. | Category | Notes |
|---------|----------|-------|
| 133 | PCOR fee | Annual, on the Q2 form (July 31). Rows (a)/(c): $3.47 for plan years ending Oct 1, 2024 – Sep 30, 2025. Rows (b)/(d): $3.84 for plan years ending Oct 1, 2025 – Sep 30, 2026. |
| 41 / 110 / 42 / 114 | Sport fishing equipment / rods and poles / electric outboard motors / tackle boxes | 10% / 10% capped at $10 per article / 3% / 3% |
| 44 / 106 | Bows, quivers, broadheads, and points / arrow shafts | 11% / $0.65 per shaft (2026) |
| 140 | Indoor tanning services | 10% of amount paid |
| 64 / 125 | Inland waterways fuel use tax / LUST tax on inland waterways fuel use | $.29 / $.001 per gallon |
| 51 / 117 | Section 40 fuels / biodiesel sold as but not used as fuel | Recapture at the credit rate |
| 20 | ODC floor stocks tax (Form 6627) | Reported on the return due July 31 |
| 150 | Repurchase of corporate stock (Form 7208) | Form 7208 Part V line 11 |
| 142 | Sales of designated drugs during statutory periods | §5000D |

### Part III — Totals and balance due

Lines 3–11 (see Step 7): total tax, claims, deposits, overpayment carried in, balance due or overpayment.

### Schedule A — Part I net liability by semimonthly period

Regular method: boxes A–F (1st–15th and 16th–last day of each month), G for the special September rule. Alternative method (IRS Nos. 22, 26, 28, 27): boxes M–R, S.

### Schedule C — Claims

Lines 1–11 (nontaxable use of fuels and ultimate vendor sales), lines 12–13 reserved, line 14 other claims (14a §4051(d) tire credit CRN 366, 14f–14h tire credits, 14i–14k other manufacturers tax claims), line 15 total. Every claim needs the rate, gallons or count, amount, and CRN (credit reference number) printed on the form, plus the "Month your income tax year ends" and "Period of claim" entries.

### Schedule T — Two-party exchange information reporting

Gallons received and delivered in two-party exchanges within a terminal, for IRS Nos. 60(a), 35(a)/69/77/111, 62(a), and 14.

---

## Validation

Run these checks before declaring the form ready. Surface any failure — don't silently fix.

### Math checks

- [ ] Each IRS No.'s tax = base × the rate printed on the current Form 720 (or Form 6627 / 6197 / 7208 for attached-form taxes)
- [ ] Part I line 1 = sum of all Part I tax entries
- [ ] Part II line 2 = sum of all Part II tax entries
- [ ] Part III line 3 = line 1 + line 2
- [ ] Line 8 = line 5 + line 6; line 9 = line 4 + line 8
- [ ] Exactly one of line 10 (line 3 − line 9) or line 11a (line 9 − line 3) is positive
- [ ] Schedule A boxes sum to the Part I net liability for the quarter (Part II taxes are not on Schedule A)
- [ ] Schedule C line 15 = sum of lines 1–14 and equals Part III line 4; each claim uses the rate and CRN printed on the form

### Sanity checks (warn, don't block)

- [ ] PCORI amount is on the 133 row matching the plan year end ($3.47 for plan years ending Oct 1, 2024 – Sep 30, 2025; $3.84 for Oct 1, 2025 – Sep 30, 2026)
- [ ] PCORI is filed on the **Q2 form (July 31)**. If the user is filing Q1/Q3/Q4 and only PCORI applies, redirect to the Q2 form; filers with other quarterly taxes leave line 133 blank on Q1, Q3, Q4 returns.
- [ ] Fishing rods and poles are on IRS No. 110 (not 41) with the $10 per-article cap; electric outboard motors (42) and tackle boxes (114) are 3%.
- [ ] Bows with a peak draw weight under 30 pounds are not taxable under §4161(b)(1); confirm bow specs.
- [ ] Arrow shafts use the per-shaft rate for the calendar year of sale ($0.63 in 2025, $0.65 in 2026), not a percentage.
- [ ] Fuel tax rates match the rates printed on the Form 720 revision for the quarter being filed.
- [ ] Part I net liability over $2,500 for the quarter and no deposits made → surface §6656 risk.
- [ ] No entries on IRS Nos. 18 or 21 (expired after 2025) and no Schedule C lines 12–13 (reserved).
- [ ] First-time filer: confirm the EIN is active; if there is none, apply first (IRS.gov/EIN or Form SS-4).

### Cross-form checks

- [ ] No HVUT credit on Schedule C. Route HVUT credits to Form 2290 line 5 or Form 8849 Schedule 6.
- [ ] Ultimate vendor or credit card issuer claims (Schedule C lines 7–11, 14e) carry a current Form 637 registration number.
- [ ] Taxes figured on Form 6627 (IRS Nos. 16, 17, 19, 20, 53, 54, 98), Form 6197 (40), or Form 7208 (150) have the form attached.
- [ ] Inland waterways fuel (IRS No. 64, $.29) also carries the LUST tax on IRS No. 125 ($.001) when the fuel was not already subject to LUST tax (i720 "Other Part II Taxes").

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to Form 720 (paper) or paste into IRS-authorized e-file software. Format:

```markdown
# Form 720 — DRAFT for Quarter [Q1/Q2/Q3/Q4] of YYYY

## Header
Name: <legal name>
EIN: <9-digit EIN>
Address: <street, city, state, ZIP>
Quarter ending: MM/DD/YYYY
Final return: [ ] Yes  [x] No
Address change: [ ] Yes  [x] No

## Part I — Excise taxes
| IRS No. | Category | Base | Rate | Tax |
|---------|----------|------|------|-----|
| <NN>    | <name>   | $X,XXX | X% | $X,XXX |
| ...     | ...      | ...    | ... | ... |
| **Subtotal Part I** | | | | $X,XXX |

## Part II — PCOR fee and other Part II taxes
| IRS No. | Category | Base | Rate | Tax |
|---------|----------|------|------|-----|
| 133(d)  | PCOR fee, self-insured plan, plan year ending Oct 1, 2025 – Sep 30, 2026 | <avg covered lives> | $3.84 | $X,XXX.XX |
| ...     | ...       | ...              | ...    | ...    |
| **Line 2 (total Part II)** | | | | $X,XXX |

## Part III — Totals
3.   Total tax (line 1 + line 2):            $X,XXX
4.   Claims (Schedule C line 15):            $X,XXX
5.   Deposits made for the quarter:          $X,XXX   [ ] safe harbor box
6.   Overpayment from previous quarters:     $X,XXX
7.   Form 720-X amount included on line 6:   $X,XXX
8.   Line 5 + line 6:                        $X,XXX
9.   Line 4 + line 8:                        $X,XXX
10.  Balance due (line 3 − line 9):          $X,XXX
11a. Overpayment (line 9 − line 3):          $X,XXX   11b [ ] apply to next return [ ] refund

## Schedule A — Part I net liability by semimonthly period
[Only when Part I shows a liability. Never for Part II taxes or a one-time gas guzzler filing.]

| Month | 1st–15th | 16th–last day |
|-------|----------|---------------|
| First month  | A: $X,XXX | B: $X,XXX |
| Second month | C: $X,XXX | D: $X,XXX |
| Third month  | E: $X,XXX | F: $X,XXX |
| Special September rule (Q3 only) | G: $X,XXX | |

## Schedule C — Claims (only if Part I or II shows a liability)
Month your income tax year ends: MM
| Line | Type of use / claim | Period of claim | Rate | Gallons or count | Amount | CRN |
|------|---------------------|-----------------|------|------------------|--------|-----|
| 3d   | Undyed diesel used on a farm (type of use 1) | MM/DD/YYYY–MM/DD/YYYY | $.243 | X,XXX | $X,XXX | 360 |
| 15   | Total claims | | | | $X,XXX | |

## Schedule T — Two-party exchanges (only for taxable fuel registrants)

## Required attachments / next steps
- [ ] Semimonthly EFT deposits required if Part I net liability for the quarter exceeds $2,500
- [ ] Form 6627 / 6197 / 7208 attached for IRS Nos. computed on those forms
- [ ] Form 637 registration number entered for ultimate vendor or credit card issuer claims
- [ ] Form 8453-EX if filing electronically and the provider requires it
- [ ] Pay line 10 by the due date: EFTPS, Direct Pay, EFW (e-file), or check with Form 720-V

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list warnings>
- Year-aware notes:
  - Form 720 and instructions revision used (Rev. MM-YYYY)
  - PCORI rate and row verified against the notice for the plan year end (Notice 2024-83: $3.47; Notice 2025-61: $3.84)
  - Inflation-adjusted rates (arrow shafts, air transportation) verified against the Rev. Proc. for the calendar year

## Sources cited in this draft
- IRS Form 720 (Rev. MM-YYYY)
- IRS Instructions for Form 720 (Rev. MM-YYYY)
- IRC sections for each IRS No. reported (e.g., §§4161, 4371, 4375–4377, 4475, 5000B)
- Notice YYYY-XX (PCORI rate, if applicable)
- IRS Pub. 510 (Excise Taxes)
```

The draft is **not** the final filed form. The user (or agent, with consent) submits via IRS-authorized e-file or paper.

---

## References

Loaded on demand based on the user's category.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete walkthrough of Form 720 header, Parts I–III, and Schedules A/C/T
- [`references/irs-number-catalog.md`](./references/irs-number-catalog.md) — Lookup table of every IRS Number on Form 720 with rate, base, and statutory citation
- [`references/pcori-fee.md`](./references/pcori-fee.md) — PCORI fee deep dive: covered-lives counting methods, rate history, plan-year-end mapping, deadline (Q2 / July 31)
- [`references/fuel-taxes.md`](./references/fuel-taxes.md) — Gasoline, diesel, kerosene, alternative fuels — rates and Schedule C claim mechanics
- [`references/sport-fishing-archery.md`](./references/sport-fishing-archery.md) — Manufacturer's tax computation under §4161; sales price, constructive sale price, exemptions
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes that trigger §6651/§6656 penalties on Form 720
- [`filing.md`](./filing.md) — Filing channels: Form 720 e-file via an IRS-approved MeF provider, paper to Ogden, payment options

## Examples

End-to-end worked Form 720s. Use these as patterns when the user's situation is similar.

- [`examples/pcori-fee-self-insured-health.md`](./examples/pcori-fee-self-insured-health.md) — Small business with a self-insured health plan computing the PCORI fee for the Q2 2026 return
- [`examples/sport-fishing-equipment-importer.md`](./examples/sport-fishing-equipment-importer.md) — Fishing rod importer reporting §4161 tax on IRS No. 110 (Part II, no Schedule A, no deposits)
- [`examples/trucking-hvut-credit-reconciliation.md`](./examples/trucking-hvut-credit-reconciliation.md) — Trucking company: HVUT credits routed to Form 2290 / Form 8849, and the §4051(b) tax on parts installed within 6 months reported on IRS No. 33

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS site for the quarter being filed — rates and notices update each year.

- [Form 720 (latest)](https://www.irs.gov/pub/irs-pdf/f720.pdf) — the form itself
- [Instructions for Form 720 (latest)](https://www.irs.gov/pub/irs-pdf/i720.pdf) — line-by-line IRS guidance
- [About Form 720](https://www.irs.gov/forms-pubs/about-form-720) — IRS landing page with archive of past revisions
- [Publication 510](https://www.irs.gov/pub/irs-pdf/p510.pdf) — Excise Taxes (the deep authority)
- [Notice 2024-83](https://www.irs.gov/irb/2024-49_IRB#NOT-2024-83) — PCOR fee $3.47 for policy and plan years ending Oct 1, 2024 – Sep 30, 2025
- [Notice 2025-61](https://www.irs.gov/irb/2025-45_IRB#NOT-2025-61) — PCOR fee $3.84 for policy and plan years ending Oct 1, 2025 – Sep 30, 2026 (a new notice sets each later year's amount; re-check before July 31)
- [Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) §§2.44–2.45 and [Rev. Proc. 2025-32](https://www.irs.gov/irb/2025-45_IRB#REV-PROC-2025-32) §§4.43–4.44 — arrow shaft and air transportation amounts for 2025 and 2026
- [Notice 2025-55](https://www.irs.gov/pub/irs-drop/n-25-55.pdf) — remittance transfer tax deposit penalty relief, Q1–Q3 2026
- [Form 720 e-file FAQ](https://www.irs.gov/e-file-providers/frequently-asked-questions-form-720-quarterly-federal-excise-tax-return-e-file) — e-filing Form 720 is optional
- [Instructions for Form 2290 (Rev. July 2026)](https://www.irs.gov/pub/irs-pdf/i2290.pdf), "Line 5" — where HVUT credits go
- Treas. Reg. §46.4376-1 — self-insured plan counting methods; Treas. Reg. §§40.6302(c)-1 to -3 — deposit rules
- IRC Subtitle D (Miscellaneous Excise Taxes), chapters 31–36 and 49
- IRC §4051 — retail tax on heavy trucks, trailers, tractors; §4051(b) parts installed within 6 months; terminates Oct 1, 2028 (§4051(c))
- IRC §4161 / §4162 — sport fishing and archery manufacturers tax
- IRC §4371 — tax on policies issued by foreign insurers
- IRC §4375 / §4376 / §4377 — PCOR fee (ends for policy and plan years ending after Sep 30, 2029)
- IRC §4475 — remittance transfer tax (P.L. 119-21, transfers after Dec 31, 2025)
- IRC §4611 / §4661 / §4671 — Superfund petroleum and chemical taxes
- IRC §4681 — ozone-depleting chemicals
- IRC §4701 — tax on obligations not in registered form (IRS No. 31)
- IRC §5000B — indoor tanning services tax
- IRC §6651 — failure to file and failure to pay penalties
- IRC §6656 — failure to deposit penalty
- IRC §7502 / §7503 — timely mailing; weekend and holiday due dates

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. Federal excise tax has narrow industry-specific rules; complex situations (multi-jurisdiction fuel distribution, large-volume manufacturer credits, foreign-insurance treaties) warrant a licensed tax professional or excise-tax specialist.
