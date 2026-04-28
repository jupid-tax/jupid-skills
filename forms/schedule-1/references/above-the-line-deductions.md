# Schedule 1 Part II — Above-the-Line Deductions (Eligibility Tests)

Each Part II line has its own eligibility test, dollar cap, and supporting form. This file is the agent's deep reference for **whether** an adjustment can be claimed and **how much**.

Above-the-line deductions are valuable because they reduce AGI directly — improving eligibility for credits and reducing phaseouts. They are available whether the user takes the standard deduction or itemizes.

The agent's job for each Part II line: confirm eligibility (don't assume), apply the cap, attach the right form. When in doubt, ask the user — never invent a number.

---

## Line 11 — Educator expenses

**Cap**: $300 (2025 figure, Rev. Proc. 2024-40; 2026 announced October 2025 — verify).

**Eligibility test** (all must be true):
- Filer is a teacher, instructor, counselor, principal, or aide
- For kindergarten through grade 12
- Worked at least **900 hours** at an elementary or secondary school during the school year (state law definitions apply)

**Qualifying expenses**:
- Books, supplies, computer equipment (including software/services), other equipment used in the classroom
- Supplementary materials used in the classroom
- Professional development courses related to the curriculum or to the students taught
- COVID-19 protective items (per Notice 2021-15, if still applicable)

Expenses must be unreimbursed.

**Spouses**: each spouse who separately qualifies can claim up to $300 → up to $600 combined on a MFJ return.

**Source**: IRC §62(a)(2)(D).

---

## Line 12 — Reservists, performing artists, fee-basis officials (Form 2106)

Three narrow groups; most filers leave this blank.

**12a — Armed Forces reservists**: travel more than 100 miles from home for reserve duty. Form 2106 captures qualifying travel expenses.

**12b — Qualifying performing artists**: ALL must be true:
- 2 or more employers in the field, **earning $200+ from each**
- Performing-arts business expenses > **10% of gross income from the activity**
- AGI **before this deduction ≤ $16,000** (statutory; not inflation-adjusted)

**12c — Fee-basis state or local government officials**: paid in whole or part on a fee basis (rare; most government officials are paid on salary).

Form 2106 is required.

---

## Line 13 — HSA deduction (Form 8889)

**Eligibility test** (all must be true):
- Covered by a qualifying High-Deductible Health Plan (HDHP) for the month(s) of contribution
- Not enrolled in Medicare
- Not a dependent on another taxpayer's return
- Not covered by other non-HDHP health insurance (some exceptions for specific limited coverage)

**HDHP definition (2025)**:
- Minimum deductible: $1,650 (self) / $3,300 (family)
- Maximum out-of-pocket: $8,300 (self) / $16,600 (family)

**2025 contribution caps** (Rev. Proc. 2024-25):
- Self-only HDHP: $4,300
- Family HDHP: $8,550
- Catch-up (55+): additional $1,000

**2026** announced May 2025 — verify before filing.

**Critical**: only contributions made **outside payroll** go on Line 13. Cafeteria-plan payroll contributions are already excluded from Box 1 W-2 wages — claiming them again on Line 13 is double-dipping.

Form 8889 must be attached.

**Source**: IRC §223; IRS Publication 969.

---

## Line 14 — Moving expenses for Armed Forces (Form 3903)

**Eligibility**: Active-duty service member moving on Permanent Change of Station (PCS) orders. Civilians cannot deduct moving expenses (TCJA 2018 suspension; verify 2026 status).

**Qualifying expenses**:
- Cost of moving household goods and personal effects
- Storage in transit (up to 30 consecutive days)
- Travel (lodging, but not meals) for the move

Form 3903 captures the calculation.

**Source**: IRC §217(g); IRS Publication 521.

---

## Line 15 — Half of self-employment tax

**Eligibility**: Filer paid SE tax (Schedule SE Line 12 > 0).

**Amount**: Schedule SE Line 13 (computed as half of SE tax under IRC §164(f)).

**Math example**:
```
Schedule C net profit  = $80,000
Net SE earnings        = $80,000 × 0.9235 = $73,880
SE tax (Sch SE Line 12)= $73,880 × 0.153  = $11,304
Half of SE tax (L15)   = $11,304 / 2      = $5,652  →  Schedule 1 Line 15
```

If filer has Schedule C profit > $400 but Line 15 is blank → Schedule SE was missed.

**Source**: IRC §164(f).

---

## Line 16 — Self-employed retirement plans (SEP / SIMPLE / qualified)

Owner's contribution to retirement plans for themselves. **Employee** contributions go on Schedule C Line 19 — never Line 16.

### SEP-IRA

**Eligibility**:
- Filer has self-employment earnings (Schedule C profit > 0 after §164(f) deduction)
- Plan is established by the **return due date including extensions**

**Cap (2025)**:
- 25% of net SE earnings (after §164(f) — this creates a circular calc resolved to ~20% of pre-§164(f) SE earnings via the worksheet in Pub 560)
- Absolute max: **$70,000** (2025; Notice 2024-80)

### SIMPLE IRA

**Eligibility**: plan must have been established **by Oct 1 of the prior year** (or first year of business). Cannot stack with a SEP for the same year.

**Cap (2025)**:
- $16,500 employee deferral
- Catch-up at 50+: additional $3,500 (and "super catch-up" 60-63 of $5,250 per SECURE 2.0)

### Solo 401(k)

**Eligibility**: filer is sole proprietor with no common-law employees (spouse OK as co-participant). Plan must be established by year-end (Dec 31 of the tax year); deferrals usually need to be elected during the year too (with limited employer-only contributions allowed by tax filing deadline).

**Caps (2025)**:
- Employee deferral: $23,500
- Catch-up at 50+: $7,500 (super catch-up 60-63: $11,250)
- Employer profit-share: 25% of compensation
- Combined (employee + employer): $70,000 (or $77,500 with catch-up; $81,250 with super catch-up)

### Common contribution worksheet (SEP-IRA simplified)

```
Step 1: Net SE earnings = Schedule C profit − Schedule 1 Line 15 (half SE tax)
Step 2: Deduction rate = 0.25 / (1 + 0.25) = 0.20 (effective 20% of step 1)
Step 3: Deduction = Step 1 × 0.20, capped at $70,000 (2025)
```

**2026 figures** announced fall 2025 — verify.

**Source**: IRC §§408(k), 408(p), 401(k); IRS Publication 560; Notice 2024-80.

---

## Line 17 — Self-employed health insurance deduction

**Eligibility test** (all must be true):
- Filer has net SE earnings (Schedule C, partnership K-1 with SE earnings, or S-corp 2% shareholder W-2)
- Filer was **NOT eligible** to participate in an employer-subsidized health plan during the month(s) for which premiums are claimed — including via spouse's employer

**Coverage scope**:
- Filer
- Filer's spouse
- Filer's dependents
- Filer's children under age 27 at year end (even if not a dependent)

**Premium types**:
- Health insurance (medical)
- Dental
- Vision
- Qualified long-term care insurance (capped per age band — IRC §213(d)(10))

**Cap**: limited to **net earned income from the business** for which the plan was established (after §164(f) and Line 16 deductions). Excess is not deductible above the line; could potentially be itemized on Schedule A subject to AGI floor.

**ACA Premium Tax Credit interaction**: if user received marketplace coverage with an advance Premium Tax Credit, the calculation is circular (the deduction reduces AGI, which changes the PTC, which changes the deductible premium). IRS-approved tax software handles this; manual calc requires the iterative method in IRS Rev. Proc. 2014-41.

**Common errors**:
- Claiming for a month the spouse had employer plan eligibility (even if the user didn't enroll)
- Claiming on Schedule C Line 14 (that's for **employee** benefits) instead of here
- Claiming more than net Schedule C profit

**Source**: IRC §162(l); IRS Publication 535; Rev. Proc. 2014-41.

---

## Line 18 — Penalty on early withdrawal of savings

**Eligibility**: filer paid an early-withdrawal penalty on a CD, savings bond, or other time deposit before maturity. Bank reports on Form 1099-INT Box 2 or 1099-OID Box 3.

**Amount**: the penalty itself (Box 2/3 amount), separate from any interest income reported on Form 1040 Line 2b.

No cap. Form 1099-INT/1099-OID is sufficient documentation.

---

## Line 19a — Alimony paid

**Eligibility**: payment must be alimony under a **pre-2019 divorce or separation agreement**. Post-2018: no deduction.

**Definition of alimony** (pre-TCJA, IRC §71):
- Cash or check (not property)
- Required by the decree
- Spouses live apart
- No obligation to make payment after recipient dies
- Payment is not designated as something other than alimony
- Payment is not child support

**19b**: recipient SSN — required.
**19c**: original decree date — required.

Without a valid 19b SSN, the IRS rejects the deduction.

---

## Line 20 — Traditional IRA deduction

**Eligibility test**:
- Filer (or spouse if MFJ) had **earned income** at least equal to the contribution
- Filer is under age 70½ (no — TCJA repealed the age cap; SECURE Act made it permanent: contributions allowed at any age)
- Contribution made by the **return due date NOT including extensions** (April 15, 2027 for tax year 2026)

**2025 contribution limits**:
- $7,000 (under 50)
- $8,000 (50+)

**2025 deductibility phaseouts** (Rev. Proc. 2024-40):
| Filing status | Active participant in employer plan? | Phaseout (MAGI) |
|--------------|--------------------------------------|------------------|
| Single, HoH | Yes | $77,000 – $87,000 |
| MFJ | Filer is active participant | $123,000 – $143,000 |
| MFJ | Filer NOT active, spouse IS | $230,000 – $240,000 |
| MFJ | Neither is active | No phaseout (full deduction) |
| MFS | Yes | $0 – $10,000 |

**Active participant**: covered by a workplace 401(k), 403(b), 457(b), pension, SEP, SIMPLE, or other employer-sponsored retirement plan during the year. Box 13 of the W-2 ("Retirement plan") is checked.

**MFS lived apart all year**: treated as single for this purpose.

**Roth IRA contributions**: NOT deductible (after-tax). They go nowhere on Schedule 1.

**Source**: IRC §219; IRS Publication 590-A.

---

## Line 21 — Student loan interest deduction

**Cap**: **$2,500** statutory (IRC §221) — does not change with inflation.

**Eligibility test** (all must be true):
- Filer paid interest on a **qualified student loan** during the year
- The loan was for the **filer, spouse, or a dependent** at the time the loan was taken
- Filer is **legally obligated** on the loan
- Filer is **not claimed as a dependent** on someone else's return
- Filing status is **not MFS**
- MAGI is below the phaseout ceiling

**2025 phaseouts** (Rev. Proc. 2024-40):
| Status | Phaseout range (MAGI) |
|--------|----------------------|
| Single, HoH | $80,000 – $95,000 |
| MFJ | $165,000 – $195,000 |
| MFS | Not allowed |

**2026** announced fall 2025 — verify.

**Qualified student loan**: a loan used solely to pay qualified higher education expenses (tuition, fees, room, board, books, supplies) at an eligible institution, for a student enrolled at least half-time in a degree program. The loan must be incurred within a reasonable time before/after the expenses (typically within 90 days).

**Documentation**: Form 1098-E from the lender (Box 1 = interest paid). Lender issues 1098-E only when interest paid ≥ $600 — but the filer can still claim less than $600 if they paid less, as long as they have records.

**Available with standard deduction** — one of the most-missed adjustments.

**Source**: IRC §221; IRS Publication 970 chapter 4.

---

## Line 22 — Reserved for future use

Always blank.

---

## Line 23 — Archer MSA deduction (Form 8853)

Archer MSAs predate HSAs. New entrants are largely closed (must have started before 2008 in most cases, with grandfather rules). Most filers leave Line 23 blank — HSAs (Line 13) replaced this for new contributors.

**Source**: IRC §220.

---

## Line 24 — Other adjustments

For most solo filers, all 24 sub-lines are blank. Notable exceptions:

### 24a — Jury duty pay turned over to employer

If the user's employer continued paying their regular wages during jury service and required turnover of the jury pay, report jury pay on **Line 8h** and offset on **Line 24a**.

### 24c — Olympic/Paralympic medals offset

Offsets Line 8m income if AGI ≤ $1M ($500K MFS). Per IRC §74(d).

### 24h — Attorney fees for unlawful discrimination

Above-the-line deduction for legal fees and court costs in unlawful discrimination cases (Title VII, ADA, ADEA, etc.). Without this provision, the fees would only be itemizable as miscellaneous deductions (suspended by TCJA). IRC §62(a)(20).

### 24i — Attorney fees for IRS whistleblower awards

Above-the-line deduction for legal fees in pursuing an IRS whistleblower award. IRC §62(a)(21).

### 24z — Other adjustments (catchall)

Specific labeled item that doesn't fit any pre-printed sub-line. Always label clearly.

---

## Line 26 — Total adjustments

```
Line 26 = Line 11 + Line 12 + Line 13 + Line 14 + Line 15
        + Line 16 + Line 17 + Line 18 + Line 19a + Line 20
        + Line 21 + Line 23 + Line 25
```

(Line 22 is always blank.)

Flows to **Form 1040 Line 10**.

---

## Eligibility-test cheatsheet

Before claiming any Part II adjustment, the agent must confirm:

| Line | Critical eligibility check |
|------|----------------------------|
| 11 | 900-hour K-12 educator threshold met |
| 13 | Qualifying HDHP for the contribution months; no Medicare; not someone's dependent |
| 15 | Schedule SE Line 13 actually computed |
| 16 | Plan in place by required deadline; contribution within cap |
| 17 | No employer-subsidized plan eligibility (filer or spouse) for the month(s) claimed; capped at SE earnings |
| 19a | Pre-2019 decree; recipient SSN on file |
| 20 | Earned income ≥ contribution; MAGI under phaseout if active participant |
| 21 | $2,500 cap; MAGI under phaseout; not MFS; not someone's dependent |

When any check fails, surface the issue to the user — don't silently zero the line.

---

## Sources

- IRS Schedule 1 (Form 1040), 2025 revision and instructions
- IRC §§62(a)(2)(D), 162(l), 164(f), 217(g), 219, 221, 223, 408(k), 408(p), 401(k)
- IRS Publications 535, 521, 590-A, 560, 969, 970
- Rev. Proc. 2024-25 (HSA limits 2025)
- Rev. Proc. 2024-40 (inflation adjustments 2025)
- Notice 2024-80 (retirement plan limits 2025)
- Rev. Proc. 2014-41 (PTC / SE health insurance circular calc)
