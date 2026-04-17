# Dr. P: Checkout-to-Delivery Flows (v2 — UX-First Redesign)
## Every step from "Buy Now" to transformation — designed around what she needs to feel, not when the system fires

---

# GLOBAL RULES (Apply to Every Flow)

## 1. Confirmation Page Strategy
The checkout confirmation page is the highest-intent moment in the entire journey. 100% of buyers see it. Zero competition for attention. Every flow MUST use it.

**Standard confirmation page structure:**
- "You're in!" celebration moment (dopamine hit — she just made a decision, reward it)
- Immediate next action — not "check your email" but the actual thing to do RIGHT NOW
- "What happens next" timeline (sets expectations, kills anxiety)
- Email backup: "We also sent this to your inbox in case you need it later"

The email is the BACKUP. The confirmation page is the PRIMARY delivery vehicle.

## 2. Email Throttle: Max 1 Email Per Day Per Contact
No matter how many flows are running simultaneously (bump offers, parallel programs), a contact receives a MAXIMUM of 1 email per day from Dr. P. If two emails are scheduled for the same day, priority order:
1. Transactional (purchase confirmation, dunning) — always sends
2. Active program content (module unlocks, live event reminders)
3. Onboarding/orientation
4. Ascension/upsell — gets pushed to next available slot

Exception: Purchase confirmation emails always send immediately regardless of throttle.

## 3. Kajabi Password — One Clear Path
Stop sending two competing emails. The system should work like this:
- GHL sends the ONLY onboarding email. This email contains:
  - a direct Kajabi login URL for the course or membership
  - "If you already set up your account, use this link now."
  - "If you already had an existing account, use this link and your existing password."
  - "If neither is true yet, watch for the Kajabi setup email in the next few minutes and use that to create your password."
- The confirmation PAGE shows password setup steps visually (screenshot/GIF of what the Kajabi email looks like) so they know what to look for

## 4. Bump Offer Flow Coordination
When a bump offer is accepted, the secondary program flow is DELAYED and MODIFIED:
- Primary program flow runs normally
- Secondary program flow starts on Day 2 (not simultaneously)
- Secondary program's confirmation is folded into the primary confirmation page as a "Bonus" section
- Secondary flow skips its own purchase confirmation email (already covered on the confirmation page)

## 5. Voice
Every email should sound like Dr. P talking to a friend who also happens to be a patient. Not a course platform. Not a marketing funnel. A doctor who cares about this specific woman.

---

# FLOW 1: ULTIMATE HORMONE ASSESSMENT (UHA) — $47

**Checkout bump offer:** 7-Day Challenge ($47 add-on)

```
CHECKOUT PAGE (GHL)
    |
    v
PAYMENT PROCESSED (GHL)
    |
    |--- Apply tags: purchased_uha, customer
    |--- IF bump accepted: purchased_challenge (Challenge flow starts Day 2, modified)
    |
    v
==========================================================
CONFIRMATION PAGE — THE QUIZ STARTS HERE (not in an email)
==========================================================
    - "Payment confirmed! Let's find out what your hormones are telling you."
    - Quiz is EMBEDDED on this page or auto-redirects to quiz within 3 seconds
    - No friction. No "check your email." She's already here. Start now.
    - Below the quiz start: "We also sent a backup link to your email"
    - IF bump accepted: small section at bottom — "Your 7-Day Challenge is ready
      too — we'll send you access tomorrow so you can focus on your assessment first"
    |
    v
EMAIL 1: Backup Confirmation (immediately, but she may not need it)
    - Subject: "Your assessment link (in case you need it)"
    - Short. Not the hero moment — the confirmation page already was.
    - Quiz link
    - "If you already started on the last page, ignore this — your results
      are coming as soon as you finish"
    - Receipt at bottom (not the star of the email)
    |
    v
QUIZ TAKEN (quiz platform → GHL webhook)
    |
    |--- Apply tags: uha_completed, uha_result_estrogen_dominant OR uha_result_balanced
    |
    v
================================================================
QUIZ RESULTS PAGE — IMMEDIATE, ON-SCREEN (not email-first)
================================================================
    - Results displayed immediately after quiz submission
    - Full personalized breakdown ON THE PAGE:
        - IF estrogen_dominant:
            - What estrogen dominance means (in plain language, not clinical jargon)
            - Her top 3 contributing factors based on quiz answers
            - 3 immediate things she can do THIS WEEK
            - Visual: hormone balance scale showing where she falls
        - IF balanced:
            - What this means (and why it's not "mission accomplished")
            - Her top 3 strengths to maintain
            - 3 optimization moves for the next level
            - Visual: hormone balance scale showing where she falls
    - "Your full report is being sent to your email right now"
    - Soft CTA at bottom (not a hard pitch): "Women with your profile see the
      biggest shifts in the 7-Day Challenge" — link to Challenge page
    |
    v
EMAIL 2: Your Hormone Report (triggered on quiz completion)
    - Subject: "[First Name], your hormone results"
    - This is the KEEPSAKE version — something she'll save and refer back to
    - Feels like a document, not a marketing email:
        - Result type + what it means
        - Her 3 key factors (pulled from quiz)
        - Her 3 action items
        - Link to results page (if she wants to revisit)
    - NO upsell in this email. Pure value delivery. She just got her
      results — let them land. Pitching here cheapens the assessment.
    |
    v
WAIT — quiz completion check
    |
    |--- IF quiz NOT completed within 4 hours (not 2 — give her time):
    |       |
    |       v
    |   EMAIL 3: Gentle Nudge (4 hours post-purchase, conditional)
    |       - Subject: "Your assessment is waiting for you"
    |       - Tone: helpful, not nagging
    |       - "It takes about 10 minutes — and the insights are worth it"
    |       - Direct quiz link
    |       - SKIP if quiz completed (even mid-send — check tag at send time)
    |
    |--- IF quiz NOT completed by Day 2 morning:
    |       |
    |       v
    |   EMAIL 3b: Last Nudge (Day 2, 9am, conditional)
    |       - Subject: "Still curious about your hormones?"
    |       - Reframe value: "Most women are surprised by what they learn"
    |       - Quiz link
    |       - IF still not completed by Day 4: stop nudging. She's not going to.
    |         Apply tag: uha_quiz_abandoned. Move to general nurture.
    |
    v
DAY 3 (quiz completers only):
    |
    v
EMAIL 4: The "Now What" Email (Day 3, 9am)
    - Subject: "So now you know — here's what to do about it"
    - NOT a pitch. Educational bridge content:
        - IF estrogen_dominant: "3 things estrogen dominant women get wrong
          about diet" — genuine insight, positions Dr. P as the expert
        - IF balanced: "The #1 thing balanced women do that accidentally
          throws them off" — pattern interrupt, creates need for action
    - Soft CTA at bottom: "This is exactly what we work on in the 7-Day
      Challenge" — text link, not a button. Not a pitch. An FYI.
    |
    v
DAY 6:
    |
    v
EMAIL 5: Ascension Bridge (Day 6, 9am)
    - Subject: "Can I be honest with you about something?"
    - Dr. P voice: personal, direct
    - "Knowing your hormone profile is step one. But information without
      action is just trivia. The 7-Day Challenge is where we turn what you
      learned into actual changes in how you feel."
    - Testimonial: one woman's before/after with the Challenge
    - CTA → Challenge checkout page
    - IF already purchased Challenge (tag check): SKIP entirely
    |
    v
DAY 10:
    |
    v
EMAIL 6: Final Touch (Day 10, 9am — only if no Challenge purchase)
    - Subject: "One more thing about your results"
    - New angle: address the #1 objection ("I don't have time" or
      "I can figure this out myself")
    - Social proof: "X women have taken the Challenge this month"
    - CTA → Challenge checkout
    - IF purchased Challenge: SKIP
    - After this: UHA flow ends. Contact enters general nurture list.
```

**UHA Flow Summary:**
- Confirmation page: quiz starts immediately (no email dependency)
- Results page: full breakdown on-screen (email is the keepsake copy)
- Emails: 2-6 depending on behavior (down from 3-5, but higher quality)
- Ascension window: Day 6-10 (moved from Day 2-4 — let the results breathe)
- Systems: GHL (checkout, CRM, email) + Quiz platform + Results page
- Kajabi: NOT involved

---

# FLOW 2: 7-DAY HORMONE RESET & RECHARGE CHALLENGE — $47

**Checkout bump offer:** UHA ($47 add-on)

```
CHECKOUT PAGE (GHL)
    |
    v
PAYMENT PROCESSED (GHL)
    |
    |--- Apply tags: purchased_challenge, customer
    |--- IF bump accepted: purchased_uha (UHA flow starts Day 2, modified)
    |
    v
KAJABI ACCOUNT LOGIC (GHL)
    |
    |--- IF tag kajabi_account_created EXISTS: returning user
    |--- IF NOT: new user → apply tag kajabi_account_created
    |
    v
GRANT KAJABI ACCESS (GHL → Kajabi webhook)
    - Enroll in Challenge course (Day 1 unlocked, Days 2-7 dripped daily)
    |
    v
================================================================
CONFIRMATION PAGE — HER FIRST WIN HAPPENS HERE
================================================================
    - "You're in the Challenge!"
    - IF new Kajabi user:
        - Visual step-by-step (with screenshots):
          "Step 1: Check your email for a login setup message from Kajabi
           (it looks like this → [screenshot]). Click the link to create
           your password."
          "Step 2: Once you're logged in, Day 1 is already waiting for you."
        - Direct Kajabi course link (will work once password is set)
    - IF returning Kajabi user:
        - "Day 1 is live right now — jump in"
        - Direct Kajabi course link (instant access)
    - What to expect: "One module per day for 7 days. Each takes about
      15 minutes. By Day 7, you'll feel the difference."
    - Bonus preview: "You also get: meal plan, grocery list, training
      program lite, and 5 more bonuses — all inside the course"
    - IF UHA bump accepted: "Your Hormone Assessment is also ready —
      we'll send that tomorrow so you can focus on Day 1 first"
    |
    v
EMAIL 1: Welcome + Access (immediately)
    - Subject: "Your Challenge starts now — here's your login"
    - Backup of everything on the confirmation page
    - IF new Kajabi user: "Look for an email from Kajabi to set your
      password. It might be in spam. Here's what it looks like: [description]"
    - IF returning Kajabi user: direct link
    - Day 1 overview: what she'll do, time commitment (15 min)
    - Bonuses list
    - "Reply to this email and tell me: what's the #1 thing you want
      to change about how you feel?" (engagement trigger — reply creates
      GHL conversation, gives Dr. P's team a personal touchpoint)
    |
    v
DAY 2 (8am):
    |
    v
EMAIL 2: Day 2 Nudge + Day 1 Check-in
    - Subject: "Did you finish Day 1? (Be honest)"
    - Quick Day 1 accountability: "If you did Day 1 — amazing. If not,
      go do it now. It takes 15 minutes. I'll wait."
    - Day 2 teaser: "Today we talk nutrition — and I'm going to tell you
      the one thing most hormone 'experts' get completely wrong about food"
    - Kajabi link to Day 2
    |
    v
DAY 4 (8am):
    |
    v
EMAIL 3: Midpoint Momentum
    - Subject: "You're almost halfway — don't stop now"
    - "Days 1-3 laid the groundwork. Days 4-7 is where you actually
      start to FEEL different."
    - Day 4 topic teaser (hydration + hormone connection)
    - Kajabi link
    - IF no Kajabi login detected since purchase:
        - This email becomes the RE-ENGAGEMENT version instead:
        - Subject: "Hey [First Name] — you haven't logged in yet"
        - "I get it. Life happens. But you paid for this because
          something needed to change. Day 1 is still there. 15 minutes."
        - Direct Day 1 link
    |
    v
DAY 7 (8am):
    |
    v
EMAIL 4: Final Day — Finish Strong
    - Subject: "LAST DAY. Let's bring it home."
    - Day 7 topic: integration — pulling everything together
    - "After today, you'll have a complete hormone reset foundation"
    - Urgency: "Log in and finish Day 7 today"
    - Kajabi link
    |
    v
DAY 8 (9am):
    |
    v
EMAIL 5: Celebration + Reflection (NOT an upsell)
    - Subject: "7 days. Look at what you just did."
    - Pure celebration. No selling. This email exists to make her
      feel proud and to cement the transformation in her mind.
    - "Here's what changed in 7 days:"
      - Day 1: You set your intention
      - Day 3: You started eating for your hormones
      - Day 5: You addressed the stress-hormone connection
      - Day 7: You integrated it all into a system
    - "You're not the same person who started this Challenge."
    - Ask: "Hit reply and tell me your biggest win this week.
      I read every response." (builds connection for later ascension)
    |
    v
==================================================================
ASCENSION BRIDGE: CHALLENGE → MEM ($47 → $1,997)
This is NOT a 1-email pitch. This is a 2-week nurture bridge.
The price jump is 42x — she needs time, proof, and trust.
==================================================================
    |
    v
DAY 11 (9am):
    |
    v
EMAIL 6: The Gap Email
    - Subject: "The truth about 7-day challenges"
    - Dr. P voice, honest and direct:
      "Here's what I know after helping thousands of women: a 7-day
      reset gives you the spark. But sparks fade. The women who actually
      transform — who fix their hormones for good — they go deeper."
    - No CTA. No link. Just plants the seed. Let it sit.
    - IF already purchased MEM: SKIP all ascension emails
    |
    v
DAY 14 (9am):
    |
    v
EMAIL 7: The Proof Email
    - Subject: "She started exactly where you are"
    - Full testimonial/transformation story from a MEM graduate
      who started with the Challenge
    - Her before: same symptoms, same doubts
    - Her after: specific, measurable results
    - "She went from the Challenge into my Mastermind program.
      12 weeks later..." [results]
    - Soft mention: "The Madame Estrogen Mastermind" — name-drop only,
      no link yet. Let her Google it or ask.
    |
    v
DAY 17 (9am):
    |
    v
EMAIL 8: The Full Picture Email
    - Subject: "What 12 weeks with me actually looks like"
    - Now she knows the name. Now show the substance:
      - 12 modules covering [brief list]
      - Weekly accountability calls with Dr. P
      - Private community ("Empowered Sister Community")
      - 3-month HWN membership included
    - Address the elephant: "It's $1,997 — or $667/month for 3 months,
      or $497 down and $150/month. I'm not going to pretend that's nothing.
      But what's it costing you to keep feeling the way you feel?"
    - CTA → MEM checkout page
    |
    v
DAY 20 (9am):
    |
    v
EMAIL 9: Objection Buster + Final CTA
    - Subject: "The 3 things women ask me before they join"
    - FAQ-style: address real objections
      1. "Is it worth $2,000?" → ROI framing + payment plan
      2. "I'm not sure I'll follow through" → accountability calls +
         community + Dr. P's personal involvement
      3. "Can I just do this on my own?" → "You've been trying. How's
         that going?" (direct but caring)
    - Final CTA → MEM checkout
    - IF no click/purchase by Day 23: flow ends, contact enters
      general nurture. No more MEM pitches for 60 days.
```

**Challenge Flow Summary:**
- Confirmation page: clear password setup path + immediate Day 1 access
- Emails: 4 during Challenge (not 7), 1 celebration, 4 ascension bridge
- Total: 9 emails over 20 days (was 11 over 11 days — same count, better spacing)
- Ascension: 2-week warm bridge (Day 11-20), not a 1-day ambush (Day 9)
- Engagement check: Day 4 conditional (active vs. inactive get different emails)
- Systems: GHL + Kajabi

---

# FLOW 3: MADAME ESTROGEN MASTERMIND (MEM) — $1,997

**Checkout bump offer:** UHA ($47 add-on)
**Payment options:** Full pay $1,997 | 3x $667 | $497 down + 10x $150

```
CHECKOUT PAGE (GHL)
    |
    v
PAYMENT PROCESSED (GHL)
    |
    |--- Apply tags: purchased_mem, customer, high_value_customer
    |--- Apply: mem_paid_full OR mem_payment_plan
    |--- IF bump accepted: purchased_uha (UHA flow starts Day 3, modified)
    |
    v
KAJABI ACCOUNT LOGIC (GHL)
    |
    |--- IF kajabi_account_created: returning user
    |--- IF NOT: new user → apply tag
    |
    v
GRANT KAJABI ACCESS (GHL → Kajabi)
    - Enroll in MEM course (Week 1 unlocked, Weeks 2-12 dripped weekly)
    - Enroll in Empowered Sister Community
    |
    v
GRANT HWN BONUS ACCESS
    - Enroll in HWN inside Kajabi
    - Apply tags: hwn_bonus_active, hwn_bonus_start_[date]
    - DO NOT trigger HWN welcome flow
    |
    v
================================================================
CONFIRMATION PAGE — SHE JUST SPENT $2K. MAKE HER FEEL IT.
================================================================
    - "Welcome to the Mastermind, [First Name]. This is where
      everything changes."
    - This page should feel PREMIUM. Not a generic "thanks for
      your order." She just made a major investment.
    - Clear setup steps (with visuals):
      IF new Kajabi user:
          "Step 1: Check your email for a login from Kajabi [screenshot]"
          "Step 2: Set your password and log in"
          "Step 3: Jump into Week 1 — it's already unlocked"
      IF returning Kajabi user:
          "Step 1: Log into Kajabi — Week 1 is live"
    - "Join your community" — direct link to Empowered Sister Community
    - First accountability call: date, time, calendar add link
    - "What to expect over the next 12 weeks" — brief visual timeline
    - Bonus mention: "You also have full access to the Hormone Wellness
      Network for the next 3 months — we'll show you around later.
      Right now, focus on Week 1."
    |
    v
EMAIL 1: Welcome + Access (immediately)
    - Subject: "You're in the Mastermind. Here's everything you need."
    - Warm, personal tone: "I don't take this decision lightly, and
      neither should you. You just invested in yourself in a real way.
      Let me make sure it pays off."
    - Everything from the confirmation page (backup copy)
    - Kajabi login instructions (appropriate to new/returning)
    - Community link
    - First call date + calendar link
    - Payment plan schedule (if applicable)
    - "Your one job today: get logged in and watch the Week 1 intro.
      That's it. Don't try to do everything at once."
    |
    v
DAY 2 (9am):
    |
    v
EMAIL 2: Onboarding — How This Works
    - Subject: "Here's how to get the most out of the next 12 weeks"
    - NOT 4 hours after purchase (old flow). She's had a night to
      set up her account and look around.
    - The weekly rhythm:
      - New module drops every Monday
      - Accountability call on [day/time]
      - Community is your support system between calls
    - "Your first action: go to the community and introduce yourself.
      Tell us who you are and what you're hoping to change. The women
      in there will have your back for the next 12 weeks."
    - Link to community + link to Week 1 module
    |
    v
DAY 4 (9am):
    |
    v
EMAIL 3: Week 1 Accountability
    - Subject: "Have you started Week 1?"
    - "You've had a few days to get settled. Week 1 (Rejuvenation)
      sets the foundation for everything that comes after."
    - "If you haven't watched it yet — do it before our first call
      on [day]. You'll get so much more out of it."
    - Direct module link
    - Accountability call reminder
    |
    v
================================================================
WEEKS 2-12: SMART MODULE CADENCE (not 12 identical emails)
================================================================

Phase 1 — HABIT FORMATION (Weeks 2-4): Active weekly nudges
    |
    v
WEEK 2 (Monday, 8am):
EMAIL 4: "Week 2 is live: Nutrition"
    - Module overview + why it matters
    - Kajabi link + call reminder
    - "How did Week 1 land for you? Reply and tell me."
    |
    v
WEEK 3 (Monday, 8am):
EMAIL 5: "Week 3: Movement"
    - Module overview + Kajabi link + call reminder
    |
    v
WEEK 4 (Monday, 8am):
EMAIL 6: "Week 4: Hormones Deep Dive"
    - Module overview + Kajabi link + call reminder
    - "You're 1 month in. The women who finish this program are the
      ones who made it through the first month. You made it."

Phase 2 — MOMENTUM (Weeks 5-8): Milestone emails, not weekly nags
    |
    v
WEEK 5 (Monday, 8am):
    - Kajabi drips Week 5 (Toxins). NO email. She has the habit.
    |
    v
WEEK 6 (Monday, 8am):
EMAIL 7: Midpoint Milestone
    - Subject: "6 weeks. Halfway. Let's talk about what's changed."
    - NOT a generic "halfway there!" — ask a specific question:
      "What's one thing that's different now vs. 6 weeks ago?
      Reply and tell me. I share these (anonymously) with the
      community to inspire the women behind you."
    - Recap what she's covered (Weeks 1-6 topics)
    - "The second half goes deeper — gut health, stress, sleep,
      liver, supplements. This is where it gets transformational."
    - Community engagement prompt
    |
    v
WEEKS 7-8:
    - Kajabi drips Weeks 7-8. NO email. Let her work.
    |
    v

Phase 3 — FINISH LINE (Weeks 9-12): Re-engage for the push
    |
    v
WEEK 9 (Monday, 8am):
EMAIL 8: Final Stretch
    - Subject: "4 weeks left. Let's finish this the right way."
    - "You've done 8 weeks of deep work. The last 4 modules —
      liver, supplements, digestion, integration — pull everything
      together into a system that lasts."
    - Kajabi link
    - "Don't fade out now. Show up for these last 4 weeks like
      you showed up for the first."
    |
    v
WEEKS 10-11:
    - Kajabi drips content. NO email.
    |
    v
WEEK 12 (Monday, 8am):
EMAIL 9: Final Module
    - Subject: "Your last module is live. And I have something to say."
    - Personal message from Dr. P about the journey
    - Direct link to Week 12 (Integration & Transformation)
    - "Finish this module. Then look back at who you were 12 weeks ago.
      That's the whole point."
    |
    v
WEEK 12 + 3 DAYS:
    |
    v
==========================================================
GRADUATION (separate from any commercial message)
==========================================================
EMAIL 10: Graduation
    - Subject: "12 weeks. You did it."
    - Pure celebration. ZERO selling. ZERO mention of HWN.
    - "You committed to 12 weeks of deep, real work on your hormone
      health. Most people never do that. You did."
    - Invite to share: "Reply with your biggest transformation — or
      post it in the community. Your story will inspire someone
      who's on Week 2 right now."
    - Testimonial request (subtle): "Would you be open to sharing
      your experience? [link to simple form]"
    |
    v
WEEK 13 + 3 DAYS (approximately Day 95 — still within HWN bonus):
    |
    v
EMAIL 11: HWN Transition — The Soft Open
    - Subject: "So... what now?"
    - "The Mastermind gave you the transformation. But hormones don't
      stop changing just because the program ended."
    - Reintroduce HWN (which she's been using for 3 months as a bonus):
      "You've had access to the Hormone Wellness Network since you
      joined — the Q&As, masterclasses, the community. That access
      was included with your Mastermind for 3 months."
    - "Your bonus access runs through [date]. If you want to keep it,
      it's $47/month — less than $2/day to keep Dr. P in your corner."
    - CTA → HWN subscription checkout
    - Tone: no urgency, no scarcity. Just an honest "here's the deal."
    |
    v
7 DAYS BEFORE BONUS EXPIRY:
    |
    v
EMAIL 12: HWN Bonus Expiry — Clear and Direct
    - Subject: "Your HWN access ends [date]"
    - Recap what she's used: Q&As attended, masterclasses watched,
      community posts (pull actual data if possible)
    - "I don't want to lose you from the community."
    - CTA → HWN checkout ($47/mo or $470/yr — show annual savings)
    - "If it's not for you, no pressure. You have everything you need
      from the Mastermind. But if you want ongoing support, this is
      the easiest way to get it."
    |
    v
1 DAY BEFORE BONUS EXPIRY:
    |
    v
EMAIL 13: Final HWN Notice (only if NOT converted)
    - Subject: "Tomorrow your access ends — wanted you to know"
    - Short. No manipulation. "Your HWN bonus expires tomorrow.
      If you want to continue, here's the link: [link]. If not,
      it's been an honor having you in the community."
    - IF already purchased HWN: SKIP
    |
    v
BONUS EXPIRES:
    - Remove tag: hwn_bonus_active
    - IF NOT purchased_hwn: revoke HWN Kajabi access
    - IF purchased_hwn: no action (converted)

---

### MEM PAYMENT PLAN: DUNNING SEQUENCE

Only for mem_payment_plan contacts. Runs independently of content flow.
Tone: helpful and concerned, never threatening. She spent $2K — treat
her like a VIP with a billing hiccup, not a deadbeat.

PAYMENT FAILS (GHL webhook)
    |
    |--- Apply tag: mem_payment_failed
    |--- Internal alert to Dr. P team (immediate — high-value customer)
    |
    v
DUNNING EMAIL 1: Within 2 hours
    - Subject: "Quick heads up about your Mastermind payment"
    - "We tried to process your payment and it didn't go through —
      this happens all the time (expired card, bank hold, etc.)"
    - "Just update your payment method here: [link]"
    - "If you need help, reply to this email. We'll sort it out."
    - NO mention of access being at risk. Not yet.
    |
    v
DUNNING EMAIL 2: Day 3 (if still failed)
    - Subject: "Following up on your payment — need a hand?"
    - "Still seeing an issue with your payment. Want to make sure
      you don't lose momentum in the Mastermind."
    - Update payment link
    - "You can also reply and we'll hop on a quick call to fix it."
    |
    v
DUNNING EMAIL 3: Day 6 (if still failed)
    - Subject: "Last step to keep your Mastermind access"
    - Now mention access: "We need to resolve this in the next few
      days to keep your course and community access active."
    - Update payment link
    - "Reply or call [phone number] — we want to help."
    |
    v
DAY 10 PAST DUE — ACCESS PAUSED
    - Revoke Kajabi access (MEM course only, NOT community — let her
      keep community access for 7 more days as a grace period)
    - Apply tag: mem_access_paused
    - Internal notification to Dr. P team for personal outreach
    |
    v
DAY 17 PAST DUE — FULL ACCESS REVOKED
    - Revoke community access
    - Internal team should have attempted personal outreach by now
    |
    v
PAYMENT RECOVERED (at any point):
    - Remove: mem_payment_failed, mem_access_paused
    - Restore all Kajabi access
    - EMAIL: "You're all set — your access is back"
    - Personal touch: Dr. P team sends a quick "welcome back" DM
      in community
```

**MEM Flow Summary:**
- Confirmation page: premium feel, clear setup, visual timeline
- Onboarding: Day 1 + Day 2 + Day 4 (not Day 1 + 4 hours later)
- Module emails: 9 strategic emails over 12 weeks (not 12 weekly copy-paste)
  - Weeks 1-4: weekly (habit formation)
  - Weeks 5-8: midpoint milestone only (habit is set)
  - Weeks 9-12: final stretch + finale (re-engage for finish)
- Graduation: standalone celebration, no upsell
- HWN transition: 3-email sequence starting ~Day 95, not Day 84
- Dunning: warmer tone, 10-day grace before access pause (not 7)
- Total emails: 13 content + 3 dunning max = 16 (down from 21)

---

# FLOW 4: HORMONE WELLNESS NETWORK (HWN) — $47/mo or $470/yr

```
CHECKOUT PAGE (GHL)
    |
    |--- Payment type: monthly ($47/mo) or annual ($470/yr)
    |
    v
PAYMENT PROCESSED (GHL)
    |
    |--- Apply tags: purchased_hwn, customer
    |--- Apply: hwn_monthly OR hwn_annual
    |--- IF from MEM bonus conversion: hwn_converted_from_mem
    |
    v
KAJABI ACCOUNT LOGIC (GHL)
    |
    |--- IF kajabi_account_created: returning user
    |--- IF NOT: new user → apply tag
    |
    v
GRANT KAJABI ACCESS (GHL → Kajabi)
    - Enroll in HWN content + community
    |
    v
================================================================
CONFIRMATION PAGE — MAKE HER FEEL LIKE SHE JOINED SOMETHING
================================================================
    - "You're part of the Network now."
    - Not transactional. This is a COMMUNITY welcome.
    - IF new Kajabi user: password setup steps with visual
    - IF returning Kajabi user: direct login link
    - "Here's what's happening right now in the Network:"
      - Next Q&A with Dr. P: [date/time] + calendar add
      - Next masterclass: [topic] on [date] + calendar add
      - Community highlight: "[Member name] just posted about [topic]"
    - "Your first move: introduce yourself in the community.
      Tell us who you are and what brought you here."
    |
    v
EMAIL 1: Welcome (immediately)
    - Subject: "Welcome to the Network, [First Name]"
    - Backup of confirmation page content
    - Kajabi access instructions (new vs. returning)
    - Community link
    - Upcoming events with calendar links
    - "Your one action item today: post your intro in the community.
      That's it. Everything else can wait."
    - Tone: warm, community-first. Not a feature list dump.
    |
    v
DAY 3 (9am):
    |
    v
EMAIL 2: The Rhythm
    - Subject: "Here's how this works (it's simpler than you think)"
    - Don't dump everything at once. Just the rhythm:
      - "Twice a month: Q&A with me (Dr. P). Bring your questions."
      - "Once a month: live masterclass on a focused topic + replay"
      - "Every week: accountability check-in to keep you on track"
      - "Always: the community — your people who get it"
    - "The best way to get value from this: show up to ONE live
      session this month. That's it. Just one."
    - IF member has NOT logged into Kajabi or community yet:
        - Add: "I noticed you haven't logged in yet. Need help?
          Reply to this email and I'll walk you through it."
    |
    v
ONGOING — MONTHLY DIGEST MODEL (replaces 6 scattered emails)
================================================================
One email per month + day-of live event reminders. That's it.
================================================================
    |
    v
MONTHLY DIGEST (1st of each month, 9am):
    |
    v
EMAIL: "What's happening in the Network this month"
    - Subject: "[Month] in the Network: [masterclass topic] + more"
    - THIS MONTH'S SCHEDULE:
      - Masterclass: [Topic] on [date] at [time]
      - Q&A #1: [date] at [time]
      - Q&A #2: [date] at [time]
    - LAST MONTH RECAP (for members past Month 1):
      - Masterclass replay link (if they missed it)
      - Top community conversation or win
    - One-click calendar add buttons for all events
    - "If you only do one thing this month: come to the masterclass."
    |
    v
LIVE EVENT DAY-OF REMINDERS (morning of each live event):
    |
    v
EMAIL: Day-of Reminder (morning of masterclass or Q&A)
    - Subject: "Today at [time]: [Masterclass/Q&A] with Dr. P"
    - Short. 3 lines max:
      "Today's [masterclass/Q&A] is at [time]."
      "[One sentence about the topic or how to submit questions]"
      "[Join link]"
    |
    v
SMS (optional, if opted in): 30 minutes before live event
    - "Dr. P goes live in 30 min! Join: [link]"
    - Only for contacts who opted in to SMS at checkout or via
      preference center. Never default-on.
    |
    v
MASTERCLASS REPLAY (day after masterclass):
    |
    v
EMAIL: Replay Available
    - Subject: "Replay: [Masterclass Topic]"
    - For people who DIDN'T attend live (attendance tracked via
      Kajabi/Zoom/whatever platform):
      "Missed yesterday's masterclass? Here's the replay: [link]"
    - For people who DID attend: SKIP (they already got the value —
      don't clutter their inbox with a link to something they watched)
    |
    v
================================================================
RETENTION: ENGAGEMENT-BASED, NOT CALENDAR-BASED
================================================================
No "your membership renews in 5 days" email. Silent renewal.
Instead: engagement monitoring that PREVENTS churn before it starts.

ENGAGEMENT SCORING (GHL automation, monthly check):
    |
    |--- ACTIVE (2+ of: attended live event, community post, course
    |    login in last 30 days):
    |       Tag: hwn_engaged
    |       Action: none needed. She's getting value. Leave her alone.
    |
    |--- AT RISK (0-1 engagement signals in last 30 days):
    |       Tag: hwn_at_risk
    |       |
    |       v
    |   RE-ENGAGEMENT EMAIL (triggered by at_risk tag, once per 60 days max)
    |       - Subject: "Haven't seen you lately — everything okay?"
    |       - NOT guilt-trippy. Genuinely checking in.
    |       - "I noticed you haven't been around the Network lately.
    |         Life gets busy — I get it."
    |       - Highlight ONE specific thing she's missing: "This month's
    |         masterclass on [topic] is [date] — it's a good one."
    |       - "If something's not working for you, reply and tell me.
    |         I'd rather fix it than lose you."
    |       - IF no engagement within 14 days of this email:
    |           Internal flag → Dr. P team does personal outreach
    |           (DM in community or personal email from team member)
    |
    |--- POWER USER (attended every live event + active in community):
    |       Tag: hwn_power_user
    |       Action: candidate for testimonial request, community
    |       spotlight, or MEM referral program (future optimization)
    |
    v
================================================================
DUNNING: WARM + EFFICIENT
================================================================

RENEWAL PROCESSED (GHL):
    |
    |--- IF successful: SILENT. No email. No "you've been charged."
    |    Happy members don't want payment reminders.
    |
    |--- IF failed:
    |       Apply tag: hwn_payment_failed
    |       |
    |       v
    |   DUNNING EMAIL 1: Within 2 hours
    |       - Subject: "Quick note about your Network membership"
    |       - "Your payment didn't go through — probably just an
    |         expired card or bank hold."
    |       - Update payment link
    |       - "Takes 30 seconds to fix: [link]"
    |
    |   DUNNING EMAIL 2: Day 3 (if still failed)
    |       - Subject: "Still need to update your payment method"
    |       - Update link + "reply if you need help"
    |
    |   DUNNING EMAIL 3: Day 6 (if still failed)
    |       - Subject: "Your Network access needs attention"
    |       - "We need to hear from you in the next few days to
    |         keep your membership active."
    |       - Update link + phone number
    |
    |   DAY 10 PAST DUE:
    |       - Revoke Kajabi access
    |       - Apply tag: hwn_churned
    |       - Internal notification for personal outreach
    |
    v
================================================================
CANCELLATION: GRACEFUL EXIT + REAL WIN-BACK
================================================================

CANCELLATION REQUEST:
    |
    |--- Apply tag: hwn_cancel_requested
    |--- Internal alert to Dr. P team
    |
    v
EMAIL: Cancellation Confirmed
    - Subject: "Your membership cancellation"
    - Confirm: "Your cancellation has been processed. You'll have
      access through [end of billing period date]."
    - One-question exit survey: "Would you mind telling me why?
      It takes 10 seconds and genuinely helps me improve:
      [link to 1-question form with options:
       - Too expensive
       - Not enough time to use it
       - Didn't feel like I was getting value
       - Got what I needed
       - Other]"
    - "If you ever want to come back, the door is always open."
    - No guilt. No hard save attempt. Graceful exit.
    |
    v
ACCESS EXPIRES (end of billing period):
    - Revoke Kajabi HWN access
    - Finalize tag: hwn_churned
    |
    v
WIN-BACK SEQUENCE (longer, smarter — this is the #1 churn problem):
    |
    v
DAY 14 POST-CHURN:
EMAIL: Win-Back 1 — The Update
    - Subject: "Here's what's been happening in the Network"
    - NOT "we miss you" — that's needy. Instead, show value:
      "Since you left, here's what happened:"
      - [This month's masterclass topic + one key insight]
      - [Community highlight or member win]
    - "If any of that sounds useful, you can rejoin anytime: [link]"
    - Casual. No pressure.
    |
    v
DAY 30 POST-CHURN:
EMAIL: Win-Back 2 — The Personal Note
    - Subject: "Can I ask you something?"
    - Short, from Dr. P:
      "I looked at your exit survey [if completed] and I wanted you
      to know we [specific action taken based on feedback].
      If [reason they left] was the issue, I think you'd see a
      difference now."
    - IF exit survey said "too expensive": offer annual plan at
      $470/yr ($39/mo effective — save $94/yr vs. monthly)
    - CTA → rejoin link
    |
    v
DAY 45 POST-CHURN:
EMAIL: Win-Back 3 — Social Proof
    - Subject: "What [member name] said about coming back"
    - Testimonial from someone who cancelled and came back
    - "She left for 2 months, came back, and said [quote]"
    - CTA → rejoin link
    |
    v
DAY 60 POST-CHURN:
EMAIL: Win-Back 4 — Final Touch
    - Subject: "One last thing from me"
    - "I'm not going to keep emailing you about this. You know
      where to find us if you want to come back."
    - "But I wanted to leave you with this: [one powerful stat
      or insight about hormone health maintenance — free value,
      no pitch]"
    - "Take care, [First Name]. — Dr. P"
    - Small text link at bottom: "Rejoin the Network"
    - After this: DONE. No more win-back. Contact moves to
      general nurture list. Can be reactivated through regular
      content marketing.
    |
    v
IF RE-SUBSCRIBED at any point:
    - Remove: hwn_churned, hwn_cancel_requested
    - Apply: purchased_hwn, hwn_returning_member
    - Restore Kajabi access
    - Welcome-back email: "Good to have you back. Here's what's
      happening this month: [current month digest]"
    - Skip full onboarding (she already knows how it works)
```

**HWN Flow Summary:**
- Confirmation page: community-first welcome, upcoming events, calendar links
- Onboarding: 2 emails (Day 1 + Day 3) — not 3 with a pointless Day 5 check-in
- Monthly: 1 digest + day-of reminders + replay for non-attendees only
  - ~2-3 emails/month (down from ~6)
- Retention: engagement-based scoring (active/at-risk/power-user), not calendar reminders
- NO pre-renewal email (silent renewal — stops triggering cancellations)
- Dunning: 3-email sequence, warm tone, 10-day grace
- Win-back: 4 emails over 60 days (up from 2 over 30 — matches the churn severity)
- Cancellation: graceful, exit survey feeds win-back personalization

---

# CROSS-PROGRAM LOGIC (v2)

## Tag Architecture (GHL)

### Purchase Tags
| Tag | When |
|-----|------|
| `customer` | Any purchase |
| `purchased_uha` | UHA bought |
| `purchased_challenge` | Challenge bought |
| `purchased_mem` | MEM bought |
| `purchased_hwn` | HWN bought (paid, not bonus) |
| `high_value_customer` | MEM or HWN annual |

### Product State Tags
| Tag | When |
|-----|------|
| `kajabi_account_created` | First Kajabi product (set once, never removed) |
| `uha_completed` | Quiz finished |
| `uha_result_estrogen_dominant` | Quiz result |
| `uha_result_balanced` | Quiz result |
| `uha_quiz_abandoned` | Quiz not taken by Day 4 |
| `hwn_bonus_active` | MEM buyer's 3-month HWN |
| `hwn_bonus_start_[date]` | When HWN bonus started |

### Payment Tags
| Tag | When |
|-----|------|
| `mem_paid_full` | MEM paid in full |
| `mem_payment_plan` | MEM on installments |
| `mem_payment_failed` | Installment declined |
| `mem_access_paused` | MEM access revoked for non-payment |
| `hwn_monthly` | HWN monthly subscriber |
| `hwn_annual` | HWN annual subscriber |

### Lifecycle Tags
| Tag | When |
|-----|------|
| `hwn_engaged` | Active in last 30 days (2+ signals) |
| `hwn_at_risk` | Inactive in last 30 days (0-1 signals) |
| `hwn_power_user` | Highly active (all events + community) |
| `hwn_payment_failed` | HWN renewal declined |
| `hwn_cancel_requested` | Cancellation initiated |
| `hwn_churned` | HWN lapsed or cancelled |
| `hwn_converted_from_mem` | Converted from MEM bonus |
| `hwn_returning_member` | Rejoined after churning |

## Email Throttle Rules
- Max 1 email/day per contact (except purchase confirmations)
- Priority: Transactional > Active program > Onboarding > Ascension
- Bump offer flows start Day 2 (not same day as primary purchase)
- Ascension emails: always check purchase tags before sending — skip if already bought

## Confirmation Page Priority
- The confirmation page is the primary delivery mechanism
- Emails are the backup/keepsake copy
- Every confirmation page follows the structure:
  1. Celebration / emotional payoff
  2. Immediate next action (ON this page, not "check email")
  3. What happens next (timeline/expectations)
  4. "We also sent this to your inbox"

## Voice Guidelines
- Write like Dr. P talking to a patient she cares about
- No marketing jargon: "ascension," "conversion," "funnel" never appear
- Subject lines: conversational, curiosity-driven, never formatted as "Day X: Topic"
- Emails are short. If it takes more than 90 seconds to read, cut it in half.
- CTAs: text links feel personal. Buttons feel like marketing. Use text links
  for relationship emails. Buttons only for transactional (login, update payment).

## Sending Windows
- Transactional (confirmations, dunning): immediately, any time
- Content + onboarding: 8-9am in contact's timezone
- Ascension: 9-10am in contact's timezone
- Live event day-of reminders: morning of event
- SMS (opt-in only): 30 min before live events
- Never send non-transactional emails between 9pm-7am

## Contact Lifecycle After Flows End
- UHA-only (no Challenge purchase after Day 10): → general nurture list
- Challenge-only (no MEM purchase after Day 23): → general nurture list
- MEM complete (no HWN conversion after bonus expiry): → general nurture list
- HWN churned (no win-back conversion after Day 60): → general nurture list
- General nurture: monthly value email from Dr. P (education, not sales).
  Re-entry to any product flow happens naturally through content marketing.
