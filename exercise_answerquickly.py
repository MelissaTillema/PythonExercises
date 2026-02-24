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

            # Receive data from server
        data = data.strip().replace("?", " ").split()

    # Multiply index 2 and 4 (0-based indexing)
        num1 = int(data[2])
        num2 = int(data[4])
        result = num1 * num2
        
        # Send result back
        s.sendall((str(result) + "\n").encode())
        
        # Checks if there are two numbers and multiplies them
        print( result)