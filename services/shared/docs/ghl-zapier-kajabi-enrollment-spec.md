# GHL → Zapier → Kajabi Enrollment Spec
## Canonical integration pattern for all Kajabi-delivered courses

---

## Purpose

This document defines the exact technical integration that connects `GHL` checkout to `Kajabi` course access through `Zapier`.

It is the single source of truth for how course enrollment works across every program in the Dr. P ecosystem (`Challenge`, `MEM`, `HWN`, `UHA`, and any future Kajabi-hosted course).

Each per-course production-automation-map should reference this spec instead of restating the enrollment mechanics.

---

## Scope

This spec covers:

- what `GHL` must do immediately after a successful purchase
- what payload `GHL` sends to `Zapier`
- the exact Zap step order and each step's configuration
- what `Zapier` does in `Kajabi` (find/create contact + grant offer)
- what `Kajabi` does on its own (welcome email, access)
- how failures are caught and recovered
- the per-course configuration required to reuse this pattern

This spec does NOT cover:

- GHL email cadence after purchase (lives in each course's flow doc)
- Kajabi course content / curriculum (lives in Kajabi itself)
- Support/rescue operational policy (see `kajabi-access-decision-tree.md`)

---

## Architecture At A Glance

```text
BUYER
  └─ completes payment in embedded GHL checkout
      │
      ▼
GHL
  ├─ creates/updates contact
  ├─ applies tags (customer + purchased_<course>)
  ├─ redirects buyer to confirmation page
  └─ triggers "Kajabi Enrollment" workflow
          │
          ▼
      GHL workflow fires Outbound Webhook → Zapier Catch Hook URL
          │
          ▼
ZAPIER (per-course Zap, identical shape)
  ├─ Step 1: Catch Hook (payload from GHL)
  ├─ Step 2: Filter — only continue if `tag` matches `purchased_<course>`
  ├─ Step 3: Kajabi "Find Person" by email
  ├─ Step 4: Paths — New user vs Returning user
  │     ├─ Path A: New user  → "Create Person" + "Grant Offer"
  │     └─ Path B: Existing  → "Grant Offer" only
  ├─ Step 5: Webhook back to GHL — mark `kajabi_enrolled = true`
  └─ On error: Zap catches failure → webhook back to GHL alert workflow
          │
          ▼
KAJABI
  ├─ contact exists with correct offer access
  └─ sends welcome / password-setup email to NEW users only
          │
          ▼
GHL
  ├─ CH-1 / MEM-1 / etc. sends immediately per course cadence
  └─ downstream flow continues
```

---

## GHL Side

### 1. Checkout asset

Embedded order form, one per course. Required result on successful payment:

- contact exists or is updated in `GHL`
- purchase data is attached
- redirect lands on the course confirmation page

### 2. Tags applied on purchase

Apply both:

- `customer`
- `purchased_<course>` (e.g. `purchased_challenge`, `purchased_mem`, `purchased_hwn`, `purchased_uha`)

### 3. Post-purchase workflow

Workflow name convention: `Kajabi Enrollment — <Course>`

Trigger: tag `purchased_<course>` applied (or order fulfilled event, whichever is more reliable per GHL tenant behavior).

Action sequence:

1. **Wait** 30 seconds (lets GHL settle contact + order record)
2. **Outbound Webhook** → Zapier Catch Hook URL for that course
3. **Wait** 2 minutes
4. **If** custom field `kajabi_enrolled` is empty → route to **Alert** sub-workflow (internal email to ops + add tag `enrollment_pending`)

### 4. Webhook payload (GHL → Zapier)

Send as `POST` with `Content-Type: application/json`. Fields required:

```json
{
  "event": "purchase",
  "course_key": "challenge",
  "course_offer_id": "<kajabi_offer_id>",
  "contact": {
    "id": "{{contact.id}}",
    "email": "{{contact.email}}",
    "first_name": "{{contact.first_name}}",
    "last_name": "{{contact.last_name}}",
    "phone": "{{contact.phone}}"
  },
  "order": {
    "id": "{{order.id}}",
    "amount": "{{order.amount}}",
    "currency": "{{order.currency}}",
    "created_at": "{{order.created_at}}"
  },
  "tag": "purchased_challenge",
  "source": "ghl"
}
```

`course_key` and `course_offer_id` are per-course constants; the other fields are merge tokens.

### 5. Post-Zap callback

`GHL` must expose a second Inbound Webhook that Zapier calls back to mark enrollment success. That webhook sets:

- custom field `kajabi_enrolled = true`
- custom field `kajabi_enrolled_at = <timestamp>`
- tag `kajabi_enrollment_ok`

If the alert sub-workflow fires (enrollment still blank after 2 min), it adds tag `enrollment_pending` so ops can intervene.

---

## Zapier Side

### Zap naming convention

One Zap per course. Name format: `Enroll → Kajabi — <Course>`

### Step 1 — Catch Hook (Webhooks by Zapier)

- Trigger: `Catch Hook`
- URL: use this exact URL as the `GHL` Outbound Webhook target
- No "Pick off a child key" needed; payload is consumed as-is

### Step 2 — Filter (Only Continue If...)

- `tag` exactly matches `purchased_<course>`
- `contact.email` contains `@`

This blocks malformed or misrouted payloads from proceeding.

### Step 3 — Find Person in Kajabi

- App: **Kajabi**
- Action: `Find Person` (NOT `Find or Create Person` — we need the branch to know which path to take)
- Search field: `email` = `contact.email`
- "Should this step be considered a success when nothing is found?" → **Yes**

Result: either a Kajabi Person ID or a null.

### Step 4 — Paths

Path logic uses the Step 3 output:

- **Path A (New user)**: Step 3 returned null → run `Create Person` + `Grant Offer`
- **Path B (Returning user)**: Step 3 returned a Person ID → run `Grant Offer` only

**Path A — steps:**

1. Kajabi → `Create Person`
   - `email` = `contact.email`
   - `first_name` = `contact.first_name`
   - `last_name` = `contact.last_name`
   - `send_welcome_email` = **true** (Kajabi handles welcome/password setup)
2. Kajabi → `Grant Offer`
   - `person_id` = Step A.1 output
   - `offer_id` = `course_offer_id` from payload

**Path B — steps:**

1. Kajabi → `Grant Offer`
   - `person_id` = Step 3 output
   - `offer_id` = `course_offer_id` from payload

Returning users do NOT get a second welcome email — they already have a login.

### Step 5 — Webhook back to GHL

- App: **Webhooks by Zapier**
- Action: `POST`
- URL: GHL Inbound Webhook for the `Kajabi Enrollment Success` handler
- Body:

```json
{
  "contact_id": "<from catch hook>",
  "course_key": "<from catch hook>",
  "kajabi_person_id": "<from Step 3 or Path A.1>",
  "path": "new|existing"
}
```

### Step 6 — Error path (Zap Error Handling)

Turn on Zapier's built-in **Error Handling** for Steps 3–5. If any step errors:

- fire a `Webhooks by Zapier POST` to the GHL `Kajabi Enrollment Failure` Inbound Webhook
- include `contact_id`, `course_key`, `step_failed`, `error_message`
- GHL failure handler adds tag `enrollment_failed` and alerts ops

---

## Kajabi Side

### Required setup (per course)

- One `Offer` per course, priced at $0 (access-only; payment lives in GHL)
- Offer ID recorded in the GHL custom field or referenced in the Zap config
- Welcome email template toggled ON for each offer that new users should receive a setup email for
- Welcome email should NOT be enabled on any returning-user code path (controlled by `send_welcome_email` flag at create-person time)

### Kajabi-owned

- `Person` record
- `Offer` access and course hosting
- Welcome / password-setup email (only for new users)
- Login state (`last_sign_in_at`, used downstream for the Day-4 branch in Challenge)

### Kajabi does NOT own

- Payment
- Marketing email cadence
- Tags (Kajabi tags are optional and not used as system-of-record)

---

## Per-Course Configuration Table

Each course reuses the same pattern with these values swapped in:

| Course       | `course_key` | Tag                   | Kajabi Offer ID (placeholder)     | GHL Workflow                      | Zap name                        |
| ------------ | ------------ | --------------------- | --------------------------------- | --------------------------------- | ------------------------------- |
| 7-Day Challenge | `challenge`  | `purchased_challenge` | `<challenge_offer_id>`           | `Kajabi Enrollment — Challenge`   | `Enroll → Kajabi — Challenge`   |
| MEM          | `mem`        | `purchased_mem`       | `<mem_offer_id>`                 | `Kajabi Enrollment — MEM`         | `Enroll → Kajabi — MEM`         |
| HWN          | `hwn`        | `purchased_hwn`       | `<hwn_offer_id>`                 | `Kajabi Enrollment — HWN`         | `Enroll → Kajabi — HWN`         |
| UHA          | `uha`        | `purchased_uha`       | `<uha_offer_id>`                 | `Kajabi Enrollment — UHA`         | `Enroll → Kajabi — UHA`         |

Fill in the offer IDs once they exist in Kajabi. Keep the pattern identical — any divergence needs an explicit note here.

---

## Error Handling & Recovery

### Failure modes

1. **GHL webhook never fires** — usually a workflow trigger config issue. Detected by: no Zap run in Zap history for a known purchase.
2. **Zapier filter blocks payload** — tag mismatch or missing email. Detected by: Zap run shows "Filter didn't pass."
3. **Kajabi `Find Person` errors** — API quota or auth issue. Detected by: Zap run error on Step 3.
4. **Kajabi `Create Person` fails on duplicate** — usually means Step 3 returned null but the person actually exists (race or email case mismatch). Detected by: Step 4 Path A.1 errors with `422` or similar.
5. **`Grant Offer` fails** — offer ID invalid or person ID expired. Detected by: Zap error on `Grant Offer` step.
6. **Callback webhook to GHL fails** — GHL endpoint down or misconfigured. Detected by: Zap error on Step 5.

### Recovery rules

- Zap **Error Handling** must be ON for all Kajabi steps and the callback.
- On any error, Zap must POST to the GHL `Kajabi Enrollment Failure` endpoint so ops is alerted.
- The GHL alert workflow adds tag `enrollment_failed` and emails `ops@<internal>`.
- Manual rescue: ops grants the offer in Kajabi directly, then adds tag `kajabi_enrolled_manual` in GHL and sets `kajabi_enrolled = true` so downstream flows proceed.

### Idempotency

The pattern is safe to retry because:

- `Find Person` is a read, no side effect
- `Create Person` only runs on the null branch; if retried after a race, it will 422 and the error path fires (ops handles)
- `Grant Offer` is idempotent in Kajabi — granting an offer the person already has is a no-op

If Zapier Auto-Replay is enabled, leave it on for transient failures (5xx), off for 4xx (don't retry business-logic failures).

---

## Test Checklist (Go / No-Go)

Before a course goes live, execute this full sequence with a real test purchase:

1. Submit a test purchase through the embedded `GHL` checkout
2. Confirm `purchased_<course>` + `customer` tags are applied to the GHL contact
3. Confirm Zap history shows a run for that purchase (Step 1 fired)
4. Confirm Step 2 filter passed
5. Confirm Step 3 `Find Person` returned the expected null / person ID
6. Confirm the correct Path (A or B) ran
7. For new users: confirm Kajabi sent the welcome / password-setup email
8. Confirm the buyer can log into Kajabi and sees the course
9. Confirm Step 5 callback fired and GHL custom field `kajabi_enrolled = true`
10. Confirm GHL downstream emails (CH-1, MEM-1, etc.) send on cadence
11. Intentionally fail one step (e.g. pause Kajabi auth) and confirm the failure webhook + `enrollment_failed` tag + ops alert all fire

Ship only when all 11 pass. Re-run after any Zap or Kajabi config change.

---

## Monitoring

- **Zap history** — daily spot check for failed runs
- **GHL tag `enrollment_pending`** — should always be 0; any value = ops intervention needed
- **GHL tag `enrollment_failed`** — should always be 0; alert-level
- **Kajabi Offer grant rate** — should roughly match GHL purchase count per course per day

---

## Where This Is Referenced

Each course's production-automation-map should link to this spec instead of restating the enrollment mechanics:

- `services/challenge/docs/challenge-production-automation-map.md`
- `services/mem/docs/*-production-automation-map.md` (when created)
- `services/hwn/docs/*-production-automation-map.md` (when created)
- `services/uha/docs/*-production-automation-map.md` (when created)

If this spec changes, update every course that depends on it or pin the reference to a commit.
