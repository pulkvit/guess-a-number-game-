# guess-a-number-game-
the guess a number which includes the player to guess a number and also the machine to guess a number.
# Guess the Number – Python Project

##  Overview
This is a simple Python-based "Guess the Number" game.  
The project contains *two modes*:
1. *Player Guess Mode* – The computer picks a random number and the player tries to guess it.
2. *Computer Guess Mode* – The player thinks of a number and the computer tries to guess it based on the player's hints.
Both modes run in the terminal and use basic Python logic such as loops, conditionals, and the random module.
# Game Modes

# 1. Player Guesses the Number
Function: guess(x)
The computer selects a random number between 1 and x.
The player inputs guesses until they find the correct number.
Hints are provided:  
  a. “Too high”  
  b. “Too low”

#2. Computer Guesses the Number
Function: computer_guess(x)
 The player thinks of a number between **1 and x**.
 The computer tries to guess it.
 The player responds using:
    `h` → too high  
    `l` → too low  
    `c` → correct  

The computer uses a shrinking range to reach the correct number.
#3. Technologies used
pycharm




