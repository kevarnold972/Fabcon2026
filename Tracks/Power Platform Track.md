---
type: Track
track_name: Power Platform Track
conference: FABCON
tags:
  - fabcon2026
  - track
---

## Power Platform Track

Sessions focused on Power Apps, Power Automate, and Power Platform integration with Fabric.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[Power Platform Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[Power Platform Track]]
GROUP BY status
```
