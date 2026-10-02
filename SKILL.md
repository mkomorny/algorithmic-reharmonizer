---
name: reharmonization-engine
description: Transforms simple, standard, or repetitive chord progressions into sophisticated Neo-Soul, Modern Jazz (Tritone substitutions), and Cinematic Modal Interchange variations with step-by-step harmonic explanations. Triggered in chat whenever the user asks to reharmonize, spice up, add passing chords, or make chords more emotional.
---

# Reharmonization Engine

Upgrades basic, repetitive, or predictable chord progressions into 3 distinct harmonic aesthetics: **Neo-Soul & R&B**, **Modern Jazz (Tritone Sub)**, and **Cinematic Modal Interchange**.

Whenever the user asks to spice up a chord progression, add passing chords, reharmonize a melody, or make chords sound richer, activate this skill.

---

## When to Activate

Trigger this skill whenever the user says things like:
* *"Take this chord progression (C - G - Am - F) and reharmonize it."*
* *"How can I make this chord loop sound more like Neo-Soul or D'Angelo?"*
* *"Give me some spicy jazz passing chords or tritone substitutions for this chorus."*
* *"Make this chord sequence more emotional using borrowed chords."*
* *"How do I reharmonize this simple 4-chord loop?"*

---

## The 3 Reharmonization Flavors

1. **Neo-Soul & R&B:** Expands basic triads into rich 9ths, 11ths, and 13ths while injecting half-step chromatic passing chords (e.g. $Eb7\#9 \rightarrow Dm9$) and secondary dominants.
2. **Modern Jazz (Tritone Sub):** Replaces traditional dominant $V^7$ chords with their tritone substitutions ($subV^7$) spaced 6 semitones away, creating silky chromatic bass step-downs (e.g. $Dm7 \rightarrow Db7 \rightarrow Cmaj7$).
3. **Cinematic Modal Interchange:** Borrows poignant chords from the parallel minor mode—injecting the bittersweet minor $iv$ chord (e.g. $Fm6$ in C major), dramatic $\flat VI$ major 7ths, and ethereal backdoor $\flat VII$ chords.

---

## How to Execute Under the Hood (Silent Agent Workflow)

You do **NOT** ask the user to run scripts in PowerShell. Run the engine invisibly using terminal/bash commands:

```bash
python "<skill_dir>/scripts/reharmonize.py" --chords "C,Am,F,G"
```

The script analyzes the tonic center, calculates substitutions, and returns clean JSON containing the 3 variations and theoretical explanations.

---

## Chat Presentation Guidelines

When presenting the reharmonizations to the user in chat:

1. **Show the Original vs. Variations clearly** in a side-by-side table or distinct block sections.
2. **Explain the Music Theory "Secret Sauce":** Point out the exact moment a chromatic step or borrowed chord creates tension and release.
3. **Provide Voicings:** Break down the specific notes (e.g. $Fm6 = F - Ab - C - D$) so they can play it immediately.
4. **Offer Instant Ableton Export:** Ask the user: *"Would you like me to generate an Ableton MIDI clip for any of these variations?"* (Which seamlessly bridges to `ableton-midi-chord-builder`).
