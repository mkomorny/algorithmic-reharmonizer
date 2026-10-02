# Algorithmic Reharmonizer - Usage Guide

## Prerequisites
- **Python**: 3.8+

---

## 1. Command-Line Usage

Reharmonize a classic `ii-V-I` progression (`Dm7 G7 Cmaj7`) into Neo-Soul:
```bash
python scripts/reharmonize.py --chords "Dm7 G7 Cmaj7" --style neo-soul
```

Apply Jazz Tritone Substitutions:
```bash
python scripts/reharmonize.py --chords "Dm7 G7 Cmaj7" --style tritone-sub
```

Apply Cinematic Modal Borrowing:
```bash
python scripts/reharmonize.py --chords "C Am F G" --style modal-interchange
```

---

## 2. Programmatic Python Import

```python
from scripts.reharmonize import reharmonize_progression

original = ["Cmaj7", "Am7", "Dm7", "G7"]
variations = reharmonize_progression(original, mode="all")
print(variations)
```
