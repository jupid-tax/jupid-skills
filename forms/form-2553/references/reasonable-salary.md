# Reasonable Salary for S-Corp Shareholder-Employees

After the S-corp election, the single biggest ongoing compliance question is: how much salary must the shareholder-employee pay themselves?

The IRS requires that S-corp shareholders who perform services for the corporation pay themselves a **reasonable salary** subject to FICA tax (Social Security + Medicare) before taking distributions. Underpaying salary to dodge FICA is the single most common S-corp audit trigger.

This file gives the agent the framework to advise on reasonable salary — but the final number is a judgment call that depends on industry, geography, role, and hours. **The skill must NOT pick a default salary for the user.** Ask, don't guess.

---

## The legal basis

### Statutory hook

There is no Internal Revenue Code section that says "S-corp shareholders must pay themselves a reasonable salary." The requirement is constructed from:

- **IRC §3121(a)** — "wages" for FICA purposes include all remuneration for services performed by an employee
- **IRC §1366(e)** — the IRS may reallocate income between an S-corp and a related shareholder if necessary to reflect the value of services performed
- **IRS Fact Sheet FS-2008-25** — explicitly states that S-corp shareholder-employees must take "reasonable compensation" for services

### Case law

The cornerstone case is **Watson v. Commissioner, 668 F.3d 1008 (8th Cir. 2012)**:

- David Watson, CPA, owned 100% of an S-corp accounting firm
- He paid himself $24,000 salary and took $203,651 in distributions
- The IRS reclassified $67,044 of distributions as wages, owed FICA on it
- The Tax Court and 8th Circuit upheld the reclassification
- The court applied a **multi-factor reasonableness test** — not a fixed percentage

The Watson decision is the most-cited S-corp reasonable-salary case. It establishes that the IRS will look at *what an arm's-length employer would pay an arm's-length employee for the same services*.

### Revenue rulings

- **Rev. Rul. 74-44 (1974)** — early authority that distributions from a closely-held corporation can be recharacterized as wages when the corporation distributes to a shareholder-employee in lieu of paying salary. This is the foundational ruling.
- **Rev. Rul. 73-361** — supports the reasonableness analysis for closely-held corporations generally.

---

## The IRS multi-factor test

There is **no fixed dollar amount or percentage** the IRS will accept. Reasonableness is fact-and-circumstances based, looking at all of these:

### Watson factors (as applied by the 8th Circuit)

1. **Training and experience** of the shareholder-employee
2. **Duties and responsibilities**
3. **Time and effort devoted to the business**
4. **Dividend history** (distributions in prior years)
5. **Payments to non-shareholder employees** for similar services
6. **Timing and manner of paying bonuses** to key people
7. **What comparable businesses pay for similar services**
8. **Compensation agreements** (formal contracts, board minutes)
9. **Use of formula** to determine compensation

### Practical approach

The agent's framework for advising:

```
Reasonable salary ≈ what the entity would have to pay an unrelated third party
                    to perform the same services that the shareholder-employee performs
```

Concretely:

1. **Identify the shareholder-employee's actual role** — CEO, software developer, hairstylist, real estate agent, etc.
2. **Look up market wages for that role** in the entity's geographic area using **BLS OES (Occupational Employment and Wage Statistics)**: https://www.bls.gov/oes/
3. **Adjust for hours worked** — if the shareholder works 30 hrs/week, scale BLS full-time data by 0.75
4. **Adjust for experience and duties** — early-career vs. senior, individual contributor vs. managing the whole company
5. **Compare to similar S-corps** — sites like RCReports, Glassdoor, salary.com provide comp data
6. **Document the analysis** — keep a written reasonable-comp memo for the user's records

### BLS OES — how to use it

BLS publishes wage data by **6-digit SOC (Standard Occupational Classification) code**, by **state**, and by **metropolitan area**. The 50th percentile (median) is typically the starting point for reasonable comp analysis; the agent can adjust up or down based on the multi-factor test.

Example flow:
- User: "I'm a freelance software developer"
- BLS SOC: 15-1252 Software Developers
- Geographic area: pick the user's state or metro
- Pull median wage from https://www.bls.gov/oes/current/oes_nat.htm
- 2024 median for Software Developers (national): $130,160
- If user works 40 hrs/wk, $130,160 is a reasonable starting point
- If user works 20 hrs/wk on the S-corp (and has another job for the other 20), reduce to ~$65,000

---

## The risks of underpayment

### IRS reclassification

If the IRS audits and finds the salary is too low, it will:

1. **Reclassify distributions as wages** for the under-paid amount
2. Assess **back FICA** (15.3% combined) on the reclassified amount
3. Assess **failure-to-deposit penalties** (per IRC §6656, up to 15% of the unpaid amount)
4. Assess **failure-to-file penalties** for the unfiled Form 941s
5. Assess **interest** from the original due date

For a $50,000 reclassification, this typically results in $7,500-$10,000 of tax + penalties + interest. Multi-year reclassifications compound.

### The $0 salary trap

The most aggressive (and dangerous) S-corp strategy is paying $0 salary and taking 100% as distribution. This is **almost certain to be reclassified** if audited:

- Watson factors yield > $0 if the shareholder performed any services
- The IRS specifically targets $0-salary returns for audit
- Defending $0 salary requires proving the shareholder performed *no services* — virtually impossible for a working owner

The agent should never advise $0 salary for a working shareholder. Even a passive investor-shareholder who genuinely performs no services should pay something nominal if they're at all involved in operations.

### Common safe(r) ranges

The traditional rule of thumb — though **not** an IRS-sanctioned safe harbor — is roughly:

```
Reasonable salary ≈ 30% to 60% of net profit, depending on industry and hours
```

Service businesses (consulting, law, accounting, design) tend to land at the higher end (50-60%) because the value is mostly the owner's labor.

Capital-intensive businesses (e-commerce inventory, real estate, machinery rental) tend to land lower (30-40%) because some of the profit is return on capital, not labor.

This is not a defense against audit by itself, but it's a reasonable starting frame. The Watson-factors analysis is what actually defends the number.

---

## Documentation the agent should produce or recommend

For the user's records (and for any future audit defense):

1. **Reasonable-comp memo**:
   - Description of shareholder's role and duties
   - Hours per week
   - Experience and qualifications
   - BLS data citation (URL, date pulled, percentile)
   - Adjustments made (and why)
   - Final salary figure
   - Date prepared and signed by shareholder
2. **Board / member resolution** (for corp / LLC respectively) approving the salary
3. **Annual review** — re-do the analysis each year as profits and hours change
4. **Payroll records** — W-2 forms, Form 941 quarterly returns, federal/state UI returns
5. **Distribution log** — separate ledger of distributions, dated, with shareholder approval

Tools like **RCReports** automate steps 1-4 and produce a defensible report — useful for users with complex situations.

---

## Worked example (from the Jupid blog)

```
Marcus, IT consultant, single-member LLC, S-corp elected for 2026
Net profit projection: $150,000

Reasonable-salary analysis:
  Role: Senior software/IT consultant
  BLS SOC: 15-1299 (Computer Occupations, All Other) — 2024 national median $103,030
  Adjustment: Marcus is senior (15+ years), works 50 hr/wk → +20% = ~$124,000
  Geographic: Marcus is in mid-cost metro → no adjustment
  Final reasonable salary: $80,000 (conservative; below BLS median due to documented
    factors: 60% of time is operations/sales not coding, mid-tier client base)

  Salary:        $80,000  → FICA 15.3% = $12,240
  Distribution:  $70,000  → FICA $0
  Net SE-equivalent tax: $12,240

Compare to sole-prop on $150,000:
  SE base: $150,000 × 0.9235 = $138,525
  SE tax: $138,525 × 15.3% (capped at SS base for SS portion) = $21,194

Annual savings: $21,194 − $12,240 = $8,954

Compliance overhead:
  - Payroll software: $600
  - State UI tax: $400
  - Bookkeeping increment: $1,200
  - Form 1120-S preparation: $1,500
  Total overhead: ~$3,700

Net benefit: $8,954 − $3,700 = ~$5,250/year
```

The $80K salary in this example is **defensible** because:
- BLS-anchored to a specific SOC
- Adjusted with documented reasoning
- Documented in writing before the year started
- Below BLS median (conservative)

If Marcus had taken $30K salary on $150K profit, the $50K differential would be at high reclassification risk.

---

## Cross-references

- Form mechanics: [`line-by-line.md`](./line-by-line.md)
- Eligibility (must be a working shareholder for this to matter): [`eligibility.md`](./eligibility.md)
- Common mistakes (under-salary): [`common-mistakes.md`](./common-mistakes.md)
- Authorities:
  - *Watson v. Commissioner*, 668 F.3d 1008 (8th Cir. 2012)
  - *Rev. Rul. 74-44*
  - IRS Fact Sheet FS-2008-25
  - IRC §3121, §1366(e)
  - BLS OES https://www.bls.gov/oes/
