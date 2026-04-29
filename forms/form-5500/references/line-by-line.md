# Form 5500 Series Line-by-Line Reference

Lookup for Form 5500, Form 5500-SF, and Form 5500-EZ. Use when the agent needs to confirm where a piece of plan data belongs or what a line means.

The DOL / IRS revise the 5500 series annually. Line numbers are stable but new compliance questions get added (e.g., the late-deferral test, the cybersecurity item). Always verify line labels against the most recent revision at https://www.dol.gov/agencies/ebsa/employers-and-advisers/plan-administration-and-compliance/reporting-and-filing/form-5500.

---

## Form 5500-EZ (one-participant plans)

The simplest variant. ~25 numbered items.

### Header

| Line | Field | What goes here |
|------|-------|----------------|
| Plan year (top) | Beginning / ending dates | Calendar year is most common |
| A | Type of plan (check all that apply) | Defined contribution / defined benefit / multiple |
| B | Type of return (check) | First / amended / final / short year |
| C | Plan effective date | When plan was first established |
| D | Plan number (PN) | 001 (first pension plan); use prior year's PN if continuing |

### Sponsor / administrator

| Line | Field | What goes here |
|------|-------|----------------|
| 1a | Plan sponsor's legal name | Match plan document; not the trust |
| 1b | EIN | Sponsor's EIN; not plan trust EIN |
| 1c | Address | Sponsor's principal place of business |
| 1d | Phone | Direct contact |
| 2a | Plan administrator name | Often same as sponsor |
| 2b | Administrator EIN | If different from sponsor |
| 3a | Did you change plan sponsor or admin since last 5500-EZ? | Y/N |
| 3b–3d | If yes, prior info | Document the change |

### Participants

| Line | Field | What goes here |
|------|-------|----------------|
| 4a | Total participants at year start | Owner + spouse |
| 4b | Total participants at year end | Owner + spouse |
| 5 | Plan characteristics codes | List from instructions; typical solo 401(k): 2J (safe harbor), 3D (matching), 3F (profit sharing) |

### Plan financial info

| Line | Field | What goes here |
|------|-------|----------------|
| 6a | Total plan assets at year start | Beginning fair-market value |
| 6b | Total plan assets at year end | Ending fair-market value |
| 7a | Total income (contributions + earnings) | All inflows during plan year |
| 7b | Total expenses (distributions + admin) | All outflows |
| 7c | Net change in plan assets | 7a − 7b |
| 8 | Benefits paid to participants | Distributions during year |
| 9 | Plan administration expenses | Trustee, recordkeeper, audit fees |

### Compliance questions

| Line | Question | Answer |
|------|----------|--------|
| 10 | Plan termination indicated? | Y/N |
| 11a | Did the plan participate in any prohibited transaction? | Y/N (file Form 5330 if Y) |
| 11b | Did the plan have a loss due to fraud or dishonesty? | Y/N |
| 11c | Did the plan have any unrelated business income? | Y/N (file Form 990-T if Y) |

### Sign here

Plan administrator (usually the owner-employee) signs and dates.

### Required attachments

5500-EZ is self-contained. **No schedules** attach.

---

## Form 5500-SF (small plan, simplified)

For plans with < 100 participants that meet the eligible-asset test. Eligible plans: 100% mutual funds / publicly-traded securities / annuity contracts / participant-directed accounts in eligible vehicles. Excluded: real estate, private equity, hard-to-value assets, employer securities (except publicly-traded).

### Header — same as full 5500

### Sponsor / administrator — same as full 5500

### Participant count

- **Line 5a–5e** — Active participants, retired/separated with vested benefits, beneficiaries, deceased participants whose beneficiaries are receiving, total
- **Line 6** — number of active participants

### Plan funding / benefits arrangement

- **Line 7** — funding (insurance, trust, general assets, etc.)
- **Line 8** — benefits (insurance, trust, general assets)
- **Line 9** — plan characteristics codes

### Plan compliance

- **Line 10a** — Was the plan covered by a fidelity bond? (ERISA §412 requires; minimum 10% of plan assets, max $500K, or $1M if plan holds employer securities)
- **Line 10b** — Did any contributions to the plan fail to be remitted within 7 business days (small plan safe harbor) or "as soon as administratively feasible" (large plan)? **Late deferrals = DOL hot button**. If Y, file Form 5330 for 15% excise tax under IRC §4975.
- **Line 10c** — Did the plan have any prohibited transactions? File Form 5330 if Y.
- **Line 10d** — Did the plan have a loss due to fraud / dishonesty? Trustees may have personal liability.
- **Line 10e** — In-service distributions to non-terminated participants?
- **Line 10f** — Were ADP / ACP nondiscrimination tests passed? (For 401(k)s that aren't safe harbor)

### Schedule SB (DB plans only)

If the plan is a defined benefit plan, attach Schedule SB with actuarial certifications.

### Financial info

- **Line 7a–7m** — Asset categories and totals
- **Line 8a–8d** — Income (contributions, gains, etc.)
- **Line 8e–8m** — Expenses (benefits paid, admin, etc.)

### Sign here

Filer authentication via EFAST2 PIN.

### Required attachments — none for 5500-SF

The whole point of 5500-SF is "no schedules". If a schedule would otherwise be required, the plan can't use 5500-SF — must use full Form 5500.

---

## Form 5500 (full)

For plans with 100+ participants OR plans that don't meet the eligible-asset test.

### Header — same as 5500-SF

### Sponsor / administrator — same as 5500-SF

### Participant count — same structure as 5500-SF

### Plan compliance questions — same as 5500-SF, plus:

- **Line 11** — IQPA audit info (large plans: required attachment)
- **Line 12** — Participant directed accounts indicator
- **Schedule R** — retirement plan info (separate schedule; line on 5500 says "Schedule R attached")
- **Schedule MB / SB** — DB actuarial info

### Schedules summary lines

Form 5500 main form has summary lines that pull totals from each attached schedule. The schedules themselves contain the detail.

### Schedule attachments — see [`schedules.md`](./schedules.md)

Common combinations:

| Plan type | Attachments |
|-----------|-------------|
| Large 401(k) DC plan | Schedule H, Schedule R, Schedule C (if any provider > $5K), Schedule A (if any insurance) |
| Large welfare plan | Schedule H, Schedule A (insurance contracts), Schedule C |
| Single-employer DB | Schedule H, Schedule R, Schedule SB, Schedule C |
| Multiemployer DB | Schedule H, Schedule MB, Schedule R, Schedule C |
| Master trust investment account | Schedule H, Schedule D |

### IQPA audit attachment (large plans)

ERISA §103(a)(3)(A) and 29 CFR §2520.103-1(c) require an audit by an Independent Qualified Public Accountant for "large" plans. Audit report is attached as a PDF on Schedule H.

Audit categories:
- **Full scope audit** — auditor opines on the entire plan financials
- **Limited-scope audit** (called "ERISA section 103(a)(3)(C) audit" since 2021) — bank/insurance company certifies investment values; auditor reviews the rest. Cheaper but produces a "limited scope" opinion.

---

## Schedule H — Large plan financial info (most complex schedule)

Required for any plan filing full Form 5500 with 100+ participants.

### Part I — Asset and liability statement (year-end)

| Line | Field | Notes |
|------|-------|-------|
| 1a | Total assets | All asset categories sum |
| 1b–1l | Asset categories | Cash, receivables, investments by type, real estate, employer securities, loans to participants, buildings, other |
| 2 | Total liabilities | Loan offsets, payables, accruals |
| 3 | Net assets | 1a − 2 |

### Part II — Income and expenses

| Line | Field | Notes |
|------|-------|-------|
| 2a | Total income | Contributions + investment earnings |
| 2a(1)–(3) | Contribution categories | Employer, participant, others (rollovers) |
| 2b | Investment earnings | Interest, dividends, gains/losses |
| 2c | Other income | |
| 2d | Total income | Sum |
| 2e | Total benefits paid | Distributions to participants/beneficiaries |
| 2f | Other expenses | Admin, audit, legal |
| 2i | Net change | Total income − total expenses |

### Part III — Accountant's opinion

Indicate type of audit opinion: unqualified, qualified, adverse, disclaimer, or §103(a)(3)(C) limited-scope.

### Part IV — Compliance questions (40+ Yes/No items)

This is where DOL examiners focus. Examples:
- Were any plan assets transferred to or from the plan in a non-arm's-length transaction?
- Were any participant contributions remitted late?
- Did the plan have a fidelity bond?
- Did the plan engage in any prohibited transactions?
- Was there any cybersecurity incident?

Every "Yes" requires an attachment or further detail. The agent should walk each question carefully — wrong answers (especially on the late-deferral question) are common audit triggers.

### Part V — Trust info

For plans whose assets are held in trust: trustee name, EIN, address, type of trust.

---

## Schedule I — Small plan financial info (when 5500-SF can't be used)

For pension plans with < 100 participants that don't qualify for 5500-SF (e.g., investing in real estate or private equity). Less detailed than Schedule H but more than 5500-SF.

---

## Schedule A — Insurance contract info

Required for any plan that has an insurance contract (welfare or pension). Insurance company files this (or the plan administrator copies it from the carrier). Includes:
- Carrier name, EIN, NAIC code
- Policy number
- Premiums paid
- Commissions paid
- Type of contract (group health, life, annuity, etc.)

---

## Schedule C — Service provider compensation

Large plans only. Required for any service provider receiving > $5,000 in direct + indirect compensation:
- Name
- EIN
- Service code (recordkeeping, audit, legal, investment management, etc.)
- Direct compensation (paid by plan)
- Indirect compensation (revenue sharing, 12b-1 fees, etc.)
- Eligible indirect compensation (alternative reporting if extensive)

This schedule has been a DOL focus since 2009 (transparency on plan fees).

---

## Schedule R — Retirement plan info

For pension plans. Includes:
- Distributions during the year
- Vesting schedules
- Funded percentage (DC plans)
- Employer profit-sharing contributions
- ADP / ACP test results
- Rollover info

---

## Schedule SB — Single-employer DB actuarial

For single-employer defined benefit plans only. Filed by enrolled actuary. Includes:
- Funding target (PPA)
- Target normal cost
- Actuarial value of assets
- Funding shortfall / surplus
- Employer contributions

---

## Schedule MB — Multiemployer DB actuarial

For multiemployer defined benefit plans (collectively bargained, multiple unrelated employers). Includes funded status, withdrawal liability, etc.

---

## Schedule D — Plan participation in DFE (master trust)

For plans whose assets are pooled in a Master Trust Investment Account (MTIA), Common/Collective Trust (CCT), Pooled Separate Account (PSA), or Group Insurance Arrangement (GIA).

---

## Schedule G — Financial transactions

Large plans only, when applicable. Reports:
- Loans / fixed income obligations in default or uncollectible
- Lease leases / non-routine transactions
- Reportable transactions exceeding 5% of plan assets

---

## Form 5558 — Application for Extension

Single-page form. Filed with IRS Ogden by original due date. 2.5-month extension to:
- October 15 for calendar plan year (instead of July 31)
- Or 2.5 months after the regular due date for non-calendar plans

5558 must be **filed by the original due date** to be effective. Late 5558 = no extension.
