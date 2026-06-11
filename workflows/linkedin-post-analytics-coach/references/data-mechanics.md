# Data Mechanics

Use these mechanics when analyzing LinkedIn single-post analytics.

## Inputs

Common LinkedIn export fields:

- Post URL
- Post Date
- Post Publish Time
- Impressions
- Members reached
- Profile viewers from this post
- Followers gained from this post
- Social engagements
- Reactions
- Comments
- Reposts
- Saves
- Sends on LinkedIn
- Link engagements
- Premium custom button engagements
- Viewer demographics by job title, location, seniority, company, industry,
  and company size

## Core formulas

```text
Engagement rate by impressions = Social engagements / Impressions
Engagement rate by reach = Social engagements / Members reached
Comment rate = Comments / Impressions
Reaction rate = Reactions / Impressions
Save rate = Saves / Impressions
Profile-view rate by impressions = Profile viewers / Impressions
Profile-view rate by reach = Profile viewers / Members reached
Follower conversion from profile views = Followers gained / Profile viewers
Comment share = Comments / Social engagements
Reaction share = Reactions / Social engagements
Save share = Saves / Social engagements
Impressions per reached member = Impressions / Members reached
```

Always name the denominator. Do not say "engagement rate" without saying
whether it is by impressions, reach, followers, or another base.

## Interpretation guide

Use these as diagnostic signals, not fixed universal rules:

- High comments with low reposts: strong conversation, weak shareability.
- High saves with low comments: useful asset, less controversial.
- High profile views with low follows: profile or offer mismatch.
- High followers from profile views: strong personal trust once people click.
- High industry/audience match: the post reached the right people even if the
  overall engagement rate is modest.
- Zero link engagements: the post did not create a measurable click path, or
  the link was not present / not attractive / not tracked.

## Benchmarking

Benchmark in this order:

1. User's own historical posts with the same post type and goal.
2. User's recent median.
3. Current public benchmarks with the same denominator.
4. Directional heuristics only if no better source exists.

External LinkedIn benchmarks vary heavily by source, profile size, post format,
industry, and denominator. Treat them as context, not as the source of truth.

## Common analytics mistakes

- Comparing personal profile post metrics to company page benchmarks without a
  caveat.
- Comparing impression-based rates to follower-based rates.
- Treating reactions as the main success signal when the goal was comments,
  DMs, or leads.
- Ignoring audience fit. A smaller post reaching the exact buyer can be more
  valuable than a broad post reaching the wrong audience.
- Over-optimizing the hook while ignoring the CTA and asset.

