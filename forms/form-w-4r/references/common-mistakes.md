# Common Form W-4R mistakes — and how to avoid them

Form W-4R has only a few fields, but recipients still make consequential mistakes. The penalties for under-withholding (§6654 estimated-tax penalty) or for missing the §72(t) early-withdrawal tax (separate from W-4R) can add up quickly.

This reference covers the top mistakes recipients make, the symptoms, and the fixes.

---

## 1. Choosing the wrong form (W-4R vs. W-4P)

**The mistake**: Recipient files W-4R when the distribution is actually periodic (recurring monthly/quarterly/annual payments scheduled for more than one year). Or files W-4P when the distribution is a one-time lump sum.

**Why it happens**: The forms were redesigned in 2022 (effective 2023) to split the formerly combined Form W-4P into two: W-4P (periodic) and W-4R (nonperiodic + ERD). Many recipients still think of "withholding on retirement distributions" as a single concept.

**Symptom**: 
- W-4R filed for periodic payments → payor may apply default 10% (other nonperiodic), but actual payments are periodic and the IRS expects W-4P withholding under bracket-based rules.
- W-4P filed for lump sum → the form's "additional withholding" structure doesn't map cleanly to the payor's nonperiodic distribution.

**Fix**: Identify the right form. If payments are scheduled for more than one year (annuity, monthly pension, 10-year installment), use W-4P. If one-time or unscheduled, use W-4R.

**Prevention**: Before signing, confirm the payment structure with the payor. "Is this a one-time distribution or recurring?" is the key question.

---

## 2. Under-withholding a lump sum and getting hit with §6654 estimated-tax penalty

**The mistake**: Recipient takes a $100,000 IRA lump sum, elects 0% withholding via W-4R, and assumes they'll pay the tax at filing. The IRS imposes a §6654 underpayment penalty because total withholding + estimated tax falls short of the safe harbor.

**Why it happens**: Recipient confuses "I'll pay the tax at filing" with "no penalty." The §6654 safe harbor requires that total tax payments during the year (withholding + estimated taxes) equal at least:

- 90% of the current year's tax liability, OR
- 100% of the prior year's tax (110% if prior-year AGI > $150,000)

If neither safe harbor is met, the §6654 penalty applies on the underpayment, computed at the IRS short-term rate plus 3%.

**Symptom**: Notice from the IRS in spring (after filing) assessing the underpayment penalty. Or, if the recipient self-computes via Form 2210, they discover the penalty.

**Fix**: 
- **For the current year**: Pay an additional Form 1040-ES estimated payment ASAP to cover the shortfall. The earlier in the year the payment is made, the less penalty accrues.
- **For prior years**: The penalty is part of the tax bill. Pay it.

**Prevention**: Before electing 0% withholding on a large distribution, run a back-of-envelope calculation:

- Estimate marginal bracket × distribution amount = additional federal tax
- Compare to current withholding (W-2, prior W-4P, etc.) — is the additional tax already covered?
- If not, either elect a non-zero W-4R rate OR pay quarterly estimates

---

## 3. Not filing W-4R when required (defaults apply)

**The mistake**: Recipient doesn't submit W-4R to the payor for an IRA distribution or 401(k) lump sum. The payor applies the default withholding rate (10% for other nonperiodic, 20% for ERD).

**Why it happens**: Recipient assumes "I don't need to fill anything; the payor will figure it out." Technically true (defaults apply), but the recipient may have wanted a different rate.

**Symptom**: Distribution comes through with default withholding. If the recipient wanted 0% (for a Roth conversion, for example, where they want full conversion amount), they got 10% withheld and lost the benefit.

**Fix**: 
- For the current distribution: probably too late — payor processes the distribution at the default rate, sends out the net, files 1099-R.
- For future distributions: file W-4R BEFORE the next distribution is processed.

**Prevention**: For any large or unusual distribution, file W-4R explicitly. Don't rely on defaults. The form takes 5 minutes; the wrong default can cost thousands.

---

## 4. Choosing wrong form: W-4R vs. W-4P specifically

**The mistake**: A retired federal employee with a monthly pension benefit submits W-4R to their pension administrator (OPM). The form is rejected — pension benefit is periodic, requires W-4P.

**Why it happens**: 2022/2023 redesign created two separate forms. Recipients submit the wrong one.

**Symptom**: Payor rejects the form and applies default withholding from prior election (or, if no prior election, applies single-no-allowances rate per W-4P).

**Fix**: Submit W-4P. For periodic pension benefits, W-4P is the correct form.

**Prevention**: Before submitting any retirement-distribution withholding form, confirm with the payor: "Periodic or nonperiodic?"

---

## 5. Forgetting §72(t) early-withdrawal penalty (separate from W-4R)

**The mistake**: Recipient under 59½ takes a $40,000 IRA distribution, elects 22% withholding via W-4R, and assumes 22% covers everything. At tax time, they owe an additional $4,000 (10% of $40,000) under §72(t) because they're under 59½ and no exception applies.

**Why it happens**: W-4R is a federal income tax withholding form. The §72(t) 10% additional tax is a separate excise tax, paid via Form 5329 with the recipient's annual Form 1040. W-4R does NOT withhold for §72(t).

**Symptom**: Unexpectedly large tax bill at filing, or §6654 underpayment penalty if quarterly estimates weren't made.

**Fix**: 
- For the current year: pay the §72(t) penalty with Form 5329 attached to Form 1040.
- For future early withdrawals: factor §72(t) into the rate decision (effective rate becomes ordinary rate + 10%).

**Prevention**: For under-59½ withdrawals, set the W-4R rate to (marginal bracket + 10%) OR pay quarterly estimates for the §72(t) portion. Or qualify for an exception (hardship, first-home, education, medical, qualified domestic relations order, separation from service after age 55 from employer plan, SEPP, etc.).

---

## 6. Trying to get below 20% on an ERD

**The mistake**: Recipient takes a $50,000 401(k) lump sum after leaving employer. Wants 0% withholding because they intend to roll the full amount to an IRA within 60 days. Submits W-4R with Line 2 = "0".

**Why it happens**: Recipient confuses ERD rules (20% mandatory) with other nonperiodic rules (0–100%).

**Symptom**: Payor applies 20% by force of §3405(c) regardless of W-4R. Recipient receives $40,000 net. The $10,000 withholding is gone — the recipient must "make whole" the full $50,000 within 60 days using non-IRA cash to complete the rollover, or only $40,000 is rolled and the $10,000 withheld is taxable distribution.

**Fix**: 
- Better path: do a **direct trustee-to-trustee rollover** instead of indirect rollover. Direct rollover bypasses the 20% withholding entirely (Form 1099-R Code G, $0 withholding).
- If indirect rollover already happened: contribute the $10,000 from non-IRA cash within 60 days to make the rollover whole. The withheld $10,000 is recovered when filing Form 1040 (it becomes federal tax payment / refund).

**Prevention**: Before taking an ERD, confirm with the payor whether you want direct or indirect rollover. Direct is almost always better when the goal is to move funds between retirement accounts.

---

## 7. Mismatched name/SSN/address

**The mistake**: Recipient's W-4R has a different name, SSN, or address than the payor's records. The payor rejects the form.

**Why it happens**: Recipient moved, married/divorced (name change), or made a typo on the SSN.

**Symptom**: Payor's distribution-processing team flags the form. Distribution is delayed.

**Fix**: 
- Update the payor's records first (via the payor's address change form, name change form, etc.)
- Then resubmit W-4R with the matching information

**Prevention**: Pull the most recent statement from the payor and copy the name/SSN/address verbatim onto W-4R.

---

## 8. Submitting W-4R to the IRS instead of the payor

**The mistake**: Recipient mails W-4R to the IRS along with their tax return.

**Why it happens**: Recipient confuses W-4R with other tax forms that get filed with IRS.

**Symptom**: IRS receives a stray form with no return; either ignores or returns to recipient. The payor never receives the form. Default withholding applies to the distribution.

**Fix**: Resubmit W-4R to the payor (IRA custodian, plan administrator, employer).

**Prevention**: W-4R is **delivered to the payor**, not filed with the IRS. The form's instructions clearly state this. Read them.

---

## 9. Not signing or not dating the form

**The mistake**: Recipient fills the form but forgets to sign or date it.

**Why it happens**: Speed; e-signature confusion; fillable PDF without signature field activated.

**Symptom**: Payor returns the form for completion. Distribution is delayed.

**Fix**: Sign and date, resubmit.

**Prevention**: Before submitting, verify all fields including signature and date are completed.

---

## 10. Using last year's revision

**The mistake**: Recipient pulls W-4R from an old saved file and submits to payor. The payor accepts but the form revision is outdated.

**Why it happens**: IRS occasionally revises W-4R (rates, instructions). Recipient uses cached version.

**Symptom**: Usually the payor doesn't reject (the form layout has been stable since 2023), but for tax-year-specific items (e.g., updated bracket information in the marginal-rate table on the form's reverse), the recipient may use stale information for rate selection.

**Fix**: Re-pull the current version from https://www.irs.gov/pub/irs-pdf/fw4r.pdf and re-submit.

**Prevention**: Always pull from the IRS site in the year of the distribution. The URL is stable; the PDF revision date in the lower-right of page 1 indicates the current revision.

---

## 11. Conflating Roth conversion withholding with regular distribution

**The mistake**: Recipient is doing a Roth conversion (Traditional IRA → Roth IRA) and elects 22% withholding via W-4R, thinking the 22% will satisfy the tax on the conversion.

**Why it happens**: Recipient understands the conversion is taxable and wants to "pay the tax."

**Symptom**: The 22% withheld from the Traditional IRA reduces the converted amount in the Roth. Worse, if recipient is under 59½, the 22% withheld is itself a taxable distribution (and subject to §72(t) 10% penalty).

**Fix**: 
- For future conversions: 0% withholding via W-4R; pay the conversion tax with Form 1040-ES from non-IRA cash. This keeps the full conversion amount in the Roth.
- For the current incorrect conversion: depending on timing, may be able to recharacterize (but recharacterization of conversions was eliminated by TCJA effective 2018; verify current law).

**Prevention**: For Roth conversions, default rule: W-4R = 0%, pay quarterly estimates from non-IRA cash. Keep the full converted amount in the Roth.

---

## Summary checklist

Before signing W-4R:

- [ ] Right form (W-4R, not W-4P or W-4)
- [ ] Distribution classification confirmed (ERD vs. other nonperiodic)
- [ ] Rate within allowed range (≥ 20% for ERD; 0–100% for other)
- [ ] Recipient under 59½? Factor §72(t) 10% penalty (paid separately on Form 5329)
- [ ] Other income / withholding considered for §6654 safe harbor
- [ ] Name / SSN / address match payor records
- [ ] Form delivered to payor (NOT to IRS)
- [ ] Signed and dated
- [ ] Current year's IRS revision used
- [ ] State withholding handled separately
- [ ] Roth conversion → typically 0% withholding (don't deplete Roth balance)
