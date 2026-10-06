# Example — ITIN Renewal After Expiration (3 Years Non-Use)

## Facts

- **Applicant**: Rajesh Subramaniam, Indian citizen
- **Existing ITIN**: 9XX-78-XXXX (issued in 2020, so the rule that pre-2013 ITINs never renewed have expired does not apply; the relevant expiration trigger is the **3-year non-use rule**)
- **ITIN history**: Originally issued 2020 when Rajesh was a postdoctoral researcher at a US university on a J-1 visa, used the ITIN to claim US-India tax treaty benefits on his fellowship income (1042-S). Filed 1040-NR for tax years 2020 and 2021. Returned to India after his postdoc, didn't file US tax returns 2022, 2023, 2024. Now (2025) he received a one-time consulting payment from a US biotech company for a research collaboration ($45,000 paid via Form 1042-S with 30% NRA withholding).
- **Tax year**: 2025 (filing 1040-NR in early 2026 to claim treaty-based reduced rate and refund of over-withheld tax)
- **Why ITIN renewal is needed**: Rajesh's ITIN has not been used on any tax return for 3+ consecutive years (2022, 2023, 2024 — no 1040-NR filed). Per IRC §6109(i) (added by the PATH Act of 2015), an ITIN not included on a federal tax return for 3 consecutive tax years expires on December 31 of the third consecutive tax year (Instructions for Form W-7, Reminders). To file his 2025 1040-NR (claiming treaty refund), he must first renew the ITIN.
- **Identification documents Rajesh has**:
  - Indian passport, valid through 2031
  - Indian PAN card (tax ID)
  - Aadhaar card (national ID)
- **CP48 notice received?** Rajesh doesn't recall receiving one (he's been in India; mail forwarding spotty). No notice is required for renewal; he renews because the ITIN will be included on a federal tax return.

## Analysis

### Step 1 — SSN ineligibility

Rajesh is a non-resident alien (returned to India in 2022, no US presence, no work authorization). He is not SSN-eligible. ITIN renewal is appropriate.

### Step 2 — Reason code

For renewal, Rajesh checks the reason box that fits his current filing: **(b) Nonresident alien filing a U.S. federal tax return**, since he's filing a 1040-NR (a renewal must still check a reason box; "renewal" alone is not a valid reason).

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
- The identifying-number field: the W-7 instructions tell applicants to leave the SSN area blank on the attached return for each person applying for an ITIN; the expired ITIN goes on W-7 line 6f. Do not invent a notation such as "RENEWAL APPLIED FOR"
- $45,000 consulting income reported on the appropriate line
- Tax treaty article (US-India tax treaty Article 15 for independent personal services, if applicable — verify the article and treaty position for one-off consulting income; some independent services for short-duration may qualify for treaty exemption)
- Credit for $13,500 of withholding from Form 1042-S
- Refund claim for the difference between $13,500 withheld and actual US tax owed (which may be substantially less if treaty-exempt)

Per IRS instructions, the renewal W-7 + the 2025 1040-NR are filed together. The return cannot be e-filed during the W-7 renewal process; paper filing required.

### Step 5 — Fill the W-7 for renewal

Key fields:

- **Top of form**: check the **"Renew an existing ITIN"** box
- Reason code: **(b) Nonresident alien filing a U.S. federal tax return**
- Line 1a: Rajesh Subramaniam (matching passport)
- Line 2 (mailing address): Rajesh's address in Mumbai, India
- Line 3: re-enter the same Mumbai address (reason b requires the complete foreign address)
- Line 4: DOB, place of birth (Chennai, India)
- Line 5: Male
- Line 6a: India (citizenship)
- Line 6b: Indian PAN number (foreign tax ID)
- Line 6c: N/A (no current U.S. visa; the J-1 expired in 2022)
- Line 6d: Passport box; issued by India; number; expiration 2031; date of entry into the United States: his most recent entry date in MM/DD/YYYY (ask Rajesh; do not guess)
- Line 6e: **Yes**
- Line 6f: **ITIN 9XX-78-XXXX** and the first, middle, and last name under which it was issued (renewal-specific; required to avoid delays)
- Line 6g: N/A
- Sign and date

### Step 6 — Assemble the renewal package

Stack:

1. Form W-7 (with **Renew** box checked, reason (b), line 6e Yes, existing ITIN and name on Line 6f)
2. CAA-certified copy of Indian passport
3. CAA W-7 COA (Certificate of Accuracy)
4. **Form 1040-NR (2025)** with:
   - Identifying-number field handled per the W-7 instructions (see Step 4)
   - Consulting income reported
   - Tax treaty position taken (with statement explaining the treaty article)
   - Schedule OI (treaty country, treaty article, summary of treaty position)
   - Credit for 1042-S withholding
   - Refund claim
5. Form 1042-S issued by the US biotech company (showing income and withholding)
6. (Optional) Copy of any prior CP48 notice received

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

Processing time: allow 7 weeks; 9-11 weeks for applications submitted January 15 through April 30 or from overseas. Rajesh applies from India in February 2026; expects a notice by April-May 2026.

If 11 weeks elapse without response, call 267-941-1000 from outside the U.S. (800-829-1040 inside the U.S.).

### Step 9 — After renewal is processed

IRS mails a notice confirming the renewal. The same ITIN number stays — renewal doesn't change the number, just reactivates it (the IRS ITIN FAQ: a renewed ITIN keeps its original assignment date). Rajesh's ITIN 9XX-78-XXXX is now valid through the next 3-year non-use window.

The 2025 1040-NR is processed using the renewed ITIN. If a refund is owed (likely due to treaty position reducing actual tax below withheld amount), IRS sends refund check to Rajesh's Mumbai address (or direct deposit if Rajesh provided US bank info — non-resident aliens often don't have US bank accounts, so paper check is more common; expect 6-8 additional weeks).

### Step 10 — Use of renewed ITIN going forward

Rajesh should:
- Use the same ITIN on any future 1040-NR filings
- Keep the ITIN active by filing at least once every 3 years (even if no tax owed, file the return that triggers the ITIN need)
- If Rajesh later becomes SSN-eligible (e.g., if he immigrates to the US in the future), he should rescind the ITIN and switch to SSN

### Why this matters — the cost of letting an ITIN expire

If Rajesh had filed his 2025 1040-NR using the expired ITIN without renewing, the IRS says (How to renew an ITIN page):
- There may be a delay in processing the return
- Certain credits may not be allowed until the ITIN is renewed
- This may result in a reduced refund or penalties and interest

By renewing proactively at the time of filing, Rajesh avoids all of that. The W-7 + 1040-NR submitted together signals the IRS to process the renewal first, then the return.

## Validation checks

- [x] **Renew** box checked at top of W-7
- [x] Reason code (b) — matches the current filing (1040-NR)
- [x] Line 6e Yes; existing ITIN (9XX-78-XXXX) and name listed on Line 6f
- [x] Identification documents same standard as new application (originals or certified copies)
- [x] 2025 Form 1040-NR attached (renewal still requires the underlying return that triggers the ITIN need)
- [x] Form 1042-S attached as evidence of withholding
- [x] Mailing address is Rajesh's actual Mumbai address
- [x] Mailed to ITIN Operation Austin

## Lessons

1. **3-year non-use trigger** is the most common renewal trigger. Filers who leave the US and stop filing returns lose their ITIN after 3 consecutive years. Even one filing in that window (even a $0-tax 1040-NR) keeps the ITIN active.
2. **Renewal is not faster than a new application** — same processing window (7 weeks; 9-11 weeks in peak season or from overseas), same documentation requirements. Don't assume "renewal" means a shortcut.
3. **Same ITIN number** is preserved on renewal — Rajesh's number doesn't change. This matters for prior-year cross-references and 1042-S matching.
4. **Renew only when needed**: an expired ITIN needs renewal only if it will be included on a U.S. federal tax return. An ITIN used only on information returns (e.g., Form 1099) needs no renewal (Instructions for Form W-7, Reminders). A CP48 expiration notice is not, by itself, a reason to file a W-7.
5. **PATH Act 2015 expiration triggers**: 3-year non-use, plus the rule that ITINs assigned before 2013 and never renewed have expired (the middle-digit waves are complete). Rajesh's ITIN was assigned in 2020, so only the 3-year non-use trigger is relevant.
6. **Treaty positions on 1040-NR** require careful Article citation in Schedule OI. Don't assume any one-off US payment to an Indian resident is treaty-exempt — check the specific income type and treaty article.
7. **Plan international refund delivery**: paper checks to foreign addresses can take 6-8 weeks beyond the standard refund timeline; consider opening a US bank account if recurring filings are expected.

## Citations

- IRC §6109 — TIN requirements
- PATH Act of 2015 (Pub. L. 114-113) — ITIN expiration rules (3-year non-use; pre-2013 ITINs)
- Treas. Reg. §301.6109-1(d)(3) — ITIN issuance and renewal
- Pub. 1915 — Understanding Your IRS ITIN (covers renewal procedures)
- Pub. 519 — US Tax Guide for Aliens
- Form W-7 instructions (Rev. December 2024) — renewal box, lines 6e/6f, expired ITINs
- IRS "How to renew an ITIN" page — https://www.irs.gov/individuals/itin-expiration-faqs
- US-India Income Tax Treaty (1989) — Article 15 (Independent Personal Services); verify article numbers and current treaty status
- Form 1042-S instructions — withholding reporting on US-source income to nonresident aliens
- Notice CP48 — IRS notice of ITIN expiration
