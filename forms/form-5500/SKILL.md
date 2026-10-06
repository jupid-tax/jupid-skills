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
  plan whose year-end assets (all one-participant plans of the employer
  combined) do not exceed $250,000 and that is not in its final year (5500-EZ
  instructions, Who Does Not Have To File); welfare plans with < 100 participants that are
  unfunded, fully insured, or a combination (exempt under DOL Reg.
  29 CFR §2520.104-20); governmental plans, church plans (generally exempt
  from Title I ERISA reporting); plans terminating but not yet distributed
  (file final 5500 once assets fully distributed).
form: Form 5500 series (5500, 5500-SF, 5500-EZ)
audience: [employer, scorp, solo, llc1, partnership]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f5500ez.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i5500ez.pdf
---

# Form 5500 — Annual Return/Report of Employee Benefit Plan

This skill produces an audit-grade draft of the appropriate Form 5500 variant from the plan's year-end facts: participant count, assets, contributions, distributions, plan provisions, and (for large plans) audited financial statements. It walks through variant selection, line-by-line entries, applicable schedules, and validation, then emits a deliverable the plan administrator can transcribe to EFAST2 (electronic filing system for 5500/5500-SF) or to paper for 5500-EZ.

Line maps verified against the 2025 Form 5500, 2025 Form 5500-SF and Schedules H and I (DOL/IRS/PBGC, for plan years beginning in 2025, filed in 2026), the 2025 Form 5500-EZ (IRS), and Form 5558 (Rev. January 2025). Before using this skill for a 2026 plan year, re-check the 2026 forms at https://www.dol.gov/agencies/ebsa/employers-and-advisers/plan-administration-and-compliance/reporting-and-filing/form-5500 and https://www.irs.gov/forms-pubs/about-form-5500-ez.

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
- The plan is a **one-participant plan whose year-end assets, combined with all other one-participant plans of the employer, do not exceed $250,000** AND it is not the final year of the plan — the 5500-EZ filing is **not required** (2025 Form 5500-EZ instructions, Who Does Not Have To File).
- The plan is a **welfare plan with < 100 participants** that is unfunded (paid from general assets), fully insured, or a combination — exempt from Form 5500 under DOL Reg. 29 CFR §2520.104-20.
- The plan is a **governmental plan** (state, local, federal employee plans) — exempt from Title I of ERISA, no Form 5500.
- The plan is a **church plan** that has not elected ERISA coverage under IRC §410(d) — exempt.
- The plan is a **fringe-benefit plan** like a §125 cafeteria plan — these have separate reporting (Form 5500 doesn't apply unless the underlying welfare plan crosses 100 participants).
- The user wants help with **plan termination distributions** themselves — that's a separate flow (loan offsets, rollovers, 1099-R, lump-sum distributions). Form 5500 reports the year of termination but isn't the distribution mechanism.

If the plan type is ambiguous, ask before proceeding. Common confusion points:

- **"Solo 401(k)" with two participants** (owner + spouse): still a one-participant plan if it covers only the owner and spouse and they own the entire business; the spouse does not need to be an owner. A plan covering only partners (and their spouses), or 2% S corporation shareholders treated as partners, also qualifies (2025 Form 5500-EZ instructions, Who Must File). Covering any non-owner employee makes it a Title I plan: 5500-SF / 5500 applies (a one-participant plan cannot file 5500-SF, and a Title I plan cannot file 5500-EZ).
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
8. **Participant count at the beginning of the plan year**. For pension plans, includes active employees, retirees with vested benefits, and beneficiaries receiving benefits. For a defined contribution plan, also get the number of participants **with account balances** on the first day of the year: that number (Form 5500 line 6g(1), Form 5500-SF line 5c(1)) decides large vs. small plan status.
9. **Participant count at the end of the plan year**.
10. **Year-end plan assets** (for pension plans) — total fair-market value.
11. **Is this a one-participant plan?** Owner-only, owner + spouse, or partners + spouses? If yes, 5500-EZ likely applies. Then ask: **how many returns of any type** (W-2s, 1099s, income, employment, excise) must the employer file with the IRS in the calendar year that includes the first day of the plan year? 10 or more makes EFAST2 filing of the 5500-EZ mandatory.
12. **Is every plan asset an "eligible plan asset" at all times during the year, with no employer securities at all?** (Mutual funds, bank and insurance investment contracts valued at least annually, publicly traded securities held by a registered broker-dealer, cash held by a bank, participant loans.) If yes, the plan may qualify for 5500-SF; if no (real estate, private equity, limited partnerships, any employer securities), it files Form 5500 with Schedule I (small) or Schedule H (large).

### For Form 5500 large plans (100+ participants)

13. **Audited financial statements** — required attachment from an Independent Qualified Public Accountant (IQPA). The audit takes 4-12 weeks; start early.
14. **Trustee / custodian info** — name, EIN, address.
15. **Investment manager(s)** if any — Form ADV registration if §3(38) ERISA fiduciary.

### For welfare plans

16. **Funding type**: Funded through trust, fully insured (premiums paid to insurance carrier), unfunded (paid from employer general assets), or combination.
17. **Number of participants on first day of plan year** — drives the 100-participant test for filing requirement.

### For Form 5558 extension

18. **Original due date** + the desired extended due date (no later than the 15th day of the 3rd month after the normal due date).
19. **Plan year being extended** + plan number.

For DFVC (delinquent filer) program, additionally ask:
- Year(s) of delinquent filings
- Whether the DOL has already issued a Notice of Intent to Assess a Penalty (if yes, DFVC is not available)

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Determine if filing is required

Use this decision flow:

```
Is the plan an IRA-based plan (SEP-IRA, SIMPLE IRA)?
  → No 5500 required. Stop. (Custodian handles annual 5498 for participants.)

Is the plan a governmental or non-electing church plan?
  → No 5500 required. Stop.

Is this a one-participant plan (owner/partners and spouses only, no non-owner employees)?
  → Do year-end assets of all the employer's one-participant plans combined exceed $250,000,
    OR is this the final plan year?
    → Yes: file 5500-EZ
    → No: NOT required to file (2025 Form 5500-EZ instructions, Who Does Not Have To File)

Is this a welfare plan with < 100 participants on first day?
  → Is the plan funded (trust holds assets)?
    → Yes: must file 5500-SF or 5500
    → No (unfunded, fully insured, or combo): exempt under 29 CFR §2520.104-20

Is this a pension plan with < 100 participants at the start of the year (DC plans: participants
with account balances; or the 80-120 rule) that meets every 5500-SF condition: 100% eligible
plan assets, no employer securities, audit waiver met without enhanced bonding, not
multiemployer / pooled employer plan / ESOP / DCG / Form M-1 filer?
  → Eligible for 5500-SF (small plan, short form)

Small plan that fails any 5500-SF condition?
  → Form 5500 + Schedule I (+ IQPA report only if the audit waiver is not met)

Pension plan with 100+ participants (and the 80-120 rule not available)?
  → Must file full 5500 + Schedule H + IQPA report
```

See [`references/variant-selection.md`](./references/variant-selection.md) for full decision tree with edge cases.

### Step 2 — Confirm plan type and variant

Confirm with the user. The most common mistake is filing the wrong variant — if the user thinks they're a 5500-EZ filer but the plan covers a non-owner employee, it is a Title I plan that must file 5500-SF or 5500, and a 5500-EZ does not satisfy its filing obligation.

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

For Schedule H (large plans), much more detail is required — see the Schedule H section of [`references/line-by-line.md`](./references/line-by-line.md).

### Step 4 — Determine which schedules attach

Different schedules apply based on variant + plan type:

| Schedule | Purpose | Required when |
|----------|---------|--------------|
| Schedule A | Insurance information | Any benefits provided by an insurer, including investment contracts (GICs, PSAs) |
| Schedule C | Service provider information | Large plan; a provider received $5,000 or more in reportable compensation, or an accountant/actuary was terminated |
| Schedule D | DFE/participating plan information | Plan invested in a CCT, PSA, MTIA, or 103-12 IE |
| Schedule G | Financial transaction schedules | Large plan with Schedule H line 4b, 4c, or 4d "Yes" |
| Schedule H | Large plan financial information | Plans filing as large plans (100+ participants) and DFEs, unless exempt under 29 CFR 2520.104-44 |
| Schedule I | Small plan financial information | Small plan filing Form 5500 instead of 5500-SF |
| Schedule MB | Multiemployer DB / money purchase actuarial info | Multiemployer DB plans; money purchase plans amortizing a funding waiver |
| Schedule MEP | Multiple-employer retirement plan information | Multiple-employer pension plans |
| Schedule R | Retirement plan information (distributions, funding, nondiscrimination, coverage, amendments) | Pension plans filing Form 5500, except IRA-funded plans |
| Schedule SB | Single-employer DB actuarial information | Single- and multiple-employer DB plans subject to minimum funding |

Form 5500-EZ never attaches schedules (Schedule SB/MB stay in the plan records). Form 5500-SF attaches only Schedule SB, MB, or MEP when applicable. Form 5500 attaches Schedule H or I unless the plan is a fully insured, unfunded, or combination welfare plan, or a pension plan described in 29 CFR 2520.104-44(b)(2) or funded only with IRAs (2025 Instructions for Form 5500, What To File).

See the schedule sections of [`references/line-by-line.md`](./references/line-by-line.md).

### Step 5 — Fill the form line by line

Use [`references/line-by-line.md`](./references/line-by-line.md) for every variant:
- 5500-EZ: Part I lines A–E, Part II lines 1a–5c, Part III lines 6a–7c, Part IV line 8, Part V lines 9–12.
- 5500-SF: Part I lines A–E, Part II lines 1a–6c, Part III lines 7a–8j, Part IV 9a–9b, Part V 10a–10i, Part VI 11–12e, Part VII 13a–13c, Part VIII 14a–15.
- Full 5500: Part I lines A–E, Part II lines 1a–10b, Part III 11a–11c (welfare), plus Schedule H or I and the other schedules.

### Step 6 — For large plans — coordinate the audit

If the plan files as a large plan, the financials must be audited by an independent qualified public accountant (IQPA) under ERISA §103(a)(3)(A) and 29 CFR §2520.103-1(b). The accountant's report is attached to the Form 5500 filing; Schedule H Part III records the opinion. Independence standards: 29 CFR 2509.2022-01.

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

Form 5558 (Rev. January 2025) grants a one-time extension to the 15th day of the 3rd month after the normal due date, approved automatically if filed complete by the original due date. For calendar-year plans, the original due date is July 31 (last day of the 7th month after plan year end); the extension runs to October 15.

Since January 1, 2025, Form 5558 can be filed electronically through EFAST2 or on paper with the Internal Revenue Service Center, Ogden, UT 84201-0045. Must be filed **by the original due date** to be effective. Late Form 5558 = no extension. Alternative: an automatic extension to the employer's extended income tax return due date applies if the plan year equals the employer's tax year and a copy of the income tax extension is kept with the plan records (check the "automatic extension" box instead).

### Step 8 — Run validation checks

See **Validation** below.

### Step 9 — Produce the deliverable

See **Output format** below.

### Step 10 — Hand off downstream

State next forms / actions:

- **Distribute SAR (Summary Annual Report)** to participants within 9 months after plan year end (calendar plan: by September 30 of the year after), or within 2 months after the end of an IRS extension period (29 CFR 2520.104b-10(c)). Required for 5500 / 5500-SF; not for 5500-EZ. Plan administrator obligation under ERISA §104(b)(3).
- **Form 8955-SSA** (separated participants with deferred vested benefits) — filed directly with the IRS, never attached to the EFAST2 filing.
- **PBGC comprehensive premium filing** (PBGC-covered defined benefit plans only) through My PAA, due the 15th day of the 10th calendar month that begins on or after the first day of the plan year (29 CFR 4007.11); Form 5558 does not extend it.
- **Provide participants with annual statement** of account balances (defined contribution plans) — separate from 5500.
- **State filings** — some states have parallel reporting (rare for retirement plans; common for welfare plans).
- **Audit follow-up** — if the IQPA found findings, address before next plan year.

### Step 11 — File the return (optional)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). It contains:

- Channel decision tree (EFAST2 for 5500/5500-SF; paper or EFAST2 for 5500-EZ, with EFAST2 mandatory for filers of 10+ returns)
- EFAST2 credentials setup (Login.gov sign-in, User ID + PIN, Filing Author / Filing Signer)
- Field-by-field mapping
- Pre-flight checklist
- Submission state machine
- Security rules — never store EFAST2 credentials in agent logs

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

The three variants share many lines but differ in detail. The 5500-EZ is the simplest (lines A–E and 1a–12); 5500-SF is medium (lines A–E and 1a–15); full 5500 is the most complex (with its schedules).

### Form header (all variants)

- **Plan year** — beginning and ending dates
- **Type of return** — first return, amended, final, short plan year (less than 12 months)
- **Plan number** — start at 001 for pension plans and 501 for welfare plans, numbering further plans consecutively; never 888 or 999. Consistent year over year; never reused.
- **Plan name** — exact match to plan document
- **Sponsor's name + EIN + address**
- **Administrator's name + EIN + address** (often same)

### Participant counts

- **Active participants** — currently employed and accruing benefits
- **Retired / separated participants with vested benefits** — former employees with account balances
- **Beneficiaries receiving benefits**
- **Total** — sum

The 100-participant threshold for "large plan" status is tested on the **first day** of the plan year. Defined contribution plans count only participants with account balances (Form 5500 line 6g(1); Form 5500-SF line 5c(1); end-of-year count on a first return). The 80-120 rule lets a plan that filed as small last year stay small up to 120 participants.

### Plan characteristics codes

Two-character codes describing plan provisions, pulled from the plan document and the code list in the instructions (e.g., 2E profit-sharing, 2J section 401(k) feature, 2K section 401(m) arrangement such as matching contributions, 2S automatic enrollment, 2T default investment account, 3B plan covering self-employed individuals, 3D pre-approved plan). Safe harbor status is not a code; on Form 5500-SF it is line 14b.

### Financial info (varies by variant)

- 5500-EZ: line 6 (assets, liabilities, net assets at beginning and end of year) and line 7 (contributions only); no income or expense lines
- 5500-SF: lines 7a–7c and 8a–8j
- 5500 + Schedule H: Part I lines 1a–1l and Part II lines 2a–2l with detailed asset and income categories

### Compliance questions

Yes/no questions:
- Late participant contributions? (5500-SF line 10a; Schedule H or I line 4a — DOL hot button)
- Nonexempt party-in-interest transactions? (5500-SF line 10b; Schedule H or I line 4d)
- Fidelity bond? (5500-SF line 10c; Schedule H or I line 4e)
- Participant loans? (5500-EZ line 9; 5500-SF line 10g)
- IQPA opinion (Schedule H Part III) or audit waiver claim (5500-SF line 6b; Schedule I line 4k)
- Insurance contracts? (drives Schedule A)

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] End-of-year net assets = beginning-of-year net assets + net income + transfers (5500-SF: 7c(b) = 7c(a) + 8i + 8j; Schedule H: 1l(b) = 1l(a) + 2k + 2l)
- [ ] Form 5500: 6d = 6a(2) + 6b + 6c and 6f = 6d + 6e
- [ ] If 5500-EZ: combined year-end assets of the employer's one-participant plans exceed $250,000 (or final year)
- [ ] If 5500-SF: participant count < 100 (DC plans: with account balances; or 80-120 rule) AND lines 6a and 6b both "Yes"
- [ ] Beginning-of-year amounts equal the prior year's end-of-year amounts (5500-EZ 6c(1), 5500-SF 7c(a), Schedule H 1l(a), Schedule I 1c(a))

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Participant count grew by > 50% year-over-year — verify business growth or merger
- [ ] Year-end assets dropped by > 20% but no large distribution — investigate (audit issue, market loss?)
- [ ] Late-deferral question answered "Yes" — DOL flag; confirm correction (lost earnings restored) and Form 5330 for the 15% excise tax unless VFCP + PTE 2002-51 relief applies
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
- [ ] If any service provider received $5,000 or more in reportable compensation, Schedule C attached (large plans)

---

## Output format

The agent's deliverable depends on variant. Below is the 5500-EZ template (simplest); 5500-SF and full 5500 use longer templates filled from same data.

```markdown
# Form 5500-EZ — DRAFT for Plan Year YYYY

## Part I — Annual Return Identification
Plan year:                   01/01/YYYY – 12/31/YYYY
A  [ ] (1) First return  [ ] (2) Amended  [ ] (3) Final  [ ] (4) Short plan year
B  [ ] Form 5558  [ ] Automatic extension  [ ] Special extension: ______
C  [ ] Foreign plan
D  [ ] IRS Late Filer Penalty Relief Program (paper only)
E  [ ] Retroactively adopted plan (SECURE Act §201)

## Part II — Basic Plan Information
1a Plan name:                <full legal name from plan document>
1b Plan number (PN):         001
1c Effective date:           MM/DD/YYYY
2a Employer name / address:  <legal name, trade name, C/O, address>
2b Employer EIN:             XX-XXXXXXX
2c Employer phone:           <phone>
2d Business code:            <six digits>
3a Plan administrator:       Same
3b Administrator EIN:        (blank if 3a is "Same")
3c Administrator phone:      (blank if 3a is "Same")
4a–4d Prior name/EIN/plan:   (only if changed)
5a(1) Participants, BOY:     X
5a(2) Active, BOY:           X
5b(1) Participants, EOY:     X
5b(2) Active, EOY:           X
5c Terminated, <100% vested: 0

## Part III — Financial Information
                             (1) Beginning of year   (2) End of year
6a Total plan assets:        $XXX,XXX                $XXX,XXX
6b Total plan liabilities:   $0                      $0
6c Net plan assets:          $XXX,XXX                $XXX,XXX
7a Employer contributions:   $XX,XXX
7b Participant contributions: $XX,XXX
7c Others (incl. rollovers): $0

## Part IV — Plan Characteristics
8  Codes: <two-character codes from the plan document, e.g., 2E 2J 3B 3D>

## Part V — Compliance and Funding Questions
9  Participant loans:        [ ] Yes  [ ] No   Year-end amount: $____
10 DB plan subject to minimum funding: [ ] Yes [ ] No   10a: $____
11 DC plan subject to §412:  [ ] Yes [ ] No   (11a–11e if Yes)
12 Opinion letter date / serial: MM/DD/YYYY  X999999

## Sign here
Signature of employer or plan administrator: __________   Date: ______
Name of individual signing:  __________

## Filing
- Channel: [ ] Paper to Department of the Treasury, Internal Revenue Service, Ogden, UT 84201-0020
           [ ] EFAST2 (required if the employer files 10+ returns of any type with the IRS this calendar year)
- Due: last day of the 7th month after plan year end (calendar plan: July 31); Form 5558 extends to October 15
- No Summary Annual Report for 5500-EZ filers

## Validation summary
- Math: 6c = 6a − 6b both columns; 6c(1) equals last year's 6c(2); workpaper rollforward ties
- Threshold: combined year-end assets of all one-participant plans = $_____ (> $250,000, or final year)
- Sanity: <list any warnings raised>
- Next steps: <handoff items from Step 10>

## Sources cited in this draft
- 2025 Form 5500-EZ and 2025 Instructions for Form 5500-EZ
- IRC §6058(a) (filing requirement); IRC §6652(e) (late filing penalty)
- Treas. Reg. §301.6058-2 (mandatory electronic filing)
- Form 5558 (Rev. January 2025), if an extension was filed
```

For 5500-SF / full 5500, see [`references/line-by-line.md`](./references/line-by-line.md) for the longer template.

The draft is **not** the final filed form. The plan administrator still has to file via EFAST2 (5500/5500-SF, electronic only) or, for 5500-EZ, on paper with the IRS or through EFAST2 (EFAST2 mandatory if the filer must file 10+ returns of any type with the IRS in the calendar year).

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/line-by-line.md`](./references/line-by-line.md) — Every line of the 2025 Form 5500-EZ, 5500-SF, and 5500, Schedules H and I, summaries of Schedules A, C, D, G, MB, MEP, R, SB, and Form 5558
- [`references/variant-selection.md`](./references/variant-selection.md) — Decision tree for picking 5500 vs. 5500-SF vs. 5500-EZ (vs. no filing at all); welfare plan exemptions; one-participant plan rules
- [`references/efast2-filing.md`](./references/efast2-filing.md) — EFAST2 credentials (Login.gov, User ID, PIN), IFILE, attachments, signatures, filing status, public disclosure, amendments
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes with fixes, including late filing penalties, DFVC, and the IRS late filer relief program
- [`filing.md`](./filing.md) — Browser-automation playbook: how an agent files via EFAST2 (5500/5500-SF/5500-EZ) or on paper for 5500-EZ, plus DFVC and Rev. Proc. 2015-32 mechanics

## Examples

End-to-end worked Form 5500 filings. Use these as patterns when the user's situation is similar.

- [`examples/solo-401k-5500-ez.md`](./examples/solo-401k-5500-ez.md) — Owner-only 401(k) crossing $250,000 for the first time, first Form 5500-EZ, calendar plan year 2025
- [`examples/small-plan-5500-sf.md`](./examples/small-plan-5500-sf.md) — Small 401(k) plan (50 active participants), all 5500-SF conditions met, Form 5500-SF
- [`examples/large-plan-with-audit.md`](./examples/large-plan-with-audit.md) — Mid-size 401(k) plan (200 active), full Form 5500 with Schedule H, Schedule C, Schedule R, and the IQPA report

## Sources

Authoritative sources used by this skill. Always re-verify against the IRS / DOL site for the plan year being filed — forms revise yearly.

- [Form 5500-EZ (2025)](https://www.irs.gov/pub/irs-pdf/f5500ez.pdf) — IRS-hosted PDF
- [Instructions for Form 5500-EZ (2025)](https://www.irs.gov/pub/irs-pdf/i5500ez.pdf) — threshold, mandatory e-filing, addresses, codes
- [About Form 5500-EZ](https://www.irs.gov/forms-pubs/about-form-5500-ez) — IRS landing page
- [DOL Form 5500 series page](https://www.dol.gov/agencies/ebsa/employers-and-advisers/plan-administration-and-compliance/reporting-and-filing/form-5500) — 2025 Form 5500, 5500-SF, schedules, and instructions
- [2025 Instructions for Form 5500](https://www.dol.gov/sites/dolgov/files/ebsa/employers-and-advisers/plan-administration-and-compliance/reporting-and-filing/form-5500/2025-instructions.pdf) and [2025 Instructions for Form 5500-SF](https://www.dol.gov/sites/dolgov/files/ebsa/employers-and-advisers/plan-administration-and-compliance/reporting-and-filing/form-5500/2025-sf-instructions.pdf)
- [EFAST2 filing system](https://www.efast.dol.gov) and the [EFAST2 Guide for Filers and Service Providers](https://www.efast.dol.gov/fip/pubs/EFAST2_Guide_Filers_Service_Providers.pdf) (v4.0, Dec. 2, 2024)
- [Form 5558 (Rev. January 2025)](https://www.irs.gov/pub/irs-pdf/f5558.pdf) — extension to the 15th day of the 3rd month after the normal due date
- [Rev. Proc. 2015-32](https://www.irs.gov/pub/irs-drop/rp-15-32.pdf) — IRS late filer penalty relief for 5500-EZ
- [Publication 560 (Retirement Plans for Small Business)](https://www.irs.gov/pub/irs-pdf/p560.pdf) — SEP, SIMPLE, qualified plan rules
- [Publication 963 (Federal-State Reference Guide)](https://www.irs.gov/pub/irs-pdf/p963.pdf) — governmental plan exclusions
- IRC §401(a) (qualified plan requirements)
- IRC §410, §411 (participation, vesting)
- IRC §6058(a) (information required by certain employee benefit plans)
- IRC §6652(e) (failure to file — IRS penalty $250/day, max $150,000)
- IRC §6058 / 6059 (filing requirements + actuarial info)
- ERISA §101, §103, §104 (annual reporting)
- ERISA §502(c)(2) (DOL penalty up to $2,739 per day for failure to file; 2025 adjustment, 90 FR 1854; DOL cancelled the 2026 adjustment, 91 FR 31358; re-check each January)
- Treas. Reg. §301.6058-2 (mandatory electronic filing of Form 5500-EZ for filers of 10+ returns)
- 29 CFR §2520.103-1 (annual reporting rules)
- 29 CFR §2520.103-1(b) (large plan contents, including the accountant's report); §2520.103-1(c) (small plan contents, including the Form 5500-SF option); §2520.103-1(d) (80-120 participant rule)
- 29 CFR §2520.104-20 (small welfare plan exemption)
- 29 CFR §2520.104-44 (Schedule H/I exemption for fully insured and unfunded plans)
- 29 CFR §2520.104-46 (small pension plan audit waiver)
- ERISA §412 and 29 CFR 2580.412-11 (fidelity bond amount)
- 29 CFR §2520.104b-10 (summary annual report timing and content)
- 29 CFR §2510.3-102 (participant contribution deposit timing)
- 29 CFR 2509.2022-01 (IQPA independence)
- DFVC Program (Delinquent Filer Voluntary Compliance) — https://www.dol.gov/agencies/ebsa/employers-and-advisers/plan-administration-and-compliance/correction-programs/dfvcp

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS / DOL forms, publications, the Internal Revenue Code, and ERISA. It is not legal or tax advice and does not establish a CPA / attorney / enrolled agent relationship. The agent invoking this skill should remind the user that the output is a starting point and that complex situations (controlled groups, multiple-employer plans, defined benefit funding issues, prohibited transactions, DFVC navigation, plan termination distributions, IQPA findings) warrant a licensed ERISA attorney or third-party administrator's review.
