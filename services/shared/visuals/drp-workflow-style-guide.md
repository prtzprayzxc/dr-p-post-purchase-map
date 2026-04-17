# Dr. P Workflow Design System — Blueprint Style Guide

This document defines the visual language, components, and layout principles for Dr. P's automation workflow visualizations. Use these tokens to ensure all future service flows maintain a consistent, high-precision "blueprint" aesthetic.

---

## 1. Color Palette

### Semantic Flow Colors (Role)
These colors indicate the **functional role** of a card or path within the automation sequence.

| Token | Hex | Usage |
| :--- | :--- | :--- |
| `--spine` | `#0E6B6B` | **The Happy Path**. Main sequence of events. Used for left-borders and connectors. |
| `--spine-deep` | `#0A5050` | High-contrast text or details within spine cards. |
| `--recovery` | `#C47A2C` | **Conditionals/Nudges**. Alerts, catch-up emails, or "quiz not done" branches. |
| `--side` | `#C47A2C` | Secondary parallel paths (e.g., UHA-1 backup emails). |
| `--scaffold` | `#8A8A8A` | **System/BTS**. Behind-the-scenes logic, exits, or transitions. |

### Surface Colors (Location)
These colors indicate **where** the action happens (UI context).

- **Web (Blue)**: `#2E6FAE` (Website/Landing Pages)
- **Quiz (Purple)**: `#6B5B8A` (Custom Quiz logic)
- **Mail (Amber)**: `#B8863D` (Inboxes/Email clients)
- **BTS (Slate)**: `#5C6670` (Server-side/Automation logic)

---

## 2. Typography

- **Headings (Brand)**: `Fraunces`, Serif. Weight: 600+.
    - Used for Card titles and the main dashboard header.
- **Body / Labels**: `Inter`, Sans-serif.
    - Modern, clean, highly readable in small sizes.
- **Mono / Technical**: `SF Mono` or `Consolas`.
    - Used for URLs, time-chips, IDs, and trigger logic.

---

## 3. Layout & Grid Structural Logic

The workflow uses a **3-row horizontal grid system** with center-aligned elements.

- **Row 1 (Top Satellite)**: System triggers and recovery branches (Amber/Slate).
- **Row 2 (Hero Spine)**: The primary sequence ("The Happy Path" - Teal).
- **Row 3 (Bottom Satellite)**: Supplementary side paths and secondary emails.

### Constants
- **Column Gap**: `260px` (provides breathing room for long straight connectors).
- **Row Gap**: `185px`.
- **Hero Card Width**: `320px`.
- **Vertical Alignment**: `place-items: center` (Every card must share a vertical midpoint).

---

## 4. Component Library

### Step Badges (The "Sequence Headers")
The primary navigational cue for the user journey.

- **Shape**: Pill-shaped chip (Width: max-content).
- **Position**: **Bottom-Right** (absolute: `bottom: -12px; right: -12px`).
- **Styles**: 
    - `background: #0E6B6B` (Spine Teal)
    - `border: 2.5px solid #FFFFFF`
    - `border-radius: 20px`
    - `padding: 0 14px`
    - `white-space: nowrap` (Critical: prevents clipping)

### Chrome Wrappers
Each card should look like its environment (Affordance).

- **Web Chrome**: Includes traffic dots (Red, Yellow, Green) and a URL pill at the top.
- **Email Chrome**: Mimics an inbox with sender avatar, subject lines, and preview text.
- **System Card**: Uses a dark slate top-bar with a "gear" icon to signal automation.

---

## 5. Connections & Annotation

- **Connector Style**: Strictly **Straight Geometric Lines** (`pathD` logic).
- **Labeling**: Path labels are positioned at the 50% midpoint of the straight line.
- **Path Variants**: 
    - **Solid Line**: Direct, non-conditional flow.
    - **Dashed Line**: Conditional branches (Recovery/Wait states).

---

## 6. Motion & Feedback

- **Hero Float**: Subtle vertical hover/swing on main path cards to signal "active" status.
- **Email Pulse**: Soft amber glow animation on email previews.
- **Interaction**: Cards lift (`-8px`) and scale slightly (`1.005`) on hover to feel interactive and premium.
