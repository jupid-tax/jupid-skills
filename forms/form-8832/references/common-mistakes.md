# Form 8832 Common Mistakes

The 10 most-repeated mistakes filers make on Form 8832, with citations and fixes. Use this when validating a draft or auditing a prior filing.

---

## Mistake 1 — Filing Form 8832 when only Form 2553 is needed

**Pattern**: SMLLC owner wants S-corp tax treatment. Files Form 8832 (electing C-corp) and then Form 2553 (electing S-corp).

**Why it's wrong**: Rev. Proc. 2013-30 § 4 explicitly provides that an eligible entity electing S-corp via Form 2553 is **deemed** to have made the corresponding entity classification election. Form 8832 is unnecessary and adds a paper trail with no benefit.

**Fix**: File Form 2553 alone, citing Rev. Proc. 2013-30. The IRS treats this as both an entity classification change AND an S-corp election in one filing.

**Citation**: Rev. Proc. 2013-30 § 4; IRS Form 2553 Instructions ("LLC")

---

## Mistake 2 — Effective date more than 75 days back without Part II

**Pattern**: Owner wants effective date of January 1 (start of tax year). Files Form 8832 in May (4 months later). Leaves Part II blank.

**Why it's wrong**: The 75-day window in §301.7701-3(c)(1)(iii) is hard-coded. Anything earlier requires Late Election Relief (Part II) under Rev. Proc. 2009-41. Without Part II, the IRS will accept the filing but use the postmark date as the effective date — typically not what the entity wanted.

**Fix**: Either (a) accept the postmark date as the effective date, or (b) re-file with Part II completed under Rev. Proc. 2009-41 with a reasonable-cause statement.

**Citation**: 26 CFR §301.7701-3(c)(1)(iii); Rev. Proc. 2009-41 § 4.

---

## Mistake 3 — Missing owner consents on Line 11

**Pattern**: Multi-member LLC files Form 8832 with only the manager's signature. Other members do not sign.

**Why it's wrong**: Form 8832 Line 11 requires "Each member, manager, and owner who has an ownership interest in the entity at the time of the election" to sign — OR an officer/manager authorized under state law to sign on behalf of all owners with documented authority. Without all signatures or documented authority, the IRS may reject (CP278 missing-consent) or the election may be challenged in audit.

**Fix**: Re-file with all owner signatures. Or, if the manager has clear state-law authority, attach the operating agreement excerpt or a board resolution authorizing the manager to make federal tax elections on behalf of all members.

**Citation**: 26 CFR §301.7701-3(c)(2); Form 8832 Line 11 instructions.

---

## Mistake 4 — Re-electing within 60 months without documenting an exception

**Pattern**: LLC elected C-corp 24 months ago. Owner regrets the election (deemed liquidation tax was painful, business hasn't generated retained earnings to justify the 21% corporate rate). Files new Form 8832 to revert to disregarded entity. Marks Line 2a = Yes, Line 2b = No. Mails it anyway.

**Why it's wrong**: 26 CFR §301.7701-3(c)(1)(iv) blocks re-elections for 60 months. The IRS will issue CP278 rejection. The entity loses the desired effective date and may have to wait until the original effective date + 60 months.

**Fix**:
- **Option 1**: Wait until the 60-month period expires (entity may pre-file up to 12 months in advance once eligible)
- **Option 2**: Document a >50% ownership change since the prior effective date and file with an attached statement claiming the exception
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

**Why it's wrong**: Form 8832 has only two service centers (Kansas City and Ogden), and the routing depends on the entity's principal place of business. Mailing to the wrong center delays processing — IRS will eventually forward, but it adds weeks. The "filing date" remains the postmark, so the timing rules are still satisfied, but the entity may not receive CP277/CP278 within the typical 60-day window.

**Fix**: Re-verify the service center against the "Where to File" table on Form 8832 page 6 before mailing. If foreign principal place of business, Kansas City is the routing.

**Citation**: Form 8832 (Rev. Dec 2013), "Where to File" table on page 6.

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

**Why it's wrong**: Some states (notably California, New York, New Jersey, Pennsylvania) have separate rules or require separate elections. A federal-only Form 8832 may not change state classification — the entity could be a C-corp federally and a partnership for state purposes, or vice versa.

**Fix**: After filing Form 8832 federally, confirm state conformity with the state department of revenue:

- Does the state automatically conform to the federal entity classification election?
- Is a separate state form / election required?
- Is there a state-level filing deadline tied to the federal election?
- Are there state-specific franchise tax / minimum tax consequences of the federal election?

This is a state-by-state question. The skill does not handle state filings; surface the question to the user and recommend confirmation with the state DOR or state-tax counsel.

**Citation**: State-specific. Common references: California R&TC §23038, NY Tax Law §658, NJ N.J.S.A. §54:10A-15.

---

## Quick audit checklist

Run through this before declaring a Form 8832 draft ready:

- [ ] Entity is eligible (not state-law corp, not foreign per-se, not trust/estate/REIT)
- [ ] EIN is on file (not pending)
- [ ] Box 6 election target is consistent with single/multi-owner status (Line 3)
- [ ] Effective date (Line 8) is within 75 days back / 12 months forward of filing date — OR Part II is completed
- [ ] If Line 2a = Yes, Line 2b is honestly answered (don't inflate prior-election status to evade 60-month rule)
- [ ] All owner signatures collected (Line 11) — OR documented officer/manager authority
- [ ] Service center selected from current "Where to File" table
- [ ] Form 2553 NOT being filed simultaneously for an LLC seeking S-corp (use Form 2553 alone per Rev. Proc. 2013-30)
- [ ] §301.7701-3(g) deemed-transaction consequences reviewed with CPA
- [ ] State conformity question surfaced to user
- [ ] If Part II: reasonable-cause statement is fact-specific (not boilerplate)
- [ ] If Part II: consistent-returns declaration signed under penalties of perjury
