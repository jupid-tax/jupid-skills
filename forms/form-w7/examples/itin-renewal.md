# Example — ITIN Renewal After Expiration (3 Years Non-Use)

## Facts

- **Applicant**: Rajesh Subramaniam, Indian citizen
- **Existing ITIN**: 9XX-78-XXXX (middle digits 78 — falls in the 70-87 range that was systematically expired by IRS notice in 2016-2019, but Rajesh's ITIN was issued in 2020 and was renewed at issuance; the relevant expiration trigger is the **3-year non-use rule** for his case)
- **ITIN history**: Originally issued 2020 when Rajesh was a postdoctoral researcher at a US university on a J-1 visa, used the ITIN to claim US-India tax treaty benefits on his fellowship income (1042-S). Filed 1040-NR for tax years 2020 and 2021. Returned to India after his postdoc, didn't file US tax returns 2022, 2023, 2024. Now (2025) he received a one-time consulting payment from a US biotech company for a research collaboration ($45,000 paid via Form 1042-S with 30% NRA withholding).
- **Tax year**: 2025 (filing 1040-NR in early 2026 to claim treaty-based reduced rate and refund of over-withheld tax)
- **Why ITIN renewal is needed**: Rajesh's ITIN has not been used on any tax return for 3+ consecutive years (2022, 2023, 2024 — no 1040-NR filed). Per IRC §6109 and the PATH Act of 2015, an ITIN expires after 3 consecutive years of non-use. To file his 2025 1040-NR (claiming treaty refund), he must first renew the ITIN.
- **Identification documents Rajesh has**:
  - Indian passport, valid through 2031
  - Indian PAN card (tax ID)
  - Aadhaar card (national ID)
- **CP-48 notice received?** Possibly — IRS sometimes sends CP-48 ("Your ITIN may expire") proactively to ITINs nearing the 3-year non-use trigger. Rajesh doesn't recall receiving one (he's been in India; mail forwarding spotty). Not required for renewal; Rajesh can renew on his own initiative.

## Analysis

### Step 1 — SSN ineligibility

Rajesh is a non-resident alien (returned to India in 2022, no US presence, no work authorization). He is not SSN-eligible. ITIN renewal is appropriate.

### Step 2 — Reason code

For renewal, Rajesh checks the **same reason code** he used originally — typically **(a) Nonresident alien required to file US tax return**, since he's filing a 1040-NR.

He also checks the special **"Renew an existing ITIN"** box at the top of Form W-7 (this is the renewal indicator distinct from a new application).

His reason: filing 2025 Form 1040-NR to report US consulting income, claim US-India treaty benefits (if applicable), and request refund of over-withholding.

### Step 3 — Identification documents

Indian passport — single-document path (proves identity and foreign status). Same as for a new ITIN application.

For renewal, the IRS requires the same documentation rigor as a new application — there is no shortcut for renewals. Rajesh must submit:
- Original passport, OR
- Certified copy from issuing authority (Indian passport office or Indian consulate-general in San Francisco, Chicago, NYC, etc.), OR
- CAA-certified copy

For this example: **Rajesh uses a CAA in Mumbai** (India has several IRS-listed CAAs). CAA certifies the passport, Rajesh keeps the original. Cost ~$200-400.

### Step 4 — Tax return attachment

Even for renewal, the W-7 must be attached to a federal tax return (no exception applies in Rajesh's case because his consulting income generates a real 1040-NR filing requirement).

The 2025 Form 1040-NR is prepared with:
- Rajesh's existing (expired) ITIN written in the SSN field, with notation "RENEWAL APPLIED FOR" or similar
- $45,000 consulting income reported on the appropriate line
- Tax treaty article (US-India tax treaty Article 15 for independent personal services, if applicable — verify the article and treaty position for one-off consulting income; some independent services for short-duration may qualify for treaty exemption)
- Credit for $13,500 of withholding from Form 1042-S
- Refund claim for the difference between $13,500 withheld and actual US tax owed (which may be substantially less if treaty-exempt)

Per IRS instructions, the renewal W-7 + the 2025 1040-NR are filed together. The return cannot be e-filed during the W-7 renewal process; paper filing required.

### Step 5 — Fill the W-7 for renewal

Key fields:

- **Top of form**: check the **"Renew an existing ITIN"** box
- Reason code: **(a) Nonresident alien required to file US tax return**
- Line 1a: Rajesh Subramaniam (matching passport)
- Line 2 (mailing address): Rajesh's address in Mumbai, India
- Line 3: same Mumbai address (no separate foreign address)
- Line 4: DOB, place of birth (Chennai, India)
- Line 5: Male
- Line 6a: India (citizenship)
- Line 6b: Indian PAN number (foreign tax ID)
- Line 6c: Past US visa (J-1, expired 2022); leave current visa blank or "N/A"
- Line 6d: Indian passport, India, number, expiration 2031
- Line 6e: Last date of entry to US (some date in 2020 when he started postdoc); his most recent entry
- Line 6f: **Existing ITIN: 9XX-78-XXXX** (this is the renewal-specific field — note the previously issued ITIN); also note "Renewal — last filed 2021"
- Sign and date

### Step 6 — Assemble the renewal package

Stack:

1. Form W-7 (with **Renew** box checked, reason (a), existing ITIN on Line 6f)
2. CAA-certified copy of Indian passport
3. CAA W-7 COA (Certificate of Accuracy)
4. **Form 1040-NR (2025)** with:
   - Rajesh's expired ITIN in the TIN field
   - Consulting income reported
   - Tax treaty position taken (with statement explaining the treaty article)
   - Schedule OI (treaty country, treaty article, summary of treaty position)
   - Credit for 1042-S withholding
   - Refund claim
5. Form 1042-S issued by the US biotech company (showing income and withholding)
6. (Optional) Copy of any prior CP-48 notice received

### Step 7 — Submit

Mail to **ITIN Operation Austin**:

```
Internal Revenue Service
ITIN Operation
P.O. Box 149342
Austin, TX 78714-9342
```

CAA process: CAA in Mumbai prepares the package, certifies passport copy, sends via international courier (DHL or FedEx) to Austin. Verify courier address (different from PO Box).

### Step 8 — Wait

Processing time: 7-11 weeks. For renewals filed during peak season, expect closer to 11 weeks. Rajesh files in February 2026; expects renewal completion by April-May 2026.

If 11 weeks elapse without response, call 1-800-908-9982 (US line; from India, use 267-941-1000).

### Step 9 — After renewal is processed

IRS issues a CP-565A (renewal confirmation, distinct from CP-565 for new ITINs). The same ITIN number stays — renewal doesn't change the number, just reactivates it. Rajesh's ITIN 9XX-78-XXXX is now valid through the next 3-year non-use window.

The 2025 1040-NR is processed using the renewed ITIN. If a refund is owed (likely due to treaty position reducing actual tax below withheld amount), IRS sends refund check to Rajesh's Mumbai address (or direct deposit if Rajesh provided US bank info — non-resident aliens often don't have US bank accounts, so paper check is more common; expect 6-8 additional weeks).

### Step 10 — Use of renewed ITIN going forward

Rajesh should:
- Use the same ITIN on any future 1040-NR filings
- Keep the ITIN active by filing at least once every 3 years (even if no tax owed, file the return that triggers the ITIN need)
- If Rajesh later becomes SSN-eligible (e.g., if he immigrates to the US in the future), he should rescind the ITIN and switch to SSN

### Why this matters — the cost of letting an ITIN expire

If Rajesh had filed his 2025 1040-NR using the expired ITIN without renewing, the IRS would have:
- Rejected the return processing (the ITIN matches no active record)
- Held the return in suspense, sending Rajesh a notice asking him to renew
- Delayed his refund by 6-12 months
- Possibly applied late-filing/late-payment penalties if the situation escalated

By renewing proactively at the time of filing, Rajesh avoids all of that. The W-7 + 1040-NR submitted together signals the IRS to process the renewal first, then the return.

## Validation checks

- [x] **Renew** box checked at top of W-7
- [x] Reason code (a) — same as original or appropriate for current filing
- [x] Existing ITIN (9XX-78-XXXX) listed on Line 6f
- [x] Identification documents same standard as new application (originals or certified copies)
- [x] 2025 Form 1040-NR attached (renewal still requires the underlying return that triggers the ITIN need)
- [x] Form 1042-S attached as evidence of withholding
- [x] Mailing address is Rajesh's actual Mumbai address
- [x] Mailed to ITIN Operation Austin

## Lessons

1. **3-year non-use trigger** is the most common renewal trigger. Filers who leave the US and stop filing returns lose their ITIN after 3 consecutive years. Even one filing in that window (even a $0-tax 1040-NR) keeps the ITIN active.
2. **Renewal is not faster than a new application** — same 7-11 week processing, same documentation requirements. Don't assume "renewal" means a shortcut.
3. **Same ITIN number** is preserved on renewal — Rajesh's number doesn't change. This matters for prior-year cross-references and 1042-S matching.
4. **CP-48 notices** are proactive IRS warnings sent ~12 months before expiration. Filers should respond to CP-48 with a renewal application even if they don't currently need to file. Many filers ignore CP-48s living overseas.
5. **PATH Act 2015 expiration triggers**: 3-year non-use AND middle-digit cohorts (70-87 expired in waves 2016-2019, 88-90 in 2020, 91-99 in 2021). Rajesh's middle digit 78 was already expired in 2016 BUT was renewed at issuance in 2020, so the 2016 wave doesn't re-apply. Only the 3-year non-use trigger is relevant now.
6. **Treaty positions on 1040-NR** require careful Article citation in Schedule OI. Don't assume any one-off US payment to an Indian resident is treaty-exempt — check the specific income type and treaty article.
7. **Plan international refund delivery**: paper checks to foreign addresses can take 6-8 weeks beyond the standard refund timeline; consider opening a US bank account if recurring filings are expected.

## Citations

- IRC §6109 — TIN requirements
- PATH Act of 2015 (Pub. L. 114-113) — ITIN expiration rules (3-year non-use; middle-digit cohort expiration)
- Treas. Reg. §301.6109-1(d)(3) — ITIN issuance and renewal
- Pub. 1915 — Understanding Your IRS ITIN (covers renewal procedures)
- Pub. 519 — US Tax Guide for Aliens
- Form W-7 instructions — renewal box and existing ITIN reporting
- US-India Income Tax Treaty (1989) — Article 15 (Independent Personal Services); verify article numbers and current treaty status
- Form 1042-S instructions — withholding reporting on US-source income to nonresident aliens
- Notice CP-48 — IRS proactive notice of pending ITIN expiration
- Notice CP-565A — IRS confirmation of ITIN renewal
