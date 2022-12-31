#!/usr/bin/env python3
#
# bulls_cows.py - assistant for bulls and cows game
#
# Usage: Run with -h to see built-in help
# bulls_cows.py -h
#
# Prompts for guesses and results during the game and restricts the solution space 
# accordingly, printing out the top-scoring remaining solutions. Solutions
# with the least number of unique characters / colors score the highest.


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

# def print_top(candidates, top):
#     print(f"{len(candidates)} candidates left")
#     if len(candidates) <= top:
#         for c in candidates:
#             print(c)

def print_top(scores, top):
    print(f"{len(scores)} candidates left")
    for (w,s) in scores[0:top]:
        print(f"{w}: {s}")

def next_guess(len):
    while True:
        print(f'Enter next guess and results. Guess must {len} characters long.')
        g = input('Guess: ')
        if len == len(g):
            break
    b = input('Bulls: ')
    c = input('Cows: ')
    return (g, b, c)

# def process_guess(scores, guess, bulls, cows):
#     match bulls:
#         match r:
#             # If black, Remove all words containing g
#             case '.':
#                 words = [w for w in words if not g in w]
#             # If yellow
#             #    * Remove all words without g
#             #    * Remove all words with g in current position
#             case 'y':
#                 words = [w for w in words if g in w and w[i] != g]
#             # If green, Remove all words without g in current position
#             case 'G':
#                 words = [w for w in words if w[i] == g]
#     return words

# returns the number of bulls and cows for the given guess, compared to the answer
def bulls_cows(answer, guess):
    bulls = [g for (a,g) in zip(answer, guess) if a == g]
    nonbull_guesses = [g for (a,g) in zip(answer, guess) if a != g]
    nonbull_answers = [a for (a,g) in zip(answer, guess) if a != g]

    cows = 0
    for g in nonbull_guesses:
        if g in nonbull_answers:
            cows += 1
            nonbull_answers.remove(g)

    return (len(bulls), cows)
        

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
        help='number of top scoring candidates to print',
        default=10, type=int)

    args = parser.parse_args()

    candidates = candidates(args.alphabet, args.squares)
    # for c in candidates:
    #     print(c)
    scores = [(c, len(set(c))) for c in candidates]
    scores.sort(key=lambda s: s[1])

    while True:
        print_top(scores, args.top)
        # deduction = next_deduction()
        # candidates = reduce(candidates, deduction, args.squares)
        (guess, bulls, cows)= next_guess()