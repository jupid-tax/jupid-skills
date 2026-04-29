# Shared-Policy Allocation (Form 8962 Part IV)

When a single marketplace policy covers people in two different tax families, Form 8962 Part IV allocates premiums, SLCSP, and APTC between the families. Each family files its own Form 8962 with its share of the policy amounts.

## When allocation applies

- **Divorced or separated parents share a policy** for joint children
- **Adult child** on parents' marketplace policy who files an independent return
- **Married couple filing separately** — generally not eligible for PTC except in domestic abuse / spousal abandonment cases under Pub 974
- **Other split-household scenarios** where Form 1095-A lists covered individuals across multiple tax families

If allocation applies for any month, the filer's Form 8962 Line 9 = "Yes" and Part IV is completed before Lines 11–25.

## Allocation rules

Per IRC §36B(c)(2)(C) and Treas. Reg. §1.36B-4(c):

- **Filers may agree** on any percentage allocation (0% – 100%) for premiums, SLCSP, and APTC, provided the percentages sum to 100% across all tax families on the policy
- **Default rule** if filers cannot agree: allocation by tax family size (e.g., parent claims 2/3 if their family is 2 of 3 covered persons)
- **All three percentages** (premiums, SLCSP, APTC) are typically the same, but they can differ if the filers have agreed to a different split
- **Allocation can be different month-to-month** within the same policy

## Common scenarios

### Scenario 1: Divorced parents, child on policy

- Parent A and Parent B divorced before the year
- Their child is on Parent A's marketplace policy
- Parent B is the custodial parent and claims the child as a dependent
- Parent A is the policyholder

Both parents must file Form 8962 (Parent A because they're the policyholder; Parent B because they claim the dependent who is on the policy).

**Allocation negotiation**:
- If Parent A and Parent B agree on a 50/50 split: each enters 0.50 for premiums, SLCSP, APTC
- If they cannot agree: default to allocation by tax family size on the policy

The two Forms 8962 (one per parent) must show consistent allocation percentages. The IRS cross-checks; mismatched allocations trigger CP12 notices.

### Scenario 2: Adult child on parents' policy

- Parents have marketplace coverage for themselves and their 24-year-old child
- The child works, files an independent return (not claimed as parents' dependent)
- The child is on the parents' policy

The parents claim PTC for their share (themselves + the dependents they claim, not the independent child). The child files Form 8962 with their share.

**Allocation negotiation**: typically by tax family size. If parents are 2 of 3 covered, parents allocate 2/3 of premiums/SLCSP/APTC; child allocates 1/3.

### Scenario 3: Married couple filing separately (MFS)

Generally, MFS filers are not eligible for PTC. Exception under Pub 974 Chapter 1: domestic abuse or spousal abandonment victims may file MFS and claim PTC, with allocation rules per the chapter. Engage with caution; this requires careful Pub 974 reading.

## Filling Part IV

For each shared policy (lines 30, 31, 32, 33), enter:

| Field | What goes here |
|-------|----------------|
| (a) Policy number | Form 1095-A Box 2 (the marketplace policy number) |
| (b) SSN of other taxpayer | The other tax family's primary filer SSN |
| (c) Allocation start month | First month the allocation applies (month number 1–12) |
| (d) Allocation stop month | Last month the allocation applies (month number 1–12) |
| (e) Premium percentage | This filer's share, 0 to 100% |
| (f) SLCSP percentage | This filer's share, 0 to 100% |
| (g) APTC percentage | This filer's share, 0 to 100% |

If allocation changes mid-year (e.g., one family drops the policy), use multiple lines (30, 31, 32, 33) — one per period of consistent allocation.

## Effect on Lines 11–25

After Part IV is completed, Lines 12–23 (monthly columns a–f) use the *allocated* amounts:

- Column (a) = 1095-A Column A × this filer's premium percentage
- Column (b) = 1095-A Column B × this filer's SLCSP percentage
- Column (f) = 1095-A Column C × this filer's APTC percentage

The other columns (c, d, e) are derived from these allocated amounts as usual.

## Common mistakes

1. **Allocation not consistent across the two families' Forms 8962**. Parents allocate 70/30 but the other parent allocates 60/40. The IRS will issue notices to both. Coordinate before filing.
2. **Allocating the dependent's coverage to the wrong tax family**. The dependent's coverage allocation belongs to the family that *claims* the dependent on Form 1040, not the family that pays the premium.
3. **Filling Part IV without completing Lines 9 = Yes**. Line 9 must be "Yes" to trigger Part IV processing.
4. **Default rule misapplied**. Default is allocation by tax family size *on the policy*, not by who pays the premium.
5. **Forgetting that Part IV is monthly-method-only**. Allocation forces monthly method; Line 10 = No.

## Pointer

For complex shared-policy scenarios, Pub 974 Chapter 4 has worked examples with multiple allocation strategies. Always cross-check the allocation percentages between filers before final submission.
