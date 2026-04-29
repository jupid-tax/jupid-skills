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
| Software rejects 5472 with "missing related party EIN" | Foreign related party has no US EIN | Use foreign tax ID with appropriate prefix; if no foreign tax ID, leave blank with notation |
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
- Pro-forma Form 1120 — completed with:
  - Entity name, EIN, address
  - Date incorporated
  - State of organization
  - **"FOREIGN-OWNED U.S. DE" notation** at top of form (handwritten or
    typed) per Form 5472 instructions
  - Income, deduction, tax lines: typically all zeros
  - Schedule attachments: Form 5472(s), nothing else needed
- Foreign owner's identification (name, address, country, foreign tax
  ID if any)
- US EIN for the DE — obtain via Form SS-4 if not already held. Foreign
  owners can apply for an EIN by phone (267-941-1099, IRS International
  Tax Line) or by mail/fax of SS-4. The DE needs a US EIN even with no
  US income.
- Printer, fax machine OR fax service (e.g., HelloFax, eFax,
  RingCentral)
- Postage and envelope if mailing instead of faxing

### Step 1 — Print and assemble the package

1. Print pro-forma Form 1120 (single-sided, full size)
2. Write "FOREIGN-OWNED U.S. DE" in capital letters at the top of page
   1 of Form 1120 (typed in PDF or handwritten on print)
3. Print Form 5472 for each related party (one Form 5472 per related
   party)
4. Sign Form 1120 in the corporate officer signature block. The
   foreign owner can sign as "Owner" or as a corporate officer
   designation (the DE may or may not have a formal officer structure;
   "Member" or "Manager" is typical for an LLC). Wet ink or digital
   signature acceptable on the printed form (the IRS accepts digital
   signatures on most paper-filed forms since IRS Notice 2020-XX
   guidance — verify current state).
5. Stack: Form 1120 (top), then each Form 5472, then any supporting
   schedules. Single staple in upper-left corner.

### Step 2 — Choose between fax and mail

Form 5472 instructions (current revision) specify a **fax number** for
filing pro-forma 1120 + 5472:

- **Fax**: **855-887-7737** (verify against current Form 5472
  instructions before sending — the IRS has changed this number in the
  past)
- **Mail address**:
  ```
  Internal Revenue Service
  1973 N Rulon White Blvd.
  M/S 6112, Attn: PIN Unit
  Ogden, UT 84404
  ```
  (Verify current address against Form 5472 instructions; the IRS shifts
  service center addresses periodically)

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
3. The postmark date is the filing date (under IRC §7502
   timely-mailing-as-timely-filing rule, applies to designated private
   delivery services per Notice 2016-30)
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
1120 + 5472. Silence after 6+ months means the filing was processed
without issues. If the user receives a notice (often a CP-210 or Letter
2205), respond promptly with documentation.

A common notice: **"We have not received your Form 1120"** — sent
because the IRS records show a corporate EIN but no return on file.
Sometimes the pro-forma 1120 + 5472 is misfiled internally. Respond
with proof of the original fax/mail filing.

### Due date

- **Due date**: April 15 (15th day of 4th month after end of DE's tax
  year — calendar year by default for DEs)
- **Extension**: Form 7004 grants automatic 6-month extension to October
  15. File Form 7004 by April 15 via the same fax number
  (855-887-7737) or by mail to the same Ogden address.
- **For foreign owners outside the US**: the automatic 2-month
  extension for "abroad" filers (June 15) does NOT apply to a US DE.
  The DE files on the corporate calendar even if its foreign owner has
  abroad-extension privileges.

### Penalty exposure for late or missed filing

- **$25,000 per related party per year** under IRC §6038A(d)(1)
- **Continuing $25,000 every 30 days** after IRS notice if not corrected
- For a DE with a single foreign owner, that's $25,000/year minimum if
  not filed; $25,000/year + $25,000/30 days if a notice is issued and
  ignored

The **First-Time Abate program does NOT apply** to §6038A penalties (per
IRM 20.1.9 — international information return penalties are outside FTA
scope). The only defense is **reasonable cause** under §6038A(d)(3),
which requires affirmative documentation:

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
(paper), the user can request an account transcript to confirm the
1120 is on file (the transcript shows TC 150 = "Original return
posted").

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
| User receives CP-210 / Letter 2205 (failure to file) | IRS shows no 5472 on file | Re-fax or re-mail with reasonable cause statement; cite original filing date if you have proof |
| User receives $25,000 penalty notice | IRS believes 5472 was missing or incomplete | Respond within 30 days with reasonable cause statement OR proof of filing |
| Fax bounces / busy signal | IRS fax number changed or temporarily unavailable | Verify current number in Form 5472 instructions; switch to mail filing |
| Mail returned undeliverable | Wrong service center address | Verify against current Form 5472 instructions and re-send |
| User filed pro-forma 1120 to wrong address (e.g., to filer's state service center) | Type 3 DEs use Ogden specifically | Re-file at correct Ogden address; document original filing for reasonable cause |
| Form 5472 "missing" but Form 1120 is on file | 5472 detached from 1120 in IRS system | Re-submit 5472 only with cover letter referencing the 1120 |
| EIN mismatch between 5472 and 1120 | Two different EINs entered | Use the same EIN consistently; the DE has only one EIN |
| Foreign owner has no US tax ID and no foreign tax ID | Some jurisdictions don't issue tax IDs to individuals | Use the foreign owner's full legal name + address + country; mark ID field "None" with notation |

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
