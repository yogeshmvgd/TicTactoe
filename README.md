Overview
This is a Python implementation of the classic Tic Tac Toe game that runs in the console. Two players take turns marking spaces in a 3×3 grid, with one player using 'X' and the other using 'Y'. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

Features
Console-based interface: Simple text-based gameplay

Position numbering system: Uses a two-digit coordinate system (11-33) where:

First digit represents the row (1-3)

Second digit represents the column (1-3)

Input validation:

Checks for valid position numbers

Prevents overwriting occupied spaces

Handles non-numeric inputs

Win detection: Automatically checks for winning combinations after each move

Draw detection: Recognizes when the board is full with no winner

Replay option: Allows players to start a new game after completion

How to Play
Run the Python script in any Python environment

Players take turns entering position numbers when prompted:

Player 1 is 'X'

Player 2 is 'Y'

The game continues until:

A player gets three in a row (win)

All spaces are filled (draw)

After each game, you can choose to play again or exit

Technical Details
Game board representation: Uses a dictionary with keys 11-33 representing positions

Win conditions: Checks against 8 possible winning combinations (3 rows, 3 columns, 2 diagonals)

Game flow control:

Uses a while loop for the main game sequence

Tracks moves with count variable

Uses flags to determine game state

Requirements
Python 3.x

