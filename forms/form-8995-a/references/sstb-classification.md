# SSTB Classification

A **Specified Service Trade or Business (SSTB)** triggers different §199A treatment above the income threshold: in the phase-in zone, the deduction phases out; above the phase-in zone, the deduction is zero. Below the threshold, SSTB status is irrelevant.

This reference helps the agent classify each business correctly and surface borderline cases for user confirmation.

---

## The 11 SSTB categories (IRC §199A(d)(2)(A) + Treas. Reg. §1.199A-5(b)(2))

### 1. Health

Includes: physicians, dentists, pharmacists, nurses, dentist hygienists, physical therapists, psychologists, veterinarians, and "other similar healthcare professionals."

Specifically excluded by Treas. Reg. §1.199A-5(b)(2)(ii): services not directly related to a medical services field, such as the operation of health clubs or health spas, payment processing, and the research, testing, manufacture, and sale of pharmaceuticals or medical devices.

**Edge cases:**
- A **medical research lab** that doesn't treat patients is NOT health SSTB
- A **medical device manufacturer** is NOT SSTB
- A **healthcare staffing agency** that places nurses but doesn't treat patients — facts and circumstances; consult specific guidance

### 2. Law

Includes: lawyers, paralegals, legal arbitrators, mediators, and similar professionals.

Excluded: services not requiring legal skills (e.g., printing, publishing, law-firm IT services).

### 3. Accounting

Includes: CPAs, enrolled agents, bookkeepers, tax preparers (Reg. §1.199A-5(b)(2)(iv)).

Excluded: payment processing, financial software vendors.

### 4. Actuarial Science

Includes: actuaries and similar professionals computing risk and probability for insurance and pensions.

### 5. Performing Arts

Includes: actors, singers, musicians, dancers, directors, and other "performing artists" providing services in their capacity as artists.

Excluded: support services (lighting technicians, set designers, broadcasters who don't perform).

### 6. Consulting

Includes: any business providing professional advice and counsel to clients to assist them in achieving goals or solving problems.

**The biggest gray area.** Per Treas. Reg. §1.199A-5(b)(2)(vii):

- Pure "consulting" (advice + recommendations + no other services) → SSTB
- Consulting embedded in, or ancillary to, the sale of goods or performance of services by a non-SSTB, with no separate payment for the consulting → not consulting (Reg. §1.199A-5(b)(2)(vii))
- De minimis rule for any SSTB field (Reg. §1.199A-5(c)(1)): gross receipts of $25 million or less → not an SSTB if less than 10% of gross receipts come from the specified service; gross receipts over $25 million → less than 5%

**Critical exclusions from "consulting":**
- **Software development and IT services** — not a listed field; consulting means advice and counsel and "does not include the performance of services other than advice and counsel" (Reg. §1.199A-5(b)(2)(vii)). Writing and delivering code is a service other than advice; separately billed IT advice can be consulting. Ask what the client pays for
- **Engineering services** — explicitly excluded by IRC §199A(d)(2)(A) (architecture and engineering carve-out)
- **Sales** (or economically similar services) — excluded from consulting; consulting with no separate payment that is ancillary to a non-SSTB's sales is not consulting (Reg. §1.199A-5(b)(2)(vii))

### 7. Athletics

Includes: athletes, coaches, team managers, and others performing services in athletic competitions.

### 8. Financial Services

Includes: financial advisors, wealth managers, retirement planners, retirement plan advisors. Treas. Reg. §1.199A-5(b)(2)(ix).

Excluded: banking (taking deposits, making loans), insurance underwriting, real estate, payment processing.

### 9. Brokerage Services

**Only securities brokerage.** Real estate brokerage and insurance brokerage are NOT SSTB. (Reg. §1.199A-5(b)(2)(x) is explicit on this.)

### 10. Investing and Investment Management

Includes: managing investments for others (for fees, commissions, or carried interest).

### 11. Trading and Dealing

Includes: trading or dealing in securities, partnership interests, or commodities.

**Trader vs. investor:** A "trader in securities" (active trader, marks to market under §475) is SSTB. A passive investor reporting capital gains/losses is not engaged in a trade or business at all (so no QBI).

### 12. The "Reputation or Skill" Provision (§199A(d)(2)(A)(ii))

Any trade or business where the principal asset is the reputation or skill of one or more employees or owners. Per Treas. Reg. §1.199A-5(b)(2)(xiv), this is narrowly defined to:

- Endorsement income (athletes, celebrities)
- Licensing of an individual's name or image (e.g., a restaurant licensed under a celebrity chef's name)
- Appearance fees and media income tied to personal celebrity

This does NOT cover ordinary skilled professionals (e.g., a custom furniture maker, an auto mechanic, a farmer) — being skilled at your job doesn't trigger this provision. It's specifically targeted at endorsements and personal-fame monetization.

---

## Critical exclusions (NOT SSTBs, even when intuitively similar)

- **Architecture and engineering** — IRC §199A(d)(2)(A) explicitly carves these out. Architects, structural engineers, civil engineers, MEP engineers, all non-SSTB.
- **Real estate brokerage and insurance brokerage** — Reg. §1.199A-5(b)(2)(x) — only securities brokerage is SSTB.
- **Software development** — Programming and IT integration are not a listed field and are services other than advice and counsel (Reg. §1.199A-5(b)(2)(vii)); confirm how the work is billed.
- **Manufacturing, retail, e-commerce, wholesale, distribution** — Not SSTB regardless of products sold.
- **Banking and lending** — Not financial services SSTB (those are about advisory, not depository institutions).

---

## Decision tree

```
Is the business in one of the 11 listed categories?
├── No → not SSTB; proceed without Schedule A
└── Yes → continue

Does it fall into a specific carve-out (architecture, engineering, real estate brokerage, etc.)?
├── Yes → not SSTB
└── No → continue

Does it qualify for the "incidental to" / de minimis exception?
├── Yes → not SSTB
└── No → SSTB

For SSTBs:
  At or below threshold ($197,300 / $394,600 MFJ in 2025)?
  ├── Yes → SSTB treated as a qualified trade or business; Form 8995 unless a co-op patron
  └── No → continue
  
  In phase-in range (within $50,000 / $100,000 MFJ above the threshold in 2025; $75,000 / $150,000 in 2026)?
  ├── Yes → Schedule A applies; partial deduction
  └── No → above phase-in top; SSTB's QBI, W-2 wages, UBIA not taken into account
```

---

## Practical tips for the agent

1. **Always ask the user to confirm SSTB status for borderline cases.** Don't silently classify a "consultant" as SSTB without confirming the nature of services.

2. **For S-corp software developers** who call themselves consultants: software development is not a listed field, and building software is not advice and counsel. Generally non-SSTB; confirm the deliverable and billing.

3. **For real estate brokers**: real estate brokerage is excluded; not SSTB.

4. **For multi-line businesses**: if SSTB activities and non-SSTB activities are conducted in the same trade or business, the de minimis rule (less than 10% of gross receipts if gross receipts are $25 million or less; less than 5% above $25 million) may keep the whole business out of SSTB status. Otherwise the business is an SSTB.

5. **For financial planners** who also sell insurance: financial advisory is SSTB; insurance brokerage is not. If the same entity does both, apply the de minimis rule.

6. **The "reputation or skill" provision is narrow.** Don't apply it to ordinary skilled professionals. A talented carpenter is not "reputation or skill" SSTB; a celebrity chef who licenses their name is.

7. **When in doubt, document the classification rationale** in the deliverable so the user (or their CPA) can challenge it later.
