# 7-Day Challenge Production Automation Map
## Verified architecture: GHL checkout -> Zapier -> Kajabi -> GHL email journey

---

## Purpose

This document defines the production automation path for the `7-Day Hormone Reset & Recharge Challenge` using the now-verified architecture:

- `GHL` owns payment and primary automation
- `Zapier` handles the handoff into Kajabi
- `Kajabi` grants course access and sends its access/setup email

This replaces earlier uncertainty about whether Kajabi needed to own checkout or first-party contact capture.

> **Enrollment mechanics** — the exact `GHL` workflow, Zap step order, Kajabi actions, payload schema, error handling, and test checklist are defined once in the shared [GHL → Zapier → Kajabi Enrollment Spec](../../shared/docs/ghl-zapier-kajabi-enrollment-spec.md). This document specifies only the Challenge-specific values and what the enrollment is bolted to.
>
> Challenge values to plug into that spec:
>
> - `course_key` = `challenge`
> - tag = `purchased_challenge`
> - Kajabi Offer ID = `<challenge_offer_id>` *(fill in once created)*
> - GHL Workflow = `Kajabi Enrollment — Challenge`
> - Zap name = `Enroll → Kajabi — Challenge`

---

## Final System Roles

### GHL

Owns:

- embedded checkout form
- payment capture
- contact record
- tags
- post-purchase workflow timing
- Challenge email sequence
- internal failure handling

### Zapier

Owns:

- receiving the post-purchase payload from `GHL`
- creating/updating the contact in `Kajabi`
- granting the correct Kajabi offer
- returning success/failure visibility through Zap history

### Kajabi

Owns:

- member record
- Challenge offer access
- setup/welcome email
- course hosting
- login state / course engagement

---

## Production Flow Overview

```text
1. Buyer completes payment in embedded GHL checkout
2. GHL creates/updates contact
3. GHL applies purchased_challenge + customer
4. GHL redirects buyer to challenge confirmation page
5. GHL workflow sends data to Zapier webhook
6. Zapier creates/updates Kajabi contact
7. Zapier grants Challenge offer in Kajabi
8. Kajabi sends account/setup or access email
9. GHL sends CH-1 immediately
10. GHL continues CH-2 through CH-9 on schedule
11. GHL stops MEM bridge if purchased_mem appears
```

---

## Required GHL Assets

### 1. Checkout asset

Embedded `GHL` order form for the Challenge.

Required result on successful payment:

- contact exists in `GHL`
- purchase data is attached to contact
- buyer is redirected to Challenge confirmation page

### 2. Tags

Required minimum tags:

- `customer`
- `purchased_challenge`
- `kajabi_account_created` if you use this as a known-user indicator
- `purchased_mem`
- optional support tags:
  - `challenge_kajabi_sync_sent`
  - `challenge_kajabi_sync_failed`
  - `challenge_access_issue`

### 3. Custom fields

Required minimum fields:

- `last_kajabi_login`

Recommended fields:

- `kajabi_sync_status`
- `kajabi_offer_granted_at`
- `kajabi_contact_id` if available from Zapier or later sync logic

### 4. Confirmation page

A website confirmation page must exist and should:

- confirm payment
- tell the buyer she is in
- explain that Kajabi access/setup email is coming
- give direct Day 1 framing
- show what to do if access email does not arrive

---

## Primary Trigger Logic in GHL

### Trigger

Use the successful Challenge purchase event as the root trigger.

Preferred production trigger:

- purchase completed for Challenge product

Fallback if needed:

- apply tag `purchased_challenge` immediately on successful payment

### Immediate actions in GHL

When Challenge purchase completes:

1. add tag `customer`
2. add tag `purchased_challenge`
3. optionally add `challenge_kajabi_sync_sent` only after webhook action fires
4. redirect to confirmation page
5. send webhook payload to Zapier
6. send `CH-1`

Important:

The Zapier handoff and `CH-1` should happen off the same purchase event, not off separate manual actions.

---

## Zapier Workflow

## Trigger Step

### App

`Webhooks by Zapier`

### Event

`Catch Hook`

### Expected payload from GHL

Minimum required fields:

- `email`
- `first_name`
- `last_name`
- `product_name`
- `purchase_date`

Recommended fields:

- `phone`
- `ghl_contact_id`
- `order_id`
- `purchase_amount`
- `tags`

### Validation rule

Do not continue if:

- email is blank
- product is not the Challenge product

If needed, add a Zapier filter step:

- continue only if `product_name = 7-Day Challenge`

## Action Step 1

### App

`Kajabi`

### Event

`Create/Update Contact`

### Required mapping

- Email -> Email
- First Name -> First Name
- Last Name -> Last Name

Optional mapping:

- Phone -> Phone

## Action Step 2

### App

`Kajabi`

### Event

`Grant Offer`

### Required configuration

- choose the exact Kajabi offer tied to the Challenge

This is the critical step.

Creating the contact alone is not enough.

## Expected result

When `Grant Offer` succeeds:

- Kajabi grants the buyer access to the Challenge
- Kajabi sends setup/welcome/access email based on its own settings

---

## Kajabi Configuration Required

### Offer

The Challenge offer must already exist in Kajabi and be the one selected in Zapier.

### Email behavior

At least one of these must be active:

- Kajabi offer confirmation / welcome email enabled
- Kajabi automation that sends the onboarding email when offer is granted

### Member experience

The granted offer must point to the Challenge product with:

- Day 1 immediately accessible
- Days 2-7 configured according to your Kajabi drip settings

---

## GHL Email Journey

These emails should continue to be triggered by the original Challenge purchase in `GHL`, not by Kajabi activity.

## Core sequence

- `CH-1` immediately
- `CH-2` Day 2 at `8am`
- `CH-3` Day 4 at `8am`
- `CH-4` Day 7 at `8am`
- `CH-5` Day 8 at `9am`

## MEM bridge

- `CH-6` Day 11 at `9am`
- `CH-7` Day 14 at `9am`
- `CH-8` Day 17 at `9am`
- `CH-9` Day 20 at `9am`

## Suppression rule

Before sending the `MEM` bridge emails, check:

- if `purchased_mem` exists -> stop the bridge

---

## Day 4 Branch Logic

The Day 4 split should stay in `GHL`.

### Decision field

- `last_kajabi_login`

### Rule

- if login detected since purchase -> send active `CH-3`
- if no login detected -> send inactive `CH-3`

### If Kajabi login sync is weak

Fallback:

- temporarily send the inactive/re-engagement version to everyone

Do not overcomplicate this branch until login tracking is reliable.

---

## Failure Handling

The automation is now validated, but production still needs explicit failure handling.

## Failure case 1: GHL webhook to Zapier does not fire

Recommended response:

- apply or log `challenge_kajabi_sync_failed`
- notify internal team
- send manual access rescue if needed

## Failure case 2: Zap runs but Kajabi contact is not created

Recommended response:

- treat as access issue
- notify support
- manually create/grant access

## Failure case 3: Kajabi contact exists but offer grant fails

Recommended response:

- this is the highest-priority failure
- apply `challenge_access_issue`
- notify support
- manually grant offer in Kajabi

## Failure case 4: Offer grants but buyer says she never got the email

Recommended response:

- direct her to password reset or resend setup path
- confirm access exists in Kajabi
- support assists same business day if needed

---

## Recommended Internal Visibility

To make troubleshooting realistic, production should include:

- internal notification on Zapier failure
- internal notification on repeated access complaints
- support note or tag for manual rescue cases

Recommended operational tags:

- `challenge_kajabi_sync_sent`
- `challenge_kajabi_sync_failed`
- `challenge_access_issue`
- `challenge_manual_rescue_complete`

---

## Recommended Production Build Order

1. Confirm the exact Challenge checkout trigger in `GHL`.
2. Confirm the exact Challenge offer in `Kajabi`.
3. Lock the webhook payload fields sent from `GHL` to `Zapier`.
4. Build or finalize the `Zapier` steps:
   - Catch Hook
   - Filter
   - Create/Update Contact
   - Grant Offer
5. Confirm Kajabi email behavior after `Grant Offer`.
6. Finalize Challenge confirmation page copy.
7. Build `CH-1` through `CH-9` in `GHL`.
8. Add access failure alerts and support rescue tags.
9. Run full end-to-end test again using a clean test email.

---

## End-to-End Acceptance Criteria

Production is ready when this sequence works:

1. buyer pays in embedded `GHL` checkout
2. contact is created/updated in `GHL`
3. `purchased_challenge` is applied
4. buyer lands on Challenge confirmation page
5. webhook reaches `Zapier`
6. `Zapier` creates/updates Kajabi contact
7. `Zapier` grants Challenge offer
8. Kajabi sends setup/welcome email
9. buyer can access the Challenge in Kajabi
10. `CH-1` sends from `GHL`
11. scheduled Challenge follow-up sequence continues correctly

If all 11 are true, the Challenge automation is production-ready.

---

## Final Architecture Statement

The 7-Day Challenge should now be built around this production assumption:

`GHL` owns commerce and customer communication.
`Zapier` performs the enrollment handoff.
`Kajabi` owns product access and member onboarding.

That is the working architecture unless later testing breaks it.
