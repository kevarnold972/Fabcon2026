---
type: Track
track_name: Data Engineering Track
conference: FABCON
tags:
  - fabcon2026
  - track
---

## Data Engineering Track

Sessions focused on data pipelines, Spark, notebooks, lakehouse architecture, and data transformation.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[Data Engineering Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[Data Engineering Track]]
GROUP BY status
```
