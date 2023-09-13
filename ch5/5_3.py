"""
#3: How Many Tosses Before You Run Out of Money?

Let’s consider a simple game played with a fair coin toss. A player wins
$1 for heads and loses $1.50 for tails. The game is over when the player’s
balance reaches $0. Given a certain starting amount specified by the user
as input, your challenge is to write a program that simulates this game.
Assume there’s an unlimited cash reserve with the computer—your oppo-
nent here.
"""

from random import randint
from time import sleep

def toss_the_coin():
    """
    Simulate a coin toss.

    Returns:
        int: 1 for heads and 0 for tails.
    """
    return randint(0, 1) # 1 is head and 0 is tails

amount = int(input("Enter your starting amount: "))
counter = 0

while amount > 0:
    coin_face = toss_the_coin()
    amount += 1 if coin_face == 1 else -1.5
    print("{0}! Current amount: {1}".format("Tails" if coin_face == 0 else "Heads", amount))
    sleep(1.5)
    counter += 1

print("Game over :( Current amount: {0}. Coin tosses: {1}".format(amount, counter))
