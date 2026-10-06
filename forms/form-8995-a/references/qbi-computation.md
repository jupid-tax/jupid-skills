# QBI Computation by Income Type

Form 8995-A Part II Line 2 is QBI. The computation is different for each income type. This reference covers the four main sources.

---

## Source 1: Schedule C (Sole Proprietor / Single-Member LLC)

### Formula

```
QBI = Schedule C Line 31 net profit
    − allocable ½ SE tax
    − allocable SE health insurance deduction
    − allocable SE retirement contributions
    − qualified tips from this business deducted under §224 (2025 and later)
```

The first three reductions per Treas. Reg. §1.199A-3(b)(1)(vi); the 2025 Instructions for Form 8995-A ("Determining your QBI") list them as items attributable to the trade or business. Tips deducted under §224 are not QBI (IRC §199A(c)(4)(D); 2025 i8995-A What's New).

### Allocation when there are multiple Schedule Cs

If the user has multiple Schedule C businesses, allocate each adjustment to the business it relates to:

- **½ SE tax**: from Schedule SE; allocate proportionally to net SE earnings of each Schedule C
- **SE health insurance**: trace to the specific business; if the policy covers the family of the sole proprietor of business A, allocate to business A's QBI (limited to net profit of that business)
- **SE retirement (SEP-IRA, Solo 401(k))**: allocate to the business sponsoring the plan

### Example

Schedule C profit: $100,000
- ½ SE tax allocable: $7,065
- SE health insurance: $4,800
- SEP-IRA contribution: $20,000

QBI = $100,000 − $7,065 − $4,800 − $20,000 = **$68,135**

If the user enters $100,000 as QBI, they overstate by $31,865 → tentative 20% deduction overstated by ~$6,373.

---

## Source 2: S-Corporation K-1

### Formula

```
QBI = QBI on the K-1 box 17 code V statement (Section 199A information)
    − owner-level deductions attributable to the business (e.g., a >2% shareholder's SE health insurance deduction)
```

Per Treas. Reg. §1.199A-3(b)(2)(ii)(H), reasonable compensation received by a shareholder is NOT QBI, and the corporation's deduction for it reduces QBI. Box 1 and the code V QBI are already after that deduction. The wages ARE W-2 wages of the corp (count toward Part II Line 4).

### Example

K-1 box 1 ordinary business income: $300,000
Owner's W-2 from S-corp: $100,000

QBI = $300,000 (NOT $300,000 − $100,000: the corporation deducted the $100,000 of wages before computing box 1). The owner reports the $100,000 W-2 on Form 1040 line 1a.

**Common confusion**: if K-1 box 17 code V says "Section 199A QBI: $295,000" but box 1 says $300,000 — use the $295,000 from box 17 code V. The corp may have made adjustments (e.g., for nondeductible expenses, depreciation differences) to compute QBI separately.

---

## Source 3: Partnership K-1

### Formula

```
QBI = QBI on the K-1 box 20 code Z statement (Section 199A information)
    − partner-level deductions attributable to the business (½ SE tax on partnership SE income, SE health insurance and retirement contributions based on it, unreimbursed partnership expenses)
```

For partnerships, there's no "reasonable compensation" concept; partners receive guaranteed payments (K-1 box 4a/4b), which the partnership deducts before computing box 1.

Guaranteed payments to a partner are NOT QBI per Treas. Reg. §1.199A-3(b)(2)(ii)(I). They appear on the partner's Form 1040 as ordinary income but don't count toward QBI.

### Example

K-1 box 1 ordinary income: $150,000 (code Z statement QBI: $150,000)
K-1 box 4a guaranteed payments for services: $80,000

QBI = $150,000 before partner-level deductions (box 4a is NOT QBI; the partnership already deducted it before computing box 1). If the partner pays SE tax on the $230,000, the ½ SE tax attributable to the $150,000 share also reduces QBI; ask.

---

## Source 4: Schedule E Rental Real Estate

Rental real estate qualifies for QBI ONLY if either:

1. **§162 trade or business**: The rental rises to the level of a trade or business (significant active management, multiple properties, regular activity). This is a facts-and-circumstances test with no bright-line rule.

2. **Rev. Proc. 2019-38 safe harbor**: Meets ALL of the following (Rev. Proc. 2019-38 §3.03):
   - Separate books and records for each rental real estate enterprise
   - 250+ hours of rental services per year (owners, employees, agents, contractors combined); for enterprises in existence at least four years, in any three of the last five years
   - Contemporaneous records (hours, description of services, dates, who performed)
   - Statement attached to a timely filed original return describing the properties, acquisitions and dispositions, with a representation that the requirements are met

Rental real estate that doesn't satisfy either test is NOT QBI. The Schedule E income is reported but doesn't appear on Form 8995-A.

### Triple-net leases (NNN)

Real estate rented under a triple net lease (tenant pays taxes, fees, insurance, and maintenance in addition to rent and utilities) cannot be included in a safe-harbor enterprise (Rev. Proc. 2019-38 §3.05(B)). It is QBI only if the activity is a §162 trade or business on its own facts. Ask; do not assume.

### Self-rental rules

A property rented from the owner to a related operating business may qualify for QBI under the self-rental rule (Treas. Reg. §1.199A-1(b)(14)) automatically, without the safe harbor — common for medical practices that own their building.

---

## Special Cases

### Trader vs. Investor

A "trader in securities" who has elected mark-to-market under §475(f) is engaged in a trade or business → income IS QBI (subject to SSTB rules — trading is SSTB).

A passive "investor" (holds securities for capital gains, dividends, interest) is NOT engaged in a trade or business → no QBI; capital gains and dividends are excluded anyway.

### State Taxes on Income

State and local income taxes are NOT QBI adjustments. Taxes deductible by the business are already in Schedule C / the K-1; the owner's personal state income tax is an itemized deduction (Schedule A, subject to the SALT cap) and is not attributable to the trade or business. No further QBI adjustment needed.

### Foreign Income

Income that is "effectively connected with a US trade or business" (ECI) qualifies for QBI. Pure foreign-source income does not.

### REIT Dividends and PTP Income

These flow to Form 8995-A Part IV Line 28 directly, NOT to Part II. They're not subject to the W-2/UBIA limit (a structural advantage). REIT dividends are reported in 1099-DIV Box 5; qualified PTP income from K-1.

---

## QBI flowchart

```
What's the income source?
├── Schedule C → net profit − ½ SE tax − SE HI − SE retirement = QBI
├── S-corp K-1 → box 17 code V statement QBI (already after owner's wages) − owner-level items
├── Partnership K-1 → box 20 code Z statement QBI (excludes guaranteed payments) − partner-level items
├── Schedule E rental → only if §162 trade or business OR safe harbor met
├── REIT dividend → Part IV Line 28, not Part II
├── PTP income → Part IV Line 28, not Part II
├── Capital gains, ordinary dividends, interest → NOT QBI
└── Foreign-source income → only ECI counts
```

---

## Validation

Before submitting QBI to the form:

- [ ] Have you reduced Schedule C net profit by ½ SE tax + SE HI + SE retirement (+ §224 tips)?
- [ ] For S-corp owners: did you confirm reasonable comp is in W-2 wages, NOT in QBI, and was not subtracted from box 1 a second time?
- [ ] For partnerships: did you confirm guaranteed payments are NOT in QBI?
- [ ] For rentals: did you confirm §162 trade or business OR §1.199A safe harbor?
- [ ] Did you exclude all capital gains, ordinary dividends, interest from QBI?
