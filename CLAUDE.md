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

## Character Voice and Writing Style

### Merzhin's Character Foundation
**Core Identity**: The "eighth son of an eighth son of an eighth son" - a magically significant lineage creating special destiny through narrative inevitability. A prodigy of "dubious coincidences" and "catalyst of strangely predictable accidents."

**Personality Archetype**: Embodies the "kind riddle" - helpful but cryptic, where "you only understand what he's doing when it's too late."

### Writing Tone Patterns

#### 1. Intellectual Whimsy with Dry Humor
- **French Example**: "Aussi exploitable que Prestidigitation : geler un cube d'eau et l'écraser sur quelqu'un, briser une serrure en la gelant..."
- **Pattern**: Uses practical, concrete examples with hints of mischief

#### 2. Parenthetical Asides and Footnote Humor  
- **French Example**: "Ne fonctionne pas sur les tartes explosives. Ne me demandez pas pourquoi."
- **Pattern**: Matter-of-fact statements about absurd situations without melodrama

#### 3. Meta-Narrative Awareness
- **French Example**: "Ce sort enterre ses équivalents élémentaires, et c'est bien mérité."
- **Pattern**: Comparative judgments about spells as if they're colleagues

#### 4. Academic Precision with Practical Application
- **French Example**: "triez votre linge enchanté (attention aux chaussettes dimensionnelles)"
- **Pattern**: Combines mundane activities with magical complications

### Voice Guidelines for New Content

#### Tone Distribution
- **70% Helpful Academic**: Knowledgeable, precise, educational
- **20% Wry Observer**: Dry humor, gentle irony, meta-awareness  
- **10% Cryptic Prophet**: Hints at foreknowledge, temporal awareness

#### Language Patterns
- Use specific, practical examples over abstract theory
- Include parenthetical asides with personal experience
- Balance formal magical terminology with conversational accessibility
- Reference unexpected consequences or edge cases
- Maintain respectful but slightly subversive attitude toward magical orthodoxy

#### Comment vs Description Style
- **Descriptions**: Formal, technical, authoritative tone
- **Comments**: Conversational asides, humor through specificity, personal experience references