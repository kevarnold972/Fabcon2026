---
type: Track
track_name: Admin and Governance Track
conference: FABCON
tags:
  - fabcon2026
  - track
---

## Admin and Governance Track

Sessions focused on administration, security, compliance, and governance of Microsoft Fabric.

## Sessions in this Track

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  level_name as "Level",
  status as "Status"
FROM "Fabcon 2026/Sessions" OR "Fabcon 2026/Workshops"
WHERE track = [[Admin and Governance Track]]
SORT date, start_time
```

## My Interest Summary

```dataview
TABLE WITHOUT ID
  length(rows) as "Count"
FROM "Fabcon 2026"
WHERE track = [[Admin and Governance Track]]
GROUP BY status
```
