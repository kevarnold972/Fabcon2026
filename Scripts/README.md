# Scripts for Fabcon2026 Vault Maintenance

This directory contains utility scripts for maintaining the Obsidian vault.

## patch_start_times.py

**Purpose:** Add `start_time_24h` field to session and workshop markdown files.

**Use case:** 
- When importing new sessions from Sessionize API
- When the field is missing from existing files
- After regenerating session files from source data

**What it does:**
1. Scans all markdown files in `Sessions/` and `Workshops/` directories
2. For each file with a `start_time` field but no `start_time_24h` field:
   - Converts the 12-hour time format (e.g., "1:45 PM") to 24-hour format (e.g., "13:45")
   - Inserts the `start_time_24h` field immediately after `start_time`
3. Skips files that already have the field to preserve user edits

**Usage:**
```bash
cd /path/to/Fabcon2026
python Scripts/patch_start_times.py
```

**Example output:**
```
Using vault path: /path/to/Fabcon2026

Found 245 session files
Found 22 workshop files
Total: 267 files to process

Updated Sessions/AI in Action.md: 4:25 PM -> 16:25
Updated Workshops/Power BI Mastery.md: 9:00 AM -> 09:00
...

✓ Modified 267 files
✓ Skipped 0 files (already have start_time_24h)
```

Note: The example shows all 267 files being updated. On subsequent runs, most files will be skipped since they already have the field.

**Why this field exists:**

The `start_time_24h` field enables correct chronological sorting in Obsidian Bases. When sorting by the original `start_time` field (12-hour format), times sort alphabetically which produces incorrect ordering:

- Incorrect (12h alphabetical): "1:00 PM", "10:10 AM", "11:30 AM", "2:00 PM"
- Correct (24h alphabetical): "08:00", "10:10", "11:30", "13:00", "14:00"

All `.base` files sort by `start_time_24h` to ensure sessions appear in chronological order.

**Safe to run multiple times:** The script checks for existing `start_time_24h` fields and only updates files that are missing the field.
