# Common Form 2553 Mistakes

The top patterns that void S-corp elections, trigger a CP264 notice (Form 2553 denied), or cause IRS reclassification post-election. Pre-flight every Form 2553 against this list. (CP262 is a different notice: it confirms a *revocation* of S status.)

---

## 1. Leaving item A blank

**Mistake**: Submitting Form 2553 with item A (EIN) blank.

**Consequence**: The IRS cannot match the election to an entity; expect delay or a CP264 denial.

**Fix**: Apply at https://www.irs.gov/EIN before drafting the form (online, issued once the application is validated), or by fax or mail on Form SS-4. If the EIN has been applied for but not received when the election is due, the instructions allow "Applied For" and the date applied in item A (Instructions for Form 2553, "Item A"). Do not miss the election deadline waiting for the EIN.

---

## 2. Entity name doesn't match IRS records

**Mistake**: Filing Form 2553 with the entity name "Smith Consulting LLC" when the EIN was issued to "Smith Consulting, LLC" (with a comma).

**Consequence**: Processing delay or a CP264 denial; after a denial the IRS asks for a new, complete Form 2553 (https://www.irs.gov/individuals/understanding-your-cp264-notice).

**Fix**: Pull the EIN assignment notice (CP575), or request Letter 147C from the Business & Specialty Tax Line, 800-829-4933. Use the **exact** name in the name field, including punctuation and "Inc."/"LLC"/"Corp." abbreviations.

---

## 3. Missing shareholder consent

**Mistake**: One shareholder forgot to sign column K, or signed but the SSN is missing from column M, or the dates of stock acquisition are missing from column L. For a late election, a former shareholder from the period since item E was left off.

**Consequence**: The election is not valid without every required consent (Form 2553 page 1 note; Reg. §1.1362-6(b)); expect a CP264 denial. A timely election missing a consent can be saved under Reg. §1.1362-6(b)(3)(iii).

**Fix**: Walk through columns J-N for every shareholder before transmission. Use a checklist:
```
For each shareholder (and former shareholder, if filed on or after item E):
□ Column J — Name and address
□ Column K — Handwritten signature and date
□ Column L — Shares/percentage AND date(s) acquired (-0- for former shareholders)
□ Column M — SSN/ITIN/EIN
□ Column N — Tax year end (month and day)
```

---

## 4. Missing community-property spouse signature

**Mistake**: Shareholder lives in a community-property state (AZ, CA, ID, LA, NV, NM, TX, WA, WI) and is married, but only the shareholder signed — the non-owner spouse did not.

**Consequence**: The election is not valid without the spouse's consent. Each person with a community interest in the stock or its income must consent (Reg. §1.1362-6(b)(2)(i)). Fixes after the fact: Reg. §1.1362-6(b)(3)(iii), or Rev. Proc. 2004-35 for a spouse who was a shareholder only because of state community property law.

**Fix**: For every married shareholder in a community-property state, list the spouse on a separate consent row and obtain their signature.

---

## 5. Filing late without the Rev. Proc. 2013-30 package

**Mistake**: Filing Form 2553 after the 2-month-15-day deadline without the "FILED PURSUANT TO REV. PROC. 2013-30" header, without the item I reasonable-cause and diligence explanation, or (for an LLC with no timely Form 8832) without the Part IV representations.

**Consequence**: A late election generally takes effect for the **following** tax year (Instructions for Form 2553, "Relief for Late Elections"); the user loses a year of S-corp treatment. The CP261 FAQ says the same: a different effective date means the form was not timely for the requested date (https://www.irs.gov/individuals/understanding-your-cp261-notice).

**Fix**: Check the deadline against today's date BEFORE drafting. If past the deadline: header; item I explanation (or signed statement); consents from everyone who was a shareholder since item E; Part IV only for an eligible entity relying on the deemed classification election. See [`timing-rules.md`](./timing-rules.md).

---

## 6. Effective date earlier than entity formation

**Mistake**: Item E (election effective date) is 01/01/2026, but the entity was formed 03/15/2026.

**Consequence**: Election is void from formation; the IRS doesn't grant retroactive S-corp status before the entity legally existed.

**Fix**: Item E must be ≥ item B (date incorporated). For a new entity wanting S-corp from day one, item E = the earliest of (shareholders / assets / began doing business).

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

**Mistake**: User files federal Form 2553 successfully, gets CP261, but forgets that NY requires Form CT-6 and AR requires Form AR1103 (within the first 75 days of the tax year), or that NJ needs registration as a corporation filer plus the CP261 copy and Shareholder Jurisdictional Consent.

**Consequence**: Federal S-corp, but state-level C-corp in those states. State corporate tax owed at full rate, defeating much of the SE-tax savings.

**Fix**: At the time of federal filing, identify state requirements (see [`state-conformity.md`](./state-conformity.md)) and queue the state filings. Confirm each with the state revenue department; state rules change (NJ dropped its separate election for periods beginning on or after December 22, 2022).

---

## 11. Filing Schedule C for the period after S-corp effective date

**Mistake**: User elects S-corp for 2026 effective 01/01/2026. In April 2027, user files 1040 with Schedule C reporting the LLC's income.

**Consequence**: Inconsistent reporting. The IRS sees the 2553 (S-corp election effective 01/01/2026) and the Schedule C (single-member LLC sole-prop treatment for 2026). Either the 1120-S wasn't filed (penalty for failure to file) OR the income is double-counted.

**Fix**: Once S-corp is effective, the entity files Form 1120-S annually (March 15 due date). The shareholder receives Schedule K-1, reports income on Form 1040 Schedule E (not Schedule C). Schedule C is for sole props only.

---

## 12. Both faxing and mailing the same election

**Mistake**: User faxes Form 2553 to be safe AND mails a paper copy via Certified Mail.

**Consequence**: The IRS receives two filings for the same election, which can cause duplicate processing or conflicting notices.

**Fix**: Pick **one** channel, document it (save the fax confirmation OR the Certified Mail receipt), and stop. Default to fax for speed and timestamp.

---

## 13. Signing Form 2553 electronically

**Mistake**: The officer or shareholders sign with a typed name, an e-signature service, or a pasted image.

**Consequence**: Form 2553 is not on the IRS list of forms that accept electronic or digital signatures in place of handwritten ones (IRM 10.10.1, Exhibit 10.10.1-2, checked 2026-10-06; the list includes Forms 1128, 3115, and 8832 but not 2553). An election without a valid signature risks a CP264 denial, and an unsigned form "won't be considered timely filed" (Instructions, "Signature").

**Fix**: Use handwritten signatures for the officer and every consenting shareholder. Faxing a hand-signed form is fine; keep the original with the entity's records (Instructions, "Where To File").

---

## 14. Misunderstanding the "tax year" choice in item F

**Mistake**: User checks item F box (2) (fiscal year) without completing Part II, or chooses a fiscal year for tax-deferral reasons.

**Consequence**: An incomplete Part II risks a CP264 denial; a business-purpose request that is not approved (with no Q3/R2 calendar-year fallback checked) can leave the election without an acceptable tax year.

**Fix**: Default to calendar year (item F box (1)) for most small entities. Fiscal year requires documented business purpose, ownership tax year, natural business year (Rev. Proc. 2006-46), or §444 election with required-payment buy-in. Most small entities should not bother.

---

## 15. Not waiting for CP261 before relying on S-corp status

**Mistake**: Filing Form 2553 in February, then in March filing payroll as if S-corp is in effect, taking distributions, etc. — without waiting for the CP261 confirmation.

**Consequence**: If a CP264 (Form 2553 denied) arrives instead of CP261, the user has been operating as an S-corp without a valid election. Payroll filings are wrong, distributions are mischaracterized, etc.

**Fix**: Ask the user how they want to handle the gap; the safest course is to confirm acceptance before relying on S status. A determination generally comes within 60 days. If neither acceptance nor nonacceptance arrives within 2 months (5 months if box Q1 was checked), call 800-829-4933 (Instructions for Form 2553, "Where To File"). Tax professionals with authorization can use the Practitioner Priority Service, 866-860-4259.

---

## Pre-flight checklist (use before every Form 2553 filing)

```
□ EIN obtained, name matches IRS records exactly
□ Entity legally formed and in good standing
□ All shareholders are eligible (no NRA, partnerships, C-corps, multi-LLCs)
□ ≤100 shareholders
□ One class of stock; LLC operating agreement reviewed for waterfalls/preferences
□ Effective date (item E) ≥ formation date (item B)
□ Effective date is consistent with the 2-month-15-day deadline
   OR the Rev. Proc. 2013-30 package is complete (header, item I, consents,
   Part IV if LLC without timely Form 8832)
□ Every shareholder consents (cols J-N) including community-property spouses
   and, if filed on or after item E, former shareholders
□ Officer signature, title, and date below item I (handwritten)
□ "FILED PURSUANT TO REV. PROC. 2013-30" in the top margin of page 1 if late
□ State follow-up queued (NY CT-6 / AR AR1103 / NJ registration + consent)
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
