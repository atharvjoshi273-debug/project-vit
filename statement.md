# Blackjack Game — Statement

## Overview

This project is a simple command-line Blackjack game written in Python. The player starts with **500 chips** and plays rounds against a dealer using randomly generated cards.

## How It Works

- The player begins with 500 chips.
- At the start of each round, the player enters a bet.
- The bet must be a valid number between 1 and the player's available chips.
- The player and dealer each receive two cards.
- The player can choose to **hit** or **stand**.
- The player loses the round immediately if their hand goes over 21.
- If the player stands, the dealer draws cards until the dealer's total reaches at least 17.
- The final hand totals are compared:
  - The player wins if the dealer busts or the player's total is higher.
  - The player loses if the player's total is lower.
  - Equal totals result in a push (tie).
- Winning adds the bet to the player's chips, while losing subtracts the bet.
- The game continues until the player runs out of chips or chooses `q` to quit.

## Card Values

The game represents cards using numbers from 1 to 13:

- `1` represents an Ace (`A`)
- `11` represents Jack (`J`)
- `12` represents Queen (`Q`)
- `13` represents King (`K`)
- Other numbers are displayed as their numeric value
- Face cards count as 10 when calculating the hand total.
- An Ace initially counts as 11 and is changed to 1 when necessary to prevent a bust.

## Main Functions

### `total(hand)`

Calculates the Blackjack value of a hand, including special handling for Aces.

### `show(hand)`

Converts numeric card values into display-friendly card names such as `A`, `J`, `Q`, and `K`.

### `draw()`

Generates a random card value between 1 and 13.

## Requirements

- Python 3
- Standard library only (`random`)

## Running the Game

Run the Python file from a terminal:

```bash
python main.py
```

Follow the prompts to place bets and choose whether to hit or stand.

## Notes

This is a simplified Blackjack implementation intended for command-line play. It does not model a full physical deck or all casino Blackjack rules.
