# Common Form 2553 Mistakes

The top patterns that void S-corp elections, trigger CP262 rejections, or cause IRS reclassification post-election. Pre-flight every Form 2553 against this list.

---

## 1. Filing without an EIN

**Mistake**: Submitting Form 2553 before the entity has an EIN, with the EIN line blank or "applied for."

**Consequence**: Automatic CP262 rejection. Form 2553 cannot be filed without an EIN.

**Fix**: Apply at https://www.irs.gov/EIN before drafting the form. Online application issues an EIN immediately for U.S. responsible parties with valid SSN/ITIN. Foreign responsible parties must apply via SS-4 fax (4-6 week wait) — file Form 2553 only after the EIN arrives.

---

## 2. Entity name doesn't match IRS records

**Mistake**: Filing Form 2553 with the entity name "Smith Consulting LLC" when the EIN was issued to "Smith Consulting, LLC" (with a comma).

**Consequence**: CP262 rejection for name mismatch. The election is void, and the user must refile from scratch.

**Fix**: Pull the IRS EIN confirmation letter (Form 147C if the original is lost — request via PPS line 866-860-4259). Use **exact-match** name on Line A, including punctuation, capitalization, and "Inc."/"LLC"/"Corp." abbreviations.

---

## 3. Missing shareholder consent

**Mistake**: One shareholder forgot to sign Column K, or signed but didn't provide SSN in Column N, or didn't list dates of stock acquisition in Column M.

**Consequence**: CP262 rejection. The election requires unanimous shareholder consent — every shareholder, every column.

**Fix**: Walk through Columns J-N for every shareholder before transmission. Use a checklist:
```
For each shareholder:
□ Column J — Name and address
□ Column K — Original signature
□ Column L — Date signed (on or before filing date)
□ Column M — Shares/percentage AND dates acquired
□ Column N — SSN/ITIN/EIN
```

---

## 4. Missing community-property spouse signature

**Mistake**: Shareholder lives in a community-property state (AZ, CA, ID, LA, NV, NM, TX, WA, WI) and is married, but only the shareholder signed — the non-owner spouse did not.

**Consequence**: Election void. Community property = both spouses are deemed shareholders for §1361 purposes; both must consent.

**Fix**: For every shareholder in a community-property state, list the non-owner spouse on a separate consent row and obtain their signature. This is the **#2 cause of voided elections** (after late filing).

---

## 5. Filing late without Part IV

**Mistake**: Filing Form 2553 after the 2-month-15-day deadline but not completing Part IV (late-relief representations) and not writing "FILED PURSUANT TO REV. PROC. 2013-30" across page 1.

**Consequence**: The IRS treats the election as effective for the **following** tax year — the user loses a year of S-corp treatment. If the user's first 1120-S is already filed for the intended year, the IRS sends back a CP262 or processes the 1120-S as a C-corp 1120 with substantial reclassification.

**Fix**: Check the deadline against today's date BEFORE drafting. If past the deadline, complete Part IV (boxes 1, 2, 3), write "FILED PURSUANT TO REV. PROC. 2013-30" across the top, and attach a reasonable-cause statement.

---

## 6. Effective date earlier than entity formation

**Mistake**: Line F (election effective date) is 01/01/2026, but the entity was formed 03/15/2026.

**Consequence**: Election is void from formation; the IRS doesn't grant retroactive S-corp status before the entity legally existed.

**Fix**: Line F must be ≥ Line D (date incorporated). For a new entity wanting S-corp from day one, Line F = the earliest of (shareholders / acquired assets / began doing business).

---

## 7. One-class-of-stock violation in LLC operating agreement

**Mistake**: LLC operating agreement contains "preferred return" or "waterfall distribution" clauses that give one class of members priority over another. The LLC files Form 2553 anyway.

**Consequence**: Election is void from day one because the entity violates IRC §1361(b)(1)(D). The IRS may not catch it immediately, but on audit the S-corp treatment is unwound retroactively, with massive tax and penalty consequences.

**Fix**: BEFORE filing Form 2553, review the operating agreement for:
- Waterfall distributions (sequential priority)
- Preferred returns (e.g., "8% to Class A before any distribution to Class B")
- Catch-up provisions
- Targeted capital accounts
- Any clause granting any member a priority over any other member's economic rights

If found, amend the operating agreement to provide pro-rata economic rights, with the amendment effective on or before the election effective date. Then file Form 2553.

---

## 8. Ineligible shareholder — non-resident alien, partnership, or multi-member LLC

**Mistake**: One shareholder is a non-resident alien, a C-corp, a partnership, or a multi-member LLC. The user files Form 2553 anyway.

**Consequence**: Election is void. Reverting to default tax treatment retroactively triggers significant tax adjustments.

**Fix**: Before drafting, check every shareholder's status against the eligibility checklist in [`eligibility.md`](./eligibility.md). If any shareholder is ineligible:
- Buy them out (transfer their interest to an eligible shareholder)
- Restructure (multi-member LLC parent → make it single-member)
- Or skip the S-corp election

Common trap: a U.S. resident with valid ITIN is eligible, but a non-resident alien with ITIN is not. The distinction is **U.S. tax residency**, not the document type. Substantial-presence test or green-card test.

---

## 9. Underpaid reasonable salary (post-election compliance)

**Mistake**: After CP261 acceptance, the shareholder takes $0 or token salary and 100% distributions, to dodge FICA.

**Consequence**: IRS reclassification on audit. Distributions reclassified as wages, FICA owed retroactively, plus penalties (failure-to-deposit, failure-to-file 941s) plus interest.

**Fix**: Run a Watson-factors analysis (see [`reasonable-salary.md`](./reasonable-salary.md)). Document the salary determination in writing before paying it. Use BLS OES data, adjust for hours and experience, defend the number with a memo. Don't take $0 salary on a working shareholder.

---

## 10. Forgetting state-level S-corp election

**Mistake**: User files federal Form 2553 successfully, gets CP261, but forgets that NY requires CT-6, NJ requires CBT-2553, AR requires AR1103, or LA requires R-6980.

**Consequence**: Federal S-corp, but state-level C-corp. State franchise / corporate tax owed at full rate, defeating much of the SE-tax savings.

**Fix**: At the time of federal filing, identify state requirements (see [`state-conformity.md`](./state-conformity.md)) and queue the state filings. NJ's 1-month deadline is the tightest — easy to miss.

---

## 11. Filing Schedule C for the period after S-corp effective date

**Mistake**: User elects S-corp for 2026 effective 01/01/2026. In April 2027, user files 1040 with Schedule C reporting the LLC's income.

**Consequence**: Inconsistent reporting. The IRS sees the 2553 (S-corp election effective 01/01/2026) and the Schedule C (single-member LLC sole-prop treatment for 2026). Either the 1120-S wasn't filed (penalty for failure to file) OR the income is double-counted.

**Fix**: Once S-corp is effective, the entity files Form 1120-S annually (March 15 due date). The shareholder receives Schedule K-1, reports income on Form 1040 Schedule E (not Schedule C). Schedule C is for sole props only.

---

## 12. Both faxing and mailing the same election

**Mistake**: User faxes Form 2553 to be safe AND mails a paper copy via Certified Mail.

**Consequence**: The IRS receives two filings for the same election. Often results in CP262 citing duplicate filing, or two CP261 letters (which confuses banks and state agencies later).

**Fix**: Pick **one** channel, document it (save the fax confirmation OR the Certified Mail receipt), and stop. Default to fax for speed and timestamp.

---

## 13. Filing Form 2553 with an electronic signature that doesn't qualify

**Mistake**: Shareholders sign with a typed name, an autofill signature, or a simple image-paste, without satisfying Reg. §1.1362-6(b)(3) qualifying-electronic-signature rules.

**Consequence**: CP262 rejection citing invalid signatures.

**Fix**: Use original wet-ink signatures whenever possible. If using e-signatures, use a service like DocuSign, Adobe Sign, or PandaDoc that captures audit trail metadata (IP, timestamp, identity verification). The IRS has been more accepting of e-signatures since 2020 but still rejects bare typed names.

---

## 14. Misunderstanding the "tax year" choice on Line I

**Mistake**: User checks Line I Box 2 (fiscal year) without completing Part II, or chooses fiscal year for tax-deferral reasons.

**Consequence**: CP262 rejection if Part II is incomplete, OR if Part II is complete, the IRS often denies fiscal year for small entities and forces calendar year — which means the election may take effect a year later than intended, or be deemed for calendar year by default.

**Fix**: Default to calendar year (Line I Box 1) for ~99% of small entities. Fiscal year requires documented business purpose, ownership tax year, natural business year (Rev. Proc. 2006-46), or §444 election with required-payment buy-in. Most small entities should not bother.

---

## 15. Not waiting for CP261 before relying on S-corp status

**Mistake**: Filing Form 2553 in February, then in March filing payroll as if S-corp is in effect, taking distributions, etc. — without waiting for the CP261 confirmation.

**Consequence**: If CP262 (rejection) arrives instead of CP261, the user has been operating as S-corp without authorization. Payroll filings are wrong, distributions are mischaracterized, etc.

**Fix**: Wait for CP261 before changing payroll, distribution, or accounting practices. CP261 typically arrives within 60 days of filing. In the interim, continue prior-year practices. If CP261 is delayed past 60 days, call PPS line 866-860-4259.

---

## Pre-flight checklist (use before every Form 2553 filing)

```
□ EIN obtained, name matches IRS records exactly
□ Entity legally formed and in good standing
□ All shareholders are eligible (no NRA, partnerships, C-corps, multi-LLCs)
□ ≤100 shareholders
□ One class of stock; LLC operating agreement reviewed for waterfalls/preferences
□ Effective date (Line F) ≥ formation date (Line D)
□ Effective date is consistent with the 2-month-15-day deadline
   OR Part IV is completed for late relief
□ Every shareholder consents (Cols J-N) including community-property spouses
□ Officer signature on Line J
□ "FILED PURSUANT TO REV. PROC. 2013-30" written across page 1 if late
□ Reasonable-cause statement attached if late
□ State-level S-corp election queued (NY CT-6 / NJ CBT-2553 / AR AR1103 / LA R-6980)
□ Reasonable salary plan documented before payroll begins
□ Single transmission channel chosen (fax OR mail, not both)
□ Confirmation page captured and saved
```

---

## Cross-references

- Form mechanics: [`line-by-line.md`](./line-by-line.md)
- Eligibility: [`eligibility.md`](./eligibility.md)
- Timing: [`timing-rules.md`](./timing-rules.md)
- Reasonable salary: [`reasonable-salary.md`](./reasonable-salary.md)
- State conformity: [`state-conformity.md`](./state-conformity.md)
- Filing channel: [`../filing.md`](../filing.md)
