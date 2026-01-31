---
type: Track
track_name: SQL Server Track
conference: SQLCON
tags:
  - fabcon2026
  - sqlcon
  - track
---

## SQL Server Track

Sessions focused on SQL Server, performance tuning, and database administration.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[SQL Server Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[SQL Server Track]]
GROUP BY status
```
