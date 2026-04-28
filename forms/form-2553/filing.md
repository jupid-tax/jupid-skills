# Filing Form 2553 (transmission to IRS)

How an agent equipped with browser/fax/printing tooling takes a completed Form 2553 draft (produced via `SKILL.md`) and actually files it with the IRS. Form 2553 is **not** an e-file form. There are exactly two valid channels: **fax** or **mail**. Pick one — never both, never neither.

The agent must produce a complete `SKILL.md`-format draft *first*, then pick a channel from the decision tree below, then execute the channel-specific steps.

---

## Channel decision tree

```
Filer is on or near the deadline (within 7 days)?
  → Fax. Instant timestamp = proof of timely filing.
    Use Section 1.

Filer has more than 7 days of cushion AND wants paper trail / Certified Mail receipt?
  → Mail (USPS Certified Mail with Return Receipt).
    Use Section 2.

Filer is filing late under Rev. Proc. 2013-30 AND attaching to first Form 1120-S?
  → Mail with the 1120-S to the same service center as the 1120-S.
    Use Section 3.

Filer wants both a fax confirmation AND a paper backup?
  → Fax first (gets the timely-filing timestamp), then DO NOT also mail —
    duplicate filings create CP261 confusion and audit-trail noise.
    The faxed copy is the authoritative copy.
```

**Default**: Fax. The timestamped fax confirmation page is the strongest single piece of evidence of timely filing for Form 2553. The IRS generally treats the fax-received date as the postmark for §7502 purposes when the fax goes through.

---

## Section 1 — Fax filing

Fax is fastest, cheapest, and provides an immediate timestamp confirmation that the IRS received the form. The IRS publishes service-center fax numbers on **page 4 of the Form 2553 instructions** — verify each year, they shift between revisions.

### Pre-flight

The agent must have:

- A signed, completed Form 2553 (all shareholder signatures original or qualifying electronic per Reg. §1.1362-6(b)(3))
- "FILED PURSUANT TO REV. PROC. 2013-30" written across the top of page 1 if late
- The reasonable-cause statement attached as a separate page if Part IV is used
- A fax service or physical fax machine the agent (or user) can use
- Confirmation of which IRS service center serves the entity's state (see address table below)
- The user's explicit consent to transmit

### IRS service centers and fax numbers

The two service centers that accept Form 2553 split the country roughly east/west. **Always re-verify against the current Form 2553 instructions page 4** — these numbers are revised periodically.

```
Kansas City, MO service center (Kansas City fax)
  States: CT, DE, DC, GA, IL, IN, KY, ME, MD, MA, MI, NH, NJ, NY, NC, OH, PA,
          RI, SC, TN, VT, VA, WV, WI
  Mail address: Department of the Treasury, IRS Service Center,
                Kansas City, MO 64999
  Fax number: 855-887-7734  [verify on Form 2553 instructions p.4]

Ogden, UT service center
  States: AL, AK, AR, AZ, CA, CO, FL, HI, ID, IA, KS, LA, MN, MS, MO, MT, NE,
          NV, NM, ND, OK, OR, SD, TX, UT, WA, WY
  Mail address: Department of the Treasury, IRS Service Center,
                Ogden, UT 84201
  Fax number: 855-214-7520  [verify on Form 2553 instructions p.4]
```

If the entity's principal place of business is outside the U.S., fax to Ogden.

### Fax flow (deterministic)

1. **Print the completed Form 2553** to PDF and to paper. Pages required:
   - Page 1 (Part I, including officer signature line and most shareholder consent rows)
   - Page 2 (continuation of shareholder consents + Parts II-IV as applicable)
   - Reasonable-cause statement attachment (if late)
2. **Visually verify** before transmission:
   - Officer signature on Line I
   - Every shareholder signed Column K
   - Every shareholder's SSN/EIN entered in Column N
   - Stock ownership in Column M sums to 100%
   - "FILED PURSUANT TO REV. PROC. 2013-30" written across page 1 if late
   - Box 1, 2, 3 checked in Part IV if late
3. **Identify the destination fax number** by looking up the entity's state in the table above
4. **Transmit**. Send the entire packet (Form 2553 + reasonable-cause statement if any) as one fax job. Do not split into multiple sends.
5. **Capture the fax confirmation page** that the fax service prints/displays. This page must show:
   - Date and time transmitted
   - Destination fax number
   - Page count
   - "Successful" / "OK" / equivalent status
   - The agent's sending fax number
6. **Save the fax confirmation page** as a PDF in the user's records, alongside the filed Form 2553. This is the single most important piece of evidence if the IRS later claims the election wasn't received.
7. **Do not also mail.** Duplicate filings cause CP261 confusion and may result in two acknowledgment letters or one rejection citing duplicate filing.

### What if the fax fails?

- Busy signal: retry up to 3 times spaced 15 minutes apart
- Persistent failure: the destination fax may be down — verify the number against the latest Form 2553 instructions page 4, or fall back to mail (Section 2)
- Partial transmission: re-fax the **entire** packet, not just the missing pages

---

## Section 2 — Mail filing

For filers who prefer paper or are filing well in advance of the deadline.

### Pre-flight

Same as fax (signed Form 2553, complete consents, reasonable-cause statement if late). Plus:

- USPS Certified Mail label with Return Receipt (Form 3811) — this provides proof of mailing date and proof of delivery
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

### When this applies

- Entity intended to be S-corp starting tax year YYYY
- Entity missed the 2-month-15-day deadline for YYYY
- Entity is now filing its first Form 1120-S for YYYY
- The 1120-S filing is itself within 3 years 75 days of the intended effective date

### Flow

1. Write "**FILED PURSUANT TO REV. PROC. 2013-30**" across the top of Form 2553 page 1
2. Complete Part IV (boxes 1, 2, 3 checked + reasonable-cause statement attached)
3. Attach the completed Form 2553 to the **front** of Form 1120-S
4. Mail the combined packet to the **1120-S service center** (not the 2553-only service center — they are typically the same, but verify against the current 1120-S instructions)
5. Use Certified Mail with Return Receipt
6. **Do not also fax the 2553 separately** — that creates a duplicate filing

### Why this is the preferred late path

- The Form 1120-S filing itself is evidence the entity intended to be an S-corp from the effective date
- The IRS processes both forms together, reducing risk of mismatch
- The reasonable-cause bar is lower because the user is showing good faith by filing 1120-S (not 1120 / Schedule C)

---

## Section 4 — Acknowledgment and follow-up

After filing (any channel), the IRS sends a **CP261 acknowledgment letter** confirming the S-corp election was accepted. Allow up to **60 days** from filing.

### State machine

```
Filed → Pending → Accepted (CP261) | Rejected (CP262 / other notice)
```

- **CP261**: Acceptance. The election is in effect from the date on Line E. Save this letter forever — it's the single proof of S-corp status. Tax software, banks, and state agencies will ask for it.
- **CP262**: Rejection. Common causes:
  - Entity name doesn't match IRS records (often a comma or "Inc." vs "Corp." mismatch)
  - EIN doesn't match
  - Shareholder consent missing or signed by someone who isn't the shareholder
  - Filed before EIN was issued
  - Late filing without Part IV completed
- **No letter at Day 60**: Call the IRS Practitioner Priority Service line **866-860-4259** (or the Business & Specialty Tax line **800-829-4933** for non-practitioners). Have the EIN, entity name, filing date, and fax confirmation (or Certified Mail receipt) ready.

### Setting follow-up reminders

The agent should automatically schedule:

- **Day 30**: First check — has CP261 arrived? If not, no action yet.
- **Day 60**: Second check — if no CP261, call the IRS.
- **Day 90**: Final check — escalate to a CPA if still no acknowledgment.

### State-level S-corp election

Federal acceptance is **not** automatic state acceptance. Several states require a separate state-level S-corp election filed with the state revenue department. See [`references/state-conformity.md`](./references/state-conformity.md) for the full list. Most-frequently-needed:

| State | Form / mechanism | Deadline |
|-------|------------------|----------|
| California | FTB Form 100S (S-corp return) — federal election conforms automatically, but state files 100S | Annual |
| New York | Form CT-6 (separate state S election) | Within 2½ months of effective date or any prior year |
| New Jersey | Form CBT-2553 (separate state S election) | Within 1 month of federal effective date |
| Arkansas | Form AR1103 | Within 75 days of federal effective date |
| Louisiana | Form R-6980 | Within 30 days of federal acknowledgment |
| Wisconsin | Schedule 5K-1 conformity (no separate election but check Form 5S instructions) | Annual |

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
4. **Never fax to an unverified number.** Always cross-check the destination against the current Form 2553 instructions page 4 before sending. Bad actors have set up lookalike fax numbers to harvest SSNs from misdirected 2553s.
5. **Always save the fax confirmation or Certified Mail receipt** in the user's secure records, not the agent's transcript.
6. **If anything looks wrong** (consent missing, EIN mismatch, fax failure), **stop and surface the issue**. Do not retry blindly.
7. **One channel only.** Never fax AND mail the same election. Pick one, document it, move on.

---

## Section 6 — Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| CP262 rejection: "name mismatch" | Form 2553 entity name doesn't match IRS EIN records | Pull IRS EIN confirmation letter (147C); refile with exact-match name |
| CP262: "missing consent" | Shareholder forgot Column K signature or community-property spouse missed signing | Get missing signature; refile entire form |
| CP262: "late, no relief claim" | Filed after deadline without Part IV completed | Refile with "FILED PURSUANT TO REV. PROC. 2013-30" + Part IV + reasonable-cause statement |
| No CP261 by Day 60 | Possibly lost in IRS processing OR fax never received | Call PPS line 866-860-4259 with fax confirmation in hand |
| Fax confirmation says "successful" but IRS denies receipt | Rare — keep the fax confirmation page; resubmit with cover letter referencing original transmission | Refile via mail Certified, attach copy of original fax confirmation |
| State agency demands proof of S-corp status before CP261 arrives | State doesn't accept "pending" | Provide a copy of the filed 2553 + fax confirmation as interim proof |
