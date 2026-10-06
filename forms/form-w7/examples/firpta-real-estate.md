# Example — Foreign Real Estate Investor (FIRPTA Withholding)

## Facts

- **Applicant (W-7 subject)**: Lin Wei, Chinese citizen and resident; never lived in the US; non-resident alien for US tax purposes
- **Transaction**: Lin is buying a $1.4 million single-family rental investment property in Miami, FL. Closing scheduled for May 2026.
- **Why an ITIN is needed**:
  - As a foreign buyer, Lin will rent out the property and earn US-source rental income subject to either §871(d) net election (taxed as ECI on Form 1040-NR) or §871(a) gross 30% withholding via Form 1042-S. Either way, Lin needs an ITIN to file 1040-NR or have Form 1042-S issued.
  - More urgent: Lin plans to **resell** the property in 3-5 years. When she does, FIRPTA (IRC §1445) requires the buyer to withhold 15% of the gross sale price on a sale by a foreign person. To **reduce or eliminate** that withholding (because the actual capital gain tax owed will be far less than 15% of gross), Lin can file **Form 8288-B (Application for Withholding Certificate)** at the time of resale — but Form 8288-B requires an ITIN.
  - Lin's CPA recommends getting the ITIN now (during purchase) so that all rental-period reporting (Form 1042-S, 1040-NR) flows through smoothly and so that when resale time comes, Lin can move quickly on the 8288-B without a 9-11 week ITIN delay (processing time for applications from overseas).
- **Identification documents Lin has**:
  - Chinese passport, valid through 2030
  - Chinese national ID card
  - Chinese household registration ("hukou")
- **No US tax filing yet** — this is Lin's first interaction with the US tax system
- **Lin will not be in the US** during the W-7 application; she's in Shanghai

## Analysis

### Step 1 — SSN ineligibility

Lin is a non-resident alien with no US visa, no US work authorization, and no plans to immigrate. She is not SSN-eligible. ITIN is the appropriate TIN.

### Step 2 — Reason code

This is the key decision for Lin's situation. Several reason codes could apply:

- **(b)** Nonresident alien filing a US federal tax return — applies once Lin files a 1040-NR for rental income
- **(h)** Other — appropriate when applying under an Exception (no current tax return required)

For the **purchase** stage (now), Lin doesn't yet have a 1040-NR to file (no rental income yet). She's applying for the ITIN proactively. This places her under **Exception 3** (third-party reporting of mortgage interest — if she's financing the purchase with a US mortgage and the lender will issue Form 1098 in her name). Exception 3 is written for a "home mortgage loan on real property located in the United States"; ask the user to confirm the loan is a mortgage the lender will report on Form 1098 before relying on it.

If Lin is **paying cash** (no mortgage), Exception 3 doesn't apply. Exception 4 doesn't apply to her purchase either: it covers dispositions of US real property interests *by a foreign person* (the foreign seller, or a buyer withholding from a foreign seller). It becomes relevant when Lin sells.

**Most clean approach without a mortgage**: wait until rental income starts (Lin's first rent check after closing), then file W-7 under reason **(b)** with the first 1040-NR she files.

**With a US mortgage**: file W-7 now under **Exception 3**, reason code **(h)** — Other.

For this example: assume Lin is taking a US mortgage to finance the property. Use **Exception 3**, reason code **(h)**.

### Step 3 — Identification documents

Lin's Chinese passport is the cleanest single-document option. It proves both identity and foreign status. No second document needed.

**Submission options**:
1. Mail original passport from China to IRS Austin — risky (3+ months without passport, international mail risk)
2. Mail certified copy from issuing authority — Lin can request a certified copy from the Chinese passport authority or from the Chinese consulate in the US (not directly available to her in Shanghai; may need to use a designated agent)
3. **Use a Certifying Acceptance Agent (CAA)** — a CAA must review the original passport or a certified copy from the issuing agency; notarized copies and scans are not accepted (ITIN supporting documents page).
4. **CAA in China**: the IRS acceptance agent list includes agents in China and Hong Kong: https://www.irs.gov/tin/itin/itin-acceptance-agents
5. In-person TAC: not feasible — Lin would have to fly to a US TAC

For this example: **Lin uses a CAA in Shanghai**. Cost ~$300-500 (international CAA fees are higher).

### Step 4 — Exception application — no tax return attached

Under Exception 3, Lin's W-7 is **not** attached to a 1040-NR. She files the W-7 alone with supporting evidence. The Exceptions Table requires "documentation showing evidence of a home mortgage loan," including "a copy of the contract of sale or similar documentation":

- Copy of the purchase contract for the Miami property showing Lin as buyer
- Mortgage loan documents (commitment letter, note, or Closing Disclosure) showing Lin as borrower
- Optional: a lender letter confirming it will report mortgage interest on Form 1098 in Lin's name

### Step 5 — Fill the W-7

Key fields:

- Reason: check **box (h) — Other**; on the dotted line write "Exception 3-Mortgage Interest"
- Application type: **Apply for a new ITIN**
- Line 1a: LIN WEI (passport rendering, or "Wei Lin" with surname-first noted on Chinese passport)
- Line 2 (mailing address): Lin's address in Shanghai, where she receives mail (the IRS mails the CP565 there; the CAA also receives a copy)
- Line 3: re-enter the same Shanghai address (the instructions require the foreign address even when it matches line 2)
- Line 4: DOB, place of birth (Shanghai, China)
- Line 5: Female
- Line 6a: China (citizenship)
- Line 6b: Lin's Chinese tax ID (Citizen ID Number) if she has one
- Line 6c: N/A (no U.S. visa)
- Line 6d: Passport box; issued by China; number; expiration 2030; date of entry into the United States: "Never entered the United States" (Pub 1915 wording)
- Line 6e: No/Don't know (never had an ITIN or IRSN)
- Line 6f: N/A
- Line 6g: N/A
- Sign and date

### Step 6 — Supporting evidence

Attach to the W-7:

- Property purchase contract showing Lin as buyer
- Mortgage commitment letter or Closing Disclosure showing the home mortgage loan
- Lender letter (optional, per Step 4 above)

### Step 7 — Submit

Mail to the **ITIN Operation Center**:

```
Internal Revenue Service
ITIN Operation
P.O. Box 149342
Austin, TX 78714-9342
```

For courier (FedEx, UPS, DHL — verify the courier address, different from PO Box):
```
Internal Revenue Service
ITIN Operation
Mail Stop 6090-AUSC
3651 S. Interregional Hwy 35
Austin, TX 78741-0000
```
(Verify against current Pub 1915.)

CAA process: the CAA in Shanghai prepares the package, certifies the passport copy, and sends it via international courier to Austin. CAA also files Form W-7 COA (Certificate of Accuracy). Lin keeps her original passport in Shanghai.

### Step 8 — Wait

Processing: allow 7 weeks; 9-11 weeks for applications from overseas or submitted January 15 through April 30. Lin applies from overseas, so plan on 9-11 weeks.

Lin should expect the CP565 by August 2026 if filed in May 2026.

### Step 9 — After ITIN is issued

Lin can now:
- Receive Form 1098 from the US lender with her ITIN
- File Form 1040-NR for the year of the property purchase (and each subsequent year of rental income)
- Make the §871(d) election to treat rental income as ECI (effectively connected income), allowing deduction of mortgage interest, depreciation, property tax, etc.
- When resale time comes (3-5 years), file Form 8288-B to apply for a withholding certificate that reduces FIRPTA withholding from 15% of sale price to a smaller amount tied to actual gain

### Step 10 — When Lin sells the property (future)

This is when the ITIN becomes critical:

- Buyer of the property must withhold 15% of gross sale price under §1445 unless reduced by IRS withholding certificate
- Lin (or her CPA) files Form 8288-B with the IRS BEFORE closing, requesting a reduced withholding amount
- Form 8288-B requires Lin's ITIN
- IRS issues a withholding certificate within ~90 days, allowing buyer to withhold a smaller amount (tied to actual capital gains tax estimated)
- Lin then files 1040-NR for the year of sale, claiming credit for the withheld amount, paying any balance or receiving refund

Without an ITIN obtained in advance, Lin would face full 15% gross withholding ($210,000 on a $1.4M sale), and waiting for ITIN + 8288-B during a closing is a recipe for delay.

## Validation checks

- [x] Reason code (h) checked with "Exception 3-Mortgage Interest" on the dotted line
- [x] Mailing address is Lin's Shanghai address
- [x] Passport submitted via CAA-certified copy (originals stay with Lin)
- [x] Contract of sale and mortgage documents showing the home mortgage loan attached
- [x] Lines 6e-6g answered, date of entry reads "Never entered the United States"
- [x] No 1040-NR attached (Exception 3 path — no tax return required at this stage)
- [x] Mailed to ITIN Operation Austin

## Lessons

1. **Get the ITIN before you need it**: applying during property purchase rather than waiting for resale avoids 9-11 weeks of delay during a time-pressured closing.
2. **FIRPTA 15% gross withholding** can be reduced via Form 8288-B — but only if you have an ITIN. The ITIN is the gating prerequisite for foreign real estate investors.
3. **Reason code (h) + Exception 3** is the path for foreign buyers with a US mortgage reported on Form 1098. Without a mortgage (cash purchase), the cleanest path is to wait until rental income starts and file W-7 with the first 1040-NR (reason code (b)).
4. **CAA in the foreign country** is the most operationally efficient option — Lin doesn't have to mail her passport internationally.
5. **§871(d) election**: foreign rental property income can be treated as ECI (effectively connected income), enabling deductions. Without the election, gross income is subject to 30% withholding with no deductions. The election is made on the first 1040-NR.
6. **Different ITIN mailing address** vs. regular 1040 address — always send W-7 packets to the Austin ITIN Operation.

## Citations

- IRC §1445 — FIRPTA withholding on sale of US real estate by foreign person
- IRC §871(d) — election to treat real property income as ECI
- IRC §6050H — mortgage interest reporting on Form 1098
- IRC §6109 — TIN requirements
- Form 8288-B — Application for Withholding Certificate for Dispositions by Foreign Persons of US Real Property Interests
- Pub. 519 — US Tax Guide for Aliens
- Pub. 1915 — Understanding Your IRS ITIN
- Form W-7 instructions (Rev. December 2024), Exception 3 — third-party reporting of mortgage interest
- Form W-7 instructions (Rev. December 2024), Exception 4 — disposition by a foreign person of a U.S. real property interest
- IRS Acceptance Agent Program — international CAA list
