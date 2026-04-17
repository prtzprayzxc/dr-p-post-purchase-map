# Session Notes
## 2026-04-17

---

## Scope Covered

This session focused on the `7-Day Hormone Reset & Recharge Challenge` post-purchase journey, especially:

- post-purchase flow structure
- visual journey mapping
- `GHL` checkout to `Kajabi` access logic
- feasibility of `GHL -> Zapier -> Kajabi` enrollment without a Kajabi-native checkout

---

## Artifacts Created

### Written docs

- [challenge-post-purchase-flow.md](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/services/challenge/docs/challenge-post-purchase-flow.md:1)
  Focused written flow for the 7-Day Challenge post-purchase sequence only.

- [challenge-strategy.md](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/services/challenge/docs/challenge-strategy.md:1)
  Higher-level strategy document for the Challenge role, pacing, and launch priorities.

- [challenge-production-automation-map.md](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/services/challenge/docs/challenge-production-automation-map.md:1)
  Build-ready production map for the verified `GHL -> Zapier -> Kajabi` architecture.

### Visual doc

- [challenge-flow-simple.html](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/services/challenge/visuals/challenge-flow-simple.html:1)
  Visual post-purchase journey in the same style as the existing `uha-flow-simple.html`.

---

## What Was Decided

### 1. The 7-Day Challenge flow is not a daily nag sequence

The intended cadence remains:

- `CH-1` immediately on purchase
- `CH-2` on Day 2
- `CH-3` on Day 4 with active/inactive branch
- `CH-4` on Day 7
- `CH-5` on Day 8 as celebration-only
- `CH-6` to `CH-9` as the later `MEM` bridge on Days 11, 14, 17, and 20

### 2. The confirmation page is still the primary onboarding moment

The flow assumes the buyer sees a Challenge confirmation page immediately after successful `GHL` checkout.

That page should:

- confirm the purchase
- explain the Kajabi access path
- push Day 1 as the only immediate next action
- show new-vs-returning Kajabi instructions

### 3. The Day 4 split is the main behavior branch

The branch should be based on `last_kajabi_login`:

- logged in → active midpoint momentum version
- not logged in → inactive recovery version

### 4. Day 8 must remain celebration-only

No upsell should happen in `CH-5`.

The `MEM` bridge starts later so the Challenge still feels like a complete product.

---

## Key Technical Clarification

### GHL checkout is a locked requirement

The user stated clearly that all payments should remain in `GHL`.

That means the architecture cannot rely on Kajabi-native checkout as the payment layer.

### Core risk identified

The main technical risk is not email automation. It is whether a successful `GHL` purchase can reliably result in Kajabi access.

Without a working enrollment path, the post-purchase journey can send emails but cannot safely promise course access.

---

## Kajabi Integration Discussion

Three possible patterns were discussed:

### 1. `GHL` checkout only, with direct automated Kajabi enrollment

This is the preferred architecture if it works.

It requires a verified way for `GHL` or `Zapier` to create/update the Kajabi contact and grant the Challenge offer.

### 2. `GHL` checkout + Kajabi form capture after purchase

This was discussed as a fallback assumption if Kajabi must capture the contact itself.

Pro:
- keeps payment in `GHL`
- lets Kajabi own contact creation + offer grant

Con:
- introduces friction after payment
- creates the risk that someone pays but does not complete the Kajabi access form

### 3. Manual rescue if automated enrollment fails

This must exist as a support fallback regardless of the primary path.

---

## Validation Direction Agreed

The most credible path discussed was:

`GHL form / checkout -> GHL workflow -> webhook -> Zapier -> Kajabi contact -> Grant Offer -> Kajabi welcome/setup email`

Conclusion:

- this can work
- the critical action is `Grant Offer`
- creating the contact alone is not enough
- this path has now been reported as working end-to-end

`GHL -> Zapier -> Kajabi` should now be treated as the validated enrollment method for Kajabi-delivered products in this project unless later testing contradicts it.

---

## Integration Status

The user confirmed that the `GHL -> Zapier -> Kajabi` path worked.

That means the previously open question is now resolved in the positive:

- `GHL` can remain the payment layer
- `Zapier` can pass the buyer into Kajabi
- `Kajabi` can receive the contact and grant access through the tested workflow

This removes the need to redesign the Challenge flow around a mandatory Kajabi-native checkout or a required Kajabi form capture step.

## Recommended Go/No-Go Test

Before production logic is finalized, verify this exact path for the Challenge:

1. submit a real test purchase through the embedded `GHL` checkout
2. confirm `purchased_challenge` is applied in `GHL`
3. confirm `Zapier` receives the payload
4. confirm `Kajabi` creates or updates the contact
5. confirm `Grant Offer` succeeds
6. confirm the test user receives the Kajabi setup/welcome email
7. confirm the user can log in and see the Challenge in Kajabi

This path has now been validated by the user.

---

## Current File Status

These are the current relevant files for the Challenge:

- [session-notes.md](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/session-notes.md:1)
- [challenge-post-purchase-flow.md](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/services/challenge/docs/challenge-post-purchase-flow.md:1)
- [challenge-strategy.md](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/services/challenge/docs/challenge-strategy.md:1)
- [challenge-production-automation-map.md](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/services/challenge/docs/challenge-production-automation-map.md:1)
- [challenge-flow-simple.html](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/services/challenge/visuals/challenge-flow-simple.html:1)

---

## Recommended Next Step

The next high-value step is:

implement the production map in `GHL`, `Zapier`, and `Kajabi` using the exact Challenge offer, payload fields, and failure handling defined in the new automation doc.

---

## Claude Handoff Note: 7-Day Challenge Visual Flow

If Claude is asked to create or refine the visual flow for the 7-Day Challenge, the required source-of-truth points are:

### Core architecture

- payment happens in embedded `GHL` checkout
- `GHL` is the system of record for purchase + email automation
- `Zapier` passes buyer data from `GHL` into `Kajabi`
- `Zapier` successfully creates/updates Kajabi contact and grants the Challenge offer
- `Kajabi` sends the access/setup email
- `Kajabi` hosts and delivers the Challenge product

### Simplified journey

1. buyer pays in `GHL`
2. `GHL` applies `purchased_challenge`
3. buyer lands on Challenge confirmation page
4. `GHL` sends webhook to `Zapier`
5. `Zapier` creates/updates Kajabi contact
6. `Zapier` grants Challenge offer
7. `Kajabi` sends login/setup email
8. `GHL` sends Challenge emails

### Challenge email cadence

- `CH-1` immediately
- `CH-2` Day 2 at `8am`
- `CH-3` Day 4 at `8am`
- `CH-4` Day 7 at `8am`
- `CH-5` Day 8 at `9am`
- `CH-6` Day 11 at `9am`
- `CH-7` Day 14 at `9am`
- `CH-8` Day 17 at `9am`
- `CH-9` Day 20 at `9am`

### Branches Claude should show

- new Kajabi user vs returning Kajabi user
  This affects access messaging in the confirmation page and `CH-1`
- Day 4 login branch using `last_kajabi_login`
  - active version of `CH-3` if logged in
  - inactive / re-engagement version of `CH-3` if not
- suppress `MEM` bridge if `purchased_mem` exists

### Important visual/logic notes

- the confirmation page is the primary onboarding moment
- `CH-5` on Day 8 is celebration-only and should not be visualized as a sales email
- the `MEM` bridge begins after the Challenge, not during the first 7 days
- the biggest system dependency is successful `GHL -> Zapier -> Kajabi Grant Offer`

### Relevant files for Claude

- [services/challenge/docs/challenge-post-purchase-flow.md](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/services/challenge/docs/challenge-post-purchase-flow.md:1)
- [services/challenge/docs/challenge-production-automation-map.md](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/services/challenge/docs/challenge-production-automation-map.md:1)
- [services/challenge/copy/email-copy-challenge.md](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/services/challenge/copy/email-copy-challenge.md:1)
- [services/challenge/visuals/challenge-flow-simple.html](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/services/challenge/visuals/challenge-flow-simple.html:1)
- [services/uha/visuals/uha-flow-simple.html](C:/Users/fgcon/Documents/Dr.%20P%20Program%20Automation/services/uha/visuals/uha-flow-simple.html:1)

Claude should use the Challenge docs as logic source-of-truth and the UHA/Challenge HTML visuals as style/pattern references.
