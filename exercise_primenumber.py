#!/bin/python3

import random

def isprime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for _ in range(5):
    x=random.randint(2,10000)
    if isprime(x):
        print(x, "is a prime number")
    else:
        print(x, "is not a prime number")