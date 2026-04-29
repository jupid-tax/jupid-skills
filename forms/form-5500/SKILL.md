---
name: form-5500
description: >
  Use this skill when an employer / plan administrator must file the annual
  Form 5500 series (Form 5500, Form 5500-SF, or Form 5500-EZ) reporting
  information about a retirement plan (401(k), defined benefit, profit-sharing)
  or large welfare plan (health/dental with 100+ participants) under ERISA and
  the Internal Revenue Code. Triggers on phrases like "Form 5500", "5500-EZ
  solo 401(k)", "5500-SF small plan", "retirement plan annual return", "ERISA
  reporting", "401(k) Form 5500", "5500 due date", "5500 extension Form 5558",
  "EFAST2 filing", "DFVC delinquent filer". Do NOT use for: SEP-IRA or SIMPLE
  IRA plans (no 5500 required — IRA-based, not ERISA plans); a one-participant
  plan with assets < $250,000 at year-end and not in final year (5500-EZ
  exempt under IRC §6058(a)); welfare plans with < 100 participants that are
  unfunded, fully insured, or a combination (exempt under DOL Reg.
  29 CFR §2520.104-20); governmental plans, church plans (generally exempt
  from Title I ERISA reporting); plans terminating but not yet distributed
  (file final 5500 once assets fully distributed).
form: Form 5500 series (5500, 5500-SF, 5500-EZ)
audience: [employer, scorp]
tax_year: 2026
last_verified: 2026-04-29
official_form: https://www.irs.gov/pub/irs-pdf/f5500ez.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i5500ez.pdf
---

# Form 5500 — Annual Return/Report of Employee Benefit Plan

This skill produces an audit-grade draft of the appropriate Form 5500 variant from the plan's year-end facts: participant count, assets, contributions, distributions, plan provisions, and (for large plans) audited financial statements. It walks through variant selection, line-by-line entries, applicable schedules, and validation, then emits a deliverable the plan administrator can transcribe to EFAST2 (electronic filing system for 5500/5500-SF) or to paper for 5500-EZ.

The math is mechanical given clean financials. The judgment is in *which variant applies* (5500 vs. 5500-SF vs. 5500-EZ — a wrong pick triggers DOL rejection or audit), *whether an audit attaches* (large plans 100+ participants), *which schedules attach*, and *whether the plan even needs to file* (welfare plan exemptions, IRA-based plan exclusion). This skill optimizes for the latter — the agent should ask, not guess.

> **No Jupid blog companion exists for Form 5500 yet.** This skill stands alone for now. When a blog companion is published, link it here.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 5500, 5500-SF, 5500-EZ, EFAST2, or DFVC
- The user is a plan sponsor or administrator and the plan year is closing / has closed
- The user mentions a 401(k), profit-sharing plan, defined benefit / pension plan, ESOP, money purchase plan, or 403(b) ERISA plan
- The user mentions a large welfare plan: group health, dental, vision, life, or disability with 100+ participants
- The user describes a solo 401(k) ("solo K", "individual 401k", "owner-only plan") and is unsure whether they need to file
- The user just received a DOL letter about delinquent 5500 and asks how to fix (→ DFVC path)

Do **not** engage this skill when:

- The plan is a **SEP-IRA or SIMPLE IRA** — these are IRA-based plans, not ERISA pension plans, and have no Form 5500 obligation. (SEP plans use Form 5305-SEP / 5305A-SEP for adoption; SIMPLE plans use Form 5304-SIMPLE / 5305-SIMPLE. Annual reporting is via the IRA custodian's Form 5498, not the employer.)
- The plan is a **one-participant 401(k) with year-end assets < $250,000** AND it is not the final year of the plan — the 5500-EZ filing is **not required** under IRC §6058(a) (one-participant plan exception).
- The plan is a **welfare plan with < 100 participants** that is unfunded (paid from general assets), fully insured, or a combination — exempt from Form 5500 under DOL Reg. 29 CFR §2520.104-20.
- The plan is a **governmental plan** (state, local, federal employee plans) — exempt from Title I of ERISA, no Form 5500 (with limited exceptions for IRC §401(a)(26) reporting).
- The plan is a **church plan** that has not elected ERISA coverage under IRC §410(d) — exempt.
- The plan is a **fringe-benefit plan** like a §125 cafeteria plan — these have separate reporting (Form 5500 doesn't apply unless the underlying welfare plan crosses 100 participants).
- The user wants help with **plan termination distributions** themselves — that's a separate flow (loan offsets, rollovers, 1099-R, lump-sum distributions). Form 5500 reports the year of termination but isn't the distribution mechanism.

If the plan type is ambiguous, ask before proceeding. Common confusion points:

- **"Solo 401(k)" with two participants** (owner + spouse who is a co-owner): still qualifies as one-participant plan if both are 100% owners or sole proprietors with spouse — but read IRS Pub. 560 carefully. Adding a non-owner W-2 employee converts to a regular 401(k) plan and 5500-SF / 5500 applies (no longer 5500-EZ).
- **SEP-IRA mistakenly called "SEP plan"**: SEP-IRA doesn't file 5500 *ever*. If the user says "I have a SEP", confirm they mean SEP-IRA (no 5500) or a true qualified profit-sharing plan (5500 applies).
- **403(b) plans**: Public school / governmental 403(b) plans are exempt; ERISA 403(b) plans (most non-governmental, non-church 403(b) plans where the employer makes contributions or has discretionary involvement) file 5500.

For adjacent skills:
- For SEP / SIMPLE IRA setup → forthcoming `form-5305-sep` skill
- For solo 401(k) plan termination distribution → forthcoming `form-1099-r` skill
- For 401(k) plan corrections / VCP / EPCRS → forthcoming `epcrs-correction` skill

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

### Plan identity (required for all variants)

1. **Plan year being reported** — usually calendar year (Jan 1 – Dec 31). Plan year drives the due date.
2. **Plan name** — exact name from plan document.
3. **Plan number (PN)** — three-digit number (001 for first pension plan, 501 for first welfare plan; subsequent plans use 002, 003, etc.). This is set in the plan document and must remain consistent year over year.
4. **Plan sponsor's legal name** (business name) and **EIN**.
5. **Plan administrator's name + EIN** (often same as sponsor).
6. **Plan effective date** (when the plan first existed).

### Plan facts (required to pick variant)

7. **Plan type**: Pension/retirement (defined contribution like 401(k), or defined benefit) OR welfare (health, dental, life, disability).
8. **Participant count at the beginning of the plan year**. For pension plans, includes active employees, retirees with vested benefits, and beneficiaries receiving benefits.
9. **Participant count at the end of the plan year**.
10. **Year-end plan assets** (for pension plans) — total fair-market value.
11. **Is this a one-participant plan?** Owner-only or owner + spouse? If yes, 5500-EZ likely applies.
12. **Does the plan invest only in eligible assets?** (Mutual funds, registered investments, employer stock if publicly traded.) If yes, may qualify for 5500-SF; if no (real estate, private equity, hard-to-value), full 5500 + Schedule H.

### For Form 5500 large plans (100+ participants)

13. **Audited financial statements** — required attachment from an Independent Qualified Public Accountant (IQPA). The audit takes 4-12 weeks; start early.
14. **Trustee / custodian info** — name, EIN, address.
15. **Investment manager(s)** if any — Form ADV registration if §3(38) ERISA fiduciary.

### For welfare plans

16. **Funding type**: Funded through trust, fully insured (premiums paid to insurance carrier), unfunded (paid from employer general assets), or combination.
17. **Number of participants on first day of plan year** — drives the 100-participant test for filing requirement.

### For Form 5558 extension

18. **Original due date** + the desired extended due date (max 2.5 months extension).
19. **Plan year being extended** + plan number.

For DFVC (delinquent filer) program, additionally ask:
- Year(s) of delinquent filings
- Whether the DOL has already sent a letter (if yes, DFVC may not be available — full late-filing penalty applies)

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Determine if filing is required

Use this decision flow:

```
Is the plan an IRA-based plan (SEP-IRA, SIMPLE IRA)?
  → No 5500 required. Stop. (Custodian handles annual 5498 for participants.)

Is the plan a governmental or non-electing church plan?
  → No 5500 required (with narrow exceptions). Stop.

Is this a one-participant plan (owner + spouse only, no non-owner employees)?
  → Are year-end assets ≥ $250,000 OR is this the final plan year?
    → Yes: file 5500-EZ
    → No: NOT required to file (IRS Notice 2011-31; IRC §6058(a) exception)

Is this a welfare plan with < 100 participants on first day?
  → Is the plan funded (trust holds assets)?
    → Yes: must file 5500-SF or 5500
    → No (unfunded, fully insured, or combo): exempt under 29 CFR §2520.104-20

Is this a pension plan with < 100 participants AND limited to "eligible plan assets" with no employer securities (other than publicly traded)?
  → Eligible for 5500-SF (small plan, simplified)

Is this a pension plan with 100+ participants OR with non-eligible assets?
  → Must file full 5500 + Schedule H + audited financials
```

See [`references/variant-selection.md`](./references/variant-selection.md) for full decision tree with edge cases.

### Step 2 — Confirm plan type and variant

Confirm with the user. The most common mistake is filing the wrong variant — if the user thinks they're a 5500-EZ filer but actually has a non-spouse employee on the plan, they're a 5500-SF filer and 5500-EZ filing causes EFAST2 rejection.

### Step 3 — Gather year-end financial data

Build the master plan-financial table for the year:

```
| Item                                        | Amount    |
|---------------------------------------------|-----------|
| Beginning of year assets                    | $X,XXX,XXX |
| Employer contributions                      | $X,XXX,XXX |
| Employee contributions (deferrals)          | $X,XXX,XXX |
| Rollovers in                                | $X,XXX,XXX |
| Investment earnings (gains/losses, dividends, interest) | $X,XXX,XXX |
| Benefit payments / distributions out        | $X,XXX,XXX |
| Administrative expenses                     | $X,XXX,XXX |
| End of year assets                          | $X,XXX,XXX |
```

For Schedule H (large plans), much more detail is required — see [`references/schedules.md`](./references/schedules.md).

### Step 4 — Determine which schedules attach

Different schedules apply based on variant + plan type:

| Schedule | Purpose | Required when |
|----------|---------|--------------|
| Schedule A | Insurance contract info | Welfare or pension plan with insurance contract |
| Schedule C | Service provider compensation | Large plan with provider compensation > $5,000 |
| Schedule D | Plan participation in a master trust / DFE | Plan invests in master trust, CCT, PSA, etc. |
| Schedule G | Financial transactions (loans, fixed-income, leases) | Large plans with reportable transactions |
| Schedule H | Large plan financial info (audited) | Pension/welfare with 100+ participants |
| Schedule I | Small plan financial info (unaudited) | Small pension plan that doesn't qualify for 5500-SF |
| Schedule MB / SB | Multiemployer / single-employer DB actuarial info | Defined benefit plans |
| Schedule R | Retirement plan info (vesting, ADP/ACP test, distributions) | Pension plans |
| Schedule SB | Single-employer DB actuarial cert | DB plans only |

Form 5500-SF and 5500-EZ are self-contained (no schedules). Form 5500 always has at least Schedule H or I.

See [`references/schedules.md`](./references/schedules.md).

### Step 5 — Fill the form line by line

For 5500-EZ, see [`references/line-by-line.md`](./references/line-by-line.md) — the 5500-EZ has ~25 numbered items.
For 5500-SF, similar structure with more financial detail.
For full 5500, the line-by-line is in the IRS / DOL instructions; the agent should pull data from the financials and Schedule H (or I) into the form's summary lines.

### Step 6 — For large plans — coordinate the audit

If the plan has 100+ participants, the financials must be audited by an Independent Qualified Public Accountant (IQPA) under DOL Reg. 29 CFR §2520.103-1. The audit report attaches to Schedule H.

The auditor needs:
- Trial balance and general ledger
- Trust statements (year-end balances, reconciliations)
- Participant data (eligibility, contributions, vesting)
- Plan document and amendments
- Prior year 5500 + audit report
- Service provider invoices
- Loan and distribution records

Audit takes 4-12 weeks. **Start before plan year ends** if filing on extension is undesired.

### Step 7 — File Form 5558 if needing extension

Form 5558 grants a **2½-month extension** (one-time, automatic if filed by original due date). For calendar-year plans, original due date is July 31; extension pushes to October 15.

Form 5558 is paper-mailed to the IRS. Must be filed **by the original due date** to be effective. Late Form 5558 = no extension.

### Step 8 — Run validation checks

See **Validation** below.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off downstream

State next forms / actions:

- **Distribute SAR (Summary Annual Report)** to participants within 9 months after plan year end (calendar plan: by September 30 of the year after). Required for 5500 / 5500-SF; not for 5500-EZ. Plan administrator obligation under ERISA §104(b)(3).
- **PBGC premium filing (Form PRM, defined benefit only)** — separate from 5500.
- **Provide participants with annual statement** of account balances (defined contribution plans) — separate from 5500.
- **State filings** — some states have parallel reporting (rare for retirement plans; common for welfare plans).
- **Audit follow-up** — if the IQPA found findings, address before next plan year.

### Step 11 — File the return (optional)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- Channel decision tree (EFAST2 for 5500/5500-SF, paper or IRS-fillable PDF for 5500-EZ)
- EFAST2 credentials setup (signer + filer credentials)
- Field-by-field mapping
- Pre-flight checklist
- Submission state machine
- Security rules — never store EFAST2 credentials in agent logs

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

The three variants share many lines but differ in detail. The 5500-EZ is the simplest (~25 items); 5500-SF is medium; full 5500 is the most complex (with all schedules).

### Form header (all variants)

- **Plan year** — beginning and ending dates
- **Type of return** — first return, amended, final, short plan year (less than 12 months)
- **Plan number** — 001-099 for pension, 501-599 for welfare. Consistent year over year.
- **Plan name** — exact match to plan document
- **Sponsor's name + EIN + address**
- **Administrator's name + EIN + address** (often same)

### Participant counts

- **Active participants** — currently employed and accruing benefits
- **Retired / separated participants with vested benefits** — former employees with account balances
- **Beneficiaries receiving benefits**
- **Total** — sum

The 100-participant threshold for "large plan" status is tested on the **first day** of the plan year (with rare exception for short years).

### Plan characteristics codes

A list of codes (e.g., 2J for safe harbor 401(k); 3D for plan with employer matching) describing plan provisions. Pulled from the plan document.

### Financial info (varies by variant)

- 5500-EZ: simple 3-line totals
- 5500-SF: ~10 financial lines
- 5500 + Schedule H: ~50+ lines with detailed asset categorization

### Compliance questions

Yes/no questions:
- Late deferrals? (5500-SF / 5500 lines 10a / 10b — DOL hot button)
- Plan loans? Defaults? Prohibited transactions?
- IQPA audit performed? (large plans only)
- Insurance contracts? (drives Schedule A)

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] End-of-year assets = beginning-of-year + contributions + investment earnings − distributions − admin expenses (the "rollforward" equation)
- [ ] Total participants = active + retired/separated + beneficiaries
- [ ] If 5500-EZ: assets ≥ $250,000 to be required (or final year)
- [ ] If 5500-SF: participant count < 100 AND eligible-asset test met
- [ ] Schedule H rollforward (if attached) ties to 5500 main form summary

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Participant count grew by > 50% year-over-year — verify business growth or merger
- [ ] Year-end assets dropped by > 20% but no large distribution — investigate (audit issue, market loss?)
- [ ] Late-deferral question answered "Yes" — DOL flag; ensure VFCP correction filed and 15% excise tax computed (Form 5330)
- [ ] No employer contributions reported but plan document requires — check whether employer skipped a year (could be plan failure)
- [ ] Plan number changed from prior year — IRS / DOL will flag; plan numbers stay constant unless plan terminates and re-creates
- [ ] First-time filer for a plan that's been in existence multiple years — DFVC may apply for prior years
- [ ] Schedule A indicates insurance contract but no insurance company filed Schedule A info — verify contract exists
- [ ] Plan termination indicated but assets not zero — terminations require full distribution before final filing
- [ ] Final 5500-EZ but plan still has assets — clarify: was termination effective, are distributions in process?

### Cross-form / cross-year checks

- [ ] EIN matches prior 5500 (and matches plan sponsor's other tax filings)
- [ ] Beginning of year assets = prior year's ending assets (else explain in Schedule H footnote)
- [ ] Plan number consistent with prior year
- [ ] Effective date consistent with prior year
- [ ] Plan administrator on file with DOL matches form filing
- [ ] If audit required (100+), Schedule H + IQPA report attached
- [ ] If insurance contracts, Schedule A attached
- [ ] If service providers > $5,000, Schedule C attached (large plans)

---

## Output format

The agent's deliverable depends on variant. Below is the 5500-EZ template (simplest); 5500-SF and full 5500 use longer templates filled from same data.

```markdown
# Form 5500-EZ — DRAFT for Plan Year YYYY

## Header
Plan year:                   01/01/YYYY – 12/31/YYYY
Type of return:              [ ] First [ ] Amended [ ] Final [ ] Short year
Plan number:                 001
Plan name:                   <full legal name from plan document>
Plan effective date:         MM/DD/YYYY

## Plan sponsor / administrator
Sponsor name:                <legal business name>
Sponsor EIN:                 XX-XXXXXXX
Sponsor address:             <full address>
Plan administrator:          [X] Same as sponsor  [ ] Other: __________

## Participants
Beginning of plan year:      X
End of plan year:            X
Active participants:         X
Retired or separated:        X
Beneficiaries receiving:     X

## Plan characteristics codes
<list of 2-letter codes from plan document>

## Plan assets and liabilities (end of year)
Total plan assets:           $XXX,XXX
Total plan liabilities:      $X,XXX (loans, accrued expenses)
Net plan assets:             $XXX,XXX

## Income, expenses, and changes
Total income (contributions + earnings): $XXX,XXX
Total expenses (distributions + admin):  $XXX,XXX
Net change in plan assets:               $XXX,XXX

## Compliance questions
Did the plan have any of:
  Loans to participants > 0:           [ ] Yes  [ ] No
  In-kind contributions:               [ ] Yes  [ ] No
  Distributions other than rollovers:  [ ] Yes  [ ] No
Other: <as required>

## Sign here
Plan administrator name:     __________
Title:                       __________
Date:                        __________
Signature:                   __________

## Required attachments / next actions
- [ ] None required for 5500-EZ (self-contained)
- [ ] If filed paper: mail to IRS Ogden address
- [ ] Distribute Summary Annual Report by September 30 of the year following — N/A for 5500-EZ filers (one-participant plans exempt from SAR)

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 10>

## Sources cited in this draft
- IRS Form 5500-EZ (latest revision)
- IRS Instructions for Form 5500-EZ (latest revision)
- IRC §6058 (information required of certain plans)
- ERISA §103, §104 (annual reporting and disclosure)
- 29 CFR §2520.104-20 (welfare plan exemption — N/A here, retirement plan)
- IRS Notice 2011-31 (one-participant plan filing threshold $250,000)
```

For 5500-SF / full 5500, see [`references/line-by-line.md`](./references/line-by-line.md) for the longer template.

The draft is **not** the final filed form. The plan administrator still has to file via EFAST2 (5500/5500-SF, electronic only) or paper-mail (5500-EZ, optional electronic via IRS FIRE / IRS portal).

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete table of every Form 5500 / 5500-SF / 5500-EZ line with examples and edge cases
- [`references/variant-selection.md`](./references/variant-selection.md) — Decision tree for picking 5500 vs. 5500-SF vs. 5500-EZ (vs. no filing at all); welfare plan exemptions; one-participant plan rules
- [`references/schedules.md`](./references/schedules.md) — Every Schedule (A, C, D, G, H, I, MB, SB, R) — what attaches when, what data is required, common errors
- [`references/dfvc-and-penalties.md`](./references/dfvc-and-penalties.md) — Late filing penalties, Delinquent Filer Voluntary Compliance program, IRS / DOL enforcement
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with examples and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook: how an agent files via EFAST2 (5500/5500-SF), via paper for 5500-EZ, or via the new IRS electronic 5500-EZ option

## Examples

End-to-end worked Form 5500 filings. Use these as patterns when the user's situation is similar.

- [`examples/solo-401k-300k-assets.md`](./examples/solo-401k-300k-assets.md) — Owner-only 401(k) with $300,000 year-end assets, 5500-EZ filing required, calendar plan year
- [`examples/50-employee-401k-sf.md`](./examples/50-employee-401k-sf.md) — Small 401(k) plan (50 active participants), eligible-asset test passes, 5500-SF filing
- [`examples/200-employee-large-plan.md`](./examples/200-employee-large-plan.md) — Mid-size 401(k) plan (200 active), full Form 5500 with Schedule H and audited financial statements

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS / DOL site for the plan year being filed — forms revise yearly.

- [Form 5500-EZ (latest)](https://www.irs.gov/pub/irs-pdf/f5500ez.pdf) — IRS-hosted PDF
- [Instructions for Form 5500-EZ](https://www.irs.gov/pub/irs-pdf/i5500ez.pdf) — IRS guidance
- [About Form 5500-EZ](https://www.irs.gov/forms-pubs/about-form-5500-ez) — IRS landing page
- [DOL Form 5500 portal](https://www.dol.gov/agencies/ebsa/employers-and-advisers/plan-administration-and-compliance/reporting-and-filing/form-5500) — Form 5500 / 5500-SF current-year forms and instructions
- [EFAST2 filing system](https://www.efast.dol.gov) — electronic filing portal for 5500 / 5500-SF
- [Form 5558 (extension)](https://www.irs.gov/pub/irs-pdf/f5558.pdf) — application for 2.5-month extension
- [Publication 560 (Retirement Plans for Small Business)](https://www.irs.gov/pub/irs-pdf/p560.pdf) — SEP, SIMPLE, qualified plan rules
- [Publication 963 (Federal-State Reference Guide)](https://www.irs.gov/pub/irs-pdf/p963.pdf) — governmental plan exclusions
- IRC §401(a) (qualified plan requirements)
- IRC §410, §411 (participation, vesting)
- IRC §6058(a) (information required by certain employee benefit plans)
- IRC §6652(e) (failure to file — IRS penalty $250/day, max $150,000 per IRC §6652(e); verify current adjustment)
- IRC §6058 / 6059 (filing requirements + actuarial info)
- ERISA §101, §103, §104 (annual reporting)
- ERISA §502(c)(2) (DOL penalty up to $2,739 per day for failure to file — verify current adjustment via 29 CFR §2575.502c-2)
- 29 CFR §2520.103-1 (annual reporting rules)
- 29 CFR §2520.103-1(c) (audit requirement for large plans)
- 29 CFR §2520.104-20 (small welfare plan exemption)
- 29 CFR §2520.104-44 (small plan filing simplification — basis for 5500-SF)
- IRS Notice 2011-31 (one-participant plan $250,000 filing threshold)
- DFVC Program (Delinquent Filer Voluntary Compliance) — DOL FAQ at https://www.dol.gov/agencies/ebsa/employers-and-advisers/plan-administration-and-compliance/reporting-and-filing/form-5500/dfvc-faqs

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS / DOL forms, publications, the Internal Revenue Code, and ERISA. It is not legal or tax advice and does not establish a CPA / attorney / enrolled agent relationship. The agent invoking this skill should remind the user that the output is a starting point and that complex situations (controlled groups, multiple-employer plans, defined benefit funding issues, prohibited transactions, DFVC navigation, plan termination distributions, IQPA findings) warrant a licensed ERISA attorney or third-party administrator's review.
