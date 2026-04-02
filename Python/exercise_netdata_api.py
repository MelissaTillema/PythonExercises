#!/bin/python3
# Author: Melissa

import requests

servers = [148, 149, 150]

# Loops through all my servers
for server in servers:
    url = f"http://10.0.5.{server}:19999/api/v1/info"
    while True:
        response = requests.get(url, timeout=5)
        data = response.json()  # Convert response to JSON

        # Extract the values you want
        os_name = data.get("os_name")
        os_version = data.get("os_version")
        mirrored_hosts = data.get("mirrored_hosts")

        # Print nicely
        print(f"Server 10.0.5.{server}:")
        print(f"  OS Name: {os_name}")
        print(f"  OS Version: {os_version}")
        print(f"  Mirrored Hosts: {mirrored_hosts[0]}")
        print(" ")
        break