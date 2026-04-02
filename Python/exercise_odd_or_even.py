#!/bin/python3
x=int(input("Skriv ett hel tal "))

if 0 <= x <= 10:
   print("Vardet ar mellan 0 och 10!")
else:
   print("Vardet ar inte mellan 0 och 10!")

if x%2 == 1:
   print("Vardet ar udda")
else:
   print("Vardet ar jamt")

