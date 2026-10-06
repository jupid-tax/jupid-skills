---
name: form-7004
description: >
  Use this skill when a partnership, multi-member LLC, S corporation, C corporation,
  estate, trust, or other business entity needs more time to file its federal return
  and must prepare IRS Form 7004. Triggers on phrases like "Form 7004", "business tax
  extension", "extend my 1065", "extension for my S corp", "1120-S extension",
  "extend the corporate return", "LLC tax extension", "file an extension for my
  partnership", "Form 7004 form code", "what code for Form 7004", "when is the 7004
  due", "tentative tax on 7004", "where do I mail Form 7004". Do NOT use for an
  individual return, a Schedule C sole proprietorship, or a single-member LLC owned by
  a US person (Form 4868; use form-1040). Do NOT use for Form 990-series or Form 1041-A
  (Form 8868), Form 5500 (Form 5558; use form-5500), Forms W-2/1099 (Form 8809), payroll
  returns such as Form 941 (no Form 7004 code; use form-941), or state extensions. Do NOT
  use to prepare the business return itself (use form-1065, form-1120-s, or form-1120).
form: Form 7004 (Application for Automatic Extension of Time To File Certain Business Income Tax, Information, and Other Returns)
audience: [llcm, scorp, ccorp, partnership, nonresident]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f7004.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i7004.pdf
---

# Form 7004 — Application for Automatic Extension of Time To File Certain Business Income Tax, Information, and Other Returns

This skill produces a filing-ready Form 7004 draft: the correct form code, the original and extended due dates, Part II status boxes, a tentative tax with the arithmetic shown, the balance to pay by the original due date, and the right channel and address. The form is one page, but a wrong code, a late filing date, a mismatched name, or an unpaid balance each defeats it.

The judgment concentrates in four places: whether the return is covered at all (individual, exempt-organization, information, and payroll returns are not), the original due date (it varies by return type, fiscal year end, June 30 corporations, dissolutions, and weekends), the line 6 estimate (the extension extends filing, never payment), and the paper address (state group, asset test, foreign-owned DE exception).

**Companion guide for end users:** [Form 7004 Instructions 2026: Business Tax Extension Line by Line, Form Codes, and 2027 Due Dates](https://jupid.com/blog/form-7004-instructions-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

**Version verified:** Form 7004 (Rev. December 2025) and Instructions for Form 7004 (Rev. December 2025), the current revisions on irs.gov as of 2026-10-06. They apply to 2026 fiscal-year returns now coming due and to tax year 2026 returns due in 2027. Before each use, open https://www.irs.gov/forms-pubs/about-form-7004 and confirm no newer revision exists; if one does, re-check every code, line, and address against its PDF.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user mentions Form 7004 or asks for an extension of a business return: Form 1065, 1120-S, 1120, 1041, 1120-F, 1042, 3520-A, 8804, or any other return on the Form 7004 code list
- A multi-member LLC, partnership, S corporation, C corporation, estate, or trust will not have its return ready by the original due date
- A foreign-owned single-member LLC needs more time for its pro forma Form 1120 with Form 5472
- The user asks what form code, due date, or mailing address applies to a business extension

Do **not** engage this skill when:

- The return is a Form 1040, 1040-SR, 1040-NR, or 1040-SS, including Schedule C businesses and single-member LLCs owned by an individual → Form 4868; see [`form-1040`](../form-1040/SKILL.md)
- The return is Form 990, 990-EZ, 990-PF, 990-T, 1041-A, 4720, 5227, 6069, or 8870 → Form 8868
- The return is Form 5500 or 8955-SSA → Form 5558; see [`form-5500`](../form-5500/SKILL.md)
- The return is Form 706 → Form 4768; Form 709 → Form 4868 or Form 8892
- The return is an information return (W-2, 1099, 1098, 1095, 5498, 8027, others) → Form 8809
- The return is Form 940, 941, 943, 944, 945, 720, or 2290: none is on the Form 7004 code list; see [`form-941`](../form-941/SKILL.md) for quarterly payroll
- The user wants more time to **pay**: Form 7004 does not give it; see [`form-9465`](../form-9465/SKILL.md) for installment agreements after the return is filed
- The user wants the business return itself prepared → [`form-1065`](../form-1065/SKILL.md), [`form-1120-s`](../form-1120-s/SKILL.md), [`form-1120`](../form-1120/SKILL.md)

Boundaries with sibling skills:
- [`form-5472`](../form-5472/SKILL.md) prepares the foreign-owned DE's Form 5472 and pro forma Form 1120; this skill prepares its Form 7004 (code 12, special fax/mail address).
- [`form-3520`](../form-3520/SKILL.md) covers Form 3520-A; this skill prepares its extension (code 27).
- [`form-843`](../form-843/SKILL.md) handles penalty abatement requests after a notice; Form 7004 is not a reasonable-cause filing.

If the entity type is unclear (for example, "my LLC needs an extension"), ask how the LLC is taxed before choosing between Form 4868 and Form 7004.

---

## Prerequisites

Collect these before drafting. If any is missing, **ask and stop until answered.** Do not pick defaults.

1. **Return type to be extended.** Which return the entity files (Form 1065, 1120-S, 1120, 1041 and which kind of 1041, or another code-list return). For an LLC, ask how it is classified (default partnership, Form 2553 S election, Form 8832 C election, or single-member disregarded). For a homeowners association electing Form 1120-H, ask which form type the IRS originally assigned (i7004, Line 1).
2. **Legal name exactly as on last year's return**, and whether it changed since. Form 7004 must use last year's name (i7004).
3. **EIN.** No EIN, no valid extension; stop and route to the EIN application.
4. **Mailing address**, and whether it changed (Form 7004 does not update it; Form 8822-B does).
5. **Tax year.** Calendar year, or fiscal year begin and end dates. If shorter than 12 months, the reason: initial return, final return (and the dissolution date), change in accounting period (and whether Form 1128 was filed), consolidated return to be filed, or other.
6. **Special status questions** (one line each):
   - Foreign corporation with no office or place of business in the United States? (line 2)
   - Common parent of a group filing a consolidated return? If yes, every member's name, address, and EIN (line 3)
   - Books and records kept outside the United States and Puerto Rico, foreign corporation with a U.S. office, or domestic corporation with principal income from U.S. territories? (line 4)
   - Foreign-owned U.S. disregarded entity filing Form 5472? (special filing channel)
7. **Tax figures** (skip to "-0-" only after the user confirms no entity-level tax):
   - Corporations: projected taxable income, nonrefundable credits, any other taxes on the return
   - Partnerships and S corporations: whether any entity-level tax applies (look-back interest, imputed underpayment, built-in gains, excess net passive income, LIFO recapture)
   - Payments already made: estimated tax payments, prior-year overpayment credited, withholding, refundable credits
8. **Filing channel and payment method.** E-file through software or a provider, paper, or (foreign-owned DE) fax. If line 8 will be positive: EFTPS, Electronic Funds Withdrawal, or a third party.
9. **For a paper filing:** the state of the principal business, office, or agency and total assets at the end of the tax year.
10. **Today's date** relative to the original due date. If the due date has passed, stop: see Step 2.

Tight questions to use when a fact is missing:

- "How is the LLC taxed for federal purposes: as a partnership (the default for two or more members), as an S corporation (Form 2553 filed), or as a C corporation (Form 8832 filed)?"
- "What exact name appears on the entity's last filed federal return? Has the legal name changed since?"
- "Does the tax year end December 31? If not, what are the first and last days of the year you need to extend?"
- "Will the return show any tax owed by the entity itself? If yes, what is the projected amount before payments, and what has already been paid this year?"
- "Will you e-file the return itself? If yes, we should e-file this extension too."

---

## Workflow

Execute in order.

### Step 1 — Confirm the return is covered and pick the code

Find the return in [`references/form-codes-and-due-dates.md`](./references/form-codes-and-due-dates.md). If it is not on the code list, stop and redirect (Form 4868, 8868, 5558, 4768, 8892, or 8809). Read the two-digit code from the form's table. One Form 7004 covers one return; list every return the entity needs to extend and draft one application for each (i7004, No Blanket Requests).

### Step 2 — Compute the deadlines

Compute the original due date from the year end (or dissolution date) using the return's rule, then apply the Saturday/Sunday/legal-holiday rule (IRC §7503). Compute the extended due date by adding the extension period to the statutory date, then apply §7503 again. Extension periods: 6 months generally; 5½ months for Form 1041 estates (other than bankruptcy estates) and trusts; 7 months for C corporations with a June 30 year end beginning before January 1, 2026 (i7004, Extension Period).

If today is after the original due date, Form 7004 cannot be validly filed (i7004, When To File). Tell the user, recommend filing the return as soon as possible, and stop drafting.

### Step 3 — Identification block

Name exactly as on last year's return; EIN; street address (P.O. box only if no street delivery); foreign address in city, province or state, country order (i7004, Specific Instructions).

### Step 4 — Part II status lines 2 to 4

Check line 2, 3, or 4 only on a "yes" from Prerequisite 6. Apply the different deadlines: line 2 and line 4 filers file Form 7004 by the 15th day of the 6th month (i7004). Line 4 gives 3 more months (partnerships, S corporations) or 4 more months (C corporations, Form 1120-POL).

### Step 5 — Lines 5a and 5b

Enter the calendar year or fiscal dates. For a short year, check exactly one reason on 5b; "Other" needs an attached explanation; "Change in accounting period" needs Form 1128 approval applied for unless conditions are met (i7004).

### Step 6 — Lines 6 to 8

Load [`references/tentative-tax-and-payment.md`](./references/tentative-tax-and-payment.md). Show the arithmetic for line 6 from the user's figures, sum line 7, subtract for line 8. Round only totals. If the user's estimate looks low against the facts, say so; a corporation's extension requires remitting the properly estimated unpaid tax (Treas. Reg. §1.6081-3(a)(3)).

### Step 7 — Plan the payment

Line 8 is due by the original due date. Record the method and date. For corporations, run the 90% check: line 6 (or tax paid by the original due date) should be at least 90% of the expected final total tax for late-payment relief (i7004).

### Step 8 — Validate

Run every check under **Validation**.

### Step 9 — Produce the deliverable

Fill the **Output format** template, every line including zeros.

### Step 10 — Hand off

- Tell owners that the business extension does not extend their own returns; each partner or shareholder waiting on a K-1 files Form 4868 by their own deadline (Treas. Reg. §1.6081-2(e); see [`form-1040`](../form-1040/SKILL.md)).
- Put the extended due date on the calendar. For partnerships it is also the Schedule K-1 deadline (Treas. Reg. §1.6031(b)-1T(b)).
- When the return is prepared, the Form 7004 payment goes on Form 1120 Schedule J line 17, Form 1120-S line 24b, or Form 1065 line 30 (2025 forms).
- Route the return to [`form-1065`](../form-1065/SKILL.md), [`form-1120-s`](../form-1120-s/SKILL.md), or [`form-1120`](../form-1120/SKILL.md).

### Step 11 — File (only with explicit authorization)

Follow [`filing.md`](./filing.md): channel decision tree, e-file through MeF, paper addresses by form and state, the foreign-owned DE fax/mail route, consent and security rules. If the user will file themselves, give them the draft and the address or channel and stop.

---

## Line-by-line guidance

Full map with the printed text of each field: [`references/line-by-line.md`](./references/line-by-line.md). Key rules:

### Identification

- **Name**: last year's name, even after a rename. A name or EIN that does not match IRS records means "you will not have a valid extension" (i7004).
- **Address**: a new address here does not update IRS records (i7004).
- **No signature** line exists (i7004).

### Part I, line 1 — form code

| Entity | Return | Code |
|---|---|---|
| Partnership or multi-member LLC (default) | Form 1065 | 09 |
| S corporation (including an LLC with a Form 2553 election) | Form 1120-S | 25 |
| C corporation (including an LLC electing association status) | Form 1120 | 12 |
| Foreign-owned U.S. DE (pro forma Form 1120 + Form 5472) | Form 1120 | 12 |
| Estate other than a bankruptcy estate | Form 1041 | 04 |
| Trust | Form 1041 | 05 |
| Bankruptcy estate | Form 1041 | 03 |
| Partnership withholding on foreign partners | Form 8804 | 31 |
| Foreign corporation | Form 1120-F | 15 |
| Withholding agent | Form 1042 | 08 |
| Foreign trust with a U.S. owner | Form 3520-A | 27 |

The full 34-code table is in [`references/form-codes-and-due-dates.md`](./references/form-codes-and-due-dates.md). Codes 10, 13, and 14 do not exist on the December 2025 form.

### Part II

| Line | Check or enter when | Effect |
|---|---|---|
| 2 | Foreign corporation with no U.S. office or place of business | Form 7004 due the 15th day of the 6th month |
| 3 | Common parent filing a consolidated return | Attach member list (name, address, EIN) |
| 4 | Qualifies under Treas. Reg. §1.6081-5 | Already has to the 15th day of the 6th month to file and pay; line 4 asks for 3 (partnership, S corp) or 4 (C corp, 1120-POL) more months to file |
| 5a | Always | Calendar year, or beginning and ending dates |
| 5b | Year shorter than 12 months | Exactly one reason; "Other" needs a statement |
| 6 | Always | Expected total tax after nonrefundable credits; "-0-" if none |
| 7 | Always | Payments and refundable credits already made |
| 8 | Always | Line 6 − line 7, paid by the original due date |

### Deadlines at a glance (calendar year)

| Return | TY2025 Form 7004 due | TY2025 extended | TY2026 Form 7004 due | TY2026 extended |
|---|---|---|---|---|
| 1065, 1120-S | March 16, 2026 | Sept 15, 2026 | March 15, 2027 | Sept 15, 2027 |
| 1120 | April 15, 2026 | Oct 15, 2026 | April 15, 2027 | Oct 15, 2027 |
| 1041 estate/trust | April 15, 2026 | Sept 30, 2026 | April 15, 2027 | Sept 30, 2027 |

TY2025 calendar-year Forms 1065 and 1120-S were due Monday, March 16, 2026 because March 15 fell on a Sunday (2025 Instructions for Forms 1065 and 1120-S). Extended dates run from the statutory 15th, not from the rolled date (Treas. Reg. §1.6081-2(a), §1.6081-3(a)).

### Special due-date rules

| Situation | Original due date | Extension | Source |
|---|---|---|---|
| Fiscal-year partnership or S corporation | 15th day of 3rd month after year end | 6 months | IRC §6072(b); i7004 |
| Fiscal-year C corporation (not June 30) | 15th day of 4th month | 6 months | IRC §6072(a); i7004 |
| C corporation, June 30 year end, year began before Jan 1, 2026 | 15th day of 3rd month | 7 months | 2025 i1120; IRC §6081(b); Treas. Reg. §1.6081-3(e) |
| C corporation, June 30 year end, year began in 2026 | 15th day of 4th month | 6 months | P.L. 114-41 §2006(a)(3)(B); i7004 |
| Dissolved corporation | 15th day of 4th month after the dissolution date | 6 months | 2025 i1120, When To File |
| Foreign corporation, no U.S. office (line 2) | 15th day of 6th month | 6 months | IRC §6072(c); i7004 Line 2 |
| §1.6081-5 filer (line 4) | Automatic to 15th day of 6th month | +3 months (partnership, S corp) or +4 (C corp, 1120-POL) | i7004 Line 4 |

A short tax year ending anytime in June is treated as ending June 30 (i7004).

### Foreign-owned U.S. disregarded entity

A foreign-owned single-member LLC files a pro forma Form 1120 with Form 5472 and extends it on Form 7004 with code 12, "Foreign-owned U.S. DE" written across the top, filed by fax to 855-887-7737 or by mail to the PIN Unit (Internal Revenue Service, 1973 Rulon White Blvd, M/S 6112, Attn: PIN Unit, Ogden, UT 84201), never to the regular Form 7004 address (Instructions for Form 5472, Rev. December 2024). Line 6 is -0-. See [`form-5472`](../form-5472/SKILL.md).

### What a valid extension does not do

- It does not extend the time to pay. Interest runs from the original due date even with an extension; the failure-to-pay penalty is 1/2 of 1% per month or part of a month, up to 25% (i7004, Payment of Tax).
- It does not extend any partner's or shareholder's own return (Treas. Reg. §1.6081-2(e)).
- It does not cover a second return; each return needs its own Form 7004 (i7004).
- It does not produce an approval letter; the IRS writes only to disallow (i7004).

### What the deadline is worth (year-dependent; re-check the current Rev. Proc.)

| Penalty avoided by a timely Form 7004 | Returns required to be filed in 2026 | In 2027 |
|---|---|---|
| Form 1065 (IRC §6698) or Form 1120-S (IRC §6699), per partner or shareholder per month or part, max 12 months | $255 | $260 |
| Income tax return more than 60 days late (IRC §6651(a)), minimum | lesser of $525 or the tax | lesser of $535 or the tax |

Sources: 2025 Instructions for Forms 1065, 1120-S, 1120; Rev. Proc. 2024-40 §2.53, §2.56, §2.57; Rev. Proc. 2025-32 §4.52, §4.55, §4.56.

---

## Validation

Run every check. Surface failures; do not silently fix.

### Math checks

- [ ] Line 8 = line 6 − line 7
- [ ] Line 6 arithmetic reproduced from the user's figures (taxable income × rate, plus other taxes, minus nonrefundable credits for corporations)
- [ ] Line 7 equals the sum of the listed payments and refundable credits, excluding the payment to be made with Form 7004
- [ ] Rounding applied to totals only, and to all amounts if any are rounded (i7004)
- [ ] Line 8 is not negative; if line 7 exceeds line 6, flag it and confirm with the user's preparer how the software reports it (Form 7004 is not a refund claim)

### Validity checks (any failure blocks the extension)

- [ ] The return is on the Form 7004 code list and line 1 matches the return the entity actually files
- [ ] Filing date is on or before the original due date (line 2 and line 4 filers: the 15th day of the 6th month)
- [ ] Name matches last year's return; EIN is correct
- [ ] One Form 7004 per return
- [ ] Line 8 will be paid by the original due date (corporations: Treas. Reg. §1.6081-3(a)(3))

### Consistency checks

- [ ] Exactly one 5b box if the year is short; none if it is 12 months
- [ ] Line 5a dates match the year end used for the due date
- [ ] Line 3 checked → member list attached; line 5b "Other" → explanation attached
- [ ] Line 2 checked → entity is a foreign corporation with no U.S. office; line 4 checked → entity is in one of the four §1.6081-5 categories
- [ ] Extension length matches the filer: 5½ months for codes 04 and 05; 7 months only for June 30 C corporation years beginning before 2026
- [ ] Paper address chosen from the i7004 table using form, state, and (for 1065/1120/1120-S and others in the Kansas City states) total assets
- [ ] Foreign-owned U.S. DE → code 12, "Foreign-owned U.S. DE" across the top, fax or PIN Unit address only

### Sanity checks (warn, do not block)

- [ ] Corporation: line 6 below 90% of the expected final total tax → late-payment penalty risk after the original due date
- [ ] Line 7 well below line 6 for a corporation → possible estimated tax penalty (Form 2220), separate from Form 7004
- [ ] Paper Form 7004 with a return that will be e-filed → i7004 penalty-notice caution
- [ ] Partnership or S corporation with a nonzero line 6 → confirm the entity-level tax with the preparer
- [ ] Owners told to file their own Form 4868
- [ ] Return due date falls in June for a C corporation → explain the June 30 rule and the IRS chart inconsistency noted in the due-date reference

---

## Output format

```markdown
# Form 7004 — DRAFT for <entity name> (<tax year or period>)

## Filing summary
- Return extended: Form <number> (code <NN>)
- Tax year: <calendar year YYYY | MM/DD/YYYY to MM/DD/YYYY (short year: reason)>
- Form 7004 due (original due date of the return): <Weekday, Month D, YYYY>
- Extended return due: <Weekday, Month D, YYYY> (<6 | 5½ | 7> months)
- Channel: <e-file via software/provider | paper to <address> | fax 855-887-7737 (foreign-owned DE)>
- Payment due with this form: $<line 8> by <original due date> via <EFTPS | EFW | third party>

## Identification
Name: <exactly as on prior-year return>
Identifying number: <EIN>
Address: <street, room/suite, city, state, ZIP | foreign format>

## Part I
1. Form code: <NN>

## Part II
2. Foreign corporation without U.S. office:      ☐ | ☒
3. Common parent of consolidated group:          ☐ | ☒  (member list attached: yes/no)
4. Qualifies under Reg. §1.6081-5:              ☐ | ☒
5a. Calendar year 20<YY> | tax year beginning <MM/DD>, 20<YY>, ending <MM/DD>, 20<YY>
5b. Short tax year: N/A | ☒ <Initial | Final | Change in accounting period | Consolidated return to be filed | Other (statement attached)>
6. Tentative total tax:                          $<amount or -0->
7. Total payments and credits:                   $<amount or -0->
8. Balance due:                                  $<amount or -0->

## Line 6 and 7 workings
<arithmetic, one line per component, with the source of each figure>

## Attachments
- [ ] Consolidated group member list (if line 3)
- [ ] Short-year explanation (if 5b "Other")
- [ ] Form 1138 (if reducing the deposit for an expected NOL carryback)

## Validation summary
- Math: <pass | failures>
- Validity: <pass | failures>
- Consistency: <pass | failures>
- Warnings: <list>

## Next steps
- Owners' Form 4868 by <date>
- Extended return (and K-1s) due <date>
- Report the Form 7004 payment on <return line> when the return is filed

## Sources cited in this draft
- Form 7004 (Rev. December 2025); Instructions for Form 7004 (Rev. December 2025)
- <return instructions used for the due date>
- <regulations and IRC sections used>
```

The draft is not a filed extension. Nothing is extended until the IRS receives a valid Form 7004 by the original due date and the balance is paid.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — every field of Form 7004 with the printed text and the instruction for it
- [`references/form-codes-and-due-dates.md`](./references/form-codes-and-due-dates.md) — all 34 form codes, returns not covered and their forms, extension lengths, original and extended due dates, fiscal-year worked dates
- [`references/tentative-tax-and-payment.md`](./references/tentative-tax-and-payment.md) — estimating line 6 by return type, line 7 components, paying line 8, the 90% rule, failure-to-pay penalty, interest, late-filing penalty amounts by year
- [`references/common-mistakes.md`](./references/common-mistakes.md) — fifteen recurring errors with the fix and authority
- [`filing.md`](./filing.md) — channel decision tree, MeF e-file, full Where To File table, foreign-owned DE fax/mail route, consent and security rules

## Examples

- [`examples/partnership-llc-1065.md`](./examples/partnership-llc-1065.md) — calendar-year multi-member LLC, code 09, zero tax, paper filing to Ogden, partner-count penalty math, owners' Form 4868
- [`examples/c-corp-balance-due.md`](./examples/c-corp-balance-due.md) — calendar-year C corporation, code 12, tentative tax with a credit, EFW payment, 90% relief test and a counterfactual penalty
- [`examples/dissolved-ccorp-short-year.md`](./examples/dissolved-ccorp-short-year.md) — C corporation dissolved mid-2026, short final year on lines 5a/5b, November due date, Kansas City address with the asset test

## Sources

Re-verify each source every filing season; codes, addresses, and dollar amounts change.

- [Form 7004 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/f7004.pdf) and [Instructions for Form 7004 (Rev. December 2025)](https://www.irs.gov/pub/irs-pdf/i7004.pdf)
- [About Form 7004](https://www.irs.gov/forms-pubs/about-form-7004) — current revision check
- [E-filing Form 7004](https://www.irs.gov/Efile7004) — MeF availability, items that cannot be e-filed, due date charts
- [Where to file Form 7004](https://www.irs.gov/filing/where-to-file-form-7004)
- [Instructions for Form 5472 (Rev. December 2024)](https://www.irs.gov/pub/irs-pdf/i5472.pdf) — foreign-owned U.S. DE extensions
- 2025 Instructions for [Form 1065](https://www.irs.gov/pub/irs-pdf/i1065.pdf), [Form 1120-S](https://www.irs.gov/pub/irs-pdf/i1120s.pdf), [Form 1120](https://www.irs.gov/pub/irs-pdf/i1120.pdf), [Form 1041](https://www.irs.gov/pub/irs-pdf/i1041.pdf) — due dates and penalties
- [Form 8878-A](https://www.irs.gov/pub/irs-pdf/f8878a.pdf) — EFW authorization for Form 7004
- Forms [4868](https://www.irs.gov/pub/irs-pdf/f4868.pdf), [8868](https://www.irs.gov/pub/irs-pdf/f8868.pdf), [5558](https://www.irs.gov/pub/irs-pdf/f5558.pdf), [4768](https://www.irs.gov/pub/irs-pdf/f4768.pdf), [8892](https://www.irs.gov/pub/irs-pdf/f8892.pdf), [8809](https://www.irs.gov/pub/irs-pdf/f8809.pdf) — extension forms for returns Form 7004 does not cover
- IRC §6072 (due dates), §6081 (extensions), §7503 (weekends and holidays), §7502 (timely mailing), §6651 (failure to file and pay), §6698 and §6699 (partnership and S corporation late-filing penalties), §11(b) (21% corporate rate), §6621 (interest rate), §6655 (corporate estimated tax), §443 (short periods)
- Treas. Reg. §1.6081-2 (partnerships), §1.6081-3 (corporations), §1.6081-5 (books abroad, foreign corporations with U.S. office), §1.6081-6 (estates and trusts), §1.6031(b)-1T(b) (K-1 timing)
- P.L. 114-41 §2006(a)(3)(B) — June 30 C corporation due-date transition
- [Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) and [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) — penalty amounts for returns required to be filed in 2026 and 2027

## Disclaimer

This skill encodes procedural guidance from public IRS forms, instructions, regulations, and the Internal Revenue Code. It is not tax advice and does not create a CPA-client relationship. Tell the user that the draft is a starting point and that entity classification questions, consolidated groups, foreign filers, and any entity-level tax estimate deserve review by a licensed tax professional.
