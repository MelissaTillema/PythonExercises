#!/bin/python3
# Author: Melissa

import datetime

today = datetime.datetime.now()
x=today.strftime("%H:%M:%S") #time
y=today.strftime("%A") #day of the week

print(f"The time is {x} and today is {y}")