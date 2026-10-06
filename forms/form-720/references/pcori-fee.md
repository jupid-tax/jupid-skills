# PCORI Fee Deep Dive

The Patient-Centered Outcomes Research Institute (PCORI) fee, called the patient-centered outcomes research (PCOR) fee on Form 720, is an annual federal fee imposed on issuers of specified health insurance policies (§4375) and plan sponsors of applicable self-insured health plans (§4376). It funds the Patient-Centered Outcomes Research Trust Fund. It applies to policy and plan years ending after Sep 30, 2012, and before Oct 1, 2029 (§4375(e), §4376(e); Notice 2025-61 §II).

**Verified against:** Form 720 (Rev. June 2026) line 133, Instructions for Form 720 (Rev. June 2026), Notices 2023-70, 2024-83, 2025-61, and Treas. Reg. §46.4376-1, on 2026-10-06.

PCORI is the most commonly asked-about Form 720 item for small businesses with self-insured health plans, HRAs, FSAs (sometimes), and certain levels of stop-loss arrangements.

---

## Who owes the PCORI fee

### Self-insured plan sponsors (§4376)

The plan sponsor of an "applicable self-insured health plan" pays the fee. "Plan sponsor" is generally the employer (for single-employer plans) or the plan committee (for multi-employer plans).

Self-insured plans subject to PCORI include:
- Traditional self-insured medical plans (employer pays claims directly)
- Health Reimbursement Arrangements (HRAs) — most types
- Health FSAs that are not excepted benefits (a health FSA that qualifies as an excepted benefit is not subject)
- Retiree-only health plans (yes, taxable)

### Issuers of specified health insurance policies (§4375)

The insurance company pays the fee on premiums it issues. Captive insurance companies and small group plans are typically subject.

### Common exclusions

- HSA contributions themselves (not a plan)
- Stand-alone vision and dental "excepted benefits" plans
- Most FSAs that qualify as "excepted benefits" under HIPAA
- Employee Assistance Programs (EAPs) without significant medical benefits
- Plans designed specifically to cover primarily employees working and residing outside the United States (Treas. Reg. §46.4376-1(b)(1)(ii)(C))

If the user is unsure whether their HRA/FSA is subject to PCORI, the agent walks the Treas. Reg. §46.4376-1(b)(1) definition and exceptions with them.

---

## Plan-year-ending → filing year mapping

PCORI is **annual**, filed on the **Q2 Form 720 due July 31 of the calendar year immediately following the last day of the plan year** (i720 "Reporting and paying the fee").

| Plan year ends | File Form 720 by |
|----------------|------------------|
| Jan 1, 2025 – Sep 30, 2025 | July 31, 2026 (Q2 2026 form) |
| Oct 1, 2025 – Dec 31, 2025 | July 31, 2026 (Q2 2026 form) |
| Jan 1, 2026 – Sep 30, 2026 | July 31, 2027 (Q2 2027 form) |

The plan year **ending date** determines the applicable rate (see next section). The filing is always on the Q2 form following the end of the plan year.

---

## Applicable rate (changes annually)

The PCORI rate is set by IRS notice each year. Recent rates:

| Plan year ending | Rate per covered life | Source |
|------------------|----------------------|--------|
| Oct 1, 2022 – Sep 30, 2023 | $3.00 | Notice 2022-59 |
| Oct 1, 2023 – Sep 30, 2024 | $3.22 | Notice 2023-70 |
| Oct 1, 2024 – Sep 30, 2025 | $3.47 | Notice 2024-83 (Form 720 rows 133(a) and 133(c)) |
| Oct 1, 2025 – Sep 30, 2026 | $3.84 | Notice 2025-61 (Form 720 rows 133(b) and 133(d)) |
| Oct 1, 2026 – Sep 30, 2027 | Not yet published on 2026-10-06; the IRS issues a notice each fall. ASK the user to wait for it or check irs.gov before computing. | — |

The rate is fixed by the **plan-year-ending date**, NOT the calendar year of filing. A plan year ending September 2024 uses the Notice 2023-70 rate ($3.22), even though it's filed in 2025. A plan year ending December 31, 2024 uses $3.47 and was due July 31, 2025; a plan year ending December 31, 2025 uses $3.84 and was due July 31, 2026.

---

## Counting "covered lives"

Per Treas. Reg. §46.4376-1(c)(2), self-insured plan sponsors choose ONE of three methods to count covered lives. The same method must be used for the whole plan year; a different method may be used the next plan year (§46.4376-1(c)(2)(ii)). Issuers of specified health insurance policies have four methods: actual count, snapshot, member months, and state form (i720 "Specified health insurance policies").

### Method 1 — Actual count

Sum the number of lives covered each day of the plan year, divide by the number of days in the plan year.

```
average_covered_lives = sum(daily_count[1..N]) / N
```

Most precise, requires daily payroll/HRIS data.

### Method 2 — Snapshot

Count lives covered on a date in the first, second, or third month of each quarter (or on more dates per quarter if the same number of dates is used in each quarter). Average the counts.

```
average_covered_lives = sum(snapshot_count[1..K]) / K
```

Less precise, more practical for small employers.

Each date used in the second, third, and fourth quarters must be within three days of the date that corresponds to the first-quarter date, and all dates must fall within the same plan year. The 30th and 31st are treated as the last day of the month (e.g., March 31 corresponds to June 30) (§46.4376-1(c)(2)(iv)(A)). The count on each date can be the actual number of lives (snapshot count method) or self-only participants plus 2.35 × participants with other than self-only coverage (snapshot factor method, §46.4376-1(c)(2)(iv)(B)–(C)).

### Method 3 — Form 5500

Use the participant counts at the beginning and end of the plan year reported on the plan's Form 5500 or Form 5500-SF (§46.4376-1(c)(2)(v)):

```
self-only coverage only:                 average_covered_lives = (participants at beginning + participants at end) / 2
self-only and other than self-only:      average_covered_lives =  participants at beginning + participants at end
```

This method is available only if the Form 5500 or 5500-SF for that plan year is filed no later than the PCOR fee due date (July 31). A Form 5500 filed later under an extension disqualifies the method for that year (§46.4376-1(c)(2)(v), Example 1).

### Special HRA rule — count only employee-covered lives

If the plan sponsor does not maintain any applicable self-insured health plan other than a health FSA or HRA, it may treat each participant's HRA or FSA as covering a single life: spouses and dependents are not counted (§46.4376-1(c)(2)(vi)). This applies, for example, to an HRA paired with a fully insured medical plan.

For a 50-employee stand-alone HRA, covered lives = 50 (regardless of how many family members are also eligible).

If the HRA has the same plan sponsor and plan year as a self-insured medical plan, the two may be treated as one plan (§46.4376-1(b)(1)(iii)); then HRA participants who are also in the medical plan are counted under the medical plan's method, and only HRA-only participants get the single-life rule.

---

## Computation examples

### Example A — Small self-insured medical plan

- Plan year: Jan 1, 2025 – Dec 31, 2025
- Method: Actual count (HRIS daily roster)
- Average covered lives: 87 (employees + spouses + dependents enrolled)
- Plan year ending date: Dec 31, 2025 (within Oct 1, 2025 – Sep 30, 2026 range)
- Rate: $3.84 (Notice 2025-61; Form 720 row 133(d))
- PCORI fee = 87 × $3.84 = $334.08

Per i720 "Reporting and paying the fee", the fee is due July 31 of the calendar year immediately following the last day of the plan year. Plan year ending Dec 31, 2025 → due July 31, 2026 (Q2 2026 form). Plan year ending June 30, 2025 → due July 31, 2026, at $3.47 (row 133(c)). Plan year ending June 30, 2026 → due July 31, 2027.

### Example B — HRA only

- Plan year: Jan 1, 2025 – Dec 31, 2025
- Number of employees with HRA: 50
- HRA rule: the sponsor has no other self-insured plan (its medical plan is fully insured), so each participant counts as one life (§46.4376-1(c)(2)(vi))
- Covered lives: 50
- PCORI fee: 50 × $3.84 = $192.00

Filed on Q2 2026 Form 720, due July 31, 2026.

### Example C — Multiple plans (combined HRA + medical)

If the employer has both a self-insured medical plan AND an HRA with the same plan year, the IRS allows treating them as one plan (Treas. Reg. §46.4376-1(b)(1)(iii)):

- HRA covered lives: 50 (employee-only count)
- Medical plan covered lives: 87 (full count)
- The HRA is treated as covering the same lives as the medical plan (no double-counting)
- Total covered lives: 87, if every HRA participant is also in the medical plan
- PCORI fee: 87 × $3.84 = $334.08

But: HRA participants who are not in the medical plan are added as one life each (§46.4376-1(c)(2)(vi)). If the plan years differ, the plans can't be combined.

---

## Filing mechanics on Form 720

PCORI is reported on Part II, IRS No. 133:

| Row | Applies to | Columns |
|-----|------------|---------|
| 133(a) | Specified health insurance policies, policy year ending before Oct 1, 2025 | (a) average lives covered, (b) $3.47, (c) fee |
| 133(b) | Specified health insurance policies, policy year ending Oct 1, 2025 – Sep 30, 2026 | (a), (b) $3.84, (c) |
| 133(c) | Applicable self-insured health plans, plan year ending before Oct 1, 2025 | (a), (b) $3.47, (c) |
| 133(d) | Applicable self-insured health plans, plan year ending Oct 1, 2025 – Sep 30, 2026 | (a), (b) $3.84, (c) |

Combine the fees from all rows into one entry in the "Tax" column for IRS No. 133. That amount is part of Part II line 2, which flows to Part III line 3.

PCORI does NOT require:
- Schedule A (Part II taxes are never on Schedule A)
- Semimonthly deposits (i720 "Payment of Taxes")
- Schedule C or Schedule T

Pay the fee with the Q2 return: EFTPS, IRS Direct Pay, electronic funds withdrawal when e-filing, or check or money order with Form 720-V. If paid through EFTPS, apply the payment to the second quarter (i720 "Reporting and paying the fee").

---

## Common PCORI mistakes

1. **Counting spouses/dependents on HRA**: HRA is employee-only (per regs). Counting all family members over-pays.

2. **Wrong rate for plan-year-end**: rate is fixed by plan-year-end date, not filing year. A plan year ending June 30, 2024 uses the Oct 2023 – Sep 2024 rate ($3.22 from Notice 2023-70), not the rate for the year of filing. On the current form, putting a calendar-2025 plan on row 133(c) at $3.47 instead of row 133(d) at $3.84 underpays.

3. **Filing on wrong quarter form**: PCORI is always on the Q2 form (July 31). Filers who file Form 720 in other quarters for other taxes leave IRS No. 133 blank on the Q1, Q3, and Q4 returns.

4. **Forgetting to file**: small employers with self-insured plans (HRAs especially) frequently miss the PCORI obligation. The §6651(a)(1) failure-to-file penalty is 5% of the unpaid tax per month or part of a month (max 25%), so a $300 fee can grow by $75 before interest and the failure-to-pay penalty.

5. **Confusing PCORI with the ACA "Health Insurance Provider Fee"**: the latter (§9010) was repealed effective 2021. Don't conflate.

6. **Switching counting methods mid-year**: pick Actual / Snapshot / Form 5500 and use it for the whole plan year (§46.4376-1(c)(2)(ii)).

7. **Not filing in the year a plan terminates**: even a plan that ends mid-year owes PCORI on the partial year's covered lives. The agent should not assume "no plan = no fee" — the partial plan year is still subject.

---

## Quick decision tree

```
Q: Does the user sponsor a self-insured health plan, HRA, or applicable FSA?
   No → no PCORI fee, skip
   Yes → continue

Q: What is the plan-year-end date?
   Use this to determine the applicable rate and Form 720 row (table above).

Q: Have they chosen a covered-lives counting method?
   No → ASK which method they will use (actual count, snapshot, or Form 5500 if
        the Form 5500 is filed by July 31); show the data each one needs; don't pick
   Yes → use the user's chosen method

Q: What's the average covered lives count?
   Compute per chosen method.

Q: What's the PCORI fee?
   covered_lives × rate

Q: Filing deadline?
   July 31 of the calendar year following the plan-year-end.
   File on the Q2 Form 720 of that filing year.
```

The agent runs this decision tree and surfaces the result on the SKILL.md output template.
