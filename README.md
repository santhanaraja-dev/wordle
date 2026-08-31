# Wordle CLI Game

A command-line Wordle game built with Python.

The player has **6 attempts** to guess a randomly selected **5-letter word**. Each guess is evaluated and displayed using:

* `✓` — Correct letter in the correct position
* `~` — Correct letter in the wrong position
* `✗` — Letter is not present in the secret word

The project also maintains game history and provides statistics such as total games, wins, win percentage, current streak, and best streak.

## Project Structure

wordle/
├── pyproject.toml
├── README.md
├── .gitignore
├── src/
│   └── wordle/
│       ├── game.py
│       ├── history.py
│       ├── wordle.py
│       └── words.txt
└── tests/
    └── test_game.py

## Requirements

* Python 3.10+
* pytest
* ruff

## Setup

Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\Activate.ps1

Install the development dependencies:

python -m pip install pytest ruff

## Run the Game

From the project root:

python src/wordle/wordle.py

The game will randomly select a word from `words.txt` and prompt you for guesses.

## Run Tests

Run all tests with:

python -m pytest

The test suite covers:

* Fully correct guesses
* Mixed correct, present, and absent letters
* Duplicate-letter handling
* Invalid words
* Winning condition
* Game-over condition after 6 failed guesses

## Code Quality

Run Ruff to check the project:

python -m ruff check .

## Game History

Completed games are stored locally in:

history.json

The history file is generated automatically when the game is run and is excluded from Git using `.gitignore`.

## Features

* Random secret word selection
* Six attempts per game
* Word-list validation
* Duplicate-letter handling
* Game board display
* Persistent local game history
* Win percentage
* Current winning streak
* Best winning streak
* Automated tests with pytest
* Code quality checks with Ruff
