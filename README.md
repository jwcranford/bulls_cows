# Bulls and Cows Assistant

Assistant for a bulls and cows game (aka Mastermind aka Guess).
This program generates all possible solutions, then revises the
list after each guess.

## Usage

```
usage: bulls_cows.py [-h] [-t TOP] alphabet squares

Assistant for bulls and cows game. Prompts for guesses and results during the
game and restricts the solution space accordingly, printing out the top-
scoring remaining solutions. Solutions with the least number of unique
characters / colors score the highest.

positional arguments:
  alphabet           characters to use to fill in the squares
  squares            number of squares in each guess

options:
  -h, --help         show this help message and exit
  -t TOP, --top TOP  number of top scoring candidates to print
```

## See Also

* [Wikipedia - Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows)
* [Guess, from Simon Tatham's Portable Puzzle Collection](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/guess.html)
