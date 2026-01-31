---
type: Track
track_name: Microsoft Purview Track
conference: FABCON
tags:
  - fabcon2026
  - track
---

## Microsoft Purview Track

Sessions focused on data governance, data catalog, lineage, and compliance with Microsoft Purview.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[Microsoft Purview Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[Microsoft Purview Track]]
GROUP BY status
```
