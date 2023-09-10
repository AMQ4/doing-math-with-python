"""
#3: Summing a Series

Your challenge is to write a program that’s capable of finding the sum
of an arbitrary series when you supply the nth term of the series and the
number of terms in it.

Usage:
1. Enter the nth term of the series, using 'x' as the independent variable.
2. Enter the number of terms in the series.

The program will compute and print the sum of the series.
"""

import sympy

# Get user input for the nth term and the number of terms
nth_term = sympy.simplify(input("Enter the nth term, using 'x' as the independent variable:\n> "))
number_of_terms = int(input("Enter the number of terms:\n> "))

# Calculate the sum of the series
series = sympy.summation(nth_term, (sympy.Symbol('x'), 1, number_of_terms))

# Print the result
sympy.pprint(series)
