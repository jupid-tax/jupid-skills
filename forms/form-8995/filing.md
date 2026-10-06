# Form 8995 Filing Playbook

This playbook is for browser-automation runtimes (Playwright, Puppeteer, Browserbase) that have explicit user authorization to file Form 8995 as an attachment to Form 1040.

**Critical rule:** Form 8995 is **never** filed standalone. It is always an attachment to Form 1040. The filing channel is determined by how Form 1040 is filed.

---

## Decision tree: Pick the filing channel

```
┌─ Is Form 1040 already in progress on a paid software channel (TurboTax, H&R, TaxAct, FreeTaxUSA)?
│  └─ Yes → File 8995 inside that software (it auto-generates from Schedule C + adjustments)
│  └─ No → next question
│
├─ AGI ≤ $89,000 (IRS Free File guided software limit for the 2026 filing season)?
│  └─ Yes → IRS Free File guided software (multiple providers; pick one that supports Form 8995)
│  └─ No → next question
│
├─ Comfortable with manual fillable forms?
│  └─ Yes → IRS Free File Fillable Forms (FFFF) — supports Form 8995 as attached schedule; open for 2025 returns until Oct. 15, 2026
│  └─ No → use paid tax software
│
└─ Paper filing as last resort:
   - Print Form 8995, attach to Form 1040, mail to IRS service center for taxpayer's state
```

IRS Direct File was not offered in the 2026 filing season; do not route users to it. Sources: https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free (Free File $89,000 AGI), https://www.irs.gov/e-file-providers/free-file-fillable-forms (FFFF closes Oct. 15, 2026).

---

## Channel-specific field mapping

### IRS Free File Fillable Forms (FFFF)

URL: `https://www.freefilefillableforms.com/`

Form 8995 is added via the "Add Form" menu, then attached to Form 1040.

Field mapping from this skill's draft to FFFF labels:

| Skill output line | FFFF field label | Notes |
|-------------------|------------------|-------|
| Header — Name | "Name(s) shown on return" | Auto-populates from 1040 |
| Header — SSN | "Your taxpayer identification number" | Auto-populates from 1040 |
| Line 1i (a) | "Trade, business, or aggregation name" | Free text |
| Line 1i (b) | "Taxpayer identification number" | EIN if the business has one, else SSN; entity EIN for K-1 source |
| Line 1i (c) | "Qualified business income or (loss)" | Numeric, can be negative |
| (Repeat for 1ii–1v if multiple sources) | | |
| Line 2 | "Total qualified business income or (loss)" | Sum of column (c); can be negative |
| Line 3 | "Qualified business net (loss) carryforward from the prior year" | Negative or 0 |
| Line 4 | "Total qualified business income" | Auto-computed; 0 if negative |
| Line 5 | "Qualified business income component" | Auto-computed (20% of line 4) |
| Line 6 | "Qualified REIT dividends and publicly traded partnership (PTP) income or (loss)" | Manually entered |
| Line 7 | "Qualified REIT dividends and qualified PTP (loss) carryforward from the prior year" | Negative or 0 |
| Line 8 | "Total qualified REIT dividends and PTP income" | Auto-computed; 0 if negative |
| Line 9 | "REIT and PTP component" | Auto-computed (20% of line 8) |
| Line 10 | "Qualified business income deduction before the income limitation" | Auto-computed |
| Line 11 | "Taxable income before qualified business income deduction" | Manually entered |
| Line 12 | "Net capital gain, increased by qualified dividends" | Manually entered |
| Line 13 | "Subtract line 12 from line 11" | Auto-computed |
| Line 14 | "Income limitation" | Auto-computed (20% of line 13) |
| Line 15 | "Qualified business income deduction" | Smaller of line 10 or 14; flows to 1040 line 13a |
| Line 16 | "Total qualified business (loss) carryforward" | Negative or 0 |
| Line 17 | "Total qualified REIT dividends and PTP (loss) carryforward" | Negative or 0 |

Labels above are the 2025 form's line captions; FFFF field names can differ slightly. After saving Form 8995, verify on Form 1040 in FFFF that line 13a matches Form 8995 line 15.

### Paid software (TurboTax, H&R Block, TaxAct, FreeTaxUSA)

Each package handles Form 8995 automatically once Schedule C and Schedule 1 are complete. The agent's role is verification:

1. Complete Schedule C entry in the software
2. Complete Schedule SE (½ SE tax)
3. Complete Schedule 1 (SE health insurance, SE retirement)
4. Navigate to "Deductions → Qualified Business Income"
5. Verify the software's computed QBI matches this skill's Line 2 and Line 4 figures
6. Verify the final QBI deduction matches this skill's Line 15 figure

If figures differ by more than $1, do not submit. Reconcile manually first.

### Paper filing

For paper Form 8995:

1. Print blank Form 8995 from `https://www.irs.gov/pub/irs-pdf/f8995.pdf`
2. Fill in by hand or PDF editor; line up with the skill's draft
3. Attach in attachment sequence order behind Form 1040 (the Attachment Sequence No. is in the form header; 2025 Form 8995 is No. 55)
4. Mail Form 1040 + all schedules + Form 8995 to the IRS service center for the taxpayer's state (addresses on Form 1040 instructions)

Paper returns take longer to process than e-filed returns. E-file strongly preferred.

---

## Pre-flight checklist

Before submitting Form 1040 with Form 8995 attached:

- [ ] Skill's Line 15 matches what's on Form 1040 line 13a
- [ ] Schedule C is complete (Line 31 net profit reconciles)
- [ ] Schedule SE Line 13 (½ SE tax) used in QBI adjustment matches what flows to Schedule 1
- [ ] Schedule 1 Lines 16, 17 (SE retirement, SE health insurance) used in QBI adjustment match what flows to Form 1040
- [ ] Taxable income before QBI (Form 8995 line 11) is at or below the threshold; otherwise use Form 8995-A
- [ ] No K-1 has Section 199A info that wasn't included in rows 1i–1v
- [ ] If REIT income claimed: 1099-DIV Box 5 amount (not Box 1a) was used
- [ ] Carryforwards (if any) are documented from prior year's return

---

## Submission state machine

```
Draft → Validated → Authorized → Submitted → Accepted → Processed
```

- **Draft** — Skill produced output; user has not reviewed
- **Validated** — User has reviewed and confirmed numbers
- **Authorized** — User has explicitly granted submission permission (separate consent from "fill out for me")
- **Submitted** — Filed via channel; transmission acknowledged
- **Accepted** — IRS accepted the e-file (auto-checks passed); paper filing skips this state
- **Processed** — Refund issued or balance due notice received

---

## Security rules

- **Never persist** SSN, DOB, IP PIN, AGI from prior year, or any tax data after the session ends
- **Always require explicit consent** at the Authorized state — separate from any earlier authorization to "help fill out the form"
- **Show the diff** between this skill's draft and the final submission on the channel — if anything was changed by the channel, surface it before submission
- **Log the confirmation number** returned by the channel after submission, but redact SSN/DOB from the log
- **For paper filing**: do not print to a shared printer; advise the user to print themselves

---

## Common channel-specific issues

### FFFF: Form 8995 not appearing in Add Form menu

FFFF retires older forms each year. If Form 8995 is missing, the user is filing for a year FFFF no longer supports — switch to a paid software channel.

### Paid software: Software wants Form 8995-A even though user is below threshold

Some packages auto-route to 8995-A if any K-1 has SSTB indicator. If the user's total taxable income is below threshold, Form 8995 is correct regardless of SSTB status. Override the software's choice if the package allows; otherwise, file with 8995-A — the math produces the same answer below the threshold.

### Paper: Form 8995 attached to wrong year's 1040

The tax year is printed in the form header (the attachment sequence number, 55, does not change). Use the Form 8995 revision for the same tax year as the 1040.
