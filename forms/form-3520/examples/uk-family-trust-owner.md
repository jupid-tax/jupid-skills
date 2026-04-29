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
  threshold)
- David also files FBAR (FinCEN 114) for the trust's UK bank account
  (signature authority via beneficial interest)
- David did NOT receive any distribution from the trust in 2026; if he
  had, Part III would also apply on the same Form 3520

## The 3520-A problem

Crockett, Hughes & Partners LLP (UK trustees) refuse to file Form 3520-A.
Their position: they have no US tax filing obligation. David has tried
since 2021 to convince them; they remain firm.

David must file a **substitute Form 3520-A** as an attachment to his
Form 3520 Part II, signed by him as US owner.

## Trust data for tax year 2026

David obtained the trust's UK accounting (prepared by the trustees for
UK tax purposes) and converted the figures to USD using the **Treasury
yearly average rate for 2026** (illustrative: $1.2540/GBP; verify against
https://www.fiscal.treasury.gov/reports-statements/treasury-reporting-rates-exchange/).

### Trust beginning-of-year FMV (2026-01-01)

- UK investment portfolio: £405,000 → $507,870
- Manchester rental property: £278,000 → $348,612
- UK bank account: £8,400 → $10,533
- **Total**: $867,015

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

His Foreign Grantor Trust Owner Statement (page 3 of the substitute
3520-A) shows: 100% ownership, $886,327 year-end FMV attributable to him,
$49,157 trust income reportable on his Form 1040, $11,537 trust expenses
deductible.

## Part III consideration

David received no distribution. Sophie's $10,032 distribution is to a
non-US beneficiary; it doesn't trigger Part III for David (Part III
covers distributions to US persons).

If Lisa had received a distribution, she would file her own Part III on
this same joint Form 3520 (one Form 3520 per joint 1040 is allowed).

## Filled draft

```markdown
# Form 3520 — DRAFT for tax year 2026

## Filer identification
Name: David Hughes
Identifying number: 234-56-7890
Address: 218 Beacon Hill Road, Berkeley, CA 94708
Filing status: MFJ (joint with Lisa Hughes, SSN 234-56-7891)
Country of citizenship: USA (also UK)
Initial: No (5th annual filing for this trust)

Spouse identification:
Name: Lisa Hughes
SSN: 234-56-7891
(Filing jointly because both spouses are reportable persons —
Lisa is a contingent beneficiary; one Form 3520 covers both)

## Parts being filed
- [ ] Part I
- [x] Part II — US owner of foreign trust
- [ ] Part III — (would apply if Lisa or David received distribution)
- [ ] Part IV

## Part II — US Owner

Foreign trust name: Hughes Family Trust (UK)
Trust country: United Kingdom
Trust EIN (US): 99-XXXXXXX (obtained 2021 via SS-4)
Trust governing law: English
Date trust created: 2021-06-15
Date David became US owner: 2021-06-15
US agent appointed under §6048(b)(2): Yes — David Hughes, self
  (filer designated himself as US agent per Form 3520 Part I from 2021)

Form 3520-A filed by trust for 2026: No
Substitute Form 3520-A attached: Yes

US owner's portion (100% of trust, all attributable to David's transfer):
| Line | Item                            | Amount (USD) |
|------|----------------------------------|--------------|
|      | Beginning-of-year FMV           | $867,015     |
|      | Trust income (2026)             | $49,157      |
|      | Trust expenses (2026)           | $11,537      |
|      | Net income passing through      | $37,620      |
|      | Distributions in 2026           | $10,032      |
|      |   (all to non-US beneficiary)   |              |
|      | End-of-year FMV                 | $886,327     |

Foreign Grantor Trust Owner Statement (page 3 of substitute 3520-A)
attached: Yes

## Currency translation
Source: Treasury yearly average exchange rate for 2026
Rate: $1.2540/GBP (verify against fiscal.treasury.gov before filing)
Notes: All trust income, expense, distribution figures translated at
yearly average; FMV figures translated at year-end and beginning-of-year
spot rates respectively (year-end 2025 = $1.2410/GBP; year-end 2026 =
$1.2540/GBP, illustrative)

## Required attachments
- [x] Substitute Form 3520-A (full form, signed by David as US owner)
- [x] Foreign Grantor Trust Owner Statement (page 3 of 3520-A)
- [x] Statement of reasonable effort to obtain trustee filing
      (correspondence with Crockett, Hughes & Partners LLP showing
      annual requests and trustee refusals)
- [ ] Trust instrument (kept with David's records; not refiled annually)

## Mailing address
Internal Revenue Service Center
P.O. Box 409101
Ogden, UT 84409

## Validation summary
- Math: trust income $49,157 = dividends $17,807 + rent $23,324 +
  cap gains $8,026 ✓
- Math: trust expenses $11,537 = trustee $6,019 + property $4,013 +
  accountant $1,505 ✓
- Math: end-FMV $886,327 = portfolio $526,680 + property $351,120 +
  bank $8,527 ✓
- Sanity: trust has accumulated UK undistributed income; future
  distributions to David will be tax-free corpus return (he's already
  paid US tax annually on the trust's income via this Part II). Future
  distributions to Lisa (if she inherits the trust on David's death)
  may convert this to a non-grantor trust → throwback consideration
  for her downstream
- Sanity: substitute 3520-A signed by David, not the UK trustees;
  reasonable cause statement on file documenting trustee refusal
- Next steps:
  1. David and Lisa both sign Form 3520 page 6 in blue ink
  2. David signs the substitute 3520-A as US owner
  3. Mail combined package (Form 3520 + substitute 3520-A + Owner
     Statement + reasonable cause statement) to Ogden by April 15, 2027
     (or October 15, 2027 if Form 4868 extension filed for 1040)
  4. On Form 1040, report the $37,620 net trust income via Schedule 1
     and apply UK foreign tax credit on Form 1116 for any UK tax paid
     by the trust on the same income (treaty article on dividends,
     rental income, and capital gains)
  5. Continue annual FBAR for the trust's UK bank account
  6. Continue annual Form 8938 reporting

## Sources cited in this draft
- IRS Form 3520 (latest revision)
- IRS Instructions for Form 3520 (latest revision)
- IRS Form 3520-A (latest revision)
- IRC §679 (foreign trust having US beneficiaries)
- IRC §6048 (information returns)
- IRC §6677 (penalties)
- Treas. Reg. §1.679-1 through §1.679-4
- Notice 97-34 (substitute filings by US owner)
- US-UK Income Tax Treaty (1980, as amended)
- Treasury yearly average exchange rates
```

## Why this case is hard

- Trustee refuses to file 3520-A → substitute required every year
- Trust holds non-financial property (rental real estate) in addition to
  financial assets → Form 8938 needs to itemize the property
  classification carefully
- Multiple compliance regimes apply simultaneously: 3520, 3520-A
  (substitute), 8938, FBAR, Form 1040 with foreign tax credit
- David must maintain documentation of his "reasonable effort" to
  obtain trustee cooperation, in case the IRS challenges the substitute
  filing position

## What would change this case

- **If David transferred property to the trust in 2026**: also file
  Part I for the new transfer, in addition to Part II
- **If David received a distribution in 2026**: also file Part III. As a
  US owner of a grantor trust, the distribution is generally tax-free
  (Schedule A of Part III applies)
- **If David died during 2026**: complex transition. The trust converts
  from grantor (taxed to David) to non-grantor (taxed to beneficiaries
  on distribution). Final Form 3520 + 3520-A for David; new analysis
  for Lisa as the US beneficiary going forward
- **If a beneficiary became a US person mid-year**: §679 status adjusts;
  trust ownership may shift; the year of conversion needs careful
  practitioner review
