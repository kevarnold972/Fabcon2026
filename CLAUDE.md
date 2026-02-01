# FabCon 2026 Obsidian Vault

## Project Overview

This is an Obsidian vault for planning attendance at FabCon 2026 (Microsoft Fabric Community Conference) and SQLCON 2026, co-located conferences in Atlanta, GA from March 16-20, 2026.

## Structure

```
Fabcon 2026/
├── Bases/              # Obsidian Bases (.base files) for dynamic views
├── Templates/          # Obsidian templates for new notes
├── Tracks/             # 19 track overview files
├── Planning/           # Dashboard, schedule, and conflict resolution
├── Workshops/
│   ├── Monday/         # 11 full-day workshops (March 16)
│   └── Tuesday/        # 11 full-day workshops (March 17)
├── Sessions/           # Breakout sessions (Wed-Fri, March 18-20)
└── Speakers/           # Speaker profile files
```

## Conference Schedule

| Day | Date | Type |
|-----|------|------|
| Monday | March 16 | Workshops (9 AM - 5 PM) |
| Tuesday | March 17 | Workshops (9 AM - 5 PM) |
| Wednesday | March 18 | Keynote + Sessions |
| Thursday | March 19 | Sessions + Expo |
| Friday | March 20 | Sessions |

## Obsidian Bases

This vault uses **Obsidian Bases** (core plugin) instead of Dataview for dynamic views. Base files are stored in `Bases/` and embedded in markdown files using `![[BaseFile.base]]` or `![[BaseFile.base#ViewName]]` syntax.

### Base Files

| File | Purpose |
|------|---------|
| `Track Sessions.base` | Shows sessions for the embedding track file (uses `this.file`) |
| `Speaker Sessions.base` | Shows sessions for the embedding speaker file (uses `this.file`) |
| `My Attending Sessions.base` | Sessions with status="Attending", views by day |
| `Considering Sessions.base` | Sessions with status="Considering" |
| `High Interest Sessions.base` | Sessions with interest >= 4 |
| `All Sessions.base` | All sessions grouped by Status, Interest, Track, Day |
| `All Speakers.base` | List of all speakers |
| `All Tracks.base` | List of all tracks |
| `Session Conflicts.base` | Sessions by time slot for conflict detection |

### Bases Syntax Reference

Bases use YAML syntax. Key patterns used in this vault:

```yaml
# Filter by folder
filters:
  or:
    - file.inFolder("Sessions")
    - file.inFolder("Workshops")

# Filter by property value
filters:
  and:
    - status == "Attending"
    - day == "Wednesday"

# Dynamic filter using embedding file (for Track/Speaker pages)
filters:
  - file.hasLink(this.file)

# Views with grouping
views:
  - type: table
    name: "By Status"
    groupBy:
      property: status
      direction: DESC
    order:
      - file.name
      - day
      - start_time
```

### Embedding Bases

```markdown
# Embed default view
![[Track Sessions.base]]

# Embed specific view by name
![[My Attending Sessions.base#Wednesday]]
![[All Sessions.base#By Track]]
```

## YAML Frontmatter Schema

### Sessions & Workshops
```yaml
title: "Session Title"
date: 2026-03-18
day: Wednesday
start_time: "1:45 PM"
end_time: "2:45 PM"
duration: 60
room: "C111-C112"
track: "[[Power BI Track]]"
session_type: "Breakout Session"  # Workshop, CORENOTE, Sponsor Speaker, etc.
level: 200
level_name: "Feature Oriented"    # 100=Business, 200=Feature, 300=Technical, 400=Deep Technical
audience:
  - Data Engineer
  - Data Analyst
speakers:
  - "[[Speaker Name]]"
conference: FABCON                # or SQLCON
requires_laptop: true             # workshops only
url: ""
interest:                         # 1-5 rating
status: Considering               # Considering, Attending, Skip
tags:
  - fabcon2026
```

### Speakers
```yaml
type: Speaker
name: "Speaker Name"
company: ""
role: ""
conference: FABCON
speaker_type: Community Session Speaker
```

### Tracks
```yaml
type: Track
track_name: Power BI Track
conference: FABCON
```

## Key Files for Planning

- `Planning/My Schedule.md` - Day-by-day view of sessions marked "Attending"
- `Planning/Conference Dashboard.md` - Overview stats and quick links
- `Planning/Session Conflicts.md` - Identify overlapping time slots

## Obsidian Plugins Required

- **Bases** - Core plugin (enable in Settings > Core plugins)

## Workflow

1. Browse sessions by Track or use the Dashboard
2. Set `interest: 1-5` to rate sessions
3. Change `status: Considering` to `status: Attending` for sessions to attend
4. Check My Schedule to see your plan by day
5. Use Session Conflicts to resolve overlapping sessions

## Conferences

- **FABCON** - Microsoft Fabric focused (13 tracks)
- **SQLCON** - SQL Server, Azure SQL, PostgreSQL, MySQL focused (6 tracks)

## Tracks

### FABCON Tracks
- Admin and Governance
- Power BI
- Data Engineering
- Data Warehousing
- Data Science
- Data Integration
- Real-Time Intelligence
- OneLake
- Microsoft Purview
- Data Dev
- Developer Experiences
- Microsoft Foundry
- Power Platform

### SQLCON Tracks
- SQL Server
- Azure SQL
- SQL in Fabric
- Cosmos DB
- PostgreSQL
- MySQL

## Data Source

**Official session data via Sessionize APIs (authoritative source):**
- Workshops: `https://sessionize.com/api/v2/coqpz3x7/view/All`
- Sessions: `https://sessionize.com/api/v2/1op0w2v7/view/All`

These APIs return JSON with complete session data including: title, description, date/time, room, speakers, track, level, audience, and session type.

### Syncing Session Data

When updating or verifying session data:

1. **Always use the Sessionize APIs** - they are the source of truth for the official agenda
2. **Count verification** - API should return 267 total sessions (245 sessions + 22 workshops as of Jan 2026)
3. **After any sync, verify counts match** - compare vault file count to API count
4. **Unverified sessions** go in `Sessions/_Unverified/` or `Workshops/_Unverified/`
5. **Check for empty `room:` fields** - indicates incomplete data that needs updating

### Session File Validation

A properly populated session file should have:
- `room:` with an actual value (not empty)
- `speakers:` with `[[Speaker Name]]` links
- `track:` with `[[Track Name]]` link
- `## Description` section with content

## Tool Preferences

When scraping or fetching web data, prefer **Python with requests/BeautifulSoup** over browser automation (Chrome MCP). Python is faster, more reliable, and uses less resources for data extraction tasks.
