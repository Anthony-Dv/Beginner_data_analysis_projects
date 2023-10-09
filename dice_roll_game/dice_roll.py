# This is dice rolling game for 2 players.
# When you roll the dice whatever number you get is added to your total score
# After each roll you can choose to roll again or "lock in" your total score
# If you roll number 1 you loose your chance to "lock in" your score and its other players turn
# Whoever rolls 100 in less tries wins

import random

first = input("Please enter the first player:\n") # get names of the players
second = input("Please enter second player:\n")

def roll_dice(first_player, second_player): # define the game funct
    first_total = 0 # create total score counters
    second_total = 0
    # if any players reached score 100 end the loop
    while first_total < 100 and second_total < 100:
        # define first player loop
        subscore_first = 0 # create subscore counter                     
        x = None # define x for while loop
        while x != 0:
            # if you roll number 1 its second players turn
            print(f"Its {first_player} turn!")
            roll = random.randint(1, 6)
            if roll == 1:                           
                print("Bad luck! You rolled 1")
                break
            # if you roll number other than 1 you can choose to keep rolling or locking in your score
            else:
                print("You rolled: " + str(roll))
                subscore_first += roll
                decision_1 = input("Do you want to roll again(type roll) or do you want to lock in your score(type lock)?\n")
                if decision_1 == "lock":
                    x = 0
                    first_total += subscore_first
        # define second player loop
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
    # determine who won
    if first_total > second_total:
        print("The winner is: " + first_player + " with score of: " + str(first_total))
    else:
        print("The winner is: " + second_player + " with score of: " + str(second_total))

roll_dice(first, second)



