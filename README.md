# guess-a-number-game-
the guess a number which includes the player to guess a number and also the machine to guess a number.





---

## Guess the Number – Python Project

###  Overview
This project is a basic Python-based "Guess the Number" game.  
It contains **two interactive modes**:

1. **Player Guess Mode** – The computer picks a random number and the player tries to guess it.
2. **Computer Guess Mode** – The player thinks of a number and the computer tries to guess it using hints.

Both versions run in a terminal and use loops, conditionals, user input, and the `random` module.

---

##  Game Modes

### 1️ Player Guesses the Number
**Function:** `guess(x)`

- The computer selects a random number between **1 and x**.
- The player keeps guessing until the correct number is found.
- Hints provided:
  - “Too high”
  - “Too low”

---

### 2️.Computer Guesses the Number
**Function:** `computer_guess(x)`

- The player thinks of a number between **1 and x**.
- The computer keeps guessing.
- The player responds using:
  - `h` → too high  
  - `l` → too low  
  - `c` → correct  

The computer adjusts its range based on the hints and eventually reaches the right number.

---

##  Technologies Used
- **Python 3**
- **PyCharm** (for running and editing the code)
- Built-in Python modules (especially `random`)

---

