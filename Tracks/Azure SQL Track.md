---
type: Track
track_name: Azure SQL Track
conference: SQLCON
tags:
  - fabcon2026
  - sqlcon
  - track
---

## Azure SQL Track

Sessions focused on Azure SQL Database, Azure SQL Managed Instance, and cloud SQL workloads.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[Azure SQL Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[Azure SQL Track]]
GROUP BY status
```
