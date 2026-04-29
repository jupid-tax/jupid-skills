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
last_verified: 2026-04-29
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
  person, and the aggregate from all foreign individuals + foreign estates
  exceeded $100,000, OR the aggregate from foreign corporations + foreign
  partnerships exceeded the inflation-adjusted threshold (Rev. Proc.
  2024-40 set this at $19,570 for 2025; the 2026 figure is set by Rev. Proc.
  2025-XX — verify before filing)

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
  disregarded entity → use the [`form-5472`](../form-5472/) skill

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
   citizenship, US tax residency status. If filing jointly with a spouse who
   also has a 3520 trigger, ask whether they will file a single joint Form
   3520 (allowed for spouses filing a joint income tax return when both have
   the same reportable transactions) or two separate forms.
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
5. For **Part II** — trust identifying details; whether a Foreign Grantor
   Trust Owner Statement and Beneficiary Statement (page 3 of Form 3520-A,
   or substitute) are available from the trust; trust's income, expenses,
   and distributions for the year; FMV of trust assets at year-end; list of
   beneficiaries who received distributions
6. For **Part III** — name of foreign trust; whether the trust is a grantor
   trust with a US owner (treated differently from a non-grantor foreign
   trust); date and FMV of each distribution; whether the trust provided a
   Foreign Nongrantor Trust Beneficiary Statement (allows actual-method
   reporting); if no statement, the default-method calculation requires
   prior-year distribution history
7. For **Part IV** — list of foreign donors with: donor's name, address,
   relationship to filer, type of donor (foreign individual, foreign estate,
   foreign corporation, foreign partnership), date of each gift/bequest,
   description and FMV of each gift, currency conversion source

For currency translation, ask the user which exchange-rate source they want
to use. The IRS accepts the Treasury yearly average rate
(https://www.fiscal.treasury.gov/reports-statements/treasury-reporting-rates-exchange/)
or the spot rate on the date of each transaction. Document the choice and be
consistent within the return.

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

If only Part IV applies (gift/bequest reporting), most of the trust-specific
sections of the form stay blank — Form 3520 is one form serving multiple
purposes.

### Step 3 — Run threshold checks for Part IV

Part IV thresholds (these are the only thresholds in Form 3520; Parts I-III
have no de minimis):

- **Foreign individuals + foreign estates**: aggregate > **$100,000** during
  the tax year (statutory; IRC §6039F(c)(1)(B); not inflation-adjusted)
- **Foreign corporations + foreign partnerships**: aggregate > **inflation-
  adjusted threshold**. Rev. Proc. 2024-40 set this at **$19,570 for 2025**.
  The 2026 figure will be in the 2025 inflation-adjustment Rev. Proc. —
  verify before filing. The instructions at the top of the current-year
  Form 3520 instructions PDF state the exact figure for that year.

If aggregate from individual/estate donors is between $0 and $100,000,
**no Part IV reporting is required for that category**. If aggregate is
above $100,000, the user must list each donor that contributed > $5,000
individually; smaller donors aggregate.

For corporate/partnership donors above the threshold, all donors are listed
individually with the donor's name and the IRS may presume the gift is
income unless the user rebuts the presumption (IRC §6039F(b)).

### Step 4 — Collect and structure the data per applicable Part

For each Part the user is filing, build a structured table the agent can
walk line by line. Templates in `references/line-by-line.md` (Parts I-IV).

Examples of what to extract:

```
| Donor (Part IV)            | Type        | Date       | FMV (USD) |
|----------------------------|-------------|------------|-----------|
| Maria Rossi (grandmother)  | Individual  | 2026-08-12 | $200,000  |
| Banca Popolare di Milano   | Foreign corp| 2026-09-30 | $25,000   |

| Distribution (Part III)    | Trust       | Date       | FMV (USD) |
|----------------------------|-------------|------------|-----------|
| Cash distribution          | UK Family Trust | 2026-04-15 | $42,000  |
| Use of London flat (1 mo)  | UK Family Trust | 2026-07   | $4,800    |
```

### Step 5 — For Part III, determine reporting method

If the foreign trust is a **grantor trust** with a US owner who received the
distribution: the distribution from a US-owned grantor trust is generally
not separately taxable (it's already taxed to the US owner), but it's still
reportable on Part III, and the US owner files Schedule A of Part III.

If the trust is a **foreign non-grantor trust** (no US owner), the
distribution may carry out the trust's distributable net income (DNI) plus
any "accumulation distribution" (an UNI carryout subject to throwback tax
and an interest charge under IRC §§667–668).

- If the trust provides a **Foreign Nongrantor Trust Beneficiary
  Statement**: use the **actual method**. Compute DNI/UNI portions using the
  statement's amounts.
- If no statement is provided: use the **default method** (Form 3520
  instructions, Part III). Default method computes the accumulation
  distribution using the average of the prior 3 years' distributions and
  treats much of the current distribution as UNI subject to throwback +
  interest charge — almost always worse than actual method. If user is
  receiving repeated distributions from a foreign non-grantor trust without
  a beneficiary statement, recommend they request one from the trustee.

### Step 6 — For Part II, ensure Form 3520-A coordination

A US owner of a foreign trust must ensure a **Form 3520-A is filed by the
trust** for the same tax year, due March 15 (or 6-month extension via
Form 7004 filed by the trust, not the owner).

If the foreign trust does not file its own 3520-A, the US owner must file a
**substitute Form 3520-A** as an attachment to Part II of their own Form
3520. The substitute is a fully completed 3520-A signed by the US owner.
This is an extremely common pitfall — many US owners file Form 3520 Part II
but neglect the substitute 3520-A and trigger the 5%/$10,000 §6677 penalty.

If the user is the US owner and the trustee is uncooperative, the user must
file the substitute. Ask for the data needed.

### Step 7 — Currency translation

Translate foreign currency to USD consistently. Document the exchange rate
source and date(s) used in the deliverable.

For Part IV gifts: use the spot rate on the date of receipt of each gift, OR
the Treasury yearly average rate for that currency for the calendar year.
For Part I/II/III trust amounts: typically yearly average for income/expense
accumulations and spot rate for asset valuations on a specific date.

### Step 8 — Compute totals per Part

- Part I: total value of property transferred + obligations received
- Part II: trust's income + distributions to all beneficiaries; portion
  attributable to US owner
- Part III: total distributions received; if non-grantor trust without
  beneficiary statement, run default method calculation
- Part IV: aggregate gifts/bequests by donor category

### Step 9 — Run validation checks

See **Validation** below. Run every check.

### Step 10 — Produce the deliverable

See **Output format** below.

### Step 11 — Hand off downstream

State the next steps:

- **Form 3520 is filed separately from Form 1040** — it does NOT attach to
  the 1040. Mail to: Internal Revenue Service Center, P.O. Box 409101,
  Ogden, UT 84409 (verify mailing address against current Form 3520
  instructions; the IRS shifts service center addresses periodically)
- **Due date** — Same as the filer's income tax return, including extensions.
  For an individual: April 15 (or April 18 if 15th falls on weekend/holiday),
  extended to October 15 if Form 4868 is filed for the 1040. The Form 3520
  extension follows the 1040 extension automatically; no separate form
  needed for individuals.
- **For a domestic trust or estate filer**: due date follows Form 1041
  (April 15 or 15th day of 4th month after fiscal year-end); extension via
  Form 7004 extends 1041 and 3520 together
- **If Part II applies**: confirm the foreign trust filed Form 3520-A by
  March 15 (with extension via Form 7004 by the trust); if not, attach
  substitute 3520-A
- **Penalties for failure to file or incomplete filing**:
  - Part I/II/III: 35% of the gross reportable amount (transfer or
    distribution) under IRC §6677, with continuing 5%/month penalties up to
    100% of the reportable amount
  - Part IV gift reporting: 5% per month of the unreported gift, up to 25%
    (IRC §6039F(c)(1)(B))
  - Reasonable cause is a defense (IRC §6677(d)) but is hard to establish
- **Information return only**: Form 3520 itself doesn't compute tax owed.
  Tax consequences (e.g., throwback tax on Part III default-method UNI)
  are reported on Form 1040 + Schedule 1 + Form 4970 (Tax on Accumulation
  Distribution of Trusts) where applicable

### Step 12 — File the return (optional, if the user wants the agent to file)

Form 3520 is **not e-filable as of tax year 2025** — it must be paper filed.
See [`filing.md`](./filing.md) for the paper filing playbook (assembly,
mailing, certified mail proof of timely filing, retention).

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md).
High-level rules below.

### Identifying information (top of page 1)

- **Lines 1a-1k** — Filer's name, ID number, address, filing status. Check
  the box for which Part(s) apply.
- **Lines 2a-2k** — If filing jointly with a spouse, spouse's information
- **Initial / final / amended return** — check the appropriate box
- **If excepted from filing**: there's an exception checkbox for transfers
  to foreign trusts in connection with the filer's death (Part I) — see
  Form 3520 instructions

### Part I — Transfers by US Persons to a Foreign Trust

Lines 5-18 cover the transfer details. Key lines:

- **Lines 5a-5h** — Foreign trust identification (name, address, country,
  EIN if any, US agent if appointed under §6048(b)(2))
- **Line 6** — Trustee information
- **Line 7** — Beneficiary information at time of transfer
- **Line 8** — Schedule A: Obligations received in exchange for the transfer
  (if any). A "qualified obligation" (specific terms in the regs) avoids
  Part I treatment of the transfer; a non-qualified obligation triggers
  full-FMV transfer treatment.
- **Lines 9-18** — Transfer details (cash + property), date(s), FMV

### Part II — US Owner of a Foreign Trust

Lines 19-22 cover ownership details. Key lines:

- **Lines 19-21** — Trust identification, date became US owner, attached
  Foreign Grantor Trust Owner Statement (page 3 of Form 3520-A)
- **Line 22** — Description of US owner's portion of trust during the year
  (income, expenses, FMV at year-end)
- **Box at top of Part II** — "Did the foreign trust file Form 3520-A?" If
  No, attach substitute 3520-A

### Part III — Distributions to a US Person From a Foreign Trust

Lines 24-32 cover distribution details. Key lines:

- **Lines 24-26** — Trust identification, type of trust (grantor /
  non-grantor)
- **Line 27** — Whether a Foreign Nongrantor Trust Beneficiary Statement
  was provided
- **Lines 28-29** — Each distribution: date, type (cash/property/loan/use
  of property), FMV
- **Line 30** — If actual method: portion that is income (DNI) vs. corpus
- **Line 31** — If default method: schedule walking the 3-year average
  calculation, throwback amounts, IRC §668(a) interest charge

Schedule A of Part III is for grantor trust distributions; Schedule B is
for non-grantor trust actual method; Schedule C is for default method.

### Part IV — US Recipients of Gifts or Bequests From Foreign Persons

Lines 54-56 cover gift reporting:

- **Line 54** — Gifts > $5,000 from foreign individuals + foreign estates
  (only required to itemize if aggregate > $100,000). Each row: donor
  name, address, relationship, date, description, FMV
- **Line 55** — Gifts from foreign corporations + foreign partnerships
  above the inflation-adjusted threshold. Itemize all such donors.
- **Line 56** — Whether the donor is related to a US person; whether the
  gift is from a partnership/corporation that is a CFC/PFIC

For Part IV, the gift is generally **not taxable income** to the US
recipient — gifts and inheritances are excluded under IRC §102. The Form
3520 reporting is informational. However, if the donor is a foreign
corporation or partnership, IRC §6039F(b) creates a presumption that the
gift is income unless rebutted.

---

## Validation

Before declaring the form ready, run these checks. Surface anything that
fails — don't silently fix.

### Math and structural checks

- [ ] At least one Part (I, II, III, or IV) is filled in — otherwise the
      form has no purpose
- [ ] Part-applicable boxes at top of page 1 match the Parts actually
      filled in
- [ ] If Part IV used: aggregate by donor category exceeds the relevant
      threshold; otherwise Part IV is not required and should be removed
- [ ] If Part II used: confirmation that Form 3520-A was filed by the trust
      OR a substitute 3520-A is attached
- [ ] If Part III default method used: 3-year average distribution
      calculation is shown; §668 interest charge is computed using current
      AFR for underpayments
- [ ] All foreign-currency amounts have a stated USD conversion + the
      exchange-rate source documented
- [ ] All trust identifying information includes country (IRS treats this
      as a required field)

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
      distribution (Part III) → both Parts must be filed; don't double-tax
- [ ] Filer also has FBAR (FinCEN 114) and/or Form 8938 obligations on
      same foreign trust assets → those are separate filings, remind user
- [ ] Aggregate Part IV gifts include any item > $14,000 from a single
      donor → confirm this isn't actually a US-source item misreported as
      foreign

### Cross-form / cross-filing checks

- [ ] Form 3520 + Form 8938: trust assets reported on Form 8938 in
      Section VI must match Form 3520 trust details
- [ ] Form 3520 + FBAR: if a foreign trust holds a foreign financial
      account on which the user has signature authority or beneficial
      interest, the account is reportable on FBAR independently
- [ ] Form 3520 due date: same as 1040; extension via 4868 covers 3520
      automatically for individuals
- [ ] If filing jointly: only one Form 3520 needed; both spouses sign

---

## Output format

The agent's deliverable is a **filled draft** the user can transcribe to
the IRS Form 3520 PDF or have a tax professional review. Format:

```markdown
# Form 3520 — DRAFT for tax year YYYY

## Filer identification
Name: <Filer Name>
Identifying number: <SSN/ITIN/EIN>
Address: <full address>
Filing status: Single | MFJ | MFS | HoH | QW
Country of citizenship: <country>
Initial / Final / Amended: <one>

## Parts being filed
- [ ] Part I — Transfer to foreign trust
- [ ] Part II — US owner of foreign trust
- [ ] Part III — Distribution from foreign trust
- [ ] Part IV — Gift from foreign person

## Part I — Transfers (if applicable)
Foreign trust name: <name>
Trust country: <country>
Trust EIN (if any): <EIN or "None">
Date trust created: <date>
US agent appointed under §6048(b)(2): Yes | No
Schedule A (obligations): N/A | <details>

| Line | Description                  | Amount (USD) |
|------|------------------------------|--------------|
| 9    | Cash transferred             | $X,XXX       |
| 10   | FMV of property transferred  | $X,XXX       |
| ...  | ...                          | ...          |
| 18   | Total transfers              | $X,XXX       |

## Part II — US Owner (if applicable)
Foreign trust name: <name>
Date became US owner: <date>
Form 3520-A filed by trust for this year: Yes | No (substitute attached)
US owner's portion of trust:
  - Beginning-of-year FMV: $X,XXX
  - Income: $X,XXX
  - Distributions: $X,XXX
  - End-of-year FMV: $X,XXX
Foreign Grantor Trust Owner Statement attached: Yes | No

## Part III — Distributions (if applicable)
Foreign trust name: <name>
Trust type: Grantor | Non-grantor
Beneficiary Statement provided: Yes (actual method) | No (default method)

| Line | Date       | Type            | FMV (USD) |
|------|------------|-----------------|-----------|
| 28a  | YYYY-MM-DD | Cash            | $X,XXX    |
| 28b  | YYYY-MM-DD | Property        | $X,XXX    |
| ...  | ...        | ...             | ...       |
| 29   | Total                          | $X,XXX    |

If actual method:
  - Portion that is current income (DNI): $X,XXX
  - Portion that is corpus: $X,XXX

If default method (Schedule C):
  - 3-year average distribution: $X,XXX
  - Excess (deemed UNI): $X,XXX
  - Throwback tax: $X,XXX (computed on Form 4970)
  - §668 interest charge: $X,XXX

## Part IV — Gifts/Bequests (if applicable)
Aggregate from foreign individuals + foreign estates: $X,XXX
Threshold: $100,000 (statutory)
Aggregate from foreign corporations + foreign partnerships: $X,XXX
Threshold: $XX,XXX (Rev. Proc. 2024-40 / 2025-XX — verify)

| Donor name      | Type       | Country | Date       | Description | FMV (USD) |
|-----------------|------------|---------|------------|-------------|-----------|
| <name>          | Individual | <ctry>  | YYYY-MM-DD | <descr>     | $X,XXX    |
| ...             | ...        | ...    | ...        | ...         | ...        |

## Currency translation
Source: <Treasury yearly average | spot rate per date | other>
Notes: <list rates used>

## Required attachments
- [ ] Substitute Form 3520-A (if Part II and trust didn't file)
- [ ] Foreign Grantor Trust Owner Statement (if Part II)
- [ ] Foreign Nongrantor Trust Beneficiary Statement (if Part III actual)
- [ ] Trust instrument (recommended for Part I, optional otherwise)
- [ ] Form 4970 (if Part III default method generates throwback tax —
      attached to Form 1040, not Form 3520)

## Mailing address
Internal Revenue Service Center
P.O. Box 409101
Ogden, UT 84409
(verify against current Form 3520 instructions)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 11>

## Sources cited in this draft
- IRS Form 3520 (revision date YYYY-MM-DD)
- IRS Instructions for Form 3520 (revision date YYYY-MM-DD)
- IRC §6048 (foreign trust info reporting)
- IRC §6039F (gifts from foreign persons)
- IRC §679 (US grantor of foreign trust with US beneficiary)
- IRC §§665–668 (throwback rules; accumulation distributions)
- Rev. Proc. 2024-40 (2025 inflation-adjusted §6039F threshold)
- (any other authority used)
```

The draft is **not** the final filed form. The user still has to enter the
data into the IRS Form 3520 fillable PDF, sign in ink, and mail to Ogden.
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
- [`filing.md`](./filing.md) — Paper-filing playbook (Form 3520 is not
  e-filable as of 2026)

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
- [Treasury yearly average exchange rates](https://www.fiscal.treasury.gov/reports-statements/treasury-reporting-rates-exchange/)
- [About Form 4970](https://www.irs.gov/forms-pubs/about-form-4970) — Tax on Accumulation Distribution of Trusts
- IRC §679 (foreign trust having one or more US beneficiaries)
- IRC §6048 (information returns with respect to certain foreign trusts)
- IRC §6039F (gifts from foreign persons)
- IRC §6677 (penalty for failure to file information returns with respect to certain foreign trusts)
- IRC §§665–668 (treatment of excess distributions by trusts; throwback rules)
- Rev. Proc. 2024-40 — inflation-adjusted §6039F threshold for 2025
- Treas. Reg. §1.679-1 through §1.679-4 (foreign trusts having US beneficiaries)
- Notice 97-34 (foreign trust reporting requirements; still cited in current Form 3520 instructions)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS
forms and publications. It is not tax advice. It does not establish a
CPA-client relationship. The penalties under IRC §6677 and §6039F are
severe and the rules around foreign trust classification are fact-intensive;
any user with a six-figure transfer, a beneficial interest in a foreign
trust, or a non-trivial foreign inheritance should have a licensed
international tax practitioner (CPA, EA, or attorney) review the draft
before filing.
