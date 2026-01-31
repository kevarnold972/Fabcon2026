---
type: Track
track_name: PostgreSQL Track
conference: SQLCON
tags:
  - fabcon2026
  - sqlcon
  - track
---

## PostgreSQL Track

Sessions focused on Azure Database for PostgreSQL and PostgreSQL workloads.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[PostgreSQL Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[PostgreSQL Track]]
GROUP BY status
```
