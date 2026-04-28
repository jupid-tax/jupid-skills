# Example: Self-Only Young Saver Maxing the Cafeteria Plan

End-to-end Form 8889 for a 28-year-old solo filer maxing self-only HSA contributions through their employer's cafeteria plan. Tax year 2025.

---

## Background

- **Maya**, age 28, single, no dependents
- Software engineer at a startup that offers a self-only HDHP and a Section 125 cafeteria plan
- HDHP is HSA-qualified: $2,500 deductible (above $1,650 minimum), $5,000 OOP max (below $8,300 max)
- Maya elected $4,300 in cafeteria-plan HSA contributions, deducted from her paycheck pre-tax across 2025
- HSA is at HealthEquity (employer's default custodian); Maya self-transferred to Fidelity in October to access better investment options
- Maya paid $850 of qualified medical expenses in 2025: $200 dental cleaning, $150 prescription, $300 LASIK consultation co-pay, $200 in OTC medications
- Maya took $850 in distributions from the HSA during 2025 to reimburse herself for the above
- 22% federal bracket
- Eligible all 12 months (no Medicare, no other coverage, no FSA, not a tax dependent)

---

## Form 8889

### Part I — HSA Contributions

```
Header
  Name: Maya <last name>
  SSN: <Maya's SSN>

Line 1: Coverage on Dec 1: Self-only ✓
Line 2: HSA contributions Maya made (direct):           $0
Line 3: Contribution limit (self-only, 12 months):  $4,300
Line 4: Archer MSA contributions:                       $0
Line 5: Line 3 − Line 4:                            $4,300
Line 6: Line 5:                                     $4,300
Line 7: Catch-up (under 55):                            $0
Line 8: Total limit:                                $4,300
Line 9: Employer contributions (W-2 Box 12 W):      $4,300
Line 10: Qualified HSA funding distribution:            $0
Line 11: Line 9 + Line 10:                          $4,300
Line 12: Line 2 + Line 11 (cap Line 8):             $4,300
Line 13: HSA deduction:                                 $0
            → Schedule 1, Line 13 = $0
```

### Part II — HSA Distributions

```
Line 14a: Total distributions (1099-SA Box 1):      $850
Line 14b: Excess returns + rollovers:                 $0
       Note: Maya's HealthEquity → Fidelity move was
       a trustee-to-trustee transfer, NOT a rollover.
       Trustee-to-trustee transfers are not reported
       on Form 8889 at all.
Line 14c: Line 14a − Line 14b:                      $850
Line 15: Qualified medical expenses:                $850
Line 16: Taxable HSA distributions:                   $0
Line 17a: Exception:                                N/A
Line 17b: 20% additional tax:                         $0
```

### Part III — Failure to Maintain HDHP

Skip — Maya did not use the last-month rule.

### Reasoning

- **Why Line 13 = $0 despite the deduction working**: All of Maya's $4,300 contributions went through the cafeteria plan (Line 9). Her W-2 Box 1 wages already exclude the $4,300 — the deduction is taken at the payroll level, before she ever sees the income on her return. Putting the same $4,300 on Line 2 would be **double-deducting** — the most common Form 8889 mistake.
- **Why she still files Form 8889**: Even though Line 13 = $0, Maya had Line 9 > 0 and Line 14a > 0. Both trigger the filing requirement. Skipping Form 8889 would create a mismatch between her W-2 Box 12 code W income exclusion and her tax return — likely to trigger an IRS notice.
- **Why the trustee-to-trustee transfer is invisible**: Maya moved her HSA from HealthEquity to Fidelity by signing a trustee-to-trustee transfer form. This is **not a rollover** — no 60-day rule, no once-per-12-months limit, not reported on Form 8889 at all. It's just an account transfer. Maya should have a copy of the transfer paperwork in case of audit but doesn't enter anything on the form.
- **Why all $850 is qualified**: Dental cleaning, prescription, LASIK, and OTC medications are all on the Pub 502 qualified list. (Dental under "Dentist"; prescription under "Medicines"; LASIK under "Eye surgery"; OTC under the post-CARES Act expanded list.)
- **Tax effect**: Federal tax savings from cafeteria-plan exclusion = $4,300 × 22% = $946. FICA savings = $4,300 × 7.65% = $329. State savings (varies, ~5%) = $215. **Total ~$1,490 in first-year cash savings.**

---

## What Maya should do differently next year

The agent should flag the following improvements (not strictly required, but worth surfacing):

1. **Keep the cafeteria plan election at the max** — the FICA savings ($329) is unique to cafeteria-plan contributions and unavailable elsewhere.
2. **Pay the $850 of medical from cash next year, not the HSA.** Reimburse herself decades from now using saved receipts. At age 65 and 7% returns, $850 today compounds to ~$32,000 of tax-free withdrawal capacity.
3. **Invest the HSA balance.** Now that she's at Fidelity, she can buy index funds with the full balance (Fidelity has a $0 cash buffer requirement, unlike most custodians). Currently her ~$3,500 net balance after the $850 distribution should be invested in a total-market index fund.
4. **Save every medical receipt.** Even small ones. Each is a future tax-free withdrawal lottery ticket. Scan and store with date, provider, amount.

---

## Sources cited

- IRS Form 8889 (2025 revision)
- IRS Instructions for Form 8889 (2025 revision)
- IRC §223 (HSA limits)
- IRC §125 (cafeteria plans — pre-tax exclusion at payroll)
- IRC §213(d), Pub 502 (qualified medical expenses)
- Rev. Proc. 2024-25 (2025 self-only limit $4,300)
- Notice 2004-50 (trustee-to-trustee transfer treatment, not reportable on 8889)
