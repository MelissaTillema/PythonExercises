#!/bin/python3
# Author: Melissa

def pin(numbers):
    total = 0
    multiplier = 2
    for n in numbers:
        num = int(n) * multiplier
        if num > 9:
            num-=9
        
        total += num
        if multiplier == 1:
            multiplier = 2
        else:
            multiplier = 1

    final_num = 0
    while (total + final_num) % 10 != 0: #(total + final_num) divisible by 10
            final_num += 1 #It finds the smallest digit (0–9) that makes the total end in 0
    return final_num

if __name__ == "__main__":
    while True:
        user_input = (input('Input the first 9 numbers of a 10 number swedish pin: '))
        if not user_input.isdigit():
            print("Error: Only numbers are allowed.")
            continue
            
        if len(user_input) != 9:
            print("Error: You must enter exactly 9 numbers.")
            continue
        break

    last_number = pin(user_input)
    print("The last number is:", last_number)
