#!/bin/python3
# Author: Melissa

try:
    f=open("/home/irc24/lista.txt", "r") #open file and read
    list=open("lista.txt", "w",) #open file and write
    for x in f:
        list.write(x.upper()) #copy first file and write it in the second file with uppercase letter
    f.close()
    list.close()

except FileNotFoundError:
    print("Insufficent permissions or file not found")
except PermissionError:
    print("Permission denied")