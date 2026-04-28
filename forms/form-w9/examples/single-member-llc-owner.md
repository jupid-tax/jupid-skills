# Example: Single-Member LLC Owner (Disregarded Entity, Default Classification)

A complete walkthrough of Form W-9 for the most common and most misfiled case: a freelancer who formed a single-member LLC for liability protection but never made a corporate tax election. This is the canonical "I have an LLC and an EIN — what do I put on the form?" pattern, and it is also the pattern from the Jupid blog companion article.

## The filer

- **Name**: Maya Garcia
- **Business**: Garcia Design LLC — freelance graphic design (logos, brand identity, web mockups)
- **Entity**: Single-member LLC formed in California in 2024
- **Tax election**: None — no Form 2553 (S-corp), no Form 8832 (C-corp). Default = disregarded entity.
- **Has EIN?**: Yes — applied for one when she opened her business bank account
- **Tax year**: 2026 (calendar year filer)

## The trigger

Maya signed a project agreement with a new client, **Acme Brand Co.**, for a $12,000 brand identity package. Acme's accounts-payable team emailed her on April 28, 2026 asking for a completed W-9 before they release the first invoice payment. The email came from `ap@acmebrand.com`, signed by an AP coordinator Maya met during the kickoff call. Existing engagement, known sender → request is legitimate.

## Inputs gathered (Step 1-4 of workflow)

### Step 1 — Verify the requestor

- Requestor: Sarah Chen, AP Coordinator at Acme Brand Co.
- Channel: Client portal (Acme uses a vendor onboarding system that runs through Adobe Sign)
- Existing engagement: Yes — signed SOW + kickoff call in week prior
- Verdict: Legitimate. Proceed.

### Step 2 — US-person status

Maya is a US citizen, born in California. US person → W-9 is the correct form.

### Step 3 — Line 3a classification

Decision tree (`references/tax-classification-decisions.md`, Section B.1):

1. Did Maya form an LLC? **Yes** — Garcia Design LLC, California Articles of Organization filed 2024.
2. Has she filed Form 2553 or Form 8832? **No.**
3. Is the LLC owned by one person or multiple? **One** — Maya is the sole member.

Result: **Single-member LLC, no corporate election → default disregarded entity → Line 3a = "Individual/sole proprietor or single-member LLC."**

The agent confirms back to Maya: "You're filling this out as Individual/sole proprietor, using your personal SSN — not your LLC's EIN. Your LLC has its own EIN, but the IRS treats your LLC as part of you for income tax. Right?" Maya: "Right."

### Step 4 — TIN selection

Per `references/tin-selection.md`: SMLLC default → owner's SSN.

Maya has both:
- Personal SSN: `XXX-XX-1234`
- LLC's EIN: `87-XXXXXXX` (not used on this W-9)

She enters her SSN.

## The completed W-9 draft

```markdown
# Form W-9 — DRAFT (revision March 2024)

## Identity
1. Name (as shown on income tax return):       Maya Garcia
2. Business name / disregarded entity name:    Garcia Design LLC

## Tax classification (Line 3)
3a. Federal tax classification:                Individual/sole proprietor or single-member LLC
    (If LLC) Tax classification letter:        n/a (LLC box NOT checked)
3b. (FATCA pass-through indicator):            blank

## Exemptions (Line 4) — usually blank
Exempt payee code:                             blank
FATCA reporting code:                          blank

## Address (Lines 5-6)
5. Address (street + apt/suite):               1428 Sunset Boulevard, Suite 200
6. City, state, ZIP:                           Los Angeles, CA 90026

## Optional account number(s) (Line 7)
7. List account number(s):                     blank

## Part I — Taxpayer Identification Number
TIN (SSN or EIN):                              XXX-XX-1234
TIN type:                                      SSN

## Part II — Certification
Signature:                                     Maya Garcia (electronic via Adobe Sign)
Date:                                          04/28/2026
Item 2 struck through?                         No (Maya has never received an IRS BUW notice)

## Delivery
Channel:                                       Adobe Sign (Acme's vendor portal)
Recipient (requestor):                         Sarah Chen, AP Coordinator, Acme Brand Co.
Verification of requestor legitimacy:          Existing signed SOW; portal link from known AP email
```

## Why each non-obvious choice

**Why is Line 1 "Maya Garcia" and not "Garcia Design LLC"?** Line 1 is "the name on your income tax return." Maya files Form 1040 with Schedule C — there is no separate LLC tax return because the IRS treats the SMLLC as disregarded. The name the IRS will match against the TIN is the name on the 1040. That's "Maya Garcia." If Maya wrote "Garcia Design LLC" on Line 1 and her SSN in Part I, the IRS TIN-matching system would fail (LLC name doesn't match an SSN's name record). Acme would receive a CP2100 / "B" notice and would have to apply 24% backup withholding until Maya sent a corrected W-9.

**Why is Line 3a "Individual/sole proprietor" and not "Limited liability company"?** This is the single most-misfiled box on Form W-9. The W-9 form's Line 3a explicitly bundles "Individual/sole proprietor or single-member LLC" into the same checkbox. The "Limited liability company" checkbox is only for LLCs that have made a corporate tax election (S-corp or C-corp) OR multi-member LLCs. Maya's LLC has done neither. Checking the LLC box and writing "S" or leaving the letter blank would create a category mismatch that, again, fails IRS TIN matching.

**Why is Part I her SSN, not the LLC's EIN — even though the LLC has an EIN?** Because the LLC is disregarded for federal income tax. The IRS doesn't have a Schedule C or Form 1040 filed under the LLC's EIN — those filings happen under Maya's SSN. The LLC's EIN exists in IRS records only for federal employment taxes (if Maya had employees), some excise taxes, and IRS communication when Maya opens accounts in the LLC's name. For 1099-NEC matching, the IRS expects the SSN of the person on Schedule C — Maya's. **The trap**: Maya checks "Limited liability company" + "S" (because she's heard S-corps are tax-advantageous) + writes her LLC's EIN. The W-9 fails IRS TIN matching → 24% backup withholding starts on her next Acme payment.

**Why is Line 2 "Garcia Design LLC"?** Line 2 is the "business name / disregarded entity name" line. For an SMLLC, this is exactly where the LLC name belongs — it's the disregarded entity name. Acme's vendor system will store both: Line 1 (Maya Garcia) for IRS matching, Line 2 (Garcia Design LLC) for the bill-to / pay-to display.

**Why is Line 4 blank?** Sole proprietors and single-member LLC owners are NEVER exempt from backup withholding under IRC §3406. Code 5 (Corporations) does not apply because Maya is filing as Individual/sole proprietor for tax purposes, not as a corporation. Sole props ALWAYS leave Line 4 blank.

**Why is Adobe Sign the right delivery channel?** Acme's vendor portal already supports Adobe Sign with audit trails meeting IRS Pub 1345 standards (signer identity verified by email + IP + timestamp; tamper-evident document seal). This satisfies the W-9 electronic-signature requirement. Maya should NOT email a scanned W-9 PDF over plain email — the form contains her full legal name + SSN, which is identity-theft-grade data.

## What if Maya had made an S-corp election?

Same scenario, but in March 2026 Maya filed Form 2553 to elect S-corp taxation for her LLC effective January 1, 2026. The W-9 would change as follows:

| Line | Default SMLLC (above) | SMLLC with S-corp election |
|------|----------------------|---------------------------|
| **Line 1** | Maya Garcia | Garcia Design LLC |
| **Line 2** | Garcia Design LLC | blank (or DBA if any) |
| **Line 3a** | Individual/sole proprietor | Limited liability company |
| **LLC letter** | n/a | S |
| **Part I (TIN)** | Maya's SSN | Garcia Design LLC's EIN |

The S-corp election makes the LLC a separate taxpayer for federal income tax. The LLC files Form 1120-S; Maya gets a K-1 and a W-2 from her own LLC. The W-9 reflects the entity, not the owner.

## What if Maya was multi-member?

If Maya had brought in a co-owner (e.g., her partner Joel as a 50/50 LLC member) without a corporate election, the LLC would be taxed as a partnership by default. The W-9 would change to:

- **Line 1**: Garcia Design LLC
- **Line 3a**: Limited liability company
- **LLC letter**: P
- **Part I**: LLC's EIN

(See `examples/freelance-individual-no-llc.md` for the simpler pure-individual case, and `references/tax-classification-decisions.md` Section C for the full multi-member tree.)

## Handoff: what the requestor (Acme) does next

Acme stores Maya's W-9 in their vendor master record. Through 2026, Acme tracks total payments to Garcia Design LLC. At year-end:

- **If total payments ≥ $2,000** (the new OBBBA threshold for tax year 2026 per IRC §6041 as amended by OBBBA Section 112201): Acme files **Form 1099-NEC** by January 31, 2027, reporting the total in Box 1. Payee name on the 1099 = "Maya Garcia" (Line 1 of W-9), payee TIN = Maya's SSN (Part I). Maya gets a copy.
- **If total payments < $2,000**: No 1099-NEC required, but Maya still owes income tax + self-employment tax on the income. Maya must self-report on her Schedule C.
- **No backup withholding**: Maya's W-9 is on file with a valid name + matching TIN, certified, and Item 2 not struck. Acme pays gross.

Maya then uses the 1099-NEC (or her own records if no 1099 issued) to file her 2026 Schedule C — see the companion `forms/schedule-c` skill in this same repository.

## Audit-defense documentation Maya keeps

- Adobe Sign audit trail (PDF download from the portal showing signer email, IP, timestamp)
- Copy of the completed W-9 (encrypted on her local drive, not in plain cloud storage)
- Email thread with Sarah Chen (proves the requestor identity)
- Note on the LLC-vs-SMLLC decision rationale, in case the IRS or her CPA reviews the matching choice

## Sources cited in this draft

- IRS Form W-9 (Rev. March 2024)
- IRS Instructions for Form W-9 (Rev. March 2024)
- IRC §3406 (backup withholding, 24% rate)
- IRC §6041 (information return reporting; threshold $2,000 effective 2026 per OBBBA Section 112201)
- IRC §6109 (TIN furnishing requirement)
- IRC §7701(a)(31) (definition of US person; SMLLC default treatment)
- IRS Publication 1345 (e-signature standards for tax forms)
- Treasury Reg. §301.7701-3 (SMLLC default classification — disregarded entity)
- Companion Jupid blog: [What Is a W-9 Form? Guide for Freelancers and Independent Contractors 2026](https://jupid.com/blog/what-is-a-w9-form-guide-2026)
