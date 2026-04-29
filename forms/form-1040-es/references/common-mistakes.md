# Common Form 1040-ES Mistakes That Trigger §6654 Penalties

Even taxpayers who "pay quarterly estimates" routinely get hit with underpayment penalties. The mistakes below cover ~90% of avoidable §6654 assessments.

Each mistake includes: how to spot it, the citation, and how the agent prevents it.

---

## Mistake 1 — Missing the Q1 deadline because "I don't owe much in Q1"

**Symptom**: Filer skips the April 15 voucher because their Schedule C income hasn't really kicked in by Q1, then catches up Q2–Q4.

**Why it's wrong**: §6654 requires 25% of the annual safe-harbor amount paid by April 15. Even if Q1 income is low, the prior-year safe harbor still requires 25% of `prior_tax × 1.10` (or 1.00) by April 15. Skipping Q1 → penalty for the Q1 underpayment, even if Q2-Q4 are fully paid.

**Citation**: IRC §6654(b)(2), §6654(d)(1)(A).

**Agent prevention**: the SKILL.md output template shows all four installments with their due dates. The agent flags "Q1 installment is required even if income is low" in the output.

---

## Mistake 2 — Treating prior-year safe harbor as 100% when AGI > $150K

**Symptom**: High-AGI filer pays exactly `prior_tax × 1.00` in equal quarterly installments, then gets penalty.

**Why it's wrong**: per IRC §6654(d)(1)(C), if prior-year AGI exceeds $150,000 (or $75,000 MFS), the safe harbor is **110%** of prior-year tax, not 100%.

**Citation**: IRC §6654(d)(1)(C).

**Agent prevention**: the SKILL.md workflow Step 2 explicitly checks prior-year AGI against $150K (or $75K MFS). The agent asks for prior-year AGI in Prerequisites. The output shows whether 110% applies.

---

## Mistake 3 — Forgetting SE tax in projected total tax

**Symptom**: Schedule C filer projects income tax based on brackets but forgets the 15.3% SE tax. Pays estimates 30% short.

**Why it's wrong**: §6654 looks at **total tax** (Form 1040 Line 24), which includes SE tax. SE tax is often the largest chunk of tax for solo Schedule C filers.

**Citation**: IRC §6654(b)(2) (refers to "tax" which is defined in the regulations to include SE tax).

**Agent prevention**: SKILL.md worksheet Line 9 computes SE tax. The agent runs the full algorithm and never skips Line 9.

---

## Mistake 4 — Forgetting NIIT on a year with significant capital gain

**Symptom**: Filer realizes a large capital gain, pays estimated tax on the gain at the LTCG rate, but forgets the additional 3.8% NIIT.

**Why it's wrong**: NIIT applies on top of regular income tax / capital gains tax for filers above the MAGI threshold ($200K single / $250K MFJ).

**Citation**: IRC §1411.

**Agent prevention**: SKILL.md worksheet Line 10 includes NIIT. The agent computes NIIT for any filer with investment income whose AGI is near or above threshold.

---

## Mistake 5 — Forgetting Additional Medicare Tax 0.9% when both spouses earn near $200K

**Symptom**: MFJ couple, each spouse earns $180K W-2 wages. Each employer withholds the regular 6.2% + 1.45% Medicare on full wages. Neither employer triggers the Additional 0.9% withholding (since each individual is under $200K). At filing, couple owes Additional Medicare on the joint excess over $250K.

**Why it's wrong**: employers withhold based on individual wages, not joint income. Joint MAGI threshold is $250K. The shortfall must be covered by estimated tax or W-4 additional withholding.

**Citation**: IRC §3101(b)(2); IRS Pub. 505.

**Agent prevention**: when both spouses have W-2 income summing above the MFJ threshold, the SKILL.md agent surfaces the Additional Medicare gap.

---

## Mistake 6 — Roth conversion with no estimated tax bump

**Symptom**: Retiree converts $100K traditional IRA to Roth in March. Pays no extra estimated tax. Files in April of next year owing $25K, gets §6654 penalty.

**Why it's wrong**: Roth conversion amount is fully ordinary income in the year converted. Tax is owed by Q1 (or annualized over Q1, Q2, Q3, Q4 if using Schedule AI).

**Citation**: IRC §408A(d)(3) (Roth conversion as taxable event); §6654.

**Agent prevention**: SKILL.md prerequisites #5 explicitly asks about Roth conversions. The agent computes the conversion's tax impact and adds it to Line 1 / Line 4 of the worksheet.

---

## Mistake 7 — Capital gain in Q3 with equal-installment plan and no annualization

**Symptom**: Investor sells a rental property in August for a $200K gain. Uses equal-installment plan based on prior-year safe harbor. The Q1, Q2 installments are based on prior-year income; the Q3 sale produces a current-year tax spike not reflected in installments.

**Why it's wrong**: the plan technically satisfies Safe Harbor B (prior-year × 1.10) and avoids §6654 penalty. **Not actually a mistake** — but filers sometimes panic and overpay Q3 estimates trying to "match" the gain.

**Agent guidance**: if the user is on prior-year safe harbor, the gain doesn't change the per-quarter installment. The full balance due on the gain is settled at filing. Don't over-pay quarterly.

The mistake to actually avoid: switching to 90%-current-year safe harbor mid-year, which **requires** the full current-year (gain-inclusive) tax projection. If switching, the user must pay 25% of `0.9 × current_tax` per quarter — which means catching up retroactively for Q1, Q2.

**Citation**: IRC §6654(d)(1)(B).

---

## Mistake 8 — State estimated tax confused with federal

**Symptom**: Filer pays $5,000 to "the IRS" via Direct Pay for a state estimated tax obligation, or pays the state and forgets the federal.

**Why it's wrong**: state estimated tax is a separate channel (state DOR, varies by state). Federal Form 1040-ES does not satisfy state. State forms (e.g., CA Form 540-ES, NY Form IT-2105) have different schedules and rules.

**Citation**: state-specific.

**Agent prevention**: SKILL.md Step 9 reminds the user about state. The agent asks for the user's state in Prerequisites.

---

## Mistake 9 — Year-end W-2 withholding bump but no acknowledgment in plan

**Symptom**: Filer realizes in November they're under-paid. Asks employer to withhold an extra $5,000 from December paychecks via Form W-4 Line 4(c). Then ALSO pays $5,000 via the Q4 1040-ES voucher. Now over-paid and has cash tied up until refund.

**Why it's wrong**: per §6654(g), W-2 withholding is treated as paid evenly across the year. Once the December bump is in place, no additional Q4 voucher is needed.

**Citation**: IRC §6654(g).

**Agent prevention**: SKILL.md `references/uneven-income.md` documents this. The agent asks about year-end withholding bumps and adjusts the Q4 voucher.

---

## Mistake 10 — Wrong "Reason for Payment" on Direct Pay

**Symptom**: User selects "Tax Return" or "Balance Due" instead of "Estimated Tax" on Direct Pay. Money goes to the wrong tax bucket. IRS doesn't credit the estimated tax account; user gets a §6654 penalty notice; refund of misallocated payment takes 3–6 weeks.

**Why it's wrong**: Direct Pay's "Reason for Payment" determines which IRS module receives the funds. Wrong reason = wrong account.

**Citation**: operational, not statutory.

**Agent prevention**: `filing.md` Section 1 Step 3 specifies "Estimated Tax" → "1040ES (for 1040, 1040A, 1040EZ)". The agent verifies before submitting.

---

## Mistake 11 — Single-payment "I'll just pay everything at year-end"

**Symptom**: Filer makes one large $30K payment in December, expecting to satisfy the whole year. §6654 still assesses penalty for Q1, Q2, Q3 underpayment.

**Why it's wrong**: §6654 assesses penalty per-quarter. A single Q4 payment covers Q4 but NOT prior quarters. The penalty for Q1, Q2, Q3 is based on the unpaid amount for each quarter × interest from that quarter's due date to the payment date.

**Citation**: IRC §6654(b)(2), §6654(d)(1)(A).

**Agent prevention**: the SKILL.md output template shows four discrete vouchers with four discrete due dates. The agent never recommends a single year-end payment for an estimated-tax-required filer (except for farmers/fishers under §6654(i), which is a separate path).

---

## Mistake 12 — MFJ filer using $150K threshold for 110% rule when filing MFS

**Symptom**: Spouse files MFS and uses $150K threshold for the 110% rule, instead of $75K.

**Why it's wrong**: §6654(d)(1)(C) explicitly halves the threshold for MFS filers. MFS at $80K AGI triggers 110% rule.

**Citation**: IRC §6654(d)(1)(C).

**Agent prevention**: SKILL.md workflow Step 2 explicitly checks MFS status when applying 110% threshold.

---

## What the agent does to avoid these

The SKILL.md workflow forces:

1. **Asking** for prior-year AGI (catches mistake 2, 12)
2. **Asking** for filing status with MFS treated separately (catches mistake 12)
3. **Computing** SE tax, Add'l Medicare, NIIT explicitly (catches mistakes 3, 4, 5)
4. **Asking** about Roth conversions and capital gain events (catches mistake 6, 7)
5. **Producing** all four vouchers with explicit due dates (catches mistakes 1, 11)
6. **Flagging** withholding-as-paid-evenly rule for Q4 catch-up (catches mistake 9)
7. **Verifying** "Reason for Payment" in `filing.md` (catches mistake 10)
8. **Reminding** about state estimated tax (catches mistake 8)

If any of these checks fail, the agent surfaces the issue rather than producing a clean-looking but wrong plan.
