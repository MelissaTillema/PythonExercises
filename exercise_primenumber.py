#!/bin/python3

import random
x=random.randint(2,10000)

def isprime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

for b in range(5):
    x=random.randint(2,10000)
    if isprime(x):
        print(x, "is a prime number")
    else:
        print(x, "is not a prime number")