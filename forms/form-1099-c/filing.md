# Reporting a 1099-C (no separate filing channel)

The 1099-C is **informational** — it is sent by the creditor to the IRS and to the recipient. The recipient does not file the 1099-C itself. Reporting happens through the recipient's Form 1040 (and Form 982 if claiming an exclusion).

This file describes how an agent equipped with browser tooling routes the 1099-C analysis from `SKILL.md` into the recipient's 1040 e-file or paper return. There is no standalone "1099-C filing channel."

The agent must produce a complete `SKILL.md`-format reporting plan **first**, then map the plan into one of the channels below.

---

## Channel decision tree

```
Recipient is filing 1040 anyway and is using IRS Free File Fillable Forms (FFFF)?
  → Map plan into FFFF: report on Schedule 1 Line 8c (or Schedule C Line 6) AND
    add Form 982 if exclusion is claimed.
    Use Section 1 below.

Recipient is using paid tax software (TurboTax, H&R Block, FreeTaxUSA, etc.)?
  → Use the software's "cancellation of debt" or "1099-C" wizard.
    Use Section 2 (generic pattern).

Recipient is filing on paper?
  → Schedule 1 + Form 982 attached to 1040, mailed.
    Use Section 3.

Recipient is using IRS Direct File?
  → As of early 2026, Direct File supports limited 1099-C scenarios.
    Verify current scope; if Form 982 is unsupported, redirect to FFFF or paper.
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

Same authentication and pre-flight requirements as the Schedule C filing playbook. Identity verification, prior-year AGI, etc.

### Field-by-field mapping from the SKILL plan

#### If the canceled amount is reported as taxable income (no exclusion or partial)

**Personal debt — Schedule 1:**

| SKILL plan field | FFFF location |
|------------------|---------------|
| Reporting target = Schedule 1 Line 8c | Open Schedule 1, fill Line 8c "Cancellation of debt" with the taxable amount |

**Sole-prop business debt — Schedule C:**

| SKILL plan field | FFFF location |
|------------------|---------------|
| Reporting target = Schedule C Line 6 | Open Schedule C, add the canceled amount to Line 6 "Other income" |

**Farming business debt — Schedule F:**

| SKILL plan field | FFFF location |
|------------------|---------------|
| Reporting target = Schedule F Line 8 | Open Schedule F, fill Line 8 |

#### If exclusion is claimed — add Form 982

1. From the FFFF return dashboard, click "Add a Form / Schedule"
2. Search "Form 982" or pick from the list
3. The form opens with field labels matching the paper form

| SKILL plan field | FFFF field label |
|------------------|------------------|
| Box 1a checked | "Discharge of indebtedness in a title 11 case" checkbox |
| Box 1b checked | "Discharge of indebtedness to the extent insolvent (not in a title 11 case)" checkbox |
| Box 1c checked | "Discharge of qualified farm indebtedness" checkbox |
| Box 1d checked | "Discharge of qualified real property business indebtedness" checkbox |
| Box 1e checked | "Discharge of qualified principal residence indebtedness" checkbox |
| Line 2 amount | "Total amount of discharged indebtedness excluded from gross income" numeric field |
| Line 3 (only if 1d) | "Do you elect to treat all real property described in section 1221(a)(1)..." Yes/No |
| Line 4 | Reduction of basis of depreciable property under §1017(b)(3)(F) |
| Line 6 | NOL reduction |
| Line 7 | General business credit reduction |
| Line 8 | Minimum tax credit reduction |
| Line 9 | Capital loss carryover reduction |
| Line 10a | Basis of property reduction (non-depreciable) |
| Line 10b | Basis of principal residence reduction |
| Line 11 | Passive activity loss/credit reduction |
| Line 12 | Foreign tax credit carryover reduction |
| Line 13 | Reserved |
| Line 14 | §108(b)(5) election (advanced — depreciable property basis first) |

4. **Run FFFF's "Check Form" tool** — flags missing required fields if a box is checked but Line 2 is zero, etc.
5. **Cross-check** every field against the SKILL plan's "Form 982 draft" section. If any disagrees, stop and recompute.
6. **Verify the 1040 Line 8 total** does NOT include the excluded amount. If FFFF shows the canceled debt as income on Line 8 even though Form 982 is filled, the user accidentally entered the excluded amount on Schedule 1 Line 8c. Remove it.

### What the agent should NOT do

- Do not file Form 982 without an actual exclusion — the IRS treats unsupported Form 982 filings as audit triggers
- Do not enter the canceled amount on both Schedule 1 Line 8c **and** Form 982 Line 2 — the amount goes on exactly one (Schedule 1 if taxable, Form 982 if excluded)
- Do not skip attribute reduction (Lines 6-12) just because the user has no NOLs — explicitly enter zeros and document "no attributes to reduce" in the plan

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| FFFF rejects "Form 982 missing Box 1 selection" | Filled Line 2 without checking 1a-1e | Check the appropriate box per SKILL plan |
| FFFF rejects "Schedule 1 Line 8c amount disagrees with 1099-C reported by creditor" | IRS matched their copy to user's reported amount | Confirm Box 2 amount; if Form 982 exclusion is being claimed, ensure it's on Form 982 not Schedule 1 |
| 1040 Line 8 includes canceled amount despite Form 982 | Double-reporting | Remove from Schedule 1 Line 8c if claiming full exclusion |
| Recipient doesn't have Form 982 in their FFFF return | Wasn't added | Use "Add a Form / Schedule" to add it before submitting |

---

## Section 2 — Generic tax-software pattern

For users with paid software (TurboTax, H&R Block, FreeTaxUSA, TaxSlayer, TaxAct, Cash App Taxes), the flow varies by provider but converges on:

1. Sign in → start or resume a return
2. Find the "Other income" or "1099-C / Cancellation of Debt" wizard. Most software has a dedicated 1099-C input screen.
3. Enter the 1099-C box-by-box from the form
4. The software asks "Was the debt discharged in bankruptcy?" or "Were you insolvent at the time of the cancellation?" — answer based on the SKILL plan's exclusion analysis
5. If insolvency is claimed, most software has an insolvency worksheet — fill it from the SKILL plan's liability/asset itemization
6. Software auto-generates Form 982 if an exclusion is claimed; verify the generated form matches the SKILL plan's "Form 982 draft"
7. Continue to 1040 review; confirm Schedule 1 Line 8c is zero (or only contains the unexcluded portion if partial)
8. Pay software fee; e-file

**Why this section is generic:** provider-specific selectors and wizard labels change yearly. Rely on visible label text, not DOM IDs.

---

## Section 3 — Paper filing

If filing on paper, assemble the return:

1. **Form 1040** (signed)
2. **Schedule 1** — if the canceled amount (or unexcluded portion) goes on Line 8c
3. **Schedule C** — if business 1099-C and reporting on Line 6
4. **Form 982** — if an exclusion is claimed (single page)
5. Other schedules in attachment-sequence order
6. W-2s and 1099s with federal withholding stapled to front of 1040

Mail to the IRS address for paper Form 1040 (with or without payment, by state):
https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

Send via USPS Certified Mail with Return Receipt for proof of timely filing under IRC §7502.

---

## Section 4 — Submission state machine

After filing, the return moves through:

1. **Submitted** — sent to IRS
2. **Accepted** — basic validation passed (e-file: 24-48 hours; paper: 4-8 weeks)
3. **Processed** — return fully ingested
4. Possible outcomes specific to 1099-C:
   - **Refund issued** — if the exclusion eliminated tax that was withheld elsewhere
   - **Balance due** — if the canceled amount was taxable
   - **CP2000 notice** — if the IRS's matching engine flags an unreported 1099-C; respond with copies of Form 982 and Pub 4681 Worksheet 2 if the exclusion was claimed

The most common 1099-C-related notice is **CP2000**. If the user receives one, follow Pub 4681 Chapter 1 response guidance — the user has 30 days to respond agreeing or disagreeing with the proposed change.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission
2. **Never store the user's SSN, DOB, PIN, or prior-year AGI** in agent logs, vector stores, or transcripts
3. **Never fabricate a Form 982 exclusion** — every box checked must be supported by the SKILL plan's analysis
4. **Always capture the post-submission acknowledgment** (FFFF submission ID or paper certified-mail receipt) in the user's records
5. **If FFFF rejects the return for an unfamiliar reason, stop** — don't retry blindly. Surface the rejection code and ask the user how to proceed.
