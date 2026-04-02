#!/bin/python3
# Author: Melissa

import sys

# Check if exactly 3 arguments are given (not counting script name)
if len(sys.argv) != 4:
    print("Invalid input. Must be: <number> <plus|minus|ganger|delamed> <number>")
    sys.exit(1)

# Get arguments
num1 = sys.argv[1]
operator = sys.argv[2]
num2 = sys.argv[3]

# Try converting numbers
try:
    if "." in num1:
        num1 = float(num1)
    else:
        num1 = int(num1)

    if "." in num2:
        num2 = float(num2)
    else:
        num2 = int(num2)
except ValueError:
    print("Invalid input: First and third arguments must be numbers.")
    sys.exit(1)

# Perform calculation
if operator == "plus":
    result = num1 + num2
elif operator == "minus":
    result = num1 - num2
elif operator == "ganger":
    result = num1 * num2
elif operator == "delamed":
    if num2 == 0:
        print("Invalid input: Cannot divide by zero.")
        sys.exit(1)
    result = num1 / num2
else:
    print("Invalid input: Operator must be plus, minus, ganger, or delamed.")
    sys.exit(1)

# Define operator symbols
operator_symbols = {
    "plus": "+",
    "minus": "-",
    "ganger": "*",
    "delamed": "/"
}

# Print result
if isinstance(result, float) and result.is_integer():
    print(num1, operator_symbols[operator], num2, "=", int(result))
else:
    print(num1, operator_symbols[operator], num2, "=", result)