# Filing Schedule D — Browser-Automation Playbook

This document covers the filing-stage workflow for Schedule D + Form 8949 once the agent has produced the validated draft (see `SKILL.md`). It assumes the user has explicitly authorized filing and has consented to the agent operating browser automation on their behalf.

Schedule D is rarely filed alone — it is always attached to a Form 1040 return. This playbook covers the filing channel choice and the field-by-field map for the most common channel; the broader 1040 e-file mechanics are in [`forms/form-1040/filing.md`](../form-1040/filing.md) when that skill is needed.

---

## Decision tree — pick a filing channel

```
Is the user's AGI ≤ $84,000 (2025 limit, verify current)?
├── YES → IRS Free File: most providers support Schedule D + 8949 directly
└── NO  → Continue
    │
Does the user already have paid tax software (TurboTax, H&R Block, FreeTaxUSA, TaxAct, etc.)?
├── YES → Use that software's Schedule D / 8949 import path (broker 1099 import is the fast path)
└── NO  → Continue
    │
Does the user prefer free filing and accept manual data entry?
├── YES → IRS Free File Fillable Forms (FFFF) — supports Schedule D + 8949 but no broker import
└── NO  → Continue
    │
Is the user in a state covered by IRS Direct File and within scope?
├── YES → IRS Direct File supports limited capital gain scenarios (verify current scope — historically excludes complex cases)
└── NO  → FreeTaxUSA (free federal, ~$15 state) is the most common fallback
```

**Notes on channel limitations:**

- **IRS Direct File** in tax year 2024 expanded to 25 states but historically **does not support Schedule D for complex situations** (e.g., wash sales, multiple boxes, carryovers). Verify each year before recommending. A Schedule D with only 1099-DIV Box 2a capital gain distributions and no Form 8949 entries may qualify; anything with 8949 detail typically falls out of scope.
- **IRS Free File Fillable Forms (FFFF)** supports Schedule D and Form 8949 but requires manual entry of every transaction. Acceptable for filers with under 20 transactions; impractical for active traders.
- **Paid tax software** is the right answer for any filer with more than ~20 transactions or any crypto activity. The 1099-B import (TXF format or direct broker connection) handles boxes A/D automatically. Crypto tax software (CoinTracker, Koinly, TaxBit) can produce a TXF or 8949 PDF that the main tax software imports.

---

## Field-by-field map: IRS Free File Fillable Forms (FFFF)

FFFF presents Schedule D as a fillable PDF. The agent must populate each line in the order below. Because FFFF auto-computes most arithmetic, the agent fills the source figures and verifies the auto-totals.

### Header

- **Name** → exact match to Form 1040 (case-insensitive but spelling must match)
- **SSN** → exact match to Form 1040

### Part I — Short-Term

For each Box A page on Form 8949:
- Form 8949 (Part I) page is filled separately; FFFF auto-rolls totals to Schedule D Line 1b
- Or, if no adjustments and aggregation is acceptable, fill Schedule D **Line 1a** directly with proceeds, basis, and gain/loss totals

For **Line 2** (Box B), **Line 3** (Box C): fill from Form 8949 detail. FFFF rolls totals automatically if 8949 was completed first.

**Line 4** (other forms): manually enter short-term totals from Form 6252 (installments), Form 6781 (40% short-term portion), Form 8824 (like-kind boot recognized as ST).

**Line 5** (K-1): manually enter short-term capital gain from any K-1 received.

**Line 6** (carryover): enter prior-year short-term carryforward as a negative number (e.g., `-2500`).

**Line 7**: FFFF auto-computes.

### Part II — Long-Term

Same pattern for Lines 8a, 8b, 9, 10.

**Line 11**: combine §1231 net gain from Form 4797 + Form 6252 long-term + Form 6781 60% portion + Form 8824 long-term portion. FFFF does not break these out; one combined total goes here.

**Line 12** (K-1 long-term): from K-1.

**Line 13** (capital gain distributions): from 1099-DIV Box 2a, all sources combined.

**Line 14** (LT carryover): prior-year long-term carryforward, negative number.

**Line 15**: FFFF auto-computes.

### Part III — Summary

**Line 16**: FFFF auto-computes.

**Line 17**: Yes/No based on whether Lines 15 and 16 are both gains. FFFF does not auto-determine; the agent must select.

**Line 18** (28% Rate Gain Worksheet): FFFF does **not** include this worksheet. The agent computes externally using the 28% Rate Gain Worksheet from the Schedule D instructions, then enters the result. Common inputs: collectibles gain (8949 code C), §1202 QSBS partial-exclusion gain (code Q).

**Line 19** (Unrecaptured §1250 Gain Worksheet): also **not** auto-computed. Agent computes externally and enters the result. Inputs: real estate sales with prior depreciation.

**Line 20**: select the right tax worksheet — Schedule D Tax Worksheet (if Line 18 or 19 > 0) or Qualified Dividends and Capital Gain Tax Worksheet.

**Line 21**: if Line 16 is a loss, enter the smaller of |Line 16| or $3,000 ($1,500 MFS) as a negative number.

**Line 22**: Yes/No based on whether the user has qualified dividends; routes to the right worksheet.

### Tax-rate computation

FFFF includes both worksheets as separate fillable forms. The agent must:

1. Determine which worksheet applies (Step 6 of `SKILL.md` workflow)
2. Open the correct worksheet
3. Fill in all input fields (taxable income, capital gain, qualified dividends, etc.)
4. Verify the worksheet's auto-computed tax matches the agent's expected tax
5. Transfer the worksheet result to Form 1040 Line 16

If the user has Form 8960 NIIT exposure, complete that form separately and route the result to Schedule 2 Line 12.

---

## Pre-flight checklist (before submission)

The agent must verify all of the following before authorizing submission:

- [ ] Filer's legal name and SSN match Form 1040 exactly
- [ ] Filing status on Schedule D matches Form 1040
- [ ] All Form 8949 pages are attached (FFFF: each box has its own page in the PDF)
- [ ] Schedule D Line 16 ties to Form 1040 Line 7 (or Line 21 if loss capped)
- [ ] Form 8960 attached if MAGI > NIIT threshold
- [ ] Form 4797, 6252, 6781, 8824 attached if their results flow to Schedule D
- [ ] Capital Loss Carryover Worksheet saved locally for next year (not filed with return, but agent must produce and save it)
- [ ] Tax-rate worksheet (Qualified Dividends and Capital Gain Tax Worksheet or Schedule D Tax Worksheet) computed and result entered on Form 1040
- [ ] Math checks from `SKILL.md` Validation passed
- [ ] User has reviewed the draft and explicitly approved submission

---

## Submission state machine

```
DRAFT → REVIEWED → SUBMITTED → ACCEPTED → PROCESSED → REFUND_OR_PAYMENT
                              ↓
                          REJECTED → FIX_AND_RESUBMIT
```

- **DRAFT** — `SKILL.md` produced; not yet validated by user
- **REVIEWED** — User has reviewed the draft and authorized filing
- **SUBMITTED** — E-filed; awaiting IRS acknowledgment (typically minutes to 48 hours)
- **ACCEPTED** — IRS acknowledged receipt and basic validation passed
- **REJECTED** — Common reasons: SSN/name mismatch, prior-year AGI mismatch on signature, identity theft block. Fix and resubmit.
- **PROCESSED** — Return processed; refund issued or balance due posted
- **NOTICE** (out of band) — A CP2000 notice can arrive 9–18 months later if 8949 totals don't match 1099-B

---

## Security rules

The agent **must**:

- **Never persist** the user's SSN, DOB, or e-file PIN past the active session
- **Never store** broker login credentials — use only OAuth or one-time imports
- **Require explicit consent** at the moment of submission ("I am about to e-file your return — confirm by typing CONFIRM")
- **Show a diff** between the draft and the final submitted return when the user reviews
- **Log only metadata** (timestamp, channel, acceptance status) — never the full return contents

The agent **must not**:

- Submit without explicit per-session consent
- Copy/paste SSN into a chat log or any file the user can browse later
- Use any browser automation that bypasses the IRS authentication flow
- Re-submit after a rejection without surfacing the rejection reason and getting fresh consent

---

## Paper filing fallback

If the user cannot or will not e-file:

1. Print Form 1040, Schedule D, all Form 8949 pages, Form 8960 (if applicable), and any other required attachments
2. Sign and date Form 1040 (and spouse if MFJ)
3. Attach copies of any 1099-Bs that show federal income tax withheld (most don't, but if any do, attach them)
4. Mail to the address corresponding to the user's state and whether a payment is enclosed (see Form 1040 instructions, "Where to File")
5. Include certified mail receipt for proof of timely filing
6. Allow 6–8 weeks for processing (paper returns are slower than e-file by an order of magnitude)

For tax year 2025 and later, the IRS strongly prefers e-file. Paper filing of complex returns (multiple Form 8949 pages, several K-1s) significantly raises the risk of transcription errors during IRS data entry. E-file is the safer path.

---

## Channel-specific notes

### TurboTax / H&R Block / TaxAct

- 1099-B import via direct broker connection is the fast path; verify each imported transaction against the 1099-B PDF
- Crypto transactions: import from a crypto tax aggregator (CoinTracker, Koinly, TaxBit) using TurboTax's TXF or CSV import
- Wash sale handling: software flags wash sales reported on the 1099-B but not cross-account washes — the agent must add cross-account wash adjustments manually

### FreeTaxUSA

- Manual entry only for 1099-B (no direct broker import in the free version)
- Acceptable for under 50 transactions; tedious above that
- Schedule D Tax Worksheet is auto-computed when applicable

### IRS Direct File (where available)

- Verify each tax year whether Schedule D scope includes the user's situation
- Historically excludes wash sales, multiple boxes, carryovers, §1250, §1202
- Useful for the simplest cases: 1099-DIV Box 2a only, single-broker covered shares, no carryover

---

## Sources

- [IRS Free File](https://www.irs.gov/filing/free-file-do-your-federal-taxes-for-free)
- [IRS Free File Fillable Forms](https://www.irs.gov/e-file-providers/free-file-fillable-forms)
- [IRS Direct File](https://directfile.irs.gov)
- [Schedule D Instructions](https://www.irs.gov/pub/irs-pdf/i1040sd.pdf) — contains 28% Rate Gain Worksheet, Unrecaptured §1250 Gain Worksheet, Capital Loss Carryover Worksheet, Schedule D Tax Worksheet
- [Form 1040 Instructions](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf) — contains Qualified Dividends and Capital Gain Tax Worksheet
