# Contributing to Jupid Skills

Thanks for your interest. This repo is a slow, deliberate project — we ship few skills, but every skill we ship has to be right. Here's how to add or improve one.

## Before you start

1. Open an issue describing the form or task and the audience it serves
2. Wait for a maintainer to confirm scope before writing — it's easy to spend a weekend writing a skill that overlaps with one already in flight
3. Read at least two existing skills (`schedule-c/` is the reference implementation) so your skill matches the house style

## Skill structure

```
<skill-name>/
  SKILL.md                # Required. Frontmatter + workflow.
  references/             # Required. Lookup material the skill loads on demand.
    *.md
  examples/               # Required. At least 2 worked examples.
    *.md
  scripts/                # Optional. Helper scripts for deterministic computation.
    *.py
```

### `SKILL.md`

Required frontmatter fields:

```yaml
---
name: <skill-name>                    # Match the directory name
description: >
  Use this skill when … <triggers and qualifiers>.
form: <IRS form number>               # e.g. "Schedule C (Form 1040)"
audience: [solo, freelance, llc1, scorp, …]   # Match jupid-tax/OS audience tags
tax_year: 2026
last_verified: YYYY-MM-DD             # When the cited rates / limits were last checked
---
```

The body should follow this section order (we copy from `schedule-c/SKILL.md`):

1. **When to invoke** — trigger phrases and qualifiers, plus what makes the skill *not* applicable
2. **Prerequisites** — exactly what data the agent needs from the user before it can produce anything correct. State what to ask for if missing.
3. **Workflow** — numbered steps. Each step is a discrete action the agent takes.
4. **Line-by-line / field-by-field guidance** — the real meat. What each line means, what goes there, what edge cases trigger a different path.
5. **Validation** — sanity checks the agent runs before declaring the form ready.
6. **Output format** — the deliverable the agent produces (a filled draft, a checklist, a CSV, etc.).
7. **References** — links into the `references/` folder for deep material.
8. **Sources** — IRS forms, publications, IRC sections, Revenue Procedures, with URLs and revision dates.

### `references/`

Each reference is a focused topic the skill loads on demand. Examples:

- `naics-codes.md` — common business codes for the form
- `line-by-line.md` — quick lookup table
- `common-mistakes.md` — the 10 most frequent filer errors with examples
- `<rule-area>.md` — deep dive on a single sub-topic (home office, mileage, COGS, etc.)

References should be self-contained. The agent might load just one of them without the rest of the skill, so don't write "see above" — repeat the context.

### `examples/`

At least two end-to-end worked examples, each with:

- A persona (Maya the freelance designer, Carlos the rideshare driver, etc.)
- Their actual numbers (income, expenses, deductions)
- The completed form, line by line
- The "why" behind each non-obvious choice

Examples should look real. Round numbers are fine, but the *pattern* of inputs should match what a real filer would have.

## Quality bar (non-negotiable)

A skill ships only when:

- [ ] Every monetary value cites a source (IRS form, publication, IRC § or Rev. Proc.)
- [ ] Every annual number (mileage rate, contribution limit, threshold) is flagged as year-dependent and points to the canonical IRS page
- [ ] The skill explicitly handles "user has incomplete information" — what to ask for, what to flag, what to refuse
- [ ] At least two examples are end-to-end consistent (start with inputs, end with a filled form)
- [ ] The filled-form output matches the actual line numbering and ordering of the IRS form for the stated tax year
- [ ] A reviewer with a CPA license has read it (we'll arrange this for first-time contributors)

## What we won't merge

- Skills that hallucinate IRS rules or invent thresholds
- Skills that bundle tax advice ("you should incorporate as an S-corp because…")
- Skills that omit edge cases to look simpler than reality
- Skills that fail on the audit-grade test: "could a CPA reading this output trust the math without re-deriving it?"

## Style

- Write for an agent reading the skill, not a human reading a blog post
- Imperative voice ("Read the user's transactions"), not descriptive ("The skill reads transactions")
- Inline links to `references/` and `examples/` rather than long quoted blocks
- Code fences for any structured input the agent should produce (CSV, table, JSON)
- No marketing language. No "premium", "comprehensive", "best-in-class". The agent doesn't care.

## License

By contributing, you agree your contribution is licensed under the MIT License (see [LICENSE](./LICENSE)).
