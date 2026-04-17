# Email Copy: UHA
### Every email written in full — Dr. P voice, brand-first and concise

**From name:** Dr. P
**From email:** info@callmedoctorp.com
**Reply-to:** info@callmedoctorp.com (replies create GHL conversation)

---

# UHA EMAILS (7 templates, 2 with conditional variants)

---

## UHA-1: Backup Confirmation

**Trigger:** Immediate on purchase
**Workflow:** UHA — Post-Purchase
**Conditional:** None

```
SUBJECT: Your assessment link, in case you need it

PREHEADER: You should've already started on the last page — this is your backup.

---

Hey [First Name],

If you're already taking your Hormone Assessment, keep going.

This email is just here in case life interrupted you or that page got closed.

If that happened, here is your link:

👉 Take Your Assessment Now → [QUIZ URL]

It takes about 10 minutes.

Answer honestly. The more honest you are, the more useful your results will be.

Your personalized results show up the moment you finish.

Talk soon,
Dr. P

---
Order summary:
Ultimate Hormone Assessment — $47
[Order details / receipt]
```

---

## UHA-2: Hormone Report (ESTROGEN DOMINANT VERSION)

**Trigger:** Immediate on quiz completion (webhook)
**Workflow:** UHA — Quiz Results
**Conditional:** uha_result_type = estrogen_dominant

```
SUBJECT: [First Name], your hormone results

PREHEADER: Here's what your assessment revealed — save this email.

---

[First Name],

Your results are in. Save this email. This is your personal hormone report.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YOUR RESULT: ESTROGEN DOMINANT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What this means:

Your body is producing or retaining more estrogen than it can efficiently clear. I see this all the time. And when it goes unaddressed, women usually feel it as bloating, mood swings, stubborn weight around the middle, heavy or irregular periods, breast tenderness, fatigue, and brain fog.

You don't have to live with it.


YOUR TOP 3 CONTRIBUTING FACTORS:

Based on your answers, here's what's likely driving your estrogen dominance:

1. Sluggish estrogen metabolism — your liver isn't clearing excess estrogen efficiently, so it recirculates in your system

2. Gut health disruption — when gut bacteria are out of balance, an enzyme called beta-glucuronidase reactivates estrogen your body already tried to eliminate

3. Environmental estrogen exposure — xenoestrogens from plastics, personal care products, and processed foods are adding to your estrogen load


3 THINGS YOU CAN DO THIS WEEK:

These do not have to be complicated. Begin with this:

1. Eat cruciferous vegetables daily — broccoli, cauliflower, Brussels sprouts, kale. These contain DIM and I3C, which directly support estrogen detoxification. Aim for 1-2 cups a day.

2. Swap one plastic container for glass — every time you heat food in plastic, you're adding xenoestrogens. Start with whatever you use most.

3. Add ground flaxseed to your morning — 2 tablespoons daily. Flax contains lignans that help your body process and eliminate excess estrogen. Sprinkle it on anything.


These are starting points, not the whole plan. But if you do these three things consistently for 7 days, you may be surprised by what shifts.

Your full results are also saved here: [RESULTS PAGE URL]


This is what your hormones are telling you right now. The next question is what you want to do with that information.

— Dr. P

P.S. I'm not pitching you in this email. You paid for an assessment, and you got one. Let these results sit for a day or two. I'll check in soon.
```

---

## UHA-2: Hormone Report (BALANCED VERSION)

**Trigger:** Immediate on quiz completion (webhook)
**Workflow:** UHA — Quiz Results
**Conditional:** uha_result_type = balanced

```
SUBJECT: [First Name], your hormone results

PREHEADER: Here's what your assessment revealed — save this email.

---

[First Name],

Your results are in. Save this email. This is your personal hormone report.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YOUR RESULT: HORMONALLY BALANCED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What this means:

Good news: based on your answers, your hormones are in a balanced range. That's a good sign, and it means something in your current habits is working.

But balanced does not mean bulletproof.

Hormone balance shifts with stress, sleep, diet, age, and environmental exposure. What looks balanced now can drift if the conditions change, and for most women they do.

The goal isn't just balance. It's building the daily habits that KEEP you balanced, especially through the transitions ahead.


YOUR TOP 3 STRENGTHS TO MAINTAIN:

Based on your answers, here's what's working in your favor:

1. Stress management — your current lifestyle is keeping cortisol from overwhelming your other hormones. Protect this. Cortisol is the first domino that knocks everything else down.

2. Nutritional foundation — your food choices are supporting hormone production and metabolism. The basics are in place.

3. Sleep quality — you're giving your body the recovery window it needs for hormone regulation. This is more important than most people realize.


3 OPTIMIZATION MOVES:

You're balanced. Now protect it:

1. Prioritize liver support — your liver is your primary estrogen processing organ. Add lemon water in the morning, increase leafy greens, and minimize alcohol. Your liver doesn't need a "detox" — it needs less to detox FROM.

2. Track your cycle patterns — even balanced hormones shift throughout your cycle. Start noting energy, mood, and symptoms by week. You'll spot changes early instead of after they've cascaded.

3. Reduce environmental hormone disruptors — switch to clean personal care products and avoid heating food in plastic. This isn't about perfection — it's about reducing the load so your body can stay where it is.


Your full results are also saved here: [RESULTS PAGE URL]


You're in a good place. The smart move is making sure you stay there.

— Dr. P

P.S. No pitch coming. You paid for an assessment and you got one. I'll check in soon with something you might find useful.
```

---

## UHA-3: Quiz Nudge 1

**Trigger:** 4 hours after purchase, IF uha_completed tag is absent
**Workflow:** UHA — Post-Purchase
**Conditional:** Only sends if quiz NOT completed

```
SUBJECT: Your assessment is waiting for you

PREHEADER: 10 minutes → personalized hormone insights. You already paid for it.

---

Hey [First Name],

Just circling back because your assessment is still waiting for you.

No pressure. I just do not want you to pay for insight and then never get it.

👉 Take Your Assessment Now → [QUIZ URL]

It is quick, it is personal, and your results show up right away.

The sooner you take it, the sooner we stop guessing.

— Dr. P
```

---

## UHA-3b: Quiz Nudge 2

**Trigger:** Day 2, 9am, IF uha_completed tag is still absent
**Workflow:** UHA — Post-Purchase
**Conditional:** Only sends if quiz NOT completed

```
SUBJECT: Still curious about your hormones?

PREHEADER: Your assessment is ready whenever you are.

---

[First Name],

Just checking in because you still have not taken your Hormone Assessment.

I know life gets busy. But you signed up for this because something felt off, or because you wanted to know where you stand. That part has not changed.

Here is your link: [QUIZ URL]

10 minutes. That's it. Your results appear the moment you finish, and most women tell me they learn something important right away.

Whenever you're ready, it is here for you.

— Dr. P
```

---

## UHA-4: The Now-What Email (ESTROGEN DOMINANT VERSION)

**Trigger:** Day 3, 9am (quiz completers only)
**Workflow:** UHA — Post-Purchase
**Conditional:** uha_result_type = estrogen_dominant

```
SUBJECT: So now you know — here's what to do about it

PREHEADER: 3 things estrogen dominant women get wrong about diet.

---

[First Name],

A few days ago you found out you're estrogen dominant. That matters, because now we can stop guessing and be more strategic.

Before you Google "estrogen dominance diet" and end up with 40 tabs open, let me save you some time.

Here are 3 things estrogen dominant women get wrong about food:

1. They cut calories instead of cutting the right things.
Estrogen dominance isn't a calorie problem. It's a metabolism and elimination problem. You can eat 1,200 calories a day and still have excess estrogen recirculating because your liver and gut aren't processing it out. Stop starving yourself. Start supporting your detox pathways.

2. They avoid all fats.
Your hormones are MADE from fat. Cholesterol is the raw material for estrogen, progesterone, and testosterone. The issue isn't fat — it's the wrong fats. Seed oils and trans fats increase inflammation and make estrogen dominance worse. Avocado, olive oil, wild-caught fish, and nuts support hormone production without feeding the problem.

3. They ignore their gut.
Here's something most women don't know: there's a collection of bacteria in your gut called the estrobolome. Its entire job is regulating how much estrogen stays in your body vs. how much gets eliminated. When your gut is out of balance, that system breaks down — and estrogen that was supposed to leave your body gets reabsorbed. Fiber, fermented foods, and probiotics aren't optional when you're estrogen dominant. They're foundational.

This is the kind of thing I go deep on in the 7-Day Hormone Reset & Recharge Challenge — it's 7 days of focused work on exactly what your body needs.

But for now, just start with what I sent you in your results. Those 3 action items are your foundation.

Talk soon,
Dr. P
```

---

## UHA-4: The Now-What Email (BALANCED VERSION)

**Trigger:** Day 3, 9am (quiz completers only)
**Workflow:** UHA — Post-Purchase
**Conditional:** uha_result_type = balanced

```
SUBJECT: So now you know — here's how to protect it

PREHEADER: The #1 thing balanced women do that accidentally throws them off.

---

[First Name],

Your results came back balanced, and that is good news.

But there's something I see all the time with women in your position, and I want to flag it before it happens to you.

The most common mistake I see in hormonally balanced women is this: they stop paying attention.

"I'm fine" becomes "I don't need to worry about this" becomes "I'll deal with it later" becomes "wait, why do I feel terrible and when did that start?"

By the time most women notice their hormones have shifted, they're 3-6 months into the problem. The bloating, the brain fog, the fatigue, the sleep disruption — it didn't start overnight. It crept in while they weren't tracking.

Here's what I'd recommend while you're still balanced:

Build the daily habits NOW that catch changes early:

→ Track your energy and mood by week — just a 1-10 score in your phone notes. When the pattern shifts, you'll see it immediately instead of months later.

→ Protect your stress response. Cortisol is the first domino. When stress stays chronically elevated, it steals progesterone (your calming hormone) to make more cortisol. That's the beginning of the cascade.

→ Keep your liver happy. It's doing the heavy lifting on hormone metabolism. Less alcohol, more cruciferous vegetables, adequate hydration. Not glamorous. Extremely effective.

This is what I work on with women in the 7-Day Challenge — not just fixing problems, but building the system that prevents them.

For now, keep doing what you're doing. And keep watching.

— Dr. P
```

---

## UHA-5: Ascension Bridge

**Trigger:** Day 6, 9am
**Workflow:** UHA — Post-Purchase
**Conditional:** SKIP if purchased_challenge tag exists

```
SUBJECT: Can I be honest with you about something?

PREHEADER: I've been thinking about your results.

---

[First Name],

I've been thinking about your results since you took the assessment.

Here's what I know after 16 years as an OB-GYN and helping thousands of women with their hormones: information doesn't change how you feel. Action does.

Your assessment told you where you stand. That matters — most women are guessing. You're not. But knowing you're [estrogen dominant / balanced] doesn't actually shift your hormones. Knowing what cruciferous vegetables do doesn't put them on your plate. Knowing stress affects cortisol doesn't change how you handle your 3pm crash.

The gap between "I know what to do" and "I'm actually doing it" is where most women get stuck. Not because they're lazy. Because nobody gave them a system.

That's why I built the 7-Day Hormone Reset & Recharge Challenge.

7 days. One focused module each morning. Nutrition, movement, hydration, stress, sleep — each one targeted at what your hormones actually need. Plus a meal plan, grocery list, and training program so you're not figuring it out alone.

It's $47. It takes 15 minutes a day. And by Day 7, you'll feel the difference.

I built this for women who already know something needs to change — they just need the structure to make it happen.

If that's you: [CHALLENGE CHECKOUT URL]

If it's not — no pressure. Your assessment results are yours to keep, and everything I sent you still applies.

— Dr. P
```

---

## UHA-6: Final Touch

**Trigger:** Day 10, 9am
**Workflow:** UHA — Post-Purchase
**Conditional:** SKIP if purchased_challenge tag exists. After this email: END workflow → general nurture.

```
SUBJECT: One more thing about your results

PREHEADER: This was on my mind and I wanted to share it.

---

[First Name],

Last email about your assessment — I promise.

When I look at your results, here's what I see: a woman who took the time to find out where she actually stands. That puts you ahead of 95% of women who just keep guessing and Googling and hoping something changes.

But I also know that a week from now, life takes over. The assessment becomes something you "did that one time." The action items become something you "meant to get to." And slowly, nothing changes.

I don't want that for you.

If you're thinking about the 7-Day Challenge but haven't pulled the trigger, I want you to ask yourself one question:

If nothing changes in the next 30 days, will you be okay with that?

If the answer is yes — great. Truly. Keep your results, use the tips I gave you, and take care of yourself.

If the answer is no — here's the link: [CHALLENGE CHECKOUT URL]

7 days. 15 minutes a day. $47. And a real plan for what to do with what you now know.

Either way, I'm glad you took the assessment. Knowledge is never wasted.

Take care,
Dr. P
```

---

# EMAIL TOTAL: UHA

| Flow | # | Templates | Conditional Variants |
|------|---|-----------|---------------------|
| UHA | 7 | UHA-1, UHA-2 (x2), UHA-3, UHA-3b, UHA-4 (x2), UHA-5, UHA-6 | UHA-2 and UHA-4 each have ED/Balanced versions |
