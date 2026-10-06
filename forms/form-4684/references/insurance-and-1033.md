# Insurance Reimbursements and §1033 Deferred Gains

How to handle the reimbursement column on Form 4684, what to do when a claim is pending, and the basics of §1033 involuntary-conversion deferral when reimbursement exceeds basis.

This reference is loaded when the agent has any of these signals from the user:
- Mentioned filing or having filed an insurance claim
- Reimbursement amount is large relative to basis
- Insurance settled for more than the property cost
- Reimbursement is pending or disputed

---

## The reimbursement entry rule

On Form 4684:
- **Section A Line 3**: insurance / other reimbursement received OR reasonably expected
- **Section B Line 21**: same, for business / income-producing property

You MUST reduce the loss by reimbursement, even if not yet received, **as long as there is a reasonable prospect of recovery**. If you expect to be reimbursed but haven't been paid yet, enter the expected amount (instructions for line 3).

If a claim with a reasonable prospect of recovery is pending, the part of the loss that may be reimbursed is not sustained until it is reasonably certain whether it will be paid, for example by settlement, adjudication, or abandonment of the claim (Reg. §1.165-1(d)(2)(i)). The part not covered by the claim is deductible in the casualty year (Reg. §1.165-1(d)(2)(ii)). Tell the user this — part of the deduction may move to a later year.

### Three reimbursement scenarios

| Scenario | Treatment | Year of deduction |
|----------|-----------|-------------------|
| Settled and paid in full or part | Subtract amount on Line 3 / Line 21 | Year of loss (or year of disaster-year election) |
| Settled and denied | No reduction | Year of loss |
| Pending; reimbursement expected | Subtract the expected amount; if the final amount differs, adjust in the later year (see below), do not amend | Year of loss for the uncovered part |
| Pending; recovery uncertain | The part that may be reimbursed is deducted when it becomes reasonably certain it won't be | Year of resolution for that part |
| User did not file a claim though insured | Loss is REDUCED by what insurance WOULD have covered | Year of loss |

The last row catches a common trap: if the user had homeowners insurance and chose not to file (e.g., to avoid a premium increase), the deduction is reduced by the amount insurance would have paid; only the part not covered by the policy is deductible (IRC §165(h)(4)(E); Pub 547, "Failure to file a claim for reimbursement"; instructions for line 3 example).

### Late-arriving recoveries

If the user deducts the loss in year 1, then receives a larger reimbursement than expected in year 2:
- Include the extra reimbursement in **income** in year 2, but only to the extent the year-1 deduction reduced tax (Reg. §1.165-1(d)(2)(iii); Pub 547, "Actual reimbursement more than expected"; Pub 525, "Recoveries")
- If total reimbursements exceed adjusted basis, there is a gain in year 2: ordinary income up to the deduction that reduced tax, then possibly postponed under §1033 (Pub 547)
- Do NOT amend year 1 — the original deduction was correct based on facts known then

If the user deducts the loss in year 1, then receives LESS reimbursement than expected:
- Deduct the shortfall as a loss in the year it becomes reasonably certain no more will be paid (Pub 547, "Actual reimbursement less than expected"; instructions for line 3)
- Do NOT amend year 1

---

## When reimbursement creates a gain

If insurance / reimbursement **exceeds basis**, the user has a **gain**, not a loss:

```
Reimbursement: $250,000
Basis:         $180,000
Gain:          $70,000
```

This is reported on Form 4684:
- Section A Line 4 (personal-use)
- Section B Line 22 (business / income-producing)

The gain typically flows to **Schedule D** (capital gain) for personal-use property held > 1 year, OR Form 4797 for business property.

But — the user can often **defer** the gain under IRC §1033 (involuntary conversion).

---

## §1033 deferred gain — the basics

IRC §1033 lets the user postpone recognizing a gain from an involuntary conversion (casualty, theft, condemnation) if they reinvest the proceeds in qualifying replacement property.

### Election mechanics

1. The user chooses §1033 postponement on the return for the year the gain is realized, which is the year the insurance or other reimbursement is received (Pub 547, "How To Postpone a Gain").
2. The choice is shown by attaching a statement to that return (Pub 547, "Required statement"):
   - Identify the converted property
   - Date of conversion
   - Amount of reimbursement
   - Cost basis
   - Statement: "Election under IRC §1033 to defer gain"
   - Description of replacement property (or intent if not yet acquired)

### Replacement period

The user has a **replacement period** to acquire qualifying replacement property:

| Conversion type | Replacement period |
|-----------------|---------------------|
| General casualty/theft (most cases) | Begins on the date of the casualty or theft; ends 2 years after the close of the first tax year in which any part of the gain is realized (IRC §1033(a)(2)(B); Pub 547, "Replacement Period") |
| Main home or its contents in a federally declared disaster area | 4 years after the close of the first tax year in which any part of the gain is realized (IRC §1033(h)(1)(B); Pub 547) |
| Condemnation of real property used in trade/business or for investment | 3 years (IRC §1033(g)(4); condemnations only, not casualties; Pub 544) |
| Business or investment property in a federally declared disaster area | Period is not lengthened, but any tangible property held for productive use in a business is treated as similar or related in service or use (IRC §1033(h)(2); instructions, "Gain on Reimbursement") |

The user can ask the IRS for an extension, ideally before the period ends (Pub 547, "Extension"). Verify the exact period against Pub 547 for the user's situation.

### Qualifying replacement property

The replacement property must be **similar or related in service or use** to the converted property:

- Personal residence destroyed by hurricane → replacement = another personal residence (broader test for principal residence under §1033(h))
- Rental building destroyed by fire → replacement = property similar or related in service or use (the broader like-kind test of §1033(g) applies only to condemned real property)
- Business equipment destroyed → replacement = similar business equipment

The IRS has more lenient rules for federally declared disasters and for principal residences (§1033(h)): no gain is recognized on insurance proceeds for unscheduled personal property in the main home, and other proceeds for the home and its contents are treated as one pool that can be reinvested in a replacement home and contents (instructions, "Gains Realized on Homes in Disaster Areas").

### Mechanics of the deferred gain

If §1033 elected and replacement property acquired:
- The gain is NOT recognized in the year of conversion
- Basis of replacement property = cost of replacement − deferred gain
- When the replacement is later sold, the deferred gain is recognized

If the replacement period expires without acquiring qualifying property, or the replacement costs less than the reimbursement:
- The user must amend the return for the year of the gain (Form 1040-X) to report the gain that can't be postponed (Pub 547, "Amended return")

---

## Decision tree — what to tell the user

```
Did reimbursement exceed basis on any property?
├── No → just enter reimbursement on Line 3 / 21; no gain issue
└── Yes → there's a gain
    ├── Is the user planning to rebuild / replace the property?
    │   ├── Yes → recommend §1033 election; flag the replacement period;
    │   │       refer to a CPA for the election statement
    │   └── No → gain is recognized this year on Schedule D / Form 4797
    └── Special: federally declared disaster + principal residence
        └── §1033(h) is more flexible; user may have 4 years to replace
```

The agent should NOT prepare a §1033 election unilaterally — it requires careful tracking of replacement basis and is best handled by a CPA. The skill's job is to flag the opportunity and produce the Form 4684 gain entry correctly.

---

## Common reimbursement mistakes

| Mistake | Why it's wrong | Fix |
|---------|----------------|-----|
| Forgetting to reduce loss by insurance proceeds | IRC §165(a) requires the loss to be net of compensation by insurance | Subtract on Line 3 / 21 |
| Claiming the full loss while a claim with a reasonable prospect of recovery is pending | Reg. §1.165-1(d)(2)(i): that part isn't sustained yet | Subtract the expected amount; deduct any shortfall when it becomes certain |
| Claiming loss when user chose not to file insurance claim | Pub 547 reduces by amount insurance would have covered | Compute "phantom" reimbursement and subtract |
| Treating reimbursement > basis as a loss of zero instead of a gain | Mathematically wrong | Report gain on Line 4 / 22; consider §1033 |
| Using replacement cost instead of basis | Basis is cost-not-replacement | Use cost + improvements − prior depreciation |
| Missing late-arriving reimbursement (year 2+) | Tax-benefit rule requires income recognition | Include in income in the year received, to the extent the earlier deduction reduced tax (Pub 525, "Recoveries") |
| Filing §1033 election informally without statement | IRS may deny the deferral | Attach the formal election statement to the return |

---

## What the agent should NOT do

- Prepare the §1033 election statement and basis tracking unilaterally — too easy to get wrong; refer to a CPA
- Guess at "reasonable expected reimbursement" when the user doesn't know — ASK
- Tell the user to skip the insurance claim to maximize the deduction — this is wrong (the loss is reduced by the unfiled-claim amount)
- File without a clear status on the insurance claim
