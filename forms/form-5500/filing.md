# Filing Form 5500 (browser automation)

How an agent equipped with browser tooling (Playwright, Puppeteer, Selenium, Browserbase) can take a completed 5500 / 5500-SF / 5500-EZ draft and file it. This file describes deterministic flows. It's complementary to `SKILL.md`, which produces the draft.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a filing channel from the decision tree, then execute channel-specific steps.

**Key difference from individual / employer tax forms**: Form 5500 / 5500-SF is filed with the **DOL via EFAST2** (Employee Benefits Security Administration's electronic filing system), not with the IRS. The data is shared among DOL, IRS, and PBGC. Form 5500-EZ is filed with the **IRS** — paper or, since plan year 2020, optional electronic filing via the IRS portal.

---

## Channel decision tree

```
Form variant?
  → Form 5500 (full) or 5500-SF
    Channel: EFAST2 (electronic only — paper rejected for 5500/5500-SF since 2010)
    Use Section 1 below.

  → Form 5500-EZ (one-participant plan)
    Channel options:
      a) Paper-mail to IRS Ogden — traditional, reliable
      b) Electronic via EFAST2 (5500-EZ option launched 2021)
    User picks; default to paper for first-time filers (less credentialing overhead).
    Use Section 2 (paper) or Section 3 (5500-EZ via EFAST2).

Is the filer represented by a TPA (third-party administrator) or recordkeeper?
  → TPA files via EFAST2 with their own credentials
    Browser automation: TPA-specific dashboards
    Use Section 4 — handoff package; verify don't refile.
```

---

## Section 1 — EFAST2 for Form 5500 / 5500-SF

URL: https://www.efast.dol.gov

EFAST2 (ERISA Filing Acceptance System) is the DOL's electronic filing portal. It's been the **only** way to file 5500 / 5500-SF since plan year 2009.

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

EFAST2 has two credential types:

1. **Signer credentials** — the plan administrator (or designated signer) needs these to sign the filing. Apply at https://www.efast.dol.gov via the "Register" button. Receive a "User ID" and "PIN" by email + postal mail.
2. **Filer credentials** — the person submitting the form. Often same as signer, or could be a TPA / agent.

If credentials don't exist:
- Apply for signer credentials **at least 2 weeks before filing**. The PIN is mailed via USPS to verify identity.
- Filer credentials are issued faster (online).

### Browser flow

The agent navigates and interacts deterministically. EFAST2 has a browser-based form-completion tool (called **IFILE**) and supports XML upload for software-prepared filings.

#### Option A — IFILE (browser form completion)

1. **Navigate** to https://www.efast.dol.gov
2. **Sign in** with filer credentials
3. **Click** "IFILE" → **Start a new filing**
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
8. **Attach plan opinion letter** (defined benefit only) — required for Schedule SB.
9. **Run "Validate"** in IFILE — checks for missing fields, math errors, schedule consistency. Resolve every flag.
10. **Add signers** — enter the signing official's signer credentials (User ID + PIN). The signer can sign now or later via their own login.
11. **Submit**:
    - Click "Submit"
    - Confirmation receipt displayed (Acknowledgment ID — save this)

12. **Wait for processing**: EFAST2 processes filings in real time. Acceptance status appears within minutes. Failures show specific error codes.

#### Option B — XML upload (software-prepared)

If the user has software (Datair, ftwilliam.com, Relius, FT William, etc.) that produces an EFAST2-format XML file:

1. **Navigate** to https://www.efast.dol.gov
2. **Sign in** with filer credentials
3. **Click** "Upload" → "EFAST2-Compliant Filing"
4. **Browse** to the XML file, upload
5. **Validate** server-side — EFAST2 checks the XML against its schema
6. **Sign** via signer credentials
7. **Submit**

XML upload is faster for large plans with complex Schedule H / Schedule of Assets. Ask the user if they have such a file ready before defaulting to IFILE.

### What the agent should NOT do

- Do not submit without the user's explicit go-ahead at step 11 / step 7
- Do not bypass IFILE validation even if it looks like a false positive (DOL parses heavily)
- Do not store the user's signer User ID + PIN together in any log
- Do not file 5500 / 5500-SF on paper — paper is rejected since 2010 (only 5500-EZ accepts paper)
- Do not retry on a duplicate-filing error — file an amended return instead

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "Filing already exists for this plan year" | Duplicate (TPA already filed) | File **amended** filing instead |
| "Plan number mismatch with prior year" | Plan number changed | DOL sends letter; verify plan number with prior 5500 |
| "Schedule H attachment missing" | Forgot IQPA report | Re-open filing, attach PDF, resubmit |
| "Signer credentials invalid" | Wrong PIN | Reset via EFAST2 (takes 1–2 weeks for re-mailing) |
| "Plan participant count anomaly" | Year-over-year participant count change > X% | Provide explanation in Schedule H comments or attached PDF |
| "Late deferrals reported but no Form 5330 filed" | DOL hot button | File Form 5330 separately to pay 15% excise tax |

---

## Section 2 — Paper filing (Form 5500-EZ only)

Form 5500-EZ can be paper-mailed to the IRS Ogden Service Center.

### Assemble the return

1. Print Form 5500-EZ from https://www.irs.gov/pub/irs-pdf/f5500ez.pdf — most recent revision matching the plan year
2. Sign in ink (plan administrator)
3. Single-side print, full-size letter

### Mailing address

Per current Form 5500-EZ instructions:

```
Department of the Treasury
Internal Revenue Service
Ogden, UT 84201-0027
```

Verify each year against https://www.irs.gov/pub/irs-pdf/i5500ez.pdf — addresses occasionally update.

### Mailing best practices

- USPS Certified Mail with Return Receipt
- Postmark by **last day of 7th month after plan year end** (calendar plan = July 31). If extension via Form 5558 was filed timely, postmark by extended date (October 15 for calendar plan).
- Keep a complete photocopy
- IRS confirmation: a CP216F notice is sometimes sent acknowledging receipt; otherwise no confirmation. Check IRS account transcript via Form 4506-T 6-12 weeks later.

### Producing the printable PDF

1. Download latest Form 5500-EZ revision from https://www.irs.gov/pub/irs-pdf/f5500ez.pdf
2. Open in fillable PDF tool
3. Map draft values to PDF field names (`f1_3`, `f2_5`, etc. — stable on IRS forms)
4. Save as flattened PDF for printing

---

## Section 3 — EFAST2 for Form 5500-EZ (electronic option)

Since plan year 2020, the IRS allows 5500-EZ filers to **optionally** file electronically via EFAST2. The data flows from EFAST2 to the IRS.

Same browser flow as Section 1 (IFILE), with form-type "5500-EZ" selected. Filer credentials still required.

Practical: most 5500-EZ filers (solo 401(k) sponsors) stick with paper because EFAST2 credentialing has overhead and 5500-EZ is simple. The IRS accepts both. If filing recurrently, electronic is more convenient long-term.

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
2. **Accepted** — DOL acknowledges receipt and basic validation passed (EFAST2: minutes; paper 5500-EZ: 6-12 weeks)
3. **Processed** — fully ingested
4. **Notice issued** OR **No further action**

Possible notices:

- **CP403 / CP406** (IRS, for 5500-EZ) — late filing penalty notice
- **DOL letter** for missing schedules, participant count anomaly, late deferrals, or audit issues
- **PBGC notice** (defined benefit only) — premium reconciliation

Status checks:

- EFAST2: filing status visible in user's filing history at efast.dol.gov
- 5500-EZ paper: IRS account transcript via Form 4506-T (allow 6-12 weeks)
- DOL: 1-866-444-EBSA (3272)
- PBGC: 1-800-400-7242

The agent should set a follow-up reminder 7 days after submission (EFAST2) or 12 weeks (paper 5500-EZ) to check status.

---

## Section 6 — DFVC (Delinquent Filer Voluntary Compliance)

If the user is filing late and DOL has not yet sent a notice, they can use DFVC to dramatically reduce penalties:

- DFVC penalty: $10/day, capped at $750 per filing, $1,500 per plan administrator (for plans < 100 participants); $2,000 / $4,000 for large plans
- Without DFVC: up to $2,739/day per ERISA §502(c)(2) (verify current adjustment via 29 CFR §2575.502c-2)

DFVC requires:
1. File the late 5500 via EFAST2 (or 5500-EZ paper) AND
2. Submit DFVC penalty payment via the DOL's online payment system at https://www.dol.gov/agencies/ebsa/employers-and-advisers/plan-administration-and-compliance/reporting-and-filing/form-5500/dfvc-online-payment

For 5500-EZ specifically, DFVC does NOT apply (DFVC is a DOL program; 5500-EZ is IRS-only). Instead, IRS has a **Late Filer Penalty Relief Program for One-Participant Plans** (Rev. Proc. 2015-32) — flat $500 per delinquent return, capped at $1,500 per plan.

See [`references/dfvc-and-penalties.md`](./references/dfvc-and-penalties.md) for full DFVC mechanics.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** at the moment of submission. "I authorize you to file Form 5500 / 5500-SF / 5500-EZ for plan year [YYYY] right now" must be captured.
2. **Never store EFAST2 signer credentials** (User ID + PIN) in agent logs, vector stores, or transcripts. Pull at filing time, use, discard.
3. **Never bypass identity verification or CAPTCHAs.** If EFAST2 / IRS asks for proof, pause and let the user respond directly.
4. **Always capture submission confirmations** as screenshots stored under the user's account, not the agent's.
5. **If anything looks wrong** (math disagreement, unexpected screen, MFA failures, validation errors), **stop and surface the issue**. Don't retry blindly.
6. **Pre-submission diff**: show the user a side-by-side of the draft vs. what's about to be submitted. Get explicit OK before clicking submit.
7. **Audit report attachments**: handle with care — IQPA reports may contain participant SSNs in detail tables. Verify the attached PDF before submission; redact SSNs if not required by Schedule H instructions (most participant data goes in summary form, not list form).
