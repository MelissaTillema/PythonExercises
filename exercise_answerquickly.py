#!/bin/python3
# Author: Melissa

import socket

HOST = "10.0.0.3"
PORT = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Loop through
    while True:
        data = s.recv(1024).decode() # decode() converts bytes to string
        if not data:
            break

        # Print the questions
        print(data.strip())

        # If answer is correct, end the script
        if "Bra jobbat" in data:
            break

        # Extract full numbers
        numbers = []
        current = ""

        # Loop over each character in the string
        for char in data:
            if char.isdigit(): # if it is a digit is gets added to current
                current += char
            else:
                if current != "":
                    numbers.append(int(current))
                    current = ""

        # Checks if there are two numbers and multiplies them
        if len(numbers) >= 2:
            result = numbers[0] * numbers[1]
            s.sendall((str(result) + "\n").encode())
            print( result)