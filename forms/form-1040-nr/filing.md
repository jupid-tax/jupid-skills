# Filing Form 1040-NR

How an agent takes a finished Form 1040-NR draft from `SKILL.md` to a filed return. Produce and validate the draft first, then pick the channel below. Every address and rule here is from the Instructions for Form 1040-NR (2025, dated Jan 29, 2026), the Instructions for Form W-7 (Rev. December 2024), Pub. 519 (2025), and Form 1040-ES (NR) (2026). Addresses change between years: re-check the current instructions at https://www.irs.gov/forms-pubs/about-form-1040-nr before mailing anything.

---

## Channel decision tree

```
Is this a dual-status year?
  → YES: not drafted by this skill. Pub. 519 (2025): dual-status taxpayers cannot e-file their
    2025 return. Paper only (addresses in Section 3). Stop and refer to a CPA.

Does the filer lack an SSN and ITIN, or need to renew an expired ITIN?
  → YES: Section 2 (paper package with Form W-7 to the ITIN Operation).
    A return using an ITIN can't be e-filed in the calendar year the ITIN is assigned,
    including prior-year returns (Instructions for Form W-7).

Is a paid preparer filing?
  → Paid preparers must generally e-file Form 1040-NR, except for dual-status, fiscal-year,
    trust, and estate returns (Instructions for Form 1040-NR, Reminders; Notice 2020-70).
    Section 1.

Is the filer filing themselves with a valid SSN or ITIN?
  → Commercial software that supports Form 1040-NR: Section 1.
    Check the provider's supported-forms list for Form 1040-NR and Schedules NEC, OI, A (NR), P
    before starting; many consumer products support only Form 1040.
  → Or paper: Section 3.

Only claiming a refund of chapter 3/4 withholding, no U.S. trade or business, tax fully satisfied
by withholding?
  → Simplified Procedure (Instructions for Form 1040-NR): page 1 identity (and line 1k if
    treaty-exempt), Schedule NEC lines 1a–15, lines 23a–35e, signature, Schedule OI, copies of
    Forms 1042-S (or 1099 for backup withholding). Then Section 1 or 3.

No return required, but Form 8843 or Form 8840 is?
  → Mail the form alone to: Department of the Treasury, Internal Revenue Service Center,
    Austin, TX 73301-0215, by the Form 1040-NR due date including extensions.
```

---

## Section 1 — E-file

### Pre-flight

The agent must have:

- The validated draft (every line, Schedules NEC, OI, A (NR), P as applicable, and the attachments list).
- The user's explicit permission to enter data into the software or to hand the draft to a preparer.
- Identity data at filing time only: SSN or ITIN, date of birth, prior-year AGI or prior-year Self-Select PIN for signature verification (the Form 1040 e-file rules; ask the user to type them directly where possible).
- Form 1042-S, W-2, 8805, 8288-A amounts exactly as on the forms.
- Banking details only if the user wants direct deposit or an electronic payment (U.S. account).

### Flow

1. The user (or preparer) opens the software and selects Form 1040-NR, not Form 1040.
2. Enter the header and filing status; confirm the software offers no MFJ or HOH.
3. Enter page 1 ECI, Schedule 1/C/D/E data, Schedule A (Form 1040-NR), Schedule NEC by column, Schedule OI items A–M, Form 8843/8840/8833 if attached.
4. Compare every computed line in the software with the draft. If any line differs, stop: one of them is wrong. Do not override silently.
5. Pay attention to line 16: the software must use the Single, MFS, or QSS column that the draft used.
6. Review the software's error checks; resolve every one.
7. Submit only after the user gives explicit consent at that moment ("Yes, file my 2025 Form 1040-NR now").
8. Save the submission ID and acceptance acknowledgment for the user.

---

## Section 2 — Paper package with Form W-7 (new or renewed ITIN)

Build the W-7 with [`../form-w7/SKILL.md`](../form-w7/SKILL.md). Then:

1. Leave the identifying number area blank on Form 1040-NR; the IRS assigns the ITIN to the return after processing the W-7 (Instructions for Form W-7).
2. Assemble: Form W-7 on top, the identification documents (originals or certified copies, or through an Acceptance Agent / CAA), then the complete signed Form 1040-NR with all schedules and attachments.
3. Mail to:

   Internal Revenue Service
   ITIN Operation
   P.O. Box 149342
   Austin, TX 78714-9342

   Do **not** mail it to the Form 1040-NR address; the return is processed as part of the ITIN package (Instructions for Form W-7, Where To Apply).
4. Processing: allow 7 weeks for notice of the ITIN application status; 9 to 11 weeks if submitted January 15 through April 30 or from overseas (Instructions for Form W-7).
5. Because the return must be timely for deductions (16-month rule), mail the package well before the due date when deductions matter, and keep proof of mailing.

---

## Section 3 — Paper filing (no W-7)

### Addresses for 2025 Forms 1040-NR filed in 2026 (Instructions for Form 1040-NR, Where To File)

| Filer | Not enclosing a payment | Enclosing a payment |
|---|---|---|
| Individual | Department of the Treasury, Internal Revenue Service, Austin, TX 73301-0215, USA | Internal Revenue Service, P.O. Box 1303, Charlotte, NC 28201-1303, USA |
| Estate or trust (out of scope) | Department of the Treasury, Internal Revenue Service, Kansas City, MO 64999, USA | Internal Revenue Service, P.O. Box 1303, Charlotte, NC 28201-1303, USA |

Only the U.S. Postal Service delivers to P.O. boxes; a private delivery service can't be used to send a payment to a P.O. box.

### Assembly

- Attach to the **front** of Form 1040-NR: Forms W-2, 1042-S, SSA-1042S, RRB-1042S, 2439, and 8288-A; Form 1099-R if tax was withheld; original W-2s plus any W-2c.
- Attach to the **back**: Forms 8805 (a foreign trust or estate also attaches the Forms 8805 it furnished, with Schedule T).
- Then the schedules and forms in attachment sequence order (Schedule A (Form 1040-NR) is sequence 7A, Schedule NEC 7B, Schedule OI 7C, Schedule P 7D), followed by statements (election statements, treaty statements, Form 8233 substitute statements).
- Enclose, but don't attach, any payment.
- The filer signs in ink. An agent in the U.S. may sign only if the filer was ill or injured, was not in the U.S. at any time during the 60 days before the due date, or for other IRS-approved reasons, and must attach a power of attorney (Form 2848) that specifically authorizes signing the return.

### Due dates and extensions

- April 15, 2026 (wages as an employee subject to U.S. income tax withholding) or June 15, 2026 (all others). A due date on a weekend or holiday moves to the next business day.
- Form 4868 by the original due date extends filing to October 15, 2026, or December 15, 2026 for the June 15 group (Pub. 519 ch. 7). It does not extend payment; interest and the failure-to-pay penalty run from the original due date.
- Keep the 16-month deadline in view for deductions (Treas. Reg. §1.874-1(b)).

---

## Payment

- Electronic: IRS Direct Pay, debit or credit card, digital wallet, or the online account (IRS.gov/Payments). Without a U.S. bank account: IRS.gov/Individuals/International-Taxpayers/Foreign-Electronic-Payments.
- Check or money order: must be drawn on a U.S. financial institution; write "2025 Form 1040-NR", name, address, daytime phone, and SSN or ITIN on it; include Form 1040-V.
- Next year's estimates: Form 1040-ES (NR). With wages subject to withholding: four installments (April 15, June 15, September 15, January 15). Without: 1/2 by June 15, 2026, 1/4 by September 15, 2026, 1/4 by January 15, 2027 (Form 1040-ES (NR) 2026, Payment Due Dates).

## Refund

- Direct deposit needs a U.S. account (an IRA deposit needs a U.S. institution and an IRA set up before the request).
- Paper check to a foreign address: line 35e if different from page 1.
- Refunds of tax shown on Forms 1042-S, 8805, or 8288-A can take up to 6 months.
- Transcripts from outside the U.S.: 267-941-1000 (not toll free) (Instructions for Form 1040-NR, Need a Copy of Your Tax Return Information?).

---

## After filing

1. **Submitted → Accepted** (e-file acknowledgment) or **mailed** (keep certified-mail or PDS proof).
2. **Processed** → refund, balance-due notice, or correspondence.
3. If an error is found later, amend with Form 1040-X ([`../form-1040-x/SKILL.md`](../form-1040-x/SKILL.md)); the 1040-X instructions describe the paper format for amending a Form 1040-NR.
4. Calendar the companion deadlines: the LLC's Form 5472 with pro forma Form 1120 ([`../form-5472/SKILL.md`](../form-5472/SKILL.md)), state nonresident returns, Form 1040-ES (NR) installments.

---

## Security and consent rules

1. Never file or mail without the user's explicit consent at the moment of submission.
2. Never store SSNs, ITINs, passport numbers, dates of birth, PINs, prior-year AGI, or bank account numbers in logs, memory, or transcripts. Collect them at filing time, use them, discard them.
3. Never mail original passports or identity documents without the user's explicit choice of that option in the W-7 workflow; offer the Acceptance Agent and certified-copy routes first.
4. Never bypass identity verification, CAPTCHAs, or multi-factor prompts; hand control to the user.
5. If the software's numbers disagree with the draft, or a screen asks something the draft didn't anticipate (for example, a residency question answered differently), stop and surface it.
6. Treaty positions, dual-status, expatriation, and tie-breaker questions are CPA territory; the agent drafts and flags, it doesn't decide them.
