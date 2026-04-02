#!/bin/python3
x= " "
while x.lower()!="quit":
    x=input("Skriv något, avsluta med 'quit': ")
    if x.lower()!= "quit":
        print(x, "konverterat till stora bokstaver blir", x.upper())
print("Tack och hej")