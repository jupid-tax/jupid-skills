# Filing Form 3115

How an agent files Form 3115 to request consent for an accounting method change. Form 3115 has unusual logistics: most filings are **automatic consent** with a duplicate-copy requirement, and a smaller subset are **non-automatic** with a user fee and IRS review.

The agent must produce a complete `SKILL.md`-format draft *first*, then determine the filing path, then execute.

---

## Channel decision tree

```
Change is on the automatic-consent list (DCN matches in Rev. Proc. 2024-23 or successor)?
  → Automatic consent path. Section 1.

Change is NOT on the automatic-consent list?
  → Non-automatic (advance consent) path. Section 2.

Change involves a method that's specifically excluded from automatic consent
(e.g., listed in Section 5 of Rev. Proc. 2015-13 — under IRS exam, prior change
within 5 years, etc.)?
  → Non-automatic, even if DCN exists. Section 2.

Taxpayer is currently under IRS examination?
  → Special rules apply. Verify whether the issue under exam includes the
    accounting method being changed. Generally non-automatic in this case;
    may need IRS area office consent.
```

---

## Section 1 — Automatic consent filing

### Pre-flight

The agent must have:

- The user's permission to prepare and file
- Filer's full legal name, SSN/EIN, mailing address
- The completed Form 3115 draft from `SKILL.md`
- The §481(a) adjustment schedule
- The DCN number from the current Rev. Proc.
- The current-year tax return draft (Form 1040, 1120, 1120-S, or 1065) — Form 3115 attaches to this

### Two copies required

Automatic consent under Rev. Proc. 2015-13 / Rev. Proc. 2024-23 requires:

1. **Original Form 3115** attached to the **timely-filed federal tax return** for the year of change
2. **Duplicate copy of Form 3115** mailed (or e-faxed in some recent updates — verify) **separately** to the IRS Ogden Service Center

Both must be filed by the **due date of the return including extensions**.

### Mailing the duplicate copy

Address (verify in the current Rev. Proc. — Ogden address has been the consistent address for automatic-consent duplicates for several years):

```
Internal Revenue Service
Ogden, UT 84201-0054
```

Use **USPS Certified Mail with Return Receipt** for proof of timely filing under IRC §7502.

Some recent Rev. Procs have authorized duplicate copies to be filed electronically via fax or a designated portal — **verify the latest Rev. Proc. for accepted submission methods** before mailing. The IRS has been transitioning some 3115 filings to e-fax (e.g., Rev. Proc. 2024-23 or 2025 successor may specify a fax number).

### What goes in the mailing envelope

- Form 3115 (the duplicate copy — clearly marked "DUPLICATE COPY" at the top, per Rev. Proc. instruction)
- Any required attachments: §481(a) adjustment schedule, statement of present method, statement of proposed method, asset-by-asset detail for Schedule E
- Cover letter optional but helpful: identifies taxpayer, year of change, DCN, and confirms the original was attached to the return

### Attaching the original to the return

For e-filed returns:
- Most tax software supports Form 3115 as an attachment. Locate "Forms" or "Statements" → search "3115" → enter line by line.
- Some software does not support Form 3115 — in which case the entire return must be paper-filed (which means the Ogden duplicate is also paper).
- Verify with the software's documentation before assuming e-file support.

For paper-filed returns:
- Form 3115 attaches behind the main form (Form 1040 / 1120 / etc.) in the typical attachment-sequence order.
- Sign Form 3115 (signature required on Page 1).
- The duplicate Ogden copy is also signed.

### Browser flow for e-filing through tax software

1. Sign in / start the return
2. Locate the "Add Form" or "Forms list" feature
3. Search "3115" or navigate to the depreciation / accounting-methods section
4. Fill Form 3115 line by line per the draft
5. Attach the §481(a) schedule as a PDF upload (most software supports this)
6. Verify the form appears in the return's "filed forms" list
7. E-file the return — the original Form 3115 goes with it
8. **Separately**, prepare the duplicate copy and mail/fax to Ogden per current Rev. Proc.

### What the agent should NOT do

- Do not file the duplicate AFTER the return — must be filed by the same due date as the return
- Do not skip the duplicate copy — automatic consent isn't valid without it; the IRS can deny consent retroactively
- Do not file Form 3115 without the corresponding §481(a) schedule
- Do not file before the change is finalized — once filed, the change is committed
- Do not file for a change that's not on the automatic list while claiming it is — the IRS will reject and the change reverts to non-automatic with associated user fee

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| IRS sends Letter 4994 (incomplete 3115) | Missing schedule, signature, or DCN | Respond within deadline; attach missing items |
| IRS rejects DCN claim | DCN doesn't apply to this change per current Rev. Proc. | File non-automatic (advance consent) instead |
| Duplicate not received at Ogden | Mailing issue | Re-mail with certified receipt; document the original mailing date |
| Tax software doesn't support 3115 e-file | Software limitation | Paper-file the entire return |
| Year of change ended without filing | Missed deadline | Generally cannot retroactively file; request late-filing relief under Reg. §301.9100-3 (rare, expensive) |

---

## Section 2 — Non-automatic (advance consent) filing

### When non-automatic applies

- No DCN matches the change in the current Rev. Proc.
- DCN exists but the taxpayer is excluded (under IRS exam, prior change within 5 years, etc., per Section 5 of Rev. Proc. 2015-13)
- Change is to a method that IRS specifically requires advance review for

### Pre-flight

Same as Section 1 plus:

- User fee per current Rev. Proc. 2025-1 (or successor for the year). For tax year 2025, fees ranged $11,500 (most non-automatic) to higher amounts for specific change categories. **Verify 2026 fee schedule** before filing.
- Acknowledgment that processing takes 6-12+ months; the new method cannot be used until the IRS issues a consent letter ruling.

### Filing procedure

1. **File Form 3115** by the **last day of the year of change**:
   - Calendar-year filer changing for 2025: file by December 31, 2025
   - Fiscal-year filer: by the last day of the fiscal year
   - There's a 6-month grace period under Reg. §1.446-1(e)(3)(i) for some changes — verify
2. **Address**: per current Rev. Proc., usually:
   ```
   Internal Revenue Service
   Attn: CC:PA:LPD:DRU
   PO Box 7604
   Ben Franklin Station
   Washington, DC 20044
   ```
   (Verify in the current procedure — some changes go to other addresses.)
3. **Include**:
   - Original Form 3115 (signed)
   - Check or money order for the user fee, made payable to "United States Treasury"
   - Statement of present and proposed methods
   - §481(a) adjustment computation
   - Description of business reasons for the change
4. **Wait for IRS letter ruling** — generally 6-12 months. The taxpayer cannot use the new method until the ruling is received.
5. **After the ruling**, attach a copy of the ruling letter to the year-of-change tax return as evidence of consent.

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Filing returned for missing user fee | Fee not enclosed or wrong amount | Re-submit with correct fee |
| IRS denies the change | Change not in the IRS's interest, conflicts with policy, or facts insufficient | Negotiate with the IRS branch handling the case; appeal limited |
| IRS requests more information | Common; respond within deadline (usually 30 days) | Provide requested data |
| Year of change ends before ruling | Taxpayer cannot use new method yet | File using old method; once ruling received, retroactive application via §481(a) |

---

## Section 3 — Submission state machine

### Automatic consent

1. **Submitted** — Form 3115 attached to return + duplicate to Ogden
2. **Deemed consent** — granted upon timely filing (no separate notification)
3. **Examination risk** — IRS may later challenge the change in audit; deemed consent is rebuttable if facts misstated

### Non-automatic

1. **Submitted** — Form 3115 + user fee mailed to IRS
2. **Acknowledged** — IRS sends a confirmation receipt (sometimes weeks later)
3. **Reviewed** — branch chief assigns; questions or proposed conditions sent
4. **Ruling issued** — consent letter (or denial) issued
5. **Effective** — taxpayer can now use the new method, retroactive to the year of change

---

## Section 4 — Tracking the §481(a) adjustment

The §481(a) adjustment doesn't just go on the year-of-change return — it spreads.

For positive adjustments (4-year spread default):
- Year of change: include 1/4 of adjustment in income
- Year +1, +2, +3: include 1/4 each year

The agent should:
- Note the per-year amount on the deliverable
- Remind the user to track it on each subsequent year's return
- For Schedule C: include the §481(a) portion on Schedule C Line 6 (other income) or Line 27a as "§481(a) adjustment" depending on the change
- For entity returns: similar — usually as "Other income" or a separate line

If the taxpayer disposes of the business during the spread period, **all remaining §481(a) adjustment is recognized in the year of disposition** (acceleration rule).

---

## Section 5 — Common timing pitfalls

1. **Missing the year-end deadline** for non-automatic filings — irreparable; the change can't be made for that year
2. **Filing automatic when non-automatic required** — IRS rejects; user fee may need to be paid retroactively
3. **Forgetting the duplicate to Ogden** — IRS may treat consent as not granted
4. **Filing 3115 with a return that's not yet due** — fine, as long as both copies are filed by the due date
5. **5-year prior-change limitation** — once a method change is made for a particular item, no further automatic-consent change for that item for 5 years (Rev. Proc. 2015-13 Section 5.01)

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file Form 3115 without explicit user consent**. The change is irrevocable for the items covered.
2. **Never store SSN, DOB, EIN, or financial details** in agent logs.
3. **Never submit the duplicate copy without the original** (or vice versa) — both are required.
4. **Always verify the DCN** against the current Rev. Proc. before claiming automatic consent. DCN numbers are renumbered periodically.
5. **Always verify the user fee** in the current Rev. Proc. 2025-1 (or successor) — fees adjust annually.
6. **If the taxpayer is under IRS examination**, surface this immediately. Special rules apply and method changes are often unavailable without IRS area office consent.
7. **Never file for a change spanning <2 years** — that's an error, not a method change. Redirect to amended return.
