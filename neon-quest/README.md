# NEON QUEST – The Ultimate Treasure Hunt

A colorful, beginner-friendly terminal adventure built with Python. Explore a mysterious 5×5 map, gather coins, dodge traps, and find the hidden treasure before your lives or moves run out.

## Features

- Colorful terminal interface and ASCII-art title screen
- A freshly randomized treasure, five coins, and four traps for every game
- Hidden map tiles revealed as you explore
- Simple W, A, S, D movement with boundary and input validation
- Three lives and a 20-move limit
- Coin scoring, a treasure-finding bonus, and four explorer ranks
- Victory and game-over screens, plus an option to play again
- No third-party packages required

## Technologies

- Python 3.8+
- Python standard library: `random`, `os`, `sys`, and `dataclasses`
- ANSI escape sequences for terminal color (automatically disabled when output is not interactive)

## Installation

1. Install Python 3.8 or newer from [python.org](https://www.python.org/downloads/).
2. Download or clone this repository.
3. Open a terminal in the `neon-quest` project folder.

There are no dependencies to install.

## How to run

From the project folder, run:

```bash
python game.py
```

On systems where Python 3 is invoked with a separate command, use:

```bash
python3 game.py
```

In VS Code, open the `neon-quest` folder, open `game.py`, then select **Run Python File in Terminal**.

## Game controls

| Key | Action |
| --- | --- |
| `W` | Move up |
| `A` | Move left |
| `S` | Move down |
| `D` | Move right |

Movement keys are case-insensitive. Invalid keys and moves beyond the map do not use a turn. After a round, enter `Y` to start another expedition or `N` to exit.

## Scoring and ranks

- Collect a coin: **+10 points**
- Find the hidden treasure: **+100 bonus points**

Your rank is based on your final score:

| Score | Rank |
| ---: | --- |
| 150 or more | NEON LEGEND |
| 100–149 | TREASURE MASTER |
| 50–99 | GOLDEN EXPLORER |
| 0–49 | BRAVE ROOKIE |

## Example output

```text
       YOUR EXPEDITION MAP
     1   2   3   4   5
   +---+---+---+---+---+
 1 | ? | ? | ? | ? | ? |
   +---+---+---+---+---+
 2 | ? | ? | ? | ? | ? |
   +---+---+---+---+---+
 3 | ? | ? | @ | ? | ? |
   +---+---+---+---+---+
 4 | ? | ? | ? | ? | ? |
   +---+---+---+---+---+
 5 | ? | ? | ? | ? | ? |
   +---+---+---+---+---+
   @ You   ? Unexplored   . Explored
   $ Coins: 0   ^ Traps: beware   * Treasure: hidden

   Score:   0   Lives: ♥♥♥   Moves left: 20
```

The map layout changes with every expedition. In an interactive terminal, the interface uses color and refreshes as you explore.
