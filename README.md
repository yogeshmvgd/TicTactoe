# Tic Tac Toe Game - README

## Overview
This is a Python implementation of the classic Tic Tac Toe game that runs in the console. Two players take turns marking spaces in a 3×3 grid, with one player using 'X' and the other using 'Y'. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Features
- **Console-based interface**: Simple text-based gameplay
- **Position numbering system**: Uses a two-digit coordinate system (11-33) where:
  - First digit represents the row (1-3)
  - Second digit represents the column (1-3)
- **Input validation**: 
  - Checks for valid position numbers
  - Prevents overwriting occupied spaces
  - Handles non-numeric inputs
- **Win detection**: Automatically checks for winning combinations after each move
- **Draw detection**: Recognizes when the board is full with no winner
- **Replay option**: Allows players to start a new game after completion

## How to Play
1. Run the Python script in any Python environment
2. Players take turns entering position numbers when prompted:
   - Player 1 is 'X'
   - Player 2 is 'Y'
3. The game continues until:
   - A player gets three in a row (win)
   - All spaces are filled (draw)
4. After each game, you can choose to play again or exit

## Technical Details
- **Game board representation**: Uses a dictionary with keys 11-33 representing positions
- **Win conditions**: Checks against 8 possible winning combinations (3 rows, 3 columns, 2 diagonals)
- **Game flow control**: 
  - Uses a while loop for the main game sequence
  - Tracks moves with count variable
  - Uses flags to determine game state

## Requirements
- Python 3.x

## How to Run
Simply execute the script in a Python environment:
```bash
python tic_tac_toe.py
```

## Example Gameplay
```
Welcome to the Game Tic Tac Toe
Full Game in Console Command

New game started!
Positions are numbered as:
 11 | 12 | 13 
-----------
 21 | 22 | 23 
-----------
 31 | 32 | 33 

Player 1 enter the value: 11
 X |   |  
-----------
   |   |  
-----------
   |   |  
Player 2 enter the value: 22
 X |   |  
-----------
   | Y |  
-----------
   |   |  
...
```

## Potential Improvements
1. Add single-player mode against computer AI
2. Implement score tracking across multiple games
3. Add color to the console output
4. Create a GUI version
5. Add input timeout for turns

This project is a great example of a simple but complete game implementation in Python, demonstrating fundamental programming concepts like loops, conditionals, data structures, and user input handling.
