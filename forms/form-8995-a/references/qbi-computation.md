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
```

All three reductions per Treas. Reg. §1.199A-3(b)(1)(vi). The IRS confirmed in FAQ 33 (Apr 2019) that these adjustments are required.

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

If the user enters $100,000 as QBI, they overstate by $31,865 → tentative 20% deduction overstated by ~$6,373 → IRS notice within ~12 months.

---

## Source 2: S-Corporation K-1

### Formula

```
QBI = K-1 Box 1 ordinary business income
    − reasonable compensation paid to owner-shareholder (the owner's W-2 from the S-corp)
```

Per Treas. Reg. §1.199A-3(b)(2)(ii)(H), reasonable compensation paid by an S-corp to a shareholder is NOT QBI. It IS W-2 wages of the corp (counts toward Part II Line 4).

If the K-1 already excludes reasonable comp from box 1 (the S-corp computed and reported QBI separately in K-1 box 17 code V), use that figure directly. Recent K-1s often pre-compute this — check.

### Example

K-1 box 1 ordinary business income: $300,000
Owner's W-2 from S-corp: $100,000

QBI = $300,000 − $0 = $300,000  (NOT $300,000 − $100,000 — box 1 already excludes the W-2; the corp deducted the wages already)

Wait. Box 1 ordinary business income is AFTER the corp's W-2 wage expense (the owner's $100,000 W-2 was an expense to the corp that reduced its ordinary income). So box 1 already nets out the $100,000.

The QBI = $300,000 box 1 figure as-is. The owner enters the $100,000 W-2 separately on Form 1040 Line 1a (it's also on the W-2 the owner received from the S-corp).

**Common confusion**: if K-1 box 17 code V says "Section 199A QBI: $295,000" but box 1 says $300,000 — use the $295,000 from box 17 code V. The corp may have made adjustments (e.g., for nondeductible expenses, depreciation differences) to compute QBI separately.

---

## Source 3: Partnership K-1

### Formula

```
QBI = K-1 Box 1 ordinary business income (or box 17/20 code with QBI label, if separately computed)
```

For partnerships, there's no "reasonable compensation" concept; partners receive guaranteed payments (K-1 box 4) for services, and these are NOT included in box 1 ordinary income. So no further reduction from box 1 is needed.

Guaranteed payments to a partner are NOT QBI per Treas. Reg. §1.199A-3(b)(2)(ii)(I). They appear on the partner's Form 1040 as ordinary income but don't count toward QBI.

### Example

K-1 box 1 ordinary income: $150,000
K-1 box 4a guaranteed payments for services: $80,000

QBI = $150,000 (box 4a is NOT QBI; the partnership already deducted it before computing box 1)

---

## Source 4: Schedule E Rental Real Estate

Rental real estate qualifies for QBI ONLY if either:

1. **§162 trade or business**: The rental rises to the level of a trade or business (significant active management, multiple properties, regular activity). This is a facts-and-circumstances test with no bright-line rule.

2. **§1.199A-1(b)(14) safe harbor (Rev. Proc. 2019-38)**: Meets ALL of the following:
   - Separate books and records for each rental real estate enterprise
   - 250+ hours of rental services per year (the taxpayer, employees, contractors, agents combined)
   - Contemporaneous records (logs of hours, services, dates, who performed)
   - Statement attached to the return under penalty of perjury

Rental real estate that doesn't satisfy either test is NOT QBI. The Schedule E income is reported but doesn't appear on Form 8995-A.

### Triple-net leases (NNN)

Triple-net leases (where the tenant pays property taxes, insurance, and maintenance) typically do NOT qualify even if the safe harbor 250-hour test is met, because the landlord is doing very little. Practitioners increasingly conclude NNN leases are not QBI without strong contrary evidence.

### Self-rental rules

A property rented from the owner to a related operating business may qualify for QBI under the self-rental rule (Treas. Reg. §1.199A-1(b)(14)) automatically, without the safe harbor — common for medical practices that own their building.

---

## Special Cases

### Trader vs. Investor

A "trader in securities" who has elected mark-to-market under §475(f) is engaged in a trade or business → income IS QBI (subject to SSTB rules — trading is SSTB).

A passive "investor" (holds securities for capital gains, dividends, interest) is NOT engaged in a trade or business → no QBI; capital gains and dividends are excluded anyway.

### State Taxes on Income

State and local income taxes paid by the business are NOT QBI adjustments. They're deducted by the business as an expense (already in Schedule C / K-1) or not deductible at all (state income tax of the owner). No further QBI adjustment needed.

### Foreign Income

Income that is "effectively connected with a US trade or business" (ECI) qualifies for QBI. Pure foreign-source income does not.

### REIT Dividends and PTP Income

These flow to Form 8995-A Part IV Line 28 directly, NOT to Part II. They're not subject to the W-2/UBIA limit (a structural advantage). REIT dividends are reported in 1099-DIV Box 5; qualified PTP income from K-1.

---

## QBI flowchart

```
What's the income source?
├── Schedule C → net profit − ½ SE tax − SE HI − SE retirement = QBI
├── S-corp K-1 → use box 17 code V if provided; else box 1 (already excludes owner's W-2)
├── Partnership K-1 → box 1 ordinary income (excludes guaranteed payments)
├── Schedule E rental → only if §162 trade or business OR safe harbor met
├── REIT dividend → Part IV Line 28, not Part II
├── PTP income → Part IV Line 28, not Part II
├── Capital gains, ordinary dividends, interest → NOT QBI
└── Foreign-source income → only ECI counts
```

---

## Validation

Before submitting QBI to the form:

- [ ] Have you reduced Schedule C net profit by ½ SE tax + SE HI + SE retirement?
- [ ] For S-corp owners: did you confirm reasonable comp is in W-2 wages, NOT in QBI?
- [ ] For partnerships: did you confirm guaranteed payments are NOT in QBI?
- [ ] For rentals: did you confirm §162 trade or business OR §1.199A safe harbor?
- [ ] Did you exclude all capital gains, ordinary dividends, interest from QBI?
