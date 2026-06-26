Your backend is:

> Typing Engine → Appearance Graph → Consumers

The UI should represent:

> The five jobs users hire the app to do.

Your architecture already has a single source of truth—the Appearance Graph—which every feature reads from after the typing pipeline resolves a CompoundProfile.

---

# The Mental Model

```text
                    Appearance Graph
                           │
      ┌──────────┬──────────┬──────────┬──────────┐
      │          │          │          │          │
    Today     Closet    Improve    Discover    Identity
```

The Appearance Graph is invisible.

Users only see five ways of interacting with it.

---

# Bottom Navigation

```text
🏠 Today

👔 Closet

✨ Improve

🛍 Discover

👤 Me
```

These are verbs, not technologies.

---

# 1. 🏠 TODAY

## Purpose

The AI's homepage.

This should become the most visited screen.

Everything is contextual.

---

## User asks

> What should I wear?

> What should I do today?

> Anything I should know?

---

## Inputs

Appearance Graph

Weather

Calendar

Events

Wardrobe

Laundry

Shopping

Goals

Recent outfits

---

## Outputs

### Daily outfit

```text
Wear this today

↓

Blue Oxford

Grey trousers

Brown loafers
```

---

### Explanation

```text
Why?

• Perfect temperature

• Business casual

• Haven't worn these pants in 2 weeks

• Matches profile
```

---

### Today's recommendations

```text
Upcoming

Interview

↓

Iron blazer

↓

Need black belt
```

---

### Cards

Morning Brief

Upcoming Events

Wardrobe Reminder

Style Tip

Progress

Shopping Alerts

---

## Future

Morning notification

Wear reminders

Packing reminders

Laundry reminders

Travel reminders

---

Think of this as

```text
Your appearance dashboard.
```

NOT

```text
Fashion newsfeed.
```

---

# 2. 👔 CLOSET

This is the digital wardrobe.

Everything you own.

---

## Purpose

Maintain your appearance inventory.

---

## Objects

```text
Wardrobe

↓

Category

↓

Item

↓

Relationships
```

Example

```text
White Oxford

Supports

Soft Natural

Soft Autumn

Works With

12 items

Conflicts

2 jackets

Wear Count

24

Cost/Wear

₹118
```

---

## Features

Digital wardrobe

Outfit builder

Capsule wardrobe

Packing

Laundry

Wishlist

Favorites

Recently worn

Seasonal storage

Outfit history

---

## AI Jobs

Generate outfit

Find missing item

Find duplicates

Suggest donation

Optimize wardrobe

---

## Hidden Goal

Build

```text
Wardrobe Graph
```

instead of

```text
Photo Gallery
```

---

# 3. ✨ IMPROVE

This is where transformation lives.

Not fashion.

Appearance.

---

## Purpose

Move user from

Current

↓

Target

---

## User Goals

Look older

Look younger

Look richer

Look professional

Look approachable

Look attractive

Look masculine

Look feminine

Improve dating

Creator branding

Executive presence

---

## Domains

Hair

Beard

Glasses

Fitness

Body composition

Posture

Skincare

Wardrobe

Photography

Profile pictures

Confidence

Accessories

Personal brand

---

## AI Output

Instead of

100 tips

Generate

```text
Current

↓

Target

↓

Highest ROI Actions
```

Example

```text
Current

Hair

6/10

↓

Recommended Cut

+18%

Appearance Score

↓

Expected Impact

High
```

---

## Progress

Monthly reviews

Timeline

Before / After

Improvement history

Goal tracking

---

This is basically

```text
Appearance Coach
```

---

# 4. 🛍 DISCOVER

Everything involving acquisition.

Not only shopping.

---

## Purpose

Expand wardrobe intelligently.

---

## Sources

Marketplace

Affiliate

Brands

Collections

Second-hand

Community

Creators

---

## AI Recommendation

Instead of

```text
Trending jacket
```

Recommend

```text
You need

↓

Lightweight overshirt

↓

Unlocks

18 outfits

↓

Pairs with

7 items

↓

Matches profile
```

---

## Sections

For You

Wardrobe Gaps

Collections

Brands

Wishlist

Marketplace

Sales

---

## Commerce Logic

Every recommendation explains itself.

Everything should answer

> Why?

---

## Future

Sell clothes

Rent clothes

Trade

Community wardrobes

Influencer wardrobes

---

# 5. 👤 ME

Everything about the user.

This is NOT settings.

---

## Identity

Compound Profile

Confidence

Reasoning

Appearance graph

Timeline

---

## Reports

Color report

Kibbe report

Essence report

PDFs

---

## Preferences

Budget

Lifestyle

Brands

Fit

Goals

Climate

---

## Subscription

Premium

Credits

History

---

## Retake

Update profile

New photos

Confidence changes

---

## Analytics

Outfit stats

Compliments

Purchase history

Wardrobe value

Wear frequency

---

Think

```text
Identity

+

Analytics

+

Settings
```

---

# Floating AI

Instead of making

Stylist

another page

make it global.

```text
          ○

      Ask SYNTHE
```

Works everywhere.

---

Questions

```text
Rate this outfit

Should I buy this?

Generate outfit

Pack for Goa

Review Tinder photos

Wedding outfit

Find alternatives

Which glasses?

What color tie?

```

Internally

everything queries

Appearance Graph.

---

# Events

Events shouldn't be navigation.

They're temporary contexts.

```text
Create Event

↓

Wedding

↓

Interview

↓

Vacation

↓

Date

↓

Conference
```

Each event creates

```text
Event Context
```

The graph changes.

Recommendations change.

Home changes.

Shopping changes.

Wardrobe changes.

After event

it disappears.

---

# Identity Engine

This isn't a tab.

It's onboarding.

```text
Install App

↓

Typing Engine

↓

Appearance Graph

↓

Done
```

Afterwards

User never thinks about Kibbe again.

They think

> "Help me."

---

# The Real Architecture

I would describe the product like this:

```text
                Identity Engine
                      │
                      ▼
             Appearance Graph
                      │
      ┌─────────┬─────────┬─────────┬─────────┬─────────┐
      ▼         ▼         ▼         ▼         ▼
    Today    Closet    Improve   Discover     Me
      │         │         │         │          │
      └─────────┴─────────┴─────────┴──────────┘
                      │
              Outcome Feedback
                      │
                      ▼
             Appearance Graph
```

Every interaction either:

- **Reads** from the Appearance Graph (generate outfits, recommendations, coaching).
    
- **Writes** to the Appearance Graph (new clothes, purchases, goals, outfit ratings, event outcomes, photos).
    

That creates a closed learning loop where the user's profile evolves from a one-time "type" into a continuously improving personal appearance model. This is the transition from an AI fashion app to an **Appearance Operating System**, which is also consistent with the direction your architecture and pipeline are already moving toward.