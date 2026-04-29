# PCORI Fee Deep Dive

The Patient-Centered Outcomes Research Institute (PCORI) fee is an annual federal fee imposed on issuers of certain health insurance policies (§4375) and plan sponsors of self-insured health plans (§4376). It funds the PCORI nonprofit research institute.

PCORI is the most commonly asked-about Form 720 item for small businesses with self-insured health plans, HRAs, FSAs (sometimes), and certain levels of stop-loss arrangements.

---

## Who owes the PCORI fee

### Self-insured plan sponsors (§4376)

The plan sponsor of an "applicable self-insured health plan" pays the fee. "Plan sponsor" is generally the employer (for single-employer plans) or the plan committee (for multi-employer plans).

Self-insured plans subject to PCORI include:
- Traditional self-insured medical plans (employer pays claims directly)
- Health Reimbursement Arrangements (HRAs) — most types
- FSAs (only "non-excepted" FSAs; most FSAs are "excepted benefits" and exempt)
- Retiree-only health plans (yes, taxable)

### Issuers of specified health insurance policies (§4375)

The insurance company pays the fee on premiums it issues. Captive insurance companies and small group plans are typically subject.

### Common exclusions

- HSA contributions themselves (not a plan)
- Stand-alone vision and dental "excepted benefits" plans
- Most FSAs that qualify as "excepted benefits" under HIPAA
- Employee Assistance Programs (EAPs) without significant medical benefits
- Plans covering only employees outside the US

If the user is unsure whether their HRA/FSA is subject to PCORI, the agent walks the IRS Reg. §46.4376-1(a)(2) tests with them.

---

## Plan-year-ending → filing year mapping

PCORI is **annual**, filed on the **Q2 Form 720 (due July 31)** for the plan year **ending in the prior 12 months**.

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
| Oct 1, 2024 – Sep 30, 2025 | $3.22 | Notice 2024-83 |
| Oct 1, 2025 – Sep 30, 2026 | TBD — verify against IRS notice (typically issued late 2025 / early 2026) | TBD |

The rate is fixed by the **plan-year-ending date**, NOT the calendar year of filing. A plan year ending September 2024 uses the Notice 2023-70 rate ($3.22), even though it's filed in 2025.

Note: the IRS announced the same $3.22 rate for two consecutive years (2023-2024 and 2024-2025) — this is the only year-pair where rates didn't change. Verify the agent uses the right rate for the right plan-year-end.

---

## Counting "covered lives"

Per IRS Reg. §46.4376-1(c)(2), self-insured plan sponsors choose ONE of three methods to count covered lives. Once chosen, the method should be used consistently within a plan year.

### Method 1 — Actual count

Sum the number of lives covered each day of the plan year, divide by the number of days in the plan year.

```
average_covered_lives = sum(daily_count[1..N]) / N
```

Most precise, requires daily payroll/HRIS data.

### Method 2 — Snapshot

Pick at least one day per quarter (4 days minimum). Average the count on those snapshot days.

```
average_covered_lives = sum(snapshot_count[1..K]) / K
```

Less precise, more practical for small employers.

The snapshot date must be in approximately the same position within each quarter (e.g., the last day of the quarter, or the 15th of the second month). Variation > 3 days requires explanation.

### Method 3 — Form 5500

Use Schedule MD of Form 5500 (annual benefit plan return). For plans with one type of coverage (e.g., self+spouse only), use:

```
average_covered_lives = (5500 Line 5 + 5500 Line 6) / 2
```

This method works only if the plan files Form 5500 by the PCORI Form 720 due date. New plans (year-1) typically use Method 2 (Snapshot).

### Special HRA rule — count only employee-covered lives

For HRAs (and certain other "excepted-benefit-like" arrangements), the rule is **only the employee** counts as a covered life — not spouse or dependents. This is a major reduction from the typical "all enrolled" count.

For a 50-employee HRA, covered lives = 50 (regardless of how many family members are also enrolled).

---

## Computation examples

### Example A — Small self-insured medical plan

- Plan year: Jan 1, 2025 – Dec 31, 2025
- Method: Actual count (HRIS daily roster)
- Average covered lives: 87 (employees + spouses + dependents enrolled)
- Plan year ending date: Dec 31, 2025 (within Oct 1, 2025 – Sep 30, 2026 range)
- Rate: $TBD (must verify against successor to Notice 2024-83)

If we hypothesize the rate stays at $3.22:
- PCORI fee = 87 × $3.22 = $280.14

Filed on Q2 2026 Form 720 (due July 31, 2026). Wait — the plan year ends Dec 31, 2025, so it's actually filed on the Q2 2026 form (filing year is the year following the plan-year-end's calendar year). Confirm by checking the latest Form 720 instructions for the year being filed.

Actually, let's re-check: per IRS Reg. §46.4376-1(d), the fee is due July 31 of the calendar year **immediately following** the last day of the policy/plan year. Plan year ending Dec 31, 2025 → due July 31, 2026 (Q2 2026 form). Plan year ending June 30, 2025 → due July 31, 2026 (Q2 2026 form). Plan year ending June 30, 2026 → due July 31, 2027 (Q2 2027 form).

### Example B — HRA only

- Plan year: Jan 1, 2025 – Dec 31, 2025
- Number of employees with HRA: 50
- HRA rule: count only employees (not spouses/dependents)
- Covered lives: 50
- PCORI fee: 50 × $3.22 = $161.00

Filed on Q2 2026 Form 720, due July 31, 2026.

### Example C — Multiple plans (combined HRA + medical)

If the employer has both a self-insured medical plan AND an HRA, the IRS allows combining (per Reg. §46.4376-1(b)(2)):

- HRA covered lives: 50 (employee-only count)
- Medical plan covered lives: 87 (full count)
- The HRA is treated as covering the same lives as the medical plan (no double-counting)
- Total covered lives: 87 (the larger count; HRA "rides" the medical count)
- PCORI fee: 87 × $3.22 = $280.14

But: if the HRA covers different employees than the medical plan, count separately. Verify with Reg. §46.4376-1(b)(2).

---

## Filing mechanics on Form 720

PCORI is reported on Part II Line 133:

| Line | Field | Value |
|------|-------|-------|
| (a) IRS No. | (preprinted) | 133 |
| (b) Type of tax | (preprinted) | Patient-Centered Outcomes Research |
| Avg # covered lives — applicable self-insured | (input) | covered lives count |
| Rate | (input) | $3.22 (verify for plan-year-end range) |
| (c) Tax | (computed) | covered lives × rate |

The amount flows to Part III Line 2 (Total Part II) → Part III Line 3 → Line 5 (Net tax).

PCORI does NOT require:
- Schedule A (semi-monthly deposits)
- Schedule C claims (not refundable)
- Schedule T

Payment is made with the Q2 return via EFTPS (or check if below electronic-payment threshold).

---

## Common PCORI mistakes

1. **Counting spouses/dependents on HRA**: HRA is employee-only (per regs). Counting all family members over-pays.

2. **Wrong rate for plan-year-end**: rate is fixed by plan-year-end date, not filing year. A 2024 plan year ending in June uses the Oct 2023 – Sep 2024 rate ($3.22 from Notice 2023-70), not the rate for the year of filing.

3. **Filing on wrong quarter form**: PCORI is always on Q2 form (July 31). Filing on Q1, Q3, Q4 is wrong even though the filer is reporting an annual fee.

4. **Forgetting to file**: small employers with self-insured plans (HRAs especially) frequently miss the PCORI obligation. The §6651 late-filing penalty is 5% of unpaid tax per month (max 25%), so a $300 fee can become $375.

5. **Confusing PCORI with the ACA "Health Insurance Provider Fee"**: the latter (§9010) was repealed effective 2021. Don't conflate.

6. **Switching counting methods mid-year**: pick Actual / Snapshot / Form 5500 and stick with it for the plan year.

7. **Not filing in the year a plan terminates**: even a plan that ends mid-year owes PCORI on the partial year's covered lives. The agent should not assume "no plan = no fee" — the partial plan year is still subject.

---

## Quick decision tree

```
Q: Does the user sponsor a self-insured health plan, HRA, or applicable FSA?
   No → no PCORI fee, skip
   Yes → continue

Q: What is the plan-year-end date?
   Use this to determine the applicable rate (look up in the table above).

Q: Have they chosen a covered-lives counting method?
   No → ASK; recommend Snapshot for small employers
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
