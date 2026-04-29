# Form 5472 — Line by Line

Walkthrough of every page of Form 5472 with the rule that governs each
line and where the agent should ask vs. compute. Ordered as the form
prints. References are to the most recent revision of Form 5472 (check
revision date in the form's footer). Line numbers are stable but always
cross-check.

## Top of page 1 — Tax year and reporting type

- **Tax year box** — Beginning and ending dates of the reporting
  corporation's tax year. For calendar-year filers, 1/1/YYYY to
  12/31/YYYY.
- **Type of reporting corporation** — Check appropriate boxes:
  - 25% foreign-owned US corporation (Type 1)
  - Foreign corporation engaged in a US trade or business (Type 2)
  - Foreign-owned US disregarded entity (Type 3 — combined with
    pro-forma 1120)

## Part I — Reporting Corporation

### Lines 1a-1g — Identifying information

- **Line 1a** — Name of reporting corporation. For a DE, the LLC's
  legal name as filed with state registration.
- **Line 1b** — Employer ID number. The reporting corp's US EIN. For a
  foreign-owned DE, the EIN obtained via Form SS-4. EIN is mandatory.
- **Line 1c** — Address. Use the corporation's principal US address. A
  DE with no US office uses its registered agent's address (most
  Delaware LLCs use a registered agent service like Harvard Business
  Services or CSC).
- **Line 1d** — Total assets. Year-end book value, US GAAP or local
  GAAP if foreign. For a DE with no operations, this may be just the
  capital contribution from the foreign owner.
- **Line 1e** — Principal business activity. Plain-English description
  + 6-digit NAICS code.
- **Line 1f** — Total US-source gross income. For a Type 3 DE with no
  US-source income, this is $0.
- **Line 1g** — Total payments and receipts from reportable
  transactions. Sum of all monetary flows on all attached 5472s.

### Line 1h — Country(ies) where return is filed for tax purposes

List all foreign countries where the reporting corporation files an
income tax return. For a US C-corp with foreign owner, this is usually
just "United States". For a foreign corp filing 1120-F, list the home
country.

### Line 1i — Country(ies) of filing for tax purposes

Similar to 1h; sometimes the IRS form combines or splits these — read
the current-year instructions.

## Part II — 25% Foreign Shareholder

This identifies the foreign related party. **One Form 5472 per related
party** — if the reporting corp has 3 foreign related parties, file 3
Form 5472s, each with its own Part II.

### Lines 2a-2k — Foreign related party information

- **Line 2a** — Name (legal name as registered in foreign jurisdiction)
- **Line 2b** — US identifying number. If the related party has an EIN
  or ITIN in the US, list it. Otherwise, list the foreign tax ID with
  appropriate prefix or "FOREIGNUS".
- **Line 2c** — Reference ID number. A unique identifier the reporting
  corp assigns to track the related party across years. Once assigned,
  use the same reference ID on every year's 5472 for that party.
- **Line 2d** — Foreign taxpayer ID number (the related party's home
  country tax ID, e.g., German Steuernummer, UK UTR, Canadian BN).
- **Line 2e** — Country in which related party files an income tax
  return as a tax resident.
- **Line 2f** — Address (in foreign country).
- **Line 2g** — Country of citizenship/organization.
- **Line 2h** — Country in which related party's principal business is
  conducted.
- **Line 2i** — Principal business activity (description + NAICS or
  international equivalent).
- **Line 2j** — Ownership percentage. Direct ownership; see line 2k for
  total.
- **Line 2k** — Total direct + indirect ownership percentage.

## Part III — Related Party Other Than Reporting Corp / Direct Owner

If Part II identifies an indirect owner (e.g., the reporting corp is
held by a foreign holding company that is in turn held by an ultimate
foreign individual), Part III identifies the **direct** owner or the
intermediate.

For simple two-level ownership (foreign owner → US sub directly), Part
III duplicates Part II and the form sometimes leaves Part III blank
with notation "Same as Part II".

For multi-level chains, Part III names the intermediate owner. The IRS
needs to map the chain.

### Lines 3a-3j — Direct owner / intermediate identification

Mirror of Part II for the direct/intermediate owner: name, address,
country, ownership %, ID numbers.

## Part IV — Monetary Transactions Between Reporting Corp and Foreign Related Party

The core of the form. For each transaction category, fill the dollar
amount of transactions during the year. Two columns:

- "**Amounts received from related party**" — money flowing from the
  related party TO the reporting corp
- "**Amounts paid to related party**" — money flowing FROM the reporting
  corp to the related party

Don't net offsetting transactions. Show gross flows in each direction.
A US sub that bought $10M of inventory from foreign parent and sold
$3M of inventory to foreign parent reports both $10M and $3M, not net
$7M.

### Line-by-line categories (approximate; verify against current form)

| Line | Category                                                   | Notes                                                       |
|------|-----------------------------------------------------------|-------------------------------------------------------------|
| 8    | Sales of stock in trade (inventory)                       | Goods sold for resale                                       |
| 9    | Sales of tangible property other than stock in trade      | Equipment, fixed assets                                     |
| 10   | Platform contribution transaction amounts                 | Cost-sharing arrangement platform contributions             |
| 11   | Cost-sharing arrangement amounts                          | Annual CSA cost shares                                      |
| 12   | Rents and royalties                                       | Receipts/payments for use of property                       |
| 13   | Sales of intangible property                              | Patents, trademarks, software (transferred not licensed)    |
| 14   | Consideration for services                                | Services rendered between parties                           |
| 15   | Commissions                                               | Sales commissions                                           |
| 16   | Amounts borrowed during year                              | New loans extended TO reporting corp                        |
| 17   | Amounts loaned during year                                | New loans made BY reporting corp                            |
| 18   | Interest                                                  | On any intercompany debt                                    |
| 19   | Premiums received and paid for insurance/reinsurance      | Captive insurance arrangements                              |
| 20   | Other amounts                                             | Reimbursements, management fees, anything not above         |

For each line, fill both columns (received and paid) where applicable.
Leave $0 if no transactions of that type occurred.

### Loan balances (Lines 16, 17)

These lines report **amounts borrowed/loaned during the year**, not
the year-end balance. If the reporting corp repaid an existing loan
and didn't borrow new, Line 16 is $0 even though there was a balance
during the year. The year-end balance is informational only on certain
attached schedules; the 5472 line is about flows.

### Interest (Line 18)

Interest paid to or received from the related party. If a loan
exists but no interest is being charged at AFR, the IRS may impute
interest under IRC §482 / §7872. Document the rate.

### Other amounts (Line 20)

Catch-all for reimbursements, management fees, license fees not
captured above, etc. Most "miscellaneous" intercompany flows land here.
Itemize in a supporting statement attached to Form 5472 (or a footnote
on Line 20 itself if the form provides space).

## Part V — Reportable Transactions of a Reporting Corporation That Is a Foreign-Owned US DE

Used when the reporting corporation is a Type 3 foreign-owned US DE.
Captures transactions between the DE and any related party (most often
just the foreign owner).

Categories include:

- Capital contributions received (e.g., the foreign owner's initial
  $1,000 to fund the LLC)
- Capital distributions paid (the foreign owner's withdrawals)
- Loans (changes during year)
- Interest, services, sales, etc. — same general categories as Part
  IV but tailored to the DE pattern

A Type 3 DE in its formation year reports the formation contribution
in Part V even if no other activity occurred.

A Type 3 DE that received NO contributions and made NO distributions
during a year still files Form 5472 with all-zero Part V — confirming
nothing happened. Filing with all zeros is required; not filing is what
triggers the $25,000 penalty.

## Part VI — Nonmonetary and Less-Than-FMV Transactions

Any transaction not in cash, or any cash transaction not at arm's
length. Examples:

- Equipment transferred from foreign parent to US sub for less than
  FMV
- IP licensed without compensation
- Services performed by one party for the other without billing
- Stock issued for less than FMV consideration

Report:
- Description of property/service
- Date of transaction
- FMV (market value if arm's length)
- Amount actually paid (if any)
- Difference (the IRS uses this to assess transfer pricing
  adjustments under §482)

These transactions are flagged for transfer-pricing scrutiny. The user
should be prepared with §6662(e) contemporaneous documentation if the
amounts are material.

## Part VII — Additional Information About the Reporting Entity, Foreign Shareholders, or Other Persons

Various Yes/No questions. Read carefully against current-year
instructions; the IRS adds and removes questions over revisions.
Common questions:

- Did the reporting corp pay any income to a treaty country at a
  reduced withholding rate? (Form W-8BEN-E elections; treaty positions)
- Does the reporting corp have any cost-sharing arrangements? (If
  yes, complete Part VIII)
- Does the reporting corp have any intercompany loans outstanding at
  year-end? (Balance disclosure)
- Did the reporting corp have any "base erosion payments" subject to
  BEAT? (If yes, complete Part IX)

## Part VIII — Cost-Sharing Arrangement

Only if the reporting corp is party to a CSA under §482 regulations.
The form asks for:

- Identification of the CSA
- Each participant's contribution for the year
- Allocation of intangible development costs
- "Reasonably anticipated benefits" allocation

Most small filers leave Part VIII blank. CSAs are typically a
multinational-corp issue, not a small-DE issue.

## Part IX — Base Erosion Payments (BEAT)

Only if the reporting corp meets the BEAT thresholds under IRC §59A:

- Average annual gross receipts of **$500 million** or more over the
  prior 3 years (or $1 billion for certain foreign banks; verify
  current threshold), AND
- Base erosion percentage of **3%** or more (2% for banks/securities
  dealers)

If both met, BEAT is computed and reported separately on Form 8991.
Part IX of Form 5472 captures the underlying base erosion payments to
related parties.

For 99% of foreign-owned DEs and small-to-mid US C-corps, Part IX is
N/A.

## Signature

Form 5472 is signed by an authorized officer of the reporting
corporation when filed standalone, but more commonly the signature
of the underlying Form 1120 / 1120-F / pro-forma 1120 covers all
attached 5472s. The 1120 signature block is enough; no separate
signature on each 5472.

For a foreign-owned DE, the foreign owner (as Member or Manager of
the LLC) signs the pro-forma 1120. The 5472(s) follow as attachments
under that signature.
