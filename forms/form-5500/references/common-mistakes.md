# Common Form 5500 mistakes — and how to avoid them

The Form 5500 series has a high error rate among first-time filers and small-plan sponsors. The DOL and IRS each publish lists of frequent issues; this reference combines those lists with patterns observed across plan administrators, TPAs, and recordkeepers.

---

## 1. Picking the wrong variant

**The mistake**: Filing 5500-EZ when the plan covers a non-owner employee, or filing 5500-SF when the plan holds non-eligible assets (real estate, private LP interests, hedge funds), or filing full 5500 when 5500-SF would have sufficed.

**Why it happens**: The variant selection requires understanding both the participant test and the asset test. Owners assume "small = 5500-SF" without checking the eligible-assets list.

**Symptom**: EFAST2 accepts the filing (it doesn't enforce variant choice from the form data alone), but DOL examination later flags the issue. Or, for 5500-EZ filed when 5500-SF was correct, EFAST2 / IRS may accept and the error surfaces only on audit.

**Fix**: Re-file as the correct variant with "amended" indicator. If the wrong variant resulted in a missed audit (i.e., 5500-SF used instead of full 5500 for 100+), commission the audit retroactively and file the amended 5500 with the audit attached.

**Prevention**: Walk the variant decision tree (`variant-selection.md`) every year. Re-test each year — a plan that was 5500-SF eligible last year may not be this year (e.g., crossed 100 participants, or acquired non-eligible assets).

---

## 2. Missing required schedules

**The mistake**: Filing Form 5500 without Schedule H (large plan financial info), Schedule A (insurance), Schedule C (service provider compensation), or Schedule SB (DB actuarial certification) when required.

**Why it happens**: The schedule requirements are scattered across the instructions, and a plan that was small last year may cross the 100-participant threshold without the administrator realizing additional schedules are now required.

**Symptom**: EFAST2 may list missing schedules as errors in the filing status (some it catches, some it doesn't). DOL correspondence later requests the missing schedule; filings with errors are subject to rejection and penalties.

**Fix**: File an amended 5500 (a complete replacement filing) with the missing schedule. If the missing item is the IQPA report, commission the audit and file the amendment by the response date in the DOL letter.

**Prevention**: Use EFAST2's IFILE built-in schedule logic — IFILE prompts for schedules based on form responses. If using XML upload, double-check the schedule list against the requirements table.

---

## 3. Late filing with no extension

**The mistake**: Missing the 5500 due date (last day of 7th month after plan year end — July 31 for calendar plans) and not filing Form 5558 for an extension by that date.

**Why it happens**: The administrator forgot, the auditor was delayed, the TPA missed the deadline, the sponsor's CFO changed.

**Symptom**: DOL letter or IRS letter assessing penalties. DOL penalty up to $2,739/day per ERISA §502(c)(2) (2025 adjustment, 90 FR 1854; DOL made no 2026 adjustment, 91 FR 31358). IRS penalty $250/day up to $150,000 per IRC §6652(e). For 5500-EZ, IRS penalties only. IRS sends CP403 and CP406 delinquency notices for missing Forms 5500/5500-SF and a CP283 penalty notice for a late 5500-EZ.

**Fix**: 
- For 5500/5500-SF: Use the **DFVC Program** (Delinquent Filer Voluntary Compliance) before DOL issues a Notice of Intent to Assess a Penalty. DFVC penalty: $10/day, capped at $750 per filing and $1,500 per plan for small plans ($750 per plan if the sponsor is a 501(c)(3) organization), and $2,000 per filing and $4,000 per plan for large plans. Payment is online only (https://www.dol.gov/agencies/ebsa/employers-and-advisers/plan-administration-and-compliance/correction-programs/dfvcp).
- For 5500-EZ: Use the IRS late filer penalty relief program (Rev. Proc. 2015-32): $500 per delinquent return, capped at $1,500 per plan, paper filing with Form 14704 and a check. Not available once a CP283 penalty notice has been issued.

Once DOL or IRS has issued correspondence, voluntary-relief programs may not apply — full penalties.

**Prevention**: If the filing may run late, file Form 5558 by July 31 for a calendar plan year. Since January 1, 2025 it can be filed through EFAST2 or on paper (Form 5558, Rev. January 2025); approval of a timely, complete form is automatic and extends the due date to October 15.

---

## 4. Plan number inconsistency

**The mistake**: Changing the plan number from year to year, or starting a new plan with a previously used plan number.

**Why it happens**: Sponsor changes recordkeeper, TPA, or in-house administrator. New person assigns a "fresh" plan number not knowing the historical number must continue.

**Symptom**: EFAST2 / DOL records show what looks like two separate plans. DOL correspondence asking about the discontinued plan or the "new" plan's history.

**Fix**: File an amended return with the correct plan number. Provide a written explanation of the renumbering history. Coordinate with DOL via EBSA to merge records if needed.

**Prevention**: Treat the plan number like the plan's social security number. Document it in plan records, on the plan document, on every filing, on TPA hand-off documents. Plan numbers 001–099 for pension; 501–599 for welfare. Once assigned, they don't change.

---

## 5. Beginning-of-year assets ≠ prior year's end-of-year assets

**The mistake**: The asset rollforward equation doesn't tie. Beginning of year assets on the current 5500 differ from the prior year's ending assets.

**Why it happens**: Restated values (e.g., audit findings, valuation adjustments), trustee reconciliation differences, fund mergers, recordkeeper transitions.

**Symptom**: DOL and IRS examiners catch it. The instructions require beginning-of-year amounts to equal the end-of-year amounts on the prior year's return (2025 Form 5500-SF instructions, line 7; 2025 Form 5500-EZ instructions, Part III).

**Fix**: Reconcile against the trustee statements. If the prior year's ending figures were wrong, amend the prior-year return so the two years tie (Schedule H Part I holds assets and liabilities; Part II holds income and expenses).

**Prevention**: Reconcile trust statements at year-end. Coordinate with trustee, recordkeeper, and IQPA auditor on year-end values. Document any restatement.

---

## 6. Late deferrals not reported, or reported but not corrected

**The mistake**: Employee 401(k) deferrals deposited to the trust late (after the earliest date they can reasonably be segregated from the employer's general assets; for plans with fewer than 100 participants, deposits within 7 business days are deemed timely under 29 CFR 2510.3-102(a)(2)). Either not reported (Form 5500-SF line 10a, Schedule H or I line 4a), or reported but no corrective action taken.

**Why it happens**: Payroll-to-recordkeeper handoff is delayed, sponsor cash flow tight, processing error.

**Symptom**: DOL examination targets late deferrals. The late deposit is a prohibited transaction: 15% first-tier excise tax on the amount involved under IRC §4975(a), reported on Form 5330.

**Fix**: 
1. Calculate lost earnings on the late deferrals (using DOL's online calculator or actual fund returns, whichever higher)
2. Deposit the lost earnings into the trust
3. File Form 5330 reporting the 15% excise tax on the lost-earnings amount
4. Consider VFCP (Voluntary Fiduciary Correction Program). Applicants that satisfy VFCP and PTE 2002-51 get relief from the excise tax and do not file Form 5330 for the corrected transaction (2025 Form 5500-SF instructions, line 10a)

**Prevention**: Establish written deferral-deposit policy. Audit deposit timing quarterly. For small plans, the DOL's safe harbor is 7 business days; aim for same-day or next-day deposit.

---

## 7. IQPA audit issues — wrong opinion type, conflicts, or missing report

**The mistake**: Large plan files Form 5500 + Schedule H without an IQPA audit report attached, or with an audit that has a disclaimer or adverse opinion that the plan didn't address.

**Why it happens**: Audit was delayed, auditor's findings weren't addressed in time, sponsor used an auditor who lacked ERISA-specific expertise.

**Symptom**: DOL rejects or sends a letter. The plan may face penalties for filing without the required audit.

**Fix**: Commission a qualified IQPA audit from a firm with ERISA expertise. Address findings (operational failures, material weaknesses). File the amended 5500 with the audit attached.

**Prevention**: Engage the auditor 4–6 months before plan year end. Use a firm with ERISA practice. Address any control weaknesses identified during the audit before filing. For first-time large-plan filers (just crossed 100), start the audit conversation as soon as the participant count crosses 80 (early warning).

---

## 8. Ignoring the small-plan audit waiver requirements

**The mistake**: Small plan files 5500-SF or 5500 + Schedule I, claims audit waiver, but doesn't meet the conditions of 29 CFR §2520.104-46.

**Why it happens**: Small-plan audit waiver requires either (a) at least 95% of plan assets in "qualifying plan assets" (similar to eligible assets for 5500-SF), OR (b) any non-qualifying assets bonded by an ERISA fidelity bond at 100% of value (vs. the standard 10%). Sponsors miss the conditions.

**Symptom**: DOL examination determines audit waiver doesn't apply; full audit required retroactively.

**Fix**: Commission audit, file amended 5500 with Schedule H + audit. Or, if the issue is a missing fidelity bond at 100% of non-qualifying asset value, obtain the bond going forward and document.

**Prevention**: Verify the small-plan audit waiver conditions every year. Maintain the ERISA fidelity bond at no less than 10% of funds handled in the preceding plan year, minimum $1,000, maximum required $500,000 ($1,000,000 for plans holding employer securities or pooled employer plans) (ERISA §412(a); 29 CFR 2580.412-11). Increase coverage to at least 100% of any non-qualifying assets if relying on the enhanced-bond prong of the waiver. A plan that meets the waiver only through the enhanced bond cannot file Form 5500-SF.

---

## 9. Missing the SAR (Summary Annual Report) distribution

**The mistake**: Form 5500 / 5500-SF is filed but the Summary Annual Report (SAR) is never distributed to participants.

**Why it happens**: The SAR is a separate ERISA obligation under §104(b)(3); the administrator forgets that filing 5500 doesn't fulfill it.

**Symptom**: Participant complaint, DOL examination finding.

**Fix**: Distribute the SAR retroactively. Document the distribution.

**Prevention**: Calendar the SAR deadline: 9 months after plan year end (calendar plan: September 30 of the following year), or 2 months after the end of an IRS extension period if an extension was granted (29 CFR 2520.104b-10(c)). Model SAR content is in 29 CFR 2520.104b-10(d). Small plans relying on the audit waiver must include the waiver disclosure in the SAR. Form 5500-EZ filers (one-participant plans) are NOT required to distribute a SAR.

---

## 10. Wrong participant count — including or excluding the wrong people

**The mistake**: Counting only currently active employees, missing terminated participants with vested balances, or including ineligible employees.

**Why it happens**: Pension plan participant counts include retirees and beneficiaries — not just current employees. The first-day-of-year count drives the audit threshold.

Specifically:

- **Active participants**: currently employed and accruing or eligible to accrue benefits
- **Retired or separated participants with vested benefits**: former employees with account balances or vested DB benefits
- **Beneficiaries**: receiving benefits (after participant's death)

A 401(k) plan with 50 active employees with balances and 75 former employees who still have balances has 125 participants with account balances on the first day of the year (the count a defined contribution plan uses, Form 5500 line 6g(1) / Form 5500-SF line 5c(1)), which is over the large plan threshold.

**Symptom**: Wrong audit decision, wrong variant choice, wrong Schedule H/I selection. DOL correspondence.

**Fix**: Re-count. File amended return if variant or audit requirement changes.

**Prevention**: Coordinate with recordkeeper or TPA on participant data. Review separated-participant list at year-end. If the plan document permits, involuntary cash-outs of vested balances up to $7,000 (IRC §411(a)(11)(A)) reduce the count of former employees with balances.

---

## 11. Form 5500-EZ filed when not required

**The mistake**: One-participant plan with year-end assets below $250,000 files anyway. Not strictly an error, but unnecessary.

**Why it happens**: Owner doesn't realize the filing exemption for one-participant plans whose combined year-end assets do not exceed $250,000 (2025 Form 5500-EZ instructions, Who Does Not Have To File).

**Symptom**: Filing accepted but the IRS files it. No harm, but no benefit either.

**Fix**: None needed; future years can skip filing if assets remain below $250,000.

**Prevention**: Read the exception. The $250,000 threshold aggregates across all one-participant plans of the same employer.

---

## 12. PBGC premium filing skipped (defined benefit plans only)

**The mistake**: DB plan files 5500 + Schedule SB but doesn't make the PBGC comprehensive premium filing (through PBGC's My PAA) by the PBGC due date.

**Why it happens**: Form 5500 and PBGC are different filings to different agencies.

**Symptom**: PBGC penalty letter. PBGC premiums + late penalty.

**Fix**: File PBGC premium with late penalty. Address per PBGC guidance.

**Prevention**: Calendar PBGC due dates separately from 5500. The premium filing is due the 15th day of the 10th calendar month that begins on or after the first day of the plan year (calendar plan: October 15 of the same year) (29 CFR 4007.11(a)). A Form 5558 extension does not extend it (Form 5558 instructions).

---

## Summary checklist before submission

Before clicking "Submit" in EFAST2 (or mailing 5500-EZ), confirm:

- [ ] Correct variant (re-walked decision tree this year)
- [ ] All required schedules attached
- [ ] IQPA audit attached if Schedule H
- [ ] Plan number consistent with prior year
- [ ] Beginning-of-year assets = prior year ending
- [ ] Participant count includes retirees and beneficiaries
- [ ] Late deferrals (if any) reported AND corrected (Form 5330 + lost earnings)
- [ ] Fidelity bond in place at adequate level
- [ ] SAR ready to distribute (calendar 9-month deadline)
- [ ] Form 5558 filed if extension needed
- [ ] PBGC premium filed if DB plan
- [ ] Signer credentials valid; signer ready to sign
