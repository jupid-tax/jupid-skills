# Line 1 — State Tax Refund Taxability

A prior-year state or local income tax refund (Form 1099-G Box 2) is **only sometimes** taxable on Line 1. The rule is the **tax benefit rule**: the refund is taxable only to the extent it gave the user a tax benefit when deducted in the prior year.

This file walks through the test the agent must run before putting any amount on Line 1. On the 2025 return (filed in 2026), the refund being tested is usually a refund of 2024 state income tax, so the prior-year return is the 2024 Form 1040 and Schedule A. Verified 2026-10-06 against the State and Local Income Tax Refund Worksheet in the 2025 Instructions for Form 1040 (Schedule 1, line 1).

---

## The 60-second decision tree

```
Is the refund an income tax refund for 2024, and none of the Pub 525 exceptions applies?
├── NO → use Itemized Deduction Recoveries in Pub 525 instead (see list below)
└── YES → continue
        │
        Did the user take the standard deduction last year?
        ├── YES → Line 1 is $0. Stop. The refund is not taxable.
        └── NO (itemized, used Schedule A) → continue
                │
                Did the user deduct state and local income tax on Schedule A?
                ├── NO (deducted general sales tax instead) → Line 1 is $0. Stop.
                └── YES → run the IRS worksheet below. Two limits apply:
                      (1) SALT cap: 2024 Schedule A line 5d minus line 5e ($10,000 cap for 2024)
                      (2) itemized deductions minus the standard deduction you could have taken
```

---

## Why the rule exists

If the user deducted $5,000 of state income tax on Schedule A in year 1 and got a $400 refund in year 2, they effectively deducted $400 they didn't pay. The IRS recovers that with Line 1 in year 2.

But if the user deducted $5,000 and got a $400 refund — but the SALT cap ($10,000 for 2018–2024) was already maxed out by their property tax, then the state income tax deduction added zero benefit. The refund is non-taxable. The same logic applies when total itemized deductions beat the standard deduction by less than the refund.

For refunds of 2025 tax (reported on the 2026 return), the 2025 cap is $40,000 ($20,000 MFS), reduced by 30% of MAGI over $500,000 ($250,000 MFS) but not below $10,000 ($5,000 MFS) (IRC §164(b)(7); 2025 Schedule A line 5e).

**Source**: IRC §111 (recovery of tax benefit items); 2025 Form 1040 instructions (Schedule 1, line 1); IRS Publication 525 (Recoveries chapter).

---

## When the refund is fully taxable

All of the following:
- Prior year: filer itemized (Schedule A)
- Prior year: SALT deduction included state/local income tax (not sales tax)
- Prior year: Schedule A line 5d was not more than line 5e (no taxes lost to the cap)
- Prior year: total itemized deductions (line 17) exceeded the standard deduction the filer could have taken by at least the refund
- Refund amount ≤ the state income tax actually deducted

→ Report the full refund amount on Line 1.

---

## When the refund is fully non-taxable

ANY of the following:
- Prior year: standard deduction
- Prior year: itemized but elected sales tax (not income tax) on Schedule A Line 5a
- Prior year: SALT cap fully maxed by other taxes, so line 5d − line 5e ≥ the refund (state income tax was deducted but produced zero marginal benefit)
- Prior year: itemized deductions did not exceed the standard deduction (rare, since the filer chose to itemize)

→ Line 1 = $0. Don't enter anything. Keep the 1099-G Box 2 in records to substantiate.

---

## When the refund is partially taxable (the worksheet case)

Scenario: prior-year SALT deduction included state income tax and either the cap kicked in or itemized deductions only slightly beat the standard deduction. Compute the benefit.

**State and Local Income Tax Refund Worksheet — Schedule 1, Line 1 (2025 Form 1040 instructions)**:

```
1. Income tax refund from Form(s) 1099-G, but not more than the state and
   local income taxes shown on 2024 Schedule A, line 5d:             $______
2. If 2024 Schedule A line 5d > line 5e: line 5d − line 5e; else enter
   line 1 on line 3 and go to line 4:                                  $______
3. Line 1 − line 2 (if line 1 is not more than line 2, STOP: none
   of the refund is taxable):                                          $______
4. Total itemized deductions, 2024 Schedule A line 17:                 $______
5. 2024 standard deduction for the 2024 filing status: $14,600 single
   or MFS, $29,200 MFJ or QSS, $21,900 HOH (MFS whose spouse itemized:
   skip 5–7, enter line 4 on line 8):                                  $______
6. Boxes checked (born before Jan 2, 1960; blind; same for spouse)
   × $1,550 ($1,950 if 2024 status was single or HOH):                 $______
7. Line 5 + line 6:                                                    $______
8. If line 7 < line 4: line 4 − line 7 (else STOP: none taxable):      $______
9. Taxable part of refund = smaller of line 3 or line 8 → Schedule 1, line 1
```

**Example** (single, under 65, 2025 return):
- 2024: filer itemized; $7,000 state income tax + $5,000 property tax = $12,000 on line 5d; line 5e capped at $10,000; total itemized deductions (line 17) $18,000
- 2025: filer receives an $800 state refund

```
1. Refund:                                    $800
2. 5d − 5e = $12,000 − $10,000:               $2,000
3. Line 1 is not more than line 2 → STOP

Line 1 = $0
```

The cap soaked up the marginal state income tax deduction; the refund produced no benefit, so it's not taxable.

**Counter-example** (single, under 65):
- 2024: $4,000 state income tax + $3,000 property tax = $7,000 (5d = 5e, under the cap); total itemized deductions (line 17) $16,000 with mortgage interest
- 2025: filer receives a $300 refund

```
1. $300
2. 5d not more than 5e → line 3 = $300
4. $16,000
5. $14,600
6. $0
7. $14,600
8. $16,000 − $14,600 = $1,400
9. Smaller of $300 or $1,400 = $300

Line 1 = $300
```

Full refund taxable: no taxes were lost to the cap and itemizing beat the standard deduction by more than the refund.

**Use Pub 525 instead of this worksheet** if any of these applies (2025 instructions, Line 1 Exception): the refund is for a year other than 2024; it is not an income tax refund (e.g., sales or property tax); 2024 taxable income was fully taxed at 0% on capital gains; the refund exceeds the income tax deduction minus the sales tax the filer could have deducted; the last 2024 estimated state payment was made in 2025; the filer owed AMT in 2024; 2024 credits exceeded tax; the filer could be claimed as a dependent in 2024; or the refund is from a joint state return but the 2025 federal return is not joint with the same person.

---

## The AMT wrinkle

If the user paid AMT in the prior year, the state income tax deduction may have been disallowed for AMT purposes — which means it produced no AMT benefit even if it produced a regular-tax benefit.

When the prior-year tax was driven by AMT, the recoverable amount under the tax benefit rule may be reduced. This is rare for solo filers since TCJA shrank AMT's scope, but it can apply to high earners with deferred-comp items.

If the user had AMT in the prior year, surface the issue and flag for professional review.

---

## What the agent must ask the user

Before entering any amount on Line 1:

1. **Did you receive a Form 1099-G Box 2** (state/local income tax refund)? Which tax year is it for?
2. **Did you itemize last year** (Schedule A)?
3. If yes: **did you deduct state income tax or general sales tax** on Schedule A line 5a (the line 5a box is checked only when sales tax was elected)?
4. **Prior-year Schedule A lines 5d, 5e, and 17**, and the prior-year filing status and age/blind boxes.
5. Any Pub 525 exception facts (AMT last year, dependent status, joint state return, last estimated payment timing).

Without these, the agent cannot compute Line 1. Stop and ask for the prior-year return (or an IRS transcript); do not default to $0 or to the full refund.

---

## Common mistakes

### Mistake: assuming any 1099-G Box 2 amount is taxable

Most filers take the standard deduction. For them, Line 1 is always $0.

### Mistake: ignoring the SALT cap

A high-property-tax state filer who itemized often had the full state income tax deduction wasted by the cap. Line 1 is $0 even though they got a refund.

### Mistake: confusing 1099-G Box 1 with Box 2

Box 1 is unemployment compensation → **Line 7**, always taxable.
Box 2 is state/local refund → **Line 1**, often $0.

### Mistake: reporting a federal tax refund

Federal tax refunds are NEVER taxable. They don't appear anywhere on the return.

### Mistake: reporting a property tax refund

Property tax refunds (rare — some states refund excess property tax) follow the same tax benefit rule, but they are not Line 1 items. Figure any taxable recovery with Itemized Deduction Recoveries in Pub 525 and report it on Line 8z (2025 instructions, Line 1 Exception item 2 and the Line 8z list).

---

## Sources

- IRC §111 (recovery of tax benefit items)
- IRC §164(b)(5) (election to deduct state sales tax in lieu of state income tax)
- IRC §164(b)(6)–(7) (SALT cap: $10,000 for 2018–2024; $40,000 for 2025 and $40,400 for 2026 with the MAGI phasedown, as amended by P.L. 119-21)
- 2025 Instructions for Form 1040, Schedule 1 line 1 and its State and Local Income Tax Refund Worksheet
- IRS Publication 525 (Recoveries chapter — Itemized Deduction Recoveries)
- IRS Publication 17 (Federal Income Tax for Individuals)
