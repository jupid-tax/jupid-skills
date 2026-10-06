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

Recipient wants IRS Free File guided software (AGI $89,000 or less)?
  → Start at IRS.gov/FreeFile; check the partner supports Form 982 before starting.
    https://www.irs.gov/filing/irs-free-file-do-your-taxes-for-free

IRS Direct File was not offered in the 2026 filing season; do not route users to it.
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF)

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

Same authentication and pre-flight requirements as the Schedule C filing playbook: an account for the current filing year, an email address and a 10-digit U.S. cell phone for SMS, prior-year AGI or self-select PIN. FFFF prepares a federal return only and, for 2025 returns, closes Oct. 15, 2026 (FFFF page). It works for any income level.

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

**Nonfarm rental real property debt — Schedule E:**

| SKILL plan field | FFFF location |
|------------------|---------------|
| Reporting target = Schedule E Line 3 | Open Schedule E, add the canceled amount to Line 3 for that property (Pub. 4681) |

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
| Line 3 | §1017(b)(3)(E) election: "Do you elect to treat all real property described in section 1221(a)(1)... as if it were depreciable property?" Yes/No (not for QRPBI; consumers leave it) |
| Line 4 | QRPBI (box 1d) applied to reduce basis of depreciable real property |
| Line 5 | §108(b)(5) election to reduce basis of depreciable property first |
| Line 6 | NOL reduction |
| Line 7 | General business credit carryover reduction |
| Line 8 | Minimum tax credit reduction |
| Line 9 | Net capital loss and carryover reduction |
| Line 10a | Basis of nondepreciable and depreciable property (nonbusiness debt: smallest of the three amounts in the Form 982 instructions) |
| Line 10b | Basis of principal residence (box 1e only, home still owned) |
| Lines 11a-11c | Qualified farm indebtedness basis reductions |
| Line 12 | Passive activity loss and credit carryover reduction |
| Line 13 | Foreign tax credit carryover reduction |
| Part III | Corporate consent under §1081(b) — individuals leave it blank |

4. **Run FFFF's "Check Form" tool** — flags missing required fields if a box is checked but Line 2 is zero, etc.
5. **Cross-check** every field against the SKILL plan's "Form 982 draft" section. If any disagrees, stop and recompute.
6. **Verify the 1040 Line 8 total** does NOT include the excluded amount. If FFFF shows the canceled debt as income on Line 8 even though Form 982 is filled, the user accidentally entered the excluded amount on Schedule 1 Line 8c. Remove it.

### What the agent should NOT do

- Do not file Form 982 without an actual exclusion — the IRS treats unsupported Form 982 filings as audit triggers
- Do not enter the canceled amount on both Schedule 1 Line 8c **and** Form 982 Line 2 — the amount goes on exactly one (Schedule 1 if taxable, Form 982 if excluded)
- Do not skip attribute reduction (Lines 6-13) just because the user has no NOLs — compute Line 10a for a nonbusiness debt, enter zeros where there is nothing, and document it in the plan

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| FFFF rejects "Form 982 missing Box 1 selection" | Filled Line 2 without checking 1a-1e | Check the appropriate box per SKILL plan |
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
   - **CP2000 notice** — if the IRS's matching engine flags an unreported 1099-C; respond with copies of Form 982 and the Pub. 4681 Insolvency Worksheet if the exclusion was claimed

The most common 1099-C-related notice is **CP2000**. If the user receives one, respond by the date on the notice, agreeing or disagreeing with the proposed change (https://www.irs.gov/individuals/understanding-your-cp2000-notice).

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission
2. **Never store the user's SSN, DOB, PIN, or prior-year AGI** in agent logs, vector stores, or transcripts
3. **Never fabricate a Form 982 exclusion** — every box checked must be supported by the SKILL plan's analysis
4. **Always capture the post-submission acknowledgment** (FFFF submission ID or paper certified-mail receipt) in the user's records
5. **If FFFF rejects the return for an unfamiliar reason, stop** — don't retry blindly. Surface the rejection code and ask the user how to proceed.
