# Filing Form 4797 — Browser Automation Playbook

This file is loaded only when the user explicitly authorizes the agent to file the return on their behalf. The agent should never persist SSN, DOB, EFIN, or PIN beyond the active session, and must require explicit consent before final submission.

---

## Pre-flight checklist

Before navigating to any filing channel, the agent must confirm:

- [ ] Form 4797 draft has passed all validation checks in `SKILL.md`
- [ ] Each disposition has accumulated depreciation reconciled against prior Forms 4562
- [ ] 5-year §1231 lookback confirmed with the user
- [ ] Schedule D and Schedule 1 downstream entries are computed
- [ ] If Part IV §179 recapture applies, Schedule C Line 6 entry is computed
- [ ] If installment sale, Form 6252 is also drafted
- [ ] User has provided explicit "yes, file this" consent on the day of submission

---

## Filing channel decision tree

Form 4797 cannot be filed standalone — it is always attached to Form 1040 (individual), Form 1065 (partnership), Form 1120-S (S-corp), or Form 1120 (C-corp). Follow the parent-form filing channel:

```
Is the user an individual filing Form 1040?
├── Yes → AGI ≤ $84,000 (2025 threshold)?
│   ├── Yes → IRS Free File guided software (most providers support 4797)
│   └── No → Free File Fillable Forms (FFFF), paid commercial software, or paper
└── No → Partnership (1065) / S-corp (1120-S) / C-corp (1120)?
    └── Use commercial pro-prep software (Drake, Lacerte, ProSeries, ATX, UltraTax)
```

**IRS Direct File** — Confirm whether Form 4797 is supported in the user's state for the current tax year. As of TY2025, Direct File supports limited W-2 + simple credits only. If Form 4797 is needed, Direct File is generally NOT a viable channel.

**Free File Fillable Forms (FFFF)** is the most common channel for self-filers with Form 4797. It is digital paper — no calculations, but it transmits to the IRS e-file system.

---

## Channel A — Free File Fillable Forms (FFFF)

URL: https://www.freefilefillableforms.com (active during filing season; closes after Oct 15)

### Field-by-field map

After signing in, navigate: **Add a Form → Form 4797**.

**Header**
- Name(s) shown on return → from Form 1040 header
- Identifying number → SSN (or EIN if filing for an entity)

**Part I (Lines 1-9)**
- Line 1 → Year and 1099-S info if applicable
- Line 2 columns (a)-(g) → for each non-depreciable §1231 asset
- Line 6 → residual §1231 gain from Part III (FFFF auto-pulls if Part III is filled correctly)
- Line 7 → FFFF auto-sums Lines 2-6
- Line 8 → manual entry (FFFF does not track lookback)
- Line 9 → FFFF auto-computes Line 7 − Line 8

**Part II (Lines 10-18)**
- Line 10 → short-term ordinary
- Line 11 → from Part I Line 7 (if loss)
- Line 12 → from Line 8 if Line 7 is positive
- Line 13 → FFFF auto-pulls from Part III Line 32
- Line 18 → FFFF auto-sums

**Part III (Lines 19-32)**
- Each disposed depreciable asset gets a column (A, B, C, D)
- Line 25b: enter manually as min(Line 24, Line 25a)
- Line 26 §1250: most filers post-1986 enter $0 in Line 26g
- Line 32 → FFFF auto-sums

**Part IV (Lines 33-35)**
- Only complete if §179 / §280F recapture applies
- Line 35 amount must also be entered on Schedule C Line 6 (or 1040 Line 8 for non-Schedule-C filers)

### Common FFFF gotchas

- **No calculations.** FFFF won't compute §1245 recapture for you. Compute it offline and enter the final number.
- **Sub-total fields auto-fill but are sometimes wrong.** Always verify Line 7, Line 18, Line 31, Line 32 against your draft.
- **Schedule D linkage.** After saving Form 4797, navigate to Schedule D Line 11 and verify Part I Line 9 amount carried over. FFFF does not always cross-link.
- **Unrecaptured §1250 Gain Worksheet.** FFFF does not include this worksheet — you must compute the 25%-cap amount externally and adjust Schedule D Line 19 manually.

---

## Channel B — Commercial software

For filers with multiple dispositions, cost segregation, or installment sales, use commercial software:

- **TurboTax Premier or Self-Employed** — supports Form 4797 with guided interview; weak on cost segregation splits
- **H&R Block Premium** — similar to TurboTax
- **TaxAct Self-Employed** — cheaper, supports Form 4797
- **FreeTaxUSA** — free federal, supports Form 4797 including Part III

For pro-prep:
- **Drake / Lacerte / ProSeries / UltraTax** — full §1245/§1250 split with cost segregation support, depreciation schedule import, lookback tracking

The agent should ask the user which software they have access to before selecting a channel.

---

## Channel C — Paper filing

For users who cannot or do not want to e-file:

1. Print Form 4797 from https://www.irs.gov/pub/irs-pdf/f4797.pdf
2. Hand-fill or fill in Adobe Acrobat (the form has fillable fields)
3. Attach to Form 1040 (or entity return) as part of the standard package
4. Mail to the address shown in the Form 1040 instructions for the user's state

Paper filing adds 6-8 weeks to processing. Use only if e-file is not an option.

---

## Submission state machine

After submission via FFFF or commercial software:

```
[Draft] → [Submitted] → [IRS Received] → [Accepted | Rejected]
                                              │           │
                                              ▼           ▼
                                       [Processing]   [Fix errors → Resubmit]
                                              │
                                              ▼
                                  [Refund Issued | Notice (CP2000, etc.)]
```

The agent should:
1. After Submitted: log the submission ID locally (NOT the SSN)
2. After Accepted: notify the user with the IRS confirmation number
3. After Rejected: parse the reject code and route to fix workflow
4. If a CP2000 notice arrives later: re-engage with the prior draft and the notice's proposed adjustments

---

## Security rules

**Never store:**
- Full SSN (only last 4 if needed for identification)
- Date of birth
- IRS e-file PIN or self-select PIN
- Driver's license number
- Bank account / routing numbers (for refund direct deposit)

**Always require:**
- Explicit consent at the moment of submission ("Type 'submit' to file this return")
- Diff between the last draft and the final form being submitted
- Read-back of the bottom-line numbers (§1231 long-term gain, ordinary recapture, total tax impact) before clicking Submit

**Session hygiene:**
- Clear browser session storage and cookies after submission
- Do not screenshot pages containing SSN or PIN
- If the agent's transcript will be stored, redact SSN before persisting

---

## Post-filing handoffs

After the return is accepted:

- [ ] Save final Form 4797 PDF locally (filer's records)
- [ ] Save the depreciation schedule per asset for next-year basis tracking
- [ ] Note any non-recaptured §1231 loss for next year's lookback
- [ ] If installment sale: schedule reminder for next year's Form 6252 continuation
- [ ] If §179 recapture: update Schedule C basis for any remaining depreciation in future years
- [ ] If real estate sale with unrecaptured §1250 gain: ensure Schedule D Line 19 is reflected on Form 1040 tax computation
