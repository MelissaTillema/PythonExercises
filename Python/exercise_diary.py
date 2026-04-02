#!/bin/python3
# Author: Melissa

import sys
from datetime import datetime

diary_file = "dagbok.txt"

# If no arguments are given → print help
if len(sys.argv) < 2:
    print("Instruktioner:")
    print("dagbok.py titta")
    print("dagbok.py skriv <din dagbok text>")
    sys.exit()

command = sys.argv[1]

# View command
if command == "titta":
    try:
        with open(diary_file, "r") as file:
            content=file.read()
        if content.strip() == "":
            print("Dagbok ar tomt")
        else:
            print(content)
    except FileNotFoundError:
        print("dagbok.txt finns inte")

# Write command
elif command == "skriv":
        if len(sys.argv) < 3:
            print("Felaktig inmatning: ingen text")
            sys.exit()
        
        text = " ".join(sys.argv[2:])
        timestamp = datetime.now().strftime("%Y-%m-%d kl %H:%M")
        entry = f"{timestamp} {text}\n"

        with open(diary_file, "a") as file:
            file.write(entry)
else:
    print("Felaktig inmatning: Skriv 'titta' eller 'skriv'")