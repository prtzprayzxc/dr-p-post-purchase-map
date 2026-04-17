# 7-Day Challenge Post-Purchase Flow
## Focused flow for buyers of the Hormone Reset & Recharge Challenge

---

## Purpose

This document defines the post-purchase flow for the `7-Day Hormone Reset & Recharge Challenge` only.

It covers:
- what happens immediately after purchase
- what the buyer sees on the confirmation page
- what emails send and when
- what behavioral branches matter
- what should happen after the 7 days are over

This is the focused post-purchase flow, not the full ecosystem strategy.

---

## Core Goal

The post-purchase flow has one primary job:

Get the buyer into `Day 1` quickly and keep her moving through the Challenge without over-emailing her.

Secondary job:

After the Challenge ends, bridge her toward `MEM` gradually instead of pitching too early.

---

## Flow Summary

### Immediate post-purchase

- Payment succeeds in `GHL`
- Tags applied: `customer`, `purchased_challenge`
- Kajabi enrollment triggers
- Contact is treated as either:
  - new Kajabi user
  - returning Kajabi user
- Buyer is redirected to the Challenge confirmation page
- Immediate welcome/access email sends

### During the 7-day Challenge

- `Day 2`: accountability check
- `Day 4`: momentum email or re-engagement email
- `Day 7`: final-day push
- `Day 8`: celebration email

### After the Challenge

- `Day 11`: seed email for `MEM`
- `Day 14`: testimonial/proof email
- `Day 17`: full picture of `MEM`
- `Day 20`: objection handling + final CTA

---

## Post-Purchase Flow Logic

```text
PURCHASE: 7-Day Challenge
    |
    |-- Apply tags: customer, purchased_challenge
    |-- Trigger Kajabi enrollment
    |
    v
CHECK KAJABI STATUS
    |
    |-- If existing Kajabi account: returning user
    |-- If no Kajabi account: new user
    |
    v
REDIRECT TO CHALLENGE CONFIRMATION PAGE
    |
    v
SEND IMMEDIATE WELCOME EMAIL
    |
    v
DAY 2 EMAIL
    |
    v
DAY 4 BRANCH
    |-- If logged into Kajabi: momentum version
    |-- If not logged in: re-engagement version
    |
    v
DAY 7 EMAIL
    |
    v
DAY 8 CELEBRATION
    |
    v
DAY 11-20 MEM BRIDGE
    |-- Skip if purchased_mem
    |
    v
END
```

---

## Confirmation Page

The confirmation page is the most important part of the post-purchase flow.

It should do more work than the first email.

### Required content

- Celebration headline:
  `You're in the Challenge!`

- Access instructions:
  - If new Kajabi user:
    - look for the Kajabi setup email
    - explain that it is a separate email
    - tell her to check spam if needed
    - tell her Day 1 is waiting once password is set
  - If returning Kajabi user:
    - tell her to log in with her existing Kajabi password
    - give direct course link

- Day 1 framing:
  - Day 1 is already unlocked
  - takes about 15 minutes
  - do Day 1 today

- Expectations:
  - 7 days
  - 1 module per day
  - simple daily action

- Bonus preview:
  - meal plan
  - grocery list
  - training program lite
  - other included bonuses

### What the page should not do

- do not pitch `MEM`
- do not make email the primary next step
- do not overwhelm with too many actions

---

## Email Flow

## Email 1: Welcome + Access

### Timing

Immediate on purchase

### Purpose

Get her into the course and reduce Kajabi confusion.

### Version A: New Kajabi user

Main points:
- you are in
- look for a separate Kajabi email
- set password there
- then start Day 1
- reply with your #1 goal for the next 7 days

### Version B: Returning Kajabi user

Main points:
- you are in
- use your existing Kajabi login
- Day 1 is live now
- reply with your #1 goal for the next 7 days

### Email job

The email is backup for access plus a reply prompt.

It is not a sales email.

---

## Email 2: Day 2 Check-In

### Timing

Day 2 at `8:00 AM`

### Purpose

Make sure she starts and connect Day 1 to Day 2.

### Main message

- Did you finish Day 1?
- If yes, great, keep going.
- If not, go do it now.
- Today is nutrition.
- Direct link to the course.

### Tone

Direct, accountable, not guilty or preachy.

---

## Email 3: Day 4 Midpoint Branch

### Timing

Day 4 at `8:00 AM`

### Purpose

Split engaged buyers from silent buyers.

### Branch rule

Use `last_kajabi_login`.

- If logged in since purchase:
  send active version
- If not logged in:
  send inactive version

### Active version

Subject direction:
`You're almost halfway — don't stop now`

Main message:
- Days 1-3 built the foundation
- Days 4-7 are where it starts to click
- keep going

### Inactive version

Subject direction:
`Hey [First Name] — you haven't logged in yet`

Main message:
- no judgment
- you do not need to catch up
- just start with Day 1
- reply if access is broken

---

## Email 4: Day 7 Final Push

### Timing

Day 7 at `8:00 AM`

### Purpose

Push completion of the final module.

### Main message

- this is Day 7
- everything comes together today
- do not leave the Challenge unfinished
- direct course link

### Tone

Urgent in a completion sense, not a fake scarcity sense.

---

## Email 5: Day 8 Celebration

### Timing

Day 8 at `9:00 AM`

### Purpose

Make the buyer feel proud of completing the week.

### Main message

- look at what you did in 7 days
- recap the week
- reinforce that she is not the same person who started
- ask her to reply with her biggest win

### Rule

No upsell in this email.

This is important. If this becomes a pitch, the flow cheapens the Challenge and weakens the later `MEM` bridge.

---

## Ascension Bridge: Challenge to MEM

This starts after the Challenge is complete.

It should feel like a thoughtful continuation, not an ambush.

### Global rule

Skip all `MEM` bridge emails if tag `purchased_mem` exists.

---

## Email 6: Day 11 The Gap

### Timing

Day 11 at `9:00 AM`

### Purpose

Plant the idea that a 7-day reset is a start, not the full solution.

### Main message

- the Challenge works
- but 7 days creates a spark, not long-term transformation
- deeper work is what creates lasting change

### CTA

No CTA link required.

---

## Email 7: Day 14 The Proof

### Timing

Day 14 at `9:00 AM`

### Purpose

Show what happens when someone continues into `MEM`.

### Main message

- tell one transformation story
- connect Challenge result to Mastermind outcome
- make the path feel believable

### CTA

Soft only. This email can remain story-first.

---

## Email 8: Day 17 The Full Picture

### Timing

Day 17 at `9:00 AM`

### Purpose

Explain what `MEM` actually is.

### Main message

- 12 weeks
- modules
- accountability calls
- community
- HWN bonus
- pricing options

### CTA

Direct CTA to `MEM` checkout.

---

## Email 9: Day 20 Objection Buster

### Timing

Day 20 at `9:00 AM`

### Purpose

Handle the final objections clearly.

### Main message

- Is it worth the money?
- What if I do not follow through?
- Can I just do this on my own?

### CTA

Final direct CTA to `MEM`.

After this email:
- end the bridge
- suppress additional `MEM` pitching for a defined cooldown period

---

## Tags and Fields Needed

### Required tags

- `customer`
- `purchased_challenge`
- `kajabi_account_created`
- `purchased_mem`

### Required field

- `last_kajabi_login`

This field matters because it powers the Day 4 branch.

If this field is not reliable at launch, default Day 4 to the inactive/re-engagement version until tracking is fixed.

---

## Launch Priorities

If this flow is being built now, prioritize in this order:

1. Kajabi enrollment works correctly on Challenge purchase.
2. Confirmation page clearly explains new vs returning Kajabi access.
3. Immediate welcome email variants are built.
4. Day 2, Day 4, Day 7, and Day 8 emails are built.
5. Day 11-20 `MEM` bridge is built after the core challenge flow is stable.
6. End-to-end testing is run for:
   - new Kajabi user
   - returning Kajabi user
   - inactive user
   - buyer who purchases `MEM` during the bridge

---

## Non-Negotiables

- The buyer must know exactly how to access Day 1.
- The flow must not send daily nag emails just because the course is 7 days long.
- Day 8 must stay celebration-only.
- The `MEM` bridge must start after the Challenge, not during the first week.
- Access confusion is a bigger risk than copy quality.

---

## Recommended Build Structure

Use two connected layers:

### Layer 1: Challenge core post-purchase

- purchase
- confirmation page
- Email 1
- Email 2
- Day 4 branch
- Email 4
- Email 5

### Layer 2: Challenge to MEM bridge

- Email 6
- Email 7
- Email 8
- Email 9

This keeps the actual onboarding flow separate from the later ascension sequence.

---

## Final Definition

If someone asks, "What is the 7-Day Challenge post-purchase flow?" the short answer is:

It is a Kajabi-access and momentum flow that starts at purchase, gets the buyer into Day 1, supports her through the week with a light but intentional email cadence, celebrates completion on Day 8, and only then begins a measured bridge toward `MEM`.
