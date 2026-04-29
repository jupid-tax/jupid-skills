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

You MUST reduce the loss by reimbursement, even if not yet received, **as long as the recovery is reasonably foreseeable**. Pub 547 makes this explicit.

If the recovery is uncertain or disputed, the loss is generally not deductible until the year it's resolved. Tell the user this — they may need to wait a year before claiming.

### Three reimbursement scenarios

| Scenario | Treatment | Year of deduction |
|----------|-----------|-------------------|
| Settled and paid in full or part | Subtract amount on Line 3 / Line 21 | Year of loss (or year of disaster-year election) |
| Settled and denied | No reduction | Year of loss |
| Pending; reasonable estimate possible | Subtract estimate; if final amount differs, file amended return | Year of loss |
| Pending; no reasonable estimate | Defer the entire loss until resolved | Year of resolution |
| User did not file a claim though insured | Loss is REDUCED by what insurance WOULD have covered | Year of loss |

The last row catches a common trap: if the user had homeowners insurance and chose not to file (e.g., to avoid a premium increase), the IRS treats the claim as available but unused and reduces the deduction by the amount insurance would have paid (Pub 547, "Failure to file a claim").

### Late-arriving recoveries

If the user deducts the loss in year 1, then receives an unexpected larger reimbursement in year 2:
- The excess reimbursement is **income** in year 2 to the extent it exceeded the deducted loss (tax-benefit rule)
- Report on Schedule 1 Line 8z "Other income" (verify line number against current Schedule 1)
- Do NOT amend year 1 — the original deduction was correct based on facts known then

If the user deducts the loss in year 1, then receives LESS reimbursement than expected in year 2:
- File an amended return for year 1 (Form 1040-X) to claim the additional loss
- Statute of limitations: generally 3 years from the original return due date

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

1. The user must **elect** §1033 treatment by reporting the gain and the election on the year-of-conversion return (or an amended return within the replacement period).
2. The election is made by attaching a statement to the return:
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
| General casualty/theft (most cases) | 2 years from end of first tax year with realized gain |
| Federally declared disaster — principal residence | 4 years (with extensions for severely damaged areas) |
| Condemnation of real property used in trade/business or for investment | 3 years |
| Federally declared disaster — business property generally | 4 years (in some cases) |

Verify the exact period against Pub 547 and §1033(g) for the user's situation. The IRS sometimes extends the period for specific disasters via Notice / Rev. Proc.

### Qualifying replacement property

The replacement property must be **similar or related in service or use** to the converted property:

- Personal residence destroyed by hurricane → replacement = another personal residence (broader test for principal residence under §1033(h))
- Rental building destroyed by fire → replacement = another rental building (any class of investment real estate)
- Business equipment destroyed → replacement = similar business equipment

The IRS has more lenient rules for federally declared disasters and for principal residences (see §1033(h) — special rule for principal residence and contents in declared disasters).

### Mechanics of the deferred gain

If §1033 elected and replacement property acquired:
- The gain is NOT recognized in the year of conversion
- Basis of replacement property = cost of replacement − deferred gain
- When the replacement is later sold, the deferred gain is recognized

If the replacement period expires without acquiring qualifying property:
- The user must amend the year-of-conversion return to recognize the gain

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
| Claiming loss when insurance claim is pending and recovery likely | Pub 547 requires deferral until resolved | Wait until resolution year |
| Claiming loss when user chose not to file insurance claim | Pub 547 reduces by amount insurance would have covered | Compute "phantom" reimbursement and subtract |
| Treating reimbursement > basis as a loss of zero instead of a gain | Mathematically wrong | Report gain on Line 4 / 22; consider §1033 |
| Using replacement cost instead of basis | Basis is cost-not-replacement | Use cost + improvements − prior depreciation |
| Missing late-arriving reimbursement (year 2+) | Tax-benefit rule requires income recognition | Report on Schedule 1 in year of receipt |
| Filing §1033 election informally without statement | IRS may deny the deferral | Attach the formal election statement to the return |

---

## What the agent should NOT do

- Prepare the §1033 election statement and basis tracking unilaterally — too easy to get wrong; refer to a CPA
- Guess at "reasonable expected reimbursement" when the user doesn't know — ASK
- Tell the user to skip the insurance claim to maximize the deduction — this is wrong (the loss is reduced by the unfiled-claim amount)
- File without a clear status on the insurance claim
