# Kajabi Access Decision Tree
## Operational logic for onboarding without Kajabi API access

---

## Launch Status Update

This document still matters as an exception-handling and fallback reference, but launch assumptions are now more specific than the original draft.

For launch:
- `Challenge`, `MEM`, and `HWN` should be treated as auto-enrolling Kajabi products
- new users should receive Kajabi setup email
- returning users should receive direct-library access without a new setup email
- manual rescue is exception-only and owned by the support inbox handler

Use this document primarily for:
- support-path design
- edge cases
- rescue-state planning

See [session-notes.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/session-notes.md:1) for the latest handoff summary.

---

## Purpose

This document defines how customer access should work if Kajabi access behavior is degraded, inconsistent, or needs support intervention.

That means:
- GHL controls checkout, CRM, tags, emails, reminders, and internal workflow logic
- Kajabi still owns enrollment, account setup, access, and community permissions
- normal launch behavior assumes Kajabi access works reliably
- this document defines what to do when that assumption breaks

The goal is to make sure no customer gets stuck waiting for access, and no automation promises something the system cannot do.

---

## Core Rule

**GHL should communicate access. It should not claim to create access unless that behavior has been verified inside Kajabi.**

Use language like:
- "Watch for a separate email from Kajabi"
- "Use your existing login if you've purchased from us before"
- "If you don't see your access email within 15 minutes, reply here and we'll help"

Do NOT use language like:
- "We've created your account"
- "Your password has been generated"
- "Your Kajabi login is ready now"

Unless that has been proven operationally for the exact product and checkout path.

---

## System Boundary

### GHL Owns
- Checkout and payment confirmation
- Contact creation and deduplication
- Tags
- Custom fields
- Workflow timing
- Transactional and nurture emails
- Internal alerts and rescue workflows

### Kajabi Owns
- Member account creation
- Login/password setup
- Product enrollment
- Course access
- Community access

### Team Owns
- Manual rescue if Kajabi invitation/access fails
- Edge-case resolution for duplicate emails or missing access
- Updating internal tags when manual intervention is used

---

## Required Contact States

Create and use these states in GHL even if some must be updated manually.

### Tags
- `kajabi_access_pending`
- `kajabi_access_sent`
- `kajabi_account_created`
- `kajabi_returning_user`
- `kajabi_access_issue`
- `kajabi_manual_rescue_needed`
- `kajabi_manual_rescue_complete`

### Optional Product-Specific Tags
- `challenge_access_sent`
- `mem_access_sent`
- `hwn_access_sent`

### Suggested Custom Fields
- `kajabi_access_status`
- `kajabi_last_access_email_date`
- `kajabi_manual_rescue_owner`
- `kajabi_manual_rescue_notes`

Recommended values for `kajabi_access_status`:
- `pending`
- `sent`
- `confirmed`
- `issue`
- `manual_resolved`

---

## High-Level Decision Tree

```
PURCHASE OCCURS
    |
    v
IS THIS PRODUCT DELIVERED IN KAJABI?
    |-- No -> Send normal non-Kajabi confirmation flow
    |-- Yes
           |
           v
DO WE KNOW THIS CONTACT ALREADY HAS A KAJABI ACCOUNT?
    |-- Yes -> Send returning-user login instructions
    |-- No / Unknown
           |
           v
WILL KAJABI SEND ACCESS NATIVELY FOR THIS PURCHASE PATH?
    |-- Yes -> Send "watch for Kajabi email" instructions
    |-- No / Not confirmed
           |
           v
SEND TEAM ALERT + MANUAL RESCUE PROCESS
```

---

## Detailed Decision Logic

### Step 1: Product Check

Ask first: does this purchase even require Kajabi access?

- `UHA`: No, unless part of a bundle or future Kajabi-hosted asset
- `Challenge`: Yes
- `MEM`: Yes
- `HWN`: Yes

If the answer is no:
- do not apply Kajabi access tags
- do not send Kajabi instructions
- continue with the normal product flow

---

### Step 2: Known Returning User Check

If the contact has any of the following, treat her as a likely returning Kajabi user:
- `kajabi_account_created`
- prior purchase of another Kajabi-hosted product
- prior successful access confirmation from the team

If yes:
- apply `kajabi_returning_user`
- send login-based onboarding, not setup-based onboarding
- use copy like:
  - "Log in with the same email address you've used before"
  - "If you forgot your password, use Kajabi's reset link"

Do not tell returning users to wait for a new account unless you know Kajabi will send a new invitation anyway.

---

### Step 3: New or Unknown User Check

If the user is not confirmed as an existing Kajabi user:
- apply `kajabi_access_pending`
- assume she needs guidance
- do not promise instant access unless the exact checkout path has been tested

At launch, assume Kajabi will send access automatically. Use the remainder of this tree if testing or support cases show otherwise.

---

### Step 4: Enrollment Path Verification

For each Kajabi-delivered product, document the actual enrollment path:

1. Where purchase happens
   - GHL order form
   - Kajabi checkout
   - manual invoice/payment link

2. How access is granted
   - Kajabi offer auto-enrollment
   - manual admin enrollment
   - third-party connector

3. What the customer receives
   - invitation email
   - password setup email
   - nothing automatically

Launch assumption is that these paths are confirmed enough to build against. If real-world testing or support traffic shows otherwise, downgrade the affected product into a fallback mode.

---

## Approved Operating Modes

Use one of these three modes for each product.

### Mode A: Verified Native Kajabi Invite

Use this only if testing confirms:
- the customer is enrolled automatically
- Kajabi sends the invitation or login email on its own
- the process works for both new and returning users, or you know the difference clearly

Workflow:
1. GHL purchase trigger fires
2. Apply `kajabi_access_pending`
3. Send immediate GHL email with instructions:
   - "Watch for a separate email from Kajabi"
   - "If you've been here before, try logging in with your existing email"
4. Wait 15-30 minutes
5. Mark `kajabi_access_sent`
6. If no access complaint or support issue appears, keep flow moving

Recommended copy:
- "Your course access is on the way in a separate email from Kajabi."
- "If you don't see it within 15 minutes, reply to this email and we'll help."

---

### Mode B: Verified Returning-User Login, Manual New-User Rescue

Use this if:
- returning users can log in normally
- new users do not always receive a reliable Kajabi invite

Workflow:
1. Purchase trigger fires
2. If `kajabi_account_created` or prior Kajabi purchase exists:
   - send direct login instructions
   - apply `kajabi_returning_user`
3. If not:
   - apply `kajabi_access_pending`
   - send access-pending email
   - create internal task/alert for team review
   - if no confirmation within service window, execute manual rescue

This is a practical middle-ground if legacy customers behave differently than new ones.

---

### Mode C: Manual Enrollment Required

Use this if:
- purchase does not auto-enroll in Kajabi
- Kajabi does not send access without a manual team step
- current setup cannot guarantee self-serve access

Workflow:
1. Purchase trigger fires
2. Apply `kajabi_access_pending`
3. Send immediate purchase confirmation:
   - confirm payment
   - explain access is being prepared
   - give a realistic fulfillment window
4. Trigger internal alert to assigned team member
5. Team manually creates/enrolls/invites customer in Kajabi
6. Team updates GHL:
   - remove `kajabi_access_pending`
   - apply `kajabi_access_sent`
   - optionally apply `kajabi_account_created`
   - add rescue notes if needed
7. Send follow-up:
   - "Your access is ready"

If this mode is required, do not fake instant automation. Set the expectation clearly.

---

## Product-by-Product Recommendation

### UHA

Recommended mode: `No Kajabi logic`

Reason:
- UHA is currently not treated as a Kajabi-delivered product in the existing flow design
- it should remain independent unless fulfillment changes

Action:
- keep UHA outside this decision tree unless bundled with a Kajabi product

---

### 7-Day Challenge

Launch mode: `Mode A`

Reason:
- low-ticket buyers expect fast access
- delay or confusion will create avoidable support tickets

Needed verification:
- does GHL purchase create Kajabi access automatically?
- does Kajabi send a welcome/invite email to brand-new users?
- what happens for returning users?

Fallback if issues appear: `Mode B`

---

### Madame Estrogen Mastermind (MEM)

Launch mode: `Mode A` with same-business-day support fallback

Reason:
- higher-ticket buyers need white-glove confidence
- manual rescue is acceptable if framed well
- a team-assisted path is less risky than broken automation

Fallback if issues appear:
- keep immediate concierge-style onboarding
- route support issues to same-business-day priority handling
- do not leave high-value buyers in ambiguity

---

### Hormone Wellness Network (HWN)

Launch mode: `Mode A`

Reason:
- recurring members need reliable first access
- recurring billing plus missing access is a churn risk

Needed verification:
- does the monthly or annual purchase path consistently enroll members?
- what happens on rejoin/reactivation?

Fallback if issues appear: `Mode B`

---

## Manual Rescue Process

This is the fallback the team should use whenever access is not confirmed.

### Trigger Manual Rescue If
- contact replies that no Kajabi email was received
- contact cannot log in
- checkout was successful but no access path is verified
- internal team sees purchase on a path known to require manual enrollment

### Rescue Steps
1. Confirm payment in GHL
2. Confirm correct purchase/product
3. Check whether the email used at purchase matches any existing Kajabi member profile
4. If existing user:
   - send login/reset instructions
5. If new user:
   - manually invite or enroll inside Kajabi
6. Update GHL tags/fields:
   - remove `kajabi_access_pending`
   - apply `kajabi_manual_rescue_complete`
   - apply `kajabi_access_sent`
   - update `kajabi_access_status = manual_resolved`
7. Send confirmation email:
   - "Your access is ready"

### Internal SLA Recommendation
- Challenge: within 1 business day
- MEM: same business day priority
- HWN: same business day priority

---

## Confirmation Page Rules

Because the confirmation page is the highest-attention moment, every Kajabi-delivered product page should reflect one of these messages.

### Returning User Version
- "You're in."
- "Use the same email address you've used before to log in."
- direct Kajabi login link
- "Forgot your password? Use the reset link on the login page."

### New or Unknown User Version
- "You're in."
- "Watch for a separate email from Kajabi with your access steps."
- "It should arrive within 15 minutes."
- "If you don't see it, check spam or reply to our email and we'll help."

### Manual Fulfillment Version
- "You're in."
- "We're preparing your access now."
- "You'll receive your course invitation shortly."
- include a realistic time window

---

## Email Logic Rules for GHL Builder

### Rule 1
If Kajabi access is not verified, send an **access guidance** email, not an **access completed** email.

### Rule 2
Never send conflicting paths in the same email.

Bad example:
- "Set your password in the Kajabi email"
- "Also log in with your existing password"

Good example:
- branch email copy by user state

### Rule 3
All Kajabi-delivered products need an access issue branch.

At minimum:
- wait period
- support CTA
- internal alert
- manual rescue tag

### Rule 4
If manual rescue is common, operationalize it instead of pretending it is exceptional.

That means:
- assign ownership
- define response time
- use tags and status fields
- write the rescue email templates in advance

---

## Minimum Testing Plan Before Build Goes Live

Test each Kajabi-delivered product with:
- a brand-new email address
- an email address tied to an existing Kajabi user
- a checkout with a bump where relevant
- a resend/support-needed scenario

For each test, document:
- was enrollment successful?
- did Kajabi send an email?
- how long did it take?
- what did the customer see on the confirmation page?
- did GHL send the correct branch email?
- was manual rescue needed?

Do not finalize automation copy until this test matrix is complete.

---

## Builder Handoff Summary

Use this operating principle:

**Until Kajabi enrollment behavior is verified, build workflows around access guidance, access pending states, and manual rescue paths.**

That protects the customer experience and prevents the system from making promises it cannot keep.

Immediate builder tasks:
1. Create the Kajabi access tags and custom fields in GHL
2. Verify enrollment behavior for Challenge, MEM, and HWN
3. Assign each product to Mode A, B, or C
4. Build confirmation-page copy to match the assigned mode
5. Build support/rescue branches before launch
