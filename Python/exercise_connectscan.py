#!/bin/python3
# Author: Melissa

import socket

# A function that returns a boolean to if it worked or not to connect to the socket
def ipconnect(ip: str, port: int):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as x:
            x.settimeout(5)  
            x.connect((ip, port))
        return True
    except (socket.timeout, socket.error):
        return False
    
# IP and ports to test
ip = "10.0.0.197"
ports = [21, 22, 23, 24, 25, 80]

# Testing the IP and ports
for port in ports:
    if ipconnect(ip, port):
        print("Det gick bra att ansluta till", ip, "på port", port)
    else:
        print("Anslutningen till", ip, "på port", port, "misslyckades.")
