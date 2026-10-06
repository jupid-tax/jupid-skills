# When Not to File Form 1040-X (and What to Do Instead)

Run this table before preparing any amendment. Every row cites the IRS source it comes from; re-check the page date before relying on it. If a row applies, tell the user which one, what to do instead, and stop or redirect.

---

## Decision table

| # | Situation | Do this instead of (or before) Form 1040-X | Source |
|---|---|---|---|
| 1 | The IRS notified the user that it corrected a math or clerical error on the return | Nothing to amend. Review the IRS notice; respond to it if the user disagrees, following the notice's instructions | irs.gov [File an amended return](https://www.irs.gov/filing/file-an-amended-return) (reviewed 30-Sep-2026): "You don't need to amend your return if we: Let you know that we corrected errors on your return." Topic 308 (reviewed 24-Sep-2026): "The IRS may correct certain errors on a return ... there's no need to amend" |
| 2 | A form or schedule was left off, and the IRS accepted the return without it or asked for it | Send what the IRS letter requests; no amendment, unless the missing form changes the numbers (then go to row 13) | Same two sources: "Accept your return without certain forms or schedules or ask you to send them" |
| 3 | The original e-file was **rejected** | It was never filed. Correct it and retransmit, or file on paper. Form 1040-X is filed "only after you have filed your original return" | Instructions for Form 1040-X, When To File. IRM 3.42.5.14.6 (reviewed 30-Apr-2026): a timely return rejected in e-file can be retransmitted within the perfection period (for tax year 2025, the last day was April 20, 2026 for returns due April 15, 2026, and October 20, 2026 for returns on a Form 4868 extension); if it cannot be perfected, a paper return is timely if filed by the later of the due date or 10 calendar days after the IRS rejection notice, with an explanation |
| 4 | The original was filed but not yet processed, and the user expects a **larger refund** | Wait for the original refund, then file Form 1040-X. Waiting does not extend the §6511 claim deadline (see [`refund-statute.md`](./refund-statute.md)) | irs.gov [Amending a return (video script)](https://www.irs.gov/newsroom/amending-a-return-youtube-video-text-script) (reviewed 14-Sep-2026): "if you're filing for an additional refund, wait until you get your original refund before filing a 1040-X" |
| 5 | The user received a **CP2000** and agrees with it, with no other income, credits, or expenses to report | Follow the notice and return the response form. No amendment | irs.gov [Understanding your CP2000 notice](https://www.irs.gov/individuals/understanding-your-cp2000-notice) (reviewed 14-Jul-2026): "If you agree with the notice and don't have other income, credits, or expenses to report, follow the notice's instructions. You don't need to amend your return." |
| 6 | CP2000 is correct **and** the user has other changes to report | Complete Form 1040-X, write "CP2000" at the top, and submit it **with the notice response** through the notice's reply channel (upload, fax, or mail to the notice address) | Same page, "Amend your return". Mailing address: the address on the notice (Instructions for Form 1040-X, Where To File: "in response to a notice you received from the IRS → the address shown in the notice") |
| 7 | CP2000 for one year; the same error exists in other years | Amend the other years with Form 1040-X | Same page: "Check your tax returns from prior years. If they have the same issue, file an amended return." |
| 8 | The user wants back only **penalties, interest, or an addition to tax** already paid | Form 843 — [`../../form-843/SKILL.md`](../../form-843/SKILL.md) | Instructions for Form 1040-X, Purpose of Form |
| 9 | A joint refund was offset for the spouse's past-due debt, and the user wants their share | Form 8379 (Injured Spouse Allocation). It can be e-filed attached to a Form 1040-X even when nothing is amended | Instructions for Form 1040-X, Purpose of Form and What's New |
| 10 | The due date (without extensions) has **not** passed and the user owes more | A corrected Form 1040 or a Form 1040-X filed with payment by the due date **supersedes** the original and avoids penalties and interest on the extra tax | [Topic 308](https://www.irs.gov/taxtopics/tc308): "you can avoid penalties and interest if you file Form 1040-X or a corrected return (Form 1040) and pay the tax by the filing due date ... This return will replace or supersede the original return." |
| 11 | Loss or credit **carryback** (NOL, general business credit, section 1256 loss, claim of right) | Form 1045 is an alternative if filed within 1 year after the end of the loss/credit year; otherwise Form 1040-X marked "Carryback Claim" | Instructions for Form 1040-X, Loss or credit carryback |
| 12 | The user filed the original return and now wants to file "another original" because the refund is slow | Don't. After the due date, filing another original or a second copy can delay the refund | Instructions for Form 1040-X, When To File caution |
| 13 | Income, deductions, credits, filing status, dependents, or tax liability changed | **Amend** with Form 1040-X | irs.gov File an amended return, "Reasons to amend a return" |
| 14 | The change also affects the **state** return | Out of scope here. Tell the user to check with the state tax agency; never attach the state return to the federal amendment | irs.gov File an amended return, "State tax returns" |

---

## Quick tests for ambiguous cases

- **A corrected 1099 arrives.** Compare it to what was reported. If the reported number already matched the corrected amount, nothing changes (no amendment). If it differs, it is row 13.
- **A late 1099 arrives for income the user never reported.** Row 13. Amending before the IRS contacts the user is generally preferable; the accuracy-related penalty interaction (qualified amended return, Treas. Reg. §1.6664-2(c)(3)) is fact-specific, so refer that question to a CPA rather than promising penalty relief.
- **The user wants to change from married filing jointly to married filing separately.** Generally not allowed after the due date (Form 1040-X, filing status caution). Stop and explain.
- **The user filed Form 1040-NR but was a resident (or the reverse).** Amend with Form 1040-X and attach the correct return (Instructions for Form 1040-X, Resident and nonresident aliens).
- **The user wants to make or change an election after the deadline.** Form 1040-X can carry certain late elections under Regulations §§301.9100-1 through -3; this needs a CPA.

---

## What to tell the user in each "do not amend" case

State, in one or two sentences: which situation applies, the source, what to do instead, and any deadline that still runs (the §6511 claim period keeps running while the user waits for an original refund or a notice).
