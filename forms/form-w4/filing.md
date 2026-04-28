# W-4 Filing Playbook (Browser Automation)

This playbook covers how an agent submits a completed W-4 draft on the user's behalf via common payroll platforms or paper. Load this only when the user has produced a W-4 draft (per `SKILL.md`) AND has explicitly authorized submission.

The W-4 is **not filed with the IRS** — it goes to the employer's payroll system. The employer keeps it on file and uses it for paycheck withholding calculations.

---

## Decision Tree: Pick the Right Channel

```
START
│
├─ Does the user have a payroll platform (Workday, Gusto, ADP, etc.)?
│   ├─ YES → Identify which platform → use platform-specific section below
│   └─ NO  → Continue
│
├─ Does HR provide an electronic onboarding portal?
│   ├─ YES → Use the HR portal (BambooHR, Rippling, Paychex Flex, etc.)
│   └─ NO  → Continue
│
└─ Paper W-4 (PDF, hand-deliver or scan)
```

The most common 2026 channels, in rough order:

1. **Workday** (large enterprises, 10K+ employees)
2. **Gusto** (SMBs, 1-500 employees)
3. **ADP Workforce Now / RUN** (mid-market and enterprise)
4. **Paychex Flex** (SMB)
5. **BambooHR** (mid-market)
6. **Rippling** (mid-market tech)
7. **Justworks** (PEO, small businesses)
8. **Paper** (PDF download from irs.gov, sign, hand to HR)

---

## Pre-Flight Checklist

Before starting the submission, the agent must have:

- [ ] Completed W-4 draft from `SKILL.md` workflow (all five steps)
- [ ] User's payroll-platform credentials (the user should authenticate themselves; agent does NOT store passwords)
- [ ] User's employee ID (sometimes shown on prior pay stub or onboarding email)
- [ ] User's electronic-signature consent — the platform will ask "I authorize this form" — agent must NOT click without explicit user OK
- [ ] User's effective-date preference: most platforms apply changes to the next pay period; ask if the user wants to delay
- [ ] Confirmation that the user understands: the new withholding will appear on the next pay stub after the platform processes it (1-2 pay periods)

---

## Channel: Workday

URL: `https://<company>.myworkday.com`

Path:
1. Log in (user authenticates, agent does NOT touch credentials)
2. Click profile menu → "Pay" → "Withholding Elections"
3. Click "Update" next to "Federal Withholding" → "Use 2020 W-4 Form" (default for 2026 forms)
4. Fill out:
   - Filing status (Step 1(c))
   - Multiple Jobs Indicator (Step 2(c) checkbox if applicable)
   - Dependents — children under 17 amount + other dependents amount (Step 3)
   - Other income (Step 4(a))
   - Deductions (Step 4(b))
   - Additional withholding (Step 4(c))
5. Review summary screen — agent should pause here and show the user the entries before submitting
6. Click "Submit" → e-signature consent → confirmation screen
7. Verify the new Federal Withholding shows in the user's profile

Effective: usually next pay period, but Workday lets users set a future effective date.

## Channel: Gusto

URL: `https://app.gusto.com`

Path:
1. Log in (employee account, not employer admin)
2. Click "Profile" in the top-right → "Tax Withholdings"
3. Click "Edit" on "Federal income tax withholding"
4. Wizard:
   - Filing status
   - Multiple jobs question (Step 2)
   - Dependents wizard (Step 3 broken into "qualifying children" and "other dependents")
   - Other adjustments (Step 4(a)/(b)/(c))
5. Click "Save changes" → e-signature → confirmation
6. Gusto auto-emails the employer's payroll admin

Effective: applies to the next pay run.

## Channel: ADP Workforce Now / RUN

URL: `https://workforcenow.adp.com` or `https://runpayroll.adp.com`

Path:
1. Log in (employee self-service)
2. "Myself" → "Pay" → "Tax Withholdings"
3. Click "Federal" → "Edit"
4. ADP often uses a stepper UI matching the IRS W-4 step numbers
5. Step 1, Step 2 (with toggle for "I have multiple jobs"), Step 3 (with calculator), Step 4 (with three sub-fields)
6. "Save" → e-signature → ADP returns a PDF receipt
7. Save the receipt PDF to the user's records

ADP RUN (small business) is similar but with fewer fields per page.

## Channel: Paychex Flex

URL: `https://myapps.paychex.com`

Path:
1. Log in
2. "Personal Info" → "Tax Information"
3. "Federal Tax Withholding" → "Update"
4. Fill the W-4 step fields (Paychex matches IRS step numbering exactly)
5. Submit → e-signature → PDF download

## Channel: BambooHR

URL: `https://<company>.bamboohr.com`

BambooHR routes the W-4 update through "My Info" → "Documents" → "W-4" → "Update". The system actually generates an IRS-format PDF for the user to e-sign. Agent must verify the PDF matches the draft before signing.

## Channel: Rippling

URL: `https://app.rippling.com`

Path: "Me" → "Tax info" → "Federal W-4" → "Update". Rippling validates the math (e.g., warns if Step 3 amount looks off given dependent count entered).

## Channel: Justworks

URL: `https://secure.justworks.com`

Path: "My Info" → "Tax Withholdings" → "Federal W-4" → "Edit". Justworks requires re-authentication before submitting tax form changes.

## Channel: Paper

If no electronic platform exists:
1. Download the latest W-4 PDF from `https://www.irs.gov/pub/irs-pdf/fw4.pdf`
2. Open in a PDF editor (Preview, Adobe Acrobat, browser PDF) — most modern PDFs allow form fill
3. Fill the five steps from the draft
4. Sign (digital signature in the PDF, or print + sign + scan)
5. Email or hand to HR / payroll contact
6. Confirm receipt — request HR confirm the new withholding will apply starting on `<date>`

---

## Submission State Machine

```
Draft → Submitted → Acknowledged → Effective → Verified
```

- **Draft**: produced by the SKILL.md workflow, not yet sent
- **Submitted**: agent (or user) clicked "Submit" / signed the PDF / handed to HR
- **Acknowledged**: payroll platform shows the new W-4 in the user's profile (instant on most platforms; up to 24h on legacy systems)
- **Effective**: payroll has applied the change to a pay run (usually next pay period)
- **Verified**: agent compares the next pay stub's federal withholding amount against the projected number from SKILL.md output. If within ±5%, verified. If off by more than 10%, investigate (common cause: payroll set a future effective date, or the user's wages changed).

---

## Security Rules

These rules are absolute — no exceptions.

1. **Never persist the user's SSN, DOB, or PIN beyond the immediate session.** Use only in-memory references during the submission flow.
2. **Never auto-click "Submit" or "Sign" without explicit user consent at the moment of submission.** Even if the user authorized "filing the W-4" earlier, ask one more time at the point of irreversible signature: "About to submit. Confirm with 'yes' to proceed."
3. **Show a diff between the draft and the platform's pre-submission summary screen.** If they don't match, stop and surface the discrepancy.
4. **Save a PDF receipt of the submission.** Most platforms generate one; if not, take a full-page screenshot of the confirmation screen.
5. **Don't submit on the user's behalf if you don't have their direct credentials access.** If the user logged in themselves and handed over the session, that's fine; if you're being asked to type their password, refuse.
6. **Verify the platform domain matches the user's employer.** Phishing W-4 forms exist — confirm the URL is `*.workday.com`, `*.gusto.com`, `*.adp.com`, etc., and matches the user's actual employer.

---

## Common Submission Failures

- **"Multiple W-4s on file" warning.** Some platforms keep historical W-4s. The new one supersedes; the warning is informational. Continue.
- **"Filing status mismatch with state form" warning.** Federal W-4 filing status differs from state withholding form (e.g., CA DE-4). Resolve the state form separately — out of scope for this skill.
- **"E-signature not enrolled."** User must enroll in the platform's e-sign first (one-time setup, usually 2-3 minutes). Pause and let the user complete enrollment, then resume.
- **"Withholding allowance number invalid."** Older platforms still expect the pre-2020 W-4 with allowances. Switch the platform to the 2020+ W-4 format if available, or contact payroll admin for help.
- **"Effective date in the past."** Some platforms reject backdated effective dates. Set effective to "next pay period" instead.
