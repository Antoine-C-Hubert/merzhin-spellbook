# D&D Spellbook Interface

A beautiful web interface for viewing and managing D&D spells with a realistic book design.

## Features

- **Realistic book design** with leather spine and parchment texture
- **BJJ belt color system** for spell levels (white → yellow → orange → green → blue → purple → brown → black → red)
- **School-based color coding** for spell categorization
- **Interactive filtering** by level, school, class, and learning status
- **Search functionality** across spell names and descriptions
- **Learning progress tracking** with comprehensive statistics
- **Special spell icons** for ritual, concentration, and reaction spells
- **Learning source tracking** for learned spells

## Files

- `spellbook.json` - Main spell data file
- `spellbook.html` - Web interface (self-contained)
- `update-spellbook.sh` - Script to sync JSON data into HTML

## Usage

### Method 1: Direct Opening (Recommended)
Simply double-click `spellbook.html` to open it in your browser. The file contains embedded spell data and works without any server setup.

### Method 2: With Web Server (For Development)
If you want the interface to automatically load the latest `spellbook.json` data:

```bash
# Start a simple web server
python3 -m http.server 8000

# Open in browser
open http://localhost:8000/spellbook.html
```

## Updating Spell Data

When you modify `spellbook.json`, run the update script to sync the embedded data:

```bash
./update-spellbook.sh
```

This ensures the HTML file works offline with the latest spell data.

## Spell Data Structure

Each spell in `spellbook.json` contains:
- `name` - Spell name in French
- `level` - Spell level (0-9)
- `school` - Magic school (Abjuration, Evocation, etc.)
- `class` - Available classes array
- `casting_time` - Time to cast
- `range` - Spell range
- `components` - V/S/M components array
- `concentration` - Boolean for concentration spells
- `ritual` - Boolean for ritual spells
- `reaction` - Boolean for reaction spells
- `duration` - Spell duration
- `description` - Full spell description
- `higher_levels` - Scaling effects (optional)
- `origin` - Source book
- `learned` - Boolean for learning status
- `learning_source` - Where the spell was learned (optional)

## Color System

### Spell Levels (BJJ Belt Colors)
- Level 0 (Cantrips): White
- Level 1: White → Yellow
- Level 2: Yellow → Orange  
- Level 3: Orange → Green
- Level 4: Green → Blue
- Level 5: Blue → Purple
- Level 6: Purple → Brown
- Level 7: Brown → Black
- Level 8: Black → Red
- Level 9: Red

### Magic Schools
- Abjuration: Blue
- Invocation: Red
- Divination: Gold
- Enchantement: Pink
- Évocation: Orange
- Illusion: Purple
- Nécromancie: Dark Gray
- Transmutation: Green

## Statistics

The interface displays comprehensive statistics in two rows:
- **Row 1**: Total spells by level
- **Row 2**: Learned spells by level

## Icons

- 🕯️ **Ritual** (Purple): Can be cast as a ritual
- 🧠 **Concentration** (Orange): Requires concentration
- ⚡ **Reaction** (Red): Cast as a reaction