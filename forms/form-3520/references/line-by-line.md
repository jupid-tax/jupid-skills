# Form 3520 — Line by Line

Walkthrough of every page of Form 3520 with the rule that governs each line
and where the agent should ask vs. compute. Ordered as the form prints.
References are to the 2024-revision Form 3520 PDF; line numbers are stable
across revisions but always cross-check against the year being filed.

## Page 1 — Identifying information and filing triggers

### Filer identification block

- **Line 1a** — Name of US person (filer). Use the legal name from Form
  1040. For a domestic estate or trust, the legal name from Form 1041.
- **Line 1b** — Filer's identifying number: SSN for individuals, ITIN if
  no SSN, EIN for entity filers (estate/trust/partnership/corporation).
- **Lines 1c-1f** — Mailing address. Use the address used on Form 1040 or
  1041 for the same year. If the filer is abroad, use the foreign address.
- **Line 1g** — Check if the filer is an individual; otherwise mark the
  type (partnership, corporation, estate, non-grantor trust, etc.)
- **Line 1h** — Filing status: Single, MFJ, MFS, HoH, QW. Match Form 1040.
- **Line 1i** — If amended return, check the box and identify the original
  filing date.

### Spouse identification (if joint Form 3520)

- **Lines 2a-2f** — Spouse name, SSN, address. Only complete if filing a
  joint Form 3520 (allowed when both spouses file a joint Form 1040 AND
  both have reportable transactions on the same Form 3520; see Form 3520
  instructions).

### Trigger boxes (top of page 1)

- Box A — Filing because of transfer to foreign trust (Part I)
- Box B — Filing as US owner of foreign trust (Part II)
- Box C — Filing because of distribution from foreign trust (Part III)
- Box D — Filing because of receipt of foreign gift/bequest (Part IV)

The user can check multiple boxes. The Parts they fill must match the
boxes checked.

### Initial / Final / Amended

- **Initial return** — first time filing for this trust/situation
- **Final return** — last time (e.g., trust terminated, last distribution
  received)
- **Amended return** — supersedes a prior 3520 for the same year. Show the
  changed lines and attach an explanation.

---

## Part I — Transfers by US Persons to a Foreign Trust

Filed when the user transferred cash, property, or services (gratuitously
or at less than FMV) to a foreign trust during the tax year. Also filed
when the user's death triggers a transfer (special exception applies).

### Lines 5a-5h — Foreign trust identification

- **Line 5a** — Trust name (legal name as registered in the foreign
  jurisdiction)
- **Line 5b** — Trust EIN if any. Many foreign trusts have no US EIN; if
  none, write "N/A". Some practitioners obtain a US EIN for the foreign
  trust to facilitate compliance — ask the user.
- **Line 5c** — Country in which the trust was created
- **Line 5d** — Country whose laws govern the trust (sometimes different
  from the country of creation)
- **Line 5e** — Date trust was created
- **Line 5f-5h** — Trust mailing address

### Line 6 — Trustee information

For each trustee: name, address, country. If the trustee is an institution
(a foreign bank or trust company), use the institutional name and address.

### Line 7 — Identification of US agent (if appointed)

A US person who is the grantor of a foreign trust may appoint a US agent
under IRC §6048(b)(2). If a US agent is appointed and accepts service of
process, certain reporting simplifications apply (the IRS can audit the
trust through the US agent rather than treating all trust transactions as
deemed income to the grantor). If no US agent is appointed, the IRS may
recharacterize trust transactions as deemed income.

Ask the user: "Has a US agent been appointed for this trust under
§6048(b)(2)? If yes, the agent's name and address. If no, this is fine
but the IRS may apply less favorable presumption rules."

### Lines 9-18 — Transfer details

- **Line 9** — Cash transferred during the year (USD)
- **Line 10** — FMV of property transferred. For non-cash property, attach
  a description and valuation method.
- **Lines 11-13** — Loans to the trust, sale of property to the trust,
  other transactions. Each row: description, date, amount.
- **Lines 14-17** — Tax basis of property transferred (separate from FMV);
  description of property in detail
- **Line 18** — Total transfers, summing prior lines

### Schedule A of Part I — Obligations received

If the user received an obligation from the trust in exchange for the
transfer (e.g., a note), Schedule A documents it. A "qualified obligation"
under Treas. Reg. §1.679-4(d)(1) avoids treating the transfer as a
gratuitous transfer:

- Term of obligation ≤ 5 years
- Stated principal in USD or specified foreign currency
- Interest at rate ≥ AFR for the obligation's term
- Filer agrees to extend statute of limitations on assessment for the
  transfer

If any condition fails, the obligation is "non-qualified" and the
transfer's full FMV is reported in Part I as if no obligation existed.

---

## Part II — US Owner of a Foreign Trust

Filed when the user is treated as the owner of any portion of a foreign
trust under the grantor trust rules (IRC §§671-679). The most common
trigger is **§679**: a US person who transferred property to a foreign
trust at any time, where the trust has at least one US beneficiary, is
treated as the owner.

### Lines 19-21 — Trust identification

Same data as Lines 5a-5h. If the user filed Part I in a prior year for
this trust, the same identifying information should appear here.

- **Line 21** — Date the user became the US owner. For §679, this is
  generally the date of the transfer (not retroactive).

### Line 22 — US owner's portion of trust

Describe in detail the user's portion of the trust. For each item:

- Beginning-of-year FMV of US owner's portion
- Trust income earned attributable to US owner during the year
- Trust expenses attributable to US owner
- Distributions during the year to US owner (cross-reference to Part III)
- End-of-year FMV

The amounts here should match the **Foreign Grantor Trust Owner Statement**
attached (page 3 of Form 3520-A). If the trust didn't file Form 3520-A,
the user must file a substitute (see `3520-vs-3520-a.md`).

### Box at top of Part II — "Did the foreign trust file Form 3520-A?"

- **Yes** — confirm the trust's 3520-A was filed by March 15 (or by the
  trust's extended due date if Form 7004 was filed). Attach the Foreign
  Grantor Trust Owner Statement (page 3) to Part II.
- **No** — file a substitute Form 3520-A as an attachment. The substitute
  is a fully completed 3520-A signed by the US owner with notation
  "Substitute" in the heading.

If neither path is taken, the user faces a §6677 penalty equal to 5% of
the trust's gross value (per IRC §6677(b)).

---

## Part III — Distributions From a Foreign Trust to a US Person

Filed when the user received any distribution (cash, property, or use of
trust property) from a foreign trust during the tax year. Loans from a
foreign trust that are not "qualified obligations" are treated as
distributions under IRC §643(i).

### Lines 24-26 — Trust identification

Same identification as Lines 5/19. Critical addition:

- **Line 26** — Type of trust: Grantor or Non-grantor. If grantor (the US
  owner already reports trust income), the distribution is generally tax
  free to the recipient (it's already been taxed to the owner). If
  non-grantor, the distribution carries DNI / UNI and may trigger
  throwback tax.

### Line 27 — Foreign Nongrantor Trust Beneficiary Statement

- **Yes** — actual method available. Use Schedule B of Part III to compute
  the income / corpus split per the statement.
- **No** — default method required. Use Schedule C of Part III to compute
  the deemed accumulation distribution and §668 interest charge.

### Lines 28-29 — Distribution details

For each distribution:

- Date received
- Type (cash, property, use of property — including rent-free use of
  foreign real estate held by the trust, valued at fair rental value)
- FMV in USD on the date of receipt

### Schedule A — Distributions from a grantor trust with a US owner

If the trust is a grantor trust with a US owner who received the
distribution, the distribution is generally not separately taxable. The
US owner already reported the trust's income on their 1040 (via the
Foreign Grantor Trust Owner Statement). Schedule A documents the
distribution but no tax flows through.

### Schedule B — Actual method (Beneficiary Statement provided)

Use the statement's allocation of the distribution between current-year
DNI (taxable to the recipient as ordinary income, capital gain, etc.,
based on the statement's character classifications) and corpus (tax-free).

### Schedule C — Default method

Without a Beneficiary Statement, the default method computes:

1. **Average distribution over prior 3 years** = (sum of distributions
   from this trust to this beneficiary in years 1-3) ÷ 3
2. **Excess distribution** = current-year distribution − 1.25 × average
3. The excess is treated as a "deemed accumulation distribution" — UNI
   carryout taxable in the current year
4. The throwback tax is computed on **Form 4970** (Tax on Accumulation
   Distribution of Trusts) and added to Form 1040 tax
5. An **interest charge** under IRC §668(a) applies, computed using the
   underpayment rate from the year the income was deemed accumulated
   through the current year

The default method almost always produces a worse outcome than actual
method. Recommend the user request a Beneficiary Statement from the
trustee for current and future years.

See [`throwback-default-method.md`](./throwback-default-method.md) for the
mechanics.

---

## Part IV — US Recipients of Gifts or Bequests From Foreign Persons

Filed when aggregate gifts/bequests during the tax year exceed:

- **$100,000** from foreign individuals + foreign estates (statutory; not
  inflation-adjusted; IRC §6039F(c)(1)(B))
- **Inflation-adjusted threshold** from foreign corporations + foreign
  partnerships. Rev. Proc. 2024-40 set this at **$19,570 for 2025**. The
  2026 figure will be in the 2025 inflation-adjustment Rev. Proc. — verify
  before filing using the current-year Form 3520 instructions.

### Line 54 — Gifts from foreign individuals + foreign estates

Aggregate threshold check first. If aggregate ≤ $100,000, Part IV is not
required for these donors and the line is blank.

If aggregate > $100,000:

- Itemize each donor that contributed > $5,000 individually
- Donors that contributed ≤ $5,000 can be aggregated as "various donors,
  each ≤ $5,000"
- For each itemized donor: name, address, country, relationship to filer,
  date of each gift, description, FMV in USD

### Line 55 — Gifts from foreign corporations + foreign partnerships

If aggregate > the inflation-adjusted threshold, all such donors are
itemized regardless of individual amount. For each: donor name, address,
country, type (corporation/partnership), date, description, FMV.

### Line 56 — Additional questions about Line 55 donors

- Was the donor a related person to the filer or to a US person? (This
  goes to whether the gift might actually be a §301 distribution
  recharacterizable as income.)
- Is the donor a CFC (controlled foreign corporation) or PFIC (passive
  foreign investment company)? If yes, additional reporting may apply on
  Form 5471 / Form 8621.

### What Part IV is NOT

- Not a tax computation. Gifts and bequests are excluded from gross income
  under IRC §102. The reporting is purely informational.
- Not for gifts received indirectly through a domestic intermediary (those
  are not "from a foreign person" for §6039F purposes — but they may be
  reportable on other forms if the intermediary is a foreign trust).
- Not for purchases at FMV. A bona fide sale isn't a gift even if the
  buyer is a foreign person.

### Rebutting the §6039F(b) presumption (Line 55 only)

If the donor is a foreign corporation or partnership above the threshold,
the IRS may presume the "gift" is actually disguised income (e.g., a
bonus, a dividend, or compensation routed through a related entity). To
rebut, attach a statement explaining:

- The donor's relationship to the recipient (no employment, no service,
  no investment relationship)
- The donative intent of the donor
- Whether the donor expects anything in return

---

## Signature

The filer signs at the bottom of page 6. For a joint return, both spouses
sign. For a corporate or trust filer, an authorized officer/trustee signs.
**Wet ink signature required** — Form 3520 is paper-only and the IRS does
not accept digital signatures on paper-filed information returns as of 2026.

If a paid preparer assisted, the preparer signs and provides PTIN. Most
3520s are self-prepared or attorney-prepared; CPAs and EAs sign in their
PTIN block.
