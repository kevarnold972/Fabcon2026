---
type: Speaker
name: "{{name}}"
title: "{{title}}"
company: "{{company}}"
speaker_type:
linkedin: ""
twitter: ""
tags:
  - fabcon2026
  - speaker
---

## Bio

{{bio}}

## Sessions at FabCon 2026

```dataview
TABLE
  session_type as "Type",
  day as "Day",
  start_time as "Time",
  track as "Track"
FROM "Fabcon 2026"
WHERE contains(speakers, this.file.link)
SORT date, start_time
```

## Notes

### Speaking Style


### Key Expertise


## Follow Up

- [ ] Connect on LinkedIn
- [ ] Follow on Twitter
