#!/bin/python3
# Author: Melissa

while True:
    number=input("Skriv ett heltal: ")
    try:
        doublenumber=int(number)**2
        print("Talet i kvadrat är", doublenumber)
        break
    except ValueError:
        print("Tyvärr, det är inget heltal")