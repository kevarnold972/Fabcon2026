---
type: Track
track_name: SQL in Fabric Track
conference: SQLCON
tags:
  - fabcon2026
  - sqlcon
  - track
---

## SQL in Fabric Track

Sessions focused on SQL Database in Microsoft Fabric and T-SQL analytics endpoints.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[SQL in Fabric Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[SQL in Fabric Track]]
GROUP BY status
```
