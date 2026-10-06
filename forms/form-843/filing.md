# Submitting a Penalty or Interest Relief Request (Phone, Letter, or Form 843)

How an agent takes a completed relief decision from `SKILL.md` to the IRS. There is no e-file channel for a standalone Form 843 in the instructions: the routes are a phone call, a written statement, or a paper Form 843 mailed to the address the instructions specify. Pick the channel first, then follow its playbook.

Sources: Instructions for Form 843 (Rev. December 2024), "Where To File", "Who Can File", "Signature" (https://www.irs.gov/pub/irs-pdf/i843.pdf); IRS penalty relief pages (https://www.irs.gov/payments/penalty-relief, https://www.irs.gov/payments/penalty-relief-due-to-first-time-abate-or-other-administrative-waiver, https://www.irs.gov/payments/penalty-relief-for-reasonable-cause); IRS interest abatement page (https://www.irs.gov/payments/interest-abatement); IRS penalty appeal page (https://www.irs.gov/appeals/penalty-appeal); Publication 5 (Rev. 4-2021).

---

## Channel decision tree

```
Is the charge Form 843 material at all? (references/wrong-form-routing.md)
  No  → stop; route to the named form or skill
  Yes ↓

Is the return a 2025+ annual or 2026+ quarterly return of an AEP series, with a
clean 3-year history, and a penalty was assessed anyway?
  Yes → Channel A (phone the notice number); "contact us" per the IRS AEP section
  No  ↓

Does the user hold an IRS notice for this charge?
  Yes → Is the request FTA, or reasonable cause the user wants to try by phone?
          Yes → Channel A (phone). If the call cannot approve it → Channel C
          No  → Channel B (written statement) or Channel C (Form 843) to the notice address
  No  → Channel C (Form 843) to the service center for the current-year return of that tax

Is any part of the request a refund of money already paid, with a §6511 deadline
inside 30 days?
  Yes → Channel C by certified mail now (a written claim filed inside the period
        protects the refund; IRC §6511(b)(1)), even if a call is also made

Is it §6404(e) interest abatement?
  Yes → Channel C (Form 843) or a signed letter (IRS interest abatement page)

Did the user receive a denial (usually Letter 854C)?
  Yes → Channel D (appeal), not a new Form 843
```

---

## Channel A — Phone

The IRS: "Some penalty relief requests may be accepted over the phone. Call us at the toll-free number on your notice or letter" (penalty relief page). For FTA: "Call the IRS at the toll-free number found in the top right corner of your notice or letter."

### Pre-flight (the user makes the call; the agent prepares)

- The notice, with its number, date, and the penalty lines
- The penalty or penalties to be removed, by name and period
- The reason (FTA: "I'd like you to check whether I qualify for First Time Abate"; reasonable cause: dates and documents at hand)
- SSN or EIN, the return, and the prior-year return for identity checks
- A representative may call only with a Form 2848 on file covering the period

### Call script (for the user)

```
"I'm calling about notice <CP number> dated <date> for tax period <period>.
I'm asking for removal of the <failure-to-file / failure-to-pay / failure-to-deposit>
penalty of $<amount>. [FTA:] Please check whether I qualify for First Time Abate;
my returns for <years> were filed on time with no penalties.
[Reasonable cause:] On <date> <event> happened, which lasted until <date>, and I
<filed/paid> on <date>. I have <documents>."
```

Ask the representative for: the decision, whether the failure-to-pay penalty will keep accruing on any unpaid tax, and the letter that will confirm the outcome. The IRS reasonable cause page: if the phone agent cannot approve relief, request it in writing with Form 843.

Log the date, time, representative ID if given, and the outcome. Do not record the call without the user's consent and the representative's.

---

## Channel B — Written statement

Accepted by the IRS for FTA and reasonable cause ("Send a written statement or Form 843," IRS FTA page) and for §6404(e) interest ("a signed letter," IRS interest abatement page). Use the same content as Form 843 line 8, plus name, TIN, tax period, notice number, the penalty and amount, and a signature. Mail to the notice return address. Form 843 is preferred when the request includes a refund of paid amounts, because it captures payment dates (line 3).

---

## Channel C — Form 843 by mail

### Where to file (i843, "Where To File")

| If you are filing Form 843 ... | Mail to |
|---|---|
| In response to an IRS notice regarding a tax or fee (income, employment, gift, estate, excise, etc.) | The return address from which the notice was sent |
| To request a claim for refund in a Form 706 or 709 tax matter | Internal Revenue Service, Attn: E&G, Stop 824G, 7940 Kentucky Drive, Florence, KY 41042-2915 |
| In response to Letter 4658 (branded prescription drug fee) | Internal Revenue Service, Mail Stop 4921 BPDF, 1973 N. Rulon White Blvd., Ogden, UT 84201-0051 |
| In response to Letter 5067C (annual fee on health insurance providers final fee) | Internal Revenue Service, Mail Stop 4921 IPF, 1973 N. Rulon White Blvd., Ogden, UT 84201 |
| For a net interest rate of zero | The service center where you filed your most recent return |
| As a nonresident alien requesting a refund of social security or Medicare tax withheld in error | The address in Pub. 519, following its document rules |
| For requests related to Form 8300 | Internal Revenue Service, Rosa Parks Federal Building, P.O. Box 32621, Detroit, MI 48232 |
| For penalties, or for any other reason except those above | The service center where you would be required to file a current year tax return for the tax to which your claim or request relates (see the instructions for that return) |

For the last row with Form 1040, look up the user's state on https://www.irs.gov/filing/where-to-file-paper-tax-returns-with-or-without-a-payment (use the address for returns without a payment). For business returns, use the "Where to file" section of the current instructions for that return. Never use an address from memory; addresses change. The instructions note that mail sent to a changed address is forwarded.

### Pre-flight checklist

- [ ] Draft passes every Validation check in `SKILL.md`
- [ ] One Form 843 per period and tax type (or a documented exception)
- [ ] Printed on the current revision (Rev. December 2024) downloaded fresh from https://www.irs.gov/pub/irs-pdf/f843.pdf
- [ ] Signed in ink by the taxpayer; by both spouses for a joint return; by an officer with title for a corporation; by the fiduciary for an estate or trust
- [ ] IP PIN entered only if the IRS issued one
- [ ] Attachments labeled with name and SSN/ITIN/EIN on every page
- [ ] Form 2848 attached if a representative files; Form 1310 and authority documents for a decedent
- [ ] Copy of the notice attached when responding to one
- [ ] Full copy of the package kept by the user

### Mailing

- Certified mail with return receipt; keep the receipt with the copy as proof of the mailing date.
- One envelope per notice address. Separate Forms 843 for different periods can share an envelope only if they go to the same address.

### After mailing

- The instructions describe no tracking channel. The IRS notifies the taxpayer of its decision (IRS FTA page: "The IRS will notify you of its decision").
- The failure-to-pay penalty and interest continue on unpaid tax while the request is pending (IRS FTA page comparison table).
- If the user moves, file Form 8822 or 8822-B (i843, "Address change").
- If nothing arrives after a reasonable period, the user calls the number on the notice, or 800-829-1040 for individuals (the number the IRS lists for payment plan and general questions in the Instructions for Form 9465), with the copy and mailing receipt at hand.

---

## Channel D — Appeal of a denial

- Denials of penalty relief usually arrive on Letter 854C, "Penalty Waiver or Abatement Disallowed/Appeals Procedure Explained" (IRM 20.1.1.3.5.3).
- "You generally have 30 days from the date of the rejection letter to file your request for an appeal. Refer to your rejection letter for the specific deadline" (IRS penalty appeal page).
- Publication 5: if the total tax and penalties for each period in the letter is $25,000 or less, a small case request is allowed (the appeal form in the letter, Form 12203, or a brief written statement listing the disputed issues and why). Otherwise a formal written protest with facts, law, and a penalties-of-perjury statement is required for all periods.
- Send the appeal to the address in the denial letter, not to the Form 843 address.
- §6404(e) interest denials: Tax Court review under IRC §6404(h) is available to taxpayers within the §7430(c)(4)(A)(ii) net-worth limits, within 180 days after the final determination is mailed. Refer the user to a tax professional.

---

## Security and consent rules

Non-negotiable.

1. **The user signs.** The agent never signs Form 843, never signs as paid preparer, and never fabricates a signature or date.
2. **Explicit consent before any submission step.** Read back the reason box, line 2, the periods, and the mailing address, and get a yes before the user mails or faxes anything the agent prepared.
3. **No secrets in logs.** Do not store SSNs, ITINs, IP PINs, bank details, or medical records after the draft is delivered. Redact them in any saved working file (XXX-XX-XXXX).
4. **Medical and personal facts:** include only what the user chose to disclose, in the user's words. Do not add diagnoses or details.
5. **Do not overstate.** Write "likely eligible" for FTA, never "approved". Do not claim facts the user did not state (for example, that prior returns were timely).
6. **Representatives:** do not let a third party sign or call for the user without a Form 2848 on file.
7. **If the IRS response contradicts the draft** (different amounts, a prior FTA the user forgot), surface it to the user and re-run the workflow; do not resubmit blindly.
