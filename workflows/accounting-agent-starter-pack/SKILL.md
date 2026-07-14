---
name: accounting-agent-starter-pack
description: >
  Use this skill when an accounting firm owner, CPA, EA, tax preparer,
  bookkeeper, CAS manager, or controller wants a small set of read-only agents
  and prompts for document triage, client document requests, cleanup review,
  month-end close completeness, or a skeptical second-pass review. Triggers on
  phrases like "which accounting agent should I use", "client is missing tax
  documents", "draft a client document request", "review this cleanup", "check
  this close package", or "run a tired reviewer pass". Do not use it to send
  messages, post entries, approve books, make final tax decisions, or replace
  licensed professional review.
workflow: Accounting agent starter pack
audience: [accounting, bookkeeping, tax, CPA, EA, CAS, controller]
last_verified: 2026-07-14
---

# Accounting Agent Starter Pack

This public pack contains five small, read-only accounting agents and three
client-chasing prompts. Use only the component that matches the current job.

## Public link

```text
https://github.com/jupid-tax/jupid-skills/tree/main/workflows/accounting-agent-starter-pack
```

The same link works as a one-off instruction source for Codex or Claude Code.

## Choose the right component

| Need | Component | What it must not do |
|---|---|---|
| Compare an expected checklist with received files | `agents/document-triage.md` | Decide tax treatment or declare a file complete |
| Turn an approved gap list into a client request | `agents/client-request-writer.md` | Determine what is missing or send the message |
| Review cleanup work for anomalies and missing support | `agents/cleanup-reviewer.md` | Edit, recategorize, reconcile, or approve books |
| Check a close package before manager review | `agents/month-end-close-checker.md` | Post entries or approve/certify the close |
| Run a skeptical omission and contradiction pass | `agents/tired-reviewer.md` | Replace professional review or sign-off |
| Create a gap list, client request, and follow-up schedule | `prompts/three-client-chasing-prompts.md` | Automate tax judgment or send/schedule messages |

## One-off use from GitHub

Paste this into Codex or Claude Code:

```text
Use this public accounting workflow pack:
https://github.com/jupid-tax/jupid-skills/tree/main/workflows/accounting-agent-starter-pack

First read SKILL.md. Choose only the agent or prompt that matches my task.
Keep all work read-only and draft-only. Ask for missing firm rules instead of
guessing, and require human review before anything is sent or posted.

My task:
[describe the client file, cleanup, close package, or review need]
```

For the three client-chasing prompts specifically:

```text
Open:
https://github.com/jupid-tax/jupid-skills/blob/main/workflows/accounting-agent-starter-pack/prompts/three-client-chasing-prompts.md

Run Prompt 1 first using my real checklist and a redacted file inventory.
Stop for preparer review before Prompt 2. Draft only; do not send anything.
```

## Install for repeated use

Clone or download the repository, then copy the workflow folder:

```bash
# Codex
mkdir -p ~/.codex/skills
cp -r workflows/accounting-agent-starter-pack ~/.codex/skills/

# Claude Code
mkdir -p ~/.claude/skills
cp -r workflows/accounting-agent-starter-pack ~/.claude/skills/
```

Claude Code users can also copy individual files from `agents/` into the
project's `.claude/agents/` directory. Each file has Claude Code agent
frontmatter and a constrained system prompt.

## Safe first run

1. Start with synthetic or redacted client data.
2. Supply the firm's actual checklist, deadlines, escalation rules, and secure
   upload method.
3. Review every gap, conclusion, and draft before using it with a client or in
   the books.
4. Do not upload unredacted client information to an unapproved model or
   environment.
5. Never treat a completeness label as accounting or tax approval.

## Files

- [Document triage agent](./agents/document-triage.md)
- [Client request writer agent](./agents/client-request-writer.md)
- [Cleanup reviewer agent](./agents/cleanup-reviewer.md)
- [Month-end close checker agent](./agents/month-end-close-checker.md)
- [Tired reviewer agent](./agents/tired-reviewer.md)
- [Three client-chasing prompts](./prompts/three-client-chasing-prompts.md)
- [Validation and known limits](./references/validation.md)

## Release boundary

This repository does not automate LinkedIn connections, messages, email,
client-portal requests, bookkeeping entries, or approvals. Human review remains
mandatory before any external communication or accounting action.
