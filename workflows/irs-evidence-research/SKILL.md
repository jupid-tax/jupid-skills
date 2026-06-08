---
name: irs-evidence-research
description: >
  Use this skill when the user asks an agent to research a US federal tax rule,
  IRS filing requirement, deadline, threshold, penalty, form instruction, or
  tax-code question and wants citation-gated output from official sources.
  Triggers on phrases like "research IRS rule", "what does the IRS say",
  "cite the authority", "tax code research", "IRS-only answer",
  "hallucination-free tax research", "find the official source", or any tax
  research request where unsupported inference would be risky. Do NOT use this
  skill to prepare a return, fill a form line by line, or give personalized tax
  advice when a narrower form skill applies.
workflow: IRS evidence research
audience: [tax, accounting, research, compliance]
tax_year: variable
last_verified: 2026-06-08
official_sources:
  - https://www.irs.gov/
  - https://uscode.house.gov/
  - https://www.ecfr.gov/
---

# IRS Evidence Research

This skill turns an AI agent into a citation-gated tax research assistant. It
does not reward clever inference. It rewards finding the controlling official
text, quoting only what is needed, and refusing to answer when the located
authority does not support the claim.

Use this workflow before any form-specific skill when the legal rule is unclear,
when a user asks for authority, or when a proposed tax position depends on a
threshold, deadline, definition, exception, penalty, or filing trigger.

---

## Core rule

Every material claim must be supported by official authority or labeled
`not determined`.

Do not present a tax rule, threshold, deadline, exception, entity relationship,
filing obligation, penalty, or tax position as true unless the answer includes:

- the source type: IRC, Treasury Regulation, IRS form instruction, IRS
  publication, IRS notice, revenue procedure, revenue ruling, official IRS page,
  Tax Court / court authority when specifically requested, or state authority if
  the user explicitly asks for state tax;
- a URL or file path;
- a pinpoint reference such as section, subsection, page, line, worksheet,
  table, question number, form line, or instruction heading;
- the tax year or effective date when the rule is year-dependent.

If the source text does not answer the question, say so. Do not bridge the gap
with general tax knowledge.

---

## When to invoke

Engage this skill when any of the following is true:

- The user asks what the IRS, IRC, Treasury Regulations, or official
  instructions say.
- The user wants citations, authority, audit support, or a "source of truth".
- The answer depends on a number that changes by year: standard deduction,
  mileage rate, Social Security wage base, Section 179 limit, retirement plan
  limits, penalty rates, interest rates, or filing thresholds.
- The answer depends on a legal trigger: residency, filing status, entity
  classification, foreign ownership, related-party transactions, trade or
  business, reportable transaction, material participation, or reasonable cause.
- The user asks for a reusable prompt or workflow to reduce hallucinations in
  tax research.

Do not engage this skill when:

- A form-specific skill can directly fill or draft a form from known facts.
  Use that form skill, and use this workflow only for unresolved legal authority.
- The user asks for financial planning, bookkeeping cleanup, or client intake
  without a tax-law research question.
- The user wants a final professional opinion. Produce research support and
  identify open issues; do not claim to replace a CPA, EA, or attorney.

---

## Source hierarchy

Prefer sources in this order:

1. IRC sections from `uscode.house.gov` or another official code source.
2. Treasury Regulations from `ecfr.gov`.
3. IRS form instructions for the exact form and tax year.
4. IRS publications, notices, revenue procedures, revenue rulings, FAQs, and
   official IRS topic pages.
5. Court authority only when the user asks for case law or when primary IRS
   sources leave a dispute unresolved.

Never use blogs, forums, AI summaries, software help centers, or generated
notes as authority. They can be leads only. If a non-official source points to a
rule, follow it to the official authority and cite the official authority.

For the full source policy, load
[`references/source-policy.md`](./references/source-policy.md).

---

## Workflow

Execute these steps in order.

### Step 1 - Restate the research question

Convert the user's request into a narrow research question.

Include:

- taxpayer type: individual, sole proprietor, partnership, corporation, S corp,
  disregarded entity, foreign owner, employer, payor, recipient, etc.;
- tax year or filing year;
- form or filing obligation involved;
- jurisdiction: federal unless the user asks for a state;
- the exact issue to prove.

If any of these are missing and they materially affect the answer, ask before
researching. Do not assume the year.

### Step 2 - Search official sources first

Search only official sources unless the user explicitly asks for a broader
landscape scan.

Useful starting points:

- `site:irs.gov [form number] instructions [tax year]`
- `site:irs.gov [topic] irs`
- `site:uscode.house.gov [IRC section or phrase]`
- `site:ecfr.gov [Treasury regulation section or phrase]`
- `site:irs.gov revenue procedure [tax year] [threshold]`

When browsing is unavailable, ask the user to provide source documents or state
that live verification is unavailable. Do not rely on memory for current-year
amounts.

### Step 3 - Extract authority

For each relevant source, capture:

```text
Source:
Authority type:
URL or file path:
Tax year/effective date:
Pinpoint:
Short excerpt:
How it answers the question:
Limits / ambiguity:
```

Keep excerpts short. Paraphrase the rule in your own words after the citation.

### Step 4 - Test the claim

Before writing the answer, check each material claim:

- Is this claim directly supported by a cited source?
- Does the source apply to the user's tax year?
- Does another official source limit or contradict it?
- Is a key fact missing?
- Is this actually tax advice rather than research support?

If support is missing, downgrade the statement to `not determined` or ask a
question.

### Step 5 - Answer in citation-gated format

Use this output structure:

```markdown
## Short Answer
[One direct answer. If not supported, say "Not determined from the located official sources."]

## Authorities
| Point | Source | Pinpoint | What it supports |
| --- | --- | --- | --- |

## Analysis
- [Claim.] Source: [official URL], [pinpoint].
- [Claim.] Source: [official URL], [pinpoint].

## Not Determined / Open Facts
- [Missing fact or unsupported issue.]

## Practical Next Step
[One conservative next step, such as collecting a document, checking a form instruction for the exact year, or asking a CPA/EA to confirm.]
```

For detailed output patterns, load
[`references/output-formats.md`](./references/output-formats.md).

### Step 6 - Run the evidence review

Before returning the answer, run this checklist:

- Every material claim has an official source.
- Every annually changing number has a tax year and current official source.
- Every citation has a pinpoint reference.
- No blog, forum, software article, or AI summary is treated as authority.
- Unanswered issues are labeled `not determined`.
- The answer distinguishes research support from personalized tax advice.

If you have access to the repository files, run:

```bash
python3 workflows/irs-evidence-research/scripts/validate-citations.py path/to/answer.md
```

The script is a guardrail, not a substitute for judgment.

---

## Refusal rule

Refuse or narrow the answer when the user asks for:

- a conclusion without source support;
- a current-year threshold without live official verification;
- a personalized tax position based on incomplete facts;
- a claim that contradicts located official authority;
- use of unofficial sources as the final authority.

Use this wording:

```text
I cannot support that conclusion from the official sources located. The closest authority found is [source], which supports [narrower point]. The remaining issue is not determined from the current evidence.
```

---

## Examples

Load only the example that matches the task:

- [`examples/supported-answer.md`](./examples/supported-answer.md) - official
  source supports the answer.
- [`examples/insufficient-source-refusal.md`](./examples/insufficient-source-refusal.md)
  - source does not support the requested conclusion.
- [`examples/research-request.md`](./examples/research-request.md) - reusable
  prompt for invoking the workflow in Codex, Claude Code, or another agent.

