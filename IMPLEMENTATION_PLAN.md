# Implementation Plan: Reharmonization Engine

Transforms standard, repetitive, or simple chord progressions into sophisticated Neo-Soul, Modern Jazz (Tritone substitutions), and Cinematic Modal Interchange variations.

---

## Deliverables Checklist

### v1.0.0 — Initial Release
- [x] **Core Reharmonization Script**: `scripts/reharmonize.py` performing interval parsing and harmonic transformation. ✅ done in v1.0.0
- [x] **Flavor 1 (Neo-Soul & R&B)**: Extension upgrades (9ths/11ths/13ths) and half-step chromatic passing chords/secondary dominants. ✅ done in v1.0.0
- [x] **Flavor 2 (Modern Jazz)**: Dominant detection, tritone substitutions ($subV^7$), and altered dominant chords. ✅ done in v1.0.0
- [x] **Flavor 3 (Cinematic Modal Interchange)**: Borrowed parallel minor chords ($\text{iv}^{6}$, $\flat\text{VI}\text{maj7}$, and $\flat\text{VII}\text{maj9}$). ✅ done in v1.0.0
- [x] **Tri-Platform Accessibility**: Canonical `.agents` installation linked to Claude, Grok, and Antigravity via NTFS junctions. ✅ done in v1.0.0
- [x] **Standard Documentation Suite**: `SKILL.md`, `HOW_TO_USE.txt`, `README.md`, `App Changes Tracker.html`, and `dev-notes-v1.0.0.md`. ✅ done in v1.0.0

---

## Roadmap & Future Enhancements

### v1.1.0 — Extended Voicing Engine
- [ ] Implement automatic Drop-2 and Rootless jazz voicing generation.
- [ ] Voice-leading smoothness score (calculates total semitone movement between consecutive chords).
- [ ] Parallel fifths and octaves collision detector for classical voice-leading modes.

### v1.2.0 — Direct DAW Clip Export Pipeline
- [ ] Direct programmatic link to `ableton-midi-chord-builder` without requiring manual copy-pasting.
- [ ] Export audio preview renders using local SoundFont synthesis.
- [ ] Support for microtonal and quarter-tone neo-soul detuning offsets.
