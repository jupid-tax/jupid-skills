# 3 Prompts To Stop Chasing Clients For Missing Tax Documents

Use these prompts when a client has uploaded some documents, but the file is not ready for preparation or review.

The goal is not to automate tax judgment. The workflow turns a messy file into:

1. a clear gap list;
2. a client-ready request;
3. a follow-up schedule.

## Prompt 1: File Gap Review

Purpose: turn a partial client file into a prioritized missing-document list.

```text
You are a senior tax workflow coordinator reviewing a client file before preparation begins.

Your task is to identify what is complete, what is missing, what is unclear, and what should be escalated to a preparer or reviewer.

Context:
- Tax year: [YEAR]
- Client type: [INDIVIDUAL / SOLE PROPRIETOR / S-CORP OWNER / OTHER]
- Filing deadline: [DATE]
- Firm cutoff date for on-time filing: [DATE]
- Client status: [NEW / RETURNING]
- Preparation stage: [INTAKE / PREP QUEUE / IN PREPARATION / REVIEW]
- Firm rule: Do not ask for documents by email if they contain sensitive tax data. Ask the client to upload them to the portal.

Expected document checklist:
[PASTE CHECKLIST]

Documents already received:
[PASTE FILE LIST OR ORGANIZER SUMMARY]

Known client notes:
[PASTE NOTES]

Output format:
1. Ready to proceed: items that appear complete.
2. Missing and required: items blocking preparation.
3. Unclear: items that may be needed but require confirmation.
4. Reviewer questions: anything that needs professional judgment.
5. Client request draft bullets: short numbered bullets I can reuse in a client email.

Rules:
- Do not invent documents.
- Do not give final tax advice.
- If something is uncertain, mark it as uncertain.
- Keep the client request specific and short.
```

## Prompt 2: Client Request Writer

Purpose: convert an approved gap list into a message the client can answer quickly.

```text
You are writing on behalf of an accounting firm to a tax client.

Use the approved gap list below to write a short, professional, friendly message requesting only the items needed to keep the return moving.

Client context:
- Client name: [CLIENT NAME]
- Tax year: [YEAR]
- Deadline or target completion date: [DATE]
- Upload method: [PORTAL / SECURE LINK / OTHER]
- Tone: clear, calm, specific, and not blameful.

Approved gap list:
[PASTE REVIEWED OUTPUT FROM PROMPT 1]

Write:
1. Subject line.
2. Email body.
3. Optional SMS version under 320 characters.

Rules:
- Start by acknowledging what was received.
- Ask for missing items in a numbered list.
- Explain why each item is needed in plain English.
- Do not use jargon unless necessary.
- Do not say "ASAP." Use a concrete date.
- Do not ask for sensitive documents by regular email.
- End with one clear next step.
- Draft only. Do not send anything.
```

## Prompt 3: Follow-Up Schedule

Purpose: decide when to remind, escalate, or move the return to extension risk.

```text
You are helping an accounting firm manage tax-season follow-up.

Create a follow-up schedule for a client who has missing tax documents.

Context:
- Client name: [CLIENT NAME]
- Tax year: [YEAR]
- Filing deadline: [DATE]
- Firm cutoff date for on-time filing: [DATE]
- Date first request will be sent: [DATE]
- Missing items:
[PASTE FINAL REVIEWED MISSING-ITEM LIST]
- Firm escalation rule:
[PASTE RULES, E.G. PREPARER ESCALATION AFTER 7 DAYS, EXTENSION DISCUSSION AFTER CUTOFF]

Output format:
1. Follow-up timeline table with date, channel, owner, message goal, and escalation trigger.
2. Reminder message 1.
3. Reminder message 2.
4. Extension-risk message if the client misses the cutoff.
5. Internal note for the preparer or admin team.

Rules:
- Keep reminders respectful and specific.
- Do not over-message the client.
- Do not promise on-time filing after the firm cutoff date.
- Flag any item that should be reviewed by a tax professional.
- Draft only. Do not schedule or send anything.
```

## Recommended workflow

1. Run Prompt 1 with the firm's real checklist and the file inventory.
2. Have a preparer review the gap list.
3. Run Prompt 2 only with the approved gap list.
4. Run Prompt 3 with the final missing-item list and the firm's real escalation rules.
5. Have a human approve every message before sending.
