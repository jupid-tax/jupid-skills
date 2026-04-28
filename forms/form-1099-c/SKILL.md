---
name: form-1099-c
description: >
  Use this skill when an individual taxpayer has received a Form 1099-C
  (Cancellation of Debt) from a creditor and needs to determine whether and
  how to report the canceled debt on their tax return. Triggers on phrases
  like "I got a 1099-C", "canceled debt tax", "credit card debt forgiven
  taxes", "insolvency exclusion", "Form 982", "do I owe tax on canceled
  debt", "mortgage forgiveness tax", "settled credit card and got a tax
  form". Do NOT use for: ongoing business debt restructuring (separate
  workstream), Public Service Loan Forgiveness specifically (PSLF
  exclusion is automatic under §108(f)(1) and does not require Form 982),
  or partnership/S-corp debt cancellation at the entity level (those are
  reported on the entity return, not the individual 1040).
form: Form 1099-C (Cancellation of Debt) — informational; received not filed
audience: [individual, solo]
tax_year: 2026
last_verified: 2026-04-28
official_form: https://www.irs.gov/pub/irs-pdf/f1099c.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1099ac.pdf
---

# Form 1099-C — Cancellation of Debt (recipient guide)

This skill produces an audit-grade decision and reporting plan for an individual who has received a Form 1099-C from a creditor. The 1099-C is **informational** — the recipient does not file the 1099-C itself; they report the canceled debt as income on the 1040 series, **unless** an IRC §108 exclusion applies.

The judgment is in: (a) reading the form correctly, (b) testing every exclusion in the right order, (c) computing insolvency precisely if that's the path, and (d) routing the income to the correct place on the return (Schedule 1 Line 8c vs. Schedule C Line 6 vs. Schedule F).

The math is mechanical. The wrong answer most filers give is "default to taxable" — they pay tax on canceled debt that the Code lets them exclude. This skill exists to make that mistake impossible.

**Companion guide for end users:** [Form 1099-C (2026): Cancellation of Debt Tax Guide & Exclusions](https://jupid.com/blog/form-1099-c-cancellation-debt-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions a 1099-C, "cancellation of debt", "1099-C tax form", or "Form 982"
- The user describes a debt that was settled, written off, forgiven, or canceled (credit card settled for less than balance, mortgage forgiven in foreclosure or short sale, business debt forgiven by a vendor, student loan canceled, medical debt forgiven)
- The user asks "do I owe tax on canceled debt" or "is forgiven debt taxable"
- The user mentions receiving a tax form they don't recognize after settling a debt
- The user is testing whether they qualify for the insolvency exclusion

Do **not** engage this skill when:

- The user is a partnership, S-corp, or C-corp with entity-level debt cancellation → that goes on the entity return (Form 1065, 1120-S, or 1120), not on Form 1040
- The user has Public Service Loan Forgiveness (PSLF) only — PSLF is automatically excluded under IRC §108(f)(1) and does not require Form 982; flag the automatic exclusion and stop
- The user is restructuring ongoing business debt that has not yet been canceled — there's nothing to report until cancellation
- The user is in active bankruptcy proceedings that have not yet produced a discharge order — wait for the discharge

If the user's situation is ambiguous (e.g., they have both personal and business 1099-Cs), handle each 1099-C separately. Do not aggregate.

---

## Prerequisites

Before producing a reporting plan, the agent must have these eight inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the 1099-C is for (taken from Box 1 date). A 1099-C dated 2025 is reported on the 2025 return filed in 2026.
2. **Box 2 amount** — the canceled debt amount, in dollars.
3. **Box 6 identifiable event code** — A through I. This shapes the analysis.
4. **Box 4 debt description** — what the debt was (credit card, mortgage, auto loan, student loan, business loan, medical debt, other).
5. **Box 5** — was the borrower personally liable? (Yes/No.) Affects foreclosure analysis.
6. **Was the debt personal or business?** Routing depends on this. A sole proprietor's vendor debt is business; a credit card used for personal purchases is personal.
7. **Has the debtor filed bankruptcy?** If yes, get the chapter (7, 11, 13) and the discharge order date.
8. **Approximate financial position immediately before the cancellation date (Box 1)** — total liabilities, total fair market value of assets. This is required for the insolvency test. If the user can't ballpark, ask for: cash + checking, retirement balances, vehicle FMV, home FMV less mortgage, total credit card balances, total auto/personal loan balances, mortgage balance, student loan balance, the canceled debt itself at face value before cancellation.

For mortgage cancellation specifically, additionally ask:
- Was this the user's principal residence? (Required for §108(a)(1)(E) exclusion.)
- Was the debt acquisition indebtedness (used to buy/build/substantially improve), or was some portion home equity used for non-housing purposes?
- Total acquisition debt balance immediately before the cancellation.

For student loan cancellation, additionally ask:
- Federal or private loan?
- Reason for discharge (PSLF, teacher cancellation, death/disability, school closure, borrower defense, other)?
- Date of discharge — affects whether ARPA's 2021-2025 broad exclusion applies (verify 2026 extension status).

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm the 1099-C is the user's to report

The 1099-C should be addressed to the user (matching name + SSN/TIN in the recipient box). If the form is addressed to a different person (spouse, deceased relative, business entity), redirect:

- Spouse's 1099-C on a joint return → still report jointly, no redirect
- Deceased person's 1099-C → reported on the decedent's final return or the estate return (Form 1041), out of scope here
- Business entity's 1099-C → entity return (1065/1120-S/1120), redirect to the right skill

### Step 2 — Read the form

Build the internal record:

```
| Box | Field                              | Value             |
|-----|------------------------------------|-------------------|
| 1   | Date of identifiable event         | YYYY-MM-DD        |
| 2   | Amount of debt discharged          | $X,XXX            |
| 3   | Interest if included in Box 2      | $X,XXX            |
| 4   | Debt description                   | <credit card / mortgage / etc.> |
| 5   | Borrower personally liable?        | Yes / No          |
| 6   | Identifiable event code            | A | B | ... | I  |
| 7   | FMV of property                    | $X,XXX (if foreclosure) |
```

If Box 6 = A (bankruptcy), bankruptcy exclusion is the obvious path — confirm with the user that they have a Title 11 discharge order.

If Box 6 = E (probate), this is decedent-related and out of scope for individual reporting.

### Step 3 — Classify the debt as personal or business

Ask: "Was this debt incurred for personal purposes (consumer credit card, personal mortgage, personal auto loan, medical, personal student loan), or for a business you operate (vendor account, business loan, business credit card)?"

This determines the **default reporting line**:

- Personal → Schedule 1 Line 8c (cancellation of debt)
- Business (sole prop) → Schedule C Line 6 (other income)
- Business (farming) → Schedule F Line 8 (other income)

Write down the routing target before testing exclusions, so the agent doesn't lose track.

### Step 4 — Test exclusions in this order

The exclusions are stacked. The agent tests each in order; the **first** one that fully covers the canceled amount is the path. If none covers it fully, the unexcluded portion is taxable income on the routing target from Step 3.

#### 4a. Bankruptcy — IRC §108(a)(1)(A)

**Test:** Was the debt discharged in a Title 11 case (Chapter 7, 11, 12, or 13) where the discharge order has been entered?

**If yes:** Full exclusion. File Form 982 Box 1a. Line 2 = Box 2 amount. Apply attribute reduction per IRC §108(b).

Reference: [`references/bankruptcy-exclusion.md`](./references/bankruptcy-exclusion.md)

#### 4b. Insolvency — IRC §108(a)(1)(B)

**Test:** Was the user insolvent immediately before the cancellation (liabilities > FMV of assets)?

**Computation:** Run the Pub 4681 Worksheet 2 walkthrough in [`references/insolvency-test.md`](./references/insolvency-test.md). Output: insolvency amount in dollars (zero or positive).

**Exclusion amount:** min(canceled amount, insolvency amount). The exclusion is capped at insolvency.

**If full coverage:** File Form 982 Box 1b. Line 2 = excluded amount. Apply attribute reduction.

**If partial coverage:** The excluded portion goes on Form 982. The remaining portion (canceled − insolvency) goes on the routing target from Step 3 (Schedule 1 Line 8c, or Schedule C Line 6).

#### 4c. Qualified Principal Residence Indebtedness — IRC §108(a)(1)(E)

**Test:** Is the debt acquisition indebtedness on the user's principal residence?

**Limit:** $750,000 ($375,000 MFS).

**Year-aware:** This exclusion was extended through Dec 31, 2025. **Verify 2026 status** with the IRS before relying on it for tax year 2026 cancellations. Check https://www.irs.gov/forms-pubs/about-form-982 and recent legislative updates.

**If applies:** File Form 982 Box 1e. Line 10b reduces the basis of the principal residence by the excluded amount.

Reference: [`references/qualified-principal-residence.md`](./references/qualified-principal-residence.md)

#### 4d. Student Loan Discharge — IRC §108(f)

**Test categories (each independently sufficient):**

- PSLF discharge → automatic exclusion under §108(f)(1), **no Form 982 required**, just don't report the income. Flag this and stop.
- Teacher loan cancellation → automatic exclusion
- Death/total-and-permanent-disability discharge → automatic exclusion
- School closure / borrower defense discharge → automatic exclusion
- Other federal student loan discharge in tax years 2021-2025 under ARPA → broad exclusion under §108(f)(5). **Verify 2026 extension status before filing.**

For state tax purposes, some states tax forgiven student loans even when federally excluded. Flag this if the user mentions state tax.

Reference: [`references/student-loan-discharge.md`](./references/student-loan-discharge.md)

#### 4e. Qualified Farm Indebtedness — IRC §108(a)(1)(C)

For farmers. Specific tests on lender and gross receipts. Out of scope for the typical consumer 1099-C; if the user is a farmer with farm-related cancellation, see Pub 4681 Chapter 3 and consult a CPA.

#### 4f. Qualified Real Property Business Indebtedness — IRC §108(a)(1)(D)

For non-corporate taxpayers with depreciable real property used in a trade or business. Limited and reduces basis. See Pub 4681 Chapter 4.

### Step 5 — Determine the reporting path

Based on Step 4, the canceled amount falls into one of these buckets:

| Scenario | Form 982 box | Reporting target |
|----------|-------------|------------------|
| Bankruptcy fully covers | 1a | None (excluded) |
| Insolvency fully covers | 1b | None (excluded) |
| Insolvency partially covers | 1b (for excluded portion) | Routing target from Step 3 (for remainder) |
| Principal residence fully covers (and exclusion is in effect for tax year) | 1e | None (excluded), basis reduction on Line 10b |
| Student loan automatic exclusion (PSLF, teacher, death/disability, school closure) | None required | None (excluded) |
| Student loan ARPA broad exclusion (verify year) | 1e or per current instructions | None (excluded) |
| No exclusion applies, personal debt | None | Schedule 1 Line 8c |
| No exclusion applies, sole-prop business debt | None | Schedule C Line 6 |
| No exclusion applies, farming business debt | None | Schedule F Line 8 |

### Step 6 — Apply attribute reduction (Form 982 Part II)

If an exclusion is claimed via Form 982 (Boxes 1a, 1b, 1c, 1d, 1e), IRC §108(b) requires reducing the user's tax attributes in this order:

1. Net operating loss for the year of discharge → Form 982 Line 6
2. General business credit carryovers → Line 7
3. Minimum tax credits → Line 8
4. Capital loss carryovers → Line 9
5. Basis of property (depreciable first, then non-depreciable, then principal residence) → Lines 10a / 10b
6. Passive activity losses and credits → Line 11
7. Foreign tax credit carryovers → Line 12

For most consumer filers with no carryovers, attribute reduction is a non-event. Document this explicitly: "No attributes to reduce."

For users with NOLs or carryovers, work through the order with care; the reduction is the price of the exclusion.

### Step 7 — Run validation checks

See **Validation** below. Run every check.

### Step 8 — Produce the deliverable

See **Output format** below.

### Step 9 — Hand off downstream

State the next steps:

- If excluded fully → attach Form 982 to 1040
- If partially excluded → attach Form 982 + report remainder on Schedule 1/C/F
- If no exclusion → report on Schedule 1/C/F, no Form 982
- If business 1099-C → reminder that the income may flow into self-employment tax via Schedule SE
- If basis was reduced → record the basis adjustment in user's tax records for future sale of the property
- Recordkeeping reminder: keep the Pub 4681 Worksheet 2 and Form 982 with tax records for at least 3 years

### Step 10 — File the return (optional, if user authorizes)

If the user wants the agent to file, follow [`filing.md`](./filing.md). The 1099-C is informational so there's no separate filing channel for it; reporting happens through the 1040 e-file or paper return. Form 982 attaches to the 1040.

---

## Line-by-line guidance

For full reference, load [`references/1099-c-boxes.md`](./references/1099-c-boxes.md) for the form itself and [`references/form-982-walkthrough.md`](./references/form-982-walkthrough.md) for Form 982.

### 1099-C box rules (high level)

| Box | Use |
|-----|-----|
| 1 | Date determines tax year of reporting |
| 2 | The income amount (or excluded amount) |
| 3 | Interest portion (informational) |
| 4 | Description of debt — used to classify personal vs. business |
| 5 | Personal liability flag — relevant if foreclosure |
| 6 | Event code drives initial exclusion analysis (A=bankruptcy auto-flag) |
| 7 | FMV of property — used in foreclosure gain/loss analysis (separate Pub 4681 Chapter 2 procedure) |

### Form 982 high-level rules

- **Part I, Line 1a-1e** — check the box matching the exclusion claimed
- **Part I, Line 2** — total amount excluded
- **Part I, Line 3** — applies if §108(a)(1)(D) qualified real property business indebtedness
- **Part II, Lines 4-13** — required attribute reduction in the order specified above
- **Part III, Line 14** — only for §108(b)(5) election to apply reduction first to depreciable property basis

---

## Validation

Before declaring the plan ready, run these checks. Surface failures — don't silently fix.

### Math checks

- [ ] Box 2 amount agrees with the user's recollection of the canceled balance
- [ ] If insolvency claimed: liabilities − assets = insolvency amount, and excluded amount ≤ insolvency
- [ ] If insolvency partially covers: excluded amount + reported amount = Box 2
- [ ] Form 982 Line 2 = sum of exclusions claimed across boxes 1a-1e
- [ ] If basis reduction applied: Line 10a + Line 10b ≤ Line 2 of Form 982

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] User claims insolvency but did not include retirement accounts as assets → likely overstates insolvency; ask
- [ ] User claims insolvency but did not include the canceled debt itself in liabilities (at face value before cancellation) → likely understates liabilities; ask
- [ ] User has Box 6 = A but no bankruptcy discharge order → confirm the bankruptcy is final, not pending
- [ ] User has Box 6 = F (by agreement) on a credit card and is reporting as personal → confirm the card was not used for business
- [ ] User has multiple 1099-Cs in the same year → each tested separately; aggregate exclusions can compound
- [ ] User claims principal residence exclusion → verify the law is in effect for the tax year (extension status changes); flag for re-verification
- [ ] User claims student loan ARPA exclusion → verify the law is in effect for the tax year
- [ ] User received a 1099-A in addition to or instead of 1099-C (foreclosure abandonment) → different treatment; route to Pub 4681 Chapter 2
- [ ] Excluded amount > $100,000 and no Form 982 attached → impossible; Form 982 is required
- [ ] User reports business 1099-C on Schedule 1 instead of Schedule C → wrong line; redirect

### Cross-form checks

- [ ] If exclusion claimed → Form 982 must be attached to the 1040
- [ ] If business 1099-C → income flows into Schedule C Line 6 → may affect Schedule SE
- [ ] If basis of property reduced → user's records for the property must show the new basis; relevant on future sale

---

## Output format

The agent's deliverable is a **reporting plan** the user can transcribe to their 1040 / Schedule 1 / Schedule C / Form 982. Format:

```markdown
# Form 1099-C Reporting Plan — DRAFT for tax year YYYY

## 1099-C as reported by creditor
- Creditor: <name from form>
- Box 1 (date of event):           YYYY-MM-DD
- Box 2 (amount discharged):       $X,XXX
- Box 3 (interest in Box 2):       $X,XXX
- Box 4 (debt description):        <description>
- Box 5 (personally liable):       Yes | No
- Box 6 (event code):              <A | B | C | D | E | F | G | H | I>
- Box 7 (FMV of property):         $X,XXX (if applicable)

## Classification
- Debt type:                       Personal | Business (sole prop) | Business (farm)
- Default reporting target:        Schedule 1 Line 8c | Schedule C Line 6 | Schedule F Line 8

## Exclusion analysis
- Bankruptcy (§108(a)(1)(A)):      Applies | Does not apply | Reason
- Insolvency (§108(a)(1)(B)):
  - Liabilities immediately before: $X,XXX (itemized in worksheet)
  - Assets immediately before:      $X,XXX (itemized in worksheet)
  - Insolvency amount:              $X,XXX
  - Exclusion amount:               $X,XXX (min of insolvency, canceled)
- Principal residence (§108(a)(1)(E)): Applies | Does not apply | Reason | Year-status: <verified for YYYY>
- Student loan (§108(f)):          Applies | Does not apply | Sub-rule: <PSLF | teacher | disability | school closure | ARPA broad>
- Farm / business real property:   Applies | Does not apply

## Reporting outcome
- Excluded via Form 982:           $X,XXX (Box <1a/1b/1e> checked)
- Reported as income:              $X,XXX on <Schedule 1 Line 8c | Schedule C Line 6 | Schedule F Line 8>
- Federal tax estimate at marginal rate: $X,XXX

## Form 982 draft (if exclusion claimed)
- Part I:
  - Box 1a (Title 11):             ☐ | ☑
  - Box 1b (insolvency):           ☐ | ☑
  - Box 1c (qualified farm):       ☐ | ☑
  - Box 1d (qualified real prop):  ☐ | ☑
  - Box 1e (principal residence):  ☐ | ☑
  - Line 2 (amount excluded):      $X,XXX
- Part II — attribute reduction:
  - Line 6 (NOL):                  $X,XXX
  - Line 7 (general business cr.): $X,XXX
  - Line 8 (minimum tax credits):  $X,XXX
  - Line 9 (capital loss carryov.): $X,XXX
  - Line 10a (basis non-deprec.):  $X,XXX
  - Line 10b (basis prin. res.):   $X,XXX
  - Line 11 (passive activity):    $X,XXX
  - Line 12 (foreign tax credits): $X,XXX
- "None — no attributes to reduce" if applicable

## Required attachments
- [ ] Form 982 (if any exclusion claimed)
- [ ] Worksheet 2 from Pub 4681 (kept in records, not filed) if insolvency claimed

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list warnings raised>
- Year-aware flags: <principal residence / ARPA student loan extension status verified for YYYY>
- Next steps: <handoff items from Step 9>

## Sources cited in this plan
- IRC §61(a)(11), §108(a)–(f), §108(b)
- IRS Pub 4681 (revision date YYYY-MM-DD)
- Form 982 (revision date YYYY-MM-DD)
- Form 1099-C and Instructions for 1099-A and 1099-C (revision date YYYY-MM-DD)
- (any other authority used)
```

The plan is **not** the final filed return. The user transcribes Form 982 to their 1040 e-file software or paper return. The plan's value is that every step is computed and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/1099-c-boxes.md`](./references/1099-c-boxes.md) — Box-by-box explanation of every field on Form 1099-C
- [`references/insolvency-test.md`](./references/insolvency-test.md) — Pub 4681 Worksheet 2 walkthrough; what counts as asset / liability; retirement inclusion
- [`references/bankruptcy-exclusion.md`](./references/bankruptcy-exclusion.md) — Title 11 cases; timing of discharge order
- [`references/student-loan-discharge.md`](./references/student-loan-discharge.md) — ARPA temporary federal exclusion 2021-2025; PSLF; teacher cancellation; year-aware status
- [`references/qualified-principal-residence.md`](./references/qualified-principal-residence.md) — §108(a)(1)(E); $750k limit; extension history; year-aware status
- [`references/form-982-walkthrough.md`](./references/form-982-walkthrough.md) — line-by-line of Form 982
- [`references/common-mistakes.md`](./references/common-mistakes.md) — top filer mistakes
- [`filing.md`](./filing.md) — reporting via 1040 e-file or paper, Form 982 attachment rules

## Examples

End-to-end worked 1099-C scenarios. Use these as patterns when the user's situation is similar.

- [`examples/credit-card-settled-with-insolvency.md`](./examples/credit-card-settled-with-insolvency.md) — Personal credit card, negotiated settlement, insolvency exclusion
- [`examples/mortgage-foreclosure-with-residence-exclusion.md`](./examples/mortgage-foreclosure-with-residence-exclusion.md) — Principal residence mortgage forgiven in foreclosure, §108(a)(1)(E)
- [`examples/business-debt-canceled-on-schedule-c.md`](./examples/business-debt-canceled-on-schedule-c.md) — Sole proprietor's vendor debt forgiven, Schedule C Line 6 routing, no exclusion

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being reported.

- [Form 1099-C Cancellation of Debt Tax Guide & Exclusions](https://jupid.com/blog/form-1099-c-cancellation-debt-2026) — Jupid's narrative companion for human readers
- [About Form 1099-C](https://www.irs.gov/forms-pubs/about-form-1099-c) — IRS landing page
- [Form 1099-C (PDF)](https://www.irs.gov/pub/irs-pdf/f1099c.pdf) — the form itself
- [Instructions for Forms 1099-A and 1099-C](https://www.irs.gov/pub/irs-pdf/i1099ac.pdf) — line-by-line IRS guidance
- [Form 982 (PDF)](https://www.irs.gov/pub/irs-pdf/f982.pdf) — Reduction of Tax Attributes Due to Discharge of Indebtedness
- [Instructions for Form 982](https://www.irs.gov/pub/irs-pdf/i982.pdf)
- [Publication 4681](https://www.irs.gov/publications/p4681) — Canceled Debts, Foreclosures, Repossessions, and Abandonments
- [Publication 525](https://www.irs.gov/publications/p525) — Taxable and Nontaxable Income (canceled debts chapter)
- IRC §61(a)(11) (canceled debt = income)
- IRC §108(a)–(f) (exclusions)
- IRC §108(b) (attribute reduction)
- Treas. Reg. §1.6050P-1 (creditor reporting)
- Rev. Rul. 92-53 (retirement accounts as assets in insolvency test)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user that the §108(a)(1)(E) qualified principal residence exclusion and the §108(f)(5) ARPA student loan exclusion both have sunset dates that require year-by-year verification. The output is a starting point and complex situations (multiple 1099-Cs, foreclosure with both 1099-A and 1099-C, partial insolvency) warrant a licensed tax professional's review.
