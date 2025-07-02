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
- **Multiple starting options**: Random patterns or preset interesting patterns
- **Real-time visualization**: Watch the patterns evolve with colorful terminal output
- **Game over detection**: Automatically detects static patterns, oscillators, and empty boards
- **Wrapping boundaries**: Toroidal grid where patterns can move across edges
- **Save/Load functionality**: Save interesting patterns and load them later
- **Pattern library**: Includes classic patterns like gliders, oscillators, and static formations

## 🚀 How to Run

```
┌──────────────────────────────────────┐
│           🎮 LAUNCH GAME 🎮          │
│                                      │
│  python script.py                   │
│                                      │
│  ✨ Enter board size when prompted   │
│  🎯 Choose starting pattern          │
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
5. Choose from these starting options:
   - **Random**: Randomly generated pattern
   - **Glider**: Classic moving pattern
   - **Blinker**: Simple oscillator
   - **Block**: Static pattern
   - **Toad**: Period-2 oscillator
   - **Beacon**: Period-2 oscillator
   - **Load from file**: Load a previously saved pattern
6. Watch the Game of Life unfold!
7. Press Ctrl+C to exit (you'll be prompted to save your pattern)

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
┌─────────────────────────┐
│   🎹 CONTROLS 🎹        │
├─────────────────────────┤
│  Ctrl+C → Exit Game     │
│  (auto-save prompt)     │
└─────────────────────────┘
```

## 🌟 New Features

### 🎯 Game Over Detection
- **Static patterns**: Detects when the board reaches a stable state
- **Oscillating patterns**: Identifies repeating cycles (up to period 10)
- **Empty boards**: Recognizes when all cells have died

### 📁 Pattern Management
- **Save patterns**: Automatically prompted when game ends or exits
- **Load patterns**: Choose from saved files or preset patterns
- **Pattern library**: Includes famous Conway's Game of Life patterns
- **JSON format**: Easy to edit and share patterns

### 🌐 Toroidal Grid
- **Wrapping boundaries**: Patterns can move across edges
- **Infinite feel**: No more dead border zones
- **Glider journeys**: Watch gliders travel across the wrapped world

## ⚙️ Technical Details

- **Language**: Python 3
- **Dependencies**: Built-in modules only (`time`, `os`, `random`, `copy`, `json`)
- **Display**: Terminal-based with ANSI color codes
- **Update Rate**: 0.1 seconds between generations
- **Grid Type**: Toroidal (wrapping boundaries)
- **Pattern Storage**: JSON format for easy editing and sharing

## 📁 File Structure

```
📦 game_of_life/
├── 🐍 script.py          # Main Game of Life implementation
├── 🚀 main.py            # Launcher script to open game in new terminal
├── 👋 hello_world.py     # Additional Python script
├── 📜 rules.txt          # Game rules reference
├── 📖 README.md          # This file
└── 📂 patterns/          # Pattern library
    ├── glider.json       # Classic glider pattern
    └── toad.json         # Toad oscillator pattern
```

## ⚠️ Known Limitations

- None! All major features have been implemented ✅

## 🎯 Completed Features

All the features from the original wishlist have been implemented:

```
┌─────────────────────────────────────────────┐
│             ✅ COMPLETED ✅                 │
├─────────────────────────────────────────────┤
│ ✅ Game over detection for static patterns  │
│ ✅ Pattern loading from files               │
│ ✅ Preset interesting starting patterns     │
│ ✅ Save/load functionality                  │
│ ✅ Wrapping boundaries (toroidal grid)      │
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
