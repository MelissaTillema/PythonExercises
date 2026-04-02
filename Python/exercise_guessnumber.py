#!/bin/python
# Author: Melissa
import random
x=random.randint(0,100)

guesses = 0

while True:
    try:
        number=int(input("Enter a number between 1 - 100: "))
        guesses += 1
        if number==x:
            print("You nailed it, it took you", guesses, "guesses. Congratulations!")
            break
        elif number<x:
            print("Your guess was too low")
        else:
            print("Your guess was too high") 
    except ValueError:
        print("That’s not a valid number. Try again!")