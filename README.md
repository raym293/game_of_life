```
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ███████╗    ██╗     ██╗███████╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██╔════╝    ██║     ██║██╔════╝██╔════╝
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║█████╗      ██║     ██║█████╗  █████╗  
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║██╔══╝      ██║     ██║██╔══╝  ██╔══╝  
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝██║         ███████╗██║██║     ███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝ ╚═╝         ╚══════╝╚═╝╚═╝     ╚══════╝
```

<div align="center">

🧬 **Conway's Game of Life** 🧬

*A mesmerizing cellular automaton simulation*

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

![Game](https://img.shields.io/badge/game-Conway's%20Game%20of%20Life-purple.svg)
![Terminal](https://img.shields.io/badge/interface-terminal-black.svg)
![Real%20Time](https://img.shields.io/badge/simulation-real--time-red.svg)
![Zero%20Player](https://img.shields.io/badge/players-zero-orange.svg)

</div>

---

## 🎯 Overview

A Python implementation of Conway's Game of Life - a cellular automaton devised by mathematician John Conway. This zero-player game evolves based on its initial state, requiring no further input from players.

This implementation creates a grid of cells that can be either alive (represented by colored blocks) or dead (empty spaces). The simulation follows the classic rules of Conway's Game of Life and displays the evolution in real-time in your terminal.

```
┌─────────────────────────────────────────┐
│  ████    █    ████   ██   ████   ████  │
│   ██    ███    ██   ████   ██     ██   │
│   ██     █     ██    ██    ██     ██   │
│  ████   ███   ████  ████  ████   ████  │
└─────────────────────────────────────────┘
```

## ✨ Features

- **Customizable board size**: Choose your preferred grid dimensions
- **Multiple starting patterns**: Choose from random generation or 5 preset patterns (Glider, Blinker, Block, Toad, Beacon)
- **Game over detection**: Automatically detects static patterns, oscillating patterns, and empty boards
- **Wrapping boundaries**: Toroidal grid implementation where edges wrap around
- **Real-time visualization**: Watch the patterns evolve with colorful terminal output
- **Pattern recognition**: Intelligent detection of repeating and static states

## 🚀 How to Run

```
┌──────────────────────────────────────┐
│           🎮 LAUNCH GAME 🎮          │
│                                      │
│  python script.py                   │
│                                      │
│  ✨ Enter board size when prompted   │
│  🎨 Watch the magic happen!         │
└──────────────────────────────────────┘
```

1. Make sure you have Python installed on your system
2. Navigate to the project directory
3. Run the script:
   ```bash
   python script.py
   ```
4. Enter your desired board size when prompted
5. Choose whether to override game over mechanisms (for continuous play)
6. Select your starting pattern (random or one of 5 presets)
7. Watch the Game of Life unfold!

## 📜 Game Rules

```
┌─────────────────────────────────────────────────────────────┐
│                    🧬 RULES OF LIFE 🧬                     │
├─────────────────────────────────────────────────────────────┤
│  💀 UNDERPOPULATION   │  < 2 neighbors → cell dies         │
│  💚 SURVIVAL          │  2-3 neighbors → cell survives     │
│  💀 OVERPOPULATION    │  > 3 neighbors → cell dies         │
│  🎯 REPRODUCTION      │  = 3 neighbors → cell born         │
└─────────────────────────────────────────────────────────────┘
```

The simulation follows Conway's original rules:

1. **Underpopulation**: Any live cell with fewer than 2 live neighbors dies
2. **Survival**: Any live cell with 2 or 3 live neighbors survives
3. **Overpopulation**: Any live cell with more than 3 live neighbors dies
4. **Reproduction**: Any dead cell with exactly 3 live neighbors becomes alive

## 🎮 Controls

```
┌─────────────────────────────────────────────┐
│               🎹 CONTROLS 🎹                │
├─────────────────────────────────────────────┤
│  Enter board size → Set grid dimensions     │
│  Choose pattern → Select starting pattern   │
│  Override option → Enable/disable game over │
│  Ctrl+C → Exit Game                         │
└─────────────────────────────────────────────┘
```

## ⚙️ Technical Details

- **Language**: Python 3
- **Dependencies**: Built-in modules only (`time`, `os`, `random`, `copy`)
- **Display**: Terminal-based with ANSI color codes
- **Update Rate**: 0.1 seconds between generations
- **Grid Type**: Toroidal (wrapping boundaries)

## 📁 File Structure

```
📦 game_of_life/
├── 🐍 script.py          # Main Game of Life implementation
├── 📜 rules.txt          # Game rules reference
└── 📖 README.md          # This file
```

## ⚠️ Known Limitations

- Performance may degrade with very large board sizes
- Terminal display requires ANSI color support
- No save/load functionality for custom patterns

## 🔮 Future Improvements

```
┌─────────────────────────────────────────────┐
│             🚀 COMING SOON 🚀               │
├─────────────────────────────────────────────┤
│ ☑ Game over detection for static patterns  │
│ ☑ Pattern loading with preset patterns     │
│ ☑ Wrapping boundaries (toroidal grid)      │
│ ☐ Pattern loading from custom files        │
│ ☐ Pause/resume functionality               │
│ ☐ Save/export functionality for patterns   │
│ ☐ Color customization options              │
│ ☐ Speed control during simulation          │
└─────────────────────────────────────────────┘
```

## 🔬 About Conway's Game of Life

Conway's Game of Life is a famous example of a cellular automaton and has been studied extensively for its complex emergent behaviors arising from simple rules. Despite being a "zero-player game," it can produce fascinating patterns including gliders, oscillators, and even more complex structures.

```
┌──────────────────────────────────────────────────────────────┐
│                   🌟 FAMOUS PATTERNS 🌟                      │
├──────────────────────────────────────────────────────────────┤
│  🔄 Oscillators  │  Patterns that repeat periodically       │
│  🚁 Gliders      │  Patterns that move across the grid      │
│  🏭 Factories    │  Patterns that create other patterns     │
│  🌌 Gardens      │  Complex evolving ecosystems             │
└──────────────────────────────────────────────────────────────┘
```

---

<div align="center">

```
✨ Created with ❤️ as part of a Python programming project ✨

🎮 Happy Gaming! 🎮
```

</div>
