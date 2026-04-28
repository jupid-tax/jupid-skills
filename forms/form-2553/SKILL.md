---
name: form-2553
description: >
  Use this skill when an LLC owner, corporation, or small-business founder wants
  to elect S-corporation tax status. Triggers on phrases like "elect S-corp",
  "file Form 2553", "S-corp election deadline", "make S-corp election for my LLC",
  "should my LLC be an S-corp", "late S-corp election", "Rev. Proc. 2013-30",
  "missed S-corp deadline", "convert LLC to S-corp". Also engages when the user
  asks "is S-corp worth it for me" and provides profit figures. Do NOT use for
  terminating an existing S-corp election (Form 8869 / IRC §1362(d)), changing
  the tax year of an already-elected S-corp (Form 1128), or filing the annual
  return for an entity that already elected S-corp (use form-1120-s). Do NOT use
  for entity formation itself — that's a state filing, not federal.
form: Form 2553 (Election by a Small Business Corporation)
audience: [scorp, llc1, llcm]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f2553.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i2553.pdf
---

# Form 2553 — Election by a Small Business Corporation

This skill produces an audit-grade Form 2553 election package: confirmed eligibility, calculated deadline, completed Part I (entity info + shareholder consents), Part II / III / IV as needed, and a filing checklist for fax or mail submission to the IRS service center.

The math is mostly date arithmetic and a yes/no eligibility checklist. The judgment is in (a) whether the user actually wants to elect — there's a real break-even threshold below which it's not worth the compliance overhead — and (b) catching late filings early so the user can use Rev. Proc. 2013-30 relief instead of losing a year.

**Companion guide for end users:** [Form 2553 (2026): S-Corp Election Filing Guide & Deadlines](https://jupid.com/blog/form-2553-s-corp-election-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 2553, "S-corp election", "elect S-corp", or "Subchapter S"
- The user has formed (or is forming) an LLC or corporation and asks about tax structure choice
- The user is a sole proprietor / single-member LLC owner with profit ≥$40K asking about SE tax savings
- The user mentions missing a deadline and asks about late S-corp election or Rev. Proc. 2013-30
- The user describes wanting to "be paid as W-2 from my own company"

Do **not** engage this skill when:

- The user already has an S-corp and is filing the annual return → use the (forthcoming) `form-1120-s` skill
- The user wants to **terminate** an existing S-corp election → file Form 8869 or use IRC §1362(d) revocation procedures, not 2553
- The user wants to change the tax year of an existing S-corp → Form 1128
- The user is a multi-member LLC that does NOT want to elect S-corp → file Form 1065 (partnership return); use the (forthcoming) `form-1065` skill
- The user is asking about C-corp election → that's the default for any corporation; no election needed (use Form 1120)
- The user wants entity *formation* (Articles of Organization, etc.) → that's a state filing; redirect to the secretary-of-state filing process

If the user's situation is ambiguous (e.g., "I formed an LLC but I don't know what type of taxation I'm under"), ask before proceeding. Default LLC taxation is sole prop (single-member) or partnership (multi-member). S-corp requires an affirmative election via this form.

---

## Prerequisites

Before producing anything, the agent must have these inputs. **If any are missing, ask explicitly and stop until you get an answer.** Do not pick defaults for these — wrong answers void the election or trigger a year of incorrect tax returns.

### Always required

1. **Tax year** the election is to take effect (2025, 2026, etc.)
2. **Entity name** — exactly as registered with the state and on IRS records
3. **Entity type** — corporation (Inc., Corp.) or LLC. If LLC, confirm whether Form 8832 has been filed; if not, Form 2553 alone makes the combined election (per Rev. Proc. 2013-30)
4. **Date of formation** — date articles of incorporation/organization were accepted by the state
5. **State of formation**
6. **EIN** — if entity doesn't have one, ASK the user to apply at IRS.gov/EIN before proceeding. Form 2553 cannot be filed without an EIN
7. **Date entity began doing business** OR **date shareholders first owned stock** OR **date entity acquired assets** — whichever was earliest. Used to compute the deadline for new entities.
8. **Desired effective date of election** (Line E)
9. **Tax year choice** — calendar year (default; almost always the right answer for small entities) or fiscal year (Part II required if non-calendar)
10. **Complete shareholder list**: each shareholder's full legal name, address, SSN/ITIN/EIN, number of shares (or LLC ownership %), date acquired, and whether they consent
11. **For shareholders in community-property states (AZ, CA, ID, LA, NV, NM, TX, WA, WI)**: name of non-owner spouse and confirmation that they will sign Form 2553 in Column J

### Required if filing late (Rev. Proc. 2013-30)

12. **Reasonable cause statement** — why was the election filed late? Acceptable: "filer was unaware of the deadline", "accountant failed to file", "filer believed entity was already an S-corp". The agent should help the user articulate this in 2-4 sentences. Not acceptable: "we wanted to wait and see how the year went" (this is willful, not inadvertent)
13. **Confirmation that no return inconsistent with S-corp treatment has been filed** since the intended effective date — if the user already filed Form 1120 (C-corp) or Schedule C / 1065 for the period since the intended effective date, Rev. Proc. 2013-30 still works but the user must amend those returns

### Optional but strongly recommended

14. **Reasonable salary analysis** — what salary will the shareholder-employee be paid? The agent should ask for the user's industry, role, geographic market, and hours worked, then point to BLS OES (Occupational Employment Statistics) data for the right NAICS code. **Do NOT pick a default salary** — under-salary triggers IRS reclassification per Watson v. Commissioner. This is a "ask, don't guess" point.
15. **Profit projection for the election year** — if not provided, ask. Used to calculate break-even (whether the election is worth the compliance overhead) and to validate that the proposed reasonable salary is plausible.

---

## Workflow

Execute in order. Don't skip ahead.

### Step 1 — Confirm eligibility

Walk through the IRC §1361(b) eligibility checklist with the user. Surface failures immediately — there is no point completing the form if the entity is ineligible.

```
Eligibility checklist (all must be YES):
□ Domestic corporation OR domestic LLC (formed under U.S. state law)
□ Not a bank using the reserve method, insurance company under Subchapter L,
  IRS §936 possessions corporation, or DISC
□ ≤100 shareholders (spouses count as one; six-generation family election available)
□ All shareholders are individuals (U.S. citizens or resident aliens),
  qualifying trusts, estates, or qualifying tax-exempt orgs
□ No shareholders are: C-corps, partnerships, multi-member LLCs,
  non-resident aliens, most foreign trusts, or IRAs
□ One class of stock (voting/non-voting OK; no preferred, no debt-recharacterized-as-stock)
```

For LLCs: check the operating agreement for waterfall distributions, preferred returns, or other clauses that violate the one-class-of-stock rule. If found, the operating agreement must be amended to pro-rata economic rights before filing 2553.

### Step 2 — Compute the deadline

Use [`references/timing-rules.md`](./references/timing-rules.md). Decision tree:

```
Has the entity ever filed a tax return as an entity (not Schedule C)?

YES → Existing entity case.
  Deadline = 2 months 15 days from start of intended tax year.
  Calendar-year entity → March 15 of the intended year.
  Fiscal-year entity → 2 months 15 days from start of fiscal year.

NO → New entity case.
  Deadline = 2 months 15 days from EARLIEST of:
    (a) date entity had shareholders/members
    (b) date entity acquired assets
    (c) date entity began doing business
```

State the computed deadline back to the user explicitly. Compare with today's date:

- **Today is before the deadline** → standard election, Part IV not needed
- **Today is after the deadline but within 3 years 75 days of intended effective date** → late election, Rev. Proc. 2013-30 relief, Part IV required
- **Today is more than 3 years 75 days after intended effective date** → Rev. Proc. 2013-30 unavailable; user must request a Private Letter Ruling under Reg. §301.9100-3 (expensive, beyond this skill's scope — redirect to a CPA)

### Step 3 — Run the break-even check (advisory)

If the user hasn't yet committed to the election, surface the economic case:

```
Estimated annual SE tax savings = (Net profit − reasonable salary) × 15.3%
                                     [up to SS wage base]

Estimated annual compliance overhead:
  Payroll software:        $400-$800
  State unemployment tax:  $100-$700 (varies by state and wage base)
  Bookkeeping increment:   $1,000-$2,000
  Form 1120-S preparation: $800-$2,000

Break-even: net profit roughly $40,000-$60,000 depending on state.
```

If projected net profit is below $40K and the user hasn't yet made the election, ASK whether they still want to proceed. Don't decide for them — but make the trade-off visible. If above $80K, the math is decisively in favor.

### Step 4 — Collect shareholder consent data

Build the shareholder consent table:

```
| # | Name | Address | SSN/ITIN | Shares (or LLC %) | Date acquired | Spouse consent? |
|---|------|---------|----------|-------------------|---------------|-----------------|
| 1 | ...  | ...     | ...      | ...               | ...           | ...             |
```

For each shareholder, confirm they will sign in Column K. For community-property states, confirm the non-owner spouse will also sign.

If any shareholder is in an ineligible category (C-corp, non-resident alien, partnership, multi-member LLC), STOP — entity is ineligible.

### Step 5 — Determine tax year (Part II?)

Default: calendar year (Box F1). For small entities, this is almost always correct.

If the user wants a fiscal year, ask why. Acceptable reasons:
- Natural business year (≥25% of gross receipts in last 2 months for last 3 years; Rev. Proc. 2006-46)
- Ownership tax year (matching majority shareholders)
- Documented business purpose
- §444 election (required-payment buy-in)

If non-calendar, complete Part II. Most small filers should not.

### Step 6 — Determine if Part IV needed (late relief)

If Step 2 identified a late election, complete Part IV. Required elements:

1. Check Box 1 — entity intended to be classified as S-corp
2. Check Box 2 — failure was inadvertent
3. Check Box 3 — reasonable cause exists
4. Attach reasonable-cause statement (concise, factual, 2-4 sentences)
5. Write "FILED PURSUANT TO REV. PROC. 2013-30" across the top of page 1

### Step 7 — Determine if Part III needed (QSST)

Only needed if a Qualified Subchapter S Trust is among the shareholders. Most LLCs and small corporations have no trust shareholders. If applicable, see Form 2553 instructions page 5 for QSST election content; otherwise skip.

### Step 8 — Run validation checks

See **Validation** below. Run every check.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off to filing

If the user authorizes the agent to file, follow [`filing.md`](./filing.md). Otherwise, produce the printable PDF and instruct the user to fax or mail per Step 10 in filing.md, plus inform them of state-level S-corp election requirements (see [`references/state-conformity.md`](./references/state-conformity.md)).

### Step 11 — Set follow-up reminders

- 60 days from filing: check for CP261 acknowledgment
- 30 days from acknowledgment: confirm payroll provider is set up
- Quarterly: Form 941 deadlines (Apr 30, Jul 31, Oct 31, Jan 31)
- Annual: Form 940 (Jan 31), W-2 (Jan 31), Form 1120-S (Mar 15), state returns

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Part I — Election Information

- **A. Name of corporation** — exactly as on IRS records (must match EIN registration). If the legal name has a comma in it (e.g., "Smith, LLC"), include it.
- **B. Address** — current mailing address; PO box acceptable
- **C. Employer Identification Number** — required. No EIN, no election.
- **D. Date incorporated** — the date the state accepted the formation filing
- **E. State of incorporation** — two-letter postal abbreviation
- **F. Election effective date** — the SINGLE most important field. Triggers the 2-month-15-day deadline calculation.
- **G. Election change** — only if changing election; new elections leave blank
- **H. Tax year** — check exactly one of:
  - Box 1: Calendar year
  - Box 2: Fiscal year ending [MM/DD]
  - Box 3: 52-53 week year ending with reference to month
  - Box 4: Other (with explanation in Part II)
- **I. Officer signature, title, date** — corporate officer or LLC manager/member with signing authority

### Shareholder consent table (Page 1, bottom — and Page 2)

For each shareholder/member:
- **J. Name and address** — as on IRS records
- **K. Signature** — must be original (or qualifying electronic signature)
- **L. Date signed** — must be on or before the filing date
- **M. Stock owned** — number of shares (corp) or % interest (LLC), plus dates acquired
- **N. SSN or EIN** — for individuals, SSN; for trusts, trust EIN

For community-property states, non-owner spouse signs in column J too. Failure here is the #2 cause of voided elections.

### Part II — Selection of Fiscal Tax Year

Skip if calendar year. If non-calendar, document the basis (natural business year / ownership / business purpose / §444 election). Most small filers leave this blank.

### Part III — Qualified Subchapter S Trust Election

Only if a QSST is a shareholder. Rare for small entities. Requires the trust to elect to be treated as the deemed owner of S-corp stock under IRC §1361(d).

### Part IV — Late Corporate Classification Election Representations

Only if filing late under Rev. Proc. 2013-30. Three boxes:
1. Election filed under Rev. Proc. 2013-30
2. Failure to file timely was inadvertent
3. Reasonable cause exists; statement attached

---

## Validation

Run all checks before declaring ready.

### Eligibility checks

- [ ] Entity is a domestic corp or LLC formed under U.S. state law
- [ ] All shareholders are eligible (no C-corps, no partnerships, no multi-member LLCs, no non-resident aliens, no IRAs)
- [ ] Shareholder count ≤100 (with spouses/family aggregations)
- [ ] One class of stock confirmed (operating agreement reviewed for LLCs)
- [ ] EIN obtained and matches IRS records
- [ ] Entity is not in an ineligible class (bank reserve method, insurance, possessions, DISC)

### Date checks

- [ ] Election effective date (Line E) is on or after the date the entity began doing business (for new entities)
- [ ] Election effective date is the start of a tax year (e.g., Jan 1 for calendar year filers continuing from prior year)
- [ ] Today's date is computed against the deadline; on-time vs late status surfaced
- [ ] If late, today is within 3 years 75 days of effective date (Rev. Proc. 2013-30 window)

### Shareholder consent checks

- [ ] Every shareholder named on the form
- [ ] Every shareholder has signed (Column K)
- [ ] Every shareholder has provided SSN/ITIN/EIN (Column N)
- [ ] Total ownership in Column M sums to 100%
- [ ] In community-property states, non-owner spouses have signed

### Form completeness checks

- [ ] Lines A-I all completed
- [ ] Tax year box (Line H) is checked exactly once
- [ ] If non-calendar (H Box 2/3/4), Part II is completed
- [ ] If late filing, Part IV is completed and "FILED PURSUANT TO REV. PROC. 2013-30" written across top
- [ ] If QSST shareholder, Part III is completed for that trust

### Sanity warnings (do not block)

- [ ] Effective date is more than 1 year in the past → unusual; verify the user wants this
- [ ] Reasonable salary projected to be <30% of net profit → flag risk of IRS reclassification (Watson v. Commissioner)
- [ ] Reasonable salary projected to be >100% of net profit → mathematically impossible to draw distributions; question whether election makes sense
- [ ] Single shareholder is a non-resident alien → ineligible; STOP
- [ ] Operating agreement contains "preferred return" or "waterfall" language → potential one-class-of-stock violation; require operating agreement review

### Cross-form checks

- [ ] User informed about Form 1120-S annual filing requirement
- [ ] User informed about Form 941 quarterly payroll filings
- [ ] User informed about Form 940 annual FUTA
- [ ] User informed about W-2 issuance to shareholder-employee
- [ ] User informed about state-level S-corp election (if state requires separate)
- [ ] User has chosen a payroll provider before the election effective date

---

## Output format

The agent's deliverable is a filled draft + filing instructions:

```markdown
# Form 2553 — DRAFT Election by a Small Business Corporation

## Header
Filed pursuant to Rev. Proc. 2013-30  [only if late]

## Part I — Election Information

A. Name of corporation:               <name>
B. Address:                           <street, city, state, zip>
C. Employer Identification Number:    <EIN>
D. Date incorporated:                 MM/DD/YYYY
E. State of incorporation:            <XX>
F. Election effective date:           MM/DD/YYYY
G. Name change:                       <yes/no>
H. Tax year:
   [X] (1) Calendar year, OR
   [ ] (2) Fiscal year ending MM/DD, OR
   [ ] (3) 52-53 week year, OR
   [ ] (4) Other (see Part II)
I. Number of shareholders at time of election: <N>
   Officer signature: <name>
   Officer title:     <title>
   Date signed:       MM/DD/YYYY

## Shareholder Consent Statement

| # | J. Name & address | K. Signature | L. Date | M. Shares (or %) and dates acquired | N. SSN/EIN |
|---|-------------------|--------------|---------|--------------------------------------|------------|
| 1 | ...               | ...          | ...     | ...                                  | ...        |

(Plus non-owner spouse rows for community-property states.)

## Part II — Fiscal Year (if applicable)

Reason for fiscal year: <natural business year | ownership | business purpose | §444>
Supporting facts: <brief description>

## Part III — QSST Election (if applicable)

[Only if a Qualified Subchapter S Trust is a shareholder]
Trust name and EIN: <...>
Beneficiary name and SSN: <...>
Date stock transferred to trust: MM/DD/YYYY

## Part IV — Late Election Relief (if applicable)

[X] (1) Election filed pursuant to Rev. Proc. 2013-30
[X] (2) Failure to file timely was inadvertent
[X] (3) Reasonable cause exists

Reasonable cause statement: <2-4 sentence explanation>

## Filing instructions

- Service center: <address> (verify on Form 2553 instructions p. 4 for current year)
- Method: Fax to <fax number> [preferred] OR mail Certified Mail with Return Receipt
- Filing date: MM/DD/YYYY
- Expected acknowledgment: CP261 letter within 60 days
- If no CP261 by Day 60: call IRS Business & Specialty line at 800-829-4933

## Required follow-up filings

- [ ] State-level S-corp election (see references/state-conformity.md)
- [ ] Set up payroll provider before election effective date
- [ ] Form 941 quarterly (Apr 30, Jul 31, Oct 31, Jan 31)
- [ ] Form 940 annual (Jan 31)
- [ ] W-2 to shareholder-employee (Jan 31)
- [ ] Form 1120-S annual (March 15, or Sep 15 with extension)

## Validation summary

- Eligibility: <pass | list failures>
- Timing: on-time | late under Rev. Proc. 2013-30 | beyond 3-year 75-day window
- Consents: <N of N collected>
- Math: <pass | list issues>
- Sanity warnings: <list>

## Sources cited in this draft

- IRS Form 2553 (revision date YYYY-MM)
- IRS Instructions for Form 2553 (revision date YYYY-MM)
- IRC §1361(b), §1362(a), §1362(b)
- Reg. §1.1361-1(l), §1.1362-6
- Rev. Proc. 2013-30 (if late filing)
- Rev. Proc. 2006-46 (if natural business year claimed in Part II)
```

The draft is **not** the final filed form — the user (or agent under explicit consent in `filing.md`) must transcribe to the IRS PDF and fax or mail.

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every box on Form 2553 Parts I-IV with examples
- [`references/eligibility.md`](./references/eligibility.md) — IRC §1361 eligibility detailed: shareholder types, one-class-of-stock rule, ineligible corporation classes
- [`references/timing-rules.md`](./references/timing-rules.md) — When the 2-month-15-day clock starts; Rev. Proc. 2013-30 late relief mechanics
- [`references/reasonable-salary.md`](./references/reasonable-salary.md) — IRS factors test (Watson v. Commissioner, Rev. Rul. 74-44); BLS OES wage data approach
- [`references/state-conformity.md`](./references/state-conformity.md) — States requiring separate S-corp election (CA, NY, NJ, AR, WI) and rate/form details
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top 8 mistakes that void elections or trigger reclassification
- [`filing.md`](./filing.md) — Browser-automation playbook: fax vs mail decision tree, CP261 follow-up, state filings

## Examples

End-to-end worked elections.

- [`examples/consulting-llc-on-time.md`](./examples/consulting-llc-on-time.md) — Single-member LLC, $150K profit, on-time election, $80K reasonable salary
- [`examples/late-election-with-relief.md`](./examples/late-election-with-relief.md) — LLC formed 2024, missed deadline, retroactive election via Rev. Proc. 2013-30 in 2026
- [`examples/multi-member-llc-electing-scorp.md`](./examples/multi-member-llc-electing-scorp.md) — 2-member LLC (50/50) electing S-corp, both members consent, operating agreement amended for one-class-of-stock

## Sources

Authoritative sources used by this skill. Re-verify each year — the IRS revises Form 2553 and instructions periodically.

- [Form 2553 (latest)](https://www.irs.gov/pub/irs-pdf/f2553.pdf) — the form itself
- [Instructions for Form 2553 (latest)](https://www.irs.gov/pub/irs-pdf/i2553.pdf) — line-by-line IRS guidance, service center addresses page 4
- [About Form 2553](https://www.irs.gov/forms-pubs/about-form-2553) — IRS landing page
- [Form 1120-S](https://www.irs.gov/pub/irs-pdf/f1120s.pdf) — annual S-corp return (downstream)
- [Publication 542](https://www.irs.gov/publications/p542) — Corporations
- [Publication 15 (Circular E)](https://www.irs.gov/publications/p15) — Employer's Tax Guide
- IRC §1361 (S-corp eligibility)
- IRC §1362 (election, revocation, termination)
- IRC §3121 (FICA tax definitions)
- Reg. §1.1361-1(l) — One-class-of-stock rule
- Reg. §1.1362-6 — Election filing requirements
- Reg. §301.9100-3 — Discretionary 9100 relief (last-resort late filing)
- Rev. Proc. 2013-30 — Late S-corp election relief
- Rev. Proc. 2006-46 — Natural business year procedure
- Rev. Rul. 74-44 — Reasonable compensation framework
- *Watson v. Commissioner*, 668 F.3d 1008 (8th Cir. 2012) — reasonable-salary case law
- Bureau of Labor Statistics OES — wage data for reasonable-salary analysis (https://www.bls.gov/oes/)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms, publications, and case law. It is not tax or legal advice. S-corp election has consequences across federal tax, state tax, payroll compliance, and shareholder estate planning. The agent invoking this skill should remind the user that the output is a starting point and that complex situations (multi-state operations, shareholder buy-sell agreements, anticipated changes in ownership) warrant a licensed CPA or tax attorney's review.
