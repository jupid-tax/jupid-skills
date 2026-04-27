# Jupid Skills

Open-source agent skills for filing US accounting and tax forms. Built for Claude Code, the Anthropic Agent SDK, and other agent runtimes that load skill packages.

## What is a skill here?

Each skill is a self-contained walkthrough for one IRS form or one accounting task. A skill teaches an AI agent how to:

1. **Know when to engage** — clear trigger phrases and qualifiers
2. **Gather the right inputs** — what data the agent needs from the user before it can produce anything correct
3. **Apply the rules** — line-by-line procedure, edge cases, official IRS guidance
4. **Validate the output** — sanity checks, common-mistake guardrails, audit-ready documentation
5. **Cite sources** — every number, every rule, traceable to an IRS form, publication, or IRC section

These are not LLM prompts. They are operating manuals.

## Skills available

| Skill | Form | Audience | Status |
|-------|------|----------|--------|
| [schedule-c](./schedule-c/) | Schedule C (Form 1040) | Sole proprietors, single-member LLCs, freelancers, gig workers | ✓ Stable |

More skills are tracked in the [roadmap](./ROADMAP.md) and prioritized by search-volume + audience-fit research.

## Using a skill

### With Claude Code

```bash
# Install as a plugin (once we publish)
claude install github.com/jupid-tax/jupid-skills

# Or copy a single skill directly
mkdir -p ~/.claude/skills
cp -r jupid-skills/schedule-c ~/.claude/skills/
```

Then in any Claude Code session:

```
> Help me fill out Schedule C for my freelance business
```

Claude will detect the trigger and invoke the skill.

### With the Anthropic Agent SDK

Load the skill's `SKILL.md` into your system prompt. The skill's frontmatter (`name`, `description`) tells your agent when to engage; the body teaches it how.

```python
from anthropic import Anthropic
from pathlib import Path

skill = Path("jupid-skills/schedule-c/SKILL.md").read_text()
references = {
    p.stem: p.read_text()
    for p in Path("jupid-skills/schedule-c/references").glob("*.md")
}
# Pass `skill` as the operating instruction; pull from `references` on demand.
```

### With other agent runtimes

Each skill is plain markdown with optional reference and example folders. Any runtime that supports tool / file context can use them.

## Authoring a new skill

See [CONTRIBUTING.md](./CONTRIBUTING.md). Short version:

1. Pick a form from the [roadmap](./ROADMAP.md) (or open an issue to propose one)
2. Copy the structure of an existing skill into a new `<skill-name>/` directory
3. Fill in `SKILL.md`, `references/`, and at least two `examples/`
4. Open a PR — every skill is reviewed for accuracy against the cited IRS sources

## Quality standards

Every skill in this repo is held to four rules:

1. **Cite every number.** No invented thresholds, rates, or limits. Every value links to an IRS form, publication, IRC section, or Revenue Procedure.
2. **Year-aware.** State the tax year clearly. Numbers that change annually (mileage rate, Section 179 limit, SS wage base) are flagged as "year-dependent" with a pointer to the canonical IRS page.
3. **Edge-case honest.** When a rule depends on facts the agent doesn't have, say so out loud and ask the user — don't guess.
4. **Audit-grade output.** The agent's deliverable should be something a CPA could read without having to re-derive the math.

## Why this exists

Tax filing is procedural knowledge: a form, a set of rules, edge cases. Generic LLMs answer Schedule C questions with reasonable surface-level summaries that miss the lines, the limits, and the gotchas. Skills bridge that gap by encoding the *exact procedure* a human professional would follow.

Jupid uses these skills internally for our [AI accountant](https://app.jupid.com). We're publishing them because the same procedural rigor is useful to anyone building agents in this space.

## License

MIT — see [LICENSE](./LICENSE).

## Disclaimer

The skills in this repository encode procedural guidance based on publicly available IRS forms and publications. They are *not* tax advice. They do not establish a CPA-client relationship. Tax law is complex and individual circumstances vary; always consult a licensed tax professional for advice specific to your situation.
