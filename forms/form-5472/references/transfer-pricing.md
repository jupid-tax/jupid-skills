# Transfer Pricing and Form 5472

Transfer pricing is the IRS's mechanism for ensuring that intercompany
transactions between related parties are priced at arm's length — what
unrelated parties would have paid in a comparable transaction. Form
5472 is the primary disclosure of these intercompany flows; transfer
pricing is the substantive law that says what amounts should appear on
each line.

This reference outlines what the agent needs to know about transfer
pricing when drafting a Form 5472, what documentation the user should
have, and the red flags that draw IRS attention.

## The core rule — IRC §482

**IRC §482** authorizes the IRS to allocate income, deductions,
credits, or allowances among related parties when necessary to "clearly
reflect income" — i.e., when the parties' actual pricing departs from
what arm's-length parties would have used.

The arm's-length standard: a transaction's pricing should reflect what
two unrelated parties would have negotiated under comparable
circumstances. If a US sub buys widgets from its German parent at $10
each but unrelated buyers in the same market would pay $7, the IRS
can adjust the US sub's deduction to $7, increasing taxable income by
$3 per widget.

Treas. Reg. §1.482-1 through §1.482-9 specify methods for various
transaction types:

- **§1.482-3** — Tangible property (sales of goods)
- **§1.482-4** — Intangible property (royalties, licenses)
- **§1.482-5** — Comparable Profits Method (a fallback when other
  methods don't fit)
- **§1.482-7** — Cost-sharing arrangements
- **§1.482-9** — Services

For each transaction type, the regs prescribe a method or methods. The
"best method" rule (§1.482-1(c)) requires the taxpayer to choose the
method that produces the most reliable measure of an arm's-length
result.

## What the agent should know for Form 5472

Form 5472 reports the **amounts of intercompany transactions** during
the year. It does NOT compute or assert transfer pricing — that
substantive analysis happens elsewhere (in transfer-pricing studies
and on supporting documentation under §6662(e)).

But the amounts reported on Form 5472 are the IRS's primary lens into
the user's transfer pricing. Large amounts on Lines 12-14 (royalties,
intangibles, services) attract attention. Cost-sharing amounts on
Lines 10-11 attract attention. Loans without interest at AFR attract
attention.

The agent should:

1. Report amounts as they appear on the user's books (don't reprice
   on Form 5472)
2. Flag potential transfer-pricing issues for the user to consider
3. Recommend §6662(e) contemporaneous documentation if the user doesn't
   have it
4. NOT attempt to perform transfer-pricing analysis itself —that's a
   specialist's job

## Documentation the user should have (IRC §6662(e))

IRC §6662(e) imposes a 20% accuracy-related penalty on transfer-pricing
adjustments that exceed certain thresholds. The penalty can be avoided
if the taxpayer maintains "contemporaneous documentation" supporting
the pricing. Documentation must include:

1. Description of the taxpayer's organizational structure
2. Description of the transactions covered
3. Functional analysis of each related party (functions performed,
   risks borne, assets used)
4. Method used to establish arm's-length pricing
5. Comparables used to support the pricing
6. Why the chosen method was the "best method"
7. Any economic analyses or studies
8. Other relevant data

This documentation must be in the taxpayer's possession **on the date
the return is filed**. After-the-fact documentation does not satisfy
§6662(e).

For small filers (foreign-owned DEs with simple flows), formal
transfer-pricing studies are often disproportionate. Practical
documentation:

- A short memo describing the relationship and the basis for pricing
- Comparable rate / price citations (e.g., "We charge our foreign
  parent $X/hour for services, which matches the rate we charge
  unrelated clients for similar services")
- For loans: a comparison to AFR or commercial lending rates
- For royalties: a comparison to industry royalty rate databases
  (RoyaltyStat, ktMINE)
- For services: third-party benchmarks (e.g., "consultants in our
  field charge $200-300/hour for similar work; we charge our parent
  $250/hour")

For mid-size and large filers (substantial intercompany flows), a
formal transfer-pricing study by a specialist firm (Big Four,
boutique TP firm) is standard.

## Common red flags on Form 5472

These attract IRS attention and likely audit scrutiny:

### High royalty rates to foreign parent

Royalty payments on Line 12 exceeding 5% of US sub gross income
suggest aggressive transfer pricing. Reasonable royalty rates depend
on industry but commonly fall in the 3-8% range for established IP.
Rates above 10% are unusual and require strong support.

### Intercompany loans without interest at AFR

If a foreign parent lent funds to a US sub at 0% interest (or below
AFR), the IRS will impute interest at AFR under §482 / §7872. The
imputed interest creates additional taxable income to the parent and
deduction to the sub, but more importantly, the IRS may then
recharacterize the underlying transaction as a disguised dividend.

### Sales of inventory at non-market prices

US sub buys inventory from foreign parent at prices that produce
unusually low (or unusually high) gross margins for the US sub. The
IRS compares the US sub's gross margin to industry benchmarks for
similar resellers; significant deviation triggers adjustment.

### Cost-sharing arrangements without a written agreement

If parties claim a CSA on Form 5472 Part VIII but lack a written
arrangement meeting Treas. Reg. §1.482-7(b) requirements, the IRS may
disallow the CSA characterization and impose a "buy-in" payment — a
payment from US sub to foreign parent for past intangible
contributions, often in the millions.

### IP transfers for less than FMV

A foreign parent transfers IP to its US sub for nominal consideration,
or vice versa. Reported on Form 5472 Part VI as a non-monetary
transaction. The IRS will assess the FMV of the transfer and adjust the
parties' basis and income; under §367(d), an outbound transfer of IP
from the US triggers ongoing deemed royalty income to the US transferor.

### Management fees / service charges with no apparent service

US sub pays a $200,000 "management fee" to foreign parent each year
with no documentation of services performed. The IRS reclassifies as a
disguised distribution (constructive dividend), nondeductible.

### "Cost plus" services with high markups

Foreign parent provides services to US sub at cost plus 30%+. Industry
benchmarks for routine back-office services typically support markups
of 5-10%. Markups outside this range require specific economic
justification.

## What the agent does when transfer pricing is suspect

If the agent identifies a likely transfer-pricing issue (high
royalties, no-interest loans, services with no documentation, etc.):

1. **Flag in the validation summary** — surface the issue to the user
2. **Recommend §6662(e) documentation** — tell the user to prepare or
   obtain contemporaneous documentation before filing
3. **Recommend a transfer-pricing specialist** for non-trivial flows
   (typically: any single line item > $1M, total intercompany flows
   > $10M, or any cost-sharing / IP transfer arrangement)
4. **Do NOT reprice on Form 5472** — the form reports actual
   transactions, not what the IRS might adjust them to. Repricing
   is the substantive position the user takes; it goes on the
   underlying 1120 / 1120-F (e.g., a §482 adjustment showing on the
   tax return), not on Form 5472.

## Transfer pricing for foreign-owned DEs

Most foreign-owned DEs have minimal transfer-pricing exposure because
they're disregarded for income tax — no separate corporate income to
allocate. However:

- **Loans between DE and foreign owner**: imputed interest applies if
  no rate or below-AFR rate
- **Services performed by foreign owner for the DE** (or vice versa):
  technically related-party services subject to §482; in practice
  often informal but documentable
- **Sales between DE and foreign owner's other entities**: sister
  entity transactions; full §482 analysis needed if material

For a typical small foreign-owned DE (e-commerce, holding LLC), the
transfer-pricing posture is usually:

- Foreign owner contributes capital → arm's length (no
  consideration; no §482 issue)
- Foreign owner withdraws distributions → arm's length (no
  consideration)
- DE pays no royalties, no service fees, has no intercompany loans

In this simple pattern, transfer pricing is not a concern. As soon as
intercompany **flows** exist (loans, services, IP licensing), §482
enters the picture.

## The practical position for the skill

For a typical small filer with simple flows:
- Report amounts on Form 5472 as they appear on books
- Flag any transaction > $100,000 with a related party for the user to
  confirm transfer-pricing support exists
- Recommend §6662(e) documentation as a baseline
- Do not perform substantive transfer-pricing analysis

For a mid-to-large filer or any complex pattern:
- Recommend the user engage a transfer-pricing specialist before
  filing
- Note in validation summary: "Transfer-pricing review recommended;
  amounts on Lines X, Y exceed materiality thresholds"
- Do not file without practitioner sign-off

The penalties for getting transfer pricing wrong are substantial: 20%
or 40% accuracy-related penalty under §6662(e) on top of the tax
adjustment. Form 5472 is the IRS's first lens; getting the form right
matters but doesn't fix bad pricing.
