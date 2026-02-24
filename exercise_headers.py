#!/bin/python3
# Author: Melissa

# Part 1
'''
import requests
import sys
 
domain = sys.argv[1]
response = requests.get(f"https://{domain}")

print(response.headers.get('Server'))
''' 
# Part 2
import requests

# Open domains.txt to read the domain names
with open("domains.txt", "r") as file:
    for line in file:
        domain = line.strip() #.strip makes it so that the strings are not called upon as a function

        # Collect the server software
        response = requests.get(f"https://{domain}") 
        server = response.headers.get("Server")
        print(domain, "=", server)