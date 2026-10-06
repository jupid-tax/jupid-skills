# Entity Type and Reason for Applying (Form SS-4, Lines 8a to 10)

How to answer the LLC questions, choose the one line 9a box, fill line 9b, pick the one line 10 reason, and decide whether a new EIN is needed at all. Sources: Instructions for Form SS-4 (Rev. December 2025), "Lines 8a–8c", "Line 9a", "Disregarded entities", "Line 10"; Form SS-4 page 2 footnotes; IRS page [When to get a new EIN](https://www.irs.gov/businesses/small-businesses-self-employed/when-to-get-a-new-ein) (reviewed 21-Jul-2026); Instructions for Form 2553 (Rev. December 2020), "When To Make the Election".

Line 9a is not an election. "This isn't an election for a tax classification of an entity" (Instructions, Line 9a caution). The election happens on Form 8832 or Form 2553. Line 9a must describe the classification the entity will have, so settle the plan before drafting.

## Step A — Ask the classification questions

Ask, and stop until answered:

1. "Is the entity an LLC (or a foreign equivalent)?" → line 8a
2. "How many members?" → line 8b
3. "Was it organized under the law of a U.S. state?" → line 8c
4. "Will it keep its default federal classification, elect to be taxed as a corporation on Form 8832, or elect S corporation status on Form 2553?"
5. For a single-member LLC: "Is the owner a U.S. person or a foreign person? Why do you need the EIN: employees, excise tax, a state requirement, a bank, Form 5472, Form 8832, or Form 2553?"

The skill does not recommend a classification. If the user is undecided, say so and refer them to a tax adviser before applying, because the answer changes line 9a.

## Default classifications (for reference when answering Step A)

| Entity | Default | Source |
|---|---|---|
| Domestic LLC, one member | Disregarded as separate from its owner; income on the owner's return (e.g., Schedule C) | Instructions, Lines 8a–8c |
| Domestic LLC, two or more members | Partnership | Instructions, Lines 8a–8c |
| Foreign LLC, 2+ members, at least one without limited liability | Partnership | Instructions, Lines 8a–8c |
| Foreign LLC, all members with limited liability | Association taxable as a corporation | Instructions, Lines 8a–8c |
| Foreign LLC, single owner without limited liability | Disregarded | Instructions, Lines 8a–8c |
| LLC owned by spouses in a community property state that choose disregarded treatment | Disregarded; enter "1" on line 8b | Instructions, Lines 8a–8c |

"Don't file Form 8832 if the LLC accepts the default classifications above." An LLC that timely files Form 2553 is treated as a corporation from the S election's effective date if it otherwise qualifies, and does not also need Form 8832 (Instructions, Lines 8a–8c caution). Route to `../../form-8832/SKILL.md` and `../../form-2553/SKILL.md`.

## Step B — Line 9a decision table

| Facts | Line 9a box | Write-in | Source |
|---|---|---|---|
| Domestic single-member LLC staying disregarded; EIN for employment or excise taxes or a non-federal (state) requirement | Other | "Disregarded entity" | Instructions, Disregarded entities; Lines 8a–8c TIP |
| U.S. disregarded entity wholly owned by a foreign person; EIN to file Form 5472 | Other | "Foreign-owned U.S. disregarded entity-Form 5472" | Instructions, Disregarded entities |
| Single-member LLC that will file Form 8832 (corporation) or Form 2553 (S corporation) | Corporation | "Single-member" and "1120" or "1120-S" | Instructions, Disregarded entities |
| Domestic LLC, 2+ members, accepting partnership classification | Partnership | — | Instructions, Lines 8a–8c TIP |
| Domestic LLC (any member count) filing Form 8832 for corporate classification | Corporation | "1120" | Instructions, Lines 8a–8c |
| Domestic LLC (any member count) filing Form 2553 | Corporation | "1120-S" | Instructions, Lines 8a–8c |
| Disregarded entity that acquired more owners and became a partnership under Reg. 301.7701-3(f) | Partnership | — | Instructions, Disregarded entities |
| Foreign eligible entity filing Form 8832 to elect disregarded status | Other | "foreign disregarded entity" | Instructions, Disregarded entities |
| Qualified subchapter S subsidiary | Other | "QSub" | Instructions, Line 9a Other |
| State-law corporation (not personal service) | Corporation | Return form number | Instructions, Line 9a |
| Personal service corporation | Personal service corporation | — | Instructions, Line 9a |
| Nonprofit other than church | Other nonprofit organization | Type; GEN if any; "Section 527 organization" for political organizations | Instructions, Line 9a |
| Individual Schedule C/F filer with qualified plan or excise/employment/ATF returns or gambling payouts | Sole proprietor | SSN or ITIN | Instructions, Line 9a |
| Individual household employer | Other | "Household employer" and SSN | Instructions, Line 9a Other |
| Withholding agent filing Form 1042 | Other | "Withholding agent" | Instructions, Line 9a Other |

Contradictions to catch:

- 8b = 1 and box Partnership (unless the entity is reporting a past change to partnership, which needs a second member)
- 8b ≥ 2 and "Disregarded entity" (only the community-property spouses rule allows "1" with two owners)
- "Sole proprietor" for any LLC. The instructions route single-member LLCs to Other, Corporation, or Partnership depending on the facts; there is no instruction to check Sole proprietor for an LLC
- Corporation without a form number

### S election timing to state in the hand-off

The Form SS-4 instructions warn: if "1120-S" is entered, the corporation must file Form 2553 no later than the 15th day of the 3rd month of the tax year the election is to take effect, and until Form 2553 is received and approved it is considered a Form 1120 filer (Instructions, Line 9a caution). The Form 2553 instructions state the window as "No more than 2 months and 15 days after the beginning of the tax year the election is to take effect", with the 2-month period ending the day before the numerically corresponding day of the second following month (Instructions for Form 2553, "When To Make the Election"). Compute the exact date in `../../form-2553/SKILL.md`; do not compute it only from the SS-4.

An existing corporation electing or revoking S status uses its existing EIN (Form SS-4, page 2, footnote 9).

## Step C — Line 9b

Line 9b reads "If a corporation, name the state or foreign country (if applicable) where incorporated." The instructions contain no further text. When line 9a is Corporation, ask the user for the state or foreign country under whose law the entity was formed and enter it. For an LLC taxed as a corporation, flag the entry for review, because the LLC was "organized", not "incorporated".

## Step D — Line 10, one reason

| User's situation | Box | Specify |
|---|---|---|
| New business needing an EIN | Started new business | Type of business |
| Existing business without an EIN that now has employees | Hired employees | Complete line 13 |
| EIN needed only for a bank account (club, league) | Banking purpose | Banking purpose |
| Sole proprietorship incorporated or became a partnership | Changed type of organization | "From sole proprietorship to partnership" etc. |
| Bought an operating business | Purchased going business | — |
| Created a trust (non-grantor, or grantor trust that needs one) | Created a trust | Type of trust |
| New pension plan | Created a pension plan | Type; also 9a Other "Created a pension plan" |
| Foreign person needs an EIN for withholding documentation or treaty claims | Compliance with IRS withholding regulations | — |
| Foreign-owned U.S. disregarded entity needing an EIN for Form 5472 | Other | "Foreign-owned U.S. disregarded entity filing Form 5472" |
| Anything else | Other | The reason |

Do not apply if the business already has an EIN and is only adding a location ("Started new business") or only hiring ("Hired employees") (Instructions, Line 10). Hiring triggers electronic deposits through EFTPS (Instructions, Line 10 caution).

## When a new EIN is needed

From Form SS-4 page 2 footnotes and the IRS "When to get a new EIN" page:

| Entity | New EIN needed | No new EIN |
|---|---|---|
| Sole proprietor | Incorporate; form a partnership; declare bankruptcy | Change name or locations; own multiple businesses |
| Corporation | New charter from the secretary of state; becoming a subsidiary; changing to a partnership or sole proprietorship; merger creating a new corporation | Name or location change; bankruptcy; division of a corporation; surviving corporation after merger; electing S status; reorganizing only identity or location; converting at state level without changing business structure |
| Partnership | Incorporate; taken over by one partner as a sole proprietor; ending a partnership and starting a new one | Name or location change; bankruptcy; ownership change that does not terminate the partnership |
| LLC | Terminating an LLC and forming a new corporation or partnership; single-member LLC that must file excise or employment taxes | Name or location change; reporting income as a branch or division with no employees or excise tax; converting a partnership to an LLC classified as a partnership; changing the tax election to corporation or S corporation; using the sole proprietor EIN for a single-member LLC with no corporate election, no employees, no excise tax |
| Estate | Trust created with estate funds; estate operating a sole proprietorship after the owner's death | Change of administrator's name or address |
| Trust | Grantor of many trusts (generally one EIN each); change to an estate; living trust becomes testamentary; terminating a living trust into a residual trust; revocable becomes irrevocable | Change of trustee; change of grantor or beneficiary name or address |

Also from Form SS-4 page 2, footnote 2: do not apply for a new EIN if the existing entity only changed its business name, elected on Form 8832 to change how it is taxed (or is covered by the default rules), or terminated its partnership status because at least 50% of the total interests in partnership capital and profits were sold or exchanged within a 12-month period; the terminated partnership keeps its EIN (Regulations section 301.6109-1(d)(2)(iii)). Footnote 3: do not use a prior owner's EIN unless you became the owner of a corporation by acquiring its stock.
