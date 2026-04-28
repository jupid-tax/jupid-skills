# Filing Form 8995-A — Browser Automation Playbook

This document is consumed only when the user explicitly authorizes the agent to file the return. Otherwise the deliverable is the draft from `SKILL.md` and the user types it into their own software.

Form 8995-A is **not filed independently**. It is an attachment to Form 1040 (or 1040-SR, 1040-NR, 1041). The agent files Form 1040 and attaches the completed Form 8995-A as part of that submission.

---

## Decision tree — picking a filing channel

```
Does the user already have a tax software account they want to use?
├── Yes → use that channel; map the draft fields to its UI labels
└── No → proceed below

Does the user qualify for IRS Free File guided software?
  (AGI ≤ ~$84,000 OR they want guided software)
├── Yes → IRS Free File Alliance partner
└── No → continue

Is the user comfortable filling forms directly?
├── Yes → IRS Free File Fillable Forms (FFFF)
└── No → paid commercial software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes)

Does the user prefer paper?
└── Yes → paper Form 1040 + paper Form 8995-A attached
```

**IRS Direct File** does NOT support QBI as of the 2026 filing season — Direct File covers W-2 wages, Social Security, unemployment, interest, and limited credits. If the user has QBI, they're not in Direct File scope. Do not route them there.

---

## Pre-flight checklist

Before opening any browser session, confirm the agent has:

- [ ] Completed Form 8995-A draft with all four schedules (or "N/A" markers) from `SKILL.md`
- [ ] Form 1040 draft with Line 13 = Form 8995-A Line 39
- [ ] Schedule C / K-1 source documents that fed QBI
- [ ] User's verified identity for IRS e-file PIN signature (prior-year AGI or self-select PIN)
- [ ] Direct deposit info (if expecting refund) OR payment method (if owing)
- [ ] User's explicit consent to submit — do NOT submit without "yes, file this"

The agent must NEVER persist:
- SSN/ITIN beyond the active session
- Date of birth beyond the active session
- Self-select PIN or prior-year AGI used for e-file authentication
- Bank account/routing for direct deposit beyond the active session

If the agent's runtime cannot guarantee these are wiped at session end, the agent must refuse to file and produce a draft instead.

---

## Channel: IRS Free File Fillable Forms (FFFF)

FFFF is the IRS's no-cost web app for filers who can fill out their own forms. Maps closely to paper.

### Field map: Form 8995-A on FFFF

| Draft Section | FFFF Form | FFFF Field |
|---------------|-----------|------------|
| Part I L1(a) | Form 8995-A | "Trade, business, or aggregation name" rows 1-3 |
| Part I L1(b) | Form 8995-A | "Specified service trade or business" checkbox |
| Part I L1(c) | Form 8995-A | "Taxpayer Identification Number" |
| Part II L2-13 | Form 8995-A | Numeric grid columns A, B, C |
| Schedule A | Form 8995-A Sch A | Add Schedule A from "Schedules" dropdown |
| Schedule B | Form 8995-A Sch B | Add Schedule B from "Schedules" dropdown |
| Schedule C | Form 8995-A Sch C | Add Schedule C from "Schedules" dropdown |
| Schedule D | Form 8995-A Sch D | Add Schedule D from "Schedules" dropdown |
| Part IV L27-39 | Form 8995-A | Bottom-of-form numeric fields |

### Submission state machine

```
Draft → Reviewed → Signed → Submitted → Accepted (IRS) → Processed → Refund issued / Balance due processed
                                    ↓
                                  Rejected → Surface error code → Retry
```

After submission, capture the IRS Submission ID and surface to the user. Do not close the session until the IRS returns "Accepted" (typical: minutes to hours).

---

## Channel: Commercial software (TurboTax, H&R Block, FreeTaxUSA, etc.)

Each commercial product has its own UI. The agent should:

1. Walk through the product's "self-employment" or "business income" wizard
2. When the wizard reaches QBI, enter the figures from the Form 8995-A draft
3. Most software computes Form 8995-A automatically from the Schedule C / K-1 inputs — verify the software's auto-computed figures match the agent's draft
4. If they DIVERGE: flag to user before proceeding. Common causes:
   - Software treated business as non-SSTB when agent classified it as SSTB (or vice versa)
   - Software didn't apply SE-tax / SE-HI / SE-retirement adjustment to QBI
   - Software pulled wrong W-2 wages figure (e.g., included guaranteed payments)

Always run the agent's validation checks against the software's output, not the other way around.

---

## Channel: Paper filing

If the user is paper-filing:

1. Print Form 1040, all schedules, Form 8995-A, and any required schedules of 8995-A
2. Confirm the user signs (and spouse signs if MFJ)
3. Mail to the IRS service center for the user's state (per Form 1040 instructions, page 110 for tax year 2025)
4. Use Certified Mail with return receipt — the receipt is proof of timely filing under IRC §7502
5. Keep a complete copy

Paper filing has no e-file authentication so the SSN/AGI rules don't apply, but the agent should still NOT persist this data beyond the session.

---

## Common rejections and fixes

| Error | Cause | Fix |
|-------|-------|-----|
| Form 8995-A Line 39 ≠ Form 1040 Line 13 | Transcription error | Re-enter Line 13 to match Form 8995-A Line 39 |
| Schedule A mandatory but not attached | SSTB business in phase-in zone with no Schedule A | Add Schedule A; recompute the phase-in reduction |
| QBI loss not carried forward | Prior-year QBI was negative; current year missed the carryforward input | Pull prior-year Form 8995-A Line 16 (or the carryforward worksheet) |
| W-2 wages overstated | Included guaranteed payments or independent-contractor 1099s | Reduce L4 to actual W-2 wages only |
| Aggregation eligibility not confirmed | Schedule B used but one of the businesses is SSTB | Disaggregate; SSTBs cannot be in an aggregation |

---

## Security rules (recap)

- NEVER persist SSN/DOB/PIN
- NEVER submit without explicit user consent
- ALWAYS show the diff between the agent's draft and the final form before submission
- ALWAYS capture the IRS Submission ID and surface to the user
- ALWAYS produce a PDF copy of the filed return for the user's records

If the runtime cannot satisfy these rules, refuse to file and produce a draft for the user to file themselves.
