from fractions import Fraction

def add(f1, f2):
    return f1 + f2

def subtract(f1, f2):
    return f1 - f2

def multiply(f1, f2):
    return f1 * f2

def divide(f1, f2):
    return f1 / f2

m = {'a': add, 's': subtract, 'm' : multiply, 'd' : divide}
while True:
    try:
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
        op = input('Operation to perform - Add, Subtract, Divide, Multiply, or Exit to exit the program: ').lower()
        if op[0] == 'e':
            exit()
        if op not in ["add", "subtract", "divide", "multiply"]:
            raise ValueError("undefined operation.")
    except ValueError as e:
        print(e)
    else:
        print(m[op[0]](a, b))
