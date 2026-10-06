# Form 8832 Common Mistakes

The 10 most-repeated mistakes filers make on Form 8832, with citations and fixes. Use this when validating a draft or auditing a prior filing.

---

## Mistake 1 — Filing Form 8832 when only Form 2553 is needed

**Pattern**: SMLLC owner wants S-corp tax treatment. Files Form 8832 (electing C-corp) and then Form 2553 (electing S-corp).

**Why it's wrong**: Treas. Reg. §301.7701-3(c)(1)(v)(C) provides that an eligible entity that timely elects S status on Form 2553 is **deemed** to have elected association classification, and the Form 8832 instructions ("Who Must File") say not to file Form 8832 for an entity electing S status. A separately filed Form 8832 is unnecessary, and if it is accepted while the S election fails, the entity is left a C corporation.

**Fix**: File Form 2553 alone when the corporate classification and the S election start on the same date. For a late election, Rev. Proc. 2013-30 §5.03 covers both elections on Form 2553. File Form 8832 first only if the entity wants a C-corp period before the S election.

**Citation**: Treas. Reg. §301.7701-3(c)(1)(v)(C); Form 8832 instructions, "Who Must File"; Rev. Proc. 2013-30 §§4.01(1), 5.03; IRS Form 2553 Instructions

---

## Mistake 2 — Effective date more than 75 days back without Part II

**Pattern**: Owner wants effective date of January 1 (start of tax year). Files Form 8832 in May (4 months later). Leaves Part II blank.

**Why it's wrong**: The 75-day window in §301.7701-3(c)(1)(iii) is hard-coded. Anything earlier requires Late Election Relief (Part II) under Rev. Proc. 2009-41. Without Part II, the regulation makes the election effective 75 days before the filing date — not January 1, and typically not what the entity wanted.

**Fix**: Either (a) accept an effective date 75 days before the filing date, or (b) re-file with Part II completed under Rev. Proc. 2009-41 with a reasonable-cause statement (and the top-of-form Rev. Proc. 2009-41 box checked).

**Citation**: 26 CFR §301.7701-3(c)(1)(iii); Rev. Proc. 2009-41 § 4.

---

## Mistake 3 — Missing owner consents on the Consent Statement

**Pattern**: Multi-member LLC files Form 8832 with only the manager's signature. Other members do not sign.

**Why it's wrong**: The Consent Statement (unnumbered, below line 10) must be signed by "Each member of the electing entity who is an owner at the time the election is filed" — OR by "Any officer, manager, or member of the electing entity who is authorized (under local law or the organizational documents) to make the election," who represents that authority under penalties of perjury. For a retroactive effective date, former owners from the effective date to the filing date must also sign. Without the required signatures, the IRS may deny the election (CP278) or it may be challenged in audit.

**Fix**: Re-file with all owner signatures. Or have a manager with clear authority under local law or the operating agreement sign for the entity, and keep the operating agreement excerpt or resolution in the file.

**Citation**: 26 CFR §301.7701-3(c)(2); Form 8832 instructions, "Consent statement and signature(s)".

---

## Mistake 4 — Re-electing within 60 months without documenting an exception

**Pattern**: LLC elected C-corp 24 months ago. Owner regrets the election (deemed liquidation tax was painful, business hasn't generated retained earnings to justify the 21% corporate rate). Files new Form 8832 to revert to disregarded entity. Marks Line 2a = Yes, Line 2b = No. Mails it anyway.

**Why it's wrong**: 26 CFR §301.7701-3(c)(1)(iv) blocks re-elections for 60 months. The IRS will issue CP278 rejection. The entity loses the desired effective date and may have to wait until the original effective date + 60 months.

**Fix**:
- **Option 1**: Wait until the 60-month period expires, then file (do not pre-file: line 2a looks back 60 months from the filing date)
- **Option 2**: If persons who held no interest at the prior election now own more than 50%, request a private letter ruling permitting the change (not an attached statement on Form 8832)
- **Option 3**: Live with the C-corp classification and consider an S-corp overlay election (Form 2553) — that election is separate and not blocked by §301.7701-3(c)(1)(iv)

**Citation**: 26 CFR §301.7701-3(c)(1)(iv).

---

## Mistake 5 — Filing for a foreign per-se corporation

**Pattern**: Owner of a UK PLC or German AG files Form 8832 to elect partnership or disregarded status.

**Why it's wrong**: Foreign per-se corporations listed in 26 CFR §301.7701-2(b)(8) are classified as corporations by regulation. They cannot elect down to partnership or disregarded. The IRS will reject (CP278 ineligibility).

**Fix**: Confirm whether the foreign entity is on the per-se list (see [`eligibility.md`](./eligibility.md) for the country-by-country table). If yes, no election is available. If no, verify the entity's default classification under §301.7701-3(b)(2)(i) (limited liability vs. unlimited liability test) before electing.

**Citation**: 26 CFR §301.7701-2(b)(8); §301.7701-3(b)(2).

---

## Mistake 6 — Filing for a state-law corporation

**Pattern**: Owner of an entity formed as "[Name] Inc." or "[Name] Corp." under state law files Form 8832 to elect partnership or disregarded.

**Why it's wrong**: Under §301.7701-2(b)(1), a state-law corporation is a corporation for federal tax purposes — period. Form 8832 cannot elect away from corporate classification for an entity formed as a corporation.

**Fix**: If the owner wants pass-through taxation, the entity must be reorganized into a different state-law form (typically dissolution and re-formation as an LLC, with all the associated state-law and tax consequences). Form 8832 cannot fix this. To get S-corp treatment within the state-law corporate form, file Form 2553 instead.

**Citation**: 26 CFR §301.7701-2(b)(1).

---

## Mistake 7 — Ignoring the §301.7701-3(g) deemed liquidation

**Pattern**: SMLLC with $200K basis and $500K of appreciated assets (real estate, intellectual property, goodwill) elects C-corp. Files Form 8832. Doesn't realize that §301.7701-3(g)(1)(iv) treats the change as a deemed contribution of assets to a newly-formed corporation in exchange for stock — potentially triggering §351 analysis or, if §351 doesn't apply, gain recognition on the appreciation.

**Why it's wrong**: The owner may have unknowingly triggered $300K of recognized gain. Even if §351 does apply (likely, for a SMLLC controlled by a single owner), the corporation takes a carryover basis and the owner takes a substituted basis in the stock — preserving the gain for later recognition. Without planning, the owner may face surprise tax consequences.

**Fix**: Always recommend a CPA review the deemed-transaction consequences **before** mailing Form 8832. Run through:

- §351 control and substantial-investment requirements
- Carryover/substituted basis calculations
- §357(c) liabilities-in-excess-of-basis rule
- §704(c) built-in gain accounting (for partnership-to-corp transitions)
- §1374 built-in gains tax exposure (if the corporation later elects S-corp)

**Citation**: 26 CFR §301.7701-3(g); IRC §§351, 357, 358, 362, 704(c), 1374.

---

## Mistake 8 — Wrong service center

**Pattern**: Filer mails Form 8832 to the closest IRS office, or to a service center based on memory rather than the current "Where to File" table.

**Why it's wrong**: Form 8832 goes to one of two service centers (Kansas City or Ogden; foreign and possession filers use Ogden, UT 84201-0023), and the routing depends on the entity's principal business, office, or agency. Mailing to the wrong center delays processing. Worse, the §7502 timely-mailing rule applies only to an envelope "properly addressed" to the office where the document must be filed (Treas. Reg. §301.7502-1(c)(1)(i)), so a misaddressed form may be treated as filed only when the correct center receives it, which can push the 75-day window or the Rev. Proc. 2009-41 deadline.

**Fix**: Re-verify the service center against the "New Mailing Address" page at the front of the current f8832.pdf and the IRS [Where to file your taxes for Form 8832](https://www.irs.gov/filing/where-to-file-your-taxes-for-form-8832) page before mailing. The table printed in the 2013 instructions (form page 5) is out of date. A foreign country or U.S. possession routes to Ogden, UT 84201-0023.

**Citation**: Form 8832 (Rev. Dec 2013), IRS mailing-address update (PDF page 1); IRS "Where to file your taxes for Form 8832".

---

## Mistake 9 — Boilerplate reasonable cause that the IRS rejects

**Pattern**: Late-filing entity completes Part II with a one-sentence reasonable-cause statement: "We forgot to file the form."

**Why it's wrong**: Rev. Proc. 2009-41 requires reasonable cause, which the IRS interprets as a fact-specific narrative showing the entity took ordinary business care and the failure was outside its control. "We forgot" is not reasonable cause; it's voluntary noncompliance.

**Fix**: Rewrite Part II Line 11 with a specific factual narrative. Patterns that work:

- Reliance on a tax professional who failed to file (with engagement letter as evidence)
- Unawareness of the rule combined with prompt action upon discovery (with specific discovery date and event)
- Death or incapacity of the principal who managed filings (with documentation)
- Change in IRS guidance that triggered the need to elect (with citation to the new guidance)

See [`late-relief.md`](./late-relief.md) for full reasonable-cause language patterns.

**Citation**: Rev. Proc. 2009-41 § 4.01(3).

---

## Mistake 10 — Not addressing state conformity

**Pattern**: Entity files Form 8832 federally, then files state income tax returns based on the federal classification, assuming state law conforms.

**Why it's wrong**: States differ. Some have separate rules or require separate state elections; others follow the federal classification but still impose their own entity-level taxes or fees. California, for example, follows the federal classification by statute (R&TC §23038(b)(2)(B)) but still applies its LLC annual tax and fee to a disregarded LLC. Do not assume the state result.

**Fix**: After filing Form 8832 federally, confirm state conformity with the state department of revenue:

- Does the state automatically conform to the federal entity classification election?
- Is a separate state form / election required?
- Is there a state-level filing deadline tied to the federal election?
- Are there state-specific franchise tax / minimum tax consequences of the federal election?

This is a state-by-state question. The skill does not handle state filings; surface the question to the user and recommend confirmation with the state DOR or state-tax counsel.

**Citation**: State-specific. Example: California R&TC §23038(b)(2)(B) (follows federal classification). Confirm other states with the state revenue department.

---

## Quick audit checklist

Run through this before declaring a Form 8832 draft ready:

- [ ] Entity is eligible (not state-law corp, not foreign per-se, not trust/estate/REIT)
- [ ] EIN is on file (not pending)
- [ ] Box 6 election target is consistent with single/multi-owner status (Line 3)
- [ ] Effective date (Line 8) is within 75 days back / 12 months forward of filing date — OR Part II is completed
- [ ] If Line 2a = Yes, Line 2b is honestly answered (don't inflate prior-election status to evade 60-month rule)
- [ ] All owner signatures collected on the Consent Statement — OR an authorized officer/manager/member signs
- [ ] Service center selected from current "Where to File" table
- [ ] Form 8832 NOT being filed alongside Form 2553 for an LLC seeking S-corp from the same date (use Form 2553 alone; Treas. Reg. §301.7701-3(c)(1)(v)(C))
- [ ] §301.7701-3(g) deemed-transaction consequences reviewed with CPA
- [ ] State conformity question surfaced to user
- [ ] If Part II: reasonable-cause statement is fact-specific (not boilerplate)
- [ ] If Part II: Rev. Proc. 2009-41 box checked at top; Part II declaration signed by the entity and each affected person
