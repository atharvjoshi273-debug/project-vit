# Blackjack Game

A simple command-line Blackjack game written in Python.

## Description

This project lets you play Blackjack against a computer-controlled dealer. You start with **500 chips**, place bets, and choose whether to hit or stand.

The game uses randomly generated cards and implements basic Blackjack scoring, including Ace handling.

## Features

- Starts the player with 500 chips
- Allows the player to place bets each round
- Randomly generates cards
- Supports **Hit** and **Stand**
- Handles Aces as either 11 or 1 when necessary
- Automatically plays the dealer's hand until the dealer reaches 17
- Tracks wins, losses, and remaining chips
- Allows the player to quit at any time

## Card Values

| Card | Value |
|---|---:|
| Ace | 11, or 1 when needed |
| 2–10 | Face value |
| Jack | 10 |
| Queen | 10 |
| King | 10 |

Internally, cards are represented by numbers from 1 to 13.

## How to Play

1. Run the program.
2. Enter a bet when prompted.
3. Choose:
   - `h` — Hit and draw another card
   - `s` — Stand and end your turn
4. The dealer then plays their hand.
5. The final hand totals are compared.
6. Your chips are updated based on the result.
7. Continue playing until you run out of chips or enter `q` to quit.

## Rules

- A hand over 21 is a **bust** and loses the bet.
- The dealer draws while their total is below 17.
- You win if:
  - Your total is higher than the dealer's, or
  - The dealer busts.
- You lose if the dealer's total is higher.
- Equal totals result in a **push** (tie).
- A winning bet is added to your chips.
- A losing bet is subtracted from your chips.

## Project Structure

```text
.
├── main.py
├── statement.md
└── README.md
```

### `main.py`

Contains the complete Blackjack game, including card generation, hand scoring, player input, dealer behavior, and chip management.

### `statement.md`

Contains a more detailed project statement describing the game's purpose, rules, functions, requirements, and usage.

## Requirements

- Python 3
- No external packages are required.

The program uses Python's built-in `random` module.

## Installation

Clone or download the project, then open a terminal in the project directory.

No additional dependencies need to be installed.

## Running the Game

Run:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

## Example

```text
Chips: 500. Bet (or q to quit): 50
Your hand: 10 A = 21 | Dealer shows: 7
...
You win 50!
```

The exact cards and results will vary because cards are randomly generated.

## Limitations

This is a simplified command-line Blackjack game. It does not implement every rule used in casino Blackjack, and it does not model a physical deck with card removal.

## License

This project does not specify a license.
