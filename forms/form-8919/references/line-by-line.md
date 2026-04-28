# Form 8919 — Line-by-Line Reference

Definitive line-by-line guidance for Form 8919 (Uncollected Social Security and Medicare Tax on Wages). Cross-reference against the current-year form revision at https://www.irs.gov/pub/irs-pdf/f8919.pdf — line numbers and labels can shift between revisions.

---

## Header Section

### Name(s) shown on return

The filer's full legal name as it appears on Form 1040. For joint returns where only one spouse is the misclassified worker, enter both spouses' names (matching 1040 header) but the form pertains to the worker spouse only.

### Social security number

The misclassified worker's SSN. If filing jointly and the misclassified worker is not the primary taxpayer, the SSN here should be the worker's, not the primary's. The IRS matches the 8919 wage entry on 1040 Line 1g to the SSN listed on the 8919.

---

## Line 1 — Firm Information Table

The form provides space for **up to 5 firms**. If more, attach a continuation Form 8919 (or a schedule with the same column headers).

### Column (a) — Name of firm

The legal name of the firm or business that paid the worker. Match this exactly to the name on the 1099-NEC (Box "PAYER'S name") or 1099-MISC. Do not abbreviate or paraphrase — the IRS database matches firm name + EIN.

**Example:**
- 1099-NEC says "ABC Consulting LLC dba ABCConsult" → enter "ABC Consulting LLC dba ABCConsult"

### Column (b) — Firm's federal identification number

The firm's Employer Identification Number (EIN). This is on:
- 1099-NEC: Box 6 ("PAYER'S TIN")
- 1099-MISC: Box "PAYER'S TIN"
- W-2 (if also issued): Box b ("Employer identification number")

Format: XX-XXXXXXX (two digits, dash, seven digits).

If the worker has the firm's EIN from a different source (a contract, a bank record), use the 1099/W-2 source as authoritative. If they conflict, ask the user to clarify before filing.

### Column (c) — Reason code

Single-letter code A, C, G, or H. See `references/reason-codes.md` for the decision tree. Summary:

| Code | Trigger |
|------|---------|
| **A** | Filed SS-8, received determination ruling worker = employee |
| **C** | Same firm issued W-2 + 1099 for same job (no SS-8 needed) |
| **G** | Filed SS-8, awaiting determination, reasonably believes employee status |
| **H** | Same as C, plus firm filed W-2c that still excluded the 1099 amount |

Other codes (B, D, E, F) are not generally used by workers; they exist in IRS internal documentation but are not active in current form revisions.

### Column (d) — Date of IRS determination or correspondence

For **code A only**: enter the date on the IRS determination letter (MM/DD/YYYY).

For **codes C, G, H**: leave blank or enter the date of any related IRS correspondence the user has on file.

### Column (e) — Check if Form SS-8 was filed

Check the box if Form SS-8 has been filed. **Required for codes A and G.** For code C, the box is typically left unchecked; for code H, it depends on whether SS-8 was also filed.

If using code G and the user has not yet mailed SS-8: instruct the user to mail SS-8 **before** mailing the 1040 (or before e-filing if going that route). The check on column (e) certifies SS-8 has been filed; checking it falsely is a misrepresentation.

### Column (f) — Total wages received with no Social Security or Medicare tax withholding

The **gross** amount reported on the 1099-NEC (Box 1) or 1099-MISC, plus any unreported wages from this firm.

**Important:** This is gross, NOT net of business expenses. Form 8919 treats the income as wages, and wages are not netted against expenses. Business deductions don't apply because the income isn't being treated as self-employment. (This is a feature, not a bug — it's part of why 8919 saves money.)

If the worker also received some legitimate self-employment income from the same firm (e.g., a side project genuinely contracted out), that legitimate portion goes on Schedule C and **not** on Form 8919. Only put the misclassified-employee portion on column (f).

---

## Line 2 — Total wages with no SS/Medicare withholding

Sum column (f) across all rows on Line 1. This is the total Form 8919 wage amount, used for both the SS calculation (Lines 3-7) and the Medicare calculation (Lines 8-9).

This is also the amount that will appear on **Form 1040, Line 1g** (current revision; verify line label on the current 1040).

---

## Line 3 — Maximum amount subject to Social Security tax

The Social Security wage base for the tax year. This is set annually by the SSA based on the National Average Wage Index.

| Tax Year | SS Wage Base |
|----------|--------------|
| 2025 | $176,100 |
| 2026 | TBD (verify on https://www.ssa.gov/oact/cola/cbb.html) |

For tax year 2026, the SSA typically announces the new figure in October 2025. Always verify before filing.

---

## Line 4 — Total Social Security wages and tips (W-2 + Form 8919)

Sum:
- Line 2 of this Form 8919 (the misclassified wages)
- Box 3 of every W-2 the user received (Social Security wages)
- Box 7 of every W-2 the user received (Social Security tips)
- Tier 1 Railroad Retirement compensation (if applicable)

Do **not** include:
- Box 1 of W-2 (gross wages — Box 3 may differ if there were 401(k) deferrals)
- Self-employment income (computed separately on Schedule SE; SE wage base interaction handled there)
- 1099 amounts that are NOT being reported on Form 8919 (those are SE income on Schedule C/SE)

---

## Line 5 — Subtract Line 4 from Line 3

If the result is **zero or negative**, the worker has already maxed out the Social Security wage base via W-2 income. Enter zero on Line 5 → Lines 6 and 7 will be zero → no additional Social Security tax via Form 8919.

If positive, this is the remaining room under the wage base.

---

## Line 6 — Wages subject to Social Security tax

The smaller of Line 2 or Line 5.

**Example:** Worker has $72,000 on Line 2 and $104,100 on Line 5 → Line 6 = $72,000.

**Example:** Worker has $200,000 on Line 2 and $50,000 on Line 5 → Line 6 = $50,000 (only $50,000 of the 8919 wages fits under the wage base; the rest is exempt from SS but still subject to Medicare on Line 8).

---

## Line 7 — Social Security tax

Line 6 × 6.2%, rounded to the nearest whole dollar.

The 6.2% is the **employee** Social Security rate per IRC §3101(a). The employer rate of 6.2% is **not** also collected here — that's the entire point of Form 8919 (the employee pays only the employee share).

---

## Line 8 — Wages subject to Medicare tax

Same as Line 2. There is no wage base for Medicare; all wages are subject to the Medicare tax.

---

## Line 9 — Medicare tax

Line 8 × 1.45%, rounded to the nearest whole dollar.

The 1.45% is the **employee** Medicare rate per IRC §3101(b)(1). The Additional Medicare Tax (0.9%) is computed separately on Form 8959 (next section).

---

## Line 10 — (Reserved or Additional Medicare reference)

The current form revision may reserve this line or use it for cross-reference to Form 8959. **Verify against the current form PDF.** If Form 8959 applies (total wages exceed filing-status threshold), the additional 0.9% is computed there, not on 8919 directly.

---

## Line 11 — Total uncollected Social Security and Medicare tax on wages

Line 7 + Line 9. This is the FICA-equivalent amount the worker owes.

**Routing:** This amount flows to **Schedule 2, Line 5** ("Social security and Medicare tax on unreported tip income or wages from Form 8919"). From Schedule 2, it then flows to **Form 1040, Line 23** (other taxes added to total tax).

---

## Cross-Form Mapping Summary

| From | To | Amount |
|------|-----|--------|
| Form 8919 Line 2 | Form 1040 Line 1g | Wage amount (subject to ordinary income tax) |
| Form 8919 Line 11 | Schedule 2 Line 5 | FICA tax |
| Schedule 2 Total | Form 1040 Line 23 | All "other taxes" added to total tax |

---

## Verification Math

For each filing, the agent should verify:

```
Line 7  = ROUND(Line 6 × 0.062)
Line 9  = ROUND(Line 8 × 0.0145)
Line 11 = Line 7 + Line 9

If Line 2 ≤ Line 5: Line 7 = ROUND(Line 2 × 0.062)
If Line 2 >  Line 5: Line 7 = ROUND(Line 5 × 0.062)
                     Line 8 = Line 2 (Medicare always full)

Total effective rate on Line 2 (when fully under wage base): 7.65%
```

---

## Edge Cases

### Worker has no W-2 wages

Line 4 = Line 2; Line 5 = Line 3 − Line 2; Line 6 = MIN(Line 2, Line 5). For 2025 wage base of $176,100, a worker with $72,000 of 8919-only wages: Line 4 = $72,000, Line 5 = $104,100, Line 6 = $72,000.

### Worker has W-2 wages exactly at the SS wage base

Line 4 = wage base; Line 5 = 0; Line 6 = 0; Line 7 = 0. No additional SS tax via 8919. Medicare (Line 9) still applies on full Line 2.

### Worker has W-2 wages well above the SS wage base from prior employer

W-2 Box 3 is capped at the wage base by the employer. Line 4 = wage base + Line 2. Line 5 = Line 3 − Line 4 = 0 − Line 2 = negative → Line 5 = 0; Line 6 = 0; Line 7 = 0. Same outcome: no SS via 8919, full Medicare.

### Worker has multiple firms, some 8919-eligible, some genuinely SE

Only the 8919-eligible firms appear on Line 1. The genuinely self-employed income goes on Schedule C and Schedule SE separately. Schedule SE will compute SE tax on the SE income; Form 8919 computes FICA on the misclassified income; the two coexist on Form 1040.

### Worker discovers misclassification after filing original return

File Form 1040-X with Form 8919 attached for the misclassified year. The amended return swaps Schedule SE treatment for 8919 treatment. Refund of overpaid SE tax (minus the underpaid FICA) is the typical result. Statute of limitations: 3 years from original filing under IRC §6511.

---

## Cross-References

- IRC §3101 — Employee FICA rates
- IRC §3121(d) — Definition of "employee"
- IRC §1401 — Self-employment tax (alternative if 8919 doesn't apply)
- IRC §6511 — Statute of limitations on refund claims
- Rev. Rul. 87-41 — Common-law worker classification test
- IRS Pub 15-A — Employer's Supplemental Tax Guide
- Form 8959 — Additional Medicare Tax
- Form SS-8 — Determination of Worker Status
- Schedule 2 (Form 1040) — Additional Taxes
