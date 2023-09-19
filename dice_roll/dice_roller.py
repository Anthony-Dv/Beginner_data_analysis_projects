# This program will display random dice rolls with the number of dice you specify, it can display dice vertically as well as horizontally.
import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice_num = int(input("How many dice you wish to roll?\n"))
dice = []

# generate random dice number within 1 - 6 range
for x in range(dice_num):
    dice.append(random.randint(1, 6))

# display dice horizontally

# for x in dice:
#    for y in dice_art.get(x):
#        print(y)

# display dice vertically
for i in range(5):
    for x in dice:
        print(dice_art.get(x)[i], end= " ")
    print()

# count the total dice rolled
total = 0
for x in dice:
    total += x

print(f"Your total dice roll is: {total}")


