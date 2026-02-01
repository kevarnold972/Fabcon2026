# FabCon 2026 Obsidian Vault

An [Obsidian](https://obsidian.md/) vault for planning your attendance at **FabCon 2026** (Microsoft Fabric Community Conference) and **SQLCON 2026** - co-located conferences in Atlanta, GA from March 16-20, 2026.

**Official Conference Website:** https://fabriccon.com/

## Features

- **267 sessions and workshops** with full descriptions, speakers, tracks, and room assignments
- **358 speaker profiles** with bios and social links
- **19 track overview pages** for browsing by topic
- **Dynamic views** using Obsidian Bases for filtering and organizing sessions
- **Planning tools** for building your personal schedule and resolving conflicts

## Getting Started

1. Download or clone this repository
2. Open the folder as a vault in Obsidian
3. Enable the **Bases** core plugin (Settings > Core plugins > Bases)
4. Start with the `Planning/Conference Dashboard.md` to explore sessions

## Conference Schedule

| Day | Date | Type |
|-----|------|------|
| Monday | March 16 | Full-day Workshops (9 AM - 5 PM) |
| Tuesday | March 17 | Full-day Workshops (9 AM - 5 PM) |
| Wednesday | March 18 | Keynote + Breakout Sessions |
| Thursday | March 19 | Breakout Sessions + Expo |
| Friday | March 20 | Breakout Sessions |

## Planning Your Schedule

### Key Properties for Sessions

The Planning views filter sessions based on these frontmatter properties:

| Property | Values | Description |
|----------|--------|-------------|
| `status` | `Considering`, `Attending`, `Skip` | Your decision on attending |
| `interest` | `1` to `5` | How interested you are (5 = must attend) |
| `day` | `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` | Day of the session |

### Workflow

1. **Browse sessions** - Use the Dashboard or Track pages to explore
2. **Rate sessions** - Set `interest: 1-5` in the frontmatter
3. **Mark attendance** - Change `status: Considering` to `status: Attending`
4. **Check your schedule** - View `Planning/My Schedule.md` to see your plan by day
5. **Resolve conflicts** - Use `Planning/Session Conflicts.md` to find overlapping sessions

### Planning Files

| File | Purpose |
|------|---------|
| `Planning/Conference Dashboard.md` | Overview stats, tracks, and quick navigation |
| `Planning/My Schedule.md` | Your personalized day-by-day schedule |
| `Planning/Session Conflicts.md` | Identify and resolve time slot conflicts |

## Vault Structure

```
Fabcon 2026/
├── Bases/           # Obsidian Bases for dynamic views
├── Planning/        # Dashboard, schedule, and conflict tools
├── Sessions/        # 245 breakout sessions (Wed-Fri)
├── Workshops/       # 22 full-day workshops (Mon-Tue)
├── Speakers/        # 358 speaker profiles
├── Tracks/          # 19 track overview pages
└── Templates/       # Templates for new notes
```

## Session Frontmatter

Each session file includes structured frontmatter:

```yaml
title: "Session Title"
date: 2026-03-18
day: Wednesday
start_time: "1:45 PM"
end_time: "2:45 PM"
duration: 60
room: "C111-C112"
track: "[[Power BI Track]]"
session_type: "Breakout Session"
level: 200
level_name: "Feature Oriented"
audience:
  - Data Engineer
  - Data Analyst
speakers:
  - "[[Speaker Name]]"
conference: FABCON
interest:           # Set 1-5 to rate
status: Considering # Change to Attending or Skip
```

### Level Guide

| Level | Name | Description |
|-------|------|-------------|
| 100 | Business Level | Business-focused, non-technical |
| 200 | Feature Oriented | Feature overviews and capabilities |
| 300 | Technical | Technical implementation details |
| 400 | Deep Technical | Advanced deep-dives |

## Conferences

This vault covers two co-located conferences:

### FABCON (13 tracks)
Microsoft Fabric focused: Power BI, Data Engineering, Data Warehousing, Data Science, Data Integration, Real-Time Intelligence, OneLake, Admin & Governance, Microsoft Purview, Data Dev, Developer Experiences, Microsoft Foundry, Power Platform

### SQLCON (6 tracks)
Database focused: SQL Server, Azure SQL, SQL in Fabric, Cosmos DB, PostgreSQL, MySQL

## Requirements

- [Obsidian](https://obsidian.md/) (free)
- **Bases** core plugin enabled

## Data Source

Session and speaker data sourced from the official FabCon 2026 agenda via the Sessionize API. Data is current as of the last commit date.

## Issues and Feedback

Found a bug, missing session, or have a suggestion? Please open an issue at:

**https://github.com/kevarnold972/Fabcon2026/issues**

---

*This vault is a community project and is not officially affiliated with Microsoft or the FabCon conference organizers.*
