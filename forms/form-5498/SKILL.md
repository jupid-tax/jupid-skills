---
name: form-5498
description: >
  Use this skill when an individual has received Form 5498 (IRA Contribution
  Information) from an IRA custodian and needs help understanding it,
  reconciling its boxes against the user's tax return, verifying that IRA
  contributions, rollovers, conversions, and RMDs were reported correctly,
  or interpreting Box 7 codes and the RMD indicator in Box 11. Triggers on
  phrases like "received Form 5498", "Form 5498 from Fidelity / Vanguard /
  Schwab", "what is Box 1 / Box 3 / Box 7 / Box 11 on 5498", "verify IRA
  contribution reporting", "Form 5498 vs Form 1040", "5498 doesn't match my
  return", "year-end IRA statement", "rollover reported on 5498",
  "conversion shown on 5498", "FMV on 5498". Do NOT use for: HSA contributions
  reported on Form 5498-SA (use the form-5498-sa skill); Coverdell ESA
  contributions reported on Form 5498-ESA; reporting IRA distributions
  (those are on Form 1099-R, not 5498); claiming the IRA deduction itself
  (that goes on Schedule 1; Form 5498 is informational only); excise taxes
  on excess contributions or missed RMDs (use the form-5329 skill).
form: Form 5498 (IRA Contribution Information)
audience: [individual]
tax_year: 2026
last_verified: 2026-10-06
official_form: https://www.irs.gov/pub/irs-pdf/f5498.pdf
official_instructions: https://www.irs.gov/pub/irs-pdf/i1099r.pdf
---

# Form 5498 — IRA Contribution Information

This skill helps an individual interpret and reconcile a Form 5498 received
from an IRA custodian. **Form 5498 is informational** — the recipient does
not file it with their tax return. The custodian files it with the IRS
and sends the contribution information to the account holder by **May 31**
of the year following the contribution year (next business day if May 31
falls on a weekend: **June 1, 2026** for the 2025 form). The year-end FMV and
any RMD statement come earlier, by January 31 (February 2, 2026 for 2025
values) (2025 Instructions for Forms 1099-R and 5498, "Statements to
participants"; Pub. 1099).

**Companion guide for end users:** [Form 5498 Explained (2026): IRA Contributions, SEP, and Why It Arrives After You File + AI Agent Skill](https://jupid.com/blog/form-5498-ira-contributions-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

**Form revision.** The box map was verified against the 2025 Form 5498 (furnished in 2026) and the 2025 Instructions for Forms 1099-R and 5498. The 2026 Form 5498 (Created 6/12/26, furnished in 2027) keeps the same box numbers and splits the address fields; box 11 there reads "Check if RMD for 2027". Re-check https://www.irs.gov/forms-pubs/about-form-5498 before use.

The skill produces:

1. A box-by-box explanation of what each populated value on the 5498 means
2. A reconciliation against the user's Form 1040 / Schedule 1 / Form 8606
   to confirm contributions and rollovers are reported consistently
3. Flags for any inconsistencies the user should resolve before the IRS
   does (CP2000 risk)

The math is mostly cross-checking, not new computation. The judgment is
in *which boxes correspond to which return lines* and *what to do when
the 5498 says something different from what the user reported*.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user received Form 5498 in the mail or via a custodian portal and
  is asking what to do with it
- The user is reconciling a Form 5498 they received against an already-
  filed Form 1040 (e.g., catching errors before an IRS notice)
- The user is preparing a Form 1040 and wants to verify their IRA
  contribution claim is consistent with the eventual Form 5498
- The user has multiple IRAs at different custodians and received
  multiple 5498s; needs to total contributions correctly
- The user did a Roth conversion and is matching the 1099-R (distribution
  side) with the 5498 (receiving side)
- The user is checking Box 11 (RMD required) to confirm they've taken or
  must take an RMD this year
- The user is verifying Box 5 (FMV at year-end) which is used to compute
  next year's RMD

Do **not** engage this skill when:

- The user received Form 5498-SA (HSA contributions) → use the
  `form-5498-sa` skill
- The user received Form 5498-ESA (Coverdell contributions) → that's
  out of scope; refer to IRS Pub 970
- The user is asking how to report an IRA distribution → use the
  `form-1040` skill (Lines 4a/4b for IRA distributions; the 1099-R is
  the source document, not the 5498)
- The user wants to claim a traditional IRA deduction → the 5498 is
  evidence of contribution, but the deduction is computed and claimed
  on Schedule 1, Line 20 (subject to MAGI/active-participant phaseouts);
  use the `schedule-1` skill
- The user has an excess contribution or missed RMD → use the
  `form-5329` skill
- The user has nondeductible IRA basis to track → Form 8606 (no skill
  for it in this repo yet; follow the Form 8606 instructions)

If the user has multiple issues (e.g., 5498 verification + a missed RMD),
run this skill first for the verification, then hand off to `form-5329`.

---

## Prerequisites

Before producing anything, the agent must have:

1. **The Form 5498 itself** — either as a PDF, photo, or text transcription
   of every populated box. Specifically the agent needs:
   - Custodian/trustee name and TIN (top section)
   - Account holder name and SSN
   - Account number
   - Box 1 (IRA contributions, not including amounts in Boxes 2-4, 8-10,
     13a, and 14a)
   - Box 2 (rollover contributions)
   - Box 3 (Roth IRA conversion amount)
   - Box 4 (recharacterized contributions)
   - Box 5 (FMV of account on 12/31)
   - Box 6 (life insurance cost included in Box 1, rare)
   - Box 7 (IRA type checkbox: IRA / Roth IRA / SEP / SIMPLE)
   - Box 8 (SEP contributions)
   - Box 9 (SIMPLE contributions)
   - Box 10 (Roth IRA contributions)
   - Box 11 (RMD required for next year — check box)
   - Box 12a (RMD date)
   - Box 12b (RMD amount)
   - Boxes 13a-13c (postponed contribution or late rollover: amount, year,
     code FD / PO / SC or a combat-zone code)
   - Box 14a (repayments of qualified reservist, qualified disaster, birth
     or adoption, emergency personal expense, domestic abuse victim, or
     terminally ill individual distributions)
   - Box 14b (code for Box 14a: QR, DD, BA, EP, DA, TI)
   - Box 15a (FMV of certain specified assets, like alternative
     investments)
   - Box 15b (code for Box 15a)

2. **The corresponding tax year** — Form 5498 is for the prior calendar
   year's contributions (e.g., a 5498 received by June 1, 2026 covers tax
   year 2025 contributions). Boxes 1 and 10 include contributions made
   *for* that year through April 15 of the next year (no extension), even
   if deposited in the next year. Boxes 8 and 9 (SEP, SIMPLE) report
   contributions made *during* the calendar year, including ones for the
   prior year and excluding ones made next year for this year. Boxes 2, 3,
   4, and 5 also reflect calendar-year activity.

3. **The user's tax return for the same tax year** — Form 1040, Schedule
   1 (for the IRA deduction or self-employed retirement deduction), and
   Form 8606 if any nondeductible contributions or Roth conversions.
   Without the return, the agent can explain the 5498 but can't reconcile.

4. **Any other Forms 5498 the user received** — if the user has IRAs at
   multiple custodians, each issues a separate 5498. They must be
   totaled.

5. **The user's 1099-Rs for the same year** — for distributions and
   conversions, the 1099-R is the distributing-side document; the 5498
   may be the receiving-side document for a rollover or conversion. The
   pair must be reconciled.

---

## Workflow

Execute these steps in order.

### Step 1 — Identify which boxes are populated

Walk the 5498 and list every non-zero / non-blank box. Many 5498s have
only a few boxes filled (e.g., Box 1 + Box 5 + Box 7 for a simple
contribution year).

### Step 2 — Identify the IRA type from Box 7

Box 7 is a checkbox indicating the account type:
- **IRA** (traditional IRA)
- **Roth IRA**
- **SEP** (Simplified Employee Pension)
- **SIMPLE** (Savings Incentive Match Plan for Employees)

The IRA type drives which contribution box is populated:
- Traditional IRA → Box 1
- Roth IRA → Box 10
- SEP → Box 8 (a Roth SEP IRA has both "SEP" and "Roth IRA" checked)
- SIMPLE → Box 9 (a Roth SIMPLE IRA has both "SIMPLE" and "Roth IRA" checked)

If the agent sees a Roth contribution in Box 1 (instead of Box 10), the
custodian made an error. Surface this for correction with the custodian.

### Step 3 — Reconcile contribution boxes against Schedule 1

Map the contribution box(es) to the user's return:

| 5498 Box | Account type | Reported on | Notes |
|----------|--------------|-------------|-------|
| Box 1 | Traditional IRA | Schedule 1, Line 20 (deductible) AND/OR Form 8606 (nondeductible) | If user is an active participant in employer plan, deduction may be phased out |
| Box 8 | SEP-IRA | Schedule 1, Line 16 (self-employed retirement) | Self-employed owner: about 20% of net SE earnings after half of SE tax (25% plan rate, Pub. 560 rate table). Box 8 is calendar-year deposits, so a deposit made in 2026 for 2025 is on the 2026 form |
| Box 9 | SIMPLE-IRA | Schedule 1, Line 16 (self-employed) OR W-2 reduction | Self-employed: Line 16. Employee: already reduces W-2 wages. Calendar-year deposits, like Box 8 |
| Box 10 | Roth IRA | **Not deductible** — does not appear on the return | Verified only via 5498 box; user's records must show contribution stayed under MAGI phaseout |

**Critical reconciliation**: Box 1 (or Box 10) must equal the user's
claimed traditional IRA contribution (or Roth contribution). If Box 1 =
$5,000 but the user claimed $6,000 on Schedule 1 Line 20, one of them is
wrong. Investigate before filing or amending.

### Step 4 — Reconcile rollovers (Box 2) against Form 1040 Lines 4a-5c

Box 2 reports rollover contributions *received* by the IRA. If the user
did a 401(k)-to-IRA rollover, the corresponding 1099-R (from the 401(k))
should appear on Form 1040 Line 5a (gross distribution) and Line 5b ($0
taxable), with box 1 ("Rollover") checked on Line 5c (2025 Form 1040). An
IRA-to-IRA 60-day rollover goes on Lines 4a/4b with box 1 checked on
Line 4c. Direct trustee-to-trustee transfers between IRAs of the same type
are not reported on Form 5498 at all. Late rollovers appear in Box 13a,
not Box 2.

If Box 2 is non-zero, look for the corresponding 1099-R:
- 1099-R Box 7 code G → direct rollover (no tax)
- 1099-R Box 7 code H → direct rollover from designated Roth account

The Box 2 amount on the 5498 should match (or come close to matching) the
1099-R distribution amount that was rolled over.

### Step 5 — Reconcile Roth conversions (Box 3) against Form 8606 Part II

Box 3 reports a Roth IRA conversion amount received during the year. The
corresponding 1099-R (from the traditional IRA being converted) should
appear on Form 1040 Lines 4a (gross) and 4b (taxable amount, computed
via Form 8606 Part II if user has nondeductible basis).

Reconciliation:
- Form 5498 Box 3 should equal the gross conversion amount
- Form 1099-R Box 1 (gross distribution) should equal Form 5498 Box 3
  for the converted amount
- Form 1099-R Box 7 should be code 2 (early distribution, exception
  applies — the 1099-R instructions list "A Roth IRA conversion" for a
  participant under 59½) or code 7 (normal distribution if user is 59½+)
- Form 8606 Part II computes the taxable portion if the user has basis

### Step 6 — Verify Box 11 (RMD required for next year)

If Box 11 is checked, the IRS knows the user has an RMD requirement for
the year following the 5498 year (the 2025 form's box reads "Check if
RMD for 2026"). Cross-check against the user's age:

- The custodian must check Box 11 for the year the owner reaches the
  applicable age, even though that first RMD can wait until April 1 of
  the following year, and for every later year. The applicable age is 73
  for owners who reach 72 after 2022 and 73 before 2033, and 75 for
  owners who reach 74 after 2032 (IRC §401(a)(9)(C)(v); 2025 Instructions
  for Forms 1099-R and 5498, Box 11). So the 2025 form's Box 11 should be
  checked if the owner turns 73 in 2026 or is older
- If the user is past the applicable age and Box 11 is not checked,
  contact custodian — this could be a custodian error
- If Box 11 is checked and Box 12a/12b are populated, those give the
  date and amount of the RMD computed by the custodian
- Inherited IRAs: custodians are not required to report RMDs for IRAs of
  deceased owners (except when a surviving spouse treats the IRA as their
  own), so an unchecked Box 11 does not mean a beneficiary owes no RMD

The custodian-computed RMD amount in Box 12b is informational; the user
is ultimately responsible for taking the correct RMD across all
applicable accounts.

### Step 7 — Verify Box 5 (FMV at year-end) for next year's RMD

Box 5 is the IRA's FMV on 12/31 of the 5498 year. This drives next
year's RMD computation:

```
Next year's RMD = Box 5 ÷ (Distribution period factor for next year's age)
```

If the user has multiple IRAs, sum Box 5 across all 5498s for the IRA
RMD calculation (IRA RMDs may be aggregated across IRAs; not across
401(k)s).

### Step 8 — Surface inconsistencies

Produce a report listing:
- Boxes populated and what they mean
- Each reconciliation (5498 box ↔ return line) with status (Match /
  Mismatch / N/A)
- Any unresolved mismatches the user should address (correct the
  return via amendment, or correct the 5498 with the custodian)

### Step 9 — Hand off

State next actions:
- If the return matches the 5498: the user files the 5498 with their
  tax records. No filing action required.
- If the return doesn't match the 5498: amend the return via Form 1040-X
  ([`form-1040-x`](../form-1040-x/SKILL.md)), or contact the custodian to
  issue a corrected 5498 (Form 5498 marked "CORRECTED" in the top
  checkbox).
- If Box 11 indicates an RMD is due: confirm the user has taken or
  scheduled the RMD; if missed, hand off to the `form-5329` skill.
- If Box 3 (Roth conversion) appears: confirm Form 8606 Part II was
  completed correctly on the return.

---

## Box-by-box guidance

For full detail, load [`references/box-by-box.md`](./references/box-by-box.md).
High-level summary below.

### Box 1 — IRA contributions (other than amounts in 2-4, 8-10, 13a, and 14a)

Total **traditional IRA** contributions for the year, including amounts
contributed for the year by April 15 of the next year (extensions do not
extend this date). Gross amount, including any excess contribution even
if it was withdrawn. Excludes rollovers (Box 2), conversions (Box 3),
recharacterizations (Box 4), other-account contributions (Boxes 8-10),
postponed contributions (Box 13a), and repayments (Box 14a).

### Box 2 — Rollover contributions

Total rollover amount received by this IRA during the calendar year,
from any source (qualified plan, another IRA, etc.). Includes both 60-
day rollovers and direct rollovers from plans, plus plan-to-Roth IRA
rollovers, military death gratuities and SGLI payments. Late rollovers go
in Box 13a; IRA-to-IRA trustee-to-trustee transfers are not reported.

The agent must reconcile Box 2 with the corresponding 1099-R from the
distributing account.

### Box 3 — Roth IRA conversion amount

Amount converted from a traditional IRA, SEP-IRA, or SIMPLE IRA to a
Roth IRA during the calendar year. Reported on Form 1040 Line 4b
(taxable portion) via Form 8606 Part II. A rollover from a 401(k) or
other plan straight into a Roth IRA is in Box 2, not Box 3.

### Box 4 — Recharacterized contributions

Amount of contributions recharacterized between traditional and Roth IRAs
during the year. Note: TCJA (2018+) eliminated recharacterization of
*conversions*; only contribution-recharacterizations are still allowed.

### Box 5 — FMV of account on December 31

Year-end fair market value. Drives next year's RMD calculation.

### Box 6 — Life insurance cost

Rare. For endowment contracts only, the part of Box 1 allocable to the
cost of life insurance; subtract it from the allowable contribution to
figure the IRA deduction. Most filers will see Box 6 = blank.

### Box 7 — IRA type checkbox

Indicates account type. Critical for determining which other boxes apply:
- IRA = traditional IRA → Box 1
- Roth IRA → Box 10
- SEP → Box 8
- SIMPLE → Box 9

### Box 8 — SEP contributions

SEP-IRA contributions made during the calendar year, including ones made
for the prior year and excluding ones made next year for this year
(employer-side; includes a self-employed person's contribution to their
own account and Roth SEP contributions).

### Box 9 — SIMPLE contributions

SIMPLE-IRA contributions made during the calendar year (employer +
employee salary deferrals), on the same calendar-year basis as Box 8.

### Box 10 — Roth IRA contributions

Roth IRA contributions for the year, made by April 15 of the next year
(regular contributions only; not conversions), plus 529-to-Roth IRA
rollovers designated for the year.

### Box 11 — Required minimum distribution checkbox

Checked if an RMD is required for the year following the 5498 year. Cross-
check against the user's age (RMDs begin at the applicable age: 73 for
owners who reach 72 after 2022 and 73 before 2033; 75 for owners who
reach 74 after 2032, IRC §401(a)(9)(C)(v)).

### Box 12a — RMD date

Date the custodian computes as the RMD deadline (typically December 31
of the year following the 5498 year, or April 1 for a first-year RMD).

### Box 12b — RMD amount

Custodian's computed RMD for the next year. Informational; the user is
ultimately responsible for the correct amount.

### Boxes 13a-13c — Postponed/late rollover information

Postponed prior-year contributions (combat zone service; federally
declared disasters, code FD) and late rollovers (qualified plan loan
offsets, code PO; self-certified late rollovers under Rev. Proc. 2020-46,
code SC). Box 13b shows the year for a postponed contribution and is
blank for late rollovers. Most filers will see these blank.

### Box 14a — Repayments

Repayments of qualified reservist (QR), qualified disaster (DD), birth or
adoption (BA), emergency personal expense (EP), domestic abuse victim
(DA), or terminally ill individual (TI) distributions. Box 14a reports the
repayment amount; Box 14b reports the code.

### Box 15a — FMV of certain specified assets

For self-directed IRAs holding hard-to-value assets (non-traded stock,
debt, LLC or partnership interests, real estate, other assets without a
readily available FMV). Most retail filers will see Box 15 blank.

### Box 15b — Code for Box 15a

Up to two codes A–G identifying the asset types; code H if more than two
types are held.

---

## Validation

### Cross-form checks

- [ ] Box 1 + Box 10 (whichever is populated) matches the user's IRA
      contribution claim on Schedule 1, Form 8606, or (Roth) implicit;
      Box 8 / Box 9 match the SEP / SIMPLE deposits made during the
      calendar year (not necessarily the deduction for that tax year)
- [ ] Box 2 matches a corresponding 1099-R distribution (code G or H) for
      a direct rollover
- [ ] Box 3 matches a 1099-R distribution from a traditional / SEP /
      SIMPLE IRA, with the same amount
- [ ] Box 7 IRA type matches the contribution box that's populated
- [ ] If Box 11 checked: user reaches the applicable age (73 or 75) in the
      following year or is older, and either has taken or has scheduled
      the RMD
- [ ] Box 5 used as input for next year's RMD calculation

### Sanity checks (warn, do not block)

- [ ] Box 1 + Box 10 across all IRAs > IRA dollar limit for the year
      (2025: $7,000 / $8,000 age 50+, Notice 2024-80; 2026: $7,500 /
      $8,600 age 50+, Notice 2025-67) → possible excess contribution
- [ ] Box 10 > Roth dollar limit AND user's MAGI in phaseout → possible
      excess (use form-5329 Part IV)
- [ ] Box 7 IRA type = SIMPLE and the salary-deferral part of Box 9 >
      $16,500 for 2025 ($17,000 for 2026; plus $3,500 / $4,000 catch-up at
      50+, $5,250 at ages 60-63; $17,600 / $18,100 base for certain plans)
      → possible excess. Box 9 also holds employer contributions, so the
      box total alone does not prove an excess
- [ ] Box 4 (recharacterization) populated but user did not report any
      recharacterization → reconcile
- [ ] Box 11 checked but no RMD distribution evident on 1099-R → check
      whether RMD was satisfied; if not, possible Form 5329 Part IX issue
- [ ] User has multiple 5498s but only one was reconciled → hand off
- [ ] Box 5 = $0 but user claims to have an active IRA → custodian
      error or account closure; investigate

---

## Output format

The agent's deliverable is a **reconciliation report**. Format:

```markdown
# Form 5498 Reconciliation — Tax Year YYYY

## Custodian
Name: <custodian name>
TIN: <TIN>
Account #: <account number>

## Account holder
Name: <name>
SSN: <SSN>
IRA Type (Box 7): IRA | Roth IRA | SEP | SIMPLE

## Populated boxes

| Box | Label | Amount | Reconciled to |
|-----|-------|--------|----------------|
| 1 | IRA contributions | $X,XXX | Schedule 1 Line 20 / Form 8606 Line 1 |
| 2 | Rollover contributions | $X,XXX | 1099-R from <source>, Form 1040 Line 4a or 5a (box 1 checked on Line 4c / 5c) |
| 3 | Roth conversion | $X,XXX | 1099-R, Form 1040 Line 4a, Form 8606 Part II |
| 4 | Recharacterized | $X,XXX | (note) |
| 5 | FMV 12/31 | $X,XXX | (next-year RMD input) |
| 7 | IRA type | (type) | — |
| 8/9/10 | SEP/SIMPLE/Roth | $X,XXX | (matching return line) |
| 11 | RMD required next year | (Yes/No) | — |
| 12a/12b | RMD date / amount | (date/amount) | — |
| ... | (other populated boxes) | ... | ... |

## Reconciliation status

For each line above:
- ✓ Match — 5498 amount matches the return / 1099-R
- ✗ Mismatch — discrepancy of $X,XXX (action required)
- — N/A — informational only

## Issues to resolve

[List of mismatches and recommended actions, e.g.:
- Box 3 (Roth conversion) on 5498 = $25,000; 1099-R = $25,000; Form 1040
  Line 4b = $20,000 (with $5,000 nondeductible basis applied via Form
  8606). Math is consistent.
- Box 1 (IRA contribution) on 5498 = $7,000; Schedule 1 Line 20 = $6,000.
  $1,000 discrepancy. **Action**: review user's contribution records;
  if 5498 is correct, amend Schedule 1; if Schedule 1 is correct, ask
  custodian to issue corrected 5498.]

## Required actions
- [ ] File 5498 with tax records (no filing of 5498 with IRS by user)
- [ ] Resolve any mismatches before they trigger an IRS CP2000 notice
- [ ] If Box 11 checked: confirm RMD will be taken
- [ ] Use Box 5 for next year's RMD computation
```

---

## References

- [`references/box-by-box.md`](./references/box-by-box.md) — Full box-by-box reference with examples
- [`references/reconciliation.md`](./references/reconciliation.md) — How to reconcile 5498 against Form 1040, Schedule 1, Form 8606, Form 1099-R
- [`references/contribution-deadlines.md`](./references/contribution-deadlines.md) — Timing of contributions, prior-year vs. current-year designations, custodian deadlines
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer mistakes around 5498
- [`filing.md`](./filing.md) — How a user (and an agent acting on their behalf) handles a 5498 — verifying, requesting corrections, archiving

## Examples

- [`examples/traditional-contribution.md`](./examples/traditional-contribution.md) — Simple traditional IRA contribution year; reconciling Box 1 against Schedule 1
- [`examples/roth-conversion-year.md`](./examples/roth-conversion-year.md) — Roth conversion year; reconciling Box 3 with Form 8606 Part II and the 1099-R
- [`examples/rmd-verification.md`](./examples/rmd-verification.md) — 73-year-old verifying Box 11 indicator and reconciling Box 12 RMD against the actual distribution shown on 1099-R

## Sources

Authoritative sources used by this skill. Re-verify each year.

- [Form 5498 (latest)](https://www.irs.gov/pub/irs-pdf/f5498.pdf)
- [Instructions for Forms 1099-R and 5498 (combined)](https://www.irs.gov/pub/irs-pdf/i1099r.pdf)
- [About Form 5498](https://www.irs.gov/forms-pubs/about-form-5498)
- [Publication 590-A](https://www.irs.gov/publications/p590a) — Contributions to IRAs
- [Publication 590-B](https://www.irs.gov/publications/p590b) — Distributions from IRAs
- [Publication 560](https://www.irs.gov/publications/p560) — Retirement Plans for Small Business
- IRC §6047(d) — information returns by retirement plan custodians
- IRC §408(d), §408A — IRA distribution and Roth IRA rules
- Notice 2024-80 — 2025 retirement plan and IRA limits
- Notice 2025-67 — 2026 retirement plan and IRA limits ($7,500 IRA limit, $1,100 catch-up)
- [Form 5498 Explained (2026): IRA Contributions, SEP, and Why It Arrives After You File + AI Agent Skill](https://jupid.com/blog/form-5498-ira-contributions-2026) — Jupid's narrative companion to this skill

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS
forms and publications. It is not tax advice. Form 5498 is informational
only — the user does not file it with their tax return. The recipient's
job is to verify it matches their tax return and resolve any mismatches.
