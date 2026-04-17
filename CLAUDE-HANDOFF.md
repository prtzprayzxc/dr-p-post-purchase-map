# Claude Handoff — Dr. P Post-Purchase Automation
**Last Updated:** 2026-04-16
**Status:** Builder-ready handoff
**Use This First:** Yes

---

## What This File Is

This is the single-file handoff for the next Claude or builder.

It compresses the current repo into one implementation baseline and resolves the main conflicts that existed across earlier planning docs.

If any older file conflicts with this handoff, use this file plus the normalized launch docs listed below.

---

## Canonical Files

Use these as the active source set:

- [session-notes.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/session-notes.md:1)
- [brief-ghl-specialist.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/brief-ghl-specialist.md:1)
- [brief-dr-p-stakeholder.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/brief-dr-p-stakeholder.md:1)
- [kajabi-access-decision-tree.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/kajabi-access-decision-tree.md:1)
- [email-copy-uha-challenge.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/email-copy-uha-challenge.md:1)
- [email-copy-mem.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/email-copy-mem.md:1)
- [email-copy-hwn.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/email-copy-hwn.md:1)

Treat older exploratory notes, visuals, and superseded logic as reference only.

---

## Repo Index

Use this as the quick orientation map.

### Primary Handoff
- [CLAUDE-HANDOFF.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/CLAUDE-HANDOFF.md:1)
  Single-file launch baseline for the next builder.

- [session-notes.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/session-notes.md:1)
  Clean working-session summary with resolved decisions and launch assumptions.

### Build Specs
- [brief-ghl-specialist.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/brief-ghl-specialist.md:1)
  Main technical implementation brief for workflows, tags, and logic.

- [kajabi-access-decision-tree.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/kajabi-access-decision-tree.md:1)
  Kajabi exception handling, fallback modes, and manual rescue logic.

- [brief-dr-p-stakeholder.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/brief-dr-p-stakeholder.md:1)
  Client-facing experience summary, now updated with launch decisions.

### Email Copy
- [email-copy-uha-challenge.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/email-copy-uha-challenge.md:1)
  Launch email copy for UHA and Challenge.

- [email-copy-mem.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/email-copy-mem.md:1)
  Launch email copy for MEM, including dunning and HWN bonus conversion.

- [email-copy-hwn.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/email-copy-hwn.md:1)
  Launch email copy for HWN evergreen onboarding, retention, dunning, cancellation, and win-back.

### Visual / Reference Docs
- [checkout-to-delivery-flows.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/checkout-to-delivery-flows.md:1)
  Large narrative architecture doc. Useful for context, but not the first file to trust if it conflicts with launch handoff docs.

- [visual-flow-overview.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/visual-flow-overview.md:1)
  High-level ecosystem map and visual summary.

- [visual-flow-detailed.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/visual-flow-detailed.md:1)
  Detailed step-by-step visual reference of the original flow concepts.

### Legacy / Context Files
- `.mcp.json`
  Environment/integration context. Not a business-logic source of truth.

Older visuals and exploratory notes may still contain superseded assumptions. Use them only for context after checking the launch files above.

---

## System Direction

- `GHL` is the automation system of record
- `Kajabi` is the delivery platform for Kajabi-hosted products
- `Interact` powers the paid `UHA` quiz
- `ActiveCampaign` is being retired
- Historical contacts move into GHL as CRM records only unless verified purchase state says otherwise
- Launch should be treated as a greenfield GHL build unless an existing asset is explicitly verified as reusable

---

## Products In Scope

### 1. UHA
- Product: `Ultimate Hormone Assessment`
- Price: `$47`
- Delivery: Interact quiz + GHL follow-up
- Kajabi: `No`

### 2. Challenge
- Product: `7-Day Hormone Reset & Recharge Challenge`
- Price: `$47`
- Delivery: Kajabi course
- Kajabi: `Yes`

### 3. MEM
- Product: `Madame Estrogen Mastermind`
- Launch pricing: `Full pay + 3x installments`
- Delivery: Kajabi course + community
- Includes: `3 months HWN bonus access`
- Kajabi: `Yes`

### 4. HWN
- Product: `Hormone Wellness Network`
- Delivery: Kajabi membership environment
- Launch model: evergreen/on-demand membership
- Kajabi: `Yes`

---

## Launch Assumptions Locked

### Kajabi Access

For:
- `Challenge`
- `MEM`
- `HWN`

Assume:
- purchase triggers immediate Kajabi enrollment
- new Kajabi users receive Kajabi setup email
- returning Kajabi users get product access added directly to their library
- manual rescue is exception-only

Manual rescue owner:
- support inbox handler via GHL Conversations

Priority:
- `MEM`: same business day priority
- `HWN`: same business day priority
- `UHA` access issue: same business day if quiz access fails
- `Challenge`: within 1 business day

---

## UHA Logic

### Platform
- Quiz platform: `Interact`
- Quiz length: `48 questions`
- Result count at launch: `2`

### Final Result Types
- `estrogen_dominant`
- `balanced`

### Webhook Destination
- `Interact -> GHL`

### Expected Webhook Fields
- `email`
- `first_name`
- `last_name` if captured
- `hormone_profile`
- `quiz_completed_timestamp`
- `quiz_name = UHA`

### Normalization Rule In GHL
- `dominant -> estrogen_dominant`
- `balanced -> balanced`

Do not change Interact result labels at launch.

---

## MEM Logic

### Enrollment
- evergreen
- immediate Kajabi access
- immediate HWN bonus access

### Module Pacing
- weekly pacing inside Kajabi

### Launch Checkout Configuration
- `pay in full`
- `3x installments`

Do not launch with:
- `$497 + 10x $150`

### Accountability Call Handling

Use generic evergreen language only.

Allowed pattern:
- `Join the weekly accountability call inside your member area.`

Do not depend on:
- fixed dates
- calendar links
- schedule pages

### MEM HWN Bonus Mechanics
- bonus starts immediately on purchase
- buyer gets full HWN environment access
- no automatic paid conversion

Reminder cadence:
- Day `75`
- Day `82`
- Day `88`
- Day `90` revoke if not converted

Conversion options:
- monthly
- annual

---

## HWN Logic

### Launch Model

Launch HWN as:
- evergreen
- on-demand
- community/resource-oriented

Do not make launch automation depend on:
- event dates
- live-session reminders
- replay attendance logic
- manual monthly calendar updates
- SMS

### Monthly Email Structure
- start-of-month orientation
- mid-month engagement reminder
- end-of-month preview

### Cancellation At Launch
- cancel subscription
- retain access through billing period
- remove access automatically afterward

Cancellation survey:
- not part of launch
- may be added later

---

## Sender Setup

- From Name: `Dr. P Team`
- From Email: `info@callmedoctorp.com`
- Reply-To: `info@callmedoctorp.com`
- Support channel: email only through GHL Conversations
- Phone support: not part of launch

---

## Tag Direction

### Core Purchase Tags
- `customer`
- `purchased_uha`
- `purchased_challenge`
- `purchased_mem`
- `purchased_hwn`

### UHA State Tags
- `uha_completed`
- `uha_result_estrogen_dominant`
- `uha_result_balanced`
- `uha_quiz_abandoned`

### Kajabi Access Baseline
- `kajabi_account_created`

### MEM Payment Tags
- `mem_paid_full`
- `mem_payment_plan`
- `mem_payment_failed`
- `mem_access_paused`

### HWN Tags
- `HWN_member_paid`
- `HWN_bonus_member`
- `HWN_member_expired`

### Legacy Tag Rule
- do not use `hwn_bonus_active`
- replace legacy bonus references with `HWN_bonus_member`

Note:
- Some older normalized docs still use lowercase historical tag naming in places because they were patched rather than fully rewritten. For new implementation, prefer the final launch naming direction above.

---

## Migration Rules

- `ActiveCampaign` is being retired
- AC automations should not remain active after GHL go-live
- historical contacts import into GHL as CRM records
- do not auto-enroll imported contacts into post-purchase workflows unless verified purchase state exists
- Interact routing must move off AC and into GHL

Known AC context from audit:
- `5,954` active subscribers
- `17` active automations

This matters operationally, but AC logic should not be treated as launch behavior.

---

## What Changed From Older Drafts

These older assumptions are no longer launch-valid:

- HWN launch based on event-date reminders
- SMS reminders at launch
- cancellation survey at launch
- MEM launch using `$497 + 10x $150`
- hard-coded accountability-call dates in MEM emails
- undefined UHA quiz platform
- AC remaining live alongside GHL

---

## Current Email Status

### Normalized Launch Email Files
- [email-copy-uha-challenge.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/email-copy-uha-challenge.md:1)
- [email-copy-mem.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/email-copy-mem.md:1)
- [email-copy-hwn.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/email-copy-hwn.md:1)

These have already been updated for:
- launch sender identity
- evergreen HWN launch logic
- generic MEM accountability-call language
- retired MEM payment-plan removal
- revised MEM HWN bonus cadence

One intentional future-phase conditional remains in HWN win-back copy for exit-survey handling.

---

## Recommended Build Order

1. Finalize tag and custom field schema in GHL
2. Set up Kajabi enrollment triggers and confirm new vs returning user behavior
3. Configure Interact -> GHL webhook mapping for UHA
4. Build UHA workflows
5. Build Challenge workflows
6. Build MEM workflows, payment handling, and HWN bonus logic
7. Build HWN evergreen onboarding and recurring monthly value cycle
8. Add dunning, cancellation, and win-back
9. Add cross-flow throttle logic
10. Test end-to-end with new-user and returning-user scenarios

---

## What Claude Should Do Next

If starting fresh from this file:

1. Treat this handoff as the working baseline
2. Avoid re-opening launch decisions that are already locked here
3. Implement only launch-scope logic first
4. Push event-based HWN features, SMS, and cancellation-survey enhancements into post-launch scope
5. If a doc conflict appears, prefer this file, then `session-notes.md`, then the normalized brief files

---

## Open But Non-Blocking

These are not launch blockers:

- exact live-event cadence for HWN
- exact long-term MEM/HWN pricing flexibility beyond launch
- future SMS consent collection
- future cancellation survey implementation
- future calendar-based HWN live-event automation
- inbox assignment automation inside GHL

---

## Final Rule

Use this file to keep momentum.

If a future builder changes launch logic, they should update this file first so the repo does not drift back into conflicting specs.
