# Dr. P — Detailed Visual Flow
### Every touchpoint labeled with exact location, channel, and medium

---

## CHANNEL KEY

Every step below is tagged with where it lives:

| Icon | Channel | Platform | Notes |
|------|---------|----------|-------|
| `[CHECKOUT PAGE]` | Web page | GHL funnel page | Customer-facing order form |
| `[CONFIRMATION PAGE]` | Web page | GHL funnel page | Post-purchase thank-you page |
| `[RESULTS PAGE]` | Web page | Quiz platform or standalone landing page | UHA-specific |
| `[LANDING PAGE]` | Web page | GHL or standalone | Estrogen dominant / balanced results pages |
| `[EMAIL]` | Email | GHL email workflow | Sent from Dr. P's email via GHL |
| `[KAJABI COURSE]` | Course platform | Kajabi | Module delivery, drip content |
| `[KAJABI COMMUNITY]` | Community | Kajabi community | Empowered Sister Community / HWN community |
| `[QUIZ]` | Interactive quiz | Quiz platform (embedded or standalone) | UHA 48-question assessment |
| `[SMS]` | Text message | GHL SMS | Opt-in only, live event reminders |
| `[GHL BACKEND]` | Automation | GHL workflow engine | Tags, webhooks, delays — invisible to customer |
| `[CALENDAR]` | Calendar event | Google/Apple/Outlook via .ics link | Add-to-calendar for live events |
| `[FORM]` | Web form | GHL form or Typeform | Exit surveys, testimonial requests |
| `[INTERNAL]` | Team notification | GHL notification / Slack / email | Dr. P's team sees this, not the customer |

---

# FLOW 1: UHA ($47) — EVERY TOUCHPOINT

```
STEP    CHANNEL                  WHAT HAPPENS                              WHO SEES IT
────    ───────                  ────────────                              ──────────

1       [CHECKOUT PAGE]          GHL order form: UHA $47                   Customer
        GHL Funnel               - Name, email, payment info
                                 - Bump offer: 7-Day Challenge $47
                                 - "Add the 7-Day Challenge for $47"
                                   checkbox below payment button
                                 URL: callmedoctorp.com/uha-checkout
                                 (or GHL hosted funnel URL)

2       [GHL BACKEND]            Payment processes                         Nobody
        GHL Workflow             - Apply tags: purchased_uha, customer
                                 - IF bump: purchased_challenge
                                 - Create/update GHL contact record
                                 - Trigger Workflow: "UHA — Post-Purchase"

3       [CONFIRMATION PAGE]      Thank-you page with embedded quiz         Customer
        GHL Funnel Page          start OR auto-redirect to quiz
        URL: /uha-confirmed
                                 PAGE CONTENT:
                                 ┌────────────────────────────────────┐
                                 │ "Payment confirmed! Let's find     │
                                 │  out what your hormones are        │
                                 │  telling you."                     │
                                 │                                    │
                                 │  [START YOUR ASSESSMENT]  ← button │
                                 │  (links to quiz URL or quiz is     │
                                 │   embedded directly on this page)  │
                                 │                                    │
                                 │  "Takes about 10 minutes. Your     │
                                 │   personalized results appear      │
                                 │   immediately after."              │
                                 │                                    │
                                 │  ───────────────────────           │
                                 │  "We also sent a backup link to    │
                                 │   your email in case you need it   │
                                 │   later."                          │
                                 │                                    │
                                 │  IF BUMP ACCEPTED:                 │
                                 │  ───────────────────────           │
                                 │  "Your 7-Day Challenge is ready    │
                                 │   too — we'll send access          │
                                 │   tomorrow so you can focus on     │
                                 │   your assessment first."          │
                                 └────────────────────────────────────┘

4       [QUIZ]                   48-question hormone assessment            Customer
        Quiz Platform            URL: quiz platform hosted
        (standalone or           (e.g., Typeform, ScoreApp, or
         embedded on             custom quiz tool)
         confirmation page)
                                 - Customer answers 48 questions
                                 - On submit: quiz platform sends
                                   webhook to GHL with result data

5       [GHL BACKEND]            Quiz completion webhook received          Nobody
        GHL Workflow             - Apply tag: uha_completed
                                 - Set custom field: uha_result_type
                                 - Apply tag: uha_result_estrogen_dominant
                                   OR uha_result_balanced
                                 - Trigger Workflow: "UHA — Quiz Results"

6       [RESULTS PAGE]           Immediate on-screen results               Customer
        Quiz Platform or         (displayed right after quiz submit)
        Standalone Landing
        Page                     PAGE CONTENT (Estrogen Dominant):
        URL: /uha-results-ed     ┌────────────────────────────────────┐
        OR /uha-results-bal      │ "Your Results: Estrogen Dominant"  │
                                 │                                    │
                                 │ What this means:                   │
                                 │ [Plain-language explanation]        │
                                 │                                    │
                                 │ Your top 3 contributing factors:   │
                                 │ 1. [Based on quiz answers]         │
                                 │ 2. [Based on quiz answers]         │
                                 │ 3. [Based on quiz answers]         │
                                 │                                    │
                                 │ 3 things you can do THIS WEEK:     │
                                 │ 1. [Actionable step]               │
                                 │ 2. [Actionable step]               │
                                 │ 3. [Actionable step]               │
                                 │                                    │
                                 │ [Visual: hormone balance scale]    │
                                 │                                    │
                                 │ "Your full report is being sent    │
                                 │  to your email right now."         │
                                 │                                    │
                                 │ ─────────────────────              │
                                 │ "Women with your profile see the   │
                                 │  biggest shifts in the 7-Day       │
                                 │  Challenge"                        │
                                 │  [Learn more] ← text link to      │
                                 │  Challenge sales page              │
                                 └────────────────────────────────────┘

                                 PAGE CONTENT (Balanced):
                                 ┌────────────────────────────────────┐
                                 │ "Your Results: Hormonally          │
                                 │  Balanced"                         │
                                 │                                    │
                                 │ What this means:                   │
                                 │ [Explanation + why it's not        │
                                 │  "mission accomplished"]           │
                                 │                                    │
                                 │ Your top 3 strengths to maintain:  │
                                 │ 1. [Based on quiz answers]         │
                                 │ 2. [Based on quiz answers]         │
                                 │ 3. [Based on quiz answers]         │
                                 │                                    │
                                 │ 3 optimization moves:              │
                                 │ 1. [Actionable step]               │
                                 │ 2. [Actionable step]               │
                                 │ 3. [Actionable step]               │
                                 │                                    │
                                 │ [Visual: hormone balance scale]    │
                                 │                                    │
                                 │ "Your full report is being sent    │
                                 │  to your email right now."         │
                                 │                                    │
                                 │ ─────────────────────              │
                                 │ "Want to optimize even further?    │
                                 │  The 7-Day Challenge locks this    │
                                 │  in."                              │
                                 │  [Learn more] ← text link         │
                                 └────────────────────────────────────┘

7       [EMAIL]                  Email UHA-1: Backup Confirmation          Customer inbox
        GHL Workflow             Trigger: immediate on purchase
        Sent: immediately        (See email-copy-uha-challenge.md
                                  for full copy)

8       [EMAIL]                  Email UHA-2: Hormone Report               Customer inbox
        GHL Workflow             Trigger: on quiz completion
        Sent: on quiz            (keepsake version of results)
        completion               Conditional: estrogen_dominant OR
                                 balanced version

        ════════════════════════════════════════════════════════
        IF QUIZ NOT COMPLETED — NUDGE PATH:
        ════════════════════════════════════════════════════════

9       [GHL BACKEND]            Wait 4 hours, check tag                   Nobody
        GHL Workflow             uha_completed

10      [EMAIL]                  Email UHA-3: Quiz Nudge 1                 Customer inbox
        GHL Workflow             Trigger: 4 hrs post-purchase,
        Sent: +4 hours           only if uha_completed tag absent
        (conditional)

11      [EMAIL]                  Email UHA-3b: Quiz Nudge 2                Customer inbox
        GHL Workflow             Trigger: Day 2, 9am,
        Sent: Day 2, 9am        only if still no uha_completed
        (conditional)

12      [GHL BACKEND]            Day 4: if still no quiz completion,       Nobody
        GHL Workflow             apply tag uha_quiz_abandoned.
                                 END workflow. Contact → general nurture.

        ════════════════════════════════════════════════════════
        QUIZ COMPLETERS — ASCENSION PATH:
        ════════════════════════════════════════════════════════

13      [EMAIL]                  Email UHA-4: "The Now-What Email"         Customer inbox
        GHL Workflow             Trigger: Day 3, 9am
        Sent: Day 3, 9am        Educational bridge, soft CTA to
                                 Challenge at bottom (text link)
                                 Conditional on result type

14      [EMAIL]                  Email UHA-5: Ascension Bridge             Customer inbox
        GHL Workflow             Trigger: Day 6, 9am
        Sent: Day 6, 9am        Dr. P voice, testimonial
        (conditional)            CTA → Challenge checkout page
                                 SKIP if purchased_challenge tag exists

        [CHECKOUT PAGE]          CTA links to: Challenge checkout page     Customer
        GHL Funnel               (same as Flow 2, Step 1)
        URL: /challenge-checkout

15      [EMAIL]                  Email UHA-6: Final Touch                  Customer inbox
        GHL Workflow             Trigger: Day 10, 9am
        Sent: Day 10, 9am       New angle, social proof
        (conditional)            CTA → Challenge checkout page
                                 SKIP if purchased_challenge
                                 After this: END. → General nurture.

────────────────────────────────────────────────────────────────────

UHA PAGES/ASSETS NEEDED:
  1. [CHECKOUT PAGE] UHA order form with Challenge bump offer
  2. [CONFIRMATION PAGE] with quiz embed/redirect
  3. [RESULTS PAGE] Estrogen Dominant version
  4. [RESULTS PAGE] Balanced version
  5. [QUIZ] 48-question assessment (quiz platform)
  6. [EMAILS] 6 email templates (see email copy doc)

────────────────────────────────────────────────────────────────────
```

---

# FLOW 2: CHALLENGE ($47) — EVERY TOUCHPOINT

```
STEP    CHANNEL                  WHAT HAPPENS                              WHO SEES IT
────    ───────                  ────────────                              ──────────

1       [CHECKOUT PAGE]          GHL order form: 7-Day Challenge $47       Customer
        GHL Funnel
        URL: /challenge-checkout
                                 - Name, email, payment info
                                 - Bump offer: UHA $47
                                 - "Add the Hormone Assessment for $47"

2       [GHL BACKEND]            Payment processes                         Nobody
        GHL Workflow             - Apply tags: purchased_challenge, customer
                                 - IF bump: purchased_uha
                                 - Check kajabi_account_created tag
                                 - IF new: apply kajabi_account_created
                                 - Trigger Kajabi enrollment webhook
                                 - Trigger Workflow: "Challenge — Post-Purchase"

3       [GHL BACKEND →           Kajabi receives enrollment webhook         Nobody
         KAJABI COURSE]          - Creates Kajabi account (if new user)
        Webhook/API              - Enrolls in Challenge course
                                 - Day 1 unlocked, Days 2-7 dripped
                                 - Kajabi sends password setup email
                                   (new users only)

4       [CONFIRMATION PAGE]      Post-purchase thank-you page              Customer
        GHL Funnel Page
        URL: /challenge-confirmed
                                 PAGE CONTENT:
                                 ┌────────────────────────────────────┐
                                 │ "You're in the Challenge!"         │
                                 │                                    │
                                 │ IF NEW KAJABI USER:                │
                                 │ ┌──────────────────────────────┐   │
                                 │ │ Step 1: Check your email for │   │
                                 │ │ a login message from Kajabi  │   │
                                 │ │ (it looks like this):        │   │
                                 │ │                              │   │
                                 │ │ [SCREENSHOT of Kajabi invite │   │
                                 │ │  email — subject line,       │   │
                                 │ │  sender name, what it looks  │   │
                                 │ │  like in inbox]              │   │
                                 │ │                              │   │
                                 │ │ Step 2: Click the link in    │   │
                                 │ │ that email to set your       │   │
                                 │ │ password                     │   │
                                 │ │                              │   │
                                 │ │ Step 3: Log in and start     │   │
                                 │ │ Day 1 → [LINK TO COURSE]    │   │
                                 │ │                              │   │
                                 │ │ Don't see it? Check spam.    │   │
                                 │ │ Still nothing after 5 min?   │   │
                                 │ │ Email support@callmedoctorp  │   │
                                 │ │ .com                         │   │
                                 │ └──────────────────────────────┘   │
                                 │                                    │
                                 │ IF RETURNING KAJABI USER:          │
                                 │ ┌──────────────────────────────┐   │
                                 │ │ Day 1 is live right now.     │   │
                                 │ │                              │   │
                                 │ │ [LOG IN & START DAY 1]       │   │
                                 │ │  ← button → Kajabi course    │   │
                                 │ └──────────────────────────────┘   │
                                 │                                    │
                                 │ What to expect:                    │
                                 │ "One module per day for 7 days.    │
                                 │  Each takes about 15 minutes.      │
                                 │  By Day 7, you'll feel the         │
                                 │  difference."                      │
                                 │                                    │
                                 │ Your bonuses:                      │
                                 │ ✓ Hormone-friendly meal plan       │
                                 │ ✓ Grocery shopping list            │
                                 │ ✓ Training program lite            │
                                 │ ✓ [other bonuses]                  │
                                 │ (All inside the course)            │
                                 │                                    │
                                 │ ───────────────────────            │
                                 │ "We also sent all of this to       │
                                 │  your email."                      │
                                 │                                    │
                                 │ IF UHA BUMP ACCEPTED:              │
                                 │ ───────────────────────            │
                                 │ "Your Hormone Assessment is also   │
                                 │  ready — we'll send access         │
                                 │  tomorrow so you can focus on      │
                                 │  Day 1 first."                     │
                                 └────────────────────────────────────┘

5       [EMAIL]                  Email CH-1: Welcome + Access              Customer inbox
        GHL Workflow             Trigger: immediate on purchase
        Sent: immediately        (Full copy in email-copy-uha-challenge.md)

6       [KAJABI COURSE]          Customer logs into Kajabi                 Customer
        Kajabi                   Accesses Day 1: Goal-Setting
        URL: Kajabi course URL   (inside Kajabi platform)
                                 - Video/content for Day 1
                                 - Days 2-7 locked, drip daily

7       [EMAIL]                  Email CH-2: Day 2 Check-In               Customer inbox
        GHL Workflow             "Did you finish Day 1?"
        Sent: Day 2, 8am

8       [KAJABI COURSE]          Day 2 module unlocks in Kajabi            Customer
        Kajabi (auto-drip)       Customer accesses directly in Kajabi
                                 (no email needed — they know the rhythm)

9       [KAJABI COURSE]          Day 3 module unlocks                      Customer
        Kajabi (auto-drip)

10      [EMAIL]                  Email CH-3: Midpoint Momentum             Customer inbox
        GHL Workflow             Sent: Day 4, 8am
        Sent: Day 4, 8am        TWO VERSIONS (conditional):

        [GHL BACKEND]            Check: has contact logged into Kajabi?    Nobody
                                 (via last_kajabi_login custom field)

                                 VERSION A — ACTIVE (has logged in):
                                 "You're almost halfway — don't stop"

                                 VERSION B — INACTIVE (no login):
                                 "Hey [Name] — you haven't logged in yet"
                                 Focus: get them to Day 1, not Day 4

11      [KAJABI COURSE]          Days 4-6 modules unlock in Kajabi         Customer
        Kajabi (auto-drip)       (no emails — Kajabi handles drip)

12      [EMAIL]                  Email CH-4: Final Day                     Customer inbox
        GHL Workflow             "LAST DAY. Let's bring it home."
        Sent: Day 7, 8am

13      [KAJABI COURSE]          Day 7 module unlocks: Integration         Customer
        Kajabi (auto-drip)

14      [EMAIL]                  Email CH-5: Celebration                   Customer inbox
        GHL Workflow             "7 days. Look at what you just did."
        Sent: Day 8, 9am        Pure celebration. NO upsell.
                                 Reply prompt for engagement.

        ════════════════════════════════════════════════════════
        ASCENSION BRIDGE: CHALLENGE → MEM ($47 → $1,997)
        4 emails over ~12 days. Gradual trust-building.
        ════════════════════════════════════════════════════════

15      [EMAIL]                  Email CH-6: "The Gap"                     Customer inbox
        GHL Workflow             Seed-planting. No CTA. No link.
        Sent: Day 11, 9am       Just honest Dr. P perspective.
        (conditional)            SKIP if purchased_mem tag exists

16      [EMAIL]                  Email CH-7: "The Proof"                   Customer inbox
        GHL Workflow             MEM testimonial story.
        Sent: Day 14, 9am       Name-drop "Madame Estrogen Mastermind"
        (conditional)            but NO link yet. Let her be curious.
                                 SKIP if purchased_mem

17      [EMAIL]                  Email CH-8: "The Full Picture"            Customer inbox
        GHL Workflow             Full MEM details, payment plans,
        Sent: Day 17, 9am       CTA → MEM checkout page
        (conditional)            SKIP if purchased_mem

        [CHECKOUT PAGE]          CTA links to: MEM checkout page           Customer
        GHL Funnel               (same as Flow 3, Step 1)
        URL: /mem-checkout

18      [EMAIL]                  Email CH-9: "Objection Buster"            Customer inbox
        GHL Workflow             FAQ format, final CTA
        Sent: Day 20, 9am       → MEM checkout page
        (conditional)            SKIP if purchased_mem
                                 After this: END. → General nurture.
                                 No MEM pitches for 60 days.

────────────────────────────────────────────────────────────────────

CHALLENGE PAGES/ASSETS NEEDED:
  1. [CHECKOUT PAGE] Challenge order form with UHA bump offer
  2. [CONFIRMATION PAGE] with conditional Kajabi setup (new vs returning)
     - ASSET: Screenshot of Kajabi invite email for visual reference
  3. [KAJABI COURSE] 7 modules set up with daily drip
  4. [EMAILS] 9 email templates (see email copy doc)

────────────────────────────────────────────────────────────────────
```

---

# FLOW 3: MEM ($1,997) — EVERY TOUCHPOINT

```
STEP    CHANNEL                  WHAT HAPPENS                              WHO SEES IT
────    ───────                  ────────────                              ──────────

1       [CHECKOUT PAGE]          GHL order form: MEM $1,997                Customer
        GHL Funnel
        URL: /mem-checkout
                                 - Name, email, payment info
                                 - Payment options:
                                   ○ Pay in full: $1,997
                                   ○ 3 payments of $667
                                   ○ $497 down + 10 x $150
                                 - Bump offer: UHA $47

2       [GHL BACKEND]            Payment processes                         Nobody
        GHL Workflow             - Apply tags: purchased_mem, customer,
                                   high_value_customer
                                 - Apply: mem_paid_full OR mem_payment_plan
                                 - IF bump: purchased_uha
                                 - Check kajabi_account_created
                                 - Trigger Kajabi enrollment: MEM course
                                   + Empowered Sister Community
                                 - Trigger Kajabi enrollment: HWN (bonus)
                                 - Apply: hwn_bonus_active
                                 - Set field: hwn_bonus_expiry_date
                                 - Trigger Workflow: "MEM — Post-Purchase"

3       [GHL BACKEND →           Kajabi receives enrollment webhooks        Nobody
         KAJABI COURSE]          - MEM course: Week 1 unlocked, Weeks 2-12
        Webhook/API                dripped weekly
                                 - Empowered Sister Community access
                                 - HWN membership access (bonus)
                                 - Kajabi sends password email (if new)

4       [CONFIRMATION PAGE]      Premium post-purchase page                Customer
        GHL Funnel Page          (Design should reflect $2K investment)
        URL: /mem-confirmed
                                 PAGE CONTENT:
                                 ┌────────────────────────────────────┐
                                 │ "Welcome to the Mastermind,        │
                                 │  [First Name]."                    │
                                 │                                    │
                                 │ "This is where everything          │
                                 │  changes."                         │
                                 │                                    │
                                 │ IF NEW KAJABI USER:                │
                                 │ ┌──────────────────────────────┐   │
                                 │ │ [Same Kajabi password setup  │   │
                                 │ │  instructions as Challenge    │   │
                                 │ │  with screenshot]             │   │
                                 │ └──────────────────────────────┘   │
                                 │                                    │
                                 │ IF RETURNING KAJABI USER:          │
                                 │  "Log in — Week 1 is live"         │
                                 │  [GO TO YOUR COURSE] ← button      │
                                 │                                    │
                                 │ ───────────────────────            │
                                 │ Join your community:               │
                                 │ [JOIN THE EMPOWERED SISTER         │
                                 │  COMMUNITY] ← button               │
                                 │  → Kajabi community URL            │
                                 │                                    │
                                 │ ───────────────────────            │
                                 │ Your first accountability call:    │
                                 │ [Day], [Date] at [Time]            │
                                 │ [ADD TO CALENDAR] ← .ics link      │
                                 │                                    │
                                 │ ───────────────────────            │
                                 │ Your 12-week journey:              │
                                 │                                    │
                                 │ Wk 1  Rejuvenation     ← NOW      │
                                 │ Wk 2  Nutrition                    │
                                 │ Wk 3  Movement                     │
                                 │ Wk 4  Hormones                     │
                                 │ Wk 5  Toxins                       │
                                 │ Wk 6  Gut Health      ← MIDPOINT  │
                                 │ Wk 7  Stress                       │
                                 │ Wk 8  Sleep                        │
                                 │ Wk 9  Liver                        │
                                 │ Wk 10 Supplements                  │
                                 │ Wk 11 Digestion                    │
                                 │ Wk 12 Integration     ← FINALE    │
                                 │                                    │
                                 │ ───────────────────────            │
                                 │ BONUS: You also have full access   │
                                 │ to the Hormone Wellness Network    │
                                 │ for the next 3 months — Q&As with  │
                                 │ Dr. P, monthly masterclasses, and  │
                                 │ more. We'll show you around later. │
                                 │ Right now, focus on Week 1.        │
                                 │                                    │
                                 │ ───────────────────────            │
                                 │ IF PAYMENT PLAN:                   │
                                 │ "Payment schedule: [details]"      │
                                 │                                    │
                                 │ "We sent all of this to your       │
                                 │  email too."                       │
                                 └────────────────────────────────────┘

5       [EMAIL]                  Email MEM-1: Welcome                      Customer inbox
        GHL Workflow             Trigger: immediate
        Sent: immediately

6       [KAJABI COMMUNITY]       Customer joins community                  Customer
        Kajabi                   Posts intro (prompted by email/page)
        URL: Kajabi community

7       [CALENDAR]               Customer adds first call to calendar      Customer
        .ics download            via link from confirmation page
                                 or welcome email

8       [EMAIL]                  Email MEM-2: "How This Works"             Customer inbox
        GHL Workflow             Trigger: Day 2, 9am
        Sent: Day 2, 9am        Weekly rhythm, community intro prompt

9       [KAJABI COURSE]          Customer watches Week 1: Rejuvenation     Customer
        Kajabi                   (should happen between Day 1-4)

10      [EMAIL]                  Email MEM-3: Week 1 Accountability        Customer inbox
        GHL Workflow             "Have you started Week 1?"
        Sent: Day 4, 9am

11      [KAJABI COURSE]          Week 1 accountability call (live)         Customer
        Zoom/Kajabi Live         Dr. P + team, recorded
        (link in email/page)     Replay posted to Kajabi after

        ════════════════════════════════════════════════════════
        WEEKS 2-12: MODULE DELIVERY
        ════════════════════════════════════════════════════════

        WEEK 2:
12      [KAJABI COURSE]          Week 2 module unlocks: Nutrition          Customer
        Kajabi (auto-drip)       (Monday)

13      [EMAIL]                  Email MEM-4: "Week 2: Nutrition"          Customer inbox
        GHL Workflow             Module overview + call reminder
        Sent: Wk 2 Monday, 8am

        WEEK 3:
14      [KAJABI COURSE]          Week 3 unlocks: Movement                  Customer
15      [EMAIL]                  Email MEM-5: "Week 3: Movement"           Customer inbox
        Sent: Wk 3 Monday, 8am

        WEEK 4:
16      [KAJABI COURSE]          Week 4 unlocks: Hormones Deep Dive        Customer
17      [EMAIL]                  Email MEM-6: "Week 4: Hormones"           Customer inbox
        Sent: Wk 4 Monday, 8am  + "1 month in" milestone

        WEEK 5:
18      [KAJABI COURSE]          Week 5 unlocks: Toxins                    Customer
        Kajabi (auto-drip)       NO EMAIL — habit is set

        WEEK 6:
19      [KAJABI COURSE]          Week 6 unlocks: Gut Health                Customer
20      [EMAIL]                  Email MEM-7: Midpoint Milestone           Customer inbox
        GHL Workflow             "6 weeks. Halfway."
        Sent: Wk 6 Monday, 8am  Reply prompt, recap

        WEEKS 7-8:
21      [KAJABI COURSE]          Weeks 7-8 unlock (Stress, Sleep)          Customer
        Kajabi (auto-drip)       NO EMAILS

        WEEK 9:
22      [KAJABI COURSE]          Week 9 unlocks: Liver                     Customer
23      [EMAIL]                  Email MEM-8: Final Stretch                Customer inbox
        GHL Workflow             "4 weeks left. Finish strong."
        Sent: Wk 9 Monday, 8am

        WEEKS 10-11:
24      [KAJABI COURSE]          Weeks 10-11 unlock (Supplements,          Customer
        Kajabi (auto-drip)       Digestion) — NO EMAILS

        WEEK 12:
25      [KAJABI COURSE]          Week 12 unlocks: Integration              Customer
26      [EMAIL]                  Email MEM-9: Final Module                 Customer inbox
        GHL Workflow             "Your last module."
        Sent: Wk 12 Monday, 8am

        ════════════════════════════════════════════════════════
        GRADUATION + HWN TRANSITION
        ════════════════════════════════════════════════════════

27      [EMAIL]                  Email MEM-10: Graduation                  Customer inbox
        GHL Workflow             "12 weeks. You did it."
        Sent: Wk 12 + 3 days    Pure celebration. ZERO upsell.

28      [FORM]                   Testimonial request form                  Customer
        GHL Form or Typeform     (linked from graduation email)
        URL: /mem-testimonial    Simple: name, photo, "share your
                                 experience in a few sentences"

29      [EMAIL]                  Email MEM-11: "So... what now?"           Customer inbox
        GHL Workflow             HWN reintroduction, soft CTA
        Sent: Wk 12 + 8 days    → HWN checkout page
        (~Day 95)

        [CHECKOUT PAGE]          CTA links to: HWN checkout page           Customer
        GHL Funnel               (same as Flow 4, Step 1)
        URL: /hormone-wellness-network-checkout

30      [EMAIL]                  Email MEM-12: HWN Expiry Notice           Customer inbox
        GHL Workflow             "Your HWN access ends [date]"
        Sent: 7 days before      CTA → HWN checkout
        hwn_bonus_expiry_date    SKIP if purchased_hwn
        (conditional)

31      [EMAIL]                  Email MEM-13: Final HWN Notice            Customer inbox
        GHL Workflow             "Tomorrow your access ends"
        Sent: 1 day before       SKIP if purchased_hwn
        expiry (conditional)

32      [GHL BACKEND]            Bonus expiry date reached                 Nobody
        GHL Workflow             - Remove tag: hwn_bonus_active
                                 - IF NOT purchased_hwn:
                                   revoke Kajabi HWN access
                                 - Contact → general nurture

        ════════════════════════════════════════════════════════
        PARALLEL: PAYMENT DUNNING (payment plan only)
        ════════════════════════════════════════════════════════

D1      [GHL BACKEND]            Payment fails (GHL webhook)               Nobody
        GHL Workflow             - Apply tag: mem_payment_failed

D2      [INTERNAL]               Team notification: payment failed         Dr. P team
        GHL Notification         for high-value customer
        /Slack

D3      [EMAIL]                  Email MEM-D1: Dunning 1                   Customer inbox
        GHL Workflow             "Quick heads up about your payment"
        Sent: +2 hours

D4      [EMAIL]                  Email MEM-D2: Dunning 2                   Customer inbox
        GHL Workflow             "Following up — need a hand?"
        Sent: Day 3              SKIP if payment recovered
        (conditional)

D5      [EMAIL]                  Email MEM-D3: Dunning 3                   Customer inbox
        GHL Workflow             "Last step to keep access"
        Sent: Day 6              SKIP if recovered
        (conditional)

D6      [GHL BACKEND →           Day 10: revoke MEM course access          Nobody
         KAJABI COURSE]          (keep community access 7 more days)       (customer
        Webhook                  Apply tag: mem_access_paused              notices
                                                                           on login)

D7      [INTERNAL]               Team alert: personal outreach needed      Dr. P team
        GHL Notification

D8      [GHL BACKEND →           Day 17: revoke community access           Nobody
         KAJABI COMMUNITY]
        Webhook

DR      [EMAIL]                  Recovery email (if payment recovered      Customer inbox
        GHL Workflow             at any point): "You're all set"
        Sent: on recovery        + restore all Kajabi access

────────────────────────────────────────────────────────────────────

MEM PAGES/ASSETS NEEDED:
  1. [CHECKOUT PAGE] MEM order form with payment plan options + UHA bump
  2. [CONFIRMATION PAGE] premium design, conditional Kajabi setup,
     community link, call calendar, 12-week timeline
     - ASSET: Screenshot of Kajabi invite email
     - ASSET: Calendar .ics file for first accountability call
  3. [KAJABI COURSE] 12 modules set up with weekly drip
  4. [KAJABI COMMUNITY] Empowered Sister Community set up
  5. [FORM] Testimonial request form
  6. [EMAILS] 13 content + 3 dunning + 1 recovery = 17 templates

────────────────────────────────────────────────────────────────────
```

---

# FLOW 4: HWN ($47/mo or $470/yr) — EVERY TOUCHPOINT

```
STEP    CHANNEL                  WHAT HAPPENS                              WHO SEES IT
────    ───────                  ────────────                              ──────────

1       [CHECKOUT PAGE]          GHL order form: HWN membership            Customer
        GHL Funnel
        URL: /hormone-wellness-network-checkout
                                 - Name, email, payment info
                                 - Plan selection:
                                   ○ Monthly: $47/mo
                                   ○ Annual: $470/yr (save $94)

2       [GHL BACKEND]            Payment processes                         Nobody
        GHL Workflow             - Apply tags: purchased_hwn, customer
                                 - Apply: hwn_monthly OR hwn_annual
                                 - IF hwn_churned exists: remove it,
                                   apply hwn_returning_member
                                 - Check kajabi_account_created
                                 - Trigger Kajabi enrollment: HWN
                                   content + community
                                 - Trigger Workflow: "HWN — Post-Purchase"

3       [GHL BACKEND →           Kajabi enrollment                         Nobody
         KAJABI COURSE]          - HWN membership content access
        Webhook/API              - HWN community access
                                 - Kajabi sends password email (if new)

4       [CONFIRMATION PAGE]      Community-first welcome page              Customer
        GHL Funnel Page
        URL: /hormone-wellness-network-membership-thank-you-reg
                                 PAGE CONTENT:
                                 ┌────────────────────────────────────┐
                                 │ "You're part of the Network now."  │
                                 │                                    │
                                 │ IF NEW KAJABI USER:                │
                                 │ [Password setup instructions       │
                                 │  with screenshot — same as         │
                                 │  Challenge/MEM]                    │
                                 │                                    │
                                 │ IF RETURNING KAJABI USER:          │
                                 │ [LOG IN] ← button → Kajabi         │
                                 │                                    │
                                 │ ───────────────────────            │
                                 │ What's happening right now:        │
                                 │                                    │
                                 │ 📅 Next Q&A with Dr. P:            │
                                 │    [Day, Date at Time]             │
                                 │    [ADD TO CALENDAR]               │
                                 │                                    │
                                 │ 📅 Next Masterclass:                │
                                 │    [Topic] — [Day, Date at Time]   │
                                 │    [ADD TO CALENDAR]               │
                                 │                                    │
                                 │ 💬 Community:                       │
                                 │    "[Member name] just posted       │
                                 │     about [topic]"                  │
                                 │    [JOIN THE COMMUNITY] ← button    │
                                 │    → Kajabi community URL           │
                                 │                                    │
                                 │ ───────────────────────            │
                                 │ Your first move:                   │
                                 │ "Introduce yourself in the         │
                                 │  community. Tell us who you are    │
                                 │  and what brought you here."       │
                                 │                                    │
                                 │ "We sent all of this to your       │
                                 │  email too."                       │
                                 └────────────────────────────────────┘

                                 NOTE: The "Next Q&A" and "Next
                                 Masterclass" sections need to be
                                 updated on this page whenever
                                 event dates change. Options:
                                 - Manual update by VA
                                 - GHL custom values that auto-populate
                                 - Calendly/TidyCal embed

5       [EMAIL]                  Email HWN-1: Welcome                      Customer inbox
        GHL Workflow             Trigger: immediate
        Sent: immediately
                                 IF hwn_returning_member:
                                 → Send "Welcome Back" version instead
                                 → SKIP onboarding (Step 7)

6       [KAJABI COMMUNITY]       Customer joins community                  Customer
        Kajabi                   Posts intro (prompted by email/page)

7       [EMAIL]                  Email HWN-2: "The Rhythm"                 Customer inbox
        GHL Workflow             How the membership works
        Sent: Day 3, 9am        Conditional: if no Kajabi login →
                                 add help offer paragraph

        [CALENDAR]               Calendar links for upcoming events        Customer
        .ics downloads           (included in welcome email + page)

        ════════════════════════════════════════════════════════
        ONGOING MONTHLY OPERATIONS
        ════════════════════════════════════════════════════════

        1ST OF EACH MONTH:
8       [EMAIL]                  Email HWN-3: Monthly Digest               Customer inbox
        GHL Workflow             "What's happening this month"
        Sent: 1st of month,     Schedule, last month recap, calendar
        9am                      links

                                 NOTE: This is a TEMPLATE that must
                                 be duplicated and customized each
                                 month with current:
                                 - Masterclass topic + date
                                 - Q&A dates (2x/month)
                                 - Last month's masterclass replay link
                                 - Community highlight
                                 Could be partially automated with
                                 GHL custom values.

        MORNING OF EACH LIVE EVENT:
9       [EMAIL]                  Email HWN-4: Day-Of Reminder              Customer inbox
        GHL Workflow             "Today at [time]: [Event]"
        Sent: morning of         Short — 3 lines + join link
        event (scheduled)
                                 Live event join link → Zoom or
                                 Kajabi Live URL

10      [SMS] (opt-in only)      "Dr. P goes live in 30 min!              Customer phone
        GHL SMS Workflow         Join: [link]"
        Sent: 30 min before      ONLY for contacts who opted in to SMS
        live event

11      [KAJABI COURSE /         Customer attends live event               Customer
         ZOOM]                   (Q&A or masterclass)
        Live session             Via Zoom link or Kajabi Live

12      [KAJABI COURSE]          Masterclass replay posted to Kajabi       Customer
        Kajabi                   (by Dr. P team, day after live)

13      [EMAIL]                  Email HWN-5: Masterclass Replay           Customer inbox
        GHL Workflow             "Replay: [Topic]"
        Sent: day after          ONLY sent to non-attendees
        masterclass              (skip if contact attended live)
        (conditional)

        ════════════════════════════════════════════════════════
        RETENTION ENGINE (monthly background process)
        ════════════════════════════════════════════════════════

14      [GHL BACKEND]            Engagement scoring runs monthly           Nobody
        GHL Workflow             Check last 30 days:
        Trigger: 1st of month   - Attended live event?
                                 - Community post?
                                 - Kajabi login?
                                 - Email opens/clicks?

                                 → 2+ signals: tag hwn_engaged
                                 → 0-1 signals: tag hwn_at_risk
                                 → All events + community: hwn_power_user

15      [EMAIL]                  Email HWN-6: Re-Engagement                Customer inbox
        GHL Workflow             "Haven't seen you lately"
        Sent: when hwn_at_risk   Personal check-in, one event highlight
        applied (max 1x per      ONLY if no re-engagement email sent
        60 days)                 in last 60 days

16      [INTERNAL]               Team alert: at-risk member                Dr. P team
        GHL Notification         needs personal outreach
        Trigger: 14 days after   (community DM or personal email)
        re-engagement email
        with no engagement

        ════════════════════════════════════════════════════════
        RENEWALS + DUNNING
        ════════════════════════════════════════════════════════

17      [GHL BACKEND]            Renewal processes successfully            Nobody
        GHL Payment              SILENT — no email sent.
                                 (No "you've been charged" notification)

18      [EMAIL]                  Email HWN-D1: Dunning 1                   Customer inbox
        GHL Workflow             "Quick note about your membership"
        Trigger: payment failed  Sent +2 hours after failure
        Sent: +2 hours

19      [EMAIL]                  Email HWN-D2: Dunning 2                   Customer inbox
        GHL Workflow             "Still need to update"
        Sent: Day 3              SKIP if recovered
        (conditional)

20      [EMAIL]                  Email HWN-D3: Dunning 3                   Customer inbox
        GHL Workflow             "Access needs attention"
        Sent: Day 6              SKIP if recovered
        (conditional)

21      [GHL BACKEND →           Day 10: revoke Kajabi access              Nobody
         KAJABI COURSE]          Apply: hwn_churned
        Webhook                  Remove: purchased_hwn
                                 → Trigger Win-Back workflow

        ════════════════════════════════════════════════════════
        CANCELLATION
        ════════════════════════════════════════════════════════

22      [GHL BACKEND]            Cancellation request received             Nobody
        GHL Workflow             Apply tag: hwn_cancel_requested

23      [INTERNAL]               Team alert: cancellation                  Dr. P team
        GHL Notification

24      [EMAIL]                  Email HWN-7: Cancellation Confirmed       Customer inbox
        GHL Workflow             Access end date, exit survey link
        Sent: immediately

25      [FORM]                   Exit survey (1 question)                  Customer
        GHL Form                 "What made you decide to cancel?"
        URL: /hwn-exit-survey    Options:
                                 - Too expensive
                                 - Not enough time
                                 - Didn't feel like I was getting value
                                 - Got what I needed
                                 - Other

        [GHL BACKEND]            Survey response → update custom field      Nobody
                                 hwn_cancel_reason

26      [GHL BACKEND →           End of billing period:                    Nobody
         KAJABI COURSE]          - Revoke Kajabi access
        Webhook                  - Apply: hwn_churned
                                 - Set field: hwn_churn_date
                                 - Remove: purchased_hwn
                                 - Trigger Win-Back workflow

        ════════════════════════════════════════════════════════
        WIN-BACK (60 days, 4 emails)
        ════════════════════════════════════════════════════════

27      [EMAIL]                  Email HWN-W1: "What's been happening"     Customer inbox
        GHL Workflow             Value update, not guilt
        Sent: Day 14 post-churn  CTA → /hormone-wellness-network-checkout
        (conditional — skip
         if re-subscribed)

28      [EMAIL]                  Email HWN-W2: "Can I ask you something?"  Customer inbox
        GHL Workflow             Personalized to exit reason
        Sent: Day 30 post-churn  IF "too expensive": offer annual plan
        (conditional)            CTA → /hormone-wellness-network-checkout

29      [EMAIL]                  Email HWN-W3: Social proof                Customer inbox
        GHL Workflow             Returning member testimonial
        Sent: Day 45 post-churn  CTA → /hormone-wellness-network-checkout
        (conditional)

30      [EMAIL]                  Email HWN-W4: "One last thing"            Customer inbox
        GHL Workflow             Graceful close, free value, subtle link
        Sent: Day 60 post-churn  After this: END → general nurture
        (conditional)            No more HWN-specific emails.

        IF RE-SUBSCRIBED (at any point):
31      [GHL BACKEND]            Remove: hwn_churned, hwn_cancel_requested Nobody
                                 Apply: purchased_hwn, hwn_returning_member
                                 Restore Kajabi access
                                 Stop Win-Back workflow

32      [EMAIL]                  "Good to have you back"                   Customer inbox
        GHL Workflow             Current month digest, skip onboarding

────────────────────────────────────────────────────────────────────

HWN PAGES/ASSETS NEEDED:
  1. [CHECKOUT PAGE] HWN order form with monthly/annual toggle
  2. [CONFIRMATION PAGE] community-first, upcoming events, calendar links
     - Requires: current event dates (manual update or custom values)
     - ASSET: Screenshot of Kajabi invite email
     - ASSET: Calendar .ics files for upcoming events
  3. [KAJABI COURSE] HWN membership content set up
  4. [KAJABI COMMUNITY] HWN community set up
  5. [FORM] Exit survey (1-question cancel reason)
  6. [EMAILS] 14 templates:
     - 2 onboarding (welcome + rhythm)
     - 1 welcome back (returning members)
     - 1 monthly digest (template — duplicated monthly)
     - 1 day-of reminder (template)
     - 1 masterclass replay
     - 1 re-engagement
     - 3 dunning
     - 1 cancellation confirmation
     - 4 win-back
     - 1 recovery
  7. [SMS] Live event reminder template (30-min before)

────────────────────────────────────────────────────────────────────
```

---

# COMPLETE ASSET INVENTORY

## Web Pages to Build (GHL Funnel Pages)

| # | Page | Type | URL Slug | Flow |
|---|------|------|----------|------|
| 1 | UHA Checkout | Order form | /uha-checkout | UHA |
| 2 | UHA Confirmation | Thank-you + quiz start | /uha-confirmed | UHA |
| 3 | UHA Results — Estrogen Dominant | Results display | /uha-results-ed | UHA |
| 4 | UHA Results — Balanced | Results display | /uha-results-bal | UHA |
| 5 | Challenge Checkout | Order form | /challenge-checkout | Challenge |
| 6 | Challenge Confirmation | Thank-you + Kajabi setup | /challenge-confirmed | Challenge |
| 7 | MEM Checkout | Order form + payment plans | /mem-checkout | MEM |
| 8 | MEM Confirmation | Premium thank-you + setup | /mem-confirmed | MEM |
| 9 | HWN Checkout | Order form + plan toggle | /hormone-wellness-network-checkout | HWN |
| 10 | HWN Confirmation | Community welcome | /hormone-wellness-network-membership-thank-you-reg | HWN |

## Forms to Build (GHL Forms)

| # | Form | Purpose | URL Slug | Flow |
|---|------|---------|----------|------|
| 1 | MEM Testimonial | Post-graduation story collection | /mem-testimonial | MEM |
| 2 | HWN Exit Survey | 1-question cancel reason | /hwn-exit-survey | HWN |

## External Platform Assets

| # | Asset | Platform | Flow |
|---|-------|----------|------|
| 1 | 48-question quiz | Quiz platform (TBD) | UHA |
| 2 | Quiz → GHL webhook | Quiz platform config | UHA |
| 3 | Challenge course (7 modules, daily drip) | Kajabi | Challenge |
| 4 | MEM course (12 modules, weekly drip) | Kajabi | MEM |
| 5 | Empowered Sister Community | Kajabi | MEM |
| 6 | HWN membership content | Kajabi | HWN |
| 7 | HWN community | Kajabi | HWN |
| 8 | Kajabi invite email screenshot | Screenshot asset | All Kajabi flows |
| 9 | Calendar .ics files for recurring events | Generated | MEM, HWN |

## GHL Workflows to Build

| # | Workflow Name | Trigger | Flow |
|---|-------------|---------|------|
| 1 | UHA — Post-Purchase | Tag: purchased_uha | UHA |
| 2 | UHA — Quiz Results | Inbound webhook (quiz complete) | UHA |
| 3 | Challenge — Post-Purchase | Tag: purchased_challenge | Challenge |
| 4 | MEM — Post-Purchase | Tag: purchased_mem | MEM |
| 5 | MEM — Payment Dunning | Payment failed event | MEM |
| 6 | HWN — Post-Purchase | Tag: purchased_hwn | HWN |
| 7 | HWN — Monthly Digest | 1st of month (scheduled) | HWN |
| 8 | HWN — Live Event Reminders | Event day (scheduled) | HWN |
| 9 | HWN — Masterclass Replay | Day after masterclass (scheduled) | HWN |
| 10 | HWN — Engagement Scoring | 1st of month (scheduled) | HWN |
| 11 | HWN — Payment Dunning + Cancellation | Payment failed / cancel event | HWN |
| 12 | HWN — Win-Back | Tag: hwn_churned | HWN |

## Email Templates Needed

| # | Email ID | Flow | Conditional Variants |
|---|----------|------|---------------------|
| 1 | UHA-1: Backup Confirmation | UHA | None |
| 2 | UHA-2: Hormone Report | UHA | Estrogen dominant / Balanced |
| 3 | UHA-3: Quiz Nudge 1 | UHA | None |
| 4 | UHA-3b: Quiz Nudge 2 | UHA | None |
| 5 | UHA-4: The Now-What | UHA | Estrogen dominant / Balanced |
| 6 | UHA-5: Ascension Bridge | UHA | None |
| 7 | UHA-6: Final Touch | UHA | None |
| 8 | CH-1: Welcome + Access | Challenge | New Kajabi / Returning Kajabi |
| 9 | CH-2: Day 2 Check-In | Challenge | None |
| 10 | CH-3: Midpoint Momentum | Challenge | Active / Inactive |
| 11 | CH-4: Final Day | Challenge | None |
| 12 | CH-5: Celebration | Challenge | None |
| 13 | CH-6: The Gap | Challenge | None |
| 14 | CH-7: The Proof | Challenge | None |
| 15 | CH-8: The Full Picture | Challenge | None |
| 16 | CH-9: Objection Buster | Challenge | None |
| 17 | MEM-1: Welcome | MEM | New Kajabi / Returning + Full pay / Plan |
| 18 | MEM-2: How This Works | MEM | None |
| 19 | MEM-3: Week 1 Accountability | MEM | None |
| 20 | MEM-4: Week 2 Nutrition | MEM | None |
| 21 | MEM-5: Week 3 Movement | MEM | None |
| 22 | MEM-6: Week 4 Hormones | MEM | None |
| 23 | MEM-7: Midpoint Milestone | MEM | None |
| 24 | MEM-8: Final Stretch | MEM | None |
| 25 | MEM-9: Final Module | MEM | None |
| 26 | MEM-10: Graduation | MEM | None |
| 27 | MEM-11: What Now (HWN) | MEM | None |
| 28 | MEM-12: HWN Expiry Notice | MEM | None |
| 29 | MEM-13: Final HWN Notice | MEM | None |
| 30 | MEM-D1: Dunning 1 | MEM | None |
| 31 | MEM-D2: Dunning 2 | MEM | None |
| 32 | MEM-D3: Dunning 3 | MEM | None |
| 33 | MEM-DR: Recovery | MEM | None |
| 34 | HWN-1: Welcome | HWN | New Kajabi / Returning Kajabi |
| 35 | HWN-1b: Welcome Back | HWN | Returning member variant |
| 36 | HWN-2: The Rhythm | HWN | Logged in / Not logged in |
| 37 | HWN-3: Monthly Digest | HWN | Template (customized monthly) |
| 38 | HWN-4: Day-Of Reminder | HWN | Template (masterclass / Q&A) |
| 39 | HWN-5: Masterclass Replay | HWN | None |
| 40 | HWN-6: Re-Engagement | HWN | None |
| 41 | HWN-D1: Dunning 1 | HWN | None |
| 42 | HWN-D2: Dunning 2 | HWN | None |
| 43 | HWN-D3: Dunning 3 | HWN | None |
| 44 | HWN-7: Cancellation Confirmed | HWN | None |
| 45 | HWN-W1: Win-Back Update | HWN | None |
| 46 | HWN-W2: Win-Back Personal | HWN | Conditional on cancel reason |
| 47 | HWN-W3: Win-Back Social Proof | HWN | None |
| 48 | HWN-W4: Win-Back Final | HWN | None |
| 49 | HWN-DR: Recovery | HWN | None |
| 50 | HWN-WB: Welcome Back (re-sub) | HWN | None |

**TOTAL: 50 email templates** (some with 2 conditional variants = ~58 versions)
