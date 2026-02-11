#!/bin/python3

import random
max = 100000
totalguess = 0
amountsecretnumber = 10000

for x in range(amountsecretnumber):
    secretnumber = random.randint(0, max)

    mymin = 0
    mymax = max 
    guess = -1
    guessamount = 0

    while guess != secretnumber:
        totalguess += 1
        guessamount += 1
        guess = round((mymax + mymin) / 2)
        print(f"My guess: {guess}")
        if guess > secretnumber:
            mymax = guess
            print("Too high! Try again")
        if guess < secretnumber:
            mymin = guess
            print("Too low! Try again")
        if guess == secretnumber:
            print(f"Congratulations! It took {guessamount} tries. Good job!")
print(f"It took {totalguess} tries to guess 1000 secret number between 0 and {max}") 
print(f"Which means it took {totalguess/amountsecretnumber} on average")
