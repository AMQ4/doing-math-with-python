"""
#5: Estimating the Area of a Circle

1- write a program that will find the estimated
   area of a circle, given any radius, using this approach. The program should
   print the estimated area of the circle for three different values of the num-
   ber of darts: 1e3, 1e5, and 1e6.

2- write a program that will estimate the value of π assuming any 
   value for the radius.
"""

from random import uniform
from math import pi

def random_dart_throw(r):
    """
    Simulate a random dart throw within a circular dartboard with radius r 
    inscribed in a square with side 2r.

    Returns:
        float: The distance from the center of the square to where the dart lands.
    """
    x, y = uniform(0, r), uniform(0, r)
    distance = (x ** 2 + y ** 2) ** 0.5
    return distance

r = float(input("Radius:\n> "))

number_of_darts = [1_000, 100_000, 1_000_000]
number_of_darts_that_hits_the_circle = 0

for i in range(number_of_darts[-1]):
    if i+1 in number_of_darts:
        print(f"Area: {r ** 2 * pi}, Estimated ({i+1} darts):" 
              f"{4 * r**2 * (number_of_darts_that_hits_the_circle / (i+1))}, "
              f"Estimated value of PI: {4 * (number_of_darts_that_hits_the_circle / (i+1))}\n")
    if random_dart_throw(r) <= r:
        number_of_darts_that_hits_the_circle += 1
