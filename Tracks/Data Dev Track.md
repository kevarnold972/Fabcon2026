---
type: Track
track_name: Data Dev Track
conference: FABCON
tags:
  - fabcon2026
  - track
---

## Data Dev Track

Sessions focused on development tools, APIs, SDKs, and developer experiences in Fabric.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[Data Dev Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[Data Dev Track]]
GROUP BY status
```
