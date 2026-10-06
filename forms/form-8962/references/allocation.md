# Shared-Policy Allocation (Form 8962 Part IV)

When a single marketplace policy covers people in two different tax families, Form 8962 Part IV allocates premiums, SLCSP, and APTC between the families. Each family files its own Form 8962 with its share of the policy amounts.

## When allocation applies

- **Divorced or separated parents share a policy** for joint children
- **Adult child** on parents' marketplace policy who files an independent return
- **Married couple filing separately** — generally not eligible for PTC except in domestic abuse / spousal abandonment cases under Pub 974
- **Other split-household scenarios** where Form 1095-A lists covered individuals across multiple tax families

If allocation applies for any month, the filer's Form 8962 Line 9 = "Yes", Part IV is completed before Line 10, and Line 10 = "No".

## Allocation rules

Per Treas. Reg. §1.36B-4 and the 2025 Form 8962 instructions (Table 3 and Part IV, Allocation Situations 1–4):

- **Situation 1 — divorced or legally separated during the year** (Reg. §1.36B-4(b)(3)): for the months married, filers may agree on any percentage (0%–100%), but must use the **same percentage for premiums, SLCSP, and APTC**. If they do not agree, **50%** each.
- **Situation 2 — married at year end, filing separately**: certain policy amounts are allocated 50% to each spouse (Reg. §1.36B-4(b)(4)); a spouse who is not an applicable taxpayer enters "0.50" in column (g) only.
- **Situation 3 — no APTC paid**: enrollment premiums are allocated in proportion to the SLCSP premium that applies to each taxpayer's coverage family; complete only column (e).
- **Situation 4 — any other shared policy** (e.g., adult child, ex-spouses divorced in an earlier year) (Reg. §1.36B-4(a)(1)(ii)(B)): filers may agree on any percentage and may use different percentages for different months, but must use the **same percentage for all three amounts in a month**. If they do not agree, the percentage equals the number of individuals enrolled by one taxpayer who are in the other taxpayer's tax family, divided by the total number of individuals enrolled in the policy.
- Percentages are entered as decimals (e.g., "0.33") and must sum to 100% across the tax families on the policy.

## Common scenarios

### Scenario 1: Divorced parents, child on policy

- Parent A and Parent B divorced before the year
- Their child is on Parent A's marketplace policy
- Parent B is the custodial parent and claims the child as a dependent
- Parent A is the policyholder

Both parents must file Form 8962 (Parent A because they're the policyholder; Parent B because they claim the dependent who is on the policy).

**Allocation negotiation** (Allocation Situation 4, because they divorced before the year):
- If Parent A and Parent B agree on a 50/50 split: each enters 0.50 for premiums, SLCSP, APTC
- If they cannot agree: the percentage allocated to Parent B = number of individuals Parent A enrolled who are in Parent B's tax family ÷ total individuals enrolled in the policy

The two Forms 8962 (one per parent) must show consistent allocation percentages. Mismatched allocations can lead to IRS correspondence.

### Scenario 2: Adult child on parents' policy

- Parents have marketplace coverage for themselves and their 24-year-old child
- The child works, files an independent return (not claimed as parents' dependent)
- The child is on the parents' policy

The parents claim PTC for their share (themselves + the dependents they claim, not the independent child). The child files Form 8962 with their share.

**Allocation negotiation** (Allocation Situation 4): any agreed percentage; absent agreement, by enrolled individuals. If parents are 2 of 3 covered, parents allocate 2/3 of premiums/SLCSP/APTC; child allocates 1/3.

### Scenario 3: Married couple filing separately (MFS)

Generally, MFS filers are not eligible for PTC (IRC §36B(c)(1)(C)). Exception 2 in the Form 8962 instructions: domestic abuse or spousal abandonment victims may file MFS and claim PTC by checking the box on line A. A non-qualifying MFS filer enters "0.50" in column (g) only and leaves (e) and (f) blank (Allocation Situation 2). Engage with caution; this requires careful reading of the instructions and Pub 974.

## Filling Part IV

For each shared policy (lines 30, 31, 32, 33), enter:

| Field | What goes here |
|-------|----------------|
| (a) Policy number | Form 1095-A line 2 (the marketplace policy number; last 15 characters if longer) |
| (b) SSN of other taxpayer | The other tax family's primary filer SSN |
| (c) Allocation start month | First month the allocation applies ("01"–"12") |
| (d) Allocation stop month | Last month the allocation applies ("01"–"12") |
| (e) Premium percentage | This filer's share as a decimal (e.g., "0.50") |
| (f) SLCSP percentage | This filer's share as a decimal |
| (g) APTC percentage | This filer's share as a decimal |

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
4. **Default rule misapplied**. Absent agreement, the default is 50/50 for a divorce during the year (Situation 1) and the enrolled-individuals ratio for other shared policies (Situation 4), never who paid the premium.
5. **Forgetting that Part IV is monthly-method-only**. Allocation forces monthly method; Line 10 = No.

## Pointer

For complex shared-policy scenarios (including three or more tax families on one policy), Pub 974 has worked examples. Always cross-check the allocation percentages between filers before final submission.
