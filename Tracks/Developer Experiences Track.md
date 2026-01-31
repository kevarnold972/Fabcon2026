---
type: Track
track_name: Developer Experiences Track
conference: FABCON
tags:
  - fabcon2026
  - track
---

## Developer Experiences Track

Sessions focused on developer productivity, CI/CD, Git integration, and development workflows.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[Developer Experiences Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[Developer Experiences Track]]
GROUP BY status
```
