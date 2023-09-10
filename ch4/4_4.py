"""
#4: Solving Single-Variable Inequalities

For this challenge, create a function, isolve(), that will take
any inequality, solve it, and then return the solution.
"""

from sympy import *

def isolve(inequality: str):
    """
    Solves a given inequality expression involving the variable 'x' and returns the solution.

    Args:
        inequality (str): A string representing the inequality expression with 'x' as the independent variable.

    Returns:
        None: If the input cannot be parsed or simplified.
        Solution: The solution to the input inequality.

    Note:
        This function simplifies the input inequality and determines whether it's polynomial,
        rational, or neither. Then, it calls the appropriate solver function to find the solution.
    """
    # Define a symbol 'x' to represent the independent variable in the inequality.
    x = Symbol('x')

    try:
        # Attempt to simplify the input inequality expression.
        inq_expr = simplify(inequality)
    except SympifyError as e:
        # If there's an error during simplification, print the error and return.
        print(e)
        return

    if inq_expr.lhs.is_polynomial():
        # If the left-hand side of the simplified inequality is a polynomial, call the polynomial inequality solver.
        print(inq_expr)
        pprint(poly_inq_solver(inq_expr))
    elif inq_expr.lhs.is_rational_function():
        # If the left-hand side of the simplified inequality is a rational function, call the rational inequality solver.
        print(inq_expr)
        pprint(rational_inq_solver(inq_expr))
    else:
        # If the inequality is neither polynomial nor rational, call the generic inequality solver.
        pprint(neither_polynomial_nor_rational_inq_solver(inq_expr))

def neither_polynomial_nor_rational_inq_solver(inequality):
    """
    Solves an inequality that is neither polynomial nor rational.

    Args:
        inequality: The inequality to be solved.

    Returns:
        Solution: The solution to the inequality.
    """
    return solve_univariate_inequality(inequality, x, relational=False)

def poly_inq_solver(inequality):
    """
    Solves a polynomial inequality.

    Args:
        inequality: The polynomial inequality to be solved.

    Returns:
        Solution: The solution to the polynomial inequality.
    """
    rhs = -1 * inequality.rhs
    lhs = inequality.lhs + rhs

    # Convert the left-hand side of the inequality to a polynomial.
    poly_inq = Poly(lhs, x)
    rel_op = inequality.rel_op

    # Solve the polynomial inequality and return the solution.
    return solve_poly_inequality(poly_inq, rel_op)

def rational_inq_solver(inequality):
    """
    Solves a rational inequality.

    Args:
        inequality: The rational inequality to be solved.

    Returns:
        Solution: The solution to the rational inequality.
    """
    rhs = -1 * inequality.rhs
    lhs = inequality.lhs + rhs

    # Separate the numerator and denominator of the left-hand side.
    numer, denom = lhs.as_numer_denom()

    # Convert the numerator and denominator to polynomials.
    numer = Poly(numer, x)
    denom = Poly(denom, x)

    rel_op = inequality.rel_op

    # Solve the rational inequality and return the solution.
    return solve_rational_inequalities([[((numer, denom), rel_op)]])

# Prompt the user to enter an inequality and call the isolve function.
isolve(input("Enter your inequality to solve, use `x` as the independent variable:\n> "))
