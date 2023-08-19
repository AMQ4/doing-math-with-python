from fractions import Fraction

try:
    n = float(input("Enter a number:\n> "))
    if(not n.is_integer()):
        raise ValueError("The number is not an integer.")
except ValueError as e:
    print(e)
else:
    n = int(n)
    print(*("{0} ".format(n) for n in range(n, 21, 2)))
