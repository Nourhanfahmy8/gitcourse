# Number Scrabble Game

## Description
Number Scrabble is a two-player game where participants take turns selecting numbers from a predefined list. The objective of the game is to be the first player to collect a set of three numbers that add up to 15. Each number can only be chosen once by either player.

## How to Play
1. **Setup**: 
   - The game begins with a list of numbers from 1 to 9.
   - Players take turns selecting numbers from the list.

2. **Game Rules**:
   - Players alternate turns, with each player selecting one number per turn.
   - Once a number is chosen, it cannot be selected again.
   - The game ends when:
     - A player accumulates three numbers whose sum equals 15.
     - All numbers have been chosen from the list without any player achieving a sum of 15 with their selections.

3. **Winning**:
   - The player who first collects a set of three numbers with a sum of 15 wins the game.
   - If no player achieves this goal and all numbers are selected, the game ends in a draw.

## Game Controls
- Players input their chosen numbers when prompted during their turn.
- Input validation ensures that only valid numbers are accepted, and players cannot select a number that has already been chosen or is outside the range of 1 to 9.

## Running the Game
- Execute the Python script `number_scrabble.py` to start the game.
- Follow the on-screen prompts to play the game.
- After the game ends, players have the option to start a new game or exit.

## Game Mechanics
- The game utilizes a combination of input validation, player checks, and list manipulations to facilitate gameplay.
- Players are informed of their current selections and the remaining numbers in the list after each turn.
- Clear messages announce the winner or declare a draw at the end of the game.

## Enjoy playing Number Scrabble!
