#!/bin/python3
# Author: Melissa

import requests

TARGET = "http://10.0.0.197"
LIST = "https://raw.githubusercontent.com/daviddias/node-dirbuster/master/lists/directory-list-2.3-small.txt"

# Download the list
response = requests.get(LIST) # download as a big string
words = response.text.splitlines() # splits it into a list of lines

# Open the list, filter is and go through each word as path
for line in words:
    path = line.strip() # removes the whitespaces
  
    if not path or path.startswith("#"): # checks if the line is empty and skips the comments
        continue
        
    url = f"{TARGET.rstrip('/')}/{path}" # removes / if it exists
        
    try:
        response = requests.get(url, timeout=5)

        # if code is not 404 it prints    
        if response.status_code != 404:
            print(f"[{response.status_code}] {url}")
            break
        
    except requests.RequestException:
        pass