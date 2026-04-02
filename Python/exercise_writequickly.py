#!/bin/python3
# Author: Melissa

import readchar
import datetime

print("Write the alphabet (a-z) as fast as possible!")

alphabet = "abcdefghijklmnopqrstuvwxyz"
x = 0
y = 26

while True:
    key = readchar.readkey()
    if key == alphabet[x]:
        if key == "a":
            start=datetime.datetime.now()
        print(alphabet[x])
        x = x + 1
        if x == y:
            break  

end = datetime.datetime.now()
duration = (end - start).total_seconds()

print("You did it!")    
print("It took you", duration, "seconds")