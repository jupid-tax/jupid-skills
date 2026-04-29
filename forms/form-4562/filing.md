# Filing Form 4562 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, or a hosted browser like Browserbase) can take a completed Form 4562 draft and file it with the related income tax return. Form 4562 never files standalone — it attaches to Form 1040 (with Schedule C/E/F), Form 1120, Form 1120-S, or Form 1065.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

```
Filer is a sole prop / SMLLC with Schedule C?
  → Form 4562 attaches to Form 1040; choose 1040 channel:
    - Free File Fillable Forms (FFFF) if user wants to fill directly
    - Paid software (TurboTax, FreeTaxUSA, H&R Block) if already paying
    - Paper if FFFF closed or user prefers
  → Use Section 1 below (FFFF flow) or Section 2 (generic software)

Filer is a partnership (Form 1065)?
  → FFFF does not support Form 1065. Use paid software (Drake, Lacerte,
    UltraTax, ProSeries, FreeTaxUSA Business) or paper.
  → Use Section 2 (generic software) or Section 3 (paper)

Filer is an S-corp (Form 1120-S)?
  → Same as 1065 — FFFF does not support 1120-S. Paid software or paper.
  → Use Section 2 or Section 3

Filer is a C-corp (Form 1120)?
  → Same as 1120-S — FFFF does not support 1120. Paid software or paper.

User wants IRS Direct File?
  → As of early 2026, IRS Direct File does NOT support Schedule C with
    depreciation (Line 13). Form 4562 is therefore unsupported. Redirect to
    FFFF or paid software.
```

---

## Section 1 — IRS Free File Fillable Forms (FFFF) for Form 1040 + Schedule C + Form 4562

URL: https://www.irs.gov/e-file-providers/free-file-fillable-forms

**Availability**: late January through mid-October each year. Outside that window, FFFF returns "season closed".

**Account model**: each tax year is a separate FFFF account.

### Pre-flight

The agent must have:

- The user's permission to log in / register on their behalf
- Filer's full legal name, SSN, date of birth, mailing address, prior-year AGI
- The completed Form 4562 draft from `SKILL.md`
- The completed Schedule C (or other related schedule) draft
- Form 1040 base inputs (filing status, dependents, W-2s, etc.)
- Email address the user controls

### Browser flow

1. **Navigate** to https://www.irs.gov/e-file-providers/free-file-fillable-forms and click "Start Free File Fillable Forms"
2. **Sign in / register** (current tax year account)
3. **Identity verification** via prior-year AGI or self-select PIN
4. **Start a new return** → Form 1040 landing
5. **Fill 1040 header**, then add Schedule C (see schedule-c skill's `filing.md` for that flow)
6. **Add Form 4562**:
   - Click "Add a Form / Schedule"
   - Search "4562" or pick from the form list
   - Form 4562 opens with field labels matching the paper form
7. **Fill Form 4562 from the draft** — field-by-field mapping:

| Form 4562 line | FFFF field label | Source (in draft) |
|----------------|------------------|-------------------|
| Name(s) shown on return | "Name(s) shown on return" | Header |
| Identifying number | "Identifying number" | Header SSN/EIN |
| Business or activity | "Business or activity to which this form relates" | Header activity |
| **Part I §179** | | |
| 1 | "Maximum amount" | Line 1 ($1,250,000 for 2025) |
| 2 | "Total cost of section 179 property" | Line 2 |
| 3 | "Threshold cost of section 179 property" | Line 3 ($3,130,000 for 2025) |
| 4 | (auto-computed) | (verify equals draft Line 4) |
| 5 | (auto-computed) | (verify) |
| 6 | "(a) Description / (b) Cost / (c) Elected cost" — repeat row | Each Line 6 row |
| 7 | "Listed property... from line 29" | Line 7 |
| 8 | (auto-computed) | (verify) |
| 9 | (auto-computed) | (verify) |
| 10 | "Carryover of disallowed deduction from line 13 of prior year" | Line 10 |
| 11 | "Business income limitation" | Line 11 |
| 12 | (auto-computed) | (verify) |
| 13 | (auto-computed) | (verify) |
| **Part II Bonus** | | |
| 14 | "Special depreciation allowance for qualified property" | Line 14 |
| 15 | "Property subject to section 168(f)(1)" | Line 15 |
| 16 | "Other depreciation" | Line 16 |
| **Part III MACRS** | | |
| 17 | "MACRS deductions for assets placed in service in tax years before [current]" | Line 17 |
| 18 | "If you are electing to group any assets..." | Line 18 checkbox |
| 19a–19i | One row per asset class with (b) month/yr, (c) basis, (d) recovery period, (e) convention, (f) method, (g) deduction | Each Line 19 row |
| 20a–20d | ADS rows | Each Line 20 row |
| **Part IV Summary** | | |
| 21 | "Listed property... from line 28" | Line 21 |
| 22 | (auto-computed) | (verify) |
| 23 | "For assets shown above and placed in service during the current year..." | Line 23 |
| **Part V Listed Property** | | |
| 24a | "Do you have evidence to support the business/investment use claimed?" Yes/No | 24a |
| 24b | "If 'Yes,' is the evidence written?" Yes/No | 24b |
| 25 | "Special depreciation allowance for qualified listed property" | Line 25 |
| 26 | "Property used more than 50% in a qualified business use" — repeat per asset | Each row |
| 27 | "Property used 50% or less in a qualified business use" — ADS only | Each row |
| 28 | (auto-computed) | (verify, → Line 21) |
| 29 | (auto-computed) | (verify, → Line 7) |
| 30a–30c | "Total business / commuting / other personal miles driven during the year" per vehicle | Per vehicle |
| 31–36 | Yes/No questions per vehicle | Per vehicle |
| **Part VI Amortization** | | |
| 42 | One row per current-year intangible: (a) description, (b) date begins, (c) cost, (d) IRC code, (e) period, (f) deduction | Each row |
| 43 | "Amortization of costs that began before [current year]" | Line 43 |
| 44 | (auto-computed = Line 42 + 43) | (verify) |

8. **Cross-check** every auto-computed field against the draft. If FFFF disagrees with the draft, **stop**; one is wrong.
9. **Verify Line 22 flows correctly to Schedule C Line 13** (or Schedule E / F / corporate equivalent). FFFF should auto-link; if not, manually re-enter Schedule C Line 13 to match Form 4562 Line 22.
10. **Run FFFF's "Check Form" / "Verify" tool**. Resolve every flag.
11. **Attach bonus opt-out election statement** if applicable (FFFF supports an "Additional Statements" attachment area or a PDF upload).
12. **Save**, then continue with the rest of the 1040.
13. **E-file** when the entire return is verified — sign with self-select PIN + prior-year AGI.

### What the agent should NOT do

- Do not submit Form 4562 alone — it must accompany the income tax return
- Do not bypass FFFF's verification tool
- Do not file if the user has already filed for the tax year
- Do not store SSN, DOB, or PIN in any log
- Do not silently "fix" Line 22 vs. Schedule C Line 13 mismatches — surface to the user

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Line 22 ≠ Schedule C Line 13 | Numbers entered separately and don't match | Re-derive both from the draft |
| "§179 exceeds business income" | Line 11 < Line 9 + Line 10 | Reduce Line 6 elected amount or accept carryforward |
| Bonus depreciation rejected by FFFF | Asset class ineligible (e.g., 39-year nonresidential not QIP) | Move to MACRS only |
| §280F cap reduced auto deduction silently | FFFF applied luxury cap; user expected full deduction | Verify draft applied caps; adjust expectations |
| "Listed property substantiation" warning | Lines 24a/24b answered "No" | If user has no evidence, deduction is at audit risk; let user decide |

---

## Section 2 — Generic tax-software pattern

For users with paid software (TurboTax, H&R Block, FreeTaxUSA, TaxAct, Drake Tax, ProSeries, Lacerte, UltraTax):

1. Sign in → start or resume the return
2. Navigate to "Assets" / "Depreciation" / "Section 179" section
3. The software asks for each asset:
   - Description
   - Date placed in service
   - Cost or basis
   - Business-use %
   - Asset category (it picks recovery period / class)
   - Election: §179 / bonus / MACRS / opt out of bonus
4. Software computes Form 4562 in the background and places Line 22 into Schedule C Line 13 / Schedule E Line 18 / etc.
5. Most software has a "Form 4562 review" screen — verify each line against the draft.
6. Override anything that disagrees. If you don't know which one is right, stop and consult the IRS instructions.
7. Continue through the rest of the return.

**Why this section is generic**: provider-specific selectors and wizard flows change every tax year. The agent should rely on visible labels and human-readable navigation, not DOM IDs.

---

## Section 3 — Paper filing

### Assemble the return

The IRS expects this stack from top to bottom for a sole prop with depreciation:

1. **Form 1040** (signed)
2. **Schedule 1, 2, 3** in order if applicable
3. **Schedule C** (signed)
4. **Schedule SE** (if Schedule C Line 31 > $400)
5. **Form 4562** (because Schedule C Line 13 > 0)
6. **Form 8829** (if home office regular method)
7. **Other schedules and forms** in attachment-sequence order printed top-right of each form
8. **W-2 Copy B** stapled to front lower-left of Form 1040

For partnerships, the order changes — Form 1065 with K-1s replaces Form 1040; Form 4562 attaches per-activity.

### Mailing addresses

Vary by tax form, payment status, and state. Look up at:

https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment

Do not hardcode addresses.

### Producing the printable PDF

1. Download the latest Form 4562 PDF from https://www.irs.gov/pub/irs-pdf/f4562.pdf
2. Open in a PDF tool that supports form filling
3. Map draft values to PDF field names (stable on IRS forms)
4. Save as flattened PDF

For multi-asset Form 4562s, the form supports overflow: Lines 6, 19, 26, 27, 42 each accept multiple rows. If asset count exceeds the rows printed, attach a continuation statement labeled "Form 4562 Line [N] continuation" with the same column structure.

---

## Section 4 — Bonus depreciation opt-out election

If the user elects out of bonus depreciation under IRC §168(k)(7), the agent must:

1. Identify the asset class for which the election applies (3-year, 5-year, 7-year, 10-year, 15-year, 20-year, or qualified improvement property — election is per class, applies to *all* assets in that class placed in service in the year)
2. Prepare a written statement attached to the timely-filed return that says:
   - "Taxpayer [name, ID number] elects out of the additional first-year depreciation allowance under IRC §168(k)(7) for the following classes of property placed in service during tax year [year]: [list classes]."
3. The election is irrevocable without IRS consent (Rev. Proc. requirement; verify current process).
4. On Form 4562, do not enter bonus depreciation on Line 14 for property in the elected-out class.
5. MACRS Section A applies normally to the assets.

---

## Section 5 — §179 carryforward tracking

The §179 deduction is limited to the user's aggregate active business income. Excess carries forward.

The agent must:
- Note Line 13 (carryover to next year) in the draft and the user's records
- Tell the user this is **per-taxpayer**, not per-business — so a sole prop with multiple Schedule Cs aggregates income across all of them
- Include the carryover on next year's Form 4562 Line 10
- The carryover is also subject to next year's income limit; if income remains low, it can carry forward again

---

## Section 6 — Submission state machine

After filing the return that includes Form 4562:

1. **Submitted** — sent to IRS
2. **Accepted** — basic validation passed (within 24–48 hours for e-file; 4–8 weeks for paper)
3. **Processed** — full ingest
4. **Notice or refund** — possible CP2000 if Form 4562 doesn't reconcile with the related schedule

Status checks:
- E-file confirmation: usually within 48 hours
- Account transcript: https://www.irs.gov/individuals/get-transcript

The agent should set a follow-up reminder 7 days post-submission.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. Capture: "I authorize you to file Form [1040/1120/etc.] including Form 4562 on my behalf right now."
2. **Never store SSN, DOB, EIN, or PIN** in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.**
4. **Always capture submission confirmations** as screenshots stored under the user's account.
5. **Never silently adjust Line 22 vs. Schedule C Line 13 mismatches** — these signal a draft error; surface to the user.
6. **Never auto-elect bonus opt-out** without explicit user instruction — it's irrevocable.
7. **If the user's mileage log is missing or incomplete** for a vehicle on Part V, flag it before submission. The agent should not file on the user's behalf if the listed-property substantiation question (24b) is being answered untruthfully.
