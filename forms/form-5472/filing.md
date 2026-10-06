# Filing Form 5472

How an agent equipped with browser/printing/fax tooling helps the user
file Form 5472 with the IRS. Filing channel depends on which type of
reporting corporation:

- **Type 1** (US C-corp with foreign owner) → Form 5472 attached to Form
  1120, e-fileable in standard channels
- **Type 2** (foreign corp with US ECI) → Form 5472 attached to Form
  1120-F, e-fileable in some channels
- **Type 3** (foreign-owned US DE) → Form 5472 attached to **pro-forma
  Form 1120**, **NOT e-fileable** — paper filing via fax or mail to a
  specific Ogden address

The agent must produce a complete `SKILL.md`-format draft *first*, then
identify the type, then execute the channel-specific steps.

---

## Channel decision tree

```
Reporting corporation Type?
  ├─ Type 1 (US C-corp, 25% foreign-owned) → Section 1: 1120 + 5472 e-file
  ├─ Type 2 (Foreign corp w/ US ECI) → Section 2: 1120-F + 5472
  └─ Type 3 (Foreign-owned US DE) → Section 3: pro-forma 1120 + 5472 paper/fax
```

---

## Section 1 — Type 1: US C-corp with Form 1120 + Form 5472

### Pre-flight

Agent must have:

- Completed Form 5472 draft for each related party
- Completed Form 1120 (with all schedules — Schedule M-1, M-2, M-3 if
  required)
- Reporting corporation's full identification, EIN
- Foreign related parties' identifying details
- E-file PIN or signature authority for the corporate officer
- IRS-accepted tax software (commercial) — Form 5472 attaches to 1120 in
  most major corporate tax packages

### Browser flow

Most large corporations use enterprise tax software (CCH, Thomson
Reuters, etc.) that handles 1120 + 5472 e-file natively. For smaller
corporations using DIY software:

1. Sign in to chosen tax software (TurboTax Business, H&R Block
   Business, TaxAct Business, or equivalent)
2. Start a new corporate return for the tax year
3. Fill the 1120 income, deductions, schedules
4. Navigate to the "International / Foreign Owner" section
5. Add a Form 5472 attachment for each related foreign party
6. Software typically maps to the Form 5472 fields directly
7. Review each Form 5472 against the draft before submission
8. E-file the complete package (1120 + all 5472s + schedules)

**Capture the e-file confirmation** — typically arrives within 24-48
hours via the software's status page. Save the IRS submission ID.

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Software rejects 5472 with "missing related party EIN" | Foreign related party has no US EIN | Enter the reference ID the corporation assigned (lines 4b(2) / 8b(2)) and the FTIN if any (4b(3) / 8b(3)) per the Instructions for Form 5472 |
| 1120 e-file rejected for inconsistency between 1120 and 5472 amounts | Cross-form mismatch | Reconcile (interest expense on 1120 must match interest paid on 5472) |
| Software doesn't support Form 5472 | Some DIY packages omit international forms | Switch to enterprise software, or paper file |

---

## Section 2 — Type 2: Foreign corp with Form 1120-F + Form 5472

### Pre-flight

Same as Section 1 plus:

- Foreign corporation's home country incorporation documents
- US trade/business activity description
- Branch profits tax computation if applicable (IRC §884)
- Treaty-based return position statements (Form 8833) if applicable

### Filing channels

- **E-file**: Form 1120-F is e-fileable for many foreign corporations
  (the IRS expanded e-file mandates over recent years; check current
  rules). Major corporate tax software supports 1120-F + attached 5472.
- **Paper file**: If e-file not available, mail to the IRS service
  center indicated in current Form 1120-F instructions (typically
  Ogden or Austin depending on the foreign corp's specific situation).

### Due date and extension

- **Due date**: 15th day of 4th month after end of foreign corp's tax
  year, IF the foreign corp has an office or place of business in the
  US. If no US office, the due date is 15th day of **6th month** after
  fiscal year-end.
- **Extension**: Form 7004 grants automatic 6-month extension. File by
  the original due date.

---

## Section 3 — Type 3: Foreign-owned US DE with pro-forma 1120 + Form 5472

This is the most common and most-bungled 5472 scenario. The DE has no
US tax liability of its own (income flows through to the foreign owner),
but must file a pro-forma 1120 + Form 5472 every year.

### Pre-flight

Agent must have:

- Completed Form 5472 draft for each related party (typically just the
  foreign owner)
- Pro-forma Form 1120 — completed with only (Instructions for Form
  5472, When and Where To File):
  - Entity name and address
  - Item B: EIN
  - Item E: initial return / final return / name change / address
    change boxes as applicable
  - **"Foreign-owned U.S. DE" written across the top** of the Form 1120
  - Every other line left blank
  - Attachments: Form 5472(s) and the Part V statement
- Foreign owner's identification (name, address, country, foreign tax
  ID if any)
- US EIN for the DE — obtain via Form SS-4 if not already held. Foreign
  owners with no US residence or place of business can apply by phone
  (267-941-1099, not toll free), by fax (855-215-1627 from within the
  US, 304-707-9471 from outside), or by mail (Instructions for Form
  SS-4, Rev. December 2025; see [`form-ss-4`](../form-ss-4/SKILL.md)).
  The DE needs a US EIN even with no US income.
- Printer, fax machine OR fax service (e.g., HelloFax, eFax,
  RingCentral)
- Postage and envelope if mailing instead of faxing

### Step 1 — Print and assemble the package

1. Print pro-forma Form 1120 (single-sided, full size)
2. Write "FOREIGN-OWNED U.S. DE" in capital letters at the top of page
   1 of Form 1120 (typed in PDF or handwritten on print)
3. Print Form 5472 for each related party (one Form 5472 per related
   party)
4. Signature: the Form 5472 instructions list only name, address,
   items B and E as required on the pro forma 1120 and do not address
   the signature block. ASK the user or CPA; a common practice is for
   the foreign owner to sign as the LLC's "Member" or "Manager". Use a
   wet-ink signature unless the CPA confirms the IRS currently accepts
   an electronic signature on this paper filing.
5. Stack: Form 1120 (top), then each Form 5472, then any supporting
   schedules. Single staple in upper-left corner.

### Step 2 — Choose between fax and mail

The Instructions for Form 5472 (Rev. December 2024), "Dedicated mailing
address", specify the only two channels for a foreign-owned DE. These
filers do not use the addresses in the Instructions for Form 1120:

- **Fax**: **855-887-7737** (300 DPI or higher)
- **Mail address**:
  ```
  Internal Revenue Service
  1973 Rulon White Blvd
  M/S 6112 Attn: PIN Unit
  Ogden, UT 84201
  ```

Re-check both against the instructions current on the filing date
(https://www.irs.gov/forms-pubs/about-form-5472).

**Fax is preferred** for foreign filers because:
- No postal delivery delays from abroad
- IRS confirmation is faster (the fax transmission report serves as
  proof of filing date)
- No risk of international mail loss

**Mail is required if** the package exceeds typical fax page limits
(rare for a DE with one related party) or if the foreign owner is in a
country where international fax is unreliable.

### Step 3 — Send via fax (if fax route chosen)

1. Confirm fax number from current-year Form 5472 instructions
2. Use a fax service that produces a transmission report with date,
   time, and recipient
3. Send the complete package
4. Keep the **fax transmission report** as proof of timely filing
5. The fax serves as the original filing — no need to also mail

### Step 4 — Send via mail (if mail route chosen)

1. Use **USPS Priority Mail International** (or equivalent express
   service from foreign country) with **tracking**
2. Get a **certified mail receipt** or international tracking number
3. The postmark date is the filing date under the IRC §7502
   timely-mailing-as-timely-filing rule, which also covers IRS-designated
   private delivery services (current list at IRS.gov/PDS; a PDS cannot
   deliver to a P.O. box, per the Instructions for Form 1120 (2025))
4. International mail from outside the US: timely-mailing rules apply
   only to USPS and IRS-designated private delivery services. If using
   foreign postal service, the filing date is the date of IRS receipt,
   not postmark — leave extra time.

### Step 5 — Make a complete copy

Retain a digital and paper copy of the entire package for the user's
records, including the fax transmission report or mail tracking
confirmation.

### Step 6 — Wait for IRS processing

The IRS does not send routine acknowledgments for paper-filed pro-forma
1120 + 5472. Silence generally means no issue was raised. If the user
receives a notice (for example a penalty notice or a request for a
missing return), respond by the deadline on the notice with
documentation.

A common notice: **"We have not received your Form 1120"** — sent
because the IRS records show a corporate EIN but no return on file.
Sometimes the pro-forma 1120 + 5472 is misfiled internally. Respond
with proof of the original fax/mail filing.

### Due date

- **Due date**: the due date of Form 1120: April 15 for a calendar-year
  DE (the DE uses its owner's U.S. tax year or, if none, the calendar
  year)
- **Extension**: Form 7004 grants automatic 6-month extension to October
  15. File Form 7004 by April 15 via the same fax number
  (855-887-7737) or by mail to the same Ogden address, with
  "Foreign-owned U.S. DE" written across the top and the Form 1120 code
  on Part I, line 1 (Instructions for Form 5472, Extension of time to
  file).
- **For foreign owners outside the US**: Treas. Reg. §1.6081-5 gives an
  automatic extension to the 15th day of the 6th month to a domestic
  corporation that transacts its business and keeps its books and
  records outside the US and Puerto Rico (Instructions for Form 7004,
  Line 4). The Form 5472 instructions do not say whether a foreign-owned
  DE's pro forma 1120 can use it. Do not rely on it: file by April 15
  or file Form 7004, and ask the CPA.

### Penalty exposure for late or missed filing

- **$25,000 per related party per year** under IRC §6038A(d)(1) and
  Treas. Reg. §1.6038A-4(a)(3)
- **Additional $25,000 per 30-day period (or part)** if the failure
  continues more than 90 days after IRS notice (§6038A(d)(2))
- For a DE with a single foreign owner, that's $25,000/year if not
  filed; plus $25,000 per 30-day period once 90 days pass after a
  notice that is ignored

The **First-Time Abate program does not apply** to Form 5472 penalties:
IRM 20.1.1.3.3.2.1 lists Form 5472 among returns where FTA relief is
not applicable (it points to IRM 20.1.9 for an exception). The normal
defense is **reasonable cause** under §6038A(d)(3) and Treas. Reg.
§1.6038A-4(b), which requires an affirmative showing:

- The user (foreign owner) was unaware of the filing requirement and
  acted promptly upon discovery
- The user relied on a tax professional who failed to advise — and the
  user disclosed all facts to the professional
- A natural disaster, illness, or similar circumstance prevented timely
  filing

A "reasonable cause statement" attached to a late filing improves the
chance of penalty abatement but does not guarantee it.

---

## Section 4 — Submission state machine

After filing (any channel), the form moves through:

1. **Submitted** — fax sent, mail postmarked, or e-file accepted
2. **Acknowledged** — only for e-filed Type 1/2; Type 3 paper has no
   acknowledgment
3. **Processed** — IRS ingests the form
4. **Action** — silence (most common), notice of incomplete filing, or
   penalty assessment

There is no "Where's My 5472" tool. For Type 1 (1120 e-file), the
e-file software status page shows acceptance/rejection. For Type 3
(paper), the fax transmission report or mail tracking is the proof of
filing; the user can also request a business account transcript for
the EIN and have the CPA read it.

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file without explicit user consent** — capture the user's
   "yes, file this" before sending fax / mailing / submitting e-file
2. **Never store EIN, SSN, ITIN, or foreign tax ID** in agent logs,
   vector stores, or transcripts. Pull at filing time, use, discard.
3. **For fax filing**, use a fax service with secure transmission (TLS
   for the API) — avoid sending sensitive identifying information over
   non-secure fax services
4. **Always retain a complete copy** of the filed package + transmission
   receipt in the user's account, not the agent's
5. **If anything looks wrong** — related party identifying info doesn't
   match user's description, transaction amounts don't reconcile to
   1120, EIN format is wrong — stop and surface the issue before the
   package is filed

---

## Failure modes summary

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| User receives a notice that the return or Form 5472 was not filed | IRS shows no 5472 on file | Re-fax or re-mail with reasonable cause statement; cite original filing date if you have proof |
| User receives $25,000 penalty notice | IRS believes 5472 was missing or incomplete | Respond by the deadline on the notice with reasonable cause statement OR proof of filing |
| Fax bounces / busy signal | IRS fax number changed or temporarily unavailable | Verify current number in Form 5472 instructions; switch to mail filing |
| Mail returned undeliverable | Wrong service center address | Verify against current Form 5472 instructions and re-send |
| User filed pro-forma 1120 to wrong address (e.g., to filer's state service center) | Type 3 DEs use Ogden specifically | Re-file at correct Ogden address; document original filing for reasonable cause |
| Form 5472 "missing" but Form 1120 is on file | 5472 detached from 1120 in IRS system | Re-submit 5472 only with cover letter referencing the 1120 |
| EIN mismatch between 5472 and 1120 | Two different EINs entered | Use the same EIN consistently; the DE has only one EIN |
| Foreign owner has no US tax ID and no foreign tax ID | Some jurisdictions don't issue tax IDs to individuals | Assign a reference ID on line 4b(2) (alphanumeric, no spaces or special characters, up to 50 characters, same every year) and enter "None" or "N/A" on line 4b(3) (Instructions for Form 5472) |

---

## Coordination with the foreign owner's own US tax return

A foreign-owned US DE is often only one piece of the foreign owner's US
tax footprint:

- **If the foreign owner is an individual with US-source income from
  the DE** (e.g., the DE has US-source ECI like rental real estate),
  the foreign owner files **Form 1040-NR** for their personal US
  income tax. The DE's pro-forma 1120 + 5472 is separate.
- **If the foreign owner is a foreign corporation with US ECI through
  the DE**, the foreign corp files **Form 1120-F**. The DE's
  pro-forma 1120 + 5472 is separate.
- **If the DE has no US activities at all** (e.g., a Delaware LLC used
  only as a holding vehicle for non-US assets), the foreign owner may
  have no individual US tax filing requirement. The DE still files
  pro-forma 1120 + 5472 every year regardless.

The skill should remind the user that the pro-forma 1120 + 5472 is the
DE's compliance, separate from the foreign owner's personal compliance.
