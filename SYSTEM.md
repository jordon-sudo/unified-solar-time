# Unified Solar Time System Specification

## Complete System Documentation

### 1. Base Definition

**Unified Solar Time (UST)** is a decimal time system where:
- 1 Sol (S) = 1 complete Earth rotation = 24 standard hours = 86,400 standard seconds
- The system uses 100,000 metric seconds per day
- 1 metric second = 0.864 standard seconds

### 2. Unit Hierarchy

```
1 Sol (S)
├── 10 Centisols (cS) - each equals 4 standard hours
│   ├── 100 Millisols (mS) - each equals 86.4 standard seconds
│   │   ├── 100 Microsols (μS) - each equals 0.864 standard seconds
│   │   └── Smaller units available via standard SI prefixes
```

### 3. Metric Prefixes (SI Standard)

| Prefix | Symbol | Factor |
|--------|--------|--------|
| Centi- | c | 10^-2 |
| Milli- | m | 10^-3 |
| Micro- | μ | 10^-6 |
| Nano- | n | 10^-9 |
| Pico- | p | 10^-12 |

### 4. Time Display Format

**Primary Format: `H.MMSS` (Centisol.Millisol.Microsol)**

Example: `5.3042` represents:
- 5 Centisols
- 30 Millisols
- 42 Microsols

Alternative full format: `H.MMSS` with full decimal representation

### 5. Conversion Tables

#### Standard Time to Unified Solar Time

| Standard Time | UST Equivalent | Notes |
|---------------|----------------|-------|
| 00:00:00 | 0.0000 S | Midnight |
| 03:00:00 | 1.2500 S | 3 AM |
| 06:00:00 | 2.5000 S | 6 AM |
| 09:00:00 | 3.7500 S | 9 AM |
| 12:00:00 | 5.0000 S | Noon |
| 15:00:00 | 6.2500 S | 3 PM |
| 18:00:00 | 7.5000 S | 6 PM |
| 21:00:00 | 8.7500 S | 9 PM |
| 23:59:59 | 9.9999 S | End of day |

### 6. Mathematical Formulas

#### Standard to UST Conversion

```
Input: hours (0-23), minutes (0-59), seconds (0-59)

Step 1: Convert to total standard seconds
totalStdSeconds = hours × 3600 + minutes × 60 + seconds

Step 2: Convert to metric seconds
totalMetricSeconds = totalStdSeconds ÷ 0.864

Step 3: Extract UST units
centisols = floor(totalMetricSeconds ÷ 10000)
millisols = floor((totalMetricSeconds mod 10000) ÷ 100)
microsols = floor(totalMetricSeconds mod 100)

Step 4: Format output
ustTime = centisols.millisols microsols
```

#### UST to Standard Conversion

```
Input: centisols (0-9), millisols (0-99), microsols (0-99)

Step 1: Convert to total metric seconds
totalMetricSeconds = (centisols × 10000) + (millisols × 100) + microsols

Step 2: Convert to standard seconds
totalStdSeconds = totalMetricSeconds × 0.864

Step 3: Extract standard units
hours = floor(totalStdSeconds ÷ 3600) mod 24
minutes = floor((totalStdSeconds mod 3600) ÷ 60)
seconds = floor(totalStdSeconds mod 60)
```

### 7. Key Reference Points

| Event | Standard Time | UST | Notes |
|-------|---------------|-----|-------|
| Midnight | 00:00:00 | 0.0000 S | Start of day |
| Sunrise (average) | 06:00:00 | 2.5000 S | Morning |
| Noon | 12:00:00 | 5.0000 S | Middle of day |
| Sunset (average) | 18:00:00 | 7.5000 S | Evening |
| Hour mark | Each hour | +0.4166 S | Roughly +1/24 per hour |

### 8. Precision and Granularity

- **Maximum Precision:** 1 Microsol = 0.864 seconds
- **Practical Precision:** 1 Millisol = 86.4 seconds (1.44 minutes)
- **Common Usage:** Centisol.Millisol format (4-hour and 1.44-minute precision)
- **Sub-microsol:** Can extend to nanosols (n⊙) = 0.864 nanoseconds

### 9. Physical Basis

- **Planetary Reference:** Earth's sidereal day + solar day average
- **Metric Alignment:** 100,000 metric seconds = 10^5 μS
- **SI Compliance:** Uses standard metric prefixes
- **Decimal Logic:** All conversions based on powers of 10

### 10. Advantages Over Historical Time

| Aspect | Historical | UST |
|--------|-----------|-----|
| Day Division | 24 hours | 10 centisols |
| Hour Division | 60 minutes | 100 millisols |
| Minute Division | 60 seconds | 100 microsols |
| Base System | Mixed bases | Pure decimal (base-10) |
| Computing | Complex | Simple decimals |
| Scientific | Variable | Metric standard |

### 11. Leap Second Handling

- **Standard:** UTC occasionally adds leap seconds
- **UST:** Follows UTC leap second convention
- **Effect:** Minimal (occurs ~every 1.5 years)
- **Display:** Rounded to nearest microsol

### 12. Timezone Considerations

- **Base Reference:** UTC (same as standard Coordinated Universal Time)
- **Local Time:** Can apply standard timezone offsets
- **Example:** EST = UTC-5, so 5 centisols of offset
- **Implementation:** Multiply standard timezone offset by 0.4166 (= 1/24)

### 13. Historical Context

- **Inspiration:** French Revolutionary Decimal Time (1793-1795)
- **Improvement:** UST uses solar day (Earth rotation) as basis
- **Modern:** Designed for metric system adoption in timekeeping
- **Future:** Scalable for other celestial bodies (Sol times on Mars, etc.)

### 14. Compatibility

- **Backwards Compatible:** Can always convert to standard time
- **Bi-directional:** Lossless conversion both directions
- **Precision Loss:** None with proper rounding
- **Digital Native:** Perfect for computer systems

---

## Symbol Reference

- **⊙** = Sol (sun symbol, represents Earth's rotation)
- **cS** = Centisol
- **mS** = Millisol
- **μS** = Microsol (note: lowercase mu)
- **S** = Sol (used in general time notation)

---

## Usage Examples

### Example 1: Breakfast at 8 AM
**Standard:** 08:00:00 UTC  
**UST:** 3.3333 S  
*(8 hours ÷ 24 hours/day = 0.333... = 3.3333 centisols)*

### Example 2: Meeting at 2:30 PM
**Standard:** 14:30:00 UTC  
**UST:** 6.0416 S  
*(14.5 hours ÷ 24 hours/day = 0.604166... = 6.0416 centisols)*

### Example 3: Midnight countdown
**Standard:** 23:59:60 UTC (leap second)  
**UST:** 9.99988 S  
*(Just before 10.0000, which wraps to 0.0000)*

---

**System Version:** 1.0  
**Last Updated:** October 21, 2026  
**Author:** Dublow Digital
