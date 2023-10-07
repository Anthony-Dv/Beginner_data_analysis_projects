# This is dice rolling game for 2 players.
# When you roll the dice whatever number you get is added to your total score
# After each roll you can choose to roll again or "lock in" your total score
# If you roll number 1 you loose your chance to "lock in" your score and its other players turn
# Whoever rolls 100 in less tries wins

import random

first = input("Please enter the first player:\n") # get names of the players
second = input("Please enter second player:\n")

def roll_dice(first_player, second_player): # define roll_dice funct
    first_total = 0
    second_total = 0
    while first_total < 10 and second_total < 10: # if one of the players hasnt won do the loop
        subscore_first = 0
        x = None
        while x != 0:
            print(f"Its {first_player} turn!")
            roll = random.randint(1, 6)
            if roll == 1:
                print("Bad luck! You rolled 1")
                break
            else:
                print("You rolled: " + str(roll))
            subscore_first += roll
            decision_1 = input("Do you want to roll again(type roll) or do you want to lock in your score(type lock)?\n")
            if decision_1 == "lock":
                x = 0
                first_total += subscore_first
            print(subscore_first)
            print(first_total)
        subscore_second = 0
        y = None
        while y != 0:
            print(f"Its {second_player} turn!")
            roll = random.randint(1, 6)
            if roll == 1:
                print("Bad luck! You rolled 1")
                break
            else:
                print("You rolled: " + str(roll))
            subscore_second += roll
            decision_1 = input("Do you want to roll again(type roll) or do you want to lock in your score(type lock)?\n")
            if decision_1 == "lock":
                y = 0
                second_total += subscore_second
            print(subscore_second)
            print(second_total)
    if first_total > second_total:
        print("The winner is: " + first_player + " with score of: " + str(first_total))
    else:
        print("The winner is: " + second_player + " with score of: " + str(second_total))

roll_dice(first, second)



