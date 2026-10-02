# Algorithmic Reharmonizer

An algorithmic music theory engine written in pure Python standard library. It transforms standard, basic, or repetitive chord progressions into sophisticated **Neo-Soul**, **Modern Jazz (Tritone Substitutions)**, and **Cinematic Modal Interchange** harmonic arrangements.

## Theoretical Reharmonization Modes

1. **Neo-Soul & Gospel Extensions**:
   - Elevates basic triads and 7ths to lush 9ths, 11ths, and 13ths.
   - Inserts chromatic passing chords, diminished passing movements, and smooth half-step voice leading.
2. **Modern Jazz & Tritone Substitutions**:
   - Analyzes secondary dominants and substitutes dominant 7th chords with their tritone counterparts (`subV7`, e.g., substituting `Db7` for `G7` resolving to `Cmaj7`).
   - Introduces sharp/flat altered tensions (`7#9`, `7b13`, `7alt`).
3. **Cinematic Modal Interchange**:
   - Borrows evocative chords from parallel minor modes (Aeolian, Dorian, Phrygian).
   - Generates emotional minor iv cadences (`iv6` to `I`), flat-VI (`bVI`), and backdoor dominants (`bVII7`).

## Dependencies

- **Python**: Version 3.8+ (Standard Library only: `sys`, `json`, `argparse`, `pathlib`). Zero third-party pip dependencies.

## Instructions

See [INSTRUCTIONS.md](./INSTRUCTIONS.md) for CLI commands, JSON API input/output, and music theory examples.
