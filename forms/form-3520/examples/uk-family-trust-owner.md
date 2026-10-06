# Example — US Owner of a UK Family Trust (Part II + Substitute 3520-A)

End-to-end Form 3520 for a US person treated as US owner of a UK family
trust under IRC §679, where the foreign trustee did not file Form
3520-A. Part II + substitute 3520-A.

## Filer profile

- **Name**: David Hughes (US citizen, dual UK-US)
- **SSN**: 234-56-7890 (illustrative)
- **Address**: 218 Beacon Hill Road, Berkeley, CA 94708
- **Filing status**: Married Filing Jointly (with spouse Lisa Hughes)
- **Tax year**: 2026 (calendar year)

## Background

David emigrated from the UK to the US in 2019 and became a US citizen in
2024. In 2021, while a US tax resident (green card holder), David
transferred £350,000 of his UK assets to a UK family trust he established
under English law. The trust:

- Is governed by English law (Crockett, Hughes & Partners LLP, London)
- Has two UK solicitors as trustees
- Names David's UK-resident niece (Sophie) and David himself as
  beneficiaries; David's US-citizen wife Lisa is also a contingent
  beneficiary
- Holds UK investment portfolio (£420,000 GBP at year-end 2026) plus a
  Manchester rental property (£280,000 GBP value, held in trust since
  2021)

## §679 status

Under IRC §679, a US person who transferred property to a foreign trust
that has at least one US beneficiary (or could have one) is treated as
the **US owner** of the trust to the extent of the property transferred,
regardless of trustee discretion or distribution history.

David transferred £350,000 to a foreign trust in 2021, while a US tax
resident. The trust has US beneficiaries (David, Lisa). Therefore David
is the **US owner** of the portion attributable to his transfer. He
files Form 3520 Part II annually.

David's first Form 3520 was filed for tax year 2021 and every year since.
This example covers the 2026 filing.

## What's also true

- David also files Form 8938 annually (foreign financial assets above
  threshold); his interest in the trust, reported on Form 3520, is an
  excepted asset there (item C on Form 3520; Form 8938 Part IV line 15)
- David also files FBAR (FinCEN 114) for the trust's UK bank account
  (as owner of a grantor trust he is treated as having a financial
  interest; confirm against the FinCEN 114 instructions)
- David did NOT receive any distribution from the trust in 2026; if he
  had, Part III would also apply on the same Form 3520

## The 3520-A problem

Crockett, Hughes & Partners LLP (UK trustees) refuse to file Form 3520-A
or to sign a U.S. agent agreement. Their position: they have no US tax
filing obligation. David has tried since 2021 to convince them; they
remain firm. So the trust has no U.S. agent (Form 3520 line 3 "No"), and
the IRS may redetermine the amounts David must take into account (IRC
§6048(b)(2)).

David must attach a **substitute Form 3520-A** to his Form 3520, signed
by him as US owner with his name and TIN on the "Title" line. Without it,
the §6677(b) penalty would be the greater of $10,000 or 5% of $886,327 =
$44,316.

## Trust data for tax year 2026

David obtained the trust's UK accounting (prepared by the trustees for
UK tax purposes) and converted income, expenses, and distributions to USD
at the **IRS yearly average rate for 2026** (illustrative: $1.2540/GBP;
check https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates
once 2026 is published) and balance-sheet values at year-end spot rates
(illustrative: $1.2410/GBP at 12/31/2025, $1.2540/GBP at 12/31/2026).
Math: /tmp/jupid-skills-work/calc/g4-3520-uk.py.

### Trust beginning-of-year FMV (2026-01-01)

- UK investment portfolio: £405,000 → $502,605
- Manchester rental property: £278,000 → $344,998
- UK bank account: £8,400 → $10,424
- **Total**: $858,027

### Trust income (2026)

- Investment dividends and interest: £14,200 → $17,807
- Rental income (Manchester property): £18,600 → $23,324
- Realized capital gains: £6,400 → $8,026
- **Total income**: $49,157

### Trust expenses (2026)

- UK trustee fees: £4,800 → $6,019
- UK property maintenance: £3,200 → $4,013
- UK accountant: £1,200 → $1,505
- **Total expenses**: $11,537

### Distributions (2026)

- To David (US owner): $0
- To Lisa (US contingent beneficiary): $0
- To Sophie (UK niece beneficiary): £8,000 → $10,032
- **Total distributions**: $10,032

### Trust end-of-year FMV (2026-12-31)

- UK investment portfolio: £420,000 → $526,680
- Manchester rental property: £280,000 → $351,120
- UK bank account: £6,800 → $8,527
- **Total**: $886,327

## David's portion

The full trust corpus is attributable to David's 2021 transfer of
£350,000, which has since appreciated. David is the US owner of 100% of
the trust under §679 (no other contributions from non-grantors).

His Foreign Grantor Trust Owner Statement (pages 3–4 of the substitute
3520-A) shows 100% ownership, $886,327 year-end gross value attributable
to him, and the trust's income and expense items. As owner he reports
each item on his own return by character: dividends and interest on
Form 1040 / Schedule B, rent and rental expenses on Schedule E, capital
gains on Form 8949 / Schedule D. Trustee and accountant fees are not
rental expenses; ASK the CPA how they are treated (for individuals,
miscellaneous itemized deductions are limited by §67(g)).

## Part III consideration

David received no distribution. Sophie's $10,032 distribution is to a
non-US beneficiary; it doesn't trigger Part III for David (Part III
covers distributions to US persons).

If Lisa had received a distribution, she would file her own Part III on
this same joint Form 3520 (one Form 3520 per joint 1040 is allowed).

## Filled draft

```markdown
# Form 3520 (Rev. December 2023) — DRAFT for tax year 2026

## Page 1
A. Initial / Final / Amended: none (6th annual filing for this trust)
B. Filer type: Individual
C. Counted on Form 8938 Part IV line 15: Yes
Trigger box checked: Part II (U.S. owner of a foreign trust)
1a. Name: David Hughes and Lisa Hughes   1b. TIN: 234-56-7890
1c, 1e–1h. Address: 218 Beacon Hill Road, Berkeley, CA 94708, United States
1d. Spouse's TIN: 234-56-7891
1i. Joint Form 3520: [x] (joint income tax return; David is the owner and a
    beneficiary, Lisa a contingent beneficiary of the same trust)
1j. 2-month extension: [ ]   1k. Income tax return extension: [ ]
2a. Foreign trust: Hughes Family Trust   2b. EIN: 99-XXXXXXX (obtained 2021 via SS-4)
2c, 2e–2h. Trust address: c/o Crockett, Hughes & Partners LLP, London, United Kingdom
2d. Date created: 06/15/2021
3. U.S. agent: No (trustees declined)
4a–4f. (blank)

## Part II — U.S. owner of a foreign trust
20. | (a) David Hughes | (b) 218 Beacon Hill Road, Berkeley, CA 94708 | (c) United States | (d) 234-56-7890 | (e) 679 |
21a. Country code where created: UK   21b. Country code of governing law: UK
21c. Date created: 06/15/2021
22. Trust filed Form 3520-A for 2026: No → substitute Form 3520-A attached
23. Gross value of portion owned at end of 2026: $886,327

## Substitute Form 3520-A (attached; summary of amounts)
- Balance sheet: beginning of year $858,027; end of year $886,327
- Income (2026): dividends and interest $17,807; rent $23,324; capital gains $8,026; total $49,157
- Expenses (2026): trustee fees $6,019; property maintenance $4,013; accountant $1,505; total $11,537
- Distributions (2026): $10,032 to Sophie (non-U.S. beneficiary); $0 to David and Lisa
- Owner Statement (pages 3–4) for David; Beneficiary Statement (page 5) not needed (no U.S. beneficiary received a distribution)
- "Substitute Form 3520-A" box checked; signed by David with his name and TIN on the "Title" line

## Currency translation
Source: IRS yearly average rate for 2026 (income, expenses, distributions); year-end spot rates (balance sheet)
Rates: $1.2540/GBP average; $1.2410/GBP at 12/31/2025; $1.2540/GBP at 12/31/2026 (illustrative)

## Required attachments
- [x] Substitute Form 3520-A (including the Owner Statement, pages 3–4)
- [x] Copy of the Owner Statement furnished to David by the Form 3520 due date
- [x] Record of annual requests to the trustees and their refusals (kept with
      the file; reluctance of a foreign fiduciary is not reasonable cause, so
      the substitute itself is what avoids the §6677(b) penalty)

## Mailing address
Internal Revenue Service Center
P.O. Box 409101
Ogden, UT 84409

## Validation summary
- Math (python): income $49,157 = $17,807 + $23,324 + $8,026 ✓
- Math: expenses $11,537 = $6,019 + $4,013 + $1,505 ✓
- Math: line 23 $886,327 = $526,680 + $351,120 + $8,527 ✓; beginning
  balance $858,027 = $502,605 + $344,998 + $10,424 ✓
- Sanity: one Form 3520 for this one trust; joint filing conditions met
- Sanity: substitute 3520-A signed by David, not the UK trustees
- Next steps:
  1. David and Lisa both sign Form 3520 page 6
  2. David signs the substitute 3520-A as US owner
  3. Mail the package (Form 3520 + substitute 3520-A) to Ogden by April 15,
     2027 (or October 15, 2027 if Form 4868 is filed and line 1k checked)
  4. On Form 1040, report the trust's income items by character
     (Schedule B, Schedule E, Form 8949 / Schedule D) and claim a foreign
     tax credit on Form 1116 for UK tax paid on the same income, if any
  5. Continue annual FBAR for the trust's UK bank account
  6. Continue annual Form 8938 (trust interest excepted via Form 3520)

## Sources cited in this draft
- IRS Form 3520 (Rev. December 2023) and Instructions (Rev. December 2025)
- IRS Form 3520-A (Rev. December 2023) and Instructions (Rev. December 2025)
- IRC §679, §6048, §6677(b)
- Treas. Reg. §§1.679-1 through 1.679-7
- Notice 97-34
- IRS yearly average currency exchange rates
```

## Why this case is hard

- Trustee refuses to file 3520-A → substitute required every year
- Trust holds non-financial property (rental real estate) in addition to
  financial assets → the substitute 3520-A balance sheet and line 23 must
  include it at FMV (liabilities disregarded for line 23)
- Multiple compliance regimes apply simultaneously: 3520, 3520-A
  (substitute), 8938, FBAR, Form 1040 with foreign tax credit
- David keeps documentation of his requests to the trustees; the
  instructions say a reluctant foreign fiduciary is not reasonable cause,
  so the timely substitute is what protects him

## What would change this case

- **If David transferred property to the trust in 2026**: also file
  Part I for the new transfer, in addition to Part II
- **If David received a distribution in 2026**: also file Part III. For
  an amount from the portion he owns, complete only lines 24 and 27; it
  is generally not taxed again
- **If David died during 2026**: complex transition. The trust converts
  from grantor (taxed to David) to non-grantor (taxed to beneficiaries
  on distribution). Final Form 3520 + 3520-A for David; new analysis
  for Lisa as the US beneficiary going forward
- **If a beneficiary became a US person mid-year**: §679 status adjusts;
  trust ownership may shift; the year of conversion needs careful
  practitioner review
