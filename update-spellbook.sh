#!/bin/bash

# Script to update the embedded JSON data in spellbook.html from spellbook.json
# This allows the HTML file to work without a web server while staying in sync with the JSON file

set -e  # Exit on any error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JSON_FILE="$SCRIPT_DIR/spellbook.json"
HTML_FILE="$SCRIPT_DIR/spellbook.html"
TEMP_FILE="$SCRIPT_DIR/spellbook_temp.html"

# Check if files exist
if [[ ! -f "$JSON_FILE" ]]; then
    echo "Error: spellbook.json not found in $SCRIPT_DIR"
    exit 1
fi

if [[ ! -f "$HTML_FILE" ]]; then
    echo "Error: spellbook.html not found in $SCRIPT_DIR"
    exit 1
fi

echo "Updating embedded JSON data in spellbook.html..."

# Escape JSON content for safe insertion into HTML
# This function properly escapes the JSON for HTML insertion
escape_json_for_html() {
    # Read the JSON and escape special characters
    sed 's/\\/\\\\/g; s/"/\\"/g' "$JSON_FILE"
}

# Create a temporary file with the updated HTML
{
    # Print everything before the JSON data section
    sed -n '1,/<!-- Embedded spell data as fallback -->/p' "$HTML_FILE"
    
    # Insert the updated JSON data
    echo '    <script type="application/json" id="spell-data">'
    cat "$JSON_FILE"
    echo '    </script>'
    echo ''
    
    # Print everything after the JSON data section
    sed -n '/^    <script>$/,$p' "$HTML_FILE"
    
} > "$TEMP_FILE"

# Replace the original file with the updated version
mv "$TEMP_FILE" "$HTML_FILE"

echo "✅ Successfully updated spellbook.html with latest JSON data"
echo "📖 The HTML file now contains the latest spell data and can be opened directly in any browser"

# Get some stats about the update
TOTAL_SPELLS=$(jq '. | length' "$JSON_FILE" 2>/dev/null || echo "unknown")
LEARNED_SPELLS=$(jq '[.[] | select(.learned == true)] | length' "$JSON_FILE" 2>/dev/null || echo "unknown")

echo "📊 Spellbook contains: $TOTAL_SPELLS total spells, $LEARNED_SPELLS learned"