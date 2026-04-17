# Kajabi "Set Up Your Account" Email — Shared Across All Courses

**Owner:** Kajabi system email (customize inside Kajabi → Settings → Email → "Sign up offer" or "Account created" template)
**Fires:** Automatically, minutes after Grant Offer, for new Kajabi users only.
**Used by:** Every Kajabi course — Challenge, MEM, HWN, and any future Kajabi product.
**Do not duplicate:** One template, used over and over. Returning users never see this email.

---

## Subject
Set up your account — you're in.

## Preheader
One quick step: create your password so you can log in anytime.

## From
Dr. P Team <info@callmedoctorp.com>
(Set the reply-to address inside Kajabi so responses route to our inbox, not Kajabi's.)

---

## Body

Hi {{ user.first_name }},

You're in — welcome.

Before you jump into the course, let's get your account set up. It takes 30 seconds.

**Step 1 — Create your password:**
👉 [Set Up Your Account]({{ account_setup_link }})

**Step 2 — Log in from either spot, anytime:**
- The **Login** button on [callmedoctorp.com](https://callmedoctorp.com)
- Or any course link in our emails

That's it. The same password works for **every** Dr. P course you take with us — Challenge, Madame Estrogen Mastermind, Hormone Wellness Network, and anything else you grab down the road. Set it once, use it forever.

If the button above doesn't work, paste this into your browser:
`{{ account_setup_link }}`

— The Dr. P Team

---

## Footer / fine print
- Heads up: this link expires in 7 days. If it's too late, just hit the Login button on callmedoctorp.com and use "Forgot password."
- Didn't sign up? Reply to this email and we'll sort it out.

---

## Kajabi merge tags used
- `{{ user.first_name }}` — contact first name
- `{{ account_setup_link }}` — Kajabi's auto-generated password-setup URL (actual tag name may vary by Kajabi template: confirm in the template editor; options include `{{ setup_url }}` or `{{ password_setup_link }}`)

## Tone notes
- Warm, confident, no hype — matches Dr. P's voice across the rest of the sequence.
- Transactional first, brand second. Do not mix in upsells or course content — this is a utility email.
- Mention cross-course reuse once so new users understand the password is one-and-done.
