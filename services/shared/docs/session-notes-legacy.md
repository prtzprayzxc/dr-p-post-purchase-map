# Dr. P Lifecycle Automation — Claude Handover Notes
**Last Updated:** 2026-04-16
**Status:** Build handoff ready
**Priority:** Use this file as the current handoff summary. If older notes conflict, this file wins unless replaced by a newer approved architecture spec.

---

## Purpose

This file is the clean handoff summary for the next builder or strategist.

It reflects the latest decisions confirmed in the working session and is intended to prevent build errors caused by older drafts, outdated assumptions, or conflicting planning notes.

---

## Canonical Direction

- GHL replaces ActiveCampaign as the automation system of record
- Kajabi remains the delivery platform for Kajabi-hosted products only
- Interact powers the paid UHA quiz
- ActiveCampaign is being retired, not run in parallel after GHL launch
- Historical contacts migrate into GHL as CRM records, not as active post-purchase participants unless purchase state is verified
- Launch should be treated as a greenfield GHL build unless specific existing assets are verified

---

## Products In Scope

### 1. Ultimate Hormone Assessment (`UHA`)
- Price point: `$47`
- Delivery: Interact quiz + GHL email follow-up
- Kajabi involved: `No`

### 2. 7-Day Hormone Reset & Recharge Challenge
- Price point: `$47`
- Delivery: Kajabi course
- Kajabi involved: `Yes`

### 3. Madame Estrogen Mastermind (`MEM`)
- Price point at launch: `Full pay + 3x installment option`
- Delivery: Kajabi course + community
- Includes: `3 months HWN bonus access`
- Kajabi involved: `Yes`

### 4. Hormone Wellness Network (`HWN`)
- Pricing: still flexible overall, but lifecycle should support paid membership plus MEM bonus members
- Delivery: Kajabi membership environment
- Kajabi involved: `Yes`

---

## Launch Assumptions Locked

### Kajabi Access Behavior

For all Kajabi-delivered products:
- Challenge
- MEM
- HWN

Assume:
- purchase triggers immediate Kajabi enrollment
- new Kajabi users receive Kajabi account setup email
- returning Kajabi users get the product added to their library without a new setup email
- manual rescue is exception-only, not normal fulfillment logic

### Manual Rescue Ownership

Owner:
- GHL Conversations Inbox support handler

Priority rules:
- MEM access issues: same business day priority
- HWN access issues: same business day priority
- UHA access issues: same business day if quiz access fails
- Challenge access issues: within 1 business day

MEM is the highest-priority rescue case.

---

## UHA Launch Logic

### Quiz Platform
- Platform: `Interact`
- Length: `48 questions`
- Scoring: already configured inside Interact

### Launch Result Types
- `estrogen_dominant`
- `balanced`

No expansion at launch.

### Webhook Destination
- Interact sends to GHL directly
- ActiveCampaign is removed from the routing chain

### Expected Webhook Fields
- `email`
- `first_name`
- `last_name` if captured
- `hormone_profile`
- `quiz_completed_timestamp`
- `quiz_name = UHA`

### Normalization Rule

Normalization happens inside GHL on webhook receipt.

Map:
- `dominant -> estrogen_dominant`
- `balanced -> balanced`

Do not change Interact result labels at launch.

---

## MEM Launch Logic

### Enrollment and Access
- Evergreen enrollment
- Immediate Kajabi access on purchase
- Immediate HWN bonus access on purchase

### Module Pacing
- Use weekly pacing structure inside Kajabi

### Weekly Accountability Call Handling
- Emails should reference a generic weekly accountability call
- Do not reference specific dates
- Do not depend on calendar automation
- Do not link to a static schedule page

Approved wording pattern:
- `Join the weekly accountability call inside your member area.`

### Launch Checkout Configuration
- `Full pay`
- `3x installment option`

Do not implement at launch:
- `$497 down + 10x $150`

Builder should structure checkout and automation logic so additional plans can be added later without rebuilding the system.

### HWN Bonus Mechanics for MEM

Confirmed:
- MEM includes 3 months free HWN access
- access starts immediately on purchase
- bonus members receive full HWN environment access

Includes:
- community
- masterclasses
- replays
- membership resources

No automatic paid conversion.

Conversion timing:
- Day 75 reminder
- Day 82 reminder
- Day 88 conversion invitation
- Day 90 revoke access if not converted

Conversion offer options:
- monthly
- annual

---

## HWN Launch Logic

### Launch Content Model

At launch, HWN should function as:
- primarily an on-demand membership with evergreen onboarding
- plus lightweight recurring monthly value emails

Do not depend on:
- live event dates
- calendar-triggered reminder logic
- manual event-date updates

### Recurring Email Structure
- start-of-month orientation email
- mid-month engagement reminder
- end-of-month preview email

### SMS
- not included at launch
- reason: SMS consent collection not implemented yet

### Cancellation Survey
- not implemented at launch
- cancellation flow should still:
  - cancel subscription
  - retain access until billing cycle end
  - remove access automatically afterward

---

## Final Tag Direction

Use these HWN lifecycle tags at minimum:
- `HWN_member_paid`
- `HWN_bonus_member`
- `HWN_member_expired`

Do not use:
- `hwn_bonus_active`

Reason:
- one bonus-access tag avoids ambiguity

If older docs reference `hwn_bonus_active`, replace it with `HWN_bonus_member` during implementation planning.

---

## Sender and Reply Handling

### Launch Sender Identity
- From Name: `Dr. P Team`
- From Email: `info@callmedoctorp.com`
- Reply-To: `info@callmedoctorp.com`

### Support Channel
- email only via GHL Conversations
- no phone support number at launch

### Inbox Monitoring
- monitored by support team inbox handler
- not Dr. P personally

Assignment rules inside GHL can be defined later.

---

## ActiveCampaign Migration Rules

### Retirement Direction
- ActiveCampaign is being retired
- do not keep AC automations active after GHL goes live

### Migration Handling
- contacts migrate into GHL as CRM records
- do not automatically enroll historical contacts into post-purchase workflows unless verified purchase state exists
- Interact routing moves from `Interact -> ActiveCampaign` to `Interact -> GHL`

### Current Known AC Context
- `5,954` active subscribers identified in audit
- `17` active automations discovered
- existing customers do exist
- old AC automation logic should not be treated as launch behavior baseline

---

## Build Strategy

Assume the GHL implementation is greenfield unless verified otherwise.

Unknown current build status:
- checkouts
- products
- tags
- workflows
- funnels

Default build assumption:
- build from scratch unless an existing asset is confirmed usable

---

## What Claude / Builder Should Treat As Outdated

The following older assumptions are superseded by this handoff:

- HWN launch automation should not depend on event-date reminders or calendar-driven scheduling
- SMS is not part of launch
- MEM launch does not include the `$497 + 10x $150` payment structure
- older `hwn_bonus_active` naming should be replaced
- older AC-based routing assumptions should be ignored
- older notes implying historical contacts should automatically enter lifecycle sequences should be ignored
- any flow copy depending on fixed event dates for launch should be rewritten to evergreen wording

---

## Remaining Open Items

These items are not blockers for the handoff, but they are still unresolved and should be finalized later:

- exact MEM accountability call schedule
- exact HWN live-event cadence
- ownership of monthly HWN content operations after launch
- detailed inbox assignment rules inside GHL
- final long-term pricing flexibility across programs beyond launch configuration

These should be handled as post-baseline implementation refinements, not blockers for the first build pass.

---

## Recommended Immediate Next Steps For Claude

1. Consolidate conflicting docs into one latest architecture spec
2. Replace outdated launch logic in older planning files
3. Build or outline final tag schema and custom field schema in GHL terms
4. Convert UHA webhook requirements into exact GHL mapping logic
5. Rewrite MEM and HWN launch messaging so it is fully evergreen
6. Remove event-date dependency from HWN launch workflows
7. Prepare build order for greenfield GHL implementation

---

## Final Source Of Truth Rule

Final source of truth is:
- latest approved lifecycle architecture spec
- latest approved provisioning logic
- latest approved tagging schema

If older notes conflict, the newest approved architecture from this conversation overrides them.
