# Blokus Bot Battleground

Owner: Gabe Stanton

## Requirements

- python 3.\*.\*

## Install Dependencies

`python setup.py install`

## Usage

- `python core.py`
- `python core.py <player 1 name> <player 1 file name> ...`
  - e.g: `python3 core.py kevin randomPlayer gabe randomPlayer alissa randomPlayer john bigPiecePlayer`

## Creating a Player

Add a file to `players/` containing a class called `Player` that subclasses `BasePlayer`
