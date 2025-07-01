# Conway's Game of Life

A Python implementation of Conway's Game of Life - a cellular automaton devised by mathematician John Conway. This zero-player game evolves based on its initial state, requiring no further input from players.

## Overview

This implementation creates a grid of cells that can be either alive (represented by colored blocks) or dead (empty spaces). The simulation follows the classic rules of Conway's Game of Life and displays the evolution in real-time in your terminal.

## Features

- **Customizable board size**: Choose your preferred grid dimensions
- **Random initial state**: Each run starts with a randomly generated pattern
- **Real-time visualization**: Watch the patterns evolve with colorful terminal output
- **Continuous simulation**: The game runs indefinitely until manually stopped

## How to Run

1. Make sure you have Python installed on your system
2. Navigate to the project directory
3. Run the script:
   ```bash
   python script.py
   ```
4. Enter your desired board size when prompted
5. Watch the Game of Life unfold!

## Game Rules

The simulation follows Conway's original rules:

1. **Underpopulation**: Any live cell with fewer than 2 live neighbors dies
2. **Survival**: Any live cell with 2 or 3 live neighbors survives
3. **Overpopulation**: Any live cell with more than 3 live neighbors dies
4. **Reproduction**: Any dead cell with exactly 3 live neighbors becomes alive

## Controls

- **Ctrl+C**: Stop the simulation and exit

## Technical Details

- **Language**: Python 3
- **Dependencies**: Built-in modules only (`time`, `os`, `random`)
- **Display**: Terminal-based with ANSI color codes
- **Update Rate**: 0.1 seconds between generations

## File Structure

- `script.py` - Main Game of Life implementation
- `main.py` - Launcher script to open the game in a new terminal window
- `hello_world.py` - Additional Python script
- `rules.txt` - Game rules reference

## Known Limitations

- The game currently runs indefinitely (TODO: implement game over detection)
- Border cells are treated as permanently dead
- No save/load functionality for interesting patterns

## Future Improvements

- [ ] Implement game over detection for static or oscillating patterns
- [ ] Add pattern loading from files
- [ ] Include preset interesting starting patterns
- [ ] Add pause/resume functionality
- [ ] Implement wrapping boundaries (toroidal grid)

## About Conway's Game of Life

Conway's Game of Life is a famous example of a cellular automaton and has been studied extensively for its complex emergent behaviors arising from simple rules. Despite being a "zero-player game," it can produce fascinating patterns including gliders, oscillators, and even more complex structures.

---

*Created as part of a Python programming project*
