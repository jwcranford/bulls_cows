#!/usr/bin/env python3
#
# bulls_cows.py - assistant for bulls and cows game
#
# Usage: Run with -h to see built-in help
# bulls_cows.py -h
#
# Prompts for deductions during the game and restricts the solution space 
# accordingly, printing out the number of remaining possible solutions.

# Forms of deductions:
# - Solution has exactly X reds - 2r
# - Solution has red in position Y - .r...

import argparse

# cross() generates a list cross-product of the given alphabet
def cross(alphabet, words):
    return [a + w for a in alphabet for w in words]

def crossn(alphabet, words, cell_count):
    if cell_count == 0:
        return words
    else:
        return crossn(alphabet, cross(alphabet, words), cell_count - 1)
        
# candidates() is a generator that yields all possible solutions for
# the given alphabet and the number of cells
# 
# alphabet is a set that contains all the possible values for a single cell
# cell_count is the number of cells in the problem
def candidates(alphabet, cell_count):
    if cell_count == 0:
        return []
    else:
        return crossn(alphabet, alphabet, cell_count - 1)

# reduce() takes the current list of candidates and a deduction, 
# then returns the revised candidates excluded by the deduction
def reduce(candidates, deduction, cell_count):
    if len(deduction) == 2:
        count = int(deduction[0])
        label = deduction[1]
        return [w for w in candidates if w.count(label) == count]
    elif len(deduction) == cell_count:
        for i in range(0,cell_count):
            if deduction[i] != '.':
                candidates = [w for w in candidates if w[i] == deduction[i]]
    return candidates

def next_deduction():
    print('Enter a deduction. Forms:')
    print('  2r     - means that the solution must have exactly 2 "r" squares')
    print('  ..r..  - means that the solution must have r in the 3rd spot, for a 5-square game')
    return input('Deduction: ')

def print_top(candidates, top):
    print(f"{len(candidates)} candidates left")
    if len(candidates) <= top:
        for c in candidates:
            print(c)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''Assistant for bulls and cows game. 
Prompts for deductions during the game, reduces the solution space, and
prints out the number of remaining possible solutions''')
    parser.add_argument("alphabet", 
        help="characters to use to fill in the squares")
    parser.add_argument('squares', 
        help='number of squares in each guess', default=3, type=int)
    parser.add_argument('-t', '--top', 
        help="when only this many solutions remain, print them all",
        default=10, type=int)

    args = parser.parse_args()

    candidates = candidates(args.alphabet, args.squares)
    # for c in candidates:
    #     print(c)

    while True:
        print_top(candidates, args.top)
        deduction = next_deduction()
        candidates = reduce(candidates, deduction, args.squares)
