---
name: linkedin-post-analytics-coach
description: >
  Use this skill when the user wants to analyze a LinkedIn post, a LinkedIn
  single-post analytics export, or a lead-magnet post campaign and improve the
  next post. Triggers on phrases like "analyze my LinkedIn post", "post
  analytics", "benchmark this post", "what worked", "what did not work",
  "improve the next post", "people commented plus", "lead magnet post",
  "LinkedIn CTA", "make this post perform better", or requests to turn a
  LinkedIn analytics export into recommendations. The skill works in Codex,
  Claude Code, and any runtime that can load markdown skill folders.
workflow: LinkedIn post analytics coaching
audience: [founder, creator, accounting, tax, finance, b2b]
last_verified: 2026-06-11
---

# LinkedIn Post Analytics Coach

This skill helps an agent review a LinkedIn post and its analytics export,
explain performance in plain language, and coach the user toward a better next
post. It is designed for B2B founder-led posts, especially lead magnets where
the desired action is a comment, DM, follow, save, repost, or click.

The agent must not just summarize numbers. It should diagnose the post as a
funnel:

```text
Hook -> audience fit -> engagement -> profile action -> follow / DM / click -> next post improvement
```

---

## Use from GitHub

Canonical public link:

```text
https://github.com/jupid-tax/jupid-skills/tree/main/workflows/linkedin-post-analytics-coach
```

When a user gives this GitHub link and asks to use or install the skill, first
determine the current runtime:

- If you are running in Codex, treat this as a Codex skill.
- If you are running in Claude Code, treat this as a Claude Code skill.
- If the runtime is unclear, ask one short question: "Are you using Codex or
  Claude Code?"

Do not make the user choose a different GitHub link. The same repository folder
is the source for both runtimes.

For one-off use without installation, read this `SKILL.md`, then load
`references/` or `examples/` only when needed for the user's task.

For repeated local use:

```bash
# Codex
mkdir -p ~/.codex/skills
cp -r workflows/linkedin-post-analytics-coach ~/.codex/skills/

# Claude Code
mkdir -p ~/.claude/skills
cp -r workflows/linkedin-post-analytics-coach ~/.claude/skills/
```

---

## Core rule

Separate evidence from interpretation.

Evidence can come from:

- LinkedIn analytics export rows and fields;
- the public LinkedIn post text, image, comments, and visible engagement count;
- user-provided campaign context such as goal, audience, CTA, and DM results;
- current benchmark sources, when browsing is available.

Interpretation must be labeled as judgment. Do not claim benchmark superiority
or failure without naming the denominator and source.

---

## Required inputs

Ask for the missing items before giving final recommendations:

1. LinkedIn post URL or pasted post text.
2. Analytics export, screenshot, or typed metrics.
3. Goal of the post:
   - comments / "plus" replies;
   - DMs;
   - repo or website clicks;
   - follower growth;
   - saves;
   - reposts;
   - authority building.
4. Target audience:
   - accountants, tax professionals, CFOs, founders, finance teams, etc.
5. What the user plans to post next, if known.

If the user only has the post URL and no export, review the visible public data
and ask for the export before making metric-heavy conclusions.

For the dialogue flow, load
[`references/dialogue-playbook.md`](./references/dialogue-playbook.md).

---

## Data mechanics

When a LinkedIn single-post analytics export is available, parse the source
data before writing conclusions. If repository files are available, use:

```bash
python3 workflows/linkedin-post-analytics-coach/scripts/analyze-linkedin-post-export.py path/to/export.xlsx
```

The script emits JSON with:

- post metadata;
- raw metrics;
- calculated rates;
- top demographics.

If the script is unavailable, compute the same rates manually. See
[`references/data-mechanics.md`](./references/data-mechanics.md).

Always name the denominator:

- engagement rate by impressions = social engagements / impressions;
- engagement rate by reach = social engagements / members reached;
- profile-view rate = profile viewers / impressions or reach;
- follower conversion from profile views = followers gained / profile viewers;
- comment share = comments / social engagements;
- save share = saves / social engagements.

---

## Benchmark hierarchy

Use benchmarks in this order:

1. The user's own historical posts with the same format and goal.
2. The user's own median across recent posts.
3. Current external LinkedIn benchmarks for similar post type, creator size,
   industry, and metric definition.
4. Generic creator heuristics only when no better benchmark exists.

If using external benchmarks, cite the source and state the benchmark's
denominator. Do not compare a post-level personal profile export to a company
page benchmark without caveat.

If browsing is not available, say that benchmark comparison is directional and
ask for historical exports.

---

## Workflow

Execute these steps in order.

### Step 1 - Clarify the job

Ask:

```text
What was the main goal of this post: comments, DMs, followers, clicks, saves, reposts, or authority?
```

If the user has already answered, do not ask again. Use the stated goal.

### Step 2 - Extract the post promise

From the post text, identify:

- hook;
- enemy or tension;
- promised mechanism;
- proof or story;
- CTA;
- asset being offered;
- risk claims that may need softer wording.

Do not rewrite the post yet. Diagnose first.

### Step 3 - Parse the analytics

Create a compact metric table:

```markdown
| Metric | Value | Rate / meaning |
| --- | ---: | --- |
| Impressions |  |  |
| Members reached |  |  |
| Social engagements |  |  |
| Reactions |  |  |
| Comments |  |  |
| Reposts |  |  |
| Saves |  |  |
| Profile viewers |  |  |
| Followers gained |  |  |
```

Then compute the rates listed in Data mechanics.

### Step 4 - Score the post

Use a four-part scorecard:

```markdown
| Dimension | Score | Evidence | Diagnosis |
| --- | ---: | --- | --- |
| Audience fit | /5 |  |  |
| Hook strength | /5 |  |  |
| Engagement quality | /5 |  |  |
| Conversion path | /5 |  |  |
```

Scoring must be tied to evidence. Example: strong audience fit can be supported
by viewer demographics; weak distribution can be supported by zero reposts.

### Step 5 - Explain what worked

Name 3-5 specific wins. Good examples:

- the post reached the target profession;
- comments are a high share of engagements;
- profile viewers converted into followers;
- saves show utility;
- the problem was concrete and painful.

### Step 6 - Explain what did not work

Name 3-5 specific weaknesses. Good examples:

- no reposts means low shareability;
- CTA asks for friction without making the asset concrete enough;
- no visible proof of the asset;
- hook creates conflict but may reduce trust;
- link or next step is not easy enough.

### Step 7 - Recommend the next post

Recommendations must be actionable:

- one hook revision;
- one CTA revision;
- one asset packaging change;
- one format recommendation;
- one measurement plan.

If the user wants copy, provide a short post draft and a first-comment draft.

### Step 8 - Provide a test plan

End with the next experiment:

```markdown
Next test:
- Format:
- Hook:
- CTA:
- Asset:
- Metric to beat:
- What would count as a win:
```

---

## Output format

Use this structure:

```markdown
## Verdict
[2-3 sentences. Was it successful for the stated goal?]

## Numbers
| Metric | Value | Interpretation |
| --- | ---: | --- |

## What Worked
- [Evidence-backed point.]

## What Did Not Work
- [Evidence-backed point.]

## Recommendations
- [Actionable next change.]

## Next Test
- [Specific experiment and metric.]
```

Keep the tone direct and friendly. The user should understand exactly what to
do next.

---

## Examples

- [`examples/review-request.md`](./examples/review-request.md) - pasteable
  request for Codex or Claude Code.
- [`examples/example-output.md`](./examples/example-output.md) - compact review
  format.

