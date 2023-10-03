# This program will calculate what is the probability of N same birthdays in determined size of population

import random

population_size = int(input("How big should be the size of the population?\n")) # get population size
number_of_same_birthdays = int(input("How many same birthdays should match?\n")) # get how many birdays should match
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


# generate random dates
def gen_dates(size):
    dates = []
    for y in range(size):
        m = random.choice(months) # choose random month
        d = str(random.randint(1, 30)) # choose random day 1 - 30 (I know this sollution gives me only 360 different dates, but its fine for the purpose of this project)
        dates.append(m + d)
    return dates # return list of random dates

# determine if randomly generated dates have specified number of dates matches
def get_match(y):
    date = gen_dates(population_size)
    matches = []
    for d in date:
        count = date.count(d)
        matches.append(count)
    if max(matches) >= y: # check if there are "X" same birthdays
        return True # if yes return True
    else:
        return False # if no return False

# how many simulations you want to run?
num_simulations = 10000

# get the probability of "X" same birthdays in "Y" size population
def get_probability():
    probab_true = 0
    probab_false = 0
    for x in range(num_simulations):
        match = get_match(number_of_same_birthdays)
        if match == True:
            probab_true += 1
        else:
            probab_false += 1
    print(f"Out of {str(num_simulations)} simulations {str(probab_true)} birthday mathced and in {str(probab_false)} birthday did not.")
    print(f"Probability of {str(number_of_same_birthdays)} birthdays matching in a population of {str(population_size)} is: {str((probab_true / num_simulations) * 100)}%.")


get_probability()










