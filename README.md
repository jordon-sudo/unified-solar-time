# Unified Solar Time (UST) Clock

A metric-based time system using **Sol** as the base unit. This repository contains an interactive clock and converter that displays time in the Unified Solar Time format.

## Overview

Unified Solar Time is a decimal time system based on Earth's rotation (1 Sol = 1 day), using metric prefixes similar to the International System of Units (SI). It provides a pure base-10 time measurement system.

### System Structure

```
1 Sol (S) = 1 day = 86,400 standard seconds

1 Sol = 10 Centisols (cS)
1 Centisol = 100 Millisols (mS)
1 Millisol = 100 Microsols (μS)

Total: 100,000 Microsols per day
```

### Conversion Reference

| Unified Solar Time | Standard Equivalent |
|-------------------|-------------------|
| 1 Sol (S) | 24 hours |
| 1 Centisol (cS) | 4 hours |
| 1 Millisol (mS) | 86.4 seconds |
| 1 Microsol (μS) | 0.864 seconds |

### Time Format

**Format:** `H.MMSS` (Centisol.Millisol.Microsol)

**Examples:**
- `0.0000 S` = Midnight (start of day)
- `5.0000 S` = Noon (middle of day)
- `9.9999 S` = Almost end of day

## Features

✓ **Real-time Clock Display** - Shows current time in both standard (UTC) and Unified Solar Time formats  
✓ **Time Converter** - Convert any standard time (HH:MM:SS) to Unified Solar Time  
✓ **Live Updates** - Clock updates every second  
✓ **Responsive Design** - Works on desktop, tablet, and mobile  
✓ **No Dependencies** - Pure HTML5, CSS3, and JavaScript

## Usage

### Option 1: View Online
Download or clone this repository and open `index.html` in any modern web browser.

```bash
git clone https://github.com/jordon-sudo/unified-solar-time.git
cd unified-solar-time
# Open index.html in your browser
```

### Option 2: Run Locally
Since this is a standalone HTML file with no server requirements, simply:
1. Save `index.html` to your computer
2. Double-click it to open in your default browser
3. Or right-click → "Open with" → Your preferred browser

### Option 3: Windows Desktop Application
To run as a Windows desktop app:
1. Create a shortcut to the HTML file
2. Right-click the shortcut → Properties
3. In Target, add: `--app=` before the file path
4. Or use a tool like [Nativefier](https://github.com/jiahaog/nativefier) to wrap it as an executable

## Calculator

The built-in calculator lets you convert standard time to Unified Solar Time:

1. Enter a standard time in HH:MM:SS format (e.g., 12:00:00)
2. The result displays instantly in Unified Solar Time format (e.g., 5.0000 S)

## Mathematical Basis

The conversion formula:

```javascript
Standard seconds → Metric seconds (divide by 0.864)
Metric seconds → Centisols (divide by 10,000)
Millisols (divide metric seconds by 100)
Microsols (metric seconds mod 100)
```

## Why Metric Time?

Decimal/metric time offers several advantages:
- **Pure Base-10 System** - Makes calculations easier (no 60s or 24s)
- **Scientific Standard** - Aligns with SI/metric system principles
- **Digital-Friendly** - Decimals work better with computers
- **Universal** - Not tied to historical conventions
- **Scalable** - Easy to extend to nanosols, picosols, etc.

## System Specifications

- **Base Unit:** Sol (⊙) - represents one Earth rotation
- **Metric Prefixes:** Centi-, Milli-, Micro- (standard SI prefixes)
- **Total Seconds/Day:** 100,000 metric seconds
- **Precision:** Microsol (0.864 standard seconds)
- **Time Reference:** UTC (Coordinated Universal Time)

## Technical Details

- **Language:** HTML5, CSS3, JavaScript (ES6)
- **Dependencies:** None
- **Browser Support:** All modern browsers (Chrome, Firefox, Safari, Edge)
- **File Size:** ~11 KB
- **License:** Open Source

## Future Enhancements

- [ ] Timezone support
- [ ] Historical time conversion
- [ ] Multiple display modes (digital, analog, decimal)
- [ ] Command-line converter tool
- [ ] Mobile app version

## Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests
- Propose features

## References

- International System of Units (SI): https://www.nist.gov/pml/weights-and-measures/metric-si
- French Revolutionary Calendar: https://en.wikipedia.org/wiki/French_revolutionary_time
- Decimal Time Systems: https://en.wikipedia.org/wiki/Decimal_time

## License

This project is open source and available for personal and commercial use.

---

**Developed by:** Jordon Whitelow  
**Organization:** Dublow Digital  
**Created:** 2026

For questions or suggestions, open an issue on GitHub!

---

### Quick Reference Card

```
🌍 UNIFIED SOLAR TIME (UST) - METRIC TIME SYSTEM

┌─────────────────────────────────────┐
│ TIME CONVERSIONS                    │
├─────────────────────────────────────┤
│ Midnight  → 0.0000 S                │
│ 06:00 UTC → 2.5000 S (6 AM)         │
│ Noon      → 5.0000 S (12 PM)        │
│ 18:00 UTC → 7.5000 S (6 PM)         │
│ 23:59:59  → 9.9999 S                │
└─────────────────────────────────────┘

UNIT HIERARCHY:
1 Sol = 10 Centisols
1 Centisol = 100 Millisols
1 Millisol = 100 Microsols
= 100,000 Microsols/day

SYMBOL: ⊙ (Sun symbol)
```