---
type: Track
track_name: Microsoft Foundry Track
conference: FABCON
tags:
  - fabcon2026
  - track
---

## Microsoft Foundry Track

Sessions focused on Microsoft Foundry capabilities and AI agent development.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[Microsoft Foundry Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[Microsoft Foundry Track]]
GROUP BY status
```
