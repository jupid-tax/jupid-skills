---
name: form-1040-nr
description: >
  Use this skill when a nonresident alien individual (or the representative of
  one) needs to prepare Form 1040-NR, the U.S. Nonresident Alien Income Tax
  Return, with its Schedules OI, NEC, A (Form 1040-NR), and P. Triggers on
  phrases like "Form 1040-NR", "nonresident alien tax return", "1040NR",
  "I'm on an F-1 / J-1 / H-1B visa and need to file", "substantial presence
  test", "am I a resident or nonresident for tax", "Schedule NEC", "30% tax
  on dividends refund", "treaty exemption on my US return", "foreign owner of
  a US LLC personal return", "Form 8843 with my return", or "refund of tax
  withheld on Form 1042-S". Do NOT use for: U.S. citizens and resident aliens,
  including green card holders and anyone who meets the substantial presence
  test without an exception (use form-1040); a nonresident spouse electing to
  be treated as a resident on a joint return (use form-1040); the LLC's own
  pro forma Form 1120 and Form 5472 (use form-5472); ITIN applications (use
  form-w7); amending a filed 1040-NR (use form-1040-x together with this skill
  for the corrected return); dual-status years (this skill identifies them and
  stops; see Boundaries).
form: Form 1040-NR (U.S. Nonresident Alien Income Tax Return)
audience: [nonresident, individual, llc1, freelance]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f1040nr.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1040nr.pdf
---

# Form 1040-NR — U.S. Nonresident Alien Income Tax Return

This skill produces an audit-grade draft of Form 1040-NR and its schedules for an individual who is a nonresident alien for the whole tax year. It settles residency first, sorts every U.S. item of income into effectively connected income (page 1, graduated rates), income not effectively connected (Schedule NEC, 30% or a treaty rate on the gross amount), or exempt income (Schedule OI item L and line 1k), then computes the tax and reconciles withholding from Forms W-2, 1042-S, 8805, and 8288-A.

The arithmetic is ordinary. The judgment sits in four places: whether the person is a nonresident at all, whether they were engaged in a U.S. trade or business, which treaty article applies and whether Form 8833 is required, and which deductions survive (no standard deduction except one treaty case). At each of these the agent asks; it never assumes.

The line map below was verified against the **2025 Form 1040-NR (filed in 2026)**: form created 9/8/25, Instructions for Form 1040-NR (2025) dated Jan 29, 2026, Schedule NEC created 4/16/25, Schedule OI created 4/17/25, Schedule A (Form 1040-NR) created 12/19/25, Schedule P created 4/17/25. The 2026 revision (filed in 2027) must be re-checked line by line before use: https://www.irs.gov/forms-pubs/about-form-1040-nr.

### Key numbers for 2025 returns (year-dependent unless marked statutory)

| Item | Value | Source |
|---|---|---|
| Due date, wages subject to withholding | April 15, 2026 | Instructions for Form 1040-NR, When and Where Should You File? |
| Due date, no such wages | June 15, 2026 | Same; IRC §6072(c) (statutory) |
| Extended due date with Form 4868 | October 15, 2026; December 15, 2026 for the June 15 group | Pub. 519 (2025), ch. 7 |
| Deductions and credits require a return filed within | 16 months of the due date | Treas. Reg. §1.874-1(b) (statutory rule) |
| Substantial presence test | 31 days this year and 183 weighted days (×1, ×1/3, ×1/6) | IRC §7701(b)(3) (statutory) |
| Tax on NEC income | 30% of gross, or treaty rate | IRC §871(a); Schedule NEC |
| NEC capital gains taxable only if present | 183 days or more in the tax year | IRC §871(a)(2) (statutory) |
| India Art. 21(2) standard deduction | $15,750 single or MFS; $31,500 QSS | Pub. 519 (2025) Worksheet 5-1 |
| Schedule A (NR) line 1b cap | $40,000 ($20,000 MFS), reduced above $500,000 ($250,000 MFS) line 11b, floor $10,000 ($5,000 MFS) | Instructions for Form 1040-NR, What's New and Schedule A line 1b |
| Form 8833 failure penalty, individual | $1,000 per failure | IRC §6712; Form 8833 |
| Refund wait for 1042-S, 8805, 8288-A withholding | up to 6 months | Instructions for Form 1040-NR, Refund Information |

**Companion guide for end users:** [Form 1040-NR Instructions 2026: Who Must File, Line by Line, Schedule NEC, and the Substantial Presence Test](https://jupid.com/blog/form-1040-nr-instructions-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user names Form 1040-NR, Schedule NEC, Schedule OI, or Schedule A (Form 1040-NR).
- The user is not a U.S. citizen, holds no green card, and had U.S. wages, a U.S. business, U.S. rental property, U.S. dividends, or a Form 1042-S.
- The user is a student, teacher, trainee, or researcher on an F, J, M, or Q visa with any U.S. income, or needs Form 8843 with a return.
- The user owns a U.S. single-member LLC from abroad and asks about their own personal U.S. return.
- The user wants a refund of U.S. tax withheld at 30% (or above the treaty rate) on Form 1042-S.

Do **not** engage this skill when:

- The person is a U.S. citizen or green card holder at any time in the year, or meets the substantial presence test with no exception → [`../form-1040/SKILL.md`](../form-1040/SKILL.md).
- A nonresident married to a U.S. citizen or resident wants the one-time election to be treated as a resident for the whole year → that is made on a joint Form 1040, not Form 1040-NR (Instructions for Form 1040-NR, "Election To Be Taxed as a Resident Alien") → [`../form-1040/SKILL.md`](../form-1040/SKILL.md).
- The question is the LLC's own information return → [`../form-5472/SKILL.md`](../form-5472/SKILL.md) (pro forma Form 1120 with Form 5472). This skill covers only the owner's Form 1040-NR.
- The person needs an ITIN → [`../form-w7/SKILL.md`](../form-w7/SKILL.md) first; the W-7 travels with this return.
- The 1040-NR was already filed and needs a change → [`../form-1040-x/SKILL.md`](../form-1040-x/SKILL.md), using this skill to build the corrected return.
- The filer is a nonresident alien estate or trust → out of scope (the instructions route those to subchapter J and the Form 1041 instructions). Say so and stop.

### Boundaries: stop and ask

- **Dual-status year** (arrived or left mid-year, green card granted or surrendered mid-year, residency starting or ending date in the year). The return is Form 1040 or 1040-NR depending on status on December 31, with the other form attached as a statement; standard deduction, joint filing, head of household, EIC, and education credits are barred; and Pub. 519 says dual-status returns for 2025 cannot be e-filed. Tell the user this is a dual-status year, list those consequences, and ask whether they want a CPA. Do not draft a dual-status return with this skill.
- **Treaty tie-breaker** for someone who is a U.S. resident under the Code but a resident of the treaty country under the treaty: the skill can identify the position and the Form 8833 requirement, but the residency article analysis goes to a CPA.
- **Expatriates** (Schedule OI item D answered Yes): special rules and Form 8854 may apply (Pub. 519, chapter 4). Ask before going further.

---

## Prerequisites

Before producing anything, collect these inputs. If any is missing, ask for it explicitly and stop until it is answered. Never fill a default.

1. **Tax year.** This skill's numbers are for 2025 returns filed in 2026.
2. **Identity.** Legal name, foreign and U.S. addresses, SSN or ITIN. If neither exists, the return goes with Form W-7 ([`../form-w7/SKILL.md`](../form-w7/SKILL.md)) and must be paper filed.
3. **Citizenship and tax residence.** Every country of citizenship (Schedule OI item A) and the country where the user claimed tax residence (item B).
4. **Immigration history.** Visa type or status on December 31, any change of status with date (items E, F), any green card application ever (item C: Forms I-485, DS-230, DS-260), ever a U.S. citizen or green card holder (item D).
5. **Day counts.** Every entry and exit date in the tax year (item G) and total days present in the tax year and the two prior years (item H). For F, J, M, or Q holders: the visa held in each of the six prior years and in which years they were exempt.
6. **Marital status** and, if married, whether the spouse is a U.S. citizen or resident.
7. **Income documents**: Forms W-2, 1042-S (income code, rate, chapter 3 exemption code, box 10 withholding), 1099 series, SSA-1042S, RRB-1042S, 8805, 8288-A, Schedules K-1 and K-3, brokerage realized-gain reports with dates, rental ledgers.
8. **U.S. business facts**: office or fixed place of business, employees, dependent agents, LLC ownership and classification, personal services performed in the U.S. (days, pay, payer).
9. **Treaty facts**: residence country under the treaty, the article claimed, months claimed in prior years, whether Form 8233 or W-8BEN was given to the payer, any Competent Authority letter.
10. **Deduction facts**: state and local income tax paid on effectively connected income, gifts to U.S. charities (with acknowledgments for $250+ gifts), federally declared disaster losses, and for Indian students or business apprentices, eligibility under Article 21(2) of the U.S.–India treaty.
11. **Social security coverage**: if there is self-employment income, the home country and any certificate of coverage under a totalization agreement.
12. **Payments**: estimated tax payments with dates (Form 1040-ES (NR)), amount paid with Form 4868, tax paid with Form 1040-C.
13. **Prior returns**: whether a U.S. return was filed for the prior year and which form (item I; also drives the 16-month rule).
14. **Refund delivery**: U.S. bank account for direct deposit, or the foreign address for a paper check (line 35e).

---

## Workflow

Execute in order. Each step is a decision point; record the answer and its source.

### Step 1 — Confirm the year and revision

Confirm the tax year and that the 2025 form and instructions are the ones in use. For any other year, re-verify every line and number against that year's PDFs before continuing.

### Step 2 — Determine residency

Load [`references/residency-tests.md`](./references/residency-tests.md) and run it in this order:

1. **Green card test.** A lawful permanent resident at any time in the year is a resident; route to form-1040 (or the dual-status boundary).
2. **Substantial presence test** (IRC §7701(b)(3)). Resident if present at least **31 days** in the current year and at least **183 days** using all current-year days + 1/3 of first-prior-year days + 1/6 of second-prior-year days. Any part of a day counts. Compute with exact fractions and show the sum. Pub. 519's own example: 120 days in each of 2025, 2024, and 2023 gives 120 + 40 + 20 = 180, so the test is not met. When the total lands within a few days of 183, ask for the passport stamps or the CBP I-94 travel history before relying on the user's estimate.
3. **Excluded days**: regular commuters from Canada or Mexico, in transit under 24 hours, foreign-vessel crew, medical condition that arose in the U.S., NATO visa members, and exempt individuals (A or G visa other than A-3/G-5; J or Q teachers and trainees; F, J, M, or Q students; athletes at charitable events). Exempt status has limits: a teacher or trainee is not exempt if exempt for any part of 2 of the preceding 6 years; a student is not exempt after more than 5 calendar years unless they show no intent to reside permanently. Excluding days as a student, teacher, trainee, athlete, or for a medical condition requires **Form 8843**.
4. **Closer connection exception** (fewer than 183 days this year, tax home and closer connection abroad, no green card application) requires **Form 8840**.
5. **Treaty tie-breaker** for dual residents: Form 1040-NR with **Form 8833**. Boundary: confirm with a CPA.
6. **Dual-status check.** If status changed during the year, stop at the boundary above.

Write the result as one line: "Nonresident alien for all of 2025 because …", with the computation.

### Step 3 — Confirm the filing requirement and due date

Use Table A of the instructions. A nonresident must file if engaged in a U.S. trade or business at any time in the year (even with no income, no U.S.-source income, or only treaty-exempt income), or if not engaged but Schedule NEC income was not fully covered by withholding, plus the special-tax cases in Table A. The three exceptions (F/J/M/Q with no taxable income; India Article 21(2) students and apprentices with gross income up to $15,750 single / $31,500 QSS; partners in a U.S. partnership not engaged in a trade or business with only NEC-type income) still leave a refund reason to file.

Due date (Instructions for Form 1040-NR, "When and Where Should You File?"; IRC §6072(c)):

- **April 15, 2026** if the user received wages as an employee subject to U.S. income tax withholding.
- **June 15, 2026** otherwise.
- Form 4868 extends to October 15, 2026, or to December 15, 2026 for the June 15 group (Pub. 519, chapter 7). An extension never extends payment.
- Deductions and credits are allowed only on a timely, true, and accurate return: filed within **16 months** of the due date if the prior-year return was filed or this is the first year a return is required (Treas. Reg. §1.874-1(b); IRC §874(a)). Check this date for every late return.

If the only reason to file is a refund of chapter 3 or 4 withholding and the user had no U.S. trade or business, use the **Simplified Procedure for Claiming Certain Refunds** in the instructions (page 1 identity, Schedule NEC, lines 23a–35e, Schedule OI, signature, and the Form 1042-S copies).

### Step 4 — Classify every income item

Load [`references/eci-vs-fdap.md`](./references/eci-vs-fdap.md). Decide first whether the user was engaged in a U.S. trade or business (personal services in the U.S. usually are; trading securities for one's own account through a U.S. broker is not; a single-member LLC with a U.S. office, employees, or dependent agent usually is). Then place each item in exactly one bucket:

| Bucket | Where it goes | Tax |
|---|---|---|
| Effectively connected (ECI) | Form 1040-NR page 1 and Schedules 1, C, D, E (only the ECI part) | Graduated rates after deductions |
| U.S.-source, not effectively connected (FDAP and similar) | Schedule NEC lines 1–12, column by rate | 30% or treaty rate on the gross amount, no deductions |
| Treaty-exempt | Schedule OI item L, total on line 1k only | None |
| Exempt by statute, not reported | U.S. bank deposit interest, portfolio interest, NEC capital gains when present fewer than 183 days | None |
| U.S. real property dispositions | Schedule D (Form 1040) and line 7a, with Form 8288-A on line 25f | Graduated (treated as ECI) |

When an item could go in two buckets, ask a tight question, for example: "Was the $6,200 of consulting paid for work you performed while physically in the U.S., or from abroad? Only the U.S. days are U.S.-source."

### Step 5 — Settle treaty positions

Load [`references/treaty-claims.md`](./references/treaty-claims.md). For each claimed benefit, record country, article, months claimed in prior years, amount, whether the payer already applied it on Form 1042-S, and whether Form 8833 is required or waived (Treas. Reg. §301.6114-1(c)). Failure to file a required Form 8833 carries a **$1,000** penalty per failure for individuals (IRC §6712). If the payer did not have Form 8233 or W-8BEN, attach the statement the instructions require.

### Step 6 — Build page 1 (effectively connected income)

Run sibling skills for the ECI pieces only: [`../schedule-c/SKILL.md`](../schedule-c/SKILL.md) (ECI income and expenses only), [`../schedule-e/SKILL.md`](../schedule-e/SKILL.md) (rentals under a §871(d) election), [`../form-8949/SKILL.md`](../form-8949/SKILL.md) and [`../schedule-d/SKILL.md`](../schedule-d/SKILL.md) (ECI gains and U.S. real property), [`../schedule-1/SKILL.md`](../schedule-1/SKILL.md). Import their bottom lines; do not invent them. Sum line 9 and line 11a.

### Step 7 — Deductions

- **Line 12**: Schedule A (Form 1040-NR) total, or the standard deduction only for students and business apprentices eligible under Article 21(2) of the U.S.–India treaty (Pub. 519 Worksheet 5-1: $15,750 single or MFS, $31,500 QSS for 2025). Everyone else: itemize or enter 0.
- **Line 13a**: QBI deduction, only for effectively connected qualified business income ([`../form-8995/SKILL.md`](../form-8995/SKILL.md) or [`../form-8995-a/SKILL.md`](../form-8995-a/SKILL.md); Form 8995 applies when taxable income before QBI is at or below $197,300, or $394,600 MFJ, for 2025).
- **Line 13b**: estates and trusts only; individuals enter nothing.
- **Line 13c**: Schedule 1-A (tips, overtime, seniors). The 1040-NR instructions say nonresident aliens generally are not eligible for the car loan interest deduction.

### Step 8 — Tax

- **Line 16**: Tax Table if line 15 is under $100,000, otherwise the Tax Computation Worksheet, in the 2025 Instructions for Form 1040. Columns available: Single, Married filing separately (Section C), Qualifying surviving spouse (Section B, the MFJ column). A married nonresident uses MFS unless one of the narrow Single exceptions applies.
- **Line 23a**: Schedule NEC line 15.
- **Line 23b**: Schedule 2 line 21. Self-employment tax appears only if a totalization agreement places the user in the U.S. social security system (Instructions for Schedule 2, line 4). Ask for the certificate of coverage; never assume either way.
- **Line 23c**: 4% transportation tax, rare.

### Step 9 — Credits and payments

Child tax credit and credit for other dependents only for U.S. nationals and residents of Canada or Mexico, and in limited form residents of South Korea and India Article 21(2) students (line 19 exception). No EIC (line 27 is reserved). Payments: line 25a–25c (W-2, 1099, other), 25e (8805), 25f (8288-A), 25g (1042-S box 10), 26 (estimated tax, prior-year overpayment), 29 (Form 1040-C).

### Step 10 — Refund or balance due

Lines 34–38. Refunds of tax shown on Forms 1042-S, 8805, or 8288-A can take up to 6 months. Estimated tax penalty on line 38 runs through [`../form-2210/SKILL.md`](../form-2210/SKILL.md); a filer without wages subject to withholding pays estimates in three installments (1/2, 1/4, 1/4) per Form 1040-ES (NR).

### Step 11 — Schedule OI

Answer every item A through M. Item H day counts must match the Step 2 computation. Item L total must equal line 1k. Item M records a §871(d) real property election.

### Step 12 — Validate, output, hand off

Run **Validation**, emit the **Output format**, then list the companion filings (Form 8843, 8840, 8833, W-7, the LLC's Form 5472 with pro forma Form 1120, state nonresident returns, next year's Form 1040-ES (NR)). If the user wants help filing, follow [`filing.md`](./filing.md).

---

## Line-by-line guidance

Full map: [`references/line-by-line.md`](./references/line-by-line.md). Key rules:

### Header

- Tax year boxes; special boxes: filed pursuant to section 301.9100-2, combat zone, deceased (with date), Other.
- Identifying number: SSN or ITIN. Estates and trusts use an EIN.
- Filing status: Single, Married filing separately, Qualifying surviving spouse, Estate, Trust. No MFJ, no head of household. Married persons check MFS even if not separated, except married residents of Canada, Mexico, or South Korea, married U.S. nationals, and India Article 21(2) students and apprentices who meet all five "lived apart with a child" tests, who check Single. QSS only for those same groups and only if they were a resident alien or U.S. citizen in the year the spouse died.
- Digital assets question: answer Yes or No for every filer.
- Dependents: only U.S. nationals and residents of Canada and Mexico on the Form 1040 terms; South Korea residents and India Article 21(2) students on the limited Pub. 519 terms; nobody else.

### Page 1 (lines 1a–11a): effectively connected income only

- 1a: W-2 box 1 wages that are U.S.-source and effectively connected; treaty-exempt wages move to 1k. Wages for days worked in and out of the U.S. are sourced by days (U.S. workdays ÷ total workdays × pay).
- 1b–1h as on Form 1040; 1i and 1j reserved; **1k** treaty-exempt income from Schedule OI item L(1)(e), never repeated elsewhere; **1z** = 1a through 1h (1k excluded).
- 2a/2b, 3a/3b, 4a/4b, 5a/5b: effectively connected amounts only; the non-ECI U.S.-source versions go to Schedule NEC lines 1, 2, 7.
- 6 reserved. 7a capital gain from Schedule D (ECI and U.S. real property). 8 Schedule 1 line 10. **9** = 1z + 2b + 3b + 4b + 5b + 7a + 8. 10 Schedule 1 line 26. **11a** = 9 − 10.

### Page 2 (lines 11b–38)

- 12 deduction as in Step 7; 13a QBI; 13b estates and trusts; 13c Schedule 1-A line 38; **14** = 12 + 13a + 13b + 13c; **15** = 11b − 14, not below 0.
- 16 tax; 17 Schedule 2 line 3; 18 = 16 + 17; 19 CTC/ODC (eligible residents only); 20 Schedule 3 line 8; 21 = 19 + 20; 22 = 18 − 21, not below 0.
- 23a Schedule NEC line 15; 23b Schedule 2 line 21; 23c transportation tax; 23d = 23a + 23b + 23c; **24** = 22 + 23d.
- 25a–25c withholding; 25d sum; 25e Form 8805; 25f Form 8288-A; 25g Form 1042-S; 26 estimated payments; 27 reserved; 28 ACTC; 29 Form 1040-C; 30 refundable adoption credit; 31 Schedule 3 line 15; 32 = 28 + 29 + 30 + 31; **33** = 25d + 25e + 25f + 25g + 26 + 32.
- 34 overpaid; 35a refund (35b–35d direct deposit; 35e foreign mailing address); 36 applied to 2026 estimates; 37 amount owed; 38 estimated tax penalty.
- Third party designee phone must be a U.S. number. An agent may sign only in the listed cases (ill, injured, outside the U.S. for the 60 days before the due date, or IRS-approved reasons), with Form 2848 attached.

### Schedule NEC

Columns (a) 10%, (b) 15%, (c) 30%, (d) other rate (use for treaty rates, including 0%). Lines 1a–1c dividends and dividend equivalents, 2a–2c interest, 3–5 royalties, 6 real property income and natural resource royalties (unless the §871(d) election moved it to page 1), 7 pensions and annuities, 8 social security (85% of SSA-1042S box 5), 9 capital gain from line 18, 10a–10c gambling for Canada residents, 11 gambling for others (winnings only), 12 other; 13 column totals; 14 = 13 × column rate; **15** = sum of line 14 → Form 1040-NR line 23a. Lines 16–18 report U.S.-source capital gains and losses not effectively connected, **only if present 183 days or more** (IRC §871(a)(2)); no loss carryover; net loss → 0.

### Schedule A (Form 1040-NR)

1a state and local income taxes on ECI; 1b smaller of 1a or **$40,000 ($20,000 MFS)**, reduced when line 11b exceeds $500,000 ($250,000 MFS) but not below $10,000 ($5,000 MFS); 2–4 gifts to U.S. charities and carryover; 5 = 2 + 3 + 4; 6 federally declared disaster casualty losses (Form 4684 line 18); 7 other listed items; **8** = 1b + 5 + 6 + 7 → line 12. No mortgage interest, no medical expenses, no property tax line.

### Schedule P

Only for transfers of partnership interests subject to §864(c)(8) or §897(g); data comes from Schedule K-3 Part XIII. If it applies, draft Part I and flag Part II for CPA review.

---

## Validation

Surface every failure; never fix silently.

### Math checks

- [ ] 1z = 1a + 1b + 1c + 1d + 1e + 1f + 1g + 1h (line 1k excluded)
- [ ] 9 = 1z + 2b + 3b + 4b + 5b + 7a + 8; 11a = 9 − 10; 11b = 11a
- [ ] 14 = 12 + 13a + 13b + 13c; 15 = max(0, 11b − 14)
- [ ] 16 matches the Tax Table row or TCW section for the checked filing status
- [ ] 18 = 16 + 17; 21 = 19 + 20; 22 = max(0, 18 − 21); 23d = 23a + 23b + 23c; 24 = 22 + 23d
- [ ] 25d = 25a + 25b + 25c; 32 = 28 + 29 + 30 + 31; 33 = 25d + 25e + 25f + 25g + 26 + 32
- [ ] At most one of 34 or 37 is positive; 35a + 36 = 34
- [ ] Schedule NEC: each column's line 14 = line 13 × that column's rate; line 15 = sum of line 14 = Form 1040-NR line 23a; line 9 = line 18
- [ ] Schedule A: 1b ≤ cap; 5 = 2 + 3 + 4; 8 = 1b + 5 + 6 + 7 = line 12
- [ ] Schedule OI item L(1)(e) = line 1k; item H matches the Step 2 day count

### Residency and classification checks

- [ ] Substantial presence computation shown with exact fractions and the 31-day test
- [ ] Every excluded day backed by Form 8843 (or 8840 for closer connection)
- [ ] No dual-status facts (arrival or departure that changed status in the year)
- [ ] Every income item assigned to exactly one bucket; nothing treaty-exempt also appears on 1a–8 or NEC
- [ ] No U.S. bank deposit interest or portfolio interest taxed by mistake; no NEC capital gains taxed when present fewer than 183 days

### Sanity checks (warn, do not block)

- [ ] Line 12 standard deduction used without India Article 21(2) eligibility → error
- [ ] MFJ or HOH anywhere, line 27 filled, or CTC claimed by an ineligible resident → error
- [ ] Married filer using the Single column without meeting the exception → error
- [ ] Line 23b SE tax without a totalization determination, or a certificate showing U.S. coverage with no SE tax → ask
- [ ] Form 1042-S box 10 not on line 25g, or 8805/8288-A credits without the forms attached
- [ ] Return date later than 16 months after the due date → deductions at risk (Treas. Reg. §1.874-1(b))
- [ ] Foreign-owned single-member LLC: Form 5472 with pro forma Form 1120 on the to-do list
- [ ] State nonresident return possibly required (states do not all follow treaties)

---

## Output format

```markdown
# Form 1040-NR — DRAFT for tax year 2025 (filed in 2026)

## Residency determination
- Green card test: No
- Substantial presence: 2025 days X + 2024 days Y/3 + 2023 days Z/6 = N (31-day test: pass|fail) → resident|nonresident
- Excluded days: <category, count, Form 8843|8840>
- Conclusion: Nonresident alien for all of 2025 because <reason>
- Due date: April 15, 2026 | June 15, 2026 (reason); 16-month deadline: <date>

## Header
Name / identifying number (SSN | ITIN | blank with Form W-7 attached) / address / foreign address
Filing status: Single | MFS | QSS     Special boxes: <none|...>     Digital assets: Yes|No
Dependents: <none|eligible residents only>

## Page 1 — Effectively connected income
1a … 1h, 1k, 1z, 2a, 2b, 3a, 3b, 4a, 4b, 5a, 5b, 6 (reserved), 7a, 8, 9, 10, 11a
(every line with an amount, including $0)

## Page 2 — Tax and payments
11b, 12, 13a, 13b, 13c, 14, 15, 16 (method: Table|TCW, column), 17 … 38 (every line, including $0)

## Schedule NEC
| Line | Item | (a) 10% | (b) 15% | (c) 30% | (d) __% |
| 13 | Totals | | | | |
| 14 | Tax | | | | |
15. Total → 1040-NR line 23a: $X
16–18 (capital gains): <detail|"not taxable: present fewer than 183 days">

## Schedule A (Form 1040-NR)  (or "Not filed: standard deduction under U.S.–India treaty Art. 21(2)" | "Not filed: no allowable deductions")
1a, 1b, 2, 3, 4, 5, 6, 7 (itemized list), 8

## Schedule OI
A … M, each answered; item L table (country, article, months, amount, total = line 1k)

## Schedule P  (or "Not applicable: no partnership interest transferred")

## Attachments and companion filings
- [ ] Forms W-2, 1042-S, SSA-1042S, RRB-1042S, 8288-A (front); 8805 (back); 1099-R if tax withheld
- [ ] Form 8843 | 8840 | 8833 | W-7 | Schedule 1, 2, 3, 1-A, C, D, E, 8995 as applicable
- [ ] Separate: LLC Form 5472 + pro forma 1120; state nonresident return; Form 1040-ES (NR) for 2026

## Validation summary
- Math: all checks passed | <failures>
- Classification: <items needing review>
- Sanity: <warnings>

## Sources cited in this draft
- 2025 Form 1040-NR and Schedules NEC, OI, A, P; Instructions for Form 1040-NR (2025)
- 2025 Instructions for Form 1040 (Tax Table / Tax Computation Worksheet)
- Pub. 519 (2025); IRC §§7701(b), 871, 874, 6072(c); Treas. Reg. §1.874-1(b)
- <treaty article(s); Form 8833 instructions; any other authority used>
```

The draft is not the filed return. Every line is computed and traceable so a CPA can review it without re-deriving the math.

---

## References

- [`references/line-by-line.md`](./references/line-by-line.md) — every line of Form 1040-NR (2025) and Schedules NEC, OI, A, and P, from the PDF text
- [`references/residency-tests.md`](./references/residency-tests.md) — green card test, substantial presence formula, exempt individuals and Form 8843, closer connection and Form 8840, treaty tie-breaker, dual-status boundary
- [`references/eci-vs-fdap.md`](./references/eci-vs-fdap.md) — U.S. trade or business, effectively connected income, Schedule NEC categories and rates, statutory exemptions, §871(d) real property election, FIRPTA, foreign-owned single-member LLCs, self-employment tax and totalization
- [`references/treaty-claims.md`](./references/treaty-claims.md) — Schedule OI item L and line 1k, Form 8833 required vs waived, Form 8233 statements, India Article 21(2) standard deduction
- [`references/common-mistakes.md`](./references/common-mistakes.md) — frequent errors with the rule that each one breaks
- [`filing.md`](./filing.md) — e-file vs paper decision tree, mailing addresses, W-7 packages, payment from abroad, consent and security rules

## Examples

- [`examples/f1-student-india-treaty.md`](./examples/f1-student-india-treaty.md) — F-1 student from India, on-campus wages, Article 21(2) standard deduction, Form 8843, refund of withholding
- [`examples/foreign-founder-llc-eci.md`](./examples/foreign-founder-llc-eci.md) — married German resident who owns a U.S. single-member LLC with a U.S. office: Schedule C ECI, Schedule A (NR), QBI limit, MFS rates, 15% treaty dividends on Schedule NEC, no SE tax under a certificate of coverage, Form 5472 boundary
- [`examples/rental-condo-871d-election.md`](./examples/rental-condo-871d-election.md) — Brazilian resident with a Miami rental condo making the §871(d) net-basis election, first return with Form W-7, refund of 30% withholding

## Sources

Re-verify each item against irs.gov for the year being filed.

- [Form 1040-NR Instructions 2026 (Jupid blog)](https://jupid.com/blog/form-1040-nr-instructions-2026) — narrative companion for human readers
- [Form 1040-NR (2025)](https://www.irs.gov/pub/irs-pdf/f1040nr.pdf) and [Instructions for Form 1040-NR (2025)](https://www.irs.gov/pub/irs-pdf/i1040nr.pdf)
- [Schedule NEC](https://www.irs.gov/pub/irs-pdf/f1040nrn.pdf), [Schedule OI](https://www.irs.gov/pub/irs-pdf/f1040nro.pdf), [Schedule A (Form 1040-NR)](https://www.irs.gov/pub/irs-pdf/f1040nra.pdf), [Schedule P](https://www.irs.gov/pub/irs-pdf/f1040nrp.pdf)
- [About Form 1040-NR](https://www.irs.gov/forms-pubs/about-form-1040-nr) — revision history and updates
- [2025 Instructions for Form 1040](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — Tax Table and Tax Computation Worksheet
- [Publication 519, U.S. Tax Guide for Aliens (2025)](https://www.irs.gov/pub/irs-pdf/p519.pdf)
- [Form 8843 (2025)](https://www.irs.gov/pub/irs-pdf/f8843.pdf), [Form 8840 (2025)](https://www.irs.gov/pub/irs-pdf/f8840.pdf), [Form 8833 (Rev. 12-2022)](https://www.irs.gov/pub/irs-pdf/f8833.pdf)
- [Form 1040-ES (NR) (2026)](https://www.irs.gov/pub/irs-pdf/f1040esn.pdf); [Instructions for Form 8995 (2025)](https://www.irs.gov/pub/irs-pdf/i8995.pdf); [Instructions for Form W-7 (Rev. 12-2024)](https://www.irs.gov/pub/irs-pdf/iw7.pdf)
- [Tax treaty tables](https://www.irs.gov/individuals/international-taxpayers/tax-treaty-tables) (Table 1, Rev. May 2023) and [U.S. income tax treaties A to Z](https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z)
- IRC §7701(b) (residency), §864(b)–(c) (trade or business, ECI), §871(a), (b), (d) (30% tax, graduated tax, real property election), §874(a) (deductions only on a timely return), §897 and §1445 (FIRPTA), §6072(c) (June 15 due date), §6114 and §6712 (treaty disclosure and $1,000 penalty)
- Treas. Reg. §1.874-1(b) (16-month rule), §301.7701(b)-2 (closer connection), §301.7701(b)-7 (dual-resident taxpayers), §301.6114-1 (treaty-based return positions)
- [SSA international social security agreements](https://www.ssa.gov/international/agreements_overview.html) — totalization agreements

## Disclaimer

This skill encodes procedural guidance from public IRS forms, instructions, and publications. It is not tax, legal, or immigration advice and does not create a CPA-client relationship. Residency, trade-or-business status, and treaty positions are fact-specific; remind the user that the draft is a starting point and that dual-status years, tie-breaker claims, and expatriation questions need a licensed cross-border tax professional.
