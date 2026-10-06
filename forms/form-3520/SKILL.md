---
name: form-3520
description: >
  Use this skill when a US person (citizen, resident, domestic corporation,
  partnership, estate, or non-grantor trust) needs to report transactions with
  a foreign trust or the receipt of large gifts/bequests from foreign persons.
  Triggers on phrases like "Form 3520", "foreign trust reporting", "received
  inheritance from abroad", "foreign gift over $100,000", "foreign trust
  beneficiary", "transferred money to a foreign trust", "I'm the US owner of a
  foreign trust", "got a bequest from my parents in [country]". Do NOT use for:
  foreign bank account reporting (use FinCEN 114 / FBAR), foreign financial
  asset reporting (use Form 8938), the foreign trust's own annual return (use
  Form 3520-A — filed BY the trust, not by the US person), or domestic trust
  reporting (use Form 1041).
form: Form 3520 (Annual Return To Report Transactions With Foreign Trusts and Receipt of Certain Foreign Gifts)
audience: [foreign, individual]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f3520.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i3520.pdf
---

# Form 3520 — Annual Return To Report Transactions With Foreign Trusts and Receipt of Certain Foreign Gifts

This skill produces an audit-grade draft of Form 3520 for a US person who:
(1) created or transferred property to a foreign trust, (2) is treated as the
US owner of a foreign trust under the grantor trust rules, (3) received a
distribution from a foreign trust, or (4) received aggregate gifts/bequests
above the reporting threshold from foreign individuals or foreign
entities/estates during the tax year.

The form has four parts and the part(s) you fill depend on which trigger
applies. The skill walks the agent through identifying which Part(s) apply,
collecting the inputs each Part needs, applying the IRC §6048 / §6039F /
§679 rules, and emitting a deliverable the user can transcribe to the IRS
fillable PDF and mail to Ogden.

**Form revision.** The line map in this skill was verified on 2026-10-06
against Form 3520 (Rev. December 2023) and the Instructions for Form 3520
(Rev. December 2025, continuous-use for tax year 2025 and later). Before
use, check https://www.irs.gov/forms-pubs/about-form-3520 for a newer
revision and re-check the line numbers if one exists.

The math is mechanical. The judgment is in (a) deciding whether the foreign
trust is a grantor trust as to the US person, (b) classifying a foreign
"distribution" vs. a "gift" when it comes from a foreign person who controls
a foreign entity, and (c) determining whether the throwback / accumulation
distribution rules of IRC §§665–668 apply to a distribution from a foreign
non-grantor trust. The skill instructs the agent to ASK rather than guess on
each of these.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 3520, "foreign trust reporting", "foreign
  gift reporting", or "received inheritance from abroad"
- The user transferred cash, property, or services to a foreign trust during
  the tax year (gratuitous transfer or sale at less than FMV)
- The user is treated as the owner of any portion of a foreign trust under
  the grantor trust rules (IRC §§671–679, in particular §679 for transfers
  by US persons)
- The user received any distribution (cash, property, or use of property)
  from a foreign trust — including loans from a foreign trust, which are
  treated as distributions under IRC §643(i) unless they are "qualified
  obligations"
- The user received gifts or bequests during the tax year from a foreign
  person: more than $100,000 from a nonresident alien individual or a
  foreign estate (aggregating donors known to be related to each other),
  OR more than the §6039F threshold from foreign corporations or foreign
  partnerships ($20,116 for 2025 under Rev. Proc. 2024-40 §2.48; $20,573
  for 2026 under Rev. Proc. 2025-32 §4.47)

Do **not** engage this skill when:

- The user only needs to report a foreign bank or securities account → use
  FinCEN Form 114 (FBAR), filed separately with FinCEN, not the IRS
- The user holds foreign financial assets above the §6038D thresholds →
  Form 8938 attaches to Form 1040 (separate filing; many filers must do
  both 8938 and 3520)
- The user IS the foreign trust (or its US agent) filing the trust's annual
  information return → that is Form 3520-A, filed BY the trust, due
  March 15 (or extended via Form 7004); see [`references/3520-vs-3520-a.md`](./references/3520-vs-3520-a.md)
- The trust is a domestic trust → Form 1041
- The user owns an interest in a foreign corporation or partnership →
  Form 5471 (CFC) or Form 8865 (foreign partnership), not 3520
- The user owns a 25%-foreign-owned US corporation or a foreign-owned
  disregarded entity → use the [`form-5472`](../form-5472/SKILL.md) skill

If the user's situation is ambiguous (e.g., a "foundation" abroad that may
or may not be a trust under US law; a "loan" from a relative abroad that
may be a disguised gift or distribution), ask before proceeding. Foreign
classification is fact-intensive; the wrong classification produces a
correctly-filled wrong form.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are
missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the return covers. Form 3520 follows the calendar/tax year
   of the US filer (the taxpayer's tax year — calendar year for individuals).
2. **Filer identity**: legal name, SSN/ITIN/EIN, mailing address, country of
   citizenship, US tax residency status. If the user files a joint income
   tax return and both spouses are transferors, grantors, or beneficiaries
   of the same foreign trust, ask whether they will file a joint Form 3520
   (line 1i; Instructions, Joint Returns) or separate forms. Ask whether the
   user lives and works outside the United States (June 15 due date, line
   1j) and whether an income tax return extension was requested (line 1k).
3. **Identify which Part(s) apply** — Parts I, II, III, IV. Do this with
   the user explicitly:
   - **Part I** — Created a foreign trust this year, or transferred property
     to a foreign trust this year, or held an outstanding obligation from a
     "related" foreign trust treated as a transfer
   - **Part II** — US owner of any portion of a foreign trust at any point
     during the tax year (grantor trust rules, especially §679)
   - **Part III** — Received a distribution from a foreign trust during the
     tax year (cash, property, use of property, or a non-qualified loan)
   - **Part IV** — Received gifts/bequests from foreign person(s) above
     thresholds during the tax year
4. For **Part I** — date of trust creation; trust name, address, country,
   trust EIN if any; identification of trustee(s); description of all
   property transferred (cash + FMV of property) with dates; any obligations
   received in exchange and their terms; copy of trust instrument if
   available
5. For **Part II** — trust identifying details; every person treated as
   an owner and the Code section (line 20); whether the trust filed Form
   3520-A and sent the Foreign Grantor Trust Owner Statement (pages 3 and
   4 of Form 3520-A) — if not, the data for a substitute Form 3520-A; trust's income, expenses,
   and distributions for the year; FMV of trust assets at year-end; list of
   beneficiaries who received distributions
6. For **Part III** — name of foreign trust; whether the trust is a grantor
   trust with a US owner (treated differently from a non-grantor foreign
   trust); date and FMV of each distribution; whether the trust provided a
   Foreign Nongrantor Trust Beneficiary Statement (allows actual-method
   reporting) or a Foreign Grantor Trust Beneficiary Statement; whether
   Schedule A (default) was used for this trust in any earlier year (once
   used, it must keep being used); if no statement, the default method
   needs the number of years the trust has been foreign and the
   distributions of the 3 preceding years, and Form 4970 needs the user's
   taxable income for the 5 preceding years
7. For **Part IV** — for each gift or bequest: donor type (nonresident
   alien individual, foreign estate, foreign corporation, foreign
   partnership), whether donors are related to each other, date,
   description and FMV; for corporate/partnership donors also the donor's
   name, address, and TIN (line 55 asks for them; line 54 does not); and
   whether any donor acted as a nominee for someone else (line 56)

For currency translation, ask the user which exchange-rate source they want
to use. Form 3520 requires all amounts in U.S. dollars but does not
prescribe a rate. Common choices: the spot rate on each transaction date,
or the IRS yearly average rates
(https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates)
for items spread across the year. Document the choice and be consistent
within the return.

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm the filer is a "US person"

A US person for Form 3520 purposes is a US citizen, US resident alien (green
card or substantial presence), domestic partnership, domestic corporation,
domestic estate, or domestic non-grantor trust (Form 3520 Instructions,
"Who Must File"). If the user is none of these, Form 3520 doesn't apply.

A common edge case: a non-resident alien who became a US tax resident
mid-year. They are a US person from the residency starting date forward;
transactions before the start date aren't reportable on Form 3520. Ask for
the residency start date.

### Step 2 — Determine which Part(s) apply

Walk the four triggers explicitly. The user can have multiple Parts on a
single Form 3520 (e.g., a US owner of a foreign trust who also receives a
distribution files both Part II and Part III).

If only Part IV applies (gift/bequest reporting), lines 2–4 and Parts
I–III stay blank. If the user deals with two foreign trusts, file a
separate Form 3520 for each trust.

### Step 3 — Run threshold checks for Part IV

Part IV thresholds (Parts I–III have no de minimis):

- **Nonresident alien individuals + foreign estates** (line 54): more than
  **$100,000** treated as gifts or bequests during the year. Aggregate
  gifts from donors the user knows or has reason to know are related to
  each other, or where one acts as nominee for another (Instructions,
  Line 54). The $100,000 figure comes from the form and instructions
  (Notice 97-34), not from the statute, and is not inflation-adjusted.
- **Foreign corporations + foreign partnerships** (line 55, including
  foreign persons related to them): more than the **§6039F threshold** —
  $20,116 for 2025 (Rev. Proc. 2024-40 §2.48), $20,573 for 2026 (Rev. Proc.
  2025-32 §4.47). The instructions send filers to IRS.gov/InflationAdjustment
  for the current year's figure.

If line 54 applies, list each gift or bequest over $5,000 by date,
description, and FMV (line 54 does not ask for donor names). If none
exceeds $5,000, write "No gifts or bequests exceed $5,000" in column (b).
If line 55 applies, list every such gift with the donor's name, address,
TIN, and type. Gifts from foreign corporations or partnerships can be
recharacterized by the IRS under §672(f)(4), and an unreported gift lets
the IRS determine its tax consequences (§6039F(c)(1)(A)).

### Step 4 — Collect and structure the data per applicable Part

For each Part the user is filing, build a structured table the agent can
walk line by line. Templates in [`references/line-by-line.md`](./references/line-by-line.md) (Parts I–IV).

Examples of what to extract:

```
| Gift (Part IV line 54)        | Donor type  | Date       | FMV (USD) |
|-------------------------------|-------------|------------|-----------|
| Cash from grandmother         | NRA indiv.  | 2026-08-12 | $200,000  |

| Gift (Part IV line 55)        | Donor                    | Date       | FMV (USD) |
|-------------------------------|--------------------------|------------|-----------|
| Cash                          | Rossi S.r.l. (foreign corp.) | 2026-09-30 | $25,000 |

| Distribution (Part III)       | Trust           | Date       | FMV (USD) | Line |
|-------------------------------|-----------------|------------|-----------|------|
| Cash distribution             | UK Family Trust | 2026-04-15 | $42,000   | 24   |
| Use of London flat (1 mo)     | UK Family Trust | 2026-07    | $4,800    | 25   |
```

### Step 5 — For Part III, determine reporting method

If the user received an amount from a portion of the trust the user is
treated as **owning** (Part II): complete only lines 24 and 27.

If the trust is a **foreign grantor trust owned by someone else** and the
user received a complete Foreign Grantor Trust Beneficiary Statement:
check "Yes" on line 29, attach it, and stop for that distribution (it is
treated as coming directly from the owner, e.g., a gift).

If the trust is a **foreign nongrantor trust**, the distribution may carry
out the trust's current income plus an "accumulation distribution" (prior
undistributed net income, UNI) subject to the §667 tax and the §668
interest charge.

- With a complete **Foreign Nongrantor Trust Beneficiary Statement** (line
  30 "Yes"): use Schedule B (actual calculation, lines 39–47) — or
  Schedule A if Schedule A was used for this trust in any earlier year
  (consistency rule; only exception is the termination year).
- Without a statement: **Schedule A, default calculation** (lines 31–38).
  The part of the year's distributions up to 125% of the average of the 3
  preceding years' distributions (line 35) is ordinary income for the
  current year (line 36); the rest is an accumulation distribution (line
  37). Line 38 = years the trust has been foreign ÷ 2.
- If line 37 or 41a is above zero: **Schedule C** — compute the tax on
  Form 4970 (attached to Form 3520 as a worksheet), multiply it by the
  combined interest rate (IRS.gov/CombinedInterestRate table for
  calendar-year filers using June 30), and carry line 53 to the income
  tax return as additional tax.
- If the user receives repeated distributions without a statement,
  recommend asking the trustee for one. See
  [`references/throwback-default-method.md`](./references/throwback-default-method.md).

### Step 6 — For Part II, ensure Form 3520-A coordination

A US owner of a foreign trust must ensure a **Form 3520-A is filed by the
trust** for the same tax year: due the 15th day of the 3rd month after the
trust's year ends (March 15 for a calendar-year trust), extendable only by
a Form 7004 filed with the trust's EIN (an income tax return extension does
not extend Form 3520-A; Instructions for Form 3520-A).

If the foreign trust does not file its own 3520-A, the US owner must
complete a **substitute Form 3520-A** (with the Owner Statement, pages 3–4,
and the Beneficiary Statement, page 5), check the "Substitute Form 3520-A"
box at its top, sign it with the owner's name and TIN on the "Title" line,
and attach it to the owner's Form 3520 by the Form 3520 due date. Missing
it triggers the §6677(b) penalty: the greater of $10,000 or 5% of the gross
value of the portion owned.

If the user is the US owner and the trustee is uncooperative, the user must
file the substitute. Ask for the data needed.

### Step 7 — Currency translation

Translate foreign currency to USD consistently. Document the exchange rate
source and date(s) used in the deliverable. Form 3520 requires USD but
prescribes no rate; a dated transaction (gift, transfer, distribution) is
usually translated at the rate on that date, and items spread across the
year at a yearly average rate. Ask the user, and ask a CPA when the choice
moves an amount across the $100,000 or §6039F threshold.

### Step 8 — Compute totals per Part

- Part I: Schedule B line 13 totals of columns (c) and (i)
- Part II: line 23, gross value (FMV, liabilities disregarded) of the
  portion owned at year-end
- Part III: line 27 = line 24 column (f) + line 25 column (g); then
  Schedule A or B, and Schedule C if needed
- Part IV: line 54 / line 55 totals

### Step 9 — Run validation checks

See **Validation** below. Run every check.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next steps:

- **Form 3520 is filed separately from Form 1040** — it does NOT attach to
  the 1040. Mail to: Internal Revenue Service Center, P.O. Box 409101,
  Ogden, UT 84409 (Instructions for Form 3520, Rev. December 2025, When
  and Where To File). Only a complete Form 3520 with all required
  attachments is considered timely filed.
- **Due date** — the 15th day of the 4th month after the end of the
  filer's tax year (April 15 for a calendar-year individual; next business
  day if it falls on a weekend or legal holiday). A U.S. citizen or
  resident living and working outside the United States and Puerto Rico
  (or on military duty outside them) has until June 15 and checks line 1j
  with a statement. If the filer was granted an extension for the income
  tax return, Form 3520 is due by the 15th day of the 10th month (October
  15): check line 1k and enter the return's form number. The instructions
  note this due date "is not tied to the due date of the U.S. person's
  income tax return."
- **For a decedent or an estate**: the 15th day of the 4th month after the
  decedent's last tax year or the estate's tax year, extended to the 15th
  day of the 10th month if the income tax return was extended
- **If Part II applies**: confirm the foreign trust filed Form 3520-A (due
  March 15 for a calendar-year trust; Form 7004 with the trust's EIN to
  extend); if not, attach a substitute Form 3520-A
- **Penalties for failure to file or incomplete filing** (Instructions,
  Penalties; IRC §6677, §6039F):
  - Part I and Part III: the greater of $10,000 or 35% of the gross value
    of the property transferred / distributions received
  - Part II / Form 3520-A: the greater of $10,000 or 5% of the gross value
    of the portion of trust assets treated as owned
  - If the failure continues more than 90 days after the IRS mails a
    notice: an additional $10,000 for each 30-day period (or part); total
    §6677 penalties are capped at the gross reportable amount
  - Part IV gifts: 5% of the gift per month the failure continues, up to
    25% (§6039F(c)(1)(B)), and the IRS may determine the gift's tax
    consequences
  - Reasonable cause is a defense (§6677(d); §6039F(c)(2)); foreign-law
    penalties for disclosure, a reluctant foreign fiduciary, or trust
    terms that bar disclosure are not reasonable cause
  - A U.S. owner's 20% accuracy penalty can rise to 40% under §6662(j) for
    underpayments tied to assets that had to be reported on Form 3520-A
- **Information return, with one tax computation**: Part III Schedule C
  computes the tax and interest on an accumulation distribution (Form 4970
  as a worksheet attached to Form 3520); line 53 goes on the income tax
  return as additional tax (Form 1040: Schedule 2, Part II, "any other
  taxes" line). Line 36 ordinary income from the default method and actual-
  method income go on the user's income tax return.

### Step 12 — File the return (optional, if the user wants the agent to file)

The Instructions for Form 3520 (Rev. December 2025) give only the Ogden
mailing address; no electronic filing channel is described. See
[`filing.md`](./filing.md) for the paper filing playbook (assembly,
mailing, certified mail proof of timely filing, retention).

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md).
Key rules below (Form 3520, Rev. December 2023).

### Page 1 — identifying information

- **A / B / C** — Initial, final, or amended return; type of filer; item C
  only if this Form 3520 is counted on the filer's Form 8938 Part IV line
  15 (duplicative-reporting exception).
- **Four trigger boxes** — check each that applies; complete the matching
  Part(s).
- **Lines 1a–1k** — filer name, TIN, address, spouse's TIN (1d, joint
  filing only), joint Form 3520 box (1i), automatic 2-month extension box
  with statement (1j), income-tax-return extension box and form number
  (1k).
- **Lines 2a–2h** — foreign trust name, EIN, address, date created.
- **Line 3, 3a–3g** — U.S. agent; "No" with Part I means lines 15–18 too.
- **Lines 4a–4f** — U.S. decedent information for an executor.

### Part I — Transfers by U.S. Persons to a Foreign Trust (lines 5–19)

- **5a–5c** trust creator; **6a–6c** country codes and date created;
  **7a–7b** other persons treated as owner; **8** completed gift or bequest
  (Form 709 / 706 may apply); **9a–9b** U.S. beneficiary now or possible
  by amendment; **10** reserved.
- **Schedule A (11a–12)** — transfers to a related trust for obligations;
  qualified obligations (written; ≤ 5 years including renewals; all USD;
  yield 100%–130% of AFR; assessment-period extension agreed on line 12;
  status reported each year on line 19 / 28).
- **Schedule B (13–18)** — gratuitous transfers, columns (a)–(i); sale and
  loan documents (14); if no U.S. agent, beneficiaries, trustees, other
  powers, and trust documents (15–18).
- **Schedule C (19)** — qualified obligations outstanding.

### Part II — U.S. Owner of a Foreign Trust (lines 20–23)

- **20** — every owner: name, address, country of tax residence, TIN,
  Code section (e.g., 679).
- **21a–21c** — country codes and date created.
- **22** — did the trust file Form 3520-A? Yes: attach Owner Statement
  (pages 3–4). No: attach a substitute Form 3520-A.
- **23** — gross value (FMV, liabilities disregarded) of the portion owned
  at year-end.

### Part III — Distributions From a Foreign Trust (lines 24–53)

- **24** — distributions (cash and FMV of property), columns (a)–(f).
- **25–26** — loans of cash or marketable securities and uncompensated
  use of trust property from a related foreign trust (§643(i)): the amount
  treated as a distribution is column (a) minus the FMV of any qualified
  obligation; line 26 assessment-period agreement.
- **27** — total distributions; **28** — trust holds your qualified
  obligation.
- **29 / 30** — Foreign Grantor / Nongrantor Trust Beneficiary Statement
  received?
- **Schedule A (31–38)** — default calculation; **Schedule B (39–47)** —
  actual calculation; **Schedule C (48–53)** — tax (Form 4970 line 28) plus
  interest (combined interest rate) = line 53 additional tax.

### Part IV — Gifts or Bequests From Foreign Persons (lines 54–56)

- **54** — more than $100,000 from nonresident alien individuals or foreign
  estates (related donors aggregated): list each gift over $5,000 by date,
  description, FMV.
- **55** — gifts from foreign corporations/partnerships above the §6039F
  threshold ($20,116 for 2025; $20,573 for 2026): date, donor name,
  address, TIN, type, description, FMV.
- **56** — any donor acting as a nominee or intermediary?

For Part IV, a gift or bequest is generally **not taxable income** to the
US recipient (IRC §102); the reporting is informational. Gifts from
foreign corporations or partnerships can be recharacterized under
§672(f)(4). A gift from a covered expatriate may require Form 708
(§2801).

---

## Validation

Before declaring the form ready, run these checks. Surface anything that
fails — don't silently fix.

### Math and structural checks

- [ ] At least one Part (I, II, III, or IV) is filled in — otherwise the
      form has no purpose
- [ ] Trigger boxes at top of page 1 match the Parts actually filled in
- [ ] One Form 3520 per foreign trust
- [ ] If Part IV used: line 54 total exceeds $100,000 (related donors
      aggregated) and/or line 55 total exceeds the year's §6039F threshold;
      every line 54 gift over $5,000 listed by date, description, FMV
- [ ] If Part II used: Owner Statement (Form 3520-A pages 3–4) attached OR
      a substitute Form 3520-A attached; line 23 filled
- [ ] If Part III: line 27 = line 24(f) total + line 25(g) total; Schedule A
      math: line 34 = line 33 × 1.25, line 35 = line 34 ÷ 3 (or fewer
      years), line 36 = smaller of 31 and 35, line 37 = 31 − 36, line 38 =
      32 ÷ 2; Schedule A used again if it was used in an earlier year
- [ ] If line 37 or 41a > 0: Form 4970 attached as a worksheet; line 49 =
      Form 4970 line 28; line 51 from the IRS.gov/CombinedInterestRate
      table for the year (or computed); line 53 = 49 + 52
- [ ] All foreign-currency amounts have a stated USD conversion + the
      exchange-rate source documented
- [ ] Country codes on lines 6a/6b and 21a/21b from IRS.gov/CountryCodes

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] User received a "loan" from a foreign relative or foreign trust →
      may be a disguised gift (Part IV) or a non-qualified obligation
      (Part I/III); ask user to characterize
- [ ] Part IV reports gift from a foreign individual but donor's address is
      a tax haven and donor is described as an "estate" or "foundation" →
      may actually be a trust/entity, ask user
- [ ] Part III default method generates a very high throwback tax → user
      should request a Beneficiary Statement from the trustee for actual
      method
- [ ] Filer is a US owner of the trust (Part II) AND received a
      distribution from the owned portion → lines 24 and 27 only; don't
      double-tax
- [ ] Filer also has FBAR (FinCEN 114) and/or Form 8938 obligations on
      same foreign trust assets → those are separate filings, remind user
- [ ] A "gift" came from a U.S. person or through a U.S. account of a
      foreign donor → confirm who the donor really is before using Part IV
      (a gift from a U.S. person is not reportable on Form 3520)

### Cross-form / cross-filing checks

- [ ] Form 3520 + Form 8938: assets reported on Form 3520 are excepted
      from detailed Form 8938 reporting; check item C and count the Form
      3520 on Form 8938 Part IV, line 15
- [ ] Form 3520 + FBAR: if a foreign trust holds a foreign financial
      account on which the user has signature authority or beneficial
      interest, the account is reportable on FBAR independently
- [ ] Form 3520 due date: April 15 (June 15 with line 1j statement if
      living and working abroad); October 15 if the income tax return was
      extended and line 1k is completed
- [ ] If filing a joint Form 3520 (line 1i): joint income tax return, both
      spouses transferors/grantors/beneficiaries of the same trust; both
      spouses sign

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to
the IRS Form 3520 PDF or have a tax professional review. Format:

```markdown
# Form 3520 (Rev. December 2023) — DRAFT for tax year YYYY

## Page 1
A. Initial | Final | Amended: <one or none>
B. Filer type: Individual | Partnership | Corporation | Trust | Executor
C. Counted on Form 8938 Part IV line 15: Yes | No
Trigger boxes checked: <Part I / Part II / Part III / Part IV>
1a. Name: <Filer Name>          1b. TIN: <SSN/ITIN/EIN>
1c, 1e–1h. Address: <full address>
1d. Spouse's TIN: <joint Form 3520 only>
1i. Joint Form 3520: [ ]   1j. 2-month extension (statement attached): [ ]
1k. Income tax return extension: [ ]  Form number: <4868 / 7004>
2a–2h. Foreign trust: <name, EIN or none, address, date created | blank if Part IV only>
3. U.S. agent: Yes | No   3a–3g: <agent name, TIN, address>
4a–4f. U.S. decedent: <executor filings only>

## Part I — Transfers (if applicable)
5a–5c. Trust creator: <name, address, TIN>
6a / 6b / 6c. Country codes (created / governing law), date created
7a / 7b. Other owner of transferred assets: Yes | No (<details>)
8. Completed gift or bequest: Yes | No
9a / 9b. U.S. beneficiary now / by amendment: Yes | No
11a / 11b / 12. Related-trust obligations; qualified; assessment extension agreed
13. Gratuitous transfers:
| (a) Date | (b) Property | (c) FMV | (d) Basis | (e) Gain recognized | (f) (c)−(d)−(e) | (g) Property received | (h) FMV received | (i) (c)−(h) |
14a–14c. Documents attached / previously attached
15–18. Beneficiaries, trustees, other powers, trust documents (only if line 3 = No)
19. Qualified obligations outstanding: <columns (a)–(f)>

## Part II — US Owner (if applicable)
20. Owners: <name | address | country of tax residence | TIN | Code section>
21a / 21b / 21c. Country codes, date created
22. Form 3520-A filed by trust: Yes (Owner Statement pp. 3–4 attached) | No (substitute Form 3520-A attached)
23. Gross value of portion owned at year-end: $X,XXX

## Part III — Distributions (if applicable)
24. | (a) Date | (b) Property received | (c) FMV | (d) Property transferred | (e) FMV transferred | (f) (c)−(e) |
25. Loans / uncompensated use: | (a) FMV | (b) Date | (c) Max term | (d) Rate | (e) Qualified? | (f) FMV of qualified obligation | (g) (a)−(f) |
26. Assessment extension agreed: Yes | No | N/A
27. Total distributions: $X,XXX
28. Trust holds your qualified obligation: Yes | No
29. Foreign Grantor Trust Beneficiary Statement: Yes | No | N/A
30. Foreign Nongrantor Trust Beneficiary Statement: Yes | No | N/A
Schedule A (default): 31 $ | 32 years | 33 $ | 34 $ | 35 $ | 36 $ | 37 $ | 38 years
Schedule B (actual): 39–47 <amounts from the beneficiary statement>
Schedule C: 48 $ | 49 $ (Form 4970 line 28) | 50 years | 51 rate | 52 $ | 53 $ → Schedule 2 additional tax

## Part IV — Gifts/Bequests (if applicable)
54. More than $100,000 from NRA individuals / foreign estates: Yes | No
| (a) Date | (b) Description | (c) FMV (USD) |   (each gift over $5,000)
55. Gifts from foreign corporations / partnerships over $XX,XXX (year's §6039F threshold): Yes | No
| (a) Date | (b) Donor | (c) Address | (d) TIN | (e) Corp / Partnership | (f) Description | (g) FMV |
56. Donor acting as nominee or intermediary: Yes | No

## Currency translation
Source: <spot rate per date | IRS yearly average | other>
Notes: <list rates used>

## Required attachments
- [ ] Line 1j statement (if abroad)
- [ ] Owner Statement (Form 3520-A pages 3–4) or substitute Form 3520-A (Part II)
- [ ] Beneficiary statement (line 29 or 30 "Yes")
- [ ] Explanation of line 32 years (Schedule A)
- [ ] Form 4970 worksheet (Schedule C)
- [ ] Loan / sale documents (lines 11b, 14) and trust documents (line 18) as applicable

## Mailing address
Internal Revenue Service Center
P.O. Box 409101
Ogden, UT 84409

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 11>

## Sources cited in this draft
- IRS Form 3520 (Rev. December 2023)
- IRS Instructions for Form 3520 (Rev. December 2025)
- IRC §6048 (foreign trust info reporting); IRC §6677 (penalties)
- IRC §6039F (gifts from foreign persons); Rev. Proc. 2024-40 §2.48 / Rev. Proc. 2025-32 §4.47 (threshold)
- IRC §679 (US grantor of foreign trust with US beneficiary)
- IRC §§665–668 (accumulation distributions; interest charge); Form 4970
- (any other authority used)
```

The draft is **not** the final filed form. The user still has to enter the
data into the IRS Form 3520 fillable PDF, sign it (the instructions accept
e-signatures), and mail it to Ogden.
The deliverable's value is that every reportable item is identified,
classified, and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete
  walkthrough of Parts I-IV, line by line, with edge cases
- [`references/foreign-trust-classification.md`](./references/foreign-trust-classification.md)
  — When is an entity a "foreign trust" under US tax rules; common
  misclassifications (foundations, hybrid trusts, Stiftungen)
- [`references/3520-vs-3520-a.md`](./references/3520-vs-3520-a.md) —
  Coordination of Form 3520 (filed by the US person) and Form 3520-A
  (filed by the trust); when a substitute 3520-A is required
- [`references/throwback-default-method.md`](./references/throwback-default-method.md)
  — Mechanics of the §§665–668 throwback rules and the Form 3520 default
  method calculation
- [`references/common-mistakes.md`](./references/common-mistakes.md) —
  Top mistakes that trigger §6677 / §6039F penalties, with fixes
- [`filing.md`](./filing.md) — Paper-filing playbook (the instructions give
  only a mailing address)

## Examples

End-to-end worked Form 3520s. Use these as patterns when the user's
situation is similar.

- [`examples/italian-inheritance.md`](./examples/italian-inheritance.md) —
  US citizen receives $200,000 cash inheritance from grandparent in Italy;
  Part IV gift reporting only
- [`examples/uk-family-trust-owner.md`](./examples/uk-family-trust-owner.md)
  — US person treated as owner of UK family trust under §679; Part II + need
  for substitute 3520-A
- [`examples/offshore-trust-distribution.md`](./examples/offshore-trust-distribution.md)
  — US beneficiary receives distribution from foreign non-grantor trust
  without a Beneficiary Statement; Part III default method and throwback

## Sources

Authoritative sources used by this skill. Always re-verify these against
the IRS site for the tax year being filed — the IRS revises forms and
instructions each cycle.

- [Form 3520 (latest)](https://www.irs.gov/pub/irs-pdf/f3520.pdf) — the form itself
- [Instructions for Form 3520 (latest)](https://www.irs.gov/pub/irs-pdf/i3520.pdf) — line-by-line IRS guidance
- [About Form 3520](https://www.irs.gov/forms-pubs/about-form-3520) — IRS landing page with archive of past revisions
- [Form 3520-A (latest)](https://www.irs.gov/pub/irs-pdf/f3520a.pdf) — Annual Information Return of Foreign Trust With a US Owner
- [Instructions for Form 3520-A (latest)](https://www.irs.gov/pub/irs-pdf/i3520a.pdf)
- [IRS yearly average currency exchange rates](https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates)
- [Combined interest rate tables for Part III Schedule C](https://www.irs.gov/CombinedInterestRate)
- [Form 4970 (2025)](https://www.irs.gov/pub/irs-pdf/f4970.pdf) — Tax on Accumulation Distribution of Trusts (worksheet attached to Form 3520 for foreign trusts)
- [About Form 4970](https://www.irs.gov/forms-pubs/about-form-4970) — Tax on Accumulation Distribution of Trusts
- IRC §679 (foreign trust having one or more US beneficiaries)
- IRC §6048 (information returns with respect to certain foreign trusts)
- IRC §6039F (gifts from foreign persons)
- IRC §6677 (penalty for failure to file information returns with respect to certain foreign trusts)
- IRC §6662(j) (40% penalty for undisclosed foreign financial asset understatements)
- IRC §§665–668 (treatment of excess distributions by trusts; throwback rules)
- Rev. Proc. 2024-40 §2.48 — §6039F threshold $20,116 for 2025; Rev. Proc. 2025-32 §4.47 — $20,573 for 2026
- Treas. Reg. §1.679-1 through §1.679-4 (foreign trusts having US beneficiaries)
- Notice 97-34, 1997-25 I.R.B. 22 (foreign trust reporting; source of the $100,000 Part IV amount and the default method; still cited in current Form 3520 instructions)
- Rev. Proc. 2014-55, Rev. Proc. 2020-17, and Prop. Reg. §1.6048-5 (exemptions for certain foreign retirement and tax-favored trusts)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS
forms and publications. It is not tax advice. It does not establish a
CPA-client relationship. The penalties under IRC §6677 and §6039F are
severe and the rules around foreign trust classification are fact-intensive;
any user with a six-figure transfer, a beneficial interest in a foreign
trust, or a non-trivial foreign inheritance should have a licensed
international tax practitioner (CPA, EA, or attorney) review the draft
before filing.
