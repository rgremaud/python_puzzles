# The Birthday Paradox, also called the Birthday Problem, 
# is the surprisingly high probability that two people will have the same birthday 
# even in a small group of people. In a group of 70 people, there’s a 99.9 percent 
# chance of two people having a matching birthday. But even in a group as small as 23 people, 
# there’s a 50 percent chance of a matching birthday. This program performs several probability 
# experiments to determine the percentages for groups of different sizes. We call these types of 
# experiments, in which we conduct multiple random trials to understand the likely outcomes, 
# Monte Carlo experiments.

import random

date_array = [["January", 31], ["February", 28], ["March", 31], ["April", 30], ["May", 31],
              ["June", 30], ["July", 31], ["August", 31], ["September", 30], ["October", 31]
              , ["November", 30], ["December", 31]]


def build_dates(quantity, date_array = date_array):
    """Build out an array with random Month, Days.  Max of 100."""
    random_dates = []
    i = 0
    if quantity > 100:
        print("Maximum amount of dates is 100.  Adjusting for 100.")
        build_dates(100)
    else: 
        while i <= quantity:
            random_number = random.randint(0, 11)
            month = date_array[random_number][0]
            total_days = date_array[random_number][1]
            random_day = random.randint(1, total_days)
            random_date = month + str(random_day)
            random_dates.append(random_date)
            i += 1
    
        return random_dates

def duplicate_check(array):
    """Check for duplicate amounts in a list"""
    if len(array) != len(set(array)):
        return True
    else:
        return False

def birthday_paradox(quantity_of_dates, number_of_simulations):
    """Crunch the numbers to check for duplicate bdays"""
    i = 0
    duplicates = 0
    while i <= number_of_simulations:
        bday_array = build_dates(quantity_of_dates, date_array = date_array)
        if duplicate_check(bday_array):
            duplicates += 1
        i += 1
    
    dupe_percentage = duplicates/number_of_simulations
    print(f"Number of dupes {duplicates}")
    print(f"The percentage of duplicates on the simulation are {dupe_percentage:2%}")
    

birthday_paradox(23, 100)

