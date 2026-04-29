# Variant selection — Form 5500 vs. 5500-SF vs. 5500-EZ vs. no filing

The Form 5500 series has three variants. Picking the wrong one is the most common cause of EFAST2 rejection or DOL/IRS correspondence. This reference walks the full decision tree, explains each variant's eligibility, and covers the edge cases.

---

## The three variants at a glance

| Variant | Audience | Filing system | Schedules | Audit |
|---------|----------|---------------|-----------|-------|
| **Form 5500** (full) | Large pension/welfare plans (100+ participants) OR plans with non-eligible assets | EFAST2 only | A, C, D, G, H, MB/SB, R | IQPA audit required if 100+ |
| **Form 5500-SF** (Short Form) | Small pension/welfare plans (< 100 participants) with eligible assets only | EFAST2 only | None (self-contained) | None |
| **Form 5500-EZ** | One-participant plans (owner + spouse, no non-owner employees) | IRS — paper or optional EFAST2 | None | None |

---

## Decision tree

### Step 1 — Is this a Form 5500 plan at all?

```
Plan is SEP-IRA or SIMPLE IRA?
  → No 5500. Stop. (IRA-based, not ERISA pension plan.)

Plan is governmental plan (state/local/federal)?
  → No 5500. Stop. (Title I ERISA exempt, narrow IRC §401(a)(26) exception.)

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

A one-participant plan covers **only**:

- One owner (sole proprietor, single-member LLC member, 100% S-corp shareholder, partner who owns 100% of partnership), AND/OR
- The owner's spouse (so long as the spouse is also an owner — e.g., both partners in a 50/50 LLC or both spouses are sole proprietors with separate businesses)

It must have **no non-owner W-2 employees** participating in the plan during the year.

```
Plan covers only owner(s) + owner's spouse, no non-owner employees?
  → Year-end plan assets ≥ $250,000?  → File 5500-EZ
  → Year-end plan assets < $250,000?  
      → Is this the final plan year (terminating)?  → File 5500-EZ
      → Otherwise: NOT REQUIRED to file (IRC §6058(a) exception, IRS Notice 2011-31)
```

**Multiple one-participant plans by the same employer**: Aggregate the assets of all one-participant plans for the $250,000 test. If the aggregate exceeds $250,000, all the plans must file (each on its own 5500-EZ).

**Adding a non-owner employee**: Plan converts from 5500-EZ filer to 5500-SF / 5500 filer the year the employee becomes eligible (not the year hired). The plan is no longer one-participant.

### Step 3 — Welfare plan exemption (no 5500 at all for many small welfare plans)

```
Plan is a welfare plan (health, dental, vision, life, disability, EAP, etc.)?
  → Participants on first day of plan year < 100?
      → Is the plan funded (trust holds assets)?
          → No (unfunded, fully insured, or combination)?  → EXEMPT under 29 CFR §2520.104-20
          → Yes (plan has a trust)?  → Must file 5500 / 5500-SF
      → Continue
  → Participants ≥ 100?  → Must file Form 5500 + Schedule A (insurance) and possibly Schedule C
```

Most small-employer health plans are exempt because they are fully insured (premiums paid to a carrier, no trust holding plan assets) or unfunded (paid from employer general assets).

### Step 4 — Pension plan size and asset test (5500-SF vs. 5500)

For pension plans (401(k), profit-sharing, money purchase, target benefit, defined benefit) that are not one-participant:

```
Participants on first day of plan year < 100?
  → Plan invests only in "eligible plan assets"?
      → Yes: file 5500-SF (no schedules, no audit)
      → No (plan holds non-eligible assets — see below): file 5500 + Schedule I
  → Continue

Participants ≥ 100?
  → File full 5500 + Schedule H + IQPA audit
```

**80-120 participant rule** (29 CFR §2520.103-1(d)): A plan that filed as a small plan in the prior year may continue filing as small if its participant count at the beginning of the current year is between 80 and 120. This avoids forcing a plan that crosses 100 into a full audit if it's likely to drop back. The plan can elect to remain a small filer until the participant count exceeds 120.

### Eligible plan assets (5500-SF qualification)

A plan's assets are "eligible" if **all** assets are:

- Bank or similar institution deposits (CDs, money market accounts)
- Insurance company general or separate accounts
- Mutual funds (registered investment companies)
- Investment company securities (registered under the Investment Company Act of 1940)
- Publicly traded employer securities held by a participant-directed account
- Participant loans (meeting §72(p) requirements)
- Cash held by trustee/custodian

If any plan asset is **not** on this list, the plan must file 5500 (not 5500-SF). Common non-eligible assets:

- Real estate held directly
- Privately held employer stock (non-public)
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

Multiple corporations under common control are treated as one employer for ERISA purposes. The participant count test applies to the controlled group as a whole.

### Top-heavy plan determination

Top-heavy status is determined separately under IRC §416 — it does NOT affect the 5500 variant choice but does affect contribution requirements.

### Frozen plan

A plan where no new contributions or accruals are made still files 5500 each year until all assets are distributed. The participant count includes all retirees and beneficiaries with vested benefits.

---

## Common variant-selection mistakes

1. **5500-EZ filed when a non-owner employee was on the plan**. The plan was no longer one-participant; the correct form was 5500-SF or 5500. EFAST2 / IRS will reject or correspond.

2. **5500-SF filed when plan held non-eligible assets** (real estate, private LP interest, hedge fund). Must file full 5500 + Schedule H. DOL flags during examination.

3. **No filing when the plan crossed $250,000**. Owner forgot the threshold. IRS penalty $250/day up to $150,000 per IRC §6652(e). Use the IRS one-participant late-filer relief program (Rev. Proc. 2015-32) for $500 flat fee per delinquent return.

4. **Continued filing 5500-SF after participant count exceeded 120**. The 80-120 rule allows continued small-plan filing only up to 120 participants. Above 120, full Form 5500 + audit are required.

5. **Filed 5500 for a terminated plan that hasn't fully distributed assets**. The "final" return is filed only when all assets have been distributed. If assets remain, continue filing as an ongoing plan until distribution is complete.

6. **Used the wrong plan number**. Plan numbers are set at plan inception and remain constant. Switching plan numbers (even by mistake) creates a new "plan" in DOL records and triggers correspondence.

---

## When in doubt

If the plan's variant is genuinely ambiguous (e.g., a plan with one non-owner employee who was let go mid-year, or a plan that crossed 100 participants for one day before dropping back), do **not** guess. Recommend the user consult their TPA, recordkeeper, or ERISA counsel. The cost of consulting is far less than the cost of a wrong-variant filing — DFVC penalties for delinquent filings, IQPA-audit costs for unexpectedly large plans, and DOL examinations.
