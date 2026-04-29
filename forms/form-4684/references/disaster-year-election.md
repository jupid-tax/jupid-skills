# Disaster-Year Election (IRC §165(i))

The §165(i) election lets a taxpayer who suffers a loss in a federally declared disaster claim the deduction in the **year before** the loss. This reference covers when the election is worth making, how to make it, and what statement language is required.

---

## What §165(i) does

By default, a casualty loss is deducted in the year the loss occurred. §165(i) lets the taxpayer elect to treat the loss as if it had occurred in the **immediately preceding** tax year. This is only available for losses in federally declared disaster areas.

Example: Hurricane in October 2025 destroys a home. By default, deduct on the 2025 return (filed April 2026). Under §165(i), elect to deduct on the 2024 return (amend with Form 1040-X).

---

## When the election is worth making

### Reasons to elect (claim in prior year)

1. **Lower prior-year AGI**. The 10% AGI floor (Section A Line 17) reduces the deduction. If prior-year AGI was lower, more of the loss survives the floor.
2. **Higher prior-year tax bracket**. A deduction in a higher bracket saves more tax (e.g., 32% bracket vs. 22% bracket).
3. **Faster refund**. Amended returns process in 8-16 weeks. If the user needs the refund to fund repairs, claiming in the prior year accelerates the cash.
4. **Prior year had a refund vs. balance due in current year**. Refund recovery is faster than reducing a current balance.
5. **NOL planning**. A casualty loss in the prior year may create or enlarge a net operating loss carryback (where applicable).

### Reasons NOT to elect (claim in current year)

1. **Higher current-year tax bracket**. Loss is more valuable in the higher bracket.
2. **Lower current-year AGI**. Less of the loss is consumed by the 10% floor.
3. **Prior year already finalized with refund received and audit risk concerns**. Amending invites another look.
4. **Statute of limitations** for the prior year is closing — the election deadline is constrained.
5. **Prior year used standard deduction and current year will itemize anyway**. The election forces itemization in the prior year, which may not be advantageous.

The agent should compute both scenarios when feasible. Build a small comparison:

```
Scenario A: claim in current year
  AGI:          $X
  10% floor:    $X
  Deductible:   $X
  Marginal rate: X%
  Tax savings:   $X

Scenario B: claim in prior year (amended)
  Prior AGI:    $X
  10% floor:    $X
  Deductible:   $X
  Prior marginal rate: X%
  Tax savings:   $X
```

Recommend whichever produces a larger benefit, and flag refund-timing as a separate factor.

---

## How to make the election

1. **Check the Section D box** on Form 4684 of the prior-year return (or amended return).
2. **Attach a statement** to the return with:
   - Heading: "Election under IRC §165(i) to deduct disaster loss in preceding year"
   - Filer's name, SSN
   - The FEMA disaster declaration number (e.g., "DR-4856-FL")
   - Date of the disaster
   - Address of the property
   - Description of the loss
3. **File** Form 1040-X amending the prior-year return, with Form 4684 attached.
4. **Re-compute prior-year tax** with the loss included.
5. **Submit** within the election deadline.

### Statement template

```
ELECTION UNDER IRC §165(i) TO DEDUCT DISASTER LOSS IN PRECEDING YEAR

Taxpayer: [Filer Name]
SSN: [SSN]
Tax year of election: [Prior Year, e.g., 2024]
Tax year of loss: [Loss Year, e.g., 2025]

The taxpayer hereby elects under IRC §165(i) to deduct the loss
described below in the tax year ending [prior-year end date]
instead of the tax year in which the loss was sustained.

Disaster: [Hurricane Helene / etc.]
FEMA Declaration Number: DR-XXXX-XX
Date of declaration: [date]
Date of loss: [date]
Property address: [address]
Description of property: [home / vehicle / etc.]

The election is made under §165(i) and is irrevocable.

Signed: ______________________
Date:   ______________________
```

The IRS does not provide a fixed-format statement; this template captures all required elements per Reg. §1.165-11. Attach as a PDF (e-file) or printed page (paper).

---

## The election deadline

Per IRC §165(i)(4) and Reg. §1.165-11(g):

> The election must be made by the later of:
> (a) The due date (without extensions) of the return for the loss year, OR
> (b) The due date (with extensions) of the return for the year preceding the loss year.

In practice, for a 2025 disaster:
- Loss-year return (2025) due date without extensions: **April 15, 2026**
- Prior-year return (2024) due date with extensions: **October 15, 2025**

The later of these is April 15, 2026 → election deadline.

For a disaster occurring late in 2025 (October-December), the election window may be tight. Flag this to the user immediately if they bring the question up after April 15.

The IRS sometimes extends the election period via Notice for specific disasters; check IRS.gov disaster relief pages.

---

## Irrevocability

The §165(i) election is **irrevocable** once filed. The user cannot change their mind later. Make sure the user understands:

- Amending the prior year locks in the prior-year treatment
- If the user later finds the current year was the better choice, there is no remedy
- This is why the agent should compute both scenarios before filing

---

## Practical agent guidance

When a user describes a federally declared disaster loss, ask:

> "Do you want me to compute the deduction for both the loss year and the prior year? For federally declared disasters, you can elect to claim the deduction on your prior-year return. Sometimes the prior year produces a bigger refund. The election is irrevocable, so it's worth comparing."

If the user wants to proceed with the prior-year election:

1. Ask for prior-year AGI (the floor calculation)
2. Ask for prior-year filing status (in case it differs)
3. Compute Form 4684 with prior-year AGI on Line 17
4. Compute the resulting Schedule A
5. Compute Form 1040-X
6. Prepare the §165(i) election statement
7. Walk the user through the amended-return submission process (typically paper for older years; e-file 1040-X is supported for recent years — verify IRS scope)

If the user wants to proceed with the loss-year deduction:

1. Compute Form 4684 with current-year AGI on Line 17
2. Continue with the standard workflow

---

## Common §165(i) mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Claiming the loss in BOTH years | Double-deduction | Pick one; the election is one or the other |
| Filing the election after the deadline | IRS will deny | Track deadline carefully; consider extending the prior-year return |
| Using the wrong AGI for the floor | Floor uses the AGI of the year claimed | If electing prior year, use prior-year AGI |
| Missing the FEMA disaster number on the statement | Reg. §1.165-11(c) requires identification | Always include FEMA-DR / EM number |
| Treating the election as revocable | It's irrevocable | Compute both scenarios before electing |
| Forgetting to amend basis on remaining property | Basis adjustments still apply in the year claimed | Track basis correctly in whichever year |

---

## Sources

- IRC §165(i) — election to deduct disaster loss in preceding year
- Reg. §1.165-11 — election mechanics, statement requirements
- IRS Pub 547 — Casualties, Disasters, and Thefts (disaster-year election section)
- IRS disaster relief page — https://www.irs.gov/newsroom/tax-relief-in-disaster-situations
