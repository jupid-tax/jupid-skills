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
├─ Is taxpayer eligible for IRS Direct File (limited states, simple returns)?
│  └─ Yes & QBI source is Schedule C only → IRS Direct File supports basic QBI from Schedule C
│  └─ Yes but K-1 / REIT / PTP income → Direct File does not support; use FFFF or paid software
│  └─ No → next question
│
├─ AGI ≤ Free File threshold (~$84K for tax year 2025)?
│  └─ Yes → IRS Free File guided software (multiple providers; pick one that supports Form 8995)
│  └─ No → next question
│
├─ Comfortable with manual fillable forms?
│  └─ Yes → IRS Free File Fillable Forms (FFFF) — supports Form 8995 as attached schedule
│  └─ No → use paid tax software
│
└─ Paper filing as last resort:
   - Print Form 8995, attach to Form 1040, mail to IRS service center for taxpayer's state
```

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
| Line 1a (i) | "Trade, business, or aggregation name" | Free text |
| Line 1a (ii) | "Taxpayer identification number" | SSN for sole prop, EIN for K-1 source |
| Line 1a (iii) | "Qualified business income or (loss)" | Numeric, can be negative |
| (Repeat for 1b-1e if multiple sources) | | |
| Line 2 | "Total qualified business income or (loss)" | Sum or 0 |
| Line 3 | "Qualified business net (loss) carryforward from prior years" | Negative or 0 |
| Line 4 | "Total qualified business income component" | Auto-computed by FFFF |
| Line 5 | "Qualified REIT dividends and PTP income" | |
| Line 6 | "Qualified REIT dividends and PTP (loss) carryforward" | |
| Line 7 | "Total qualified REIT dividends and PTP income" | Auto-computed |
| Line 10 | "QBI component (Line 4 × 20%)" | Auto-computed |
| Line 11 | "REIT/PTP component (Line 7 × 20%)" | Auto-computed |
| Line 12 | "QBI deduction before income limitation" | Auto-computed |
| Line 13 | "Taxable income before QBI deduction" | Manually entered |
| Line 14 | "Net capital gain" | Manually entered |
| Line 15 | "Line 13 minus Line 14" | Auto-computed |
| Line 16 | "20% of Line 15 (income limitation)" | Auto-computed |
| Line 17 | "QBI deduction (smaller of Line 12 or Line 16)" | Auto-computed; flows to 1040 Line 13 |

After saving Form 8995, FFFF auto-links Line 17 to Form 1040 Line 13. Verify by inspecting Form 1040 in FFFF: Line 13 should match Line 17.

### IRS Direct File

URL: `https://directfile.irs.gov/`

Direct File handles QBI computation in the Schedule C and Schedule 1 flows automatically — no separate Form 8995 entry. Verify the QBI deduction shows on the final review screen and matches this skill's Line 17 output.

If the user's situation is supported by Direct File but the computed QBI differs from this skill's draft by more than $1, investigate before submitting. Most likely causes:
- Direct File auto-applied SE adjustments differently
- Direct File treated rental income as not qualifying
- User entered different numbers in Direct File than they gave the agent

### Paid software (TurboTax, H&R Block, TaxAct, FreeTaxUSA)

Each package handles Form 8995 automatically once Schedule C and Schedule 1 are complete. The agent's role is verification:

1. Complete Schedule C entry in the software
2. Complete Schedule SE (½ SE tax)
3. Complete Schedule 1 (SE health insurance, SE retirement)
4. Navigate to "Deductions → Qualified Business Income"
5. Verify the software's computed QBI matches this skill's Line 4 figure
6. Verify the final QBI deduction matches this skill's Line 17 figure

If figures differ by more than $1, do not submit. Reconcile manually first.

### Paper filing

For paper Form 8995:

1. Print blank Form 8995 from `https://www.irs.gov/pub/irs-pdf/f8995.pdf`
2. Fill in by hand or PDF editor; line up with the skill's draft
3. Attach behind Schedule 1 in the Form 1040 packet (sequence number is on the form footer; for 2024 revision Form 8995 is sequence 55)
4. Mail Form 1040 + all schedules + Form 8995 to the IRS service center for the taxpayer's state (addresses on Form 1040 instructions)

Paper filing requires 6-8 weeks to process. E-file strongly preferred.

---

## Pre-flight checklist

Before submitting Form 1040 with Form 8995 attached:

- [ ] Skill's Line 17 matches what's on Form 1040 Line 13
- [ ] Schedule C is complete and signed (Line 31 net profit reconciles)
- [ ] Schedule SE Line 13 (½ SE tax) used in QBI adjustment matches what flows to Schedule 1
- [ ] Schedule 1 Lines 16, 17 (SE retirement, SE health insurance) used in QBI adjustment match what flows to Form 1040
- [ ] Form 1040 Line 15 (taxable income) is below the threshold OR Form 8995-A would be more appropriate
- [ ] No K-1 has Section 199A info that wasn't included in Lines 1a-1e
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

### Direct File: QBI deduction shows as $0

Most common cause: Direct File flagged the Schedule C as a hobby (no profit motive) or the user marked it as "not a trade or business". Reopen Schedule C entry and confirm the profit motive question.

### Paid software: Software wants Form 8995-A even though user is below threshold

Some packages auto-route to 8995-A if any K-1 has SSTB indicator. If the user's total taxable income is below threshold, Form 8995 is correct regardless of SSTB status. Override the software's choice if the package allows; otherwise, file with 8995-A — the math produces the same answer below the threshold.

### Paper: Form 8995 attached to wrong year's 1040

The sequence number on the form footer changes annually. Use the Form 8995 revision dated for the same tax year as the 1040.
