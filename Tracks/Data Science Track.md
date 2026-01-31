---
type: Track
track_name: Data Science Track
conference: FABCON
tags:
  - fabcon2026
  - track
---

## Data Science Track

Sessions focused on machine learning, AI, data science notebooks, and ML models in Fabric.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[Data Science Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[Data Science Track]]
GROUP BY status
```
