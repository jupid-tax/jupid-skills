# Line 1 — State Tax Refund Taxability

A prior-year state or local income tax refund (Form 1099-G Box 2) is **only sometimes** taxable on Line 1. The rule is the **tax benefit rule**: the refund is taxable only to the extent it gave the user a tax benefit when deducted in the prior year.

This file walks through the test the agent must run before putting any amount on Line 1.

---

## The 60-second decision tree

```
Did the user take the standard deduction last year?
├── YES → Line 1 is $0. Stop. The refund is not taxable.
└── NO (itemized, used Schedule A) → continue
        │
        Did the user deduct state and local income tax (SALT) on Schedule A?
        ├── NO (deducted state sales tax instead) → Line 1 is $0. Stop.
        └── YES → continue
                │
                Was the SALT deduction (state income tax + property tax) ≥ $10,000 cap?
                ├── NO (under cap, full benefit) → refund is fully taxable up to amount deducted
                └── YES → run the worksheet — refund may be partially or fully NOT taxable
```

---

## Why the rule exists

If the user deducted $5,000 of state income tax on Schedule A in year 1 and got a $400 refund in year 2, they effectively deducted $400 they didn't pay. The IRS recovers that with Line 1 in year 2.

But if the user deducted $5,000 and got a $400 refund — but the SALT cap ($10,000 since TCJA) was already maxed out by their property tax, then the state income tax deduction added zero benefit. The refund is non-taxable.

**Source**: IRC §111 (recovery of tax benefit items); IRS Publication 525 (Recoveries chapter).

---

## When the refund is fully taxable

All of the following:
- Prior year: filer itemized (Schedule A)
- Prior year: SALT deduction included state/local income tax (not sales tax)
- Prior year: SALT total deducted < $10,000 cap (full benefit)
- Refund amount ≤ the state income tax actually deducted

→ Report the full refund amount on Line 1.

---

## When the refund is fully non-taxable

ANY of the following:
- Prior year: standard deduction
- Prior year: itemized but elected sales tax (not income tax) on Schedule A Line 5a
- Prior year: SALT cap fully maxed by property tax alone (state income tax was deducted but produced zero marginal benefit)

→ Line 1 = $0. Don't enter anything. Keep the 1099-G Box 2 in records to substantiate.

---

## When the refund is partially taxable (the worksheet case)

Scenario: prior-year SALT deduction included some state income tax but the cap kicked in. Compute the marginal benefit.

**Worksheet (from IRS Pub 525)**:

```
A. State refund received in current year:                      $______
B. State income tax actually deducted on prior-year Sch A 5a:  $______
C. Smaller of A or B:                                          $______
D. Total SALT deducted on prior-year Sch A Line 5e (capped):   $______
E. Sum of state income tax + property tax + state sales tax    $______
   actually paid in prior year (uncapped):
F. Excess over cap (E − D, but not less than zero):           $______
G. Recoverable benefit = C − F (but not less than zero):       $______

Enter G on Schedule 1 Line 1.
```

**Example**:
- 2025: filer itemized; deducted $7,000 state income tax + $5,000 property tax (uncapped paid: $12,000); SALT capped at $10,000 → deducted $10,000
- 2026: filer receives $800 state refund

```
A. State refund:                              $800
B. State income tax deducted:                 $7,000
C. Smaller of A or B:                         $800
D. SALT deducted (capped):                    $10,000
E. SALT actually paid:                        $12,000
F. Excess over cap (E − D):                   $2,000
G. Recoverable benefit (C − F):               $0   (because $800 − $2,000 < 0)

Line 1 = $0
```

The cap soaked up the marginal state income tax deduction; the refund produced no benefit, so it's not taxable.

**Counter-example**:
- 2025: filer deducted $4,000 state income tax + $3,000 property tax (uncapped: $7,000); under cap → deducted full $7,000
- 2026: filer receives $300 refund

```
A. $300
B. $4,000
C. $300
D. $7,000
E. $7,000
F. $0
G. $300

Line 1 = $300
```

Full refund taxable because under the cap.

---

## The AMT wrinkle

If the user paid AMT in the prior year, the state income tax deduction may have been disallowed for AMT purposes — which means it produced no AMT benefit even if it produced a regular-tax benefit.

When the prior-year tax was driven by AMT, the recoverable amount under the tax benefit rule may be reduced. This is rare for solo filers since TCJA shrank AMT's scope, but it can apply to high earners with deferred-comp items.

If the user had AMT in the prior year, surface the issue and flag for professional review.

---

## What the agent must ask the user

Before entering any amount on Line 1:

1. **Did you receive a Form 1099-G Box 2** (state/local income tax refund)?
2. **Did you itemize last year** (Schedule A)?
3. If yes: **did you deduct state income tax** (Schedule A Line 5a, "income tax box checked") or sales tax (general sales tax box checked)?
4. If state income tax was deducted: **what was your total SALT deducted on Line 5e** (post-cap amount)?
5. **What was your total state income tax + property tax + sales tax actually paid** (pre-cap)?

Without these, the agent cannot compute Line 1 and should default to $0 with a note that the user should verify with prior year's Schedule A.

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

Property tax refunds (rare — some states refund excess property tax) follow the same tax benefit rule but typically would not have been deducted as income tax — only as property tax on Schedule A Line 5b. The same SALT-cap analysis applies.

---

## Sources

- IRC §111 (recovery of tax benefit items)
- IRC §164(b)(5) (election to deduct state sales tax in lieu of state income tax)
- TCJA / IRC §164(b)(6) ($10,000 SALT cap)
- IRS Publication 525 (Recoveries chapter — full worksheet)
- IRS Publication 17 (Federal Income Tax for Individuals)
