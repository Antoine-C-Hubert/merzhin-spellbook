#!/usr/bin/env python3
"""
D&D 5e Spellbook Fetcher

Fetches all D&D 5e spells from the open SRD API and stores them in a structured JSON format.
Uses the free D&D 5e API (dnd5eapi.co) to retrieve spell data.
"""

import json
import uuid
import requests
from typing import List, Dict, Any
import time
import sys
from pathlib import Path


class SpellbookFetcher:
    """Fetches D&D 5e spells from API and formats them according to requirements."""
    
    def __init__(self):
        self.base_url = "https://www.dnd5eapi.co/api"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'D&D-Spellbook-Fetcher/1.0'
        })
    
    def fetch_spell_list(self) -> List[Dict[str, str]]:
        """Fetch the list of all available spells."""
        print("Fetching spell list...")
        try:
            response = self.session.get(f"{self.base_url}/spells")
            response.raise_for_status()
            data = response.json()
            return data.get('results', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching spell list: {e}")
            return []
    
    def fetch_spell_details(self, spell_index: str) -> Dict[str, Any]:
        """Fetch detailed information for a specific spell."""
        try:
            response = self.session.get(f"{self.base_url}/spells/{spell_index}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching spell {spell_index}: {e}")
            return {}
    
    def parse_spell_data(self, spell_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse and format spell data according to requirements."""
        if not spell_data:
            return {}
        
        # Extract classes
        classes = []
        if 'classes' in spell_data:
            classes = [cls.get('name', '') for cls in spell_data['classes']]
        
        # Extract components
        components = []
        if 'components' in spell_data:
            components = spell_data['components']
        
        # Generate UUID for this spell
        spell_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, spell_data.get('name', '')))
        
        # Determine origin (SRD spells are from PHB 2014)
        origin = "Player's Handbook (2014 edition)"
        
        # Format the spell according to requirements
        formatted_spell = {
            'id': spell_id,
            'name': spell_data.get('name', ''),
            'level': spell_data.get('level', 0),
            'school': spell_data.get('school', {}).get('name', '') if spell_data.get('school') else '',
            'class': classes,
            'casting_time': spell_data.get('casting_time', ''),
            'range': spell_data.get('range', ''),
            'components': components,
            'duration': spell_data.get('duration', ''),
            'description': '\n'.join(spell_data.get('desc', [])),
            'origin': origin
        }
        
        return formatted_spell
    
    def fetch_all_spells(self) -> List[Dict[str, Any]]:
        """Fetch all spells and format them."""
        spell_list = self.fetch_spell_list()
        if not spell_list:
            print("No spells found!")
            return []
        
        print(f"Found {len(spell_list)} spells. Fetching details...")
        
        all_spells = []
        total_spells = len(spell_list)
        
        for i, spell_ref in enumerate(spell_list, 1):
            spell_index = spell_ref.get('index', '')
            if not spell_index:
                continue
            
            print(f"Fetching spell {i}/{total_spells}: {spell_ref.get('name', spell_index)}")
            
            spell_details = self.fetch_spell_details(spell_index)
            if spell_details:
                formatted_spell = self.parse_spell_data(spell_details)
                if formatted_spell:
                    all_spells.append(formatted_spell)
            
            # Be respectful to the API
            time.sleep(0.1)
        
        return all_spells
    
    def save_spells_to_json(self, spells: List[Dict[str, Any]], output_file: str = "dnd_spells.json"):
        """Save spells to a JSON file."""
        output_path = Path(__file__).parent / output_file
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(spells, f, indent=2, ensure_ascii=False)
            print(f"Successfully saved {len(spells)} spells to {output_path}")
        except Exception as e:
            print(f"Error saving spells to file: {e}")
    
    def run(self, output_file: str = "dnd_spells.json"):
        """Main method to fetch and save all spells."""
        print("Starting D&D 5e Spell Fetcher...")
        print("=" * 50)
        
        spells = self.fetch_all_spells()
        
        if spells:
            self.save_spells_to_json(spells, output_file)
            print(f"\nCompleted! Fetched and saved {len(spells)} spells.")
            
            # Print sample spell for verification
            if spells:
                print("\nSample spell (first in list):")
                print(json.dumps(spells[0], indent=2))
        else:
            print("No spells were fetched successfully.")


def main():
    """Main entry point."""
    output_file = "dnd_spells.json"
    
    # Allow custom output file from command line
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
    
    fetcher = SpellbookFetcher()
    fetcher.run(output_file)


if __name__ == "__main__":
    main()