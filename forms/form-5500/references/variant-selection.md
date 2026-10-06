# Variant selection — Form 5500 vs. 5500-SF vs. 5500-EZ vs. no filing

The Form 5500 series has three variants. Picking the wrong one is the most common cause of EFAST2 rejection or DOL/IRS correspondence. This reference walks the full decision tree, explains each variant's eligibility, and covers the edge cases.

---

## The three variants at a glance

| Variant | Audience | Filing system | Schedules | Audit |
|---------|----------|---------------|-----------|-------|
| **Form 5500** (full) | Large pension/welfare plans (100+ participants) OR small plans that fail any 5500-SF condition | EFAST2 only | H or I, R, and as applicable A, C, D, G, MB, SB, MEP, DCG | IQPA audit required for large plans; small plans only if the audit waiver is not met |
| **Form 5500-SF** (Short Form) | Small pension/welfare plans (< 100 participants) that meet every 5500-SF condition | EFAST2 only | None, except Schedule SB, MB (lines 3, 9, 10), or MEP when applicable | None (the plan must qualify for the audit waiver) |
| **Form 5500-EZ** | One-participant plans (owners/partners and their spouses only) and foreign plans | Paper to the IRS or EFAST2; EFAST2 required if the filer must file 10+ returns of any type in the calendar year | None (keep Schedule SB/MB in records) | None |

---

## Decision tree

### Step 1 — Is this a Form 5500 plan at all?

```
Plan is SEP-IRA or SIMPLE IRA?
  → No 5500. Stop. (IRA-based, not ERISA pension plan.)

Plan is governmental plan (state/local/federal)?
  → No 5500. Stop. (Listed as exempt in the 2025 Form 5500-SF instructions, Plans Exempt from Filing.)

Plan is non-electing church plan?
  → No 5500. Stop. (Unless plan elected ERISA coverage under IRC §410(d).)

Plan is fringe-benefit only (e.g., §125 cafeteria plan with no underlying welfare component)?
  → No 5500. Stop.

Plan is a §403(b) plan sponsored by a governmental employer?
  → No 5500. Stop.

Plan is a §403(b) plan sponsored by a non-governmental, non-church employer with employer contributions or discretionary involvement?
  → ERISA 403(b) — file 5500. Continue.
```

### Step 2 — One-participant plan test (5500-EZ candidate)

A one-participant plan (2025 Form 5500-EZ instructions, Who Must File) is a retirement plan, other than an ESOP, that:

- Covers only the owner (or the owner and spouse), and the owner (or owner and spouse) owns the entire business, incorporated or unincorporated; or
- Covers only one or more partners (or partners and their spouses) in a partnership, treating a 2% S corporation shareholder as a partner; and
- Provides benefits for no one else.

The spouse does not have to be an owner. Any covered non-owner employee ends one-participant status.

```
Plan covers only owner(s)/partners and their spouses?
  → Year-end plan assets (all one-participant plans of the employer combined) > $250,000?  → File 5500-EZ
  → Combined year-end assets $250,000 or less?
      → Is this the final plan year (terminating)?  → File 5500-EZ
      → Otherwise: NOT REQUIRED to file (2025 Form 5500-EZ instructions, Who Does Not Have To File)
```

**Multiple one-participant plans by the same employer**: Aggregate the assets of all one-participant plans for the $250,000 test, using line 6a(2). If the aggregate exceeds $250,000, all the plans must file (each on its own 5500-EZ).

**Adding a non-owner employee**: Once the plan covers a non-owner employee it is no longer a one-participant plan; it becomes a Title I plan filing Form 5500-SF or Form 5500. A one-participant plan cannot file Form 5500-SF (5500-EZ instructions, Purpose of Form). Ask the user when the employee entered the plan.

### Step 3 — Welfare plan exemption (no 5500 at all for many small welfare plans)

```
Plan is a welfare plan (health, dental, vision, life, disability, EAP, etc.)?
  → Participants on first day of plan year < 100?
      → Is the plan funded (trust holds assets)?
          → No (unfunded, fully insured, or combination)?  → EXEMPT under 29 CFR §2520.104-20
          → Yes (plan has a trust)?  → Must file 5500 / 5500-SF
      → Continue
  → Participants ≥ 100?  → Must file Form 5500 + Schedule A (insurance), Schedule C if applicable, and Schedule H unless fully insured/unfunded under 29 CFR 2520.104-44
```

Most small-employer health plans are exempt because they are fully insured (premiums paid to a carrier, no trust holding plan assets) or unfunded (paid from employer general assets).

### Step 4 — Pension plan size and asset test (5500-SF vs. 5500)

For pension plans (401(k), profit-sharing, money purchase, target benefit, defined benefit) that are not one-participant. Count participants on the first day of the plan year; defined contribution plans count only participants with account balances (Form 5500-SF line 5c(1), Form 5500 line 6g(1); end-of-year count on a first return):

```
Participants on first day of plan year < 100 (or 80-120 rule)?
  → Every 5500-SF condition met (100% eligible plan assets, no employer securities,
    audit waiver met without enhanced bonding, not multiemployer / PEP / M-1 filer / ESOP / DCG)?
      → Yes: file 5500-SF (no audit)
      → No: file 5500 + Schedule I (IQPA report only if the audit waiver is not met, Schedule I line 4k "No")
  → Continue

Participants ≥ 100 (and 80-120 rule not elected)?
  → File full 5500 + Schedule H + IQPA audit
```

**80-120 participant rule** (29 CFR §2520.103-1(d)): A plan that filed as a small plan (Form 5500-SF, or Form 5500 with Schedule I) for 2024 may elect to file as a small plan for 2025 if it covers no more than 120 participants at the beginning of the 2025 plan year (2025 Form 5500 instructions, What To File, Exception (1)).

### Eligible plan assets (5500-SF qualification)

"Eligible plan assets" (2025 Form 5500-SF instructions, line 6a) have a readily determinable fair market value, are not employer securities, and are held or issued by a bank or similar institution, a state-qualified insurance company, a registered broker-dealer, a registered investment company, or another organization authorized to act as an IRA trustee. Examples:

- Mutual fund shares
- Investment contracts with insurance companies or banks that value the contract at least annually
- Publicly traded stock held by a registered broker-dealer
- Cash and cash equivalents held by a bank
- Participant loans meeting ERISA §408(b)(1), even if deemed distributed

If any plan asset is **not** eligible at any time during the year, the plan must file 5500 (not 5500-SF). Common non-eligible assets:

- Any employer securities, publicly traded or not
- Real estate, even if held by a bank as trustee
- Limited partnership interests
- Hedge funds, private equity funds
- Tangible personal property
- Collectibles
- Loans to non-participants

---

## Edge cases

### Final return (terminating plan)

When a plan terminates, file a **final 5500** (any variant) for the year all assets are distributed. Mark "the final return/report" box. The plan number remains the same; do not reuse the plan number for a new plan.

For 5500-EZ, the final filing is required even if year-end assets are below $250,000 (the $250,000 exemption does not apply in the final year).

### Short plan year

If the plan year is less than 12 months (initial year, plan year change, plan termination mid-year), the filing is still required. Mark "short plan year" box. Due date adjusts based on the short year-end.

### Initial year

For a plan's first year, file the 5500 for that year (any variant, based on the rules above). The plan effective date and the plan year's start date may differ — the plan effective date is when the plan first existed; the plan year's start date is when the reporting year begins.

### Plan year change

If the plan changes its plan year (e.g., from calendar to fiscal), file two returns: one for the old short plan year ending the day before the change, one for the new plan year. The transitional short year requires its own 5500.

### Multiple plans sponsored by the same employer

Each plan files its own 5500. Plan numbers must differ (001, 002, 003 for pension; 501, 502 for welfare). Do not consolidate.

### Multiple-employer plans (MEPs) / Pooled employer plans (PEPs)

Filed at the plan level by the lead employer / pooled plan provider, not by each participating employer. The PEP / MEP's 5500 includes participant data for all participating employers.

### Controlled group / affiliated service group

A controlled group (Code §414(b), (c), or (m)) is generally considered one employer for Form 5500 and Form 5500-SF reporting, so a plan covering several members checks the single-employer box (2025 Form 5500-SF instructions, Line A). Participants are still counted plan by plan. Enter plan characteristic code 3H.

### Top-heavy plan determination

Top-heavy status is determined separately under IRC §416 — it does NOT affect the 5500 variant choice but does affect contribution requirements.

### Frozen plan

A plan where no new contributions or accruals are made still files 5500 each year until all assets are distributed. The participant count includes all retirees and beneficiaries with vested benefits.

---

## Common variant-selection mistakes

1. **5500-EZ filed when a non-owner employee was on the plan**. The plan was no longer one-participant; the correct form was 5500-SF or 5500. EFAST2 / IRS will reject or correspond.

2. **5500-SF filed when plan held non-eligible assets** (real estate, private LP interest, hedge fund). Must file full 5500 + Schedule H. DOL flags during examination.

3. **No filing when the plan crossed $250,000**. Owner forgot the threshold. IRS penalty $250/day up to $150,000 per IRC §6652(e). Use the IRS late filer penalty relief program (Rev. Proc. 2015-32): $500 per delinquent return, maximum $1,500 per plan, paper filing only.

4. **Continued filing 5500-SF after participant count exceeded 120**. The 80-120 rule allows continued small-plan filing only up to 120 participants. Above 120, full Form 5500 + audit are required.

5. **Filed 5500 for a terminated plan that hasn't fully distributed assets**. The "final" return is filed only when all assets have been distributed. If assets remain, continue filing as an ongoing plan until distribution is complete.

6. **Used the wrong plan number**. Plan numbers are set at plan inception and remain constant. Switching plan numbers (even by mistake) creates a new "plan" in DOL records and triggers correspondence.

---

## When in doubt

If the plan's variant is genuinely ambiguous (e.g., a plan with one non-owner employee who was let go mid-year, or a plan that crossed 100 participants for one day before dropping back), do **not** guess. Recommend the user consult their TPA, recordkeeper, or ERISA counsel. The cost of consulting is far less than the cost of a wrong-variant filing — DFVC penalties for delinquent filings, IQPA-audit costs for unexpectedly large plans, and DOL examinations.
