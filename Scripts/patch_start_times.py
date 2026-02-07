#!/usr/bin/env python3
"""
Script to add start_time_24h field to all session and workshop markdown files.
This field enables proper chronological sorting in Obsidian Bases.
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime

def get_vault_path():
    """
    Determine the vault path automatically.
    
    Returns:
        Path object pointing to the vault root directory
    """
    # Try to find vault path relative to script location
    script_dir = Path(__file__).parent
    vault_path = script_dir.parent
    
    # Verify this looks like the vault by checking for expected directories
    if (vault_path / 'Sessions').exists() and (vault_path / 'Workshops').exists():
        return vault_path
    
    # Fallback to current working directory
    cwd = Path.cwd()
    if (cwd / 'Sessions').exists() and (cwd / 'Workshops').exists():
        return cwd
    
    # Last resort: hardcoded path for GitHub Actions
    fallback = Path('/home/runner/work/Fabcon2026/Fabcon2026')
    if fallback.exists() and (fallback / 'Sessions').exists():
        return fallback
    
    print("Error: Could not find vault path. Please run from vault root or Scripts directory.")
    sys.exit(1)

def convert_12h_to_24h(time_12h):
    """
    Convert 12-hour time format to 24-hour format.
    
    Args:
        time_12h: String in format like "1:45 PM" or "9:00 AM"
    
    Returns:
        String in format "13:45" or "09:00", or None if conversion fails
    """
    if not time_12h:
        return None
    
    try:
        # Parse the 12-hour time
        dt = datetime.strptime(time_12h.strip(), "%I:%M %p")
        # Format as 24-hour time
        return dt.strftime("%H:%M")
    except ValueError as e:
        print(f"Warning: Could not parse time '{time_12h}': {e}")
        return None

def process_markdown_file(filepath):
    """
    Process a markdown file to add start_time_24h field after start_time.
    
    Args:
        filepath: Path to the markdown file
    
    Returns:
        True if file was modified, False otherwise
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if start_time_24h already exists
    if 'start_time_24h:' in content:
        return False
    
    # Find the start_time field using regex - handles both quoted and unquoted formats
    # Matches: start_time: "10:10 AM" or start_time: 10:10 AM
    match = re.search(r'^start_time:\s*"?([^"\n]+?)"?\s*$', content, re.MULTILINE)
    if not match:
        print(f"Warning: No start_time found in {filepath}")
        return False
    
    time_12h = match.group(1).strip()
    time_24h = convert_12h_to_24h(time_12h)
    
    if not time_24h:
        print(f"Warning: Could not convert time in {filepath}")
        return False
    
    # Insert start_time_24h right after start_time line
    # Find the full line including newline
    start_time_line = match.group(0)
    new_line = f'{start_time_line}\nstart_time_24h: "{time_24h}"'
    
    # Replace in content
    new_content = content.replace(start_time_line, new_line, 1)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {filepath}: {time_12h} -> {time_24h}")
    return True

def main():
    """Main function to process all session and workshop files."""
    vault_path = get_vault_path()
    print(f"Using vault path: {vault_path}\n")
    
    # Find all markdown files in Sessions and Workshops
    session_files = list(vault_path.glob('Sessions/*.md'))
    workshop_files = list(vault_path.glob('Workshops/*.md'))
    
    all_files = session_files + workshop_files
    
    print(f"Found {len(session_files)} session files")
    print(f"Found {len(workshop_files)} workshop files")
    print(f"Total: {len(all_files)} files to process\n")
    
    modified_count = 0
    for filepath in sorted(all_files):
        if process_markdown_file(filepath):
            modified_count += 1
    
    print(f"\n✓ Modified {modified_count} files")
    print(f"✓ Skipped {len(all_files) - modified_count} files (already have start_time_24h)")

if __name__ == '__main__':
    main()
