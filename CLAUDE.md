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
start_time_24h: "13:45"
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

---

## Replicating This Vault for Another Conference

This section documents how to create a similar vault for a different conference.

### Step 1: Find the Data Source

Most tech conferences use **Sessionize** for session management. To find the API:

1. Go to the conference agenda page
2. View page source (Ctrl+U) and search for "sessionize.com/api"
3. Look for URLs like `https://sessionize.com/api/v2/XXXXXX/view/All`
4. The API returns JSON with sessions, speakers, rooms, and categories

**Alternative sources:**
- Conference website with structured agenda
- Sched.com (similar API pattern)
- Custom conference apps (may need scraping)

### Step 2: Understand the API Structure

Sessionize API returns:
```json
{
  "sessions": [...],      // All session data
  "speakers": [...],      // All speaker profiles
  "rooms": [...],         // Room name mappings
  "categories": [...]     // Tracks, levels, session types, etc.
}
```

Key session fields:
- `title`, `description` - Session content
- `startsAt`, `endsAt` - ISO datetime strings
- `roomId` - Maps to rooms array
- `speakers` - Array of speaker IDs
- `categoryItems` - Array of category IDs (track, level, etc.)

Key speaker fields:
- `fullName`, `bio`, `tagLine` - Profile info
- `links` - Social media URLs
- `sessions` - Array of session IDs
- `categoryItems` - Speaker type categories

### Step 3: Create the Vault Structure

```
Conference Name/
├── CLAUDE.md           # This file - project documentation
├── README.md           # User-facing documentation
├── Bases/              # Obsidian Bases for dynamic views
├── Planning/           # Dashboard, schedule, conflicts
├── Sessions/           # Breakout sessions
├── Workshops/          # Pre-conference workshops (if applicable)
├── Speakers/           # Speaker profiles
├── Tracks/             # Track overview pages
└── Templates/          # Templates for manual additions
```

### Step 4: Create Python Scripts

#### Session/Workshop Creation Script Pattern

```python
import requests
import re
from pathlib import Path
from datetime import datetime

API_URL = "https://sessionize.com/api/v2/XXXXXX/view/All"
VAULT_PATH = Path(r"path/to/vault")

# Fetch data
data = requests.get(API_URL).json()

# Build lookup maps
rooms_map = {r['id']: r['name'] for r in data.get('rooms', [])}
speakers_map = {s['id']: s for s in data.get('speakers', [])}

# Build categories map (tracks, levels, session types)
categories_map = {}
for cat in data.get('categories', []):
    for item in cat.get('items', []):
        categories_map[item['id']] = {
            'name': item['name'],
            'category': cat['title']  # e.g., "Track", "Level", "Session Type"
        }

# Process sessions
for session in data.get('sessions', []):
    title = session['title']

    # Parse datetime
    starts_at = session.get('startsAt')
    if starts_at:
        dt = datetime.fromisoformat(starts_at.replace('Z', '+00:00'))
        date_str = dt.strftime("%Y-%m-%d")
        start_time = dt.strftime("%I:%M %p").lstrip('0')
        day = dt.strftime("%A")

    # Get room
    room = rooms_map.get(session.get('roomId'), '')

    # Get speakers
    speaker_names = [speakers_map[sid]['fullName']
                     for sid in session.get('speakers', [])
                     if sid in speakers_map]

    # Get categories (track, level, etc.)
    track = ""
    level = ""
    for cid in session.get('categoryItems', []):
        if cid in categories_map:
            cat_info = categories_map[cid]
            if 'track' in cat_info['category'].lower():
                track = cat_info['name']
            elif 'level' in cat_info['category'].lower():
                level = cat_info['name']

    # Build frontmatter and content
    # ... (see existing scripts in scratchpad for full examples)
```

#### Speaker Creation Script Pattern

```python
# Similar pattern - iterate speakers, extract:
# - fullName, bio, tagLine (parse for role/company)
# - links (LinkedIn, Twitter, Blog)
# - categoryItems (speaker type)
# - sessions (to determine which conference track)
```

### Step 5: Create Base Files

Copy and adapt the Bases from this vault:

| Base File | Adapt For |
|-----------|-----------|
| `Track Sessions.base` | Change folder names if different |
| `Speaker Sessions.base` | Usually works as-is |
| `My Attending Sessions.base` | Update day names if different schedule |
| `All Sessions.base` | Update groupBy properties if schema differs |
| `Session Conflicts.base` | Update time slot grouping |

### Step 6: Create Planning Files

- **Conference Dashboard.md** - Update conference info, embed bases
- **My Schedule.md** - Update day structure to match conference
- **Session Conflicts.md** - Embed conflict detection base

### Step 7: Verification Checklist

After initial data import:

- [ ] Session count matches API count
- [ ] All sessions have `room:` populated
- [ ] All sessions have `speakers:` with wiki links
- [ ] All sessions have `track:` with wiki link
- [ ] All sessions have `## Description` content
- [ ] Speaker count matches API count
- [ ] All speakers have bios
- [ ] Track files exist for all unique tracks
- [ ] Bases render correctly in Obsidian
- [ ] Planning views show correct data

### Common Issues and Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| TypeError with None | API returns null for optional fields | Use `value or ''` pattern |
| Missing sessions | Partial API fetch or fuzzy matching issues | Compare normalized titles |
| Empty rooms | Session not yet scheduled | Re-sync closer to conference |
| Broken wiki links | Speaker/track name mismatch | Ensure exact name matching |
| Bases not rendering | Plugin not enabled | Enable Bases in core plugins |

### Maintenance

- **Before conference**: Re-sync data weekly as schedule changes
- **During conference**: Update with room changes, cancellations
- **After conference**: Add notes, resources, recordings links
