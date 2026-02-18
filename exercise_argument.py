#!/bin/python3
# Author: Melissa

import sys

argumentlist = sys.argv
print("Total arguments:", len(argumentlist)-1)

for arg in argumentlist:
    print("Argument: ", arg)