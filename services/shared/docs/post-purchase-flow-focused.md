# Dr. P: Post-Purchase Flow (Focused)
## The first 48 hours after checkout — per program. Nothing else.

> **Scope:** From "Payment Processed" to "She's inside, oriented, and knows what to do next." This is the piece to build first. Everything beyond hour 48 (module drips, ascension, dunning, win-back) is covered in `checkout-to-delivery-flows.md` and comes in later phases.

---

# CURRENT STATE: WHAT SHE ACTUALLY GETS TODAY

Pulled live from the ActiveCampaign API on 2026-04-16. This is the reality of the existing post-purchase flows, and it's worse than we assumed:

| Program | Automation | Email "Purchase Confirmation" sends | What it should be | What it actually is |
|---|---|---|---|---|
| **UHA** ($47) | #13 "Purchase Confirmation Email \| Ultimate Hormone Assessment" | Subject: **"Final Call: $47 Is All It Takes to Start Balancing Your Hormones!"** | Quiz link + access | A SALES pitch for the $27 7-Day Challenge |
| **UHA Results** | #18 "UHA Send Results" | Subject: **"Last Chance to Join Us and Transform Your Health in Just 7 Days!"** | Her personalized hormone results | Another sales pitch for the Challenge |
| **Challenge** ($47) | #7 "Post Purchase Email Sequence" | Subject: **"Final call — I'd hate for you to miss this."** | Kajabi login + Day 1 access | A sales/urgency email |
| **Challenge Day 1** | #9 Day 1 Welcome | Subject: **"We worked hard to create something incredible just for you!"** | Day 1 login + what to do today | A generic "we made something" email |
| **MEM** ($1,997) | #5 "Purchase Confirmation Email \| MEM" | Subject: **"Your exclusive invitation is expiring soon! ⌛"** | Premium welcome + Kajabi + community + first call | A sales pitch for **HWN** at $47/mo, with an unrendered `[First Name]` placeholder in the body |

**Bottom line:** People who just paid Dr. P money are being sold something else instead of welcomed. The $2K MEM buyer gets an email pitching a $47/month product. The UHA buyer never receives her quiz. There is no access, no welcome, no "here's what to do now." This is the single biggest leak in the funnel and the most important thing to fix first.

---

# GLOBAL RULES FOR THE FIRST 48 HOURS

1. **Confirmation page is the hero.** The email is backup. 100% of buyers see the confirmation page — design for it first.
2. **The first email's one job is access.** No pitches, no upsells, no "here's what we offer." Login info, next step, reply prompt. That's it.
3. **Send the right email at the right time.** Email 1: immediately. Email 2: Day 1 morning (or 4hr conditional for UHA quiz). Email 3: Day 2 morning. Stop there for this phase.
4. **Kajabi password: one clear path.** Single GHL email mentions what the Kajabi password email looks like so she knows to look for it. Confirmation page shows a visual. That same first email also includes the direct login URL and says: "If you already set up your account, use this link now. If you already had an existing account, use this link with your existing password."
5. **Bump offer flows delay by 24 hours.** If she buys UHA with Challenge bump, the Challenge flow doesn't fire until tomorrow — no inbox bombing.
6. **Voice:** Dr. P talking to a patient she cares about. Warm, direct, human. No "secure your spot," no "exclusive invitation," no urgency language after a purchase.

---

# FLOW 1: UHA ($47) — POST-PURCHASE FIRST 48 HOURS

```
HOUR 0: PAYMENT PROCESSED (GHL)
    │
    ├─ Apply tags: purchased_uha, customer
    ├─ Apply: uha_quiz_pending
    ├─ IF bump accepted: purchased_challenge + schedule Challenge flow for +24hr
    │
    ▼
HOUR 0: REDIRECT TO CONFIRMATION PAGE (embedded quiz)
    Page content (THIS is the product delivery, not an email):
      • "Payment confirmed. Let's find out what your hormones are telling you."
      • Quiz embedded directly OR auto-redirects to quiz in 3 seconds
      • NO "check your email" step — she's already here
      • Below quiz: "We also sent a backup link to your inbox in case you need it"
      • IF bump: small "Your Challenge is also ready — we'll send access tomorrow"
    │
    ▼
HOUR 0 + 2 MIN: EMAIL 1 — Backup Access
    From: Dr. Kerry-Anne Perkins <support@callmedoctorp.com>
    Subject: "Your assessment link — in case you need it"
    Preheader: "Already started on the last page? Ignore this one."
    Body (short, 4 lines):
      "Hi [First Name],
       Your Hormone Assessment is ready.
       [TAKE THE QUIZ — link]
       If you already started on the payment page, just keep going — your
       results will land in your inbox as soon as you finish.
       — Dr. P"
      + receipt at bottom (small text)
    │
    ▼
HOUR 0 to HOUR 4: QUIZ COMPLETION WEBHOOK (from quiz platform → GHL)
    │
    ├─ Apply: uha_completed + result tag (uha_result_estrogen_dominant OR uha_result_balanced)
    ├─ Remove: uha_quiz_pending
    │
    ▼
IMMEDIATELY ON QUIZ SUBMIT: RESULTS PAGE (on-screen, not email-first)
    Page content:
      • Full personalized breakdown (result type, 3 factors, 3 actions, visual scale)
      • Conditional on result (ED vs Balanced)
      • "Your full report is being sent to your email right now"
      • Soft CTA at bottom: "Women with your profile see the biggest shifts
         in the 7-Day Challenge" (text link, NOT a pitch button)
    │
    ▼
HOUR 0 TO 4 + 2 MIN: EMAIL 2 — Your Hormone Report (conditional content)
    Subject: "[First Name], your hormone results"
    Preheader: "The keepsake version — save this one."
    Body:
      • Result type + plain-language explanation
      • Her 3 key factors (pulled from quiz answers)
      • Her 3 action items for this week
      • Link back to results page
      • NO upsell. Pure value delivery.
    │
    ▼
==========================================================
CONDITIONAL BRANCH: Did she take the quiz?
==========================================================
    │
    ├─ IF quiz completed by Hour 4: STOP (48-hour flow ends here for completers)
    │
    └─ IF quiz NOT completed by Hour 4:
         │
         ▼
HOUR 4: EMAIL 3 — Gentle Nudge
    Subject: "Your assessment is waiting for you"
    Body (2 sentences):
      "Hi [First Name],
       It takes about 10 minutes — and the insights are worth it.
       [START YOUR ASSESSMENT — link]
       — Dr. P"
    │
    ▼
DAY 2 @ 9AM: QUIZ STATUS CHECK
    │
    ├─ IF completed: STOP (she's in, no more nudges)
    │
    └─ IF still not completed:
         │
         ▼
DAY 2 @ 9AM: EMAIL 4 — Last Nudge
    Subject: "Still curious about your hormones?"
    Body:
      "Most women are surprised by what they learn about themselves
       in this assessment — even the ones who thought they had it figured out.
       [TAKE THE QUIZ — link]
       — Dr. P
       P.S. If something's off and you need help, just reply to this email."
    │
    ▼
IF STILL NOT COMPLETED BY DAY 4:
    Apply tag: uha_quiz_abandoned
    Flow exits 48-hour phase. Pick up in ascension phase later.
```

**UHA 48-hour summary:**
- Confirmation page is the real delivery (quiz starts there)
- Email 1: access backup only (immediate)
- Email 2: personalized results (on quiz completion, conditional content)
- Email 3: nudge (Hour 4, conditional on quiz incomplete)
- Email 4: last nudge (Day 2, conditional on quiz still incomplete)
- Max emails: 4 | Typical emails: 2 (if she completes the quiz quickly)

---

# FLOW 2: 7-DAY CHALLENGE ($47) — POST-PURCHASE FIRST 48 HOURS

```
HOUR 0: PAYMENT PROCESSED (GHL)
    │
    ├─ Apply tags: purchased_challenge, customer
    ├─ IF bump accepted: purchased_uha + schedule UHA flow for +24hr
    │
    ▼
HOUR 0: KAJABI ACCOUNT LOGIC
    │
    ├─ IF tag kajabi_account_created EXISTS: treat as returning user
    ├─ IF NOT: apply tag kajabi_account_created → treat as new user
    │
    ▼
HOUR 0: GRANT KAJABI ACCESS (GHL → Kajabi webhook)
    • Enroll in Challenge course
    • Day 1 unlocked immediately
    • Days 2-7 drip daily (handled later — not part of this flow)
    │
    ▼
HOUR 0: REDIRECT TO CONFIRMATION PAGE
    Page content differs by user type:

    IF new Kajabi user:
      • "You're in the Challenge!"
      • Visual step-by-step:
           Step 1: Check your email for a login setup message from Kajabi
                   (it looks like this → [screenshot of Kajabi password email])
                   Click the link to set your password.
           Step 2: Once logged in, Day 1 is already waiting.
      • "What to expect: one module per day for 7 days, 15 min each"
      • Bonus preview (meal plan, grocery list, training program)
      • IF bump: "Your Hormone Assessment is also ready — we'll send access tomorrow"

    IF returning Kajabi user:
      • "You're in the Challenge! Day 1 is live right now."
      • Direct login button → Kajabi Day 1
      • Same expectations + bonus preview
    │
    ▼
HOUR 0 + 2 MIN: EMAIL 1 — Welcome + Access
    Subject: "Your Challenge starts now — here's your login"
    Preheader: "Everything you need to get into Day 1."
    Body (short, clear):
      "Hi [First Name],
       You're in the Hormone Reset & Recharge 7-Day Challenge. Here's how
       to get started.

       [LOG IN AND START DAY 1 — link]
       If you already set up your Kajabi account, use that link now.
       If you already had a Kajabi account before today, use that same link
       and your existing password.
       If neither is true yet, you'll get a second email from Kajabi asking
       you to set your password. Click the link in THAT email, then come back
       to the login link above.
       ↳ Can't find it? Check spam. Still missing? Reply to this email.

       Day 1 takes about 15 minutes. Do that today if you can — it sets the
       tone for the week.

       Reply to this email and tell me the #1 thing you want to change about
       how you feel. I read every reply.

       — Dr. P"
      + receipt at bottom
    │
    ▼
DAY 2 @ 8AM: LOGIN CHECK
    │
    ├─ IF Kajabi login detected: send standard Day 2 email (see below)
    │
    └─ IF NO login yet: send re-engagement Day 2 email (different content)
    │
    ▼
DAY 2 @ 8AM: EMAIL 2 — Day 2 Nudge (conditional)

    IF logged in / Day 1 completed:
      Subject: "Did you finish Day 1? (Be honest.)"
      Body:
        "If you did it — amazing.
         If not, go do it now. It's 15 minutes. I'll wait.
         Today we talk nutrition — and I'm going to tell you the one thing
         most hormone 'experts' get completely wrong about food.
         [LOG IN TO DAY 2 — link]
         — Dr. P"

    IF NOT logged in yet:
      Subject: "Hey [First Name] — Day 1 is still waiting for you"
      Body:
        "I get it. Life happens.
         But you paid for this because something needed to change.
         Day 1 is 15 minutes. It's still there waiting for you.
         [LOG IN HERE — link]
         Reply if something's blocking you and I'll help you through it.
         — Dr. P"
    │
    ▼
48-HOUR FLOW ENDS HERE. Day 3-7 emails are part of the challenge content cadence
(covered in the full flows doc), not the post-purchase phase.
```

**Challenge 48-hour summary:**
- Confirmation page: clear password path + Day 1 access
- Email 1: welcome + login + engagement prompt (immediate)
- Email 2: Day 2 nudge, conditional on login status (Day 2 @ 8am)
- Max emails in first 48hrs: 2

---

# FLOW 3: MEM ($1,997) — POST-PURCHASE FIRST 48 HOURS

> MEM is high-stakes. She just made a major investment. The first 48 hours need to make her feel that decision was right — not like she walked into a generic marketing funnel. Everything here should feel premium.

```
HOUR 0: PAYMENT PROCESSED (GHL)
    │
    ├─ Apply tags: purchased_mem, customer, high_value_customer
    ├─ Apply payment tag: mem_paid_full OR mem_payment_plan
    ├─ Apply: hwn_bonus_active + hwn_bonus_start_[date]
    ├─ IF bump: purchased_uha + schedule UHA flow for +48hr (longer delay for MEM buyer)
    │
    ▼
HOUR 0: KAJABI ACCOUNT LOGIC
    │
    ├─ IF kajabi_account_created: returning user
    ├─ IF NOT: apply tag → new user
    │
    ▼
HOUR 0: GRANT KAJABI ACCESS (GHL → Kajabi)
    • Enroll in MEM course (Week 1 unlocked, Weeks 2-12 drip weekly)
    • Enroll in Empowered Sister Community
    • Enroll in HWN (bonus, 3 months)
    • DO NOT trigger HWN welcome flow (it's a bonus, not a separate purchase)
    │
    ▼
HOUR 0: REDIRECT TO CONFIRMATION PAGE (premium feel)
    Page content:
      • "Welcome to the Mastermind, [First Name]. This is where everything changes."
      • Video message from Dr. P (optional but high-impact — 60 sec, personal)
      • Setup steps (conditional on new/returning Kajabi user, same pattern as Challenge)
      • "Join your community" — direct link to Empowered Sister Community
      • First accountability call date/time + "Add to calendar" button
      • "What to expect over 12 weeks" — visual timeline
      • Bonus section: "You also have 3 months of Hormone Wellness Network
         access — we'll show you around later. Right now, focus on Week 1."
      • Payment plan schedule if applicable (full transparency)
    │
    ▼
HOUR 0 + 2 MIN: EMAIL 1 — Welcome + Access
    Subject: "You're in the Mastermind. Here's everything you need."
    Preheader: "Your one job today: get logged in."
    Body:
      "[First Name],
       I don't take this decision lightly, and neither should you.
       You just invested in yourself in a real way. Let me make sure it pays off.

       [LOG IN AND WATCH THE WEEK 1 INTRO — link]
       If you already set up your Kajabi account, use that link now.
       If you already had a Kajabi account before today, use that same link
       and your existing password.
       If neither is true yet, you'll get a separate login email from Kajabi
       in the next few minutes. Set your password there, then come back to the
       login link above.
       ↳ Can't find it? Check spam. Still missing? Reply and we'll fix it.

       Our first accountability call is [day, date, time].
       [ADD TO CALENDAR — link]

       Join the Empowered Sister Community here:
       [COMMUNITY LINK]

       Your one job today: get logged in and watch the Week 1 intro video.
       That's it. Don't try to do everything at once.

       If anything is unclear or not working, reply to this email.
       I want this to work for you.

       — Dr. P"
      + payment plan schedule (if applicable)
      + receipt
    │
    ▼
DAY 2 @ 9AM: EMAIL 2 — How This Works
    Subject: "Here's how to get the most out of the next 12 weeks"
    Preheader: "Your first action item today."
    Body:
      "[First Name],
       You've had a night to get your account set up. Here's how the next
       12 weeks actually work:

       • New module drops every Monday morning
       • Accountability call every [day] at [time] — that's where the real
         breakthroughs happen
       • The community is your support system between calls
       • Week 12 we integrate everything and you graduate

       Your action today: go to the community and introduce yourself.
       Tell us who you are and what you're hoping to change. The women
       in there will have your back for the next 12 weeks.

       [INTRODUCE YOURSELF — community link]
       [OR HEAD TO WEEK 1 — kajabi link]

       — Dr. P"
    │
    ▼
HOUR 48+ / DAY 3: MOVED TO LONGER-TERM FLOW
(Week 1 accountability email on Day 4 is part of the program cadence — not this phase)
```

**MEM 48-hour summary:**
- Confirmation page: premium welcome + (optional) video + setup + first call date
- Email 1: warm welcome, access, community, first call — all in one place (immediate)
- Email 2: "how this works" orientation + community intro prompt (Day 2 @ 9am)
- Max emails in first 48hrs: 2
- Bump offer UHA delays 48hr (not 24hr) — MEM buyer deserves focus

---

# FLOW 4: HWN ($47/mo or $470/yr) — POST-PURCHASE FIRST 48 HOURS

```
HOUR 0: PAYMENT PROCESSED (GHL)
    │
    ├─ Apply tags: purchased_hwn, customer
    ├─ Apply: hwn_monthly OR hwn_annual
    ├─ IF from MEM bonus expiring: hwn_converted_from_mem
    │
    ▼
HOUR 0: KAJABI ACCOUNT LOGIC (same as above)
    │
    ▼
HOUR 0: GRANT KAJABI ACCESS
    • Enroll in HWN content + community
    │
    ▼
HOUR 0: REDIRECT TO CONFIRMATION PAGE
    Page content:
      • "You're part of the Network now."
      • Community-first framing (not transactional)
      • Setup steps for new/returning Kajabi user
      • "Here's what's happening right now in the Network:"
           - Next Q&A with Dr. P: [date/time] + Add to calendar
           - Next masterclass: [topic] on [date] + Add to calendar
           - Community highlight: one recent member win or post
      • "Your first move: introduce yourself in the community."
    │
    ▼
HOUR 0 + 2 MIN: EMAIL 1 — Welcome
    Subject: "Welcome to the Network, [First Name]"
    Body:
      "[First Name],
       You're in the Hormone Wellness Network.
       Here's everything you need:

       [DIRECT KAJABI LOGIN LINK]
       If you already set up your Kajabi account, use that link now.
       If you already had a Kajabi account before today, use that same link
       and your existing password.
       If neither is true yet, watch for the Kajabi setup email, create your
       password there, then come back to the login link above.

       Next Q&A with me: [date/time] → [ADD TO CALENDAR]
       Next masterclass: [topic] on [date] → [ADD TO CALENDAR]

       Your one action today: post your intro in the community.
       [COMMUNITY LINK]

       Everything else can wait. Just get your account set up and say hi.

       — Dr. P"
    │
    ▼
DAY 2 @ 9AM: EMAIL 2 — The Rhythm
    Subject: "Here's how this works (it's simpler than you think)"
    Body:
      "[First Name],
       A quick map of your month in the Network:

       • Twice a month: Q&A with me. Bring your questions.
       • Once a month: live masterclass on a focused topic + replay
       • Weekly: accountability check-in
       • Always: the community. Your people who get it.

       Best way to get value from this: show up to ONE live session
       this month. Just one.

       [IF NOT logged into Kajabi/community yet:]
         I noticed you haven't logged in yet. Need help finding your way
         around? Reply to this email and I'll walk you through it.

       — Dr. P"
    │
    ▼
48-HOUR FLOW ENDS. Monthly digest and ongoing cadence handled separately.
```

**HWN 48-hour summary:**
- Confirmation page: community-first welcome, upcoming events with calendar links
- Email 1: welcome + access + events + intro prompt (immediate)
- Email 2: the rhythm / how this works + login check (Day 3 @ 9am)
- Max emails in first 48hrs: 2

---

# TAGS REQUIRED FOR PHASE 1 (FIRST 48 HOURS)

This is the minimum tag set needed to build just this phase. Full tag architecture in the master flows doc.

### Purchase tags (applied on payment processed)
- `customer` — any purchase
- `purchased_uha`, `purchased_challenge`, `purchased_mem`, `purchased_hwn`
- `high_value_customer` — MEM or HWN annual
- `mem_paid_full`, `mem_payment_plan` — MEM only
- `hwn_monthly`, `hwn_annual` — HWN only
- `hwn_bonus_active` + `hwn_bonus_start_[date]` — MEM buyers' 3-month bonus
- `hwn_converted_from_mem` — bonus-to-paid conversion

### Kajabi state
- `kajabi_account_created` — first Kajabi product (set once, never removed)

### UHA quiz state
- `uha_quiz_pending` — after purchase, before quiz
- `uha_completed` — quiz finished
- `uha_result_estrogen_dominant`, `uha_result_balanced` — quiz result
- `uha_quiz_abandoned` — quiz not taken by Day 4

### Login tracking (for conditional Day 2 emails)
- `kajabi_login_detected` — at least one login event after purchase (event webhook from Kajabi)

---

# BUILD ORDER (Recommended for GHL specialist)

**What to build, in this order:**

1. **Tag architecture** (30 min) — Create all Phase 1 tags listed above.
2. **Kajabi integration webhook** (1-2 hrs) — Confirm GHL → Kajabi enrollment works end-to-end for all 4 products. Test the new vs. returning user tag logic.
3. **Kajabi login event webhook** (30 min) — So we can conditionally send re-engagement emails.
4. **4 confirmation pages** (4-8 hrs) — UHA, Challenge, MEM, HWN. This is the highest-leverage work. Test on mobile + desktop.
5. **UHA quiz → webhook → results delivery** (2-3 hrs) — Quiz platform webhook fires GHL workflow that tags results + redirects to results page + sends results email.
6. **4 Welcome emails (Email 1)** (2 hrs) — Write, test merge tags, test conditional new/returning blocks.
7. **4 Follow-up emails (Email 2)** (2 hrs) — UHA nudge/Day 2, Challenge Day 2 nudge (conditional on login), MEM orientation, HWN rhythm.
8. **UHA conditional nudge emails (3 & 4)** (1 hr) — Hour 4 and Day 2 nudges for non-completers.
9. **End-to-end test** for each program with 2 test contacts (new vs. returning Kajabi user).

**What NOT to build in this phase:**
- Module drip emails (Challenge Day 3-7, MEM Week 2-12)
- Ascension sequences (UHA → Challenge, Challenge → MEM, MEM → HWN)
- Dunning sequences
- Win-back flows
- Engagement scoring / retention logic
- Monthly HWN digest

Those come after this foundation is tested and live.

---

# EDGE CASES TO HANDLE (PHASE 1 ONLY)

1. **Bump offer purchase:** Primary flow runs normally. Secondary flow delays 24hr (UHA/Challenge bump on each other) or 48hr (UHA bump on MEM). Secondary skips its own purchase confirmation email — folded into primary confirmation page.
2. **Duplicate purchase:** If she already has `purchased_mem` and buys HWN directly, skip HWN flow since HWN bonus is already active. Show a different confirmation page: "You already have HWN access through your Mastermind bonus — we've extended your access by 3 months instead of charging you twice." (Escalate to team.)
3. **Kajabi password email delayed/missing:** Confirmation page shows a "Didn't get the Kajabi email?" link with instructions to check spam and a "contact us" fallback.
4. **Quiz webhook fails (UHA):** Fallback — Email 2 at Hour 4 includes a direct link to the results page with a message to "click here if your results didn't come through."
5. **Failed payment mid-flow:** Don't send welcome emails. Show a "Payment issue — let's fix this" page and tag `payment_failed_at_checkout`.

---

# WHAT SUCCESS LOOKS LIKE FOR THIS PHASE

After build + test, every new buyer experiences this:
- Clicks "Buy" → sees a confirmation page that tells her exactly what to do (not "check your email")
- Within 2 minutes: gets ONE email that is actually about her purchase (not a sales pitch for something else)
- Within 48 hours: gets ONE follow-up email appropriate to her program
- If UHA: gets her real quiz results (not a sales pitch disguised as "results")
- If Challenge/MEM/HWN: logs into Kajabi and starts engaging

And critically: **no MEM buyer ever again receives a $47/month HWN pitch as their "purchase confirmation."**
