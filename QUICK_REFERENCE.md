# Unified Solar Time (UST) - Quick Reference Card

## System Overview

**Unified Solar Time (UST)** is a metric time system where 1 Sol (S) = 1 day, using decimal units instead of the traditional 24/60/60 system.

---

## Quick Conversions

| Standard Time | Unified Solar Time | What's Happening |
|---|---|---|
| **00:00:00** | **0.0000 S** | Midnight - Start of day |
| **03:00:00** | **1.2500 S** | Early morning (1/8 through day) |
| **06:00:00** | **2.5000 S** | Sunrise area (1/4 through day) |
| **09:00:00** | **3.7500 S** | Mid-morning (3/8 through day) |
| **12:00:00** | **5.0000 S** | **NOON** - Exact middle |
| **15:00:00** | **6.2500 S** | Afternoon (5/8 through day) |
| **18:00:00** | **7.5000 S** | Evening (3/4 through day) |
| **21:00:00** | **8.7500 S** | Late evening (7/8 through day) |
| **23:59:59** | **9.9999 S** | Almost end of day |

---

## Unit Hierarchy

```
┌─────────────────────────────────────────────┐
│ 1 SOL (S) = 1 Day = 86,400 Standard Seconds │
│        Base Unit: Earth's Rotation          │
└─────────────────────────────────────────────┘
                    ↓
        ┌──────────────────────┐
        │ ÷ 10 = CENTISOL (cS) │  (4 hours)
        │ 100,000 ÷ 10 = 10   │
        └──────────────────────┘
                    ↓
        ┌──────────────────────┐
        │ ÷ 100 = MILLISOL (mS)│  (86.4 seconds)
        │ 10,000 ÷ 100 = 100  │
        └──────────────────────┘
                    ↓
        ┌──────────────────────┐
        │ ÷ 100 = MICROSOL (μS)│  (0.864 seconds)
        │ 100 ÷ 100 = 1       │
        └──────────────────────┘

TOTAL: 10 × 100 × 100 = 100,000 Microsols per day
```

---

## Display Format

### Time Display: `H.MMSS`

**Example: `5.3042 S`**

- **5** = Centisol (0-9)
- **.** = Decimal separator
- **30** = Millisol (00-99)
- **42** = Microsol (00-99)

**Reading:** "Five point three zero forty-two sols"

---

## Conversion Cheat Sheet

### To Convert Standard Time → UST:

1. Take the hour (0-23)
2. Divide by 24
3. Result is your Sol decimal
4. Multiply fractional part by 10 for centisols
5. Multiply fractional part by 100 for millisols
6. Multiply fractional part by 100 for microsols

**Example: 9:30 AM**
- Hours = 9, Minutes = 30
- Standard seconds = 9×3600 + 30×60 = 32,400 + 1,800 = 34,200 seconds
- Metric seconds = 34,200 ÷ 0.864 = 39,583.33
- Centisols = 39,583.33 ÷ 10,000 = 3.95833
- Millisols = (39,583.33 % 10,000) ÷ 100 = 3.95833 × 100 = 395.833...
- **Result: 3.9583 S** (approximately)

### To Convert UST → Standard Time:

1. Take the Sol decimal
2. Multiply by 24 to get hours
3. Multiply fractional part by 60 for minutes
4. Multiply fractional part by 60 for seconds

**Example: 5.0000 S (Noon)**
- 5.0000 × 24 = 120 hours = 5 days (noon on day 5 would be day 0, hour 12)
- Since 5.0000 is exactly half the day: 0.5 × 24 hours = 12 hours = **12:00:00**

---

## Key Facts

| Item | Value |
|------|-------|
| **Base Unit** | Sol (S) |
| **Symbol** | ⊙ (sun symbol) |
| **1 Centisol** | 4 standard hours |
| **1 Millisol** | 86.4 standard seconds |
| **1 Microsol** | 0.864 standard seconds |
| **Total per day** | 100,000 metric seconds |
| **Metric second** | 0.864 standard seconds |
| **System basis** | Earth's rotation (solar day) |
| **Time reference** | UTC (Coordinated Universal Time) |

---

## Why UST?

### Problems with Traditional Time
- 24 hours per day (not decimal)
- 60 minutes per hour (not decimal)
- 60 seconds per minute (not decimal)
- Mixed bases make calculations hard
- Computer systems need 60→10 conversions

### UST Advantages
- ✓ Pure decimal (base-10)
- ✓ Metric aligned
- ✓ Perfect for computers
- ✓ Solar-synchronized
- ✓ Universal standard
- ✓ Easy mental math
- ✓ Scalable

---

## Common Time Blocks

| Duration | Standard | UST | What is it? |
|----------|----------|-----|-------------|
| 1 day | 24 hours | 10.0000 S | Full rotation |
| 1/2 day | 12 hours | 5.0000 S | Half day (noon) |
| 1/4 day | 6 hours | 2.5000 S | Quarter day |
| 1/10 day | 2.4 hours | 1.0000 S | Centisol |
| 1 hour | 60 min | ~0.4166 S | Roughly 0.42 S |
| 15 minutes | 900 sec | ~0.1041 S | Roughly 0.10 S |
| 1 minute | 60 sec | ~0.0069 S | Roughly 0.007 S |

---

## Example Schedules

### Meeting Times

| Event | Standard | UST | Notes |
|-------|----------|-----|-------|
| Morning standup | 09:00 AM | 3.7500 S | 9 AM sharp |
| Lunch | 12:30 PM | 5.2083 S | Midday |
| Afternoon review | 03:00 PM | 6.2500 S | 3 PM |
| End of workday | 05:00 PM | 7.0833 S | 5 PM |

### Work Hours

| Period | Standard | UST | Duration |
|--------|----------|-----|----------|
| Start | 09:00 AM | 3.7500 S | Work begins |
| Mid-morning | 10:30 AM | 4.3750 S | Break time |
| End | 05:30 PM | 7.2916 S | 8.5 hour day |

---

## Metric Prefixes Extended

| Prefix | Symbol | Factor | Example |
|--------|--------|--------|----------|
| **Centi** | c | 10⁻² | 1 cS = 0.01 S |
| **Milli** | m | 10⁻³ | 1 mS = 0.001 S |
| **Micro** | μ | 10⁻⁶ | 1 μS = 0.000001 S |
| **Nano** | n | 10⁻⁹ | 1 nS = 0.000000001 S |
| **Pico** | p | 10⁻¹² | 1 pS = 10⁻¹² S |
| **Deci** | d | 10⁻¹ | 1 dS = 0.1 S |
| **Deca** | da | 10¹ | 1 daS = 10 S |
| **Kilo** | k | 10³ | 1 kS = 1000 S |
| **Mega** | M | 10⁶ | 1 MS = 1000000 S |

---

## Mental Math Tips

### Quick Conversions

**Rule of Thumb: Multiply hours by ~0.4166 to get Sols**

- 00:00 → 0.0 S
- 03:00 → 1.25 S
- 06:00 → 2.5 S (divide by 4)
- 12:00 → 5.0 S (divide by 2)
- 24:00 → 10.0 S (exactly 1 day)

**In decimals:**
- Each hour ≈ 0.4166 Sols
- Each half-hour ≈ 0.2083 Sols
- Each 15 minutes ≈ 0.1041 Sols
- Each 6 minutes ≈ 0.0417 Sols

---

## Scientific Precision

### Significant Digits

- **1 Centisol** = 4 hours (coarse)
- **1 Millisol** = 86.4 seconds (practical)
- **1 Microsol** = 0.864 seconds (precise)
- **1 Nanosol** = 0.864 milliseconds (very precise)

### Accuracy

- UST is lossless when converting to/from standard time
- Rounding at millisol level loses ~86 seconds per conversion
- Microsol precision maintained for 1-day cycles

---

## Comparison Chart

```
STANDARD TIME vs UNIFIED SOLAR TIME

Standard:    00 : 00 : 00  (hours : minutes : seconds)
             ↓    ÷60    ÷60
UST:         0.0000        (decimal representation)
             ↓ ÷ 10 / ÷100 / ÷100
Format:      H.MMSS        (Centisol.Millisol.Microsol)
```

---

## Common Questions

**Q: Is this official?**  
A: No, it's a proposed standard combining metric principles with Earth's rotation.

**Q: What about leap seconds?**  
A: UST follows UTC convention (leap seconds occur ~every 1.5 years).

**Q: Can I use this for work?**  
A: Yes! It's fully compatible. Use the converter for meetings with standard-time folks.

**Q: Is this just for fun?**  
A: Both! It's educational AND practical for understanding decimal time systems.

**Q: Does it work on other planets?**  
A: Yes! A "Martian Sol" is Mars's rotation. Just recalibrate the base unit.

---

## Resources

- **GitHub:** https://github.com/jordon-sudo/unified-solar-time
- **System Spec:** See `SYSTEM.md` for technical details
- **Windows Setup:** See `WINDOWS_SETUP.md` for installation
- **Full Docs:** See `README.md` for complete information

---

## Symbol Reference

```
⊙ = Sol (sun symbol)
S = Sol abbreviation
cS = Centisol
mS = Millisol
μS = Microsol (mu symbol)
H = Centisol (in format H.MMSS)
M = Millisol
μ = Microsol
```

---

**Print this card or save it for quick reference!**

*Unified Solar Time (UST) - A Metric Time System*  
*Created: 2026 | Dublow Digital*

---

## Last Updated

October 21, 2026 | Version 1.0
