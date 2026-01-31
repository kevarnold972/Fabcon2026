---
type: Track
track_name: OneLake Track
conference: FABCON
tags:
  - fabcon2026
  - track
---

## OneLake Track

Sessions focused on OneLake, shortcuts, data sharing, and unified data storage.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[OneLake Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[OneLake Track]]
GROUP BY status
```
