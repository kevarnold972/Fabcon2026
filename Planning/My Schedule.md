---
type: Planning
tags:
  - fabcon2026
  - planning
---

# My FabCon 2026 Schedule

## Conference Overview

**Dates:** March 16-20, 2026
**Location:** Atlanta, GA

| Day | Date | Focus |
|-----|------|-------|
| Monday | March 16 | Workshops |
| Tuesday | March 17 | Workshops |
| Wednesday | March 18 | Breakout Sessions |
| Thursday | March 19 | Breakout Sessions |
| Friday | March 20 | Breakout Sessions |

---

## Workshop Selection (Mon-Tue)

### Monday Workshops I'm Attending

```dataview
TABLE
  start_time as "Time",
  room as "Room",
  level_name as "Level"
FROM "Fabcon 2026/Workshops/Monday"
WHERE status = "Attending"
SORT start_time
```

### Tuesday Workshops I'm Attending

```dataview
TABLE
  start_time as "Time",
  room as "Room",
  level_name as "Level"
FROM "Fabcon 2026/Workshops/Tuesday"
WHERE status = "Attending"
SORT start_time
```

---

## Wednesday Sessions

```dataview
TABLE WITHOUT ID
  file.link as "Session",
  start_time as "Time",
  room as "Room",
  track as "Track"
FROM "Fabcon 2026/Sessions"
WHERE day = "Wednesday" AND status = "Attending"
SORT start_time
```

---

## Thursday Sessions

```dataview
TABLE WITHOUT ID
  file.link as "Session",
  start_time as "Time",
  room as "Room",
  track as "Track"
FROM "Fabcon 2026/Sessions"
WHERE day = "Thursday" AND status = "Attending"
SORT start_time
```

---

## Friday Sessions

```dataview
TABLE WITHOUT ID
  file.link as "Session",
  start_time as "Time",
  room as "Room",
  track as "Track"
FROM "Fabcon 2026/Sessions"
WHERE day = "Friday" AND status = "Attending"
SORT start_time
```

---

## Sessions I'm Considering

```dataview
TABLE
  day as "Day",
  start_time as "Time",
  track as "Track",
  interest as "Interest"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE status = "Considering"
SORT interest DESC, date, start_time
```

---

## High Interest Sessions (Rating 4-5)

```dataview
TABLE
  day as "Day",
  start_time as "Time",
  track as "Track",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE interest >= 4
SORT interest DESC, date, start_time
```

---

## Summary Stats

### By Status

```dataview
TABLE WITHOUT ID
  status as "Status",
  length(rows) as "Count"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE status != null
GROUP BY status
```

### By Track (Attending)

```dataview
TABLE WITHOUT ID
  track as "Track",
  length(rows) as "Count"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE status = "Attending"
GROUP BY track
SORT length(rows) DESC
```
