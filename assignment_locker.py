#!/usr/bin/python3

antal=10000

skap = "S" * (antal + 1)

# S = Stänga, O = öppna
action = "S"

# Loopa igenom alla eleverna
for elevnr in range(1, antal+1):

    # Loopa igenom alla skåp
    for skapnr in range(0, antal + 1, elevnr):
        skap = skap[:skapnr] + action + skap[skapnr+1:]

    # Ändra action
    action = "S" if action == "O" else "O"
print(f"{skap[1:].count('O')} skåp är öppna")