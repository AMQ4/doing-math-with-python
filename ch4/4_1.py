"""
#1: Factor Finder
You learned about the factor() function, which prints the factors of an
expression. Now that you know how your program can handle expressions
input by a user, write a program that will ask the user to input an expres-
sion, calculate its factors, and print them. Your program should be able to
handle invalid input by making use of exception handling.

Usage:
1. Run the program.
2. Input an expression when prompted.
3. The program will calculate and print the factors of the expression.
"""

import sympy

# Get user input for the expression to factor
expr = input("Write your expression to factor it:\n> ")

try:
    # Attempt to parse the user input as a sympy expression
    expr = sympy.sympify(expr)
except sympy.SympifyError as e:
    # Handle invalid input by printing an error message
    print("Invalid input:", e)
else:
    # Calculate and print the factors of the expression
    print(expr.factor())

