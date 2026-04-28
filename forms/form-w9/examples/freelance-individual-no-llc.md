# Example: Freelance Individual / Sole Proprietor (No LLC, No EIN)

A complete walkthrough of Form W-9 for the simplest possible case: an individual freelancer operating under their own name, with no LLC, no DBA, and no EIN. Personal name on Line 1, SSN in Part I, every other line either filled with the obvious value or left blank.

This is the baseline pattern. The other examples (`single-member-llc-owner.md`, `s-corp-shareholder-employee.md`) layer entity complexity on top of this; if the user describes a situation simpler than this, fall back here.

## The filer

- **Name**: David Kim
- **Business**: Freelance technical writer (API documentation, developer guides) — operating under his own personal name, no DBA
- **Entity**: None — David is an individual, no LLC, no corporation
- **Has EIN?**: No — David never applied for one; he uses his SSN for everything
- **Tax year**: 2026 (calendar year filer)

## The trigger

David accepted a 4-month writing contract from **Stripe-like Devtools Inc.** to produce API reference docs. The hiring manager Sarah introduced him via email to **Marcus Lee**, the AP coordinator, who sent David a DocuSign link asking for a completed W-9 before they release the first milestone payment ($3,500 due on completion of the first deliverable). The DocuSign envelope came from Marcus's verified `@devtools.com` email — same domain as the offer letter David already signed. Existing engagement, verified sender → request is legitimate.

## Inputs gathered (Step 1-4 of workflow)

### Step 1 — Verify the requestor

- Requestor: Marcus Lee, AP Coordinator at Stripe-like Devtools Inc.
- Channel: DocuSign envelope from `marcus@devtools.com`
- Existing engagement: Yes — countersigned offer letter from prior week, intro from hiring manager
- Verdict: Legitimate. Proceed.

### Step 2 — US-person status

David is a US citizen, born in Oregon, currently living in Brooklyn, NY. US person → W-9 is the correct form.

### Step 3 — Line 3a classification

Decision tree (`references/tax-classification-decisions.md`, Section A):

1. Did David form an LLC? **No.**
2. Did he file Articles of Incorporation as a corporation? **No.**
3. Is he in a partnership? **No.**
4. Therefore: **Individual / sole proprietor.**

Result: **Line 3a = "Individual/sole proprietor or single-member LLC"** (the box covers both individuals with no entity AND single-member LLCs by default — David is the first case).

The agent confirms back to David: "You're filling this out as Individual/sole proprietor, using your personal SSN. No LLC, no EIN — just you. Right?" David: "Right."

### Step 4 — TIN selection

Per `references/tin-selection.md`: Individual/sole proprietor → SSN.

- David's SSN: `XXX-XX-5678`
- No EIN to consider.

### Step 5 — Line 4 (exemption codes)

Sole proprietors / individuals are NEVER exempt from backup withholding (per `references/backup-withholding.md`). Code 5 applies only to corporations. David has no FATCA-reportable foreign accounts. **Both fields blank.**

## The completed W-9 draft

```markdown
# Form W-9 — DRAFT (revision March 2024)

## Identity
1. Name (as shown on income tax return):       David Kim
2. Business name / disregarded entity name:    blank

## Tax classification (Line 3)
3a. Federal tax classification:                Individual/sole proprietor or single-member LLC
    (If LLC) Tax classification letter:        n/a (LLC box NOT checked)
3b. (FATCA pass-through indicator):            blank

## Exemptions (Line 4) — usually blank
Exempt payee code:                             blank
FATCA reporting code:                          blank

## Address (Lines 5-6)
5. Address (street + apt/suite):               325 Atlantic Avenue, Apt 3C
6. City, state, ZIP:                           Brooklyn, NY 11201

## Optional account number(s) (Line 7)
7. List account number(s):                     blank

## Part I — Taxpayer Identification Number
TIN (SSN or EIN):                              XXX-XX-5678
TIN type:                                      SSN

## Part II — Certification
Signature:                                     David Kim (electronic via DocuSign)
Date:                                          04/28/2026
Item 2 struck through?                         No (David has never received an IRS BUW notice)

## Delivery
Channel:                                       DocuSign (Devtools' standard onboarding envelope)
Recipient (requestor):                         Marcus Lee, AP Coordinator, Stripe-like Devtools Inc.
Verification of requestor legitimacy:          Existing countersigned offer letter; envelope from known AP email
```

## Why each non-obvious choice

**Why is Line 1 just "David Kim" with no extras?** Line 1 is the name on David's federal income tax return. He files Form 1040 as "David Kim" — that's exactly what goes on Line 1. No middle initial unless it's on the return; no "DBA" suffix; no "freelance writer" descriptor. The IRS TIN-matching system compares Line 1 against the SSA's record for the SSN — "David Kim" matches; "David Kim, Freelance Writer" does not.

**Why is Line 2 blank?** Line 2 is for a separate business / DBA / disregarded-entity name. David has none — he operates under his own legal name. Leaving it blank is correct. Filling it with "Freelance Technical Writing" or similar would be wrong — that's a description of his work, not a registered business name.

**Why is Line 3a "Individual/sole proprietor" and not just "Individual"?** Because the W-9 form bundles the two into one checkbox: "Individual/sole proprietor or single-member LLC." A "sole proprietor" for federal tax purposes is just an individual operating a business under their own name (or DBA) without forming an entity. David's Schedule C income makes him a sole proprietor for tax purposes — even though there's no formal "sole proprietorship" filing at the state or federal level. The tax classification follows from the business activity, not from a registration.

**Why doesn't David need an EIN?** EINs are useful but not required for individual sole proprietors. David could apply for one (free at IRS.gov, instant issuance) for privacy reasons — to avoid sharing his SSN with every client. But even if he had one, the IRS instructions say sole proprietors should enter the **SSN** on W-9, not the EIN. So getting an EIN doesn't change Line 1 ("David Kim") or Part I (SSN). For now, David has no EIN, so there's nothing to choose between.

**Why is Lines 5-6 his apartment address and not a PO Box or a coworking address?** The address on the W-9 is where Devtools will mail his year-end 1099-NEC and where the IRS expects to find him for correspondence. David files Form 1040 from his Brooklyn address — the W-9 address must match. A PO Box would be acceptable if David files his 1040 with a PO Box; he doesn't, so the apartment address is correct. A coworking address would NOT match his tax-return address and is wrong here.

**Why is Item 2 NOT struck?** Item 2 is the certification that David is not subject to backup withholding for under-reporting interest or dividends. He has never received an IRS notice on this — so he can sign the certification as-is. Striking Item 2 only applies if the IRS has actively notified the user that they ARE subject to BUW for past under-reporting. This is rare; most filers leave it unstruck.

**Why DocuSign rather than email?** The W-9 contains David's full legal name + SSN — identity-theft-grade data. Emailing it as a plain PDF attachment exposes it to interception, mailbox compromise, and forwarding. DocuSign provides:
- Signer identity verification (Marcus's authenticated session + David's authenticated session)
- Tamper-evident audit trail (any post-signature modification breaks the seal)
- Encrypted transit and storage
- IRS Pub 1345 compliance for electronic-signature standards

This satisfies the secure-delivery requirement without any extra effort on David's part.

## Why this is the simplest possible W-9 case

Almost every other W-9 scenario adds at least one of these complications:

| Complication | Where it appears |
|--------------|------------------|
| LLC with no corporate election | `single-member-llc-owner.md` — owner's personal name on Line 1, but LLC name on Line 2 |
| LLC with S-corp / C-corp election | `single-member-llc-owner.md` (footnote) — LLC name on Line 1, EIN in Part I |
| Multi-member LLC | `tax-classification-decisions.md` Section C — LLC name on Line 1, "Limited liability company" + P (or S/C), EIN in Part I |
| State-formed corporation | `s-corp-shareholder-employee.md` — corp name on Line 1, S Corporation box, corp EIN in Part I, Code 5 exemption |
| Partnership | `tax-classification-decisions.md` Section E — partnership name on Line 1, Partnership box, partnership EIN in Part I |
| Trust / estate | `tax-classification-decisions.md` Section F — trust/estate name, trust/estate EIN |
| Sole prop with EIN | TIN selection nuance — IRS prefers SSN even when filer has EIN; see `tin-selection.md` |
| ITIN instead of SSN | filer is a US person but ineligible for SSN; uses ITIN (also goes in SSN boxes) |

David's case has none of these. Personal name, SSN, no entity, no exemption codes. Three minutes from start to signed delivery.

## Handoff: what the requestor (Devtools) does next

Devtools stores David's W-9 in their vendor / contractor master record. Through 2026, Devtools tracks total payments to David Kim. At year-end:

- **If total payments ≥ $2,000** (the new OBBBA threshold for tax year 2026 per IRC §6041 as amended by OBBBA Section 112201): Devtools files **Form 1099-NEC** by January 31, 2027, reporting the total in Box 1. Payee name = "David Kim", payee TIN = his SSN. David gets a copy.
- **If total payments < $2,000**: No 1099-NEC required. David still owes income tax + self-employment tax on the income and must self-report on Schedule C.
- **No backup withholding**: David's W-9 is on file with a valid name + matching TIN, certified, and Item 2 not struck. Devtools pays gross.

David then uses the 1099-NEC (or his own records if no 1099 issued) to file his 2026 Schedule C — see the companion `forms/schedule-c` skill. The Schedule C net profit also flows to Schedule SE for self-employment tax (15.3% on 92.35% of net earnings, up to the Social Security wage base for the SS portion).

## Audit-defense documentation David keeps

- DocuSign completion certificate (signer email, IP, timestamp, tamper-evident seal)
- Copy of the signed W-9 (encrypted on his local drive, not in plain cloud storage)
- Email thread with Marcus Lee establishing the request was legitimate
- His personal tax-return address record showing it matches the W-9 address

## Sources cited in this draft

- IRS Form W-9 (Rev. March 2024)
- IRS Instructions for Form W-9 (Rev. March 2024)
- IRC §3406 (backup withholding, 24% rate; sole proprietors not exempt)
- IRC §6041 (information return reporting; threshold $2,000 effective 2026 per OBBBA Section 112201)
- IRC §6109 (TIN furnishing requirement; SSN sufficient for individuals)
- Form 1099-NEC (year-end information return for nonemployee compensation)
- IRS Publication 1345 (e-signature standards for tax forms)
- Companion Jupid blog: [What Is a W-9 Form? Guide for Freelancers and Independent Contractors 2026](https://jupid.com/blog/what-is-a-w9-form-guide-2026)
