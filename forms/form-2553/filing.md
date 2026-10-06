# Filing Form 2553 (transmission to IRS)

How an agent equipped with browser/fax/printing tooling takes a completed Form 2553 draft (produced via `SKILL.md`) and actually files it with the IRS. Form 2553 is **not** an e-file form. The channels are **fax** or **mail** to the service center (Instructions for Form 2553, "Where To File"), plus, for late elections only, attachment to a Form 1120-S (Rev. Proc. 2013-30 §4.03(2)). Pick one, never both, never neither.

Addresses and fax numbers below were checked on 2026-10-06 against the Instructions for Form 2553 (Rev. December 2020), page 3, and https://www.irs.gov/filing/where-to-file-your-taxes-for-form-2553.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

```
Filer wants the fastest delivery, or the deadline is days away?
  → Fax (keep the transmission report and the original form).
    Use Section 1. A same-day certified mail postmark also meets a deadline.

Filer wants proof of filing that the instructions name?
  → Mail by USPS Certified or Registered Mail with Return Receipt
    (or a designated private delivery service). Use Section 2.

Filer is filing late under Rev. Proc. 2013-30 AND attaching to a Form 1120-S?
  → File with the 1120-S where the 1120-S is filed.
    Use Section 3.

Filer wants both a fax and a paper backup?
  → Pick one. Duplicate filings can cause duplicate processing or
    conflicting notices.
```

**Default**: ask the user. Fax is fastest. Note the instructions' list of acceptable proof of filing if the IRS questions whether Form 2553 was filed: a certified or registered mail receipt (timely postmarked) from USPS or a designated private delivery service equivalent, Form 2553 with an accepted stamp, Form 2553 with a stamped IRS received date, or an IRS letter stating Form 2553 was accepted. A fax transmission report is not on that list, so keep it but treat the CP261 as the real proof.

---

## Section 1 — Fax filing

Fax is fastest and cheapest. If the entity files by fax, it keeps the original Form 2553 with its permanent records (Instructions, "Where To File"). The IRS publishes service-center fax numbers on **page 3 of the Form 2553 instructions** and on the where-to-file page; verify before each use.

### Pre-flight

The agent must have:

- A signed, completed Form 2553 with handwritten officer and shareholder signatures (Form 2553 is not on the IRS e-signature list, IRM 10.10.1, Exhibit 10.10.1-2)
- "FILED PURSUANT TO REV. PROC. 2013-30" in the top margin of page 1 if late
- The reasonable-cause and diligence explanation in item I, or as a signed attached statement, if late
- A fax service or physical fax machine the agent (or user) can use
- Confirmation of which IRS service center serves the entity's state (see address table below)
- The user's explicit consent to transmit

### IRS service centers and fax numbers

The two service centers that accept Form 2553 split the country by the state of the entity's principal business, office, or agency. **Always re-verify against the current where-to-file page**; the filing address last changed effective June 18, 2019 (About Form 2553, "Recent developments").

```
Kansas City, MO service center (Kansas City fax)
  States: CT, DE, DC, GA, IL, IN, KY, ME, MD, MA, MI, NH, NJ, NY, NC, OH, PA,
          RI, SC, TN, VT, VA, WV, WI
  Mail address: Department of the Treasury, IRS Service Center,
                Kansas City, MO 64999
  Fax number: 855-887-7734  [verify on Form 2553 instructions p.3]

Ogden, UT service center
  States: AL, AK, AR, AZ, CA, CO, FL, HI, ID, IA, KS, LA, MN, MS, MO, MT, NE,
          NV, NM, ND, OK, OR, SD, TX, UT, WA, WY
  Mail address: Department of the Treasury, IRS Service Center,
                Ogden, UT 84201
  Fax number: 855-214-7520  [verify on Form 2553 instructions p.3]
```

The instructions list only U.S. states and DC. A foreign entity is not eligible to elect (Who May Elect, test 1); if the principal office is outside the U.S., stop and ask a CPA.

### Fax flow (deterministic)

1. **Print the completed Form 2553** to PDF and to paper. The form has 4 pages:
   - Page 1 (Part I items A-I, officer signature)
   - Page 2 (shareholder consents, columns J-N; extra copies if more rows)
   - Page 3 (Part II, only if item F box (2) or (4))
   - Page 4 (Part III QSST and Part IV late classification representations, as applicable)
   - Any attachments (reasonable-cause statement, continuation sheets, Part II statements)
2. **Visually verify** before transmission:
   - Officer signature, title, and date below item I
   - Every required shareholder signed and dated column K
   - Every shareholder's SSN/EIN entered in column M; tax year end in column N
   - Stock ownership in column L sums to 100% (former shareholders -0-)
   - "FILED PURSUANT TO REV. PROC. 2013-30" in the top margin of page 1 if late
   - Item I explanation present if late; Part IV representations completed only if the entity is an LLC without a timely Form 8832
3. **Identify the destination fax number** by looking up the entity's state in the table above
4. **Transmit**. Send the entire packet (Form 2553 + reasonable-cause statement if any) as one fax job. Do not split into multiple sends.
5. **Capture the fax confirmation page** that the fax service prints/displays. This page must show:
   - Date and time transmitted
   - Destination fax number
   - Page count
   - "Successful" / "OK" / equivalent status
   - The agent's sending fax number
6. **Save the fax confirmation page** as a PDF in the user's records, alongside the filed Form 2553. This is the single most important piece of evidence if the IRS later claims the election wasn't received.
7. **Do not also mail.** Duplicate filings can cause duplicate processing or conflicting notices.

### What if the fax fails?

- Busy signal: retry up to 3 times spaced 15 minutes apart
- Persistent failure: the destination fax may be down; verify the number against the where-to-file page, or fall back to mail (Section 2)
- Partial transmission: re-fax the **entire** packet, not just the missing pages

---

## Section 2 — Mail filing

For filers who prefer paper or are filing well in advance of the deadline.

### Pre-flight

Same as fax (signed Form 2553, complete consents, reasonable-cause statement if late). Plus:

- USPS Certified Mail (or Registered Mail) label with Return Receipt (PS Form 3811). A timely postmarked certified or registered mail receipt is on the instructions' list of acceptable proof of filing. A designated private delivery service also works; use the street address from https://www.irs.gov/PDSStreetAddresses
- A printed copy for the user's records

### Mail flow

1. **Assemble the packet**:
   - Form 2553 (printed single-sided, no staples)
   - Reasonable-cause statement attachment (if late)
   - Cover letter (optional but useful) — one paragraph stating "Enclosed please find Form 2553 for [Entity Name], EIN [XX-XXXXXXX], electing S-corporation status effective [date]"
2. **Address the envelope** using the service-center address from the table in Section 1 (state-based)
3. **Send via USPS Certified Mail with Return Receipt**:
   - Certified Mail provides a USPS-stamped mailing date — this is the postmark date for IRC §7502 timely-mailing-as-timely-filing
   - Return Receipt (PS Form 3811) provides proof the IRS received the envelope
4. **Save** the Certified Mail receipt and the returned Form 3811 in the user's records — these are the proof of timely filing
5. **Do not also fax.** See Section 1.

### Timing buffer

USPS delivery to the IRS service centers typically takes 3-7 business days. If the deadline is within 7 days, switch to fax (Section 1) — Certified Mail's postmark protection only works if it actually gets postmarked on time, and counter delays at the post office can wreck that.

---

## Section 3 — Late filing attached to Form 1120-S

When the user is filing late under Rev. Proc. 2013-30 *and* has not yet filed Form 1120-S for the first intended S-corp year, the cleanest path is to attach Form 2553 to the first 1120-S and mail them together.

### When this applies (Rev. Proc. 2013-30 §4.03(2)(a)-(b))

- Entity intended to be S-corp starting tax year YYYY and missed the 2-month-15-day deadline
- Either (a) all Forms 1120-S since the effective date have been filed and Form 2553 goes with the current-year 1120-S, or (b) no income tax or information return has been filed for YYYY or later, and Form 2553 goes with the late Form 1120-S for YYYY while all other delinquent 1120-S returns are filed at the same time
- The 1120-S is filed within 3 years 75 days of the intended effective date (an extension of the 1120-S does not extend this window)
- For an LLC needing Part IV: route (b) conflicts with representation 5 if the first-year 1120-S due date has passed. Stop and refer to a CPA in that case

### Flow

1. Write "**FILED PURSUANT TO REV. PROC. 2013-30**" in the top margin of Form 2553 page 1
2. Complete item I (reasonable cause and diligent actions) or attach the signed statement; complete Part IV only for an LLC without a timely Form 8832
3. Write "**INCLUDES LATE ELECTION(S) FILED PURSUANT TO REV. PROC. 2013-30**" in the top margin of Form 1120-S page 1
4. Attach the completed Form 2553 to Form 1120-S
5. File where the 1120-S is filed (Form 1120-S instructions, "Where To File"), by certified or registered mail if on paper
6. **Do not also fax the 2553 separately**; that creates a duplicate filing

### Alternative

Route (c): send the late Form 2553 directly to the Form 2553 service center (Sections 1-2) within 3 years 75 days. Use it when no 1120-S is ready to file.

---

## Section 4 — Acknowledgment and follow-up

After filing (any channel), the IRS sends a **CP261 notice** confirming the S-corp election was accepted. A determination generally comes within **60 days**; with box Q1 checked, about 90 days more (Instructions, "Acceptance or Nonacceptance of Election").

### State machine

```
Filed → Pending → Accepted (CP261) | Denied (CP264)
```

- **CP261**: Acceptance. Check the effective date on the notice against item E: a later date means the IRS treated the form as not timely for the requested date, and Rev. Proc. 2013-30 relief may be available (CP261 FAQ, https://www.irs.gov/individuals/understanding-your-cp261-notice). Keep the notice permanently; state agencies ask for it (NJ and AR require a copy).
- **CP264**: Form 2553 denied. The notice states the reason; the fix is a new, complete Form 2553, with no waiting period (https://www.irs.gov/individuals/understanding-your-cp264-notice). Typical causes to check: name or EIN mismatch, a missing or invalid consent or signature, a late election without the Rev. Proc. 2013-30 package, incomplete Part II.
- **CP262** is not a 2553 response: it confirms that an S election was *revoked*.
- **No letter within 2 months** (5 months if box Q1 was checked): call the Business & Specialty Tax Line **800-829-4933** (Instructions, "Where To File"). Authorized tax professionals can use the Practitioner Priority Service, **866-860-4259**. Have the EIN, entity name, filing date, and fax report or mail receipt ready.

### Setting follow-up reminders

The agent should automatically schedule:

- **Day 30**: First check — has CP261 arrived? If not, no action yet.
- **Day 60**: Second check — if no CP261, call the IRS.
- **Day 90**: Final check — escalate to a CPA if still no acknowledgment.

### State-level S-corp election

Federal acceptance is **not** automatic state acceptance everywhere. See [`references/state-conformity.md`](./references/state-conformity.md) for details and sources. Most-frequently-needed:

| State | Form / mechanism | Deadline |
|-------|------------------|----------|
| California | No separate election; FTB Form 100S annual return | Annual |
| New York | Form CT-6 (separate state S election) | Any time in the preceding tax year, or by the 15th day of the 3rd month of the tax year |
| New Jersey | No separate election for periods beginning on/after 12/22/2022; register as a corporation filer, submit CP261 and the Shareholder Jurisdictional Consent (TB-105(R)) | With registration or the CBT-100S |
| Arkansas | Form AR1103 with a copy of the IRS acceptance notice | First 75 days of the taxable year |
| Wisconsin | No separate election form identified; Form 5S return | Annual |

Louisiana Form R-6980 is a pass-through entity tax election, not an S-corp election.

Other states (most of them) automatically conform to the federal S-corp election once CP261 is received. Always cross-check the entity's state revenue department site.

---

## Section 5 — Security and consent rules

Non-negotiable.

1. **Never file without explicit user consent** at the moment of transmission. "I authorize you to fax/mail Form 2553 to the IRS on my behalf right now" must be captured.
2. **Never publish, paste, or screenshot Form 2553 publicly.** The form contains every shareholder's full SSN. When archiving copies in shared repos, **redact every SSN** to last-4-only (`XXX-XX-1234`). This includes:
   - Github / Gitlab / public Notion
   - Cloud drives shared with anyone outside the entity
   - Slack / Discord / email screenshots
   - Any AI tool that retains uploaded documents
3. **Never store SSN, EIN, or filer DOB** in agent logs, vector stores, or transcripts beyond the active filing session. Pull at filing time, use, discard.
4. **Never fax to an unverified number.** Always cross-check the destination against the current where-to-file page (or the instructions, page 3) before sending; a misdirected fax exposes every shareholder's SSN.
5. **Always save the fax confirmation or Certified Mail receipt** in the user's secure records, not the agent's transcript.
6. **If anything looks wrong** (consent missing, EIN mismatch, fax failure), **stop and surface the issue**. Do not retry blindly.
7. **One channel only.** Never fax AND mail the same election. Pick one, document it, move on.

---

## Section 6 — Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| CP264 denial: name mismatch | Form 2553 entity name doesn't match IRS EIN records | Get CP575 or Letter 147C (800-829-4933); refile a complete form with the exact name |
| CP264 denial: missing consent | Shareholder or community-property spouse did not sign column K | Get the missing signature; refile the entire form (a timely election may be saved under Reg. §1.1362-6(b)(3)(iii)) |
| CP261 shows a later effective date than item E | Filed late without the Rev. Proc. 2013-30 package | If within 3 years 75 days: file a new Form 2553 with the header, item I explanation, all-period consents, and Part IV if an LLC |
| No CP261 within 2 months | Possibly lost in IRS processing OR fax never received | Call 800-829-4933 with the fax report or mail receipt in hand |
| Fax confirmation says "successful" but IRS denies receipt | Rare — keep the fax confirmation page; resubmit with cover letter referencing original transmission | Refile via mail Certified, attach copy of original fax confirmation |
| State agency demands proof of S-corp status before CP261 arrives | State doesn't accept "pending" | Provide a copy of the filed 2553 + fax confirmation as interim proof |
