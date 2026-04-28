# Filing Form 8962 (and the underlying Form 1095-A reconciliation)

This playbook covers the browser-automation workflow for filing Form 8962. Form 1095-A itself is informational and is **not** attached to the tax return — the IRS receives a copy directly from the Marketplace. The agent's job is to produce a complete, validated Form 8962, attach it to Form 1040, and submit through the chosen filing channel.

---

## Decision tree for filing channel

```
Did the taxpayer have only Marketplace coverage and otherwise simple return (W-2, 1099, basic deductions)?
├── YES, AGI under $84,000 (2025 FFFFile-eligible) → IRS Free File partner software (TaxSlayer, OLT, etc.)
├── YES, AGI any amount, comfortable with forms → IRS Free File Fillable Forms (FFFF)
└── NO (Schedule C, complex investments, etc.)
    ├── Use paid software (TurboTax, H&R Block, FreeTaxUSA, TaxAct, Cash App Taxes)
    └── For maximum control: paper filing (Form 1040 + Form 8962 by mail)

Is taxpayer in a state where IRS Direct File is available for tax year 2025?
└── States with Direct File 2025: AZ, CA, CT, FL, ID, IL, KS, ME, MD, MA, NV, NJ, NM, NY, NC, OR, PA, SD, TN, TX, WA, WI, WY
    Note: Direct File DOES support Form 8962 for tax year 2025 (added in expansion)
    Verify current state list and supported forms at directfile.irs.gov before recommending
```

For most users with Marketplace coverage and self-employment income (the typical Jupid customer), recommend FreeTaxUSA (paid software, free federal, $14.99 state) — it handles Schedule C + Form 8962 + Form 8889 cleanly and lets the agent walk through field-by-field verification before submission.

---

## Pre-flight checklist

Before initiating filing, the agent must have:

- [ ] Form 1095-A in the user's possession (PDF or paper)
- [ ] All Part III amounts entered into the Form 8962 draft this skill produced
- [ ] Tax family size confirmed
- [ ] Modified AGI computed and reconciled with Form 1040 Line 11
- [ ] State of residence confirmed (drives FPL table)
- [ ] Filing status confirmed (MFS exception flagged if applicable)
- [ ] Shared policy allocation completed (if applicable)
- [ ] Validation checks from SKILL.md all passed
- [ ] User has explicitly authorized filing (do NOT submit without explicit consent)

Security data collected for filing — **never persist beyond session**:
- SSN (filer + spouse + dependents)
- Date of birth (filer + spouse + dependents)
- IRS Self-Select PIN or prior-year AGI (e-file authentication)
- Bank routing/account for refund deposit (if applicable)

---

## Field-by-field map: SKILL.md draft → FFFF Form 8962

The IRS Free File Fillable Forms layout for Form 8962 mirrors the paper form. Map each draft field to the corresponding FFFF input:

| SKILL.md Draft Field | FFFF Form 8962 Field |
|----------------------|----------------------|
| Tax family size | Line 1 |
| Modified AGI (filer) | Line 2a |
| Dependents' modified AGI | Line 2b |
| Household income | Line 3 (auto-computed if FFFF math) |
| FPL | Line 4 |
| Income % of FPL | Line 5 (auto if FFFF math) |
| Applicable Figure | Line 7 |
| Annual contribution | Line 8a |
| Monthly contribution | Line 8b |
| Allocation Yes/No | Line 9 |
| Annual or monthly | Line 10 |
| Annual amounts (if Line 10 = Yes) | Line 11 (a) through (f) |
| Monthly amounts (if Line 10 = No) | Lines 12–23, columns (a)–(f) |
| Total PTC | Line 24 |
| Total APTC | Line 25 |
| Net PTC | Line 26 |
| Excess APTC | Line 27 |
| Repayment limit | Line 28 |
| Excess APTC repayment | Line 29 |

After Form 8962 is completed:
- Line 26 amount → Form 1040 Schedule 3 Line 9 (Net PTC, refundable)
- Line 29 amount → Form 1040 Schedule 2 Line 1a (Excess APTC repayment, additional tax)

---

## Submission state machine

```
Draft → Validation passed → User reviews diff → User signs → Submitted →
    ├── Accepted by IRS (within 24-48h)
    │   └── Refund processed (3 weeks for direct deposit) OR balance due paid
    └── Rejected by IRS
        └── Common rejection reasons:
            • "Form 8962 missing" — must e-file with Form 8962 if 1095-A was issued
            • "PTC reconciliation incomplete" — Line 24, 25, 26 inconsistent
            • "Spouse SSN doesn't match" — Part I issuer mismatch
            • "Prior-year AGI mismatch" — re-authenticate
            └── Fix and re-submit
```

If the IRS sends a CP2000 notice months later flagging a 1095-A discrepancy:
- Compare Marketplace 1095-A (corrected version) to what was filed
- File Form 1040-X amended return with corrected Form 8962
- Respond to CP2000 notice within 30 days

---

## Security rules

The agent **must** abide by these:

1. **Never persist SSN/DOB/PIN** beyond the active filing session. After submission, scrub from memory and any local logs.
2. **Require explicit consent at submission**. The agent must show the user a final summary including Net PTC or Excess APTC repayment amount, and wait for an explicit "yes, file" before clicking submit.
3. **Show the diff between draft and final form**. If the user edits any field after the draft is produced, surface every change before submission.
4. **Never auto-resubmit on rejection**. If the IRS rejects, surface the reason to the user and ask before resubmitting.
5. **Never share Form 1095-A or 8962 across sessions** without the user's explicit reauthentication.
6. **Refund deposit info** (routing/account) must be entered by the user, not by the agent. The agent can validate format but must not store.

---

## Paper filing (fallback)

If the user prefers paper:

1. Print Form 1040 with Schedule 1, 2, 3 as needed
2. Print Form 8962 (signed copy)
3. Do NOT attach Form 1095-A — keep it in personal records
4. Mail to the IRS address for the user's state (varies; see Form 1040 instructions back cover)
5. Use certified mail with return receipt for proof of filing date

Allow 6-8 weeks for paper return processing vs. 3 weeks for e-file with direct deposit.

---

## State return considerations

A handful of states still impose a state-level individual mandate or piggy-back on the federal Premium Tax Credit:

- **California** — Form 3849 (Premium Assistance Subsidy) — separate state PTC reconciliation
- **DC, MA, NJ, RI, VT** — state mandate but no separate state PTC form; verify based on year
- **All other states** — federal Form 8962 is sufficient

Check the user's state instructions for any additional required form before submitting the federal return.
