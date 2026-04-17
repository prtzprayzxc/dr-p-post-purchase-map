# UHA Build Spec — GHL Specialist Handoff

**Scope:** Ultimate Hormone Assessment ($47) post-purchase lifecycle only. Standalone from other programs. Execute this document literally — every field, tag, trigger, delay, and condition is specified.

**Stack:** Interact (quiz host) → GHL (CRM + email + workflows + checkout). Kajabi is NOT in this flow.

**Estimated build time:** 1–2 working days end to end.

**Email copy source:** All email bodies, subjects, and preheaders live in `email-copy-uha-challenge.md` (UHA section, lines 1–401).

---

## 0. Assumptions & Prereqs

Before starting, confirm:

- [ ] GHL sub-account is provisioned and the specialist has Admin role
- [ ] Sending domain `callmedoctorp.com` is authenticated in GHL (SPF, DKIM, DMARC verified green)
- [ ] Interact quiz for the 48-question UHA assessment exists and is live
- [ ] Stripe (or chosen processor) is connected to GHL for $47 UHA charge
- [ ] Results page URL is decided (either a GHL funnel page or existing site page)
- [ ] Challenge checkout URL is known (for cross-sell emails UHA-5 and UHA-6)

If any item is unchecked, stop and resolve before building.

---

## 1. Foundation Setup (GHL)

### 1.1 Custom Fields

Path: **Settings → Custom Fields → Contact → Add Field**

| Field Name | Internal Key | Type | Options / Notes |
|---|---|---|---|
| UHA Result Type | `uha_result_type` | Dropdown (Single) | Values: `estrogen_dominant`, `balanced` |
| UHA Quiz Completed At | `uha_quiz_completed_at` | Date/Time | Populated by webhook |
| UHA Purchase Date | `uha_purchase_date` | Date/Time | Populated by order trigger |

### 1.2 Tags

Path: **Settings → Tags → Add Tag**

| Tag | Purpose |
|---|---|
| `uha_purchaser` | Applied on successful UHA checkout. Triggers WF-1. |
| `uha_quiz_pending` | Applied on purchase. Removed when quiz is completed. |
| `uha_completed` | Applied by WF-2 when webhook fires. Used to suppress nudge emails. |
| `purchased_challenge` | Used for cross-sell suppression. Applied elsewhere — do not create a trigger for this here. |

### 1.3 Product + Checkout

Path: **Payments → Products → Create Product**

- Name: `Ultimate Hormone Assessment`
- Description: (use marketing copy from product page)
- Price: `$47.00` USD, one-time
- Type: Digital

Path: **Sites → Funnels → New Funnel** (or use existing if already set up)

- Page 1: Checkout — two-step order form collecting email + first name + payment
- Page 2 (Thank You / redirect): redirect directly to the **Interact quiz URL** on successful payment
- Tracking: ensure order form captures `first_name` and `email` as GHL contact fields

### 1.4 Order → Automation Trigger

Path: **Automation → Workflows → New Workflow → "UHA — Order Intake"**

- Trigger: **Order Submitted** → Product: `Ultimate Hormone Assessment`
- Action 1: Add Tag `uha_purchaser`
- Action 2: Add Tag `uha_quiz_pending`
- Action 3: Update Custom Field → `uha_purchase_date` = `{{event.date_time}}` (current timestamp)
- Publish

*(This is a micro-workflow separate from WF-1 so the trigger stays clean.)*

---

## 2. Interact → GHL Webhook

### 2.1 Create the Inbound Webhook in GHL

Path: **Automation → Workflows → New Workflow → "UHA — Quiz Results"** (this becomes WF-2)

- Trigger: **Inbound Webhook**
- GHL will generate a URL like `https://services.leadconnectorhq.com/hooks/...`
- Copy this URL. Do not publish yet.

### 2.2 Configure the Interact Side

In the Interact dashboard → open the UHA quiz → **Integrations → Webhooks (or "Send Data")**

- Endpoint: paste the GHL webhook URL
- Method: POST
- Payload format: JSON

Required payload fields (Interact field → JSON key):

```json
{
  "email": "{respondent_email}",
  "first_name": "{respondent_first_name}",
  "uha_result_type": "{result_slug}",
  "uha_quiz_completed_at": "{completion_timestamp_iso8601}"
}
```

**Important:** the `result_slug` value sent from Interact must be exactly `estrogen_dominant` or `balanced` (lowercase, underscore). If Interact outputs a display label (e.g., "Estrogen Dominant"), add a mapping step in Interact OR add a branching node in WF-2 that maps display text → slug.

### 2.3 Map the Webhook in GHL

Back in WF-2 (Inbound Webhook trigger):

- Click the webhook node → **Map Fields**
- Map incoming JSON keys → GHL fields:
  - `email` → Standard field: Email
  - `first_name` → Standard field: First Name
  - `uha_result_type` → Custom field: `uha_result_type`
  - `uha_quiz_completed_at` → Custom field: `uha_quiz_completed_at`
- Save mapping

### 2.4 Test the Webhook

- Take the Interact quiz with a throwaway email you control
- In GHL, open Contacts → search that email
- Confirm contact exists and has the three custom fields populated correctly
- If fields are blank or malformed, stop and fix the mapping before proceeding

---

## 3. Email Templates

### 3.1 Sender Settings

Path: **Settings → Email Services → Default From**

- From name: `Dr. P Team`
- From email: `info@callmedoctorp.com`
- Reply-to: `info@callmedoctorp.com`

### 3.2 Build All 9 Templates

Path: **Marketing → Emails → Templates → New Template**

Copy the subject, preheader, and body from `email-copy-uha-challenge.md`. Use GHL merge tags:

- `[First Name]` → `{{contact.first_name}}`
- `[QUIZ URL]` → hardcode the Interact quiz URL
- `[RESULTS PAGE URL]` → hardcode the results page URL
- `[CHALLENGE CHECKOUT URL]` → hardcode the Challenge checkout URL

| Template ID | Copy Location | Notes |
|---|---|---|
| `UHA-1` | email-copy-uha-challenge.md §UHA-1 | Backup confirmation. No conditionals. |
| `UHA-2-ED` | email-copy-uha-challenge.md §UHA-2 (ESTROGEN DOMINANT VERSION) | — |
| `UHA-2-BAL` | email-copy-uha-challenge.md §UHA-2 (BALANCED VERSION) | — |
| `UHA-3` | email-copy-uha-challenge.md §UHA-3 | 4hr nudge |
| `UHA-3b` | email-copy-uha-challenge.md §UHA-3b | Day 2 nudge |
| `UHA-4-ED` | email-copy-uha-challenge.md §UHA-4 (ESTROGEN DOMINANT) | — |
| `UHA-4-BAL` | email-copy-uha-challenge.md §UHA-4 (BALANCED) | — |
| `UHA-5` | email-copy-uha-challenge.md §UHA-5 | Challenge pitch |
| `UHA-6` | email-copy-uha-challenge.md §UHA-6 | Final touch |

After building each, send a preview to yourself and verify: merge tags render, all three link types click through, mobile layout is clean.

---

## 4. Workflow WF-1: UHA — Post-Purchase

Path: **Automation → Workflows → New Workflow → "UHA — Post-Purchase"**

### Trigger
- **Tag Added:** `uha_purchaser`

### Step-by-step nodes

1. **Send Email** → Template: `UHA-1`
2. **Wait** → `4 hours`
3. **If/Else** → Condition: Contact does NOT have tag `uha_completed`
   - **YES branch:** Send Email → Template: `UHA-3`
   - **NO branch:** (empty — skip)
   - *(branches merge after)*
4. **Wait Until** → Specific time `9:00 AM` contact's timezone, on **Day 2 after workflow entry** *(GHL: use "Wait → Specific Day/Time" offset from workflow entry)*
5. **If/Else** → Contact does NOT have tag `uha_completed`
   - **YES branch:** Send Email → Template: `UHA-3b`
   - **NO branch:** skip
6. **Wait Until** → `9:00 AM` on **Day 6 after workflow entry**
7. **If/Else** → Contact does NOT have tag `purchased_challenge`
   - **YES branch:** Send Email → Template: `UHA-5`
   - **NO branch:** skip
8. **Wait Until** → `9:00 AM` on **Day 10 after workflow entry**
9. **If/Else** → Contact does NOT have tag `purchased_challenge`
   - **YES branch:** Send Email → Template: `UHA-6`
   - **NO branch:** skip
10. **End Workflow**

### Workflow Settings
- Allow Re-entry: **No**
- Stop on Response: **No**
- Event Start Time: Based on contact timezone (fallback: business timezone)
- Status: **Publish only after QA (Section 6)**

---

## 5. Workflow WF-2: UHA — Quiz Results

*(Started in §2.1 when you created the Inbound Webhook trigger.)*

### Trigger
- **Inbound Webhook** (URL already pasted into Interact)

### Step-by-step nodes

1. **Find Contact** → by `email` from webhook payload. If not found, create contact.
2. **Update Contact Field** → `first_name` = payload.first_name (only if currently blank)
3. **Update Contact Field** → `uha_result_type` = payload.uha_result_type
4. **Update Contact Field** → `uha_quiz_completed_at` = payload.uha_quiz_completed_at
5. **Add Tag** → `uha_completed`
6. **Remove Tag** → `uha_quiz_pending`
7. **If/Else** → `uha_result_type = estrogen_dominant`
   - **YES branch:** Send Email → Template: `UHA-2-ED`
   - **NO branch:** Send Email → Template: `UHA-2-BAL`
   - *(branches merge)*
8. **Wait Until** → `9:00 AM` on **Day 3 after `uha_purchase_date`** *(use custom-field date math; if GHL cannot offset from custom field, fall back to Day 3 after workflow entry)*
9. **If/Else** → `uha_result_type = estrogen_dominant`
   - **YES branch:** Send Email → Template: `UHA-4-ED`
   - **NO branch:** Send Email → Template: `UHA-4-BAL`
10. **End Workflow**

### Workflow Settings
- Allow Re-entry: **No**
- Status: **Publish only after QA (Section 6)**

---

## 6. QA Test Matrix

Run all four scenarios end-to-end with throwaway email addresses you control. Mark pass/fail.

### Scenario A — Happy path, estrogen dominant
1. Buy UHA with test email
2. Within 4 hrs: take quiz, select answers that produce `estrogen_dominant`
3. **Expected:** UHA-1 sent immediately; UHA-2-ED sent within 1 min of quiz completion; UHA-3 and UHA-3b NEVER fire; on Day 3 at 9am, UHA-4-ED fires; on Day 6, UHA-5 fires; on Day 10, UHA-6 fires.

### Scenario B — Happy path, balanced
- Same as A but quiz produces `balanced`.
- **Expected:** UHA-2-BAL and UHA-4-BAL fire instead of the ED versions.

### Scenario C — Purchaser never takes quiz
1. Buy UHA
2. Do NOT take the quiz
3. **Expected:** UHA-1 immediately; UHA-3 at +4hrs; UHA-3b at Day 2 9am; UHA-5 at Day 6; UHA-6 at Day 10. UHA-2 and UHA-4 never fire.

### Scenario D — Cross-sell suppression
1. Buy UHA, take quiz (either result)
2. Before Day 6: manually add tag `purchased_challenge` to the contact
3. **Expected:** UHA-5 and UHA-6 are skipped (If/Else branches to NO/empty side).

### Additional checks
- [ ] Send-time respects contact timezone (spot check a contact with non-local TZ)
- [ ] All links in all emails click through to correct URLs
- [ ] All merge tags resolve (no `{{contact.first_name}}` appearing as literal text)
- [ ] Unsubscribe link present and functional
- [ ] No duplicate sends if the same email address re-purchases (Allow Re-entry = No)

---

## 7. Go-Live Checklist

- [ ] Phase 1 foundation complete (fields, tags, product, order-intake workflow live)
- [ ] Phase 2 webhook tested with real Interact submission
- [ ] All 9 email templates built and preview-tested
- [ ] WF-1 and WF-2 built per spec
- [ ] All 4 QA scenarios pass
- [ ] Sender domain authenticated (green in GHL)
- [ ] Results page and Challenge checkout URLs confirmed live
- [ ] Publish WF-1 and WF-2
- [ ] Buy one real UHA seat with a personal email to confirm production flow
- [ ] Monitor first 48hrs of real purchases — watch for stuck contacts, failed webhooks, bounce rate spikes

---

## Appendix A — Contact State Transitions

```
[visitor]
   ↓ buys UHA
[contact + uha_purchaser + uha_quiz_pending + uha_purchase_date]
   ↓ (WF-1 starts)
   ↓ UHA-1 sent
   ↓
   ├── Takes quiz  →  [uha_completed, -uha_quiz_pending, uha_result_type set]
   │                  ↓ UHA-2 (ED or BAL)
   │                  ↓ Day 3 → UHA-4 (ED or BAL)
   │
   └── Skips quiz  →  4hr: UHA-3
                       Day 2: UHA-3b
   ↓
   Day 6:   UHA-5   (skipped if purchased_challenge)
   Day 10:  UHA-6   (skipped if purchased_challenge)
   ↓
   End → general nurture list
```

## Appendix B — Open Items / Decisions for Dr. P

These do not block build — flag to stakeholder and resolve in parallel:

1. **Results page URL:** Is this a new GHL funnel page to build, or an existing page on callmedoctorp.com?
2. **Challenge checkout URL:** Needs to exist before UHA-5 goes live (Day 6 from first purchaser).
3. **Interact result slug format:** Confirm the quiz tool outputs values matching the `estrogen_dominant` / `balanced` slugs — or agree on a mapping step.
4. **Bump offer on UHA checkout:** Memory notes a Challenge bump exists on UHA checkout. Decide whether to replicate in GHL at launch or post-launch.
5. **UHA-2 sends even for existing contacts:** If someone already has `uha_completed` from a prior quiz attempt and retakes it, WF-2 will re-fire and resend UHA-2. Decide: acceptable, or add a guard (check if `uha_result_type` changed)?

---

**End of spec.** Questions during build should route to the project owner, not interpreted unilaterally.
