#bin/python3
import random
x=random.randint(2,10000)

def isprime(number):
    for x in range(2, number):
        if number%x == 0:
            return(False)
    return(True)

for x in range(5):
    x=random.randint(2,10000)
    print(x, end=" ")
    if isprime(x):
        print("is a prime number")
    else:
        print("is not a prime number")
