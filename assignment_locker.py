#!/usr/bin/python3
# Author: Jimmy
# Editor: Melissa

antal=1000

# S = Stänga, O = öppna
skap = "O" * (antal + 1)

# Loopa igenom alla eleverna
for elevnr in range(1, antal+1):

    # Loopa igenom alla skåp
    for skapnr in range(0, antal + 1, elevnr):
        if skap[skapnr] == "S":
            action = "O"
        else:
            action = "S"
        skap = skap[:skapnr] + action + skap[skapnr+1:]

print(f"{skap[1:].count('O')} skåp är öppna")