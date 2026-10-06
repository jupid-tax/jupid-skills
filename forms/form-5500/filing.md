# Filing Form 5500 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, Browserbase) can take a completed 5500 / 5500-SF / 5500-EZ draft and file it. This file describes deterministic flows. It's complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree, then execute channel-specific steps.

**Key difference from individual / employer tax forms**: Form 5500 / 5500-SF is filed with the **DOL via EFAST2** (Employee Benefits Security Administration's electronic filing system), not with the IRS. The data is shared among DOL, IRS, and PBGC. Form 5500-EZ is filed with the **IRS** on paper, or electronically through EFAST2 (plan years beginning after 2019). For plan years beginning on or after January 1, 2025, EFAST2 is mandatory for a filer required to file at least 10 returns of any type with the IRS during the calendar year (2025 Form 5500-EZ instructions; Treas. Reg. §301.6058-2).

---

## Channel decision tree

```
Form variant?
  → Form 5500 (full) or 5500-SF
    Channel: EFAST2 only (both forms must be filed electronically, 2025 instructions)
    Use Section 1 below.

  → Form 5500-EZ (one-participant plan or foreign plan)
    Ask: how many returns of any type (W-2s, 1099s, income, employment, excise tax returns)
         must the filer file with the IRS in the calendar year that includes the first day of the plan year?
      10 or more → EFAST2 required (a paper return is treated as not filed). Use Section 3.
      Fewer than 10 → user picks:
        a) Paper to the IRS in Ogden. Use Section 2.
        b) EFAST2. Use Section 3.
    Late return under the IRS Late Filer Penalty Relief Program (Rev. Proc. 2015-32) → paper only, Section 6.

Is the filer represented by a TPA (third-party administrator) or recordkeeper?
  → TPA files via EFAST2 with their own credentials
    Browser automation: TPA-specific dashboards
    Use Section 4 — handoff package; verify don't refile.
```

---

## Section 1 — EFAST2 for Form 5500 / 5500-SF

URL: https://www.efast.dol.gov

EFAST2 (ERISA Filing Acceptance System) is the DOL's electronic filing portal and the required channel for Form 5500 and Form 5500-SF.

### Pre-flight

Agent must have:

- The user's permission to log in / register on EFAST2 on their behalf
- Plan sponsor's full legal name and EIN
- Plan administrator's full name, EIN (if different from sponsor), and contact info
- The completed 5500 / 5500-SF draft from `SKILL.md` (with all schedules)
- For 5500 (large plan): the auditor's IQPA report as a PDF attachment
- A signing official (must have credentials — see below)
- A "filing author" (separate role; can be a TPA or self)

### EFAST2 credential setup

Sign-in to EFAST2 is through Login.gov (email, password, two-factor authentication). After the Login.gov sign-in, each person registers an EFAST2 profile, picks user types, and receives a User ID and a 4-digit PIN on the confirmation page; there is no postal-mail step (EFAST2 Guide for Filers and Service Providers, v4.0, Dec. 2, 2024).

1. **Filing Signer** — the plan administrator (or employer/plan sponsor, or an authorized service provider under the written-authorization option). User ID + PIN are the electronic signature.
2. **Filing Author** — the person who prepares and submits the filing in IFILE. Often the same person as the signer, or a TPA.
3. **Transmitter** — needed only when submitting through third-party software.

If credentials don't exist, the user registers personally; the agent never registers on the user's behalf and never handles the user's Login.gov second factor.

### Browser flow

The agent navigates and interacts deterministically. EFAST2 has a free browser-based filing application (**IFILE**); filings prepared in EFAST2-approved third-party software are transmitted from that software. Screen and tab names below are descriptive; follow the labels IFILE actually shows.

#### Option A — IFILE (browser form completion)

1. **Navigate** to https://www.efast.dol.gov
2. **Sign in** with Login.gov (the user completes the sign-in and second factor)
3. **Open** IFILE → **Start a new filing**
4. **Pick the plan year** and **form type** (5500 or 5500-SF)
5. **Pick the filing type**: First, Amended, Final, Short year
6. **Fill the form** — IFILE has tabs for each schedule. Fill from the draft:

| Section | IFILE tab | Source (in draft) |
|---------|-----------|-------------------|
| Header (sponsor, plan info) | "Plan Identification" | Header section of draft |
| Participants | "Participants" | Participant counts |
| Plan characteristics | "Plan Characteristics" | Plan codes |
| Financial info | "Schedule H" or "Schedule I" tab | Financial section |
| Insurance | "Schedule A" | If applicable |
| Service providers | "Schedule C" | If large plan, applicable |
| Master trust | "Schedule D" | If applicable |
| Financial transactions | "Schedule G" | If applicable |
| Retirement plan info | "Schedule R" | If applicable |
| DB actuarial | "Schedule SB" or "Schedule MB" | If DB plan |

7. **Attach IQPA audit report** (large plans) — upload PDF. Required for Schedule H.
8. **Attach Schedule SB** (single-employer defined benefit plans) completed and signed by the enrolled actuary, with its attachments.
9. **Run "Validate"** in IFILE — checks for missing fields, math errors, schedule consistency. Resolve every flag.
10. **Add signers** — enter the signing official's signer credentials (User ID + PIN). The signer can sign now or later via their own login.
11. **Submit**:
    - Click "Submit"
    - Confirmation receipt displayed (Acknowledgment ID — save this)

12. **Check the filing status**: EFAST2 should show a status within about 20 minutes. "Filing Received" means no errors or warnings were found; otherwise the status lists them. "Processing Stopped" or "Unprocessable" can mean the signature was invalid and the filing may be treated as not filed (2025 Form 5500 instructions, Signature and Date).

#### Option B — EFAST2-approved third-party software

If the user or TPA uses EFAST2-approved third-party software:

1. **Prepare** the filing in the software from the draft
2. **Run** the software's error check
3. **Sign** — the Filing Signer enters their EFAST2 User ID and PIN in the software
4. **Transmit** — the software submits to EFAST2 (the transmitting person needs the Transmitter user type if the software requires it)
5. **Check status** in the software or on the EFAST2 Submissions page

Software is common for large plans with a long Schedule H and Schedule of Assets. Ask the user whether a TPA or software is already in use before defaulting to IFILE.

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 11 / step 7
- Do not bypass IFILE validation even if it looks like a false positive (DOL parses heavily)
- Do not store the user's signer User ID + PIN together in any log
- Do not file 5500 / 5500-SF on paper; both must be filed electronically (only 5500-EZ has a paper option)
- Do not retry on a duplicate-filing error — file an amended return instead

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Filing already exists for this plan year" | Duplicate (TPA already filed) | File **amended** filing instead |
| "Plan number mismatch with prior year" | Plan number changed | DOL sends letter; verify plan number with prior 5500 |
| "Schedule H attachment missing" | Forgot IQPA report | Re-open filing, attach PDF, resubmit |
| "Signer credentials invalid" | Wrong PIN | Signer signs in with Login.gov and checks or changes the PIN under Your Account → Profile & PIN |
| Late deferrals reported (5500-SF line 10a / Schedule H or I line 4a) | Deposits missed the 29 CFR 2510.3-102 deadline | File Form 5330 with the IRS for the 15% excise tax unless VFCP + PTE 2002-51 relief applies |

---

## Section 2 — Paper filing (Form 5500-EZ only)

Form 5500-EZ can be paper-mailed to the IRS Ogden Service Center.

### Assemble the return

1. Print Form 5500-EZ from https://www.irs.gov/pub/irs-pdf/f5500ez.pdf — the revision matching the plan year (2025 form for plan years beginning in 2025)
2. Sign and date (employer or plan administrator); blue or black ink if completing by hand
3. One-sided pages, no notes, arrows, or glue (2025 Form 5500-EZ instructions, Filing Tips)

### Mailing address

Per current Form 5500-EZ instructions:

```
Department of the Treasury
Internal Revenue Service
Ogden, UT 84201-0020
```

Private delivery service (IRS-designated PDS only):

```
Internal Revenue Submission Processing Center
1973 Rulon White Blvd.
Ogden, UT 84201
```

Verify each year against https://www.irs.gov/pub/irs-pdf/i5500ez.pdf — addresses occasionally update.

### Mailing best practices

- USPS Certified Mail with Return Receipt
- Postmark by **last day of 7th month after plan year end** (calendar plan = July 31). If extension via Form 5558 was filed timely, postmark by extended date (October 15 for calendar plan).
- Keep a complete photocopy
- The IRS does not send a receipt for a paper 5500-EZ. Keep the certified-mail or PDS proof of mailing. (CP216F is the notice approving a Form 5558 extension, not a receipt for the return.)

### Producing the printable PDF

1. Download latest Form 5500-EZ revision from https://www.irs.gov/pub/irs-pdf/f5500ez.pdf
2. Open in fillable PDF tool
3. Map draft values to the PDF's field names; read them from the current PDF each year, since field names can change between revisions
4. Save as flattened PDF for printing

---

## Section 3 — EFAST2 for Form 5500-EZ (electronic option)

For plan years beginning after 2019, a one-participant plan or foreign plan can file Form 5500-EZ electronically through EFAST2 instead of on paper; for plan years beginning on or after January 1, 2025 it must, if the filer is required to file 10 or more returns of any type with the IRS during the calendar year (2025 Form 5500-EZ instructions).

Same browser flow as Section 1 (IFILE), with form-type "5500-EZ" selected. The signer needs an EFAST2 User ID and PIN (Login.gov sign-in). Do not file Schedule SB or MB electronically with a 5500-EZ; keep them in the plan records.

A delinquent 5500-EZ submitted under the Late Filer Penalty Relief Program cannot go through EFAST2 (Section 6).

---

## Section 4 — TPA / recordkeeper handoff

If the user has a Third-Party Administrator (TPA) or recordkeeper (Fidelity, Vanguard, T. Rowe Price, Schwab, Empower, Guideline, Human Interest, ForUsAll, etc.) handling 5500, the agent's role:

1. **Verify** the TPA has the correct plan year on file
2. **Pull the filed 5500 PDF** from the TPA's plan portal (often labeled "Annual Report", "5500 Filing", or "Compliance")
3. **Cross-check** against the draft from `SKILL.md`. Surface any disagreements.
4. **Do NOT refile** if the TPA filed already
5. If the TPA's filing is wrong, **file an amended 5500** — coordinate with the TPA so they update their records too

Common recordkeeper portals (subject to change):

- Fidelity NetBenefits Plan Sponsor: psw.fidelity.com → Compliance & filings
- Vanguard Retirement Plan Access: vanguard.com → My plan → Compliance
- Schwab Retirement Plan Services: workplace.schwab.com → Reports → Annual filings
- Guideline: my.guideline.com → Compliance → Form 5500
- Human Interest: humaninterest.com → Plan documents → Filings

---

## Section 5 — Submission state machine

After filing (any channel):

1. **Submitted** — sent to EFAST2 / IRS Ogden
2. **Filing status** — EFAST2: about 20 minutes, "Filing Received" or a list of errors/warnings; paper 5500-EZ: no receipt is sent
3. **Processed** — the filing may still get further review by DOL, IRS, or PBGC
4. **Notice issued** OR **No further action**

Possible notices (irs.gov notice pages):

- **CP216F** (IRS) — Form 5558 extension approved
- **CP403 / CP406** (IRS) — first and second delinquency notices for a missing Form 5500 or 5500-SF
- **CP283** (IRS) — penalty charged for a late or incomplete Form 5500-EZ
- **DOL letter** for missing schedules, late deferrals, or audit issues
- **PBGC notice** (defined benefit only) — premium issues

Status checks:

- EFAST2: Submissions page after signing in, or the EFAST2 Help Desk automated line, 1-866-GO-EFAST (1-866-463-3278)
- IRS employee plans help line: 877-829-5500 (also for Form 5558 receipt questions)
- EBSA: 1-866-444-EBSA (3272)
- PBGC coverage questions: 1-800-736-2444

The agent should set a follow-up reminder for the day after an EFAST2 submission to confirm "Filing Received".

---

## Section 6 — DFVC (Delinquent Filer Voluntary Compliance)

If the user is filing late and DOL has not yet sent a notice, they can use DFVC to dramatically reduce penalties:

- DFVC penalty: $10/day; small plans capped at $750 per filing and $1,500 per plan ($750 per plan if the sponsor is a 501(c)(3) organization); large plans capped at $2,000 per filing and $4,000 per plan
- Not available after DOL issues a Notice of Intent to Assess a Penalty, for amended filings, or for 5500-EZ / one-participant plans
- Without DFVC: up to $2,739/day per ERISA §502(c)(2) (2025 adjustment; DOL made no 2026 adjustment, 91 FR 31358)

DFVC requires:
1. File each late Form 5500 or 5500-SF via EFAST2 with the DFVC box checked (Form 5500 line D, Form 5500-SF line C) AND
2. Pay through the DOL's online DFVC calculator and payment system at https://www.askebsa.dol.gov/dfvcepay/ (DOL no longer accepts paper submissions or payments)

Source: https://www.dol.gov/agencies/ebsa/employers-and-advisers/plan-administration-and-compliance/correction-programs/dfvcp

For 5500-EZ, DFVC does NOT apply. Use the IRS **Late Filer Penalty Relief Program** (Rev. Proc. 2015-32):
- $500 per delinquent return, maximum $1,500 per submission for one plan; check payable to the United States Treasury
- Paper Form 5500-EZ only (not EFAST2); check box D on the 2025 form, or for older years print "Delinquent Return Submitted under Rev. Proc. 2015-32, Eligible for Penalty Relief" in red in the top margin
- Form 14704 attached to the front of the oldest delinquent return
- Mail to: Internal Revenue Service, 1973 North Rulon White Blvd., Ogden, UT 84404-0020
- Not available once a CP283 penalty notice has been issued for that return

See [`references/common-mistakes.md`](./references/common-mistakes.md) (mistake 3) for the penalty context.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Form 5500 / 5500-SF / 5500-EZ for plan year [YYYY] right now" must be captured.
2. **Never store EFAST2 signer credentials** (User ID + PIN) in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** If EFAST2 / IRS asks for proof, pause and let the user respond directly.
4. **Always capture submission confirmations** as screenshots stored under the user's account, not the agent's.
5. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures, validation errors), **stop and surface the issue**. Don't retry blindly.
6. **Pre-submission diff**: show the user a side-by-side of the draft vs. what's about to be submitted. Get explicit OK before clicking submit.
7. **Audit report attachments**: handle with care. Filings and attachments are published on the internet; an attachment showing a Social Security number, or any part of one, can cause rejection (2025 Form 5500 and 5500-SF instructions). Check every PDF before submission and redact SSNs.
