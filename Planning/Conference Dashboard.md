---
type: Planning
tags:
  - fabcon2026
  - planning
  - dashboard
---

# FabCon 2026 Dashboard

## Quick Links

- [[My Schedule]]
- [[Session Conflicts]]

---

## Conference Info

| | |
|---|---|
| **Conference** | Microsoft Fabric Community Conference (FABCON) + SQLCON |
| **Dates** | March 16-20, 2026 |
| **Location** | Atlanta, GA |
| **Website** | [fabriccon.com](https://fabriccon.com) |

---

## My Planning Progress

### Sessions by Status

```dataview
TABLE WITHOUT ID
  status as "Status",
  length(rows) as "Count"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE status != null
GROUP BY status
SORT length(rows) DESC
```

### Sessions by Interest Level

```dataview
TABLE WITHOUT ID
  interest as "Interest Rating",
  length(rows) as "Count"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE interest != null
GROUP BY interest
SORT interest DESC
```

---

## Sessions by Track

```dataview
TABLE WITHOUT ID
  track as "Track",
  length(rows) as "Total Sessions"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track != null
GROUP BY track
SORT length(rows) DESC
```

---

## Sessions by Day

```dataview
TABLE WITHOUT ID
  day as "Day",
  length(rows) as "Sessions"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE day != null
GROUP BY day
```

---

## Recently Modified

```dataview
TABLE WITHOUT ID
  file.link as "Session",
  file.mtime as "Modified"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
SORT file.mtime DESC
LIMIT 10
```

---

## Speakers I Want to See

```dataview
LIST
FROM "Fabcon 2026/Speakers"
SORT file.name
```

---

## All Tracks

```dataview
LIST
FROM "Fabcon 2026/Tracks"
SORT file.name
```
