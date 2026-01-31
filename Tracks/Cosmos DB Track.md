---
type: Track
track_name: Cosmos DB Track
conference: SQLCON
tags:
  - fabcon2026
  - sqlcon
  - track
---

## Cosmos DB Track

Sessions focused on Azure Cosmos DB, NoSQL, and distributed database workloads.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[Cosmos DB Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[Cosmos DB Track]]
GROUP BY status
```
