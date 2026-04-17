# UHA Flow — Simple Version

**Read top to bottom. Each arrow = next step. Each email shows WHEN it fires.**

Stack: Website checkout → GHL (CRM + email) → Interact (quiz) → One results landing page.
Kajabi is NOT in this flow.

---

## The Flow

```
┌──────────────────────────────────────────┐
│  STAGE 1 — CHECKOUT PAGE                 │
│  callmedoctorp.com/uha                   │
│  User pays $47                           │
└──────────────────┬───────────────────────┘
                   │ payment succeeds
                   ▼
┌──────────────────────────────────────────┐
│  GHL fires: "Order Submitted — UHA"      │
│  • Adds tag: uha_purchaser               │
│  • Adds tag: uha_quiz_pending            │
│  • Stores uha_purchase_date              │
└──────────────────┬───────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────┐
│  STAGE 2 — THANK YOU PAGE                │
│  Auto-redirects to the Interact quiz     │
│  (no separate thank-you screen needed)   │
└──────────────────┬───────────────────────┘
                   │
         ┌─────────┴──────────┐
         │                    │
         ▼                    ▼
 ┌──────────────┐   ┌──────────────────────┐
 │ EMAIL #1     │   │ User starts the quiz │
 │ UHA-1        │   │ on Interact          │
 │ "Your        │   └──────────┬───────────┘
 │ assessment   │              │
 │ link (backup)│              │
 │ → quiz URL   │              │
 │ + receipt"   │              │
 │ Sent:        │              │
 │ immediately  │              │
 └──────────────┘              │
                               ▼
                  ┌─────────────────────────┐
                  │  STAGE 3 — QUIZ         │
                  │  Interact — 48 Qs       │
                  │  ~10 minutes            │
                  └──────────┬──────────────┘
                             │
          ┌──────────────────┴──────────────────┐
          │                                     │
          ▼                                     ▼
  ┌────────────────┐                 ┌──────────────────────┐
  │ DIDN'T FINISH  │                 │ FINISHED THE QUIZ    │
  │ quiz within    │                 │ Interact webhook     │
  │ 4 hours        │                 │ → GHL:               │
  └────────┬───────┘                 │ • Adds tag           │
           │                         │   uha_completed      │
           ▼                         │ • Removes            │
  ┌────────────────┐                 │   uha_quiz_pending   │
  │ EMAIL #2       │                 │ • Stores result:     │
  │ UHA-3          │                 │   estrogen_dominant  │
  │ "Your          │                 │   OR balanced        │
  │ assessment is  │                 └──────────┬───────────┘
  │ waiting"       │                            │
  │ Sent:          │                            ▼
  │ +4 hrs         │                 ┌──────────────────────┐
  └────────┬───────┘                 │ STAGE 4 — RESULTS    │
           │                         │ LANDING PAGE         │
           │ still not done?         │ callmedoctorp.com    │
           ▼                         │ /uha-results         │
  ┌────────────────┐                 │                      │
  │ EMAIL #3       │                 │ ONE page, content    │
  │ UHA-3b         │                 │ swaps based on URL   │
  │ "Still         │                 │ param ?result=ed OR  │
  │ curious?"      │                 │ ?result=bal          │
  │ Sent:          │                 │ (Interact passes it) │
  │ Day 2, 9am     │                 └──────────┬───────────┘
  └────────┬───────┘                            │
           │                                    ▼
           │                       ┌──────────────────────┐
           │                       │ EMAIL #4             │
           │                       │ UHA-2                │
           │                       │ "Your hormone        │
           │                       │ results" — full      │
           │                       │ report in email      │
           │                       │ (ED or Balanced      │
           │                       │ copy chosen by tag)  │
           │                       │ Sent:                │
           │                       │ immediately after    │
           │                       │ quiz completion      │
           │                       └──────────┬───────────┘
           │                                  │
           └──────────────┬───────────────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │ EMAIL #5             │
               │ UHA-4                │
               │ "So now you          │
               │ know — what to do"   │
               │ (ED or Balanced      │
               │ copy chosen by tag)  │
               │ Sent:                │
               │ Day 3, 9am           │
               │ (only if quiz done)  │
               └──────────┬───────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │ EMAIL #6             │
               │ UHA-5                │
               │ "Can I be honest?"   │
               │ Soft pitch for       │
               │ 7-Day Challenge      │
               │ Sent:                │
               │ Day 6, 9am           │
               │ (skip if already     │
               │ bought Challenge)    │
               └──────────┬───────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │ EMAIL #7             │
               │ UHA-6                │
               │ "One more thing      │
               │ about your results"  │
               │ Final Challenge      │
               │ invitation           │
               │ Sent:                │
               │ Day 10, 9am          │
               │ (skip if already     │
               │ bought Challenge)    │
               └──────────┬───────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │  END OF FLOW         │
               │  Contact moves to    │
               │  general nurture     │
               └──────────────────────┘
```

---

## The Email Schedule at a Glance

| # | Email   | When                            | Who gets it                          |
|---|---------|---------------------------------|--------------------------------------|
| 1 | UHA-1   | Immediately on purchase         | Everyone — backup quiz link          |
| 2 | UHA-2   | Immediately on quiz completion  | Quiz completers (ED or Balanced copy)|
| 3 | UHA-3   | +4 hours                        | Only if quiz NOT done yet            |
| 4 | UHA-3b  | Day 2, 9am                      | Only if quiz STILL not done          |
| 5 | UHA-4   | Day 3, 9am                      | Quiz completers (ED or Balanced copy)|
| 6 | UHA-5   | Day 6, 9am                      | All — unless already bought Challenge|
| 7 | UHA-6   | Day 10, 9am                     | All — unless already bought Challenge|

---

## The Two Paths — Plain English

**Path A — They take the quiz (happy path):**
Buy → Redirected to quiz → Email UHA-1 (backup link) hits inbox → They finish quiz → Land on results page → Email UHA-2 (full report) → Day 3 UHA-4 (what to do next) → Day 6 UHA-5 (Challenge soft pitch) → Day 10 UHA-6 (final Challenge invite) → Done.

**Path B — They DON'T take the quiz:**
Buy → Redirected to quiz → Get distracted/close the tab → Email UHA-1 arrives → Still don't take it → 4hrs later UHA-3 nudge → Day 2 UHA-3b stronger nudge → (They either take it now and jump to Path A at UHA-2, OR they never take it and still get UHA-5 + UHA-6 on Day 6/10.)

---

## The One Landing Page

**URL:** `callmedoctorp.com/uha-results`

**How it decides what to show:**
- Interact appends the result type to the URL when it redirects the user after quiz completion:
  - `?result=ed` → estrogen-dominant content blocks show
  - `?result=bal` → balanced content blocks show
- Same page, same layout — only the result headline + top 3 factors + top 3 actions swap based on the URL param.
- If someone lands on the page without a param (direct link, email click after a while), fall back to a generic "Check your email for your report" message.

**What's on the page (both versions):**
1. Result headline ("You are Estrogen Dominant" / "You are Hormonally Balanced")
2. What this means (2–3 paragraphs)
3. Your top 3 contributing factors (or strengths, for Balanced)
4. 3 things to do this week
5. "Your full report was emailed to you — save it."
6. Soft CTA to the 7-Day Challenge (same on both versions)

The full written copy for both versions already exists in `email-copy-uha-challenge.md` under UHA-2. Reuse it on the landing page — no need to write twice.

---

## The Two Tags That Run Everything

- `uha_purchaser` → applied on checkout → starts the whole flow
- `uha_completed` → applied when the quiz is finished → turns OFF the nudge emails and turns ON the results emails

Everything else (timings, conditionals) is just logic checking these two tags.
