"""
#2: Law of Large Numbers

According to the law of large numbers, the average value of results over
multiple trials approaches the expected value as the number of trials
increases. Your challenge in this task is to verify this law when rolling a
six-sided die for the following number of trials: 100, 1000, 10000, 100000,
and 500000. Here’s an expected sample run of your complete program:
"""

from random import randint

def roll_dice():
    """
    Simulate rolling a six-sided die.

    Returns:
        int: A random number between 1 and 6, representing the result of the die roll.
    """
    return randint(1, 6)

def expectation_of_a_dice_roll():
    """
    Calculate the expected value of a six-sided die roll.

    Returns:
        float: The expected value, which is the sum of all possible outcomes divided by 6.
    """
    return sum(range(1, 7)) / 6

print(f"Expected value: {expectation_of_a_dice_roll()}")

number_of_trials_to_check = [100, 1000, 10000, 100000, 500000]
trials = 0

for i in range(1, number_of_trials_to_check[-1] + 1):
    if i in number_of_trials_to_check:
        print(f"Trials: {i} Trial average {trials/i}")
    trials += roll_dice()
