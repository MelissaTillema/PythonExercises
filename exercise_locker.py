#!/bin/python3
# Author: Melissa

lockers = ["closed"] * 15

total = 15

for x in range(total):
    student = x + 1
    # Determine action based on student number
    if student%2 == 1:
        action = "close"
    else:
        action = "open"
    #print(f"Student {student} {action}s every {student}th locker")

    for locker in range(student - 1, total, student):
        lockers[locker] = action

#Collect open lockers
'''open_lockers = []
for i, state in enumerate(lockers): #enumerate loops through the list 
    if state == "open":
        open_lockers.append(i + 1) #add the locker number to the list
'''
open_lockers = 0
for state in lockers:
    if state == "open":
        open_lockers += 1


#print("Final open lockers:", open_lockers)
print("Total open lockers:", (open_lockers))




