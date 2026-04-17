# GHL Specialist — Technical Build Brief
### Complete implementation spec for Dr. P lifecycle automation

---

## Launch Override

Use [session-notes.md](/C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/session-notes.md:1) as the latest handoff summary.

This file remains a working build brief, but the following launch assumptions are now locked and override older planning language in this document:

- Kajabi enrollment for `Challenge`, `MEM`, and `HWN` is assumed automatic and reliable at launch
- `UHA` uses `Interact`, not an undefined quiz platform
- `UHA` launch result types are exactly `balanced` and `estrogen_dominant`
- `MEM` launch checkout is `full pay + 3x installments`
- `MEM` emails must use generic weekly accountability-call language only
- `HWN` launch should be evergreen and must not depend on event-date scheduling
- `SMS` is out of scope for launch
- `HWN_bonus_member` replaces `hwn_bonus_active` for bonus-access tracking
- `ActiveCampaign` is being retired and should not remain active after GHL go-live

---

## System Overview

| Component | Platform | Role |
|-----------|----------|------|
| Checkout | GHL | Payment processing, bump offers, order forms |
| CRM | GHL | Contact records, tags, segmentation, pipeline |
| Email Automation | GHL | All email workflows, sequences, triggers |
| SMS (post-launch) | GHL | Future live event reminders if consent collection is added |
| Course Delivery | Kajabi | Course hosting, module drip, community |
| Quiz | Interact | UHA 48-question quiz — webhook results into GHL |

**Integration:** GHL → Kajabi via webhook or native integration (Zapier fallback). GHL is the brain. Kajabi is the classroom.

---

## BUILD ORDER

Build in this order. Each phase depends on the previous one.

```
Phase 1: Tag Architecture + Custom Fields     (Day 1)
Phase 2: Kajabi Integration + Enrollment       (Day 2)
Phase 3: UHA Workflow                          (Day 3-4)
Phase 4: Challenge Workflow                    (Day 4-5)
Phase 5: MEM Workflow + Dunning                (Day 5-7)
Phase 6: HWN Workflow + Retention + Win-Back   (Day 7-9)
Phase 7: Cross-Flow Throttle Logic             (Day 9-10)
Phase 8: Confirmation Pages (4 pages)          (Day 10-11)
Phase 9: End-to-End Testing                    (Day 11-12)
```

---

## PHASE 1: TAG ARCHITECTURE

Create ALL tags before building any workflow. Naming convention: `category_descriptor`

### Purchase Tags
```
customer
purchased_uha
purchased_challenge
purchased_mem
purchased_hwn
high_value_customer
```

### Product State Tags
```
kajabi_account_created
uha_completed
uha_result_estrogen_dominant
uha_result_balanced
uha_quiz_abandoned
hwn_bonus_member
hwn_bonus_start_[YYYY-MM-DD]     ← dynamic, set via custom field
```

### Payment Tags
```
mem_paid_full
mem_payment_plan
mem_payment_failed
mem_access_paused
hwn_monthly
hwn_annual
hwn_payment_failed
```

### Lifecycle Tags
```
hwn_engaged
hwn_at_risk
hwn_power_user
hwn_cancel_requested
hwn_churned
hwn_converted_from_mem
hwn_returning_member
```

### Custom Fields (Contact Record)
```
uha_result_type          (dropdown: estrogen_dominant, balanced)
mem_payment_type         (dropdown: full, 3x)
hwn_subscription_type    (dropdown: monthly, annual)
hwn_bonus_expiry_date    (date field)
last_kajabi_login        (date field — updated via webhook)
hwn_engagement_score     (number: 0-5, updated monthly by automation)
hwn_churn_date           (date field)
hwn_cancel_reason        (dropdown: too_expensive, no_time, no_value, got_what_needed, other)
```

---

## PHASE 2: KAJABI INTEGRATION

### Enrollment Triggers (GHL → Kajabi)
Set up these automations to fire on purchase:

| Trigger | Kajabi Action |
|---------|--------------|
| Tag `purchased_challenge` added | Enroll in Challenge course |
| Tag `purchased_mem` added | Enroll in MEM course + Empowered Sister Community |
| Tag `purchased_mem` added | Enroll in HWN membership (bonus access) |
| Tag `purchased_hwn` added | Enroll in HWN membership + HWN community |
| Tag `mem_access_paused` added | Revoke MEM course access (keep community 7 days) |
| Tag `hwn_churned` added | Revoke HWN access |

### Kajabi → GHL Webhooks (if available)
Set up inbound webhooks to track engagement:

| Kajabi Event | GHL Action |
|-------------|------------|
| User first login | Update `last_kajabi_login` field |
| Module completed | Update engagement tracking (optional Phase 2 enhancement) |

### Kajabi Password Logic
- On `purchased_challenge` OR `purchased_mem` OR `purchased_hwn`:
  - Check: does contact have tag `kajabi_account_created`?
  - IF NO: Kajabi creates account + sends invite email. GHL applies `kajabi_account_created` tag. GHL email references Kajabi invite email with description of what it looks like.
  - IF YES: GHL email says "log in with your existing account" + direct Kajabi link. No Kajabi invite sent.

Manual rescue exists only as an exception path through the support inbox. It is not part of the normal launch fulfillment path.

---

## PHASE 3: UHA WORKFLOW

### Workflow: `UHA — Post-Purchase`

**Trigger:** Tag `purchased_uha` added

```
Step 1: Apply tags
    → customer
    → purchased_uha

Step 2: Send Email — "UHA Backup Confirmation"
    Delay: none (immediate)
    Subject: "Your assessment link (in case you need it)"
    Content: quiz link, short receipt, "if you already started on
             the confirmation page, ignore this"

Step 3: Wait 4 hours

Step 4: IF/ELSE — Check tag uha_completed
    → IF has tag: STOP (she completed the quiz, results email fires
      from separate workflow)
    → IF NOT:
        Send Email — "Quiz Nudge 1"
        Subject: "Your assessment is waiting for you"

Step 5: Wait until Day 2, 9am

Step 6: IF/ELSE — Check tag uha_completed
    → IF has tag: Go to Step 8
    → IF NOT:
        Send Email — "Quiz Nudge 2"
        Subject: "Still curious about your hormones?"

Step 7: Wait until Day 4, 9am
    → IF/ELSE — Check tag uha_completed
        → IF NOT: Apply tag uha_quiz_abandoned → END workflow
        → IF YES: Continue

Step 8: Wait until Day 3 (from purchase), 9am
    [Only reached by quiz completers]

Step 9: Send Email — "The Now-What Email"
    Subject: Conditional on uha_result_type
    - estrogen_dominant: "So now you know — here's what to do about it"
    - balanced: "So now you know — here's what to do about it"
    Content: educational bridge, soft CTA to Challenge at bottom

Step 10: Wait until Day 6, 9am

Step 11: IF/ELSE — Check tag purchased_challenge
    → IF has tag: END (already bought Challenge)
    → IF NOT:
        Send Email — "Ascension Bridge"
        Subject: "Can I be honest with you about something?"

Step 12: Wait until Day 10, 9am

Step 13: IF/ELSE — Check tag purchased_challenge
    → IF has tag: END
    → IF NOT:
        Send Email — "Final Touch"
        Subject: "One more thing about your results"
        → After send: END workflow. Contact goes to general nurture.
```

### Workflow: `UHA — Quiz Results`

**Trigger:** Inbound webhook from quiz platform (quiz completed)

```
Step 1: Apply tag uha_completed

Step 2: IF/ELSE — Check quiz result data from webhook
    → Normalize Interact result values in GHL:
      dominant → estrogen_dominant
      balanced → balanced
    → Set custom field uha_result_type = estrogen_dominant OR balanced
    → Apply tag uha_result_estrogen_dominant OR uha_result_balanced

Step 3: Send Email — "Your Hormone Report"
    Delay: none (immediate)
    Subject: "[First Name], your hormone results"
    Content: conditional on uha_result_type
    - estrogen_dominant version: result explanation, 3 factors, 3 action items
    - balanced version: result explanation, 3 strengths, 3 optimization moves
    NO upsell. Pure value.
```

---

## PHASE 4: CHALLENGE WORKFLOW

### Workflow: `Challenge — Post-Purchase`

**Trigger:** Tag `purchased_challenge` added

```
Step 1: Apply tags
    → customer
    → purchased_challenge

Step 2: Kajabi enrollment trigger fires (separate automation)

Step 3: Kajabi password conditional (check kajabi_account_created)
    → IF new: apply kajabi_account_created tag

Step 4: Send Email — "Challenge Welcome"
    Delay: none (immediate)
    Subject: "Your Challenge starts now — here's your login"
    Content: conditional on kajabi_account_created (new vs returning user)
    Includes: Day 1 overview, bonus list, reply prompt

Step 5: Wait until Day 2, 8am

Step 6: THROTTLE CHECK — was another email sent today?
    → IF yes: push to next available day
    → IF no: continue

Step 7: Send Email — "Day 2 Check-In"
    Subject: "Did you finish Day 1? (Be honest)"

Step 8: Wait until Day 4, 8am

Step 9: IF/ELSE — Check last_kajabi_login field
    → IF logged in since purchase:
        Send Email — "Midpoint Momentum (Active)"
        Subject: "You're almost halfway — don't stop now"
    → IF NOT logged in:
        Send Email — "Midpoint Momentum (Inactive)"
        Subject: "Hey [First Name] — you haven't logged in yet"
        Content: re-engagement version

Step 10: Wait until Day 7, 8am

Step 11: Send Email — "Final Day"
    Subject: "LAST DAY. Let's bring it home."

Step 12: Wait until Day 8, 9am

Step 13: Send Email — "Celebration"
    Subject: "7 days. Look at what you just did."
    Content: pure celebration, reply prompt, NO upsell

Step 14: Wait until Day 11, 9am

--- ASCENSION BRIDGE BEGINS ---

Step 15: IF/ELSE — Check tag purchased_mem
    → IF has tag: END workflow
    → IF NOT: continue

Step 16: Send Email — "The Gap Email"
    Subject: "The truth about 7-day challenges"
    Content: seed-planting, no CTA

Step 17: Wait until Day 14, 9am

Step 18: THROTTLE CHECK

Step 19: Send Email — "The Proof Email"
    Subject: "She started exactly where you are"
    Content: MEM testimonial, name-drop only, no link

Step 20: Wait until Day 17, 9am

Step 21: IF/ELSE — Check tag purchased_mem
    → IF has tag: END
    → IF NOT:
        Send Email — "The Full Picture"
        Subject: "What 12 weeks with me actually looks like"
        Content: MEM details, payment plan options, CTA to checkout

Step 22: Wait until Day 20, 9am

Step 23: IF/ELSE — Check tag purchased_mem
    → IF has tag: END
    → IF NOT:
        Send Email — "Objection Buster"
        Subject: "The 3 things women ask me before they join"
        Content: FAQ, final CTA
        → After send: END workflow. No more MEM pitches for 60 days.
```

---

## PHASE 5: MEM WORKFLOW + DUNNING

### Workflow: `MEM — Post-Purchase`

**Trigger:** Tag `purchased_mem` added

```
Step 1: Apply tags
    → customer, purchased_mem, high_value_customer
    → mem_paid_full OR mem_payment_plan (based on checkout data)

Step 2: Kajabi enrollment trigger fires (MEM course + community + HWN bonus)

Step 3: Apply tags
    → hwn_bonus_member
    → Set custom field hwn_bonus_expiry_date = purchase date + 90 days

Step 4: Kajabi password conditional

Step 5: Send Email — "MEM Welcome"
    Delay: none (immediate)
    Subject: "You're in the Mastermind. Here's everything you need."
    Content: conditional on kajabi_account_created
    Includes: course link, community link, generic weekly accountability-call reference, payment schedule if applicable

Step 6: Wait until Day 2, 9am

Step 7: Send Email — "How This Works"
    Subject: "Here's how to get the most out of the next 12 weeks"
    Content: weekly rhythm, community intro prompt

Step 8: Wait until Day 4, 9am

Step 9: Send Email — "Week 1 Accountability"
    Subject: "Have you started Week 1?"

--- WEEKLY MODULE PHASE (Weeks 2-4: active) ---

Step 10: Wait until Week 2 Monday, 8am
    Send Email — "Week 2: Nutrition"

Step 11: Wait until Week 3 Monday, 8am
    Send Email — "Week 3: Movement"

Step 12: Wait until Week 4 Monday, 8am
    Send Email — "Week 4: Hormones Deep Dive"
    Content includes: "1 month in" milestone acknowledgment

--- MILESTONE PHASE (Weeks 5-8: midpoint only) ---

Step 13: Wait until Week 6 Monday, 8am
    Send Email — "Midpoint Milestone"
    Subject: "6 weeks. Halfway. Let's talk about what's changed."

--- FINISH PHASE (Weeks 9-12: re-engage) ---

Step 14: Wait until Week 9 Monday, 8am
    Send Email — "Final Stretch"
    Subject: "4 weeks left. Let's finish this the right way."

Step 15: Wait until Week 12 Monday, 8am
    Send Email — "Final Module"
    Subject: "Your last module is live. And I have something to say."

--- GRADUATION ---

Step 16: Wait 3 days after Week 12 Monday

Step 17: Send Email — "Graduation"
    Subject: "12 weeks. You did it."
    Content: pure celebration, testimonial request, ZERO upsell

--- HWN TRANSITION ---

Step 18: Wait 5 days after graduation email

Step 19: Send Email — "What Now"
    Subject: "So... what now?"
    Content: reintroduce HWN, $47/mo, soft CTA

Step 20: Calculate: hwn_bonus_expiry_date - 15 days
    Wait until that date, 9am

Step 21: IF/ELSE — Check tag purchased_hwn
    → IF has tag: END
    → IF NOT:
        Send Email — "HWN Reminder 1"
        Subject: "Your HWN bonus is ending soon"

Step 22: Wait until hwn_bonus_expiry_date - 8 days, 9am

Step 23: IF/ELSE — Check tag purchased_hwn
    → IF has tag: END
    → IF NOT:
        Send Email — "HWN Reminder 2"
        Subject: "A quick reminder about your HWN access"

Step 24: Wait until hwn_bonus_expiry_date - 2 days, 9am

Step 25: IF/ELSE — Check tag purchased_hwn
    → IF has tag: END
    → IF NOT:
        Send Email — "HWN Conversion Invitation"
        Subject: "Keep your HWN access going"

Step 26: Wait until hwn_bonus_expiry_date

Step 27: IF/ELSE — Check tag purchased_hwn
    → IF has tag: END (converted — do nothing)
    → IF NOT:
        Remove tag: hwn_bonus_member
        → Trigger Kajabi HWN access revocation
        → END workflow
```

### Workflow: `MEM — Payment Dunning`

**Trigger:** GHL payment failed event for MEM product

```
Step 1: Apply tag mem_payment_failed

Step 2: Internal notification → Dr. P team (email or Slack)

Step 3: Wait 2 hours

Step 4: Send Email — "Dunning 1"
    Subject: "Quick heads up about your Mastermind payment"
    Content: friendly, update payment link

Step 5: Wait 3 days

Step 6: IF/ELSE — Check tag mem_payment_failed (still present?)
    → IF removed (payment recovered): END
    → IF still present:
        Send Email — "Dunning 2"
        Subject: "Following up on your payment — need a hand?"

Step 7: Wait 3 more days (Day 6 total)

Step 8: IF/ELSE — Check tag mem_payment_failed
    → IF removed: END
    → IF still present:
        Send Email — "Dunning 3"
        Subject: "Last step to keep your Mastermind access"

Step 9: Wait 4 more days (Day 10 total)

Step 10: IF/ELSE — Check tag mem_payment_failed
    → IF removed: END
    → IF still present:
        Apply tag: mem_access_paused
        → Trigger Kajabi MEM course access revocation (keep community)
        → Internal notification for personal outreach

Step 11: Wait 7 more days (Day 17 total)

Step 12: IF still not resolved:
    → Revoke community access
    → END

--- RECOVERY (separate trigger) ---
Trigger: Payment recovered / tag mem_payment_failed removed
    → Remove mem_access_paused
    → Restore Kajabi access
    → Send Email: "You're all set — your access is back"
```

---

## PHASE 6: HWN WORKFLOW + RETENTION + WIN-BACK

Launch note:
- HWN should launch as an evergreen, on-demand membership
- Do not make launch automation depend on event dates, calendar updates, replay attendance, or SMS
- Event-driven reminders can be added post-launch

### Workflow: `HWN — Post-Purchase`

**Trigger:** Tag `purchased_hwn` added
**Exclusion:** Do NOT trigger if `hwn_bonus_member` is present (MEM buyers get MEM onboarding, not HWN)

```
Step 1: Apply tags
    → customer, purchased_hwn
    → hwn_monthly OR hwn_annual
    → IF previously hwn_churned: apply hwn_returning_member, remove hwn_churned

Step 2: Kajabi enrollment

Step 3: Kajabi password conditional

Step 4: IF/ELSE — Check tag hwn_returning_member
    → IF returning:
        Send Email — "Welcome Back"
        Subject: "Good to have you back, [First Name]"
        Content: this month's digest, skip full onboarding
        → END onboarding sequence (she knows how it works)
    → IF new member: continue

Step 5: Send Email — "HWN Welcome"
    Delay: none (immediate)
    Subject: "Welcome to the Network, [First Name]"
    Content: access instructions, community link, evergreen orientation

Step 6: Wait until Day 3, 9am

Step 7: Send Email — "The Rhythm"
    Subject: "Here's how this works (it's simpler than you think)"
    Content: conditional — if no Kajabi login detected, add help offer
    → END onboarding
```

### Workflow: `HWN — Monthly Value Cycle`

**Trigger:** evergreen recurring schedule
**Audience:** active paid members and bonus members where appropriate

```
Step 1: Send Email — "Start-of-Month Orientation"
    Subject: "Here's how to use the Network this month"
    Content: evergreen guidance, community prompt, where to start

Step 2: Wait ~14 days

Step 3: Send Email — "Mid-Month Engagement Reminder"
    Subject: "A quick nudge to use what you joined for"
    Content: evergreen encouragement, one clear action, support CTA

Step 4: Wait until end of month window

Step 5: Send Email — "End-of-Month Preview"
    Subject: "Here’s your next step inside the Network"
    Content: forward-looking value framing without fixed event dates
```

### Workflow: `HWN — Engagement Scoring`

**Trigger:** Runs monthly (1st of month, after digest sends)
**Audience:** All `purchased_hwn` contacts

```
Step 1: Evaluate engagement signals from last 30 days:
    - Logged into Kajabi (last_kajabi_login field)
    - Posted in community (if trackable)
    - Opened/clicked HWN emails (GHL tracking)
    - Any tracked evergreen engagement signal available in GHL/Kajabi

Step 2: Score:
    - 2+ signals → Apply tag hwn_engaged, remove hwn_at_risk
    - 0-1 signals → Apply tag hwn_at_risk, remove hwn_engaged
    - All events attended + community active → Apply hwn_power_user

Step 3: IF hwn_at_risk AND no re-engagement email sent in last 60 days:
    Send Email — "Re-Engagement"
    Subject: "Haven't seen you lately — everything okay?"
    Content: personal check-in with one clear evergreen next step

Step 4: IF hwn_at_risk persists for 14 days after email:
    → Internal flag for personal outreach by Dr. P team
```

### Workflow: `HWN — Payment Dunning`

**Trigger:** GHL subscription payment failed for HWN

```
Step 1: Apply tag hwn_payment_failed

Step 2: Wait 2 hours
    Send Email — "Dunning 1"
    Subject: "Quick note about your Network membership"

Step 3: Wait 3 days
    IF still failed:
        Send Email — "Dunning 2"
        Subject: "Still need to update your payment method"

Step 4: Wait 3 days (Day 6)
    IF still failed:
        Send Email — "Dunning 3"
        Subject: "Your Network access needs attention"

Step 5: Wait 4 days (Day 10)
    IF still failed:
        Apply tag: hwn_churned
        Remove tag: purchased_hwn
        → Revoke Kajabi access
        → Internal notification
        → Trigger Win-Back workflow

--- RECOVERY ---
Trigger: Payment recovered
    → Remove hwn_payment_failed
    → Restore access
    → Send recovery confirmation email
```

### Workflow: `HWN — Cancellation`

**Trigger:** Subscription cancelled in GHL

```
Step 1: Apply tag hwn_cancel_requested

Step 2: Internal alert to Dr. P team

Step 3: Send Email — "Cancellation Confirmed"
    Subject: "Your membership cancellation"
    Content: access end date, exit survey link

Step 4: Wait until end of billing period

Step 5: Apply tag: hwn_churned
    Remove tag: purchased_hwn
    Set custom field: hwn_churn_date = today
    → Revoke Kajabi access
    → Trigger Win-Back workflow
```

### Workflow: `HWN — Win-Back`

**Trigger:** Tag `hwn_churned` added (from dunning or cancellation)

```
Step 1: Wait 14 days

Step 2: Send Email — "Win-Back 1: The Update"
    Subject: "Here's what's been happening in the Network"

Step 3: Wait 16 days (Day 30 post-churn)

Step 4: IF/ELSE — Check tag purchased_hwn
    → IF has tag: END (re-subscribed)
    → IF NOT:
        Send Email — "Win-Back 2: The Personal Note"
        Subject: "Can I ask you something?"
        Content: conditional on hwn_cancel_reason field
        IF "too_expensive" → offer annual plan ($470/yr = $39/mo)

Step 5: Wait 15 days (Day 45)

Step 6: IF/ELSE — Check tag purchased_hwn
    → IF has tag: END
    → IF NOT:
        Send Email — "Win-Back 3: Social Proof"
        Subject: "What [member name] said about coming back"

Step 7: Wait 15 days (Day 60)

Step 8: IF/ELSE — Check tag purchased_hwn
    → IF has tag: END
    → IF NOT:
        Send Email — "Win-Back 4: Final Touch"
        Subject: "One last thing from me"
        → After send: END. Contact moves to general nurture.
        → No more HWN-specific emails.
```

---

## PHASE 7: CROSS-FLOW THROTTLE LOGIC

### Email Throttle Workflow

**Trigger:** Before every non-transactional email send across ALL workflows

**Implementation option 1 (preferred):** Use GHL's "wait until no email sent today" condition if available.

**Implementation option 2:** Custom field `last_email_sent_date` (date field)
- Before each non-transactional email: check if `last_email_sent_date` = today
  - IF yes: push email to next day at same time
  - IF no: send email, update `last_email_sent_date` to today
- Transactional emails (purchase confirmations, dunning) ALWAYS send regardless

### Bump Offer Coordination

**When a bump offer is accepted at checkout:**

The primary product workflow starts immediately. The secondary product workflow is modified:

| Primary Purchase | Bump Offer | Bump Flow Modification |
|-----------------|------------|----------------------|
| Challenge | UHA | UHA flow starts Day 2. UHA confirmation email → replaced with "Your assessment is also ready" email. Quiz link included. |
| UHA | Challenge | Challenge flow starts Day 2. Challenge confirmation → "Your Challenge is also ready" with Kajabi setup. |
| MEM | UHA | UHA flow starts Day 3 (MEM onboarding takes priority Days 1-2). UHA confirmation → folded into a "by the way, your assessment is ready too" email. |

**Implementation:** On bump acceptance, apply the secondary product tag + a `bump_delay_[product]` tag. The secondary workflow checks for this tag at entry and adds a 24-48h wait before starting.

---

## PHASE 8: CONFIRMATION PAGES

Build 4 custom confirmation/thank-you pages in GHL:

### Page 1: UHA Confirmation
- Redirect target: quiz URL (auto-redirect after 3 seconds, or embed quiz)
- Fallback: quiz link button if redirect fails
- Receipt summary
- "We also sent a backup link to your email"
- IF bump accepted: "Your Challenge is ready too — we'll send access tomorrow"

### Page 2: Challenge Confirmation
- Conditional content (show/hide based on `kajabi_account_created` tag):
  - New user: Kajabi password setup steps with visual screenshots
  - Returning user: direct login link + "Day 1 is live"
- Bonus preview
- "We also sent this to your email"
- IF bump accepted: "Your Hormone Assessment is ready too — check tomorrow's email"

### Page 3: MEM Confirmation
- Premium design (this is a $2K purchase — make it feel like it)
- Conditional Kajabi setup instructions
- Community join link
- First accountability call date + calendar add
- 12-week visual timeline
- HWN bonus mention (brief)
- IF bump accepted: "Your Hormone Assessment is included too — we'll send it in a few days"

### Page 4: HWN Confirmation
- Community-first welcome
- Conditional Kajabi setup
- Upcoming events with calendar links
- Community highlight/recent member win
- "Post your intro in the community"

---

## PHASE 9: TESTING CHECKLIST

Test every flow end-to-end with test contacts before going live.

### Per-Flow Tests:
- [ ] Purchase triggers correct tags
- [ ] Kajabi enrollment fires correctly (new user)
- [ ] Kajabi enrollment fires correctly (returning user)
- [ ] Confirmation page displays correct conditional content
- [ ] Email 1 sends immediately with correct conditional content
- [ ] All subsequent emails fire at correct times
- [ ] Conditional branches work (engagement checks, tag checks)
- [ ] Ascension emails skip correctly when product already purchased
- [ ] Dunning sequence fires on payment failure
- [ ] Dunning sequence stops on payment recovery
- [ ] Access revocation works when triggered
- [ ] Access restoration works on payment recovery

### Cross-Flow Tests:
- [ ] Bump offer: primary + secondary flows run without collision
- [ ] Email throttle: max 1/day enforced across overlapping flows
- [ ] MEM buyer does NOT get HWN welcome flow (gets MEM onboarding instead)
- [ ] HWN returning member gets welcome-back email, not full onboarding
- [ ] Contact who buys all 4 products gets clean experience with no duplicate emails

### Edge Cases:
- [ ] Contact buys UHA, never takes quiz → gets abandoned tag at Day 4, no more emails
- [ ] Contact buys Challenge, never logs in → gets inactive version of Day 4 email
- [ ] MEM payment fails, recovers at Day 8 → access never revoked, dunning stops
- [ ] MEM payment fails, not recovered by Day 10 → course revoked, community stays 7 more days
- [ ] HWN member cancels mid-month → access continues through billing period end
- [ ] HWN member churns, re-subscribes at Day 20 → win-back stops, gets welcome-back email

---

## EMAIL TEMPLATES NEEDED

Total unique email templates to create:

| Flow | Count | Templates |
|------|-------|-----------|
| UHA | 6 | Backup confirmation, Results (2 versions), Quiz nudge 1, Quiz nudge 2, Now-What, Ascension bridge, Final touch |
| Challenge | 9 | Welcome, Day 2 check-in, Midpoint active, Midpoint inactive, Final day, Celebration, Gap, Proof, Full picture, Objections |
| MEM | 16 | Welcome, How this works, Week 1 accountability, Weeks 2-4 (3), Midpoint, Final stretch, Final module, Graduation, What now, HWN expiry, HWN final, Dunning 1-3, Recovery |
| HWN | 14 | Welcome, Welcome back (returning), The Rhythm, Monthly digest (template), Day-of reminder (template), Replay, Re-engagement, Dunning 1-3, Cancellation, Win-back 1-4, Recovery |
| **TOTAL** | **~45** | Unique templates across all flows |

NOTE: Several templates have conditional content (2 versions in 1 template):
- UHA results: estrogen_dominant vs. balanced
- Kajabi setup: new user vs. returning user
- Challenge Day 4: active vs. inactive
- HWN Rhythm: logged in vs. not logged in
- Win-back 2: conditional on cancel reason

---

## NOTES FOR BUILDER

1. **Workflow naming convention:** Use `[Product] — [Purpose]` format (e.g., "MEM — Post-Purchase", "HWN — Win-Back")

2. **Email naming convention:** Use `[Product] — [Sequence #] — [Short Name]` (e.g., "Challenge — 05 — Celebration")

3. **Time zones:** All scheduled sends should use contact timezone if available in GHL. Fallback: EST.

4. **From name:** "Dr. P" or "Dr. Kerry-Anne Perkins" — consistent across all emails. From email: TBD (confirm with client).

5. **Reply handling:** Several emails ask for replies ("tell me your #1 goal", "what's changed"). These replies should create a GHL conversation visible to Dr. P's team for personal follow-up.

6. **Internal notifications:** Use GHL internal notifications or Slack webhook for:
   - MEM payment failures (immediate)
   - HWN cancellation requests (immediate)
   - HWN at-risk members after 14 days with no re-engagement (daily digest)

7. **Monthly maintenance:** Launch HWN automation should remain evergreen and should not depend on manual event-date updates. Calendar-driven live-event logic can be added later as a post-launch enhancement.
