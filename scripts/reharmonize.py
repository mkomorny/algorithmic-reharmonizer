#!/usr/bin/env python3
"""
Reharmonization Engine
Transforms standard chord progressions into Neo-Soul, Modern Jazz (Tritone Sub), and Modal Interchange variations.
"""

import sys
import json
import argparse
from pathlib import Path

NOTE_NAMES = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
SEMITONE_MAP = {
    "C": 0, "C#": 1, "DB": 1, "D": 2, "D#": 3, "EB": 3,
    "E": 4, "FB": 4, "E#": 5, "F": 5, "F#": 6, "GB": 6,
    "G": 7, "G#": 8, "AB": 8, "A": 9, "A#": 10, "BB": 10,
    "B": 11, "CB": 11, "B#": 0
}

def parse_chord_token(chord_str):
    chord_str = chord_str.strip()
    if "/" in chord_str:
        chord_str = chord_str.split("/")[0].strip()
    if len(chord_str) > 1 and chord_str[1] in ["#", "b", "B"]:
        root = chord_str[:2].capitalize()
        quality = chord_str[2:].lower()
    else:
        root = chord_str[:1].upper()
        quality = chord_str[1:].lower()
    
    root_val = SEMITONE_MAP.get(root.upper(), 0)
    is_minor = any(q in quality for q in ["m", "min", "dim"]) and not any(q in quality for q in ["maj", "6"])
    return {
        "original": chord_str,
        "root": root,
        "root_val": root_val,
        "quality": quality,
        "is_minor": is_minor
    }

def get_root_name(val):
    return NOTE_NAMES[val % 12]

def reharmonize_progression(chord_list):
    parsed = [parse_chord_token(c) for c in chord_list if c.strip()]
    if not parsed:
        return {"error": "No chords provided."}
        
    n = len(parsed)
    
    # 1. Neo-Soul / R&B Variation (Lush Extensions & Chromatic Passing Chords)
    neo_soul_chords = []
    neo_soul_notes = []
    
    for i, c in enumerate(parsed):
        root = c["root"]
        root_val = c["root_val"]
        is_min = c["is_minor"]
        
        # Upgrade triad to 9th/11th/13th
        if is_min:
            new_chord = f"{root}m9"
        elif "7" in c["quality"] or "dom" in c["quality"]:
            new_chord = f"{root}13"
        elif "dim" in c["quality"]:
            new_chord = f"{root}m7b5"
        else:
            new_chord = f"{root}maj9"
            
        neo_soul_chords.append(new_chord)
        
        # Add chromatic passing dominant between chords if distance is a whole step
        if i < n - 1:
            next_val = parsed[i+1]["root_val"]
            # If descending whole step (e.g. F to Eb, or D to C), slip in half-step chromatic passing chord
            if (root_val - next_val) % 12 == 2:
                passing_root = get_root_name(root_val - 1)
                neo_soul_chords.append(f"{passing_root}7#9")
                neo_soul_notes.append(f"Injected chromatic passing chord ({passing_root}7#9) for smooth half-step descent to {parsed[i+1]['root']}.")
            # If ascending whole step, slip in secondary dominant
            elif (next_val - root_val) % 12 == 2:
                sec_dom_root = get_root_name(next_val + 7)
                neo_soul_chords.append(f"{sec_dom_root}7alt")
                neo_soul_notes.append(f"Injected secondary dominant ({sec_dom_root}7alt) leading into {parsed[i+1]['root']}.")

    # 2. Modern Jazz & Tritone Substitution Variation
    jazz_chords = []
    jazz_notes = []
    for i, c in enumerate(parsed):
        root = c["root"]
        root_val = c["root_val"]
        is_min = c["is_minor"]
        
        # Check if this chord functions as a dominant leading to next chord (down a fifth / up a fourth)
        is_dominant = "7" in c["quality"] and not is_min and not "maj" in c["quality"]
        if not is_dominant and not is_min and i < n - 1:
            next_val = parsed[i+1]["root_val"]
            if (root_val - next_val) % 12 == 7: # Standard 5th resolution
                is_dominant = True
                
        if is_dominant:
            # Tritone substitution: Root + 6 semitones
            sub_val = (root_val + 6) % 12
            sub_root = get_root_name(sub_val)
            sub_chord = f"{sub_root}7#11"
            jazz_chords.append(sub_chord)
            next_name = parsed[(i+1)%n]["root"]
            jazz_notes.append(f"Replaced dominant {root}7 with Tritone Sub {sub_chord} creating chromatic bass step to {next_name}.")
        elif is_min:
            jazz_chords.append(f"{root}m11")
        else:
            jazz_chords.append(f"{root}maj7#11")

    # 3. Modal Interchange / Cinematic Variation (Borrowed Chords from Parallel Minor)
    modal_chords = []
    modal_notes = []
    tonic_val = parsed[0]["root_val"]
    tonic_root = parsed[0]["root"]
    
    for i, c in enumerate(parsed):
        root = c["root"]
        root_val = c["root_val"]
        interval = (root_val - tonic_val) % 12
        
        # If standard IV chord in major (interval 5), turn into minor iv or bVI
        if interval == 5 and not c["is_minor"]:
            modal_chords.append(f"{root}m6")
            modal_notes.append(f"Borrowed minor iv ({root}m6) from parallel minor for classic bittersweet cinematic nostalgia.")
        # If standard V chord (interval 7), turn into bVII backdoor dominant
        elif interval == 7 and not c["is_minor"]:
            bVII_root = get_root_name(tonic_val + 10)
            modal_chords.append(f"{bVII_root}maj9")
            modal_notes.append(f"Substituted dominant V with borrowed bVII ({bVII_root}maj9) for an ethereal unresolved lift.")
        # If tonic major, leave as lush tonic or add bVI passing chord
        elif interval == 0 and not c["is_minor"]:
            modal_chords.append(f"{root}maj9")
            if i == 0 and n > 2:
                bVI_root = get_root_name(tonic_val + 8)
                modal_chords.append(f"{bVI_root}maj7")
                modal_notes.append(f"Added dramatic bVI borrowed chord ({bVI_root}maj7) right after tonic.")
        else:
            modal_chords.append(c["original"])

    return {
        "original_progression": [c["original"] for c in parsed],
        "variations": [
            {
                "flavor": "Neo-Soul & R&B (Lush 9ths, 11ths & Chromatic Passing Chords)",
                "chords": neo_soul_chords,
                "theory_notes": neo_soul_notes
            },
            {
                "flavor": "Modern Jazz (Tritone Substitutions & Altered Dominants)",
                "chords": jazz_chords,
                "theory_notes": jazz_notes
            },
            {
                "flavor": "Cinematic & Modal Interchange (Borrowed Parallel Minor Chords)",
                "chords": modal_chords,
                "theory_notes": modal_notes
            }
        ]
    }

def main():
    parser = argparse.ArgumentParser(description="Reharmonize chord progressions.")
    parser.add_argument("--chords", required=True, help="Comma-separated chord names (e.g. 'C,Am,F,G')")
    args = parser.parse_args()
    
    chords = [c.strip() for c in args.chords.replace("->", ",").replace("-", ",").split(",") if c.strip()]
    result = reharmonize_progression(chords)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
