#!/bin/python3
# Author: Melissa

def collatz(number):
    # Make a list
    numbers = list()

    # Make a iseven function to detect even or odd
    def iseven(number):
        if number%2 == 1: #odd
            return False  
        else:
            return True
    
    # Put number in the list
    numbers.append(number)

    # Collatz sequence
    while True: 
        if iseven(number) == False:
            number = number * 3 + 1
            numbers.append(number)
        else:
            number = int(number / 2)
            numbers.append(number)
        if number == 1:
            return numbers

#print the list without brackets and with comma
def printalista(numbers):
    print(f"n:{numbers[0]} -> ", end="" )
    print(*numbers, sep=", ")

x=int(input("Skriv ett tal: "))
listvariabel=collatz(x)
printalista (listvariabel)