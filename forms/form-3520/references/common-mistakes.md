# Top Form 3520 Mistakes

Real mistakes filers make on Form 3520, ranked by how often they trigger
§6677 / §6039F penalties or audit adjustments. Each entry has the
mistake, the consequence, and the fix.

## 1. Filing Form 3520 with Form 1040

**The mistake**: Filer attaches Form 3520 to their Form 1040 and mails
the package to the state service center where the 1040 goes.

**Why it happens**: Most IRS forms are filed with the 1040. Form 3520 is
the exception — it's a separate filing to Ogden.

**Consequence**: The state service center will (eventually) forward the
3520 to Ogden, but the timing slips. If the 1040 was timely filed but
the forwarded 3520 arrives at Ogden after April 15, the 3520 may be
deemed late, triggering §6677 or §6039F penalty. The IRS's position is
that the postmark to Ogden is what counts.

**Fix**: Mail Form 3520 separately to **Internal Revenue Service Center,
P.O. Box 409101, Ogden, UT 84409**. Use USPS Certified Mail with Return
Receipt. The 1040 goes to the filer's normal channel (e-file or state
service center).

---

## 2. Missing the substitute Form 3520-A when the trust didn't file

**The mistake**: User is the US owner of a foreign trust under §679.
They file Form 3520 Part II reporting their ownership. The trust
(foreign trustee) doesn't file Form 3520-A. User assumes the trust's
filing is the trust's problem.

**Consequence**: §6677(b) penalty equal to **5% of the gross value of
the trust's portion attributable to the US owner**, for every year the
3520-A is not filed. On a $1M trust, that's $50,000/year.

**Fix**: When the trust doesn't file 3520-A, the US owner must file a
**substitute 3520-A** as an attachment to their Form 3520. Mark it
"Substitute" and sign as US owner. See [`3520-vs-3520-a.md`](./3520-vs-3520-a.md).

---

## 3. Treating a foreign-individual gift as Part I transfer

**The mistake**: User receives $200,000 from a parent abroad.
Confusingly thinks "this is a transfer to me, so it's Part I."

**Why it happens**: Part I labels transfers TO foreign trusts; Part IV
labels gifts FROM foreign persons. Easy to confuse direction.

**Consequence**: Form is wrong on its face. The IRS may reject it or
ask for a corrected filing.

**Fix**: Part IV is for gifts/bequests RECEIVED by the US person from a
foreign person. Part I is for property the US person SENT to a foreign
trust. Read the trigger boxes at the top of page 1 carefully.

---

## 4. Aggregating gifts wrong for the threshold

**The mistake**: User received $80,000 from grandmother, $60,000 from
grandfather (both foreign individuals). Files only because the
grandmother amount exceeds some assumed threshold, doesn't realize
**aggregate** is $140,000.

Or vice versa: user received $90,000 from grandmother and considers it
under the $100,000 threshold, but also received $20,000 from a foreign
estate (foreign individual donor + foreign estate same threshold), so
aggregate $110,000 triggers Part IV.

**Consequence**: Either over-reporting (no penalty) or under-reporting
(5%/month penalty up to 25%).

**Fix**: Aggregate **across all foreign individuals + foreign estates**
for the $100,000 threshold. Aggregate **across all foreign corporations
+ foreign partnerships** for the inflation-adjusted threshold. The two
categories are independent.

---

## 5. Not knowing about a foreign trust until distribution

**The mistake**: User's parent abroad sets up a foreign trust naming the
user as a beneficiary, never tells the user. Years later, the user
receives a $300,000 distribution and only then learns of the trust.

**Consequence**: User has no Part II / 3520-A history. The IRS may
challenge the reporting position because §679 status (was the user a US
beneficiary all along?) was never established. Distribution defaults to
Part III with the default method, often producing punishing tax.

**Fix**: As soon as the trust is discovered, request the trust's full
history from the trustee or successor trustee. If the user can document
that they had no knowledge of the trust until the distribution date,
**reasonable cause** under §6677(d) may apply for prior-year filing
failures. Consider voluntary disclosure under the Streamlined Filing
Compliance Procedures (SFCP) if there are also unreported foreign income
items.

---

## 6. Treating a "loan" as not reportable

**The mistake**: User receives a "loan" of $150,000 from a foreign
relative or foreign trust. They assume loans aren't gifts and aren't
reportable.

**Consequence**: If the loan terms are not "qualified" (no AFR
interest, no fixed maturity, no documented terms), the IRS may
recharacterize as a gift (Part IV) or a distribution (Part III). Either
way, late-filing penalties apply.

**Fix**: For a **qualified obligation** under Treas. Reg. §1.679-4(d)(1)
(term ≤ 5 years, AFR interest, USD-denominated principal, statute of
limitations extension agreement), the loan avoids gift/distribution
treatment. If any condition fails, treat as gift (from individual) or
distribution (from trust). Work with a practitioner to structure
qualifying obligations BEFORE the loan, not after.

---

## 7. Filing 3520 for a Canadian RRSP

**The mistake**: User has a Canadian RRSP. They read that foreign
retirement accounts are foreign trusts and file Form 3520 + 3520-A every
year.

**Consequence**: Wasted effort. Possibly unnecessary disclosure of
trustee data the user doesn't have access to.

**Fix**: **Rev. Proc. 2014-55** grants automatic exemption for Canadian
RRSPs and RRIFs from Form 3520 / 3520-A reporting. The user files only
Form 8938 for the RRSP and reports income per the US-Canada treaty
election on Form 1040. This is a major simplification specific to
Canada — does NOT apply to UK SIPPs, Australian Super, or other foreign
retirement plans.

---

## 8. Over-aggregating donors on Line 54

**The mistake**: User received gifts from 5 different foreign
individuals, total $120,000. Aggregates them all into one line "Various
foreign donors" without itemizing.

**Consequence**: Form 3520 instructions require itemization of any
donor that contributed more than $5,000 individually when the
$100,000 aggregate threshold is exceeded.

**Fix**: List each donor that gave > $5,000 individually with name,
address, country, relationship, dates, amounts. Donors at or below
$5,000 can be aggregated.

---

## 9. Wrong currency conversion approach

**The mistake**: User translates each gift at a year-end exchange rate,
or uses a single yearly average rate even for one-time transactions
that have a clear date.

**Consequence**: The reported USD figure may be off by 5-15% from what
the IRS expects. For Part IV, this can move the aggregate above or
below the threshold and change whether reporting is required.

**Fix**: For one-time transfers (Part I gift, Part IV gift, Part III
distribution received on a specific date), use the **spot rate on the
date of the transaction**. For ongoing trust accounting (Part II
income/expenses across the year), use the **Treasury yearly average
rate** consistently. Document the source.

The Treasury yearly average rates are at:
https://www.fiscal.treasury.gov/reports-statements/treasury-reporting-rates-exchange/

---

## 10. Filing one Form 3520 for two different foreign trusts

**The mistake**: User has interests in two separate foreign trusts (e.g.,
one inherited from each parent) and tries to fit both onto one Form 3520.

**Consequence**: The IRS's processing system associates one trust per
Form 3520. Combining produces ambiguous records; the IRS may treat one
trust as unreported.

**Fix**: File **one Form 3520 per trust**. If the user has both Part II
(US owner) and Part III (distribution) for the same trust, those go
together on one form. But two trusts require two separate Forms 3520,
each in its own envelope to Ogden.

---

## Less common but worth flagging

### 11. Wet-ink signature missed

Form 3520 is paper-only. Digital signatures are NOT accepted as of 2026.
The IRS requires an actual ink signature on the original. A scanned PDF
with an image of a signature is not enough; the original must be wet-ink
signed by the filer.

### 12. Filing on the IRS Free Fillable Forms platform

FFFF doesn't support Form 3520. Don't try. Some users see that the form
exists in PDF format and assume FFFF would accept it; it won't.

### 13. Trying to e-file via tax software

Mainstream tax software (TurboTax, H&R Block, FreeTaxUSA) does not
e-file Form 3520. Some software lets the user fill the form digitally
and prints a paper version for mailing. The user must mail the printed,
signed form themselves.

### 14. Not filing because there's no tax due

Form 3520 is an **information return** — filing is required regardless
of tax owed. A Part IV gift report has zero income tax effect (gifts are
excluded under IRC §102), but the failure to file penalty is still 5%
per month up to 25% of the gift. Filing is mandatory.

### 15. Spouse files separate 3520 for joint gift

If a foreign relative gives a $150,000 gift jointly to a US married
couple, the gift can be reported on a single joint Form 3520 (filed by
the spouses who jointly file Form 1040). Filing two separate 3520s,
each reporting half, is allowed but more error-prone — easy for one
spouse to miss the threshold determination.

### 16. Missing the year of receipt

If a check from a foreign donor was dated December 2025 but cleared
January 2026, the gift is reported in the year of **constructive
receipt** — usually the year the user could have deposited the check
(typically the year of the check date for personal checks, or the year
of wire/ACH for electronic transfers). Picking the wrong year shifts the
gift to a year that may have a different aggregate.

### 17. Not appointing a US agent and getting punished by §6048(b)(2)

A US grantor of a foreign trust who does NOT appoint a US agent under
§6048(b)(2) faces a presumption: any transfer to the trust may be
treated as a deemed distribution of all trust accumulated income to the
grantor, recharacterizing what would otherwise be a tax-free transfer
into ordinary income.

The fix is to appoint a US agent (often a US trustee, a US attorney, or
a US-based trust company) who agrees to accept service of process and
respond to IRS inquiries about the trust. Documented on Line 7 of Part I.

### 18. Treating a distribution from a US-owned grantor trust as taxable

If the trust is a foreign grantor trust with a US owner (Part II), the
trust's income is already taxed annually to the US owner. A distribution
TO the US owner from such a trust is generally **not separately
taxable** — it's a return of already-taxed corpus.

Schedule A of Part III handles this. The distribution is reported but
no income tax flows. Filers sometimes include the distribution in
income on Schedule 1 of Form 1040 and double-tax themselves. Don't.

### 19. Confusing Form 3520 with Form 709 (Gift Tax)

Form 709 is filed by the **donor** (when the donor is a US person making
gifts above the annual exclusion). Form 3520 Part IV is filed by the
**US recipient** of foreign gifts. If a US donor gives a gift to a US
recipient, only Form 709 (donor) applies — no Form 3520. If a foreign
donor gives a gift to a US recipient, only Form 3520 (recipient)
applies — no Form 709 (the donor isn't a US person and has no Form 709
duty).

### 20. Filing late and not attaching reasonable cause

If the form is filed after the deadline, the IRS will assess penalties.
A reasonable cause statement attached to the late filing can prevent or
abate the penalty — but only if attached. The IRS will not infer
reasonable cause from circumstances; the filer must affirmatively assert
and document it.
