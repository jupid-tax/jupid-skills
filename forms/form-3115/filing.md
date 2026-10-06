# Filing Form 3115

How an agent files Form 3115 to request consent for an accounting method change. Form 3115 has unusual logistics: most filings are **automatic consent** with a duplicate-copy requirement, and a smaller subset are **non-automatic** with a user fee and IRS review.

The agent must produce a complete `SKILL.md`-format draft *first*, then determine the filing path, then execute.

---

## Channel decision tree

```
Change is on the automatic-consent list (DCN matches in Rev. Proc. 2025-23, as modified by Rev. Proc. 2025-28, or a later list)?
  → Automatic consent path. Section 1.

Change is NOT on the automatic-consent list?
  → Non-automatic (advance consent) path. Section 2.

An eligibility rule in Rev. Proc. 2015-13 §5.01(1) applies (change for the
same item or overall method change within the 5 tax years ending with the
year of change, final year of the trade or business, §381 transaction) and
the DCN section does not waive it?
  → Non-automatic, even if DCN exists. Section 2.

Taxpayer is currently under IRS examination, before Appeals, or in court?
  → Automatic changes are generally still available, with limits: copies to
    the examining agent/Appeals, audit protection only in the line 7b
    categories, 2-year period for a positive §481(a) adjustment
    (Rev. Proc. 2015-13 §§6.03(3), 8.02; i3115 line 25). Refer close cases
    to a CPA.
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

Automatic consent under Rev. Proc. 2015-13 §6.03(1) requires:

1. **Original Form 3115** attached to the **timely filed (including extensions) federal tax return** for the year of change. The original does not need to be signed (i3115, "When and Where To File")
2. **Signed copy of Form 3115** (a photocopy is fine) filed **separately** with the IRS in Ogden, **no earlier than the first day of the year of change and no later than the date the original is filed with the return**

### Sending the signed (Ogden) copy

Addresses (Rev. Proc. 2026-1 §9.06; Instructions for Form 3115, Address Chart):

```
Mail:                      Internal Revenue Service
                           Ogden, UT 84201
                           M/S 6111
Private delivery service:  Internal Revenue Service
                           1973 N. Rulon White Blvd.
                           Ogden, UT 84201
                           Attn: M/S 6111
Fax:                       844-249-8134 (include a cover sheet)
```

By mail, use **USPS Certified Mail with Return Receipt** for proof of timely filing under IRC §7502. By fax, keep the transmission confirmation. The IRS does not send acknowledgements of receipt for automatic change requests (i3115).

### What goes in the mailing envelope

- Form 3115 (the signed copy)
- Any required attachments: §481(a) adjustment schedule, statement of present method, statement of proposed method, asset-by-asset detail for Schedule E
- Cover letter optional but helpful: identifies taxpayer, year of change, DCN, and confirms the original was attached to the return

### Attaching the original to the return

For e-filed returns:
- Most tax software supports Form 3115 as an attachment. Locate "Forms" or "Statements" → search "3115" → enter line by line.
- Some software does not support Form 3115 — in which case the entire return must be paper-filed (which means the Ogden duplicate is also paper).
- Verify with the software's documentation before assuming e-file support.

For paper-filed returns:
- Form 3115 attaches behind the main form (Form 1040 / 1120 / etc.) in the typical attachment-sequence order.
- The original attached to the return does not need to be signed (i3115); signing it does no harm.
- The Ogden copy must be signed (filer, and spouse if joint return; for an entity, an officer with authority).

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

- Do not file the Ogden copy AFTER the return — it must be filed no later than the date the original is filed with the return
- Do not skip the Ogden copy — it is a filing requirement of the automatic procedures
- Do not file Form 3115 without the corresponding §481(a) schedule
- Do not file before the change is finalized — once filed, the change is committed
- Do not file for a change that's not on the automatic list while claiming it is — the IRS will reject and the change reverts to non-automatic with associated user fee

### Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| IRS correspondence asking for missing information | Missing schedule, signature, or DCN statement | Respond by the date in the letter; attach missing items |
| IRS rejects DCN claim | DCN doesn't apply to this change per current Rev. Proc. | File non-automatic (advance consent) instead |
| Duplicate not received at Ogden | Mailing issue | Re-mail with certified receipt; document the original mailing date |
| Tax software doesn't support 3115 e-file | Software limitation | Paper-file the entire return |
| Return filed without Form 3115 | Missed deadline | An automatic 6-month extension from the unextended due date may be available (Rev. Proc. 2015-13 §6.03(4)(a); Reg. §301.9100-2); otherwise §301.9100-3 relief (unusual and compelling circumstances; user fee) |

---

## Section 2 — Non-automatic (advance consent) filing

### When non-automatic applies

- No DCN matches the change in the current Rev. Proc.
- DCN exists but an eligibility rule in Rev. Proc. 2015-13 §5.01(1) applies and is not waived
- Change is to a method that IRS specifically requires advance review for

### Pre-flight

Same as Section 1 plus:

- User fee per Rev. Proc. 2026-1, Appendix A: $13,225 for a non-automatic Form 3115; $9,775 if gross income is $400,000 or more but under $10 million; $3,450 if under $400,000 (certification required). A successor revenue procedure is published each January; check it for 2027 requests.
- Acknowledgment that processing can take many months; the new method cannot be used until the IRS issues its consent.

### Filing procedure

1. **File Form 3115** **during the year of change** (Rev. Proc. 2015-13 §6.03(2)):
   - Calendar-year filer changing for 2026: file by December 31, 2026
   - Fiscal-year filer: by the last day of the fiscal year
   - No general grace period; late filing needs §301.9100-3 relief (i3115, "Late Application")
2. **Address** (Rev. Proc. 2026-1 §9.05):
   ```
   Internal Revenue Service
   Attn: CC:PA:LPD:TSS
   P.O. Box 7604
   Benjamin Franklin Station
   Washington, DC 20044
   ```
   Private delivery service: Internal Revenue Service, Attn: CC:PA:LPD:TSS, Room 5336, 1111 Constitution Ave., NW, Washington, DC 20224. Alternatives: secure fax 877-773-4950, or encrypted email to Userfee@irscounsel.treas.gov with the MOUs in Rev. Proc. 2026-1 Appendices G and H.
3. **Include**:
   - Original Form 3115 (signed)
   - Copy of the pay.gov receipt for the user fee (pay the full fee through www.pay.gov first)
   - Statement of present and proposed methods
   - §481(a) adjustment computation
   - Description of business reasons for the change (Part III line 22)
4. **Wait for the IRS letter ruling / consent agreement**. The taxpayer cannot use the new method until consent is received.
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
- For Schedule C: positive portion on line 6 (other income); negative in Part V, flowing to line 27b (2025 Instructions for Schedule C, Line 6)
- For entity returns: Form 1120-S line 5 (positive) or line 20 (negative); Form 1120 line 10 (positive), each with a statement

Under examination, a positive adjustment is spread over 2 years instead of 4 unless a line 7b window applies. If the taxpayer ceases the trade or business during the adjustment period (including incorporating it or transferring substantially all its assets), **the remaining §481(a) balance is taken into account in the year of cessation** (Rev. Proc. 2015-13 §§3.04, 7.03(4)).

---

## Section 5 — Common timing pitfalls

1. **Missing the year-end deadline** for non-automatic filings — the change can't be made for that year without §301.9100-3 relief
2. **Filing automatic when non-automatic required** — the filing does not obtain automatic consent; a non-automatic request with user fee is needed
3. **Forgetting the signed copy to Ogden** — the automatic change is not properly filed
4. **Filing 3115 with a return that's not yet due** — fine, as long as the Ogden copy is filed no later than the return and no earlier than the first day of the year of change
5. **5-year prior-change limitation** — a change for the same item (or an overall method change) within the 5 tax years ending with the year of change generally bars automatic consent (Rev. Proc. 2015-13 §5.01(1)(e)–(f)) unless the DCN section waives it

---

## Security and consent rules for the agent

These are non-negotiable:

1. **Never file Form 3115 without explicit user consent**. The change is irrevocable for the items covered.
2. **Never store SSN, DOB, EIN, or financial details** in agent logs.
3. **Never submit the duplicate copy without the original** (or vice versa) — both are required.
4. **Always verify the DCN** against the current list (Rev. Proc. 2025-23 or later) before claiming automatic consent. DCN numbers are reassigned between lists.
5. **Always verify the user fee** in the current annual revenue procedure (Rev. Proc. 2026-1 for 2026) — fees can change each January.
6. **If the taxpayer is under IRS examination**, surface this immediately. Special rules apply (copies to the agent, audit-protection limits, 2-year period for positive adjustments).
7. **Never file for a treatment used on fewer than 2 consecutive filed returns** without checking whether it is an established method — otherwise redirect to an amended return (DCN 7 1-year property exception).
