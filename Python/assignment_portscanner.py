#!/bin/python3
# Author: Melissa

import socket
import sys
import ipaddress

# A function that returns a boolean to if it worked or not to connect to the socket
def ipconnect(ip: str, port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as x:
            x.settimeout(2)  
            x.connect((ip, port))
        return "Open"
    except (socket.timeout):
        return "No response"
    except (socket.error):
        return "Closed"

# Check command-line argument
if len(sys.argv) != 2:
    print("Error. Input: portscanner.py <IP-address>")
    sys.exit(1)

# IP to test
ip = sys.argv[1]

# Validate IP address
try:
    ipaddress.ip_address(ip)
except ValueError:
    print("Invalid IP address.")
    sys.exit(1)

# Read ports from file
ports = []
with open("connectscan_portar.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line.isdigit():
            ports.append(int(line))

# Testing the IP and ports
for port in ports:
    result = ipconnect(ip, port)
    print(f"Port {port}: {result}")