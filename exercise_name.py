#!/bin/python3
name=input("Vad heter du? ")

if len(name) <= 8:
    print(name.capitalize(), "ar ett kort och bra namn")
else:
    print("Oj, det var ett laaaaangt namn!")
