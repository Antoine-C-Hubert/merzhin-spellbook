# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a D&D 5e spellbook interface project for the character Merzhin. It consists of:

- **spellbook.json**: Main spell data file containing French D&D spells with learning progress tracking
- **spellbook.html**: Self-contained web interface with embedded spell data and offline functionality
- **spellbook.py**: Python script to fetch D&D spells from the SRD API (dnd5eapi.co)
- **update-spellbook.sh**: Shell script to sync JSON data into the HTML file

## Key Commands

### Update spell data in HTML file
```bash
./update-spellbook.sh
```
This syncs the latest spellbook.json data into the HTML file's embedded data section, allowing offline usage.

### Fetch new spells from API
```bash
python3 spellbook.py [output_file]
```
Fetches all D&D 5e spells from the free SRD API and saves to JSON format (defaults to dnd_spells.json).

### Serve locally for development
```bash
python3 -m http.server 8000
# Then open http://localhost:8000/spellbook.html
```

## Architecture

### Data Flow
1. **spellbook.py** fetches spell data from dnd5eapi.co and generates structured JSON
2. **spellbook.json** contains the curated spell data with French translations and learning progress
3. **update-spellbook.sh** embeds JSON data into HTML for standalone functionality
4. **spellbook.html** displays spells with BJJ belt color system and filtering

### Spell Data Structure
Each spell contains standard D&D 5e fields plus custom fields:
- `learned`: Boolean tracking if spell is known
- `learning_source`: Where the spell was learned
- `comment`: Personal notes about spell usage
- `score`: Personal rating (1-4)

### Visual Design System
- **Spell levels**: BJJ belt colors (white → red for levels 0-9)
- **Magic schools**: Color-coded backgrounds
- **Special indicators**: Icons for ritual 🕯️, concentration 🧠, reaction ⚡
- **Book aesthetic**: Leather spine, parchment texture, realistic styling

### File Dependencies
- HTML file can work standalone after running update-spellbook.sh
- Python script requires internet access for API calls
- Shell script requires jq for JSON processing statistics